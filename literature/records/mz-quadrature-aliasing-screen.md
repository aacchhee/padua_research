# mz-quadrature-aliasing-screen — Trefethen, Xiang–Bornemann, Hale–Townsend

- Access/read date: 2026-10-31. Reader: Codex; gpt-6.1-sol, high (explicit orchestrator assignment).
- These are selected primary-text readings, not complete proof audits or exhaustive screens.

## Source statements

### LIT-055 — Trefethen 2008 exact mode aliasing

- Citation: L. N. Trefethen, *Is Gauss Quadrature Better than Clenshaw–Curtis?*, SIAM Rev. 50 (2008), 67–87, DOI <https://doi.org/10.1137/060659831>.
- Text: <https://www.math.stonybrook.edu/~bishop/classes/math401.F09/Trefethen-Quad.pdf>; read abstract, Theorem 4.1 and §5 Theorems 5.1–5.2/formulas (5.2)–(5.4), published pp. 73–80 (selected portions).
- Statement: Theorem 5.2 identifies equal nodal values for T_(N+p) and T_(N-p), 0<=p<=N, on N+1 Chebyshev extrema. It consequently gives exact CC moments and errors for those modes. Theorem 5.1 uses coefficient decay to explain CC convergence for sufficiently smooth functions.
- Hypotheses: standard unweighted integral on [-1,1], actual CC rule. Theorem 5.1 includes differentiability/variation assumptions and a sufficiently-large-N condition depending on regularity.
- Relation: the exact published algebra is a direct predecessor of campaign Chebyshev defect entries. The new candidate's proposed separation is assembling the quadratic-form Gram matrix and proving 2T-Q positive by an off-diagonal sign comparison. That comparison and the uniform upper ratio <2 were not found in these selected portions. This does not clear uninspected historical sources.
- Gap: remaining text not completely screened. A fixed-function convergence theorem cannot alone control a supremum over N-dependent p².

### LIT-056 — Xiang–Bornemann 2012 coefficient-decay quadrature

- Citation: S. Xiang, F. Bornemann, *On the Convergence Rates of Gauss and Clenshaw–Curtis Quadrature for Functions of Limited Regularity*, SIAM J. Numer. Anal. 50 (2012), 2581–2587, primary <https://arxiv.org/html/1203.2445> (v3, 31 July 2012).
- Coverage: abstract, introduction theorem, §3 aliasing statement and displayed error formulas (selected text; HTML has missing reference labels).
- Statement: for Chebyshev coefficients O(m^(-s-1)), s>0, the CC error is O(N^(-s-1)). Section 3 gives exact folded Chebyshev-mode aliasing and corresponding moments.
- Locator: introduction theorem; §3 *Convergence rate of Clenshaw–Curtis quadrature*.
- Relation/gap: closest coefficient-aliasing literature; does not in inspected portions state a sharp CC squared-polynomial MZ constant. Coefficient-decay constants for an N-dependent p² require separate control.

### LIT-057 — Hale–Townsend 2014 transform

- Citation: N. Hale, A. Townsend, *A Fast, Simple, and Stable Chebyshev–Legendre Transform Using an Asymptotic Formula*, SIAM J. Sci. Comput. 36 (2014), A148–A167, DOI <https://doi.org/10.1137/130932223>.
- Text: <https://appliedmaths.sun.ac.za/~nhale/publications/HaleTownsend2014a.pdf>.
- Coverage: abstract/introduction and selected §3 formulas (3.5)–(3.10); no complete stability audit.
- Statement: the paper develops a fast transform between Legendre and Chebyshev coefficients using asymptotic representations and DCTs, with evaluation at a Chebyshev grid as an intermediate step.
- Relation/gap: a computational predecessor for basis conversion. Numerical transform stability and a CC-weighted sampling norm are different claims; no sharp CC MZ constant was extracted. The separately named Hale–Townsend Gauss–Legendre/Gauss–Jacobi nodes-and-weights paper (DOI 10.1137/120889873) was discovered at publisher abstract level only, **FULLTEXT UNVERIFIED**, and is not substituted for this transform paper.

## Bibliographic trap

<https://people.maths.ox.ac.uk/trefethen/exactness.pdf> is Trefethen's *Exactness of Quadrature Formulas*, SIAM Rev. 64 (2022), 132–150, DOI 10.1137/20M1389522, not his 2008 paper. Its abstract and §3 were inspected as context only; it is not assigned a new theorem claim here.

## History

2026-10-31: selected primary-source statements; all campaign claims retain their own proof statuses elsewhere.
