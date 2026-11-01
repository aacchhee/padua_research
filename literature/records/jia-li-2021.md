# jia-li-2021 — Z. Jia, H. Li, The joint bidiagonalization process with partial reorthogonalization, Numer. Algorithms (2021), doi:10.1007/s11075-020-01064-8, arXiv:2001.04402

- DOI / URL / supplied location: https://arxiv.org/abs/2001.04402 (abstract page fetched 2026-10-31); doi:10.1007/s11075-020-01064-8
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: metadata (title, authors, DOI) + abstract confirmed on the arXiv page; journal volume/pages not shown on that page; fulltext NOT inspected. PR-preparation (2026-11-01) from the L2 prior-art review (2026-11-01): fulltext via WebFetch digest of arXiv 2001.04402 (Def. 3.1, Thms 3.1/3.3/3.4, JBDPRO).
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation). PR-preparation additions (2026-11-01): taken from the L2 prior-art review 2026-11-01 (Claude Opus 5.5, effort high; reading through WebFetch digests) by the Claude literature developer (Sonnet 5.5, effort high); the source was not re-read by the consolidator.
- Named gaps requiring future re-reading: Fulltext, as requested by notes/adv_F1_F6_F3.md §4: how much of the semi-orthogonality proof transfers to two operators. PR-preparation: Proofs; how much of the semi-orthogonality proof transfers to two commuting operators (still open); Thm 3.1 content was not extracted; Simon LAA 61 Thm 5 / Lemma 4 via Jia–Li remains secondary.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-012 — partial reorthogonalization for a matrix pair (abstract)

- Verification: **Abstract-checked only** (arXiv abstract page); full text NOT inspected, so the mathematical content stays UNVERIFIED. `LITERATURE` attribution only.
- Statement in faithful paraphrase: The joint bidiagonalization (JBD) process for a matrix pair (for the GSVD) loses orthogonality among its Lanczos vectors; the authors propose a semiorthogonalization strategy, show by error analysis that rounding errors then do not affect convergence of the computed quantities, and derive JBDPRO, which reorthogonalizes only when needed.
- Hypotheses and notation: As stated in the abstract; hypotheses beyond the abstract not checked.
- Page / theorem / equation: abstract. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance arXiv abstract page fetched 2026-10-31; also notes/adv_F1_F6_F3.md §1.1(c), §4; reports/Round 3 open problems 2023 2026.md §7 item 3; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L2: the closest 'two-matrix' semi-orthogonality theorem; a process with two matrices but a single Krylov-type recursion, not two commuting operators with growing blocks.

### LIT?bivariate-lanczos-claude-444 — Def. 3.1 and Thms 3.3/3.4: semi-orthogonality level and O(eps) accuracy of the projected bidiagonal

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Def. 3.1 sets the semi-orthogonality level omega_0 = sqrt(eps/(2k+1)). Local orthogonality is assumed in (2.11)–(2.12). Thms 3.3 and 3.4 give B_k = M_k^T Q_A N_k + O(eps) and B-hat_k to within O(‖B-hat_k^{-1}‖ eps) (as digested; Thm 3.1 is listed in the review but its content was not extracted).
- Hypotheses and notation: Joint bidiagonalization of a matrix pair, one operator QQ^T on the stacked pair; floating-point model as in the paper.
- Page / theorem / equation: Def. 3.1; Thms 3.1, 3.3, 3.4; (2.11)–(2.12).
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source.
- Relation to campaign claims (no inherited proof status): Closest predecessor of the 2D Simon-type theorem for the formed section (PD-T?bivariate-lanczos-claude-201), alongside Simon 1984; the L2 reviewer says to cite it as such. The hypotheses have the same shape (semi-orthogonality plus local orthogonality gives O(u) projected-section accuracy).

### LIT?bivariate-lanczos-claude-445 — JBDPRO: coupled Larsen-type recurrences, eta = eps^{3/4}, 55–81% of the full-reorthogonalization time

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: JBDPRO uses Larsen-type coupled recurrences, eta = eps^{3/4}, and runs at 55–81% of the full-reorthogonalization time. The process is driven by one operator (QQ^T on the stacked pair (A; L)) with two coupled bidiagonalizations; it has no commuting operators, no growing blocks and no implicit sections.
- Hypotheses and notation: As above.
- Page / theorem / equation: JBDPRO experiments (as digested; locator not recorded).
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source.
- Relation to campaign claims (no inherited proof status): Cost comparator for PRO-2D at 0.16–0.71 of CGS2-against-all (PD-T?bivariate-lanczos-claude-207): same range as Simon (about 0.2) and Jia–Li (0.55–0.81); a measurement in a new setting, not a new kind of result (L2 review). The one-operator, no-growing-block scope marks the difference from the campaign setting.

## Search and attribution notes

Plan.md cites it as Numer. Algorithms 2021; the abstract page confirms DOI 10.1007/s11075-020-01064-8 but not the volume/pages. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

PR-preparation consolidation 2026-11-01 (audit-01 protocol finding P2): the additions marked 'PR-preparation' above come from the L2 prior-art review 2026-11-01 (topics/bivariate-lanczos-20261031/reviews/), which read the source through WebFetch digests and make no novelty claim; the consolidator did not re-read the source. Any web check made at consolidation is logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-11-01 (PR-preparation consolidation, audit-01 protocol finding P2): coverage upgraded from abstract-only to fulltext via WebFetch digest (L2 prior-art review); statements 444, 445 added.
