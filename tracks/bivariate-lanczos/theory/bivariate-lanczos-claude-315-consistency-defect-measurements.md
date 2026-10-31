# PD-T?bivariate-lanczos-claude-315 — MEASURED: consistency defect of computed sections tracks the loss of orthogonality; no first-order Greenbaum regime in the tested runs

ID kind: PD-T.
Aliases: asymmetry vs loss; first-order consistent (weight-only) fit; reading (G) measurements; R06.
Split from: none (measured companion of PD-T?…-314 and of the target 300, reading (G)).
Split into: none.

## Statement

MEASURED (BJ: block window, classical Gram–Schmidt, no reorthogonalisation; L1's `l1_recurrence.py`; M = 1681 uniform weights):
1. Rotated random square (θ = 0.3): asym_J/loss = 2.2–10.2, fwd_J ≈ asym_J, asym_F/loss = 0.005–0.09, for n = 10..26 (loss 1.3e-14 … 7.3e-3).
2. Random square: asym_J ≈ (0.7–1)·loss ≈ fwd_J for n = 20..40 (loss up to 2.7e-9); asym_F ≤ 3.6e-13 while fwd_F ≈ 0.09·loss at n = 36–40, i.e. the raw F data are inaccurate but NEARLY SYMMETRIC (asym_F/fwd_F ≈ 1.5e-3–2.4e-3). Since asym_J ≈ fwd_J is a property of the completion, this is a Greenbaum-like counter-indication on the random square, not evidence against a Greenbaum regime there.
3. Tensor Chebyshev 41²: no loss (2.1e-14) and asym ≤ 1.7e2·u for n ≤ 40.
4. [Corrected per finding M1: the double-precision Householder reference is inadequate at n ≤ 15–20 — 22–56% of ‖e‖ at n ≤ 15 is the reference's own error; with the reviewer's 80-bit long-double CGS2 reference the least-squares minimiser stays in the linear regime up to n = 20 (max|η|/w_min ≤ 4e-3) with ρ = 0.45–0.79, and K15 is killed in the linear regime at n = 18, 19, 20 (ρ = 0.65–0.74, loss ≥ 1e-9); the block-window extras contribute ≤ 0.07 of ‖e‖ (L3-reconstruction-02, `consistency_recheck.py`, a different rounding realisation). The developer's original item 4 follows, kept for the record; its "leaves the linear regime for n ≥ 16" statement is an artefact of the reference.] First-order best consistent fit of the computed partial data (all computed F-coefficients incl. block-window extras, computed J-columns): rotated square ρ = ‖Jη* − e‖/‖e‖ = 0.70, 0.74 at n = 14, 15 (minimiser in the linear regime); for n = 16..26, ρ = 0.68…0.23 but with max|η*|/w_min = 1.8…1.8e7 (outside the linear regime; not an achievable fit). Random square n = 22..27: ρ ≈ 0.86 at the accuracy floor (inconclusive).
So, on the rotated square (the only set where the fit is resolved; M = 1681, BJ/CGS, linear regime n ≤ 20), the completed data are as inconsistent as they are inaccurate, and no consistent section pair in the linear neighbourhood of Φ(μ) removes more than ≈ 55% of the forward error. On the random square the claim is NOT supported (finding M2): the inaccurate F data are nearly symmetric and the fit is at the reference floor.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| items 1–4 | MEASURED | logs `directions/L3/logs/r06_*`; no general claim |

## Depends on / Checks

PD-T?…-314 (interpretation of asymmetry); commands in R06 §5. No independent rerun yet.

## Proof or evidence

Measurements only. Reference sections from a Householder QR of the weighted Chebyshev–Vandermonde matrix (accuracy floor ≈ 1e-15–1e-14 for these sizes).

## Scope

As stated; HL/ORTH, O(1) loss, other supports and larger M untested.

## Open items

A priori relation between asymmetry and L1's commutator residual; bounded positive-weight fits for n ≥ 16.

## History

2026-10-31T23:52+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer, round R06.
- 2026-11-01T00:47:14+01:00, L3 developer (Claude Opus 5.5, xhigh requested): findings M1 (reference artefact; 80-bit reference results cited), M2 (claim restricted to the rotated square; random-square counter-indication recorded) and L3 (ranges) of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1). Original wording of the replaced passages: «1. Rotated random square (θ = 0.3): asym_J/loss ≈ 4–10, fwd_J ≈ asym_J, asym_F ≈ (0.03–0.06)·loss, for n = 10..26 (loss 1.3e-14 … 7.3e-3).»; «2. Random square: asym_J ≈ (0.7–1)·loss ≈ fwd_J for n = 20..40 (loss up to 2.7e-9); asym_F ≤ 3.6e-13.»; «4. First-order best consistent fit of the computed partial data»; «So, within the tested scope, the computed coefficients are as inconsistent as they are inaccurate, and no consistent section pair in the linear neighbourhood of Φ(μ) fits them better than ≈ 0.7 × the forward error.».
