# freund-2000 — R. W. Freund, Band Lanczos method, in: Bai, Demmel, Dongarra, Ruhe, van der Vorst (eds.), Templates for the Solution of Algebraic Eigenvalue Problems, SIAM 2000, section 4.12 (locator as given by the inputs: netlib etemplates node131-135)

- DOI / URL / supplied location: netlib etemplates node131-135 (as cited in notes/adv_F1_F6_F3.md §1.1(a); not fetched by me)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: supplied secondary account only (see notes/adv_F1_F6_F3.md §1.1(a)); original fulltext NOT inspected.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Fulltext of the Templates section.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-014 — band Lanczos scope and absence of finite-precision analysis

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status.
- Statement in faithful paraphrase: Band Lanczos works with ONE square matrix and a block of starting vectors, using deflation and look-ahead. The inputs report that the Templates section has no loss-of-orthogonality or reorthogonalization analysis; the only roundoff remark is that the Lanczos matrix may become slightly indefinite (node 135).
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: section 4.12; node131-135 (node 135 for the roundoff remark). Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/adv_F1_F6_F3.md §1.1(a); attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L4-Q1: transfer question. The inputs argue HL is NOT a special case: the span {x^i y^j w} as band Lanczos for A = X needs the monomial start block [w, Yw, Y^2 w, ...] (ill-conditioned, x-degree rather than total-degree order).

## Search and attribution notes

INPUT INCONSISTENCY: notes/recent_multivariate_NLA.md R1(c) attributes band Lanczos to 'Bai-Day-Demmel-Dongarra, Math. Comp. 2000', which matches none of the other citations in the inputs (Templates: Bai-Demmel-Dongarra-Ruhe-van der Vorst, SIAM 2000; ABLE: Bai-Day-Ye SIMAX 1999; ABFH: Math. Comp. 69 (2000)). Treated as a probable conflation; UNVERIFIED. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.
