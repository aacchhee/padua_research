# Fresh frozen polynomial-checker executable

See [the preregistration](../../preregistration-polynomial-regeneration-20261114.md).
`replay.py` compiles the existing metadata-only kernel once, inventories the
new executable/runtime closure, and runs the unchanged strict checker on
retained certificates 2 and 17. It authenticates all 39 retained inputs but
does not claim that the other 37 were replayed. Original accepted records
remain separate. No production, search, retry or historical-byte recovery.

The coordinator must commit the reviewed preregistration before execution.
Outputs stay under the exact fresh local-output root specified there.
