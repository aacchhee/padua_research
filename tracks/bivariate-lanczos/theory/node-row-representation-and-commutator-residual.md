# PD-T?bivariate-lanczos-claude-104 — Node-row representation of the computed basis and the commutator residual of the injecting operator

ID kind: PD-T.
Aliases: node-row recurrence; per-node marching propagator L̂(z)⁻¹; computed-coefficient polynomials p̂; commutator residual C_res; implicit J-section Ĥ_J; "F-marching with clamped J-columns".
Split from: none.
Split into: none.

## Statement

[EXACT algebra on computed quantities] Let the window recurrence (PD-T?…-102) produce Q̂ ∈ R^{M×N} with local relations β_k q̂_k = A_k q̂_{p(k)} − Q̂_{W_k}h_k − f_k (A_k = J = X for the columns (t,0), A_k = F = Y otherwise), and let a_k(z) denote x for J-products and y for F-products, evaluated at z = (x, y).

1. **(Node rows.)** Define L̂(z) ∈ R^{N×N} lower triangular by row 0 = e_0ᵀ and, for k ≥ 1, L̂(z)_{kk} = β_k, L̂(z)_{kl} = (h_k)_l for l ∈ W_k, and L̂(z)_{k,p(k)} = (h_k)_{p(k)} − a_k(z) (p(k) ∈ W_k). Then for every node i the row ξ^{(i)} := (e_iᵀq̂_k)_k satisfies
   L̂(z_i) ξ^{(i)} = ξ^{(i)}_0 e_0 − φ^{(i)},  φ^{(i)}_k := e_iᵀ f_k (φ^{(i)}_0 := 0),
   so ξ^{(i)} = ξ^{(i)}_0 p̂(z_i) − L̂(z_i)⁻¹φ^{(i)}, where p̂(z) := L̂(z)⁻¹e_0 is the vector of values of the **computed-coefficient polynomials** (p̂_0 = 1, β_k p̂_k = a_k p̂_{p(k)} − Σ_{l∈W_k}(h_k)_l p̂_l). Column l of L̂(z)⁻¹ is the impulse response of the computed recurrence at the point z started at step l (the bivariate associated polynomials).
2. **(Implicit J-section from computed data.)** Define Ĥ_J column by column: Ĥ_J e_{(t,0)} := computed coefficients of the J-product creating (t+1, 0) (with β in row (t+1,0)); for j ≥ 1, Ĥ_J e_{(t,j)} := (T_F Ĥ_J e_{(t−1,j−1)} − Σ_{l∈W_{(t,j)}} (h_{(t,j)})_l Ĥ_J e_l)/β_{(t,j)}, with T_F the computed F-coefficients. In exact arithmetic Ĥ_J = H_J (PD-T?…-101 part 5).
3. **(Commutator residual.)** C_res := J Q̂ − Q̂ Ĥ_J (columns c_k for k of degree ≤ n−1) satisfies exactly
   c_{(t,0)} = f_{(t+1,0)},  β_k c_k = F c_{p(k)} − Σ_{l∈W_k}(h_k)_l c_l + E_F Ĥ_J e_{p(k)} − J f_k (k = (t, j), j ≥ 1),
   with E_F = F Q̂ − Q̂ T_F. In node form, γ^{(i)} := (e_iᵀc_k)_k solves the **F-marching with clamped J-columns**: γ_{(t,0)} = e_iᵀ f_{(t+1,0)} and β_kγ_k − y_iγ_{p(k)} + Σ_l (h_k)_lγ_l = e_iᵀ(E_F Ĥ_J e_{p(k)} − J f_k).
4. **(Relation to the defect.)** The defect of PD-T?…-102 part 4 is d_k = (I − Π_{s+1}) c_k, so ‖d_k‖ ≤ ‖c_k‖; in exact arithmetic C_res = 0.

## Definitions

As in PD-T?…-101/-102. Bilinear/real arithmetic throughout; X, Y diagonal.

## Assumptions

β_k > 0 for all k (no breakdown); the computed quantities of one run (Q̂, h, β) are given. No genericity is needed for the identities.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. node rows, p̂, impulse responses | PROVED (routine) | proof below |
| 2. Ĥ_J definition, exact-arithmetic agreement | PROVED (by PD-T?…-101 part 5) | |
| 3. commutator-residual recursion and node form | PROVED | proof below; checked in long double: max relative residual 1.2e-3, 8.5e-4, 1.1e-3 against u-sized terms (R02 log) |
| 4. defect bound | PROVED (routine) | |

## Depends on

PD-T?…-101 (part 5), PD-T?…-102 (local relations).

## Checks

`tracks/bivariate-lanczos/code/L1/l1_identities.py` (functions `hhat_J`, `run`): builds Ĥ_J from the computed coefficients, C_res, and evaluates both sides of 3. in long double (`topics/bivariate-lanczos-20261031/directions/L1/logs/r02_identities.log`). `code/L1/l1_node_propagator.py` uses part 1 to drive the computed recurrence at all nodes simultaneously with random forcing (PD-T?…-107).

## Proof or evidence

*1.* Row i of the local relation: since A_k is diagonal, e_iᵀA_k q̂_{p} = a_k(z_i) ξ_{p}; so β_k ξ_k = a_k(z_i)ξ_{p(k)} − Σ_l (h_k)_l ξ_l − φ_k, which is row k of L̂(z_i)ξ = −φ (k ≥ 1); row 0 is the identity ξ_0 = ξ_0. L̂(z) is lower triangular with nonzero diagonal (β_k > 0, L̂_{00} = 1), hence invertible; the stated formula follows by linearity. The p̂ recursion is row k of L̂(z)p̂ = e_0.
*3.* Multiply the F-local relation of k = (t, j), j ≥ 1, by J and use JF = FJ: β_k J q̂_k = F J q̂_{p} − Σ_l (h_k)_l J q̂_l − J f_k. Substitute J q̂_m = Q̂Ĥ_J e_m + c_m (definition of c_m) for m = p and m ∈ W_k, and F Q̂ = Q̂ T_F + E_F on the columns of degree ≤ t (Ĥ_J e_p is supported there). The Q̂-terms give β_k Q̂Ĥ_J e_k by definition 2.; the remaining terms are the stated right-hand side. For (t, 0): J q̂_{t,0} = Q̂ (computed coefficients) + f_{(t+1,0)} is the local relation of the J-product itself, and Ĥ_J e_{(t,0)} is those coefficients. Node form: take row i (F, J diagonal).
*4.* d_k = (I − Π_{s+1})J q̂_k and Q̂Ĥ_J e_k ∈ range Q̂_{s+1} (support of Ĥ_J e_k), so d_k = (I − Π_{s+1})c_k.

## Scope

Part 1 is the bivariate analogue of the classical view of Lanczos as the orthogonal-polynomial recurrence evaluated at the eigenvalues, with rounding errors propagated by associated polynomials; here the "eigenvalues" are the nodes and the propagator is the computed window recurrence at the point z_i. It makes the loss of orthogonality a function of per-node propagators: Q̂ᵀQ̂ = Σ_i ξ^{(i)}ξ^{(i)ᵀ}. Part 3 identifies the commutator residual as the forced response of the F-marching with clamped J-columns. Neither part bounds anything by itself; the size of L̂(z_i)⁻¹ is the question (PD-T?…-105 for product measures, PD-T?…-107 measured).

## Open items

A bound of max|Q̂ᵀQ̂ − I| in terms of max_i ‖L̂(z_i)⁻¹φ^{(i)}‖ and the computed-coefficient Gram Σ_i (ξ_0^{(i)})² p̂(z_i)p̂(z_i)ᵀ − I (the representation gives the identity Q̂ᵀQ̂ − I = Σ_i (ξ_0 p̂ − L̂⁻¹φ)(ξ_0 p̂ − L̂⁻¹φ)ᵀ − I, not yet a bound).

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R02).
- 2026-10-31T23:05Z (response to reconstruction 01): CONFIRMED by an exact rational simulated computed run (parts 1 and 3, 0 mismatches). No findings.
