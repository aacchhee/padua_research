# PD-T?padua-3d-20261106-codex-T8-r06-04 — exact rational phase certificate reduction

ID kind: PD-T. Aliases: root-of-unity specialization; direct-node finite
field determinant. Split from: none. Split into: none.

## Statement, definitions and assumptions

For a finite union of rational phased cyclic cosine images with common
order M and phase denominator D, put L=lcm(M,D). Represent torus angles
by integers modulo L and cosine nodes by coordinatewise folded residues
min(v,L-v). Equal folded residue triples are exactly equal real nodes.
Let V be the product-Chebyshev evaluation matrix on the distinct nodes
for Pi_n. If p is an odd prime with L|(p-1), omega has exact order L
in F_p, and V_p is formed by replacing cos(2pi v/L) with
(omega^v+omega^-v)/2 modulo p, then rank(V_p)<=rank(V).
Consequently N distinct nodes and det(V_p)!=0 prove Pi_n-unisolvence.
No converse follows from one or several deficient modular ranks.

## Status and proof

Overall status **PROVED**, elementary exact reduction. The computed
certificates and classifications are separate MEASURED records until
independently rerun, as required by the workflow. This is a known-method
implementation variant, not a new interpolation mechanism or priority claim.

Cosine is injective on [0,pi], so folding angles into [0,1/2] decides node
equality exactly. Every entry of V belongs to Z[zeta_L,1/2]. Since p does
not divide L and omega has exact order L, Phi_L(omega)=0 in F_p; the
cyclotomic quotient therefore defines a ring homomorphism
Z[zeta_L,1/2]->F_p sending zeta_L to omega. Determinants commute with
this homomorphism. Any nonzero minor modulo p was nonzero before reduction;
this proves the rank lower bound and the square full-rank criterion.

## Implementation checks and evidence

code/t8_r06_routes.py verifies prime status with SymPy isprime, finds omega
using primitive_root, and verifies omega^L=1 and omega^(L/q)!=1 for every
prime q|L. It evaluates actual distinct nodes using the Chebyshev recurrence,
then exact Gaussian elimination modulo p. Every positive selected member
has two nonzero determinants at different primes. NumPy int64 arithmetic
has a p<2e9 guard: individual recurrence products are <2p^2<8e18 and
elimination products <p^2, within the signed 64-bit range. Reduction occurs
after each product stage in three-coordinate basis multiplication.
Python arbitrary integers handle the modular inverse and determinant
accumulator. SymPy primality/root finding and NumPy exact integer arithmetic
are trusted dependencies. The receipts pin versions, code and helper hashes.

The D0 tests reproduce old n2 phase ranks8/9/8 (with analytic matching
ceilings), the audit n3 M20 fullrank example, and 2D Padua count/trace
through12. These validate the new implementation; they do not constitute
an independent rerun. code/t8_r06_near_orders.py imports the same arithmetic,
so it is not an independent checker. New independent checks are arranged
by root and must be linked when actually executed.

## Sources, scope, open items and history

No external theorem imported; the basic ring/character method has existing
T3/T7/T8 predecessors, with source comparison in literature-T8-round06.md.
This proves only finite nodes' rank. It gives no all-degree construction,
quality bound, exact negative from modular deficiency, or exhaustive
continuous-phase classification. 2026-11-06, Codex gpt-6.1-sol xhigh
assigned; rules/input 7afa6a54a4db4652267e38cd48658ba435d20481.
