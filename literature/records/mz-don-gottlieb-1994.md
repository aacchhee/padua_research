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

## 2026-11-03 journal-version comparison — padua-literature-20261103

# Addendum to mz-don-gottlieb-1994 (LIT-058) — journal version read and compared with the ICASE report

W. S. Don, D. Gottlieb, *The Chebyshev–Legendre method: implementing Legendre methods on Chebyshev points*, SIAM J. Numer. Anal. 31(6) (1994) 1519–1534, DOI <https://doi.org/10.1137/0731079>.

- Access and reading date: 2026-11-03. Publisher PDF supplied by AC (`Downloads\padua\papers\0731079.pdf`, staged to /mnt/user-data/uploads/padua/papers/), a scanned article with an OCR text layer, read with `pdftotext -layout`. OCR garbles most displayed formulas; statements below were checked against the surrounding prose and the report reading, not against page images. Not stored in Git.
- Reading coverage: pp. 1519–1525 read (abstract, §1, §2 preliminaries, §3.1 with Theorems 3.1.1 and 3.1.2 and their proofs, start of §3.2); §3.2 theorem statements (Theorems 3.2.1–3.2.2, pp. 1525–1527), §4 (Lemma 4.1, Theorem 4.1, pp. 1527–1530) and §5 (numerical results) screened. Received 9 Feb 1994, revised version accepted 30 Mar 1994.
- Reader, model and effort: Claude, Opus 5.5, high. Rules `af1ac9fde6b23cb9cd826a33d5611680566c52cb`.

## Comparison with ICASE Report 93-40 (the version read on 2026-11-01)

| Item | ICASE 93-40 (repo record) | Journal SINUM 31 (1994) | Change |
|---|---|---|---|
| Data / ghost points | Chebyshev–Gauss–Lobatto data; Legendre–Gauss–Lobatto points only in the proof | Same; the GLL points are called ghost points that never enter the computation (pp. 1524, 1530) | none |
| Thm 3.1.1 | L² stability via exactness of GLL quadrature to degree 2N−1; report p. 7 | Theorem 3.1.1, journal p. 1524: same mechanism (penalty parameter lower bound in terms of N(N+1)/(2w₀); energy identity from GLL exactness for degree 2N−1) | locator only |
| Thm 3.1.2 | Nodal quadratic form H_{jl} = Σ_k g_j(y_k)g_l(y_k)w_k in the Chebyshev–Lagrange basis; report p. 8 | Theorem 3.1.2, journal pp. 1524–1525: same identity, proved by expanding u_N at the GLL points in the CL cardinal basis (3.14) | locator only |
| Norm-equivalence constants, CC weights | none | none found in pp. 1519–1525 or in the screened §§3.2–5; the CGL quadrature (2.4)–(2.5) appears only as the Chebyshev-weighted rule of exactness 2N−1 (p. 1520–1521) | none |
| §4 parabolic | Lemma 4.1 / Theorem 4.1 energy estimate in the discrete GLL inner product | Lemma 4.1, Theorem 4.1, journal pp. 1528–1529: same | locator only |

- Conclusion: the journal version agrees with the report on every item the repo used. The verdict for PD-T017 is **unchanged: RELATED, DIFFERENT SETTING** (the nodal form is the pull-back of the discrete GLL energy, which equals ∫p² only up to degree 2N−1, not for all p ∈ Π_N; no constants).

## Old → new corrections to the record

- Old: "The journal version (SIAM J. Numer. Anal. 31(6)) was not compared (SIAM blocked)."
- New: "Journal version read 2026-11-03 from an AC-supplied PDF (OCR text layer): Theorem 3.1.1 p. 1524, Theorem 3.1.2 pp. 1524–1525, Lemma 4.1/Theorem 4.1 pp. 1528–1529; identical in substance to ICASE 93-40 on all items used. Gap closed."
- Header line "Mathematical content FULLTEXT UNVERIFIED" (2026-10-31) is historical; add a pointer to this addendum.

## History

2026-11-03: journal-vs-report comparison completed (P2 reader).
