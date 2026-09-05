"""Run dependency-free checks for the Codex Dev Workflows repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "codex-dev-workflows"
MANIFEST_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
FRONTMATTER_FIELD = re.compile(r"^(name|description):\s*(.+?)\s*$", re.MULTILINE)


def load_json(path: Path, errors: list[str]) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing JSON file: {path.relative_to(ROOT)}")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    return None


def validate_manifest(errors: list[str]) -> None:
    manifest = load_json(MANIFEST_PATH, errors)
    if not isinstance(manifest, dict):
        return
    if manifest.get("name") != PLUGIN_ROOT.name:
        errors.append("plugin manifest name must match its directory")
    if not re.fullmatch(r"(?:0|[1-9]\d*)\.\d+\.\d+", str(manifest.get("version", ""))):
        errors.append("plugin manifest version must be semantic versioning")
    if not isinstance(manifest.get("description"), str) or not manifest["description"].strip():
        errors.append("plugin manifest description must be non-empty")
    if manifest.get("skills") not in ("./skills", "./skills/"):
        errors.append("plugin manifest skills path must be ./skills/")
    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        errors.append("plugin manifest interface must be an object")
    else:
        expected_urls = {
            "websiteURL": "https://github.com/srajpal/codex-dev-workflows",
            "privacyPolicyURL": "https://github.com/srajpal/codex-dev-workflows/blob/master/PRIVACY.md",
            "termsOfServiceURL": "https://github.com/srajpal/codex-dev-workflows/blob/master/TERMS.md",
        }
        for field, expected in expected_urls.items():
            if interface.get(field) != expected:
                errors.append(f"plugin interface {field} must point to its public repository page")


def validate_marketplace(errors: list[str]) -> None:
    marketplace = load_json(MARKETPLACE_PATH, errors)
    if not isinstance(marketplace, dict):
        return
    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        errors.append("marketplace plugins must be an array")
        return
    matches = [entry for entry in entries if isinstance(entry, dict) and entry.get("name") == PLUGIN_ROOT.name]
    if len(matches) != 1:
        errors.append("marketplace must contain exactly one codex-dev-workflows entry")
        return
    entry = matches[0]
    source = entry.get("source")
    if not isinstance(source, dict) or source.get("path") != "./plugins/codex-dev-workflows":
        errors.append("marketplace source path must point to ./plugins/codex-dev-workflows")
    policy = entry.get("policy")
    if not isinstance(policy, dict) or policy.get("installation") not in {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"}:
        errors.append("marketplace installation policy is invalid")
    if not isinstance(policy, dict) or policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
        errors.append("marketplace authentication policy is invalid")


def validate_skills(errors: list[str]) -> None:
    skills_root = PLUGIN_ROOT / "skills"
    if not skills_root.is_dir():
        errors.append("missing plugins/codex-dev-workflows/skills directory")
        return
    for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"{skill_dir.relative_to(ROOT)} is missing SKILL.md")
            continue
        contents = skill_path.read_text(encoding="utf-8")
        if "[TODO:" in contents:
            errors.append(f"{skill_path.relative_to(ROOT)} contains a TODO marker")
        if not contents.startswith("---\n"):
            errors.append(f"{skill_path.relative_to(ROOT)} is missing YAML front matter")
            continue
        end = contents.find("\n---", 4)
        if end == -1:
            errors.append(f"{skill_path.relative_to(ROOT)} has unclosed YAML front matter")
            continue
        fields = dict(FRONTMATTER_FIELD.findall(contents[4:end]))
        if fields.get("name") != skill_dir.name:
            errors.append(f"{skill_path.relative_to(ROOT)} name must match its directory")
        if not fields.get("description", "").strip():
            errors.append(f"{skill_path.relative_to(ROOT)} description must be non-empty")


def validate_assets(errors: list[str]) -> None:
    assets_root = PLUGIN_ROOT / "assets"
    for asset_name in ("icon.png", "logo.png"):
        path = assets_root / asset_name
        try:
            if path.read_bytes()[:8] != PNG_SIGNATURE:
                errors.append(f"{path.relative_to(ROOT)} is not a valid PNG signature")
        except FileNotFoundError:
            errors.append(f"missing asset: {path.relative_to(ROOT)}")


def validate_no_machine_paths(errors: list[str]) -> None:
    for path in (ROOT / "README.md", ROOT / "CHANGELOG.md", ROOT / "SECURITY.md"):
        contents = path.read_text(encoding="utf-8")
        if re.search(r"C:\\\\Users\\\\srajp|/Users/srajp|Dropbox", contents, re.IGNORECASE):
            errors.append(f"{path.relative_to(ROOT)} contains a local or private path")


def main() -> int:
    errors: list[str] = []
    validate_manifest(errors)
    validate_marketplace(errors)
    validate_skills(errors)
    validate_assets(errors)
    validate_no_machine_paths(errors)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
