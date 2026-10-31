# paige-1971 — C. C. Paige, The computation of eigenvalues and eigenvectors of very large sparse matrices, PhD thesis, University of London, 1971 (title, institution and year now confirmed by the thesis PDF itself and by reference [10] of Simon 1984)

- DOI / URL / supplied location: https://www.cs.mcgill.ca/~chris/pubClassic/PaigeThesis.pdf (author's page; LaTeX re-typesetting with a 2012 addendum; read 2026-10-31); also listed as ProQuest docview 1794120404 (search hit, not fetched). Earlier (Step 0): no URL
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: exact pages: front matter, table of contents and text through section 5.5 (p. 66) via tool digest; Chapters 6-10 (including 7.x and 8.x, where the finite-precision Lanczos analysis lives) NOT reached. Locators are as digested. Earlier (Step 0): not read; named in plan.md L1 predecessors and the task brief only; the supplied inputs never cite it.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Chapters 6-8, especially sections 7.2-7.4 and 8.4-8.7 (loss of orthogonality in algorithm A2, proof of convergence), and the full-precision theorem statements. The tool's extracted text stopped inside Chapter 5; a copy read in another way is needed. Earlier (Step 0): Whole source; pending-reference. Do not import any content until a copy is inspected.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

Step 0: none extracted (no supplied input attributes a specific result to this source). Online-pass statements follow; they are digests of the thesis text and remain UNVERIFIED against page images.

### LIT?bivariate-lanczos-claude-201 — Thesis layout: where the finite-precision Lanczos analysis sits

- Verification: **Table of contents and pp. 1-66 read via tool digest; chapters 6-10 NOT reached. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: The thesis (University of London, April 1971; the PDF is a LaTeX re-typesetting with a 2012 addendum by I. Panayotov, per the digest) has ten chapters. Chapter 3 treats generalized Hessenberg processes (3.2 error analysis, 3.3 re-orthogonalization); Chapter 6 is the symmetric Lanczos process with re-orthogonalization; Chapter 7 the process without re-orthogonalization (7.3 failure of the obvious algorithm A1, 7.4 analysis of the economical algorithm A2); Chapter 8 'Error behaviour and convergence' (8.4 loss of orthogonality in A2, 8.5 the concept of convergence of A2, 8.6 lower bounds, 8.7 a proof of convergence). Paige (2019) cites thesis section 8.7 for the growth of Ritz-value error bounds (see paige-1980-lanczos record, secondary).
- Hypotheses and notation: Single symmetric matrix, single start vector, rounding errors; the 1D theory.
- Page / theorem / equation: Table of contents (digest); thesis pp. 17, 28-29, 42-66 for the items in the next statement.
- Reading evidence and limitations: Table of contents read; the extracted text ended inside Chapter 5 (p. 66), so Sections 7.x and 8.x, where the loss-of-orthogonality theory lives, were not read. The same PDF is listed as reference [10] in Simon (Math. Comp. 42, 1984; see simon-1984-mathcomp).  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L1-Q1: locates the original single-operator analysis (sections 8.4, 8.7) that a bivariate analogue must reproduce; no content of those sections is imported.

### LIT?bivariate-lanczos-claude-202 — Generalized Hessenberg process: perturbed local relation and loss-of-orthogonality formula

- Verification: **Tool digest of thesis pp. 17-29; formulas not checked against page images. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Thesis Theorem 2.1 (p. 17, section 2.2) bounds ratios of products of (1+epsilon) factors under a smallness condition on the number of operations times the unit roundoff; it is the basic tool of the later analyses. In section 3.2 (p. 28, eqs. 3.12-3.13) a computed generalized Hessenberg step is written A V = V H + E + dV with dV collecting the rounding errors of the step, the Lanczos case being a special case that needs a separate, harder analysis deferred to later chapters. Eqs. 3.14-3.16 (p. 29) express the departure from orthogonality through the rounding-error term multiplied by the inverse of the (augmented) Hessenberg matrix, so errors made early can be amplified. Chapters 4-5 (pp. 42-66) are exact-arithmetic convergence and eigenvalue-interval results (eqs. 4.11, 4.12, 4.23, 5.2-5.5); the thesis remarks that rounding errors can make practical results exceed those bounds (p. 50).
- Hypotheses and notation: General (non-symmetric allowed) Hessenberg processes for 3.2; exact arithmetic for Chapters 4-5.
- Page / theorem / equation: Theorem 2.1 p. 17; eqs. 3.12-3.16 pp. 28-29; eqs. 4.11, 4.12, 4.23 pp. 42-50; eqs. 5.2-5.5 pp. 53-54 (all as digested).
- Reading evidence and limitations: Digest only; I did not see the formulas. The statements show that the 'local relation + inverse-of-H amplification' pattern predates 1976, and that it is formulated for general Hessenberg processes (not only symmetric ones).  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L1-Q1/R02: the amplification-by-an-inverse formula is the one-operator ancestor of the measured per-node propagator amplification; any claim of parallelism remains the campaign's to prove.

## Search and attribution notes

No statement extracted: the inputs contain nothing that attributes a specific result to this item. Listed so that the 'Paige 1971/1976/1980' chain of plan.md has a stable key. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: the PDF at the author's page was fetched (log rows 13-16 of the search-log section). The earlier note 'no supplied input cites it' stays true of the inputs; the thesis is nevertheless cited by Simon 1984 [10], Paige 2019 and Meurant-Strakos as the origin of the rounding-error analysis. The tool text was 85,717 characters and ended at p. 66. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): thesis located on the author's McGill page; table of contents and pp. 1-66 read via tool digest; statements 201-202 added; coverage upgraded from 'not read' to 'exact pages (partial)'.
