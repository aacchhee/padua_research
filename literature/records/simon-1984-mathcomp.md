# simon-1984-mathcomp — H. D. Simon, The Lanczos algorithm with partial reorthogonalization, Math. Comp. 42 (1984) 115-142

- DOI / URL / supplied location: https://www.ams.org/journals/mcom/1984-42-165/S0025-5718-1984-0725988-X/S0025-5718-1984-0725988-X.pdf (PDF read via tool digest 2026-10-31); abstract page https://www.ams.org/mcom/1984-42-165/S0025-5718-1984-0725988-X/ ; doi:10.1090/S0025-5718-1984-0725988-X. Earlier (Step 0): https://www.ams.org/mcom/1984-42-165/S0025-5718-1984-0725988-X/ (abstract page fetched 2026-10-31)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: complete paper (pp. 115-142) read via AMS PDF as a tool digest (equations and page locators as digested, some displays garbled); proofs not checked. Earlier (Step 0): metadata + abstract only.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Proof of Theorem 2 is not in this paper (Report PAM-74, Theorem 2.5; see also LAA 61). The numerical constants and page numbers need confirmation against page images before being used in a proof dependency. Earlier (Step 0): Fulltext: exact hypotheses and proof of the semi-orthogonality theorem (load-bearing for L2).
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-008 — partial reorthogonalization (abstract)

- Verification: **Abstract-checked only** (AMS abstract page); full text NOT inspected, so the mathematical content stays UNVERIFIED. `LITERATURE` attribution only. **Update (online pass): the omega-recurrence, thresholds and costs are now read (statements 210-212).**
- Statement in faithful paraphrase: Partial reorthogonalization tracks the loss of orthogonality with a simple recurrence (the omega-recurrence) that needs no inner products, and reorthogonalizes only when the recurrence indicates it is necessary; this saves work relative to full reorthogonalization.
- Hypotheses and notation: As stated in the abstract; hypotheses beyond the abstract not checked.
- Page / theorem / equation: abstract. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance AMS abstract page fetched 2026-10-31; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L2-Q1 template: the omega-recurrence that a 2D analogue would have to extend (the notes say the 2D version must use the commutator defect).

### LIT?bivariate-lanczos-claude-009 — semi-orthogonality theorem (reported)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status. **Update (online pass): the paper's Theorem 2 (p. 119) uses the semiorthogonality level sqrt(u) (not sqrt(u/k)), gives no explicit O(u) bound and defers the proof; see statement 211 and the simon-1984-laa record (statement 214). The attribution of the theorem to Simon stays supported; the quantitative form reported in 009 is NOT in this paper.**
- Statement in faithful paraphrase: Reported: keeping orthogonality of the Lanczos vectors at the level sqrt(u) (semi-orthogonality) suffices for the projected (tridiagonal) matrix to be accurate to O(u) relative to the norm; this is the 'Simon theorem' whose two-operator analogue L2-Q1 asks about.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: theorem number not supplied. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/adv_F1_F6_F3.md §1.1(c) 'Selective/partial reorthogonalization'; reports/Round 3 open problems 2023 2026.md §7 item 3; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L2-Q1 kill-test criterion. Statement taken from the supplying agent's summary; the AMS abstract does not state it.

### LIT?bivariate-lanczos-claude-210 — Theorem 1: the omega-recurrence for inner products of computed Lanczos vectors

- Verification: **Full paper read through the AMS PDF (tool digest, pp. 115-142; some displays garbled). `LITERATURE` attribution only.**
- Statement in faithful paraphrase: With omega_{jk} = q_j^T q_k, the perturbed Lanczos recurrence (3.1) with rounding vectors f_j implies a second-order inhomogeneous recurrence with variable coefficients: beta_{j+1} omega_{j+1,k} = beta_{k+1} omega_{j,k+1} + (alpha_k - alpha_j) omega_{jk} + beta_k omega_{j,k-1} - beta_j omega_{j-1,k} + (q_k^T f_j - q_j^T f_k), with omega_kk = 1 and omega_{k,0} = 0. The proof multiplies the step-j and step-k Lanczos equations by q_k^T and q_j^T and subtracts. The paper attributes the recurrence to Paige and to Takahasi and Natori, and says it uses it computationally for the first time. In exact arithmetic with zero initial data all omega_jk stay zero; the paper regards this as an instability of the difference equation.
- Hypotheses and notation: Single symmetric A; f_j unknown local rounding vector.
- Page / theorem / equation: Section 3, Theorem 1, eq. (3.2), p. 117 (digest).
- Reading evidence and limitations: Read via digest; exact sign convention of the f-terms as digested.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L1-R02 and L2-Q1: the exact omega-recurrence template; confirms the campaign's 'exact omega-recurrence' is a bivariate analogue of a 1984 one-operator theorem (the attribution to Paige/Takahasi-Natori is the paper's own).

### LIT?bivariate-lanczos-claude-211 — Theorem 2 and the semiorthogonality definition

- Verification: **Read via digest; the proof is NOT in this paper (deferred). `LITERATURE` attribution only.**
- Statement in faithful paraphrase: The level of orthogonality at step j is kappa_j = max over k<j of |q_k^T q_j| (eq. 4.1, p. 119); semiorthogonality means kappa_j <= sqrt(u). Theorem 2 (p. 119): if the computed Lanczos vectors are kept semiorthogonal by some means, then T_j is, up to roundoff, the orthogonal projection of A onto span{Q_j}. The paper gives no explicit error bound in Theorem 2 (the phrase 'up to roundoff' is not formalized, and the hypothesis says nothing explicit about f_j); the proof is deferred to Simon's Berkeley report PAM-74 (1982), Theorem 2.5. An O(|L(j)| u ‖A‖) bound on inner products between non-reorthogonalized vectors appears in eq. (8.3), p. 133. The threshold in this paper is sqrt(u) (not sqrt(u/k)).
- Hypotheses and notation: Single symmetric A; semiorthogonal vectors by any means.
- Page / theorem / equation: Section 4, eq. (4.1) and Theorem 2, p. 119; eq. (8.3), p. 133.
- Reading evidence and limitations: Correction to the earlier statement LIT?bivariate-lanczos-claude-009: the paper's Theorem 2 has no explicit O(u) bound and uses sqrt(u), not sqrt(u/k); the rigorous version is in the cited report and (per Jia-Li) in LAA 61 (see simon-1984-laa). The earlier statement 009 stays as recorded, its verification line is annotated.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L2-Q1: the 'Simon theorem' whose two-operator analogue is asked; the analogue should be calibrated against the sqrt(u) level, not sqrt(u/k).

### LIT?bivariate-lanczos-claude-212 — Partial reorthogonalization: ω estimates, thresholds and costs

- Verification: **Read via digest. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Since the f_j are unknown, the omega recurrence is run with random estimates (eqs. 5.1-5.3, pp. 121-122; normal variates with standard deviation about 0.3 and 0.6 scaled by roundoff, and N(0, 1.5u) resets after a reorthogonalization, p. 123). The estimate overestimates the true level initially and tracks it closely once it reaches about sqrt(u); it signals the onset within a few steps (Figures 5.1-5.2, 6.1-6.3, pp. 122-125). Strategy: a regular Lanczos step, then update the estimates, then reorthogonalize only against an index set L(j) when an estimate exceeds sqrt(u) (pp. 119-126); neighbours are included by a second threshold eta, recommended eta = u^{3/4} (p. 129); after a reorthogonalization the next step is also reorthogonalized (p. 126). Using estimated omegas in place of exact inner products was tried and rejected (p. 126). Costs: about a third of the orthogonalizations of periodic reorthogonalization (Section 9.1, p. 133); about 20 percent of full reorthogonalization for moderately conditioned matrices (Table 10.3, p. 136); comparable to selective orthogonalization (Section 9.2).
- Hypotheses and notation: Single symmetric A.
- Page / theorem / equation: Sections 4-10, pp. 119-141 (as digested).
- Reading evidence and limitations: Digest of the whole paper; numerical constants as digested.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L2-Q1: baseline thresholds (sqrt(u), u^{3/4}) and cost figures against which the bivariate partial/selective reorthogonalization is compared.

### LIT?bivariate-lanczos-claude-213 — Reference list confirms the Paige citations and early origin of the omega recurrence

- Verification: **Read in the AMS PDF reference list (digest).**
- Statement in faithful paraphrase: Simon's references include: Paige PhD thesis (London, 1971) [10]; Paige, Computational variants of the Lanczos method for the eigenproblem, J. Inst. Math. Appl. 10 (1972) 373-381 [11]; Paige, Error analysis of the Lanczos algorithm for tridiagonalizing a symmetric matrix, J. Inst. Math. Appl. 18 (1976) 341-349 [12]; Paige, Accuracy and effectiveness of the Lanczos algorithm for the symmetric eigenproblem, Linear Algebra Appl. 34 (1980) 235-258 [13]; Simon, The Lanczos algorithm for solving symmetric linear systems, Report PAM-74, Berkeley, 1982 [20]; Scott, Analysis of the symmetric Lanczos process, PhD thesis, Berkeley, 1978 [19]; Takahasi and Natori, Eigenvalue problem of large sparse matrices, Rep. Comp. Center Univ. Tokyo 4 (1971-72) 129-148 [21]. The Math. Comp. paper does not cite the LAA 61 paper.
- Hypotheses and notation: n/a
- Page / theorem / equation: Reference list, AMS PDF (digest).
- Reading evidence and limitations: This independently confirms the venues and years of the Paige 1971/1976/1980 records.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): Citation hygiene for the Paige chain.

## Search and attribution notes

The LAA companion paper is recorded separately as simon-1984-laa. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: the AMS PDF is open and was read via the tool. Its Theorems 1 and 2 are the only numbered theorems (there is no Theorem 3 or 4). Theorem 1 is attributed in the paper to Paige and to Takahasi-Natori. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): full text read via tool digest; statements 210-213 added; annotation of 009; coverage upgraded.
