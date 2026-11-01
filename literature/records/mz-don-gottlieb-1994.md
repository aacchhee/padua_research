# mz-don-gottlieb-1994 — Chebyshev–Legendre method

- Citation: W. S. Don, D. Gottlieb, *The Chebyshev–Legendre Method: Implementing Legendre Methods on Chebyshev Points*, SIAM J. Numer. Anal. 31 (1994), 1519–1534, DOI <https://doi.org/10.1137/0731079>.
- Primary publisher: <https://epubs.siam.org/doi/10.1137/0731079>.
- PDF attempt: <https://bpb-us-w2.wpmucdn.com/blog.nus.edu.sg/dist/4/11813/files/2019/05/dg.pdf>; 17 pages reported but extracted text contains only archival cover metadata, not body text.
- Access/read: 2026-10-31, metadata/abstract discovery. Mathematical content **FULLTEXT UNVERIFIED**.
- Reader: Codex; gpt-6.1-sol, high (explicit orchestrator assignment).

## Source statement

### LIT-058 — PDE-method ancestor, unresolved norm comparison

The publisher abstract describes using Chebyshev collocation points with Legendre-method advantages through boundary-condition treatment. No theorem about the actual CC weights or sharp MZ constants was extracted.

- Locator: abstract; no theorem locator inspected.
- Relation/gap: inspect any stability/norm-equivalence lemmas in the full body, including whether its discrete inner product is a dense transformed Legendre mass matrix or diagonal CC quadrature. A matching node set is insufficient to identify the two problems.

## History

2026-10-31: source trap retained without claiming an exclusion.

## 2026-11-01 report-version reading (topic mz-prior-art-20261101)

Reader: Claude, Opus 5.5. Access: free publisher/open PDF read through the WebFetch tool, which extracts the text layer and answers through a summarizing model. Coverage is therefore paraphrase-level; OCR formulas are partly garbled. Any formula-level use needs a page-image check. Rules `9739a0c`, 2026-11-01.

- Source read: ICASE Report 93-40 / NASA CR-191497 (July 1993), https://ntrs.nasa.gov/api/citations/19940009252/downloads/19940009252.pdf (public). The journal version (SIAM J. Numer. Anal. 31(6)) was not compared (SIAM blocked).
- Findings: data at Chebyshev–Gauss–Lobatto points; stability is in the L²(dx) norm through Legendre–Gauss–Lobatto "ghost points". Thm 3.1.1 (p. 7) uses exactness of GLL quadrature to degree 2N−1. Thm 3.1.2 (p. 8) writes the GLL norm as a nodal quadratic form H_jl=Σ_k g_j(y_k)g_l(y_k)w_k in the Chebyshev–Lagrange basis (an identity). No norm-equivalence constants, no CC weights.
- **Verdict for PD-T017: RELATED, DIFFERENT SETTING.** Gap reduced to the journal-vs-report comparison.
