# simonova-tichy-2025 — D. Simonova, P. Tichy, On finite precision block Lanczos computations, BIT (2025), doi:10.1007/s10543-025-01089-2 (DOI from notes/recent_multivariate_NLA.md), arXiv:2507.16484

- DOI / URL / supplied location: https://arxiv.org/abs/2507.16484 (abstract, HTML and PDF read via tool digest 2026-10-31); BIT Numer. Math. 65(4), article 47, online 11 Nov 2025, doi:10.1007/s10543-025-01089-2 (Crossref). Earlier (Step 0): https://arxiv.org/abs/2507.16484 (abstract page fetched 2026-10-31)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: arXiv v1 text via tool digests (HTML only partly; PDF gave Theorems 1-4, Sections 5.2 and 6.1); formulas and proofs NOT checked. Venue/DOI confirmed by Crossref. Earlier (Step 0): metadata + abstract only; BIT venue not confirmed. PR-preparation (2026-11-01): the L3 prior-art review (2026-10-31) re-read §1 of the arXiv html v1 and reports the proof for intervals of size sqrt(eps)‖A‖ with eps‖A‖ only in experiments, and the block case as open; consistent with statements 016 and 230.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation). PR-preparation additions (2026-11-01): taken from the L3 prior-art review 2026-10-31 (Claude Opus 5.5, effort high; reading through WebFetch digests) by the Claude literature developer (Sonnet 5.5, effort high); the source was not re-read by the consolidator.
- Named gaps requiring future re-reading: Proofs; formulas (21), (35), (36); sufficient conditions in detail; the version differences between arXiv v1 and the BIT print. Earlier (Step 0): Fulltext: exact sufficient conditions and the status of the free parameter W_k (load-bearing for L1/L4).
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT-081 (LIT?bivariate-lanczos-claude-016) — Greenbaum-type result for block Lanczos (abstract)

- Verification: **Abstract-checked only** (arXiv abstract page); full text NOT inspected, so the mathematical content stays UNVERIFIED. `LITERATURE` attribution only. **Update (online pass): venue and DOI confirmed and Theorems 1-4 digested (statements 229-230).**
- Statement in faithful paraphrase: Extends Greenbaum's 1989 model to block Lanczos: a continuation process terminating after finitely many steps gives perturbations such that the computed block tridiagonal matrices are exact block Lanczos for a larger model matrix; sufficient conditions keep the perturbations small. In the single-vector case the conditions can always be met; whether they can always be met in the block case is stated open.
- Hypotheses and notation: As stated in the abstract; hypotheses beyond the abstract not checked.
- Page / theorem / equation: abstract. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance arXiv abstract page fetched 2026-10-31; notes/recent_multivariate_NLA.md §1 item 2; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L1/L3/L4: the block-level backward model that a two-operator statement would extend; conditional, one operator.

### LIT-082 (LIT?bivariate-lanczos-claude-017) — author statements on difficulty and free parameter (reported)

- Verification: **UNVERIFIED** against the original publication; `LITERATURE` attribution only, no inherited proof status. **Update (online pass): both phrases are located in the text, Sections 1 and 5 (statement 231).**
- Statement in faithful paraphrase: Reported quotations: generalizing Paige's analysis to the block case 'is challenging and requires further research'; a comprehensive finite-precision block Lanczos theory 'is still lacking'; a key open question is how to select the free matrix parameter W_k.
- Hypotheses and notation: As reported by the supplied note; hypotheses not independently checked.
- Page / theorem / equation: locators not supplied. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance notes/recent_multivariate_NLA.md §1 item 2 and R1 'Who states it'; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): Open-status evidence for L1/L4; wording not verified by me beyond the abstract.

### LIT-233 (LIT?bivariate-lanczos-claude-229) — Venue and DOI confirmed

- Verification: **Crossref record read. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: D. Simonova and P. Tichy (the arXiv page spells the names with diacritics), On finite precision block Lanczos computations, BIT Numerical Mathematics 65(4), article 47; published online 11 November 2025, print December 2025; doi:10.1007/s10543-025-01089-2. The reference list cites an unpublished 2022 report by Carson and Chen, Finite Precision Block Lanczos.
- Hypotheses and notation: n/a
- Page / theorem / equation: Crossref metadata.
- Reading evidence and limitations: Venue/DOI from the supplied notes now confirmed; arXiv v1 22 Jul 2025.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): Citation hygiene for L1/L4.

### LIT-234 (LIT?bivariate-lanczos-claude-230) — Theorems 1-4 and the free parameter W_k (arXiv v1 full text, digest)

- Verification: **arXiv 2507.16484 (PDF) read via tool digest; proofs and the sufficiency conditions in detail NOT checked. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Scalar case: the paper summarizes Greenbaum's 1989 result without numbering it (intervals of size about sqrt(u)‖A‖ from the proof, u‖A‖ suggested by experiments; a 'Lemma (Paige)' at Greenbaum p. 32 is invoked). Block case: Theorem 1: if the perturbations are at most eps2‖A‖ and a Ritz-vector condition holds with some eps1, every eigenvalue of T_N is within 3 max(sqrt(N) eps2, eps1)‖A‖ of an eigenvalue of A; the condition asks that every Ritz pair with a small-norm eigenvector have a nearby Ritz pair of norm at least 0.5. Theorem 2: the continuation vectors q_{k+j} are orthonormal to W_k and to each other and beta_{k+j} = q_{k+j}^T A q_{k+j-1} for j >= 3. Theorem 3: the continuation can be written as a perturbed three-term recurrence (21). Theorem 4: the perturbations are expressed through W_k with rho_k = ‖R_k^{-1}‖; if the Ritz vectors are sufficiently independent (rho_k = O(1)) two terms (35) and one term (36) dominate, and their smallness is the sufficient condition. W_k is the only free parameter, the Q-factor of a QR factorization of m selected Ritz vectors chosen by a heuristic criterion delta_{k,i} > mu‖A‖ (Section 6.1). The abstract says the conditions are always satisfiable in the single-vector case (Greenbaum, based on Paige); Section 5.2 says bounding the second term in (35) in the block case 'remains open'.
- Hypotheses and notation: Block Lanczos with block size m, one symmetric A.
- Page / theorem / equation: Theorems 1-4; Section 5.2; Section 6.1 (digest; abstract also gives the open question).
- Reading evidence and limitations: Digest; formulas (21), (35), (36) not seen.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L1/L3/L4: the block backward model whose proof pattern (continuation process with free W_k) any two-operator model would extend; conditional, one operator.

### LIT-235 (LIT?bivariate-lanczos-claude-231) — The two author statements on difficulty (CONFIRMED in the text)

- Verification: **Located in the arXiv text through two tool digests (HTML introduction and PDF). `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Section 1 says that generalizing Paige's analysis to the block case is challenging and needs further research (the HTML digest quotes the phrase 'is challenging and requires further research'). Section 5 says that a theory describing the finite-precision behaviour of block Lanczos is still lacking. So the two reported statements of 017 are located in Sections 1 and 5.
- Hypotheses and notation: n/a
- Page / theorem / equation: Section 1; Section 5.
- Reading evidence and limitations: Phrases as returned by the digests; short quotations only.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L1/L4 open-status evidence.

## Search and attribution notes

No additional attribution notes beyond the statements above. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: the BIT venue, volume, issue, article number and date are confirmed. The earlier ETNA paper by the same authors (arXiv 2106.02068) was fetched but its digest contained no theorem statements for Greenbaum or Paige. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

PR-preparation consolidation 2026-11-01 (audit-01 protocol finding P2): the additions marked 'PR-preparation' above come from the L3 prior-art review 2026-10-31 (topics/bivariate-lanczos-20261031/reviews/), which read the source through WebFetch digests and make no novelty claim; the consolidator did not re-read the source. Any web check made at consolidation is logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'PR-preparation consolidation 2026-11-01'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): venue/DOI confirmed; Theorems 1-4 and quotes located (statements 229-231).

2026-11-01 (PR-preparation consolidation, audit-01 protocol finding P2): no new statement; the L3 prior-art review's reading of §1 (sqrt(eps)‖A‖ proven, eps‖A‖ in experiments, block case 'remains open') agrees with statements 016 and 230 and is recorded as a second digest (html v1).
