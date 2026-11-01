# PD-T?bivariate-lanczos-claude-102 — [FP] local relations of the BJ/HL window recurrence, with the computed coefficient pattern and the implicit-operator defect

Final ID: **PD-T030** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: F-relations, J-relations; local rounding relations; "X Q = Q H_x + boundary + F_x" for the window recurrence; implicit defect G_J.
Split from: none (answers the [FP] part of plan L1-Q1(a); the exact pattern is PD-T?…-101).
Split into: none.

## Statement

[FP] Standard model fl(a ∘ b) = (a ∘ b)(1 + δ), |δ| ≤ u (unit roundoff); γ_k = ku/(1 − ku). Ordering, operators F (full) and J (injecting), windows W_k and parents p(k) as in PD-T?…-101 (the input code: F = Y, J = X; mirror for HL BIT). For each k ≥ 1 the computed algorithm is

- BJ (CGS, no reorthogonalization): a = fl(A_k q̂_{p(k)}), h_k = fl(Q̂_{W_k}ᵀ a), r = fl(a − Q̂_{W_k} h_k), β_k = fl(‖r‖), q̂_k = fl(r/β_k);
- HL (ORTH): the same with r obtained by one MGS sweep over W_k, and a second sweep if ‖r‖ ≤ 0.707‖a‖; h_k = sum of the coefficients of both sweeps.

Write w_k = |W_k| (≤ 3t − 1 for the block window, ≤ 2t + 1 for the exact window, t = degree of k), μ = max_l ‖q̂_l‖, κ_k = ‖Q̂_{W_k}‖₂ (≤ √w_k μ). Then, to first order in u:

1. **(Local relations.)** β_k q̂_k = A_k q̂_{p(k)} − Q̂_{W_k} h_k − f_k with
   ‖f_k‖ ≤ [ (w_k + 2)(1 + κ_k √w_k μ) + 1 ] u ‖A_k‖ μ  (BJ),  ‖f_k‖ ≤ [ 6w_k + 4 ] u ‖A_k‖ μ (κ_k)² (HL),
   and |‖q̂_k‖ − 1| ≤ (M/2 + 2)u.
2. **(Matrix form for F; the coefficient pattern.)** Let Q̂_s denote the computed columns of degree ≤ s, N_s = (s+1)(s+2)/2. For every n ≥ 1,
   F Q̂_{n−1} = Q̂_n T_F + E_F,  ‖E_F e_p‖ = ‖f_{child(p)}‖,
   where T_F ∈ R^{N_n × N_{n−1}} is the matrix of **computed** coefficients: column p = (t, j) holds h_{child(p)} in the rows W_{child(p)}, β_{child(p)} in row child(p) = (t+1, j+1), and zeros elsewhere. With the exact window the nonzero pattern of T_F is exactly the exact-arithmetic support of H_F (PD-T?…-101, 2.), and its rows of block n, B_F := T_F[block n, :], are nonzero only in the columns of block n−1 with (B_F)_{(n,r),(n−1,j)} = 0 for r > j+1 (upper-Hessenberg pattern, positive subdiagonal β's).
3. **(Matrix form for J: one formed column per degree.)** For every t ≥ 0, J q̂_{t,0} = Q̂_{t+1} τ_t + f_{(t+1,0)} with τ_t the computed coefficients (rows W_{(t+1,0)} = blocks t−1, t, and β_{(t+1,0)} in row (t+1, 0)). No relation is formed for J q̂_{t,j}, j ≥ 1.
4. **(Implicit-operator defect.)** Let Π_s := Q̂_sQ̂_s⁺ (orthogonal projector onto range Q̂_s). For every column l of degree s define, as analysis objects that the algorithm never computes, g_l := Q̂_{s+1}⁺ J q̂_l and the **defect** d_l := (I − Π_{s+1}) J q̂_l, so J q̂_l = Q̂_{s+1} g_l + d_l exactly; in matrix form J Q̂_{n−1} = Q̂_n T̃_J + G_J with columns of G_J equal to (I − Π_n) d_l. In exact arithmetic all d_l = 0. In [FP], d_{(t,0)} = (I − Π_{t+1}) f_{(t+1,0)} (local rounding only), and for j ≥ 1 the defects satisfy the exact **defect recursion**
   β_{(t,j)} d_{(t,j)} = (I − Π_{t+1}) [ F d_{(t−1,j−1)} − Σ_{l∈W_{(t,j)}} (h_{(t,j)})_l d_l + E_F^{(t)} g_{(t−1,j−1)} − J f_{(t,j)} ],
   where E_F^{(t)} = F Q̂_t − Q̂_{t+1} T_F^{(t)} collects the F-local errors of the columns of degree ≤ t. The J-defect is forced only by local rounding (f and E_F) and propagated by the same computed recurrence that produces the basis vectors, with F as the multiplier. [Wording corrected 2026-10-31, recon-01 minor: "propagated by the same computed coefficients, interleaved with the projectors (I − Π_{t+1}), with F as the multiplier".]

## Definitions

child(p): the column created from p by F. A^+: Moore–Penrose inverse (Q̂_n has full column rank as long as ‖Q̂_nᵀQ̂_n − I‖ < 1). "Formed" as in PD-T?…-101.

## Assumptions

Diagonal X, Y (so fl(A q̂) = (I + D)A q̂ with |D| ≤ uI); no underflow/overflow; β_k > 0 (generic nodes, U(n) in exact arithmetic, and no breakdown in the computed run). First-order bounds; the O(u²) terms are dropped as in Higham's standard model.

## Status by part

Overall status: PROVED (routine, first order in u).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. local relations, constants | PROVED (routine; constants not optimised) | proof below |
| 2. F matrix form and pattern | PROVED (bookkeeping) | from 1. and PD-T?…-101 |
| 3. J matrix form | PROVED (bookkeeping) | from 1. |
| 4. defect identity and recursion | PROVED (exact algebra on the computed quantities) | proof below; a priori growth bound for G_J is OPEN (R01 measures it) |

## Depends on

PD-T?bivariate-lanczos-claude-101 (pattern). Higham, ASNA, ch. 3 standard model (textbook background, cited as such; not a campaign dependency).

## Checks

R01 (`tracks/bivariate-lanczos/code/L1/l1_kill_test.py`) logs `defect_x`, `defect_y` = max column norm of (I − U_nU_nᵀ) A U_{n−1} (U = Householder Q-factor of Q̂, nested spans): the full-operator defect stays at 1e-15 throughout every run, consistent with 2.; the J-defect is reported in R01 §3.

## Proof or evidence

*1 (BJ).* a = A q̂_p + δ_a, |δ_a| ≤ u|A q̂_p| (diagonal A). r = a − Q̂_W h + δ_r with |δ_r| ≤ γ_{w+1}(|a| + |Q̂_W||h|) (a dot product of length w followed by one subtraction, componentwise). q̂_k = r/β + δ_q with |δ_q| ≤ u|r|/β, so β q̂_k = r + βδ_q. Hence f_k := −(δ_a + δ_r + βδ_q) and ‖f_k‖ ≤ u‖A‖μ + γ_{w+1}(‖a‖ + ‖|Q̂_W|‖₂‖h‖) + u‖r‖. Use ‖a‖ ≤ (1+u)‖A‖μ, ‖|Q̂_W|‖₂ ≤ ‖Q̂_W‖_F ≤ √w μ, ‖h‖ ≤ (1+γ_M)‖Q̂_W‖₂‖a‖ = (1+γ_M) κ ‖a‖, ‖r‖ ≤ ‖a‖ + ‖Q̂_W h‖ + ‖δ_r‖ ≤ (1 + κ²)‖a‖ + O(u). Collecting first-order terms: ‖f_k‖ ≤ u‖A‖μ[1 + (w+1)(1 + √w μ κ) + 1 + κ²]; since κ ≤ √w μ we have κ² ≤ κ√w μ, hence ‖f_k‖ ≤ [(w+2)(1 + κ√w μ) + 1]u‖A‖μ. Normalisation: β = ‖r‖(1 + ε), |ε| ≤ γ_M/2 + u + O(u²) (sum of M squares and a square root), so ‖q̂_k‖ = ‖r‖/β · (1 + O(u)) and |‖q̂_k‖ − 1| ≤ (M/2 + 2)u.
*1 (HL).* Each MGS step r ← r − c q̂_l with c = fl(q̂_lᵀ r) has |δ| ≤ u(|r| + 2|c||q̂_l|) componentwise; c is the recorded coefficient, so its own rounding does not enter f. Over at most 2w steps, with |c| ≤ (1+γ_M)μ‖r‖ and ‖r‖ nonincreasing up to O(u) factors bounded by κ², ‖Σδ‖ ≤ 2w·3u κ²μ‖A‖μ; add δ_a and the normalisation term.

*Corrections (2026-10-31T23:05Z, reconstruction 01, minor; first-order constants unaffected):*
- 1 (BJ): "‖h‖ ≤ (1+γ_M)κ‖a‖" is not a valid inequality. The correct bound is ‖h‖ ≤ κ‖a‖ + γ_M√w μ‖a‖. The difference enters only at O(u²).
- 1 (HL): the accounting omits the rounding of the coefficient sum h = c + c′ over the two sweeps. That term is ≲ uκ²‖a‖ and is absorbed by the κ² slack of the stated constant.
- "‖r‖ nonincreasing up to O(u) factors bounded by κ²" should read: each MGS step does not increase ‖r‖ (up to O(u)) whenever ‖q̂_l‖ ≤ √2; the κ² factor bounds the accumulated coefficients.
*2–3.* Stack the relations of 1. for the children of the columns of Q̂_{n−1} (F) and for the columns (t, 0) (J), using the window/pattern of PD-T?…-101, 4.
*4.* J q̂_l = Q̂_{s+1}g_l + d_l is the orthogonal decomposition with respect to range Q̂_{s+1}. For (t, 0): J q̂_{t,0} = Q̂_{t+1}τ_t + f_{(t+1,0)} by 3., and (I − Π_{t+1})Q̂_{t+1} = 0. For j ≥ 1: multiply the local relation β q̂_{t,j} = F q̂_{t−1,j−1} − Q̂_W h − f by J and use JF = FJ (diagonal matrices): β J q̂_{t,j} = F J q̂_{t−1,j−1} − Σ_l h_l J q̂_l − J f. Substitute J q̂_{t−1,j−1} = Q̂_t g + d_{(t−1,j−1)} and F Q̂_t = Q̂_{t+1}T_F^{(t)} + E_F^{(t)}, and J q̂_l = Q̂_{deg l+1} g_l + d_l with deg l + 1 ≤ t + 1 for l ∈ W. All Q̂_{t+1}-terms are annihilated by (I − Π_{t+1}); since β J q̂_{t,j} = β Q̂_{t+1}g_{(t,j)} + β d_{(t,j)} with d_{(t,j)} = (I − Π_{t+1})J q̂_{t,j}, applying (I − Π_{t+1}) to both sides gives the recursion.

## Scope

What is formed: the full section of F (every column, within the exact support) and one column per degree of J. Hence a per-operator Paige identity is available for F alone (PD-T?…-103); for J and for the joint operator X + iY any Paige-type identity must carry G_J. The defect recursion shows that G_J is forced only by local rounding and propagated by the F-recurrence; whether it stays O(u·poly(n)) until loss of orthogonality sets in is not proved here (OPEN; measured in R01).

## Open items

A priori bound on ‖G_J‖ in terms of u, the window and the loss of orthogonality (needed for a joint Paige statement, R02). Local-orthogonality bound for BJ/CGS within the window (Paige's local lemma has no proved analogue here).

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R01).
- 2026-10-31T23:05Z (response to reconstruction 01): CONFIRMED by recon-01. Minor corrections added after Proof 1 (HL) and in part 4's last sentence; the original wording is kept.
