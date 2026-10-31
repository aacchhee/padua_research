# Are the open problems really open? Verification after ingesting the new papers

*31 October 2026. This document supersedes the ranking in "Padua points research since 2010.md". The literature summary there still stands, apart from the corrections in §4. Detailed notes, with page-level quotes, are in `research_notes/Open problems verification/`.*

## 1. Short answer

Mostly not, in the form the report stated them. Of the ten problems, three collapse entirely (2, 4, 7). Four shrink to a narrower theoretical core (1, 3, 6, 8). Two stay open but are riskier than claimed (5, 9). One has an open goal but no new method (10).

The main cause is that the first report was written without the full text of **Huhtanen–Larsen 2002 (BIT 42:393–407)**. That paper already contains, among other things:
- a truncated short recurrence of length ≤ 2k+1 (Thm 2.3, p. 397);
- the d-variate scheme (§2.3);
- vanishing-polynomial detection along the order ideal (Cor. 2.2, p. 396);
- algebraic-curve fitting (§4.1);
- a version for arbitrary commuting symmetric matrices, not only diagonal X, Y.

Several "inferred gaps" were therefore missing citations of HL, not missing results.

My own numerical "finding" from the first round also does not hold up as new:
- **Sparse explicit H_x, H_y on Padua points.** This is a three-line corollary of the discrete orthonormality in Caliari–De Marchi–Vianello 2008 and the two-term ideal generators in Bos–De Marchi–Vianello–Xu 2007 (Thm 2.3). It extends verbatim to all Harris–Simanek rectangular checkerboard sets (Proc. AMS 2021).
- **The rank-(2n+1) uniform-weight correction.** This is automatic: on a unisolvent set the rank equals the number of weights that change. In OP language it is a multivariate Uvarov modification (Delgado–Fernández–Pérez–Piñar–Xu, Numer. Algorithms 55 (2010), the same volume as the seed paper).

## 2. Verdict per problem

| # | Problem (as stated in the report) | Verdict | Decisive evidence |
|---|---|---|---|
| 1 | Backward stability + downdating of the bivariate IEP | **Partially addressed** | Removing a node is QR row-deletion (Gill–Golub–Murray–Saunders 1974), proven stable for two-sided transforms (Paige, Math. Comp. 34 (1980)). Checked on Padua n = 12: matches recomputation to ~1e-14, and no shifts are needed, so the "joint-shift" twist is a non-issue. Plain normwise backward stability of a Givens sequence is textbook. The "structured" version is ill-posed, because computed H_x, H_y never commute exactly. |
| 2 | Closed-form recurrences on Padua nodes + fast reweighting | **Known / trivial** | CDMV 2008 eqs. 9–10 plus BDMVX 2007 Thm 2.3. The general theory is Xu 1994 (modified block Jacobi matrices, joint eigenvalues = cubature nodes). Reweighting gains only √N, and nothing for full-rank weight changes. On Pad_n, weights do not affect the interpolant, so "Lebesgue-optimized/CATCH weights on Pad_n" is meaningless. |
| 3 | Truncated multivariate "Vandermonde with Lanczos" | **Partially addressed** | This *is* HL 2002. Zaccaron (Padova MSc 2014) measured the loss of orthogonality (‖QᵀQ−I‖ ≈ 0.38 at degree 40) and fixed it with full reorthogonalization. |
| 4 | Pivot canonical form avoiding Liu–Narayan's non-convex step (d ≥ 4) | **Trivial** | The non-convexity comes from fitting each direction separately. One eigendecomposition of the full cross-direction residual Gram block (already computed in their §5.2.1) gives the answer in any d. Checked for d = 4 with a non-product measure: orthonormal to 5e-15, with a clean rank gap. The HL/seed pivot form also works in any d. |
| 5 | Sub-O(N^{5/2}) / divide-and-conquer / HSS IEP | **Open, high risk** | The correct baseline is HL's O(M N^{3/2}), not O(N³). Q is not HSS-compressible: top-level off-diagonal ranks were ~430 out of 517 at N = 1035. No stable sub-quadratic algorithm exists even for the univariate Jacobi IEP. Exact-arithmetic sub-cubic methods (Neiger–Schost) do not transfer. |
| 6 | IEP as approximate-vanishing-ideal engine | **Partially addressed** | HL Cor. 2.2 and §4.1 already do it (residual ‖x^j y^l − p̂‖ = Buchberger–Möller residual). Related: Mourrain ISSAC 2017 (orthogonal border bases), VCA (ICML 2013), Telen–Mourrain–Van Barel truncated normal forms. |
| 7 | Stable empirical Christoffel functions via recurrences | **Solved** | QR-based leverage scores and Christoffel functions are standard practice: Adcock–Cardenas SIMODS 2020; Migliorati; Zhu–Nakatsukasa IMA JNA 2026; Meurant–Sommariva 2019 on meshes of 6.4·10⁵ points. |
| 8 | RRQR/maxvol Fekete extraction with provable bounds; updatable greedy optimization | **Partially addressed** | Maxvol or strong RRQR gives Λ ≤ (1+ε)·N·C(A_n) in one line. Van Barel–Humet–Sorber already did updating-based greedy optimization to degree 60. Meurant–Sommariva 2019 is a direct competitor on the disk. |
| 9 | Total-degree Krylov for f(A,B), commuting A, B | **Partially addressed, risky** | The basis is HL's Algorithm 1; see also Huhtanen 2003 and parametric model-reduction moment matching. It has never been used for f(A,B)b, but the projected matrices do not commute, so f(H_A, H_B) is undefined beyond polynomials. On Kronecker test cases the method loses to tensorized Arnoldi. |
| 10 | 3D Padua-like points via joint spectra | **Goal open; approach not new** | Commutator minimization appears in Degani–Schiff–Tannor (Numer. Math. 2005), Xu 1994, and Collowald–Hubert 2018. Li–Sun–Xu (2009) conjecture that degree-(2n−1) Chebyshev cubature on the cube needs at least n³/4 nodes, whereas a cubature-based 3D Padua set would need about n³/6. So the report's route aims at something conjectured not to exist. |

## 3. What survives: revised short list

These are genuinely open as far as the second search could tell. That search still could not reach Google Scholar, zbMATH or Lirias. The decisive unchecked source is Humet's 2019 PhD thesis; see §5.

**A. Loss-of-orthogonality theory for truncated multivariate Lanczos (HL-type).** Strongest candidate.
- **Stated by authors:**
  - HL 2002, p. 401: loss of orthogonality "may occur among vectors from different cycles when bivariate polynomials of very high degree are computed."
  - Zaccaron 2014: "bounds are not available."
  - Sommariva–Vianello 2015 (NFAO, p. 1201) dismiss both HL and the seed method as slow at high support cardinality, and HL as losing orthogonality: "their use should be probably reserved to situations where no alternative is possible".
- **Core:**
  - a Paige/Greenbaum-type analysis for recurrences driven by two commuting operators (cycles, varying recurrence length);
  - selective/partial reorthogonalization with a provable criterion;
  - experiments well past the ~10³ points in print.
- **Why it suits you:** the cost is O(MN^{3/2}), against full reorthogonalization at O(MN²). The 2D structure (cross-cycle coupling) makes it more than a transcription of Paige.

**B. Conditioning of the map (nodes, weights) → (H_x, H_y).**
- No bivariate analysis exists; univariate analogues do (Gautschi; Laurie).
- It would explain the seed paper's unexplained 0.5–1.8-digit deficit relative to HL (Table 2; largest on Padua points).
- It would also give a correct notion of "stability" for problems A and C: a mixed forward–backward analysis instead of the ill-posed structured backward stability.

**C. Stable downdating without the full Q, for M ≫ N and sliding windows.**
- **What is solved:** row deletion with Q stored (Paige 1980).
- **What is open:**
  - removing nodes while keeping only the N-column truncated basis and recurrence matrices, with no M×M Q;
  - its stability: Elhay–Golub–Kautsky call univariate downdating "potentially unstable", and Faghih–Van Barel–Vandebril (arXiv 2608.25758, MOP case) list stability as future work.
- Combined with A, this gives a "streaming bivariate least squares" algorithm.

**D. Certified approximate border bases from tolerance-truncated recurrences.**
- **Core:** an (ε,δ)-approximate border-basis guarantee for the output of the HL/seed recurrence with a pivot tolerance.
- **Observation from the verification:** each pivot equals the ratio of consecutive Buchberger–Möller residuals. So a pivot tolerance is a *relative* criterion, unlike the absolute tests in AVI/ABM/OAVI.
- **Gap:** no paper compares HL-type methods with that literature, and the benchmark itself is publishable.

**E. Lower priority / higher risk:**
- Problem 5: compress the *rotation sequence*, or a divide-and-conquer merge of two point sets. The output alone has N² entries in Q, so the gain must come from never forming Q.
- Problem 9: a projected functional calculus for f(A,B) with non-commuting projections.
- Problem 10: any unisolvent total-degree set in [−1,1]³ with polylog Lebesgue constant by a non-cubature construction, or non-existence certificates for small n against the Li–Sun–Xu n³/4 bound.

**Author-stated theory problems that were not re-checked adversarially in this round** (they come from recent surveys, so they are likely still open):
- Morrow–Patterson Lebesgue constant O(n²) (De Marchi 2022);
- the geometry of the Padua Lebesgue function, e.g. ≥ n(n−1)/2 interior maxima (Białas-Cież–De Marchi–Suder, arXiv 2605.23299, May 2026);
- "hyperinterpolation based directly on Padua points" (An–Ran–Wu survey, arXiv 2510.04904; the formulation needs checking);
- theory for Gibbs-filter parameters on Padua/Lissajous points (De Marchi–Erb–Marchetti 2017).

## 4. Corrections to the first report

- **Huhtanen–Larsen:**
  - Treat it as the main precursor of Problems 3, 4, 6 and 9.
  - The cost baseline is O(MN^{3/2}), not O(N³). HL is real-nodes only; the seed also handles complex node pairs.
  - HL's experiments are small: at most 91 random points, degree ~12, no Padua points.
- **The seed's own position:** its "similar efficiency" to HL is loose. The Givens IEP keeps an M×M unitary, whereas HL keeps a √N-window. The accuracy gap in its Table 2 is 0.5–1.8 digits, not "about one".
- **Section "Vanishing ideals and border bases never met the IEP" is wrong.** HL 2002 already did it.
- **Problem 2 → benchmark only.** Harris–Simanek sets with arbitrary X, Y give exact benchmark recurrences with ≤ 3 nonzeros per column (≤ 2 if a side is symmetric). They are better test cases than Padua alone, because they can be badly conditioned. Checked numerically: `harris_simanek_check.py`.
- **Meurant–Sommariva 2019** use HL for the basis and do not cite the seed. They report the best-known disk Lebesgue constants and conjecture linear growth with degree.
- **Marco–Martínez–Viaña 2019** handles tensor-type spaces on vertical-line node sets only. It is not a competitor for total-degree OPs.
- **Cools–Poppe 2011:** no aliasing rules and no FFT (both announced as future work). The 3D/sD blending lattices give exactness only for n = 4ν−1 or 4ν−3, with about 1.5× (3D) and 2.1–2.4× (4D) dim Π_k points (`cools_poppe_blending_check.py`).
- **Bibliographic fixes:**
  - TW629 authors are Mach, Van Barel, Vandebril; it is very likely the preprint of the JCAM 2014 paper.
  - arXiv 2302.00355 is by Van Barel, Van Buggenhout and Vandebril.
  - Zhu–Nakatsukasa appeared in IMA J. Numer. Anal. 46(4) (2026), doi:10.1093/imanum/draf055.
  - Zaccaron is not the only reimplementation of HL; Meurant–Sommariva use it too.

## 5. Papers still needed (please obtain)

| Priority | Paper | Why |
|---|---|---|
| 1 | M. Humet, *Orthogonal polynomials and matrix computations: Applications of recurrence relations*, PhD thesis, KU Leuven, 2019 (Lirias) | Most likely hidden prior work on bivariate downdating/stability (A, C) |
| 2 | M. Van Barel, A. Bultheel, "Updating and downdating of orthonormal polynomial vectors and some applications", Contemp. Math. 281 (2001) 145–162 | The downdating template the seed cites |
| 3 | Y. Xu, SIAM J. Math. Anal. 25 (1994) 991–1001, [doi:10.1137/S0036141092237200](https://doi.org/10.1137/S0036141092237200) | Exact modified block-Jacobi construction (P2, P10) |
| 4 | M. Huhtanen, SIMAX 23 (2002) 1092–1108, [doi:10.1137/S0895479800398468](https://doi.org/10.1137/S0895479800398468); M. Huhtanen, R. M. Larsen, SIMAX 23 (2002) 1070–1091, [doi:10.1137/S0895479801384561](https://doi.org/10.1137/S0895479801384561) | Companion Lanczos-type work; any loss-of-orthogonality analysis (A) |
| 5 | S. Elhay, G. H. Golub, J. Kautsky, SIMAX 12 (1991) 327–353, [doi:10.1137/0612024](https://doi.org/10.1137/0612024) | Univariate downdating instability (C) |
| 6 | T. Sauer, Numer. Algorithms 45 (2007) 295–313, [doi:10.1007/s11075-007-9112-4](https://doi.org/10.1007/s11075-007-9112-4) | Possible precursor for D |
| 7 | R. H. Bartels, J. J. Jezioranski, ACM TOMS 11(3) (1985), [doi:10.1145/214408.214410](https://doi.org/10.1145/214408.214410) | Possibly an earlier truncated multivariate recurrence (A) |
| 8 | I. Degani, J. Schiff, D. J. Tannor, "Commuting extensions and cubature formulae", Numer. Math. 101 (2005) 479–500 | Only the abstract was seen (P10) |
| 9 | G. S. Ammar, W. B. Gragg, SIMAX 12 (1991), [doi:10.1137/0612030](https://doi.org/10.1137/0612030) | Fast univariate IEP baseline (P5) |
| 10 | M. Collowald, E. Hubert, Stud. Appl. Math. (2018), HAL 01873077 | 3D commuting-extension examples (P10) |

Lower priority: Kressner, Oper. Matrices 8 (2014); Lasserre–Pauwels–Putinar (CUP 2022, doi:10.1017/9781108937078); Limbeck (PhD, Passau 2013); Stetter, *Numerical Polynomial Algebra* (SIAM 2004).

Also: the Google Scholar "Cited by" list for the seed paper and for HL 2002, which neither round could fetch.
