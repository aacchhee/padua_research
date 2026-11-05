# Cold-storage manifest — topics/bivariate-lanczos-20261031/repro/logs

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
| `topics/bivariate-lanczos-20261031/repro/logs/bj_window.log` | 284 | `da705f121e9d39f71c2dc6a2eddaf4815a0a91c8a7c71b881b6622d17535701c` | `39bfaee7cf6309545de09c61634276c7a0a60f60` |
| `topics/bivariate-lanczos-20261031/repro/logs/closed_form_H.log` | 2112 | `549dd400c462b80e49ea3ae7fe0baee5c9f0799155901d42d9f5234501a98341` | `8d2fd82bb26d2654f200a17e51c03faa27a7dd07` |
| `topics/bivariate-lanczos-20261031/repro/logs/f1_loss_vs_ritz.log` | 5178 | `be37a83e755817dc7bd8369a485f5af3b08f63d9875414d3c372351bc16d2c0b` | `abd10d0fa2da44c017611d7fbba6cb4895a0de15` |
| `topics/bivariate-lanczos-20261031/repro/logs/f3_qfree_vs_R_downdate.log` | 1325 | `8e2309a5303953bdbbea7ef5b23412ea3d41fc0fb33af05c0a1c6999c8973660` | `10cb0f261a38909a4972635563d6e2bce2507e61` |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_diag_redundant_pivot.log` | 3677 | `2d049b2c17173678317831a28f73bc35ad29c4dbb2dbc88bad0950a8e10ce85a` | `54dc4873593465adda9aa89579ae6240bbb3fde6` |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_givens_vs_hl_deficit.log` | 4016 | `ceabdd895a21b318c08fda628b54e53508bbf13097e3aacfb1b644a598adedaf` | `038794c6ff0becbdf6bb5d1657ef7fcc180d09d2` |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_pivot_threshold_test.log` | 766 | `1ffdfcce9c943d373e06d0cbc096755933715c2b7a8f4e709e0b19f1c9fb129e` | `cba9c4be441645ffa8dd300d727ed3b6625f775e` |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_run_padua_large_20_30.log` | 1084 | `c48e6933f3db2cee4d42db1c31c22d0e4fdd001ebea761e3a393738516e9303b` | `a67d76c08b4cc63772a0e1841101d4cd35168644` |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_run_padua_large_40.log` | 542 | `3d9f29d22577f8b163627350095b6df221a438e55dad64f45a59de312fe91a8d` | `63f4924090777a2a89114fea4315c97c03ca0159` |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_run_padua_large_50.log` | 544 | `9d3a0224bdbc9215c34e904279267b532fff102eeccab599106c59b872cd0f22` | `8037a134cfdc99432faea1a1a048c43949fc0d0b` |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_run_padua_large_60.log` | 544 | `f4c3ff6a4bb173e9ee051cbf728562910dbb761f2f9deabc4c8fad7a1c68efb2` | `ce994df179d2920ba5028a5833b5ce5e91f6eacc` |
| `topics/bivariate-lanczos-20261031/repro/logs/harris_simanek_check.log` | 2863 | `4f5b84c72d73434877d66d26395a0870ca12bf6b2081fa98f99f2e0731f1d761` | `9a02b0cc914199ae8877c133541288b59fd52955` |
| `topics/bivariate-lanczos-20261031/repro/logs/padua_weights_check.log` | 1292 | `a2fe8cd104d19a8d6868faa43708f5a108dcf48378ca8c100e19531a20a3b6da` | `12a682e483d997322f5fc2cccbdfc881e17132b9` |
| `topics/bivariate-lanczos-20261031/repro/logs/qfree_bivariate_downdate.log` | 803 | `2555ee9997386d62a7cea2dad4a44c9dae501c72cd00477573250a0118261493` | `7a0f25d51b48f83e0a5c74df5102dff98496ce15` |
| `topics/bivariate-lanczos-20261031/repro/logs/qfree_vs_conditioning_I_fail.log` | 274 | `af2cbfb78802bde62ab5f5fa5e608a0561a3061cb991973aa73113c5e484fbb8` | `2e5d8d1febda8b6e78f58b41f5e2ec2fd42216db` |
| `topics/bivariate-lanczos-20261031/repro/logs/qfree_vs_conditioning_noI.log` | 490 | `f0fc62523b5058948911e3404a3bb3ed5e93cc8d7438b045bf1b1016d3c1cf8d` | `e31320a1632080640f700b9e6a5a3a21d869076d` |

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
- [topics/bivariate-lanczos-20261031/audit-01.md](../../../audit-01.md)
- [topics/bivariate-lanczos-20261031/directions/L1/SUMMARY.md](../../../directions/L1/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/directions/L2/SUMMARY.md](../../../directions/L2/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/directions/L3/SUMMARY.md](../../../directions/L3/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/report.md](../../../report.md)
- [topics/bivariate-lanczos-20261031/repro/REPRO.md](../../REPRO.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/bivariate-lanczos-20261031/LOG.md](../../../LOG.md)
- [topics/bivariate-lanczos-20261031/audit-01.md](../../../audit-01.md)
- [topics/bivariate-lanczos-20261031/directions/L1/SUMMARY.md](../../../directions/L1/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/directions/L2/SUMMARY.md](../../../directions/L2/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/directions/L3/SUMMARY.md](../../../directions/L3/SUMMARY.md)
- [topics/bivariate-lanczos-20261031/report.md](../../../report.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/repro/logs/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_repro_logs_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/repro/logs/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/repro/logs/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/repro/logs/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/repro/logs/bj_window.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/closed_form_H.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/f1_loss_vs_ritz.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/f3_qfree_vs_R_downdate.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_diag_redundant_pivot.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_givens_vs_hl_deficit.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_pivot_threshold_test.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_run_padua_large_20_30.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_run_padua_large_40.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_run_padua_large_50.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/f6_run_padua_large_60.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | C074 | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/harris_simanek_check.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/padua_weights_check.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/qfree_bivariate_downdate.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/qfree_vs_conditioning_I_fail.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/repro/logs/qfree_vs_conditioning_noI.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |

### C074

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/repro/REPRO.md:62`,
Git blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc` at retrieval source40347d1.

````text
| X60 | `f6_run_padua_large.py 60` (M = 1891) | 0 | 1726.8 s (of the 1800 s timeout) | `logs/f6_run_padua_large_60.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:43`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 4 | `bj_window.py` | none | 0 | <0.1 s | `logs/bj_window.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:41`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 2 | `closed_form_H.py` | none (deterministic); n in 5, 6, 20, 41. Imports `padua_weights_check`, whose top-level code also runs (n = 6, 20, 60 output at the head of the log) | 0 | 2.6 s | `logs/closed_form_H.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:40`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 1 | `f1_loss_vs_ritz.py` | `default_rng(0)`, one generator drawn in order: random 625, 2500 (n=24), then 1681, 6724 (n=40); tensor grids deterministic; weights = 1 | 0 | 44.7 s | `logs/f1_loss_vs_ritz.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:49`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 10 | `f3_qfree_vs_R_downdate.py` | seeds 0 and 1 per scenario | 0 | 33.3 s | `logs/f3_qfree_vs_R_downdate.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:47`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 8 | `f6_diag_redundant_pivot.py` | `default_rng(2)`; n = 6, 10, 14, 20, uniform and random weights | 0 | 6.3 s | `logs/f6_diag_redundant_pivot.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:45`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 6 | `f6_givens_vs_hl_deficit.py` (default sizes 10 20 30) | `default_rng(1)`: sanity 15 points, then random permutations, then random node sets M = 105, 300, 496 | 0 | 138.2 s | `logs/f6_givens_vs_hl_deficit.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:48`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 9 | `f6_pivot_threshold_test.py` | `default_rng(2)`; n = 20, 30; given order only | 0 | 104.2 s | `logs/f6_pivot_threshold_test.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:46`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 7 | `f6_run_padua_large.py 20 30` | `default_rng(2)`, fresh per invocation; per n: given and one random permutation, then random weights U(0.1,1) | 0 | 56.0 s | `logs/f6_run_padua_large_20_30.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:60`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| X40 | `f6_run_padua_large.py 40` (M = 861) | 0 | 191.4 s | `logs/f6_run_padua_large_40.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:61`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| X50 | `f6_run_padua_large.py 50` (M = 1326) | 0 | 546.1 s | `logs/f6_run_padua_large_50.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:42`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 3 | `harris_simanek_check.py` | `default_rng(0)`, m = 6, 15, 30 in order | 0 | 2.1 s | `logs/harris_simanek_check.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:44`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 5 | `padua_weights_check.py` | none | 0 | 2.4 s | `logs/padua_weights_check.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/repro/REPRO.md:50`,
blob `0a110b6e8a9dd50f56ded615a2b30f4f9e7ce3fc`:

````text
| 11 | `qfree_bivariate_downdate.py` | module-level `default_rng(0)`, consumed over six cases in order | 0 | 8.5 s | `logs/qfree_bivariate_downdate.log` |
````
