# Reclaiming bivariate discrete orthogonal polynomials for structured NLA

> **Superseded ranking (31 Oct 2026).** This report was written without the full text of Huhtanen–Larsen 2002 and several other papers. An adversarial verification afterwards found:
> - Problems 2, 4 and 7 are known or trivial.
> - Problems 1, 3, 6 and 8 reduce to narrower cores.
> - The section on vanishing ideals is wrong, because HL 2002 already makes that connection.
>
> See **"Open problems verification.md"** for the corrected verdicts and the revised short list. The literature summary below otherwise stands.

Since 2010 nobody has developed the 2010 bivariate Givens inverse-eigenvalue (IEP) algorithm further. It has about eight indexed citations: Semantic Scholar lists 8, OpenAlex counts 7 and OpenCitations lists 2. Its only substantive use is as the basis generator inside Van Barel–Humet(–Sorber) point-set optimization. No published work analyses its stability, downdates it, accelerates it below cubic cost or extends it to d ≥ 3 ([S2 citations](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11075-010-9392-y/citations?fields=title,authors,year,venue,externalIds&limit=1000); [OpenAlex](https://api.openalex.org/works/https://doi.org/10.1007/s11075-010-9392-y)). The surrounding field moved a lot in the same period:

- **Multivariate Vandermonde-with-Arnoldi (V+A)** re-derived the same recurrence in dense form, with full Gram–Schmidt at O(MN²) cost.
- **Liu–Narayan's multivariate Stieltjes method** computes Xu's block recurrences under an SVD canonical form that becomes non-convex for d > 3.
- **The Leuven group (Van Barel, Vandebril and co-workers)** built, in the univariate and multiple-OP settings, exactly the toolkit a modern bivariate algorithm needs: core-transformation IEPs, backward-stability tests and deflation-based updating/downdating (2025–26).
- **Padua theory** gained exact Lebesgue asymptotics, Λₙ = (4/π²) log² n + O(log n), and a large Lissajous family. Padua points in d ≥ 3 remain "the biggest open problem".

The best opportunities for you lie where these lines meet a structured-matrix viewpoint. In priority order:

1. A backward-stability analysis plus a downdating algorithm for the bivariate generalized-Hessenberg IEP. Both were left open in 2010 and in 2014, and the problem is author-stated.
2. Closed-form, sparse recurrence matrices on Padua/Lissajous nodes with cubature weights, used as exact benchmarks and as a base for fast low-rank reweighting. A quick numerical check, done after the literature search, confirmed the explicit case: at most 2 nonzeros per column. It also showed that the seed paper's own uniform-weight Padua experiment is a rank-(2n+1) = O(√N) modification of it, which points to semiseparable structure.
3. A truncated, short-recurrence "multivariate Vandermonde with Lanczos" with a loss-of-orthogonality theory.
4. A pivot (triangular) canonical form that sidesteps Liu–Narayan's non-convex step in d ≥ 4.
5. A divide-and-conquer or rank-structured (HSS) bivariate IEP, which fits your pySuperDC background best.

The citation coverage is incomplete: Google Scholar, zbMATH and Lirias could not be queried, so a manual "Cited by" check on the seed paper and on Huhtanen–Larsen 2002 is still needed.

## The 2010 paper left three doors open: downdating, stability and cost

The seed paper takes nodes ζᵢ (pairs of complex numbers) and weights wᵢ, with discrete inner product ⟨p,q⟩ = Σ wᵢ² p(ζᵢ)q(ζᵢ). It reduces bivariate orthonormal-polynomial (OP) generation to the IEP Qᴴw = ‖w‖e₁, QᴴXQ = Hₓ, QᴴYQ = H_y. Here Hₓ and H_y are "generalized Hessenberg": the pivot pattern is fixed by the graded-lex order and a "downside-up" x/y multiplication scheme. Algorithm 1 adds one point at a time. It annihilates the new weight with a Givens rotation and then chases the bulge along the pivots. For real nodes Hₓ and H_y are symmetric, but the paper stresses that "the lower bandwidth of these matrices is growing together with their size", so symmetry does not reduce the order of the cost as it does in 1D. The recurrence length grows like √(8d), following Huhtanen–Larsen ([seed paper](https://doi.org/10.1007/s11075-010-9392-y)).

Three experiments:

- **Padua degree 100, identity weights.** On N = 5,151 Padua points the orthogonality error stayed below about 10⁻¹¹. The Franke least-squares coefficients reached machine-precision size beyond k ≈ 3,000 (degree 76).
- **Zero pivot detects a vanishing polynomial.** For 44 points on two circles plus the four corners, the first zero pivot appears at the 28th OP, a degree-6 polynomial vanishing on all points. In effect, the algorithm detected a vanishing-ideal element.
- **Comparison with Huhtanen–Larsen (HL) 2D Lanczos.** HL's Q and H were about half a digit more accurate, which gives about one digit in polynomial recovery: 6·10⁻¹³ vs 1·10⁻¹⁴ on 496 Padua points. The updating ability was offered as compensation ([seed paper](https://doi.org/10.1007/s11075-010-9392-y)).

The paper left these ends open:

- **Downdating.** It states that "the downdating procedure can be developed similar to [20]" (Van Barel–Bultheel 2001).
- **Pivot choice.** Choosing the larger of the x- and y-pivots "may enhance the numerical stability".
- **Generalization to d variables.** The scheme "is easily generalized to polynomials of more than 2-variables".
- **Complexity and error analysis.** The paper gives neither.

The 2010 experiments used **uniform weights, not the Padua cubature weights**. This matters for Problem 2 below ([seed paper, §5.1](https://doi.org/10.1007/s11075-010-9392-y)).

## What happened since: six lines, one of them silent

### The seed survives as a basis generator, not as an algorithm line

The citing works fall into three clusters ([S2](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11075-010-9392-y/citations?fields=title,authors,year,venue,externalIds&limit=1000)): Van Barel's point-set papers, Padova-group mentions, and one external numerical-analysis paper.

**Van Barel–Humet–Sorber (ETNA 2014)** is the main downstream use. It minimizes the Lebesgue constant directly, by greedy add, greedy update and a weighted Gauss–Newton relaxation, on the square, triangle, disk and L-shape. It reaches degree 30, and degree 60 on the square (N = 1891, Λ ≈ 75). It computes the orthonormal basis with the seed's IEP, citing it three times ([ETNA PDF](https://etna.ricam.oeaw.ac.at/vol.42.2014/pp41-63.dir/pp41-63.pdf)). It adds two algorithmic facts:

- **A Householder variant.** "A first Householder transformation zeros all weights at once" and later steps restore the structure. It does more flops but runs faster because the work is BLAS-2.
- **A pivot rule.** The transformation is built from the vector of largest 2-norm.

It reports the only complexity figure in the line, **O(k²) flops per added point**, so O(N³) in total. It also states plainly: **"A stability analysis of these updates is not covered in this paper"** ([ETNA PDF](https://etna.ricam.oeaw.ac.at/vol.42.2014/pp41-63.dir/pp41-63.pdf)).

**Van Barel–Humet (DRNA 2015)** moves to weighted discrete least squares. With about 2× oversampling it gets Lebesgue constants of 8–9 at degree 30 on four domains, with construction cost growing empirically like O(δ⁵). Its Remark 1 is the key Padua fact: with Padua cubature weights the product-Chebyshev basis is discretely orthogonal, giving "L−1 orthonormal polynomials rather than L". The paper conjectures, without proof, that its sets are initial segments of a weakly admissible mesh ([DRNA PDF](https://drna.padovauniversitypress.it/system/files/papers/VanBarelHumet_10YPDPTS_4.pdf)).

**The Padova group** mentions the seed as an alternative. Sommariva–Vianello (MATCOM 2017) call it "an interesting approach, based on an inverse eigenvalue problem" but use QR-twice on a Chebyshev-product Vandermonde instead, without a stability comparison ([preprint](https://www.research.unipd.it/retrieve/8b370fff-6879-4d9f-92c8-114cb1d34cef/multivop.pdf)). Zaccaron's 2014 Padova M.Sc. thesis is the only work found that re-implements a Lanczos-type bivariate discrete-OP generator. It documents loss of orthogonality and fixes it with "twice is enough" reorthogonalization ([thesis PDF](https://www.math.unipd.it/~alvise/TESI_STUDENTI/ZACCARON/ZACCARON_prefinale.pdf)). The notes could not confirm that its refs [38]/[39] are the seed and HL.

**The one external citer** is Zhang et al. (G-Arnoldi, arXiv 2024), which cites the seed only in passing ([arXiv](https://arxiv.org/abs/2404.09266)).

Two further citers, Mach–Van Barel–Vandebril (JCAM 2014) and Sommariva–Vianello (NFAO 2015), were not readable, so their citing passages are unknown. The page range 377–398 for the JCAM paper was inferred from an index URL and is unverified ([journal](https://doi.org/10.1016/j.cam.2014.03.015); [journal](https://doi.org/10.1080/01630563.2015.1062394)).

**Neither author continued the bivariate line.** Your Semantic Scholar record shows only the 2011 KU Leuven thesis and two unindexed 2009/2010 items after the seed ([S2 author search](https://api.semanticscholar.org/graph/v1/author/search?query=Andrey+Chesnokov&fields=name,paperCount,papers.title,papers.year,papers.venue,papers.externalIds)).

**Huhtanen–Larsen's** post-2010 citers are similarly thin: the seed, Padova, a structural-dynamics paper, a rational-surrogate code for physics, and a 2025 self-citation. None develops the 2D Lanczos further ([S2 HL citations](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1023/A:1021907210628/citations?fields=title,authors,year,venue,externalIds&limit=1000)).

**DOI correction.** The correct HL DOI is **10.1023/A:1021907210628** (BIT 42(2), 393–407). The variant 10.1023/A:1021955019935 does not resolve to the paper ([Crossref](https://api.crossref.org/works?query.bibliographic=On+generating+discrete+orthogonal+bivariate+polynomials+Huhtanen&rows=3)).

### Leuven built the missing toolkit, but only in one variable

After 2015 the Van Barel–Vandebril group concentrated on univariate structured IEPs:

- **Orthogonal rational functions.** Pencil-based IEPs and rational Krylov (Van Buggenhout–Van Barel–Vandebril; [arXiv 2103.04788](https://arxiv.org/pdf/2103.04788)). Vermeiren (2026) extends this to vectors with "pairs of k-Hessenberg matrices" ([arXiv 2601.11317](https://arxiv.org/abs/2601.11317v1)).
- **Sobolev OPs** (Van Buggenhout, Numer. Math. 2023; [arXiv 2302.10691](https://ar5iv.labs.arxiv.org/html/2302.10691)).
- **Modifying recurrences when the discrete inner product changes.** Downdating by perfect-shift QR deflation, posed as an IEP ([arXiv 2302.00355](https://arxiv.org/abs/2302.00355); Appl. Numer. Math. 2023, [doi](https://doi.org/10.1016/j.apnum.2023.07.009)). The notes conflict on this paper's authors: one gives Van Barel, Van Buggenhout, Vandebril; another adds Faghih, but that version was not verified.
- **Arnoldi for polynomial and rational (Sobolev) least squares** ([arXiv 2407.05945](https://arxiv.org/abs/2407.05945)).

The structurally closest work is on **multiple orthogonal polynomials (MOPs)**, by Faghih, Rinelli, Van Barel, Vandebril and Vermeiren ([arXiv 2506.19796](https://arxiv.org/pdf/2506.19796); SIAM J. Numer. Anal. 2026, [doi](https://doi.org/10.1137/25m1770965)). The step-line recurrence matrix is banded Hessenberg with r = 2 superdiagonals. Two solvers are compared:

| Solver | Method | Cost | Backward stability |
|---|---|---|---|
| IEP_KRYL | biorthogonal Lanczos with several starting vectors | O(N²); O(N³) with full reorthogonalization | not backward stable; the reorthogonalized version behaves like IEP_CORE |
| IEP_CORE | non-unitary "eliminators" (LU) plus chasing | — | appears backward stable for N < 25, lost for N ≥ 25 |

The authors state that "a systematic comparison of the performance of all these algorithms would be interesting" and that they are "not aware of any extension of Laurie's approach to MOPs". The **August 2026 follow-up** adds updating (by IEP) and downdating ("an eigenvalue deflation technique inspired by QR-type algorithms") for discrete MOPs. It is univariate and does not mention the seed ([arXiv 2608.25758](https://arxiv.org/abs/2608.25758)).

**Why this matters.** The MOP Hessenberg and the bivariate generalized Hessenberg both have a bandwidth set by an indexing scheme. The bivariate case adds two operators and a bandwidth that grows like the degree. The 2025–26 toolkit (core-transformation chasing, deflation downdating, backward-stability methodology) is therefore directly transferable, and nobody has transferred it. This is an inference: no paper states it ([arXiv 2506.19796](https://arxiv.org/pdf/2506.19796)).

### Vandermonde with Arnoldi reinvented the recurrence densely

**Brubeck–Nakatsukasa–Trefethen (SIAM Rev. 2021)** is univariate and cites neither HL nor the seed ([arXiv 1911.09988](https://arxiv.org/pdf/1911.09988)).

**Hokanson's multivariate V+A (2020)** builds each new column by multiplying "the smallest k such that I[k] + eⱼ = I[ℓ]" by coordinate j. It orthogonalizes with two-pass classical Gram–Schmidt against **all** previous columns, at O(MN²) cost, and notes that "many orderings do not satisfy the required span property" ([arXiv 2009.10803](https://arxiv.org/pdf/2009.10803)). This is one fixed instance of the seed's ordering scheme π, without the seed's stability-motivated pivot choice.

**Zhu–Nakatsukasa** prove a near-optimality bound for multivariate V+A least squares on irregular domains: ‖f − L(f)‖ ≤ (1 + C(X,Ω)‖QQ*‖_∞/M)‖f − p*‖. It needs O(N²) equispaced or O(N² log N) random samples, and the VA+Weight variant needs O(N log N). They state that "the orthogonalization algorithm is subject to a loss of orthogonality due to numerical cancellation" and that optimal sampling in high-dimensional irregular domains is open ([arXiv 2301.12241](https://arxiv.org/html/2301.12241v2)). The journal venue is unverified: one note says IMA J. Numer. Anal. 2023/24, another says not confirmed.

**Zhang et al.** extend V+A to confluent (Hermite) data with a semi-definite G-inner product, warning that breakdown can occur when G is only positive semi-definite ([arXiv 2404.09266](https://arxiv.org/html/2404.09266v2)).

**What the V+A papers omit.** None truncates the orthogonalization using Xu's three-term block structure. For real nodes, x·φ_k with deg φ_k = n lies in degree blocks n−1, n and n+1, so it has O(√N) nonzero coefficients. Orthogonalizing against only those gives O(MN^{3/2}), which is the HL recurrence. This is an inferred gap, but a sharp one ([Hokanson, Alg. 2.1](https://arxiv.org/pdf/2009.10803)).

**Liu–Narayan (SISC 2023)** is the main algorithmic contribution outside Leuven ([arXiv 2202.04843](https://arxiv.org/pdf/2202.04843); [SIAM](https://epubs.siam.org/doi/10.1137/22M1477131)):

- It computes Xu's block recurrence matrices (A_{n,i}, B_{n,i}) from moments, using quadrature or Monte Carlo with up to 10⁸ samples.
- Its canonical form makes Σ B_{n,i}ᵀB_{n,i} diagonal.
- The construction is explicit in d = 2, a weighted orthogonal Procrustes problem in d = 3, and **a non-convex optimization for d > 3**.
- It is "far more stable" than moment/Gram–Schmidt methods.
- It cites neither HL nor the seed, and gives no complexity analysis.

**Sparse recurrences for classical domains** come from ladder operators: Olver–Townsend–Vasil on the triangle ([arXiv 1801.09099](https://arxiv.org/abs/1801.09099)). Linear-complexity univariate measure modifications come from Gutleb–Olver–Slevinsky ([arXiv 2302.08448](https://arxiv.org/abs/2302.08448)).

**The Christoffel–Darboux data-analysis literature** (Lasserre–Pauwels–Putinar) computes empirical Christoffel functions by inverting the monomial moment matrix. Lasserre's 2024 Leuven slides concede that "matrix inversion ... does not scale well" and offer only Tikhonov-type regularization ([arXiv 1701.02886](https://arxiv.org/pdf/1701.02886); [slides](https://homes.esat.kuleuven.be/~sistawww/bdm/backtotheroots/wp-content/uploads/christoffel-1.pdf)).

### Padua theory sharpened in 2D and stalled in 3D

**Exact leading asymptotics.** Kolomoitsev–Lomako (Appl. Math. Comput. 2021) derive Lebesgue-constant asymptotics for Lissajous–Chebyshev nodes. As a special case, **Λₙ(Pad) = (4/π²) log² n + O(log n)**, the square of the 1D Chebyshev constant 2/π. Before this only O(log² n) upper bounds and c·log² n lower bounds were known ([arXiv 2009.07114](https://ar5iv.labs.arxiv.org/html/2009.07114); [doi](https://doi.org/10.1016/j.amc.2021.126192)). The notes read this result through a summarizer, so check the precise corollary statement.

**Erb and co-authors** turned Padua points into one member of a family ([survey](https://www.maths.tcd.ie/EMIS/journals/DRNA/pdf/erb_etal_10ypdpts.pdf); [d-D](https://ar5iv.arxiv.org/html/1511.04564); [unifying](https://arxiv.org/abs/1711.00557); [sphere](https://arxiv.org/abs/1802.06546); [disk](https://arxiv.org/pdf/1812.00437)):

- degenerate and non-degenerate Lissajous nodes in 2D;
- Lissajous–Chebyshev (LC) nodes in [−1,1]^d, with unisolvence in spectral (non-total-degree) index spaces, discrete orthogonality and DCT/FFT algorithms;
- a "unifying theory" that contains Padua, Morrow–Patterson–Xu and Lissajous nodes;
- spherical Lissajous nodes;
- rhodonea nodes on the disk, with Λ ≤ C log m₁ log m₂.

Two-sided d-dimensional product-of-logs bounds hold for LC nodes ([arXiv 1608.03451](https://arxiv.org/abs/1608.03451)). The authors note that in the non-degenerate case "a direct relation to the Lissajous nodes ... is not known" ideal-theoretically ([survey](https://www.maths.tcd.ie/EMIS/journals/DRNA/pdf/erb_etal_10ypdpts.pdf)).

**Other theory:**

- **Morrow–Patterson points:** Λ_MP = O(n³) is proven; O(n²) is conjectured ([DRNA 2014](https://www.kurims.kyoto-u.ac.jp/EMIS/journals/DRNA/pdf/demarchisommarivavianello-2014-mcf.pdf)).
- **Padua vs Fekete:** Padua points are numerically not Fekete points. At degree 9, |det V| for the quasi-Fekete set is 2.38e35 vs 1.69e35 for Padua. At degree 20, Λ is 9.20 for Padua, 8.14 for quasi-Lebesgue sets and 8.99 for quasi-Fekete sets ([Briani–Sommariva–Vianello preprint](https://www.math.unipd.it/~alvise/PAPERS/ComputingFeketeAndLebesguePoints.pdf)).
- **Vandermonde determinant of Padua-like points:** the gap in the Bos–De Marchi–Waldron product formula was closed by De Marchi–Usevich, and de Camargo–De Marchi proved unisolvence of generic Padua-like sets ([arXiv 1311.6455](https://arxiv.org/abs/1311.6455); [DRNA 2015](https://www.math.unipd.it/~demarchi/papers/Vandermondians_Padua_0305.pdf)).
- **Minimal cubature:** Xu enlarged the 2D families attaining Möller's bound, for Chebyshev- and Jacobi-type weights with |x±y| factors and Koornwinder-type weights ([arXiv 1102.0055](https://ar5iv.labs.arxiv.org/html/1102.0055); [arXiv 1603.08162](https://www.arxiv.org/abs/1603.08162); [arXiv 2407.09903](https://arxiv.org/html/2407.09903v1)).
- **Harris** generalized even/odd product-node Lagrange formulas and cubature to arbitrary node sequences ([Harris–Simanek, Proc. AMS 2021](https://www.ams.org/journals/proc/2021-149-08/S0002-9939-2021-15414-2)).
- **Lebesgue-function geometry (2026):** Padua points remain "the only known set of multivariate interpolation points" with optimal O(log² n) growth. Padua and Morrow–Patterson Lebesgue functions numerically have at least n(n−1)/2 interior local maxima ([arXiv 2605.23299](https://arxiv.org/pdf/2605.23299v1)).

**What is still missing in 3D.** De Marchi's 2022 survey lists **"We do not know the Padua points on [−1,1]^d, d ≥ 3"** as "the biggest open problem". It also lists the Morrow–Patterson O(n²) conjecture, the corner location of the Lebesgue maxima, the Dubiner-equidistribution conjecture and 2D fake-node error analysis ([CMA 2022](https://www.math.unipd.it/~demarchi/papers/paperCMA2022.pdf); [doi](https://doi.org/10.33205/cma.1070020)). Xu (2024) adds that "we do not know any family of cubature rules that attain Möller's lower bound for d > 2" ([arXiv 2407.09903](https://arxiv.org/html/2407.09903v1)). In 3D the field relies on:

- hyperinterpolation, whose norm is O(log^d n) on the d-cube (Wang–Wang–Wang 2014);
- Lissajous-curve rank-1 Chebyshev lattices;
- extracted approximate Fekete points (AFP), whose Lebesgue constants "seem to increase quadratically" ([arXiv 1502.04114](https://ar5iv.labs.arxiv.org/html/1502.04114)).

### Padua algorithms are fast, and applications are narrow

**Values ↔ coefficients transforms are solved.** They are masked 2D DCTs at O(n² log n). Padua2DM reports 0.387 s at n = 1000 for the FFT route, against 1.353 s for the BLAS-3 route, and notes that the matrix-multiplication route "stagnates around 10⁻¹³" ([Padua2DM preprint](https://www.math.unipd.it/~marcov/pdf/fastpadua.pdf)). Implementations exist in Chebfun2, FastTransforms.jl, ChebyshevTransforms.jl and Erb's LC2Ditp/LC3Ditp/RDisk codes ([Chebfun](http://www.chebfun.org/examples/approx2/PaduaPoints.html); [FastTransforms.jl](https://docs.juliahub.com/FastTransforms/5Lm8s/0.13.2/generated/padua/); [Erb software](https://www.math.unipd.it/~erb/software.html)).

**Two kinds of Padua cubature weights.** The product-Chebyshev Padua rule has positive weights. The non-tensorial Clenshaw–Curtis rule for Lebesgue measure has a few small negative weights ([Padua2DM preprint](https://www.math.unipd.it/~marcov/pdf/fastpadua.pdf)). Only the first kind defines an IEP-admissible inner product.

**Applications:**

- **Magnetic particle imaging (MPI) dominates.** Lissajous sampling trajectories make Lissajous nodes natural there ([IEEE TMI 2016](https://doi.org/10.1109/TMI.2016.2580458); [Gapyak et al. 2025](https://arxiv.org/abs/2505.22797v1)).
- **Quantum tomography.** Continuous-variable quantum tomography uses Padua interpolation, with exponentially decaying error and quasi-linear runtime ([PRL 2018](https://arxiv.org/abs/1706.07816)).
- **Fredholm equations.** A Padua Nyström method has uniformly bounded condition number but uses dense solves up to n = 128 (8,385 unknowns) ([DRNA 2022](https://www.maths.tcd.ie/EMIS/journals/DRNA/pdf/laguardia_russo.pdf)).
- **Histopolation** on Padua, Fekete and Leja triangles appeared in 2026 ([arXiv 2506.03025](https://arxiv.org/abs/2506.03025)).
- **Gibbs reduction on Lissajous data** relies on heuristic spectral filters plus Canny edge detection ([DRNA 2017](https://www.kurims.kyoto-u.ac.jp/EMIS/journals/DRNA/pdf/demarchierbmarchetti_drna2017.pdf)).

A 2025 hyperinterpolation survey states that "the construction of hyperinterpolation based directly on Padua points remains an open problem", because the degree-n Padua rule is not exact on P₂ₙ ([arXiv 2510.04904](https://arxiv.org/pdf/2510.04904)). **No paper was found** on Padua differentiation matrices, structured (HSS) solvers for Padua collocation, or multivariate updating/downdating for Padua-type sets. These are search-negative findings.

### Point sets, meshes, sampling and compression matured around the OP core

**Approximate Fekete points (AFP) and discrete Leja points (DLP)** are computed by QR with column pivoting and LU with row pivoting of Vandermonde matrices on weakly admissible meshes (WAMs). The resulting arrays are asymptotically Fekete and equidistribute to the pluripotential equilibrium measure. The Lebesgue bounds, however, are only Λ ≤ N·C(Aₙ) ([NMTMA 2011](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/524BDA8F94586AE12A73D58A462F037C/S1004897900000507a.pdf/weakly-admissible-meshes-and-discrete-extremal-sets.pdf); [Bos et al. SINUM preprint](https://www.math.unipd.it/~demarchi/papers/LejaSiam.pdf)). The Bloom–Bos–Calvi–Levenberg survey lists ten open problems, including explicit Fekete points for any K ⊂ ℂ^d, d > 1, and whether Fekete arrays of order cn form admissible meshes ([arXiv 1111.6418](https://arxiv.org/pdf/1111.6418)).

**Optimal polynomial meshes of size O(n^d)** exist on every convex body (Dai–Prymak, FoCM), but the proof does not give an explicit, small-constant construction ([arXiv 2205.14111](https://ar5iv.arxiv.org/html/2205.14111); [doi](https://doi.org/10.1007/s10208-023-09606-x)).

**Random sampling theory for least squares** is essentially complete ([Cohen–Migliorati](https://smai-jcm.centre-mersenne.org/articles/10.5802/smai-jcm.24/); [Dolbeault–Krieg–Ullrich](https://arxiv.org/abs/2204.12621); [Bartel–Schäfer–Ullrich](https://arxiv.org/abs/2202.12625)):

- Christoffel sampling with m ≍ n log n samples gives quasi-optimal weighted least squares.
- O(n) samples are possible via Kadison–Singer/Marcus–Spielman–Srivastava (non-constructive).
- Batson–Spielman–Srivastava subsampling gives a polynomial-time deterministic version.

Krieg–Ullrich (Acta Numerica) state that for the non-constructive bounds "we do not know of an explicit algorithm that achieves these bounds" ([arXiv 2602.02066](https://arxiv.org/pdf/2602.02066v2)). Explicit deterministic families prove only quadratic scaling, for example the Weil-sum grids of Zhou–Narayan–Xu ([arXiv 1401.0894](https://ar5iv.arxiv.org/html/1401.0894)).

**Carathéodory–Tchakaloff (CATCH) compression** reduces a discrete measure to at most dim Π₂ₙ points by NNLS or LP while keeping least-squares error within a factor of about 2. The authors flag the solver's worst-case complexity, and Lawson–Hanson acceleration became its own research line ([arXiv 1611.02065](https://ar5iv.arxiv.org/html/1611.02065); [Vianello list](https://www.math.unipd.it/~marcov/listcomplete.html)).

**Two Padua observations from the notes (both inferences):**

- **Padua sets as exact least-squares designs.** Padua points of degree n′ ≥ n+1, used as a least-squares design for Πₙ under the product-Chebyshev measure, give an exactly orthonormal Gram matrix. This follows from cubature precision 2n′−1 ≥ 2n+1, and the design has m ≈ dim Πₙ points. No paper states this. It also does not contradict the "Padua hyperinterpolation is open" remark, which concerns degree-n Padua points for Πₙ.
- **Padua points and Fekete arrays.** That Padua points are "asymptotically Fekete" follows from their subexponential Lebesgue constants plus the Berman–Boucksom–Witt Nyström theory. It is likewise **an unverified deduction** ([Bos et al. 2006](https://profs.scienze.univr.it/caliari/pdf/BCDMVX06.pdf); [BBCL survey](https://arxiv.org/pdf/1111.6418)).

### Vanishing ideals and border bases never met the IEP

The approximate-vanishing-ideal literature (AVI 2009, Fassino 2010, ABM/Limbeck 2013, VCA, OAVI) uses Gram/SVD solves or inverse updates in a monomial-aware order. OAVI is linear in the number of samples. It relies on Sherman–Morrison updates of (AᵀA)⁻¹ and warns: "Since matrix inversions are numerically unstable, relying on them directly would make OAVI less robust" ([arXiv 2207.01236](https://arxiv.org/pdf/2207.01236)). The pre-2010 stable-border-basis baseline is Abbott–Fassino–Torrente ([arXiv 0706.2316](https://arxiv.org/pdf/0706.2316)).

**Telen–Van Barel's** stabilized normal forms compute multiplication matrices of ℂ[x]/I with an automated, numerically chosen quotient basis ([arXiv 1708.07670](https://www.arxiv.org/abs/1708.07670v1)). **Neiger–Schost** compute syzygies from multiplication matrices in O(mD^{ω−1} + rD^ω log D) in exact arithmetic ([arXiv 1912.01848](https://arxiv.org/abs/1912.01848)).

**None of these uses the recurrence-matrix (IEP) formulation.** Yet the seed's Example 3 shows that a zero pivot yields exactly the Buchberger–Möller vanishing polynomial, with its leading monomial. This is an inferred, unexploited bridge.

## Ten open problems, ranked for a structured-NLA researcher

The ranking weighs novelty, feasibility within 6–18 months, and fit with semiseparable/HSS and unitary-chasing expertise. "Author-stated" means a published source states the gap. "Inferred" means the research notes deduced it from what was absent. Each "first step" is an experiment that could produce a publishable result or a fast no-go.

| Rank | Problem | Status | Fit | Risk |
|---|---|---|---|---|
| 1 | Backward stability and downdating of the bivariate generalized-Hessenberg IEP | Author-stated (seed 2010; VB–H–S 2014) | Very high | Low–medium |
| 2 | Closed-form recurrences on Padua/Lissajous nodes with cubature weights, plus fast reweighting | Inferred | Very high | Low |
| 3 | Truncated multivariate "Vandermonde with Lanczos" and its loss-of-orthogonality theory | Partly stated (Zhu–Nakatsukasa); truncation gap inferred | High | Medium |
| 4 | Pivot (triangular) canonical form to avoid Liu–Narayan's non-convex step in d ≥ 4 | Author-stated problem (Liu–Narayan); approach inferred | High | Medium |
| 5 | Divide-and-conquer / HSS-structured bivariate IEP below the current cost | Inferred; adjacent stated (Faghih et al.: no Laurie-type MOP extension) | Very high | High |
| 6 | IEP as a stable approximate-vanishing-ideal / border-basis engine | Inferred; adjacent stated (OAVI instability) | Medium–high | Medium |
| 7 | Stable empirical Christoffel functions via recurrences | Inferred; adjacent stated (Lasserre scaling) | Medium | Low |
| 8 | Pivoted subset selection on Padua WAMs: strong RRQR/maxvol AFP and updatable greedy point optimization | Partly stated (BBCL; VB–H–S; VB–H WAM conjecture) | High | Medium |
| 9 | Total-degree multivariate Krylov for f(A,B) with commuting A, B | Inferred | Medium–high | Medium |
| 10 | Padua-like points in d = 3 via commuting truncated multiplication matrices | Author-stated (De Marchi 2022; Xu 2024); approach inferred | Medium | Very high |

### 1. Backward stability and downdating for the bivariate IEP

**Statement.** Prove or disprove that Algorithm 1, together with its ETNA-2014 Householder variant, is backward stable. That is, the computed (Ĥₓ, Ĥ_y, Q̂) should be the exact output for nearby data (X+ΔX, Y+ΔY, w+Δw) with ‖Δ‖ = O(u). Quantify how far the computed matrices lose commutativity on their valid leading block. Then design a downdating algorithm that removes a node, and a sliding-window update/downdate.

**Status.** Author-stated twice: downdating "can be developed similar to [20]" ([seed](https://doi.org/10.1007/s11075-010-9392-y)), and "A stability analysis of these updates is not covered in this paper" ([ETNA 2014](https://etna.ricam.oeaw.ac.at/vol.42.2014/pp41-63.dir/pp41-63.pdf)). Sixteen years on, neither has been done.

**What is known.** Univariate downdating works by perfect-shift QR deflation ([arXiv 2302.00355](https://arxiv.org/abs/2302.00355)). Multiple-OP downdating uses QR-type deflation of a banded Hessenberg matrix ([arXiv 2608.25758](https://arxiv.org/abs/2608.25758)). Backward-stability testing methodology, including the N ≈ 25 breakdown of non-unitary chasing, comes from [arXiv 2506.19796](https://arxiv.org/pdf/2506.19796). The seed's own HL comparison shows a half-digit accuracy deficit with no explanation ([seed](https://doi.org/10.1007/s11075-010-9392-y)).

**A twist specific to two variables (my inference).** A perfect shift in Hₓ alone deflates a node only if its x-coordinate is unique. On Padua points the x-coordinates are Chebyshev–Lobatto values and repeat heavily. Downdating therefore needs joint deflation, for example a shift on αHₓ + βH_y with generic (α, β), while restoring the generalized-Hessenberg pivot pattern in both matrices simultaneously. That is a genuinely new structured problem, not a transcription of the 1D case.

**First step.**
- Reimplement Algorithm 1 in NumPy in core-transformation form, keeping the rotation sequence.
- Run it on Padua nodes with cubature weights, where the exact answer is nearly closed-form (Problem 2); on uniform weights; on random points; and on the noisy-circle sets of the seed's Table 1.
- Report ‖Q̂ᴴXQ̂ − Ĥₓ‖, ‖Q̂ᴴQ̂ − I‖, and the commutator norm on the leading block, as functions of N up to about 10⁴.
- Compare against HL and against two-pass Gram–Schmidt V+A.
- Prototype joint-shift deflation on a 6×6 example like the seed's §4.2.

**Fit.** This is your own algorithm, analysed with unitary bulge-chasing tools you know. It also reconnects you to the group that currently owns the univariate version.

### 2. Closed-form recurrences on Padua and Lissajous nodes, and fast reweighting

**Statement.** On Pad_n with product-Chebyshev cubature weights, derive (Hₓ, H_y, Q) in closed form. Then exploit that form to compute recurrences for perturbed weights or node sets quickly, ideally in O(N log N) to O(N^{3/2}) per update. Example perturbations: the Lebesgue-optimized weights of Van Barel–Humet, CATCH-compressed weights, Christoffel weights, and Padua subsets or supersets.

**Status.** Inferred. No paper computes discrete OPs or recurrence matrices on Padua nodes for general weights, and none studies their structure. This is a search-negative finding, not a proof of absence.

**What is known.** Van Barel–Humet's Remark 1 says that with cubature weights the product-Chebyshev basis is discretely orthogonal with "L−1 orthonormal polynomials rather than L" ([DRNA 2015](https://drna.padovauniversitypress.it/system/files/papers/VanBarelHumet_10YPDPTS_4.pdf)). The Padua rule has precision 2n−1 and is exact on p ∈ Π₂ₙ with ⟨p, T₂ₙ(y)⟩ = 0 ([Bos et al. 2006](https://profs.scienze.univr.it/caliari/pdf/BCDMVX06.pdf)).

**The structure argument (an inference; the coordinator flagged this claim as unverified).**
- Normalized T_i(x)T_j(y) is graded-lex triangular, so up to signs it is the unique IEP basis.
- The only Gram defect is the norm of T_n(y), which is the last basis element in the seed's ordering. Rescaling it gives the whole basis explicitly.
- An entry ⟨xφᵢ, φ_k⟩ is exact whenever deg φᵢ + deg φ_k ≤ 2n−2. The exactness on Π₂ₙ ⊥ T₂ₙ(y) extends this to total degree 2n for products carrying an x factor.
- Consequently Hₓ and H_y should coincide with the product-Chebyshev Jacobi structure, at most two nonzeros per column, except for entries that involve the degree-n block. For H_y this also includes the y·T_{n−1}(y)·T_n(y) coupling, which carries a T₂ₙ(y) component, and the row and column of the rescaled last element.
- Products xφᵢφ_k with both factors of degree n have degree 2n+1 and are not exact. That trailing block encodes how T_{n+1}(x)T_j(y) reduces modulo the Padua vanishing ideal, which is generated by quasi-orthogonal polynomials ([ideal-theory paper](https://arxiv.org/abs/math/0604604v1)).

**Numerical check (done after the literature search; scripts `padua_checks/padua_weights_check.py` and `padua_checks/equal_weight_lowrank.py`).** The check uses the first-family convention Pad_n = {(cos jπ/n, cos kπ/(n+1)) : j+k even} with weights 2·e_j·e_k/(n(n+1)), where e = ½ at the ends of each Chebyshev–Lobatto grid and 1 elsewhere. The weights sum to 1.
- **Basis.** With these cubature weights, the normalized product-Chebyshev basis in graded order is discretely orthonormal to machine precision (n = 6, 20, 60; max off-diagonal Gram entry about 10⁻¹⁴). The only exception is one element of norm² = 2. In this convention it is T_n(x); in the other family it is T_n(y), as in Van Barel–Humet. Rescaling that element makes Q = W^{1/2}V explicit.
- **Recurrence matrices.** Hₓ = QᵀXQ and H_y = QᵀYQ have **at most 2 nonzeros per column in every column, including the degree-n block** (n = 60: 3,720 nonzeros in Hₓ, N = 1,891). On Padua points, T_{i+1}(x)T_j(y) with i+j = n aliases onto a single basis element or vanishes. So the "trailing block" predicted above is not a dense correction: the whole pair (Hₓ, H_y) is explicit and Jacobi-like. **This part of Problem 2 is settled, and is an exact benchmark for Problem 1.**
- **The seed's own uniform-weight experiment is a low-rank modification of this explicit case.** The uniform weights differ from the cubature weights only on the 2n+1 boundary Padua points (factor 2 on edges, 4 at vertices). Hence the uniform-weight Gram matrix in the Chebyshev basis equals c·(explicit cubature Gram) + a matrix of **rank exactly 2n+1 = O(√N)**. Measured ranks were 21, 41, 81 and 161 for n = 10, 20, 40, 80.
- **Consequence for structure.** The Cholesky factor R of the uniform-weight Gram is then a diagonal plus rank-(2n+1) Cholesky factor, which is generator-representable (semiseparable) with rank O(√N). The uniform-weight recurrences are R·H^{Padua}·R⁻¹, a sparse matrix conjugated by structured triangular factors. That suggests an O(N·n²) = O(N²), or with care quasi-linear-in-N·n, algorithm for the seed's own test case, plus a concrete rank-structured target for Problem 5.
- **Unproven.** The analytic proof of the aliasing pattern and the exact rank count have not been written down. The low-rank-boundary observation is my own and does not appear in any paper found.

**First step.**
- Run Algorithm 1 on Pad_n, n = 10…100, with cubature weights.
- Plot the sparsity of Hₓ and H_y, and fit the trailing block against the ideal generators.
- Treat a weight change W → W(I+E) as a sequence of Christoffel/Geronimus-type modifications applied through rotations (cf. [arXiv 2302.00355](https://arxiv.org/abs/2302.00355)).
- Use the masked-DCT structure of the Chebyshev–Vandermonde matrix for fast matvecs ([Erb et al. survey](https://www.kurims.kyoto-u.ac.jp/EMIS/journals/DRNA/pdf/erb_etal_10ypdpts.pdf)).

**Fit.** Very high, and low risk. It produces exact test problems for Problem 1 and a fast inner loop for Problem 8. The same programme applies to Lissajous, Xu and Xu-minimal-cubature nodes.

### 3. Multivariate Vandermonde with Lanczos

**Statement.** Analyse the truncated short recurrence: orthogonalize x·φ_k only against degree blocks n−1, n and n+1, at O(MN^{3/2}). Compare it with full V+A at O(MN²) and with the Givens IEP. Develop partial or selective reorthogonalization exploiting Xu's block-tridiagonal structure, with a Paige-style loss-of-orthogonality theory. Determine whether the MOP finding that "Arnoldi beats Lanczos" carries over.

**Status.** Loss of orthogonality is author-stated for multivariate V+A ([Zhu–Nakatsukasa](https://arxiv.org/html/2301.12241v2)). The truncation gap is inferred: Hokanson, Zhu–Nakatsukasa and Zhang et al. all use full Gram–Schmidt ([Hokanson](https://arxiv.org/pdf/2009.10803); [Zhang et al.](https://arxiv.org/html/2404.09266v2)).

**What is known.** HL 2002 is the truncated method. The seed found it slightly more accurate than the Givens IEP at small N ([seed](https://doi.org/10.1007/s11075-010-9392-y)). Zaccaron documented loss of orthogonality and repaired it with reorthogonalization ([thesis](https://www.math.unipd.it/~alvise/TESI_STUDENTI/ZACCARON/ZACCARON_prefinale.pdf)).

**First step.**
- Obtain HL 2002 (it heads the acquisition table).
- Implement truncated, full and selective variants.
- Run them on the irregular domains and samplings of Zhu–Nakatsukasa at N up to about 5,000 and M up to about 10⁶, tracking ‖QᵀQ − I‖ and least-squares accuracy versus N.
- Feed the result into their near-optimality bound.

**Fit.** High: this is Lanczos-type structured NLA, and it connects your line to the Nakatsukasa/Trefethen V+A community, which does not cite it.

### 4. A pivot canonical form for multivariate Stieltjes in d ≥ 4

**Statement.** Liu–Narayan fix the orthogonal freedom inside each degree block by an SVD normalization. That normalization forces a non-convex optimization for d > 3. Replace it with the seed's triangular "positive pivot" normalization, which reduces to sequences of Givens/Householder eliminations in any d. Give the explicit block-diagonal orthogonal conversion between the two forms and compare their conditioning.

**Status.** The problem is author-stated: the method "requires the numerical solution to a non-convex optimization problem in more than three dimensions ... whose investigation would be a natural extension" ([arXiv 2202.04843](https://arxiv.org/pdf/2202.04843)). The pivot-form approach is inferred.

**What is known.** In d = 2 Liu–Narayan is explicit. The seed's scheme claims a straightforward d-variate extension, but it was never implemented ([seed](https://doi.org/10.1007/s11075-010-9392-y)).

**Risk.** The triangular form depends on the monomial order and can have tiny pivots. Those pivots are exactly the near-vanishing polynomials of Problem 6. So stability-driven variable choice must be part of the design.

**First step.** Implement a d-variate pivot-normalized Lanczos/IEP on Monte Carlo samples of a non-product measure in d = 4. Compare the recurrence conditioning with a Liu–Narayan d = 3 reference, and check the commuting constraints.

**Fit.** High. It is a short, clean paper that answers a stated open problem.

### 5. A divide-and-conquer or rank-structured bivariate IEP

**Statement.** Find an algorithm below the current cost class. Possible routes:

- merge (Q, Hₓ, H_y) for two point sets by a structured update (a bivariate analogue of the univariate divide-and-conquer IEP);
- compress Q, which satisfies the displacement equations XQ = QHₓ and YQ = QH_y, or compress its rotation sequence, in HSS/semiseparable form;
- a blocked (BLAS-3) update that adds p points at a time.

**Status.** Inferred. The adjacent gap is stated: "We are not aware of any extension of Laurie's approach to MOPs" ([arXiv 2506.19796](https://arxiv.org/pdf/2506.19796)). The BLAS-2 Householder variant is the only performance data point ([ETNA 2014](https://etna.ricam.oeaw.ac.at/vol.42.2014/pp41-63.dir/pp41-63.pdf)).

**Cost baselines (unverified).** The notes estimate that exploiting the band of half-width about √(2k) gives O(k^{3/2}) per added point and **O(N^{5/2})** in total, against the O(k²) per step (O(N³) total) reported in ETNA 2014. **This estimate is unverified.** Fill-in during chasing could invalidate it, so measure it before building on it. For real nodes Hₓ and H_y are exactly zero outside the band, so any compressible structure must lie in Q or in the rotations. The bandwidth Θ(degree) is forced by full-rank A_{n,i} blocks for total degree.

**First step.** Measure the numerical ranks of off-diagonal blocks of Q (= WΦ) and of the rotation-sequence "layers" for Padua, uniform-grid and random nodes. If the ranks are small, an HSS merge in the spirit of SuperDC is the natural design.

**Fit.** The best match to your HSS/pySuperDC experience, but the highest-risk technical item.

### 6. The IEP as a stable approximate-vanishing-ideal engine

**Statement.** Run the IEP with tolerance-based pivot rejection. It should then return three things together, from unitary transformations only: an order ideal O (the accepted pivots), an orthonormal basis of span O on the points, and approximate border polynomials (the rejected pivots). Hₓ and H_y restricted to O should be the multiplication matrices of ℝ[x,y]/I in an orthonormal basis.

**Status.** Inferred. The adjacent instability is stated by OAVI ([arXiv 2207.01236](https://arxiv.org/pdf/2207.01236)).

**What is known.** The seed's zero-pivot example ([seed](https://doi.org/10.1007/s11075-010-9392-y)); Telen–Van Barel normal forms ([arXiv 1708.07670](https://www.arxiv.org/abs/1708.07670v1)); stable border bases for ideals of points ([arXiv 0706.2316](https://arxiv.org/pdf/0706.2316)).

**First step.** Sample noisy points near a curve union, as in the seed's two-circle example. Compare the IEP, ABM/AVI and OAVI on vanishing residuals, generator degrees and robustness to noise. Add a sliding-window variant using Problem 1's downdating.

**Fit.** Medium–high. It links structured NLA to a computer-algebra and machine-learning audience.

### 7. Stable empirical Christoffel functions

**Statement.** Compute the empirical kernel Kₙ(x,x) = Σ φ_k(x)² by recurrence (IEP, HL or truncated V+A) instead of by inverting the monomial moment matrix. Report cost (O(mN^{3/2}) for truncated recurrences) and accuracy versus degree.

**Status.** Inferred application. The scaling problem is stated by Lasserre ([slides](https://homes.esat.kuleuven.be/~sistawww/bdm/backtotheroots/wp-content/uploads/christoffel-1.pdf); [arXiv 1701.02886](https://arxiv.org/pdf/1701.02886)).

**First step.** On 2D point clouds, plot the error in Kₙ against n for moment inversion, regularized inversion and the recurrence. The breakdown degree of the moment approach is the headline result.

**Fit.** Medium, but quick, and it reaches a new readership.

### 8. Pivoted subset selection and updatable greedy point optimization on Padua WAMs

**Statement.** Replace the plain QR with column pivoting used for AFP with strong rank-revealing QR or maxvol, plus swap refinement. Aim to prove Lebesgue bounds sharper than Λ ≤ N·C(Aₙ). Then speed up Van Barel–Humet–Sorber-type greedy optimization to n ≫ 60. Maintain the OP basis by bivariate updating (Problem 1) and evaluate the Lebesgue function with DCT-fast transforms. A variant is to make the IEP's choice of multiplying variable stability-driven, the analogue of column pivoting.

**Status.** Partly author-stated:
- BBCL problems ([arXiv 1111.6418](https://arxiv.org/pdf/1111.6418));
- "more investigation is necessary to make this approach more robust" ([ETNA 2014](https://etna.ricam.oeaw.ac.at/vol.42.2014/pp41-63.dir/pp41-63.pdf));
- the unproven WAM conjecture for the greedy sets ([DRNA 2015](https://drna.padovauniversitypress.it/system/files/papers/VanBarelHumet_10YPDPTS_4.pdf));
- no explicit algorithm attaining the optimal sampling bounds ([Krieg–Ullrich](https://arxiv.org/pdf/2602.02066v2)).

The strong-RRQR/maxvol route and the updating route are inferred.

**What is known.** Λ ≈ 9.2 for Padua against about 7.3 for optimized sets at degree 20, with Padua density near the boundary "not high enough" ([ETNA 2014](https://etna.ricam.oeaw.ac.at/vol.42.2014/pp41-63.dir/pp41-63.pdf)). Weighted AFP has full theory only in 1D ([arXiv 1708.01296](https://arxiv.org/pdf/1708.01296)).

**First step.** Start from a Padua WAM of degree 2n. Run QRCP, strong RRQR and maxvol, followed by swap sweeps. Report Λ against degree up to n = 100 and compare with the published optimized values.

**Fit.** High: pivoting and rank-revealing factorizations sit at the centre of the problem.

### 9. Total-degree multivariate Krylov for f(A,B)

**Statement.** For commuting A and B, build an orthonormal basis of span{AⁱBʲb : i + j ≤ n}, of dimension about n²/2, through the generalized-Hessenberg recurrence. Approximate f(A,B)b ≈ ‖b‖V f(H_A,H_B)e₁ with total-degree exactness. The tensorized Krylov spaces of the bivariate matrix-function literature have dimension n².

**Status.** Inferred. Kressner's bivariate matrix-function work and Kressner–Oehme 2026 use tensorized or block-triangular Krylov spaces and cite neither HL nor the seed ([arXiv 1802.05759](https://arxiv.org/abs/1802.05759); [arXiv 2601.21799](https://arxiv.org/html/2601.21799v1)).

**First step.** Take A = I⊗T₁ and B = T₂⊗I, compute f(A,B)b, and compare convergence with the tensorized method per matrix-vector product.

**Fit.** Medium–high. It is a new application of the seed in mainstream NLA.

### 10. Padua-like points in three dimensions via joint spectra

**Statement.** Pose the search for unisolvent total-degree sets in [−1,1]³ with polylogarithmic Lebesgue constant, or for near-Möller-bound Chebyshev cubature, as a commuting-matrix completion problem. The target nodes are the joint spectrum of truncated multiplication matrices with prescribed product-Chebyshev structure up to a given degree, which is the classical link between Gaussian cubature and commuting Jacobi matrices.

**Status.** The goal is author-stated as the field's biggest open problem ([De Marchi 2022](https://www.math.unipd.it/~demarchi/papers/paperCMA2022.pdf)); Möller-bound families for d > 2 are unknown ([Xu 2024](https://arxiv.org/html/2407.09903v1)). The joint-spectrum approach is inferred. In 3D, Chebyshev curves generically do not self-intersect, so the generating-curve mechanism fails ([arXiv 1502.04114](https://ar5iv.labs.arxiv.org/html/1502.04114)).

**First step.** Reproduce Pad_n in 2D as the joint spectrum of a completed (Hₓ, H_y), with the trailing block from Problem 2. Then attempt the 3D analogue by minimizing commutator norms over the free trailing blocks. Even a non-existence certificate for small n would be publishable.

**Fit.** Medium; very high risk, very high payoff.

### Outside the core

Several author-stated approximation-theory problems fit structured NLA less well, but are worth knowing:

- the O(log n) second-order term of Λ(Pad_n) and exact asymptotics for Xu points ([arXiv 2009.07114](https://ar5iv.labs.arxiv.org/html/2009.07114));
- Λ_MP = O(n²) and the corner location of the Lebesgue maxima ([De Marchi 2022](https://www.math.unipd.it/~demarchi/papers/paperCMA2022.pdf));
- the geometry of Lebesgue-function local maxima ([arXiv 2605.23299](https://arxiv.org/pdf/2605.23299v1));
- regularized hyperinterpolation directly at Padua points ([arXiv 2510.04904](https://arxiv.org/pdf/2510.04904)).

Inferred and more applied:

- spectra and conditioning of Padua differentiation matrices;
- HSS solvers for Padua Nyström systems beyond n = 128 ([DRNA 2022](https://www.maths.tcd.ie/EMIS/journals/DRNA/pdf/laguardia_russo.pdf));
- fast structured NNLS for CATCH on DCT-structured Vandermonde matrices ([arXiv 1611.02065](https://ar5iv.arxiv.org/html/1611.02065));
- asymptotics of discrete OPs on Padua nodes with **equal** weights at degree ≈ n. This is a bivariate constrained-equilibrium question for which the seed's algorithm can supply high-degree data.

## Bibliographic conflicts and unverified claims

| Item | Issue | Resolution |
|---|---|---|
| Huhtanen–Larsen 2002 DOI | 10.1023/A:1021955019935 does not resolve | Use **10.1023/A:1021907210628** ([Crossref](https://api.crossref.org/works?query.bibliographic=On+generating+discrete+orthogonal+bivariate+polynomials+Huhtanen&rows=3)) |
| Van Barel–Humet DRNA 2015 DOI | One note gives 10.14658/pupj-drna-2015-Special_Issue-4 for this paper (from memory); another gives the same DOI for the Erb et al. survey | Collision; the PDF filename "…_4" suggests it belongs to Van Barel–Humet. **Verify both** |
| "Algorithms for modifying recurrence relations…" (Appl. Numer. Math. 2023) | Author list differs between notes (with or without Faghih) | Cite as Van Barel, Van Buggenhout, Vandebril (arXiv form); **verify** |
| Bos–Calvi–Levenberg–Sommariva–Vianello, Math. Comp. 80 (2011) | Pages 1601–1621 (Vianello list) vs 1623–1638 (BBCL survey) | **Verify** |
| Mach–Van Barel–Vandebril JCAM 272 (2014) | Pages 377–398 inferred from an index URL | **Verify** |
| Zhu–Nakatsukasa 2023 | Journal (IMA JNA?) not confirmed | Cite arXiv 2301.12241 |
| Padua2DM DOI 10.1007/s11075-010-9373-1 | Not shown on a landing page, but resolves in Semantic Scholar and matches the seed's ref. [8] | Treat as correct |
| Briani–Sommariva–Vianello 2012; De Marchi–Usevich 2014; Bos et al. SINUM 2010 | One note says no full text; others found preprints | Preprints exist (linked above); not in acquisition table |
| O(N^{5/2}) cost of banded Givens updating | An estimate in the notes, never measured | **Unverified**; measure (Problem 5) |
| Cubature-weighted Padua OPs = product Chebyshev except last element; sparse Hₓ, H_y | Remark 1 is cited; sparsity checked numerically after the search | **Numerically verified** (n ≤ 60): ≤ 2 nonzeros per column everywhere, including the degree-n block. Analytic proof still to write. Uniform-weight Gram = scaled cubature Gram + rank 2n+1 (verified to n = 80) |
| Padua degree n+1 ⇒ exact Gram for Πₙ; Padua "asymptotically Fekete" | Inferences from cubature precision and BBW-N theory | **Unverified** in the literature |
| Kolomoitsev–Lomako Padua corollary | Read through a summarizer | Check the exact statement |

## Papers without accessible preprint (to obtain), by priority

| # | Authors | Title | Venue, year | DOI / link | Why it matters |
|---|---|---|---|---|---|
| 1 | M. Huhtanen, R. M. Larsen | On generating discrete orthogonal bivariate polynomials | BIT 42 (2002) 393–407 | [10.1023/A:1021907210628](https://link.springer.com/article/10.1023/A:1021907210628) | The short-recurrence competitor. Problems 3 and 5 depend on its truncation and reorthogonalization details |
| 2 | T. Mach, M. Van Barel, R. Vandebril | Inverse eigenvalue problems for extended Hessenberg and extended tridiagonal matrices | J. Comput. Appl. Math. 272 (2014) | [10.1016/j.cam.2014.03.015](https://doi.org/10.1016/j.cam.2014.03.015) | Seed citer; unitary-similarity IEP machinery for extended Hessenberg matrices |
| 3 | A. Sommariva, M. Vianello | Compression of multivariate discrete measures and applications | Numer. Funct. Anal. Optim. 36 (2015) 1198–1223 | [10.1080/01630563.2015.1062394](https://doi.org/10.1080/01630563.2015.1062394) | Seed citer; Tchakaloff compression requiring discrete OP bases |
| 4 | T. Mach, R. Vandebril, M. Van Barel | Inverse eigenvalue problems linked to rational Arnoldi, and rational, (non)symmetric Lanczos | KU Leuven TW report, 2013 | [Lirias](https://lirias.kuleuven.be/retrieve/5886817b-138f-492b-a0b0-b11ce687bd8f) (found, not opened) | Seed citer; rational IEP analogue |
| 5 | Y. Xu | On discrete orthogonal polynomials of several variables | Adv. Appl. Math. 33 (2004) 615–632 | [10.1016/j.aam.2004.03.002](https://doi.org/10.1016/j.aam.2004.03.002) | Block-tridiagonal theory underlying all truncation arguments |
| 6 | C. F. Dunkl, Y. Xu | Orthogonal Polynomials of Several Variables, 2nd ed. | Cambridge UP, 2014 | [10.1017/cbo9781107786134](https://doi.org/10.1017/cbo9781107786134) | Reference theory for Problems 2, 4 and 10 |
| 7 | M. Humet | PhD thesis | KU Leuven, ~2015–16 | [Math Genealogy](https://mathgenealogy.org/id.php?id=250291) | Likely contains unpublished extensions of the seed's machinery |
| 8 | C. Fassino; D. Heldt, M. Kreuzer, S. Pokutta, H. Poulisse; J. Limbeck | Almost vanishing polynomials…; Approximate computation of zero-dimensional ideals; ABM thesis | J. Symb. Comput. 45 (2010); 44 (2009); Passau 2013 | DOIs from memory, unverified | AVI/ABM baselines for Problem 6 |
| 9 | J. B. Lasserre, E. Pauwels, M. Putinar | The Christoffel–Darboux Kernel for Data Analysis | Cambridge UP, 2022 | [Cambridge](https://resolve.cambridge.org/core/books/christoffeldarboux-kernel-for-data-analysis/empirical-christoffeldarboux-analysis/F265B79C7993247610247B34D9989C1D) (DOI 10.1017/9781108937078 unverified) | Shows whether any computational chapter goes beyond moment inversion (Problem 7) |
| 10 | A. Marco, J.-J. Martínez, R. Viaña | Least squares problems involving generalized Kronecker products and application to bivariate polynomial regression | Numer. Algorithms (2019) | [10.1007/s11075-018-0592-1](https://doi.org/10.1007/s11075-018-0592-1) | Competing structured-NLA (Kronecker, Bernstein–Vandermonde) route to bivariate least squares |
| 11 | D. Kressner | Bivariate matrix functions | Oper. Matrices 8 (2014) (unverified) | — | Baseline for Problem 9 |
| 12 | L. A. Harris | Lagrange polynomials, reproducing kernels and cubature in two dimensions; Alternation points and bivariate Lagrange interpolation | J. Approx. Theory 195 (2015) 43–56; J. Comput. Appl. Math. 340 (2018) 43–52 | [UKY record](https://scholars.uky.edu/en/publications/lagrange-polynomials-reproducing-kernels-and-cubature-in-two-dime/); check [possible preprint](https://www.ms.uky.edu/~larry/paper.dir/Alternation_JCAM) | Generalized even/odd node sets for Problem 2's programme |
| 13 | L. A. Harris, B. Simanek; L. A. Harris | Interpolation and cubature for rectangular sets of nodes; Bivariate Lagrange interpolation at the Chebyshev nodes | Proc. AMS 149 (2021); 138 (2010) | [10.1090/proc/15414](https://www.ams.org/journals/proc/2021-149-08/S0002-9939-2021-15414-2); [AMS 2010](https://www.ams.org/proc/2010-138-12/S0002-9939-2010-10581-6/) | Same as row 12; possibly free under the AMS 5-year rule |
| 14 | R. Cools, K. Poppe | Chebyshev lattices, a unifying framework for cubature with Chebyshev weight function | BIT 51 (2011) 275–288 | [10.1007/s10543-010-0300-6](https://link.springer.com/article/10.1007/s10543-010-0300-6) | Lattice cubatures as inner-product nodes for Problems 2 and 10 |
| 15 | H. Wang, K. Wang, X. Wang | On the norm of the hyperinterpolation operator on the d-dimensional cube | Comput. Math. Appl. 68 (2014) 632–638 | DOI unverified | The O(log^d n) result for 3D context |
| 16 | A. Kroó | On optimal polynomial meshes (and the 2019 d = 2 proof) | J. Approx. Theory 163 (2011) (DOI 10.1016/j.jat.2011.03.007 unverified) | — | Mesh-existence background for Problem 8 |
| 17 | G. Meurant, A. Sommariva | On the computation of sets of points with low Lebesgue constant on the unit disk | J. Comput. Appl. Math. (2019) | [10.1016/j.cam.2018.06.051](https://doi.org/10.1016/j.cam.2018.06.051) | Cites HL and VB–H–S; point-optimization competitor |
| 18 | L. Bos, F. Piazzon, M. Vianello | Near G-optimal Tchakaloff designs | Comput. Statistics 35 (2020) 803–819 | [10.1007/s00180-019-00933-8](https://doi.org/10.1007/s00180-019-00933-8) | Weights for Problem 2 tests |
| 19 | R. Berman, S. Boucksom, D. Witt Nyström; T. Bloom, L. Bos, N. Levenberg, S. Waldron | Fekete points and convergence towards equilibrium measures…; On the convergence of optimal measures | Acta Math. 207 (2011); Constr. Approx. 32 (2010) | DOIs unverified (10.1007/s11511-011-0067-x) | Theory behind the "asymptotically Fekete" deduction |
| 20 | C. Kaethner et al.; L. Schmiester et al. | Non-equispaced system matrix acquisition for MPI…; Direct image reconstruction … Chebyshev-based matrix compression | IEEE TMI 35 (2016); IEEE TCI 3 (2017) | [10.1109/TMI.2016.2580458](https://doi.org/10.1109/TMI.2016.2580458); TCI DOI not retrieved | Structured system matrices on Lissajous nodes (applied niche) |
| 21 | M. Huhtanen | Switching games for image compression | IEEE Signal Process. Lett. (2025) | [10.1109/LSP.2025.3543744](https://doi.org/10.1109/LSP.2025.3543744) | Shows whether HL's author revisited 2D discrete OPs |
| 22 | R. Montagna, G. D. Finlayson; De Marchi et al. (MELECON 2020); S.-D. Zhou et al.; others | Padua image indexing; fake nodes for MPI; time-varying modal analysis; misc. | IET IP 6 (2012); MELECON 2020; JSV 2014; etc. | [10.1049/iet-ipr.2010.0498](https://doi.org/10.1049/iet-ipr.2010.0498); [10.1016/j.jsv.2014.02.001](https://doi.org/10.1016/j.jsv.2014.02.001) | Low priority; application context only |

Journal versions only, since preprints exist and were read: Faghih et al. SINUM 2026 ([10.1137/25m1770965](https://doi.org/10.1137/25m1770965)); Liu–Narayan SISC 2023 ([10.1137/22M1477131](https://doi.org/10.1137/22M1477131)); Van Buggenhout–Van Barel–Vandebril, Numer. Algorithms 2022 (arXiv 2103.04788; DOI 10.1007/s11075-021-01116-7 unverified); the Appl. Numer. Math. 2023 modification paper ([10.1016/j.apnum.2023.07.009](https://doi.org/10.1016/j.apnum.2023.07.009)). Your own unindexed 2009/2010 items ("Multivariable orthogonal polynomials and structured matrix computations"; "Recurrence relations for multivariable orthogonal polynomials and discrete least-squares approximations") were not found online.

## Conclusion

The striking fact is not that the 2010 method was superseded. It is that **its competitors rediscovered its problem without its structure**. Multivariate V+A pays O(MN²) for full orthogonalization that Xu's block structure makes unnecessary. Liu–Narayan's d > 3 obstacle is an artefact of the canonical form they chose. The empirical-Christoffel and vanishing-ideal communities still invert Gram matrices, which their own authors call unstable. Meanwhile your former group spent 2019–2026 building, in one variable, the stability-tested chasing and deflation machinery that a bivariate version needs. That makes the timing unusually good: a bivariate paper that combines Problems 1 and 2 would be the natural sequel to the 2026 MOP updating/downdating paper, written by the person who wrote the original.

Strategically, Problem 2 is the cheapest entry point and should come first. It produces exact ground truth that turns Problem 1's stability study from anecdotal into rigorous. It tests the unverified sparsity and O(N^{5/2}) claims within days. And it opens the Padua-specific line, joint spectra and 3D, at no extra cost. The HSS route (Problem 5) is the long-horizon bet. It should start only after the rank measurements in its first step show that Q or the rotation sequence actually compresses.

## References

**Seed and direct relatives**
- M. Van Barel, A. Chesnokov, Numer. Algorithms 55 (2010) 383–402 — https://doi.org/10.1007/s11075-010-9392-y
- M. Huhtanen, R. M. Larsen, BIT 42 (2002) 393–407 — https://link.springer.com/article/10.1023/A:1021907210628
- M. Van Barel, M. Humet, L. Sorber, ETNA 42 (2014) 41–63 — https://etna.ricam.oeaw.ac.at/vol.42.2014/pp41-63.dir/pp41-63.pdf
- M. Van Barel, M. Humet, DRNA 8 (2015) 37–50 — https://drna.padovauniversitypress.it/system/files/papers/VanBarelHumet_10YPDPTS_4.pdf
- A. Sommariva, M. Vianello, Numerical hyperinterpolation over nonstandard planar regions, Math. Comput. Simul. (2017) — https://www.research.unipd.it/retrieve/8b370fff-6879-4d9f-92c8-114cb1d34cef/multivop.pdf
- M. Zaccaron, M.Sc. thesis, Padova 2014 — https://www.math.unipd.it/~alvise/TESI_STUDENTI/ZACCARON/ZACCARON_prefinale.pdf
- L.-H. Zhang, Y.-N. Zhang, L. Yang, Y. Wu, arXiv:2404.09266 — https://arxiv.org/abs/2404.09266
- Semantic Scholar / OpenAlex / OpenCitations records — https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11075-010-9392-y/citations?fields=title,authors,year,venue,externalIds&limit=1000 ; https://api.openalex.org/works/https://doi.org/10.1007/s11075-010-9392-y ; https://api.opencitations.net/index/v1/citations/10.1007/s11075-010-9392-y

**Leuven univariate structured IEPs**
- N. Van Buggenhout, M. Van Barel, R. Vandebril, arXiv:2103.04788 — https://arxiv.org/pdf/2103.04788
- N. Van Buggenhout, On generating Sobolev orthogonal polynomials, Numer. Math. 2023 — https://ar5iv.labs.arxiv.org/html/2302.10691
- M. Van Barel, N. Van Buggenhout, R. Vandebril, arXiv:2302.00355 / Appl. Numer. Math. 2023 — https://arxiv.org/abs/2302.00355
- A. Faghih, M. Van Barel, N. Van Buggenhout, R. Vandebril, arXiv:2407.05945 — https://arxiv.org/abs/2407.05945
- A. Faghih, M. Rinelli, M. Van Barel, R. Vandebril, R. Vermeiren, arXiv:2506.19796 / SINUM 2026 — https://arxiv.org/pdf/2506.19796
- A. Faghih, M. Van Barel, R. Vandebril, arXiv:2608.25758 (2026) — https://arxiv.org/abs/2608.25758
- R. Vermeiren, arXiv:2601.11317 (2026) — https://arxiv.org/abs/2601.11317v1

**Arnoldi, Stieltjes, sparse recurrences, Christoffel–Darboux**
- P. Brubeck, Y. Nakatsukasa, L. N. Trefethen, SIAM Rev. 63 (2021) — https://arxiv.org/pdf/1911.09988
- J. M. Hokanson, arXiv:2009.10803 — https://arxiv.org/pdf/2009.10803
- W. Zhu, Y. Nakatsukasa, arXiv:2301.12241 — https://arxiv.org/html/2301.12241v2
- A. P. Austin et al., arXiv:1912.02272 / CPC 2020 — https://arxiv.org/abs/1912.02272v1
- Z. Liu, A. Narayan, SISC 2023 — https://arxiv.org/pdf/2202.04843
- S. Olver, A. Townsend, G. Vasil, arXiv:1801.09099 — https://arxiv.org/abs/1801.09099
- T. Gutleb, S. Olver, R. M. Slevinsky, arXiv:2302.08448 — https://arxiv.org/abs/2302.08448
- J. B. Lasserre, E. Pauwels, arXiv:1701.02886 — https://arxiv.org/pdf/1701.02886 ; Lasserre slides 2024 — https://homes.esat.kuleuven.be/~sistawww/bdm/backtotheroots/wp-content/uploads/christoffel-1.pdf
- D. Kressner, arXiv:1802.05759 — https://arxiv.org/abs/1802.05759 ; D. Kressner, F. Oehme, ETNA 65 (2026) — https://arxiv.org/html/2601.21799v1

**Padua and Lissajous theory**
- S. De Marchi, Constr. Math. Anal. 5 (2022) 14–36 — https://www.math.unipd.it/~demarchi/papers/paperCMA2022.pdf
- Y. Kolomoitsev, T. Lomako, Appl. Math. Comput. 403 (2021) — https://arxiv.org/abs/2009.07114
- P. Dencker, W. Erb, Y. Kolomoitsev, T. Lomako, J. Complexity 43 (2017) — https://arxiv.org/abs/1608.03451
- P. Dencker, W. Erb, JAT 219 (2017) — https://arxiv.org/abs/1511.04564 ; unifying theory — https://arxiv.org/abs/1711.00557
- W. Erb et al., survey, DRNA 8 (2015) — https://www.maths.tcd.ie/EMIS/journals/DRNA/pdf/erb_etal_10ypdpts.pdf ; Numer. Math. 133 (2016) — https://arxiv.org/abs/1411.7589 ; sphere — https://arxiv.org/abs/1802.06546 ; disk — https://arxiv.org/abs/1812.00437
- L. Bos, M. Caliari, S. De Marchi, M. Vianello, Y. Xu, JAT 143 (2006) — https://profs.scienze.univr.it/caliari/pdf/BCDMVX06.pdf ; ideal-theory approach — https://arxiv.org/abs/math/0604604v1
- L. Bos, S. De Marchi, M. Vianello, trivariate Lissajous — https://ar5iv.labs.arxiv.org/html/1502.04114
- S. De Marchi, A. Sommariva, M. Vianello, DRNA 7 (2014) — https://www.kurims.kyoto-u.ac.jp/EMIS/journals/DRNA/pdf/demarchisommarivavianello-2014-mcf.pdf
- M. Briani, A. Sommariva, M. Vianello, preprint — https://www.math.unipd.it/~alvise/PAPERS/ComputingFeketeAndLebesguePoints.pdf
- S. De Marchi, K. Usevich, LAA 449 (2014) — https://arxiv.org/abs/1311.6455 ; A. P. de Camargo, S. De Marchi, DRNA 8 (2015) — https://www.math.unipd.it/~demarchi/papers/Vandermondians_Padua_0305.pdf
- Y. Xu, minimal cubature I, II, Koornwinder — https://ar5iv.labs.arxiv.org/html/1102.0055 ; https://www.arxiv.org/abs/1603.08162 ; https://arxiv.org/html/2407.09903v1
- L. Białas-Cież, S. De Marchi, M. Suder, arXiv:2605.23299 (2026) — https://arxiv.org/pdf/2605.23299v1

**Padua algorithms and applications**
- M. Caliari, S. De Marchi, A. Sommariva, M. Vianello, Padua2DM, Numer. Algorithms 56 (2011) — https://www.math.unipd.it/~marcov/pdf/fastpadua.pdf
- Chebfun Padua example — http://www.chebfun.org/examples/approx2/PaduaPoints.html ; FastTransforms.jl — https://docs.juliahub.com/FastTransforms/5Lm8s/0.13.2/generated/padua/ ; Erb software — https://www.math.unipd.it/~erb/software.html
- C. An, J. Ran, H.-N. Wu, hyperinterpolation survey, arXiv:2510.04904 — https://arxiv.org/pdf/2510.04904
- A. L. Laguardia, M. G. Russo, DRNA 15 (2022) — https://www.maths.tcd.ie/EMIS/journals/DRNA/pdf/laguardia_russo.pdf
- O. Landon-Cardinal, L. C. G. Govia, A. A. Clerk, PRL 120 (2018) — https://arxiv.org/abs/1706.07816
- S. De Marchi, W. Erb, F. Marchetti, DRNA 10 (2017) — https://www.kurims.kyoto-u.ac.jp/EMIS/journals/DRNA/pdf/demarchierbmarchetti_drna2017.pdf
- L. Bruni Bruno, F. Dell'Accio, W. Erb, F. Nudo, Adv. Comput. Math. 52 (2026) — https://arxiv.org/abs/2506.03025
- V. Gapyak, T. März, A. Weinmann, Phys. Med. Biol. 70 (2025) — https://arxiv.org/abs/2505.22797v1

**Point sets, meshes, sampling, compression**
- L. Bos, S. De Marchi, A. Sommariva, M. Vianello, NMTMA 4 (2011) — https://www.cambridge.org/core/services/aop-cambridge-core/content/view/524BDA8F94586AE12A73D58A462F037C/S1004897900000507a.pdf/weakly-admissible-meshes-and-discrete-extremal-sets.pdf ; SINUM 2010 preprint — https://www.math.unipd.it/~demarchi/papers/LejaSiam.pdf
- T. Bloom, L. Bos, J.-P. Calvi, N. Levenberg, arXiv:1111.6418 — https://arxiv.org/pdf/1111.6418
- M. Gunzburger, A. L. Teckentrup, arXiv:1407.3291 — https://ar5iv.labs.arxiv.org/html/1407.3291
- F. Dai, A. Prymak, FoCM — https://ar5iv.arxiv.org/html/2205.14111
- A. Cohen, G. Migliorati, SMAI JCM 3 (2017) — https://smai-jcm.centre-mersenne.org/articles/10.5802/smai-jcm.24/
- M. Dolbeault, D. Krieg, M. Ullrich, ACHA 2023 — https://arxiv.org/abs/2204.12621 ; F. Bartel, M. Schäfer, T. Ullrich — https://arxiv.org/abs/2202.12625 ; D. Krieg, M. Ullrich, Acta Numerica — https://arxiv.org/pdf/2602.02066v2
- T. Zhou, A. Narayan, Z. Xu, arXiv:1401.0894 — https://ar5iv.arxiv.org/html/1401.0894 ; L. Guo, A. Narayan, L. Yan, T. Zhou, arXiv:1708.01296 — https://arxiv.org/pdf/1708.01296
- F. Piazzon, A. Sommariva, M. Vianello, CATCH, DRNA 10 (2017) — https://ar5iv.arxiv.org/html/1611.02065 ; Vianello publication list — https://www.math.unipd.it/~marcov/listcomplete.html
- C. An, A. Sommariva, M. Vianello, weak MZ constants, arXiv:2601.04708 — https://arxiv.org/abs/2601.04708

**Vanishing ideals and computer algebra**
- E. Wirth, H. Kera, S. Pokutta, arXiv:2207.01236 — https://arxiv.org/pdf/2207.01236
- J. Abbott, C. Fassino, M.-L. Torrente, arXiv:0706.2316 — https://arxiv.org/pdf/0706.2316
- S. Telen, M. Van Barel, arXiv:1708.07670 — https://www.arxiv.org/abs/1708.07670v1
- V. Neiger, É. Schost, J. Complexity 60 (2020) — https://arxiv.org/abs/1912.01848
