# Cold-storage manifest — topics/padua-mz-2d-20261101/audit/claude-audit-01

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
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/check-t110.log` | 61 | `f7e14f332dc0a1061901eee7df25d5a32e0c0f22dad2c1aec530f6968ccceaa2` | `7cf16666ef1be09952bbcd7cd3990c9e3ad53c20` |
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/claude-audit-check.log` | 276 | `eeb36c5a578bccbcc10c74096440a6866cc0bb7eb81617112cceb863bb05cc50` | `475c1bd2b79b45e29ac38f09b6c23bc05d5012b2` |
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/claude-audit-extra.log` | 86 | `bf2f2e8b3cbe01f6fbf51b36bfb0f453928d0e09dde76990b52dba7da04abec5` | `5354ebb0a48deb1131c07ff943c85e9d040b59f2` |
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/claude-m40-cholesky.log` | 378 | `cfd5680c7f9b00842b75b2f6a7060852e53a759607045a477cca04b59a6e3305` | `388da90e062231b8c679a788f8743eee8ee2e589` |
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/dev-indep.log` | 62 | `ec4f39327520e619c5d419756a07b761b6eaab6f820d5c4d0ba72eb9523af80e` | `d693c58b6b78a78d26924a0cff670f43c5d3937b` |
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/exact-run.log` | 128 | `038fbddc6bf9b098a1b42df095caf9b88afc814bf090c2843190b816cf168908` | `342335e5738cced5722118d8c2ffd2959958cbea` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/padua-mz-2d-20261101/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/padua-mz-2d-20261101/LOG.md](../../../LOG.md)
- [topics/padua-mz-2d-20261101/audit-01.md](../../../audit-01.md)
- [topics/padua-mz-2d-20261101/audit/claude-audit-01/MANIFEST.md](../MANIFEST.md)
- [topics/padua-mz-2d-20261101/report.md](../../../report.md)

Short scientific summaries:
- [topics/padua-mz-2d-20261101/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/padua-mz-2d-20261101/LOG.md](../../../LOG.md)
- [topics/padua-mz-2d-20261101/audit-01.md](../../../audit-01.md)
- [topics/padua-mz-2d-20261101/report.md](../../../report.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/padua-mz-2d-20261101/audit/claude-audit-01/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_padua-mz-2d-20261101_audit_claude-audit-01_cold-storage-20261105 --manifest topics/padua-mz-2d-20261101/audit/claude-audit-01/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/padua-mz-2d-20261101/audit/claude-audit-01/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/padua-mz-2d-20261101/audit/claude-audit-01/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/check-t110.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/claude-audit-check.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/claude-audit-extra.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/claude-m40-cholesky.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/dev-indep.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/padua-mz-2d-20261101/audit/claude-audit-01/exact-run.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
