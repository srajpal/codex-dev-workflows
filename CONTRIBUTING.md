# Contributing

Thanks for helping make development workflows more reliable and reusable.

## Before opening a change

1. Check the roadmap and existing issues once the repository is published.
2. Keep each skill focused on one recognisable job. A description should say when it applies, not merely that it is "helpful."
3. Prefer instructions that are portable across coding agents unless Codex behavior materially improves the workflow.
4. Do not assume tools, frameworks, project layouts, commands, or permissions that the target repository has not established.

## Skill conventions

- Every skill lives in `plugins/codex-dev-workflows/skills/<name>/SKILL.md`.
- Use lower-case kebab-case for directory and metadata names.
- Keep YAML front matter limited to a clear `name` and a specific `description`.
- State expected inputs, a repeatable process, scope boundaries, and final report contents.
- Reference platform guidance only when the project uses that platform.
- Do not direct an agent to bypass approvals, alter unrelated work, expose secrets, or claim success without verification.

## Testing a contribution

Run the repository validation described in the README. Then install or re-install from a local marketplace and test the changed skill in a new Codex session with a representative request. Verify both an explicit `$skill-name` invocation and a natural-language request where appropriate.

## Pull requests

Explain the user problem, the workflow change, any compatibility implications, and the manual test prompt/results. Small, focused pull requests are easiest to review.

By contributing, you agree that your contribution is licensed under this repository's MIT License.

