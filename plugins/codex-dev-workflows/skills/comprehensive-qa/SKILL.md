---
name: comprehensive-qa
description: Perform a broad, evidence-based QA pass across software behavior, user journeys, state, regressions, accessibility, and operational risk.
---

# Comprehensive QA workflow

Use this skill for a broad QA pass of a software product, service, app, game, or user-facing workflow. Read the repository's instructions, requirements, architecture, testing documentation, and release context before choosing checks. Load the matching platform guidance from `../../shared/platforms/` when applicable.

## QA pass

1. Run the repository's configured formatter, static analysis, tests, build checks, and relevant integration or end-to-end checks. Discover the commands from project documentation and configuration; do not invent them.
2. Map the critical user journeys, entry points, state transitions, dependencies, persistence boundaries, and observable side effects.
3. Exercise normal behavior, invalid input/actions, empty or missing data, boundary values, repeated or rapid actions, errors, cancellation, retry, offline or degraded dependencies, authorization boundaries, and restart/reset behavior where applicable.
4. Compare visible behavior, stored state, API responses, logs, notifications, and terminal states so that user-facing output agrees with underlying state.
5. Check regression surfaces across shared components, navigation, settings, permissions, localization, accessibility, responsive layouts, performance-sensitive paths, and supported platforms when they apply.
6. For games, additionally verify rules, modes, scoring, lives, timers, progression, win/loss conditions, save/restore, and repeated consecutive sessions.
7. Review security and operational risks relevant to the product, including sensitive-data handling, error disclosure, recovery behavior, observability, backups, and rollback assumptions.

## Repair loop

For a confirmed defect: isolate the root cause, add a focused regression test when practical, apply the smallest correct fix, and rerun the relevant checks. Do not replace a systematic QA pass with superficial coverage growth or change intended product behavior without evidence.

## Final report

List the tests and scenarios performed, confirmed defects and fixes, tests added, remaining failures, known risks, and manual testing still needed. Never report a product as fully tested solely because its automated suite passes.
