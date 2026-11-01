# PD-T?bivariate-lanczos-claude-201 — 2D Simon theorem for the formed (full-operator) section: semi-orthogonality plus local orthogonality give W_nᵀFW_{n−1} = T_F + O(u)·(1 + χ), χ = max_k‖B_kq̂_{p(k)}‖/β_k the normalisation (near-breakdown) factor; a two-pass window supplies local orthogonality

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
**Corollary A′ (2D Simon theorem, F-part; normalisation factor made explicit after audit-01, L2-F2).** For every column k ≥ 1 of degree ≤ n let B_k ∈ {F, J} be the operator of the relation that creates k (B_k = F and p(k) = c for k = child(c); B_k = J and p(k) = (t−1, 0) for a J-column k = (t, 0)), β_k its computed normalisation, and

  χ_k := ‖B_kq̂_{p(k)}‖₂/β_k,  χ := max_k χ_k   (normalisation / near-breakdown factor; β_k > 0 alone does not bound χ by any function of N and M).

If every window is processed with two CGS passes (for columns with L_k ≠ ∅: the implemented step of Remark (i)), ‖Ω‖_F ≤ η ≤ √u, and the reorthogonalization coefficients satisfy γ ≤ c′√u‖F‖, then, in the standard model to first order in u,

  max|S − T| ≤ c(N, M)·u·(1 + χ)·(τ₁ + ‖T‖₂ + ‖F‖),  c polynomial in N and M,

i.e. the computed F-section equals the section W_nᵀFW_{n−1} of an orthonormal basis of the same (computed) nested spaces up to O(u)·(1 + χ)·‖F‖ with polynomial constants (τ₁ + ‖T‖₂ ≤ 2N((1 + η)‖F‖ + ε_c), routine, see the proof). The factor χ cannot be dropped in general: it enters through Proposition L(b) and Remark (i), which bound the local level only after division by β_k. **Quantitative non-breakdown (NB).** If in addition χ ≤ χ₀, then max|S − T| ≤ c₄(N, M)·(1 + χ₀)·u·‖F‖ (c₄ polynomial) whenever c₂(N, M)·(1 + χ₀)·u ≤ 1 (c₂ from the ε_c bound in the proof); this is "O(u)‖F‖ with polynomial constants" only when χ₀ is itself bounded polynomially in N and M. With one CGS pass the conclusion holds if, additionally, μ ≤ c_μ·u (an explicit hypothesis that semi-orthogonality does not supply), and then with (1 + c_μ) in place of (1 + χ), since χ enters only through Proposition L(b).

**Remarks added after reconstruction 01 (F8); remark (i) corrected after audit-01 (L2-F2).** (i) Proposition L(b) is stated for L_k = ∅. For the implemented reorthogonalized step (two window passes h⁽¹⁾, h⁽²⁾; two passes against L_k, g_k = g⁽¹⁾ + g⁽²⁾; one further window pass h⁽³⁾ = fl(Q̂_Wᵀr), r the residual before that pass; W = W_k, W ∩ L_k = ∅) the computation of Proposition L(b) gives, in the standard model to first order,
  β_k‖Q̂_Wᵀq̂_k‖₂ ≤ η³‖h⁽¹⁾‖₂ + η²‖g_k‖₂ + ρ′_k,  ρ′_k ≤ c(w_k, |L_k|, M)·u·‖B_kq̂_{p(k)}‖₂,
so the local level of column k is at most (η³‖h⁽¹⁾‖₂ + η²‖g_k‖₂ + ρ′_k)/β_k ≤ (√(1+η)η³ + 2√(1+η)η² + c·u)·χ_k (derivation in the proof section; routine, first order). Every term carries the factor 1/β_k; it is not O(η³ + u) uniformly in β_k (audit-01 local countercheck below). (ii) The kill test of L2-Q1 uses entrywise semi-orthogonality max|Ω| ≤ √u, which gives only η ≤ N√u; the η² terms of Theorem A are then O(N²u), so "the measurements follow Theorem A" (PD-T?…-204) holds up to such polynomial factors (measured e_F is far below the bound; reconstruction 01: worst LHS/RHS = 0.16 over 35 instances).

## Definitions

Local pair: a ≠ b with |deg a − deg b| ≤ 2 (equivalently min(a,b) ∈ W_{max(a,b)} for the block window). up(Z): strictly upper triangle of Z plus half its diagonal. ‖·‖_F Frobenius, ‖·‖₂ spectral.

## Assumptions

(H1) only (any orthogonalization scheme produces data of this form); full column rank; η ≤ 1/4 for Theorem A. Proposition L(b), Remark (i) and Corollary A′ use the standard rounding model fl(a∘b) = (a∘b)(1+δ), |δ| ≤ u, diagonal F and J, no underflow, first order in u for the rounding terms ρ_k, ρ′_k only. Theorem A itself is exact (no first-order truncation). The "O(u)‖F‖ with polynomial constants" reading of Corollary A′ additionally uses the quantitative non-breakdown hypothesis (NB) χ ≤ χ₀ (audit-01, L2-F2); the χ-explicit bound needs no such hypothesis.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Lemma 1 (exact decomposition) | PROVED | proof below |
| Lemma 2 (Cholesky perturbation, Frobenius) | PROVED | proof below |
| Lemma 3 (profile preservation) | PROVED | proof below |
| Theorem A | PROVED | region analysis below |
| Proposition L (a), (b) | PROVED ((b): first-order constant ρ_k not optimised) | proof below |
| Corollary A′ | PROVED in the χ-explicit form (constants polynomial in N, M, not optimised); the "O(u)‖F‖ with polynomial constants" form PROVED under (NB) only | from A, L(b), Remark (i) and the ε_c bounds; proof below (written out after audit-01, L2-F2) |
| Remark (i): local level of the implemented reorthogonalized step, (η³‖h⁽¹⁾‖₂ + η²‖g_k‖₂ + ρ′_k)/β_k | PROVED (routine, first order; derivation below, written after audit-01) | the earlier uniform form O(η³ + η²γ/β_k + u) is withdrawn (History) |
| measured consistency | MEASURED in PD-T?…-204 | e_F ≤ 2.2e-15 at all semi-orthogonal degrees with two-pass windows on 12 benchmarks |
| size of χ in the benchmark runs | MEASURED in PD-T?…-204 (e) | χ ≤ 5.3 on all 12 benchmarks (two-pass window and PRO-2D-J runs); not a bound |

## Depends on

PD-T?…-101 (window supports; CONDITIONAL input, developer result under review; reconstruction 01: CONFIRMED). No literature result is used as a step; Simon 1984 Thm 2 / LAA 61 Thm 5 (LIT?…-211, -214, as reported) is the single-operator template, not a dependency.

## Checks

Measured counterpart: `tracks/bivariate-lanczos/code/L2/l2_core.py::section_errors` (e_F, local level μ) in `topics/bivariate-lanczos-20261031/directions/L2/logs/r01_sections*.raw`, verdicts `r01_verdicts.txt`. The bound itself is not evaluated numerically (constants are loose); the measurements show e_F ≈ 0.15–0.3·μ on runs where μ dominates (rot0.3, triangle, annulus, one-pass windows), consistent with the 2μ₁τ₁ term.

Independent checks (recorded after audit-01): reconstruction 01, 35 stress instances, worst LHS/RHS of Theorem A 0.16; Codex audit-01 (`topics/bivariate-lanczos-20261031/audit-01/L2/theorem-A-rerun.log`, reviewer script `tracks/bivariate-lanczos/code/review_L2/rl2_thmA.py` rerun in a separate environment): 35 applicable instances, no violation, max LHS/RHS 0.1612927041, one instance with η = 0.83 correctly excluded by η ≤ 1/4; audit-01 reconstructed Lemmas 1–3, the four regions, Theorem A and the χ-dependent display of A′ (no counterexample). Audit-01 local countercheck (`audit-01/L2/check_local_beta.py`, `local-beta.log`): two unit columns with Gram entry t, a = q₁ + t²e₃, three exact CGS passes give r₃ = −t³q₂ + t²e₃, β ~ t², local overlap ~ t, η ~ 2t; at t = √u/4 the ratio local/(η³ + u) is 2.6e5, 2.7e8, 2.7e11 for u = 2⁻⁴⁰, 2⁻⁶⁰, 2⁻⁸⁰ — this refutes the former uniform-in-β wording of Remark (i) and is consistent with the corrected normalised bound (η³‖h⁽¹⁾‖/β ≈ 8t). Supplementary measurement of χ: `tracks/bivariate-lanczos/code/L2/l2_audit01_chi.py` → `topics/bivariate-lanczos-20261031/directions/L2/logs/audit01_chi.raw.gz` (PD-T?…-204 (e)).

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

**Remark (i), derivation (written after audit-01, L2-F2).** W = W_k, L = L_k (W ∩ L = ∅), â = fl(B_kq̂_{p(k)}). The implemented step computes, with z⁽ⁱ⁾ = fl(Q̂_Zᵀr) = Q̂_Zᵀr + e_i and r ← r − Q̂_Zz⁽ⁱ⁾ + δ_i:
 r⁽¹⁾ = â − Q̂_Wh⁽¹⁾ + δ₁, h⁽¹⁾ = Q̂_Wᵀâ + e₁;  r⁽²⁾ = r⁽¹⁾ − Q̂_Wh⁽²⁾ + δ₂, h⁽²⁾ = Q̂_Wᵀr⁽¹⁾ + e₂;
 r⁽³⁾ = r⁽²⁾ − Q̂_Lg⁽¹⁾ + δ₃, g⁽¹⁾ = Q̂_Lᵀr⁽²⁾ + e₃;  r⁽⁴⁾ = r⁽³⁾ − Q̂_Lg⁽²⁾ + δ₄, g⁽²⁾ = Q̂_Lᵀr⁽³⁾ + e₄;
 r⁽⁵⁾ = r⁽⁴⁾ − Q̂_Wh⁽³⁾ + δ₅, h⁽³⁾ = Q̂_Wᵀr⁽⁴⁾ + e₅;  β_k = fl(‖r⁽⁵⁾‖), q̂_k = fl(r⁽⁵⁾/β_k), so β_kq̂_k = r⁽⁵⁾ + δ₆.
Each exact update multiplies by I − Q̂_ZQ̂_Zᵀ, whose 2-norm is 1 (the eigenvalues of Q̂_ZᵀQ̂_Z lie in [1 − η, 1 + η] ⊂ (0, 2)); hence ‖r⁽ⁱ⁾‖ ≤ (1 + O(u))‖â‖, ‖z⁽ⁱ⁾‖ ≤ √(1+η)(1 + O(u))‖â‖, and in the standard model ‖δ_i‖, ‖e_i‖ ≤ c(w, |L|, M)·u·‖â‖ (first order). Using Q̂_WᵀQ̂_W = I + Ω_W:
 Q̂_Wᵀr⁽¹⁾ = −e₁ − Ω_Wh⁽¹⁾ + Q̂_Wᵀδ₁, so h⁽²⁾ = −Ω_Wh⁽¹⁾ + O(u)‖â‖ and Q̂_Wᵀr⁽²⁾ = −e₂ − Ω_Wh⁽²⁾ + Q̂_Wᵀδ₂ = Ω_W²h⁽¹⁾ + O(u)‖â‖ (this is L(b));
 Q̂_Wᵀr⁽⁴⁾ = Q̂_Wᵀr⁽²⁾ − Q̂_WᵀQ̂_Lg_k + Q̂_Wᵀ(δ₃ + δ₄), where Q̂_WᵀQ̂_L is an off-diagonal block of Ω, so ‖h⁽³⁾‖₂ ≤ η²‖h⁽¹⁾‖₂ + η‖g_k‖₂ + O(u)‖â‖;
 Q̂_Wᵀr⁽⁵⁾ = −e₅ − Ω_Wh⁽³⁾ + Q̂_Wᵀδ₅, so ‖Q̂_Wᵀr⁽⁵⁾‖₂ ≤ η³‖h⁽¹⁾‖₂ + η²‖g_k‖₂ + O(u)‖â‖, and β_k‖Q̂_Wᵀq̂_k‖₂ ≤ ‖Q̂_Wᵀr⁽⁵⁾‖₂ + √(1+η)‖δ₆‖.
This is the displayed inequality with ρ′_k = O(u)‖â‖. For the sizes: ‖h⁽¹⁾‖₂ ≤ √(1+η)(1 + O(u))‖â‖; g⁽²⁾ = −Ω_Lg⁽¹⁾ + O(u)‖â‖ (same computation as h⁽²⁾), so ‖g_k‖₂ ≤ (1 + η)√(1+η)(1 + O(u))‖â‖ ≤ 2√(1+η)(1 + O(u))‖â‖; ‖â‖ ≤ (1 + u)‖B_kq̂_{p(k)}‖₂. Dividing by β_k gives the bound in χ_k. ∎ (Without division by β_k the inequality has no χ; the audit-01 countercheck shows that the division cannot be avoided for the local level itself.)

**Corollary A′.** (1) *Local level.* For the block window every local pair (a, k) with a < k has a ∈ W_k (deg a ≥ deg k − 2), so μ ≤ max_k‖Q̂_{W_k}ᵀq̂_k‖₂ over all columns k (F- and J-columns; both are processed with two window passes, and L(b) and Remark (i) apply verbatim to the J-relations with J in place of F, since their proofs use only the form of the relation). By L(b) (columns with L_k = ∅) and Remark (i) (columns with L_k ≠ ∅), with the size bounds just proved and η ≤ 1/4, ‖Q̂_{W_k}ᵀq̂_k‖₂ ≤ (3η² + c₁(N, M)u)·χ_k, hence μ ≤ (3η² + c₁u)χ; μ_d = max_a|‖q̂_a‖² − 1| = O(Mu) from the normalisation, independent of χ. (2) *ε_c.* Multiplying (H1) by q̂_lᵀ, l ∈ W_k, gives the exact identity (h_k)_l − q̂_lᵀFq̂_c = −Σ_{l′∈W_k}Ω_{ll′}(h_k)_{l′} − Σ_{l″∈L_k}Ω_{ll″}(g_k)_{l″} − q̂_lᵀf_k − β_kΩ_{lk}; all pairs (l, l′) are local or diagonal, so |(h_k)_l − q̂_lᵀFq̂_c| ≤ (μ + μ_d)‖h_k‖₁ + ηγ + √(1+η)ε + β_k‖Q̂_{W_k}ᵀq̂_k‖₂, and the last term is bounded by L(b)/Remark (i) *before* division by β_k (no χ). With the β-part bound above (also χ-free except through μ) and ‖h_k‖₁ ≤ √N‖h⁽¹⁾ + h⁽²⁾ + h⁽³⁾‖₂ ≤ √N(1 + 4η)(1 + η)(1 + O(u))‖F‖, β_k ≤ ‖r⁽⁵⁾‖(1 + O(u)) ≤ √(1+η)(1 + O(u))‖F‖, this gives ε_c ≤ c₂(N, M)·u·(1 + χ)·‖F‖ (first order; η² ≤ u, γ ≤ c′√u‖F‖, ε ≤ c₃(N, M)u‖F‖ in the standard model). (3) *Insertion.* In Theorem A: 2ε_c ≤ 2c₂u(1 + χ)‖F‖; 2(μ₁ + η²)τ₁ ≤ 2((3η² + c₁u)χ + μ_d + η²)τ₁; ηγ ≤ c′u‖F‖; 2η²(‖T‖₂ + ‖G‖₂)/(1 − η) ≤ 3u(‖T‖₂ + √N c′√u‖F‖); 4ε ≤ 4c₃u‖F‖. Every term is ≤ c(N, M)u(1 + χ)(τ₁ + ‖T‖₂ + ‖F‖). (4) *Routine size bound.* Every nonzero entry of T is (h_k)_l (l ∈ W_k) or β_k, within ε_c of q̂_lᵀFq̂_c resp. q̂_kᵀFq̂_c, and |q̂_aᵀFq̂_b| ≤ ‖q̂_a‖‖F‖‖q̂_b‖ ≤ (1 + η)‖F‖; a row or column of T has at most N nonzeros, so τ₁ ≤ N((1 + η)‖F‖ + ε_c) and ‖T‖₂ ≤ (‖T‖₁‖T‖_∞)^{1/2} ≤ τ₁ (exact). Under (NB) and c₂(1 + χ₀)u ≤ 1, ε_c ≤ ‖F‖, so τ₁ + ‖T‖₂ ≤ 2N(2 + η)‖F‖ and max|S − T| ≤ c₄(N, M)(1 + χ₀)u‖F‖. (5) *One pass with μ ≤ c_μu.* The one-pass ε_c bound and the β-part contain no factor 1/β_k, so (3) holds with c_μ in place of χ. ∎

## Scope

Exact statement about the formed F-section of any run that satisfies (H1); semi-orthogonality in Frobenius norm (an entrywise level √u implies only η ≤ N√u, so the η² term becomes N²u — polynomial, as in single-operator theory). It says nothing about whether the computed spaces are the graded polynomial spaces S_n (PD-N?…-201: on non-product measures they are not), and nothing about the J-section (PD-T?…-202). The one-pass hypothesis μ = O(u) is genuinely extra: measured μ grows to 5e-10 (rot0.3), 6.6e-10 (triangle) at semi-orthogonal degrees, with e_F ≫ u^{3/4} there (PD-T?…-204). The constants of Corollary A′ contain the normalisation factor χ: near a breakdown (β_k ≪ ‖B_kq̂_{p(k)}‖) local orthogonality, and with it the F-section accuracy, can degrade by that factor (audit-01 countercheck: local overlap ≈ √u/4 at β ≈ u/16 after three exact passes). In the benchmark runs χ ≤ 5.3 (PD-T?…-204 (e), MEASURED); no a priori bound on χ is claimed.

## Open items

Sharper constants (τ₁ and ‖Fq̂‖/β factors); an a priori (non-breakdown) bound on χ for the 2D window recurrence on given node sets (none known; χ is only MEASURED); an analogue for MGS/HL ORTH (conditional second pass); the J-part (PD-T?…-202).

## History

- 2026-11-01: created (Claude Opus 5.5, xhigh; L2 R01). Proof route written before the R01 measurements (candidates.md IDEA?…-203); Proposition L(b) formulated after the R01 section suite showed that the semi-orthogonal F-failures coincide with local-level growth (disclosed in candidates.md IDEA?…-206).
- 2026-11-01T01:28:43+01:00: Remarks (i)–(ii) after Corollary A′ added (reconstruction 01 finding F8: Prop. L(b) was applied to runs with reorthogonalization without the extension being written; Theorem-A-vs-measurement link holds only up to N² factors under entrywise SO). Statement, proof and status unchanged (Claude Opus 5.5, xhigh; L2 developer, response to reconstruction 01, `directions/L2/response-recon-01.md`).
- 2026-11-01T08:32:22+01:00: (Codex audit-01, finding **L2-F2**; Claude Opus 5.5, xhigh; L2 developer, response `directions/L2/response-audit-01.md`; rules read at 8b61391613045f547589e48dcb8037a266bad8aa) Corollary A′ restated with the normalisation factor χ := max_k‖B_kq̂_{p(k)}‖₂/β_k defined over all columns (the original wrote ‖Fq̂_{p(k)}‖/β_k for every k, although the J-columns' relations are J's) and retained in the paraphrase; the "O(u)‖F‖ with polynomial constants" reading restricted to the new explicit hypothesis (NB) χ ≤ χ₀; one-pass sentence made quantitative (μ ≤ c_μu, χ-free). Original Corollary A′: "**Corollary A′ (2D Simon theorem, F-part).** If the window is processed with two CGS passes, ‖Ω‖_F ≤ η ≤ √u, and the reorthogonalization coefficients satisfy γ ≤ c′√u‖F‖, then max|S − T| = O(u)·(τ₁ + ‖T‖₂ + ‖F‖)·(1 + max_k‖Fq̂_{p(k)}‖/β_k)·poly(N, M), i.e. the computed F-section equals the section W_nᵀFW_{n−1} of an orthonormal basis of the same (computed) nested spaces up to O(u)‖F‖ with polynomial constants. With one CGS pass the same conclusion holds if, additionally, μ = O(u) (an explicit hypothesis that semi-orthogonality does not supply)." Remark (i) corrected (the normalisation factor had been dropped on the η³ and rounding terms; the audit's exact local countercheck refutes the uniform form). Original Remark (i): "(i) Proposition L(b) is stated for L_k = ∅. For the implemented reorthogonalized step (two window passes, two passes against L_k, one further window pass) the same computation applied to the last window pass gives β_k‖Q̂_Wᵀq̂_k‖₂ ≤ ‖Ω_W‖₂‖h⁽³⁾‖₂ + ρ′_k with h⁽³⁾ = Q̂_Wᵀr before that pass and ‖h⁽³⁾‖₂ ≤ ‖Ω_W‖₂²‖h⁽¹⁾‖₂ + ‖Q̂_WᵀQ̂_{L_k}‖₂‖g_k‖₂ + O(u) ≤ η²‖h⁽¹⁾‖₂ + η‖g_k‖₂ + O(u); hence the local level is O(η³ + η²γ/β_k + u) — routine, first order, not written out further." Original proof of A′: "**Corollary A′.** Insert L(b) (μ ≤ (η² + O(Mu))max_k‖Fq̂_{p(k)}‖/β_k + μ_d, μ_d = O(Mu)), the two-pass ε_c bound and γ = O(√u‖F‖) into Theorem A with η ≤ √u: every term is O(u) times the stated factors. ∎" — replaced by the written-out proof (local level over F- and J-columns, exact ε_c identity, routine τ₁ bound) and the derivation of Remark (i). Original status row: "| Corollary A′ | PROVED (constants polynomial, not optimised) | from A, L(b), and the ε_c bound below |". Original Assumptions sentence: "Proposition L(b) and Corollary A′ use the standard rounding model fl(a∘b) = (a∘b)(1+δ), |δ| ≤ u, diagonal F, no underflow, first order in u for ρ_k only." Original Open items: "Sharper constants (τ₁ and ‖Fq̂‖/β factors); an analogue for MGS/HL ORTH (conditional second pass); the J-part (PD-T?…-202)." Added: Checks paragraph on the reconstruction-01/audit-01 reruns and the χ measurement; status rows for Remark (i) and the χ measurement; Scope sentence on χ. Theorem A, Lemmas 1–3 and Proposition L are unchanged; the χ-dependent display of A′ is unchanged in substance (audit-01: not refuted). Title changed to show χ; original title: "PD-T?bivariate-lanczos-claude-201 — 2D Simon theorem for the formed (full-operator) section: semi-orthogonality plus local orthogonality give W_nᵀFW_{n−1} = T_F + O(u); a two-pass window supplies local orthogonality". File status PROVED unchanged; no status upgrade.
