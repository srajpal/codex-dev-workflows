<div align="center">
  <img src="plugins/codex-dev-workflows/assets/logo.png" alt="Codex Dev Workflows icon" width="160" />
  <h1>Codex Dev Workflows</h1>
  <p><strong>Reusable development workflows for Codex.</strong><br />Plan clearly. Test deliberately. Resume safely.</p>
  <p>
    <a href="https://github.com/srajpal/codex-dev-workflows"><img src="https://img.shields.io/badge/GitHub-open--source-181717?logo=github" alt="GitHub repository" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0ea5e9.svg" alt="MIT license" /></a>
    <a href="https://learn.chatgpt.com/docs/plugins"><img src="https://img.shields.io/badge/Codex-plugin-0f766e.svg" alt="Codex plugin" /></a>
  </p>
</div>

An open-source, skills-only plugin that turns a practical development prompt library into reusable workflows for Codex. It helps with project planning, agent instructions, feature work and testing, game QA, debugging, code review, release readiness, and session handoffs. Shared references add focused guidance for Flutter, JavaScript/TypeScript, Python, and Laravel/PHP.

> This project does not add a custom pinned prompt sidebar. It uses the supported Codex skill and plugin format available today. See [the compatibility notes](docs/CODEX-COMPATIBILITY.md) and [roadmap](ROADMAP.md).

## What is included

| Skill | Use it when you need to… |
| --- | --- |
| `$new-project` | turn an idea into a scoped, buildable project plan |
| `$create-agent-instructions` | create concise repository instructions and documentation routing |
| `$feature-development` | implement a focused feature with appropriate verification |
| `$feature-testing` | test a just-completed feature, including edge cases and regressions |
| `$game-qa` | perform a broad gameplay and engineering QA pass |
| `$bug-investigation` | reproduce, isolate, fix, and verify a defect |
| `$code-review` | review a change set for correctness, risk, and missing tests |
| `$pre-release-review` | assess release readiness without making an unsupported release claim |
| `$session-handoff` | produce a precise handoff for the next working session |
| `$resume-interrupted-task` | safely recover context and continue interrupted work |
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

## Install and use

Codex plugins are supported in the ChatGPT desktop app and Codex CLI; the Codex IDE extension does not support plugins. This repository is deliberately arranged as a repository-local marketplace, which is useful for testing and sharing once the project is hosted.

1. Clone or download this repository.
2. Add the repository marketplace using the plugin-management flow available in your Codex surface, pointing it at the repository root that contains `.agents/plugins/marketplace.json`.
3. Install `codex-dev-workflows` from that marketplace.
4. Start a **new** Codex session after installation.
5. Type `$` and select a workflow, for example `$feature-testing`, then provide the feature context.

In Codex CLI, use `/plugins` to browse configured marketplaces. After installation, start a new session before using the bundled skills. The exact commands and UI can evolve; the canonical plugin builder docs are linked below.

### Use a workflow

```text
$feature-development

Implement [feature]. The outcome is [behavior].
Constraints: [compatibility, design, performance, non-goals].
Read the relevant project instructions and documentation first.
```

More ready-to-edit examples are in [examples](examples/README.md).

### Resume interrupted work

```text
$resume-interrupted-task

Continue the interrupted work in this repository. The last known goal was [goal].
The interruption happened after [last known step]. Check the working tree and
existing notes first; preserve valid changes and report uncertainty explicitly.
```

### Use platform guidance

Each workflow tells Codex to load the relevant platform file when it applies. You can also invoke `$platform-guidance` directly. The guidance does not invent project commands: it tells the agent to inspect the repository's documented tooling and configuration first.

## Development and validation

Validate the plugin after changing the manifest or any skill:

```powershell
python C:\Users\<you>\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py .\plugins\codex-dev-workflows
```

Then test in a new Codex session using both an explicit `$skill-name` request and a natural-language request that should plausibly match the skill description. See [CONTRIBUTING.md](CONTRIBUTING.md) for authoring standards.

## What works now vs. later

- **Now:** installable skills, explicit `$` invocation, automatic skill matching, and a repository-local marketplace package.
- **Not provided:** custom persistent sidebar, pinned prompt buttons, or a one-click prompt-template panel. No supported extension point is assumed for those features.
- **Later:** see [ROADMAP.md](ROADMAP.md).

## License

The project is shared under the [MIT License](LICENSE), a permissive license that lets developers copy, adapt, and redistribute the workflows with attribution. The plugin manifest also declares `MIT` and links to this repository so marketplace metadata is complete.

## Documentation sources

The structure and supported-surface claims were checked against current official OpenAI documentation: [Build plugins](https://learn.chatgpt.com/docs/build-plugins), [Build skills](https://learn.chatgpt.com/docs/build-skills), and [Plugins](https://learn.chatgpt.com/docs/plugins).

## Contributing and security

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a workflow, and use [SECURITY.md](SECURITY.md) for responsible vulnerability reporting.
