# liu-narayan-2023 — Zexin Liu, A. Narayan, A Stieltjes algorithm for generating multivariate orthogonal polynomials, SIAM J. Sci. Comput. 45(3) (2023) A1125–A1147, doi:10.1137/22M1477131, arXiv:2202.04843 (first author corrected from 'Y. Liu' by the L1 prior-art review)

- DOI / URL / supplied location: doi:10.1137/22M1477131; arXiv 2202.04843 (as cited in notes/verify_algorithmic_problems.md); not fetched by me
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: supplied secondary account only (see notes/verify_algorithmic_problems.md Problems 3 and 4); original fulltext NOT inspected. PR-preparation (2026-11-01) from the L1 prior-art review (2026-10-31): fulltext via WebFetch digests (arXiv PDF ×3, ar5iv ×1; §§1–3, 5.2 and 6 text; figures not inspected); L2 prior-art review (2026-11-01): par.nsf.gov v2 digest (commuting conditions (6a–6c)).
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation). PR-preparation additions (2026-11-01): taken from the L1 prior-art review 2026-10-31 and L2 prior-art review 2026-11-01 (Claude Opus 5.5, effort high; reading through WebFetch digests) by the Claude literature developer (Sonnet 5.5, effort high); the source was not re-read by the consolidator.
- Named gaps requiring future re-reading: Fulltext. PR-preparation: Figures and error plots of §6; equation numbering (the L1 review cites Eqs. 9, 20, 24–26, 28–30; the Step 0 statement 031 cites eq. 22, eq. 35, §5.2.6; arXiv version versus published version UNRESOLVED); verbatim check.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-031 — any-d truncated Stieltjes from moments; origin of the non-convex step

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: The multivariate Stieltjes procedure is a truncated block three-term procedure in any dimension working from moments by quadrature, with no complexity analysis, citing neither HL nor the seed. The non-convex (weighted orthogonal Procrustes) step arises from fitting each direction separately (section 5.2.6), not from the canonical form imposed afterwards by one symmetric eigendecomposition (section 3.2).
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: sections 3.2, 5.2.1-5.2.7, eq. 22, eq. 35. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/verify_algorithmic_problems.md Problem 3 and Problem 4; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): P4 (deferred) and L1 background; the 'trivial' verdict for P4 is the supplying agent's, UNVERIFIED.

### LIT?bivariate-lanczos-claude-435 — Thm 3.1: stacked d three-term relations are overdetermined but consistent

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Thm 3.1, eq. (9): the next-degree polynomial vector p_{n+1} is obtained by stacking the d coordinate three-term relations. The proof states that, although the stacked system is overdetermined, it is consistent, and solves it by multiplying with B^T_{n+1}, with Lambda_{n+1} diagonal (notation as digested).
- Hypotheses and notation: Multivariate polynomials with a positive functional; exact hypotheses not extracted.
- Page / theorem / equation: Thm 3.1, eq. (9) (as digested).
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source.
- Relation to campaign claims (no inherited proof status): Algebraic frame of PD-T?bivariate-lanczos-claude-108: a consistent overdetermined stacked system with a left inverse is published (together with xu-2017-survey eq. (2.14) and olver-townsend-vasil-2019). The reviewer found no comparison of left inverses and no statement that the choice decides floating-point stability.

### LIT?bivariate-lanczos-claude-436 — multivariate Stieltjes procedure: all-coordinate block three-term truncation with SVD/eigen completion; qualitative tests on non-tensor domains

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: The multivariate Stieltjes (MS) procedure forms x_i p_n - A_{n+1,i} p_n - B^T_{n,i} p_{n-1} for every coordinate i (Eq. 24), with A from S_{n,i} (Eq. 25) and B from an eigendecomposition of T_{n,i,i} (Eq. 26), a truncated SVD (Eq. 20) and mixed moments (Eqs. 28–30, d = 2); p_{n+1} follows from all relations jointly (Eq. 9). It was run on empirical discrete measures (M = 10^8, §6.2) on non-tensor domains (annulus, region between spirals, torus, square with hole, Madagascar), with only qualitative comparison to moment methods: on the annulus MS performs better for large degrees; on the square with a hole the error is notably increased. No orthogonality numbers are given in the text and there is no comparison with a one-relation Lanczos/HL recurrence (HL and BJ are not cited). Per the L2 digest of v2 (par.nsf.gov 10435784), the commuting conditions (6a–6c) are imposed as algorithm constraints and checked only through orthogonality, not used as an error indicator.
- Hypotheses and notation: Discrete and continuous measures; as digested.
- Page / theorem / equation: Eqs. 9, 20, 24–26, 28–30; §6.2 (as digested; numbering differs from statement 031).
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source.
- Relation to campaign claims (no inherited proof status): Closest algorithmic predecessor of the two-relation remedy (IDEA?bivariate-lanczos-claude-111; PD-T?bivariate-lanczos-claude-206): the block three-term truncation using all coordinate relations with an SVD/eigen completion is published as an algorithm; equivalence of the completions with the campaign's is not checked. The comparative stability statement at equal truncation is not found here. Also relevant to PD-T?bivariate-lanczos-claude-208 (commutator as indicator: not used in this source).

## Search and attribution notes

No additional attribution notes beyond the statements above. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

PR-preparation consolidation 2026-11-01 (audit-01 protocol finding P2): the additions marked 'PR-preparation' above come from the L1 prior-art review 2026-10-31 and L2 prior-art review 2026-11-01 (topics/bivariate-lanczos-20261031/reviews/), which read the source through WebFetch digests and make no novelty claim; the consolidator did not re-read the source. Any web check made at consolidation is logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-11-01 (PR-preparation consolidation, audit-01 protocol finding P2): first author corrected from 'Y. Liu' to Zexin Liu and title/pages added (L1 prior-art review); coverage upgraded to fulltext via WebFetch digests; statements 435, 436 added; equation-number discrepancy with statement 031 recorded, not resolved.
