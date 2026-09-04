---
name: pre-release-review
description: Assess whether a software change is ready to release by checking scope, validation, risk, operations, and rollback readiness.
---

# Pre-release review workflow

Use this skill before shipping a release, demo, beta, or major milestone. Read the release scope, acceptance criteria, repository instructions, testing docs, deployment/runbook material, and changelog/release notes when present. This is a review: do not publish, deploy, tag, or modify external systems unless the user explicitly authorizes it.

## Readiness review

1. Confirm the intended release contents and identify deliberate exclusions.
2. Review the diff for correctness, compatibility, migrations, feature flags, configuration, upgrade/downgrade concerns, and user-visible behavior.
3. Verify evidence from required tests, static analysis, builds, integration/e2e checks, manual QA, and platform-specific checks. Run safe relevant checks when authorized.
4. Review operational readiness: environment configuration, secrets handling, observability, error reporting, performance/capacity risk, backups, rollback path, and support/documentation impact.
5. Identify blockers, high-risk unknowns, and deferred issues. Do not convert an uncertain condition into a release approval.

## Final recommendation

Provide a release-readiness table or concise list with each criterion, evidence, status, and owner/next action for gaps. End with one of: ready with evidence, conditionally ready with named conditions, or not ready with blockers. State exactly what remains to verify.

