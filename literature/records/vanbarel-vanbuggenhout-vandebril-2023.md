# vanbarel-vanbuggenhout-vandebril-2023 — M. Van Barel, N. Van Buggenhout, R. Vandebril, "Algorithms for modifying recurrence relations of orthogonal polynomial and rational functions when changing the discrete inner product", Appl. Numer. Math. 200 (2024) 429–452 (online 2023)

Registration (2026-11-05 PR21 final registration): LIT-346, LIT-504. Original provisional aliases remain below; [exact map](../../topics/padua-literature-20261103/preparation/final-id-map.json). Source statements, versions, reader attribution and reading limits are unchanged. Developer-only source checks remain qualified by audit02/03; no independent auditor page-image verification is inferred.

- DOI / URL: https://doi.org/10.1016/j.apnum.2023.07.009 ; preprint https://arxiv.org/abs/2302.00355 (v1, 1 Feb 2023, the only version).
- Access and reading date: 2026-11-03, arXiv v1 PDF (45 pp.) in the built-in browser, pdf.js text extraction. The journal version was not opened (ScienceDirect).
- Reading coverage: exact pages of the arXiv v1. Read: pp. 1–3 (abstract, introduction, outline), p. 11–14 (§3.2 RQ vs QR, Def. 3.2, §4 opening), p. 17 (§4.2 opening), pp. 18–19 (eigenvector method, §5 metrics), pp. 21–26 (experiment text), pp. 33–34 (§8.2 end, §9 opening), pp. 38–42 (§10 and acknowledgements), plus the section-heading list. Not read: §2 problem statements in detail, §3.3 Theorem 3.3 proof, §§6–8 theory, the journal version.
- Reader, model and effort: Claude P4 literature reader (claude-opus-5-5, high).
- Named gaps requiring future re-reading: the ANM journal version, which may differ (for example a conclusions section); Theorem 3.3 statement and proof (p. 13); §7 pencil theorems.

Locators are arXiv v1 PDF pages.

## Extracted published statements

### LIT-346 (LIT?padua-literature-claude-75) — attribution: author list

- Statement in faithful paraphrase: The paper has exactly three authors: Van Barel, Van Buggenhout (corresponding; then at Charles University, Prague) and Vandebril. Faghih is not an author.
- Page / theorem / equation: arXiv v1 PDF p. 1. Crossref metadata agree (p4-links.md row 3).
- Reading evidence and limitations: title page read.
- Relation to campaign claims: resolves the author conflict recorded in LIT-346.

### LIT-346 (LIT?padua-literature-claude-76) — method: downdating OP recurrences by perfect-shift RQ steps (three variants)

- Statement in faithful paraphrase: The paper completes the earlier updating work (Van Buggenhout–Van Barel–Vandebril 2022) with downdating, i.e., removing a node from a discrete inner product while keeping the recurrence. For polynomials (Hessenberg H_m = Q^H Z Q), a known node is deflated with one perfect-shift step. An **RQ** step, not a QR step, is needed: the QR step destroys the weight condition on the first column, while the RQ step keeps it after removing the deflated row (§3.2, eq. (8)). Three mathematically equivalent implementations are compared: the explicit matrix method, the implicit matrix method (core-transformation chasing) and the eigenvector method of Mastronardi–Van Dooren 2018, where the eigenvector is obtained by evaluating the OPs at the node through the recurrence (Golub–Welsch) and refined iteratively. For rational functions the same idea is carried to Hessenberg pencils through rational RQZ steps (§§7–8).
- Hypotheses and notation: nodes z_i ∈ C, weights w_i; unitary core transformations (Def. 3.2).
- Page / theorem / equation: abstract p. 1–2; outline p. 3; §3.2 pp. 11–12; Def. 3.2 p. 12; §4 opening p. 14; eigenvector method pp. 18–19.
- Reading evidence and limitations: pages listed above read; Theorem 3.3 (equivalent statements, p. 13) was seen only as a heading list.
- Relation to campaign claims: the unitary (OP) precursor of LIT?…-73. This is the step that a bivariate downdating would generalize.

### LIT-504 (LIT?padua-literature-claude-77) — numerical finding and stated future work

- Statement in faithful paraphrase: In the experiments (nodes on the unit circle with m = 500; Chebyshev nodes with m = 200–500; equidistant nodes with m = 250), the eigenvector method gives the best metrics but depends on an accurate eigenvector. With one refinement step it breaks down in an unbalanced Chebyshev ordering (k = 69 for m = 200); two steps fix this. Equidistant nodes need more refinement. Two items are stated in the text as future research: (i) how to choose the number b of refinement steps before re-testing the accuracy condition (p. 25); (ii) which order of left and right eigenvector treatment gives the most stable pencil variant (p. 34). The arXiv v1 has **no conclusions section**: §10 (sliding-window least squares) is followed directly by the acknowledgements (p. 42).
- Page / theorem / equation: pp. 21–25 (Figs. 2–9, Tables 1–2); future-work sentences p. 25 and p. 34; end of text p. 42.
- Reading evidence and limitations: experiment text read, plots not read.
- Relation to campaign claims: the eigenvector-accuracy sensitivity is a design warning for any bivariate eigenvector-based downdating.

## Search and attribution notes

- Searches on 2026-11-03 over all 45 pages: "bivariate", "multivariate", "Chesnokov", "two variables", "several variables" gave 0 hits.
- The introduction (pp. 2–3) cites vector orthogonal polynomial generalizations (Bultheel–Van Barel 1995; Van Barel–Bultheel 1992–2001). That is the line from which Van Barel–Chesnokov 2010 descends. The 2010 bivariate paper itself is not cited.

## History

2026-11-03: new record (P4); provisional IDs 75–77. Supersedes the secondary statement LIT-346 (see the addendum).
