# PD-T?bivariate-lanczos-claude-318 — Square case: exact first-order formula for the last-block commutator, d(κ∘Φ)(E) = (E(s_ab)), and rank d(κ∘Φ) = dim{p_C : C ⊥ Hankel}

Final ID: **PD-T074** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: derivative formula for κ; remainder polynomials R^x_a, R^y_a; s_ab = R^y_aR^x_b − R^x_aR^y_b; reduction of the 304(c) isomorphism to the quadratic-generator conjunct of 309; dκ image = Hankel family.
Split from: none (new supporting result, created in response to finding LF-M2 of Codex audit-01; supports PD-T?bivariate-lanczos-claude-316).
Split into: none.

## Statement

Notation of PD-T?…-301, 304, 309: n ≥ 1, graded order, N = N_n, V = Π_{2n+1}, S_1 = {p ∈ V : p(z_i) = 0, ∇p(z_i) = 0 ∀ i}, T = span{ev_{z_i}, ∂_x ev_{z_i}, ∂_y ev_{z_i}} ⊂ V*. For a functional L on Π_{2n+1} with M_n(L) ≻ 0 let p_a = p_a(L) be its graded orthonormal polynomials, Π_L : Π_{n+1} → Π_n the L-orthogonal projection Π_L f := Σ_{deg c ≤ n} L(f p_c) p_c, and for deg a = n
 R^x_a(L) := x p_a − Π_L(x p_a), R^y_a(L) := y p_a − Π_L(y p_a) ∈ Π_{n+1},
 s_ab(L) := R^y_a(L) R^x_b(L) − R^x_a(L) R^y_b(L) (deg a = deg b = n).
Index the last block κ(Ĥ) = ([Ĥ_x, Ĥ_y])_{nn} by the degree-n indices a, b.

(a) [Exact formula, any L.] s_ab(L) ∈ Π_{2n+1} and κ(Φ(L))_{ab} = L(s_ab(L)).
(b) [Derivative at a square-case measure.] Let M = N_n, nodes Π_n-unisolvent, w_i > 0, μ = Σ w_i δ_{z_i}, and write R^x_a, R^y_a, s_ab for their values at L_μ. Then R^x_a, R^y_a vanish at every node, s_ab ∈ S_1, and for every E ∈ V*:
 d(κ∘Φ)_{L_μ}(E)_{ab} = E(s_ab).
(c) [Image.] Let q_0, …, q_{n+1} be the basis of I_{n+1} = {q ∈ Π_{n+1} : q(z_i) = 0 ∀ i} with top forms x^j y^{n+1−j} (PD-T?…-309), and u_a ∈ ℝ^{n+1} the coefficient vector of the top form of p_a (top p_a = Σ_s u_{a,s} x^s y^{n−s}). Then R^y_a = Σ_s u_{a,s} q_s, R^x_a = Σ_s u_{a,s} q_{s+1}, s_ab = p_{C(u_a, u_b)} with C(u, v) := sym(ũ v̆ᵀ − ŭ ṽᵀ), ũ := (u, 0), ŭ := (0, u) ∈ ℝ^{n+2}, and
 span{s_ab : deg a = deg b = n, a < b} = F := {p_C : C ⊥ Hankel} (the family of PD-T?…-309(a)).
(d) [Consequences.] rank d(κ∘Φ)_{L_μ} = dim F ≤ n(n+1)/2, and d(κ∘Φ)_{L_μ} factors as E ↦ E|_{S_1} followed by the transpose of σ : ℝ^{a<b} → S_1, e_ab ↦ s_ab. The induced map V*/T → Skew_{n+1} is an isomorphism iff dim F = dim S_1 = n(n+1)/2, i.e. iff the 3N_n jet functionals are linearly independent, C ↦ p_C is injective on {C ⊥ Hankel} and S_1 = F (the conjunct recorded as MEASURED in PD-T?…-309). In that case κ is, to first order, a linear isomorphic image of the S_1*-component E|_{S_1} of the perturbation.

## Definitions

As in PD-T?…-301, 304, 309. "C ⊥ Hankel": Σ_{j+k=m} c_jk = 0 for m = 0, …, 2n+2; p_C := Σ_{j,k} c_jk q_j q_k; B_C(z, w) := Σ_{j,k} c_jk z^j w^k; h_k(z, w) := Σ_{l=0}^k z^l w^{k−l}.

## Assumptions

[EXACT]. (a): any L on Π_{2n+1} with M_n(L) ≻ 0. (b)–(d): square case, Π_n-unisolvent nodes, positive weights.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) κ_ab = L(s_ab) | PROVED | proof below; MEASURED sanity at an arbitrary perturbed functional L with M_n(L) ≻ 0, not constructed from an explicit measure (rel. err ≤ 1.4e-10, `t318_dkappa_formula_check.py`; no test of nonrepresentability is made or needed) |
| (b) derivative formula | PROVED | proof below; MEASURED sanity: central differences agree to ≤ 2.7e-8 (relative) for Padua n = 1..4, equispaced n = 3, random n = 3 |
| (c) image = F | PROVED | proof below; MEASURED: rank d(κ) = dim F in all six sets |
| (d) rank and isomorphism criterion | PROVED (routine from (b), (c)) | — |

## Depends on

PD-T?…-301 (sections, words formula not needed), PD-T?…-304(c) (factorisation, re-derived here), PD-T?…-309(a) (top-form injectivity on I_{n+1}, dimension of {C ⊥ Hankel}). The Hankel parametrisation B_C = (z − w)²K is proved below (it was a working derivation in R05 §2).

## Checks

`OPENBLAS_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L3/t318_dkappa_formula_check.py` (Python 3.13.18, numpy 2.5.3; sha256 8ade3424969a22c2aca1744ce5d8e612117a8c138ddeff9b2e17609d74ce0ea1) → `topics/bivariate-lanczos-20261031/directions/L3/logs/t318_dkappa_formula_check.log` (sha256 fcc4cc02799253d15a96c531bf93798725e46b3363befa91aaff30839c885e08), run 2026-11-01 ≈08:33 by the developer. Monomial basis; weights numpy default_rng(1) uniform [0.5, 1.5] normalised; random nodes default_rng(0); central differences on every moment coordinate with step h = min(1e-5, 2e-4 λ_min(M_n(L_μ))). Observed: jets of s_ab at the nodes ≤ 6.4e-12; FD vs formula max relative difference 1.9e-10, 2.5e-8, 2.7e-8, 2.2e-8 (Padua n = 1..4), 1.4e-8 (equispaced n = 3), 2.2e-8 (random n = 3; 1.7e-2 at h = 1e-5 because λ_min(M_3) = 5.7e-5 — pure O(h²) truncation, decreasing to 1.7e-8 at h = 1e-8 in an interactive check); rank d(κ) = dim F = dim S_1 = n(n+1)/2 in all six cases; identity (a) at a random perturbed functional with M_n ≻ 0, not constructed from an explicit measure (the checker's printed label "non-measure" means only this; it does not test that no positive representing measure exists, and (a) is proved for the whole stated class regardless): relative error ≤ 1.3e-10. This is a verification record (MEASURED), not the proof. Independent check: pending (Codex re-audit).

## Sources

None.

## Proof or evidence

(a) For deg a ≤ n, Π_L(x p_a) = Σ_c (H_x)_{ca} p_c with (H_x)_{ca} = L(x p_a p_c); orthonormality gives (H_x H_y)_{ab} = Σ_c L(x p_a p_c) L(y p_b p_c) = L(Π_L(x p_a) Π_L(y p_b)) and (H_y H_x)_{ab} = L(Π_L(y p_a) Π_L(x p_b)). Let L̃ be any linear extension of L to Π_{2n+2}. Since Π_L(x p_a) ∈ Π_n and L(R q) = 0 for every remainder R and every q ∈ Π_n (all such products have degree ≤ 2n+1):
 L(Π_L(x p_a) Π_L(y p_b)) = L̃((x p_a − R^x_a) Π_L(y p_b)) = L̃(x p_a · Π_L(y p_b)) = L̃(x p_a · y p_b) − L̃(x p_a R^y_b),
 L̃(x p_a R^y_b) = L̃(Π_L(x p_a) R^y_b) + L̃(R^x_a R^y_b) = L̃(R^x_a R^y_b).
So (H_xH_y)_{ab} = L̃(xy p_a p_b) − L̃(R^x_a R^y_b), and likewise (H_yH_x)_{ab} = L̃(xy p_a p_b) − L̃(R^y_a R^x_b). Subtracting, κ_ab = L̃(s_ab). For deg a = n, top(R^x_a) = x·top(p_a) and top(R^y_a) = y·top(p_a) (Π_L(·) has degree ≤ n), so the degree-(2n+2) parts of R^y_aR^x_b and R^x_aR^y_b are both xy·top(p_a)top(p_b) and cancel: s_ab ∈ Π_{2n+1}, and L̃(s_ab) = L(s_ab) does not depend on the extension.
(b) Square case: for f ∈ Π_{n+1}, Π_{L_μ} f is the unique g ∈ Π_n with Σ_i w_i (f − g)(z_i) q(z_i) = 0 for all q ∈ Π_n; by unisolvence (q(z_i))_i ranges over ℝ^N, so (f − g)(z_i) = 0 for all i, i.e. Π_{L_μ} is interpolation at the nodes. Hence R^x_a(z_i) = R^y_a(z_i) = 0, and each product R R′ has value and gradient 0 at every node: s_ab ∈ S_1. L ↦ p_a(L) (Cholesky of M_n(L)) and L ↦ Π_L are real-analytic on {M_n(L) ≻ 0}, so L ↦ s_ab(L) ∈ Π_{2n+1} is analytic and κ_ab(L) = L(s_ab(L)). Differentiating at L_μ in direction E: d κ_ab(E) = E(s_ab) + L_μ(Ds_ab[E]), and Ds_ab[E] = DR^y_a[E]R^x_b + R^y_a DR^x_b[E] − DR^x_a[E]R^y_b − R^x_a DR^y_b[E] (remainders at L_μ). Each term contains a factor vanishing at every node, and L_μ = Σ w_i ev_{z_i} is defined on all polynomials, so L_μ(Ds_ab[E]) = 0.
(c) R^y_a ∈ I_{n+1} has top form y·top(p_a) = Σ_s u_{a,s} x^s y^{n+1−s}, which is also the top form of Σ_s u_{a,s} q_s ∈ I_{n+1}; the top-form map is injective on I_{n+1} (an element with zero top form lies in Π_n and vanishes on a Π_n-unisolvent set; PD-T?…-309(a)), so R^y_a = Σ_s u_{a,s} q_s; likewise R^x_a = Σ_s u_{a,s} q_{s+1}. Expanding, s_ab = Σ_{j,k} (ũ_a ŭ_bᵀ − ŭ_a ũ_bᵀ)_{jk} q_j q_k = p_{C(u_a, u_b)} (a quadratic form sees only the symmetric part). The matrix U with rows u_a (deg a = n) is lower triangular with positive diagonal (the leading monomial of p_{(n,s′)} is x^{s′}y^{n−s′}, its other degree-n monomials have smaller x-exponent), hence invertible. C is bilinear and antisymmetric, so it factors through Λ²ℝ^{n+1}, and {u_a ∧ u_b} spans Λ²ℝ^{n+1}; therefore span{C(u_a, u_b)} = span{C(e_i, e_j) : 0 ≤ i < j ≤ n}. Now C(e_i, e_j) = sym(e_i e_{j+1}ᵀ − e_{i+1} e_jᵀ) has
 B_{C(e_i,e_j)}(z, w) = ½(z^i w^{j+1} + z^{j+1} w^i − z^{i+1} w^j − z^j w^{i+1}) = ½(w − z)(z^i w^j − z^j w^i) = ½(w − z)² (zw)^i h_{j−i−1}(z, w).
Hankel parametrisation: C ⊥ Hankel ⟺ B_C(z, z) = Σ_m (Σ_{j+k=m} c_jk) z^m = 0 ⟺ (z − w) | B_C; B_C is symmetric, so B_C/(z − w) is antisymmetric and vanishes on the diagonal, whence (z − w)² | B_C. Thus {C ⊥ Hankel} ≅ {K symmetric, bidegree ≤ (n−1, n−1)} via B_C = (z − w)²K, a space of dimension n(n+1)/2 with basis m_{ab} := z^a w^b + z^b w^a (a < b), m_{aa} := z^a w^a (0 ≤ a ≤ b ≤ n−1). The polynomials K_{ij} := ½(zw)^i h_{j−i−1} (0 ≤ i < j ≤ n) have bidegree ≤ (j−1, j−1) and K_{ij} = ½ m_{i, j−1} + (combination of m_{a,b} with a > i), because the monomials z^{i+l}w^{j−1−l} of (zw)^i h_{j−i−1} have both exponents ≥ i, with equality only for l = 0 or l = j−1−i. The map (i, j) ↦ (i, j−1) is a bijection onto {0 ≤ a ≤ b ≤ n−1}, so the K_{ij} are triangular with respect to a basis ordered by decreasing a, hence a basis. So {C(e_i, e_j)} is a basis of {C ⊥ Hankel}, and span{s_ab} = {p_C : C ⊥ Hankel} = F.
(d) By (b), d(κ∘Φ)(E) = (E(s_ab))_{a<b} (skew: s_ba = −s_ab, s_aa = 0), so its rank is dim span{s_ab} = dim F (V* separates V); dim F ≤ dim{C ⊥ Hankel} = n(n+1)/2. It vanishes on T = S_1^⊥ and the induced map on V*/T ≅ S_1* is the transpose of σ. That map is an isomorphism iff σ : ℝ^{n(n+1)/2} → S_1 is bijective, iff dim F = n(n+1)/2 = dim S_1 (F ⊂ S_1, dim S_1 ≥ n(n+1)/2), iff (dim S_1 = n(n+1)/2, i.e. the jet functionals are independent) and (C ↦ p_C injective on {C ⊥ Hankel}) and (F = S_1).

## Scope

Square case, any Π_n-unisolvent node set and positive weights. Turns the OPEN first-order isomorphism (PD-T?…-316) into the equivalent algebraic condition dim{p_C : C ⊥ Hankel} = dim S_1 = n(n+1)/2 on the nodes alone (weight-independent). Formula (a) holds for arbitrary functionals and gives κ explicitly in terms of degree-(n+1) remainders.

## Open items

Whether dim F = dim S_1 = n(n+1)/2 for every Π_n-unisolvent square set (PD-T?…-316 / 309 open conjunct). For Padua n = 1, 2, 3 the reviewer of L3-reconstruction-01 reports the exact identity rank(C ↦ p_C) = dim S_1 (`tracks/bivariate-lanczos/code/review_L3/indep_generator_cert.py`, log `reviews/logs_L3/indep_generator_cert.log`), which by (d) would give the isomorphism there; that corollary is not registered here (Runs needed: independent rerun of that exact check, then register it as its own claim).

## History

- 2026-11-01T08:33:39+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer: created in response to finding LF-M2 of Codex audit-01 (topics/bivariate-lanczos-20261031/audit-01/L3-framework.md; candidate 5ccfac2), which asked for a split of the unproved isomorphism of PD-T?…-304(c) or a complete proof. This file proves the derivative formula and reduces the isomorphism to the 309 conjunct; it does not prove the isomorphism.
- 2026-11-01T09:24:53+01:00 (Claude orchestrator `claude-opus-5-5`, response to Codex audit-02 A2-L4 / LC2-L1): evidence label corrected; the checker and its log are unchanged (their "non-measure" label is explained here). Original wording: «MEASURED sanity at non-measure L (rel. err ≤ 1.4e-10, `t318_dkappa_formula_check.py`)»; «identity (a) at a random non-measure functional with M_n ≻ 0: relative error ≤ 1.3e-10.». Status (PROVED) unchanged.
