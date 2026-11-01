# PD-T?bivariate-lanczos-claude-110 — Near-product upper bound for the per-node propagator via block transfer matrices (perturbed-product lemma)

Final ID: **PD-T038** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: discrete-Gronwall transfer bound; near-product upper bound; product-of-marginals reference bound.
Split from: none.
Split into: none.

## Statement

[EXACT, with exact window coefficients] Let L*(z) be the node-propagator matrix of a measure μ (PD-T?…-104, exact coefficients), ordered by degree blocks P_t ∈ R^{t+1}. Row block t of L*(z)P = −Φ reads

  D_t P_t = G_t(z) P_{t−1} + E_t P_{t−2} − Φ_t,

with D_t ∈ R^{(t+1)×(t+1)} lower triangular (diagonal β's, strictly lower part = within-degree coefficients), G_t(z) ∈ R^{(t+1)×t} (the parent entry a_k(z) − h minus the other degree-(t−1) coefficients) and E_t ∈ R^{(t+1)×(t−1)} (minus the degree-(t−2) coefficients). Define V_t = (P_t; P_{t−1}) and the block transfer matrices T_1(z) = [D_1⁻¹G_1; I_1], T_t(z) = [[D_t⁻¹G_t, D_t⁻¹E_t], [I_t, 0]] (t ≥ 2). Then:

1. **(Transfer representation.)** The response to a forcing in block s alone is P_t = [T_t(z)⋯T_{s+1}(z)]_{1st block row} (D_s⁻¹(−Φ_s); 0), so ‖(L*(z)⁻¹)_{[t],[s]}‖₂ ≤ ‖T_t(z)⋯T_{s+1}(z)‖₂ ‖D_s⁻¹‖₂ for s < t, and the diagonal block is −D_t⁻¹ [note 2026-10-31T23:37Z, recon-02 m7: this is the block of the map Φ ↦ P = −L*⁻¹Φ; the diagonal block of L*⁻¹ itself is +D_t⁻¹. Norms are unaffected].
2. **(Perturbed-product lemma.)** For matrices T⁰_r, ΔT_r of compatible sizes and K ≥ 1 with ‖T⁰_b⋯T⁰_a‖₂ ≤ K for all a ≤ b (empty product = I), every product of the perturbed matrices satisfies ‖(T⁰_b + ΔT_b)⋯(T⁰_a + ΔT_a)‖₂ ≤ K Π_{r=a}^{b}(1 + K‖ΔT_r‖₂).
3. **(Near-product bound.)** Let μ⁰ be any measure with product-type window coefficients (PD-T?…-105 part 1; e.g. the product of the marginals of μ), T⁰_r(z) its transfers at the same point z, K(z) := max(1, sup_{s<b≤n} ‖T⁰_b(z)⋯T⁰_{s+1}(z)‖₂) and ε_r(z) := ‖T_r(z) − T⁰_r(z)‖₂. Then for all s < t ≤ n
  ‖(L*(z)⁻¹)_{[t],[s]}‖₂ ≤ ‖D_s⁻¹‖₂ K(z) Π_{r=s+1}^{t}(1 + K(z)ε_r(z)) ≤ ‖D_s⁻¹‖₂ K(z) exp(K(z) Σ_r ε_r(z)).
  By PD-T?…-105 the reference transfers factorise into univariate (Jacobi) chains, so K(z) is a univariate quantity of the reference marginals at (x, y).

## Definitions

Exact window coefficients as in PD-T?…-104/-105; block window or exact window (the bound holds for either). Norms: spectral.

## Assumptions

U(n+1) for μ and μ⁰; β > 0. Exact arithmetic for the coefficients (or, as a statement about the computed propagator, any coefficients: parts 1–3 hold verbatim with the computed ones).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. transfer representation | PROVED (routine) | proof below; numerical check: transfer product vs direct inverse agree to 4.9e-15 (smoke check, R04 §5) |
| 2. perturbed-product lemma | PROVED | proof below |
| 3. near-product bound | PROVED (combination of 1, 2) | consistency (MEASURED verification record): 0 violations over 210 (s, t) pairs at 28 sampled nodes on each of the three random sets and 27 on tensor 41² (after deduplication) (`logs/r04_near_product.log`; producer rerun by Codex audit-01, `audit-01/L1-later/near_product_producer_rerun.log`). The reference coefficients are a double full-CGS2 computation, not certified exact, so this checks the inequality for the computed reference data |
| informativeness — cross-reference, not a claim of this file | MEASURED in PD-T?…-112 (f) | informative (≤ 0.4 decades) only for exact product measures; 10–28 decades for the random square and its rotations against the product of the marginals |

## Depends on

PD-T?…-104 (node propagator), PD-T?…-105 (factorised reference).

## Checks

`tracks/bivariate-lanczos/code/L1/l1_r04_near_product.py` (functions `transfers`, `product_norms`, `near_product_check`).

## Proof or evidence

*1.* Block t of L*(z)P = −Φ is the displayed equation (rows of degree t only involve unknowns of degrees t, t−1, t−2 for either window). With Φ supported in block s, P_r = 0 for r < s, P_s = −D_s⁻¹Φ_s, and for r > s, V_r = T_r V_{r−1}.
*2.* Write Π_{[a,b]} = T_b⋯T_a (T = T⁰ + ΔT), Π⁰ likewise, Π_{[a,a−1]} = I. Telescoping: Π_{[a,b]} − Π⁰_{[a,b]} = Σ_{r=a}^{b} Π⁰_{[r+1,b]} ΔT_r Π_{[a,r−1]} (each summand equals Π⁰_{[r+1,b]}Π_{[a,r]} − Π⁰_{[r,b]}Π_{[a,r−1]}). Hence x_b := ‖Π_{[a,b]}‖ ≤ K + K Σ_{r=a}^{b} ε_r x_{r−1} with x_{a−1} = 1. Let y_b := K Π_{r=a}^{b}(1 + Kε_r), y_{a−1} := K; then y_b = K + Σ_{r=a}^{b} Kε_r y_{r−1}. Induction: x_{a−1} = 1 ≤ y_{a−1}, and if x_r ≤ y_r for r < b then x_b ≤ K + KΣ ε_r y_{r−1} = y_b.
*3.* Apply 2 with T⁰_r = T⁰_r(z), ΔT_r = T_r(z) − T⁰_r(z) to the product in 1; 1 + a ≤ e^a.

## Scope

A true but, in practice, weak bound: it is informative only when Σ_r ε_r ≲ 1/K. Measured: for exact product measures ε ≈ 1e-15 and the bound is within 0.4 decades; for the random square the product of its marginals is not close at the transfer level (median max_t ε_t ≈ 0.95 at n = 20), so the bound is 10 decades above the actual product norm, and 14–28 decades for rotations by 0.05–0.3 (`logs/r04_near_product.log`). It does not explain why the random square is stable; it only bounds the propagator for (near-)exact product measures, extending PD-T?…-105 quantitatively.

## Open items

A reference closer than the product of the marginals (e.g. a product measure in rotated/optimised coordinates) and a norm adapted to the chain structure, to make the bound informative for near-product empirical measures.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R04).
- 2026-10-31T23:05Z (re-check after reconstruction 01, which covered R01–R03 only): not affected by B1/B2. The bound is exact algebra for the propagator L*(z) of the dev selection; the same transfer argument applies to any selection with a degree-block structure. The informativeness measurements (PD-T?…-112 (f)) use the dev rule.
- 2026-10-31T23:37Z (response to reconstruction 02): CONFIRMED by recon-02 (proof re-derived). The m7 sign note is added in part 1. The informativeness numbers were not rerun by the reviewer.
- 2026-11-01T08:41:34+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-later table note on T112(e,f)/N103(a)). The consistency row said "28 nodes × 210 pairs × 4 sets". The log shows 28 sampled nodes on the three random sets and 27 on tensor 41² after deduplication, and the row now says so. It also notes that the reference coefficients are computed, not certified exact. The informativeness row is relabelled as a cross-reference to PD-T?…-112 (f). Original rows: "| 3. near-product bound | PROVED (combination of 1, 2) | consistency: 0 violations over 28 nodes × 210 pairs × 4 sets (`logs/r04_near_product.log`) |" and "| informativeness | MEASURED (PD-T?…-112 records the numbers) | …". The theorem and its status (PROVED) are unchanged.
