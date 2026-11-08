# Local native replay of the 276 unsampled archive primaries (audit-03 addendum)

Authorized by AC (decision 3 of 5, 2026-11-08), run by the audit orchestrator
(`claude-sonnet-5-5`; no subagent), after a saved preregistration. This closes
the "276 degrees not replayed natively off Syvert" limit (audit-03 E-06) for the
**faithfulness** of the Syvert run. It is **not** independent arithmetic: it uses
the same frozen engine and the same Arb/FLINT kernels (idea I25, which Codex
builds next, is the independent-arithmetic step).

## What was run

- Archive: the compact return supplied by AC as two parts, joined, 36,045,486 B,
  sha256 `b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a`.
  The 276 primary receipts `outputs/all/jobs/N/produce/essential-receipt.json`
  were copied as data only (no extraction of paths, nothing executed from the
  archive; `code/replay276/pull_member.py`).
- Population: every degree of the 280 pairs except 41, 199, 238 and 511 (already
  replayed in audit-03 part E): degrees 42..319 without 199 and 238, i.e. the 22
  + 96 + 32 + 62 + 64 degrees listed below.
- Engine: `final_hybrid_engine/engine.py` from a `git archive` copy of head
  `f366535` (engine bytes verified identical; FREEZE sha256
  `0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb`).
  Command per degree: `engine.py --mode verify --n N --output NEW --run-once
  --certificate PRIMARY`, run exactly once with `os.wait4` (never subprocess).
- Runtime difference (as in part E): Ubuntu 24.04 FLINT 3.0.1 (SONAME copied as
  `libflint.so.19`), GMP 6.3.0, MPFR 4.2.1, g++ 13.3, glibc 2.39, CPython 3.13.18;
  not the pinned Debian FLINT 3.1.3 / MPFR 4.2.2 / GMP 6.3.0+dfsg-3. Engine-internal
  caps unchanged; outer wall 1050 s per call; 4 concurrent shards on 4 cores.
- Preregistration (319,335 B, kept off Git; regenerable by
  `code/replay276/make_prereg.py`): sha256
  `e9e0886f38711e37f10193fc75736d4f57ea28a3bf6013d2251e72721be520e2`. Acceptance
  per call: observed exit 0, no timeout, ECHILD afterwards, final accounting
  `FRESH_RETAINED_PROOF_VERIFY_ACCEPTED_PENDING_RESULT_REVIEW` with
  `first_failure` null and `complete` true, and the fresh essential receipt equal
  to the Syvert primary on `S_upper_columns, S_upper_rows, analytic_far, corner,
  floor, lambda_upper_columns, lambda_upper_rows, n, norm, origin_lower_hex,
  pi_bracket, tree, verification, format, status, scope`. No retry, rescue or
  substitution was allowed (none was needed).

## Result

**276 of 276 calls accepted. All 276 fresh receipts equal the Syvert primaries
on every compared field.** Every call exited 0 (observed), none timed out, ECHILD
held after each call, no first failure, no field difference. Together with the
four earlier replays (41, 199, 238, 511) all 280 degrees are now natively
re-executed off Syvert on a different library stack.

| Degrees | Calls | CPU-s per call (min / median / max) | Total CPU-s |
|---|---:|---|---:|
| 42–63 | 22 | 6.68 / 6.87 / 7.20 | 151.7 |
| 64–159 | 96 | 6.90 / 8.29 / 9.60 | 796.9 |
| 160–191 | 32 | 9.43 / 9.88 / 10.43 | 317.2 |
| 192–255 | 62 | 10.13 / 11.05 / 11.93 | 686.5 |
| 256–319 | 64 | 5.17 / 5.65 / 6.30 | 360.2 |
| **all** | **276** | **5.17 / 8.45 / 11.93** | **2312.5** |

Wall time per shard about 617–621 s (about 10 minutes); maximum resident size
163.5 MiB. The earlier projection of about 4.4k CPU-s counted a primary pass too;
a fresh verify costs about 8.5 CPU-s, so the whole replay took about 2.3k CPU-s.
The step down at 256 reflects the analytic corner branch (no lambda build) used
from degree 256. Replays are a different library stack but bit-equal results are
expected from a deterministic engine; they detect a faulty or tampered server
run, not a fault in the Arb kernels themselves.

Scripts: `code/replay276/` (hashes `make_prereg.py` aa238946…, `shard_runner.py`
84a49d5a…, `compare_results.py` ec85c05c…, `pull_member.py` eeff79d9…). The 828
output directories (6.7 GB) and the full per-call table stay outside Git in the
auditor's scratch area; they can be regenerated from the committed scripts, the
archive and the head.
