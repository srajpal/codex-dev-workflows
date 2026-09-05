# Examples

Use a skill explicitly when you want a predictable workflow. Replace bracketed text with your project details.

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

## Use platform guidance

```text
$platform-guidance

This is a [Flutter / JavaScript or TypeScript / Python / Laravel or PHP] project.
I am working on [task]. Identify the repository's actual tooling and apply only
the relevant platform guidance.
```
