# Codex compatibility

This repository uses a skills-only plugin. See [ARCHITECTURE.md](ARCHITECTURE.md) for package boundaries and validation.

## Package format

- `.codex-plugin/plugin.json` declares the plugin and skills directory.
- Each skill has `SKILL.md` with `name` and `description` front matter.
- `.agents/plugins/marketplace.json` points to `./plugins/codex-dev-workflows`.
- Display assets are bundled and referenced by the manifest.
- No MCP server, app, browser extension, hook, or scheduled task is included.

## Use and limits

Select an installed workflow with `$skill-name`. Most skills also permit automatic matching. `orchestrate-work` is explicitly selected, as declared in its `agents/openai.yaml` policy. Start a fresh session after installation or an update so it can receive the new inventory.

The plugin provides instructions, not additional tool access. Delegation depends on the host's available tools and permissions. It does not add a persistent sidebar, pinned prompt buttons, or a one-click template panel.

Supported surfaces and installation controls change. Check the official documentation below for the Codex version being used; repository validation alone does not establish host compatibility. Record the host version and results when testing a release.

## Official references

- [Build plugins](https://learn.chatgpt.com/docs/build-plugins)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Use plugins](https://learn.chatgpt.com/docs/plugins)
