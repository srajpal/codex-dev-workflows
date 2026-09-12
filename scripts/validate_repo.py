"""Run dependency-free checks for this skills-only Codex plugin repository."""
from __future__ import annotations

import json
import re
import struct
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "codex-dev-workflows"
MANIFEST_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
INVALID_JSON = object()
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$")
IDENTIFIER = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MACHINE_PATH = re.compile(r"(?:[A-Za-z]:\\Users\\[^\\\s]+|/Users/[^/\s]+|/home/[^/\s]+)")


def relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def load_json(path: Path, errors: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing JSON file: {relative(path)}")
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON in {relative(path)}: {exc}")
    return INVALID_JSON


def non_empty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = urlparse(value)
    except ValueError:
        return False
    return parsed.scheme == "https" and bool(parsed.netloc) and parsed.username is None


def resolve_asset(raw: object) -> Path | None:
    if not non_empty(raw):
        return None
    candidate = PurePosixPath(str(raw).replace("\\", "/"))
    if candidate.is_absolute() or any(part in {"", ".", ".."} for part in candidate.parts):
        return None
    if not candidate.parts or candidate.parts[0] != "assets":
        return None
    resolved = (PLUGIN_ROOT / candidate.as_posix()).resolve()
    try:
        resolved.relative_to(PLUGIN_ROOT.resolve())
    except ValueError:
        return None
    return resolved


def validate_manifest(errors: list[str]) -> None:
    manifest = load_json(MANIFEST_PATH, errors)
    if manifest is INVALID_JSON:
        return
    if not isinstance(manifest, dict):
        errors.append("plugin manifest must contain a JSON object")
        return
    allowed = {"name", "version", "description", "author", "homepage", "repository", "license", "keywords", "skills", "interface"}
    for field in sorted(set(manifest) - allowed):
        errors.append(f"plugin manifest contains unsupported field: {field}")
    name = manifest.get("name")
    if name != PLUGIN_ROOT.name or not isinstance(name, str) or IDENTIFIER.fullmatch(name) is None:
        errors.append("plugin manifest name must be kebab-case and match its directory")
    version = manifest.get("version")
    if not isinstance(version, str) or SEMVER.fullmatch(version) is None:
        errors.append("plugin manifest version must be strict semantic versioning")
    for field in ("description", "license"):
        if not non_empty(manifest.get(field)):
            errors.append(f"plugin manifest {field} must be non-empty")
    for field in ("homepage", "repository"):
        if not https_url(manifest.get(field)):
            errors.append(f"plugin manifest {field} must be an absolute HTTPS URL")
    author = manifest.get("author")
    if not isinstance(author, dict) or not non_empty(author.get("name")):
        errors.append("plugin manifest author.name must be non-empty")
    keywords = manifest.get("keywords")
    if not isinstance(keywords, list) or not keywords or not all(non_empty(item) for item in keywords):
        errors.append("plugin manifest keywords must be a non-empty array of strings")
    if manifest.get("skills") not in ("./skills", "./skills/"):
        errors.append("plugin manifest skills path must be ./skills/")
    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        errors.append("plugin manifest interface must be an object")
        return
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if not non_empty(interface.get(field)):
            errors.append(f"plugin interface {field} must be non-empty")
    capabilities = interface.get("capabilities")
    if not isinstance(capabilities, list) or not all(non_empty(item) for item in capabilities):
        errors.append("plugin interface capabilities must be an array of strings")
    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or not prompts or not all(non_empty(item) for item in prompts):
        errors.append("plugin interface defaultPrompt must be a non-empty array of strings")
    expected_urls = {
        "websiteURL": "https://github.com/srajpal/codex-dev-workflows",
        "privacyPolicyURL": "https://github.com/srajpal/codex-dev-workflows/blob/master/PRIVACY.md",
        "termsOfServiceURL": "https://github.com/srajpal/codex-dev-workflows/blob/master/TERMS.md",
    }
    for field, expected in expected_urls.items():
        if interface.get(field) != expected:
            errors.append(f"plugin interface {field} must point to its public repository page")
    for field in ("composerIcon", "logo"):
        path = resolve_asset(interface.get(field))
        if path is None or not path.is_file():
            errors.append(f"plugin interface {field} must point to a file under assets/")


def validate_marketplace(errors: list[str]) -> None:
    marketplace = load_json(MARKETPLACE_PATH, errors)
    if marketplace is INVALID_JSON:
        return
    if not isinstance(marketplace, dict):
        errors.append("marketplace must contain a JSON object")
        return
    if not non_empty(marketplace.get("name")):
        errors.append("marketplace name must be non-empty")
    interface = marketplace.get("interface")
    if not isinstance(interface, dict) or not non_empty(interface.get("displayName")):
        errors.append("marketplace interface.displayName must be non-empty")
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
    if not isinstance(source, dict) or source.get("source") != "local" or source.get("path") != "./plugins/codex-dev-workflows":
        errors.append("marketplace source must be local and point to ./plugins/codex-dev-workflows")
    policy = entry.get("policy")
    installation = policy.get("installation") if isinstance(policy, dict) else None
    if not isinstance(installation, str) or installation not in {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"}:
        errors.append("marketplace installation policy is invalid")
    authentication = policy.get("authentication") if isinstance(policy, dict) else None
    if not isinstance(authentication, str) or authentication not in {"ON_INSTALL", "ON_USE"}:
        errors.append("marketplace authentication policy is invalid")
    if not non_empty(entry.get("category")):
        errors.append("marketplace category must be non-empty")


def parse_frontmatter(contents: str) -> dict[str, str] | None:
    """Parse the supported subset: unique top-level keys with plain string values."""
    lines = contents.splitlines()
    if not lines or lines[0] != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.fullmatch(r"([a-z][a-z0-9-]*):[ \t]+([^\[\]{}|>&*!]+?)\s*", line)
        if match is None or match.group(1) in fields:
            return None
        value = match.group(2)
        if value.startswith(("'", '"')) or value.endswith(("'", '"')):
            return None
        # This repository uses plain prose, not YAML scalars or nested mappings.
        if not re.match(r"[A-Za-z]", value) or value.lower() in {
            "null", "true", "false", "yes", "no", "on", "off",
        } or re.search(r":(?:\s|$)|(?:^|\s)#", value):
            return None
        fields[match.group(1)] = value
    return fields


def validate_skills(errors: list[str]) -> None:
    skills_root = PLUGIN_ROOT / "skills"
    if not skills_root.is_dir():
        errors.append("missing plugins/codex-dev-workflows/skills directory")
        return
    directories = sorted(path for path in skills_root.iterdir() if path.is_dir() and not path.name.startswith("."))
    if not directories:
        errors.append("plugin skills directory must contain at least one skill")
        return
    seen: set[str] = set()
    for directory in directories:
        skill_path = directory / "SKILL.md"
        try:
            contents = skill_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"{relative(directory)} is missing or has unreadable SKILL.md")
            continue
        fields = parse_frontmatter(contents)
        if fields is None:
            errors.append(f"{relative(skill_path)} has invalid flat string YAML front matter")
            continue
        unexpected = set(fields) - {"name", "description"}
        if unexpected:
            errors.append(f"{relative(skill_path)} has unsupported front matter fields: {', '.join(sorted(unexpected))}")
        name = fields.get("name", "")
        if name != directory.name or IDENTIFIER.fullmatch(name) is None:
            errors.append(f"{relative(skill_path)} name must be kebab-case and match its directory")
        if name in seen:
            errors.append(f"duplicate skill name: {name}")
        seen.add(name)
        if not fields.get("description", "").strip():
            errors.append(f"{relative(skill_path)} description must be non-empty")
        if "[TODO:" in contents:
            errors.append(f"{relative(skill_path)} contains a TODO marker")


def has_basic_png_structure(path: Path) -> bool:
    """Check signature, the required first IHDR chunk, and terminal IEND marker."""
    try:
        data = path.read_bytes()
    except OSError:
        return False
    if len(data) < 45 or not data.startswith(PNG_SIGNATURE):
        return False
    return struct.unpack(">I", data[8:12])[0] == 13 and data[12:16] == b"IHDR" and data[-12:-4] == b"\0\0\0\0IEND"


def validate_assets(errors: list[str]) -> None:
    for name in ("icon.png", "logo.png"):
        path = PLUGIN_ROOT / "assets" / name
        if not has_basic_png_structure(path):
            errors.append(f"{relative(path)} is missing or lacks basic PNG structure")


def validate_license(errors: list[str]) -> None:
    root_license = ROOT / "LICENSE"
    plugin_license = PLUGIN_ROOT / "LICENSE"
    try:
        if root_license.read_bytes() != plugin_license.read_bytes():
            errors.append("plugins/codex-dev-workflows/LICENSE must match root LICENSE")
    except OSError:
        errors.append("root and packaged LICENSE files must both be readable")


def validate_no_machine_paths(errors: list[str]) -> None:
    for path in (ROOT / "README.md", ROOT / "CHANGELOG.md", ROOT / "SECURITY.md"):
        try:
            contents = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"missing or unreadable documentation file: {relative(path)}")
            continue
        if MACHINE_PATH.search(contents) or re.search(r"\bDropbox\b", contents, re.IGNORECASE):
            errors.append(f"{relative(path)} contains a local or private path")


def validate_repository() -> list[str]:
    errors: list[str] = []
    validate_manifest(errors)
    validate_marketplace(errors)
    validate_skills(errors)
    validate_assets(errors)
    validate_license(errors)
    validate_no_machine_paths(errors)
    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
