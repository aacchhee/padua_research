# Cold-storage manifest — topics/bivariate-lanczos-20261031/directions/L2

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
| `topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_staircase.raw` | 3096 | `6d0a1e28ee1cd988c7841e2cec93dc3f23327374b2087318841818c475246a02` | `c3144a66af19f9a8a2965df0695f01cc4f4ee74d` |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r01_omega_e3.raw.gz` | 12410 | `b4dfb940b96cc8c4f98a82ab62dd0e491273f1cc47f9362e63c71b950f5551cf` | `24f6973084d4a44bd370fbc71fff5e82932d0cd6` |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r01_sections_w2.raw.gz` | 16262 | `106495bc78f855c4f191106b11e13f75cf0039c87893a53450669cf2f7180e89` | `9c800bee33bdb88db9aaa16a759b9a825ccdeb02` |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r02_cost.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r02_cost.jsonl` | 12325 | `1a0973626c00e7c1a960c98fda0e5eaa95c218a2841ee5806309548943de0dd5` | `bc90d6fc07f1b875a9534c5afcd0c329958d7701` |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r02_pro.raw.gz` | 10315 | `b5b6a38edd004b361be2e4d369c2a443ae7232b8678a8b67ed0714d1e97577c3` | `969977a6e016437e0d41aa774683368b0effaa1f` |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r02_proJ.raw.gz` | 9961 | `4609986b6d431201cddba95c527c5ec6bb969582f116e1b9b7f0d7d33029d14c` | `20ddb01c1f652f047db7a0414bb7c923d882b154` |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r03_dots.raw.gz` | 12650 | `d89f16804afda084fbb9ce8a75746d965887f1f8be430cd068bd8029937581d2` | `843253852c4e8af5cdbb3b680e46be220cd5d781` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/directions/L2/R01.md](../R01.md)
- [topics/bivariate-lanczos-20261031/directions/L2/R02.md](../R02.md)
- [topics/bivariate-lanczos-20261031/directions/L2/R03.md](../R03.md)
- [topics/bivariate-lanczos-20261031/directions/L2/STATUS.md](../STATUS.md)
- [topics/bivariate-lanczos-20261031/directions/L2/SUMMARY.md](../SUMMARY.md)
- [topics/bivariate-lanczos-20261031/directions/L2/candidates.md](../candidates.md)
- [topics/bivariate-lanczos-20261031/directions/L2/response-audit-01.md](../response-audit-01.md)
- [topics/bivariate-lanczos-20261031/directions/L2/response-recon-01.md](../response-recon-01.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/directions/L2/R01.md](../R01.md)
- [topics/bivariate-lanczos-20261031/directions/L2/R02.md](../R02.md)
- [topics/bivariate-lanczos-20261031/directions/L2/R03.md](../R03.md)
- [topics/bivariate-lanczos-20261031/directions/L2/STATUS.md](../STATUS.md)
- [topics/bivariate-lanczos-20261031/directions/L2/SUMMARY.md](../SUMMARY.md)
- [topics/bivariate-lanczos-20261031/directions/L2/candidates.md](../candidates.md)
- [topics/bivariate-lanczos-20261031/directions/L2/response-audit-01.md](../response-audit-01.md)
- [topics/bivariate-lanczos-20261031/directions/L2/response-recon-01.md](../response-recon-01.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/directions/L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_directions_L2_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/directions/L2/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/directions/L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/directions/L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_staircase.raw` | Recorded output invocation; preserve original cwd/env/placeholders. | C063 | C063 |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r01_omega_e3.raw.gz` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r01_sections_w2.raw.gz` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r02_cost.err` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r02_cost.jsonl` | Recorded output invocation; preserve original cwd/env/placeholders. | C064 | C064 |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r02_pro.raw.gz` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r02_proJ.raw.gz` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/directions/L2/logs/r03_dots.raw.gz` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |

### C063

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/directions/L2/response-audit-01.md:75`,
Git blob `1b5072e7a3be5f33326e13bfe6d77d31a75c0c63` at retrieval source40347d1.

````text
cd tracks/bivariate-lanczos/code/L2 && python3 -I l2_audit01_staircase.py > ../../../../topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_staircase.raw
````

### C064

Status: documented_command_with_placeholders. Source `topics/bivariate-lanczos-20261031/directions/L2/R02.md:47`,
Git blob `c1a32c7e0ecdc33983b5ad176073e0c9d1de9bf2` at retrieval source40347d1.

````text
OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 python3 -I l2_r02_cost.py --sets rotpi4,triangle --M 1681,10000,100000 > …/L2/logs/r02_cost.jsonl   # ≈ 6 min
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/directions/L2/response-audit-01.md:71`,
blob `1b5072e7a3be5f33326e13bfe6d77d31a75c0c63`:

````text
**Files changed:** T202, T205, new T208, new T209, N201, N203, N204, T206, T207, `SPLITS.md`, R02, STATUS, SUMMARY; new `code/L2/l2_audit01_staircase.py`, log `logs/audit01_staircase.raw`.
````
