# Codex Dev Workflows

Keep repeating the same instructions to Codex: check the edge cases, review before editing, preserve unfinished work? This plugin packages those development routines into reusable skills. Choose a workflow and describe the task, without rebuilding your checklist each session.

For developers using Codex to test features, review changes, and resume interrupted work. Open source under the MIT License.

**[Install from the OpenAI plugin directory](https://chatgpt.com/plugins/plugins_6a9b7d9f2fa0819194b71d627744d569)** · [Try the review demo](examples/review-demo.md) · [All examples](examples/README.md)

## Get started

1. Open the installation link above and install the plugin if your Codex surface offers that option.
2. Start a new session in the project you want to work on.
3. Type `$`, choose a skill, and describe the task. Try one of the examples below.

Availability and controls can vary by account and surface. See the [official plugin documentation](https://learn.chatgpt.com/docs/plugins) or [troubleshooting](#troubleshooting) if a skill is missing.

## Three useful starting points

### Test a feature

```text
$feature-testing
Test the search feature I just added. Check empty queries, no results, and repeated
submissions. Run the relevant project checks. Report findings without changing files.
```

The workflow guides Codex to check the intended behavior, edge cases, and interactions, then report what it checked and what remains uncertain. Describe your feature in place of search; ask it to fix confirmed defects if you want edits too.

### Review changes

```text
$code-review
Review my uncommitted changes for bugs and regressions. Give concrete findings
with file locations and explain the impact. Do not modify files.
```

The workflow asks for evidence-backed findings and keeps the review within your requested scope.

### Resume interrupted work

```text
$resume-interrupted-task
Continue the settings-page work from the last session. Inspect the working tree
and existing notes first. Preserve my edits, verify what is finished, and continue
with the next incomplete step.
```

The workflow reconstructs progress from files and available notes. Include the last known goal; it cannot recover context that is no longer available.

## Try a small demo

The [review walkthrough](examples/review-demo.md) gives you a short Python function with an empty-input bug and a prompt to review it. Paste both into a session to see how the skill handles a concrete problem. It includes the expected finding and a read-only boundary; it is a reproducible example, not a recorded result.

## How it works

Each skill is a readable instruction file. Codex uses it alongside your request and project instructions. The plugin supplies no additional tools or permissions. Results still depend on the model, available context, and project checks; review generated work before relying on it.

The package has no telemetry or backend of its own. Your host and any tools you authorize have their own data practices. See the [privacy policy](PRIVACY.md).

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

More prompts, including orchestration, handoffs, and project planning, are in [examples](examples/README.md). Platform guidance covers Flutter, JavaScript/TypeScript, Python, and Laravel/PHP.

## Feedback

Tried a workflow? [Share feedback on GitHub](https://github.com/srajpal/codex-dev-workflows/issues): which skill you used, what you expected, and what was confusing or useful. Remove private code and credentials. Report vulnerabilities through [SECURITY.md](SECURITY.md).

## Install from source

To test local changes, clone or download this repository and add its root as a local marketplace. `.agents/plugins/marketplace.json` points to `plugins/codex-dev-workflows`. Follow the current [plugin-building documentation](https://learn.chatgpt.com/docs/build-plugins) for your host's installation controls. Start a new session after installation.

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

## Documentation and maintenance

- [Architecture](docs/ARCHITECTURE.md): package structure and boundaries.
- [Audit](docs/AUDIT.md): findings, fixes, checks, and limits.
- [Contributing](CONTRIBUTING.md): skill authoring and validation.
- [Releasing](docs/RELEASING.md): GitHub and OpenAI publication.

### Development and validation

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
