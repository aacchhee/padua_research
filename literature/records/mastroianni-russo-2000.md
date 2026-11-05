# mastroianni-russo-2000 — G. Mastroianni, M. G. Russo, Weighted Marcinkiewicz inequalities and boundedness of the Lagrange operator

- Citation: in Th. M. Rassias (ed.), *Mathematical Analysis and Applications*, Hadronic Press, Palm Harbor FL, 2000, pp. 149–182. No DOI. [zbMATH 0997.42001](https://zbmath.org/1594022).
- DOI / URL / supplied location: print-only volume. AC supplied a 34-page typeset copy, `Downloads\padua\papers\MastroianniRussoVolRassias.pdf`, staged to the session on 2026-11-05. The copy carries no printed page numbers. Its 34 pages match the 34-page range 149–182, so the page locators below are given as "copy p. k (book p. 148+k, inferred)".
- Access and reading date: 2026-11-05.
- Reading coverage:
  - §1 (copy pp. 1–3) and §3 "The algebraic case" (copy pp. 16–28: definitions, Theorems 8–12, the remark after Theorem 10, the applications, Corollaries 13 and 18, Theorems 14–17) were read in the text layer.
  - Copy pp. 22–23 (the two-system construction, Theorems 11–12) were read from page images, because the text layer garbles the hypotheses.
  - §2 (trigonometric case, Theorems 1–7) and the Appendix proofs of Theorems 11–12 (copy pp. 28–33) were only screened.
  - The whole text was searched for "log": it occurs only in a funding line. The paper states no logarithmic or other rate-type estimate.
- Reader, model and effort: Claude, Opus 5.5 (configured claude-opus-5-5). Rules `440d107`.
- Named gaps: the book-page mapping is inferred; proofs of Theorems 9–12 were not checked line by line.

## Extracted published statements

### LIT?padua-literature-claude-85 — weighted algebraic Marcinkiewicz inequalities with uniform constants under doubling / A_p hypotheses; no rates

- Statements in faithful paraphrase:
  - **Theorem 8** (copy p. 17, book p. 165 inferred). Forward inequality. For u^p doubling, 1 ≤ p < ∞, and nodes −1 = y₁ < … < y_m = 1 with angular gaps ∼ 1/m (endpoints included), the sum Σ λ_m(u^p, y_i)|P(y_i)|^p is at most C ∫|Pu|^p for every P of degree ≤ lm (l fixed). C depends on the doubling constant. The paper credits the type to Askey, Nevai and Lubinsky–Máté–Nevai.
  - **Theorem 9** (copy p. 18). Converse inequality at Gauss nodes. Let x_k be the zeros of p_m(w), with w in GDT (generalized Ditzian–Totik, eq. (45)), u^p doubling, and u/√(wφ) ∈ A_p, where φ = √(1−x²). Then ‖Pu‖_p ≤ C(Σ λ_m(u^p, x_k)|P(x_k)|^p)^{1/p} for P of degree ≤ m − 1.
  - **Theorem 10** (copy pp. 19–22). A "weak" variant with v = max{u^p, √(wφ), 1} and a bumped A_p-type condition.
  - **Theorem 11** (copy p. 23, book p. 171 inferred; hypotheses read from the page image). The "extended" converse inequality.
    - Nodes: let w̄ = (1−x²)w. The nodes are the 2m+1 zeros of p_{m+1}(w)p_m(w̄), together with ν points equispaced in [−1, t_{ν+1}) starting at −1 and μ points in (t_{2m+1+ν}, 1] ending at 1 (definition, copy p. 22).
    - Hypotheses: w ∈ GDT, u^p doubling, 1 < p < ∞, and **((u/w) σ^{(μ−1,ν−1)})^p ∈ A_p**, where σ^{(α,β)} = (1−x)^α(1+x)^β.
    - Conclusion: ‖Pu‖_p ≤ C(Σ_{k=1}^{2m+μ+ν+1} λ_m(u^p, t_k)|P(t_k)|^p)^{1/p} for every P of degree ≤ 2m+μ+ν.
    - The paper credits the generalized-Jacobi case to its reference [5].
  - **Theorem 12** (copy p. 23). The weak extended variant.
  - **Applications** (copy pp. 24–28): Corollaries 13 and 18 give boundedness of (extended) Lagrange operators from C⁰ to L^p_u with a uniform constant; Theorems 14–17 give Sobolev/Besov error estimates of order m^{−r}.
  - The remark after Theorem 10 (copy p. 22) says that for the Chebyshev weight of the first kind, Theorems 9–10 are the algebraic versions of the trigonometric Theorems 3–4.
- Hypotheses and notation: λ_m(w, x) is the Christoffel function, with λ_m ∼ Δ_m(x) w_m(x) by eq. (50), where Δ_m(x) = √(1−x²)/m + 1/m². Every constant is unspecified and uniform in m. All conditions are of Muckenhoupt A_p or doubling type, so they are open conditions at power-weight endpoints.
- Reading evidence and limitations: as in the coverage line. The hypotheses of Theorems 11–12 were confirmed on the page image, because the text layer drops the bar on w̄ and misplaces σ.
- Relation to campaign claims (no inherited proof status; the routine specialization below is this reader's, not the source's):
  - **Clenshaw–Curtis nodes are an instance of the Theorem 11 construction for even N.**
    - Take w = (1−x²)^{−1/2}, so that w̄ = (1−x²)^{1/2}. Then p_{m+1}(w) ∝ T_{m+1} and p_m(w̄) ∝ U_m.
    - Their zeros, cos((2i−1)π/(2m+2)) and cos(2iπ/(2m+2)), together form {cos(jπ/(2m+2)) : 1 ≤ j ≤ 2m+1}.
    - With μ = ν = 1 the added points are exactly ±1. So {t_k} is the Chebyshev–Lobatto (CC) node set with N = 2m+2, and the polynomial space is P_{2m+2} = Π_N, the full space.
    - For u ≡ 1 and p = 2 the hypothesis reads (1−x²) ∈ A_2. A power weight |1∓x|^a is in A_2 on [−1,1] only for −1 < a < 1, so **the CC/Lebesgue/p = 2 case is exactly the excluded endpoint a = 1**. Theorem 11 therefore gives no bound there.
    - This matches PD-T019 and the classical full-space failure recorded from Mastroianni–Milovanović–Notarangelo (LIT-299; translation T6 of `topics/mz-prior-art-20261101/translation.md`).
  - Theorem 8 at CC nodes with u ≡ 1, p = 2 gives boundedness of the upper MZ constant with an unspecified constant. Christoffel numbers are ∼ Δ_m, which is comparable to the CC weights by translation T3. This is the same information as Lubinsky–Máté–Nevai 1987, already recorded.
  - **Verdicts:** PD-T014/PD-T022 (λ_+ < 2, explicit) RELATED (implies only uniform boundedness, already classical). PD-T017/PD-T018/PD-T019 (two-sided endpoint order (1+log N)^{−2}, every N, Π_{N−1}): RELATED, DIFFERENT SETTING; the paper has sufficient conditions with uniform constants, no rate, and no necessity statement, and the CC case sits exactly at its excluded endpoint. PD-T023/PD-T024: RELATED (no fixed-ratio statement).
  - This closes the gap the MZ prior-art report named, that this book chapter was "the most likely remaining place" for a quantitative borderline result. **No matching result was found in it.**

## Search and attribution notes

The reference list (47 items, copy pp. 33–34) includes Nevai, Lubinsky–Máté–Nevai, Mastroianni–Totik and Xu JAT 76 (1994). It was checked for a quantitative borderline result at Lobatto or CC nodes: none is cited for one.

## History

2026-11-05: created from the AC-supplied copy. Provisional ID LIT?padua-literature-claude-85, within this topic's reserved LIT range.
