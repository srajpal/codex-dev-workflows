# Support

GitHub is the only support and privacy contact route. For privacy questions, contact the repository maintainers through an issue without posting personal or sensitive details. Ask for a private GitHub route when needed.

## Before opening an issue

Please check the [README troubleshooting steps](README.md#troubleshooting), [examples](examples/README.md), and [Codex compatibility notes](docs/CODEX-COMPATIBILITY.md). If possible, retry in a new session with the explicit `$skill-name` form before reporting a problem.

## Questions and bugs

Use [GitHub Issues](https://github.com/srajpal/codex-dev-workflows/issues) for installation questions, documentation problems, and reproducible workflow behavior. Do not include credentials, private source code, confidential logs, or personal information in an issue.

When reporting a problem, include:

- Plugin version and commit, if known
- Skill name and the prompt that triggered it
- Codex surface used, such as desktop app or CLI
- Expected behavior and observed behavior
- Relevant validation output with sensitive values removed

A useful minimal reproduction looks like this:

```text
Plugin version or commit: [value]
Installation method: [published listing or local marketplace]
Codex surface and version: [value]
Skill: $[skill-name]
Prompt: [smallest prompt that shows the problem]
Expected: [result]
Observed: [result]
Validation output: [optional, with sensitive values removed]
```

## Security reports

Do not report suspected vulnerabilities in a public issue. Follow [SECURITY.md](SECURITY.md) instead.

## Contributions

Pull requests for documentation, examples, and workflow improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution process.
