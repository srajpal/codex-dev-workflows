---
name: session-handoff
description: Create a concise, evidence-based handoff that lets the next development session continue safely without re-discovering context.
---

# Session handoff workflow

Use this skill at the end of a development session, before delegating work, or when context must move to another agent/person. Inspect the actual working tree, relevant task notes, tests run, and known failures before writing the handoff. Do not manufacture progress from intent.

## Capture the minimum useful context

1. State the task goal and current status.
2. List completed work and the evidence that it is complete.
3. Identify changed files/components and the reasoning behind material decisions.
4. Record tests/checks run, results, and anything not run with the reason.
5. List outstanding work in priority order, with exact next steps and dependencies.
6. Call out blockers, risks, unresolved questions, environment assumptions, and safe reproduction/verification steps.
7. Note uncommitted changes or repository state when relevant.

## Handoff quality rules

- Be concrete enough for another session to continue without guessing.
- Link to authoritative docs/files rather than duplicating long content.
- Separate confirmed facts from hypotheses and recommendations.
- Never claim a release, test pass, or bug fix without evidence.
- Do not include secrets, credentials, or sensitive user data.

## Final format

Use headings: Goal; Current status; Completed; Validation; Next steps; Risks/blockers; Files/context. Keep it compact and actionable.

