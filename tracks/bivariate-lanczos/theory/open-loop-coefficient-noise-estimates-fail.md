# PD-N?bivariate-lanczos-claude-104 — Open-loop coefficient-noise estimates of the clustered-checkerboard loss fail (generic u-noise, sign-randomised magnitudes); term-wise rounding on the exact coefficients over-estimates increasingly with clustering strength (as a kill: convention-sensitive under the noise model, inconclusive with actual double rounding)

ID kind: PD-N.
Aliases: H_cond-abs overshoot; H_sign failure; open-loop term-wise estimate killed.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] BJ block CGS, checkerboards as in PD-T?…-115, n = 16 and 20; ratios are estimate / BJ loss L(n).

(a) **Generic absolute u-noise on the structural zeros** (IDEA?…-117, H_cond-abs): 2·10⁷ (n = 16) and 4·10⁶ (n = 20) on the cubic m = 30 set. This is inconclusive by the written rule, which did not foresee an overshoot, and useless as an estimate. It reconfirms PD-N?…-103 (b) ("worst-case absolute coefficient noise over-predicts by up to 10⁷").
(b) **BJ magnitudes with random signs** (IDEA?…-118, H_sign): 3.1·10³ and 1.4·10³ on the cubic m = 30 set; killed by the written rule (> 100). The sign structure of the computed off-pattern values matters.
[Correction 2026-10-31T23:11Z: (c) is convention-sensitive. At the plan's u = 2^-53 the same rule gives "inconclusive" (quartic 60× / 11×), and H_term on cubic m = 30 gives "survives" (5.1× / 2.3×); `logs/c01_u53_rerun.log`. (c) is kept as the measured trend (the over-estimate grows with clustering strength), not as a kill.] (c) **Term-wise rounding noise on the exact coefficients** (IDEA?…-119, open-loop estimate E): killed by the written rule on quartic clustering (119 at n = 16, > 100) [at u = 2^-52 under the noise model only. With actual double rounding the written rule gives **inconclusive**, not rejected: reconstruction 02, and freshly rerun by Codex audit-01 with quartic 21.58 / 12.95 and cubic m = 36 16.40 / 21.13 at n = 16 / 20 (`audit-01/L1-later/open_loop_rerun.log`). Note 2026-11-01T08:41:34+01:00]. It survives on quadratic clustering (1.08, 0.95) and the Chebyshev–Lobatto control, and is inconclusive on cubic m = 36 (10.5, 12.8) and on cubic m = 30 (10.3, 4.6; IDEA?…-118 H_term).

## Negative-result scope (PD-N only)

Attempted mechanism: "the coefficient-channel loss is the response of the exact coefficient map to independent coefficient errors of a given size", i.e. no feedback between the computed vectors and the computed coefficients. Parameter range: the six checkerboards of PD-T?…-115 (m = 30, 36), degrees ≤ 24.

## Statement status

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | MEASURED | `logs/r06_coefficient_channel.log` |
| (b) | MEASURED | `logs/r07_offpattern_anatomy.log` |
| (c) | MEASURED (trend). The kill verdict is decided convention-free as **inconclusive** by recon-02 with actual double rounding (REVIEWER-MEASURED: E/L at n = 16/20 quadratic 1.13 / 0.53, cubic 5.13 / 4.70, quartic 21.6 / 12.9, cubic m = 36 16.4 / 21.1). | `logs/r07_termwise_predictor.log`, `logs/c01_u53_rerun.log`, `reviews/logs_L1b/open_loop.log` |

Candidate / claim disposition: IDEA?…-117 H_cond-abs inconclusive (as a predictor: failed); IDEA?…-118 H_sign REJECTED: failed; IDEA?…-119 REJECTED: failed (quartic). Corrected 2026-10-31T23:11Z: IDEA?…-119 convention-sensitive (killed at 2^-52, inconclusive at 2^-53); no longer REJECTED. Resolved 2026-10-31T23:37Z (recon-02, actual double rounding, REVIEWER-MEASURED): IDEA?…-119 inconclusive; IDEA?…-118 H_term survives.
Rejection reason: failed (MEASURED, stated ranges).

## Depends on

PD-T?…-114 (gain formulas), -117 (measured gains and first-order channel), -115 [-117 added 2026-11-01T08:41:34+01:00 after the split of PD-T?…-114].

## Checks

R06.md §7, R07.md §7 commands.

## Sources

None.

## Proof or evidence

Measured; see logs.

## Scope

Product-type checkerboards only, dev rule. The failure is attributed to the missing feedback. The closed loop with actual double dot products reproduces the loss on the same sets (PD-T?…-115 (d), REVIEWER-MEASURED, C/L 0.56–1.86); the closed-loop term-wise noise model does so only within a convention-dependent factor (115 (c)). [Corrected 2026-10-31T23:37Z, recon-02 m1; original: "Product-type checkerboards only. The failure is attributed to the missing feedback: the closed-loop model of PD-T?…-115 (c) succeeds on the same sets."]

## Open items

An exact-data estimate that includes the feedback (the operator (I − T)⁻¹ of PD-T?…-115, open items).

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R07).
- 2026-10-31T23:11Z (re-check after reconstruction 01): not affected by B1. The B2-type convention issue affects (c); IDEA?…-119's disposition is corrected to convention-sensitive. (a) (overshoot 10⁶–10⁷) and (b) (signs, no noise scale) are unaffected.
  - Title narrowed at the same time. Original title: "Open-loop coefficient-noise estimates of the clustered-checkerboard loss fail: generic u-noise, sign-randomised magnitudes, and term-wise rounding on the exact coefficients".
- 2026-10-31T23:37Z (response to reconstruction 02):
  - M3: IDEA?…-119 is decided convention-free as inconclusive with actual double rounding (reviewer-measured), replacing "convention-sensitive". The trend in (c) is confirmed by recon-02.
  - m1: the Scope sentence is corrected (original kept there).
- 2026-11-01T08:41:34+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-later table note on T115/N104(c) and LL-M2 pointers). The title parenthesis said "(its kill is convention-sensitive)", which was stale after the reconstruction-02 resolution. It now reads "convention-sensitive under the noise model, inconclusive with actual double rounding". (c) states the convention-free inconclusive verdict in place, with the audit's rerun. Depends on gains PD-T?…-117. Original title: "PD-N?bivariate-lanczos-claude-104 — Open-loop coefficient-noise estimates of the clustered-checkerboard loss fail (generic u-noise, sign-randomised magnitudes); term-wise rounding on the exact coefficients over-estimates increasingly with clustering strength (its kill is convention-sensitive)". Status (MEASURED) unchanged.
