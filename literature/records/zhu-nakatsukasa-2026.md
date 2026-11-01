# zhu-nakatsukasa-2026 — W. Zhu, Y. Nakatsukasa, Convergence and near-optimal sampling for multivariate function approximations in irregular domains via Vandermonde with Arnoldi, IMA J. Numer. Anal. 46(4) (2026) 2072-2106, doi:10.1093/imanum/draf055

- DOI / URL / supplied location: https://doi.org/10.1093/imanum/draf055 -> https://academic.oup.com/imajna/article/46/4/2072/8210327 (landing page fetched 2026-10-31); preprint arXiv 2301.12241 (as cited in reports/Padua points research since 2010.md)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: metadata (title, authors, venue, volume/issue, pages, DOI) + abstract confirmed by me on the OUP page; fulltext NOT inspected.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Fulltext: loss-of-orthogonality remarks and the near-optimality bound constants.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-024 — multivariate Vandermonde with Arnoldi (abstract)

- Verification: **Abstract-checked only** (OUP landing-page abstract); full text NOT inspected, so the mathematical content stays UNVERIFIED. `LITERATURE` attribution only.
- Statement in faithful paraphrase: Extends Vandermonde with Arnoldi to several dimensions via least squares with Stieltjes orthogonalization using sample points only; about O(N^2) equispaced or O(N^2 log N) random points give a well-conditioned near-optimal approximation on many irregular domains; a weighted variant needs O(N log N) points.
- Hypotheses and notation: As stated in the abstract; hypotheses beyond the abstract not checked.
- Page / theorem / equation: abstract. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance OUP landing page fetched 2026-10-31; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L2 cost comparator: full Arnoldi/Stieltjes orthogonalization O(M N^2).

### LIT?bivariate-lanczos-claude-025 — full orthogonalization and loss of orthogonality (reported)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Reported: the implementation uses full two-pass classical Gram-Schmidt at cost O(M N^2); the authors state multivariate V+A orthogonalization 'is subject to a loss of orthogonality due to numerical cancellation'. The 2024-2026 follow-ups are reported to be applications without truncation or rounding analysis.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: locators not supplied. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/recent_multivariate_NLA.md §1 items 1, R1 (b); reports/Padua points research since 2010.md problem-3 paragraph; notes/verify_algorithmic_problems.md venue fix; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1/L2 motivation. Quotation and cost claim are the supplying agents' reports, not in the abstract; UNVERIFIED.

## Search and attribution notes

Venue correction preserved from notes/verify_algorithmic_problems.md: the journal is IMA J. Numer. Anal. 46(4) (2026), doi:10.1093/imanum/draf055. Confirmed on the landing page (online 22 Jul 2025, issue dated July 2026). Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.
2026-11-01: orchestrator annotation — the L2 developer (response-recon-01, finding F9) reports that the sentence quoted for LIT?bivariate-lanczos-claude-025 was not found in arXiv v2 of this paper; treat that statement's wording as UNVERIFIED until checked against the published version. The identification of BJ + CGS2-against-all with this paper's multivariate V+A is also UNVERIFIED (paper digest only; code not checked).
