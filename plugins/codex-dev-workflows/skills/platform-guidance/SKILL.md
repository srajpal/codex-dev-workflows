---
name: platform-guidance
description: Load focused development and QA guidance for Flutter, JavaScript/TypeScript, Python, or Laravel/PHP projects.
---

# Platform guidance router

Use this skill when the user needs stack-specific implementation, testing, debugging, review, or QA considerations. First identify the project's platform from its files and documentation. Do not infer a framework or command from the user's language alone.

Load exactly the relevant reference:

- Flutter/Dart: `../../shared/platforms/flutter.md`
- JavaScript or TypeScript: `../../shared/platforms/javascript-typescript.md`
- Python: `../../shared/platforms/python.md`
- Laravel/PHP: `../../shared/platforms/laravel-php.md`

If the repository is mixed-stack, load only the components affected by the task. If it uses another platform, use repository configuration and docs as the source of truth rather than forcing one of these guides.

Apply the reference as a checklist, not as a replacement for project-specific instructions. Report which platform guidance was used and any commands or assumptions confirmed from the repository.

