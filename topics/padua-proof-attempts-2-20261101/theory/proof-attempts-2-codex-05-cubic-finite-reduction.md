# PD-T?proof-attempts-2-codex-05 — Finite signed-cubic reduction for strict maxima on a square

ID kind: PD-T.
Aliases: A5 finite reduction; every-active-polynomial principle; physical-coordinate crease exclusion; cubic stationary-resultant reduction.
Split from: obligation(1) and exact crease / crossing coverage in programme A5, `PD-T?programme-ideas-claude-06`.
Split into: none; the separate degree-three count is result06. The original n=3,…,8 target remains unchanged.

## Statement

Let L_0,…,L_{N−1} be real polynomials in two physical coordinates of total degree at most3, and λ=Σ|L_i| on S=[−1,1]². Put P_s=Σs_iL_i for s∈{−1,1}^N. Every strict relative local maximum of λ is covered by the following finite reduction.

1. In the interior, it is a stationary point with negative definite Hessian of every P_s active there. If A=(P_s)_x or B=(P_s)_y is identically zero, that pattern cannot account for an interior strict maximum. Otherwise remove any common factor G with coprime quotients a=A/G,b=B/G. Points on G=0 cannot account for a strict maximum. All remaining candidates lie in the Cartesian product of the real roots of the two nonzero projection resultants Res_y(a,b) and Res_x(a,b). Thus a finite exact partition of those roots and a valid disposition for every Cartesian pair covers every interior possibility.
2. An interior point on a zero-cardinal curve where one vanishing L_i has nonzero physical gradient is not a relative local maximum, whether that zero is a lone crease or part of an arbitrary crossing. At an open edge, the corresponding exclusion holds if one vanishing restricted L_i has nonzero tangential derivative.
3. At an open edge, every active restricted polynomial q_s has a strict one-dimensional maximum, hence q_s'=0 and q_s''<0. A constant q_s cannot account for such a maximum. Enumeration of all sign patterns of the non-identically zero restricted cardinals, with all roots of q_s', covers every edge strict maximum. Identicallyzero restricted cardinals may have their signs fixed arbitrarily for this tangent enumeration.
4. The four corners complete the types. Exact node-corner exclusion and exact all-active inward-derivative tests, stated below, are sufficient corner dispositions. The finite reduction does not assume these sufficient tests always decide an arbitrary cubic family.

For degree-three Padua cardinals, exact arithmetic in Q(sqrt2) suffices. Norming either resultant to Q and isolating all real roots of the squarefree norm gives a possibly larger but still complete candidate set. No near-coincidence convention, seed equality or old corner/edge-node neighbourhood discard is used.

## Definitions

A pattern s is active at z if s_iL_i(z)=|L_i(z)| for every i. The polynomial identity λ=max_sP_s holds pointwise. Interior, open edge and corner refer to the physical closed square. All gradients and Hessians here are physical, not angle, derivatives. A strict relative local maximum means λ(w)<λ(z) at every distinct sufficiently near w∈S.

## Assumptions

Degree≤3 is essential to the negative definite Hessian statement. Coefficient arithmetic and root partitions must be exact or outward-rounded. A resultant certificate verifies nonzeroness; no generic-position assumption on projections is needed because all coordinatepairs are covered. No degree-four extension is asserted.

## Status by part

Overall status: **PROVED** (written analytic/algebraic reduction).

| Mathematical part | Status | Evidence |
|---|---|---|
| every-active-polynomial principle and exact regular-crease / crossing exclusion | PROVED | elementary comparison and opposite-direction derivatives |
| cubic negative definite Hessian necessity; common-factor exclusion | PROVED | null-line and Jacobian identities below |
| complete finite projection-root reduction and physical-boundary types | PROVED | elimination identities and univariate cubic calculus |

This is a supporting finite-reduction theorem; it does not certify any count by itself. Required Claude audit of Part 2 remains pending.

## Depends on

Elementary polynomial/resultant algebra, one-variable Sturm theorem for any subsequent exact partitions, and elementary local calculus. The mathematical reduction does not depend on a numerical source execution. The eventual degree-three local count also cites `PD-T?proof-attempts-codex-03 (audit pending)` for its two alreadyproved edge representatives, while the present reduction does not redo that theorem.

## Checks

Separate new producer/checker schema: `../code/a5_schema.md`. New producer: `../code/a5_producer.py` and `a5_boundary.py`. Their computations and actual independent checks belong to the separate count record; no computational observation is needed for this theorem.

## Sources

Authoritative programme A5 and THEORY-06 at `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`; part1 auditF2 at `95279b833bca5967fcf47c1b71a56ff622185b4e`. Closest programme IDEA17 and charter IDEA048; complete relaxed registry gate recorded in `../attempts/T-A5.md`. Proof completion of a registered target; no priority/novelty claim. No count from arXiv 2605.23299 is borrowed in the proof.

## Proof or evidence

### Active polynomials and exact creases

For every s, P_s≤λ. If s is active at z and λ has a strict relative maximum there, then P_s(w)≤λ(w)<λ(z)=P_s(z) at every distinct sufficiently near feasible w. Thus **every** active P_s has a strict relative maximum. The same implication holds without strictness.

At an interior maximum, ∇P_s(z)=0 for every active s. If L_i(z)=0, flipping just s_i gives another active pattern; subtracting gradients yields 2s_i∇L_i(z)=0. Hence every vanishing cardinal has zero gradient. This excludes any point containing one regular zero exactly, including crossings of any multiplicity. At an open edge, the same argument with both feasible tangential directions gives ∂_tL_i(z)=0 for every zero restricted cardinal. It makes no assertion that the normal derivatives of zero edge cardinals vanish.

The arrangement of the finitely many algebraic zero curves partitions S into finitely many semialgebraic sign strata. At any point each cardinal is positive, negative orzero, so the finite all-pattern formulation covers cell interiors, creases, crossings, singular zeros and boundary strata without having to choose numerical curve tolerances or construct a particular drawing of the arrangement.

### Why cubic strict interior maxima have negative definite Hessian

An interior maximum of a C² function has negative semidefinite Hessian. Suppose the Hessian H of a cubic P at z is singular, and choose nonzero v with Hv=0. Since ∇P(z)=0, exact cubic Taylor expansion along the line gives P(z+tv)−P(z)=ct³. If c≠0, one sign of t is ascending; if c=0, the entire line has the same value. Both alternatives contradict strictness. Thus H≺0.

Let A=P_x=Ga and B=P_y=Gb. At a point with G=0,

H = [[aG_x,aG_y],[bG_x,bG_y]],

so its rank is atmost1 and it cannot be negative definite. If either A or B is identically zero, H has a zero row/column and again cannot be negative definite. Otherwise every strict interior maximum lies off G=0 and solves a=b=0. Take G to be the full gcd, or verify any exact factorization for which the residual resultants are nonzero. Coprime bivariate polynomials over the coefficient field have nonzero resultant in each projection (possibly a nonzero constant); a common root must make each projected resultant zero, including cases where leading coefficients vanish. The latter assertion follows from the Sylvester determinant: the common evaluation gives a nontrivial common-root relation, so that determinant vanishes. No converse is assumed.

Each nonzero univariate resultant has finitely many real roots. Isolate all of them and take every Cartesian pair of root intervals. Every residual common root lies in one pair box. Extraneousprojectionpairs and conjugate-embedding roots of a field norm are harmless if each is excluded by an exact predicate or included in a rigorously certified root box. A squarefree norm has the same distinctreal roots as the norm before squarefree reduction and includes everyreal root in the chosenembedding. Total Sturm counts at ±infinity plus disjoint supplied one-root intervals certify completeness, including singleton rationalroots. This proves the finite interior reduction.

### Edges and corners

Restrict each P_s to an open edge, with tangent t and inward normal u≥0. The active-polynomial principle gives strict one-dimensional maximality of q_s(t)=P_s(0,t). A constant restriction is therefore impossible. At a critical point of a nonconstant cubic, q_s''=0 leaves either a nonzero odd cubic term or a constant polynomial, neither a strict maximum. Thus q_s''<0. Everyedge candidate is among finitely many roots of the nonconstant derivative polynomials, with only the irrelevant signs of identically zero restrictions fixed.

For the sufficient positive edge disposition used in the certificate, suppose no non-identically zero restricted cardinal vanishes at the candidate, and each identically zero restricted cardinal has factor(normal−side)Q with Q nonzero there. Its one-sided sign is exactly −side·sign(Q), fixed in a sufficiently small relative neighbourhood. Hence λ equals the corresponding single physical signed polynomialP there. If P has strictly negative inward derivative and q has a strict tangential maximum, then P(u,t)<P(0,t)≤P(0,t_*) for u>0 sufficiently nearby, and also P(0,t)<P(0,t_*) for t≠t_* sufficiently nearby. Thus the candidate is a strict relative maximum. Strictlypositive inward derivative instead excludes maximality. These tests do not discard untested zero-normal cases; such cases must be explicitly resolved if they occur.

At a node, λ=1 and λ≥|ΣL_i|=1 provided the cardinals reproduce constants; hence that node cannot be a strict maximum. For a non-node corner, finitely many activeP_s are considered exactly. If each has both inwardpartialderivatives strictly negative, continuity gives a common relative neighbourhood in which eachdecreases on every nonzero inwarddisplacement (integrate its gradient along the segment). Nonzero-cardinal signs remainfixedthere, so all possible local sign patterns are among thoseactive at the corner. Taking their finite maximum proves a strict relative maximum. The four corners together with open edges and interior exhaust S. ∎

## Scope

This theorem supplies a finite verification problem for cubics and exact crease / crossing exclusions. It neither assumes the frozen search's local decisions nor promotes its six measured counts. Allconsistentpatterns and all coordinate pairs must still receive independentlyverified dispositions. The proposed degree-three implementation bypasses old (D)/(E) neighbourhooddiscards by exhaustive interior/edge systems plus exact point corner/node tests; no claim about their old floating inequalities is needed.

## Open items

Complete and independentlycheck the degree-three certificate; then assess degreefour separately. Globalargmax conclusions require additional treatment of non-strict maxima and rigorous values; they are not consequences of a strict maxima list alone. Required Claude audit remainspending.

## History

2026-11-01, Codex `/root/a5_develop`, allocated gpt-6.1-sol xhigh. Rules read at `3db1eee3fd9507c103c496bdf3da8157331359c5`; independentroute agent `/root/a2_independent_route` separately supplied the active-polynomial, cubic null-line and commonfactor arguments. OriginalA5 n=3,…,8 statement retained unchanged; this split result is only its finite-reduction obligation in the cubic case.
