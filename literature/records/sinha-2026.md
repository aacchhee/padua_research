# sinha-2026 — M. Sinha, Finite-Precision Symmetric Krylov Methods: Exact Rounding Examples, Block Paige Identities, and a Variable-Block Lanczos Model, arXiv:2609.08066 (8 Sep 2026)

- DOI / URL / supplied location: https://arxiv.org/abs/2609.08066 (abstract page fetched 2026-10-31)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: metadata (title, author, date) + abstract confirmed; fulltext NOT inspected. PR-preparation (2026-11-01) from the L1 prior-art review (2026-10-31): fulltext via WebFetch digest read up to §7.1; Theorem 7 NOT seen.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation). PR-preparation additions (2026-11-01): taken from the L1 prior-art review 2026-10-31 (Claude Opus 5.5, effort high; reading through WebFetch digests) by the Claude literature developer (Sonnet 5.5, effort high); the source was not re-read by the consolidator.
- Named gaps requiring future re-reading: Fulltext: block Paige identity statement and the variable-block model (load-bearing for L1/L4). PR-preparation: Theorem 7, Corollary 4 and the meaning of the injection term E^inj in relation (54), to be read in full before the 'injected-start band Lanczos' framing or the growing-block Paige identity PD-T?bivariate-lanczos-claude-103 is called new.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-018 — block Paige identity; block Lanczos with truncation (abstract)

- Verification: **Abstract-checked only** (arXiv abstract page); full text NOT inspected, so the mathematical content stays UNVERIFIED. `LITERATURE` attribution only.
- Statement in faithful paraphrase: The paper includes a block form of Paige's identity, relates its results to the frameworks of Paige and Greenbaum, and analyses block Lanczos with Householder orthogonalization and singular-value truncation. The abstract does not mention several operators.
- Hypotheses and notation: As stated in the abstract; hypotheses beyond the abstract not checked.
- Page / theorem / equation: abstract. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance arXiv abstract page fetched 2026-10-31; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1/L4: block-level Paige statement that might transfer to a 'Lanczos for X with injected vectors from Y' form.

### LIT?bivariate-lanczos-claude-019 — shrinking blocks under deflation (reported)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Reported by the supplying agent: a 'variable-block Lanczos model' in which blocks shrink under rank deflation; nothing on growing blocks or several operators.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: locator not supplied. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/recent_multivariate_NLA.md §1 item 2 (item a); notes/adv_F1_F6_F3.md §1.1(a); attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): The campaign's recurrence has GROWING blocks (degree-k block has k+1 vectors) with structural deflation; the 'shrink' wording was not confirmed by the abstract page.

### LIT?bivariate-lanczos-claude-443 — Cor. 4, relation (54): a block relation with an 'injection' term; no omega-recurrence in the part read

- Verification: **UNVERIFIED** against the original publication; WebFetch digest only (prior-art review). `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Cor. 4, relation (54) (as digested): AV = VT + W H (E_k^inj)^T + F, containing an injection term E^inj. The reviewer found no omega-recurrence in the part read (up to §7.1). Whether E^inj models vectors injected after the start was not resolved; Thm 7 was not seen.
- Hypotheses and notation: Symmetric A, block Lanczos with a variable block model; exact hypotheses not extracted.
- Page / theorem / equation: Cor. 4, eq. (54); read up to §7.1.
- Reading evidence and limitations: Read through WebFetch by the prior-art reviewer: a summarising model answers a prompt against the fetched page, so locators, quotes and displayed formulas are as digested and were NOT checked against page images or verbatim text. The consolidator (2026-11-01) did not re-read the source.
- Relation to campaign claims (no inherited proof status): The most likely source of overlap, per the L1 reviewer, for the injected-start band-Lanczos framing (PD-T?bivariate-lanczos-claude-401) and the growing-block Paige identity (PD-T?bivariate-lanczos-claude-103); also for PD-T?bivariate-lanczos-claude-106 (no omega-recurrence seen). Overlap is neither confirmed nor excluded.

## Search and attribution notes

Plan.md and the inputs write 'Sinha'; the arXiv abstract page gives the author as Mohit Sinha. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

PR-preparation consolidation 2026-11-01 (audit-01 protocol finding P2): the additions marked 'PR-preparation' above come from the L1 prior-art review 2026-10-31 (topics/bivariate-lanczos-20261031/reviews/), which read the source through WebFetch digests and make no novelty claim; the consolidator did not re-read the source. Any web check made at consolidation is logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-11-01 (PR-preparation consolidation, audit-01 protocol finding P2): coverage upgraded from abstract-only to a WebFetch digest read up to §7.1 (L1 prior-art review); statement 443 added; Thm 7, Cor. 4 and E^inj named as required re-reading.
