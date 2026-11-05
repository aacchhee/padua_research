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

## Handoff04 extension

[cold-storage-04.json](cold-storage-04.json) indexes one complete external inventory of the new G1 optimized runs, G3 n3 pilot and independent checks, and G4 replay/attribution arrays. The old index and its historical59-file retrieval pin are preserved unchanged. Run `python -B topics/padua-lanczos-frontier-20261105/code/storage_inventory_04.py` to rebuild the current local inventory and `--check` to verify every retained byte identity. This reads/hashes files only; it does not rerun science. Rebuilt logs, paths and output metadata need not reproduce historical inventory bytes.

Exact executed commands/code pins/input identities and checker outcomes are in g1-optimization.md, independent-checks-g1-04.md, g3-methods.md, independent-checks-g3-04.md, g4-methods.md and independent-checks-frontier-04.md, with compact per-run receipts. G3 essential lower/upper certificates are committed; its independent checker reconstructs the full kernel, exact jets/distances/signs/dependence rather than trusting proposer summaries. G4 independent arithmetic uses stored Q/H arrays from actual developer algorithm executions; a fresh session first regenerates those arrays with the documented fixed-input workers, then executes the independent reference/residual checker. No original historic Q/H is claimed available. All full arrays and the new complete raw inventory remain outside Git; no Windows archival or sandbox retention is promised.

## Growing file-identity inventory

The evidence-manifest.json file is now a small content-addressed index for the full per-file inventory outside Git. `python -B topics/padua-lanczos-frontier-20261105/code/check_manifest.py` reconstructs every canonical filename/size/SHA256 row directly from the repository and verifies the complete digest and file count. It does not require the temporary inventory to survive. `--write --rules <rules-SHA>` publishes an updated index only after registering the intended files with Git; `--cached` reads staged bytes for an intermediate checkpoint. Earlier per-file lists remain retrievable from prior commits. This changes only inventory representation, not mathematical checking or archival status.

## Handoff05 extension and repository-only acceptance

The handoff05 raw index is built after active jobs stop by `code/storage_inventory_05.py`; its one complete per-file inventory remains outside Git and the small `cold-storage-05.json` carries its identity. The helper reads and hashes files only. The linked methods and actual receipts distinguish source-pinned completed commands, partial/capped outcomes and future fresh-directory recipes. Physical delivery to Windows remains pending; temporary retention is not guaranteed. The older indices and historic cost failures remain unchanged.

The new n4/n5 lower certificates are small committed inputs. Their distinct `g3_n4_independent.py` and `g3_n5_independent.py` checkers reconstruct full exact nodes, kernels, polynomial jets and whole-ball Taylor inequalities without original LP output. The executed commands and negative controls are in `independent-checks-g3-05.md` and `independent-checks-g3-06.md`; substituting fresh output paths is a prospective rerun. Failed/capped upper searches are not acceptance dependencies for these lower statements. The n4 scaling diagnostic is separately measured and remains inconclusive.

The actual n1 result has a complete losslessly packed committed word/state trace, an exact interpretation and a separate integer-word checker. `l6_n1_independent.py` reconstructs the frozen computation and checks that certificate without temporary raw traces; see `l6-n1-methods.md` and `independent-checks-frontier-05.md`. The uncompressed trace identity is retained, but no old temporary path is needed to verify the finite raw-data obstruction.

L7 arrays are regenerated by the source-pinned repository/third-party commands in `l7-suite-methods.md` before applying `l7_independent.py`; the original saved samples, seed/code identities, accepted and rejected reference cases remain explicit. Small receipts preserve actual execution provenance, not an assertion that a future rerun reproduces timing or serialized archive headers. Its interpretation remains finite measured end-to-end behavior.

G1 batched/extended/remaining methods and `independent-checks-g1-05.md` record all source and old-input pins, exact overlap checks, scheduling successors, native cases and producer cases. The historical T24 comparison may be reused by identity; a derived fit-acceptance link is not a new scientific execution. Real fitting remains subject to the complete152-row guard, whose actual outcome is recorded in `g1-fit-methods.md` and `independent-checks-g1-fit.md`. Report/tree artifacts stay outside Git; future missing scratch calls for a newly recorded regeneration, never an invented recovery of old timed evidence.

The final handoff05 index is [cold-storage-05.json](cold-storage-05.json):570 retained artifacts in14 groups; complete external inventory90836bytes,SHA256 `f667850c82c56b9fca214673cdbfd2bc5e9c48cf4cb3aa6bcb1ab1b380bcecc4`. Both builder and `--check` actually execute, and every retained artifact matches. These are identity checks, not scientific reruns. Actual G1 fitting and its distinct check now complete with both finite interval verdicts INCONCLUSIVE; the manifest's creation-time NOT_RUN field remains preserved and is superseded by the actual-run records. Four small T24 case-acceptance links are provenance links to one prior actual comparison, not four new executions.

## 2026-11-05 — response-01 retrievability, platform and bounded recipes

Audit A-m7 / PROT-10 correctly distinguishes identity from retrievability. The earlier three indices identify local-only raw files/inventories; a fresh cloud session may have none of them, and no Windows delivery took place. An inventory hash alone is not a remotely retrievable artifact. The compact additions below close the bounded G1 verdict-checking gap while leaving raw choices, exact endpoint rows, full fit diagnostics and trajectories subject to retrieval or newly recorded regeneration.

- Complete per-grid76-row outward log-endpoint tables are committed as [g1-compact-triangle.json](evidence/g1-compact-triangle.json) (9585bytes,SHA256 `2c99758edf1888f2cdd8a0fcd7563512a1466407bb6659f630d7838abad37f38`) and [g1-compact-rotated.json](evidence/g1-compact-rotated.json) (9692bytes, `e52d8ac85956210b984773d1c805199e758ff537239a4926801e23146431f5f8`). Each is one complete scientific grid/four-rule object, not a split of a large raw file. `python -B topics/padua-lanczos-frontier-20261105/code/g1_compact_check.py` needs only the repository and Python standard library. It encloses the ORIGINAL exact endpoint-defined admissible corner and certifies both INCONCLUSIVE outcomes; it does not merely select a point in an enlarged rounded box or authenticate/regenerate the exact rational source endpoints. The source pins and rounding reduction are in [evidence-response-01.md](evidence-response-01.md).
- [l7-full-loss-list.json](evidence/l7-full-loss-list.json) preserves all20 Haswell loss rows, the actual original aggregate identity and aggregator SHA256 `e6fe858208a36206a7bcf9a4e81412fd3b8920cd45dfde5835a26a3c8c363a01`; [l7-cross-group.json](evidence/l7-cross-group.json) preserves six additional cross-group directions. The within-group restriction was post-registration. All original algorithms/fitting criteria remain frozen.
- L7 numerical regeneration must set `OPENBLAS_CORETYPE=Haswell OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` with the pinned NumPy2.3.5/SciPy1.17.0 and polyrat sources from l7-suite-methods.md. The audit confirms20 losses/six within-group directions on Haswell and18/nine on default AVX-512. References, triangle24-only losses, absence of entire-function loss, pair location and exact own/L2 agreement are robust across those runs; specific cells/pairs are platform-dependent. Original CPU model/ISA were not recorded and cannot be invented. [response-numerical-environment.json](evidence/response-numerical-environment.json) separately observes the current response environment (AMD EPYC7763, exposed ISA, glibc2.41 and Haswell OpenBLAS0.3.30); it is not a recovered historical CPU receipt. Future numerical receipts record actual CPU/ISA/BLAS dispatch and core-type selection before work, using code/numerical_environment.py or equivalent.
- The repository-only non-overwriting n1 recipe is in [l6-n1-methods.md](l6-n1-methods.md#repository-only-non-overwriting-checker-recipe--2026-11-05). It stages the three committed compact inputs under the checker-required names in fresh scratch and sends its receipt to scratch. Root actually validates that recipe once in `/tmp/padua-l6-response-recheck.KLTHWlF1`:367 operations, full64u residual budgets PASS, raw branch INCONSISTENT, five corruption controls rejected, elapsed0.125899961s. The new [response-n1-recheck.json](evidence/response-n1-recheck.json) is4378bytes,SHA256 `c683aaf8ff20b190cd0b4c165bdc69ad6c4cae983acca1d1bf0ec0ff6d5fb65c`; the original receipt/source/contract is unchanged and no committed evidence was overwritten.

[cold-storage-response-01.json](cold-storage-response-01.json) indexes one external complete inventory of11 new scratch artifacts (the n1 recipe run and compact packaging replay). `code/storage_response_inventory.py --check` actually verifies all11. This is identity-only work, not another science run. Rebuild/check commands and source identity are in the small index. Earlier indices and audit files remain unchanged. Physical archival and vanished original inputs remain unresolved retention limits, not hidden acceptance claims.

## 2026-11-05 — preparation provenance addendum

`storage_response_inventory.py --check` only checks retained identities. Running the builder **without `--check` rewrites the committed cold-storage-response-01.json index** and its local complete inventory; use the documented actual roots only when intentionally preparing an updated inventory, then review the diff. The earlier recipe remains execution history. Future numerical receipts should capture both default and forced BLAS dispatch where practical, labelling which environment actually ran the research. No new numerical run is made for this preparation. R2-EVD-3 is accepted as a future metadata refinement, R2-EVD-4 is addressed by this warning.


## Audited preparation working outputs — 2026-11-05

The preparation reservation scanner saves full Git-file snapshots and the complete per-copy manifest under `/tmp/padua-lanczos-frontier-preparation/`. [preparation/allocation-scan.json](preparation/allocation-scan.json) supplies the complete external manifest identity plus every unique Git path/blob/hash/size, pinned head and replay code. Regenerate with `python -B topics/padua-lanczos-frontier-20261105/preparation/scan_allocations.py` from a clone retaining those commits; it rewrites its compact receipt, so use a disposable checkout when verifying historical pins. [peer-head-recheck.json](preparation/peer-head-recheck.json) preserves the latest fifteen-file byte comparison separately.

[preparation/integration-receipt.json](preparation/integration-receipt.json) records the actual checkpoint squash/tree/cleanup checks and raw log locator. The committed `preparation/rehearse_integration.py` repeats only mechanical Git integration in a fresh owned worktree, with full input SHAs and a new output path; it never commits or mutates main. Final exact-output rehearsal details are in handoff11. Full logs and the previous application receipt are temporary conveniences; final registry reconstruction depends on committed base/proposal/map and the current receipt, and the tree comparison depends on Git objects. Local retention and physical Windows archival are not promised. No scientific computation was rerun.
