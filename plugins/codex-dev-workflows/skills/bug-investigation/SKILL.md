---
name: bug-investigation
description: Reproduce, isolate, fix, and verify a software defect with evidence and minimal scope.
---

# Bug investigation workflow

Use this skill when observed behavior differs from expected behavior. Start from concrete evidence: reproduction steps, logs, error messages, screenshots, environment, affected versions, and expected result. Read relevant repository instructions and documentation before changing code; load platform guidance from `../../shared/platforms/` when applicable.

## Investigate

1. Write a concise problem statement: expected, actual, scope, frequency, and reproducibility.
2. Reproduce safely. If it cannot be reproduced, preserve evidence and distinguish confirmed facts from hypotheses.
3. Trace the smallest likely execution path. Examine inputs, state transitions, error handling, data contracts, concurrency/timing, lifecycle, configuration, and recent relevant changes.
4. Form and test hypotheses. Do not mistake correlation, a warning, or a stack trace location for root cause.

## Fix and verify

- Prefer a focused regression test that fails before the fix and passes afterward when practical.
- Make the narrowest fix that addresses the root cause and respects the existing contract.
- Run relevant static checks and tests, then repeat the original reproduction path.
- Consider adjacent paths that share the same cause without broad unrelated refactoring.

## Final report

Report the observed issue, reproduction status, root cause evidence, fix, tests/checks run, and any remaining uncertainty or follow-up. If no defect is confirmed, say so clearly and recommend the next diagnostic data to collect.

