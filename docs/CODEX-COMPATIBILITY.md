# Codex compatibility and design choices

This repository intentionally uses the smallest supported extension: a skills-only plugin.

## What the format uses

- `.codex-plugin/plugin.json` is the plugin manifest.
- `skills/` contains focused skill directories, each with a required `SKILL.md` and YAML `name`/`description` metadata.
- `.agents/plugins/marketplace.json` is a repository-local marketplace entry that points at `./plugins/codex-dev-workflows`.

The manifest declares only skills. It intentionally omits MCP servers, apps, browser extensions, hooks, scheduled tasks, and assets because none are needed for a portable prompt/workflow library.

## Supported use model

In Codex, installed plugin skills can be explicitly selected with `$skill-name`; Codex may also select a skill when the request matches its description. Use a new session after installing or updating a plugin so the active session receives the new skill inventory.

## Supported surfaces and limits

Official documentation states that plugins work in Codex in the ChatGPT desktop app and that Codex CLI has a plugin browser. The Codex IDE extension does not support plugins. A plugin can contain skills, connectors, MCP servers, browser extensions, hooks, and scheduled-task templates, but including a capability in the platform does not make it necessary for this repository.

This project has no supported API for a custom pinned sidebar or one-click prompt-button shelf. That remains a future idea rather than a promised feature.

## Primary official references

- [Build plugins](https://learn.chatgpt.com/docs/build-plugins)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Use plugins](https://learn.chatgpt.com/docs/plugins)
- [Skills and plugins overview](https://learn.chatgpt.com/docs/skills-and-plugins)

