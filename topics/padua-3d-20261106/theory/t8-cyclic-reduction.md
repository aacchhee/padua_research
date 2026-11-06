# PD-T?padua-3d-20261106-codex-T8-01 — finite unshifted cyclic reduction

ID kind: PD-T. Aliases: eight-fold order cap; exact cosine node census;
primitive cyclic-generator normal form. Split from: none. Split into: none.

## Statement

Fix d>=1 and target cardinality N. Every finite cyclic subgroup H of
(R/Z)^d has the form H={kz/M:0<=k<M}, with
gcd(M,z_1,...,z_d)=1, where M=|H|. If |cos(2pi H)|=N, then M<=2^d N.
For zero phase its exact node set is represented by tuples
(min(kz_j mod M,-kz_j mod M)/M)_j in [0,1/2]^d.
Enumerating M=1..2^d N and all primitive z modulo M is therefore complete.

Coordinate sign changes of z preserve this node set, coordinate permutations
give cube isometries, and multiplication z by a unit mod M reparameterizes
the same H. Consequently sorting the individually folded generator
coordinates and taking unit orbits loses no class. Repeated coordinates,
zero coordinates and no-unit-coordinate generators must be retained in
the count; those with an obvious linear annihilator may be rejected for
rank only by exhibiting that annihilator.

For d=2 the same reduction contains every Padua set of degree n>=1:
M=2n(n+1), z=(n+1,n), with exactly binom(n+2,2) folded nodes.

## Definitions and assumptions

Cosine is coordinatewise. M is the true subgroup order, not an arbitrary
parameter period. Node equality means exact real equality; cosine is
strictly decreasing on angle representatives [0,pi], so reduced rational
folded angles are canonical exact equality identifiers. No cubature,
positivity, genericity or unit-coordinate hypothesis is imposed.

## Status by part

Overall status: **PROVED**, elementary written proof. Finite census results
are separate in t8-finite-screens.md and are not premises of this reduction.
Candidate disposition: retained known-mechanism tool, no novelty claim.

## Depends on

Elementary cyclic group parametrization, cosine equality and CRT. T3-01
supplies the existing exact integer folded dictionary for arbitrary M.

## Proof

Choose a generator h of H and let M be its order. Mh=0, so write h=z/M
modulo Z^d. Its order is M/gcd(M,z_1,...,z_d), proving primitivity.
For each real x in [-1,1], a coordinate angle in R/Z with cosine x has
at most two preimages (one at an endpoint). Thus each node has at most
2^d preimages in H; summing fibres gives M<=2^d N. This remains true
for translated cyclic cosets, though their phases are not enumerated here.

For zero phase, cos(2pi r/M)=cos(2pi s/M) iff r=+/-s mod M.
Folding each residue and dividing by M therefore identifies nodes exactly,
including coincidences not explained by global k->-k. The listed group
operations preserve the set or permute physical axes as asserted. A finite
orbit-marking algorithm that visits all sorted folded triples and marks all
their unit transforms visits every class. Node-set equality across orders
or generator classes is decided by sorted lists of reduced fractions,
minimized over axis permutations. The node set itself, rather than a hash
alone, is compared before counting distinct classes.

For Padua, gcd(n,n+1)=1 implies z has order M. A cyclic parameter k gives
axis indices i=k mod 2n and j=k mod 2(n+1). Generalized CRT says this pair
occurs iff i=j mod2; it then occurs once modulo lcm(2n,2n+2)=M. Thus H
is exactly the common-parity subgroup. Folding preserves parity, yielding
the usual checkerboard in [0,n]x[0,n+1]. Its count is
e(n)e(n+1)+o(n)o(n+1)=(n+1)(n+2)/2, where e(q)=floor(q/2)+1 and
o(q)=ceil(q/2). T1's local d=2 proof establishes injectivity; the new
tool additionally checks exact dictionary rank for n<=10. The order bound
2n(n+1)<=4*binom(n+2,2) holds, so the reduction admits this control.

## Reflection-invariant control

Let S={(kz_j mod M)_j:0<=k<M}. Test each coordinate reflection by exact
membership of its image in S. This decides whole-subgroup invariance,
not invariance of the physical cosine image (which is automatic). Every
exact-cardinality invariant d=3, n>=2 case must be deficient by T1.
Testing all such cases within this census verifies T1 on the full cyclic
part of the finite universe, not on all noncyclic subgroups.

## Checks and sources

Producer `code/t8_cyclic.py`; commands/receipts in attempts/T8.md.
The all-order reduction is analytic. No external source theorem is used;
source-comparison limits are in literature-T8.md.

## Scope and open items

This is a finite reduction for zero-phase cyclic subgroups at fixed N.
It supplies no finite reduction over arbitrary continuous translations,
no interpolation or quality theorem for a surviving class and no bound
excluding all cyclic families at unbounded degree. Independent audit of
the written proof and actual independent rerun of any finite census remain
separate obligations.

## History

2026-11-06, Codex T8, assigned gpt-6.1-sol high, rules e5b64450.
Written after the full gate and Part A M2, before mechanism execution.


## Dated audit-02 history correction — 2026-11-06

The preceding model/provenance header was edited in place after its first
publication. This note preserves that fact; it does not establish an earlier
execution order. See [canonical disclosure](../response-deviations-02.md).
The independent T8 executions completed in ../audit-02/T8.md; classification
status remains MEASURED with regenerate-only raw catalogues. The former
"scope exhaustion" stop is withdrawn under handoff06; special strata,
coset unions and admissible-degree phased orbits resume under new counters.


Attribution correction (2026-11-06, n5): the |H|<=8N fold bound was
supplied in Claude's handoff04; this record proves its cyclic application.
