# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-01

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
| `topics/bivariate-lanczos-20261031/audit-01/root-framework-rerun.log` | 1279 | `d52783c4c28612740baba4a1163027f56a7cd9ad1c97aab3d4ea97ccf2ba7ee6` | `d4bb744c6bf1bd803a57ef629f7ae3b9b128cef2` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/LOG.md](../../LOG.md)
- [topics/bivariate-lanczos-20261031/audit-01.md](../../audit-01.md)
- [topics/bivariate-lanczos-20261031/audit-01/protocol.md](../protocol.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-01.md](../../audit-01.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-01/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-01_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-01/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-01/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-01/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-01/root-framework-rerun.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C001 | C001 |

### C001

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/protocol.md:45`,
Git blob `431f079e9e99a1132e4399aef3c38d41d7008eeb` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 python topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.py > topics/bivariate-lanczos-20261031/audit-01/root-framework-rerun.log
````
