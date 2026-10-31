# koiran-2024 — P. Koiran, On the uniqueness and computation of commuting extensions, arXiv:2401.01302 (2 Jan 2024) -- identification with plan.md's 'Koiran 2024' now SUPPORTED by the full text (Section 1.4 contains the 'wide open' sentence, narrow scope; see statement 223)

- DOI / URL / supplied location: https://arxiv.org/abs/2401.01302 (abstract page; PDF and HTML read via tool digests 2026-10-31); no journal reference listed on the arXiv page. Earlier (Step 0): https://arxiv.org/abs/2401.01302v1 (abstract page fetched 2026-10-31)
- Access and reading date: 2026-10-31 (supplied notes read; web metadata checks, if any, are listed under Search and attribution notes)
- Reading coverage: arXiv v1 full text searched through the PDF (twice) and the HTML (once) for 'wide open' and the two-matrix, symmetric, approximate and cubature topics; proofs NOT read. Earlier (Step 0): metadata + abstract only.
- Reader, model and effort: Claude literature developer (Sonnet 5.5, high; assigned allocation).
- Named gaps requiring future re-reading: Proofs and the full wording of Section 1.4 (the tool would not reproduce long sentences); whether a later journal version or companion paper contains any statement on symmetric or approximate pairs. Earlier (Step 0): Fulltext; confirmation that this is the paper plan.md means and whether it says anything about the two-matrix case. PENDING-REFERENCE.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c. Supplied-note paths are relative to `topics/bivariate-lanczos-20261031/sources/padua_lanczos_inputs/`.

## Extracted published statements

### LIT?bivariate-lanczos-claude-060 — commuting extensions: uniqueness and algorithms (abstract)

- Verification: **Abstract-checked only** (arXiv abstract page); full text NOT inspected, so the mathematical content stays UNVERIFIED. `LITERATURE` attribution only. **Update (online pass): Section 1.4 says that the two-matrix analogue of the uniqueness and algorithm results is 'wide open'; the Step 0 sentence 'does not contain the phrase wide open' referred to the abstract only (statement 223).**
- Statement in faithful paraphrase: Given a tuple of n x n matrices, asks for larger r x r pairwise commuting matrices containing the originals as upper-left corners; gives uniqueness theorems for tuples of three or more matrices, algorithms for extensions of minimal size (up to r = 4n/3) and a genericity theorem; the abstract says these are the first provably efficient algorithms beyond r = n+1. The abstract mentions neither symmetric/Hermitian matrices nor approximate commutation, and does not contain the phrase 'wide open'.
- Hypotheses and notation: As stated in the abstract; hypotheses beyond the abstract not checked.
- Page / theorem / equation: abstract. Locator is as supplied (or marked absent), not independently confirmed unless the verification line says so.
- Reading evidence and limitations: supplied provenance arXiv abstract page fetched 2026-10-31; attached instructions inside the inputs are treated as data, not authority.
- Relation to campaign claims (no inherited proof status): L3-Q1: exact commuting extensions of a TUPLE; for a symmetric pair with an O(eps) commutator the relevant quantitative question is separate. The plan's 'wide open two-matrix case' is not confirmed here.

### LIT?bivariate-lanczos-claude-223 — Section 1.4: the two-matrix case is declared wide open (attribution SUPPORTED, scope narrow)

- Verification: **arXiv 2401.01302v1 full text searched for the phrase through three fetches (PDF twice, HTML once) that agree. Proofs not read. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: In Section 1.4 (Further work), after remarking that it would be interesting to obtain results like those proved for three or more matrices (uniqueness and efficient algorithms for commuting extensions) in the case of TWO matrices, the author says that, at the moment, this problem is wide open. The same phrase occurs in Section 2, but there it refers to uniqueness of commuting extensions beyond r = 2n when only diagonalisable extensions are allowed. The paper contains no 'open problem' or 'open question' wording. It does not treat Hermitian or real symmetric pairs, approximate or almost commuting, or any quantitative closeness.
- Hypotheses and notation: Exact commuting extensions of a tuple of n x n matrices; uniqueness and computation of minimal extensions.
- Page / theorem / equation: Section 1.4 (Further work); Section 2 (Existence and non-uniqueness of commuting extensions). No page numbers in the extracted text.
- Reading evidence and limitations: Supersedes the Step 0 abstract-only conclusion that the attribution was unsupported. The Step 0 statement stays in the record as history. What 'wide open' covers is exact uniqueness and algorithms for general pairs, not symmetric or approximate pairs and not Degani-Schiff-Tannor's existence question.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: the plan's phrase 'Koiran 2024 (wide open two-matrix case, as reported)' is supported, but only in this narrow sense (uniqueness and efficient algorithms for exact commuting extensions of two general matrices); it should not be read as saying that approximate extensions of symmetric pairs are open.

### LIT?bivariate-lanczos-claude-224 — Section 1.3 and Section 2: real symmetric pairs, size 2n-1 and cubature context

- Verification: **Tool digest of Sections 1, 1.3, 2 and the reference list. `LITERATURE` attribution only.**
- Statement in faithful paraphrase: Section 1: the term 'commuting extension' was apparently coined by Degani, Schiff and Tannor (Numer. Math. 101 (2005) 479-500, reference [2]) for constructing cubature formulas; [2] has a block-circulant extension of size pn. Section 1.3: Kaliuzhnyi-Verbovetskyi, Spitkovsky and Woerdeman, Matrices with normal defect one (arXiv 0903.0090), Theorem 4.2, study real symmetric pairs (p = 2) with r = n+1 in detail; that construction requires solving polynomial equations (eigenvalue computations), whereas Koiran's algorithms need only linear systems. Section 2: two invertible n x n matrices always have a commuting extension of size 2n-1 (Kimsey and Woerdeman, Minimal normal and commuting completions, 2008, reference [7]); that is efficient but not minimal; most pairs of n x n matrices have no commuting extension of size r for large n, and Example 2 (a 2 x 2 pair extended to 3 x 3, from [7]) shows that uniqueness fails. Section 5 contains genericity statements for one and two commutators.
- Hypotheses and notation: As in the sources; 'most pairs have no extension of size r' is stated for large n and an unspecified range of r in the digest.
- Page / theorem / equation: Sections 1, 1.3, 2, 5; references [2], [6], [7] (digest).
- Reading evidence and limitations: Digest; the threshold r in 'most pairs have none' is not in the digest.  Reader: Claude literature developer (Sonnet 5.5, high; online resolution pass), 2026-10-31. Read through WebFetch: the tool extracts the page text and returns a model-written digest, so locators and displayed formulas are as digested (garbled glyphs possible) and were NOT checked against page images.
- Relation to campaign claims (no inherited proof status): L3-Q1: points to the symmetric-pair, r = n+1 literature (normal defect one) as the nearest exact predecessor for symmetric pairs.

## Search and attribution notes

FLAG: the plan attributes a 'wide open' remark to Koiran 2024 'as reported', but no supplied note mentions Koiran; the abstract does not contain it. Web metadata checks, if any, are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`. Imported prior searches are reports of other agents' work, not this agent's execution. Unsupported assertions are UNVERIFIED.

Online resolution pass 2026-10-31: the plan's attribution 'Koiran 2024 ... wide open two-matrix case' IS supported by the full text of arXiv:2401.01302 (Section 1.4), in the narrow sense stated in statement 223; the Step 0 FLAG (attribution not found) came from reading the abstract only and is superseded. Three tool fetches (PDF, PDF v1, HTML) agree on the sentence and on its referent. Web checks are logged in `topics/bivariate-lanczos-20261031/lit/search-log.md`, section 'Online resolution pass 2026-10-31'. Unsupported assertions remain UNVERIFIED.

## History

2026-10-31: Step 0 baseline record (AC-requested; not a novelty gate). Provisional IDs only; final `LIT-nnn` allocated at PR preparation.

2026-10-31 (online pass): full text searched; attribution SUPPORTED with narrow scope; statements 223-224 added; coverage upgraded; Step 0 flag preserved above as superseded.
