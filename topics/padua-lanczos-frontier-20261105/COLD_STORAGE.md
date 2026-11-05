# Cold-storage manifest — Lanczos frontier round 2

No external delivery is claimed. [cold-storage.json](cold-storage.json) inventories only actual local G0 outputs by absolute path, SHA-256 and byte size. [Independent report](independent-checks-g0.md) gives frozen commands, source SHA, package pins, restored historical Git blobs and verification outcomes; [short receipt](evidence/g0-summary.json) and [kernel receipt](evidence/g0-kernel-probes.json) are committed. Third-party code, HTML and raw outputs stay outside Git. L7 source-access hashes are separately in [its preparation receipt](evidence/l7-preparation.json); those are retrieval metadata, not scientific evidence.

## Regeneration and checks

Run code/g0_replay.py with the report's pinned dependencies and unchanged polyrat checkout. It exports the frozen source commit, restores four historical blobs with SHA/size checks, checks upstream/local source pins and runs five replay commands. Optional diagnostics repeat E6 and vary BLAS kernels. Current controlled E6 values recur on this runtime; kernel sensitivity and missing historical dispatch constrain interpretation. Programmatic inequality/identity outcomes are separate from the checker's dated G0 stop disposition. Raw timestamps, output paths and run durations are not promised to regenerate byte for byte.

## Retention and retrieval

Actual local path is /tmp/padua-lanczos-frontier-g0; sandbox retention is not guaranteed. Desired Windows destination from handoff01 is Downloads/padua/cold_storage/padua-lanczos-frontier-20261105/, but no access or transfer took place. AC remains archive custodian; physical delivery is pending. If local files survive, hash and size must match the JSON before use. Otherwise regenerate from committed code and pinned Git history; do not claim to have recovered original timed receipts. These outputs support replay diagnosis, not a new computer-assisted theorem.

## G0 explanation outputs

The inventory now includes raw attribution Q/H, reference and propagated-residual NPZ files and independent fresh-kernel basis NPZ files. Command/checker identifiers resolve to the exact commands and results in the committed methods and independent report/receipts. No raw basis enters Git. Source08b9f18d6ac1c7c90546763ac330fff754030fcb6e1561989d764990ed3dd984 was independently executed. Additive G0 resolution changes no original output. Physical archive delivery remains pending.

## L4 exact arrays and durable scientific recheck

The local inventory includes separate developer/independent comparator envelopes (about49MB compressed each), signed full BJ responses/bases (about44MB each), vector candidates, Rayleigh values and small raw receipts. All remain outside Git. Command identifiers map to the exact generating/checker records; paths may be normalized as path_roots[root]/path in JSON. Input/source identities and actual verification outcomes are committed. No Windows delivery or guaranteed temporary-file retention is claimed.

Large historical compressed files are not required to recheck the scientific theorem. The combined fixed certificate in evidence/l4-fixed-certificate.json supplies625 upper integers and91 lower integers. code/l4_recheck_fixed.py checks those against newly generated arrays, independently of historical raw paths, gzip timestamps and fresh floating proposals; evidence/l4-fixed-recheck.json records its actual execution. The existing historical audit remains useful provenance, while this companion is the repository-only acceptance path.

### Fresh-machine recipe (planned end-to-end recipe)

The individual generator/checker executions were performed as recorded in independent-checks-l4.md. The following new-directory recipe is supplied for future reproduction and was not executed as one combined sequence. Use a full-history clone, or fetch historical source2b52b432fe59c9a50aef9deebe5152c5d6874465 first; its two blob IDs were independently verified here against the inherited cold-storage manifest. All named output directories must be new. No polyrat source is needed for L4.

```sh
python -m pip install --target /tmp/padua-l4-check-deps python-flint==0.9.0 numpy==2.3.5
python - <<'PYRECOVER'
from pathlib import Path
import subprocess,json,hashlib
rows=json.loads(Path('topics/padua-lanczos-drift-20261101/cold-storage.json').read_text())['entries']
out=Path('/tmp/padua-l4-proof-inputs');out.mkdir(parents=True,exist_ok=False)
for row in rows:
    name=Path(row['path']).name
    if name not in {'e1-scalar-cgs2.json','e1-multinode-certificates.json'}:continue
    data=subprocess.check_output(['git','show','2b52b432fe59c9a50aef9deebe5152c5d6874465:'+row['path']])
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
    (out/name).write_bytes(data)
PYRECOVER
PYTHONPATH=/tmp/padua-l4-check-deps OPENBLAS_NUM_THREADS=1 python -B topics/padua-lanczos-frontier-20261105/code/l4_envelope.py --frozen-evidence /tmp/padua-l4-proof-inputs --output-dir /tmp/padua-l4-fresh-upper --receipt /tmp/padua-l4-fresh-upper.json
PYTHONPATH=/tmp/padua-l4-check-deps OPENBLAS_NUM_THREADS=1 python -B topics/padua-lanczos-frontier-20261105/code/l4_full_witness.py --frozen-evidence /tmp/padua-l4-proof-inputs --upper-receipt topics/padua-lanczos-frontier-20261105/evidence/l4-envelope.json --output-dir /tmp/padua-l4-fresh-witness --receipt /tmp/padua-l4-fresh-witness.json
PYTHONPATH=/tmp/padua-l4-check-deps python -B topics/padua-lanczos-frontier-20261105/code/l4_recheck_fixed.py --certificate topics/padua-lanczos-frontier-20261105/evidence/l4-fixed-certificate.json --fresh-envelope-receipt /tmp/padua-l4-fresh-upper.json --fresh-witness-receipt /tmp/padua-l4-fresh-witness.json --frozen-evidence /tmp/padua-l4-proof-inputs --output /tmp/padua-l4-fresh-check.json
```

The full-witness generator deliberately uses the committed original upper receipt only as metadata for the fixed integerB; it opens no old upper matrix. The portable checker recomputes the actual upper on fresh S using the committed fixed625-vector. Newly proposed floating vectors are not certificate inputs.
