# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-01/L3-certificates

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
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/independent_certificate_check.log` | 1645 | `b61807769d4d74e0ff0708accc8e0121dabb177f06c216742fea7419211735b9` | `c4979f74806cc69e4bbb34e8484053af4b9dd1af` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_delta0.log` | 2125 | `4dea16e4b48d6d2eaf8c0e689db28843c8276c5b88ee2ba30ede9704e5702282` | `ea24fd2cbdfbed2c21ec340eba1463edb89fe102` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_family_n3.log` | 286 | `14f6dbedd7b86ec94444d1a1e6a8c2eddf08d19e496d3a5216a99cfcd03a14aa` | `22c60a52142d86308c7742950b29eaac0774b805` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_n3_exact.log` | 3259 | `2c2aded478ad891181e9a35272974ae0ea0099d0318941501e97fcf09d9d61d6` | `0447e32822865dba3854fdb96d2c318aaed23610` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_symbolic.log` | 1130 | `8b6a3b64dc6c992c61a0c8b87248901b734b10aeb878296241191436f5e63886` | `b207bd4550dcff512aa040f34b59ea75e8253331` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_turan.log` | 8082 | `e4086821e7d944e963a981e98244278861cd07ae011e38c321119f503fdee08d` | `0cdeaa5c872163c8a255d3baa96b7af84de51aae` |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_unisolvence.log` | 318 | `a1e21ecb647ce34b747d87e456a7839acb28974cb987c57edc0734e1c9093188` | `f4de059552c1c1dac99584dfc11011ae098f8025` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/audit-01/L3-certificates.md](../../L3-certificates.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-01/L3-certificates.md](../../L3-certificates.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-01/L3-certificates/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-01_L3-certificates_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-01/L3-certificates/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-01/L3-certificates/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-01/L3-certificates/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/independent_certificate_check.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_delta0.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_family_n3.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_n3_exact.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_symbolic.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_turan.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L3-certificates/rerun_unisolvence.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
