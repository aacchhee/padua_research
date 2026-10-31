# PD-T?bivariate-lanczos-claude-314 — Computed coefficient data are consistent sections iff the completed pair is symmetric

ID kind: PD-T.
Aliases: consistency ⟺ symmetry; asymmetry as consistency defect; reading (G) precondition; R06.
Split from: none (supporting result for PD-T?bivariate-lanczos-claude-300, reading (G)).
Split into: none.

## Statement

Let a run of the window recurrence (L1 convention: J injects the columns (t,0), F is full) produce, up to degree n+1, computed coefficients with positive pivots β. Let Ĥ_F ∈ ℝ^{N_n×N_n} hold the computed F-coefficients of the columns of degree ≤ n (rows truncated to degree ≤ n), and let Ĥ_J be L1's implicit J-section (PD-T?bivariate-lanczos-claude-104 part 2, developer-PROVED, under review): computed J-columns (t,0), and for j ≥ 1 Ĥ_J e_{(t,j)} := (T_F Ĥ_J e_p − Σ_{l∈W_{(t,j)}} (h_{(t,j)})_l Ĥ_J e_l)/β_{(t,j)}, p = (t−1, j−1). Then:
(a) [Ĥ_F, Ĥ_J] e_c = 0 for every column c of degree ≤ n−1 (exact identity on the computed numbers, no rounding model).
(b) If the computed T_F has the structural echelon pattern of PD-T?…-301 (exact window, PD-T?…-102 part 2), then (Ĥ_F, Ĥ_J) ∈ 𝒞_n — i.e. the computed data are exactly the degree-n sections of a unique normalised functional L̂ on Π_{2n+1} — iff Ĥ_F = Ĥ_Fᵀ and Ĥ_J = Ĥ_Jᵀ.
(c) For every (H′_F, H′_J) ∈ 𝒞_n: max_entries|Ĥ_A − H′_A| ≥ ½ max_entries|Ĥ_A − Ĥ_Aᵀ| (A = F, J).

## Definitions / Assumptions

[EXACT] algebra on computed quantities. 𝒞_n, Φ as in PD-T?…-301 (with x ↔ J, y ↔ F; the order convention of 301 is the mirror of L1's, which only relabels the echelon pattern).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) | PROVED | below; MEASURED sanity K12 (≤ 9u‖Ĥ‖² in all runs) |
| (b) | PROVED | from (a) and PD-T?…-301(b) |
| (c) | PROVED (routine) | 𝒞_n ⊂ symmetric pairs; distance of a matrix to the symmetric matrices in the max-entry norm is half its max asymmetry |

## Depends on

PD-T?…-301; L1's definition of Ĥ_J (PD-T?…-104 part 2) and the pattern statement (PD-T?…-102 part 2), both developer-PROVED and under review (used as definitions/hypotheses, not as proofs).

## Checks

`r06_consistency.py` (K12 column in the logs).

## Proof or evidence

(a) Column p of T_F is the coefficient vector of the F-product of q̂_p: T_F e_p = β_k e_k + Σ_{l∈W_k} (h_k)_l e_l with k = child(p). The definition of Ĥ_J gives β_k Ĥ_J e_k = T_F Ĥ_J e_p − Σ_l (h_k)_l Ĥ_J e_l, i.e. Ĥ_J T_F e_p = T_F Ĥ_J e_p. Every column of degree ≤ n−1 is the F-parent of a column of degree ≤ n, so [T_F, Ĥ_J] e_p = 0 for deg p ≤ n−1. Truncating rows to degree ≤ n does not change these columns: Ĥ_J e_p and T_F e_p have degree ≤ n, so P T_F P Ĥ_J e_p = P T_F Ĥ_J e_p and P Ĥ_J P T_F e_p = P Ĥ_J T_F e_p (P the projection onto degree ≤ n).
(b) If both are symmetric, the pair is structured and its commutator is skew; its columns of degree ≤ n−1 vanish by (a), hence so do its rows, so the commutator vanishes outside block (n,n), and PD-T?…-301(b) gives L̂. Conversely elements of 𝒞_n are symmetric.
(c) For symmetric H′, |Ĥ_ab − Ĥ_ba| ≤ |Ĥ_ab − H′_ab| + |H′_ba − Ĥ_ba|.

## Scope

Reduces "are the computed coefficients consistent?" (precondition of reading (G)) to symmetry of explicitly computable matrices. The implicit completion is the unique one that makes the interior commutation hold given (T_F, τ); it does not show that a small change of (T_F, τ) cannot restore symmetry (that needs a Lipschitz bound of the completion map; MEASURED first-order fits in PD-T?…-315).

## Open items

Quantitative version: distance of (T_F, τ) to the consistent partial-data manifold in terms of the asymmetry.

## History

2026-10-31T23:52+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer, round R06.
