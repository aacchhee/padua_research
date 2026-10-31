# vanbarel-humet-sorber-2014 — M. Van Barel, M. Humet, L. Sorber, Approximating optimal point configurations for multivariate polynomial interpolation, ETNA 42 (2014) 41-63 (title as given in notes/ingest_humet_thesis.md chapter 6, which writes 'multivariate interpolation'; chapter 6 of Humet 2019)

- DOI / URL / supplied location: https://etna.ricam.oeaw.ac.at/vol.42.2014/pp41-63.dir/pp41-63.pdf (URL as in reports/Padua points research since 2010.md; not fetched by me)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: supplied secondary account only (see notes/ingest_humet_thesis.md Ch. 6 and §2-§3; reports/Padua points research since 2010.md; notes/verify_algorithmic_problems.md Problem 1(h)); original fulltext NOT inspected.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Fulltext (pivot rule and cost statements).
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-066 — published pivot-choice heuristic of the Givens/Householder IEP

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Section 4 (p. 133): there is freedom in which pivot builds the Givens/Householder transformation; the authors take the vector of highest 2-norm 'since this seemed the most accurate in numerical tests' (footnote 7: similar to optimal pivoting in Gaussian elimination); the same rule is used when evaluating OPs by recurrence. 'If the pivot elements in H_k are positive, the process has a unique outcome.'
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: section 4, p. 133, footnote 7. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/ingest_humet_thesis.md Ch. 6 'IEP description'; notes/adv_F1_F6_F3.md §2.3; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L5-Q1 closest predecessor of the 'larger redundant pivot' rule; the inputs MEASURE it to be catastrophic on non-unisolvent prefixes (7e-4 on Padua n = 20, random weights) -- a reported measurement only.

### LIT?bivariate-lanczos-claude-067 — cost and stability scope (reported)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Cost O(k^2) flops per added point (p. 136) with evaluation of the new basis functions O(K k^2) per step; Householder variant faster for large problems via BLAS-2 (p. 133). 'A stability analysis of these updates is not covered' (p. 137) refers to low-rank updates of the Lagrange matrix L, NOT to the IEP; Greedy Update keeps the basis fixed and performs no (H_x, H_y) downdate (p. 138).
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: pp. 133, 136-139. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/ingest_humet_thesis.md Ch. 6; correction stated in reports/Round 3 open problems 2023 2026.md §2 'Humet's thesis' bullet; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): CORRECTION to round 2 preserved: the 'not covered' quotation was earlier read as being about IEP updates. L5/F3 background.

### LIT?bivariate-lanczos-claude-068 — failure mode when the set is non-unisolvent (reported)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: If a greedy step makes the set non-unisolvent (for example collinear points on the disk) the method fails; the authors believe this has probability zero for random choices (p. 135); no zero-pivot handling is described.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: p. 135. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/ingest_humet_thesis.md §2 table row 'Zero pivots'; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L5: the same non-unisolvent-prefix mechanism that the inputs blame for the pivot catastrophe; stated here as a limitation of the source.

## Search and attribution notes

No additional attribution notes beyond the statements above. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.
