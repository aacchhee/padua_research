# simonova-tichy-2025 — addendum (padua-literature-20261103, P3)

Addendum to `literature/records/simonova-tichy-2025.md`. D. Šimonová, P. Tichý, On finite precision block Lanczos computations, BIT Numer. Math. 65(4) (2025), article 47, [doi:10.1007/s10543-025-01089-2](https://doi.org/10.1007/s10543-025-01089-2); free version [arXiv:2507.16484](https://arxiv.org/abs/2507.16484).

- Access and reading date: 2026-11-03.
- Version read: arXiv v1 (22 Jul 2025; the PDF footer prints `arXiv:2507.16484v1`). The BIT version of record was NOT read; the version differences remain a gap.
- Reading coverage: exact PDF pages 1–5 (abstract, §1, §2 to §2.1), 10–20 (end of §3, §4, §5 with Theorems 1–4 and proofs, §6.1), 23–26 (end of §6.3, §7 conclusions, references). Pages 6–9 (§2.1 interlacing, §2.2 improper clusters, §3 block CG experiment) and 21–22 (§6.2) NOT read. Text extracted with pdf.js in the built-in browser from the arXiv PDF; formulas read from the text layer (garbling small; subscripts flattened).
- Reader, model and effort: P3 literature reader, Claude Opus 5.5 (claude-opus-5-5), high.
- Named gaps: BIT version; §§2.1–2.2 (interlacing conjecture); §6.2 implementation details.

## Extracted published statements

### LIT?padua-literature-claude-44 — Theorem 1: eigenvalue spread of a perturbed block Lanczos extension (conditional)

- Statement in faithful paraphrase: Let T_N be the block tridiagonal matrix of a perturbed block Lanczos recurrence A V_N = V_N T_N + [ΔV_{k−1}, ΔṼ_{N−k+1}] with β_{N+1} = 0, every perturbation column block bounded by ε₂‖A‖. Suppose ε₁ > 0 is such that every Ritz pair of T_N whose Ritz vector has norm below 1/2 has another Ritz pair with Ritz-vector norm at least 1/2 and Ritz value within ε₁‖A‖. Then every eigenvalue of T_N lies within 3·max(√N ε₂, ε₁)‖A‖ of an eigenvalue of A.
- Hypotheses and notation: A real symmetric n × n; block vectors of p columns; the Ritz-vector condition (15) is an explicit additional assumption, introduced because (p. 13) a comprehensive finite-precision block Lanczos theory is lacking; the authors call the existence of a small ε₁ difficult to establish theoretically (p. 14) and observe it numerically.
- Page / theorem / equation: p. 13, Theorem 1, eqs. (14)–(16); proof pp. 13–14, eqs. (17)–(18); summary paragraph p. 14.
- Reading evidence and limitations: statement and proof read; elementary proof (norm of Ritz vectors ≥ 1/2 gives 2√N ε₂).
- Relation to campaign claims (no inherited proof status): the block analogue of the Paige theorem that Greenbaum's construction feeds (`greenbaum-1989.addendum.md`, statement 57). One operator.

### LIT?padua-literature-claude-45 — Continuation process, Theorems 2–4, and the open bounding step

- Statement in faithful paraphrase: After k finite-precision block Lanczos steps, the recurrence is continued by orthogonalising each new block against an orthonormal W_k (QR factor of m selected Ritz vectors), the first continuation block, and the previous block (eq. (19)). Theorem 2: the continuation vectors together with W_k are orthonormal, and the subdiagonal blocks satisfy the exact Lanczos formula from the third continuation step on. Theorem 3: the continuation is a perturbed block three-term recurrence (21) with explicit perturbations h_{k+j} (22). Theorem 4: under the standard local bounds (8), (9), (11), (12), the perturbations are W_k W_kᵀ v_{k+1}β_{k+1} plus O(ε)‖A‖ (j = 0), a term involving W_k R_k^{−T} S_mᵀ r_k β_{k+1}ᵀ (j = 1), and q_{k+1}β_{k+1}v_kᵀq_{k+j} (j ≥ 2), each with remainders bounded by (1 + ρ_k)(‖h_k‖ + O(ε)‖A‖), ρ_k = ‖R_k^{−1}‖. Sufficient conditions for small perturbations (p. 19): v_{k+1} nearly orthogonal to the selected Ritz vectors, the columns of v_k nearly in their span ((35), (36)), and the second term of (35) small. In the single-vector case Greenbaum bounds that second term using a lemma of Paige (Greenbaum 1989, p. 32); in the block case the authors state that bounding it remains open (p. 19), and that no theory guarantees a choice of selected Ritz vectors making (35)–(36) small.
- Hypotheses and notation: the local bounds (9), (11), (12) on the computed block recurrence are attributed to an unpublished report of Carson and Chen (2022) and a thesis in preparation (p. 11); they are shown numerically (Fig. 2), not proved in the paper. Fixed block width p with dim K_k(A, v) = kp assumed (p. 4); rank deficiency in the continuation reduces the block size (pp. 14–15). W_k is the only free parameter (p. 16).
- Page / theorem / equation: §5.1 pp. 14–16 (eq. (19), Theorems 2–3, eqs. (20)–(24)); §5.2 pp. 16–19 (Theorem 4, eqs. (25)–(36)); §6.1 p. 20 (heuristic selection δ_{k,i} > μ‖A‖, eq. (37)).
- Reading evidence and limitations: statements read; Theorem 4 proof skimmed (pp. 17–18), not checked line by line.
- Relation to campaign claims (no inherited proof status): the closest published "Greenbaum-type" model beyond one vector. It concerns one symmetric operator with a fixed-width block start; it does not treat several commuting operators, a single start vector with several operators, growing blocks, or a moment/measure formulation.

### LIT?padua-literature-claude-46 — What the experiments show and what the authors claim as open

- Statement in faithful paraphrase: The block CG analogue of the Greenbaum–Strakoš experiment matches model systems with eigenvalue intervals of size comparable to ε‖A‖ (p. 10). In the continuation experiments the sufficient conditions held with a tolerance of order 10^−5 and the observed eigenvalue spread of T_N around A's eigenvalues was typically O(√ε)‖A‖, often smaller (p. 24); assumption (15) always held with ε₁ several orders below ε₂ (p. 23). Conclusions (pp. 24–25): the key open question is how to choose W_k; Paige's results have not been generalised to the block case; a rigorous justification needs block analogues of Paige's results.
- Hypotheses and notation: test matrices "strakos48" family (n = 48, ρ = 0.8), p = 2 (similar for p = 3–5), Householder QR (p. 11).
- Page / theorem / equation: pp. 10, 11–12 (Fig. 2), 23, 24–25.
- Reading evidence and limitations: read; numbers are the authors' reports.
- Relation to campaign claims (no inherited proof status): supports the repo's wording that finite-precision Greenbaum-type theory beyond one vector is open (PD-T056 reading (G) OPEN).

### LIT?padua-literature-claude-47 — Location check of the two author statements (LIT-082, LIT-235)

- Statement in faithful paraphrase: The "challenging and requires further research" statement about generalising Paige's analysis is in §1 (p. 3); the "comprehensive theory ... still lacking" statement is in §5 (p. 13), just before Theorem 1. The §4 opening (p. 10) adds that no generalisation of Paige's analysis is known to the authors and that it appears non-trivial.
- Page / theorem / equation: pp. 3, 10, 13.
- Reading evidence and limitations: located in the pdf.js text; quotations kept under 15 words in the existing records.
- Relation to campaign claims (no inherited proof status): upgrades LIT-082 and LIT-235 from digest to page-located.

## Corrections and upgrades (old → new)

- LIT-081: "abstract-checked only" → statement verified against arXiv v1 abstract (p. 1) and §5 (pp. 13–19). Coverage: exact pages listed above.
- LIT-082: UNVERIFIED (reported) → located: §1 p. 3; §5 p. 13; conclusions p. 24 (W_k open question).
- LIT-234: "tool digest" → pdf.js text of arXiv v1, pp. 13–20. Content confirmed, with one hypothesis made explicit: Theorem 4 assumes the local bounds (8)–(12), which the paper attributes to Carson–Chen (unpublished) and does not prove. Formulas (21), (35), (36) now seen (pp. 15, 19).
- LIT-235: digest → page-located (pp. 3, 13).
- Coverage line of the record: "arXiv v1 text via tool digests" → add "pdf.js text, exact PDF pages 1–5, 10–20, 23–26 (2026-11-03)".

## History

2026-11-03: addendum by the P3 reader (Claude Opus 5.5 high), padua-literature-20261103.
