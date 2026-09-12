# Releasing

Publish only when the user requests it. GitHub and the OpenAI directory are separate release steps.

1. Check the working tree and remote branch. Preserve unrelated changes and old archives.
2. Update the manifest version and changelog. Run the repository checks and host validators documented in CONTRIBUTING.md.
3. Build the ZIP from `plugins/codex-dev-workflows/` with `.codex-plugin/plugin.json`, `skills/`, `shared/`, `assets/`, and LICENSE at the archive root. Exclude the repository, Python environment, caches, and temporary files. Verify archive contents against the source and test its integrity.
4. Commit and push the reviewed source. Check GitHub Actions for the full commit SHA. Attach the verified ZIP to the matching GitHub release tag; do not silently replace an already published artifact.
5. Open [OpenAI's plugin portal](https://platform.openai.com/plugins). Find the existing Codex Dev Workflows listing and choose **Upload draft**. Do not create a duplicate listing. Upload the new ZIP.
6. Check the version, prompts, all 12 imported skills, and scan results. Set the support URL to the repository's SUPPORT.md page. The portal's public developer name must match the selected verified identity; the owner confirmed SUNNY RAJPAL for individual publication. Portal listing fields can differ from the package's contributor attribution.
7. The owner prefers the coordinator to handle future submissions when permitted. Review the final attestations. Obtain any confirmation required by the host before accepting binding developer terms; the MIT disclaimer does not override obligations owed to OpenAI.
8. Submit for review. Distinguish **Draft**, **In review**, **Approved**, and **Published**. Publish the approved version only within the user's authorization and verify that the portal labels that exact version Published.

Keep GitHub as the only support/privacy contact route. Preserve the existing plugin identity and policy URLs. Check the current portal and [official submission documentation](https://developers.openai.com/plugins/deploy/submission) if controls change.

## Release 0.4.2

- Source commit: `05b99ff4648951fd597b3a356127f9ce4bee50fa`.
- [GitHub release](https://github.com/srajpal/codex-dev-workflows/releases/tag/v0.4.2).
- [Passing CI run](https://github.com/srajpal/codex-dev-workflows/actions/runs/34663058392).
- ZIP SHA-256: `b28fabccb31e62c2f2c37e89cf79e6743890ecc0ba1569b31b890db11cf47235`.
- OpenAI listing: `plugins_6a9b7d9f2fa0819194b71d627744d569`.
- All 12 imported skills passed OpenAI scanning. The owner completed the final submission attestations, and the coordinator published the approved version. The portal confirmed **0.4.2 Published**.
