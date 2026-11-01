# PD-N?bivariate-lanczos-claude-207 — PRO-2D-J does not keep semi-orthogonality on the cubic-clustered checkerboard at its last degree

ID kind: PD-N.
Aliases: IDEA?…-209 killed; cubic-checkerboard last-degree failure.
Split from: PD-T?…-207 (a) (failure previously recorded only there), after reconstruction 01 finding F3.
Split into: none.

## Statement

[FP, MEASURED] PRO-2D-J (two-pass window, ω-trigger at √u with the J-rows measured exactly, reorthogonalization against {|ω̃| > u^{3/4}}, BJ block window) on the cubic-clustered Harris–Simanek checkerboard m = 30 (M = 496): L(n) ≤ 6.0e-12 up to n = 25, then 7.1e-11 (26), 3.2e-9 (27–28), **2.0e-7 at n = 29** > 10√u = 1.05e-7 (pre-registered kill), with 61 reorthogonalized columns. Correctly rounded window dots do not repair it (L(29) = 7.5e-7, PD-N?…-204 (d)). The oracle partial scheme (exact Ω, one-pass window) stays at 1.0e-8 on the same set. Reproduced by reconstruction 01 with an independent implementation (L(29) = 2.0e-7).

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?…-209 (PRO-2D-J as a semi-orthogonality-maintaining strategy on all R01 benchmarks).
Parameter range: the cubic checkerboard m = 30, n = 29 (M − N_29 = 31); the other 11 benchmarks pass. Not covered: other thresholds, a reset rule different from Simon-type rounding resets.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| failure | MEASURED | `directions/L2/logs/r02_proJ.raw.gz`, `r02_verdicts.txt`, `r03_dots.raw.gz`; reconstruction 01 rerun |
| cause | OPEN | not identified (candidate: estimate-selected index set misses the bad vectors at a step with strong cancellation near M = N) |

Candidate / claim disposition: IDEA?…-209 REJECTED. Rejection reason: failed (scope above). A narrowed successor (IDEA?…-211, non-clustered sets) is recorded in candidates.md, untested.

## Depends on

PD-T?…-203, -207.

## Checks

`python3 -I tracks/bivariate-lanczos/code/L2/l2_r02_pro.py --jmeasure cb_cubic`. Independent rerun: Codex audit-01 (`topics/bivariate-lanczos-20261031/audit-01/L2/proJ-rerun.log`, `dots-rerun.log`): L(29) = 1.9702675e-7 = 18.70√u (> 10√u); the failure is also reproduced with the exact-dot substitution of the R03 suite.

## Sources

None.

## Proof or evidence

Measured.

## Scope

As stated.

## Open items

Cause of the failure.

## History

- 2026-11-01T01:29:29+01:00: created from PD-T?…-207 (a) in response to reconstruction 01 finding F3 (Claude Opus 5.5, xhigh; L2 developer).
- 2026-11-01T08:32:22+01:00: Checks: audit-01 independent rerun recorded (original Checks: the command only). Statement, disposition and status MEASURED unchanged (Claude Opus 5.5, xhigh; L2 developer, response to Codex audit-01, `directions/L2/response-audit-01.md`).
