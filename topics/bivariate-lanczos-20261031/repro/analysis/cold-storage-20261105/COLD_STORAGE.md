# Cold-storage manifest — topics/bivariate-lanczos-20261031/repro/analysis

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
| `topics/bivariate-lanczos-20261031/repro/analysis/f1_ratio_table_eps.txt` | 5983 | `d331026db2fd3def83b0e1695c104bc632e2c98327c85e676cd6056e40211010` | `60368da2cec096e484bd81d1a747c1d1de64dafd` |
| `topics/bivariate-lanczos-20261031/repro/analysis/f1_ratio_table_halfeps.txt` | 5994 | `962ec1bab460f62e80c87ed10acda3c6ab7d08be69330e5a07be53fa7273395a` | `7cdd22a9bb1e4b084e8f118da19dd79c6823c23b` |
| `topics/bivariate-lanczos-20261031/repro/analysis/f6_deficit_factors.txt` | 5072 | `59f83b81be345b719d9befcaa7116202e2a4cac290cad9829937ca705b04ca3a` | `9657707f6dd78685c70886803039775f769a1856` |
| `topics/bivariate-lanczos-20261031/repro/analysis/f6_slopes_M66_1891.txt` | 6456 | `ab1dcfbe4c566c46dc4731d9cd918bab6c347b297a24541253ed141ba29ef7bf` | `2fcd64c55f82745493d3e28dd102cf7e742b6b78` |
| `topics/bivariate-lanczos-20261031/repro/analysis/f6_slopes_M66_496.txt` | 4878 | `8dbc0186bc6504233673f0b1e9247b6d1cda9c40b9f0dddc45846442f43099d8` | `bb5e8aca3c837288f8966b0d45ce1d3067816b63` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/bivariate-lanczos-20261031/LOG.md](../../../LOG.md)
- [topics/bivariate-lanczos-20261031/audit-01.md](../../../audit-01.md)
- [topics/bivariate-lanczos-20261031/directions/L1/SUMMARY.md](../../../directions/L1/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/directions/L2/SUMMARY.md](../../../directions/L2/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/directions/L3/SUMMARY.md](../../../directions/L3/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/report.md](../../../report.md)
- [topics/bivariate-lanczos-20261031/repro/REPRO.md](../../REPRO.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/bivariate-lanczos-20261031/LOG.md](../../../LOG.md)
- [topics/bivariate-lanczos-20261031/audit-01.md](../../../audit-01.md)
- [topics/bivariate-lanczos-20261031/directions/L1/SUMMARY.md](../../../directions/L1/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/directions/L2/SUMMARY.md](../../../directions/L2/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/directions/L3/SUMMARY.md](../../../directions/L3/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/report.md](../../../report.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/repro/analysis/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_repro_analysis_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/repro/analysis/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/repro/analysis/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/repro/analysis/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/repro/analysis/f1_ratio_table_eps.txt` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/analysis/f1_ratio_table_halfeps.txt` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/analysis/f6_deficit_factors.txt` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/analysis/f6_slopes_M66_1891.txt` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/analysis/f6_slopes_M66_496.txt` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
