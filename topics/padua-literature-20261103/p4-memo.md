# P4 memo for AC: the Leuven IEP / multiple-OP line since 2024 (2026-11-03)

Reader: Claude P4 (claude-opus-5-5, high). Every statement below rests on pages I read; the records give the locators. No new ideas are registered here.

## (a) What Leuven has done since 2024 that bears on bivariate IEPs

None of these papers treats two or more variables. A text search of every source for "bivariate", "multivariate", "two variables", "Padua" and "Chesnokov" gave zero hits. Van Barel–Chesnokov 2010 is not cited anywhere, and the field is open on their side. What they built is a set of 1-D tools that matter for a 2-D IEP:

- **IEP for multiple OPs** ([SINUM 2026](https://doi.org/10.1137/25M1770965), [arXiv 2506.19796](https://arxiv.org/abs/2506.19796)). Banded Hessenberg recurrence matrix; biorthogonal Lanczos with several starting vectors versus non-unitary eliminators. IEP_CORE and IEP_KRYLREORTH(full) are backward stable for most N < 25 and lose it beyond. This corrects our records LIT-347/119.
- **Updating and downdating for multiple OPs** ([arXiv 2608.25758](https://arxiv.org/abs/2608.25758), not yet published).
  - Updating: nodes are added one at a time with eliminators.
  - Scaling: dropping monicity and balancing column norms keeps about 5 digits at N = 100 on the Kravchuk/Hahn tests, where the monic one-shot methods lose all digits near N = 20–25 (pp. 10–11, 20–21).
  - Downdating: a node is removed by two perfect-shift RL steps. The needed eigenvectors are simply rows of the stored bases (pp. 13–19).
- **Downdating for OPs and rational functions** ([ANM 200 (2024)](https://doi.org/10.1016/j.apnum.2023.07.009), [arXiv 2302.00355](https://arxiv.org/abs/2302.00355)). Three authors, not Faghih. Uses RQ rather than QR steps, because RQ keeps the weight vector (pp. 11–12). The eigenvector variant is the most accurate but needs an accurate eigenvector (pp. 21–25).
- **Sobolev variants** ([Numer. Algorithms 2025](https://doi.org/10.1007/s11075-025-02149-y); [NLAA 2025](https://doi.org/10.1002/nla.70017), probable preprint [arXiv 2407.05945](https://arxiv.org/abs/2407.05945), content-consistent but unconfirmed). Same pattern: OP family ↔ Krylov space ↔ structured IEP.
- **Closest structural relatives of the 2-D case.**
  - [Vermeiren, arXiv 2601.11317](https://arxiv.org/abs/2601.11317): vectors of rational functions give pencils with k subdiagonals.
  - [Rinelli–Vandebril, arXiv 2605.16954](https://arxiv.org/abs/2605.16954): block Krylov ↔ matrix OPs. Note this is one operator with many vectors, not several commuting operators.
- **Forward problem, outside the group** (Bari/Louvain): [Laudadio–Mastronardi–Van Dooren, Numer. Algorithms 2025](https://doi.org/10.1007/s11075-024-01785-0) and the [JCAM 2024 package](https://doi.org/10.1016/j.cam.2024.116109) compute nodes and weights from H by balancing, total nonnegativity and Ehrlich–Aberth, in O(n²). [Filipuk–Haneczok–Van Assche 2015](https://doi.org/10.1007/s11075-015-9959-8) converts step-line, nearest-neighbour and marginal coefficients in Maple, with no stability analysis.

## (b) What they list as future work

| Source | Stated future work | Locator |
|---|---|---|
| SINUM 2026 | IEP conditioning theory; updating/downdating; Laurie via vector/branched continued fractions; nearest-neighbour recurrences; comparison with FHV 2015 | §7 p. 1213 |
| arXiv 2608.25758 | other multi-index paths (nearest-neighbour MOPs; MOPs on the complex plane); inner products with derivatives; a thorough stability analysis | §6 p. 24 |
| ANM 2024 | choice of the number of eigenvector refinement steps; most stable left/right order for pencils (no conclusions section in v1) | arXiv pp. 25, 34 |
| Vermeiren 2026 | downdating for rational function vectors | p. 18 |
| Rinelli–Vandebril 2026 | the deflated (degenerate) block case; block Gaussian quadrature | p. 26 |
| Laudadio–Mastronardi–Van Dooren 2025 | conjecture: method works for all nonnegative intervals and r > 2 | p. 641 |
| Sobolev ORF 2025; NLAA preprint; JCAM 2024 | none stated | conclusions |

## (c) Where contact or a joint question makes sense

This builds on the assessment's point 3 (conditioning) and point 4 (index paths). Each item below is a **proposal for a later topic, not registered**. Each needs an IDEA entry and a novelty gate before any work.

- **A. What does the MOP IEP's conditioning actually measure?** *(proposal for a later topic, not registered)* SINUM asks for a conditioning theory. 2608.25758 then shows that changing only the normalization (non-monic plus balancing) and the build order (incremental updating) turns "all digits lost at N ≈ 25" into "5 digits at N = 100". It is open how much of the SINUM ill-conditioning belongs to the monic representation and how much to the map from nodes and weights to H. Joint question: a first-order condition number for that map, under monic and balanced normalizations, tested on Kravchuk/Hahn. Our span-sensitivity and moment-cone tools (assessment point 3) fit this directly.
- **B. Nearest-neighbour MOPs as a commuting-pair IEP.** *(proposal for a later topic, not registered; home: IDEA?bivariate-lanczos-claude-041)* Both Leuven papers list nearest-neighbour recurrences as open. In FHV 2015, the nearest-neighbour coefficients satisfy compatibility relations (eqs. (3.11)–(3.13), p. 20) because steps in different index directions must commute. That is the same kind of constraint as in our bivariate pair (H_x, H_y). Joint question: is the nearest-neighbour IEP for r = 2 a commuting-pair IEP, solvable with Van Barel–Chesnokov-style updating along a path in ℕ²?
- **C. Bivariate downdating.** *(proposal for a later topic, not registered)* Leuven now has downdating for OPs, ORFs and MOPs, and Vermeiren lists it as future work for vector functions. Nobody has it for bivariate OPs. Their eigenvector route needs no shift search, because the eigenvector is a row of the stored basis (2608.25758, p. 13). In 2-D that row is a joint eigenvector of the pair, so the idea may carry over to downdating Van Barel–Chesnokov 2010. The ANM 2024 warning about eigenvector accuracy and the non-commuting-pair failures noted in the assessment are the obvious risks. This is a natural joint question with Van Barel and Vandebril.

Practical note: the first author of the MOP papers is Faghih, and Vandebril is on all of them. Van Barel retired (dedication in Numer. Algorithms 100, p. 621) but is still a co-author in 2026.
