# PD-T?bivariate-lanczos-claude-501 — Worst-case rotation-count bound for point-by-point Givens updating

ID kind: PD-T.
Aliases: Higham-style rotation bound; Theorem A (L5 R02); IDEA?bivariate-lanczos-claude-503.
Split from: none (new L5 result; routine instance of rotation error analysis).
Split into: none. The forward-error consequence is not claimed here (see Open items); the measured growth rates are in `givens-deficit-slopes-measured.md` (PD-T?bivariate-lanczos-claude-502).

## Statement

**Algorithm G** (Van Barel–Chesnokov 2010, Algorithm 1, real nodes; the code `givens_core.c` / `givens()` of the inputs). Data: x, y, v ∈ ℝ^M. A pivot map is fixed: for j ≥ 2 a pair (V(j), p(j)) with V(j) ∈ {H_x, H_y}, p(j) < j (the 'scheme' rule is one such map; any map that depends only on j is allowed); for j = 1 the pivot lives in the vector w. Arrays H_x, H_y ∈ ℝ^{M×M}, w ∈ ℝ^M start as H_x = diag(x), H_y = diag(y), w = v (entries of not yet inserted points are exact and untouched). For i = 2..M, for j = 1..i−1: let a = w_j (j = 1) or V(j)[j, p(j)], b = w_i (j = 1) or V(j)[i, p(j)]; if b = 0 skip; otherwise r = hypot(a,b), c = a/r, s = b/r, and replace (rows j,i of H_x, H_y, entries j,i of w) by (c·row_j + s·row_i, −s·row_j + c·row_i), then do the same to columns j,i of H_x, H_y.

**Lemma 1 (counting).** Every index q ∈ {1..M} is involved in at most M − 1 executed rotations (as row/column j or i) during the whole run, so every entry of H_x, H_y is overwritten at most 2(M−1) times; the total number R of executed rotations is at most M(M−1)/2.

**Theorem A.** [FP model below.] Let u = 2^{-53}, ε₁ := γ₃ + √2 γ₂ (1+γ₃) (γ_m = mu/(1−mu); ε₁ = 5.83u(1+O(u))), θ := √2 ε₁(2+ε₁) (θ = 16.5u(1+O(u))), ν := (‖x‖_∞² + ‖y‖_∞²)^{1/2}. If R θ ≤ 1/2, then there is an exactly orthogonal Q̃ ∈ ℝ^{M×M}, a product of the R plane rotations whose angles are those of the pairs (a,b) formed in the run, such that the computed Ĥ_x, Ĥ_y, ŵ satisfy

‖(Ĥ_x − Q̃ᵀ diag(x) Q̃, Ĥ_y − Q̃ᵀ diag(y) Q̃)‖_F ≤ 2 R θ ν ≤ 16.5 u ν M(M−1)(1+O(u)),
‖ŵ − Q̃ᵀ v‖₂ ≤ 2 R ε₁ ‖v‖₂.

In particular, relative to ‖(H_x, H_y)‖_F = ‖(x,y)‖₂, the bound is ≤ 16.5 u ν M(M−1)/‖(x,y)‖₂; for nodes in [−1,1]² with ‖(x,y)‖₂² ≳ M/2 this is O(u M^{3/2}).

## Definitions

Rotation G(c,s) = [[c, s], [−s, c]]. Joint Frobenius norm of a pair (A,B): (‖A‖_F² + ‖B‖_F²)^{1/2}. Ξ(·) = largest 2-norm of a row or column of the stacked pair (joint over H_x and H_y).

## Assumptions

(F1) Standard model fl(α∘β) = (α∘β)(1+δ), |δ| ≤ u for + − × ÷, no underflow/overflow; fused multiply-add may be used (it only removes errors). (F2) fl(hypot(a,b)) = √(a²+b²)(1+θ_h), |θ_h| ≤ 2u (the libm used in `givens_core.c` documents < 1 ulp; this is an assumption about the library, not a proof about it). (F3) pivot tests a,b are exact comparisons with 0 on stored values. No assumption on nodes (not necessarily unisolvent prefixes, not necessarily distinct), weights, or order.

## Status by part

Overall status: PROVED (Lemma 1, Lemma 2, Lemma 3 are routine steps of the Theorem A proof and are labelled below; the file's main statement is Theorem A).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Lemma 1 (each index in ≤ M−1 rotations) | PROVED, minor routine step | proof below |
| Lemma 2 (one computed rotation applied to a 2-vector) | PROVED, minor routine step | proof below; instance of Higham ASNA Lemma 19.7 (LITERATURE, UNVERIFIED, not read) |
| Lemma 3 (one similarity step) | PROVED, minor routine step | proof below |
| Theorem A | PROVED | induction below |

Candidate / claim disposition: not applicable (this is a positive result).

## Depends on

Nothing in the registry. Literature: `higham-2002` (LIT?bivariate-lanczos-claude-046, UNVERIFIED) is cited only as the place where an analogue is reported; no step uses it.

## Checks

Sanity check of the operation counts (Lemma 1): `givens_core.c` (production log `logs/r01_padua_cub.jsonl`, field `stats_givens-scheme`) executes R = 2 031 110 = 2016·2015/2 − 10 rotations for the Padua n = 62 set in the given order (10 skipped with b = 0), 2 031 117 for sortx (3 skipped) and exactly 2 031 120 = M(M−1)/2 for the three random orders (none skipped), consistent with R ≤ M(M−1)/2 (see R01.md). The theorem has not been checked numerically beyond that count, and the constants (e.g. 16.5u) are not claimed sharp. Independent check: none yet (audit pending).

## Sources

LIT?bivariate-lanczos-claude-046 (reported, UNVERIFIED); VB–C 2010 Algorithm 1 (p. 391; fulltext read).

## Proof or evidence

**Lemma 1.** Rotations are indexed (j,i) with j < i, formed during insertion step i. Row/column q is touched (i) at step i = q by the rotations (j,q), j = 1..q−1, i.e. ≤ q−1 of them; (ii) at each step i > q by the single rotation (j = q, i), i.e. ≤ M−q of them over the run. Total ≤ M−1. An entry (p,q) changes only when a rotation involves row p (row stage) or column q (column stage), giving ≤ 2(M−1) overwrites. The total count is Σ_i (i−1) = M(M−1)/2. ∎

**Lemma 2.** Let (a,b) be the stored pivot pair, r = √(a²+b²) (exact), c = a/r, s = b/r, G = G(c,s) (exactly orthogonal). By (F1),(F2): ĉ = c(1+θ₁), ŝ = s(1+θ₂) with |θ_i| ≤ γ₃ [(1+u)/(1−2u) ≤ 1+γ₃ and (1−u)/(1+2u) ≥ 1−γ₃]. Hence (δc,δs) := (ĉ−c, ŝ−s) satisfies ‖(δc,δs)‖₂ ≤ γ₃. Let Ĝ = G(ĉ,ŝ) = G + ΔG with ΔG = [[δc, δs], [−δs, δc]]; ΔG = ‖(δc,δs)‖₂ times a rotation, so ‖ΔG z‖₂ = ‖(δc,δs)‖₂‖z‖₂ ≤ γ₃‖z‖₂ for z ∈ ℝ². For a pair z = (p,q), the code evaluates p' = fl(fl(ĉp) + fl(ŝq)), q' = fl(fl(−ŝp) + fl(ĉq)) (three roundings each), so p' = ĉp + ŝq + e₁ with |e₁| ≤ γ₂(|ĉp|+|ŝq|) ≤ γ₂ (ĉ²+ŝ²)^{1/2}‖z‖₂ ≤ γ₂(1+γ₃)‖z‖₂, and likewise for q'. Therefore fl(Ĝz) = Gz + f with f = ΔG z + e, ‖f‖₂ ≤ [γ₃ + √2γ₂(1+γ₃)]‖z‖₂ = ε₁‖z‖₂. ∎

**Lemma 3.** Let B be one of the two arrays (restricted to the first n = i rows/columns; entries outside are exact zeros or exact untouched diagonal entries and remain unchanged by the identical operations). Row stage: for every column ℓ apply Lemma 2 to z_ℓ = (B_{jℓ}, B_{iℓ}); get B' = G B + E₁, E₁ supported on rows j,i, ‖E₁‖_F ≤ ε₁‖B[{j,i},:]‖_F. Column stage: for every row k apply Lemma 2 to (B'_{kj}, B'_{ki}); the output pair is G(·), so B'' = B'Gᵀ + E₂ with ‖E₂‖_F ≤ ε₁‖B'[:,{j,i}]‖_F. Hence B'' = G B Gᵀ + E₁Gᵀ + E₂. For the stacked pair (B_x, B_y): rows j,i of the pair have joint Frobenius norm ≤ √2 Ξ (two rows, each ≤ Ξ); ‖GB[:,{j,i}]‖_F-part is unchanged by the orthogonal row rotation so ‖B'[:,{j,i}]‖_F ≤ √2Ξ + ‖E₁‖_F ≤ √2Ξ(1+ε₁). So the joint error of the step is

‖F‖ ≤ ‖E₁‖ + ‖E₂‖ ≤ √2 ε₁ (2+ε₁) Ξ = θ Ξ,

with Ξ the maximal joint row/column norm of the stacked pair before the step. For w: ŵ' = Gŵ + f_w, ‖f_w‖₂ ≤ ε₁‖ŵ‖₂. ∎

**Theorem A.** Let Q̃_k = G₁ᵀ⋯G_kᵀ (G_k = embedded rotation of the k-th executed rotation, exactly orthogonal), S_k = (Q̃_kᵀXQ̃_k, Q̃_kᵀYQ̃_k), D_k = (Ĥ_x^{(k)}, Ĥ_y^{(k)}) − S_k the deviation of the computed pair after k executed rotations. By Lemma 3, D_k = G_k D_{k−1} G_kᵀ + F_k, and the exact orthogonal similarity preserves the Frobenius norm, so ‖D_k‖_F ≤ ‖D_{k−1}‖_F + ‖F_k‖_F ≤ ‖D_{k−1}‖_F + θ Ξ_{k−1}. Every row (column) of Q̃ᵀXQ̃ has 2-norm ≤ ‖X‖₂ and of Q̃ᵀYQ̃ ≤ ‖Y‖₂, so the joint row/column norm of S_k is ≤ ν, and for the computed pair Ξ_{k−1} ≤ ν + ‖D_{k−1}‖_F. Hence ‖D_k‖_F ≤ (1+θ)‖D_{k−1}‖_F + θν, D₀ = 0. Induction claim ‖D_k‖_F ≤ 2kθν for k ≤ R when Rθ ≤ 1/2: ‖D_k‖ ≤ (1+θ)2(k−1)θν + θν = θν(2k − 1 + 2(k−1)θ) ≤ 2kθν because 2(k−1)θ ≤ 1. With k = R ≤ M(M−1)/2 this is the first bound. For w: d_k := ‖ŵ_k − Q̃_kᵀv‖₂ ≤ d_{k−1} + ε₁(‖v‖₂ + d_{k−1}) and the same induction gives d_k ≤ 2kε₁‖v‖₂ (Rε₁ ≤ Rθ ≤ 1/2). Insertion of a new point changes no array entries in the full-size formulation (diagonal entries of future points are exact, off-diagonal entries are exact zeros). ∎

## Scope

What is proved: a normwise backward-type statement — the computed arrays are, up to the stated Frobenius error, an exact orthogonal similarity of diag(x), diag(y) — with the stated constant, for any fixed pivot map and any data. The bound counts rotations (R ≤ M²/2, each contributing ≤ θ·(row norm)); its M-dependence is the **worst case** (all rounding errors aligned): relative error O(uM^{3/2}) for nodes in the unit square.

What this does **not** show: (i) It does not separate M from √M growth. A random-sign (statistical) accumulation of the same R local errors would give ≈ √R θ ν, relative O(u M^{1/2}); the measured growth for 'scheme' (R01) lies between the two. The √M behaviour of HL/CGS2/Householder is statistical as well. (ii) For the comparators, Higham-style worst-case bounds (e.g. Householder QR: ‖ΔA‖_F ≤ γ_{cMN}‖A‖_F; LITERATURE, UNVERIFIED, not read) are of order MN u ≈ M² u for M = N — not smaller than the bound above. A worst-case comparison therefore cannot explain a Givens-versus-comparator deficit (candidate 503 fails as an explanation; see candidates.md). (iii) The computed pair does not have the exact zero pattern below the pivots; relating (Ĥ_x, Ĥ_y) to the exact structured (H_x, H_y) needs the conditioning (perturbation) hypothesis of the structured form, which is the settled-background Fischer-type extension and is **not** proved here.

**Remark (pivot map; PROVED, same proof).** The proofs of Lemmas 2–3 and of Theorem A use only that each executed rotation is G(c,s) built from one stored pair (a,b) with b != 0; they use no property of the pivot map. Theorem A therefore also holds, with the same constant, for data-dependent choices such as the 'largest' rule. Consequence (inference, not tested because the C port does not accumulate Q̃): the large errors of 'largest' (`largest-redundant-pivot-degradation.md`) are not a failure of the backward stability of the rotation sequence; they are a failure to reach the structured H of the problem (the computed arrays are an orthogonal similarity of diag(x), diag(y) to within Theorem A, but with a different Q̃ whose first-column/zero-pattern structure is not that of the problem).

## Open items

(1) Forward error: CONDITIONAL on a Lipschitz-type perturbation bound for the structured form (pivot pattern preserved), not asserted. (2) A statistical/probabilistic model of the rotation errors that explains the observed M¹ (rather than M^{1/2}) growth is OPEN; the long-double replay diagnostic in R02 tests whether the growth comes from rounding in the chase itself. (3) The sharpness of θ is not claimed.

## History

2026-10-31, Claude Sonnet 5.5 (high), L5 R02: created. No earlier version.
