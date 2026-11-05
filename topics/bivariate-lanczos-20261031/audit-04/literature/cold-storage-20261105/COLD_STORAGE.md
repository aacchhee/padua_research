# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-04/literature

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
| `topics/bivariate-lanczos-20261031/audit-04/literature/run.log` | 1575 | `55a82ba5692b136470ea38682582bcba2bece78461426cf7821190f53827ab30` | `0a2387dd8432ef49a578e030cba7a5ae164667dd` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/bivariate-lanczos-20261031/LOG.md](../../../LOG.md)
- [topics/bivariate-lanczos-20261031/audit-01/L1-foundations.md](../../../audit-01/L1-foundations.md)
- [topics/bivariate-lanczos-20261031/audit-01/L1-later.md](../../../audit-01/L1-later.md)
- [topics/bivariate-lanczos-20261031/audit-01/L2.md](../../../audit-01/L2.md)
- [topics/bivariate-lanczos-20261031/audit-01/L5.md](../../../audit-01/L5.md)
- [topics/bivariate-lanczos-20261031/audit-01/protocol.md](../../../audit-01/protocol.md)
- [topics/bivariate-lanczos-20261031/audit-02/L1.md](../../../audit-02/L1.md)
- [topics/bivariate-lanczos-20261031/audit-02/L2.md](../../../audit-02/L2.md)
- [topics/bivariate-lanczos-20261031/audit-02/L3-conventions.md](../../../audit-02/L3-conventions.md)
- [topics/bivariate-lanczos-20261031/audit-02/L3-formula-scope.md](../../../audit-02/L3-formula-scope.md)
- [topics/bivariate-lanczos-20261031/audit-04/literature.md](../../literature.md)
- [topics/bivariate-lanczos-20261031/directions/L1/R07.md](../../../directions/L1/R07.md)
- [topics/bivariate-lanczos-20261031/directions/L1/candidates.md](../../../directions/L1/candidates.md)
- [topics/bivariate-lanczos-20261031/directions/L1/response-audit-01.md](../../../directions/L1/response-audit-01.md)
- [topics/bivariate-lanczos-20261031/directions/L1/response-recon-01.md](../../../directions/L1/response-recon-01.md)
- [topics/bivariate-lanczos-20261031/directions/L2/response-audit-01.md](../../../directions/L2/response-audit-01.md)
- [topics/bivariate-lanczos-20261031/pr-prep/proof_status.rows.md](../../../pr-prep/proof_status.rows.md)
- [topics/bivariate-lanczos-20261031/response-01.md](../../../response-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-02.md](../../../reviews/L1-reconstruction-02.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-04/literature.md](../../literature.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-04/literature/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-04_literature_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-04/literature/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-04/literature/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-04/literature/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-04/literature/run.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | C031, C032, C033, C034, C035, C036 | none recovered |

### C031

Status: documented_command_with_placeholders. Source `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:43`,
Git blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6` at retrieval source40347d1.

````text
| `audit-01/L2/dots-rerun.log` | Git blob `b87241029099` at `2b52b432fe59`; AC cold storage PENDING | 56,550 | `6b7076dbdbb97cda44a75bfea7ccb90723996297128714d629de4d0772a202eb` | `2b52b432fe59` | OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L2/l2_r03_dots.py > <out> 2>&1 | committed at source commit | Summary: audit-01/L2.md:110; audit-01/L2/summary.json. Audit rerun. |
````

### C032

Status: documented_command_with_placeholders. Source `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:45`,
Git blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6` at retrieval source40347d1.

````text
| `audit-01/L2/omega-rerun.log` | Git blob `d3140f436061` at `2b52b432fe59`; AC cold storage PENDING | 20,366 | `ed93cd2cdee64f2af3fb724abd47aa7fcb3206e83a58198982882a263222f480` | `2b52b432fe59` | OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L2/l2_r01_omega.py rotpi4 triangle cb_cubic > <out> 2>&1 | committed at source commit | Summary: audit-01/L2.md:108; audit-01/L2/summary.json.  |
````

### C033

Status: documented_command_with_placeholders. Source `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:46`,
Git blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6` at retrieval source40347d1.

````text
| `audit-01/L2/selection-rerun.log` | Git blob `418264e5f6f3` at `2b52b432fe59`; AC cold storage PENDING | 79,426 | `ab0a85b8d6094b722ad462d5d54d7ed1a7d613790014b7f273cc60a3bb108e5b` | `2b52b432fe59` | OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L2/l2_r02_selection.py rotpi4 triangle cb_cubic > <out> 2>&1 | committed at source commit | Summary: audit-01/L2.md:110; audit-01/L2/summary.json.  |
````

### C034

Status: documented_command_with_placeholders. Source `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:47`,
Git blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6` at retrieval source40347d1.

````text
| `audit-01/L2/theorem-A-rerun.log` | Git blob `21b8fc2c2333` at `2b52b432fe59`; AC cold storage PENDING | 27,705 | `664613338df228d2ce16cffb04a3c404a6ef48e8b41ceaa545928b8247556300` | `2b52b432fe59` | OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/review_L2/rl2_thmA.py > <out> 2>&1 | committed at source commit | Summary: audit-01/L2.md:106 (35 instances, no violation, max LHS/RHS 0.1612927041); audit-01/L2/summary.json.  |
````

### C035

Status: documented_command_with_placeholders. Source `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:53`,
Git blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6` at retrieval source40347d1.

````text
| `audit-02/L2/chi-rerun.log` | Git blob `a2e3677b0f2f` at `2b52b432fe59`; AC cold storage PENDING | 350,451 | `d84627ccf92eb754dc36628c0c09579ad48e04ba543f50eb2cef8451f65fad8f` | `2b52b432fe59` | OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L2/l2_audit01_chi.py > <out> 2>&1 | committed at source commit | Summary: audit-02/L2.md:83 (max chi 5.279895783639854); audit-02/L2/summary.json.  |
````

### C036

Status: documented_command_with_placeholders. Source `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:54`,
Git blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6` at retrieval source40347d1.

````text
| `audit-02/L2/ldnorm-rerun.log` | Git blob `741d726fd613` at `2b52b432fe59`; AC cold storage PENDING | 57,215 | `5e021b9400d6d6e6f0c4937d7b987b25021529ce1095d17f135368b1d6ce884e` | `2b52b432fe59` | OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L2/l2_audit01_ldnorm.py > <out> 2>&1 | committed at source commit | Summary: audit-02/L2.md:84; audit-02/L2/summary.json.  |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:94`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py triangle 24 12 integer mp` | `cert_triangle_rerun.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:95`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py square 24 12` | `cert_square_rerun.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:96`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `tracks/bivariate-lanczos/code/review_L1b/rv2_certificate.py square 40 16` | `cert_square40_rerun.log` |
````
