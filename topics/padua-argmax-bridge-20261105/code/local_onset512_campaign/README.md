# Local onset-512 campaign

`runner.py` is a local orchestration adapter around the unchanged frozen engine
and trusted compact-pack validator/storage implementation. It creates one
exclusive output root with `preregister`, runs the actual n=320 `pilot`, then
`remaining` (321..510), at most four cases concurrently. Each degree receives
one primary and one separate fresh verification. Failures stop new admissions.
There is no retry or resume command.

See [the preregistration](../../preregistration-onset512-local.md) for pins, scope,
caps, prior cheap controls and the exact execution commands. All evidence remains
under the named `local-output/` tree; no large evidence is committed.

The local validator subclasses `Access` only to authenticate identities directly
at their retained local paths and to read the separately trusted release's
arithmetic-pin record. Every other pass check is the released `validate_pass`.
The scientific engine, reduction and arithmetic have not been modified.
