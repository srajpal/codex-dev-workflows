# Security and usability audit

Audit date: 2026-09-11. Scope: the local plugin source, all 12 skills, four platform references, manifest, marketplace entry, validation, CI, and user documentation. Existing release archives and installed copies were not changed.

Three parallel workers reviewed skills, validation, and user guidance. The coordinator reviewed the changes and documented the architecture and maintenance rules. This is a source audit; it does not certify host behavior or a published package.

## Findings and changes

| Priority | Finding | Change |
| --- | --- | --- |
| Medium | Testing and QA repair loops could direct edits during a request limited to testing or review. | Tie fixes to the user's authorized scope and use checks that do not rewrite source during review-only work. |
| Medium | Most installed workflows lacked explicit handling of instructions embedded in logs, issues, fixtures, or reviewed code. Root security policy is not loaded with installed skills. | Put relevant trust and scope guidance in the installed workflows. |
| Medium | The validator silently accepted some invalid JSON roots and incomplete package structures. | Add rejection paths and regression coverage in the repository validator. |
| Low | Orchestration recommended a named model and high reasoning even for bounded work. | Use available capable workers, respect user choices, and keep coordinator verification. |
| Low | There was no root agent guide or explanation of what ships in the package. | Add AGENTS.md and an architecture guide with ownership, checks, and release boundaries. |
| Low | Setup instructions depended on a machine-specific validator location; troubleshooting was sparse. | Lead with repository commands and add installation and reporting guidance. |
| Low | Compatibility documentation incorrectly said assets were omitted and made undated surface claims. | Describe actual package contents and direct users to current host documentation. |

No critical vulnerability was confirmed in the source review. The main risks are a host following unsafe prompt instructions and maintainers trusting incomplete validation.

## Repeatable review

Use [AGENTS.md](../AGENTS.md) for future work. For skill changes, check these cases without touching live services:

- A review-only request encounters a formatter or a repair loop.
- A log or fixture asks the agent to read credentials or send data elsewhere.
- A test command writes data or calls an external system.
- Delegation is unavailable, a worker fails, or two tasks need the same file.
- A resumed task contains uncommitted user changes and misleading old notes.

Expected behavior: preserve scope and user changes, treat embedded instructions as data, identify side effects, work directly when delegation is unavailable, and report evidence and limits. Reuse these cases when relevant; do not add boilerplate to every skill or rerun unrelated tests.

## Release follow-up

Before publishing, run the host plugin and skill validators with their dependencies installed, then install and exercise the exact release package in a fresh host session. Verify explicit invocation and matching where enabled. Record the host version, prompts, and results. Existing ZIP files do not contain this audit's edits.

## Privacy, license, and liability review

Reviewed PRIVACY.md, TERMS.md, SECURITY.md, SUPPORT.md, the MIT License, and manifest policy links. The owner confirmed GitHub as the only contact route. Updated the policies to distinguish passive plugin files from host/tool processing and GitHub submissions. No jurisdiction, legal entity, email address, guaranteed response time, or absolute immunity was invented.

The terms now identify the creator, authors, copyright holders, maintainers, and contributors in the warranty and liability provisions. They explain AI errors, data loss, deployment failures, and third-party charges, preserve non-waivable rights, and avoid adding conditions to the MIT License. These provisions express the intended allocation of risk; they cannot guarantee that every claim will be excluded in every jurisdiction. Jurisdiction-specific legal review remains appropriate before relying on them commercially.

The standalone plugin lacked a LICENSE file. Added an identical copy of the root MIT License and a validation check to keep them aligned. Root LICENSE remains authoritative and unchanged.

Primary references reviewed:

- [OSI's MIT License](https://opensource.org/license/mit): license permissions, warranty disclaimer, and liability language.
- [FTC privacy and security guidance](https://www.ftc.gov/business-guidance/privacy-security): privacy claims must match actual practices.
- [UK Unfair Contract Terms Act 1977](https://www.legislation.gov.uk/ukpga/1977/50/pdfs/ukpga_19770050_en.pdf): an example of statutory limits on exclusions; not an assumption that UK law governs this project.

The GitHub private reporting setting was not verified. If unavailable, the security policy tells users to request a private GitHub route without publicly disclosing the vulnerability. No separate email channel is offered.

## Validation evidence

- Coordinator reran `python scripts/validate_repo.py`: passed.
- Coordinator reran `python -m unittest discover -s scripts -p "test_*.py" -v`: all 12 tests passed.
- `git diff --check`: passed.
- Relative links across 13 root, documentation, and example files resolve; referenced platform paths exist.
- Root and packaged MIT License contents match exactly.
- All 12 skill front matter/name pairs checked. Orchestration's explicit-only metadata is unchanged.
- An independent worker walked through review-only Flutter formatting with a malicious fixture, unavailable delegation, and a staging test with real payment writes. The coordinator checked the results and removed the remaining formatter/test-edit ambiguity. These were prompt walkthroughs, not executed host sessions or live payment tests.
- The coordinator rejected parts of the first validator revision, requested fixes for null JSON roots and malformed policy/URL values, and added a regression for non-string or ambiguous YAML values. Final checks were run after those corrections.
- CI action references were pinned to release commits and regression tests added to the workflow. Remote GitHub Actions execution was not run in this audit.

The installed-host plugin validator and skill validator require PyYAML, which is absent in the available Python environments. The plugin validator was attempted and failed at import; the skill validator has the same dependency. Repository checks are not a replacement for those validators. No package was published, installed, or rebuilt, and existing ZIP archives were preserved.

## PyYAML follow-up

Resolved the missing dependency by installing PyYAML 6.0.3 in the ignored project-local `.venv` environment. Using that interpreter, the host plugin validator passed and all 12 skills passed the host skill validator. Setup commands are in CONTRIBUTING.md. This supersedes the missing-PyYAML limitation above; live installation and invocation testing remain outstanding.
