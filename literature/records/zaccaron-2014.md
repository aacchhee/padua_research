# zaccaron-2014 — M. Zaccaron, M.Sc. thesis, Universita di Padova, 2014 (title not given in inputs; Lanczos-type bivariate discrete OP generator)

- DOI / URL / supplied location: https://www.math.unipd.it/~alvise/TESI_STUDENTI/ZACCARON/ZACCARON_prefinale.pdf (URL from the inputs; not fetched by me)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: supplied secondary account only (see notes/adv_F1_F6_F3.md §1.1(b); notes/verify_algorithmic_problems.md Problem 3; reports/Padua points research since 2010.md; reports/Open problems verification.md §3 A; code/RESULTS.md); original fulltext NOT inspected; the supplying agents report reading it via WebFetch.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Fulltext: reconcile the two reported tables/figures below.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-028 — no bounds available (author statement)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: The author states that bounds on the loss of orthogonality of the Lanczos-type bivariate recurrence are not available in the present case.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: p. 17. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/adv_F1_F6_F3.md §1.1(b); notes/verify_algorithmic_problems.md Problem 3; reports/Open problems verification.md §3 A; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1: author-stated gap; evidence the question is open as of 2014.

### LIT?bivariate-lanczos-claude-029 — measured loss of orthogonality (two inconsistent reports)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Report A (notes/verify_algorithmic_problems.md): Table 2.1, ||Q^T Q - I||_inf = 6.7e-16 (degree 5), 1.2e-13 (10), 9.8e-9 (20), 6.1e-3 (30), 0.38 (40); the repair is full reorthogonalization ('Method 2', O(M N^2)) giving about 1e-15 up to degree 60; basic cost O(16 M n^3/6). Report B (notes/adv_F1_F6_F3.md): Table 2.1 value 0.499 at degree 60 (M = 3721, N = 1891), remedy 'twice is enough'.
- Hypotheses and notation: Plain truncated recurrence, uniform data, unspecified node sets; not resolved from the supplied accounts.
- Page / theorem / equation: Table 2.1; section 2.4. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/verify_algorithmic_problems.md Problem 3 (A); notes/adv_F1_F6_F3.md §1.1(b) (B); reports/Open problems verification.md §2 row 3 repeats 0.38 at degree 40; reports/Padua points research since 2010.md says 'twice is enough'; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1 benchmark datum. INCONSISTENCY between supplying notes (degree/value and remedy) is flagged for the fulltext reader, not resolved.

## Search and attribution notes

reports/Padua points research since 2010.md notes that the thesis's refs [38]/[39] could not be confirmed to be the seed and HL. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.
