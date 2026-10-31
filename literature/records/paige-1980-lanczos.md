# paige-1980-lanczos — C. C. Paige, Accuracy and effectiveness of the Lanczos algorithm for the symmetric eigenproblem, Linear Algebra Appl. 34 (1980) 235-258, doi:10.1016/0024-3795(80)90167-6 (confirmed by Crossref; also Large Scale Matrix Problems, Elsevier 1981, pp. 235-258)

- DOI / URL / supplied location: https://www.cs.mcgill.ca/~chris/pubClassic/80LAIA001.pdf (author's scan; no text layer, tool returned binary data); doi:10.1016/0024-3795(80)90167-6. Earlier (Step 0): no URL in inputs
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: metadata (Crossref; Paige's classic-papers list) + secondary accounts of the theorems (Meurant-Strakos 2006, Paige 2019, Carson-Demmel 2014); the original is NOT read. Earlier (Step 0): supplied secondary account only.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Whole source: scanned PDF not machine-readable here. Needed: Paige's own statements of Lemma 3.1, Theorems 3.1, 4.1-4.3, Corollary 3.1 and eq. (3.18), with exact constants and hypotheses. Earlier (Step 0): Whole source; pending-reference.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-004 — mechanism of loss of orthogonality (as characterised by the inputs)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status. **Update (online pass): the form 'component along a Ritz vector is of order u times the norm of A divided by (eta times the last Ritz-vector component)' is supported by three secondary accounts (statement 205); still not seen in the original.**
- Statement in faithful paraphrase: As characterised by the supplying agent: in finite precision, loss of orthogonality of Lanczos vectors occurs in the direction of converged Ritz vectors; the component of q_k along a Ritz vector is bounded by roughly u*||A|| divided by the Ritz residual, via Paige's perturbed local relations and the identity relating the strictly upper part of Q^T Q to the section T.
- Hypotheses and notation: Single symmetric operator, single start vector, floating point with unit roundoff u.
- Page / theorem / equation: no theorem number supplied. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/adv_F1_F6_F3.md §1.1(c), §1.2 ('exactly Paige's mechanism'), §1.4 item 1 (a target statement, not a quotation of Paige); attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1-Q1: the benchmark mechanism against which the 2D measurements (loss approx u / min joint Ritz residual, within 3x, MEASURED by the supplying agent) are compared.

### LIT?bivariate-lanczos-claude-205 — Loss of orthogonality only along converged Ritz vectors (secondary account)

- Verification: **Original NOT read (author's scan, 80LAIA001.pdf, has no text layer). Secondary: Meurant-Strakos Theorem 4.3; Paige (2019) Remark 3.2; Carson-Demmel eq. (5.11). UNVERIFIED against the 1980 paper.**
- Statement in faithful paraphrase: With Ritz pair (theta_j, y_j = V_k s_j) of T_k and zeta_{kj} the last component of s_j: y_j^T v_{k+1} = -(eps_{jj}) / (eta_{k+1} |zeta_{kj}|), where |eps_{jj}| <= k eps2 ‖A‖ (a quantity of rounding size). Consequently orthogonality of v_{k+1} to the Krylov basis can be lost only in the directions of Ritz vectors whose last component is small (converged), and not before the first Ritz pair converges. The secondary text adds that loss is not proved to occur in every such direction because the numerator can vanish.
- Hypotheses and notation: As for Paige 1976 (one A, one start vector, no reorthogonalization); Ritz values well separated for the clean form.
- Page / theorem / equation: Meurant-Strakos Theorem 4.3 (~p. 504), consequence ~p. 508; Paige (2019) Remark 3.2 and 3.4 cite eq. (3.18) of the 1980 paper; Carson-Demmel eqs. (5.9)-(5.11), (5.22).
- Reading evidence and limitations: Secondary accounts agree; Simons-report Problem 2.19 cites Paige 1976 and 1980 as the baseline (confirmed in the report text, see amsel-et-al-2026).  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L1-Q1 benchmark mechanism (converged Ritz direction) against which the measured 2D relation 'loss ~ u / minimal joint Ritz residual' is compared; kill test K1 in plan.md concerns exactly this alternative.

### LIT?bivariate-lanczos-claude-206 — Accuracy theorems for stabilized Ritz values and eigenvalues of T (secondary account)

- Verification: **Original NOT read. Numbering below is Carson-Demmel's mapping to 'Paige 1980' (UCB/EECS-2014-165, Section 5-6); constants are theirs, which they say differ slightly from Paige's. UNVERIFIED against Paige.**
- Statement in faithful paraphrase: Paige 1980 Lemma 3.1: each eigenpair of T_m has an earlier 'stabilized' Ritz value nearby. Theorem 3.1: a stabilized Ritz value (delta <= sqrt(3) m^2 sigma^2 u in the report's notation) lies within (m+1)^3 sigma^2 u of an eigenvalue of A. Corollary 3.1: a stabilized Ritz pair is an exact eigenpair of a matrix within ~5 t^2 sigma^2 u of A (the report has 6 t^2). Theorem 4.1: at least one eigenvalue of T_n is within (n+1)^3 sigma^2 u of an eigenvalue of A. Theorems 4.2-4.3 concern the Krylov-space perturbation and eigenpair results (not detailed in the digest). Assumptions adopted from Paige: computed betas nonzero, m(30 + eps1) <= 1, eps0 < 1/12. Paige (2019, Section 1.1) cites section 8.7 of the 1971 thesis for the growth of Ritz-value error bounds (possibly like k^2 in bounds, proportional to k in practice for well separated eigenvalues).
- Hypotheses and notation: As for Paige 1976; sigma stands for the norm of A in the report.
- Page / theorem / equation: Paige (1980) Lemma 3.1, Theorems 3.1, 4.1-4.3, Corollary 3.1 as cited by Carson-Demmel; Paige (2019) Remark 3.3 cites Theorem 3.1.
- Reading evidence and limitations: Secondary; polynomial factors in m and the constants are not those of the original with certainty.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L1/L3: 1D result that stabilized (converged) Ritz values are near true eigenvalues; Greenbaum's model (greenbaum-1989) builds on this. No bivariate content.

## Search and attribution notes

The paraphrase is of the supplying agent's summary, not of Paige. UNVERIFIED. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: DOI first guessed wrongly (10.1016/0024-3795(80)90169-X is Saad's Arnoldi paper, same volume; caught by Crossref) and corrected to 10.1016/0024-3795(80)90167-6. ScienceDirect, linkinghub and core.ac.uk routes were refused or empty. Paige's listing page gives the PDF and the Elsevier reprint note. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): metadata and DOI confirmed; secondary theorem accounts added as statements 205-206; coverage still 'original not read'.
