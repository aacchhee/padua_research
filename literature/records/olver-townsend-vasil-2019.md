# olver-townsend-vasil-2019 — S. Olver, A. Townsend, G. Vasil, A sparse spectral method on triangles, SIAM J. Sci. Comput. 41(6) (2019) A3728–A3756

- DOI / URL / supplied location: doi:10.1137/19M1245888 (checked against Crossref by the L1 reviewer); https://par.nsf.gov/servlets/purl/10158662
- Access and reading date: 2026-10-31 (read by the L1 prior-art reviewer); record written 2026-11-01 (PR-preparation consolidation).
- Reading coverage: WebFetch digest of the par.nsf.gov full text, §§2.2–2.4 (the statement below is from §2.3); the remaining sections (the sparse spectral method itself, numerical results) were not read.
- Reader, model and effort: Claude Opus 5.5, effort high (independent prior-art reviewer, topics/bivariate-lanczos-20261031/reviews/L1-prior-art-01.md, 2026-10-31). Record written by the Claude literature developer (Sonnet 5.5, effort high) at PR-preparation consolidation 2026-11-01 from the review text only.
- Named gaps requiring future re-reading: Whole paper beyond §§2.2–2.4; hypotheses of the OP family on the triangle (Jacobi-type weights) were not extracted; verbatim re-check of §2.3 and eq. (2.10).
- Source review: topics/bivariate-lanczos-20261031/reviews/L1-prior-art-01.md (audit-01 protocol finding P2). Rules/base SHA of the originating work: d36722823441dc40c6e19d69a174459348dd309c (Step 0 baseline).

## Extracted published statements

### LIT?bivariate-lanczos-claude-401 — stacked x/y three-term relations are not lower triangular; pseudo-inverse B_n^+ used to recover the next degree

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: For orthogonal polynomials on the triangle, the x- and y-recurrences stacked for the next degree form a system that, in the digest's quote, is not lower triangular and cannot be inverted immediately by forward recurrence; the authors therefore multiply by pseudo-inverses B_n^+ (eq. (2.10)) to obtain the next-degree polynomials.
- Hypotheses and notation: Orthogonal polynomials on the triangle with the paper's weights (not extracted by the reviewer).
- Page / theorem / equation: §2.3, eq. (2.10) (as digested by the reviewer).
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source. The reviewer reports that the choice of B_n^+ is made for cost and structure reasons and that no numerical comparison of different left inverses is given in the sections read.
- Relation to campaign claims (no inherited proof status): Closest prior for the 'one relation per column / left inverse' view of PD-T?bivariate-lanczos-claude-108 (row selection of the Jacobi pencil) together with xu-2017-survey eq. (2.14): the algebraic frame (consistent overdetermined stacked system, non-unique left inverse) is published; the stability role of the choice is not seen in the pages read (see also barrio-pena-sauer-2010, statements 301-303).

## Search and attribution notes

L1 search #10 (OTV 2019 SISC, par.nsf.gov); Crossref metadata also consulted by the L1 reviewer (L1 search log, 'Pages fetched'). Unsupported assertions are UNVERIFIED.

## History

2026-11-01: record created at PR-preparation consolidation (audit-01 protocol finding P2) from L1-prior-art-01.md. Provisional IDs only; final `LIT-nnn` allocated at PR preparation. No source was re-read by the consolidator; bibliographic checks (if any) are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'.
