# PD-N?padua-3d-20261106-codex-T5-03 — Sharp degree-five support bounds on a fixed Gaussian grid

ID kind: PD-N.
Aliases: Gauss3 tensor-grid thinning; one-parameter finite-support moment space.
Split from: none. Split into: none.

## Statement

Let `G={-sqrt(3)/2,0,sqrt(3)/2}^3`. For normalized product arcsine measure
on the cube, every degree-five cubature whose nodes belong to G needs
at least 21 distinct nodes if its weights are positive. This is sharp.
If arbitrary nonzero real signed weights are permitted, the sharp minimum
is instead 15 distinct nodes. In particular G contains no positive
degree-five rule with at most 20 nodes, and no signed one with at most 14.

## Definitions

Degree-five exactness means exactness for all total-degree polynomials of
degree at most five; higher accidental exactness is allowed. A subset rule
is represented by a vector `w in R^G`, setting weights outside its support
to zero. Its support size is the number of nonzero coordinates. Put
`chi(x)=T_2(x_1) T_2(x_2) T_2(x_3)`, where `T_2(x)=2x^2-1`.

## Assumptions

Only this fixed 27-point grid. Weights may vary independently initially;
no coordinate symmetry is imposed. The measure is normalized product
arcsine, and exactness is total degree five. Repeated copies of a node
are combined before counting support.

## Status by part

Overall status: PROVED, by the hand proof below. The exact computation
is corroborative and is not needed for the mathematical reduction.
Candidate IDEA?padua-3d-20261106-codex-T5-05: retained scoped certificate.
Attempted thinning to <=20 positive nodes on G: REJECTED: refuted.
This is a finite-support consequence of standard tensor orthogonality;
no historical novelty claim is made.

## Negative-result scope

Attempted mechanism: choose a subset of the three-point Gaussian tensor
grid and freely reweight it to degree five (T5-05).
Parameter range: precisely the above G and measure, exactness degree five,
all real weight vectors; positivity and signed cases distinguished.

## Depends on

The elementary three-point one-dimensional Chebyshev rule, proved directly
below; tensor interpolation and orthogonality. No imported literature
theorem or software output is a proof dependency.

## Checks

Executed:
`python topics/padua-3d-20261106/code/t5_support.py --output
topics/padua-3d-20261106/evidence/t5-support.json`.
Python 3.12.14 / SymPy 1.14.0; exact rational 56-by-27 moment matrix,
rank 26, proposed kernel residual zero, parameter endpoints and all
support-dropping parameter values verified. Independent actual replay
PENDING; no computer-proof acceptance is claimed from this run alone.

## Sources

Known mechanisms: product Gaussian quadrature and finite tensor
interpolation; predecessor context IDEA-207 and X7/IDEA-029/120.
The proof is self-contained. No source's conjecture is used.

## Proof or evidence

The normalized one-dimensional arcsine moments at powers 0,1,...,5 are
`1,0,1/2,0,3/8,0`. Averaging over the three nodes
`{-sqrt(3)/2,0,sqrt(3)/2}` gives exactly those values: sign symmetry
kills odd moments, and the even moments are `1`, `(2/3)(3/4)=1/2`
and `(2/3)(9/16)=3/8`. Therefore the uniform 27-node product rule,
with weight `1/27` per node, integrates every total-degree-five polynomial.

On each axis the nodes are the three distinct zeros of
`T_3(x)=4x^3-3x`. Modulo this polynomial, every power reduces to
degree at most two, and reduction never increases total degree.
Hence evaluation on G of any total-degree-five polynomial is a linear
combination of the tensor modes

`T_a(x_1) T_b(x_2) T_c(x_3)`, `0<=a,b,c<=2`, `(a,b,c)!=(2,2,2)`.

All these 26 modes already have total degree at most five. Together
with the remaining mode chi they form a basis of all functions on G:
each univariate degree-two evaluation matrix at three distinct nodes
is invertible, and their tensor product is invertible.

In the uniform discrete inner product on the three univariate nodes,
`T_0,T_1,T_2` are orthogonal: their pairwise products have degree at
most four, where the checked three-point rule agrees with continuous
arcsine orthogonality. Tensor orthogonality follows. Thus chi is
orthogonal to every one of the 26 allowed modes. A vector of changes
to the uniform weights annihilates the degree-five evaluation space
if and only if it is a scalar multiple of chi. Consequently all
degree-five rules on G, without any positivity or symmetry assumption,
are exactly

`w_x(t)=(1+t chi(x))/27`, `t in R`.

At a nonzero coordinate, `T_2=1/2`, and at zero, `T_2=-1`.
The four possible chi values, their multiplicities and zero-weight
parameters are therefore:

| Number of zero coordinates | chi | Multiplicity | Weight zero at t |
|---|---|---|---|
| 0 | 1/8 | 8 | -8 |
| 1 | -1/4 | 12 | 4 |
| 2 | 1/2 | 6 | -2 |
| 3 | -1 | 1 | 1 |

Every weight is nonnegative exactly when the four linear inequalities
`1+t chi>=0` hold, namely `-2<=t<=1`. In the open interval all 27
weights are positive; at t=-2 exactly six vanish, leaving 21 positive
weights; at t=1 only the centre vanishes, leaving 26. This proves
the sharp positive minimum and gives its attaining rule explicitly.
At t=-2 the remaining weights are `1/36` on the eight no-zero nodes,
`1/18` on the twelve one-zero nodes, and `1/9` at the centre.

Without positivity, weights vanish only at the four listed distinct
parameter values. At most one group vanishes at once. The largest
group has twelve nodes and vanishes at t=4, leaving 15 nodes. There
the eight no-zero nodes have weight `1/18`, the six two-zero nodes
have weight `1/9`, and the centre has weight `-1/9`. This proves
the signed minimum and sharpness. The proof enumerates every real
weight vector, not just those found by an LP solver.

## Scope

Only fixed-support cubature is excluded. The pipeline also checked a
positive 14-node degree-five rule with nodes outside G, so the 21-node
bound is certainly not universal. It does not obstruct arbitrary
near-Gaussian cube cubature, all Chebyshev grids, larger degree, or
total-degree interpolation without cubature.

## Open items

Independent code replay and required Claude audit remain pending.
General support minimization and the universal 3D problem remain OPEN.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, rules
`ccd9e905d19c0c625c196c4a3f3e707058ed042a`: candidate registered after
D4 and before the support execution; exact check and hand proof written.
The original broader minimal-cubature target is not narrowed or closed.

## Supplementary check addendum — 2026-11-06

[Distinct Astra high check](../independent-checks-computation.md) completed
within its stated scope, including actual separate execution. Earlier
pending-check wording records the development state. Required Claude
substantive audit remains due; this addendum changes no mathematical claim.


## Completed-audit process addendum — 2026-11-06 — m5

[Claude audit-01](../audit-01.md) completed the substantive independent audit
of candidate f1a5b0936d8fb2b033c69af59a6366550f170999, including the recorded
independent executions, after the supplementary Astra checks. Its accepted
mathematical scopes supersede earlier “audit/replay/rerun pending” and
“planned, no run claimed” process descriptions where those refer to that
completed work. This addendum changes no mathematical statement or status;
MEASURED observations remain MEASURED and OPEN targets remain OPEN. The
response dispositions, ID-kind mappings and evidence changes were covered
by [Claude audit-02](../audit-02.md); its accepted mathematical scope is
recorded there. This dated correction changes no statement or status.


## Attempted-construction field correction — 2026-11-06 — m9/m10

The successful affine-weight classification is IDEA?padua-3d-20261106-codex-T5-05,
not a failed mechanism. The negative construction subtargets are explicitly
recorded as IDEA?padua-3d-20261106-codex-T5-grid-construction in
../candidates-rejected-response-01.md: ≤20 positive nodes or ≤14 signed
nodes on this exact Gaussian grid. That supersedes the earlier attempted-
mechanism field. The theorem/ID/status is unchanged; final crosswalk must
map IDEA T5-05 to PD-N T5-03 using full namespace-qualified IDs.
