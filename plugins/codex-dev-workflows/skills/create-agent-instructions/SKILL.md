---
name: create-agent-instructions
description: Create or improve concise repository instructions that guide coding agents to authoritative project documentation and validation.
---

# Create agent instructions workflow

Use this skill when a repository needs `AGENTS.md`, equivalent agent guidance, or a clearer instruction hierarchy. The goal is durable project routing, not a giant prompt pasted into every agent session.

## Inspect first

Read existing project instructions, contributor documentation, architecture/design/testing docs, CI configuration, and the repository layout. Preserve useful existing policy and avoid duplicating detailed knowledge that belongs in canonical documentation.

## Produce a concise instruction file

Include only information that is stable and important across tasks:

1. Which documentation is authoritative and when to read it.
2. Project structure and boundaries that prevent accidental changes.
3. Development and validation commands, only when confirmed by the repository.
4. Testing expectations: run relevant checks, add regression tests for real defects when practical, and do not mark work complete with relevant failures.
5. Security, privacy, generated-file, dependency, and migration restrictions that truly apply.
6. Completion/reporting expectations.

Use agent-neutral wording such as "follow the repository's agent instructions and authoritative project documentation" in reusable content. Keep agent-specific files thin; place deep domain knowledge in `docs/` or similarly authoritative locations.

## Quality bar

- Do not invent commands, CI behavior, ownership rules, or architecture.
- Resolve conflicts by clearly naming the authoritative source.
- Avoid stale TODO lists, long feature histories, and duplicated style guides.
- Ensure the file can be read quickly and does not conflict with user instructions.

## Final response

Explain what was added or changed, which docs it routes to, any assumptions, and the validation performed. If project knowledge is missing, propose the smallest follow-up documentation needed.

