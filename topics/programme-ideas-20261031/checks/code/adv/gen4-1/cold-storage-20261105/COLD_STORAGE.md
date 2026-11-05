# Cold-storage manifest — topics/programme-ideas-20261031/checks/code/adv/gen4-1

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
| `topics/programme-ideas-20261031/checks/code/adv/gen4-1/adv_gen4_1_product_structure.out` | 6051 | `87dc47eac8f85468589c3a23239187294a0af71949a0f299497f78fc141b7f8e` | `95669b27bd9417c77684818cc396467524d17a1f` |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-1/adv_gen4_1_scope_extension.out` | 3363 | `d12b86f372947511115d957d07eb079d9d9ef9cdb864e6b3f5ae83e1e8465075` | `39be0d23487c2b257ab89f5e887a0db82295d994` |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-1/rerun_gen4_saturation_n_le_8.out` | 6064 | `a8942edca476f7b3c64e0aa52bf0a0c94c6f7c1c3453c3a3ec0df8736a965f59` | `78614058300de97f330dfc1d8ea517212f0c2078` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/programme-ideas-20261031/checks/adversarial-gen4-1.md](../../../../adversarial-gen4-1.md)

Short scientific summaries:
- [topics/programme-ideas-20261031/checks/adversarial-gen4-1.md](../../../../adversarial-gen4-1.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/programme-ideas-20261031/checks/code/adv/gen4-1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_programme-ideas-20261031_checks_code_adv_gen4-1_cold-storage-20261105 --manifest topics/programme-ideas-20261031/checks/code/adv/gen4-1/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/programme-ideas-20261031/checks/code/adv/gen4-1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/programme-ideas-20261031/checks/code/adv/gen4-1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/programme-ideas-20261031/checks/code/adv/gen4-1/adv_gen4_1_product_structure.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-1/adv_gen4_1_scope_extension.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/adv/gen4-1/rerun_gen4_saturation_n_le_8.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
