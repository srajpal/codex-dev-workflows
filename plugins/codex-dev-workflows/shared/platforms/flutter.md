# Flutter guidance

Use this reference only for Flutter/Dart projects. First inspect `pubspec.yaml`, repository instructions, CI configuration, and existing test conventions. Do not assume a state-management package or platform target.

## Implementation focus

- Preserve null safety and use immutable state where the project convention supports it.
- Keep business/game logic testable outside widgets when practical.
- Handle asynchronous work safely: avoid using `BuildContext` across async gaps without checking lifecycle expectations.
- Dispose controllers, focus nodes, subscriptions, timers, and listeners that the owning object created.
- Make state ownership and reset behavior explicit, especially across navigation, restart/new-game, and app lifecycle transitions.
- Test accessibility-sensitive layout: text scaling, semantics, contrast, tap targets, small screens, and long/localized strings where relevant.

## Validation

Use the project-documented commands. When no different project convention exists, the usual baseline is:

```text
dart format --set-exit-if-changed .
flutter analyze
flutter test
```

Run integration tests only when they exist or when the change requires them. Add unit tests for logic and widget tests for meaningful interactions/state transitions; avoid brittle tests tied to incidental widget structure.

## QA watch list

- `setState` after disposal, stale listeners, and leaked timers/controllers
- incorrect rebuild or retained state across routes
- back navigation, deep links, app pause/resume, and persistence behavior
- overflow, keyboard/focus behavior, and pointer/gesture conflicts
- enabled controls that should be disabled during loading or a terminal game state

