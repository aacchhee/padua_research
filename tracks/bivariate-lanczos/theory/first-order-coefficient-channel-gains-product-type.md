# PD-T?bivariate-lanczos-claude-114 — On product-type measures the first-order Gram sensitivity of the window coefficient map is given by univariate data: structurally permitted (on-pattern) entries have univariate gains, structural-zero (off-pattern) entries have cross-variable gains

Final ID: **PD-T042** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: coefficient-channel gain identity; on/off-pattern split; first-order coefficient channel; structural-zero gains.
Split from: none (explains PD-T?…-112 (a, b), "coefficient channel").
Split into: PD-T?bivariate-lanczos-claude-117 (`coefficient-channel-gain-census-checkerboards-measured.md`, MEASURED): the former part 5 (gain census, first-order predictions and their reading) and the former title clause "the clustered-checkerboard loss is this first-order channel". Split 2026-11-01T08:33:59+01:00, Codex audit-01 LL-M2.

## Statement

Let μ = Σ_i w_i δ_{z_i}, z_i = (ξ_i, η_i), be a positive discrete measure (Σ w_i = 1) and μ⁰ = μ_X ⊗ μ_Y a product of probability measures such that ∫ f dμ = ∫ f dμ⁰ for all f ∈ Π_{2n} (PD-T?…-111 hypothesis, with c = 1). Let p_s, r_s be the orthonormal polynomials of μ_X, μ_Y with Jacobi coefficients (a^x_s, b^x_s), (a^y_s, b^y_s). Use the BJ ordering of PD-T?…-101 (column k = (t, j) ↔ x^{t−j} y^j; (t, 0) = X·(t−1, 0), (t, j ≥ 1) = Y·(t−1, j−1)) and the block window W_k. For window coefficients c = (h_k, β_k)_k define the coefficient map Ξ(c): ξ_0 = √w/‖√w‖, ξ_k = (a_k ⊙ ξ_{p(k)} − Ξ_{W_k} h_k)/β_k (a_k = x or y), and let c* be the product-type coefficients (PD-T?…-105 part 1), so ξ*_k = √w ⊙ p_{t−j}(ξ) r_j(η) and Ξ*ᵀΞ* = I up to degree n. For a window entry (k, l), k = (t, j), l = (t_l, j_l), write i = t − j, i_l = t_l − j_l and ψ_l = p_{i_l}(ξ) r_{j_l}(η). Let G^{y,[j]} be the solution of the homogeneous y-recurrence with G_{j−1} = 0, G_j = 1/b^y_j (G_{s+1} = ((η − a^y_s)G_s − b^y_s G_{s−1})/b^y_{s+1}), and G^{x,[t]} likewise for x.

1. **[EXACT] Variation.** ∂Ξ/∂h_{k,l} at c* equals −R^{(k,l)}, where R^{(k,l)}_c = 0 for c < k, R_k = ξ*_l/β*_k, R_c = (a_c ⊙ R_{p(c)} − R_{W_c} h*_c)/β*_c for c > k.
2. **[EXACT] Tree propagation.** R^{(k,l)} vanishes off the descendants of k and, as node values divided by √w,
   - j ≥ 1: R_{(t+r, j+r)} = ψ_l · G^{y,[j]}_{j+r}(η), r ≥ 0;
   - j = 0: R_{(i′+r, r)} = ψ_l · G^{x,[t]}_{i′}(ξ) · r_r(η), i′ ≥ t, r ≥ 0.
3. **[EXACT] Gram derivative by univariate data.** ∂(ΞᵀΞ)/∂h_{k,l} = −(A + Aᵀ) on degrees ≤ n, with A = Ξ*ᵀR^{(k,l)} and, for e = (a, b),
   - j ≥ 1: A_{e,(t+r, j+r)} = δ_{a−b, i_l} · ⟨r_b, r_{j_l} G^{y,[j]}_{j+r}⟩_{μ_Y};
   - j = 0: A_{e,(i′+r, r)} = ⟨p_{a−b}, p_{i_l} G^{x,[t]}_{i′}⟩_{μ_X} · ⟨r_b, r_{j_l} r_r⟩_{μ_Y}.
   (A β_k-perturbation: ∂ξ_k/∂β_k = −ξ*_k/β*_k, so the derivative is −R^{(k,k)}, the case l := k with no extra weight. Corrected 2026-10-31T23:37Z, recon-02 m8; original: "(A β_k-perturbation is the case l := k with weight β*_k.)")
4. **[EXACT] On/off split.** A window entry is on-pattern — structurally permitted in c*, i.e. at a position where the product-type coefficient may be nonzero; it can vanish, e.g. a^y_{j−1} = 0 for a symmetric marginal — iff i_l = i for j ≥ 1, resp. j_l = 0 for j = 0. For on-pattern entries, the derivative in part 3 is exactly the Gram derivative of the univariate coefficient map of μ_Y, replicated on the x-degree-i chain. It is taken with respect to the h-coordinate whose product-type value is a^y_{j−1} (if j_l = j−1) or b^y_{j−1} (if j_l = j−2). For j = 0 it is the corresponding map of μ_X (h-coordinates with values a^x_{t−1}, b^x_{t−1}), replicated on each y-degree. As in the bivariate map, the h- and β-coordinates of the univariate map are independent. A perturbation of the Jacobi parameter b^y_{j−1} itself, which is also the β-coordinate of column j−1, combines the two coordinate derivatives. [Wording corrected 2026-11-01T08:33:59+01:00, audit-01 LL-L2; original in History.] Off-pattern entries have derivatives with a cross-variable factor that the univariate maps do not contain: ⟨r_b, r_{j_l} G^{y,[j]}_{j+r}⟩ with j_l unrelated to j (j ≥ 1), or the linearisation coefficient ⟨r_b, r_{j_l} r_r⟩_{μ_Y} with j_l ≥ 1 (j = 0).
5. **[Moved]** The measurements formerly stated here (gain census on two m = 30 checkerboards and the first-order coefficient-channel predictions) are PD-T?bivariate-lanczos-claude-117 (MEASURED) [split 2026-11-01T08:33:59+01:00, Codex audit-01 LL-M2; original wording in History]. Their numerical check of part 3 is kept below under Checks as a verification record.

## Definitions

D(c, n) = max |Ξ(c)_nᵀ Ξ(c)_n − I| over the columns of degree ≤ n. "On-pattern" = window positions where the product-type coefficient may be nonzero ((t−1, 0), (t−2, 0) for J-columns; (t−1, j−1), (t−2, j−2) for F-columns), "off-pattern" = all other window positions (structural zeros of c*). Off-pattern values of the BJ run are the computed inner products q̂_lᵀ(a q̂_{p(k)}).

## Assumptions

Part 1: none beyond the recursion. Parts 2–4: product-type c* (true under the moment-matching hypothesis by PD-T?…-111 part 1) and moments matched up to degree 2n, which is what makes the inner products of degree-≤-n polynomials equal under μ and μ⁰. (The precision assumptions of the former part 5 are in PD-T?…-117. Those of the verification record: long double for Ξ, c*, the formula and the direct check.)

## Status by part

Overall status: PROVED. [Before 2026-11-01T08:33:59+01:00: "parts 1–4 PROVED; part 5 MEASURED"; part 5 is now PD-T?…-117.]

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. variation | PROVED | chain rule, below |
| 2. tree propagation | PROVED | induction, below |
| 3. Gram derivative | PROVED | moment matching + Fubini, below |
| 4. on/off split | PROVED | reading of part 3 |

## Depends on

PD-T?…-101 (ordering, windows), PD-T?…-105 part 1 (product-type values), PD-T?…-111 part 1 (moment matching ⇒ product type); the univariate ingredient (first-order variation of a three-term recurrence through associated solutions) is classical.

## Checks

Verification record (MEASURED; adds no claim and does not affect the PROVED status):
- Part 3 against direct propagation on the Harris–Simanek checkerboards m = 30 (cubic-clustered and equispaced, degrees ≤ 20), 91 sampled entries per set. |A_direct − A_formula| ≤ 1.1e-14·‖R_d‖ (clustered) and 1.6e-15·‖R_d‖ (equispaced); the pre-stated criterion 1e-8 is met.
- Univariate orthonormality of p_s, r_s on the factor measures: 7.1e-16, 1.7e-16 (clustered), 3.4e-17, 6.9e-17 (equispaced).
- Command: `python3 -I tracks/bivariate-lanczos/code/L1/l1_r06_gain_identity.py > …/logs/r06_gain_identity.log` (35 s). The producer was rerun by Codex audit-01 (`audit-01/L1-later/gain_producer_rerun.log`), with formula errors 1.1e-14 / 1.6e-15 reproduced.
- [Moved here 2026-11-01T08:33:59+01:00 from part 5's first bullet.] The first-order predictions against the nonlinear long-double values of IDEA?…-117 are PD-T?…-117 (b).

## Proof or evidence

1. Columns c < k do not depend on h_k. ∂ξ_k/∂h_{k,l} = −ξ*_l/β*_k. For c > k the coefficients of c are fixed, so ∂ξ_c = (a_c ⊙ ∂ξ_{p(c)} − ∂Ξ_{W_c} h*_c)/β*_c. Hence ∂Ξ = −R.
2. With c* product type, column (t′, j′), j′ ≥ 1, uses only (t′−1, j′−1), (t′−2, j′−2) with the y-Jacobi coefficients; column (t′, 0) uses only (t′−1, 0), (t′−2, 0) with the x-Jacobi coefficients. So R obeys univariate recurrences along the x-chain {(t′, 0)} and along each y-chain {(i′ + r, r)} (fixed x-degree i′), and a chain is driven only by its own earlier members and, for a y-chain, by its base (i′, 0). For j ≥ 1 the forcing enters the y-chain of x-degree i at position j with R below j zero, so R_{(i+s, s)} = ψ_l G^{y,[j]}_s (s ≥ j); no other chain contains k. For j = 0 the x-chain carries ψ_l G^{x,[t]}_{i′}; the y-chain on (i′, 0) starts from zero predecessor, so it multiplies by r_r(η) (r_0 = 1 since μ_Y is a probability measure).
3. A_{e,d} = ∫ p_{a−b}(ξ) r_b(η) R_d dμ. Degrees: for j ≥ 1, deg ψ_l G_{j+r} ≤ t_l + r ≤ t + r = deg d; for j = 0, t_l + (i′ − t) + r ≤ i′ + r = deg d. So the integrand has degree ≤ 2n, the integral equals its μ⁰ value, and it factorises by Fubini into the stated univariate integrals (⟨p_{a−b}, p_{i_l}⟩ = δ_{a−b, i_l} in the case j ≥ 1). The Gram derivative of ΞᵀΞ at c* is (∂Ξ)ᵀΞ* + Ξ*ᵀ∂Ξ = −(Aᵀ + A).
4. In the case j ≥ 1, window degrees t−2..t with i_l = i force j_l ∈ {j−2, j−1}, the on-pattern positions; then the y-factor is ⟨r_b, r_{j_l}G^{y,[j]}_s⟩, which is the derivative of ⟨r̃_b, r̃_s⟩_{μ_Y} for the univariate recurrence with the h-coordinate of value a^y_{j−1} (j_l = j−1) or b^y_{j−1} (j_l = j−2) perturbed, the other coordinates fixed (same variation argument in one variable) [wording 2026-11-01T08:33:59+01:00, LL-L2; it read "with a^y_{j−1} (j_l = j−1) or b^y_{j−1} (j_l = j−2) perturbed"]. In the case j = 0, j_l = 0 gives ⟨r_b, r_0 r_r⟩ = δ_{b,r} and the univariate x-derivative. All other entries keep a factor with an index j_l (or i_l) not tied to the chain.
5. (Moved: measurements, PD-T?…-117; verification record under Checks.)

## Scope

Exact first-order statements at the product-type point c* (BJ ordering, block window; the HL ordering follows by x ↔ y symmetry, History 23:05Z). Not covered: second-order terms; non-product measures (no product point c* exists); other parent rules, which break the chain structure used in parts 2–4. The measurements (two checkerboards, m = 30, degrees ≤ 20) are PD-T?…-117. [Scope reworded 2026-11-01T08:33:59+01:00 after the LL-M2 split; original: "Exact first-order statements at the product-type point c*; the measured part covers two checkerboards (m = 30), BJ ordering, block window, degrees ≤ 20. Not covered: second-order terms (the n = 24 values in IDEA?…-117 are beyond first order for the u-noise draws, D ≈ 6), non-product measures (no product point c* exists), the HL ordering (mirror image, not run), the reason the BJ off-pattern errors are so much more benign than generic u-noise (R07)."]

## Open items

Size of the cross-variable factors in terms of the factor measures (an elementary bound is |⟨r_b, r_{j_l} r_r⟩| ≤ max_η |r_{j_l}(η)| ≤ (min_η w^Y)^{-1/2} over the support of μ_Y; nothing sharper is proved). Which structure of the BJ off-pattern errors keeps them away from the high-gain directions (R07): a measurement question, now recorded with PD-T?…-117 and PD-T?…-115.

## History

- R06 (2026-10-31): created after the IDEA?…-117 run (the identity was derived after seeing that the off-pattern entries carry the loss; the numerical check criterion was written before the check run, candidates.md R06 note).
- 2026-10-31T23:05Z (re-check after reconstruction 01): not affected by B1/B2. Exact algebra at a product-type point, BJ (dev) ordering; the HL mirror is covered by x ↔ y symmetry; other parent rules are not covered.
- 2026-10-31T23:37Z (response to reconstruction 02):
  - Parts 1–4 CONFIRMED (re-derived by recon-02); part 5's on/off split was reproduced independently, the gain magnitudes were not rerun.
  - m8: the β-perturbation parenthesis is corrected.
  - M1: all of part 5 is a dev-rule statement. On the same cubic checkerboard, recon-02 measures the loss at n = 24 as dev 1.0e-6, mirror 2.7e-7, alt 3.1e-13, adapt 9.3e-6. The off-pattern channel under the alt and adapt rules is not analysed (other rules break the chain structure used in parts 2–4).
- 2026-11-01T08:33:59+01:00 (Claude Opus 5.5, xhigh; response to Codex audit-01, L1-later LL-M2 and LL-L2; branch head 5f52331). The status of parts 1–4 is unchanged (PROVED); the file is now PROVED overall.
  - LL-M2 split: part 5 and its closing reading move to PD-T?…-117 (MEASURED). The formula-check bullet and the univariate orthonormality numbers stay here as a verification record under Checks.
    - Original title: "PD-T?bivariate-lanczos-claude-114 — On product-type measures the first-order Gram sensitivity of the window coefficient map is given by univariate data: on-pattern entries have univariate gains, off-pattern (structural-zero) entries have cross-variable gains; the clustered-checkerboard loss is this first-order channel".
    - Original part 5, verbatim:

      > 5. **[FP, MEASURED]** Harris–Simanek checkerboards m = 30 (PD-T?…-111, -112), degrees ≤ 20. Gain := max |A + Aᵀ| over degrees ≤ n.
      >    - Formula check: on 91 sampled entries per set, |A_direct − A_formula| ≤ 1.1e-14·‖R_d‖ (clustered), 1.6e-15·‖R_d‖ (equispaced); pre-stated criterion 1e-8 met.
      >    - Cubic-clustered: on-pattern gains ≤ 5.0e3 (n = 16 and 20); off-pattern gains up to 9.9e11 (n = 16), 1.3e14 (n = 20), 296 resp. 709 of 7031 off-pattern entries above 1e6 (medians 1.9, 6.4). Equispaced: on-pattern ≤ 5.6, off-pattern ≤ 4.2e2 (n = 16), 1.4e3 (n = 20).
      >    - The first-order prediction −Σ δh_{k,l}(A + Aᵀ) with δh = the BJ run's off-pattern values gives D = 1.8e-11 (n = 16), 7.8e-9 (n = 20) on the clustered set, against the BJ loss 2e-11, 8e-9 and the nonlinear long-double D(c* + BJ off-pattern) 2e-11, 8e-9; equispaced 4.2e-15, 1.5e-14 against 4e-15, 1e-14. For the three absolute u-noise draws of IDEA?…-117 the prediction gives 2.3–4.8e-4 (n = 16) and 2.7–5.8e-2 (n = 20) against the measured median 4e-4, 3e-2.
      > 
      >    So on the clustered checkerboard the loss up to degree 20 is reproduced to the printed digit by the first-order coefficient channel restricted to the structural zeros of c*; the large gains are off-pattern only; and the BJ run's off-pattern errors (max 2.1e-13 in absolute value) produce 10^6–10^7 times less defect than generic absolute u-noise on the same entries.

    - Lines adjusted for the split. The original Status and Scope wording is kept in place in brackets. The other originals:
      - Assumptions, last sentence: "Part 5: double precision, NumPy 2.5.3, long double (x86 80-bit) for Ξ, c*, the formula and the direct check."
      - Status row: "| 5. measurements | MEASURED | `logs/r06_gain_identity.log`, `logs/r06_coefficient_channel.log` |".
      - Checks: "Part 3 against direct propagation (part 5, first item). First-order predictions against the nonlinear long-double values of IDEA?…-117 (part 5, third item). Univariate orthonormality of p_s, r_s on the factor measures: 7.1e-16, 1.7e-16 (clustered), 3.4e-17, 6.9e-17 (equispaced)."
      - Proof 5: "`python3 -I tracks/bivariate-lanczos/code/L1/l1_r06_gain_identity.py > …/logs/r06_gain_identity.log` (35 s); the IDEA?…-117 runs are in `logs/r06_coefficient_channel.log`."
      - Open items, second sentence: "Which structure of the BJ off-pattern errors keeps them away from the high-gain directions (R07)."
  - LL-L2: in part 4, "nonzero in c*" was literally false, since on-pattern entries can vanish (a_j = 0 for a symmetric marginal). It is replaced by "structurally permitted, i.e. may be nonzero". The univariate comparison now names the h-coordinate and notes that h- and β-coordinates are independent. Original part-4 sentence: "An entry is on-pattern (nonzero in c*) iff i_l = i for j ≥ 1, resp. j_l = 0 for j = 0. For on-pattern entries the derivative in part 3 is exactly the Gram derivative of the univariate coefficient map of μ_Y (perturbing a^y_{j−1} if j_l = j−1, b^y_{j−1} if j_l = j−2) replicated on the x-degree-i chain, resp. of μ_X (a^x_{t−1}, b^x_{t−1}) replicated on each y-degree." The implemented pattern mask is positional, so no number changes.
