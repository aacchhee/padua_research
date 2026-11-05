# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-01/L1-foundations

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
| `topics/bivariate-lanczos-20261031/audit-01/L1-foundations/independent_exact.log` | 1086 | `679164554b7018a1f6a0e4f874669b90c6584ca08003a510bf5033eb804e95ad` | `66ab1ef79279271ddb94dbf2e14e6d4c8f84d190` |
| `topics/bivariate-lanczos-20261031/audit-01/L1-foundations/reviewer_exact_rerun.log` | 4550 | `01b6a329bd09f4ed329ac3a99716e3366e84e2417a72b5d9a21698c2f730e1e0` | `a010d828fc658fe9e81d01fb6aafc1e843a226ae` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/audit-01/L1-foundations.md](../../L1-foundations.md)
- [topics/bivariate-lanczos-20261031/directions/L1/response-audit-01.md](../../../directions/L1/response-audit-01.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-01/L1-foundations.md](../../L1-foundations.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-01/L1-foundations/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-01_L1-foundations_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-01/L1-foundations/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-01/L1-foundations/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-01/L1-foundations/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-01/L1-foundations/independent_exact.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C002 | C002 |
| `topics/bivariate-lanczos-20261031/audit-01/L1-foundations/reviewer_exact_rerun.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C003 | C003 |

### C002

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L1-foundations.md:76`,
Git blob `394d35d2f63008adba3a18e4ab07fbdd23f1c7ff` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I topics/bivariate-lanczos-20261031/audit-01/L1-foundations/check_foundations.py > topics/bivariate-lanczos-20261031/audit-01/L1-foundations/independent_exact.log 2>&1
````

### C003

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L1-foundations.md:75`,
Git blob `394d35d2f63008adba3a18e4ab07fbdd23f1c7ff` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I -u tracks/bivariate-lanczos/code/review_L1/rv_exact_checks.py > topics/bivariate-lanczos-20261031/audit-01/L1-foundations/reviewer_exact_rerun.log 2>&1
````
