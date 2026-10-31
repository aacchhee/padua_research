# PD-T?bivariate-lanczos-claude-309 — Square case: singular polynomials as quadratic forms in the ideal generators; Hankel form of the obstruction test; explicit Padua generators

ID kind: PD-T.
Aliases: quadratic-generator form; F = {qᵀCq : C ⊥ Hankel}; Hankel test; two-term Padua generators g_m, ω; R02 structure.
Split from: none (supporting result for PD-T?…-300 and PD-N?…-301).
Split into: none.

## Statement

Square case M = N_n, Π_n-unisolvent nodes. Let I_{n+1} := {q ∈ Π_{n+1} : q(z_i) = 0 ∀ i} (dimension n+2) and let q_0, …, q_{n+1} be its basis whose top-degree forms are x^j y^{n+1−j} (exists and is unique). For a real symmetric (n+2) × (n+2) matrix C write C ⊥ Hankel if Σ_{j+k=m} c_jk = 0 for m = 0, …, 2n+2, and set p_C := Σ_{j,k} c_jk q_j q_k.

(a) If C ⊥ Hankel then p_C ∈ S_1 (degree ≤ 2n+1, value and gradient zero at every node) and Hess p_C(z_i) = 2 G_iᵀ C G_i, G_i := [∇q_0(z_i); …; ∇q_{n+1}(z_i)] ∈ ℝ^{(n+2)×2}. The space of such C has dimension n(n+1)/2 (= the lower bound for dim S_1).
(b) Consequently: if some C ⊥ Hankel has G_iᵀ C G_i ≻ 0 for every node, the obstruction of PD-T?…-303(e) holds (no δ(ε) → 0). If moreover C ↦ p_C is injective on {C ⊥ Hankel} and dim S_1 = n(n+1)/2, then S_1 = {p_C} and: (H) ⟺ [the Hessian map is injective on S_1 AND there are A_i ≻ 0 with Σ_i G_i A_i G_iᵀ a Hankel matrix].
(c) [Padua generators.] For the Padua points {(cos jπ/n, cos kπ/(n+1)) : j+k even}, the n+2 polynomials g_m := T_{n−m}(x)T_m(y) − T_m(x)T_{n+1−m}(y) (m = 0..n) and ω := (x²−1)U_{n−1}(x) vanish at every node; top(g_m) = −λ_m x^m y^{n+1−m} with λ_m > 0 and top(ω) = 2^{n−1} x^{n+1}, so (given Padua unisolvence for Π_n) they form a basis of I_{n+1} and q_m = −g_m/λ_m, q_{n+1} = ω/2^{n−1}. At interior nodes (|x|, |y| < 1), with s := T_n(x) = (−1)^j: ∇g_m = s(−n U_{m−1}(x) T_m(y), (n+1) T_m(x) U_{m−1}(y)) (U_{−1} := 0, so ∇g_0 = 0) and ∇ω = (n s, 0).

## Definitions / Assumptions

[EXACT]; T_k, U_k Chebyshev polynomials of the first/second kind; Padua unisolvence for Π_n is used as LITERATURE (Caliari–De Marchi–Vianello / Bos et al.; record bos-dmv-xu-2007, UNVERIFIED there) — only in (c)'s "form a basis" (linear independence of the n+2 generators is proved here from their distinct top monomials; spanning I_{n+1} needs dim I_{n+1} = n+2, i.e. unisolvence; `r02_structure.py` finds numerically dim I_{n+1} = n+2 for n ≤ 7).

## Status by part

Overall status: PROVED under the stated assumption that the Padua points are Π_n-unisolvent (used only for the spanning claim in (c); verified exactly for n ≤ 4 by the reconstruction's `unisolvence_check.py`; not load-bearing for PD-N?…-301/303).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) p_C ∈ S_1, Hessian formula, dim of C-space | PROVED (routine) | below |
| (b) sufficient condition; equivalence under injectivity + dim S_1 = n(n+1)/2 | PROVED (routine, uses 303(f)) | below |
| (c) vanishing, top forms, interior gradients | PROVED | trigonometric identities below; MEASURED check `padua_generators_check.py` |
| injectivity of C ↦ p_C and S_1 = {p_C} | MEASURED (not proved) | Padua n ≤ 7; random square sets n ≤ 6 (seed 1): rank = n(n+1)/2, principal-angle cosines 1 to 1e-15 (PD-T?…-307 item 5) |

## Depends on

PD-T?…-303(e),(f). LITERATURE: Padua unisolvence; the two-term generator type matches BDMVX 2007 Thm 2.3 as reported (record bos-dmv-xu-2007, UNVERIFIED, different convention) — not used as proof.

## Checks

`python3 padua_generators_check.py` → `directions/L3/logs/padua_generators_check.log` (n = 1..8: max |generator| at nodes ≤ 2.7e-15; rank n+2; interior gradient formula error ≤ 4.1e-14). `python3 r02_structure.py padua 7` → `r02_structure_padua.log`; `python3 r02_structure.py random 6 1` → `r02_structure_random_seed1.log`.

## Sources

As above.

## Proof or evidence

(a) Top-degree part of p_C is Σ c_jk x^{j+k} y^{2n+2−j−k} = Σ_m (Σ_{j+k=m} c_jk) x^m y^{2n+2−m} = 0, so deg p_C ≤ 2n+1. q_j(z_i) = 0 gives p_C(z_i) = 0, ∇p_C(z_i) = Σ c_jk (q_j∇q_k + q_k∇q_j)(z_i) = 0, and Hess p_C(z_i) = Σ c_jk(∇q_j∇q_kᵀ + ∇q_k∇q_jᵀ)(z_i) = 2G_iᵀCG_i. Dimension: (n+2)(n+3)/2 − (2n+3) independent linear conditions (each anti-diagonal sum involves a distinct set of entries) = n(n+1)/2. Existence/uniqueness of the normalised basis: the top-form map I_{n+1} → {binary forms of degree n+1} is injective (an element with zero top form has degree ≤ n and vanishes on a Π_n-unisolvent set) between spaces of equal dimension n+2.
(b) First claim: p_C ∈ S_1 with PD Hessians; apply 303(e). Second: then S_1 = {p_C}, the Hessian map is C ↦ (2G_iᵀCG_i)_i and 303(f) reads: ∃ A_i ≻ 0 with Σ_i ⟨A_i, G_iᵀCG_i⟩ = ⟨Σ_i G_iA_iG_iᵀ, C⟩ = 0 for all C ⊥ Hankel, i.e. Σ_i G_iA_iG_iᵀ ∈ (Hankel^⊥)^⊥ = Hankel.
(c) With x = cos θ, y = cos φ, θ = jπ/n, φ = kπ/(n+1), j+k even: sin nθ = 0, sin(n+1)φ = 0, cos nθ = cos(n+1)φ = s. Then T_{n−m}(x) = cos nθ cos mθ + sin nθ sin mθ = sT_m(x) and T_{n+1−m}(y) = sT_m(y), so g_m = sT_mT_m − T_m sT_m = 0; ω = −sin θ sin nθ = 0. Top forms: only T_m(x)T_{n+1−m}(y) has degree n+1, leading coefficients of T_k are positive. Interior gradients (sin θ, sin φ ≠ 0): T_k′ = kU_{k−1}, U_{n−m−1}(x) = sin((n−m)θ)/sin θ = −s U_{m−1}(x), U_{n−m}(y) = sin((n+1−m)φ)/sin φ = −s U_{m−1}(y); substitute into ∂_x g_m = (n−m)U_{n−m−1}(x)T_m(y) − mU_{m−1}(x)T_{n+1−m}(y) and ∂_y g_m = T_{n−m}(x) mU_{m−1}(y) − T_m(x)(n+1−m)U_{n−m}(y). ω′(x) = cos θ sin nθ/ sin θ + n cos nθ = ns.

## Scope

Reduces the square-case obstruction test to a structured SDP in C (n(n+1)/2 unknowns) with explicit data for Padua; the remaining step for "obstruction for all Padua n ≥ 3" is an explicit C (OPEN, R02 next question).

## Open items

(1) Prove injectivity / S_1 = {p_C} (symbolic square of a reduced square point set in degree 2n+1). (2) Explicit C for all Padua n ≥ 3 with positivity proof, including the 2n+1 boundary nodes (where the interior gradient formula does not apply). (3) Interpret the Hankel test (Σ G_iA_iG_iᵀ Hankel = PSD Hankel = "moment matrix of directions at infinity").

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R02.
- 2026-10-31T23:54:00+01:00, L3 developer: findings L6 (injectivity as an explicit conjunct) and L7 (status wording: assumption, not LITERATURE dependency) of L3-reconstruction-01 (topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md, audited head 0b7b396).
