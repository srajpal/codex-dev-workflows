<div align="center">
  <img src="plugins/codex-dev-workflows/assets/logo.png" alt="Codex Dev Workflows icon" width="160" />
  <h1>Codex Dev Workflows</h1>
  <p><strong>Reusable development workflows for Codex.</strong></p>
  <p>
    <a href="https://github.com/srajpal/codex-dev-workflows"><img src="https://img.shields.io/badge/GitHub-open--source-181717?logo=github" alt="GitHub repository" /></a>
    <a href="https://github.com/srajpal/codex-dev-workflows/actions/workflows/validate.yml"><img src="https://github.com/srajpal/codex-dev-workflows/actions/workflows/validate.yml/badge.svg" alt="Repository validation" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0ea5e9.svg" alt="MIT license" /></a>
    <a href="https://learn.chatgpt.com/docs/plugins"><img src="https://img.shields.io/badge/Codex-plugin-0f766e.svg" alt="Codex plugin" /></a>
    <a href="https://chatgpt.com/plugins/plugins_6a9b7d9f2fa0819194b71d627744d569"><img src="https://img.shields.io/badge/OpenAI-published%20plugin-10a37f.svg" alt="Published OpenAI plugin" /></a>
  </p>
</div>

An open-source, skills-only plugin for common software-development tasks: planning, agent instructions, orchestration, feature work, testing, QA, debugging, code review, release checks, and handoffs. It also includes focused guidance for Flutter, JavaScript/TypeScript, Python, and Laravel/PHP.

The project has a [published plugin listing](https://chatgpt.com/plugins/plugins_6a9b7d9f2fa0819194b71d627744d569). Availability can vary by Codex surface and account.

## What is included

| Skill | Use it when you need to… |
| --- | --- |
| `$new-project` | turn an idea into a scoped, buildable project plan |
| `$create-agent-instructions` | create concise repository instructions and documentation routing |
| `$feature-development` | implement a focused feature with appropriate verification |
| `$feature-testing` | test a just-completed feature, including edge cases and regressions |
| `$comprehensive-qa` | perform a broad QA pass across software, apps, services, and games |
| `$bug-investigation` | reproduce, isolate, fix, and verify a defect |
| `$code-review` | review a change set for correctness, risk, and missing tests |
| `$pre-release-review` | assess release readiness without making an unsupported release claim |
| `$session-handoff` | produce a precise handoff for the next working session |
| `$resume-interrupted-task` | safely recover context and continue interrupted work |
| `$orchestrate-work` | coordinate complex work across parallel worker agents |
| `$platform-guidance` | load implementation/testing considerations for a supported stack |

## Repository layout

```text
.
├── .agents/plugins/marketplace.json     # local/repository marketplace entry
├── plugins/codex-dev-workflows/
│   ├── .codex-plugin/plugin.json        # plugin manifest
│   ├── assets/                          # icon and logo
│   ├── skills/                          # installable workflows
│   └── shared/platforms/                # Flutter, JS/TS, Python, Laravel/PHP
├── examples/
└── docs/
```

## Quick start

Plugin support and installation steps can change. Check the [official plugin documentation](https://learn.chatgpt.com/docs/plugins) for the current supported surfaces and controls.

1. Open the [published plugin listing](https://chatgpt.com/plugins/plugins_6a9b7d9f2fa0819194b71d627744d569) and install it if your Codex surface offers that option.
2. Start a new Codex session so it can load the installed skills.
3. Type `$`, select a workflow such as `$feature-testing`, and describe the task.

To test this repository locally, clone or download it, then add its root as a local marketplace. The marketplace file at `.agents/plugins/marketplace.json` points to `plugins/codex-dev-workflows`. Follow the current [plugin-building documentation](https://learn.chatgpt.com/docs/build-plugins) for the exact UI or command for your Codex version.

If a skill does not appear after installation, start a new session first. See [Troubleshooting](#troubleshooting) for more checks.

### Use a workflow

```text
$feature-development

Implement [feature]. The outcome is [behavior].
Constraints: [compatibility, design, performance, non-goals].
Read the relevant project instructions and documentation first.
```

### Orchestrate complex work

```text
$orchestrate-work

Coordinate these updates as the primary agent. Divide only genuinely independent
workstreams, prefer a capable lower-cost worker with low reasoning for bounded
tasks, prevent overlapping edits, integrate every result, and run final validation.
Complete tightly coupled work directly.
```

More ready-to-edit examples are in [examples](examples/README.md).

### Resume interrupted work

```text
$resume-interrupted-task

Continue the interrupted work in this repository. The last known goal was [goal].
The interruption happened after [last known step]. Check the working tree and
existing notes first; preserve valid changes and report uncertainty explicitly.
```

### Create a session handoff

```text
$session-handoff

Prepare a handoff for the next session. Inspect the current working tree, recent
changes, tests, decisions, risks, and blockers. Separate verified facts from
assumptions and give the next session exact first steps.
```

### Run a comprehensive QA pass

```text
$comprehensive-qa

Test the current product against its documented requirements and critical user
journeys. Discover the repository's real validation commands, exercise edge
cases and recovery paths, and report evidence, defects, risks, and remaining
manual checks. If this is a game, include rules, scoring, progression, and
save/restore behavior.
```

### Use platform guidance

Workflows that need stack-specific guidance load the relevant platform file when it applies. You can also invoke `$platform-guidance` directly. The guidance tells the agent to inspect the repository's documented tooling and configuration before choosing commands.

## Development and validation

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing a workflow. The [architecture notes](docs/ARCHITECTURE.md) explain which files are installed with the plugin and which exist only to maintain this repository.

Run the repository's dependency-free validation after changing the manifest, marketplace entry, assets, or any skill:

```powershell
python scripts/validate_repo.py
python -m unittest discover -s scripts -p "test_*.py"
```

Every push and pull request also runs the repository's dependency-free metadata check through [GitHub Actions](https://github.com/srajpal/codex-dev-workflows/actions/workflows/validate.yml). These checks cover the repository's metadata conventions, skill files, marketplace and asset paths, basic PNG structure, packaged license, and common local paths in selected public docs. They also run validator regression tests. They do not validate the full host schema, prove prompt safety, or run a user's application tests.

Then test changed skills in a new Codex session using both an explicit `$skill-name` request and a natural-language request that should plausibly match the skill description. Record that as a live plugin test only if you actually installed the changed package and exercised it in a supported host.

## Troubleshooting

- **The skill is missing:** confirm that `codex-dev-workflows` is installed, then start a new session. Existing sessions may keep their original skill inventory.
- **Local installation fails:** confirm that you selected the repository root, which contains `.agents/plugins/marketplace.json`, rather than the plugin subdirectory.
- **Validation fails:** run `python scripts/validate_repo.py` from the repository root and fix the paths or metadata named in the output.
- **A workflow uses the wrong project command:** point it to the repository's own instructions and configuration. These skills are designed to discover project commands instead of assuming them.
- **Still stuck:** follow [SUPPORT.md](SUPPORT.md) and include a minimal reproduction without private code or credentials.

## Package scope

- **Plugin:** twelve skill definitions, shared platform guidance, display assets, and the MIT License. Repository validation and the local marketplace entry are maintainer resources.
- **Not included:** a custom sidebar, pinned prompt buttons, or a prompt-template panel.
- **Planned ideas:** see [ROADMAP.md](ROADMAP.md).

## License

The project is shared under the [MIT License](LICENSE), a permissive license that lets developers copy, adapt, and redistribute the workflows while retaining the copyright and permission notices required by the license. The plugin manifest also declares `MIT` and links to this repository so marketplace metadata is complete.

## Official documentation

For current plugin and skill behavior, see OpenAI's [Build plugins](https://learn.chatgpt.com/docs/build-plugins), [Build skills](https://learn.chatgpt.com/docs/build-skills), and [Plugins](https://learn.chatgpt.com/docs/plugins) documentation.

## Policies, support, and security

Read the [privacy policy](PRIVACY.md), [terms of use](TERMS.md), and [support guide](SUPPORT.md). Please read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a workflow, and use [SECURITY.md](SECURITY.md) for responsible vulnerability reporting.
