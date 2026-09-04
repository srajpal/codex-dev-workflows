---
name: new-project
description: Turn a new software idea into a scoped, buildable project plan before implementation begins.
---

# New project workflow

Use this skill when the user is starting a project, validating an idea, or asking for a practical implementation plan. Ask only for information that materially changes the plan; otherwise state reasonable assumptions.

## Discover

1. Restate the product goal, target users, and the smallest useful first release.
2. Identify constraints: target platforms, preferred stack, integrations, privacy/security needs, accessibility, timeline, budget, deployment, and data ownership.
3. Separate confirmed requirements from assumptions and open decisions.
4. Define non-goals for the first release so the plan stays tractable.

## Design before building

Propose a lightweight foundation appropriate to the project:

- a short product brief and acceptance criteria;
- an architecture outline with major components and data flows;
- repository documentation for architecture, testing, design/system rules, and domain-specific rules when relevant;
- concise agent instructions that route an agent to authoritative project documentation;
- an ordered backlog of small, independently verifiable milestones.

Choose technology only when the user has supplied a preference or trade-offs can be explained concisely. Do not pretend a decision is final when it remains open.

## Build plan

For each milestone, state the user-visible outcome, implementation boundary, dependencies, tests/validation, and completion criteria. Put risky assumptions, security-sensitive work, and irreversible data decisions early enough to validate before substantial build effort.

## Final response

Return:

- project summary and first-release scope;
- requirements, assumptions, and non-goals;
- recommended repository/documentation structure;
- architecture and data-flow outline;
- milestone plan with acceptance criteria;
- immediate next action and unresolved decisions.

Do not start implementation unless the user asks for it.

