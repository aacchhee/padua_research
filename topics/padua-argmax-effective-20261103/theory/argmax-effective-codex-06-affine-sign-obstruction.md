# PD-N085 — An affine per-cardinal corner sign test cannot give a fixed phase radius

ID kind: PD-N.
Aliases: R6 termwise ratio obstruction; source index (3,1); n-cubed gradient/value ratio. PD-N?argmax-effective-codex-06b.
Split from: R6 uniform per-cardinal scaled-gradient candidate.
Split into: none.

## Statement

For every integer n>=4 consider the original even-checkerboard cardinal
at index (j,k)=(3,1), and c=(-1,-1). Its nonzero corner value satisfies

    q_n = L_(3,1),x(c)/L_(3,1)(c),
    lim_(n->infinity) q_n/n^3 = -5/(2*pi^2).                       (1)

Consequently no finite M can bound |q_n|<=M*n^2 for every n. For every
fixed kappa>0, the affine model

    L_(3,1)(c)+(kappa/n^2)*L_(3,1),x(c)

has the opposite sign from L_(3,1)(c) for all sufficiently large n.
Thus an argument requiring every such affine model to preserve its
corner sign cannot prove a physical radius kappa/n^2 with kappa fixed.
For all sufficiently large n its admissible radius along this single axis is at most

    -1/q_n ~ (2*pi^2/5)*n^(-3).

## Definitions and assumptions

Corrected Padua cardinals, exact real arithmetic, original physical node
indices and physical x derivative. This is an obstruction to a specified
affine sign-preservation proof step. The actual cardinal includes higher
Taylor terms, whose signs are not claimed by this result.

## Status by part

Overall status: **PROVED**. [Supplementary independent reconstruction](../independent-math-checks-01.md)
is complete and accepted; Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the stated scope.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Limit (1) and failure of the uniform affine sign step | PROVED | Exact gradient formula and elementary cosine limits |

Candidate disposition: **REJECTED: failed** for uniform termwise scaled
gradient control or uniform affine sign preservation at radius kappa/n^2.

## Negative-result scope

Attempted mechanism: bound each nonzero cardinal's gradient/value ratio
by O(n^2), then preserve its affine corner sign throughout a physical
O(n^(-2)) box. Parameters: n>=4, index(3,1), positive fixed kappa.
Aggregate sign-change estimates, weighted energy, reflection-first
bounds, true-cardinal sign stability and PD-T099 are outside this
negative statement's scope.

## Depends on

PD-T227 exact nonzero-cardinal gradient/value formula. The elementary
limit (1-cos t)/t^2->1/2 is derived from the cosine Taylor series.

## Proof or evidence

Put m=n+1, a=cos(3*pi/n), b=cos(pi/m), C=1-b and d=b-a. The index is
admissible and C,d>0. PD-T227 gives exactly

    q_n=-n^2/2+n*(a*b-1)/(C*d)-a/d+2*(1-a^2)/d^2.

The elementary Taylor limits are

    n^2*C -> pi^2/2,       n^2*d -> 4*pi^2,
    n^2*(a*b-1) -> -5*pi^2,
    n^2*(1-a^2) -> 9*pi^2.

The first, third and fourth terms in q_n are O(n^2). The second term,
divided by n^3, tends to
(-5*pi^2)/[(pi^2/2)*(4*pi^2)]=-5/(2*pi^2), proving (1).
Therefore 1+kappa*q_n/n^2 tends to minus infinity. This is exactly the
ratio of the displayed affine value to L_(3,1)(c), proving its eventual
opposite sign. The last radius asymptotic follows by inversion. QED.

## Checks and sources

Analytic proof only; exploratory values at n=16,32,64,128 motivated the
index selection but are not premises. No imported external theorem.

## Scope and open items

The smaller n^(-6) radius in codex-06b is valid. This obstruction shows
that merely sharpening its termwise affine sign constants cannot reach
the desired n^(-2) scale. The exact all-n negative slopes are retained;
aggregate control is the outstanding local obligation.

## History

2026-11-03, Codex gpt-6-astra ultra, explicit handoff02 allocation;
rules/input 8a1f394739293953e1566fd24a0a193cc78ff26f, base440d107.
The scope is an affine proof-step failure, not a local-maximizer
counterexample or a rejection of the reflection-first route.

## Final registration — 2026-11-05

Final IDs and preserved provisional aliases: [id-map](../final-id-map.json). Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the existing stated scopes; no claim, proof or epistemic status changes at registration.
