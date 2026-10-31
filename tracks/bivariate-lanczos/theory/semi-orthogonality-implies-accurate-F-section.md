# PD-T?bivariate-lanczos-claude-201 — 2D Simon theorem for the formed (full-operator) section: semi-orthogonality plus local orthogonality give W_nᵀFW_{n−1} = T_F + O(u); a two-pass window supplies local orthogonality

ID kind: PD-T.
Aliases: 2D Simon theorem (F-part); section theorem for the formed section; L2-Q1(b) positive part; Proposition L (local orthogonality of the two-pass window); IDEA?…-203 (F-part), -206.
Split from: none. (The combined L2-Q1(b) target "semi-orthogonality ⇒ both sections O(u)" is answered by this file (F-part, PROVED) and PD-T?…-202 / PD-N?…-201 (J-part: obstruction).)
Split into: none.

## Statement

[FP algebra on computed quantities; no first-order truncation] BJ ordering and block window of PD-T?…-101 (F = Y full operator, J = X injecting operator; columns 0..N−1, N = N_n; child(c) the F-child of a column c of degree ≤ n−1; W_k = {l < k : deg l ≥ deg k − 2}). Let Q̂ ∈ R^{M×N} have full column rank and, for every column c of degree ≤ n−1 with k = child(c), let

  β_k q̂_k = F q̂_c − Q̂_{W_k}h_k − Q̂_{L_k}g_k − f_k,  β_k > 0, L_k ⊆ {l : l < min W_k}   (H1)

(f_k is defined by this equation; L_k, g_k are optional reorthogonalization terms). Write T e_c := Σ_{l∈W_k}(h_k)_l e_l + β_k e_k (the computed F-section, N × N_{n−1}), G e_c := Σ_{l∈L_k}(g_k)_l e_l, E e_c := f_k, so FQ̂_{n−1} = Q̂(T + G) + E. Let Ω := Q̂ᵀQ̂ − I, R := chol(I + Ω) (upper triangular, positive diagonal), W := Q̂R⁻¹ (orthonormal, span W_{:,0..k} = span Q̂_{:,0..k} for every k), S := W_nᵀFW_{n−1}. Define

- η := ‖Ω‖_F (assume η ≤ 1/4), μ := max{|Ω_ab| : a ≠ b, |deg a − deg b| ≤ 2} (local level), μ_d := max_a|Ω_aa|, μ₁ := max(μ, μ_d/2);
- ε_c := max over all relations (H1) of max(max_{l∈W_k}|(h_k)_l − q̂_lᵀFq̂_c|, |β_k − q̂_kᵀFq̂_c|) (coefficient consistency);
- τ₁ := max(max_c‖Te_c‖₁, max_r‖e_rᵀT‖₁), γ := max_c‖Ge_c‖₂, ε := ‖E‖₂.

**Theorem A.** max_{r,c}|(S − T)_{rc}| ≤ 2ε_c + 2(μ₁ + η²)τ₁ + ηγ + 2η²(‖T‖₂ + ‖G‖₂)/(1 − η) + 4ε.

**Proposition L (local orthogonality).** For a relation (H1) computed with L_k = ∅:
 (a) one CGS pass over W_k: β_k‖Ω_{W_k,k}‖_∞ ≤ ε_c′ + ‖Ω_{W_k}h_k‖_∞ + √(1+η)‖f_k‖, where Ω_{W} := Q̂_WᵀQ̂_W − I and ε_c′ := ‖Q̂_{W_k}ᵀFq̂_c − h_k‖_∞; under semi-orthogonality alone the middle term is only bounded by ‖Ω‖₂‖h_k‖₂;
 (b) two CGS passes over W_k (h_k = h⁽¹⁾ + h⁽²⁾): β_k‖Q̂_{W_k}ᵀq̂_k‖₂ ≤ ‖Ω_{W_k}‖₂²‖h⁽¹⁾‖₂ + ρ_k, where ρ_k collects the rounding of the two passes and of the normalisation, ρ_k ≤ c(w_k, M)·u·‖Fq̂_c‖ with c polynomial in the window size w_k and M (standard model, first order).
**Corollary A′ (2D Simon theorem, F-part).** If the window is processed with two CGS passes, ‖Ω‖_F ≤ η ≤ √u, and the reorthogonalization coefficients satisfy γ ≤ c′√u‖F‖, then max|S − T| = O(u)·(τ₁ + ‖T‖₂ + ‖F‖)·(1 + max_k‖Fq̂_{p(k)}‖/β_k)·poly(N, M), i.e. the computed F-section equals the section W_nᵀFW_{n−1} of an orthonormal basis of the same (computed) nested spaces up to O(u)‖F‖ with polynomial constants. With one CGS pass the same conclusion holds if, additionally, μ = O(u) (an explicit hypothesis that semi-orthogonality does not supply).

## Definitions

Local pair: a ≠ b with |deg a − deg b| ≤ 2 (equivalently min(a,b) ∈ W_{max(a,b)} for the block window). up(Z): strictly upper triangle of Z plus half its diagonal. ‖·‖_F Frobenius, ‖·‖₂ spectral.

## Assumptions

(H1) only (any orthogonalization scheme produces data of this form); full column rank; η ≤ 1/4 for Theorem A. Proposition L(b) and Corollary A′ use the standard rounding model fl(a∘b) = (a∘b)(1+δ), |δ| ≤ u, diagonal F, no underflow, first order in u for ρ_k only. Theorem A itself is exact (no first-order truncation).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Lemma 1 (exact decomposition) | PROVED | proof below |
| Lemma 2 (Cholesky perturbation, Frobenius) | PROVED | proof below |
| Lemma 3 (profile preservation) | PROVED | proof below |
| Theorem A | PROVED | region analysis below |
| Proposition L (a), (b) | PROVED ((b): first-order constant ρ_k not optimised) | proof below |
| Corollary A′ | PROVED (constants polynomial, not optimised) | from A, L(b), and the ε_c bound below |
| measured consistency | MEASURED in PD-T?…-204 | e_F ≤ 2.2e-15 at all semi-orthogonal degrees with two-pass windows on 12 benchmarks |

## Depends on

PD-T?…-101 (window supports; CONDITIONAL input, developer result under review; reconstruction 01: CONFIRMED). No literature result is used as a step; Simon 1984 Thm 2 / LAA 61 Thm 5 (LIT?…-211, -214, as reported) is the single-operator template, not a dependency.

## Checks

Measured counterpart: `tracks/bivariate-lanczos/code/L2/l2_core.py::section_errors` (e_F, local level μ) in `topics/bivariate-lanczos-20261031/directions/L2/logs/r01_sections*.raw`, verdicts `r01_verdicts.txt`. The bound itself is not evaluated numerically (constants are loose); the measurements show e_F ≈ 0.15–0.3·μ on runs where μ dominates (rot0.3, triangle, annulus, one-pass windows), consistent with the 2μ₁τ₁ term.

## Sources

LIT?bivariate-lanczos-claude-211 (Simon Math. Comp. 1984 Thm 2, read via digest; proof deferred there), -214 (LAA 61 Thm 5, secondary). Not read: Simon LAA 61 fulltext, Parlett's book. No claim that the proof follows Simon's.

## Proof or evidence

Write Δ := R − I (upper triangular), R′, Δ′ the leading N_{n−1} blocks, X := T + G.

**Lemma 1.** S = RXR′⁻¹ + Ẽ with Ẽ := R⁻ᵀQ̂ᵀER′⁻¹, and RXR′⁻¹ − X = (ΔX − XΔ′)R′⁻¹ = (ΔX − XΔ′) + ρ, ρ := −(ΔX − XΔ′)Δ′R′⁻¹.
*Proof.* W_{n−1} = Q̂_{n−1}R′⁻¹ because R is upper triangular. S = R⁻ᵀQ̂ᵀ(Q̂X + E)R′⁻¹ = R⁻ᵀ(I+Ω)XR′⁻¹ + Ẽ = RXR′⁻¹ + Ẽ since I + Ω = RᵀR. Then RX − XR′ = ΔX − XΔ′ and R′⁻¹ − I = −Δ′R′⁻¹. ∎

**Lemma 2.** If η = ‖Ω‖_F ≤ 1/4 then ‖Δ‖_F ≤ η, Δ = up(Ω) − up(ΔᵀΔ), |Δ_ab − up(Ω)_ab| ≤ η², ‖R⁻¹‖₂ ≤ 1/(1−η), ‖R‖₂ ≤ 1 + η.
*Proof.* RᵀR = I + Ω gives Δ + Δᵀ + ΔᵀΔ = Ω. For upper triangular Δ, up(Δ + Δᵀ) = Δ, so Δ = up(Ω − ΔᵀΔ). For symmetric Z, ‖up(Z)‖_F² = Σ_{a<b}z_ab² + ¼Σz_aa² ≤ ½‖Z‖_F². Hence x := ‖Δ‖_F satisfies x ≤ (η + x²)/√2. Along Ω(t) = tΩ, t ∈ [0,1] (I + tΩ ≻ 0 since ‖Ω‖₂ ≤ 1/4), x(t) is continuous, x(0) = 0 and x(t)² − √2x(t) + tη ≥ 0; the roots x± = (√2 ± √(2 − 4tη))/2 are separated (2 − 4tη ≥ 1), so x(t) ≤ x₋(t) for all t, and x₋(1) = 2η/(√2 + √(2−4η)) ≤ η. Entrywise |up(ΔᵀΔ)_ab| ≤ |(ΔᵀΔ)_ab| ≤ ‖Δe_a‖‖Δe_b‖ ≤ ‖Δ‖_F² ≤ η². σ_min(R)² = λ_min(I+Ω) ≥ 1 − η, so ‖R⁻¹‖₂ ≤ (1−η)^{-1/2} ≤ (1−η)⁻¹; ‖R‖₂ ≤ 1 + ‖Δ‖₂. The same holds for R′ (leading block of Ω). ∎

**Lemma 3.** If Z_{ab} = 0 whenever a > π(b) with π nondecreasing, then (RZR′⁻¹)_{rc} = 0 whenever r > π(c). For Z = X take π = child (strictly increasing): supp Te_c ⊆ W_{child(c)} ∪ {child(c)} ⊆ {a ≤ child(c)}, supp Ge_c ⊆ L_{child(c)} ⊆ {a < c}.
*Proof.* (RZR′⁻¹)_{rc} = Σ_{a≥r, b≤c} R_ra Z_ab (R′⁻¹)_bc; a nonzero term needs r ≤ a ≤ π(b) ≤ π(c). ∎

**Two facts used repeatedly (block window).** (i) If X_ac ≠ 0 with a ≥ c then X_ac = T_ac, a ∈ W_{child(c)} ∪ {child(c)}, so deg c − 1 ≤ deg a ≤ deg c + 1 (G has rows < c). (ii) b ∈ W_{child(b)}, hence min W_{child(b)} ≤ b, so G_rb ≠ 0 implies r < b.

**Theorem A, region by region.** By Lemma 2, for a local pair or a = r: |Δ_ra| ≤ μ₁ + η². By Lemma 1, ‖Ẽ‖₂ ≤ √(1+η)ε/(1−η)² ≤ 2ε and ‖ρ‖₂ ≤ 2‖Δ‖₂²‖X‖₂/(1−η) ≤ 2η²(‖T‖₂ + ‖G‖₂)/(1−η).
- (I) r > child(c): (RXR′⁻¹)_rc = 0 (Lemma 3) and T_rc = 0, so |(S−T)_rc| = |Ẽ_rc| ≤ 2ε.
- (II) c ≤ r ≤ child(c) (includes the diagonal, the child position and all rows of degree n): G_rc = 0 by (ii) (r ≥ c), so (S−T)_rc = (ΔX − XΔ′)_rc + ρ_rc + Ẽ_rc. First sum Σ_{a≥r}Δ_ra X_ac: by (i) X_ac = T_ac with deg a ≤ deg c + 1, and deg r ≥ deg c, a ≥ r, so (r,a) is local or a = r: bounded by (μ₁ + η²)‖Te_c‖₁. Second sum Σ_{b≤c}X_rb Δ_bc: G_rb = 0 by (ii) since r ≥ c ≥ b; T_rb ≠ 0 needs r ∈ W_{child(b)} ∪ {child(b)}, so deg r ≤ deg b + 1 and deg c ≤ deg r, hence deg c − deg b ≤ 1 and (b,c) is local or b = c: bounded by (μ₁ + η²)‖e_rᵀT‖₁. Total ≤ 2(μ₁+η²)τ₁ + 2η²‖X‖₂/(1−η) + 2ε.
- (IVa) r < c ≤ N_{n−1} − 1, c > child(r): by symmetry of the square part S_rc = S_cr = Ẽ_cr (region (I) for column r). If r ∉ W_{child(c)}, T_rc = 0 and |(S−T)_rc| ≤ 2ε. Otherwise T_rc = (h_{child(c)})_r and |T_rc − q̂_rᵀFq̂_c| ≤ ε_c, while q̂_rᵀFq̂_c = q̂_cᵀ(Q̂Xe_r + Ee_r) = X_cr + (ΩX)_cr + q̂_cᵀEe_r with X_cr = 0 (c > child(r); G rows < r). (ΩT)_cr = Σ_a Ω_ca T_ar with a ≤ child(r) < c and deg a ≥ deg r − 1 ≥ deg c − 2 (r ∈ W_{child(c)} gives deg r ≥ deg c − 1): local pairs, ≤ μτ₁. |(ΩG)_cr| ≤ ‖Ωe_c‖₂‖Ge_r‖₂ ≤ ηγ. |q̂_cᵀEe_r| ≤ √(1+η)ε. Total ≤ ε_c + μτ₁ + ηγ + 4ε.
- (IVb) r < c ≤ child(r), square part: S_rc = S_cr = T_cr + (S−T)_cr with (c, r) in region (II) for column r. T_rc = (h_{child(c)})_r (deg r ≥ deg c − 1, r < c), T_cr = β_c if c = child(r), else (h_{child(r)})_c (deg c ≥ deg r, c < child(r)); both are within ε_c of q̂_rᵀFq̂_c = q̂_cᵀFq̂_r (F symmetric), so |T_cr − T_rc| ≤ 2ε_c and |(S−T)_rc| ≤ 2ε_c + [bound (II)].
Taking the maximum over the regions gives Theorem A. ∎

**Bounds on ε_c (used for A′).** One CGS pass, standard model: |(h_k)_l − q̂_lᵀFq̂_c| ≤ γ_{M+1}|q̂_l|ᵀ|Fq̂_c| ≤ γ_{M+1}‖F‖(1 + μ_d). Two passes: h = h⁽¹⁾ + h⁽²⁾ with h⁽²⁾ = fl(Q̂_Wᵀr⁽¹⁾) = −Ω_Wh⁽¹⁾ + (Q̂_WᵀFq̂_c − h⁽¹⁾) + O(γ_M)‖Fq̂_c‖, so |(h_k)_l − q̂_lᵀFq̂_c| ≤ μ₁‖h⁽¹⁾‖₁ + O(γ_M)‖F‖ (Ω_W has only local and diagonal entries). β: q̂_kᵀFq̂_c = Σ_W Ω_lk h_l + Σ_L Ω_lk g_l + β_k(1 + Ω_kk) + q̂_kᵀf_k, so |β_k − q̂_kᵀFq̂_c| ≤ μ‖h_k‖₁ + ‖Ω_{L,k}‖₂‖g_k‖₂ + β_kμ_d + √(1+η)‖f_k‖.

**Proposition L.** (a) Q̂_Wᵀ(β_kq̂_k) = Q̂_WᵀFq̂_c − (I + Ω_W)h_k − Q̂_Wᵀf_k = (Q̂_WᵀFq̂_c − h_k) − Ω_Wh_k − Q̂_Wᵀf_k. (b) With r⁽¹⁾ = â − Q̂_Wh⁽¹⁾ + δ₁, h⁽²⁾ = fl(Q̂_Wᵀr⁽¹⁾), r⁽²⁾ = r⁽¹⁾ − Q̂_Wh⁽²⁾ + δ₂ (â = fl(Fq̂_c)): Q̂_Wᵀr⁽²⁾ = (Q̂_Wᵀr⁽¹⁾ − h⁽²⁾) − Ω_Wh⁽²⁾ + Q̂_Wᵀδ₂ and h⁽²⁾ = −Ω_Wh⁽¹⁾ + O(γ_M‖â‖), so ‖Q̂_Wᵀr⁽²⁾‖₂ ≤ ‖Ω_W‖₂²‖h⁽¹⁾‖₂ + O(γ_M)(1 + ‖Ω_W‖₂)√w‖â‖; normalisation adds O(u)β_k. ∎ Since Ω_W is a principal submatrix of Ω, ‖Ω_W‖₂ ≤ η; no induction over earlier columns is needed, in contrast to (a), where ‖Ω_Wh‖ involves the local entries of earlier steps and can grow (the window cascade).

**Corollary A′.** Insert L(b) (μ ≤ (η² + O(Mu))max_k‖Fq̂_{p(k)}‖/β_k + μ_d, μ_d = O(Mu)), the two-pass ε_c bound and γ = O(√u‖F‖) into Theorem A with η ≤ √u: every term is O(u) times the stated factors. ∎

## Scope

Exact statement about the formed F-section of any run that satisfies (H1); semi-orthogonality in Frobenius norm (an entrywise level √u implies only η ≤ N√u, so the η² term becomes N²u — polynomial, as in single-operator theory). It says nothing about whether the computed spaces are the graded polynomial spaces S_n (PD-N?…-201: on non-product measures they are not), and nothing about the J-section (PD-T?…-202). The one-pass hypothesis μ = O(u) is genuinely extra: measured μ grows to 5e-10 (rot0.3), 6.6e-10 (triangle) at semi-orthogonal degrees, with e_F ≫ u^{3/4} there (PD-T?…-204).

## Open items

Sharper constants (τ₁ and ‖Fq̂‖/β factors); an analogue for MGS/HL ORTH (conditional second pass); the J-part (PD-T?…-202).

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R01). Proof route written before the R01 measurements (candidates.md IDEA?…-203); Proposition L(b) formulated after the R01 section suite showed that the semi-orthogonal F-failures coincide with local-level growth (disclosed in candidates.md IDEA?…-206).
