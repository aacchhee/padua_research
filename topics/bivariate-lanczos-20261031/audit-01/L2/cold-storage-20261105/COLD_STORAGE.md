# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-01/L2

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
| `topics/bivariate-lanczos-20261031/audit-01/L2/cycles-rerun.log` | 1314 | `72d3aa36b45910b850c907d7872f6bce20a0a330df3519c923dfb50607c2c588` | `cb3c2750a46fa104ab25f52b9329dfcdef215bbb` |
| `topics/bivariate-lanczos-20261031/audit-01/L2/e3-rerun.log` | 9610 | `7bf9beb6cd869ef22b55a28ca9eebe786ff03fa0856b9f1a13a25d9089f38323` | `63c0427e071cb742796ecbedb0291ee8adb9ef86` |
| `topics/bivariate-lanczos-20261031/audit-01/L2/exact-rerun.log` | 3540 | `673062185efce28f0ba3243bfc463184349a868dd754fec91f950378de40c3be` | `17689d4aa2fbe15a2551acb6e97f690d51520f49` |
| `topics/bivariate-lanczos-20261031/audit-01/L2/independent-drift.log` | 2507 | `654744a99b77d924de01460dddda4208158d6031677077235d7131737d395cb2` | `8072c73904221ba5d5aa813646c49238a84d52c4` |
| `topics/bivariate-lanczos-20261031/audit-01/L2/local-beta.log` | 721 | `cb5eadbf2aaa5a658c548395228877d92ef7153c9e2859b683bf903015ae104b` | `89bd5f3dd3c190a2e8bf473558b8931507f073c5` |
| `topics/bivariate-lanczos-20261031/audit-01/L2/pro-rerun.log` | 5800 | `9daaaf8cb073827c29267de283962ed9072457a31423304216616c97a27769f4` | `9c9ab8d9297651115e245f95be1f142b4fb6fb21` |
| `topics/bivariate-lanczos-20261031/audit-01/L2/proJ-rerun.log` | 13458 | `4040b3006364d7041e56dd8d80d30ffea425c480b42615d09d8516881230577c` | `3e935993dddf3822186af850d2e95f1f719181fc` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/audit-01/L2.md](../../L2.md)
- [topics/bivariate-lanczos-20261031/audit-02/L1.md](../../../audit-02/L1.md)
- [topics/bivariate-lanczos-20261031/directions/L2/response-audit-01.md](../../../directions/L2/response-audit-01.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-01/L2.md](../../L2.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-01/L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-01_L2_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-01/L2/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-01/L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-01/L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-01/L2/cycles-rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L2/e3-rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L2/exact-rerun.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C004 | C004 |
| `topics/bivariate-lanczos-20261031/audit-01/L2/independent-drift.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L2/local-beta.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L2/pro-rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L2/proJ-rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |

### C004

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-02/L1.md:73`,
Git blob `efc1b20b29d96251b0428ecc8cd794f4be7a978b` at retrieval source40347d1.

````text
python3 -I tracks/bivariate-lanczos/code/L1/l1_audit01_exact_checks.py > topics/bivariate-lanczos-20261031/audit-02/L1/developer-exact-rerun.log
````
