# Cold-storage manifest — Lanczos frontier round 2

No external delivery is claimed. [cold-storage.json](cold-storage.json) is the small committed index for one complete external inventory; the full inventory contains actual local G0/L4/G1/G2 artifacts with normalized roots, SHA-256 and byte size. SH created no external raw arrays. [Independent report](independent-checks-g0.md) gives frozen commands, source SHA, package pins, restored historical Git blobs and verification outcomes; [short receipt](evidence/g0-summary.json) and [kernel receipt](evidence/g0-kernel-probes.json) are committed. Third-party code, HTML and raw outputs stay outside Git. L7 source-access hashes are separately in [its preparation receipt](evidence/l7-preparation.json); those are retrieval metadata, not scientific evidence.

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

## Current storage layout and validation

The complete normalized inventory is intentionally **outside Git** at
`/tmp/padua-lanczos-frontier-storage/full-inventory.json`: 281 artifacts,
91,574 bytes, SHA-256
`2490be33b705109a09849d2efb2db3fd880041f5050534bd9bdf8efd7ee2932e`.
The small committed index points to that exact file, the historical inventory,
source pins, checker reports and status. This is one external inventory;
large manifests are not divided among committed files to evade limits.
Each entry resolves as `path_roots[root]/path`; command/checker/source IDs
normalize repeated provenance. Log timing, gzip headers and output paths
need not regenerate byte-for-byte.

All original59 identities/commands remain in the historical Git manifest:
commit `aab7bbe97899b0216d60a015c1a0d2cb2d7cbd99`, path
`topics/padua-lanczos-frontier-20261105/cold-storage.json`, blob
`11103cf9de039f226c9c9b0cac355d442308562c`, 16,209 bytes, SHA-256
`a4d4724f91257693ebb9ec400a3478743b64579f31b30ec0f6b053a4baaf23f5`.
Read-only `git show COMMIT:PATH` retrieves that manifest. It preserves its
identities; it does not promise retention of the original temporary data.

The following inventory-only commands were **actually executed**, with no
scientific reruns. The final validator checked all281 retained artifacts:
281 present and matching, zero missing, zero mismatches.

```sh
python -B topics/padua-lanczos-frontier-20261105/code/storage_inventory.py --build --output /tmp/padua-lanczos-frontier-storage/full-inventory.json --index topics/padua-lanczos-frontier-20261105/cold-storage.json
python -B topics/padua-lanczos-frontier-20261105/code/storage_inventory.py --check-index topics/padua-lanczos-frontier-20261105/cold-storage.json
```

`storage_inventory.py` recovers the pinned historical seed read-only, inventories
available G1 case files and native outputs plus G2 receipt-referenced arrays,
and writes the large inventory externally. Its root/receipt options allow a
new inventory for fresh output locations. If the native worker's supplemental
inventory is absent, it discovers current native files directly and labels
canonical regeneration commands accordingly. Exact historical metadata-writer
shell strings were not all retained; that gap is explicit rather than invented.
The scientific generators/checkers and per-case commands remain committed or
recorded in their receipts. The helper never runs scientific cases itself.

If retention has failed, `--check-index ... --allow-missing` reports missing
paths explicitly while still rejecting every identity mismatch. Missing files
must not be relabeled as recovered bytes. The committed code/recipes can
regenerate fresh scientific outputs and then a new inventory; historic
timestamps and vanished logs are not promised to reappear. Physical delivery
to the requested Padua Windows destination remains pending.

## G1 outputs and cost boundary

The external inventory contains the FLINT producer's exact basis/recurrence
arrays, per-degree endpoint files, receipts and logs for all eight legacy
cases; four completed T24 maxdegree20 cases; and degree14 BJ cost benchmarks
on both grids. Independent native GMP files, compiler artifacts, comparisons,
receipts and progress logs are normalized under `g1_native`. The independent
worker's original151-file inventory was checked against every retained file
before integration; its byte identity is also retained in the complete index.
Source pins resolve to the actual committed FLINT/C++/runner/comparison code.

Actual completed best coverage is122/152 preregistered rows. All88 inherited
2–12 overlap rows and all76 T24 degree2–20 rows agree exactly between distinct
implementations; rotated/BJ13–14 are additional completed FLINT rows. No fits
or operational trend verdict were performed. All four native rotated20 cases
hit their existing1,800-second cap. Last completed sources were BJ37,
mirror29, alternating12 and pivot13 out of230. Their four zero-byte JSONL
files are explicitly `EMPTY_TIMEOUT_OUTPUT_NO_ENDPOINT`; progress logs are
cost evidence, not endpoint certificates. The remaining30 rotated high rows
are pending, not silently omitted or replaced by a source subset.

### G1 fresh-machine recipe — prospective, not a newly executed round

A full-history clone can recover the large own-generated legacy sweep; no
old local output is required. Python/FLINT producer dependencies and the
native C++17/GMP toolchain are separate. Recover the input first:

```sh
python - <<'PYG1INPUT'
from pathlib import Path
import subprocess,hashlib
p=Path('/tmp/padua-g1-fresh-inputs');p.mkdir(parents=True,exist_ok=False)
raw=subprocess.check_output(['git','show','2b52b432fe59c9a50aef9deebe5152c5d6874465:topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json'])
assert len(raw)==616693
assert hashlib.sha256(raw).hexdigest()=='0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'
(p/'e1-full-sweep.json').write_bytes(raw)
PYG1INPUT
python -m pip install --target /tmp/padua-g1-fresh-deps python-flint==0.9.0
PYTHONPATH=/tmp/padua-g1-fresh-deps python -B topics/padua-lanczos-frontier-20261105/code/g1_exact_prefix.py --set triangle --rule bj --max-degree 12 --old-sweep /tmp/padua-g1-fresh-inputs/e1-full-sweep.json --output-dir /tmp/padua-g1-fresh-producer/triangle-bj --receipt /tmp/padua-g1-fresh-producer-triangle-bj.json
python -B topics/padua-lanczos-frontier-20261105/code/g1_independent_run.py --old /tmp/padua-g1-fresh-inputs/e1-full-sweep.json --out /tmp/padua-g1-fresh-native/overlap --degree 12 --workers 4 --timeout 1800 --receipt /tmp/padua-g1-fresh-native/overlap-receipt.json
python -B topics/padua-lanczos-frontier-20261105/code/g1_independent_compare.py --independent /tmp/padua-g1-fresh-native/overlap/triangle-bj-d12.jsonl --producer /tmp/padua-g1-fresh-producer/triangle-bj/endpoints.json --receipt /tmp/padua-g1-fresh-comparison.json
```

Repeat the producer/comparison for both grids and four rules for full overlap.
The native runner compiles using g++/GMP; it imports no FLINT producer mathematics.
Higher-degree commands and their overlap guards are in the case receipts and
[independent G1 report](independent-checks-g1.md). Repeating previously timed-out
rotated20 commands is a prospective cost experiment, not promised completion
or authorization to alter the frozen scan/fit rules.

## G2 exact arrays and portable fixed-certificate check

Developer baseline/impulse arrays, exact partial-R lower values and separate
independent regenerated exact arrays remain external under `g2`. Their
byte identities, actual generator argv/code pins and checker links are in
the complete inventory. The selected stage11/source6 calculations supply
lower certificates for the original global90-source model. R's partial sum
retains denominator `90*M*||X||²`; it is not the full expectation or a
restricted-source law. The saved W/R thresholds and scope are unchanged.

The final independent checker was actually executed for both grids with
`--partial-r --fixed-certificate`, regenerating the baseline and exact closure
responses without opening original producer files. Actual argv, versions,
raw identities and controls are in `evidence/g2-independent-triangle.json`,
`evidence/g2-independent-rotated.json` and
[independent finite L2 report](independent-checks-l1-l2.md). Fixed certificate
SHA-256 is `6bec42971911fb3f86081a13042b6c7029290702c2536c128c0a6f1bf0b746cf`;
checker SHA-256 is
`e88536c7156256de09f907923d7a51437055b685f3ccbaee62fcff4b50589ca8`.

### G2 repository-only recipe — prospective new output locations

The individual independent computations were executed, but this new-directory
recipe is a future rerun, not a claim that these exact locations were used.
It needs only this repository and python-flint0.9.0; no historical bulk input,
polyrat checkout, old receipt paths or original ell arrays are inputs.

```sh
python -m pip install --target /tmp/padua-g2-fresh-deps python-flint==0.9.0
PYTHONPATH=/tmp/padua-g2-fresh-deps python -B topics/padua-lanczos-frontier-20261105/code/g2_independent.py --set triangle --partial-r --fixed-certificate topics/padua-lanczos-frontier-20261105/evidence/g2-fixed-certificate.json --output /tmp/padua-g2-fresh-triangle.json --exact-output /tmp/padua-g2-fresh-triangle-exact.json
PYTHONPATH=/tmp/padua-g2-fresh-deps python -B topics/padua-lanczos-frontier-20261105/code/g2_independent.py --set rotated --partial-r --fixed-certificate topics/padua-lanczos-frontier-20261105/evidence/g2-fixed-certificate.json --output /tmp/padua-g2-fresh-rotated.json --exact-output /tmp/padua-g2-fresh-rotated-exact.json
```

Both scientific predicates are checked afresh against the small committed
fixed lower certificate, independently of future selection of a maximizing
node or retention of old artifacts. This supplies no all-degree or actual
working-precision PD-T055 assertion.

## SH supplemental finite checks — no external raw arrays

The SH reviewer confirmed that all exact arrays stayed in memory. Its
original small committed receipt `evidence/sh-independent.json` is3,684bytes,
SHA-256 `776b97a5e213c0125f49bac2355bc6f4e48dd628b4c21d31cf7a9adc2ec6cbbd`.
The original proof/checker hashes remain in that receipt and the report;
no original external SH raw artifact is invented or copied into this inventory.

After the separately authorized metadata impact check, the reviewer actually
reran the same scientific calculations under current packaging:

```sh
python topics/padua-lanczos-frontier-20261105/code/sh_independent.py --output topics/padua-lanczos-frontier-20261105/evidence/sh-independent-current.json
```

Current proof SHA-256 is
`f27a22c4c6f13d03710750f52eef4dc9bac31f27bd009beaa536866fbbe24d9f`;
current checker SHA-256 is
`db4df9f967e00c5d73168263526365c4d66199ff922b02e58953d046cf2daaba`;
current3,692byte receipt SHA-256 is
`c31e23273316adcc15833076818eb0458c5d473114bfb1236af65506ef31a260`.
These source/receipt anchors and both executed commands are in the external
inventory. See [SH independent report](independent-checks-sh.md) for the
metadata-only change and unchanged scientific scope.

For a **prospective** repository-only external-output rerun, install the
recorded NumPy2.3.5/SymPy1.14.0 dependencies and use an existing output directory:

```sh
python -m pip install --target /tmp/padua-sh-fresh-deps numpy==2.3.5 sympy==1.14.0
PYTHONPATH=/tmp/padua-sh-fresh-deps python topics/padua-lanczos-frontier-20261105/code/sh_independent.py --output /tmp/padua-sh-fresh-check.json
```

The checker guards the matching proof bytes. Its n2–4 exact derivative checks
and through-degree8 symbolic checks supplement the analytic proof; they are
not a finite reduction of the all-degree theorem. Different environment/path
metadata may change the receipt hash. No expensive scientific computation was
performed for this documentation/inventory update itself.
