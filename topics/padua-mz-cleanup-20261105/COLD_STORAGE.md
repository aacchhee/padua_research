# Cold storage — MZ cleanup, 2026-11-05

**Physical delivery PENDING.** Intended AC destination:
`Downloads\padua\cold_storage\padua-mz-cleanup-20261105\`.
That location is not accessible in this sandbox. A local transfer package is
ready; staging does not establish external delivery or future retention.

## Final C1 package

Frozen source commit: `39479ffca76052ea79f90c2e5e0c4bfc80bf1584`.
Actual archive:
`/tmp/mz-cleanup/transfer-stage/padua-mz-cleanup-20261105/c1-package-39479ff.tar.gz`

- Archive: **159,265,962 bytes**; SHA-256 `ac6a628153746729688851baa3aa50f41dc31509d9ce4058dc221fb0550982b1`.
- Payload: 71 files / 164,319,751 bytes, including the complete inventory.
- Inventory: `/tmp/mz-cleanup/transfer-stage/padua-mz-cleanup-20261105/checkpoint-39479ff/PACKAGE-INVENTORY.json`.
- Inventory: 19,557 bytes; SHA-256 `21e49393aa139cafa87c166520fe7478ee767694ee056356ef080f53c254170c`.
- Snapshot: `2026-11-05T14:22:23.886059+00:00`. No unfinished files skipped.

The archive contains all five final dyadic polynomial witnesses, exact positive
rational norms, producer and independent receipts; every available source
vector in `vectors/` and `growth-vectors/` at the snapshot; actual raw scan
JSON/log snapshots; frozen generating/checker source; and reproduction notes.
The larger per-file inventory stays inside the off-repository package. The
[small committed manifest](cold-storage.json) pins the archive and inventory,
and preserves the five essential finite-witness identity chains. Files were
not split to evade a size limit. Active scans may extend after this snapshot.

### Essential finite artifacts

Paths below are relative to `checkpoint-39479ff/` inside the archive.

| m | Witness bytes / SHA-256 | Exact-norm bytes / SHA-256 | Accepted sign |
|---:|---|---|---|
| 60 | 11,853 / `9a1bb58cce8d8179840a024f045e8bbb32aafe9ad58d7545af4ec74278d566e9` | 214 / `04e78a32440f8b276d88ab812794af14a034963d3d361c772fd650efbccf66c4` | positive (producer and independent checker) |
| 400 | 532,189 / `b433ab66e1d7e971629c58b4c56839a013bf1bfb64e021ccac09b84bd1bb094d` | 1,082 / `6dc2c74a7a45ce061467482b4187ac2950a144bc49367090409a9cc538870c2f` | positive (producer and independent checker) |
| 1101 | 4,196,078 / `22913a3271c0cd826ff062a1f880c3539ef937b0141820dab381b53181662813` | 2,904 / `f651dff771fd67b5b3a9afb89e8f8c01c9b7a842a93cbe3b7658b04e69270f14` | negative (producer and independent checker) |
| 1240 | 5,365,436 / `1a9faac5677ac4dde63749a6acac38d95ee88a5082445e6ba6b59cc297d35e4e` | 3,298 / `a9895473f6a97a3bca7a4b20144326a118f85d74157e00a32291eb11241f7daf` | negative (producer and independent checker) |
| 1600 | 8,692,559 / `16d89f2c8600364aac3962c4164f0e0875c4fa866fc61269fd6f849e8f1fdad6` | 4,200 / `d6b405a856e735ac4df1d9db0295fbc093af66ee620d29c52ef553d6c1d3f6fa` | negative (producer and independent checker) |

Each pair is `cert-mM/witness.json.gz` and `cert-mM/exact-norm.txt`.
The m60/m400 positive controls are distinct from the negative witnesses at
m1101/m1240/m1600. Source-vector SHA-256, producer arithmetic, exact-norm
sign and checker identity remain in the packaged receipts and small manifest.

### Verification actually executed

Every source file was read as a snapshot, copied and read back. The completed
tar.gz was reopened and **all 71 member sizes and SHA-256 values** were checked
against the inventory; its membership exactly matched. Every final witness and
norm also matched its producer receipt, every source-vector hash matched the
producer input, and each independent receipt accepted the same witness hash
and sign. These are storage/identity checks; the scientific executions are the
producer/checker runs recorded in the committed evidence and
[independent check](independent-checks-witness.md). No new scientific replay
is credited to this packaging step.

## Frozen regeneration and checking

Use the repository at the full source commit above. Dependencies and actual
commands are recorded in the receipts: Python3.12, NumPy2.3.5, SciPy1.17.0,
python-flint0.9.0. Preserve one BLAS/OMP thread. Replace `M` below by each
of 60,400,1101,1240,1600 and use fresh output paths; `N=M-1`.

```sh
PYTHONPATH=<python-flint> OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-cleanup-20261105/code/rigorous_witness.py --m M --witness <package>/checkpoint-39479ff/cert-mM/witness.json.gz --scratch <fresh>/cert-mM --output <fresh>/producer-mM.json
PYTHONPATH=<python-flint> OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-cleanup-20261105/code/independent_witness.py --witness <package>/checkpoint-39479ff/cert-mM/witness.json.gz --output <fresh>/independent-mM.json
```

The first command replays exact fixed-point/Arb certification without running
an eigensolver. The second uses separate Arb-certified binary64 tables and
the explicitly documented IEEE/BLAS forward-error assumptions. Regenerating a
proposal instead uses `g1_minimum.py` with the grid, seed and options in the
actual raw scan receipt, then `rigorous_witness.py --vector ...`. Fresh solver
bytes need not match on another platform; use the archived exact witness for
byte-pinned replay. The package README gives the same recipes. The shown
commands are reproduction instructions, not new executions by this worker.

## Inherited pending deliveries

Original artifact paths, full SHA-256/size/blob identities, generating/checker
commands and summary locations remain in the SHA-pinned manifests below.
They are referenced rather than duplicated in the new package. An old
historical manifest does not establish that old scratch is currently present.

| Source | Files / bytes | Pinned manifest SHA-256 |
|---|---:|---|
| PR14 | 13 / 1,551,583 | `c5741aad6277146ea3d1c65ca903b6d4fb49579a0dcd7a9fae77a05c0c36a25b` |
| PR14 raw audit | 6 / 991 | `8b96f4559b72810ff90aaf914d946d499185568d9182db9d7e5f5fa04ddc2437` |
| PR23 | 12 / 10,783,037 | `f9b4299cdd26e4b547c8c8ac677e668f048141ee8fe6ed9d933388c0db087ba6` |

**PR14:** `topics/padua-mz-2d-20261101/cold-storage.json` at `2b52b432fe59c9a50aef9deebe5152c5d6874465`.

**PR14 raw audit:** `topics/padua-mz-2d-20261101/audit/claude-audit-01/cold-storage-20261105/cold-storage.json` at `40347d11071c81c1c633a2578cb52325bb92584a`.

**PR23:** `topics/padua-mz-2d-frontier-20261105/cold-storage.json` at `f745e6d044c224962edc16a157efbf55efd9836b`.

PR14 has 13 original Git-backed files (1,551,583 bytes) plus the later
six-stream raw-audit addendum (991 bytes). Retrieve with the unchanged
`tools/cold_storage.py export` for each manifest directory, then
`verify-archive` with the original manifest. Fetch each pushed source commit
if absent. No such historical export was rerun in this packaging step.
Do not rerun one-shot assignment scripts to reproduce point-in-time receipts.

PR23 has twelve historical scratch artifacts (10,783,037 bytes), including
its original 10,246,528-byte m1600 vector, and zero Git-backed payload entries.
Its unretained matrices and scratch are regenerable from committed producer
and independent-checker code; an old `/tmp` path is not a durable archive.
The present package now retains the regenerated C1 data separately. All
original historical manifests remain unchanged.

## Transfer acceptance and retention

The archive and its per-file inventory must travel together. Before relying
on a delivered copy, recompute the archive SHA-256, extract safely to a fresh
directory, and verify every payload against `PACKAGE-INVENTORY.json`; verify
the inventory itself against the trusted SHA-256 above. For historical
Git-backed utility exports, run `verify-archive` immediately before reliance.

Temporary staging has no promised lifespan. AC becomes external custodian
only after actual transfer and verification. The code and small receipts stay
in Git; historical Git blobs remain retrievable while history is retained.
No historical purge, external-machine access or delivery is performed here.

## Final scan supplement

All23 scan rows completed. Final local supplement `/tmp/mz-cleanup/transfer-stage/padua-mz-cleanup-20261105/final-scan-supplement.tar.gz`: 44,618,351 bytes, SHA-256 `257fa21a83b5bb74b93483e371efcc87cf5e0ac965bb32fab2ddfadd808bc338`. Its13 members include the final raw receipts/logs, small summary, summary code, and vectors absent from the prior snapshot. Full inventory `/tmp/mz-cleanup/transfer-stage/padua-mz-cleanup-20261105/final-scan-supplement/INVENTORY.json` (1955 bytes, SHA-256 `0b2e20c0f668219720cef76f54a59262b63c04d046a7a86472d2ce746aac0f6c`) stays off-repository. Every archived member was reopened and its bytes/hash verified. These are MEASURED observations, not extra certificates. Same Padua destination; delivery remains PENDING.
