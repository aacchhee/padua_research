# degani-schiff-tannor-2005 — I. Degani, J. Schiff, D. J. Tannor, Commuting extensions and cubature formulae, Numer. Math. 101 (2005) 479-500

- DOI / URL / supplied location: https://arxiv.org/abs/math/0408076 (PDF read via tool digest 2026-10-31, July 2004 preprint); journal doi:10.1007/s00211-005-0628-z (Numer. Math. 101(3) (2005) 479-500, confirmed by Crossref). Earlier (Step 0): https://arxiv.org/abs/math/0408076 (URL as in the Codex branch record; not fetched by me)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: arXiv preprint (July 2004) full text via tool digest; the journal version is NOT read (theorem numbers may differ). Earlier (Step 0): supplied secondary account only; earlier agents saw only the abstract.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Journal version: theorem numbering; the 'colength at least N+n-1', Gorenstein and multi-Hankel content attributed to 'Thm 2' by the BTTB mapping is NOT in the preprint digest and may belong to another source. Earlier (Step 0): Fulltext: exact theorem, dimensions and hypotheses of the commuting-extension construction (load-bearing for L3). PENDING-REFERENCE for the theorem.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.
- Shared key: the Codex branch `codex/charter-unisolvence-20261031` has a record under this key; merge into one record per source at PR preparation (this record uses the `bivariate-lanczos-claude` provisional namespace only).

## Extracted published statements

### LIT?bivariate-lanczos-claude-058 — commuting extensions and cubature (reported)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status. **Update (online pass): the commuting-extension / cubature correspondence is now read in the preprint (statements 215-217): Theorems 9-13; and existence of a symmetric commuting extension of a symmetric pair is guaranteed (Theorem 1, size dn). The inference that a Greenbaum-type statement 'may have no solution' is not supported for exact extensions; the obstruction is about size, positivity and compatibility.**
- Statement in faithful paraphrase: Reported as prior art for the commutator-minimization / commuting-extension route to cubature nodes as joint eigenvalues; the inputs add that for the bivariate recurrence a Greenbaum-type 'nearby larger node set' statement needs the computed non-commuting sections embedded in a larger commuting symmetric pair, which is a commuting-extension problem that may have no solution.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: no theorem number for the first part. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/adv_F1_F6_F3.md §1.3; reports/Open problems verification.md §2 row 10; notes/verify_algorithmic_problems.md Problem 10 (via report); attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L3-Q1: closest predecessor for existence of commuting extensions; the 'may have no solution' remark is the supplying agent's inference.

### LIT?bivariate-lanczos-claude-059 — Theorem 2 as cited in the BTTB mapping (reported)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status. **Update (online pass): Theorem 2 of the preprint is the size bound N >= n + (1/2) max rank [A_i, A_j]; the BTTB mapping's reading ('correction ranks sum to at least n-1', 'colength at least N+n-1') is not found in the preprint digest.**
- Statement in faithful paraphrase: Theorem 2 is cited in the BTTB mapping for the reading 'a commuting repair of a generic multi-Hankel table needs correction ranks summing to at least n-1 and any Gorenstein extension has colength at least N+n-1'; the content of Thm 2 itself is not extracted in the inputs.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: Thm 2 (locator only). Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance reports/Round 3 open problems 2023 2026.md §6b T2 (Degani Thm 2 listed among sources); attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): Exact-arithmetic multi-Hankel side; relevant to L3 only as a measure of extension size.

### LIT?bivariate-lanczos-claude-215 — Commuting extensions: definition, general existence, symmetric case for d = 2

- Verification: **arXiv math/0408076 (July 2004 preprint) read via tool digest; journal version (Numer. Math. 101 (2005) 479-500, doi:10.1007/s00211-005-0628-z, confirmed by Crossref) NOT read, so theorem numbers may differ from the print. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Definition: N x N matrices A~_1..A~_d extend n x n matrices A_1..A_d (N >= n) if the upper-left n x n block of each A~_i is A_i and the A~_i pairwise commute. Theorem 1: any set of matrices has commuting extensions, via an explicit dn x dn block-circulant-type construction; for d = 2 this construction is symmetric when the A_i are. Theorem 3: extensions can be conjugated by diag(I_n, U) to give families. Theorem 5: symmetric extensions exist iff A_i = Q Lambda_i Q^T with diagonal Lambda_i and an n x N matrix Q with orthonormal rows. Theorem 6: the smallest eigenvalue of an extension is at most that of A, the largest at least that of A.
- Hypotheses and notation: Real or complex matrices; symmetric where stated; no positivity of weights imposed in Theorem 1.
- Page / theorem / equation: Preprint Section 2: Theorems 1, 3, 5, 6 and the definition (digest).
- Reading evidence and limitations: Digest of the preprint. Existence of a commuting (even symmetric, d = 2) extension is therefore NOT the open issue for a symmetric pair; size, closeness and the cubature compatibility condition are.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: for any symmetric pair (H_x, H_y) with nonzero commutator an exact commuting symmetric extension of size 2n exists; the campaign question is about extensions that are small and structured (nearby nodes, positive weights, same degree-n sections).

### LIT?bivariate-lanczos-claude-216 — Lower bound on extension size and non-attainment by symmetric extensions

- Verification: **Preprint digest; journal numbering not checked.**
- Statement in faithful paraphrase: Theorem 2: if N x N commuting extensions exist then N >= n + (1/2) max over i,j of rank [A_i, A_j]. Theorem 4: for n > 5 there exist symmetric n x n A_1, A_2 with rank [A_1, A_2] = 2 for which no (n+1) x (n+1) symmetric commuting extension exists, so the bound of Theorem 2 is not always attained by symmetric extensions. A parameter count (eq. 14) predicts symmetric extensions when N - n >= n(n-1)(d-1)/(2(n+d)), but for d = 2 the authors say the count is weaker than Theorem 2 when the commutator has maximal rank.
- Hypotheses and notation: Theorem 4 needs n > 5 and symmetric A_1, A_2.
- Page / theorem / equation: Preprint Theorems 2 and 4, eq. (14), Lemma 1 (digest).
- Reading evidence and limitations: Digest; the plan's 'correction ranks sum to at least n-1' and 'colength at least N+n-1' (statement 059) are NOT these statements and are not found in the preprint digest (no mention of Gorenstein, colength or multi-Hankel in the preprint text); they may come from other sources or the journal version.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: quantitative obstruction already in print for exact small symmetric extensions of a pair with low-rank commutator; relevant to the 'explicit obstruction family' alternative, only for exact extensions without positivity/compatibility.

### LIT?bivariate-lanczos-claude-217 — Cubature correspondence: positive-weight odd-degree rules and compatible commuting extensions

- Verification: **Preprint digest; journal numbering not checked.**
- Statement in faithful paraphrase: Theorem 9: an N-point positive-weight cubature rule of degree 2q+1 yields N x N symmetric commuting extensions of the matrices representing the coordinate multiplications on the degree-q polynomial space. Theorem 10: these satisfy a compatibility condition (the extensions act on the embedded degree-(q-1) polynomials as the multiplication operators do). Theorem 11 (converse): commuting extensions satisfying the compatibility condition give a cubature formula exact for degree 2q+1, with nodes the joint eigenvalues and weights the squared first components of the joint eigenvectors. Theorem 12: N >= binom(d+q, d) + (1/2) max rank [A_i, A_j]. Theorem 13: for each coordinate some node lies at or below the smallest and another at or above the largest eigenvalue of A_i. Section 6 gives 7-point degree-5 planar rules and Gaussian-weight rules of degrees 11-17 (26, 35, 46, 57 nodes). Section 7 (open questions): no existence proof for cubature via this route is available and the minimal extension size is unresolved.
- Hypotheses and notation: Positive weights; odd degree 2q+1; symmetric extensions.
- Page / theorem / equation: Preprint Theorems 9-13, Sections 6-7 (digest).
- Reading evidence and limitations: Digest of the preprint.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: the positive-weight/compatible extension is the correct representing-measure notion for the square (M = N) case; Theorem 12 links extension size to the commutator rank of the degree-q sections.

## Search and attribution notes

Shared key with codex/charter-unisolvence-20261031 (record degani-schiff-tannor-2005); merge at PR preparation. Koiran's later commuting-extension paper is recorded as koiran-2024. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: the arXiv PDF is the 2004 preprint; the digest says it has no Gorenstein, colength or multi-Hankel content. Koiran (2024) confirms the journal reference as [2] and credits the paper with coining 'commuting extension'. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): preprint read via tool digest; statements 215-217 added; coverage upgraded from 'secondary only'.
