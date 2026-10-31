# PD-N?bivariate-lanczos-claude-104 — Open-loop coefficient-noise estimates of the clustered-checkerboard loss fail (generic u-noise, sign-randomised magnitudes); term-wise rounding on the exact coefficients over-estimates increasingly with clustering strength (its kill is convention-sensitive)

ID kind: PD-N.
Aliases: H_cond-abs overshoot; H_sign failure; open-loop term-wise estimate killed.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] BJ block CGS, checkerboards as in PD-T?…-115, n = 16 and 20; ratios are estimate / BJ loss L(n).

(a) **Generic absolute u-noise on the structural zeros** (IDEA?…-117, H_cond-abs): 2·10⁷ (n = 16) and 4·10⁶ (n = 20) on the cubic m = 30 set. This is inconclusive by the written rule, which did not foresee an overshoot, and useless as an estimate. It reconfirms PD-N?…-103 (b) ("worst-case absolute coefficient noise over-predicts by up to 10⁷").
(b) **BJ magnitudes with random signs** (IDEA?…-118, H_sign): 3.1·10³ and 1.4·10³ on the cubic m = 30 set; killed by the written rule (> 100). The sign structure of the computed off-pattern values matters.
[Correction 2026-10-31T23:11Z: (c) is convention-sensitive. At the plan's u = 2^-53 the same rule gives "inconclusive" (quartic 60× / 11×), and H_term on cubic m = 30 gives "survives" (5.1× / 2.3×); `logs/c01_u53_rerun.log`. (c) is kept as the measured trend (the over-estimate grows with clustering strength), not as a kill.] (c) **Term-wise rounding noise on the exact coefficients** (IDEA?…-119, open-loop estimate E): killed by the written rule on quartic clustering (119 at n = 16, > 100). It survives on quadratic clustering (1.08, 0.95) and the Chebyshev–Lobatto control, and is inconclusive on cubic m = 36 (10.5, 12.8) and on cubic m = 30 (10.3, 4.6; IDEA?…-118 H_term).

## Negative-result scope (PD-N only)

Attempted mechanism: "the coefficient-channel loss is the response of the exact coefficient map to independent coefficient errors of a given size", i.e. no feedback between the computed vectors and the computed coefficients. Parameter range: the six checkerboards of PD-T?…-115 (m = 30, 36), degrees ≤ 24.

## Statement status

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | MEASURED | `logs/r06_coefficient_channel.log` |
| (b) | MEASURED | `logs/r07_offpattern_anatomy.log` |
| (c) | MEASURED | `logs/r07_termwise_predictor.log` |

Candidate / claim disposition: IDEA?…-117 H_cond-abs inconclusive (as a predictor: failed); IDEA?…-118 H_sign REJECTED: failed; IDEA?…-119 REJECTED: failed (quartic). Corrected 2026-10-31T23:11Z: IDEA?…-119 convention-sensitive (killed at 2^-52, inconclusive at 2^-53); no longer REJECTED.
Rejection reason: failed (MEASURED, stated ranges).

## Depends on

PD-T?…-114, -115.

## Checks

R06.md §7, R07.md §7 commands.

## Sources

None.

## Proof or evidence

Measured; see logs.

## Scope

Product-type checkerboards only. The failure is attributed to the missing feedback: the closed-loop model of PD-T?…-115 (c) succeeds on the same sets.

## Open items

An exact-data estimate that includes the feedback (the operator (I − T)⁻¹ of PD-T?…-115, open items).

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R07).
- 2026-10-31T23:11Z (re-check after reconstruction 01): not affected by B1. The B2-type convention issue affects (c); IDEA?…-119's disposition is corrected to convention-sensitive. (a) (overshoot 10⁶–10⁷) and (b) (signs, no noise scale) are unaffected.
  - Title narrowed at the same time. Original title: "Open-loop coefficient-noise estimates of the clustered-checkerboard loss fail: generic u-noise, sign-randomised magnitudes, and term-wise rounding on the exact coefficients".
