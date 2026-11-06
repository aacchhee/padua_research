# Projection reference for audit-01 M3

`projection-reference.json` is the newly pinned fixed-configuration response
run on2026-11-06, not an archive recovery of the missing Nov5 temporary
witnesses. It contains all12 cases: both families, N4/N8, C4/LU/nodeqr at
160dps, with unchanged optimizer rules and no re-selection or tuning.
Each case includes the full raw target as exact binary64 hex words, the
returned rational nodes/normalized weights, metrics and per-case identities.
The platform/source fields identify the actual producer. `source_commit`
identifies the unchanged imported baseline modules; the newly added exporter
is separately content-pinned and published with this response.

Regenerate a separate new run (never overwrite the reference):

```sh
python topics/nn-mop-stability-20261105/code/projection_reference.py --output /tmp/new-projection-reference.json
```

Verify the committed reference without generating a comparison target:

```sh
python topics/nn-mop-stability-20261105/code/independent_check_followup_projection.py
```

The checker enforces the committed file SHA-256 and all12 case/input/target
identities, then independently reconstructs the exact moment coefficients
for all12 cases. It independently forms N4 objective gradients as well;
N8 gradients are not checked by this code. No producer fit is executed by
the checker and no global nearest-minimum claim follows. Current execution
is a developer verification of the independent formulation; Claude's focused
response audit remains separate. Size/retention authority is recorded once
in LOG.md; no storage cleanup is performed.
