# PD-T?padua-3d-20261106-codex-U3-03 — finite triangular half-shift classes

ID kind: PD-T. Aliases: sparse DCT support census; exact path amplification.
Split from: none. Split into: sparse degree-seven boundary in
PD-N?padua-3d-20261106-codex-U3-01. No final ID allocated.

## Statement and definitions

For n in{3,5,7}, N=binom(n+3,3), consider every z=(1,b,c) with
1<=b<c<2Nand phase z/(4N). Let A=C/8be its exact N-by-N cosine
coefficient matrix from the existing half-shift DCT reduction. A support
edge is an exactly NONZERO combined entry of C; repeated signed aliases
are combined before its support graph is formed.

At n3exactly8of741matrices have a unique support perfect matching;
at n5exactly8of6105do. Their actual matrices are invertible, with
the following complete list and exact S=sum(abs(A^(-1))):

| n | z | S |
|---:|---|---:|
|3|(1,4,11),(1,4,29),(1,11,36),(1,29,36)|52|
|3|(1,6,15),(1,6,25),(1,15,34),(1,25,34)|78|
|5|(1,17,30),(1,17,82),(1,18,33),(1,18,79)|434|
|5|(1,30,95),(1,33,94),(1,79,94),(1,82,95)|434|

At n3there are733support graphs without any perfect matching and none
with a nonunique matching. At n5there are6085without any perfect matching
and12with nonunique matchings. The full n7outcome is separately stated
in the scoped negative record. Counts are parameter triples, not quotient
classes under reflection, permutation or parameter changes.

## Status by part

Overall status: **PROVED**, computer-assisted finite classification after
the separate complete checker executed its own leaf-stripping enumeration
and rational inverses. Its executed coverage is in
[usable-check3](../usable-check3.md); final Claude audit remains separate.
Measured mesh quality is outside this statement.

Candidate disposition: retained finite Sclass; its finite performance
failure is in [quality failures](u3-quality-failures.md).

## Depends on / exact finite reduction

The existing [cubic DCT reduction](t8-r08-cubic-classification.md) extends
directly to these N, as follows. Put theta_k=(2k+1)pi/(2N),0<=k<N,
and B[k,r]=cos(r theta_k),0<=r<N. Finite geometric cosine sums and the
product-to-sum identity give B^T B=diag(N,N/2,...,N/2), so B is invertible.
For each signed frequency m=(epsilon*alpha)·z, reduce it modulo4N,
replace by r=min(m,4N−m), delete r=N, and if r>Nreplace r by2N−r
and its coefficient by its negative. This is valid because
cos((2N−r)theta_k)=−cos(r theta_k)and cos(Ntheta_k)=0. Summing all
eight signs, including repetitions at zero exponents, gives the exact
integer matrix C and V=B C/8. This proves rank equivalence at every
listed nwithout importing an unproved generalization of the cubic theorem.
A determinant term
of C chooses a support perfect matching. No perfect matching implies
det C=0. One unique matching implies det C equals its signed product,
which is nonzero since support edges exclude zero entries.

Given any matching, direct each nonmatching edge between the two matched
pairs it meets. An alternating cycle gives a different perfect matching
by toggling that cycle. Conversely the symmetric difference of two
perfect matchings is a union of alternating cycles. Thus the matching
is unique iff this digraph is acyclic. A topological ordering then
makes C triangular. Exact rational inverse and Sfollow by substitution.
These arguments prove the reduction to the finite graph/integer checks;
no deficient finite-field rank is used.

## Checks

Published protocol3b5cb29f5d68306fa61d3079627247110911b552;
frozen source8c230e3a6bd857c8b3f8c63cd49a2c818d1449b60d9cb131c8662158ff8bc79b.
Actual command from repository root:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u3_constructions.py S --receipt topics/padua-3d-20261106/evidence/u3-s.json

[Receipt](../evidence/u3-s.json) records34.4094seconds, versions, command,
source and unique raw2,364,548-byte catalogue identity. The exact total
is741+6105+28441=35287parameter triples; none omitted.
The independent checker reconstructs signed coefficients without producer
imports and uses forced row/column degree-one stripping rather than the
producer's SciPy matching/topological algorithm. It separately derives
the exact inverse with Fraction arithmetic. Actual selected cosine nodes
also pass two fresh splitting-prime monomial checks. See the independent
record and its code/data receipts for precise source hashes and outputs.

## Scope, sources, open items and history

Known matching/aliasing mechanisms, no priority claim. Full gate and
closest-proof reading are in [usable3](../usable3.md). This is a complete
finite support-class result, not a classification of all full-rank cyclic
sets and not a stability theorem. In particular the12nonunique n5graphs
remain outside S; no singularity claim is inferred merely from their cycles.
2026-11-07, Codex assigned gpt-6.1-sol xhigh; rules/input3822720.
