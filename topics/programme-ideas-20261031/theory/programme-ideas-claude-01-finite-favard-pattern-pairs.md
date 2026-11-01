# PD-T?programme-ideas-claude-01 — Finite Favard theorem for commuting symmetric generalized-Hessenberg pattern pairs; dimension 3N−1

Final ID: **PD-T095** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: finite Favard (M2 adversary); "commuting pattern pairs are N-node sections"; 3N−1 count; block-tridiagonal 3N−1 + C(n+2,3) count; M2 (ii)(1).
Split from: the M2 adversarial record's combined row "finite Favard … commutant in the pattern = span{I, H_x, H_y}" (`report.md` §3 at `614709d`). The commutant clause is NOT part of this record; it is a finite MEASURED observation on random instances, kept with IDEA?programme-ideas-claude-08 and false if read universally (audit-01 A3).
Split into: none.

## Statement

Fix n ≥ 1, N = dim Π_n = (n+1)(n+2)/2, and a graded monomial order m_1 = 1, m_2, …, m_N (total degree first, then a fixed order compatible with multiplication, so that m_a ≺ m_b implies x·m_a ≺ x·m_b and y·m_a ≺ y·m_b) in which every m_k (k ≥ 2) is assigned a parent m_j, j < k, with m_k = x·m_j or m_k = y·m_j (the parent map π_x or π_y). A *pattern pair* is a pair (H_x, H_y) of real symmetric N × N matrices such that, for every j and every i > π(j) in the relevant variable, H_x[i, j] = 0 (respectively H_y[i, j] = 0), i.e. column j of H_x (of H_y) has no entry below the position of the monomial x·m_j (y·m_j) — the generalized-Hessenberg pattern of Van Barel–Chesnokov 2010 — and whose *pivots* H_x[π_x(j), j], H_y[π_y(j), j] (taken at the positions that define the parent map) are nonzero.

(a) If a pattern pair commutes, it has N distinct joint eigenvalues λ_k = (x_k, y_k), each joint eigenvector has nonzero first component, the weights w_k := (e_1ᵀ q_k)² are strictly positive and sum to 1, the point set {λ_k} is Π_n-unisolvent, and (H_x, H_y) is the degree-n section pair of μ = Σ_k w_k δ_{λ_k} in the graded orthonormal basis of μ determined up to the signs of the basis polynomials, i.e. H_x = [⟨x p_j, p_i⟩_μ], H_y = [⟨y p_j, p_i⟩_μ].
(b) Conversely, for every Π_n-unisolvent set of N points in ℝ² and positive weights summing to 1, there is exactly one commuting pattern pair with positive pivots whose joint spectral data are these points and weights.
(c) The set 𝒫_n of commuting pattern pairs with positive pivots is an embedded real-analytic submanifold of the space of symmetric pairs of dimension 2N + (N − 1) = 3N − 1, real-analytically diffeomorphic to {unisolvent N-point sets} × {positive normalised weights}.
(d) The set ℬ_n of commuting *block-tridiagonal* symmetric pairs (diagonal blocks of sizes 1, …, n+1) whose off-diagonal blocks have full row rank and whose spectral data are unisolvent with positive weights has dimension 3N − 1 + Σ_{k=0}^{n} k(k+1)/2 = 3N − 1 + C(n+2, 3); the extra term is the dimension of the degree-block orthogonal gauge group ∏_{k=0}^{n} O(k+1).

## Definitions

Π_n: real bivariate polynomials of total degree ≤ n. Section pair of a discrete positive measure μ with Π_n-unisolvent support: the matrices of multiplication by x and y on Π_n ⊂ L²(μ) in an orthonormal basis, compressed to Π_n; when the support has exactly N points, Π_n = L²(μ) and the compression is the full multiplication operator, so the section pair commutes. Graded orthonormal basis: Gram–Schmidt of m_1, …, m_N in L²(μ) with positive leading coefficients.

## Assumptions

Exact real arithmetic. Pivots nonzero for (a); positive for (b)–(c) (nonzero pivots are reduced to positive pivots by the diagonal sign gauge diag(±1), which preserves the pattern). (d) uses full row rank of the off-diagonal blocks A_{k,x}, A_{k,y} in the sense needed for the LQ normalisation of the proof; only the nondegenerate class is claimed.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) commuting pattern pair ⇒ N-node section pair | PROVED | proof below (developer proof of `checks/adversarial-M2.md` (ii)(1) steps (a)–(e), restated with the hypotheses explicit); independently reconstructed by the Codex audit on the nondegenerate positive-pivot class (`audit-support/obstructions-report.md`, "Checks completed") |
| (b) existence and uniqueness from nodes and weights | PROVED | proof below (step (f)) |
| (c) manifold of dimension 3N − 1 | PROVED (routine from (a), (b)) | proof below; MEASURED tangent dimensions 29/44/62/83 at n = 3..6 agree (`checks/code/adv/M2/m2_favard_commutant.py`, replayed by the audit) |
| (d) block-tridiagonal class 3N − 1 + C(n+2,3) | PROVED on the stated nondegenerate class | proof sketch below (step (g)); MEASURED 39/64/97/139 at n = 3..6 agree |

Minor classification: the sign-gauge reduction and the smoothness of the inverse map in (c) are routine steps kept here and not split.

## Depends on

Linear algebra only. Overlap, by pinned reference (not used as a dependency): `PD-T?bivariate-lanczos-claude-304`(b) at `5f523313b7b388cb114103734028f0a850dfeaad` (`tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-304-square-case-commutator-bounds.md`) proves the analogue of (a) for exactly commuting *block-tridiagonal structured* pairs with positive pivots (Lanczos class 𝒞_n). Part (a) here is the same mechanism for the generalized-Hessenberg pattern; parts (c)–(d) (the parameter counts) are not stated there. `PD-T?bivariate-lanczos-claude-301` (same SHA) is the interior-commutativity/functional version and is not needed.

## Checks

- `checks/code/adv/M2/m2_favard_commutant.py` (frozen at `614709d`): tangent dimensions of the commuting positive-pivot pattern class 29/44/62/83 and of the block-tridiagonal class 39/64/97/139 for n = 3..6 (random nodes/weights); joint-eigenvector residuals ≤ 1.7e-15. MEASURED; replayed independently by the Codex audit (`audit-support/obstructions-check.json`).
- Independent rerun of the proof: Codex audit-01 reconstructed the argument on the nondegenerate positive-pivot graded-pattern class (cyclic constant vector, simple joint eigenspaces, strictly positive weights, invertible weighted Vandermonde).

## Sources

LITERATURE context, not used as proof: Xu, Trans. AMS 342 (1994), Thms 3.2/3.4 (infinite block-Jacobi / Favard); Mysovskikh (Gaussian cubature ⇔ commuting sections; cited through Xu); Laurent–Mourrain 2009 (flat extension); Kreuzer–Robbiano arXiv 2503.01752v1 Props 5.4–5.6 (ideal chart of the planar simplicial border-basis scheme, an affine cell of dimension 2N; primary excerpt checked by the audit). These give neighbouring statements; none states the 3N − 1 count for the orthonormal recurrence-entry pattern pair (search scope: `checks/adversarial-M2.md` search log, 2026-11-01; not exhaustive).

## Proof or evidence

(a) Commuting real symmetric matrices are simultaneously orthogonally diagonalisable: H_x = QΛ_xQᵀ, H_y = QΛ_yQᵀ. Define polynomials p_1 = 1 and, for m_k = x·m_j, p_k := (x p_j − Σ_{i<k} H_x[i, j] p_i)/H_x[k, j] (the sum runs over the rows allowed by the pattern in column j; similarly with y for m_k = y·m_j). Let v be any joint eigenvector with eigenvalue λ = (ξ, η). Row j of H_x v = ξ v, read through symmetry as the column-j equation Σ_{i ≤ π_x(j)} H_x[i, j] v_i = ξ v_j, gives v_k = v_1 p_k(λ) by induction on k (the pivot H_x[k, j] ≠ 0 allows solving for v_k). Hence v_1 ≠ 0 (otherwise v = 0), every joint eigenspace is one-dimensional, and the N joint eigenvalues are distinct, with q_k = ±P(λ_k)/‖P(λ_k)‖, P = (p_1, …, p_N)ᵀ, and w_k = (e_1ᵀq_k)² = ‖P(λ_k)‖^{−2} > 0, Σ w_k = ‖e_1‖² = 1. QᵀQ = I reads Σ_k w_k p_i(λ_k) p_l(λ_k) = δ_{il}: the p_i are orthonormal in L²(μ). By construction p_k has leading monomial m_k with nonzero leading coefficient, so {p_i} spans Π_n, the N × N evaluation matrix [p_i(λ_k)] is invertible, and {λ_k} is Π_n-unisolvent. Up to the signs of the p_i (fixed by requiring positive leading coefficients, equivalently positive pivots after the diagonal sign gauge) {p_i} is the graded orthonormal basis of μ, and H_x = QΛ_xQᵀ has entries Σ_k w_k ξ_k p_i(λ_k) p_l(λ_k) = ⟨x p_l, p_i⟩_μ; likewise H_y.
(b) Given unisolvent points and positive weights, the weighted graded Vandermonde V_w = [√w_k m_i(λ_k)] is invertible; its QR factorisation with positive diagonal is unique, Q's columns give the graded orthonormal basis, and the section pair built from it is a commuting pattern pair with positive pivots (the pattern holds because x·p_j has leading monomial x·m_j and p_i ⊥ span{m_1, …, m_{i−1}}). Uniqueness of the pair from the data follows from uniqueness of the positive-diagonal QR, and (a) shows every commuting positive-pivot pattern pair arises this way.
(c) The map (points, weights) ↦ pair is real-analytic (QR with positive diagonal is analytic on invertible matrices); its inverse (pair ↦ joint spectral data) is real-analytic on 𝒫_n because the joint spectrum is simple by (a). The parameter space has dimension 2N (points) + N − 1 (normalised weights).
(d) For the block-tridiagonal class the sections in any orthonormal basis that is graded by degree blocks (not by monomials) are block-tridiagonal; two such bases differ by an element of ∏_{k=0}^n O(k+1) acting blockwise. On the nondegenerate class, LQ-factoring the off-diagonal blocks A_{k,x} = [L_k 0] degree by degree fixes this gauge up to signs and returns the pattern representative of (a)–(c) (induction on the leading forms). Hence, locally, ℬ_n is a product of 𝒫_n with an orbit of G = ∏ O(k+1); the stabiliser of a pair is exactly Z = {±I}: a block-orthogonal U preserves the one-dimensional degree-0 block, so Ue_1 = εe_1 with ε = ±1; if U stabilises both matrices it commutes with every polynomial in them, and cyclicity of e_1 (part (a)) gives U = εI [PR preparation, audit-03 support T3]. Z is central and the same for every pair, so G/{±I} acts freely and ℬ_n has dimension dim 𝒫_n + dim G = 3N − 1 + Σ_k k(k+1)/2 = 3N − 1 + C(n+2, 3). [response-02, audit-02 B4.3: earlier wording "a principal bundle over 𝒫_n/{signs} with fibre ∏ O(k+1)"; −I acts trivially, so the free action is that of the quotient by the finite stabiliser; the dimension is unchanged.]

## Scope

Exact arithmetic, real symmetric pairs, the generalized-Hessenberg pattern of a fixed graded order, nonzero (respectively positive) pivots. It says nothing about computed (nearly commuting) sections, about pairs with zero pivots, or about the dimension of the commutant of H_x inside the pattern of H_y (random instances give span{I, H_x, H_y}; the universal claim is refuted by PD-N?programme-ideas-claude-04, exact Padua n = 2, dimension 6).

## Open items

Related open target: genericity of the three-dimensional pattern commutant, `../OPEN_TARGETS.md` B5.

None for the statement. Not claimed: any stability statement for recovering the pair from the top-layer chart (the M2 record's "seed for (b)"), which remains a MEASURED observation in IDEA?programme-ideas-claude-08.

## History

- 2026-11-01, M2 adversarial agent (claude-fable-5-1, max), `checks/adversarial-M2.md` (ii)(1)–(2): proof steps (a)–(g) written; the commutant observation of (ii)(2) was placed in the same `report.md` row under a P label (`614709d`).
- 2026-11-01, response-01 (claude-opus-5-5, orchestrator/developer, effort not exposed), this file: statement and hypotheses made explicit; the commutant clause split off and relabelled MEASURED on random instances (audit-01 A3); overlap with `PD-T?bivariate-lanczos-claude-304`(b) recorded by pinned reference. Original combined wording preserved at `614709d:topics/programme-ideas-20261031/report.md` line 41.
