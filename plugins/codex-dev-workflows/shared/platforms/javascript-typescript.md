# JavaScript / TypeScript guidance

Use this reference for JavaScript or TypeScript projects. Inspect `package.json`, lockfiles, tool configuration, CI, and existing tests to discover the actual commands and framework. Do not assume React, Node, Vite, Jest, Playwright, or a package manager.

## Implementation focus

- Preserve type safety and strict compiler settings already adopted by the project.
- Validate external data at boundaries; avoid silently spreading `any`, `unknown`, `null`, or `undefined` into application state.
- Make async cancellation, error handling, and loading/terminal states explicit.
- Register and clean up event listeners, timers, subscriptions, and observers exactly once.
- Avoid stale closures, duplicated handlers, mutable shared state, and browser/server environment confusion.

## Validation

Run the configured lint, type-check, test, and production-build commands. Use existing browser automation for user-critical flows; do not introduce a large testing framework merely to satisfy a single workflow.

## QA watch list

- uncaught/rejected promises and unhandled error paths
- rapid repeat clicks/taps/keyboard input and overlapping async requests
- focus, resize, visibility, navigation, storage, and refresh behavior
- DOM/UI state that disagrees with application state
- production build or environment-variable failures masked by development mode

