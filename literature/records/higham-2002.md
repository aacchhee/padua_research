# higham-2002 — N. J. Higham, Accuracy and Stability of Numerical Algorithms, SIAM (edition/year not stated in inputs; 2nd ed. 2002 assumed), chapters 18-19, section 19.6

- DOI / URL / supplied location: no URL
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: supplied secondary account only (see notes/adv_F1_F6_F3.md §2.2; notes/verify_algorithmic_problems.md Problem 1(e)); original fulltext NOT inspected.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Exact lemma/theorem numbers and edition.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT-111 (LIT?bivariate-lanczos-claude-046) — rotation/Householder error accumulation

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Reported: an orthogonal-similarity sequence of Givens rotations yields a computed result that is an exact unitary similarity of D + E with ||E|| growing with the number of rotations per entry times u; Householder/CGS2 accumulate roughly sqrt(M) statistically. The supplying agent uses this to explain the measured Givens-IEP deficit (error ~ M vs ~ sqrt(M)) as an inference.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: chapters 18-19; section 19.6 (from memory in notes/verify_algorithmic_problems.md). Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/adv_F1_F6_F3.md §2.2 last bullet ([inference]); notes/verify_algorithmic_problems.md Problem 1(e) ([memory]); attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L5-Q1 explanation to be TESTED (slope claim), not inherited; unit-roundoff constants not supplied.

## Search and attribution notes

No additional attribution notes beyond the statements above. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.
