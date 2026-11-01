# PD-T?bivariate-lanczos-claude-112 — Checkerboard control and near-product measurements (R04): two error channels, and a product-type measure with strong loss

Final ID: **PD-T040** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: checkerboard control; coefficient channel vs vector channel; exact split Q̂ = Ξ̄ − Φ̃ measured; rotation-angle sweep.
Split from: none.
Split into: none.

## Statement

[FP, MEASURED] BJ window recurrence (block window, CGS), u := 2^-52.

(a) **Checkerboards (m = 30, M = 496, e = 0; PD-T?…-111).** Window coefficients agree with the product reference to 8.9e-16 (Chebyshev–Lobatto), 5.3e-15 (equispaced), 1.0e-6 in double / 9.4e-10 in long double (cubic clustering; bivariate weights 1.8e-67…0.47, x-factor weights 1.7e-33…0.47, y-factor 5.3e-35…0.48 — PC-12 applied 2026-11-01T08:41:34+01:00). Loss: Chebyshev–Lobatto flat at 3e-15 up to completion; equispaced grows mildly to 1e-13 (t = 28) and 2e-13 (t = 30); clustered grows from t ≈ 12: 3e-14, 1e-11, 4e-9, 9e-7, 7e-5 at t = 12, 16, 20, 24, 28, while univariate Lanczos on the factors stays ≤ 5e-16 up to step 20. The clustered growth scales with u (long double: 7e-15 at t = 16, 3e-8 at t = 28), is also present with block-window CGS2 and with HL/ORTH (so not a local Gram–Schmidt effect), and is not predicted by Ritz residuals (u/ρ_Z ≤ 4e-14, u/ρ_{H_x}, u/ρ_{H_y} ≤ 4e-11 up to t = 24).
(b) **Two error channels (exact split, PD-T?…-104).** Re-running the computed recurrence in long double from q̂_0 without forcing gives Ξ̄, and Φ̃ := Ξ̄ − Q̂ is the propagated vector-operation error. On the square rotated by π/4 the loss is carried by Φ̃ (|Φ̃| = 5e-12, 3e-9, 4e-6 vs loss 6e-12, 2e-9, 2e-6 at n = 12, 16, 20: vector channel); on the square both are at the same level (Ritz-type, vector channel); on the clustered checkerboard |Φ̃| stays at 4e-16–9e-16 up to n = 20 while the loss equals the Gram defect of Ξ̄ (1e-11 at n = 16): **coefficient channel** — the computed coefficients themselves define polynomials that are not orthonormal for μ.
(c) **Predictors.** The node-propagator response with uniform forcing u/√M (R02) or with componentwise-scaled forcing reproduces the vector channel (within 1–8× on square, rotated square, disk) but misses the coefficient channel (clustered checkerboard: response 4e-15 vs loss 1e-11 at n = 16) and still under-predicts the triangle (25× at n = 12, 350× at n = 16 with scaled forcing); a worst-case coefficient-noise model (absolute inner-product error u‖q̂_l‖‖Aq̂_p‖ on every window entry) over-predicts by up to 10⁷ (clustered) and 40× (square).
(d) **Two-relation control fails on the clustered checkerboard.** The two-relation block recurrence of PD-T?…-109 (b) loses orthogonality catastrophically there (1e-11, 1e-5, 1e-3, 0.4 at n = 8, 12, 16, 20).
(e) **Rotation sweep (exact-coefficient propagator, square M = 1681 seed 11, rate between n = 12 and 24; the "exact" coefficients are a double CGS2 computation against all previous columns, not certified exact, so these are measurements of the computed reference coefficients — note 2026-11-01T08:41:34+01:00, audit-01).** Excess growth rate over θ = 0: 0.010, 0.026, 0.126, 0.308, 0.879, 1.245 per degree at θ = 0.0125, 0.025, 0.05, 0.1, 0.2, 0.4; excess/θ = 0.80, 1.02, 2.52, 3.08, 4.39, 3.11 (superlinear onset for θ ≲ 0.2).
(f) **Near-product bound informativeness (PD-T?…-110).** No violation; median log10(bound/actual) at (s, t) = (0, 20): 0.4 (tensor 41²), 10.4 (random square vs product of its marginals; median max_t ε_t = 0.95), 13.6 (rotation 0.05), 27.8 (rotation 0.3).

## Definitions

As in PD-T?…-104, -107, -110, -111.

## Assumptions

IEEE double / x87 long double; seeds and sets as listed; weights |1/ω′| normalised.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | MEASURED | `logs/r04_checkerboard.log`, `r04_checkerboard_diag.log`, `r04_checkerboard_local.log`, `r04_checkerboard_ritz.log`, `r04_checkerboard_more.log` |
| (b) | MEASURED | `logs/r04_actual_forcing.log` |
| (c) | MEASURED | `logs/r04_scaled_predictor.log`, `r04_coef_forcing.log`, `r04_checkerboard_diag.log` |
| (d) | MEASURED | `logs/r04_checkerboard_more.log` |
| (e), (f) | MEASURED | `logs/r04_near_product.log`; producer rerun by Codex audit-01 (`audit-01/L1-later/near_product_producer_rerun.log`: zero violations; informativeness 10.4/13.6/27.8/0.4 decades; nodes 28/28/28/27) |
| mechanism of the coefficient channel on clustered product-type measures | OPEN | not explained by any tested model |

## Depends on

PD-T?…-104 (split), -110, -111.

## Checks

Commands: R04.md §5. Independent rerun: none yet.

## Sources

Liu–Narayan, arXiv 2202.04843 (multivariate Stieltjes): read only through a WebFetch model summary of the PDF on 2026-10-31 (not a direct reading): the summary reports that evaluation there stacks all coordinates' relations (Thm 3.1, eq. (9)), that one coordinate's relation is called insufficient in isolation (§3.1), no stability comparison of single vs stacked relations, and degraded orthogonality on a holed square and a Madagascar-shaped domain attributed to conditioning (§6.2). Barrio–Peña–Sauer, "Three term recurrence for the evaluation of multivariate orthogonal polynomials" (cited there as [1]): not found/read — pending-reference.

## Proof or evidence

Measured; see logs.

## Scope

m = 30 checkerboards, M = 1681 random sets, n ≤ 30. Item (a) shows that product-type exact coefficients do **not** by themselves guarantee small loss in floating point when the weights span many orders of magnitude; PD-T?…-105's factorisation is a statement about the propagator (vector channel), which stays bounded there (b, c).

## Open items

Explain the coefficient channel (candidate: conditioning of the coefficient map for weights spanning 67 decades (33 per factor) [corrected 2026-11-01T08:41:34+01:00, PC-12; it read "33 decades"], amplified through the polynomial recurrence — untested); a predictor that captures both channels.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R04).
- 2026-10-31T23:05Z (re-check after reconstruction 01):
  - All loss measurements here use the dev (BJ) parent rule (B1, PD-N?…-105: other rules change non-product losses by 10³–10⁸); (e) the rotation sweep and (f) the informativeness are dev-rule statements.
  - (d) is consistent with the narrowed PD-T?…-109 (b): the two-relation control is not a general remedy (also tensor, Gaussian and triangle, recon-01).
  - The clustered checkerboard is a product-type measure with strong loss, which is in line with recon-01's finding that the support does not classify the regime (PD-N?…-106).
  - Pending corrections PC-11 and PC-12 (candidates.md) are to be read with (a).
- 2026-10-31T23:37Z (response to reconstruction 02):
  - (a), (b), (d) are CONFIRMED by recon-02's independent rerun (cubic: 7.2e-16 … 1.0e-6 at n = 8…24).
  - m10 (PC-11): the on-pattern deviation 1.6e-14 excludes β; including β, recon-02 measures 3.0e-13 over degrees ≤ 24. Harmless either way, as the on-pattern-only D shows.
  - M1: all loss values are dev-rule; the alt rule gives 3.1e-13 at n = 24 on the cubic set (PD-N?…-105, extension).
- 2026-11-01T08:41:34+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-later table notes on T112(a,b) and T112(e,f)). (a): the pending correction PC-12 is applied. The quoted 1.7e-33…0.47 is the x-factor range; the bivariate range is 1.8e-67…0.47. The open item's "33 decades" becomes 67. (e): the reference coefficients of the near-product producer are a double full-CGS2 computation ("'exact' to ~1e-15" in the producer's docstring) and orthogonality does not certify exact coefficients, so (e) is a measurement for the computed reference coefficients. The audit's producer rerun is cited for (e), (f). Original wording: "(cubic clustering, weights 1.7e-33…0.47)", "(e) **Rotation sweep (exact-coefficient propagator, square M = 1681 seed 11, rate between n = 12 and 24).**", "weights spanning 33 decades". Status (MEASURED) unchanged.
