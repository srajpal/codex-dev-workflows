# Contributing

Contributions to the workflows, examples, and documentation are welcome.

Before editing a skill, read [the architecture notes](docs/ARCHITECTURE.md). Root documentation and `scripts/` support repository maintenance; installed skill content lives under `plugins/codex-dev-workflows/`.

## Set up and validate

1. Fork or clone the repository.
2. Make a focused change in the relevant skill or documentation file.
3. From the repository root, run:

   ```powershell
   python scripts/validate_repo.py
   python -m unittest discover -s scripts -p "test_*.py"
   ```

4. If behavior changed, install the local plugin and try the workflow in a new Codex session.

## Before opening a change

1. Check the [roadmap](ROADMAP.md) and existing [issues](https://github.com/srajpal/codex-dev-workflows/issues) for related work.
2. Keep each skill focused on one recognisable job. A description should say when it applies, not merely that it is "helpful."
3. Prefer instructions that are portable across coding agents unless Codex behavior materially improves the workflow.
4. Do not assume tools, frameworks, project layouts, commands, or permissions that the target repository has not established.

## Skill conventions

- Every skill lives in `plugins/codex-dev-workflows/skills/<name>/SKILL.md`.
- Use lower-case kebab-case for directory and metadata names.
- Keep YAML front matter limited to a clear `name` and a specific `description`. The dependency-free checker supports plain, single-line strings only; it is not a general YAML parser. Extend validation deliberately if the repository needs more YAML features.
- State expected inputs, a repeatable process, scope boundaries, and final report contents.
- Reference platform guidance only when the project uses that platform.
- Do not direct an agent to bypass approvals, alter unrelated work, expose secrets, or claim success without verification.

## Testing a contribution

Run both repository checks shown above. Then install or reinstall from the local marketplace and test the changed skill in a new Codex session with a representative request. Verify an explicit `$skill-name` invocation and, when the description should trigger automatically, a natural-language request.

In the pull request, record the prompt you used, what happened, and any checks you could not run. Do not include private repository content, credentials, or sensitive logs.

## Pull requests

Explain the user problem, the workflow change, any compatibility implications, and the manual test prompt/results. Small, focused pull requests are easiest to review.

By contributing, you agree that your contribution is licensed under this repository's MIT License.

## Host validators on Windows

The host's plugin and skill validators also need PyYAML. Keep this optional dependency in a local environment:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install PyYAML==6.0.3
.\.venv\Scripts\python.exe "$env:USERPROFILE\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" plugins/codex-dev-workflows
Get-ChildItem plugins/codex-dev-workflows/skills -Directory | ForEach-Object {
    & .\.venv\Scripts\python.exe "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" $_.FullName
    if ($LASTEXITCODE -ne 0) { throw "Skill validation failed: $($_.Name)" }
}
```

These paths assume the host's system skills are installed under your user profile. Use their actual location if different. No environment activation is needed. The `.venv/` directory is ignored by Git and is not part of the plugin. Repository CI remains dependency-free.
