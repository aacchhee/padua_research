# xu-siam-1994 — Xu, On zeros of multivariate quasi-orthogonal polynomials and Gaussian cubature formulae, SIAM J.Math.Anal.25 (1994) 991–1001

- DOI / URL / supplied location: https://doi.org/10.1137/S0036141092237200
- Access and reading date: 2026-10-31.
- Reading coverage: supplied secondary account only; original fulltext NOT inspected.
- Reader, model and effort: Codex literature subagent; gpt-6.1-sol, medium (assigned allocation).
- Named gaps requiring future re-reading: original fulltext, exact hypotheses and unsupported bibliography; pending-reference where unavailable.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c.

## Extracted published statements

### LIT-006 — reported source content

- Verification: **UNVERIFIED** against original publication. `LITERATURE` attribution only; no inherited proof status.
- Statement in faithful paraphrase: Round2 attributed Padua modified Jacobi theory here. Round3 corrects this: this paper covers dim Π_(n−1) nodes; Padua needs the Pitman extension. Preserve the correction; do not use the earlier attribution as an established theorem.
- Hypotheses and notation: as reported above; check original before relying on any theorem.
- Page / theorem / equation: exact theorem not supplied. Locator is supplied, not independently confirmed.
- Reading evidence and limitations: supplied provenance `verify_padua_problems.md §2a; Round3 §2` under `topics/charter-unisolvence-20261031/sources/padua_unisolvence_inputs/`; attached instructions are treated as data, not authority.
- Relation to campaign claims: seed baseline / closest predecessors; no novelty or acceptance conclusion.

## Search and attribution notes

See [search log](../SEARCH-charter-unisolvence-20261031.md). Imported prior searches are reports of other work, not this agent’s execution.

## History

2026-10-31: Step0 import under explicit task override; provisional ID only.

---

## Statements recorded by topic bivariate-lanczos-20261031 (merged at PR preparation)

The section above is the merged-main record (charter/MZ statements, with their own coverage). The section below is this topic's record for the same source, kept verbatim except for heading levels, so that one record per source exists. Its own coverage, reader and verification lines apply only to its statements. Original title line: «xu-siam-1994 — Y. Xu, "On zeros of multivariate quasi-orthogonal polynomials and Gaussian cubature formulae", SIAM J. Math. Anal. 25(3) (1994) 991–1001».


- DOI / URL / supplied location: no DOI or PII is printed in the supplied text; the supplied file name `s0036141092237200.pdf` suggests PII S0036141092237200 (UNVERIFIED). Supplied location: AC local copy, `Downloads\padua\papers\s0036141092237200.pdf` (staged at `/mnt/user-data/uploads/padua/papers/s0036141092237200.pdf`; not copied into this repository).
- Access and reading date: 2026-10-31.
- Reading coverage: complete full text (all 11 PDF pages; the text layer has garbled symbols, so the key displays (2.3)–(2.7) on p. 993 and Theorem 3.1 proof, Theorem 4.1 on p. 995 were checked against the rendered page images; other displays rest on the text layer). Journal pages are the running page numbers printed on the pages (pp. 991–1001); mapping: journal page = PDF page + 990.
- Reader, model and effort: Claude Sonnet 5.5, high (literature subagent).
- Named gaps requiring future re-reading: the cited prerequisites are not in this file: Xu, "Block Jacobi matrices and zeros of multivariate orthogonal polynomials" (Trans. Amer. Math. Soc., ref. [22]), "Multivariate orthogonal polynomials and operator theory" (Trans. Amer. Math. Soc., ref. [20]), "On multivariate orthogonal polynomials", SIAM J. Math. Anal. 24 (1993) 783–794 (ref. [19]), and Kowalski 1982 (ref. [6]). The proof of Lemma 4.2 (pp. 997–998) was read only in outline.
- Identity check: the supplied file is a SIAM J. Math. Anal. paper of May 1994 on quasi-orthogonal polynomials and Gaussian cubature of degree 2n−2, not the block-Jacobi paper (which is ref. [22], Trans. AMS). The key `xu-siam-1994` is correct as year and journal. The block Jacobi matrices appear here, but the commuting conditions are recalled in Section 2 and the Favard-type theorem is only cited.

### Extracted published statements

### LIT-184 (LIT?bivariate-lanczos-claude-142) — Setting: orthonormal polynomial vectors and the three-term relation; Gaussian cubature (Mysovskikh)

- Statement in faithful paraphrase: For a weight function W on R^d (assumed nonnegative with infinite support and normalized), the orthonormal polynomials of degree n are arranged in a vector P_n of length r_n = dim Π_n^d − dim Π_{n−1}^d (lexicographic order), with ∫ P_n P_nᵀ W = I. They satisfy the three-term relation x_i P_n = A_{n,i} P_{n+1} + B_{n,i} P_n + A_{n−1,i}ᵀ P_{n−1}, 1 ≤ i ≤ d (eq. (2.2)), with A_{n,i} of size r_n × r_{n+1} and B_{n,i} of size r_n × r_n. A minimal cubature formula of degree m with N nodes has N ≥ dim Π_{⌊m/2⌋}^d in general; formulae attaining this bound are Gaussian cubature formulae (degree 2n−1 or 2n−2). Mysovskikh's characterization: a Gaussian cubature formula of degree 2n−1 exists iff the degree-n orthogonal polynomials have dim Π_{n−1} common zeros. Gaussian cubature of degree 2n−1 does not always exist (Mysovskikh; Möller lower bounds), but for W = (1−x²)^{1/2}(1−y²)^{1/2} on [−1,1]² a Gaussian cubature of degree 2n−2 exists while degree 2n−1 does not.
- Hypotheses and notation: continuous weight W on R^d; exact arithmetic; d ≥ 1.
- Page / theorem / equation: eq. (1.2), pp. 991–992; (2.1)–(2.2), p. 992.
- Reading evidence and limitations: The facts in the introduction are literature citations in this paper ([8], [9], [10], [11], [12], [13]); they were not checked there.
- Relation to campaign claims (no inherited proof status): Provides the block structure A_{n,i}, B_{n,i} with r_n = n+1 for d = 2 that matches the campaign's graded blocks Q_k; for discrete weights (nodes) the paper gives no separate statement.

### LIT-185 (LIT?bivariate-lanczos-claude-143) — Rank conditions and a Favard-type statement (cited, not proved)

- Statement in faithful paraphrase: Rank conditions: for n ≥ 0, rank A_{n,i} = r_n for 1 ≤ i ≤ d, and the stacked matrix A_n = (A_{n,1}ᵀ | … | A_{n,d}ᵀ)ᵀ has rank r_{n+1} (eq. (2.3)). "Actually", if {P_n} is any sequence of polynomial vectors satisfying (2.2) and (2.3), then {P_n} is orthonormal with respect to a square-positive linear functional: a Favard theorem, cited to [6], [19], [20] (not proved here). (2.3) implies matrices D_{k,i} with Σ_i D_{k,i} A_{k,i} = I (eq. (2.4)); D_n is a generalized inverse of A_n.
- Hypotheses and notation: P_{−1} = 0, P_0 = 1; the commuting conditions below are also needed by the cited Favard theorem (this paper states the Favard theorem for sequences satisfying (2.2) and (2.3) and mentions the commuting conditions separately).
- Page / theorem / equation: eq. (2.3), eq. (2.4) and the Favard sentence, p. 993 (checked against the page image).
- Reading evidence and limitations: As printed, the statement of the Favard theorem on p. 993 lists only the three-term relation and the rank condition as hypotheses, while the following paragraph lists the commuting conditions as consequences of orthogonality; whether the commuting conditions are also hypotheses in [19], [20] is UNVERIFIED (not in this file).
- Relation to campaign claims (no inherited proof status): The converse direction (sections satisfying structure plus commutativity define a measure) is what L3 asks for in a perturbed, discrete setting; here it is only an infinite-sequence, cited statement and there is no perturbation or discrete-support content.

### LIT-186 (LIT?bivariate-lanczos-claude-144) — Commuting conditions (2.5)–(2.7) on the block coefficients

- Statement in faithful paraphrase: Orthogonality also implies that for n ≥ 0 and 1 ≤ i, j ≤ d: A_{n,i}A_{n+1,j} = A_{n,j}A_{n+1,i} (2.5); A_{n,i}B_{n+1,j} + B_{n,i}A_{n,j} = B_{n,j}A_{n,i} + A_{n,j}B_{n+1,i} (2.6); A_{n−1,i}ᵀA_{n−1,j} + B_{n,i}B_{n,j} + A_{n,i}A_{n,j}ᵀ = A_{n−1,j}ᵀA_{n−1,i} + B_{n,j}B_{n,i} + A_{n,j}A_{n,i}ᵀ (2.7). The authors describe these as the conditions that make the linear operators associated with {P_n} "formally commuting"; the spectral theorem for commuting self-adjoint operators has been used (in [20]) to study the integral representation of the linear functional in the Favard theorem.
- Hypotheses and notation: block entries as in (2.2); B_{n,i} symmetric.
- Page / theorem / equation: eqs. (2.5)–(2.7), p. 993 (checked against the page image).
- Reading evidence and limitations: Stated as consequences of orthogonality with no proof in this paper (cited from [19]).
- Relation to campaign claims (no inherited proof status): These are the "block Jacobi commutativity conditions" of the campaign's L3 (interior commutativity conditions); the 2.7 condition is the one coupling the block symmetric parts and the one most likely to be violated by computed sections. They are written for the infinite coefficient sequence; their truncated form is given in statement 147.

### LIT-187 (LIT?bivariate-lanczos-claude-145) — Block Jacobi matrices and truncated block Jacobi matrices

- Statement in faithful paraphrase: The (infinite) block Jacobi matrices T_i, 1 ≤ i ≤ d, are block tridiagonal with diagonal blocks B_{n,i} and off-diagonal blocks A_{n,i}, A_{n,i}ᵀ; they define operators on ℓ² (for d = 1 the classical Jacobi matrix). The truncated matrices T_{n,i} delete block rows and columns with index ≥ n; the joint eigenvalues of T_{n−1,i}, 1 ≤ i ≤ d, are the zeros of P_n (proved in [22]; well known for d = 1). For a quasi-orthogonal polynomial vector Q_n = P_n + Γ P_{n−1} (Γ of size r_n × r_{n−1}, eq. (3.1)), S_{n−1,i} is T_{n−1,i} with the last diagonal block B_{n−1,i} replaced by B_{n−1,i} − A_{n−1,i}Γ (and the last off-diagonal blocks unchanged), of size dim Π_{n−1}; S_n denotes the tuple (S_{n,1}, …, S_{n,d}). A joint eigenvalue of S_n is a vector Λ with S_{n,i}x = Λ_i x for all i.
- Hypotheses and notation: sizes: S_{n−1,i} has dim Π_{n−1} rows.
- Page / theorem / equation: p. 994 (definitions before Theorem 3.1).
- Reading evidence and limitations: The matrix display is garbled in the text layer; the replacement of the last block is read from the proof of Theorem 3.1 (last equation on p. 994–995, checked against the image of p. 995).
- Relation to campaign claims (no inherited proof status): The truncated block Jacobi matrices T_{n−1,i} are the exact-arithmetic counterparts of the campaign's block-tridiagonal H_x, H_y restricted to degree < n; the modified last block S is the "closure" that makes zeros appear and is the analogue of a square (M = N_n) cubature case.

### LIT-188 (LIT?bivariate-lanczos-claude-146) — Theorem 3.1 (zeros of quasi-orthogonal polynomials as joint eigenvalues)

- Statement in faithful paraphrase: Let Q_n = P_n + Γ P_{n−1} and S_{n,i} the corresponding truncated block Jacobi matrices. Then Λ = (Λ_1, …, Λ_d) is a zero of Q_n if and only if Λ is a joint eigenvalue of S_{n−1}, and the joint eigenvector is (P_0(Λ)ᵀ, …, P_{n−1}(Λ)ᵀ)ᵀ. For d = 1 and Γ = β ≠ 0 (scalar) the paper adds the formula q_n = p_n + βp_{n−1} = (a_0 … a_{n−1})⁻¹ det(xI − S_{n−1}), said to seem unnoticed in the literature. S_{n,i} is almost symmetric (only the last block questionable) and symmetric if Q_n has the maximal number of zeros (Theorem 4.1).
- Hypotheses and notation: real orthonormal P_n for a weight W; Γ arbitrary real; "zero of Q_n" means common zero of all components.
- Page / theorem / equation: Theorem 3.1, p. 994; proof pp. 994–995 (uses the three-term relation, (2.4) and induction); Γ = 0 case proved in [22].
- Reading evidence and limitations: Proof read and checked against the image; the converse direction constructs the polynomial values from the eigenvector by the same recurrence (not re-derived).
- Relation to campaign claims (no inherited proof status): An exact-arithmetic eigenvalue characterization; no perturbation statement about how joint eigenpairs of approximately commuting sections behave.

### LIT-189 (LIT?bivariate-lanczos-claude-147) — Theorem 4.1 (necessary and sufficient conditions for the maximal number of zeros)

- Statement in faithful paraphrase: The polynomial vector Q_n has N = dim Π_{n−1} distinct zeros if and only if for 1 ≤ i ≤ d: A_{n−1,i} Γ = Γᵀ A_{n−1,i}ᵀ (4.1), and for 1 ≤ i, j ≤ d the quadratic matrix equation (4.2) holds: Γᵀ(A_{n−1,i}ᵀA_{n−1,j} − A_{n−1,j}ᵀA_{n−1,i})Γ − (A_{n−1,i}A_{n−1,j}ᵀ − A_{n−1,j}A_{n−1,i}ᵀ) = (B_{n−1,i}A_{n−1,j} − B_{n−1,j}A_{n−1,i})Γ − [(B_{n−1,i}A_{n−1,j} − B_{n−1,j}A_{n−1,i})Γ]ᵀ. Proof idea (pp. 995–996): Q_n has N distinct zeros iff the S_{n,i} are simultaneously diagonalizable, iff they commute and are diagonalizable; if (4.1) holds the S_{n,i} are symmetric hence diagonalizable, and the commutation relations S_{n,i}S_{n,j} = S_{n,j}S_{n,i} reduce, using (2.5)–(2.7), to (4.2) and (4.6), with (4.6) equivalent to (4.1) via the leading coefficient matrix (Lemma 4.2). For d = 2 the theorem was proved by Schmid ([12], [15]; stated there as a Hankel-type condition on H_n, with monic orthogonal polynomials); for Γ = 0 it reduces to Mysovskikh's condition [10], as the paper notes.
- Hypotheses and notation: exact arithmetic, real coefficient matrices; N distinct real zeros means N distinct common zeros.
- Page / theorem / equation: Theorem 4.1, p. 995 (displays (4.1)–(4.2) checked against the page image); proof pp. 995–996; Lemma 4.2 p. 997; remarks on d = 2 and Γ = 0, p. 998.
- Reading evidence and limitations: The proof was read; Lemma 4.2 (that (4.7) forces H_n to have the Hankel-type form (h_{α+β})) was read in outline only.
- Relation to campaign claims (no inherited proof status): This is the exact commutativity-versus-zeros equivalence closest to the campaign's square case M = N_n (Padua-like node counts dim Π_{n−1}): commuting modified sections S_{n,i} correspond to N distinct nodes. It is an exact statement; the paper says nothing on perturbations, on discrete measures other than as cubature nodes, or on rounding.

### LIT-190 (LIT?bivariate-lanczos-claude-148) — Lemma 4.2, Corollary 4.3 and Theorem 4.4 (structure and simplicity of zeros)

- Statement in faithful paraphrase: Lemma 4.2: a matrix H_n satisfies (4.7) iff it has the form H_n = (h_{α+β}), |α| = n, |β| = n−1 (a multi-index Hankel property), rows and columns in lexicographic order; this gives a linear functional with h_γ = ℓ*(x^γ). Corollary 4.3: if Q_n has dim Π_{n−1} distinct zeros, the S_{n,i} are symmetric. Theorem 4.4: if Q_n has dim Π_{n−1} zeros, all zeros are real, distinct and simple, and Q_n and P_{n−1} have no common zeros; proof via the Christoffel–Darboux formula, giving P_{n−1}(Λ)ᵀA_{n−1,i}∂_iQ_n(Λ) = Σ_{k<n} P_kᵀ(Λ)P_k(Λ) > 0.
- Hypotheses and notation: exact arithmetic; simple zero means at least one partial derivative of Q_n is nonzero there.
- Page / theorem / equation: Lemma 4.2, pp. 997–998; Corollary 4.3 and Theorem 4.4, p. 998.
- Reading evidence and limitations: Lemma 4.2's proof read in outline; Theorem 4.4's proof read.
- Relation to campaign claims (no inherited proof status): The positivity argument (Christoffel–Darboux) is the source of simplicity and realness; real eigenvalues of symmetric S_{n,i} also underlie the real-nodes setting.

### LIT-191 (LIT?bivariate-lanczos-claude-149) — Theorems 5.1 and 5.2 (Gaussian cubature of degree 2n−2; Lagrange interpolation)

- Statement in faithful paraphrase: Theorem 5.1: for a given weight W, a Gaussian cubature of degree 2n−2 exists if and only if there is a matrix Γ satisfying (4.1) and (4.2) (earlier: iff the quasi-orthogonal polynomials have dim Π_{n−1} distinct real common zeros, due to Morrow–Patterson and Schmid). Theorem 5.2: if Γ satisfies (4.1)–(4.2), the polynomial L_n(f; x) = Σ_k f(x_k) λ_k K_n(x, x_k) (K_n the reproducing kernel, λ_k the cubature weights) is the unique solution of Lagrange interpolation in Π_{n−1} at the N = dim Π_{n−1} zeros; (4.1) is vital in the proof, which is "the same in spirit" as for d = 2 in [21] (details of the modification not given).
- Hypotheses and notation: exact arithmetic; W a nonnegative weight function.
- Page / theorem / equation: Theorem 5.1, p. 998; Theorem 5.2, p. 1000.
- Reading evidence and limitations: Theorem 5.1 is an immediate consequence of Theorem 4.1 and cited prior work; Theorem 5.2's proof is only sketched.
- Relation to campaign claims (no inherited proof status): Links the commutativity condition to cubature existence: Gaussian cubature of degree 2n−2 with dim Π_{n−1} nodes ⇔ solvable (Γ). The statement concerns existence of such nodes for a given weight function, not whether a given node set carries a positive cubature. The paper does not mention Padua points; any identification with Padua nodes or their cubature is outside the paper (UNVERIFIED here).

### LIT-192 (LIT?bivariate-lanczos-claude-150) — Example (d = 3, n = 2) and the authors' expectation of non-existence

- Statement in faithful paraphrase: For the product Chebyshev weight of the second kind in three variables, with a specific 6 × 3 matrix Γ (displayed on p. 999), all conditions of Theorem 4.1 are verified for n = 2, giving 4 = dim Π_1^3 zeros, namely (1/2,1/2,−1/2), (1/2,−1/2,1/2), (−1/2,1/2,1/2), (−1/2,−1/2,−1/2), which give a Gaussian cubature of degree 2 on R³. The authors could not find a suitable Γ for d = 3, n = 3 and believe that a result as simple as the d = 2 Morrow–Patterson result is not possible for d > 2, and that existence of Γ solving (4.1)–(4.2) "is mostly negative", even for the product Chebyshev weight.
- Hypotheses and notation: product Chebyshev weight of the second kind; d = 3.
- Page / theorem / equation: pp. 999–1000.
- Reading evidence and limitations: Example calculations were not re-derived; the nonexistence statement is a belief ("we believe"), not a theorem.
- Relation to campaign claims (no inherited proof status): For d = 2, Γ solving (4.1)–(4.2) is known to exist for the Chebyshev second-kind weight (cited [9], [14]); this is a hint that existence in the square case is delicate, relevant to the "obstruction family" alternative in L3-Q1, but the paper offers no obstruction construction.

### Search and attribution notes

- Method: pdftotext -layout output read page by page; page headers used for journal pages; key displays on pp. 993 and 995 checked against rendered images.
- The paper contains no statement about discrete weights/nodes explicitly, rounding, Lanczos methods, Ritz values, numerical algorithms or perturbation of block Jacobi matrices (the only numerical remark is that the determinant formula for d = 1 is "very useful both numerically and theoretically", p. 995).
- References for the orchestrator to chase on block Jacobi matrices and commutativity: [22] Xu, "Block Jacobi matrices and zeros of multivariate orthogonal polynomials", Trans. AMS (to appear in 1994); [20] Xu, "Multivariate orthogonal polynomials and operator theory", Trans. AMS; [19] Xu, SIAM J. Math. Anal. 24 (1993) 783–794; [6] Kowalski (1982) (Favard); [12], [15] Schmid; [9] Morrow–Patterson (1978); [21] Xu, "Gaussian cubature and bivariate polynomial interpolation", Math. Comp. 59 (1992) 547–555. None concerns finite-precision analysis.

### History

- 2026-10-31: record created from a complete reading of the supplied PDF (Claude Sonnet 5.5, high).
