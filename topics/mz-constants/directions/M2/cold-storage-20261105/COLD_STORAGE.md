# Cold-storage manifest — topics/mz-constants/directions/M2

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
| `topics/mz-constants/directions/M2/developer-run.jsonl` | 3701 | `df076812f88c19e8e6a71b58ac1eb46cacb506541cccd09a92441fd9356ae6a8` | `ceeb125fbf68b7636a24880355544ab6529796d4` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/mz-constants/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/mz-constants/LOG.md](../../../LOG.md)
- [topics/mz-constants/audit-01.md](../../../audit-01.md)
- [topics/mz-constants/directions/M2/LOG.md](../LOG.md)
- [topics/mz-constants/directions/M2/candidates.md](../candidates.md)
- [topics/mz-constants/report.md](../../../report.md)

Short scientific summaries:
- [topics/mz-constants/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/mz-constants/LOG.md](../../../LOG.md)
- [topics/mz-constants/audit-01.md](../../../audit-01.md)
- [topics/mz-constants/directions/M2/LOG.md](../LOG.md)
- [topics/mz-constants/report.md](../../../report.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/mz-constants/directions/M2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_mz-constants_directions_M2_cold-storage-20261105 --manifest topics/mz-constants/directions/M2/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/mz-constants/directions/M2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/mz-constants/directions/M2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/mz-constants/directions/M2/developer-run.jsonl` | Recorded output invocation; preserve original cwd/env/placeholders. | C098 | C098 |

### C098

Status: exact_named_output_command. Source `topics/mz-constants/directions/M2/LOG.md:24`,
Git blob `4b73a10dea8446eb219dd245c898bd20a427fd99` at retrieval source40347d1.

````text
python tracks/mz-constants/code/m2_endpoint.py --exact 512 --measure 8 16 32 64 128 256 512 1024 > topics/mz-constants/directions/M2/developer-run.jsonl
````
