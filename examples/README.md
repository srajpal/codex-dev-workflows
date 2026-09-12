# Examples

Choose the example closest to your task, replace the bracketed text, and paste it into a new Codex session after installing the plugin. The lines after the skill name are optional context; keep only what matters to your task.

## Start a project

```text
$new-project

I want to build [product] for [users]. The first useful release should [outcome].
Constraints: [stack, time, budget, privacy, accessibility, deployment].
Give me a scoped plan with assumptions, milestones, risks, validation, and the next action.
```

## Create agent instructions

```text
$create-agent-instructions

Review this repository and create concise AGENTS.md guidance. Route agents to the
authoritative architecture, testing, security, and deployment documentation.
Do not invent commands or duplicate details that belong in existing docs.
```

## Develop a feature

```text
$feature-development

Implement [feature]. The user-visible outcome is [behavior].
Constraints: [compatibility, design, performance, non-goals].
Inspect repository instructions first, keep the change focused, and report validation evidence.
```

## Test a completed feature

```text
$feature-testing

Test the [feature] I just implemented. The intended behavior is [behavior].
Focus on [edge cases/integration risk], including invalid input and reset or retry paths.
Do not redesign unrelated code.
```

## Run comprehensive QA

```text
$comprehensive-qa

Run a broad QA pass against [product or workflow] and its documented requirements.
Discover the repository's real checks, exercise critical journeys and failure paths,
and report evidence, defects, risks, and remaining manual checks.
```

## Investigate a bug

```text
$bug-investigation

Observed: [actual behavior]
Expected: [expected behavior]
Reproduction: [steps]
Relevant environment, logs, or screenshots: [details]
Find the smallest safe fix, add a regression test when practical, and verify it.
```

## Review a change

```text
$code-review

Review the current diff for correctness, regressions, security, maintainability,
accessibility, and missing tests. Start with actionable findings and cite exact files
or lines. Do not modify the code.
```

## Check release readiness

```text
$pre-release-review

Assess whether [version or change] is ready to release. Check scope, acceptance
criteria, tests, build and deployment evidence, operations, rollback, security,
documentation, and unresolved risks. Give a clear readiness decision.
```

## Create a session handoff

```text
$session-handoff

Prepare a handoff for the next session. Inspect the working tree, recent changes,
decisions, tests, risks, blockers, and exact next steps. Separate verified facts
from assumptions.
```

## Resume interrupted work

```text
$resume-interrupted-task

Continue the interrupted work in this repository. The goal was [goal], and the last
known step was [step]. Reconstruct state from files, diffs, notes, and test output.
Preserve valid changes, state uncertainty, and take the next safe action.
```

## Orchestrate complex work

```text
$orchestrate-work

Act as the coordinator for [goal]. First inspect the repository and define the
acceptance criteria. Delegate only independent workstreams that can run safely in
parallel, with exclusive file ownership and clear validation. Prefer a capable
lower-cost worker with low reasoning for bounded tasks. Review and integrate every
result, then run final validation and report remaining risks.
```

For a small or tightly coupled change, ask the coordinator to keep the work local:

```text
$orchestrate-work

Assess whether this task benefits from delegation. If it is small, tightly coupled,
or likely to create overlapping edits, complete it directly and explain why.
```

If worker agents are unavailable, the workflow falls back to direct execution:

```text
$orchestrate-work

Plan and complete [goal]. Use parallel workers only if collaboration is available;
otherwise execute the plan directly without claiming that delegation occurred.
```

For work that shares a central file, assign that file to one owner:

```text
$orchestrate-work

Coordinate the API, tests, and documentation for [feature]. Multiple workstreams
need the shared schema file, so keep that file with the coordinator and delegate
only work with exclusive ownership. Wait for all workers before final validation.
```

## Use platform guidance

```text
$platform-guidance

This is a [Flutter / JavaScript or TypeScript / Python / Laravel or PHP] project.
I am working on [task]. Identify the repository's actual tooling and apply only
the relevant platform guidance.
```

## If a workflow does not behave as expected

Start with the explicit `$skill-name` form shown above and name the expected outcome. If the skill is not listed, confirm that the plugin is installed and start a new session. For installation and reporting help, see [the main troubleshooting guide](../README.md#troubleshooting) and [SUPPORT.md](../SUPPORT.md).
