# Roadmap

## Works today

- A skills-only plugin with installable, reusable workflows.
- Explicit skill invocation in Codex with `$skill-name`.
- Automatic selection when a request closely matches a skill description.
- Local/repository marketplace packaging for testing and distribution.
- Shared platform references loaded only when relevant.
- Dependency-free repository validation on every push and pull request.

## Next

- Validate each workflow against real open-source example projects.
- Add opt-in variants for accessibility, documentation, and mobile release QA.
- Add automated checks for documentation links and release artifacts.
- Publish a release and repository marketplace instructions after a maintainer creates the GitHub repository.

## Deliberately not implemented

### Pinned prompt shelf or custom Codex sidebar

This repository does not claim to add a custom persistent sidebar, pinned prompt buttons, or a context-menu extension to Codex. The supported skills-only plugin surface does not expose that as an API. Until an official extension point exists, use the Plugins/Skills browser and `$` skill mentions.

### Template picker UI

Plugins can include an MCP server with optional UI, but this project has no service or tool requirement. Adding an app merely to imitate a prompt shelf would add unsupported assumptions and unnecessary maintenance. Reconsider this only if an official UI API or a genuinely useful local tool becomes available.

### Automatic code changes

These skills guide work; they do not grant broader permissions or replace repository-specific instructions. Each agent execution remains subject to its host's normal approvals and sandboxing.
