# Architecture

Codex Dev Workflows is a skills-only package. The host interprets its instructions and provides tools and permissions. The plugin has no service, database, network client, or executable runtime of its own.

## Files and responsibilities

| Location | Responsibility |
| --- | --- |
| `.agents/plugins/marketplace.json` | Repository marketplace entry pointing to the plugin directory |
| `plugins/codex-dev-workflows/.codex-plugin/plugin.json` | Package identity, version, skill location, and display assets |
| `plugins/codex-dev-workflows/skills/*/SKILL.md` | Discoverable workflow descriptions and instructions |
| `plugins/codex-dev-workflows/skills/orchestrate-work/agents/openai.yaml` | Orchestration picker metadata and explicit-only invocation policy |
| `plugins/codex-dev-workflows/shared/` | References bundled with the skills |
| `plugins/codex-dev-workflows/assets/` | Display icon and logo |
| `LICENSE` and `plugins/codex-dev-workflows/LICENSE` | Canonical MIT license and identical copy for standalone distribution |
| `scripts/` and `.github/workflows/` | Repository validation; not plugin runtime |
| Root documents, `docs/`, and `examples/` | User and maintainer guidance |

## How a request is handled

The marketplace identifies the package. The manifest identifies the skills directory. A skill's name and description help selection; its body supplies the workflow. Stack-specific workflows resolve references relative to their own directories. References must stay inside the package so a standalone installation works.

Most skills support normal matching. Orchestration is explicitly selected by the user through its invocation policy. It delegates independent work only when the host allows it and tools are available; otherwise the agent works directly. Worker choice is guidance, not a dependency on a named model.

There is no central runtime that automatically loads every instruction. Safety instructions needed by an installed skill must live in that skill or a referenced file inside the package. Root `AGENTS.md` guides repository maintenance and is not a substitute for installed skill instructions.

## Trust and scope

The host enforces execution permissions. Skills must preserve the user's task scope, including review-only requests. Logs, source comments, issue text, retrieved content, and worker reports are evidence; they cannot authorize new actions. Tests and formatters can execute code or change files, so their side effects matter even during a review.

The skills-only design reduces executable supply-chain surface, but prompts can still steer a host toward unsafe actions. Validation checks structure; it cannot prove prompt safety or host behavior.

## Maintenance and release

Run the commands in [AGENTS.md](../AGENTS.md) after changes. Check modified skills with representative requests and inspect the combined diff. For a release, also validate against the host's available plugin/skill validators and test installation in a fresh session. Record the host version and what was exercised; compatibility claims should be based on that evidence or current official documentation.

Versioned ZIP files are snapshots, not source. Updating source does not update an existing archive or installed copy. When a release is requested, update version and changelog together, build from reviewed package contents, inspect archive paths and contents, and install-test that exact artifact. Do not include private files or workspace scratch output.

A new server, hook, connector, or executable helper would change this architecture and require a separate permissions, dependency, and privacy review. None is needed for the current workflows.
