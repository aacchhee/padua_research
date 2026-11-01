# xu-tams-1994-blockjacobi — Y. Xu, Block Jacobi matrices and zeros of multivariate orthogonal polynomials, Trans. Amer. Math. Soc. 342(2) (1994) 855-866 (ref. [22] of xu-siam-1994)

- DOI / URL / supplied location: https://www.ams.org/journals/tran/1994-342-02/S0002-9947-1994-1258289-7/S0002-9947-1994-1258289-7.pdf (AMS PDF read via tool digest 2026-10-31); doi:10.1090/S0002-9947-1994-1258289-7
- Access and reading date: 2026-10-31
- Reading coverage: paper via a single tool digest focused on the zero/commutativity theorems; numbering and statements NOT cross-checked (see the doubt noted in the statement); proofs not read. PR-preparation (2026-11-01): the L3 prior-art review (2026-10-31) digested the same AMS PDF again (Thms 3.2, 3.4, 4.2; §2 Favard item 2°) and reports a Favard-type statement in this paper, which conflicts with the note below.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; online resolution pass). PR-preparation additions (2026-11-01): taken from the L3 prior-art review 2026-10-31 (Claude Opus 5.5, effort high; reading through WebFetch digests) by the Claude literature developer (Sonnet 5.5, effort high); the source was not re-read by the consolidator.
- Named gaps requiring future re-reading: Whole paper against page images: exact numbering of Theorems 3.1-3.5 and condition (3.1); the definition of sigma_n. PR-preparation: Where the multivariate Favard theorem and its measure version (Thm 4.2) are located: this paper (L3 review) or xu-tams-1994-operator / SIAM 1993 (note below) — UNRESOLVED.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c.

## Extracted published statements

### LIT-240 (LIT?bivariate-lanczos-claude-236) — Joint eigenvalues of truncated block Jacobi matrices = common zeros; N distinct zeros iff commutativity

- Verification: **AMS PDF read via tool digest only; theorem numbers below are as digested and the digest's Theorem 3.1 ('zeros distinct and simple') looks like a mis-numbering of a later corollary (Xu's survey puts that statement among the consequences of the joint-eigenvalue theorem), so treat numbering with caution. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Y. Xu, Block Jacobi matrices and zeros of multivariate orthogonal polynomials, Trans. Amer. Math. Soc. 342(2) (1994) 855-866. Theorem 3.2 (p. 858): lambda is a common zero of P_n if and only if it is a joint eigenvalue of the truncated block Jacobi matrices T_{n,i} (with joint eigenvector (P_0(lambda), ..., P_{n-1}(lambda))^T). Corollary 3.3 (p. 859): P_n has at most N = dim Pi_{n-1}^d distinct common zeros, all real. Theorem 3.4 (pp. 859-860): P_n has exactly N distinct common zeros if and only if the coefficient matrices satisfy the commutativity condition (3.1) for all i, j; the proof argues that N distinct zeros need N independent joint eigenvectors, hence simultaneous diagonalizability, hence commuting truncated matrices. Theorem 3.5 (p. 860): in general P_n has at most N - sigma_n distinct zeros, sigma_n a rank quantity built from the commutator of the coefficient matrices; joint eigenvectors lie in the kernel of the commutators. Mysovskikh's theorem (d = 2) is cited: a cubature of degree 2n-1 with N nodes exists iff P_n has N distinct real common zeros; since (3.1) generally fails, the node-count lower bound is usually not attained, and Moller's improved bound involves the same sigma_n.
- Hypotheses and notation: Orthonormal polynomial vectors P_n; truncated block Jacobi matrices T_{n,i}.
- Page / theorem / equation: Theorems 3.2, 3.4, 3.5 and Corollary 3.3, pp. 858-860 (digest).
- Reading evidence and limitations: Digest only. Necessity of commutativity is established only for the case of N distinct zeros (Theorem 3.4); the general case goes through the commutator rank (Theorem 3.5). Consistent with xu-siam-1994 statements 144-147 (cited [22] for 'joint eigenvalues are the zeros').  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: the exact-arithmetic mechanism that links the commutator of the truncated sections to the existence of a Gauss-type node set: no commutation, fewer distinct common zeros (quantified by sigma_n).

### LIT-292 (LIT?bivariate-lanczos-claude-449) — §2 item 2° (Favard-type) and Thm 4.2 (measure version with boundedness), as digested by the L3 reviewer

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: As digested by the L3 reviewer from the AMS PDF of Trans. AMS 342 (1994) 855–866: §2 item 2° contains a Favard-type statement (a three-term relation with the rank condition gives a square-positive functional, with commuting conditions (2.5)–(2.7)), and Thm 4.2 is a measure version with boundedness; Thms 3.2 and 3.4 agree with statement 236. Infinite sequences only.
- Hypotheses and notation: Orthonormal polynomial vectors; exact hypotheses not extracted.
- Page / theorem / equation: §2 item 2°; Thm 4.2; Thms 3.2, 3.4 (as digested).
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source. CONFLICT: the online-pass note below says the Favard theorem and rank condition are in the other Trans. AMS paper (xu-tams-1994-operator) and in SIAM J. Math. Anal. 24 (1993); the L3 reviewer's digest places a Favard statement in §2 of this paper. UNRESOLVED; the numbering is as digested.
- Relation to campaign claims (no inherited proof status): Weaker than the truncated Favard correspondence PD-T?bivariate-lanczos-claude-301 (infinite, no truncation, no count); the commuting-conditions side is the mechanism behind PD-N?bivariate-lanczos-claude-301.

## Search and attribution notes

Online resolution pass 2026-10-31: this is the block-Jacobi paper the plan means by 'Xu 1994 block Jacobi commutativity conditions' for the joint-eigenvalue and commutativity theory; the Favard theorem and the rank condition are in the other Trans. AMS paper (xu-tams-1994-operator) and in SIAM J. Math. Anal. 24 (1993). The summarizer's Theorem 3.1 ('distinct and simple zeros') is not recorded because it looks mis-numbered. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

PR-preparation consolidation 2026-11-01 (audit-01 protocol finding P2): the additions marked 'PR-preparation' above come from the L3 prior-art review 2026-10-31 (topics/bivariate-lanczos-20261031/reviews/), which read the source through WebFetch digests and make no novelty claim; the consolidator did not re-read the source. Any web check made at consolidation is logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: record created in the online resolution pass (statement 236).

2026-11-01 (PR-preparation consolidation, audit-01 protocol finding P2): second digest by the L3 prior-art review recorded as statement 449; location of the Favard theorem in conflict with the online-pass note, not resolved.
