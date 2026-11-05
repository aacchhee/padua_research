# Cold-storage manifest — topics/programme-ideas-20261031/checks/code/adv/gen4-2

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
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_corner_const.out` | 1390 | `94b1f94f71f505a494df9633b0f456c6915902d1753dee7199da28f0bd3cdb37` | `e9babc1ab0106955c67b0e90c9e6832d6636eb93` |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_corner_fit.out` | 1391 | `9284946029f218fb94ebf61bcbfa2863dc4ed68982030aa50848bc7081d9d1c5` | `e19d8f10a8e80751c91039830da6da59f34abde1` |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_corner_parity.out` | 1828 | `2cc01cf191b6b7724f8d6969bb1c3f560edf87597de0d8530749dc87b365a3bf` | `de121920d77571b1e9646fbdf71de26cb2950b9d` |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_maxima_count.out` | 5595 | `ccce6d0704549549a929d4014ef5189a3ec0cfd9b7ce436e3d8359c41c33b14d` | `89605a5ef8db7d5d91dcc7a830f95c3c087bc5a6` |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_maxima_count2.out` | 4343 | `471d961cadbc15ec619fde42077449f1db4a4f129a5f27be80e4c2c152d57791` | `8616dc8618a6e771b7f4f741fb02fb5c7e443ad9` |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_rhombus_L1.out` | 845 | `43ba2b973aec550a0cd1dc6ed100cfd8f22bed5fdbad08450512f6260e18c764` | `b9976b9fe85ae46b9246edaa5eb56634574603dd` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/programme-ideas-20261031/checks/adversarial-gen4-2.md](../../../../adversarial-gen4-2.md)

Short scientific summaries:
- [topics/programme-ideas-20261031/checks/adversarial-gen4-2.md](../../../../adversarial-gen4-2.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/programme-ideas-20261031/checks/code/adv/gen4-2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_programme-ideas-20261031_checks_code_adv_gen4-2_cold-storage-20261105 --manifest topics/programme-ideas-20261031/checks/code/adv/gen4-2/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/programme-ideas-20261031/checks/code/adv/gen4-2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/programme-ideas-20261031/checks/code/adv/gen4-2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
```

The archive is staged at the actual export directory above. Final migration
results/receipt hashes are in the [migration verification](../../../../../../padua-lebesgue-followups-20261103/preparation/cold-storage-migration.md).
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
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_corner_const.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_corner_fit.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_corner_parity.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_maxima_count.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_maxima_count2.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-2/adv_rhombus_L1.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
