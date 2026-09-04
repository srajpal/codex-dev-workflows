# Laravel / PHP guidance

Use this reference for Laravel/PHP projects. Inspect `composer.json`, `artisan` commands, environment configuration, migrations, routes, policies, queues, CI, and existing tests. Respect the project's Laravel and PHP versions.

## Implementation focus

- Preserve framework conventions for requests, validation, authorization, models, events, queues, and error responses.
- Validate at request boundaries and authorize every relevant action server-side.
- Use database transactions when a multi-step write must be atomic.
- Avoid N+1 queries, mass-assignment mistakes, missing tenant/account scoping, and inconsistent serialization.
- Keep secrets out of version control and logs; use the project's configuration conventions.

## Validation

Use repository commands and existing test configuration. Typical checks may include `php artisan test`, a formatter such as Pint, static analysis, and a frontend build when applicable, but do not assume their availability.

## QA watch list

- validation/authorization gaps and incorrect policy behavior
- migrations, seeders, factories, rollback paths, and queue failures
- cache/session behavior, locale/timezone formatting, and pagination/filtering boundaries
- HTTP status/error contracts, database constraints, and concurrency-sensitive writes

