# amsel-et-al-2026 — N. Amsel et al. (35 authors), Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop, arXiv:2602.05394 (v1 5 Feb 2026; v3 21 Aug 2026)

- DOI / URL / supplied location: https://arxiv.org/abs/2602.05394 (abstract page); PDF text of section 2.6 read via tool digest 2026-10-31. Earlier (Step 0): https://arxiv.org/abs/2602.05394 (abstract page fetched 2026-10-31); html route noted as fetchable in bttb-research record LIT-350 (notes/bttb_repo_numeric_mapping.md §3)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: metadata + abstract confirmed; section 2.6 (Problems 2.15-2.19) read via tool digest in two fetches; the other sections and Problem 4.3 are NOT read. Earlier (Step 0): PROBLEM TEXT not visible.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Problem 4.3 (requested in the Round 3 report §7 item 2); version pin of the text read (v1 versus v3). Earlier (Step 0): Exact wording of Problems 2.19 and 4.3 (requested in reports/Round 3 open problems 2023 2026.md §7 item 2).
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-021 — open problem: Paige's analysis for block Lanczos (reported)

- Verification: **UNVERIFIED**: the abstract page confirms only the report's title/authors/scope (five problem categories); the wording is the supplying agent's account. **Update (online pass): the problem text was read and confirms the content of 021; see statement 232 for the exact paraphrase and for two small corrections.**
- Statement in faithful paraphrase: Problem 2.19 (section 2.6, scribed by T. Chen and A. Greenbaum): extend Paige's analysis of the Lanczos algorithm to the block Lanczos algorithm (with block orthogonalization and deflation); Problem 2.18 asks for Lanczos under general inexact matvecs.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: Problem 2.19, section 2.6; Problem 2.18. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/recent_multivariate_NLA.md §1 item 2 and R1; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1/L4: external statement that the block (single-operator) case is open.

### LIT?bivariate-lanczos-claude-232 — Problem 2.19 text and context (section 2.6) read

- Verification: **arXiv 2602.05394 PDF text of section 2.6 read through two tool fetches that agree; page numbers not available in the extracted text. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Section 2.6, Symmetric Krylov methods in finite precision arithmetic (scribes Tyler Chen and Anne Greenbaum), contains Problems 2.15-2.19: 2.15 conditions under which updated CG/steepest-descent residuals fall below machine precision (or counterexamples); 2.16 whether CG and Lanczos behave alike in finite precision for SPD systems with good implementations; 2.17 how many bits guarantee normwise backward error eps in n or fewer CG steps; 2.18 Lanczos under general inexact matvecs and/or preconditioning; 2.19 extend Paige's finite-precision analysis of Lanczos ([Pai76, Pai80]) to block Lanczos. For 2.19 the text notes that the within-block orthogonalization scheme influences the analysis, so one may either assume an accuracy for that scheme or analyze a standard good algorithm. The preceding discussion says no Paige-style analysis of block Lanczos exists yet, that block Krylov behaviour is complicated even in exact arithmetic (blocks may become rank deficient and need deflation), and hopes for an analysis that would justify block Krylov methods in finite precision. Greenbaum 1989 [Gre89] is cited in the section background; Simonova-Tichy is not cited in the extracted text; no partial results are listed after 2.19; the problem is not attributed to a single proposer and the word 'open' does not occur in it.
- Hypotheses and notation: n/a
- Page / theorem / equation: Section 2.6, Problem 2.19 (and 2.15-2.18); no page markers in the extracted text; the extracted section showed no 'Update on August 20, 2026' note, so the version could not be pinned.
- Reading evidence and limitations: Confirms statement 021 and 003 (Problem 2.19, section 2.6, Chen/Greenbaum scribes, deflation, Paige's [Pai76, Pai80]) and corrects it in one respect: the Step 0 paraphrase said 'with block orthogonalization and deflation' as part of the request; the report mentions deflation only as a source of difficulty in the discussion and gives the within-block orthogonalization choice as an option in the statement.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L1/L4: external statement that the block (single-operator) case is open; the bivariate recurrence has no counterpart here.

## Search and attribution notes

The abstract page lists 35 authors beginning with Noah Amsel; Anne Greenbaum and Tyler Chen are among them. Key chosen as amsel-et-al-2026 to differ from the bttb-research file name (amsel-et-al-2026-simons-open-questions). Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: Problem 2.19 is in section 2.6 (scribes T. Chen and A. Greenbaum); Greenbaum 1989 is cited, Simonova-Tichy is not; deflation appears only in the discussion. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): section 2.6 read; statement 232 added; coverage upgraded.
