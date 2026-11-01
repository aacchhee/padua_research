# PD-T?lattice-c3-codex-01 — Exact witnesses and a degree bound for generic grid interpolation

ID kind: PD-T. Aliases: determinant-polynomial lifting; without-replacement Schwartz–Zippel bound.
Split from: none. Split into: finite measurements in c3-rank-observations.md; this supporting result does not prove an axis-separated criterion.

## Statement

Fix d=3, n>=0, positive lengths L=(L1,L2,L3), and a fixed index subset I of the product grid, with N=binomial(n+3,3) distinct triples. Assign independent indeterminates H_(r,j) to every axis label. Let V_I have rows I and columns all monomials x^a y^b z^c with a+b+c<=n in a fixed order. Put D_I(H)=det(V_I).

(1) D_I is an integer polynomial homogeneous of total degree B=3*binomial(n+3,4); its degree in each complete axis block is binomial(n+3,4), unless it is the zero polynomial.

(2) If an integer axis specialization has det(V_I) nonzero modulo any prime p, then D_I is nonzero over Q. Thus I is unisolvent on a nonempty Zariski-open subset of distinct axis lists over Q, and over every infinite characteristic-zero extension. This is a generic existence conclusion, not an assertion for all distinct axes. A nonzero exact integer determinant gives the same conclusion.

(3) Over F_p, suppose D_I is a nonzero polynomial and p>=max(Lr). Independently for each axis, draw a uniform ordered list of Lr distinct field values. Then

`Pr[D_I(H)=0] <= min(1, B/(p-max(Lr)+1)).`

If t draws are independent, the probability all t fail is at most that bound to power t. This is a mathematical probability for truly uniform random lists; a fixed pseudorandom seed gives a reproducible measurement, not a probability guarantee about that seed. The bound is applicable over F_p only when D_I mod p is nonzero; a Q-nonzero polynomial need not retain nonzero reduction at every prime.

## Assumptions and definitions

Distinctness is only within an axis. Labels may coincide across axes. Generic means outside the zero set of a nonzero polynomial after restricting to the open locus of within-axis distinctness. No positivity, cubature, special Chebyshev values or factorization hypothesis is used.

## Status by part

Overall status: PROVED (developer written proof; independent Astra reconstruction pending). These are elementary symbolic statements, without any dependence on computational output. Per-pattern witness claims and acceptance remain in their separate evidence records.

## Proof

The determinant expansion is a signed sum over bijections between columns and rows. Every term chooses each monomial once. Thus each term has total degree equal to the sum of the degrees of all monomials, and axis-block degree equal to the sum of the corresponding coordinate exponents. By symmetry, the three block degrees are equal. Their common value is

`sum_(a+b+c<=n) a = sum_(s=1)^n #{a+b+c<=n : a>=s} = sum_(s=1)^n binomial(n-s+3,3) = binomial(n+3,4).`

This proves (1), including the stated convention for a zero determinant polynomial.

The determinant expansion has integer coefficients and commutes with specialization and reduction modulo p. A nonzero modular determinant at one integer axis tuple therefore contradicts D_I=0 in Z[H], so D_I is nonzero over Q. Let A(H) be the product of all within-axis differences. The polynomial A is nonzero, and the polynomial ring is a domain, so D_I*A is nonzero. Over an infinite field a nonzero polynomial cannot vanish at all points (induct on the number of variables using the univariate root bound). Hence there is a tuple where both determinants and all differences are nonzero, and their joint nonvanishing is a nonempty Zariski-open set. This proves (2), with no appeal to sampled agreement or to a probabilistic heuristic.

For (3), order all node variables axis by axis, and sample each axis sequentially without replacement. At each variable the conditional sample set has size at least M=p-max(Lr)+1. Induct on the number of variables for any fixed nonzero polynomial F of total degree at most B. View F as a polynomial in the last variable, of degree b, with nonzero leading coefficient G in the earlier variables. G has total degree at most B-b. By induction the probability G vanishes at the earlier choices is at most (B-b)/M. Conditional on any earlier choices with G nonzero, the root bound for the last variable gives conditional failure probability at most b/M, even though the allowed last values depend on those earlier choices. Summing these two bounds gives B/M. The sampling law of earlier variables is exactly the same sequential without-replacement law needed for induction. Truncate at 1 and multiply for independent repetitions. This proves (3).

## Scope and limitations

This reduction applies to any fixed grid subset, periodic or otherwise. It proves no quantitative real conditioning, no universal arbitrary-axis unisolvence, no factorization into axis-only factors, and no Lebesgue bound. Finite exact witness outputs need committed provenance, an exact checker and an independent rerun before being promoted into a completed computer-assisted per-pattern proof.

For the actual C3 degrees n=1..6, B=3,15,45,105,210,378. At p=1009 and max length n+3, the bounds are respectively 3/1006,15/1005,45/1004,105/1003,210/1002,378/1001 (or smaller for shorter actual lengths). These are upper bounds conditional on the polynomial being nonzero modulo that prime. Two independent draws square each bound; they are not asserted probability statements for the chosen deterministic seeds.

## Depends on / sources / checks

Only determinant expansion, the univariate root bound and the elementary polynomial-ring domain property, proved as used above. Closest standard predecessor: the polynomial identity testing/Schwartz–Zippel method; no novelty claim. Code c3_rank.py supplies witness candidates, separately from this proof. Independent mathematical reconstruction: pending Astra.

## History

2026-10-31, Codex C3 developer, assigned gpt-6.1-sol xhigh; rules/base e949ef06895acd5463cdf8df7e0e5f795218f70f. Written before using any finite rank sample to upgrade a generic statement.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
