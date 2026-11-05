# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-02/L3-conventions

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
| `topics/bivariate-lanczos-20261031/audit-02/L3-conventions/developer-check-rerun.log` | 1394 | `b829dd853361bf2af7c3bbb9d60b5f31c991bcd6a3fd161cba26eec5419c2039` | `198ab1b9c465ba11d67dc9a4096de5d9bc9b4623` |
| `topics/bivariate-lanczos-20261031/audit-02/L3-conventions/independent-check.log` | 858 | `ae941a44bdec730c72fb614da2f81a894573b5b0a5dc40f1fcfc796284f623a7` | `dccf4df60d7f67dcfad39a59df607f58962aac93` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/audit-02/L3-conventions.md](../../L3-conventions.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-02/L3-conventions.md](../../L3-conventions.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-02/L3-conventions/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-02_L3-conventions_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-02/L3-conventions/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-02/L3-conventions/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-02/L3-conventions/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-02/L3-conventions/developer-check-rerun.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C025 | C025 |
| `topics/bivariate-lanczos-20261031/audit-02/L3-conventions/independent-check.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C026 | C026 |

### C025

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-02/L3-conventions.md:65`,
Git blob `01ab1c274817cc741c6fe8c17361a11615b7353f` at retrieval source40347d1.

````text
python3 -I tracks/bivariate-lanczos/code/L3/t302b_conventions_check.py > topics/bivariate-lanczos-20261031/audit-02/L3-conventions/developer-check-rerun.log 2>&1
````

### C026

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-02/L3-conventions.md:66`,
Git blob `01ab1c274817cc741c6fe8c17361a11615b7353f` at retrieval source40347d1.

````text
python3 -I topics/bivariate-lanczos-20261031/audit-02/L3-conventions/independent_conventions.py > topics/bivariate-lanczos-20261031/audit-02/L3-conventions/independent-check.log 2>&1
````
