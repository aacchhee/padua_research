# PD-T?argmax-bridge-codex-D19-norm — A global norm from one adaptive phase tree

ID kind: PD-T.
Aliases: leafwise Peano norm absorption; self-norming complete certificate;
single-tree norming set; self-contained exact pruning.
Split from: D14's fixed-grid norming application.
Split into: the finite2048 metadata/pruning instance is separate.

## Statement

For EVERY integer n>=2 put m=n+1,kappa=n/m and use exactly
PD-T101/PD-T364's corrected finite kernel, endpoint weights, odd-board
primitive S_n and actual finite-polynomial collision values. Let
T={a,b>=0,a+b<=1},S^t(a,b)=S_n(pi*a,pi*b). Suppose a FINITE
collection of closed rectangles B_i covers T after clipping. Rectangles
with empty intersection may be discarded only after exact emptiness
proof; all nonempty/tangent/degenerate clipped patches remain.

For each retained rectangle have validated ACTUAL upper values at
ALL its vertices, using only value-preserving phase folding, and let
V_i be their maximum. With a proved rational p_hi>=pi put

    theta_i=(p_hi²/8)[width_a(B_i)²+kappa² width_b(B_i)²].

If theta_i<1 for EVERY retained rectangle, then the finite TRUE
continuous global norm satisfies

    M*=sup_(R²) S_n=max_T S^t
       <=R:=max_i V_i/(1-theta_i).                  (1)

Any rational M>=R, including its exact integer ceiling, therefore
bounds S_n on ALL real phases, physical lambda_n, every complete
signed board polynomial and every complete signed cardinal polynomial.
It can be used in the accepted D08/D15 corner and cover criteria.
No fixed quarter-grid, completed model or assumed argmax is required.

For a complete midpoint tree root[0,1]², discard a leaf only when
a_l+b_l>1. The corner-input set supporting(1) is EXACTLY the union
of the retained tree leaves' canonical S vertices. Additional points
in an available input file are not premises of(1) unless actually used.

Overall status: **PROVED analytic developer implication**, distinct
review pending. This supplies neither good numerical size nor a
successful finite certificate, algorithm termination or runtime theorem.

## Dependencies and proof

PD-T364/D08 provide the finite primitive, exact period/evenness and
global signed-family ordinary Peano theorem. D14 already proves true
norm finiteness and the fixed-grid absorption special case; N3 already
uses a true unknown global norm in an absorption argument. This is a
STANDARD leafwise norming variant, not a new Bernstein/interpolation,
maximum or historical norming principle. No external theorem is used.

The finite sum of absolute trigonometric polynomials is continuous.
For integers p,q with p+q even, finite board reindexing gives periods
(alpha,beta)->(alpha+p*pi,beta+q*pi); separate reflections give separate
evenness. Reducing(alpha+beta)/(2pi),(alpha-beta)/(2pi) modulo integers
into[-1/2,1/2] maps every phase pair into the closed diamond
|alpha|+|beta|<=pi, then into pi*T by evenness. Hence M* is finite
and attained on the compact T. This step establishes GLOBAL validity
of the true norm before estimating a derivative or using a sample.

Each signed primitive component has alpha frequencies r/n and beta
frequencies s/m with |r|,|s|<=n, including the exceptional highest
x coefficient ONE. Global signed-family Bernstein gives l1 second
derivative bounds M*,kappa²M*. D08's common positive Peano kernel
on B_i therefore proves, in turn coordinates,

    S^t(a,b)<=V_i+theta_i*M*, (a,b) in B_i.         (2)

No derivative of the nonsmooth absolute sum S is taken. The global
norm is not replaced by a grid norm in this step. Folding only its
vertex VALUES leaves the rectangle and widths unchanged.

Choose an actual maximizer z of S^t on T and any retained rectangle
B_j containing it. Such a retained j exists by closed coverage, also
when z lies on a tangent point, shared edge or hypotenuse. Equation(2)
at this point gives M*<=V_j+theta_j M*. Since1-theta_j>0,

    M*<=V_j/(1-theta_j)<=max_i V_i/(1-theta_i)=R.

This proves(1). It is a finite norming implication, not an assertion
that M* equals a sampled maximum. The bound also equals the safe
consequence of M*<=max_i(V_i+theta_i M*), but applying absorption
at the actual maximizer's leaf avoids mixing unrelated V/theta maxima.

Every board coefficient family of magnitude<=1 is dominated by S_n.
At every physical point PD-T364 supplies an odd-center chart with
lambda=S_n-Delta<=S_n,Delta>=0. Every cardinal coefficient family of
magnitude<=1 is dominated by lambda. Actual-corner substitutions stay
in the physical square for ALL real phase variables. Thus the same
M bounds both full signed families globally, as required by D08.
All nodes/collisions/zero terms are finite polynomial values. QED.

## Self-contained coarsening contract

For n>=160 attach the accepted generic D15 premises: positive corner
lower L, rational pi bracket, ACTUAL three-point corner witness (or
another independently proved half-diamond patch), and strict phase
FAR/NEAR/SPLIT comparisons with C02's1/32 floor applied only at actual
signedrho<=1/2 and only at noncorner physical centers. On ANY candidate
complete tree first compute its R/M from its OWN corners by(1), then
recompute its ENTIRE corner criterion and EVERY phase predicate with
that M. If they pass, the generic D15 theorem proves the exact
two-corner equality set with its correct degree parity.

Replacing a subtree by its parent rectangle preserves exact closed
coverage. It does NOT inherit its children’s bounds, their norm or
their point set. A proposed replacement is accepted only after all
parent corners have valid same-degree enclosures and the preceding
whole-candidate tests pass. By induction, any finite sequence of such
accepted replacements ends with a valid self-contained certificate;
its final norm is a function ONLY of its final retained leaf corners.
Deleted children and their corner data are not hidden mathematical
premises. A prescribed finite postorder pass terminates after at most
the original number of internal-node attempts; this is only the finite
metadata algorithm's termination, not a native certifier complexity law
or proof that any merge succeeds or is optimal.

For unit-square rectangles, nonempty clipping is equivalent to
a_l+b_l<=1. Tangencies at equality remain. For raw vertex(a,b),
first fold to(1-a,1-b) if a+b>1. Within T, its only possible distinct
T orbit representative is(1-a,1-b) on the hypotenuse a+b=1,
which is(b,a). Hence lexicographic canonicalization is simply that
first fold plus lexicographic min with its coordinate reversal ON
THE HYPOTENUSE ONLY. To check the claim, write a second representative
as(eps_a*a+p,eps_b*b+q),p+q even. Coordinates in[0,1] force p,q
into{-1,0,1,2}. Nontrivial admissible odd translations must occur in
both coordinates; after identifying equivalent endpoint representations,
their only distinct feasible form is the two reflections p=q=1 with
a+b=1. This includes the endpoint interchange. Even
translations2 only give the same endpoint. There is no coordinate
swap symmetry in the interior or interchange of n and m. This routine
closed-domain key simplification is an implementation of the accepted
even-lattice orbit, not a new phase identity.

PD-N183 remains intact: its arbitrary algebraic/equispaced discrete
derivative transfer is not used. PD-N079 remains intact: ordinary
signed-component interpolation is used for S, never squared-phase
smoothness. A coarsened-parent corruption without new verification
still fails the older certificate contract. The present theorem makes
those missing verification obligations explicit, not automatic.

2026-11-06, Codex gpt-6.1-sol xhigh25min; rules/input
`0768cb93c4f829faf5f38d47cdd7e33faad8bf64`. Fresh comparison gate and
prospective finite test are in the D19 idea/attempt. No numerical,
native or phase job is part of this analytic proof. Distinct review,
any finite application and source adoption remain separate.
