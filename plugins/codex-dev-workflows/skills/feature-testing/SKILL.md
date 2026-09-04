---
name: feature-testing
description: Test a recently implemented feature for intended behavior, edge cases, regressions, and meaningful missing coverage.
---

# Feature testing workflow

Use this skill after implementing a feature or when the user wants focused verification without a full-product QA sweep. Read relevant project instructions, feature requirements, architecture, and testing documentation first. For supported stacks, load the matching file in `../../shared/platforms/`.

## Test the behavior

1. Identify the feature's intended outcome, entry points, state transitions, dependencies, and observable side effects.
2. Run the configured formatter/static checks and relevant automated tests.
3. Exercise the normal path, invalid input/actions, empty or missing data, boundary values, repeated/rapid actions, errors, cancellation/retry, and restart/reset behavior where applicable.
4. Check interactions with shared components, permissions, persistence, navigation, APIs, and adjacent features.
5. Review existing tests for high-value gaps. Add behavior-focused tests only where they protect a meaningful contract.

## Fix responsibly

When a genuine defect is found, identify the root cause, add a regression test when practical, make the smallest appropriate fix, and rerun relevant validation. Do not redesign unrelated areas during a testing pass.

## Final report

Return:

- checks and scenarios performed;
- defects found, root causes, and fixes;
- tests added or changed;
- validation results and remaining failures;
- risks or scenarios requiring manual verification.

Passing tests alone are not proof that a feature is fully tested.

