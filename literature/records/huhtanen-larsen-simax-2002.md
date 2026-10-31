# huhtanen-larsen-simax-2002 — M. Huhtanen and R. M. Larsen, "Exclusion and inclusion regions for the eigenvalues of a normal matrix", SIAM J. Matrix Anal. Appl. 23(4) (2002) 1070–1091

- DOI / URL / supplied location: PII S0895479801384561 printed on the first page (so DOI 10.1137/S0895479801384561; the DOI itself is not printed, UNVERIFIED). Supplied location: AC local copy, `Downloads\padua\papers\s0895479801384561.pdf` (staged at `/mnt/user-data/uploads/padua/papers/s0895479801384561.pdf`; not copied into this repository).
- Access and reading date: 2026-10-31.
- Reading coverage: complete full text (all 22 PDF pages read from pdftotext -layout output; Sections 5–6 on exclusion and inclusion regions were read but yielded no extracted statement; PDF pages 14 and 19 were also checked against the rendered page image). Journal pages are the running page numbers printed on the pages (pp. 1070–1091); mapping: journal page = PDF page + 1069.
- Reader, model and effort: Claude Sonnet 5.5, high (literature subagent).
- Named gaps requiring future re-reading: ref. [18] (Huhtanen, Math. Comp., polyanalytic polynomials), which the paper cites for Proposition 3.1, Theorem 3.4 and Theorem 6.1; ref. [10] (Elsner–Ikramov 1997) for the canonical form; ref. [19] (Huhtanen–Nevanlinna 2000) for "nearly normal". None of these were read.

## Extracted published statements

### LIT?bivariate-lanczos-claude-114 — Setting: the same recurrence in the polyanalytic (N, N*) form

- Statement in faithful paraphrase: The paper treats a normal matrix N ∈ C^{n×n}, with multiplications by N and N* identified with z and z̄; it builds an orthonormal basis of C^n by multiplying already computed vectors by N* (the first vector of each cycle) or by N (the remaining vectors) and orthogonalizing against a window (table (3.2) and Algorithm 1). The k-th cycle has k+1 vectors; after k cycles there are (k+1)(k+2)/2 vectors. The generated polynomials are polyanalytic polynomials p(z) = Σ h_j(z) z̄^j; the leading term of p_{s,k−s} is z^s z̄^{k−s}.
- Hypotheses and notation: N normal; starting vector q̂_0 ∈ C^n of unit length; inner products are complex. In the real-symmetric commuting case N = H + iK the Hermitian parts H = (N+N*)/2 and K = (N−N*)/(2i) commute, and the procedure is the HL BIT algorithm in complex form (this identification is mine, not an author statement).
- Page / theorem / equation: Definition 2.1 and the order on polyanalytic monomials, pp. 1071–1073; table (2.8) p. 1076; table (3.2) and Algorithm 1, pp. 1079–1080.
- Reading evidence and limitations: Read in full. Algorithm 1 in this paper orthogonalizes the first vector against indices k_0 … k_2−1 (2k−1 vectors) and each N-product against indices l−k+1 … l+k (2k vectors).
- Relation to campaign claims (no inherited proof status): This is the source of the loss-of-orthogonality remark (statement 119) and of Ritz values of a single complex section; the objects there are sections of N and N*, not of real X and Y separately.

### LIT?bivariate-lanczos-claude-115 — Exact-arithmetic properties of the process (Proposition 3.1, Corollary 3.2, Proposition 3.3, Theorem 3.4, Corollary 3.6)

- Statement in faithful paraphrase: Proposition 3.1: span{q̂_0 … q̂_{(k+1)(k+2)/2−1}} = {p(N)q̂_0 : p polyanalytic of degree ≤ k}. Corollary 3.2: for generic q̂_0 and no nonzero element of PP_k vanishing on σ(N), these vectors are linearly independent. Proposition 3.3: the number of nonzero vectors generated equals dim K_n(N; q̂_0). Theorem 3.4: q̂_{k(k+1)/2+s} = p_{s,k−s}(N)q̂_0 with leading term c·z^s z̄^{k−s} (c allowed to be zero). Corollary 3.6: if the minimal polyanalytic polynomial has leading term z^j z̄^l, then for k ≥ j+l the vectors q̂_{k(k+1)/2+s} vanish for j ≤ s ≤ k−l. Zero vectors are generally not saved and are discarded from the recurrence.
- Hypotheses and notation: N normal; "generic" means supported on every spectral subspace; exact arithmetic; PP_k polyanalytic polynomials of degree ≤ k.
- Page / theorem / equation: Proposition 3.1, Corollary 3.2, Proposition 3.3, Theorem 3.4, pp. 1080; Corollary 3.5, Corollary 3.6, p. 1080–1081; discarding of zero vectors, p. 1082.
- Reading evidence and limitations: Proofs are by reference to [18] (not read). Not independently checked.
- Relation to campaign claims (no inherited proof status): Exact-arithmetic analogues of statements 102–104; useful only to cross-check hypotheses.

### LIT?bivariate-lanczos-claude-116 — Theorem 3.7 (recurrence length 2k) and storage bound

- Statement in faithful paraphrase: Let q̂_0 be generic for N ∈ N and assume no nonzero element of PP_k vanishes on σ(N). Then, to finish the k-th cycle, the length of the recurrence for computing q̂_{k(k+1)/2+s} is 2k for s = 0, …, k. The proof starts with (k−1)+k = 2k−1 stored vectors and shows that for the N-product producing q̂_{k(k+1)/2+s} the first s−1 vectors of cycle k−2 are already orthogonal, so 2k+1 vectors need to be saved but orthogonalization is against 2k (the authors note one could reduce this to 2k−1 by a minor modification). With d = (k+1)(k+2)/2, the number of saved vectors is bounded by 2√(2d)+1 = √(8d)+1. The orthogonality of the next cycle to all but a small portion of the earlier vectors was noticed by Elsner and Ikramov [10] (eq. (3.10)).
- Hypotheses and notation: exact arithmetic; genericity as stated; N normal with N* = q(N) for a polynomial q.
- Page / theorem / equation: Theorem 3.7, p. 1081; proof, p. 1082; storage bound p. 1082; remark on [10] p. 1081.
- Reading evidence and limitations: The proof is given in outline (it uses (N q̂_a, q̂_b) = (q̂_a, N* q̂_b) and the leading-term property of Theorem 3.4); not re-derived. Compare HL BIT Theorem 2.3 (≤ 2k+1) in record `huhtanen-larsen-bit-2002`.
- Relation to campaign claims (no inherited proof status): Shows that the exact window length for this variant is 2k, not 2k+1, with a 2k−1 variant indicated; the campaign should state which variant (and which ordering) its window refers to.

### LIT?bivariate-lanczos-claude-117 — Canonical form of Elsner–Ikramov and Ritz values of the section of N

- Statement in faithful paraphrase: With the ordering (3.2), Q̂*NQ̂ has the sparsity pattern (4.1) (banded, "nearly symmetric": the j-th column has at most one more nonzero than the j-th row) when the start vector is generic and no nonzero p ∈ PP_k with (k+1)(k+2)/2 < n vanishes on σ(N). After k cycles, N[q̂_0 … q̂_{k(k+1)/2−1}] = [q̂_0 … q̂_{(k+1)(k+2)/2−1}] N_k with N_k ∈ C^{(k+1)(k+2)/2 × k(k+1)/2} collecting the inner products (eq. (4.2)). Removing the last k+1 rows of N_k gives a square matrix used to compute Ritz values; it is not normal in general but "nearly normal" in the sense of [19] (self-commutator of small rank). For Hermitian N the matrix is exactly the Hermitian Lanczos tridiagonal matrix. The authors say they do not know how the characteristic polynomial p_k of the square matrix is related to the polyanalytic polynomial P_{j,l} realizing the minimum (3.1) at the same step.
- Hypotheses and notation: exact arithmetic; N normal.
- Page / theorem / equation: (4.1) and (4.2), p. 1083 (checked against the page image); Section 4, pp. 1082–1083.
- Reading evidence and limitations: The nearly-normal claim relies on [19] (not read); no proof of the commutator rank is given in this paper.
- Relation to campaign claims (no inherited proof status): The campaign's sections H_x = QᵀXQ, H_y = QᵀYQ and Z = H_x + iH_y correspond to the square matrix of this statement only under my identification N = X+iY, N* = X−iY; the paper itself does not discuss the real pair separately. Source of "Ritz values of the section" for L1-Q1; the question whether single-section Ritz pairs suffice is not addressed.

### LIT?bivariate-lanczos-claude-118 — Finite-precision implementation: ORTH (MGS with one reorthogonalization)

- Statement in faithful paraphrase: The same ORTH procedure as in HL BIT (variant of Reichel–Gragg Algorithm 686; modified Gram–Schmidt, one reorthogonalization if the norm falls below 0.707 of the original, rank decision with tolerance 2 l u, "twice is enough" cited from Parlett p. 113) is used to decide whether a vector lies numerically in the span of the window, and Algorithm 1 is rewritten with ORTH; the first vector is orthogonalized against q̂_{k_0} … q̂_{k_2−1}, the N-products against q̂_{l−k+1} … q̂_{l+k}.
- Hypotheses and notation: floating-point arithmetic, unit round-off u; vector length l.
- Page / theorem / equation: Section 7.1, p. 1087 (ORTH), pp. 1087–1088 (Algorithm 1 using ORTH).
- Reading evidence and limitations: Read; the tolerance symbol is garbled in the extraction (read as 2 l u; UNVERIFIED). No error analysis.
- Relation to campaign claims (no inherited proof status): Defines the floating-point "HL" variant to be compared with CGS2 (plan L1/L2).

### LIT?bivariate-lanczos-claude-119 — Remark on loss of orthogonality and Ritz values (p. 1088)

- Statement in faithful paraphrase: The behaviour of Algorithm 1 in finite precision "seems to be similar" to that of the Lanczos algorithm: some loss of orthogonality occurs among vectors from different cycles after many steps. "As in the Hermitian Lanczos algorithm", this phenomenon "appears to be closely connected to the convergence of Ritz values associated with (4.2)", that is, with the square matrix of statement 117. "None of the examples below were affected by this effect."
- Hypotheses and notation: informal observation for Algorithm 1 in the (N, N*) form; the Ritz values are those of the square submatrix of N_k from (4.2) (a complex, non-normal matrix); no operator, norm or quantitative relation is specified.
- Page / theorem / equation: p. 1088 (Section 7.1, directly after Algorithm 1 using ORTH).
- Reading evidence and limitations: Correction to the reported locator: p. 1088 is confirmed, but the text is an observation ("seems", "appears"), not a stated conjecture; no numerical evidence for it is given anywhere in the paper (no orthogonality measurements are shown; Examples 11–14 were unaffected). The paper does not say whether the relevant Ritz values are those of the joint matrix N or of its Hermitian or skew parts separately; it refers to (4.2) only.
- Relation to campaign claims (no inherited proof status): This is the origin of plan.md L1-Q1's "joint Ritz pairs of Z = H_x + iH_y" formulation. The statement is a heuristic from the authors, not a theorem; it carries no proof status and no quantitative content for the kill test.

### LIT?bivariate-lanczos-claude-120 — Numerical examples relevant to storage and Ritz values (Examples 11–13)

- Statement in faithful paraphrase: Example 11: for a random diagonal normal N ∈ C^{300×300}, only ⌊√(8·300)⌋ ≤ 50 vectors need to be stored to compute the canonical form (4.1) (nonzero count 9776 in Figure 3), whereas Arnoldi with the same storage would produce a Hessenberg matrix only 1/6 × 1/6 of that size. Examples 12 and 13 (N of size 1000; storage for at most 30 vectors, giving matrices of size 30 for Arnoldi and 120 for Algorithm 1): Ritz values from Algorithm 1 are distributed more uniformly with respect to σ(N) than those from Arnoldi (pictured; no numbers are given). Example 14 treats exclusion regions.
- Hypotheses and notation: Matlab 5.3, IEEE double precision, Linux PC; start vector (1/√n)(1,…,1)ᵀ for Examples 12–14.
- Page / theorem / equation: Examples 11–13, pp. 1088–1089; Fig. 3 p. 1088 (checked against the image), Fig. 4 p. 1089.
- Reading evidence and limitations: Statements about Ritz-value quality are qualitative reports from figures; not independently checked.
- Relation to campaign claims (no inherited proof status): MEASURED-type source evidence in one unstructured setting (diagonal N, diagonal start vector with equal components); it contains no orthogonality diagnostics.

### LIT?bivariate-lanczos-claude-121 — Algebraic results on the polyanalytic process

- Statement in faithful paraphrase: Theorem 2.5: the minimal polyanalytic polynomial of a normal N has degree at most 2 deg(N) (cited as [18]). Lemma 2.11: the process (2.8) yields deg(N) orthonormal matrices. Proposition 2.12: if p with leading term z^j z̄^l annihilates N, then Q_{k(k+1)/2+s} = 0 for k ≥ j+l and j ≤ s ≤ k−l. Theorem 2.14: the common zero set of the irreducible annihilating polyanalytic polynomials generated by the process equals σ(N). Theorem 6.1 (cited as [18]): for N normal with n distinct eigenvalues and generic q̂_0, Algorithm 1 produces n polyanalytic polynomials orthogonal for the inner product (6.1), i.e. the discrete measure with masses |(q̂_0,q_j)|² at the eigenvalues.
- Hypotheses and notation: exact arithmetic; N normal; "generic" start vector.
- Page / theorem / equation: Theorem 2.5 p. 1073; Lemma 2.11 pp. 1076–1077; Proposition 2.12 p. 1077; Theorem 2.14 p. 1078; Theorem 6.1 p. 1085.
- Reading evidence and limitations: Proofs for Lemma 2.11 and Theorem 2.14 were read in outline; those for Theorem 2.5 and Theorem 6.1 depend on [18].
- Relation to campaign claims (no inherited proof status): Exact-arithmetic background only; no finite-precision content.

## Search and attribution notes

- Method: pdftotext -layout output (stripped of the wide left margin) read page by page; page headers used for journal pages; the sparsity-pattern page (p. 1083) and p. 1088 were checked against rendered images.
- Reported locator check: the reported "conjecture at p. 1088" is a remark in Section 7.1 on p. 1088 (statement 119); there is no item labelled conjecture in the paper (searched the whole text for "conjecture": none).
- This paper's variant has recurrence length 2k (Theorem 3.7), differing from the 2k+1 of HL BIT Theorem 2.3; the paper itself says it "squeezes" to 2k−1 by a minor modification.
- Section 5.2 and the rest of Sections 5–6 (exclusion regions via Bauer–Fike, inclusion regions of Householder type) do not concern finite-precision behaviour of the recurrence and were not extracted.
- References bearing on finite-precision analysis for multivariate Lanczos, for the orchestrator to chase: [8] Daniel–Gragg–Kaufman–Stewart (1976); [27] Reichel–Gragg (1990); [25] Parlett, The Symmetric Eigenvalue Problem (SIAM 1998), p. 113; [10] Elsner–Ikramov, LAA 254 (1997) 79–98 (condensed form for normal matrices); [19] Huhtanen–Nevanlinna, Numer. Math. 86 (2000) 257–281 (nearly normal matrices, small-rank self-commutator); [18] Huhtanen, Math. Comp. (polyanalytic); [21] Manteuffel–Starke, Numer. Math. 73 (1996) (Example 1 source).

## History

- 2026-10-31: record created from a complete reading of the supplied PDF (Claude Sonnet 5.5, high).
