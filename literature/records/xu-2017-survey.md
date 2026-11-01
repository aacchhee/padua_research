# xu-2017-survey — Y. Xu, Orthogonal polynomials of several variables, survey, arXiv:1701.02709 (Askey–Bateman project, vol. 2, ch. 2 per the Step 0 search log row 68)

- DOI / URL / supplied location: https://arxiv.org/abs/1701.02709
- Access and reading date: 2026-10-31 (read by the L1 prior-art reviewer); record written 2026-11-01 (PR-preparation consolidation).
- Reading coverage: WebFetch digest of the arXiv PDF, §2.2 (eq. (2.14), Thm 2.11). Another pass (Step 0 search-log row 68) digested Thms 2.7–2.18 of the same PDF and found the text of §6 absent. The original sources of the recursion (Xu 1993/1994; Dunkl–Xu 2014 §3.3) were not read.
- Reader, model and effort: Claude Opus 5.5, effort high (independent prior-art reviewer, topics/bivariate-lanczos-20261031/reviews/L1-prior-art-01.md, 2026-10-31). Record written by the Claude literature developer (Sonnet 5.5, effort high) at PR-preparation consolidation 2026-11-01 from the review text only.
- Named gaps requiring future re-reading: Verbatim check of eq. (2.14) and Thm 2.11; the primary sources named above.
- Source review: topics/bivariate-lanczos-20261031/reviews/L1-prior-art-01.md (audit-01 protocol finding P2). Rules/base SHA of the originating work: d36722823441dc40c6e19d69a174459348dd309c (Step 0 baseline).

## Extracted published statements

### LIT-245 (LIT?bivariate-lanczos-claude-402) — three-term recursion with a non-unique left inverse D_n of the stacked coefficient matrix

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: §2.2, eq. (2.14): P_{n+1} = sum_i x_i D_{n,i}^T P_n + E_n P_n + F_n P_{n-1} with D_n^T A_n = I, where A_n is the stacked matrix of three-term coefficients (notation as digested); the survey states that such a left inverse is not unique. Thm 2.11 gives the conditions under which this recursion yields orthonormal polynomials.
- Hypotheses and notation: Orthonormal polynomial vectors P_n for a positive-definite moment functional in d variables; the exact conditions of Thm 2.11 were not extracted.
- Page / theorem / equation: §2.2, eq. (2.14); Thm 2.11 (as digested).
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source.
- Relation to campaign claims (no inherited proof status): The window (BJ/HL) recurrence's triangular selection is, in the reviewer's reading, one particular choice of D_n in this recursion (PD-T?bivariate-lanczos-claude-108). The classical non-uniqueness is therefore published; the campaign's statement that the choice decides floating-point stability (PD-T?bivariate-lanczos-claude-109) is not found here.

## Search and attribution notes

L1 search #21 (Xu lecture notes / survey, left inverse D_n). The key `xu-2017-survey` is the one used in the L1 table; the arXiv number gives the posting year 2017. Unsupported assertions are UNVERIFIED.

## History

2026-11-01: record created at PR-preparation consolidation (audit-01 protocol finding P2) from L1-prior-art-01.md. Provisional IDs only; final `LIT-nnn` allocated at PR preparation. No source was re-read by the consolidator; bibliographic checks (if any) are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'.
