# kachkovskiy-safarov-2016 — I. Kachkovskiy, Yu. Safarov, Distance to normal elements in C*-algebras of real rank zero, J. Amer. Math. Soc. 29(1) (2016) 61-80 (online 8 Jan 2015), doi:10.1090/S0894-0347-2015-00823-2, arXiv:1403.2021 (journal now CONFIRMED by Crossref)

- DOI / URL / supplied location: https://arxiv.org/abs/1403.2021 (abstract page and the v3 PDF read via tool digest 2026-10-31); Crossref doi:10.1090/S0894-0347-2015-00823-2. Earlier (Step 0): https://arxiv.org/abs/1403.2021 (abstract page fetched 2026-10-31)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: arXiv v3: introduction, Theorem 1.1 and remarks, Section 1.1 (equation (1.3)), Section 3 and reference list via tool digest (two fetches); proofs NOT read. Earlier (Step 0): metadata + abstract only; journal not stated.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Proofs; the explicit value of C (none given in the paper); the JAMS pagination of eq. (1.3); Davidson (1985), Corollary 4.5, for the constant 50 sqrt(2) mentioned in Section 3. Earlier (Step 0): Fulltext: whether it contains the almost-commuting self-adjoint pair bound with the square-root dependence attributed to it by the inputs.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-056 — distance to normal operators (abstract)

- Verification: **Abstract-checked only** (arXiv abstract page); full text NOT inspected, so the mathematical content stays UNVERIFIED. `LITERATURE` attribution only. **Update (online pass): the main Theorem 1.1 and its remarks are now read (statement 220).**
- Statement in faithful paraphrase: Sharp estimate of the distance from a bounded Hilbert-space operator to the set of normal operators in terms of the commutator norm ||[A, A*]|| and the distance from A to the invertibles; a slightly modified version holds in any C*-algebra of real rank zero. The abstract page does not address almost-commuting self-adjoint matrices.
- Hypotheses and notation: As stated in the abstract; hypotheses beyond the abstract not checked.
- Page / theorem / equation: abstract. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance arXiv abstract page fetched 2026-10-31; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L3-Q1 predecessor 'quantitative Lin'. The abstract concerns NORMAL elements; applying it to the pair (H_x, H_y) via A = H_x + i H_y (with [A, A*] = -2i [H_x, H_y]) is the recorder's inference, UNVERIFIED.

### LIT?bivariate-lanczos-claude-057 — attribution of ||[A,B]||^{1/2}-type bounds (reported, memory)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status. **Update (online pass): CONFIRMED. Equation (1.3) of arXiv v3 states exactly such a bound for Hermitian pairs, with the sum of the two distances and a universal dimension-free constant (statement 221). The earlier 'unconfirmed attribution' status is superseded.**
- Statement in faithful paraphrase: The supplying agent attributes square-root-in-commutator bounds for almost commuting self-adjoint matrices to Kachkovskiy-Safarov, marked [memory]; the abstract page did not confirm this.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: no locator. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/verify_algorithmic_problems.md Problem 1(f) '[memory]'; reports/Round 3 open problems 2023 2026.md §3 F4; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): Unconfirmed attribution; keep L3-Q1 hypotheses separate until the fulltext is read.

### LIT?bivariate-lanczos-claude-220 — Theorem 1.1: distance to normal elements (upper and lower bounds)

- Verification: **arXiv 1403.2021 v3 introduction, Section 1.1 and Section 3 read via tool digest (two fetches); proofs NOT read. Journal: J. Amer. Math. Soc. 29(1) (2016) 61-80, online 8 Jan 2015, doi:10.1090/S0894-0347-2015-00823-2 (Crossref). `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Let A be a unital C*-algebra of real rank zero, N_f(A) the normal elements with finite spectrum, and d_1(A) = sup over complex lambda of the distance from A - lambda to the connected component of the invertibles. Upper bound (1.1): dist(A, N_f(A)) <= C (‖[A,A*]‖^{1/2} + d_1(A)) with C a universal constant (no numerical value given). Lower bound (1.2): dist(A, N_f(A)) >= max{ ‖[A,A*]‖/(5‖A‖), d_1(A) }. For von Neumann algebras (including B(H)) N_f may be replaced by all normal elements (Remark 1.2); for finite matrices d_1 = 0 (Remark 1.3). Remark 1.5: the lower bound's factor 1/‖A‖ cannot be replaced by C‖[A,A*]‖^{1/2}, while a square-root decay occurs for some examples. Corollary 1.4 is a quantitative Brown-Douglas-Fillmore statement for separable H.
- Hypotheses and notation: A in a unital C*-algebra of real rank zero; the norm is the C*-norm.
- Page / theorem / equation: Theorem 1.1, eqs. (1.1)-(1.2), Remarks 1.2-1.5, Corollary 1.4 (arXiv v3, pp. 2-4 of the arXiv layout; JAMS page numbers not checked).
- Reading evidence and limitations: Statements and locators as digested. No dimension dependence: the constant is universal.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: for A = H_x + i H_y one has [A, A*] = -2i [H_x, H_y], so the commutator of the sections controls distance to a normal matrix with the same square-root rate; this reduction is the recorder's, not the paper's.

### LIT?bivariate-lanczos-claude-221 — Equation (1.3): almost commuting Hermitian pair, square-root bound (CONFIRMED in the paper)

- Verification: **Statement read in arXiv v3 Section 1.1 through two tool fetches that agree; confirms the attribution that LIT?bivariate-lanczos-claude-057 reported from memory. Proof not read. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Consequence of Theorem 1.1: for any two Hermitian matrices X, Y (any size) there exist commuting Hermitian matrices X', Y' with ‖X - X'‖ + ‖Y - Y'‖ <= C ‖[X,Y]‖^{1/2}, where C is a universal constant independent of X, Y and the dimension; C has no numerical value in the paper. The bound is for the SUM of the two distances. This confirms a conjecture of Davidson and Szarek (Handbook of the Geometry of Banach Spaces, vol. 1, 2001, 317-366), whose question (C) was posed under ‖X‖ + ‖Y‖ <= 1; by homogeneity the normalization is immaterial. The exponent 1/2 cannot be improved (a function F(t) cannot decay faster than t^{1/2} as t -> 0, by homogeneity). Section 3: Theorem 3.1 is a refined version of Davidson, Almost commuting Hermitian matrices, Math. Scand. 56 (1985) 222-240, Corollary 4.5, which already suffices for (1.3) in finite dimensions (that corollary gives normal operators with a constant 50 sqrt(2) in its first estimate, per the digest).
- Hypotheses and notation: X, Y Hermitian matrices of any finite size (more generally self-adjoint operators); commutator in operator norm; the approximants have the same size and no other structure (no sparsity pattern, no tie to start vector).
- Page / theorem / equation: Equation (1.3), arXiv v3 Section 1.1 after Remark 1.3 (the first digest said 'p. 3'); Section 3 on [9, Corollary 4.5]; references [9], [11], [13], [17] (digest).
- Reading evidence and limitations: Two independent fetches agree on the statement; constant not explicit; this is a bound for existence of a nearby commuting Hermitian pair of the SAME size, with no control of structure.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: the earlier plan note 'Kachkovskiy-Safarov almost-commuting bound ... UNVERIFIED' is now supported: ‖[Ĥ_x,Ĥ_y]‖ = O(eps) gives a commuting Hermitian pair at distance O(sqrt(eps)) (sum of distances), dimension free. It does not give a block-tridiagonal structure, a common start vector or positivity of weights, so it settles only the first step of a Greenbaum-type argument.

### LIT?bivariate-lanczos-claude-222 — Weaker earlier bound by Hastings for matrices

- Verification: **As digested from the K-S introduction.**
- Statement in faithful paraphrase: The paper states that Hastings (ref. [16]) proved a bound of the form C_eps ‖[A,A*]‖^{1/5 - eps} for finite matrices with ‖A‖ <= 1, weaker than the square-root rate (p. 2).
- Hypotheses and notation: Finite matrices, ‖A‖ <= 1.
- Page / theorem / equation: Introduction, p. 2 (digest).
- Reading evidence and limitations: Secondary within K-S.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): Context for choosing the exponent in L3-Q1.

## Search and attribution notes

SEARCH NOTE: a web search for the title returned the arXiv and AMS (JAMS 2016-29-01) pages; only the arXiv abstract page was read. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: answer to the task question. Yes: eq. (1.3) gives, for any Hermitian X, Y, commuting Hermitian X', Y' with ‖X-X'‖ + ‖Y-Y'‖ <= C‖[X,Y]‖^{1/2}, C universal and unspecified; it is a corollary of Theorem 1.1 (d_1 = 0 for matrices) and, per Section 3, already follows from Davidson (Math. Scand. 56 (1985) 222-240), Corollary 4.5. The exponent 1/2 is optimal. The paper gives no structural control of the approximants. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): Theorem 1.1, eq. (1.3) and Section 3 read via tool digest; statements 220-222 added; 057 marked CONFIRMED; journal reference confirmed; coverage upgraded.
