# faghih-vanbarel-vandebril-2026 — addendum (P4, padua-literature-20261103)

A. Faghih, M. Van Barel, R. Vandebril, "Updating and Downdating the Recurrences of Discrete Multiple Orthogonal Polynomials on the Real Line", arXiv:2608.25758v1 [math.NA], 26 Aug 2026 (PDF dated 27 Aug 2026), 26 pp.

- DOI / URL: https://arxiv.org/abs/2608.25758 (arXiv DOI 10.48550/arXiv.2608.25758). No journal version found as of 2026-11-03 (arXiv shows v1 only, no journal-ref; see p4-links.md row 2).
- Access and reading date: 2026-11-03, arXiv PDF v1 loaded in the built-in browser and text-extracted with pdf.js.
- Reading coverage: **complete full text**, PDF pp. 1–26 (all sections, figures' captions and text, references). Figures were read through their extracted labels and the surrounding text only; plotted values were not read off the images.
- Reader, model and effort: Claude P4 literature reader (claude-opus-5-5, high).
- Named gaps requiring future re-reading: none for the statements below. Page images of Figs. 2–6 not inspected. The software page cited on p. 19 (footnote †) was not opened.
- Existing record: `literature/records/faghih-vanbarel-vandebril-2026.md` (LIT-117, LIT-118, secondary account). Existing INDEX row LIT-348 (programme-ideas, secondary). This addendum upgrades all three to fulltext-verified and corrects them as listed at the end.

Locators are arXiv v1 PDF page numbers (the preprint has no journal pagination).

## Extracted published statements

### LIT?padua-literature-claude-70 — method: updating the step-line MOP IEP by eliminators

- Statement in faithful paraphrase: For r = 2 positive discrete measures on the same N distinct real nodes, the step-line recurrence matrix is a 4-banded upper Hessenberg H_N, with biorthonormal W_N, V_N (type I functions and type II polynomials evaluated at the nodes) and W_N^T Z V_N = H_N. Given a solution of size N, adding one node and its two weights is done by (i) embedding all matrices into size N+1, (ii) a transformation T built from the old and new weight-coefficient triangles R_pre, R_up that fixes the first two columns of W and the first column of V, followed by one lower eliminator L_1, and (iii) restoring the banded form by 2N−3 non-unitary 2×2 triangular eliminators, alternating between the last row and the last column (Fig. 1). Breakdown (tiny pivots) is assumed not to occur.
- Hypotheses and notation: AT-system of positive discrete measures; distinct real nodes; r = 2 throughout, with r > 2 described as possible but not pursued (p. 4). Type II MOPs are **not** required to be monic, so the subdiagonal of H_N need not be 1 (p. 4). Starting vectors from Prop. 2.1 (= SINUM Prop. 3.7 with the non-monic modification, p. 6).
- Page / theorem / equation: Problem 2.1 p. 6; Problem 3.1 p. 7; Lemma 3.1 pp. 8–9; elimination count and eliminator parameters p. 10; Fig. 1 p. 11.
- Reading evidence and limitations: full text read. No error analysis is given for the eliminator steps; the paper notes possible breakdown when pivots are small (p. 10).
- Relation to campaign claims (no inherited proof status): the univariate MOP analogue of the Van Barel–Chesnokov 2010 node-by-node updating, but with non-unitary eliminators instead of Givens rotations. Van Barel–Chesnokov 2010 is not cited.

### LIT?padua-literature-claude-71 — method and numerical finding: norm-balancing scaling

- Statement in faithful paraphrase: Because the bases can be very ill conditioned, the authors drop monicity and apply, after each update, a diagonal similarity scaling that makes each pair of corresponding columns of W and V of roughly equal 2-norm (β_i = sqrt(‖w_i‖/‖v_i‖)). On multiple Kravchuk (p1 = 0.4, p2 = 0.5) and multiple Hahn (β1 = 1, β2 = 1.5, γ = 1) MOPs, the monic variant without scaling loses essentially all digits for N between 20 and 25, while the scaled updating keeps about five digits in the recurrence error at N = 100. The authors attribute the gain jointly to the scaling and to the incremental nature of updating, compared with the one-shot methods of the SINUM paper.
- Hypotheses and notation: error metrics E_r (relative recurrence residual) and E_bo (biorthonormality residual), p. 19. Kravchuk/Hahn weights are not nested, so for each N the update chain is restarted from a 2×2 core-transformation solution (p. 20).
- Page / theorem / equation: §3.1 pp. 10–11; Examples 5.1–5.2 p. 20; Fig. 2 and discussion p. 21.
- Reading evidence and limitations: full text read; numbers taken from the authors' text, not from the plots.
- Relation to campaign claims: a residual-based accuracy report, not a backward-error test of the kind used in SINUM §6.2. It does not settle the IEP conditioning question that SINUM §7 leaves open.

### LIT?padua-literature-claude-72 — numerical finding: loss of biorthogonality comes from regenerating the bases

- Statement in faithful paraphrase: Regenerating V_N, W_N from the recurrence (with exact starting vectors) loses biorthogonality as the degree grows, both with the computed H and with the exact Kravchuk/Hahn H. The two losses are comparable. The authors conclude that the computed coefficients are accurate enough and that the loss is intrinsic to running the recurrence.
- Hypotheses and notation: Kravchuk and Hahn examples, N ≤ 25.
- Page / theorem / equation: pp. 21–22, Fig. 3 p. 22.
- Reading evidence and limitations: full text read; the claim is empirical, for two families.
- Relation to campaign claims: a 1-D analogue of the distinction between coefficient error and basis-regeneration error that the drift campaign draws. Cite as an analogy only.

### LIT?padua-literature-claude-73 — method and numerical finding: downdating by two perfect-shift RL steps

- Statement in faithful paraphrase: Removing a node z_j is done by isolating it through two perfect-shift RL steps built from eigenvectors that are already available: the j-th row of V_N (left eigenvector) and the j-th row of W_N (right eigenvector), refined by a few iterative-refinement steps after Mastronardi–Van Dooren 2018. An auxiliary vector is needed to remove the second superdiagonal. The steps are followed by two lower eliminators (G_2, G_3) that fix the weight conditions, and N−4 upper eliminators that chase the bulges. RL rather than QR steps are used because they keep the biorthogonal structure (Watkins). In experiments with Chebyshev and equidistant nodes and random weights, 20 successive downdates from N = 40, and 20 alternating down/up cycles, keep E_r and E_bo between about 1e-11 and 1e-9, with no visible growth.
- Hypotheses and notation: unreduced H_N (no breakdown), diagonalizable with H_N = W_N^T Z V_N (p. 12). Uniqueness is invoked through SINUM Prop. 4.2 (p. 19).
- Page / theorem / equation: Problem 4.1 pp. 11–12; §4.1 pp. 13–16 (eq. (11) p. 16); §4.2 pp. 16–17; §4.3 pp. 17–19 (S = R_1 L_2^{-1} L_3^T R_2, p. 19); §5.2 pp. 22–24, Figs. 5–6.
- Reading evidence and limitations: full text read. The downdating start is itself a computed updating solution (p. 23). No error bound is given.
- Relation to campaign claims: confirms the reading in LIT-117 that eigenvector-driven downdating needs no extra shift search: the eigenvector is a row of the stored basis. In 2-D the analogous row of the OP evaluation matrix is a joint eigenvector of the pair, so the same idea could transfer to bivariate downdating (see the memo, question C).

### LIT?padua-literature-claude-74 — stated future work

- Statement in faithful paraphrase: The authors list (1) extending the framework to other classes of MOPs, namely other multi-index paths beyond the step-line, such as nearest-neighbour MOPs (citing Van Assche 2011), or MOPs on the complex plane (citing Mínguez Ceniceros–Van Assche 2008, which is about the unit circle); (2) updating/downdating for more general inner products, for example ones involving derivatives (Sobolev type); (3) a thorough stability analysis, which they call an important open topic even though the experiments behave well.
- Hypotheses and notation: —
- Page / theorem / equation: §6 "Conclusion and future work", p. 24.
- Reading evidence and limitations: full text read.
- Relation to campaign claims: (1) is the home of IDEA?bivariate-lanczos-claude-041 (deferred, coordinate with Leuven). No bivariate or multivariate setting is mentioned anywhere in the paper.

## Search and attribution notes

- Text searches on 2026-11-03 over all 26 extracted pages: "bivariate", "multivariate", "Chesnokov", "two variables", "several variables", "Padua" gave 0 hits. "multiple starting" (pp. 3, 25) and "block Krylov" (p. 3) occur only in the description of the SINUM Lanczos method and the Aliaga–Boley–Freund–Hernández reference.
- The ill-conditioning sentence in LIT-118 ("MOP bases typically so ill conditioned … infeasible") is in the **Introduction, p. 3**. It refers to the SINUM Lanczos/core methods in double precision, and the same paragraph claims the new scaling and updating improve on it. It is not in the conclusion.
- The code is cited as available from the KU Leuven NUMA "momentum-software" page (p. 19, footnote †; not opened).

## Corrections to the existing record and rows (old → new; literal blocks in proposed-record-changes-p4.md)

- Record header: the title is now known (above). The date is v1 26 Aug 2026 (the PDF is dated 27 Aug).
- Coverage: "supplied secondary account only … fulltext NOT inspected" → "complete full text, arXiv v1 PDF pp. 1–26, read 2026-11-03 (P4)".
- LIT-117: content confirmed, locator "conclusion" → §4.1 pp. 13–16 for the method; the stability-analysis sentence is in §6 p. 24.
- LIT-118: the future-work part is confirmed at §6 p. 24. Add "inner products with derivatives". The "complex plane" item cites a unit-circle MOP paper. The ill-conditioning clause → locator Introduction p. 3, referring to SINUM methods. Status UNVERIFIED → fulltext-verified.
- LIT-348: "stability analysis is listed as future work; the seed is not cited" is confirmed (p. 24; references pp. 25–26 contain no Van Barel–Chesnokov). "updating (by IEP)" is more precise as: updating by similarity transformations with non-unitary eliminators, following the IEP formulation. Status UNVERIFIED → fulltext-verified.

## History

2026-11-03: P4 addendum; full text read; provisional IDs 70–74.
