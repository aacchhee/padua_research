# zhang-su-li-2024 — L.-H. Zhang, Y. Su, R.-C. Li, Accurate polynomial fitting and evaluation via Arnoldi, Numer. Algebra Control Optim. 14(3) (2024) 526–546

- DOI / URL / supplied location: doi:10.3934/naco.2023002; https://par.nsf.gov/servlets/purl/10547074
- Access and reading date: 2026-11-01 (read by the L2 prior-art reviewer); record written 2026-11-01 (PR-preparation consolidation).
- Reading coverage: WebFetch digest of the par.nsf.gov full text (Thm 3.1, Lemma 3.1, Remark 3.2).
- Reader, model and effort: Claude Opus 5.5, effort high (independent prior-art reviewer, topics/bivariate-lanczos-20261031/reviews/L2-prior-art-01.md, 2026-11-01). Record written by the Claude literature developer (Sonnet 5.5, effort high) at PR-preparation consolidation 2026-11-01 from the review text only.
- Named gaps requiring future re-reading: Remaining sections and proofs; verbatim check of the theorem statements.
- Source review: topics/bivariate-lanczos-20261031/reviews/L2-prior-art-01.md (audit-01 protocol finding P2). Rules/base SHA of the originating work: d36722823441dc40c6e19d69a174459348dd309c (Step 0 baseline).

## Extracted published statements

### LIT?bivariate-lanczos-claude-408 — rounding-error theorem for univariate Vandermonde-with-Arnoldi fitting: bound on fitted/evaluated values only

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Univariate, real setting. Thm 3.1 bounds the forward error of the fitted and evaluated values. Lemma 3.1 is the Arnoldi residual relation with Frobenius norm of the residual F at most sqrt(n) times ‖X‖ times u. Remark 3.2 says only the 2-norm condition number of the computed Q-hat enters. The distance of the computed Q-hat or H-hat from the exact basis or recurrence is not bounded.
- Hypotheses and notation: Real univariate nodes; floating-point model not extracted.
- Page / theorem / equation: Thm 3.1, Lemma 3.1, Remark 3.2 (as digested).
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source.
- Relation to campaign claims (no inherited proof status): Reported by the L2 reviewer as the only rounding-error theorem found for V+A. It separates fit accuracy from span accuracy, so it does not contradict or subsume the span-drift statements PD-N?bivariate-lanczos-claude-201 and PD-N?bivariate-lanczos-claude-203; cite it to mark that separation.

## Search and attribution notes

L2 search #1–2 (V+A error analysis). Unsupported assertions are UNVERIFIED.

## History

2026-11-01: record created at PR-preparation consolidation (audit-01 protocol finding P2) from L2-prior-art-01.md. Provisional IDs only; final `LIT-nnn` allocated at PR preparation. No source was re-read by the consolidator; bibliographic checks (if any) are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'.
