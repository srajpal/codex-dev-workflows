# Try a code review

This is a small example to try after installing the plugin. It is not a recording or a claim about a completed host test. No repository, credentials, or external service is needed.

Start a new Codex session, choose `$code-review`, and paste this request:

````text
Review this Python function. It should return the arithmetic mean for a nonempty
list of numbers and None for an empty list. Identify any bug, explain when it
happens, and suggest the smallest fix. Do not create or edit files.

```python
def average(values):
    return sum(values) / len(values)
```
````

## What to look for

The concrete defect is division by zero for `average([])`: the function raises an exception instead of returning `None`. A useful review identifies that input and suggests checking for an empty list before dividing. It should preserve the read-only request and distinguish reasoning from any checks it actually runs.

The response wording may vary. A review should not invent unrelated requirements or claim tests passed without running them.

## Try it on your project

Use `$code-review` with your uncommitted changes, state the intended behavior, and say whether you want findings only or fixes too. See [three starting prompts](../README.md#three-useful-starting-points) or the [full examples](README.md).
