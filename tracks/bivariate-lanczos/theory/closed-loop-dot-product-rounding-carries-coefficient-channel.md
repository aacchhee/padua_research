# PD-T?bivariate-lanczos-claude-115 — On clustered product-type checkerboards (dev rule) closed-loop dot-product rounding through the off-pattern gains reproduces the coefficient-channel loss (sufficiency within the tested models). The BJ off-pattern values are feedback-dominated and sign-structured, open-loop models over-estimate, and the closed loop with actual double dot products of the double-rounded vectors reproduces the loss (reviewer-measured); the term-wise noise model does so only up to a convention-dependent factor

Final ID: **PD-T043** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: off-pattern error anatomy; closed-loop dot-product model; φ/ρ split; feedback cancellation.
Split from: none (continues PD-T?…-114 and its measured companion PD-T?…-117).
Split into: none.

## Statement

[FP, MEASURED] Harris–Simanek checkerboards (PD-T?…-111), BJ ordering, block window, CGS, nmax = 24, u = 2^-52. L(n) = double BJ loss; D(c, n) = long-double Gram defect of the coefficient map Ξ(c) (PD-T?…-114); c* = product-type coefficients; off-pattern = structural zeros of c*.

(a) **Anatomy on the cubic-clustered checkerboard (s|s|², m = 30; IDEA?…-118).** Split each BJ off-pattern value as h = φ + ρ: φ is the long-double inner product of the stored double vectors (feedback part) and ρ is the rounding of the double dot product. Then max|h| = max|φ| = 2.1e-13 and max|ρ| = 1.1e-16. On the 100 off-pattern entries of largest first-order gain (median gain 4.7e12, degrees ≤ 20) the medians are |h| = |φ| = 2.3e-20, |ρ| = 3.1e-23, u·Σ_i|ξ*_l||aξ*_p| = 4.4e-22 and u·‖ξ*_l ⊙ aξ*_p‖₂ = 1.4e-22. At n = 16 / 20 (L = 1.80e-11 / 7.75e-9):
   - D(c* + h) = L; D(c* + φ) = 3.02e-10 / 2.79e-8; D(c* + ρ) = 3.03e-10 / 3.53e-8, i.e. each part alone gives 17× / 4× the loss, the two give nearly equal defects, and their sum gives L (cancellation between feedback and rounding);
   - term-wise rounding noise u Σ_i ε_i ξ*_{i,l}(aξ*_p)_i on the exact coefficients (open loop, median of 3): 1.85e-10 / 3.59e-8 (10.3× / 4.6×);
   - |h| with random signs (median of 3): 5.51e-8 / 1.09e-5 (3.1·10³× / 1.4·10³×);
   - the triangle-inequality bound max gain·|h| over entries is 5.7e-6 at n ≤ 20, 700× the defect.
(b) **Open-loop estimate across clustering strengths (IDEA?…-119).** E(n) = term-wise noise on the exact coefficients, compared with L(n) at n = 16 / 20: quadratic s|s| (m = 30) 1.08 / 0.95; cubic m = 30 10.3 / 4.6 (from (a)); cubic m = 36 10.5 / 12.8; quartic s|s|³ (m = 30) 119 / 22; Chebyshev–Lobatto (flat control) E(20) = 1.2e-15. The over-estimate grows with the clustering strength.
(c) **Closed loop (IDEA?…-120).** Run the BJ recurrence in long double and replace each coefficient by its long-double inner product plus u Σ_i ε_i q_{i,l}u0_i, all window entries. The resulting loss C(n) (median of 3) satisfies C/L at n = 16 / 20 of: cubic m = 30 0.58 / 0.52; quadratic 0.33 / 0.37; quartic 1.06 / 0.82; cubic m = 36 0.28 / 0.78. On the flat sets, equispaced has C(20) = 3.7e-15 (L = 1.5e-14) and Chebyshev–Lobatto 2.5e-16 (L = 3.1e-15). Over n = 8…24 the ratio C/L on the four clustered sets lies in [0.23, 1.06]. The plain long-double BJ loss scales with the unit roundoff (cubic m = 30, n = 16: 5.9e-15 against 1.8e-11, ratio 3.0·10³ for an ε-ratio 2048).

(d) **Actual double dot products (REVIEWER-MEASURED; reconstruction 02, `reviews/logs_L1b/closed_loop.log`, `closed_loop_sets.log`, `open_loop.log`; not rerun by the developer).** The reviewer replaced the term-wise noise model by the actual IEEE-double window inner products (NumPy/OpenBLAS), so no u-convention is involved. [Note 2026-11-01T08:41:34+01:00, Codex audit-01 L1-later: in this `dot64` mode the long-double vectors are rounded to float64, their dot product is computed in float64, and the result is converted back to long double (`review_L1b/rv2_closed_loop.py`). The modelled rounding is therefore this specific mixed-precision operation, operand conversion included. It is a different rounding model from the Gaussian term-wise noise of (c) and does not retroactively validate that model. The closed loop was freshly rerun by the audit (`audit-01/L1-later/closed_loop_rerun.log`, C/L ∈ [0.56, 1.86]; open loop `open_loop_rerun.log`).]
   - Closed loop: everything else in long double. On the six IDEA?…-120 sets at n = 12/16/20/24, C/L lies in [0.56, 1.86] (cubic m = 30: 1.05 / 0.63 / 0.87 / 0.70; quartic: 0.77 / 0.66 / 0.87 / 0.87; cubic m = 36: 1.86 / 0.56 / 0.84 / 0.85). IDEA?…-120's written rule gives **survives on all six**.
   - Open loop: c* plus the actual rounding of the exact vectors' dot products on the off-pattern entries. E/L at n = 16/20: quadratic 1.13 / 0.53, cubic m = 30 5.13 / 4.70, quartic 21.6 / 12.9, cubic m = 36 16.4 / 21.1. IDEA?…-119's rule gives **inconclusive**; IDEA?…-118 H_term (cubic m = 30) gives **survives**.
   - The feedback damping (open/closed) at n = 16 is ≈ 1.5 (quadratic), 8 (cubic m = 30) and 30 (quartic, cubic m = 36).
   - The term-wise N(0,1) model under-estimates actual rounding: cubic m = 30, n = 16 gives C/L = 0.16 at σ = u/√3, 0.28 at σ = 2^-53 and 0.57 at σ = 2^-52. The per-term model misses the summation rounding.
   With actual rounding the (b) and (c) verdicts are therefore decided: IDEA?…-119 inconclusive, IDEA?…-120 survives, H_term survives. The noise-model versions remain convention-sensitive.

[Correction 2026-10-31T23:11Z: the (b) and (c) verdicts and the 25–100% figure depend on the noise-scale convention; see History.] Reading (MEASURED, scope as stated): dot-product rounding alone, fed back through the recurrence, accounts for 25–100% of the loss on all four clustered sets. [Qualified 2026-11-01T08:41:34+01:00, audit-01: "alone" means that dot-product rounding is the only error source of the closed-loop model — the term-wise noise model in (c), the dot64 operation of (d) with C/L 0.56–1.86. This shows sufficiency within these models. It does not show necessity or exclusive causation in an ordinary all-double run.] It is amplified by the off-pattern gains of PD-T?…-114 and damped by the feedback of the window inner products. That damping is the reason open-loop models over-estimate the loss, by about 1× (quadratic) to 10² (quartic). The size of the generic-u-noise overshoot (R06: 10⁶–10⁷) is mostly a scale effect: at the high-gain entries the dot-product terms have absolute size ≈ 10⁻⁶ u.

## Definitions

Gain of an entry = max |A + Aᵀ| over degrees ≤ n (PD-T?…-117; formula PD-T?…-114 part 3) [pointer updated 2026-11-01T08:41:34+01:00 after the split of PD-T?…-114; it read "(PD-T?…-114 part 5)"]. "Open loop" = perturbations added to the fixed exact coefficients c*; "closed loop" = perturbations added to coefficients that are recomputed from the current vectors at every step.

## Assumptions

Double precision, NumPy 2.5.3, x86 80-bit long double, single machine. The term-wise noise model ignores summation errors and is a model, not the BLAS rounding.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | MEASURED | `logs/r07_offpattern_anatomy.log` (3-digit rerun; the first 1-digit log `r07_offpattern_anatomy_1digit.log` has the same values) |
| (b) | MEASURED | `logs/r07_termwise_predictor.log` |
| (c) | MEASURED | `logs/r07_closed_loop.log` (noise model; verdict convention-sensitive, `logs/c01_u53_rerun.log`) |
| (d) | REVIEWER-MEASURED (recon-02, actual double dot products; not rerun by the developer) | `reviews/logs_L1b/closed_loop*.log`, `open_loop.log` |

## Depends on

PD-T?…-111 (product-type coefficients), -112 (coefficient channel), -114 (gain formulas), -117 (measured gains) [-117 added 2026-11-01T08:41:34+01:00].

## Checks

D(c* + h) reproduces L to three digits at n = 12…24, which checks the split bookkeeping. The closed-loop model with the noise switched off reduces to long-double BJ (not run separately; the plain long-double BJ loss is printed for comparison).

## Sources

None.

## Proof or evidence

Measured; commands in R07.md §7.

## Scope

Six checkerboards with m ∈ {30, 36}, BJ block CGS, degrees ≤ 24; a single machine and NumPy version. Not covered: non-product measures, where there is no product-type point and no on/off split; the HL ordering; ORTH/MGS; larger m.

## Open items

An analytic account of the feedback damping. The closed-loop linearisation is δh = ρ + T δh, with T strictly lower triangular, built from the window inner products of the propagated perturbations; the damping would be a property of (I − T)⁻¹ in the high-gain directions, and none is proved. Also open: a predictor built from exact data alone that keeps the feedback.

## History

- R07 (2026-10-31): created. IDEA?…-118 and -119 criteria were written before their runs; IDEA?…-120 was written before its run, but after the BJ losses of all six sets were known from the IDEA?…-118/-119 runs.
- 2026-10-31T23:11Z (re-check after reconstruction 01, B2-type convention issue; supersedes a provisional line written at 23:05Z that predicted, before the rerun, that the verdicts would not change):
  - Re-run with noise scale u = 2^-53 (the plan's unit roundoff; `logs/c01_u53_rerun.log`). Verdicts by the same rules:
    - (a) H_term: survives (5.1× / 2.3×);
    - (b) IDEA?…-119: inconclusive (quartic 60× / 11×);
    - (c) IDEA?…-120: inconclusive (quadratic 0.17 / 0.19; cubic m = 36 0.14 at n = 16).
    These verdicts are convention-sensitive. Statements independent of the convention: φ/ρ cancellation; random signs 10³× (H_sign killed); the scale effect; the growth of the open-loop over-estimate with clustering strength; and closed-loop C/L ∈ [0.14, 1.06] at n = 16, 20.
  - The Reading's "accounts for 25–100% of the loss" is corrected to "reproduces the order of magnitude (C/L between 0.14 and 1.06 depending on set and noise-scale convention)". Original wording is kept in the Statement.
  - Not affected by B1 (product-type checkerboards, dev rule).
- 2026-10-31T23:37Z (response to reconstruction 02):
  - M3: part (d) records the reviewer's convention-free resolution with actual double dot products, as REVIEWER-MEASURED. Closed loop C/L ∈ [0.56, 1.86], IDEA?…-120 survives on all six sets; open loop: IDEA?…-119 inconclusive, H_term survives.
  - m1: the title was stale after the 23:11Z correction and is restated. Original title: "PD-T?bivariate-lanczos-claude-115 — On clustered product-type checkerboards the coefficient-channel loss is closed-loop dot-product rounding through the off-pattern gains: the BJ off-pattern values are feedback-dominated and sign-structured, open-loop models over-estimate, the closed-loop model reproduces the loss".
  - M1: the results are dev-rule statements. On the cubic checkerboard the alt rule gives 3.1e-13 and adapt 9.3e-6 at n = 24 against dev 1.0e-6 (recon-02); the coefficient-channel mechanism under other rules is not analysed.
- 2026-11-01T08:41:34+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-later notes on T115 and the mixed-precision dot64 code; LL-M2 pointers). The title said the loss "is" closed-loop dot-product rounding. It now says that closed-loop dot-product rounding "reproduces" it (sufficiency within the tested models), and the dot64 description includes the operand conversion. (d) and the Reading are qualified accordingly. Pointers to PD-T?…-114 part 5 now go to PD-T?…-117. Original title: "PD-T?bivariate-lanczos-claude-115 — On clustered product-type checkerboards (dev rule) the coefficient-channel loss is closed-loop dot-product rounding through the off-pattern gains. The BJ off-pattern values are feedback-dominated and sign-structured, open-loop models over-estimate, and the closed loop with actual double dot products reproduces the loss (reviewer-measured); the term-wise noise model does so only up to a convention-dependent factor". Status (MEASURED) unchanged.
