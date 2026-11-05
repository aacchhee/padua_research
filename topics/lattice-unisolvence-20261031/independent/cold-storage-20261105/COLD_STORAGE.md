# Cold-storage manifest — topics/lattice-unisolvence-20261031/independent

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
| `topics/lattice-unisolvence-20261031/independent/c1-extension-rerun.log` | 9355 | `f4fe4dd9af3ce030d968339b895d1fbd2b09684fe30913f2949d1c1fa0105d4a` | `cfa2fdb96f3fb0ba988439a5b7273c2791a3c4d6` |
| `topics/lattice-unisolvence-20261031/independent/c1-gram-rerun.log` | 4147 | `7c74b77e017200915872b279f95bbd793a5070923fa95147e23aa23343d2cf0a` | `16c570a583d0d4474ad1781d0fc86c8b13d025be` |
| `topics/lattice-unisolvence-20261031/independent/c1-rerun.log` | 5077 | `7508e050d2241b52185d2cabb957cad4095030a93fdb48540d7160d531a09306` | `076c734f89b2c23777849e598807f48966a35570` |
| `topics/lattice-unisolvence-20261031/independent/c1-symbolic-rerun.log` | 1479 | `87c1f345cb8d1882796ff87cf235d198bfe370861914d208cf352da7fc87e036` | `30773b78f2a176fc73488ec0f77e5556de0b9288` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/lattice-unisolvence-20261031/COLD_STORAGE.md](../../COLD_STORAGE.md)
- [topics/lattice-unisolvence-20261031/LOG.md](../../LOG.md)
- [topics/lattice-unisolvence-20261031/audit-01.md](../../audit-01.md)
- [topics/lattice-unisolvence-20261031/independent/report.md](../report.md)
- [topics/lattice-unisolvence-20261031/protocol/report.md](../../protocol/report.md)
- [topics/lattice-unisolvence-20261031/report.md](../../report.md)
- [topics/lattice-unisolvence-20261031/response-review/report.md](../../response-review/report.md)

Short scientific summaries:
- [topics/lattice-unisolvence-20261031/COLD_STORAGE.md](../../COLD_STORAGE.md)
- [topics/lattice-unisolvence-20261031/LOG.md](../../LOG.md)
- [topics/lattice-unisolvence-20261031/audit-01.md](../../audit-01.md)
- [topics/lattice-unisolvence-20261031/independent/report.md](../report.md)
- [topics/lattice-unisolvence-20261031/protocol/report.md](../../protocol/report.md)
- [topics/lattice-unisolvence-20261031/report.md](../../report.md)
- [topics/lattice-unisolvence-20261031/response-review/report.md](../../response-review/report.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/lattice-unisolvence-20261031/independent/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_lattice-unisolvence-20261031_independent_cold-storage-20261105 --manifest topics/lattice-unisolvence-20261031/independent/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/lattice-unisolvence-20261031/independent/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/lattice-unisolvence-20261031/independent/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
```

The archive is staged at the actual export directory above. Final migration
results/receipt hashes are in the [migration verification](../../../padua-lebesgue-followups-20261103/preparation/cold-storage-migration.md).
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
| `topics/lattice-unisolvence-20261031/independent/c1-extension-rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/lattice-unisolvence-20261031/independent/c1-gram-rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/lattice-unisolvence-20261031/independent/c1-rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/lattice-unisolvence-20261031/independent/c1-symbolic-rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
