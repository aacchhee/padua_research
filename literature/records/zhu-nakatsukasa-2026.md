# zhu-nakatsukasa-2026 — W. Zhu, Y. Nakatsukasa, Convergence and near-optimal sampling for multivariate function approximations in irregular domains via Vandermonde with Arnoldi, IMA J. Numer. Anal. 46(4) (2026) 2072-2106, doi:10.1093/imanum/draf055

- DOI / URL / supplied location: https://doi.org/10.1093/imanum/draf055 -> https://academic.oup.com/imajna/article/46/4/2072/8210327 (landing page fetched 2026-10-31); preprint arXiv 2301.12241 (as cited in reports/Padua points research since 2010.md)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: metadata (title, authors, venue, volume/issue, pages, DOI) + abstract confirmed by me on the OUP page; fulltext NOT inspected. PR-preparation (2026-11-01) from the L1 (2026-10-31) and L2 (2026-11-01) prior-art reviews: fulltext via WebFetch digests of arXiv 2301.12241 (PDF twice and HTML once; the ar5iv copy was truncated), §§2–3, 5 and Remark 3. Appendix B (Algorithms 4–5, evaluation from stored H's) is absent from all copies fetched and was NOT seen.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation). PR-preparation additions (2026-11-01): taken from the L1 prior-art review 2026-10-31 and L2 prior-art review 2026-11-01 (Claude Opus 5.5, effort high; reading through WebFetch digests) by the Claude literature developer (Sonnet 5.5, effort high); the source was not re-read by the consolidator.
- Named gaps requiring future re-reading: Fulltext: loss-of-orthogonality remarks and the near-optimality bound constants. PR-preparation: Appendix B (Algorithms 4–5), where a statement on the accuracy of the stored H's would sit; which arXiv version the reviewers read; the exact location of the loss-of-orthogonality sentence (see statement 441).
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT-089 (LIT?bivariate-lanczos-claude-024) — multivariate Vandermonde with Arnoldi (abstract)

- Verification: **Abstract-checked only** (OUP landing-page abstract); full text NOT inspected, so the mathematical content stays UNVERIFIED. `LITERATURE` attribution only.
- Statement in faithful paraphrase: Extends Vandermonde with Arnoldi to several dimensions via least squares with Stieltjes orthogonalization using sample points only; about O(N^2) equispaced or O(N^2 log N) random points give a well-conditioned near-optimal approximation on many irregular domains; a weighted variant needs O(N log N) points.
- Hypotheses and notation: As stated in the abstract; hypotheses beyond the abstract not checked.
- Page / theorem / equation: abstract. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance OUP landing page fetched 2026-10-31; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L2 cost comparator: full Arnoldi/Stieltjes orthogonalization O(M N^2).

### LIT-090 (LIT?bivariate-lanczos-claude-025) — full orthogonalization and loss of orthogonality (reported)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Reported: the implementation uses full two-pass classical Gram-Schmidt at cost O(M N^2); the authors state multivariate V+A orthogonalization 'is subject to a loss of orthogonality due to numerical cancellation'. The 2024-2026 follow-ups are reported to be applications without truncation or rounding analysis.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: locators not supplied. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/recent_multivariate_NLA.md §1 items 1, R1 (b); reports/Padua points research since 2010.md problem-3 paragraph; notes/verify_algorithmic_problems.md venue fix; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1/L2 motivation. Quotation and cost claim are the supplying agents' reports, not in the abstract; UNVERIFIED.

### LIT-283 (LIT?bivariate-lanczos-claude-440) — §3: the multivariate monomial basis does not correspond to a Krylov subspace

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: §3 (as digested): unlike 1D Arnoldi, the multivariate monomial basis does not correspond to a Krylov subspace.
- Hypotheses and notation: Multivariate V+A on irregular domains.
- Page / theorem / equation: §3 (arXiv 2301.12241).
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source.
- Relation to campaign claims (no inherited proof status): An informal statement weaker than PD-T?bivariate-lanczos-claude-401 (no commuting-operator qualifier, no fixed-start count, no proof).

### LIT-284 (LIT?bivariate-lanczos-claude-441) — rounding content of multivariate V+A: CGS2 orthogonality bound feeding the fit bound; basis accuracy evidence is 1D

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: No backward-stability or forward-error theorem for multivariate V+A and no analysis of the computed Hessenberg matrices was found. §2 states in exact arithmetic that the discrete orthogonal basis spans the polynomial space (univariate wording). §2.1 and Remark 3 (§5.1) give the CGS2 loss-of-orthogonality bound eps_m = O(M N^{3/2} u) on ‖Q*Q - I‖, citing Higham Thm 19.4 and '[15, Thm 2]'; eps_m enters only the near-optimality (fit) bound. Thm 6 ('stable with high probability') is about sampling, not rounding. §5.2 says the discrete orthogonal polynomials generated by V+A are unaffected by the ill-conditioning of A; the only basis-versus-exact comparisons (phi_30 against scaled Legendre, §2.3.1, Fig. 2 and Fig. 10) are 1D, and the 2D evidence is fit error on tensor and elliptical domains. No triangles or rotated domains appear and commutativity is not discussed. Remark 3 is also reported (L1 review) to say that orthogonalization is subject to a loss of orthogonality due to numerical cancellation.
- Hypotheses and notation: As digested.
- Page / theorem / equation: §2, §2.1, §2.3.1 (Figs 2, 10), Remark 3 (§5.1), Thm 6, §5.2.
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source. CONFLICT: the 2026-11-01 orchestrator annotation in this record's History reports that the sentence quoted for statement 025 was not found in arXiv v2; the L1 reviewer reports it in Remark 3. UNRESOLVED; the version read by the reviewers was not recorded.
- Relation to campaign claims (no inherited proof status): Reported by the L2 reviewer as not contradicting or subsuming the span-drift statements PD-N?bivariate-lanczos-claude-201 and PD-N?bivariate-lanczos-claude-203: ZN's content is fit accuracy and the CGS2 bound, its basis evidence is 1D; the 'unaffected' sentence is the closest contrary-sounding claim and must be quoted with its 1D support. Appendix B unseen is a named gap for these statements.

## Search and attribution notes

Venue correction preserved from notes/verify_algorithmic_problems.md: the journal is IMA J. Numer. Anal. 46(4) (2026), doi:10.1093/imanum/draf055. Confirmed on the landing page (online 22 Jul 2025, issue dated July 2026). Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

PR-preparation consolidation 2026-11-01 (audit-01 protocol finding P2): the additions marked 'PR-preparation' above come from the L1 prior-art review 2026-10-31 and L2 prior-art review 2026-11-01 (topics/bivariate-lanczos-20261031/reviews/), which read the source through WebFetch digests and make no novelty claim; the consolidator did not re-read the source. Any web check made at consolidation is logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.
2026-11-01: orchestrator annotation — the L2 developer (response-recon-01, finding F9) reports that the sentence quoted for LIT?bivariate-lanczos-claude-025 was not found in arXiv v2 of this paper; treat that statement's wording as UNVERIFIED until checked against the published version. The identification of BJ + CGS2-against-all with this paper's multivariate V+A is also UNVERIFIED (paper digest only; code not checked).

2026-11-01 (PR-preparation consolidation, audit-01 protocol finding P2): coverage upgraded from abstract-only to fulltext via WebFetch digests of arXiv 2301.12241 (L1, L2 prior-art reviews); statements 440, 441 added; Appendix B (Algorithms 4–5) named as an unseen gap; conflict with the 2026-11-01 orchestrator annotation on statement 025 recorded, not resolved.
