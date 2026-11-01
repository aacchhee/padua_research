# PD-T?bivariate-lanczos-claude-304 — Square case M = N_n: commutator lower bound δ ≥ c√‖κ‖ and the fully commuting case δ = O(ε)

Final ID: **PD-T060** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: square-case necessity; last-block commutator diagnostic; κ = [Ĥ_x, Ĥ_y]_{nn}; fully commuting square data; normal-matrix (Bauer–Fike) representation; dim S_1 = n(n+1)/2 = dim Skew_{n+1}.
Split from: none (supporting result for PD-T?bivariate-lanczos-claude-300).
Split into: PD-T?bivariate-lanczos-claude-316 (OPEN: the induced map V*/T → Skew_{n+1} is an isomorphism when the 3N_n jet conditions are independent, i.e. the second clause of pre-audit (c)); PD-T?bivariate-lanczos-claude-317 (MEASURED: numerical rank n(n+1)/2 of d(κ∘Φ) at Padua n = 2, 3 and further sets). Related new result (not a split): PD-T?bivariate-lanczos-claude-318 (exact derivative formula of κ and reduction of 316 to the quadratic-generator conjunct of 309). Mapping in topics/bivariate-lanczos-20261031/SPLITS.md (§L3), to be moved to ID_CROSSWALK.md at PR preparation.

## Statement

Let M = N_n (n ≥ 1), nodes Π_n-unisolvent, μ = Σ w_i δ_{z_i}, w_i > 0, H := Φ(μ). Then [H_x, H_y] = 0 (Q is square orthogonal). For (Ĥ_x, Ĥ_y) ∈ 𝒞_n write κ(Ĥ) := ([Ĥ_x, Ĥ_y])_{nn} (skew-symmetric (n+1) × (n+1); all other blocks of the commutator vanish by PD-T?…-301).

(a) [Commutator bound.] There are C, δ_1 > 0 (depending on z, w, n) such that every positive measure μ′ supported in K_δ, δ ≤ δ_1, whose sections are defined and close to H (‖Φ(μ′) − H‖ ≤ δ_1) satisfies ‖κ(Φ(μ′))‖ ≤ C δ². Consequently, consistent data Ĥ near H can be the exact sections of a positive measure on K_δ only if δ ≥ (‖κ(Ĥ)‖/C)^{1/2}.
(b) [Fully commuting data.] If Ĥ ∈ 𝒞_n (structured, positive pivots) satisfies [Ĥ_x, Ĥ_y] = 0 exactly, then Ĥ is the exact section pair of the N_n-point positive measure μ′ = Σ_j (v_jᵀ e_0)² δ_{ẑ_j} (joint eigenpairs (ẑ_j, v_j) of Ĥ), whose points are distinct and satisfy dist(ẑ_j, {z_i}) ≤ ‖(Ĥ_x − H_x) + i(Ĥ_y − H_y)‖_2 ≤ ‖Ĥ_x − H_x‖_2 + ‖Ĥ_y − H_y‖_2. So δ = O(ε) with N_n atoms.
(c) [First-order factorisation — routine.] The derivative of κ ∘ Φ at L_μ vanishes on T := span{ev_{z_i}, ∂_x ev_{z_i}, ∂_y ev_{z_i}} (moving or reweighting the N_n nodes keeps the sections commuting), so it factors through V*/T ≅ S_1* (T^⊥ = S_1); dim V*/T = dim S_1 ≥ n(n+1)/2 = dim Skew_{n+1}. Whether the induced map V*/T → Skew_{n+1} is an isomorphism is not claimed here: it is the separate OPEN claim PD-T?…-316 (exact derivative formula and reduction: PD-T?…-318; finite measurements: PD-T?…-317).

## Definitions

As in PD-T?…-301/302/303. ‖·‖ any matrix norm (constants depend on it).

## Assumptions

[EXACT]; square case; for (a) μ′ ranges over all positive measures on K_δ (any number of atoms).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) ‖κ‖ ≤ Cδ², hence δ ≥ c√‖κ‖ | PROVED | barycentre argument below |
| (b) commuting data ⇒ N_n-point μ′, δ ≤ ‖ΔH‖ | PROVED | normal-matrix eigenvalue inclusion below |
| (c) d(κ∘Φ) vanishes on T (factors through V*/T) | PROVED (routine) | — |

## Depends on

PD-T?…-301. Eigenvalue inclusion for a normal matrix N and arbitrary perturbation Δ: every eigenvalue of N + Δ lies within ‖Δ‖_2 of spec(N) (Bauer–Fike with condition number 1; textbook, recalled; one-line proof: if λ ∉ spec N, ‖(N − λ)^{-1}‖_2 = 1/dist(λ, spec N) for normal N).

## Checks

Proof only.

## Sources

Textbook (Bauer–Fike for normal matrices).

## Proof or evidence

(a) Let μ′ = Σ_j w′_j δ_{ξ_j}, ξ_j = z_{i(j)} + h_j, |h_j| ≤ δ (balls disjoint for δ ≤ δ_1). Barycentre surrogate: W_i := Σ_{j: i(j)=i} w′_j, b_i := Σ_{i(j)=i} w′_j h_j / W_i, μ̃ := Σ_i W_i δ_{z_i + b_i}. Taylor expansion of ev_{ξ_j} about z_i + b_i: the first-order terms cancel by the barycentre identity, so ‖L_{μ′} − L_{μ̃}‖ ≤ C_2′ μ′(K_δ) δ². The cluster masses are positive: Φ(μ′) close to H gives L_{μ′} close to L_μ (normalised; Φ^{-1} is Lipschitz near Φ(μ), PD-T?…-301(c)), and pairing with ℓ_i² (ℓ_i the Π_n Lagrange basis at the nodes) gives W_i = L_{μ′}(ℓ_i²) + O(δ) = w_i + O(δ + ‖Φ(μ′) − H‖) > 0 for δ and ‖Φ(μ′) − H‖ small. Hence μ̃ has N_n distinct atoms with positive masses near the nodes (Π_n-unisolvent for δ small), so its Q is square orthogonal and κ(Φ(μ̃)) = 0. The map L ↦ κ(Φ(L)) is analytic on {M_n(L) ≻ 0} (PD-T?…-301(c)) hence Lipschitz near L_μ (normalising L(1) = 1): ‖κ(Φ(μ′))‖ ≤ Lip · ‖L_{μ′} − L_{μ̃}‖/μ′(K_δ) ≤ C δ². The consequence follows since κ is a function of the section pair.
(b) Commuting real symmetric Ĥ_x, Ĥ_y have a common orthonormal eigenbasis v_j with Ĥ_x v_j = x̂_j v_j, Ĥ_y v_j = ŷ_j v_j; N̂ := Ĥ_x + iĤ_y is normal with eigenvalues ẑ_j = x̂_j + iŷ_j, and N := H_x + iH_y is normal with eigenvalues z_i; N̂ − N = ΔH_x + iΔH_y, so each ẑ_j is within ‖ΔH_x + iΔH_y‖_2 of some z_i. With π as in PD-T?…-301(b), π(Π_n) = R^N, i.e. e_0 is cyclic for the pair, so the ẑ_j are distinct and all weights (v_jᵀe_0)² > 0. In the eigenbasis, Ĥ_x, Ĥ_y become diag(x̂), diag(ŷ) and e_0 becomes (v_jᵀe_0)_j; the graded Gram–Schmidt basis generated from e_0 by (Ĥ_x, Ĥ_y) is e_0, …, e_{N−1} (triangularity of π), so the degree-n sections of μ′ are Ĥ itself.
(c) Nodes and weights are local coordinates of the N_n-point measures near μ, all of which have κ = 0; dimension count dim Π_{2n+1} − 3N_n = n(n+1)/2.

## Scope

Square (Padua-type, M = N_n) node sets, perturbative regime. (a) is a computable a-posteriori diagnostic: the last-block commutator of square section data bounds from below the support spread of any exact backward measure.

## Open items

Explicit C in (a); the first-order isomorphism (PD-T?…-316, OPEN); behaviour of κ̂ for floating-point Padua runs with the H_y completion (ill-defined at the O(u) level because the computed entries are overdetermined, PD-T?…-301(d)).

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.
- 2026-10-31T23:54:00+01:00, L3 developer: finding 304(a) (added the positive-cluster-mass step) and L3 (isomorphism part of (c) relabelled MEASURED; overall file status PROVED refers to (a), (b) and the factorisation part of (c)) of L3-reconstruction-01 (topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md, audited head 0b7b396).
- 2026-11-01T00:47:14+01:00, L3 developer: finding L11 of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1) — original wording of the passages replaced at 2026-10-31T23:54 (round-1 response): «μ̃ has N_n distinct atoms near the nodes (Π_n-unisolvent for δ small), so its Q is square orthogonal and κ(Φ(μ̃)) = 0.»; «| (c) first-order identification | PROVED (routine) | — |».
- 2026-11-01T08:33:39+01:00, L3 developer (Claude Opus 5.5, xhigh requested): finding LF-M2 of Codex audit-01 (audit-01/L3-framework.md; candidate 5ccfac2) — the unproved isomorphism clause of (c) moved out of this PROVED file: general claim → PD-T?…-316 (OPEN), finite rank observation → PD-T?…-317 (MEASURED); new supporting result PD-T?…-318; (a), (b) and the factorisation part of (c) unchanged and PROVED. Original wording of the replaced passages: «Split into: none.»; «(c) [Dimension match, first order — routine.] The derivative of κ ∘ Φ at L_μ vanishes on T := span{ev_{z_i}, ∂_x ev_{z_i}, ∂_y ev_{z_i}} (moving or reweighting the N_n nodes keeps the sections commuting), and dim V*/T ≥ n(n+1)/2 = dim Skew_{n+1} = dim S_1 lower bound; when the 3N_n jet conditions are independent (verified exactly for Padua n = 1, 2, 3 and numerically for n ≤ 7, PD-T?…-307) S_1 ≅ (V*/T)* and κ is, to first order, the S_1*-component of the perturbation.»; «| (c) the induced map V*/T → Skew_{n+1} is an isomorphism ("κ is, to first order, the S_1*-component") | MEASURED | reconstruction `indep_measured.py dkappa`: rank n(n+1)/2 for Padua n = 2, 3; not proved |»; «Explicit C in (a); behaviour of κ̂ for floating-point Padua runs».
