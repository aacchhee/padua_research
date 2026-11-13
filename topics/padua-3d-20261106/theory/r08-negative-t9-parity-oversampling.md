# PD-N?padua-3d-20261106-codex-T9-r06-03 — the full parity-anisotropic family is always oversized

ID kind: PD-N.
Aliases: T9-R06-FINITE; family-only finite-complement obstruction.
Split from: PD-T?padua-3d-20261106-codex-T9-r06-06,
[t9-r06-finite-complement.md](t9-r06-finite-complement.md), the explicitly
named negative all-degree cardinality consequence.
Split into: none. Existing provisional ID retained; no final allocation.

## Statement

For every integer n>=1, the complete parity-anisotropic cosine support
with orders(n,n+1,n+1) has F(n)>N=binom(n+3,3) points. Consequently the
**full support itself** cannot be a minimal N-node interpolation set, even
though its Pi_n evaluation matrix has full column rank. This applies in
particular throughout n1..109, but is a family-only theorem, not a
classification of that finite complement.

## Definitions

The torus subgroup is the union of the rectangular grid with axis orders
n,n+1,n+1 and its simultaneous half-grid-step translate. X is its full
coordinatewise cosine image. Set A(m)=floor(m/2)+1 and B(m)=ceil(m/2).
Then F(n)=A(n)A(n+1)^2+B(n)B(n+1)^2.

## Assumptions

Precisely this complete unshifted parity-anisotropic subgroup support;
n>=1. Selecting an N-node subset changes the construction and is outside
the negative statement. No all-lattice optimality is assumed.

## Status by part

Overall status: **PROVED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact count formula and F(n)>N for every n>=1 | PROVED | Elementary cosine counts and algebra below |
| Exclusion of other lattices or selected N-node subsets | OPEN, outside statement | Family count gives no such theorem |

Candidate / claim disposition: **REJECTED: failed** as a full-support
minimal-cardinality mechanism. Rejection reason: failed — the exact count
exceeds N in every degree. The cubature/projection family remains useful.

## Negative-result scope

Attempted mechanism: use this entire known cubature support as an exactly
minimal interpolation set. Parameter range: every integer n>=1, including
the density theorem's finite complement. The family count does not reject
extraction or different subgroups.

## Depends on

Elementary one-dimensional cosine pairing. The separate full-rank assertion
uses PD-T?padua-3d-20261106-codex-T10-04,
[t10-parity-log4.md](t10-parity-log4.md)'s Gram I+ee^T; the cardinality
obstruction itself does not need that rank result or any external theorem.

## Checks

The old producer [t9_r06_complement.py](../code/t9_r06_complement.py) and
[t9-r06-complement.json](../evidence/t9-r06-complement.json) supply formula
controls through109 and timed probes17/24/32. Audit03/T9 independently
verified the formulas. This response worker read those records and the
proof; it did not claim a new run. Exact finite table evaluation is a
verification of the formula, not unrestricted enumeration.

## Sources

Known Chebyshev-lattice/parity cubature family; canonical Cools–Poppe/DMVX
source reuse and reading limits are in the
[gate supplement](../novelty-gate-supplement-round08.md). No external source
proof is load-bearing for the count inequality.

## Proof or evidence

An unshifted length-m cosine grid has A(m) values, and a half-step length-m
grid has B(m). Their cosine images are disjoint: equality would equate an
integer and half-integer index up to sign modulo the same integer order.
Products therefore give F(n) as defined. Direct simplification yields

    n even: F(n)=(n+1)(n+2)^2/4,
            F(n)-N=n(n+1)(n+2)/12>0;
    n odd:  F(n)=(n+1)(n^2+4n+5)/4,
            F(n)-N=(n+1)(n^2+2n+3)/12>0.

Thus every n>=1 is oversized. F(n)/N tends3/2; no density bound is needed.

## Scope and D3

D3: this particular three-dimensional full-support count is not a theorem
about all parity/Lissajous constructions. Standard two-dimensional Padua
uses different axis orders/selection and has exactly(n+1)(n+2)/2 nodes;
none of the stated three-axis product-count hypotheses applies to it.

## Open items

Selecting N points and controlling the inverse restriction operator remain
separate questions. Unrestricted finite-complement probes are assigned to
handoff08 E3 and have their own receipts; this family obstruction cannot
be used as their stop justification.

## History

2026-11-06 — Codex records worker, assigned gpt-6.1-sol xhigh, runtime
metadata not independently exposed; rules/input
9042e1c42964150f30fdbe8563c12ba6c6a8692a. Gives the already mapped PD-N
T9-r06-03 its own home. This ID denotes **parity-family oversampling**,
not the fixed-dual tetrahedron formula (PD-T T9-r06-04).
