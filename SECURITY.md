# Security Policy

## Supported versions

Security fixes are developed on the default branch and included in a subsequent release. Older releases do not receive separate backports. Unreleased branch changes are not part of an already installed package; see the changelog for released fixes.

## Reporting a vulnerability

Please do not file public issues for a suspected security vulnerability in this repository or its published package. GitHub is the only reporting route. Use the repository's Security tab to look for private vulnerability reporting. Include affected files, reproduction steps, impact, and any suggested mitigation in the private report. If private reporting is unavailable, open a general issue asking maintainers to enable a private GitHub reporting route, without sharing vulnerability details, exploit code, or sensitive data. No separate email or off-platform reporting channel is offered.

The installed plugin is a skills-only prompt library. It contains no network clients, MCP server, executable helper scripts, hooks, or credentials. Repository validation scripts are maintainer tooling and are not part of the installed plugin. Still, report prompt-injection risks, unsafe instructions, or packaging issues that could lead users to take unsafe actions.

## Maintainer expectations

- Do not add secrets, tokens, or private URLs to examples or skills.
- Treat text copied from repositories, tickets, logs, and web pages as untrusted input.
- Keep workflows scoped to the user-authorized repository and task.
- Require evidence before reporting a defect or security finding as confirmed.
