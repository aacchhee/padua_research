# PD-T?lanczos-nonproduct-codex-P1-01 — Triangle family admission

ID kind: PD-T. Aliases: N1 triangle admission; convex-hull obstruction to
affine products; T24; positive Hahn-type lattice weights.
Split from: P1 all-degree separation target (OPEN). Split into: none.

## Statement

Let `Delta={(u,v):u>=0,v>=0,u+v<=1}`. The uniform probability measure
`2 du dv` on Delta, and every measure supported on Delta with density
positive almost everywhere on its interior, are not affine images under an
invertible affine map of a
product of two real probability measures.

For every integer `N>=1`, let

    T_N={(2i/N-1,2j/N-1): i,j>=0, i+j<=N}.

Every strictly positive weighting of all these nodes is not affine-product.
Evaluation on `Pi_s` is injective for `0<=s<=N`. The number of nodes is
`M=(N+1)(N+2)/2`, so `M>N_s=(s+1)(s+2)/2` exactly when `s<N`.
Uniform weights are rational. The following further normalized weights are
positive rational whenever `a,b,c` are positive rationals:

    w_ij = N!/(a+b+c)_N * (a)_i/i! * (b)_j/j!
                              * (c)_(N-i-j)/(N-i-j)! .

Here `(a)_k=a(a+1)...(a+k-1)`, including `(a)_0=1`. For `a=b=c=1`
these are uniform. A concrete second scan choice is `a=b=c=2`.
No published Hahn-polynomial identity is asserted by naming these weights.

## Definitions and assumptions

Affine-product means the pushforward of `nu_1 x nu_2` under an invertible
affine map of R^2. Measures are finite positive probability measures; lattice
weights are positive on every listed node. Noninvertible changes are excluded
by definition and could not generate full-dimensional triangle support.

## Status by part

Overall status: PROVED (written elementary proof).

| Part | Status | Evidence |
|---|---|---|
| Non-affine-productness, lattice injectivity and rational admission | PROVED | Proof below; no computational premise |

Candidate disposition: retained as admission/supporting result. The original
P1 separation target remains OPEN; N2/N3 are separate obligations.

## Depends on

No unproved or literature dependency. Uses elementary support, convex hull,
and the falling-factorial polynomial basis.

## Checks

Analytic development only; no computer-assisted proof or independent rerun
is claimed. Exact numerical scans belong to P6 and are not premises here.

## Sources

Self-contained argument. The handoff's suggested Hahn/Proriol sources have
not been imported as proofs or claimed as primary reads.

## Proof

The closed support of a product measure is the product of its closed factor
supports: neighborhoods of a support pair have positive product mass, and a
point outside one factor support has a zero-mass product neighborhood.
Supports commute with invertible continuous affine changes. Compactness and
full dimension of either triangle support therefore force both factor
supports to be compact with at least two distinct points.

If their minima/maxima are `m_1<M_1`, `m_2<M_2`, the convex hull of their
product is exactly `[m_1,M_1] x [m_2,M_2]`: containment in the rectangle is
immediate, and its four corners belong to the support product, proving the
reverse convex-hull containment. An invertible affine image has a
nondegenerate parallelogram as convex hull, with four extreme points.
The continuous supports above are Delta and the lattice support contains
the three triangle vertices and lies within their hull. Their convex hulls
are nondegenerate triangles with three extreme points. This contradiction
proves both nonproduct assertions. Positivity of a continuous density almost
everywhere in the interior ensures every interior neighborhood has positive
mass and hence the closed support is the entire closed triangle.

For lattice injectivity, rescale to integer coordinates `(i,j)`. The products
`binom(i,a) binom(j,b)` for `a+b<=s` form a polynomial basis of Pi_s: their
leading terms are nonzero multiples of the distinct monomials `i^a j^b`.
Write a polynomial vanishing on the lattice in this basis. Evaluate at
points `(i,j)` in order of increasing `i+j`, through total degree s. A basis
term can be nonzero there only if `a<=i,b<=j`. Every term other than
`(a,b)=(i,j)` then has smaller total degree, so its coefficient has already
been proved zero; the remaining basis value is one. Induction makes every
coefficient zero. This proves injectivity through s=N. The displayed count
and its strict inequality follow from summing the row lengths.

Finally the coefficient of `t^N` in the formal power-series identity

    (1-t)^(-a)(1-t)^(-b)(1-t)^(-c)=(1-t)^(-(a+b+c))

is `(a+b+c)_N/N!`; the generalized binomial series itself follows by solving
`(1-t)F'=aF,F(0)=1` coefficient by coefficient. This coefficient identity
proves the weights sum to one. Each factor is positive rational under the
stated hypotheses. If a=b=c=1, every unnormalized summand is one, proving
uniformity without any external discrete-polynomial formula.

## Scope

N1 is passed mathematically for T24 at every tested s<=23; P6's proposed
2–16 (or 2–20) scan is within this range. Exact nodes must remain frozen as
`x=i/12-1,y=j/12-1,i+j<=24` to compare directly with predecessor T24.
The analytic family T_N is not an all-degree statement for the fixed T24
grid; an unbounded-degree theorem must also prescribe N=N(s)>s.

## Open items

All capacity growth/separation statements; N2/N3; primary source acquisition;
independent mathematical audit of this admission proof.

## History

2026-11-05: Codex P1 developer, assigned gpt-6.1-sol xhigh; rules head
`ed5515ed84e0e7b12163175dce9f22a859c89c99`. Written after the prospective
P1 registry/nearest-mechanism gate. No Git mutation or final-ID allocation.
