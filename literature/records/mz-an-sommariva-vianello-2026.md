# mz-an-sommariva-vianello-2026 — weak MZ constants

- Citation: C. An, A. Sommariva, M. Vianello, *On the role of weak Marcinkiewicz–Zygmund constants in polynomial approximation by orthogonal bases*, arXiv:2601.04708v1, 8 January 2026.
- URLs: <https://arxiv.org/abs/2601.04708>; <https://arxiv.org/html/2601.04708v1>.
- Access/read: 2026-10-31, primary HTML introduction, §§3.1–3.2 and bibliography inspected; selected portions only. Figures and accompanying code were not independently rerun.
- Reader: Codex, gpt-6.1-sol, high (explicit orchestrator assignment).
- Named gap: published version, listed on Sommariva's CV as *Mathematics and Computers in Simulation* 252 (February 2027), 733–745; final fulltext/DOI and changes **FULLTEXT UNVERIFIED**. The CV shortens the title by omitting “weak”.

## Extracted source statement

### LIT-045 — finite-degree CC/Padua observations

The paper computes Gram eigenvalues for orthonormal bases and reports eta<1 past half-exactness for CC on the interval and Padua-based cubature for Lebesgue measure on the square, through n=m-1. The displayed experiments use ADE m=1,...,20 and polynomial degree n=0,...,30. The introduction explicitly separates these degree-dependent constants from strong uniform constants and says the latter are outside the paper's aim.

- Hypotheses: continuous norm for the stated measure, discrete rule Gramian; square uses total-degree products. Its m denotes ADE, not the campaign's CC node index N or An–Wu's point count m.
- Locator: introduction questions and closing scope paragraphs; §3.1/Figures 1–2; §3.2/Figures 3–4.
- Relation: direct numerical predecessor to M1/M3 and Padua target; no all-degree theorem or endpoint asymptotic is extracted here. Basis/measure and parameter conventions must be preserved.

Additional selected primary coverage: the independent gpt-6-astra xhigh auditor directly inspected the introduction, equations (7)–(8), on 2026-10-31; see topics/mz-constants/independent-astra-01.md. Equation (7) gives an unfettered-hyperinterpolation estimate using an upper factor of the form 1+sqrt(1+eta), together with an aliasing term; equation (8) distinguishes least squares through inversion of the Gram matrix. Thus the general upper-Gram operator-bound mechanism is known context. The local CC bound supplies an independently proved application, without a new-mechanism claim for the generic estimate. This source paraphrase extends reading coverage, not the local proof status or a claim of a complete source audit.

## Search and attribution

Queries and limits are in `topics/mz-constants/literature-search.md`. Bibliography [28] is Trefethen's 2008 *Is Gauss quadrature better than Clenshaw–Curtis?*, distinct from his 2022 *Exactness of Quadrature Formulas*.

## History

2026-10-31: selected primary-text reading recorded, provisional ID only.

## 2026-11-01 published-version metadata (topic mz-prior-art-20261101; group-C access worker, Sonnet 5.5 high)

- Published: Math. Comput. Simul. 252 (Feb. 2027) 733–745, DOI 10.1016/j.matcom.2026.10.001, PII S0378475426004416 (Crossref). The published title includes "weak", identical to arXiv; the CV omitted it.
- Access: Elsevier TDM licence only, not open access (Crossref, OpenAlex). ScienceDirect is blocked for the tools and the automated browser. Body text is **FULLTEXT UNVERIFIED** (on AC's missing list).
- arXiv: only v1 visible (v2 neither confirmed nor refuted, rate-limited). A 16-page "Preprint" PDF is linked from Vianello's homepage, https://www.math.unipd.it/~marcov/pdf/MZ.pdf (same title/abstract; version relative to v1 undetermined; not read here).
- Forward citations: 0 in Crossref/OpenAlex/Semantic Scholar on 2026-11-01.

## 2026-11-01 published-version reading (topic mz-prior-art-20261101)

Reader: Claude, Opus 5.5. PDF supplied by AC (NTNU access), text via pdftotext; read in the session only.

- Published MCS 252 (2027) 733–745. Received 28 Feb 2026, revised 29 Sep 2026, accepted 2 Oct 2026, online 16 Oct 2026; special issue MATCOM_ATMA2026. Coverage: complete article, keyword-screened, with §§1–2 and §3.1, §3.6 read.
- Differences in theoretical content: Proposition 2.1 (eigenvalue characterization of the weak MZ constants A=λ_min(G), B=λ_max(G)). Theorem 2.1 (pp. 736–737): for a k-point Gaussian rule and n≥k, η≥1, with worst-case polynomial ±ψ_n; Remark 2.5 covers the tensor-product extension. Whether these were already in arXiv v1 was not checked line by line; the earlier record does not list them.
- CC (§3.1, p. 738): experiments m≤20, n≤30 show η<1 for ⌊m/2⌋<n≤m−1. The authors write that this behaviour is, to their knowledge, "not known" and "could deserve further study". §3.6 (p. 742) guesses the cause lies in special properties of Chebyshev polynomials, "beyond the scope of the present paper". Padua: η<1 up to n=m−1 observed.
- Relation: still the numerical predecessor. No all-N CC or Padua theorem; the authors explicitly flag the CC behaviour as theoretically open as of October 2026. **Verdict: RELATED** (numerical predecessor; PD-T014/017/018/022/024 not anticipated). Reference [4] is Lubinsky's survey.
