# Prospective external observation — not executed

Distinct Astra exact-source acceptance and root release must precede this
script's execution. The root release records full OBSERVER_SOURCE_SHA,
OPS_SOURCE_SHA and the newly built runtime MANIFEST_SHA; original Syvert2
ZIP and frozen scientific sources are not changed.

After the approved local build creates fresh `/workspace/p02`, prospective
command from repository root:

```
python3 -I -S -B topics/padua-argmax-bridge-20261105/code/audit02_observer/observe.py --output local-output/argmax-bridge-20261105/audit02-known-observation --manifest-sha MANIFEST_SHA --source-sha OPS_SOURCE_SHA
```

The output path must be unused. Exact child command is fixed in source:
`/bin/bash /workspace/p02/run_rehearsal --workers 2`; only known41/511,
primary and fresh each once. Whole engine envelope480CPU-s, worker limits
unchanged (2GiB address-space,260CPU self cap), observer wall2400s plus
bounded shutdown. Observer never imposes an inherited low CPU cap.

Root records its directly observed observer return code and observation
hash/bytes. Require observation complete=true/root decoded exit0 and raw
status0/ECHILD=true, then independently validate package results and proof
fields with the released data checker. Capture under actual two-worker
overlap is checked from retained per-case records. RSS output gives only
individual wait maxima; do not report it as concurrent aggregate RSS.

No retry after scientific admission or partial failure. Preserve failed
observer/build/control evidence. No residual campaign is authorized by
this preregistration. No execution/import/control/native work occurred
while authoring this observer.
