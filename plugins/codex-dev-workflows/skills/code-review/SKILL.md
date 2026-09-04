---
name: code-review
description: Review a change set for correctness, regressions, security, maintainability, and missing tests without changing unrelated code.
---

# Code review workflow

Use this skill to review a pull request, local diff, or proposed design change. Read repository instructions and the relevant requirements before judging the code. Review the actual diff and surrounding code needed to understand behavior; do not ask the author to solve problems that evidence does not support.

## Review process

1. Summarize the change's intended behavior and identify the code paths and contracts it affects.
2. Check correctness across normal, boundary, invalid, error, and state-transition paths.
3. Look for regressions in public APIs, data compatibility, persistence/migrations, concurrency, lifecycle/resource handling, authorization, validation, secrets, logging, performance-sensitive paths, and accessibility as relevant.
4. Evaluate whether tests prove important behavior and whether missing tests could hide a plausible regression.
5. Respect project conventions, but distinguish correctness issues from optional stylistic preferences.

## Findings standard

Only report actionable findings. For each one, give severity, exact location, concrete impact, triggering conditions, and a concise fix direction. Separate blockers from suggestions. If no material issues are found, state what was reviewed and any residual test limitations.

## Final response

Start with findings in descending severity. Then provide a short summary of assumptions, validation evidence, and positive observations only when useful. Do not modify the code unless the user asks for a fix.

