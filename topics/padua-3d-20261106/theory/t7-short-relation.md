# PD-T?padua-3d-20261106-codex-T7-02 — compatible short relations for every finite subgroup

ID kind: PD-T. Aliases: general-H T3 relation obstruction.
Split from: none. Split into: none. Supports the T7 target, still OPEN.

## Statement and definitions

Let H≤(R/Z)^3 be finite, a∈(R/Z)^3, and L=H^⊥. For nonzero
u∈L put b_j=|u_j|, and define

    q(u)=b_j                           if support(u)={j};
    q(u)=max(b_j,b_k)                  if support(u)={j,k};
    q(u)=max(2b_1,2b_2,2b_3,b_1+b_2+b_3) otherwise.

If 2u·a∈Z, then a nonzero real polynomial of total degree q(u)
vanishes on c(a+H). Thus q(u)≤n forbids Π_n-injectivity. The phase
condition is essential to this particular polynomial construction.

## Status by part / scope of obstruction

Overall status: PROVED, written elementary proof. Candidate disposition:
the general-H extension is equivalent to the T3 relation mechanism,
without a novelty claim. The negative statement covers exactly a finite
single coset with one compatible nonzero relation of the displayed
q-degree. It excludes neither all cosets nor all rank-two subgroups.

## Depends on / sources

[T3 short relations](t3-short-relations.md) uses the same polynomials.
The proof below uses only u∈H^⊥ and its compatible phase; no cyclic
hypothesis or source theorem is imported. See [literature-T7](../literature-T7.md).

## Proof

Write u·(a+h)=δ/2 modulo Z and s=(−1)^δ. At a node set
U_j=T_{b_j}(x_j)=cos(2πb_j(a_j+h_j)). Signs of individual angles
may be reversed without changing U_j. For support one the polynomial
U_j−s vanishes. For support two the relation gives U_j−sU_k=0.
These are nonzero polynomials of the asserted degrees in distinct
variables.

For support three let A_j=2πu_j(a_j+h_j). Then
A_1+A_2+A_3=δπ modulo 2π, and U_j=cos A_j. The elementary cosine
addition identity, squared after isolating the sine product, gives

    U_1²+U_2²+U_3²−2sU_1U_2U_3−1=0.

As a polynomial in x this is nonzero. Its pure highest monomials in
each separate variable cannot cancel with each other or with the
mixed product, whose exponents in all three variables are positive.
Its degree is exactly q(u). This proves the obstruction.

## D3: specialization admits 2-D Padua

In two dimensions retain the support-one and support-two definitions.
The Padua cyclic group has modulus M=2n(n+1) and generator (n+1,n).
Its annihilator consists exactly of

    u=nr, v=(n+1)t, r+t even.

Indeed the character congruence (n+1)u+nv≡0 mod M first implies
these divisibilities and then the parity condition. Pure nonzero
relations have degree at least 2n or 2(n+1). A relation using both
coordinates has max(|u|,|v|)≥n+1. Consequently there is no relation
with q≤n, even at the unshifted phase where all relations are
compatible. The obstruction provably spares Padua for every n≥1.
The new tool also reproduces its cardinality and exact rank for n≤10.

## Checks, scope and open items

This is a hand proof, not a negative inference from a modular rank.
The full finite general-coset class at n=2,3 is **not enumerated**;
therefore no finite-class exclusion or computer-assisted proof is
claimed under D3. Failure to find a short relation never proves
injectivity. The original all-coset existence problem stays OPEN.

2026-11-06, Codex, assigned gpt-6.1-sol xhigh, rules e5b6445.
Provisional ID. The equivalent proof extension is registered as PD-T,
not as a negative result for a newly failed candidate mechanism.
