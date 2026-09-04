---
name: feature-development
description: Implement a focused software feature with scoped investigation, verification, and a clear completion report.
---

# Feature development workflow

Use this skill to implement a requested feature or small enhancement. First read the repository's agent instructions and only the documentation relevant to the task. If the project uses Flutter, JavaScript/TypeScript, Python, or Laravel/PHP, load the corresponding file in `../../shared/platforms/`.

## Understand and scope

1. State the intended behavior, acceptance criteria, constraints, and non-goals.
2. Trace the smallest relevant code path and identify affected interfaces, state, data, and tests.
3. Ask for clarification only if ambiguity would change user-visible behavior, data handling, or scope.
4. Keep existing behavior stable unless the request explicitly changes it.

## Implement

- Make the smallest coherent change that satisfies the acceptance criteria.
- Match established project conventions and abstractions.
- Keep error, empty, loading, authorization, and lifecycle behavior deliberate where applicable.
- Update documentation only when it is part of the interface, behavior, or maintenance contract.
- Do not perform unrelated refactors, dependency upgrades, or formatting churn.

## Verify

Run the checks relevant to the edited code using repository-defined commands. Add or update meaningful tests for new behavior and boundary cases. Inspect failures rather than hiding them. If a check cannot run, state why and provide the safest next step.

## Final response

Report the behavior delivered, files/components changed, validation performed and result, tests added/updated, and any remaining manual verification or follow-up. Do not claim full verification beyond the evidence available.

