# paige-1976 — C. C. Paige, Error analysis of the Lanczos algorithm for tridiagonalizing a symmetric matrix, J. Inst. Math. Appl. 18(3) (1976) 341-349, doi:10.1093/imamat/18.3.341 (title, venue and pages now confirmed by Crossref and by reference [12] of Simon 1984)

- DOI / URL / supplied location: https://www.cs.mcgill.ca/~chris/pubClassic/76JIMA001.pdf (author's scan; no text layer, tool returned binary data); doi:10.1093/imamat/18.3.341. Earlier (Step 0): no URL in inputs
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: metadata (Crossref) + secondary accounts of the theorems (Meurant-Strakos 2006, Paige 2019, Carson-Demmel 2014, Simon 1984 reference list); the original is NOT read. Earlier (Step 0): supplied secondary account only.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Whole source: the scanned PDF exists but was not machine-readable here. Needed: Paige's own theorem numbers, hypotheses and constants for the local relations and the orthogonality identity, and the 1976 versus 1980 split of results. Earlier (Step 0): Whole source; pending-reference.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT-068 (LIT?bivariate-lanczos-claude-003) — reference point for block extension

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status. **Update (online pass): the text of Problem 2.19 was read and confirms that it cites [Pai76, Pai80] as the baseline; see amsel-et-al-2026 (statement LIT?bivariate-lanczos-claude-232).**
- Statement in faithful paraphrase: The Simons-workshop report's Problem 2.19 asks to extend 'Paige's analysis [Pai76, Pai80]' of the Lanczos algorithm to block Lanczos (with deflation); the 1D theory is described by the inputs as complete.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: arXiv 2602.05394, Problem 2.19, section 2.6 (as reported in notes/recent_multivariate_NLA.md §1 item 2); the abstract page fetched by me does not show the problem text. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/recent_multivariate_NLA.md §1 item 2 and R1 'What is known'; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1/L4: defines what 'a Paige-type theory' must generalise; the block case is itself reported open, hence two operators a fortiori.

### LIT-207 (LIT?bivariate-lanczos-claude-203) — Local perturbed Lanczos relations (secondary account of the standard form)

- Verification: **NOT read in the original: the author's scan (cs.mcgill.ca/~chris/pubClassic/76JIMA001.pdf) has no text layer (WebFetch returned binary data). Statement is the form given by Meurant-Strakos (2006) as Paige's, corroborated by Paige (2019) and Carson-Demmel (2014). UNVERIFIED against the 1976 paper.**
- Statement in faithful paraphrase: For the computed Lanczos quantities V_k, T_k (diagonal alpha, off-diagonal eta), the relation A V_k = V_k T_k + eta_{k+1} v_{k+1} e_k^T + dV_k holds, with: |v_{j+1}^T v_{j+1} - 1| <= eps0; ‖dv_j‖ <= eps1 ‖A‖; eta_{j+1} |v_j^T v_{j+1}| <= 2 eps0 ‖A‖; and a bound of the type 4j(3 eps0 + eps1)‖A‖^2 on the defect of eta_j^2 + alpha_j^2 + eta_{j+1}^2 versus ‖A v_j‖^2. Here eps0 = 2(n+4) u < 1/12 and eps1 = 2(7 + m_A beta) u, with m_A the maximal number of nonzeros per row of A (Meurant-Strakos; constants as digested).
- Hypotheses and notation: One symmetric A, one starting vector, floating point with unit roundoff u, no reorthogonalization, computed beta nonzero.
- Page / theorem / equation: Meurant-Strakos, Acta Numerica 15 (2006), Theorem 4.1 (~pp. 502-503); Paige (2019, SIMAX) eq. (7.1) cites the 1976 paper for the perturbed recurrence; Carson-Demmel (UCB/EECS-2014-165) Theorem 4.1, eqs. (4.2)-(4.5), say theirs is 'in the same form as Paige's'.
- Reading evidence and limitations: Three independent secondary accounts agree on the structure; none is the original. Constants are the secondary authors' and may differ from Paige's (Carson-Demmel say theirs differ).  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L1-Q1: the 1D computed local relation against which the BJ/HL bivariate local relations (two relations, X Q and Y Q) are to be written; the statement says nothing about two operators.

### LIT-208 (LIT?bivariate-lanczos-claude-204) — Orthogonality identity for the strictly upper part of V^T V (secondary account)

- Verification: **Original NOT read. Secondary: Meurant-Strakos Theorem 4.2 (attributes it to Paige 1971, 1976); Carson-Demmel eqs. (4.6)-(4.8). UNVERIFIED against Paige.**
- Statement in faithful paraphrase: Let R_k be the strictly upper triangular part of V_k^T V_k. Then T_k R_k - R_k T_k = eta_{k+1} V_k^T v_{k+1} e_k^T + dR_k, where dR_k is upper triangular and its entries are bounded in terms of eps0, eps1 (Frobenius norm of order k times u in the Carson-Demmel version, eq. (4.11)). Paige (2019, Remark 3.2) instead cites eq. (3.18) of the 1980 paper for the vector form of the relation, so which of the 1976 and 1980 papers contains which exact form is UNRESOLVED.
- Hypotheses and notation: As for the previous statement.
- Page / theorem / equation: Meurant-Strakos Theorem 4.2 (~p. 503); Carson-Demmel (4.6)-(4.8), (4.11).
- Reading evidence and limitations: Secondary only; the attribution between the 1976 and the 1980 paper is inconsistent across the accounts.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L1-Q1: this Gram-commutator-type identity is the object whose bivariate analogue (with X and Y sections and a Z = H_x + i H_y Ritz structure) the campaign investigates.

## Search and attribution notes

Identification of [Pai76] with this title is from memory: UNVERIFIED. See also paige-1980-lanczos and the distinct paige-1980-updating (the inputs use 'Paige 1980' for both). Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: bibliographic data confirmed (Crossref doi:10.1093/imamat/18.3.341; Simon 1984 [12]). The scanned original on the author's page could not be read by the fetch tool. Statements 203-204 are secondary and say so. Attribution caveat: the three accounts split the orthogonality identity between the 1971/1976 and the 1980 papers differently (see 204). Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): metadata confirmed; secondary accounts added as statements 203-204; coverage still 'original not read'.
