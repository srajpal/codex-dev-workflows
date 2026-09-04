---
name: game-qa
description: Perform a comprehensive engineering and gameplay QA pass that tries to find rule, state, UX, and regression defects in a game.
---

# Comprehensive game QA workflow

Use this skill for a game QA pass, especially before a milestone or release. Read the repository's instructions plus the relevant game rules, architecture, and testing documentation. Treat documented game rules and intended behavior as authoritative; do not change them because another design seems preferable. Load the matching platform guidance from `../../shared/platforms/`.

## QA pass

1. Run the project's configured formatter, static analysis, and existing tests. Investigate meaningful failures and warnings.
2. Review coverage for game logic and add high-value tests for important untested rules or state transitions.
3. For each affected game mode, verify initialization, valid and invalid actions, scoring, win/loss conditions, progression, completion, restart/new game, navigation away/back, state reset, and saved/restored state if applicable.
4. Actively try to break the game with boundary values, missing/corrupt data, duplicate or rapid input, unexpected action order, mid-game restart/navigation, repeated consecutive games, and unusual but valid player behavior.
5. Confirm displayed score, lives, timers, progress, selections, messages, controls, and terminal state agree with underlying state. Check that unavailable actions are actually blocked.
6. Evaluate regressions across shared components, modes, settings/difficulty, input methods, themes, localized text, accessibility, and screen sizes when they apply.

## Repair loop

For a confirmed defect: isolate the root cause, add a regression test when practical, apply the smallest correct fix, and rerun relevant checks. Do not replace a systematic QA pass with superficial coverage growth.

## Final report

List tests/scenarios performed, confirmed defects and fixes, tests added, remaining failures, known risks, and manual testing still needed. Never report a game as fully tested solely because its automated suite passes.

