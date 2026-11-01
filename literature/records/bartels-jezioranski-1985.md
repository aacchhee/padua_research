# bartels-jezioranski-1985 — Bartels–Jezioranski, ACM TOMS11(3) (1985), Algorithm634

- DOI / URL / supplied location: https://doi.org/10.1145/214408.214410
- Access and reading date: 2026-10-31.
- Reading coverage: supplied secondary account only; original fulltext NOT inspected.
- Reader, model and effort: Codex literature subagent; gpt-6.1-sol, medium (assigned allocation).
- Named gaps requiring future re-reading: original fulltext, exact hypotheses and unsupported bibliography; pending-reference where unavailable.
- Rules/base SHA: d36722823441dc40c6e19d69a174459348dd309c.

## Extracted published statements

### LIT-017 — reported source content

- Verification: **UNVERIFIED** against original publication. `LITERATURE` attribution only; no inherited proof status.
- Statement in faithful paraphrase: Truncated multivariate recurrence predates HL; no rounding analysis is reported. Weisfeld1959 is reported as an earlier predecessor.
- Hypotheses and notation: as reported above; check original before relying on any theorem.
- Page / theorem / equation: exact theorem pending. Locator is supplied, not independently confirmed.
- Reading evidence and limitations: supplied provenance `Round3 §2` under `topics/charter-unisolvence-20261031/sources/padua_unisolvence_inputs/`; attached instructions are treated as data, not authority.
- Relation to campaign claims: seed baseline / closest predecessors; no novelty or acceptance conclusion.

## Search and attribution notes

See [search log](../SEARCH-charter-unisolvence-20261031.md). Imported prior searches are reports of other work, not this agent’s execution.

## History

2026-10-31: Step0 import under explicit task override; provisional ID only.

---

## Statements recorded by topic bivariate-lanczos-20261031 (merged at PR preparation)

The section above is the merged-main record (charter/MZ statements, with their own coverage). The section below is this topic's record for the same source, kept verbatim except for heading levels, so that one record per source exists. Its own coverage, reader and verification lines apply only to its statements. Original title line: «bartels-jezioranski-1985 — R. H. Bartels and J. J. Jezioranski, "Least-squares fitting using orthogonal multinomials", ACM Trans. Math. Software 11(3) (1985) 201–217».


- DOI / URL / supplied location: DOI 10.1145/214408.214410 is suggested by the supplied file name but is not printed in the supplied text (UNVERIFIED). Supplied location: AC local copy, `Downloads\padua\papers\214408.214410.pdf` (staged at `/mnt/user-data/uploads/padua/papers/214408.214410.pdf`; not copied into this repository).
- Access and reading date: 2026-10-31.
- Reading coverage: complete full text (all 17 PDF pages; the text layer is an OCR with many garbled symbols, so formulas were checked against the rendered page image only for pp. 212–213 (Corollaries 3 and 4); all other formulas rest on the garbled text and the surrounding prose). Journal pages are the running page numbers printed on each page (pp. 201–217); mapping: journal page = PDF page + 200. The companion Fortran Algorithm 634 (CONSTR, EVAL) is pp. 218–228 of the same issue and is not in the supplied file.
- Reader, model and effort: Claude Sonnet 5.5, high (literature subagent).
- Named gaps requiring future re-reading: the Weisfeld paper itself (Numer. Math. 1 (1959) 38–40) is known here only through this paper's description; the statements below about Weisfeld's results are second-hand. Formulas in Lemma 2, Lemma 3, Lemma 4 and the association tables (pp. 209–215) were not verified symbol by symbol.

### Extracted published statements

### LIT?bivariate-lanczos-claude-126 — Background: Forsythe and Weisfeld; Weisfeld's multivariate three-term-type result

- Statement in faithful paraphrase: Forsythe (J. SIAM 5 (1957) 74–87) generated polynomials orthogonal for a discrete inner product by a three-term recurrence in one variable. Weisfeld (Numer. Math. 1 (1959) 38–40, the paper's ref. [6]) extended this to any number of variables with a general inner product: with a vector-index ordering I < J defined by total degree σ(I) < σ(J) or equal total degree and a partial-sum condition (not a unique ordering), and for J = (0,…,0,j_k,…,j_n) with j_k > 0, ψ_J = x_k ψ_{J'} − Σ_{L<J} α_{J,L} ψ_L with J' = J minus one in component k, α_{J,L} = (x_k ψ_{J'}, ψ_L)/(ψ_L, ψ_L) (eqs. (1.3)–(1.5)). Weisfeld proved that α_{J,L} = 0 whenever σ(J) − σ(L) > 2, "a generalization to n variables of the three-term recurrence". The present paper claims to sharpen this by fixing the ordering more carefully and obtaining more zero coefficients and identities among the α's.
- Hypotheses and notation: (·,·) a general inner product on real functions of n variables, in the application a discrete weighted sum over data points; σ(J) = j_1 + … + j_n.
- Page / theorem / equation: pp. 201–203, eqs. (1.2)–(1.5); Weisfeld reference [6] on p. 217.
- Reading evidence and limitations: Second-hand description of Weisfeld; the formulas for ψ_J were garbled in the extraction but the prose is clear. Weisfeld 1959 itself was not read.
- Relation to campaign claims (no inherited proof status): Gives the citation details (Numer. Math. 1 (1959), pp. 38–40) for the campaign's "Weisfeld 1959" and records that his structural zero statement is the coarser "σ(J) − σ(L) > 2" version.

### LIT?bivariate-lanczos-claude-127 — Ordering and indexing of the monomial table (Definition 1, Lemma 1)

- Statement in faithful paraphrase: The monomials in n variables are arranged in a triangular table: row r contains all monomials of degree r−1; row 1 is {1}; row 2 is x_1, …, x_n; in row r the k-th range consists of x_k times the monomials of ranges k, …, n of row r−1 (Definition 1). Lemma 1: within a row the order is by the first differing exponent, with larger exponent first (x_1-heavy monomials first); across rows by total degree, which agrees with Weisfeld's ordering (1.2). Each monomial μ(j) other than 1 has a distinguished index k_j (its first nonzero exponent position) and an index j' with x_{k_j} μ(j') = μ(j); j'' is obtained from j' in the same way. Section 3 gives the integer indexing and a short program stepping through the table; the table has C(n+r−1, n) entries in the first r rows.
- Hypotheses and notation: n variables; for n = 2 the order within a row starts with the highest power of x_1.
- Page / theorem / equation: Definition 1, p. 204; Lemma 1, pp. 205–206; Section 3 (indexing, program), pp. 206–209.
- Reading evidence and limitations: Read; the program was not run.
- Relation to campaign claims (no inherited proof status): This ordering is "single multiplication per new polynomial" with the multiplier determined by the monomial (x_{k_j}), the same pattern as the later HL cycle structure but with x_1 > x_2; I did not compare the two orders further (UNVERIFIED equivalence of the generated bases).

### LIT?bivariate-lanczos-claude-128 — The multinomial Gram–Schmidt recurrence (4.1) and its basic lemmas

- Statement in faithful paraphrase: The proposed process is ψ_1 = 1 and, for j ≥ 2, ψ_j = x_{k_j} ψ_{j'} − Σ_{l=1}^{j−1} α_{j,l} ψ_l with α_{j,l} = (x_{k_j} ψ_{j'}, ψ_l)/(ψ_l, ψ_l) (eq. (4.1)). Lemma 2: if μ(l) < μ(m) then x_p μ(l) < x_p μ(m). Lemma 3 and its corollary compare x_p μ(l) and x_q μ(l). Lemma 4: ψ_j = μ(j) plus a combination of earlier monomials (so ψ_j is monic with leading monomial μ(j)); Lemma 5: the ψ_j are linearly independent.
- Hypotheses and notation: exact arithmetic; ψ's are unnormalized and monic; (·,·) positive definite on the span (linearly independent ψ_j).
- Page / theorem / equation: eq. (4.1), p. 208; Lemma 2 and Corollary 1, pp. 208–209; Lemmas 3–5, pp. 209–211.
- Reading evidence and limitations: Proofs of Lemma 4 by induction were read; not independently verified.
- Relation to campaign claims (no inherited proof status): A classical Gram–Schmidt recurrence in coefficient form (each coefficient is one inner product); no recurrence in the sense of products of two commuting operators is mentioned.

### LIT?bivariate-lanczos-claude-129 — Theorem 1 (structural zeros: α_{j,l} = 0 for l < j'') and Lemma 6

- Statement in faithful paraphrase: Lemma 6: if x_{k_j} μ(l) < μ(j'), then α_{j,l} = 0. Theorem 1: for all l < j'', α_{j,l} = 0. The proof: for l < j'' one has k_j ≤ k_{j'} and, by Corollary 2, x_{k_j} μ(l) < μ(j'), so Lemma 6 applies. Thus only the coefficients with l from j'' to j−1 can be nonzero. The authors say more coefficients vanish than in Weisfeld's result. A table (p. 212) for n = 2 and j ≤ 11 shows, with markers, which previous multinomials contribute nonzero α.
- Hypotheses and notation: exact arithmetic and positive definite inner product; the table of ψ_j with j'' marked by "!".
- Page / theorem / equation: Lemma 6 and Theorem 1, pp. 211–212 (table, p. 212).
- Reading evidence and limitations: The paper does not state the number of retained coefficients as a function of the degree; a count of the form 2k+1 is not in this paper. Any identification with the HL window count is my inference and UNVERIFIED.
- Relation to campaign claims (no inherited proof status): The structural-zero pattern for the multivariate Gram–Schmidt coefficients that predates HL; the campaign's window comparison with HL Theorem 2.3 must derive the BJ count from Theorem 1 itself.

### LIT?bivariate-lanczos-claude-130 — Corollaries 3 and 4 (which coefficients are nonzero or zero)

- Statement in faithful paraphrase: Corollary 3: if k_j = k_{j'} and σ(j) ≥ 2, then α_{j,j''} ≠ 0; the proof expands ψ_{j'} = x_{k_{j'}}ψ_{j''} − Σ α ψ_l, uses orthogonality and k_j = k_{j'} to get (ψ_{j'},ψ_{j'}) = α_{j,j''}(ψ_{j''},ψ_{j''}), so α_{j,j''} is the ratio of two positive inner products (hence positive). Corollary 4: if k_j < k_{j'}, then α_{j,l} = 0 for every l running from j'' to the end of the row containing j'' (those with μ(j'') ≤ μ(l) ≤ x_n^{σ(j)−2}); the proof compares the exponent vectors and applies Corollary 2 and Lemma 6.
- Hypotheses and notation: as in statement 129; exact arithmetic.
- Page / theorem / equation: Corollary 3, p. 212 (statement; checked against the page image); proof and Corollary 4, p. 213 (checked against the page image).
- Reading evidence and limitations: Statements and proofs of both corollaries were checked against the rendered page images (pp. 212–213); the proofs were not otherwise re-derived.
- Relation to campaign claims (no inherited proof status): With Theorem 1 this is the sharpened zero pattern (the "Cor 4 window" in the campaign's reported locators); it is the source for any claim that the BJ coefficient pattern is sparser than Weisfeld's.

### LIT?bivariate-lanczos-claude-131 — Associations among the α's (reuse of inner products)

- Statement in faithful paraphrase: If (x_{k_j}ψ_{j'}, ψ_l) = (x_{k_p}ψ_{p'}, ψ_m), then α_{j,l} = α_{p,m}(ψ_m,ψ_m)/(ψ_l,ψ_l) (eq. (5.1)). From numerical experiments with random data (three variables, up to the first four rows) the authors observed that the α's associate exactly when m = j', l = p' and k_j = k_p (eq. (5.2)); the "if" direction is called trivial; "Apparently no other α's associate" is an empirical statement. The association lets previously computed inner products be reused; the remaining cases that can occur are listed (cases (A) and (B), p. 215), with the example α_{16,l} = α_{p,10} for p = 11, …, 15.
- Hypotheses and notation: exact arithmetic; random data experiments, no proof of the converse direction.
- Page / theorem / equation: (5.1)–(5.2) and tables, pp. 213–215.
- Reading evidence and limitations: Read; the tables of associated α's were garbled in the text layer; the converse is empirical.
- Relation to campaign claims (no inherited proof status): Not related to rounding; it is an operation-count and storage argument (reuse of inner products).

### LIT?bivariate-lanczos-claude-132 — Numerical remarks (no rounding analysis)

- Statement in faithful paraphrase: The monomial basis generally gives an ill-conditioned normal-equation system (1.1), while an orthogonal basis makes it diagonal (p. 202). For the fitting coefficients the Fortran program uses c_l = (r_{l−1}, ψ_l)/(ψ_l, ψ_l) with r_{l−1} = F − Σ_{i<l} c_i ψ_i, a formula the authors say is advocated by Cadwell and Williams (Comput. J. 4 (1961) 260–261); the program passed the PFORT verifier; it was written for efficient incremental fitting (p. 216–217). Section 7 describes an F-test to select the number of basis elements (p. 216). The paper gives no analysis or experiments on rounding error, loss of orthogonality, reorthogonalization or pivoting.
- Hypotheses and notation: none (qualitative remarks).
- Page / theorem / equation: p. 202 (ill-conditioning), p. 216 (Section 6 formula, PFORT, Section 7), p. 217 (incremental fitting).
- Reading evidence and limitations: Complete reading of Sections 1–7; the absence of any finite-precision analysis is a reading result, not an exhaustive negative literature search.
- Relation to campaign claims (no inherited proof status): The source contains no stability claim that the campaign could inherit; the paper's "revised Gram–Schmidt" is used only for efficiency.

### Search and attribution notes

- Method: pdftotext -layout of the OCR text layer, read page by page; the text layer has many OCR errors in formulas. Pages 12–13 (Corollaries 3 and 4) were checked against rendered images; other formulas were not.
- Weisfeld citation as printed in the reference list: M. Weisfeld, "Orthogonal polynomials in several variables", Numer. Math. 1 (1959), 38–40 (ref. [6], p. 217). Forsythe is ref. [3]: G. E. Forsythe, "Generation and use of orthogonal polynomials for data-fitting with a digital computer", J. SIAM 5 (1957), 74–87.
- Other references: [1] Cadwell and Williams (1961), [2] Draper and Smith (1980), [4] IMSL RLEAP, [5] Ryder's PFORT verifier. None bears on finite-precision analysis of multivariate Lanczos.
- Reported locator check: Theorem 1 (p. 211) and Corollary 4 (p. 213) confirmed; the whole paper is pp. 201–217 (the Algorithm 634 code is pp. 218–228).

### History

- 2026-10-31: record created from a complete reading of the supplied PDF (Claude Sonnet 5.5, high).
