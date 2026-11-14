# Focused synthetic continuation02 — unexecuted

Source candidate remains exactly v3 manifest
`836dcbf098ecb391b740fa884e594e260b74705e88d26339dcc5cba9bbbf673f`.
Harness `controls_02.py` SHA256:
`e759200024d35cb07ca6cac3de88001a1345b3d7bca3900f61bcc7f26d91d935`.
Root approved the fixture correction design; execution awaits its reviewed
publication and explicit release. Original failed run is retained in
RESULT-01.md and `/workspace/p02c`.

Exact command after release, from repository root:

```
python3 -I -S -B topics/padua-argmax-bridge-20261105/code/audit02_execution_review/controls_02.py --source topics/padua-argmax-bridge-20261105/code/audit02_execution --output /workspace/p02c2
```

Only these cases execute, once in order: parentdeath, reboot, preflight,
deleted, partial, zipbounds, pin. Do not repeat the five passed cases.
The original scenario meanings, substitutions, stop-first-failure behavior,
observer subreaper cleanup and per-case10/12CPU-second and20wall-second
caps remain as preregistered. Seven cases give84 self CPU seconds and140
wall seconds plus small observer overhead, within180/300 aggregate envelope.

The only fixture implementation change is in the parentdeath copied
`plans.py`: replace the uniquely matched wrapper_cpu_seconds260 with10
before creating the fixture manifest. The unchanged worker can then apply
its own10CPU-second limit inside the harness's inherited hard12. Parent-death
behavior is otherwise identical; fake engine remains only a sleeper. This
changes neither the actual package's260 limit nor any scientific engine cap.
Other fixture plans remain byte-identical to v3. No candidate source changes.

No execution is claimed here. Preserve any new failure and stop; do not
adaptively rerun a case or expand the scope.
