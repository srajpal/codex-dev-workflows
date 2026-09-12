"""Regression tests for validate_repo.py."""
from __future__ import annotations

import importlib.util
import json
import struct
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("validate_repo", Path(__file__).with_name("validate_repo.py"))
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def chunk(kind: bytes, payload: bytes) -> bytes:
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xffffffff)


class ValidatorTests(unittest.TestCase):
    def test_json_loader_rejects_non_object_and_null_at_call_site(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "marketplace.json"
            for payload in ("[]", "null"):
                with self.subTest(payload=payload):
                    path.write_text(payload, encoding="utf-8")
                    with patch.object(validator, "MARKETPLACE_PATH", path):
                        errors: list[str] = []
                        validator.validate_marketplace(errors)
                    self.assertIn("marketplace must contain a JSON object", errors)

    def test_semver_is_strict_and_allows_prerelease(self) -> None:
        self.assertIsNotNone(validator.SEMVER.fullmatch("1.2.3-beta.1+build.5"))
        for value in ("01.2.3", "1.02.3", "1.2", "v1.2.3", "1.2.3-"):
            with self.subTest(value=value): self.assertIsNone(validator.SEMVER.fullmatch(value))

    def test_frontmatter_supports_only_flat_unique_string_fields(self) -> None:
        self.assertEqual(validator.parse_frontmatter("---\r\nname: sample\r\ndescription: Useful\r\n---\r\nBody"), {"name": "sample", "description": "Useful"})
        self.assertIsNone(validator.parse_frontmatter("---\nname: one\nname: two\ndescription: Useful\n---"))
        self.assertIsNone(validator.parse_frontmatter("---\nname: sample\nmetadata:\n  key: value\n---"))

    def test_empty_skills_directory_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            plugin = Path(directory); (plugin / "skills").mkdir()
            with patch.object(validator, "PLUGIN_ROOT", plugin):
                errors: list[str] = []; validator.validate_skills(errors)
            self.assertIn("plugin skills directory must contain at least one skill", errors)

    def test_frontmatter_rejects_non_string_or_ambiguous_values(self) -> None:
        for value in ("null", "false", "123", "[]", "{}", "~", "# comment", "Task: nested", '"unfinished'):
            with self.subTest(value=value):
                self.assertIsNone(validator.parse_frontmatter(
                    f"---\nname: sample\ndescription: {value}\n---\nBody"
                ))

    def test_png_requires_basic_container_structure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "asset.png"; target.write_bytes(validator.PNG_SIGNATURE)
            self.assertFalse(validator.has_basic_png_structure(target))
            png = validator.PNG_SIGNATURE + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 6, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(b"\x00\xff\xff\xff\xff")) + chunk(b"IEND", b"")
            target.write_bytes(png)
            self.assertTrue(validator.has_basic_png_structure(target))
            target.write_bytes(png[:-12])
            self.assertFalse(validator.has_basic_png_structure(target))

    def test_marketplace_requires_local_source_and_category(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "marketplace.json"
            path.write_text(json.dumps({"name":"personal","interface":{"displayName":"Personal"},"plugins":[{"name":"codex-dev-workflows","source":{"path":"./plugins/codex-dev-workflows"},"policy":{"installation":"AVAILABLE","authentication":"ON_INSTALL"}}]}), encoding="utf-8")
            with patch.object(validator, "MARKETPLACE_PATH", path):
                errors: list[str] = []; validator.validate_marketplace(errors)
            self.assertTrue(any("source must be local" in error for error in errors)); self.assertTrue(any("category" in error for error in errors))

    def test_marketplace_policy_values_cannot_crash_validation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "marketplace.json"
            path.write_text(json.dumps({"name":"personal","interface":{"displayName":"Personal"},"plugins":[{"name":"codex-dev-workflows","source":{"source":"local","path":"./plugins/codex-dev-workflows"},"policy":{"installation":[],"authentication":{}},"category":"Productivity"}]}), encoding="utf-8")
            with patch.object(validator, "MARKETPLACE_PATH", path):
                errors: list[str] = []
                validator.validate_marketplace(errors)
            self.assertIn("marketplace installation policy is invalid", errors)
            self.assertIn("marketplace authentication policy is invalid", errors)

    def test_malformed_https_url_is_rejected_without_crash(self) -> None:
        self.assertFalse(validator.https_url("https://[invalid"))

    def test_asset_paths_reject_traversal_and_wrong_prefix(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(validator, "PLUGIN_ROOT", root):
                self.assertEqual(validator.resolve_asset("./assets/icon.png"), root / "assets" / "icon.png")
                self.assertIsNone(validator.resolve_asset("assets/../secret"))
                self.assertIsNone(validator.resolve_asset("elsewhere/icon.png"))
                self.assertEqual(validator.resolve_asset("assets/icon.png"), root / "assets" / "icon.png")

    def test_packaged_license_must_match_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            plugin = root / "plugin"
            plugin.mkdir()
            (root / "LICENSE").write_text("root", encoding="utf-8")
            (plugin / "LICENSE").write_text("different", encoding="utf-8")
            with patch.object(validator, "ROOT", root), patch.object(validator, "PLUGIN_ROOT", plugin):
                errors: list[str] = []
                validator.validate_license(errors)
            self.assertIn("plugins/codex-dev-workflows/LICENSE must match root LICENSE", errors)

    def test_missing_document_is_reported_without_crash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); (root / "README.md").write_text("ok", encoding="utf-8"); (root / "CHANGELOG.md").write_text("ok", encoding="utf-8")
            with patch.object(validator, "ROOT", root):
                errors: list[str] = []; validator.validate_no_machine_paths(errors)
            self.assertTrue(any("SECURITY.md" in error for error in errors))


if __name__ == "__main__": unittest.main()
