# PD-T?bivariate-lanczos-claude-303 — Rate of the moment-cone inradius r(δ) at a discrete measure: interior / ε / √ε / obstruction

ID kind: PD-T.
Aliases: inradius trichotomy; jet spaces S_0, S_1; Hessian condition (H); δ(ε) ≍ 1, ε, √ε, or no δ → 0; double-point (singular) polynomials at the nodes; route (i) refined.
Split from: none (supporting result for PD-T?bivariate-lanczos-claude-300).
Split into: none (applications: 304, 305, 306, PD-N?…-301, 307).

## Statement

Setting of PD-T?…-302 (nodes z_1..z_M Π_n-unisolvent, weights w_i > 0, V = Π_{2n+1}, r(δ) the inradius of C(K_δ) at L_μ). Define the jet spaces
 S_0 := {p ∈ V : p(z_i) = 0 ∀i}, S_1 := {p ∈ V : p(z_i) = 0, ∇p(z_i) = 0 ∀i},
and condition
 (H): there is no nonzero p ∈ S_1 with Hess p(z_i) ⪰ 0 for every i.
Let δ*(ε) := inf{δ : r(δ) ≥ ε} (all ε-perturbations exactly representable on K_δ for δ > δ*(ε); PD-T?…-302(b)). Constants c, C, ε_0, δ_0, δ_1 > 0 below depend only on (z, w, n, ‖·‖).

(a) [Interior; overdetermined.] If S_0 = {0} (i.e. the nodes are Π_{2n+1}-unisolvent; requires M ≥ dim Π_{2n+1}), then r(0) ≥ w_min · σ_1 > 0, σ_1 := min_{‖p‖_*=1} Σ_i |p(z_i)|. So δ*(ε) = 0 for ε < r(0): every perturbation is represented on the ORIGINAL nodes with positive weights w′, and ‖w′ − w‖ = O(ε).
(b) [Linear rate.] If S_0 ≠ {0} and S_1 = {0}: c δ ≤ r(δ) ≤ C δ for 0 ≤ δ ≤ δ_1; hence δ*(ε) ≍ ε.
(c) [√ε is necessary whenever S_1 ≠ {0}.] r(δ) ≤ C δ² for δ ≤ δ_1; hence δ*(ε) ≥ (ε/C)^{1/2}. Moreover for every positive μ′ on K_δ and every p ∈ S_1: |L_{μ′}(p)| ≤ C_p μ′(K_δ) δ².
(d) [√ε is sufficient under (H).] If S_1 ≠ {0} and (H) holds: c δ² ≤ r(δ) ≤ C δ² for δ ≤ δ_1; hence δ*(ε) ≍ √ε.
(e) [Obstruction.] If some p* ∈ S_1 has Hess p*(z_i) ≻ 0 for every i, then there is δ_0 > 0 with p* ≥ 0 on K_{δ_0}, so r(δ) = 0 for 0 ≤ δ ≤ δ_0. For every ε > 0 and every E with ‖E‖ ≤ ε and E(p*) < 0 (e.g. E = −ε ev_ζ/‖ev_ζ‖ for any ζ with p*(ζ) > 0), the consistent sections Φ(L_μ + E) are not the exact sections of any positive measure on K_δ for any δ ≤ δ_0, and dist(L_μ + E, C(K_δ)) ≥ |E(p*)|/‖p*‖_*. In particular δ*(ε) ≥ δ_0 for every ε > 0 (no δ(ε) → 0 exists).
(f) [Dual form of (H).] (H) holds iff the Hessian map p ↦ (Hess p(z_i))_i is injective on S_1 and there exist positive definite 2×2 matrices A_1..A_M with Σ_i ⟨A_i, Hess p(z_i)⟩ = 0 for all p ∈ S_1.

## Definitions

w_min = min_i w_i. ‖·‖_* on V is any norm (the one dual to the chosen norm on V*). Hess p(z) = [[p_xx, p_xy],[p_xy, p_yy]](z).

## Assumptions

[EXACT]; [IDEALIZED: perturbations given as data]. The parts are exclusive and exhaustive except for the degenerate case "S_1 ≠ {0}, (H) fails, but no p ∈ S_1 has all Hessians PD" (some PSD-singular Hessians), which is OPEN (rates between √ε and an obstruction; depends on higher-order jets).

## Status by part

Overall status: PROVED (degenerate subcase excluded from the statement and listed in Open items).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) interior case, δ = 0 | PROVED | proof below |
| (b) linear rate | PROVED | proof below |
| (c) √ε necessity | PROVED | proof below |
| (d) √ε sufficiency under (H) | PROVED | proof below |
| (e) obstruction under robust failure of (H) | PROVED | proof below |
| (f) dual characterisation of (H) | PROVED | separation argument below |

## Depends on

PD-T?bivariate-lanczos-claude-302 (reduction and inradius criterion). No external theorem used.

## Checks

Proof only. Numerical illustrations: PD-T?…-307 (LP rates: δ_min/√ε ≈ 0.191 (n = 1, r = 0.3) and ≈ 0.054 (n = 2) constant over ε = 1e-2..1e-6; residual ∝ ε, not decreasing in δ, for Padua n = 3).

## Sources

None used as proof.

## Proof or evidence

Fix δ_1 ≤ 1 so small that the balls B̄(z_i, δ_1) are disjoint. For p ∈ V with ‖p‖_* = 1 let C_k (k = 2, 3, 4) bound the k-th derivatives of p on the δ_1-neighbourhood of the nodes (finite-dimensional V, so C_k are uniform). Let J : V → R^{3M}, J(p) = (p(z_i), ∇p(z_i))_i, choose a complement W of S_1 = ker J and c_J with ‖q‖_* ≤ c_J |J q| for q ∈ W; write p = p_S + p_W.

Basic inequalities for p ∈ Pos(K_δ), ‖p‖_* = 1, η := L_μ(p) = Σ w_i p(z_i): (I) 0 ≤ p(z_i) ≤ η/w_min. (II) taking h = −δ∇p(z_i)/|∇p(z_i)| in p(z_i + h) ≥ 0 and Taylor: |∇p(z_i)| ≤ p(z_i)/δ + C_2 δ/2. (III) for unit u, p(z_i + δu) + p(z_i − δu) ≥ 0 and the even Taylor expansion (odd terms cancel): uᵀ Hess p(z_i) u ≥ −2p(z_i)/δ² − C_4 δ²/12.

(a) Pos(K_0) = {p : p(z_i) ≥ 0}; for such p, L_μ(p) ≥ w_min Σ|p(z_i)| ≥ w_min σ_1 ‖p‖_*, σ_1 > 0 because S_0 = {0}. Representation on the nodes by PD-T?…-302(a)–(b) with K_0 = {z_i}; weights: an interior point of a finitely generated cone is a strictly positive combination of the generators; w′ − w = V^+E-type bound gives O(ε).
(b) Lower: S_1 = {0} so W = V and 1 ≤ c_J |J(p)| ≤ c_J M[(η/w_min)(1 + 1/δ) + C_2δ/2] by (I), (II), giving η ≥ c δ for δ ≤ δ_1 (δ_1 reduced if needed). Upper: take q ∈ S_0, ‖q‖_* = 1, t := max_{K_δ}(−q)_+ ≤ C′δ (q vanishes at the nodes), p := (q + t)/‖q + t‖_*; then p ∈ Pos(K_δ) and L_μ(p) = t L_μ(1)/‖q + t‖_* = O(δ).
(c) Upper: as in (b) with q ∈ S_1, where t ≤ C_2 δ²/2. Pointwise: for p ∈ S_1 and ξ ∈ B̄(z_i, δ), |p(ξ)| ≤ C_2‖p‖_* δ²/2, integrate against μ′.
(d) Let κ := min{ max_i (−λ_min(Hess q(z_i))) : q ∈ S_1, ‖q‖_* = 1 }; (H) and compactness give κ > 0, and by homogeneity max_i(−λ_min(Hess p_S(z_i))) ≥ κ‖p_S‖_*. Suppose η ≤ c δ² with c to be chosen. By (I), (II): ‖p_W‖_* ≤ c_J |J(p)| ≤ c_J M[(cδ²/w_min)(1 + 1/δ) + C_2δ/2] ≤ C″δ. By (III) and ‖Hess p_W(z_i)‖ ≤ C_2‖p_W‖_*: λ_min(Hess p_S(z_i)) ≥ −2c/w_min − C_4δ²/12 − C_2C″δ for all i. Hence κ(1 − C″δ) ≤ 2c/w_min + O(δ), false for c < κ w_min/4 and δ small. So η ≥ c δ², i.e. r(δ) ≥ cδ². Upper bound from (c).
(e) Taylor: p*(z_i + h) ≥ ½λ_i|h|² − (C_3/6)|h|³ > 0 for 0 < |h| < 3λ_i/C_3 (λ_i = λ_min(Hess p*(z_i)) > 0); take δ_0 = min_i 3λ_i/C_3 (and ≤ δ_1). Then p* ∈ Pos(K_δ) for δ ≤ δ_0 and L_μ(p*) = 0, so r(δ) = 0. If E(p*) < 0, any positive μ′ on K_δ has L_{μ′}(p*) ≥ 0 > c(L_μ + E)(p*) for all c > 0, so L_{μ′} ≠ c(L_μ + E) and, by PD-T?…-301 uniqueness, Φ(μ′) ≠ Φ(L_μ + E). The distance bound is PD-T?…-302(b)'s inequality with p = p*/‖p*‖_*.
(f) Let 𝓗 : S_1 → Sym_2^M be the Hessian map and P = PSD_2^M (self-dual, nonempty interior). (H) ⟺ 𝓗 injective and 𝓗(S_1) ∩ P = {0}. For a subspace U of a space with a self-dual closed cone P with nonempty interior: U ∩ P = {0} ⟺ U^⊥ ∩ int P ≠ ∅ (⇐: ⟨A, X⟩ = 0 with A ≻ 0, X ⪰ 0 forces X = 0; ⇒: separate the subspace U^⊥ from the open convex cone int P to get X ≠ 0 with X ∈ P* = P and X ⊥ U^⊥, i.e. X ∈ U). U^⊥ ∩ int P ≠ ∅ is the existence of PD A_i with Σ⟨A_i, Hess p(z_i)⟩ = 0 on S_1.

## Scope

General finite node sets in ℝ² with positive weights, degree-n sections (functionals on Π_{2n+1}), exact representation (residual strictly smaller than the perturbation; PD-T?…-302). The square case M = N_n always has S_1 ≠ {0} (dim S_1 ≥ dim Π_{2n+1} − 3N_n = n(n+1)/2), so it is never in cases (a)/(b).

## Open items

(1) Degenerate subcase (PSD-singular Hessians). (2) Explicit constants (c, C, δ_0) in terms of computable quantities (κ, c_J, w_min) — only existence here. (3) Generic intermediate M: whether S_1 = {0} for generic nodes when 3M ≥ dim Π_{2n+1} — expected from the Alexander–Hirschowitz theorem on double points (recalled, NOT read; UNVERIFIED; not used).

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01. The orchestrator's suggestion "count 3N zero/gradient conditions vs dim Π_{2n}" is refined: the relevant space is Π_{2n+1} (positivity is only local on K_δ, so odd degree is allowed) and the decisive object in the boundary case is the Hessian cone condition (H), not the count alone.
