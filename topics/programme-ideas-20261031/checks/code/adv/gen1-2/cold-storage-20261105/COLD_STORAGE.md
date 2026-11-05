# Cold-storage manifest — topics/programme-ideas-20261031/checks/code/adv/gen1-2

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
| `topics/programme-ideas-20261031/checks/code/adv/gen1-2/ah_breakdown_exact.out` | 4575 | `4e9283e8fd4a767a92a7da4191ee898a6ac5b61a678f8cb3e6cd0a63fcdd60ca` | `94f6fdf64ce11f465c17b2a873c1430a071f9c9a` |
| `topics/programme-ideas-20261031/checks/code/adv/gen1-2/qs_rank.out` | 1128 | `47cbf5523a7c8db7cf489d5bd725707da832666b1517fdbf99a07122bb6f72f7` | `810dfefe5e9af420ae5a3f68d1e984232049511a` |
| `topics/programme-ideas-20261031/checks/code/adv/gen1-2/sobolev_adv.out` | 4359 | `fcfb5b3634d6747fa30b5d50fc71ef1aad83018d88dc79bd468b0f3fa5a454bf` | `2c60a51a6fe640f90573dff9bbf83f48f85c13e1` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/programme-ideas-20261031/checks/adversarial-gen1-2.md](../../../../adversarial-gen1-2.md)

Short scientific summaries:
- [topics/programme-ideas-20261031/checks/adversarial-gen1-2.md](../../../../adversarial-gen1-2.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/programme-ideas-20261031/checks/code/adv/gen1-2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_programme-ideas-20261031_checks_code_adv_gen1-2_cold-storage-20261105 --manifest topics/programme-ideas-20261031/checks/code/adv/gen1-2/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/programme-ideas-20261031/checks/code/adv/gen1-2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/programme-ideas-20261031/checks/code/adv/gen1-2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/programme-ideas-20261031/checks/code/adv/gen1-2/ah_breakdown_exact.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/adv/gen1-2/qs_rank.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/adv/gen1-2/sobolev_adv.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
