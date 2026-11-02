# Cold-storage manifest — padua-mz-2d-20261101

## Repository cleanup 2026-11-02 — large regenerable outputs moved off the branch head

AC (2026-11-02): "I do not think that we have to store large outputs that can be regenerated. Make sure that all needed code is in the repo, some short summaries are stored and expunge the large data files (cold storage)"; "18 mb per repo is too much."

Every generated data file of 16 KiB or more in this directory left the branch head: 12 files, 1,525,001 bytes. Machine manifest: [`cold-storage.json`](cold-storage.json). Tool: `tools/cold_storage.py`.

These files have **not been delivered to AC's Padua cold storage yet** (PENDING). Until then, the only stored copy is Git history, pinned by blob id at the pushed main commit `2b52b432fe59c9a50aef9deebe5152c5d6874465`. Each file's SHA-256 is recorded alongside, so the bytes can be verified.

Code, records, and small receipts and summaries stay. Generators committed: tracks/mz-constants/code/{mz2d_exact,mz2d_independent_check,mz2d_spectra}.py, protocol/final-*.py, response-01-20261101-validate.py. mz2d_exact.py needs python-flint 0.9.0 (about 30 s). Restore before running mz2d_independent_check.py, audit/claude-audit-01/run_dev_independent_functions.py or the protocol validators (final-validate.py needs final-assignment-checks.json and final-input-manifest.json). mz2d-eta-counterexample.md pins exact-spectra.json by SHA-256; the manifest keeps exact bytes. Protocol receipts are point-in-time records of one-shot scripts. Small committed siblings: evidence/d0-manifest.json, exact-parity-scan.json, independent-additional-checks.json, protocol/input-manifest.json.

Files of 16 KiB or more kept on purpose (not generated output):
- `protocol/final-id-map.json` (26,582 bytes): authoritative approved provisional-to-final ID map, linked from ID_CROSSWALK.md and the batch ALLOCATIONS ledger; registry record, not bulk output.

| File | Actual storage path | Bytes | SHA-256 | Source commit | Frozen generating command | Script blob IDs | Checker command / result |
|---|---|---|---|---|---|---|---|
| `audit/claude-audit-01/claude-mz2d-spectra.json` | Git blob `64ea8c7ec2a7` at `2b52b432fe59`; AC cold storage PENDING | 31,818 | `de3a6dc6726268ac5c0e61f46c79435e561be1514f76c60f6e79f17120f7bbbd` | `2b52b432fe59` | PYTHONPATH=<flint> OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 tracks/mz-constants/code/mz2d_exact.py --m 10 20 30 40 --output <out> | committed at source commit | Summary: audit-01.md:68-72 (R1: results equal exact-spectra.json); audit/claude-audit-01/MANIFEST.md:16. Auditor rerun of the exact producer. |
| `audit/claude-audit-01/final-validation.claude-rerun.json` | Git blob `ba3373a45764` at `2b52b432fe59`; AC cold storage PENDING | 18,087 | `f8cc5398347a4e0961e39e8c1d952071ee42addd0d5b76fc6cfb1435b6fc14e9` | `2b52b432fe59` | python3 topics/padua-mz-2d-20261101/protocol/final-validate.py (disposable worktree at e847601) | committed at source commit | Summary: audit-01.md:92 (R5: PASS); audit/claude-audit-01/MANIFEST.md:22.  |
| `evidence/d0-spectra.json` | Git blob `2530454a05f6` at `2b52b432fe59`; AC cold storage PENDING | 837,344 | `3c5c702ed964b240a9e96bb0be55a2a3e86c2c71eb5e49706b7c58680879e4f5` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_spectra.py --m 10 20 30 40 60 80 100 --crosscheck 10 20 30 40 --output <out> | committed at source commit | Summary: tracks/mz-constants/theory/mz2d-measured-spectra.md (PD-T108 table); directions/D0.md; evidence/d0-manifest.json. MEASURED float64 evidence; no script reads it. |
| `evidence/exact-spectra.json` | Git blob `42d88e6a18a0` at `2b52b432fe59`; AC cold storage PENDING | 31,822 | `5456917afe8fea69b0a776270ef3ae79fdc33deb02d27f89648fc342f78b93de` | `2b52b432fe59` | PYTHONPATH=<flint> OPENBLAS_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_exact.py --m 10 20 30 40 --output <out> | committed at source commit | Summary: tracks/mz-constants/theory/mz2d-certified-spectra.md (PD-T107 enclosures, sha 5456917a); mz2d-eta-counterexample.md:25,127; directions/D6.md. Evidence of PROVED PD-T107 and the eta witness; checker tracks/mz-constants/code/mz2d_independent_check.py (restore first). |
| `evidence/independent-exact-spectra.json` | Git blob `1b7c73f3267e` at `2b52b432fe59`; AC cold storage PENDING | 31,834 | `18c8623442664aa119d3581b701d200315d454071d6b8f6c89cbaf540fe34d9c` | `2b52b432fe59` | PYTHONPATH=<flint> OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_exact.py --m 10 20 30 40 --output <out>; then python tracks/mz-constants/code/mz2d_independent_check.py | committed at source commit | Summary: independent-checks.md (hash 18c86234 at :73); mz2d-certified-spectra.md. Different-agent replay of the PD-T107 producer. |
| `protocol/final-assignment-checks.json` | Git blob `2860d12f2cff` at `2b52b432fe59`; AC cold storage PENDING | 38,294 | `09a994c8e6e5e630c44febc2bc10719afb3f3e716fa9d95fb3d8b6c904dc4180` | `2b52b432fe59` | python3 topics/padua-mz-2d-20261101/protocol/final-assign.py --apply-approved (one-shot; do not repeat) | committed at source commit | Summary: LOG.md:7 (assigned ranges); protocol/README.md. Point-in-time assignment receipt; input of final-validate.py. |
| `protocol/final-assignment-dry-run.json` | Git blob `a84f9beae76c` at `2b52b432fe59`; AC cold storage PENDING | 38,193 | `a47fcdf45acc72ccd4e2ead40eeb1097a6cf154ca337a0f0543b6fa84a972732` | `2b52b432fe59` | python3 topics/padua-mz-2d-20261101/protocol/final-assign.py (dry run) | committed at source commit | Summary: protocol/README.md. Superseded by final-assignment-checks.json. |
| `protocol/final-id-map-draft.json` | Git blob `51ff243f93ce` at `2b52b432fe59`; AC cold storage PENDING | 26,384 | `d48735e66834f3c845215af83c63084236e03024011769515969c325fff409b7` | `2b52b432fe59` | topics/padua-mz-2d-20261101/protocol/final-build.py (command not recorded) | committed at source commit | Summary: protocol/README.md; LOG.md:7. Draft map superseded by final-id-map.json. |
| `protocol/final-input-manifest.json` | Git blob `b8d00293c185` at `2b52b432fe59`; AC cold storage PENDING | 56,380 | `647cf4c7bbe27691ad189ecf3373f98c2a71698070845bc601d226366a3c5ee3` | `2b52b432fe59` | topics/padua-mz-2d-20261101/protocol/final-build.py (point-in-time capture) | committed at source commit | Summary: handoffs/02-audit.md:34; protocol/README.md. Input of final-validate.py, response-01-20261101-validate.py, integration-pr14-first-20261101-check.py. |
| `protocol/final-validation.json` | Git blob `4afaf38c9e01` at `2b52b432fe59`; AC cold storage PENDING | 18,087 | `e7f2cbd5a45f709461e5b8cb5c732e075dc69cc72849d64924bd593dfb39d22a` | `2b52b432fe59` | python3 topics/padua-mz-2d-20261101/protocol/final-validate.py | committed at source commit | Summary: audit-01.md:92; LOG.md:78. PASS; mechanical ID-registration validation. |
| `protocol/response-01-20261101-reservation-recheck.json` | Git blob `d5830692976c` at `2b52b432fe59`; AC cold storage PENDING | 17,005 | `f2ff2f293e2f239bb5bb00de3bab9033a4292f8b3491929bb1ef58b584d90f0e` | `2b52b432fe59` | python3 topics/padua-mz-2d-20261101/protocol/response-01-20261101-validate.py | committed at source commit | Summary: LOG.md:7; response-01.md:58. Reservation recheck PASS; point-in-time. |
| `protocol/response-01-20261101-validation.json` | Git blob `ef2244dd041b` at `2b52b432fe59`; AC cold storage PENDING | 379,753 | `f69a2ae7c2a17c5535a2f68defb40b0f5ba33a46d21cfcdfdc4ccd1310d0f141` | `2b52b432fe59` | python3 topics/padua-mz-2d-20261101/protocol/response-01-20261101-validate.py | committed at source commit | Summary: response-01.md:59. Documentation-only validation PASS; hash inventory. |

`<out>`, `<work>`, `<deps>` and `<flint>` stand for scratch paths. Never write regenerated output over committed files.

**Retrieval**

```sh
python tools/cold_storage.py verify  padua-mz-2d-20261101   # every entry against its Git object
python tools/cold_storage.py restore padua-mz-2d-20261101   # put the files back in place, then run the recorded checkers
python tools/cold_storage.py clean   padua-mz-2d-20261101   # remove the restored copies again
python tools/cold_storage.py export  padua-mz-2d-20261101 --dest C:\Users\andreyac\Downloads\padua\cold_storage
```

These commands need a full clone. In a shallow clone, first run `git fetch origin 2b52b432fe59c9a50aef9deebe5152c5d6874465`.

**Retention**

Permanent, with AC as custodian. The Git history copy lasts as long as history is not rewritten. The AC copy is created by `export`; commit its receipt hash here when that is done.
