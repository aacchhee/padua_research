# harris-simanek-2021 — Harris, Simanek, Interpolation and cubature for rectangular sets of nodes, Proc. Amer. Math. Soc. 149 (2021) 3485-3497, doi:10.1090/proc/15414 (citation as in the Codex branch; first names not in the inputs)

- DOI / URL / supplied location: https://doi.org/10.1090/proc/15414 (as in the Codex record; not fetched by me)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: supplied secondary account only (see code/RESULTS.md 2026-10-31 'Ingestion'; reports/Open problems verification.md §4; reports/Round 3 open problems 2023 2026.md §4.3); original fulltext NOT inspected.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Fulltext.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.
- Shared key: the Codex branch `codex/charter-unisolvence-20261031` has a record under this key; merge into one record per source at PR preparation (this record uses the `bivariate-lanczos-claude` provisional namespace only).

## Extracted published statements

### LIT?bivariate-lanczos-claude-070 — rectangular checkerboard sets as exact benchmarks

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Reported: every rectangular checkerboard set of ordered real nodes gives explicit H_x, H_y with at most 3 nonzeros per column (at most 2 if one side is symmetric), checked numerically by the supplying agent (`harris_simanek_check.py`); these are better test cases than Padua alone because they can be badly conditioned.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: no locator beyond Thm 1 pp. 3488-3489 in the Codex record. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance reports/Open problems verification.md §4 'Problem 2 -> benchmark only'; code/RESULTS.md; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): Benchmark family for L1/L5 (plan.md 'Benchmarks'); a reported check, not rerun here.

### LIT?bivariate-lanczos-claude-071 — unisolvence is not field-independent (reported correction)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Reported correction: the unisolvence result needs ordered nodes even over Q; counterexample X = (0,1,2), Y = (0,1,3,2) gives rank 5/6 over Q and over F_101. Conjecture (open): unisolvent iff the two alternation functionals are quasi-definite.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: no locator. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance reports/Round 3 open problems 2023 2026.md §4.3; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): Finite-field unisolvence is out of scope for this campaign (kept for completeness).

## Search and attribution notes

Shared key with the Codex branch; merge at PR preparation. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.
