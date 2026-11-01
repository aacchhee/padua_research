# hokanson-2020 — J. M. Hokanson, Multivariate rational approximation using a stabilized Sanathanan–Koerner iteration, arXiv:2009.10803 (22 Sep 2020); title corrected by the L1 prior-art review (the Step 0 record's 'Multivariate Vandermonde with Arnoldi' was wrong)

- DOI / URL / supplied location: https://arxiv.org/pdf/2009.10803 (as cited in reports/Padua points research since 2010.md)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: supplied secondary account only (see reports/Padua points research since 2010.md §'What the V+A papers omit'); original fulltext NOT inspected; Algorithm 2.1 locator from the inputs. PR-preparation (2026-11-01) from the L1 (2026-10-31) and L2 (2026-11-01) prior-art reviews: fulltext via WebFetch digests of the arXiv abs/PDF (§2, §2.1, Alg. 2.1).
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation). PR-preparation additions (2026-11-01): taken from the L1 prior-art review 2026-10-31 and L2 prior-art review 2026-11-01 (Claude Opus 5.5, effort high; reading through WebFetch digests) by the Claude literature developer (Sonnet 5.5, effort high); the source was not re-read by the consolidator.
- Named gaps requiring future re-reading: Fulltext. PR-preparation: Verbatim check of Alg. 2.1 and the selection rule (text and algorithm differ, see statement 438); the multivariate source Austin et al. is now austin-et-al-2021.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT-098 (LIT?bivariate-lanczos-claude-033) — full-orthogonalization multivariate V+A

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Builds each column by multiplying a previous column by one coordinate, orthogonalizes by two-pass classical Gram-Schmidt against ALL previous columns at cost O(M N^2), and notes that many orderings do not satisfy the required span property; reported to be one fixed instance of the seed's ordering scheme.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: Alg. 2.1. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance reports/Padua points research since 2010.md (multivariate V+A paragraph and 'What the V+A papers omit'); attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L2 cost comparator.

### LIT-280 (LIT?bivariate-lanczos-claude-437) — §2: the multivariate monomial-ordered basis is not a Krylov subspace; Alg. 2.1 orthogonalizes twice against all previous columns

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: §2 (as digested): the basis no longer corresponds to a Krylov subspace in the multivariate case. Alg. 2.1 builds each column by multiplying a previous column by one coordinate and orthogonalizes by classical Gram–Schmidt twice against all previous columns.
- Hypotheses and notation: Multivariate Vandermonde-with-Arnoldi inside a rational-approximation iteration.
- Page / theorem / equation: §2; Alg. 2.1.
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source.
- Relation to campaign claims (no inherited proof status): An informal statement weaker than the obstruction PD-T?bivariate-lanczos-claude-401 (no commuting-operator qualifier, no fixed number of starts, no proof). Confirms the full-orthogonalization cost comparator of statement 033.

### LIT-281 (LIT?bivariate-lanczos-claude-438) — §2.1 selection rule 'smallest k' for the parent column; no rounding-error claims

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: §2.1, Alg. 2.1 (as digested): the parent of the new column is chosen by the smallest-index rule, the smallest k such that I[k] + e_j = I[l+1]; the text and the algorithm differ (l versus l+1). The text remarks that many orderings do not satisfy this constraint, which concerns the exact-arithmetic span property. The paper makes no claim about rounding error, the accuracy of the recurrence matrices, or the span in floating point. The multivariate extension is credited to Austin et al. (see austin-et-al-2021).
- Hypotheses and notation: Multi-index ordering I; exact conventions not extracted.
- Page / theorem / equation: §2.1, Alg. 2.1.
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source. The L2 reviewer's mapping, that with the within-degree order x^{t-j} y^j this rule picks the campaign's 'dev' (BJ) selection so that 'fullcgs2 + dev' coincides with Alg. 2.1 and with ZN's V+A, is the reviewer's reading, to be checked by the developer, and is NOT verified.
- Relation to campaign claims (no inherited proof status): Context for the selection-rule statements PD-T?bivariate-lanczos-claude-205, PD-T?bivariate-lanczos-claude-206 and PD-N?bivariate-lanczos-claude-201/-203: the selection is fixed by structure in this source with no numerical-effect analysis; no stability claim contradicts the span-drift statements.

## Search and attribution notes

No additional attribution notes beyond the statements above. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

PR-preparation consolidation 2026-11-01 (audit-01 protocol finding P2): the additions marked 'PR-preparation' above come from the L1 prior-art review 2026-10-31 and L2 prior-art review 2026-11-01 (topics/bivariate-lanczos-20261031/reviews/), which read the source through WebFetch digests and make no novelty claim; the consolidator did not re-read the source. Any web check made at consolidation is logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-11-01 (PR-preparation consolidation, audit-01 protocol finding P2): title corrected (it is not 'Multivariate Vandermonde with Arnoldi'); coverage upgraded from 'secondary account' to fulltext via WebFetch digests; statements 437, 438 added; the 'dev'/Alg. 2.1 selection mapping recorded as unverified.
