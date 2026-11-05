# Cold-storage manifest — topics/padua-lebesgue-followups-20261103/audit-support/claude-audit-01

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
| `topics/padua-lebesgue-followups-20261103/audit-support/claude-audit-01/boundary-regeneration.log` | 1019 | `3d13d4bff0089cb248bb2ddc3c0c8bee9bf0e86d2b8a2ea70f7ce9e5b0ba41d3` | `e8d794f5fc1b3630e6d433149ba35bb36a6c5a39` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/padua-lebesgue-followups-20261103/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/padua-lebesgue-followups-20261103/LOG.md](../../../LOG.md)
- [topics/padua-lebesgue-followups-20261103/audit-01.md](../../../audit-01.md)
- [topics/padua-lebesgue-followups-20261103/audit-support/claude-audit-01/README.md](../README.md)
- [topics/padua-lebesgue-followups-20261103/report.md](../../../report.md)

Short scientific summaries:
- [topics/padua-lebesgue-followups-20261103/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/padua-lebesgue-followups-20261103/LOG.md](../../../LOG.md)
- [topics/padua-lebesgue-followups-20261103/audit-01.md](../../../audit-01.md)
- [topics/padua-lebesgue-followups-20261103/report.md](../../../report.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/padua-lebesgue-followups-20261103/audit-support/claude-audit-01/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_padua-lebesgue-followups-20261103_audit-support_claude-audit-01_cold-storage-20261105 --manifest topics/padua-lebesgue-followups-20261103/audit-support/claude-audit-01/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/padua-lebesgue-followups-20261103/audit-support/claude-audit-01/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/padua-lebesgue-followups-20261103/audit-support/claude-audit-01/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
```

The archive is staged at the actual export directory above. Final migration
results/receipt hashes are in the [migration verification](../../../preparation/cold-storage-migration.md).
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
| `topics/padua-lebesgue-followups-20261103/audit-support/claude-audit-01/boundary-regeneration.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | C123-boundary | none recovered |

### C123-boundary

Status: documented_actual_generator_invocation; raw stdout redirection not recorded. Source `topics/padua-lebesgue-followups-20261103/audit-support/claude-audit-01/README.md:9`,
Git blob `a2911979d4eaa4aa213dd60805c8341a4a82d24d` at retrieval source40347d1.

````text
PYTHONPATH=<deps> timeout 9000 python3 -B topics/padua-lebesgue-followups-20261103/code/t1_boundary.py --output audit/t1/boundary-claude.json
````
