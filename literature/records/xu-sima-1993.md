# xu-sima-1993 — Y. Xu, On multivariate orthogonal polynomials, SIAM J. Math. Anal. 24(3) (1993) 783–794, doi:10.1137/0524048

- DOI / URL / supplied location: [doi:10.1137/0524048](https://doi.org/10.1137/0524048); journal page https://epubs.siam.org/doi/10.1137/0524048 (built from the DOI, not page-checked). Supplied location: AC's copy `~/Downloads/padua/papers/0524048.pdf` (staged by the orchestrator as `/mnt/user-data/uploads/padua/papers/0524048.pdf`). DOI, volume, issue and pages: Crossref check by the P3 link subagent 2026-11-03 (`p3-links.md`, item 8c); the first page of the PDF prints SIAM J. Math. Anal. 24(3), pp. 783–794, May 1993.
- Access and reading date: 2026-11-03.
- Reading coverage: exact pages 783–790 (Sections 1–4 and the statement of Theorem 4 in Section 4/5), read from the PDF text layer (`pdftotext`; symbols partly garbled, displays read for structure only). Pages 790–794 (proof of Theorem 4, Section 5 kernel function, Section 6 examples, references) NOT read except headings.
- Reader, model and effort: P3 literature reader, Claude Opus 5.5 (claude-opus-5-5), high.
- Named gaps requiring future re-reading: displays (3.3)–(3.8) were garbled in extraction; check them on a page image before quoting any formula. Sections 5–6 not read.

## Extracted published statements

### LIT?padua-literature-claude-40 — Kowalski's theorem as restated (Theorem K): Favard-type characterisation with a single stacked recurrence

- Statement in faithful paraphrase: For a sequence of polynomial vectors P_k (k ≥ 0) in d variables, the following are equivalent: (1) the P_k form a basis and some linear functional with L(1) = 1 is a quasi-inner product making them orthogonal; (2) there are unique stacked matrices A_k, B_k, C_k with rank A_k = r_{k+1}, x P_k = A_k P_{k+1} + B_k P_k + C_k P_{k−1} (x ⊗ P_k stacked over coordinates), and, for any left inverses D_k of A_k, a stated recursion produces nonsingular symmetric matrices.
- Hypotheses and notation: quasi-inner product = a real linear functional that is nonzero exactly on the squares of the elements of some basis (no positivity); r_k = dim of the space V_k of degree-k orthogonal polynomials.
- Page / theorem / equation: p. 785, Theorem K (attributed to Kowalski 1982).
- Reading evidence and limitations: PDF text layer; the recursion in (2)(c) is garbled in extraction and is paraphrased only at the level of "nonsingular symmetric matrices".
- Relation to campaign claims (no inherited proof status): background for PD-T057 (truncated Favard theorem). Quasi-inner products, full infinite sequences.

### LIT?padua-literature-claude-41 — Theorem 1 and Corollary 1: coordinate-wise three-term relation, moment identities, rank conditions

- Statement in faithful paraphrase: If {P_k} is an orthogonal basis for a quasi-inner product L, then for each k ≥ 0 and each coordinate i there are unique matrices A_{k,i} (r_k × r_{k+1}), B_{k,i} (r_k × r_k), C_{k,i} (r_k × r_{k−1}) with x_i P_k = A_{k,i} P_{k+1} + B_{k,i} P_k + C_{k,i} P_{k−1}. With H_k = L(P_k P_kᵀ) (invertible), the coefficients are given by moment identities (A_{k,i}H_{k+1} and B_{k,i}H_k equal moments of x_i P_k against P_{k+1}, P_k), and A_{k,i}H_{k+1} = H_k C_{k+1,i}ᵀ. A second recursion P_{k+1} = Σ_i x_i D_{k,i}ᵀ P_k + E_k P_k + F_k P_{k−1} exists (Kowalski's form), with Σ_i D_{k,i}ᵀ A_{k,i}ᵀ = I. Corollary 1: the stacked A_k and C_{k+1} have rank r_{k+1}, and each A_{k,i}, C_{k+1,i} has rank r_k. The paper remarks that the D_{k,i} are not unique for d > 1, nothing seems to be sayable about their individual ranks, and some may vanish for large d.
- Hypotheses and notation: quasi-inner product; for an inner product, B_{k,i}H_k is symmetric.
- Page / theorem / equation: pp. 785–786, Theorem 1, eqs. (3.2)–(3.8); Corollary 1, eqs. (3.9)–(3.11), p. 786; remark on D_{k,i}, pp. 786–787.
- Reading evidence and limitations: PDF text layer; exact form of (3.3)–(3.5) not transcribed.
- Relation to campaign claims (no inherited proof status): the coordinate-wise relation is the exact-arithmetic object behind the window recurrence (PD-T029, PD-T036) and the "one relation per polynomial" selections (the non-uniqueness of D_{k,i} is the published counterpart of the selection freedom studied in PD-T037, PD-T143). It contains no finite-precision content.

### LIT?padua-literature-claude-42 — Theorem 2: Favard theorem for quasi-inner products (rank conditions suffice)

- Statement in faithful paraphrase: For an arbitrary sequence {P_k} of polynomial vectors, the following are equivalent: (1) some linear functional is a quasi-inner product making {P_k} an orthogonal basis; (2) for every k and i there are matrices A_{k,i}, B_{k,i}, C_{k,i} with (a) rank A_k = r_{k+1} and rank C_{k+1} = r_{k+1} (stacked), and (b) x_i P_k = A_{k,i}P_{k+1} + B_{k,i}P_k + C_{k,i}P_{k−1} for all i. The paper compares it with Favard's theorem in one variable and notes that an integral representation of such functionals is given elsewhere.
- Hypotheses and notation: the P_k are given polynomials (so the relations for different i are automatically consistent); no positivity; no commuting conditions are stated as hypotheses, because consistency is built into the existence of the polynomial sequence.
- Page / theorem / equation: p. 787 (statement), proof pp. 787–788.
- Reading evidence and limitations: PDF text layer; statement heading partly garbled ("THEOREM" without number in extraction; numbering by sequence: Theorem 2).
- Relation to campaign claims (no inherited proof status): RELATED to PD-T057(b): PD-T057(b) starts from a structured matrix pair (not from given polynomials), assumes interior commutativity, works on Π_{2n+1} with the last block free, and concludes a positive-definite moment matrix and the words formula; Xu's Theorem 2 needs the full infinite polynomial sequence and concludes only a quasi-inner product.

### LIT?padua-literature-claude-43 — Theorems 3–4: Christoffel–Darboux formula and basis independence of the kernel

- Statement in faithful paraphrase: Theorem 3 gives a multivariate Christoffel–Darboux formula for sequences satisfying the coordinate-wise three-term relation; Theorem 4 states that the reproducing kernel built from the V_k (via a quasi-inner product) depends only on the spaces V_k, not on the chosen bases.
- Hypotheses and notation: as in Theorem 1.
- Page / theorem / equation: Theorem 3 p. 788 (eq. (4.1)); Corollary p. 789; Theorem 4 pp. 789–790.
- Reading evidence and limitations: statements only; proofs of Theorem 4 not read; formulas not transcribed.
- Relation to campaign claims (no inherited proof status): background only (the Padua Lebesgue-function pack uses the Padua kernel from other sources).

## Search and attribution notes

No previous record or INDEX row for this paper (`p3-links.md` item 8c). The paper discusses no commuting conditions on the coefficient blocks; the published commuting conditions used by the campaign are in Xu, Trans. AMS 343 (1994), Corollary 2.3 (record `xu-tams-1994-operator`, digest-level only) and in the Liu–Narayan statement of them (Theorem 2.1 there, credited to zu Castell–Filbir–Forster; see `liu-narayan-2023.addendum.md`). Text extracted with `pdftotext` into the scratchpad; no PDF text is committed.

## History

2026-11-03: new record (padua-literature-20261103, P3 reader, Claude Opus 5.5 high); AC-supplied PDF read, pp. 783–790.
