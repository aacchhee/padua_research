# Addendum 2026-11-03 — xu-tams-1994-blockjacobi (Y. Xu, Block Jacobi matrices and zeros of multivariate orthogonal polynomials, Trans. Amer. Math. Soc. 342(2) (1994) 855–866)

- DOI [10.1090/S0002-9947-1994-1258289-7](https://doi.org/10.1090/S0002-9947-1994-1258289-7). AC-supplied PDF `Downloads\padua\papers\S0002-9947-1994-1258289-7.pdf` (12 pp.), read by Claude (claude-opus-5-5, high) with pdftotext on 2026-11-03.
- Coverage: §3 complete (Thms 3.1–3.5, pp. 857–861); §4 headings. Upgrades LIT-240 from digest to primary reading.
- Statements, paraphrased, with journal pages (journal page = PDF page + 854):
  - Thm 3.2 (pp. 858–859): λ is a common zero of P_n iff λ is a joint eigenvalue, with a joint eigenvector, of the truncated block Jacobi matrices T_{n,i}. The joint eigenvector is (P_0(λ), …, P_{n−1}(λ))ᵀ. T_{n,i} has size dim Π_{n−1}.
  - Cor. 3.3: at most dim Π_{n−1} zeros.
  - Thm 3.4 (p. 859): P_n has dim Π_{n−1} distinct zeros iff A_{n−1,i}A_{n−1,j}ᵀ = A_{n−1,j}A_{n−1,i}ᵀ for all i, j.
    - The proof says this is equivalent to the T_{n,i} commuting. Through the commuting conditions (2.5)–(2.7), the only obstruction to commuting is the last-block term.
    - For d = 2 this is credited to Mysovskikh; the paper connects it with Gaussian cubature, Möller's work and Thm 3.5 (p. 860).
- Relation to PD-T057(a): for sections of a FULL orthonormal sequence, a commutator of truncated block Jacobi matrices supported only in the last diagonal block is implicit in the proof of Thm 3.4. Our statement is for a functional given only on Π_{2n+1}, with blocks 0…n and the last block free, which is slightly more general. The commutator computation is the same. Verdict for (a): IMPLIES PART, with the translation T_{n,i} ↔ our sections with n−1 in place of n. The converse (b), the words formula and (c) are not in this paper.
