# Cold-storage manifest — topics/bivariate-lanczos-20261031/reviews/logs_L1b

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
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_Q24.log` | 1512 | `ef2d488e1efd077e915834b4106f68ebea2a9127776e94dde0c0f0005e07a0b6` | `09ba59da7fae1162b7946e2f710fa94c4661d84a` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_Q24_exactcmp.log` | 1566 | `0ae5caa495afa70d3dbdb568e6e9bb987b2c7fa4eb6d5dd31ddae0375a65e555` | `540f892918a403be8024e0425bd862d268b10d02` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_T24.log` | 1516 | `ff3ffe54e2ecaa601af2031d817fab8b06e133e053bffb0545d21001af0aecdf` | `8a76dcdeb7d791efa512f23d4b3c02bfff4fdbf0` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_T24_exactcmp.log` | 1569 | `f72a130adb735a30bdc81cb510cea9674b05aafaeea2d2ba24a35f8bcf50dd4a` | `d98de25ee30355ded68fde7df8aa9e6100cdffda` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_T24_rescaled.log` | 1415 | `2e579ed2f04eff8b3978297108055ed60dd0ce2dbed6e576f416f5e643abb2fd` | `f0ed8d94434b46093882fec41b6c78ebeef8320f` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_T40.log` | 1684 | `f8e8106c0a95a573758732e4ec1948b6d8cbe47a56e442400a7f5dd19fce5981` | `6b000c0c813cff37928bbaf310c4ddd7bbf0b744` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_rotQ24.log` | 1724 | `a07a54d9562fc2adf2d81d82dfeb58b618014a89306aede6a0e623313c008489` | `2df7033049b220af206df8ca37bc6782cb90901d` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/checkerboard.log` | 4126 | `918ad576f110c1f5631cc22a22acb1e4c0875e06253bdb8c97dfa80a6c7ee09c` | `11940e4b14cc903fe55ec7b1a25b08f12dad52d8` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/checkerboard_ritz.log` | 417 | `80304a6f978fefd6b2d9b09e87a50b64f0fc99da365f9b1d72751e029df96313` | `3cfd0cd196853e49f98dd38d271206c1fce6f1ff` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/closed_loop.log` | 1297 | `eb062dd919f1a173bd2b82e6470d66e4f10775a1eaaae521c347b22f5bcf57b3` | `465f9c2cbfbfee87159619c811882cd75c13fe45` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/closed_loop_sets.log` | 821 | `77b844281db536a8101a22faee5d41037ac2799a5d2a1de5604f386fc7394ebe` | `f5159b3fc11dc649d97cd60315a675bcf91c2b8d` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/exact_checkerboard.log` | 1116 | `8a13c223cb1e8c407b8fc4eedeecad4f356346a5a2d498b67a12a9494435ffe7` | `6dd685ac94d71b80d78fc736b1c6202f6e29ce08` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/open_loop.log` | 1662 | `acc1acb224d7b7ba278a305b6718440f3dd688821eaf03669cfbc487a05d020c` | `f8ac5423e3873a195f2fbcbbe7289b11011eb093` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/directions/L1/R04.md](../../../directions/L1/R04.md)
- [topics/bivariate-lanczos-20261031/directions/L1/R07.md](../../../directions/L1/R07.md)
- [topics/bivariate-lanczos-20261031/pr-prep/negative.rows.md](../../../pr-prep/negative.rows.md)
- [topics/bivariate-lanczos-20261031/pr-prep/proof_status.rows.md](../../../pr-prep/proof_status.rows.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-prior-art-01.md](../../L1-prior-art-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md](../../L1-reconstruction-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-02.md](../../L1-reconstruction-02.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/reviews/L1-prior-art-01.md](../../L1-prior-art-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md](../../L1-reconstruction-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-02.md](../../L1-reconstruction-02.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/reviews/logs_L1b/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_reviews_logs_L1b_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/reviews/logs_L1b/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/reviews/logs_L1b/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/reviews/logs_L1b/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_Q24.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_Q24_exactcmp.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_T24.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_T24_exactcmp.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_T24_rescaled.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_T40.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/cert_rotQ24.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/checkerboard.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C049 | C049 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/checkerboard_ritz.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C053 | C053 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/closed_loop.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/closed_loop_sets.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/exact_checkerboard.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1b/open_loop.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |

### C049

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/directions/L1/R04.md:44`,
Git blob `5726717bd4b22c3eb81c7b29fd89e95569be0324` at retrieval source40347d1.

````text
python3 -I l1_r04_checkerboard.py > logs/r04_checkerboard.log
````

### C053

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/directions/L1/R04.md:44`,
Git blob `5726717bd4b22c3eb81c7b29fd89e95569be0324` at retrieval source40347d1.

````text
python3 -I l1_r04_checkerboard_ritz.py > logs/r04_checkerboard_ritz.log
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/pr-prep/proof_status.rows.md:38`,
blob `9e62efd643423bbb9b89f4813208a87f4980fa36`:

````text
| PD-T041 | Exact rational certificate: for the dev (BJ) rule the window-recurrence propagator grows exponentially on the triangle grid and stays polynomial on the square grid (degrees ≤ 12, computer-assisted; "exponentially" and "polynomial" describe the finite range only) | PROVED | 1. impulse identity: PROVED; 2. certificate on T_24, Q_24: PROVED (finite, dev rule). The independent rerun was done by recon-02 `rv2_certificate.py`, two ways: (A) full exact Gram–Schmidt with off-window coefficients checked exactly 0; (B) exact LDLᵀ of the moment matrix. Identical values and maximisers; criterion decided exactly; logs `reviews/logs_L1b/cert_{T24,Q24}*.log`. Before recon-02: CONDITIONAL.; 3. T_40, Q_40, rotated Q_24: PROVED (finite). T_40 and rotated Q_24: reproduced exactly by recon-02 (`cert_T40.log`, `cert_rotQ24.log`). Q_40: reproduced exactly by Codex audit-01 (`audit-01/L1-later/cert_square40_rerun.log`, sha256 `4375ae13eae79f3011c3455c09c85798bff7d810aae17ce9111afd17073005f2`); CONDITIONAL (not rerun) before 2026-11-01T08:33:59+01:00. Descriptive, not pre-registered. | none | PD-T029, PD-T032 | [exact-certificate-propagator-growth-triangle.md](tracks/bivariate-lanczos/theory/exact-certificate-propagator-growth-triangle.md) | bivariate-lanczos audits 01–03 (Codex); registry integration response to audit-04, independent review pending |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-02.md:140`,
blob `79db67316763344ff5518c92935959424f2ffbf9`:

````text
Independent implementation (`rv2_checkerboard.py`, `checkerboard.log`, `checkerboard_ritz.log`): m = 30, e = 0, M = 496, x = s³; factor weights 1.7e-33…0.49; bivariate weights 1.8e-67…0.47, confirming PC-12.
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/directions/L1/R07.md:86`,
blob `2454c10d2fe465bd09958747e7cccf23a9a4cc79`:

````text
- `l1_r07_closed_loop.py` → `r07_closed_loop.log` (24 s).
````
