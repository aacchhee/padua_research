# mz-an-wu-2022 — quadrature exactness in hyperinterpolation

- Citation: C. An, H.-N. Wu, *On the quadrature exactness in hyperinterpolation*, BIT Numerical Mathematics 62 (2022), 1899–1919, DOI <https://doi.org/10.1007/s10543-022-00935-x>.
- Primary text: <https://arxiv.org/html/2202.13691v3>, version dated 11 July 2022. <https://arxiv.org/abs/2202.13691> lists v1/v2/v3; no later arXiv revision was listed on access.
- Access/read: 2026-10-31; Assumption 2.1, equation (2.5), main theorem statement, §4 introductory paragraph, §4.1/Corollary 4.1. This is selected primary fulltext coverage, not a complete proof audit. Publisher page supplies metadata/abstract only: published fulltext **FULLTEXT UNVERIFIED**.
- Reader: Codex; gpt-6.1-sol, high (explicit orchestrator assignment).

## Extracted source statement

### LIT-046 — explicitly conditional CC application

For positive rules exact through n+k (0<k<=n), the main theorem assumes an MZ relative squared-norm error eta<1 on degree <=n. Section 4 assumes eta=3/4 for its examples. Corollary 4.1 includes m-point CC with n+2<=m<=2n+1, explicitly retaining the theorem's conditions and eta=3/4, and gives error <=3 sqrt(V) E_(m-1-n)(f).

- Locator: Assumption 2.1; equations (2.5)–(2.7); §4 opening; §4.1 Corollary 4.1.
- Relation: a counterexample to eta<=3/4 at m=n+2 would obstruct that application. It would not refute the stated conditional implication. Replacing a valid but loose bound by a sharper upper-Gram estimate may also improve an operator estimate; the factor based on 1/sqrt(1-eta) must not automatically be described as the true operator norm.
- Named gaps: compare the published Corollary and check publisher corrections comprehensively before calling this a published correction. Searches for exact title plus “erratum” and “correction” found no matching correction in the documented search; this is not proof that none exists.

## History

2026-10-31: conditionality and point-count scope verified against arXiv v3; provisional ID only.

## 2026-11-01 published-version comparison (topic mz-prior-art-20261101)

Reader: Claude, Opus 5.5 (orchestrator). Access: publisher PDF via AC's NTNU institutional access in AC's built-in browser, text extracted in-page with pdf.js and read in the session only; no PDF or fulltext extract stored anywhere in the repository. Rules `9739a0c`.

- Coverage: published BIT 62 (2022) 1899–1919, keyword-screened in full; Assumption 2.1 (p. 1902), Theorem 2.2 (p. 1905), §4 opening (p. 1910) and Corollary 4.1 (p. 1911) read.
- Finding: matches arXiv v3 on all inspected points. Section 4 opens by assuming the MZ property with η=3/4, "a quite loose assumption". Corollary 4.1 covers m-point CC with n+2≤m≤2n+1 "under the conditions of Theorem 2.2 with η=3/4", with error ≤3V^{1/2}E_{m−1−n}(f). PD-N004's case (m=513, n=511) is m=n+2, inside the stated range. The conditional reading is unchanged.
- Correction search: see topics/mz-prior-art-20261101/LOG.md (Crossref/publisher check by the group-C worker).

## 2026-11-03 primary-reading addendum — padua-literature-20261103

# Addendum to mz-an-wu-2022 (LIT-046) — screen for Padua / square / Chebyshev-type MZ statements

C. An, H.-N. Wu, *On the quadrature exactness in hyperinterpolation*, BIT Numer. Math. 62 (2022) 1899–1919, DOI <https://doi.org/10.1007/s10543-022-00935-x>; arXiv 2202.13691v3 (11 Jul 2022).

- Access and reading date: 2026-11-03. Reader: Claude, Opus 5.5, high. Rules `af1ac9fde6b23cb9cd826a33d5611680566c52cb`.
- Coverage of this addendum: keyword screen (Padua, square, Chebyshev, Xu, Lissajous, cube) of both the published PDF (21 pp., link.springer.com in AC's built-in browser, pdf.js text layer) and arXiv v3 (16 pp.), with the hits read in context. This is a targeted screen, not a re-reading of the theorems (those were read 2026-10-31 and 2026-11-01; see the record).
- Findings:
  - Published p. 1901 (arXiv p. 2): the square and cube occur only as regions where hyperinterpolation was previously studied (Caliari–De Marchi–Vianello), with exactness 2n assumed there.
  - Published p. 1911 area (arXiv p. 9): Chebyshev occurs only in the Clenshaw–Curtis discussion leading to Corollary 4.1 (1-D CC, η = 3/4 assumed), as already recorded.
  - "Padua", "Xu", "Lissajous" do not occur in either version.
  - **No MZ statement for Padua points, the square, or 2-D Chebyshev-type rules exists in An–Wu.** All its Chebyshev-type content is the 1-D CC Corollary 4.1 under an assumed η.
- Relation to campaign claims: unchanged for PD-N004 (conditional corollary; applicability hypothesis refuted at m = n+2 = 513). For PD-N044 (2-D, m = 30): An–Wu contains no Padua or square application, so PD-N044 refutes only the uniform-applicability hypothesis η ≤ 3/4 as used by readers who would transfer An–Wu's framework to Padua; it refutes no statement of An–Wu. *No matching result found in the documented search* for PD-T106–117.

## History

2026-11-03: targeted screen added (P2 reader).
