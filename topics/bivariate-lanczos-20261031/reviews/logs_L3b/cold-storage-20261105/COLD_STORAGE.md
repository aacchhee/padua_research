# Cold-storage manifest — topics/bivariate-lanczos-20261031/reviews/logs_L3b

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
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/consistency_recheck_rot03.log` | 3033 | `98d62813de39f933a2e2b30c9e7508b35503f5fa3ec1e4950355cf9ee95ee426` | `17d0d6c7bfd3eb689b715314296919f973064f0c` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/consistency_recheck_rot03_n20_22.log` | 1319 | `bcac5a9d01ca60fdc57099e33c97bcaddb9296971eed1b0119cfd613e15feb86` | `cfa245e853b341ac0f09522a757f309df004350e` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/dev_r06_consistency_rot03_rerun.log` | 2117 | `7c9fa7e5a1db8632767721785d755d5661146a6717a079c5e91acedfac032294` | `39c794e41b214f92171a5912e50f3dda30f3ec27` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/equi_H_cert_n1_7.log` | 5791 | `60ad0a149dc2ce66a3b7eb2e5e35d8c01f671d36dbe295d74f5770011cb7f4ac` | `e18dd48e81efd0b5b5eaa07c652c0fc88b468aaf` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/equi_H_cert_n8.log` | 1248 | `ae2467e5c5eb73557987de6b4b6cd031811e98ebeade4a09a790040e2d6c1e27` | `abd23287a5a09feef198ec662426497052aacf66` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/equi_H_cert_negative_control.log` | 3524 | `9194f7af94e2a65cc55c60f93f5e79dd9796ff11d1f8d34976ffcd5aaaf18371` | `b7ea903c5692cfea845408f0e58f2a9598fdba3d` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/kappa_family_n3.log` | 286 | `14f6dbedd7b86ec94444d1a1e6a8c2eddf08d19e496d3a5216a99cfcd03a14aa` | `22c60a52142d86308c7742950b29eaac0774b805` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/padua_delta0.log` | 2168 | `885c063a3db020a4bbb21953c099caee3717143729eb6af799ab2588f0129fd2` | `4414e39eaca556ad82c3b8f39012f513a0173e64` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/padua_turan_check.log` | 8126 | `974b306e604f4f643dc9dde6314c8142708265d4e3807b679292fd88b332413f` | `4002980ba88ccc86c9195befa7dad4c3a545ae7a` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/turan_symbolic.log` | 1172 | `e1170b52e1f7869f04dc1045a375a5316ea9f8086ad531062bc51058438833b2` | `f87461e8dd3fda6232c7098e946d7d864f011323` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/audit-01/L3-framework.md](../../../audit-01/L3-framework.md)
- [topics/bivariate-lanczos-20261031/pr-prep/proof_status.rows.md](../../../pr-prep/proof_status.rows.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-prior-art-01.md](../../L3-prior-art-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md](../../L3-reconstruction-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-02.md](../../L3-reconstruction-02.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/reviews/L3-prior-art-01.md](../../L3-prior-art-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md](../../L3-reconstruction-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-02.md](../../L3-reconstruction-02.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/reviews/logs_L3b/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_reviews_logs_L3b_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/reviews/logs_L3b/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/reviews/logs_L3b/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/reviews/logs_L3b/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/consistency_recheck_rot03.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/consistency_recheck_rot03_n20_22.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/dev_r06_consistency_rot03_rerun.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/equi_H_cert_n1_7.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C008 | C008 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/equi_H_cert_n8.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/equi_H_cert_negative_control.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/kappa_family_n3.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/padua_delta0.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/padua_turan_check.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L3b/turan_symbolic.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |

### C008

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:76`,
Git blob `9cd80e0b73871b639dbbf6c216531d3babb399a2` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/review_L3b/equi_H_cert.py 1 7 40 > topics/bivariate-lanczos-20261031/audit-01/L3-framework/equi_H_cert_n1_7.log 2>&1
````
