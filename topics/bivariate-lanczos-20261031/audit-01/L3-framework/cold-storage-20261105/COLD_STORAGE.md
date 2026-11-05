# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-01/L3-framework

2026-11-05. AC instructed: “generated outputs should go to cold storage.”
Raw transcripts/generated analysis captures are archived without changing their bytes.
Small essential receipts, scientific summaries, mathematics and all code remain tracked.

Exact retrieval source: pushed `40347d11071c81c1c633a2578cb52325bb92584a`. [Machine manifest](cold-storage.json)
records every path, SHA-256, size and Git blob. The source is a retrieval snapshot,
not a relabelling of historical execution provenance. No artifact was split; this
manifest belongs to an existing logical experiment/audit component.

## Artifact identities

| Repository path | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/closed_form_C1.log` | 850 | `660b29be0170525f2832f3b0db65620f62a42415835cf21bb6cdea1380ebe762` | `b975badfcaf24711577d1552049626244f81d745` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/consistency_random_n40.log` | 3168 | `344a2181bdd2cc039a399f177f82d230bc072f5ff0e76651ed3c3708ca248951` | `f7e033500013398ae31e0c613937e587d600b382` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/consistency_rot03_n18_20.log` | 1274 | `9507d8516b731b35bccff1a83920826a3f418dbff4edc9b2668822d8628456c6` | `9f5e6533fa942804e4b43f960abb0754f1fcffee` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/equi_H_cert_n1_7.log` | 5744 | `a8255a9c428bae43128aa0cdf9ded2942825ef601b7d8d37dc1ca185a9b37be9` | `80eadc05cd86fce27b27c8ff7a757e6e703d03ee` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.log` | 1279 | `d52783c4c28612740baba4a1163027f56a7cd9ad1c97aab3d4ea97ccf2ba7ee6` | `d4bb744c6bf1bd803a57ef629f7ae3b9b128cef2` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/favard_n1_4_seed0.log` | 1005 | `8f58b0c8165e142cb829607ca0e695e696ae2cca657e7bda1a7c2d4e3d0180f9` | `b22fe17d168fe2292809bbbbcc2e6fc687acb186` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/lstsq_sensitivity.log` | 1612 | `2b358febc8157ae1199363bde21d09ddc9e2d32bd4c293e16ca7b5c17a651012` | `da958806e44bba5054e74083ba06fd11e8b4ba1e` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/audit-01/L3-framework.md](../../L3-framework.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-02.md](../../../reviews/L3-reconstruction-02.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-01/L3-framework.md](../../L3-framework.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-01/L3-framework/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-01_L3-framework_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-01/L3-framework/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-01/L3-framework/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-01/L3-framework/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
```

The archive is staged at the actual export directory above. Final migration
results/receipt hashes are in the [migration verification](../../../../padua-lebesgue-followups-20261103/preparation/cold-storage-migration.md).
Source and destination SHA/size verification is required before removing tracked
copies. The receipt describes export-time readback; re-run verify-archive when
relying on the archive later. No Git history is rewritten.

## Retention and physical delivery

Physical delivery to AC’s `Downloads/padua/cold_storage` is **PENDING**;
that destination is not mounted/accessible in this session. The local stage has
no promised retention period and is not a substitute claim of delivery.
Pinned source blobs remain reachable through the pushed branch history; they
provide cloud retrieval if staging is lost. Keep staging while available.
No purge or deletion of historical Git objects is authorized.

## Frozen command records

These are verbatim historical records, not new executions. Direct named-output
invocations are distinguished from partial argv, checker/input mentions and
script/output mappings. Preserve the original record’s working directory,
environment, source revision and placeholders; do not treat an abbreviated
line as a newly reconstructed runnable command. For missing capture details,
exact-byte retrieval from the pinned blob is the supported archival route.

| Artifact | Status | Command record IDs | Direct output IDs |
|---|---|---|---|
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/closed_form_C1.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C005 | C005 |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/consistency_random_n40.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C006 | C006 |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/consistency_rot03_n18_20.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C007 | C007 |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/equi_H_cert_n1_7.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C008 | C008 |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C009 | C009 |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/favard_n1_4_seed0.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C010 | C010 |
| `topics/bivariate-lanczos-20261031/audit-01/L3-framework/lstsq_sensitivity.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C011 | C011 |

### C005

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:97`,
Git blob `9cd80e0b73871b639dbbf6c216531d3babb399a2` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/L3/r02_closed_form_C.py > topics/bivariate-lanczos-20261031/audit-01/L3-framework/closed_form_C1.log 2>&1
````

### C006

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:98`,
Git blob `9cd80e0b73871b639dbbf6c216531d3babb399a2` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/L3/r06_consistency.py random 40 > topics/bivariate-lanczos-20261031/audit-01/L3-framework/consistency_random_n40.log 2>&1
````

### C007

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:99`,
Git blob `9cd80e0b73871b639dbbf6c216531d3babb399a2` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/review_L3b/consistency_recheck.py rot03 18 20 > topics/bivariate-lanczos-20261031/audit-01/L3-framework/consistency_rot03_n18_20.log 2>&1
````

### C008

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:76`,
Git blob `9cd80e0b73871b639dbbf6c216531d3babb399a2` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/review_L3b/equi_H_cert.py 1 7 40 > topics/bivariate-lanczos-20261031/audit-01/L3-framework/equi_H_cert_n1_7.log 2>&1
````

### C009

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:66`,
Git blob `9cd80e0b73871b639dbbf6c216531d3babb399a2` at retrieval source40347d1.

````text
python3 -I topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.py > topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.log 2>&1
````

### C010

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:96`,
Git blob `9cd80e0b73871b639dbbf6c216531d3babb399a2` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/L3/favard_check.py 4 0 > topics/bivariate-lanczos-20261031/audit-01/L3-framework/favard_n1_4_seed0.log 2>&1
````

### C011

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:100`,
Git blob `9cd80e0b73871b639dbbf6c216531d3babb399a2` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I topics/bivariate-lanczos-20261031/audit-01/L3-framework/lstsq_sensitivity.py > topics/bivariate-lanczos-20261031/audit-01/L3-framework/lstsq_sensitivity.log 2>&1
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:21`,
blob `9cd80e0b73871b639dbbf6c216531d3babb399a2`:

````text
An exact counterexample is implemented in [exact_framework_checks.py](L3-framework/exact_framework_checks.py), output [exact_framework_checks.log](L3-framework/exact_framework_checks.log):
````
