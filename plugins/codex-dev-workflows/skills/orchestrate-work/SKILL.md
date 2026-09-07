---
name: orchestrate-work
description: Coordinate complex, divisible work by planning, delegating independent tasks in parallel, integrating the results, and verifying the complete outcome.
---

# Orchestrate work

Use this skill when the requested outcome contains multiple genuinely independent workstreams. The current agent remains the coordinator and owns the plan, important decisions, integration, final verification, and user-facing result.

First inspect the request, repository or project instructions, current state, acceptance criteria, and available collaboration capabilities. Work directly when the task is small, tightly coupled, sequencing-sensitive, collaboration is unavailable, or delegation overhead would exceed its benefit. Never claim that delegation occurred when it did not.

## Coordinate the work

1. Define the end-to-end acceptance criteria and divide the work into packages with clear objectives, inputs, outputs, dependencies, validation, and file or resource ownership.
2. Give each package exclusive edit ownership. Do not dispatch parallel workers that can modify the same file or shared state. Keep shared interfaces, migrations, generated outputs, and other conflict-prone areas with one worker or the coordinator.
3. Dispatch only independent packages in parallel and sequence dependent packages. Use the collaboration capabilities available in the host without assuming a particular API or workspace-isolation model.
4. Prefer a lower-cost capable worker, such as Luna with high reasoning when that model and effort are available and appropriate for clear, bounded work. Use a stronger worker for ambiguous, cross-cutting, security-sensitive, or integration-heavy work. Follow an explicit user model choice. If the preferred combination is unavailable, use a supported equivalent or inherit the host default.
5. Tell each worker its objective, scope, owned and prohibited files or resources, constraints, acceptance criteria, validation, and expected report. Require evidence of findings, changes, checks, failures, and follow-up needs.
6. Continue useful coordinator work while workers run only when it is read-only or limited to paths and resources that no worker owns. Otherwise wait. Track dependencies and communicate new constraints when they affect active work.
7. Treat worker output as evidence or a proposed change, not as automatically correct. Inspect it against the source and acceptance criteria, resolve conflicts centrally, and preserve the user's authorization boundaries.
8. Before final integration, wait for every dispatched worker to finish or explicitly stop and account for any worker that is canceled, blocked, or no longer needed. Integrate completed work in dependency order only after this barrier. Inspect the aggregate diff or resulting state, re-check shared assumptions, and run the relevant tests, lint, build, and end-to-end checks.

## Completion report

Report whether work was delegated, which workstreams ran, what was integrated, validation results, incomplete or blocked work, and remaining risks. Do not claim that a worker ran or a check passed without evidence.
