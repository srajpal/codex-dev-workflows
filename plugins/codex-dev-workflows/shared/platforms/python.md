# Python guidance

Use this reference for Python projects. Inspect `pyproject.toml`, `requirements` files, lockfiles, task runners, CI, and the test layout before selecting commands. Respect the project's Python-version and dependency-management choices.

## Implementation focus

- Preserve type hints and validation patterns used by the project.
- Separate deterministic business logic from I/O where practical.
- Handle resources with context managers and clean up files, sessions, subprocesses, and background work.
- Make exceptions actionable; do not swallow errors without an established reason.
- Treat configuration and environment data as untrusted and avoid logging secrets.

## Validation

Run the project's formatter, linter, type checker, and test suite. Common tools include `ruff`, `black`, `mypy`/`pyright`, and `pytest`, but use only the configured tooling. Add focused regression tests that cover behavior rather than implementation trivia.

## QA watch list

- boundary type/value errors, encoding and timezone issues
- exception paths, retry/idempotency behavior, and cleanup after failure
- mutable defaults, global state, import-time side effects, and concurrency hazards
- differences between local and packaged/CI execution

