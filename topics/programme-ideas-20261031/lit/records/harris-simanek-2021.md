# harris-simanek-2021 — L. A. Harris and B. Simanek, "Interpolation and cubature for rectangular sets of nodes", Proceedings of the American Mathematical Society 149(8) (2021) 3485–3497

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator)

- DOI / URL / supplied location: DOI 10.1090/proc/15414 (printed on the first page). Supplied location: AC local copy `/home/claude/inputs/papers/S0002-9939-2021-15414-2.pdf` (AMS version licensed to NTNU; not copied into the repository).
- Access and reading date: 2026-10-31.
- Reading coverage: exact pages — p. 3485 (hypotheses and node definitions), pp. 3488–3489 (Theorem 1, Corollary 2, Conjecture 3 and the computer-verification remark) and the statement of Theorem 5 (p. 3491) read from the `pdftotext -layout` text layer; the Lagrange-polynomial formulas (eqs (9)–(14)), the cubature weights of Theorem 5, §4 (proof of Theorem 1) and Appendix A not read. Mapping: journal page = PDF page + 3484.
- Reader, model and effort: Claude Fable 5.1, xhigh (programme-ideas Step-0 literature subagent).
- Named gaps requiring future re-reading: the explicit kernel/Lagrange formulas and where positivity of the kernel terms is used in the proof (the charter branch's partial inspection of the author-hosted draft says positivity is used explicitly); the cubature weight formula in Theorem 5; whether the hypothesis "arranged in decreasing order" is needed for Theorem 1 as opposed to the cubature; the §3 remarks on minimal degree.
- Shared key: `records_charter/harris-simanek-2021.md` (LIT-001, secondary plus a partial primary inspection of an author-hosted draft) and `records_lanczos/harris-simanek-2021.md` (LIT?bivariate-lanczos-claude-070/-071, secondary). Merge at PR preparation; this record adds the first check of the published AMS pagination.

## Extracted published statements

### LIT?programme-ideas-claude-52 — fact: hypotheses, even-odd rectangular nodes, Theorem 1, Corollary 2, Theorem 5

- Statement in faithful paraphrase: X = {h_0, …, h_m} and Y = {h̃_0, …, h̃_{m+σ}} are sets of distinct real numbers arranged in decreasing order, m ≥ 1, σ ≥ 0; the rectangle N^σ_m = X × Y has (m+1)(m+σ+1) points, too many for degree-m Lagrange polynomials, so the paper takes the even and odd checkerboard subsets N^σ_{m,0}, N^σ_{m,1} (i − j even, resp. odd). Theorem 1 (σ = 1): the polynomials G^σ_m define Lagrange polynomials of degree m for N^1_{m,k}, k = 0, 1, and there are no other Lagrange polynomials if all are required to have degree at most m; the σ = 0 analogue is in Harris's earlier work and the σ = 1 Morrow–Patterson case in an earlier paper, and this note proves it for arbitrary even-odd product nodes. Corollary 2: G^1_{m+σ−1} gives Lagrange polynomials of degree m + σ − 1 for N^σ_{m,k} when σ ≥ 1 (by nesting N^σ_{m,k} ⊆ N^{σ−1}_{m+1,k}). Theorem 5 (σ = 1): for any polynomial p of degree at most 2m − 1, the product integral of p against dμ(s)dμ̃(t) equals Σ λ_{n,q} p(h_n, h̃_q) over the nodes of N^1_{m,k}, with explicit λ_{n,q}. The text before Theorem 1 observes that G^σ_m(u,v,u,v) > 0 because every term of the kernel sums is a nonnegative square and the first is positive.
- Hypotheses and notation: distinct real nodes in decreasing order; orthogonal polynomials p_i, p̃_j with norms H_i, H̃_j for measures μ, μ̃ whose Gauss-type nodes are X, Y (notation (9), not read); K_{m−1} the reproducing kernel; Γ_m a correction term.
- Page / theorem / equation: node definitions p. 3485 (PDF p. 1); positivity remark, Theorem 1, pp. 3488 (PDF p. 4); Corollary 2 p. 3489 (PDF p. 5); Theorem 5 p. 3491 (PDF p. 7).
- Reading evidence and limitations: Text layer only, formulas partly garbled; the Theorem 5 weight formula was not transcribed. The page numbers given in the charter record (Thm 1 pp. 3488–3489; Cor. 2, Conj. 3 p. 3489; Thm 5 pp. 3490–3491) are consistent with mine.
- Relation to campaign claims (no inherited proof status): Fixes the published hypotheses (ordered real nodes) behind RESULTS.md's correction that unisolvence is not field-independent; the Padua points are the σ = 1 Chebyshev–Lobatto instance (per the round-2 note, not stated on the pages read).

### LIT?programme-ideas-claude-53 — open problem (author-stated conjecture): Conjecture 3

- Statement in faithful paraphrase: Conjecture 3: the polynomials G^σ_m define Lagrange polynomials of degree m + ⌊σ/2⌋ for N^σ_{m,k} when σ ≥ 1 and k = 0, 1. The authors verified it by computer for m, σ = 1, …, 15 and k = 0, 1 with randomly chosen rational node sets in decreasing order (Maple 2017, RandomTools), and ask whether the minimal-degree property of Theorem 1's Lagrange polynomials also holds for those of the conjecture.
- Hypotheses and notation: as above; random rational nodes from a symmetric interval, arranged in decreasing order.
- Page / theorem / equation: Conjecture 3 and the verification paragraph, p. 3489 (PDF p. 5); the minimal-degree question is reported by the round-2 note at p. 3489 (not re-read here).
- Reading evidence and limitations: Text layer. The charter branch records (LIT-033) that Cao–Ghimire–Wang, Proc. AMS 150 (2022) 2153–2163, prove this conjecture; that paper is not in the local input set and is UNVERIFIED here.
- Relation to campaign claims (no inherited proof status): The Padua reports treat Conjecture 3 as open (round-2 ingest note); if the charter branch's reading of Cao–Ghimire–Wang is right, any programme candidate must not cite it as open.

## Search and attribution notes

No web search in this step. Attribution flag for the orchestrator: the Padua inputs (`research_notes/Open problems verification/ingest_nodes_cubature_papers.md` line 89) list Conjecture 3 as open; the charter branch's LIT-033 says it was proved in 2022. Resolve at PR preparation by reading Cao–Ghimire–Wang.

## History

- 2026-10-31: record created from a text-layer reading of pp. 3485, 3488–3489 and the Theorem 5 statement (claude-fable-5-1, xhigh).
