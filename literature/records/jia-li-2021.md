# jia-li-2021 — Z. Jia, H. Li, The joint bidiagonalization process with partial reorthogonalization, Numer. Algorithms (2021), doi:10.1007/s11075-020-01064-8, arXiv:2001.04402

- DOI / URL / supplied location: https://arxiv.org/abs/2001.04402 (abstract page fetched 2026-10-31); doi:10.1007/s11075-020-01064-8
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: metadata (title, authors, DOI) + abstract confirmed on the arXiv page; journal volume/pages not shown on that page; fulltext NOT inspected.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Fulltext, as requested by notes/adv_F1_F6_F3.md §4: how much of the semi-orthogonality proof transfers to two operators.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-012 — partial reorthogonalization for a matrix pair (abstract)

- Verification: **Abstract-checked only** (arXiv abstract page); full text NOT inspected, so the mathematical content stays UNVERIFIED. `LITERATURE` attribution only.
- Statement in faithful paraphrase: The joint bidiagonalization (JBD) process for a matrix pair (for the GSVD) loses orthogonality among its Lanczos vectors; the authors propose a semiorthogonalization strategy, show by error analysis that rounding errors then do not affect convergence of the computed quantities, and derive JBDPRO, which reorthogonalizes only when needed.
- Hypotheses and notation: As stated in the abstract; hypotheses beyond the abstract not checked.
- Page / theorem / equation: abstract. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance arXiv abstract page fetched 2026-10-31; also notes/adv_F1_F6_F3.md §1.1(c), §4; reports/Round 3 open problems 2023 2026.md §7 item 3; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L2: the closest 'two-matrix' semi-orthogonality theorem; a process with two matrices but a single Krylov-type recursion, not two commuting operators with growing blocks.

## Search and attribution notes

Plan.md cites it as Numer. Algorithms 2021; the abstract page confirms DOI 10.1007/s11075-020-01064-8 but not the volume/pages. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.
