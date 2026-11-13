# Exact analytic checks: current rerun interface

From the repository root, use:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/onset512_analytic/check.py
```

`-E` ignores Python environment variables, including PYTHONOPTIMIZE. The
current checker also refuses explicit optimized execution (`-O`, `-OO`)
before evaluating or printing a verdict. Its assertions are part of the
check and must remain active.

The audit-05 response adds that guard and an explicit exact-rational check
of `log(pi) > 11/10`, an already consumed manuscript input. It changes no
comparison constant or theorem threshold. The resulting source SHA-256 is
`5ce8cc0701ed105fa619674993583f749046709cb02d233570e2dedc59ca1d2d`.
The normal output has the same eleven fields and values as receipt.json
on the recorded Python 3.12.14 runtime. The Python version field can differ
on another runtime.

PREREGISTRATION.md and receipt.json are historical execution records. Their
original command and source identity remain unchanged; the safe current
command above supersedes them for prospective reruns. Prior recorded normal
executions are not retroactively attributed to the new guarded source.

The sixty manuscript base-table entries are evaluated using this module's
exact interval API; they are not sixty fields in receipt.json. The table's
own explanation distinguishes those evaluations from the stored receipt.
