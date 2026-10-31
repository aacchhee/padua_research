# PD-T?bivariate-lanczos-claude-115 — On clustered product-type checkerboards the coefficient-channel loss is closed-loop dot-product rounding through the off-pattern gains: the BJ off-pattern values are feedback-dominated and sign-structured, open-loop models over-estimate, the closed-loop model reproduces the loss

ID kind: PD-T.
Aliases: off-pattern error anatomy; closed-loop dot-product model; φ/ρ split; feedback cancellation.
Split from: none (continues PD-T?…-114).
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

Reading (MEASURED, scope as stated): dot-product rounding alone, fed back through the recurrence, accounts for 25–100% of the loss on all four clustered sets. It is amplified by the off-pattern gains of PD-T?…-114 and damped by the feedback of the window inner products. That damping is the reason open-loop models over-estimate the loss, by about 1× (quadratic) to 10² (quartic). The size of the generic-u-noise overshoot (R06: 10⁶–10⁷) is mostly a scale effect: at the high-gain entries the dot-product terms have absolute size ≈ 10⁻⁶ u.

## Definitions

Gain of an entry = max |A + Aᵀ| over degrees ≤ n (PD-T?…-114 part 5). "Open loop" = perturbations added to the fixed exact coefficients c*; "closed loop" = perturbations added to coefficients that are recomputed from the current vectors at every step.

## Assumptions

Double precision, NumPy 2.5.3, x86 80-bit long double, single machine. The term-wise noise model ignores summation errors and is a model, not the BLAS rounding.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | MEASURED | `logs/r07_offpattern_anatomy.log` (3-digit rerun; the first 1-digit log `r07_offpattern_anatomy_1digit.log` has the same values) |
| (b) | MEASURED | `logs/r07_termwise_predictor.log` |
| (c) | MEASURED | `logs/r07_closed_loop.log` |

## Depends on

PD-T?…-111 (product-type coefficients), -112 (coefficient channel), -114 (gains).

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
