# PD-N?padua-3d-20261106-codex-T8-r06-07 — continuous nearby-order count strata

ID kind: PD-N. Aliases: Phi3b; gcd-stratum phase optimization. Split from:
initial Phi3 half-grid selector; split into: none. Rules/input 7afa6a54.
Assigned Codex gpt-6.1-sol xhigh; runtime model metadata not separately exposed.

## Statement, scope and status

The separately preregistered Phi3b rules all have actual outcomes. The
s1 rule reaches a complete exact-count obstruction at n6; s2 and s3 at
n3; s4 at n4. Here M=binom(n+3,3)+s, z=(1,b,c), 1<=b<c<M, and phases
range over the continuous first-unit collision strata, not just a phase
grid. These finite rule dispositions are **MEASURED** pending independent
reconstruction. The arithmetic implications below are **PROVED** directly
from PD-T?padua-3d-20261106-codex-T8-r06-02. They do not exclude nonunit
first coordinates, repeated/zero coordinates, or other degree sequences.

A selected cubic M21 example has an exact positive certificate and sampled
Lebesgue value31.23177280536. The full-rank certificate is **MEASURED**
pending independent rerun; all floating quality remains **MEASURED**.
There is no competitive-family, asymptotic, or novel-priority claim.

## Prospective gate and actual run

The Phi3b append in preregistration-T8-round06.md and the root gate were
published in commit7f773ebe6ca04dbfdcb743b22e92da6469741748 before this run.
The initial route boundary was frozen separately. No optimized Phi3b
quality had been inspected at registration. The initiating observation
was the disclosed S mixed-stratum cubic M21 positive, followed by the
analytic fold formula. Underlying E/T4/H39 remain closed.

Command, repository root, exit0:
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t8_r06_near_orders.py`

Code sampled16 seeded nonzero free rational phases/257 for each of the
first128 count-permitted strata, then optimized the top3 determinants
with at most250 Nelder-Mead evaluations. Compatible phases stayed exact.
Every sampled direct count agreed with the theorem. No180s degree budget
bound; reported search times sum15.678s, excluding quality evaluation and
receipt overhead. A SciPy invalid-subtraction warning arose when an
optimizer simplex had infinite objective values; no uncertified result
was promoted. Selection preceded quality and used determinant only.

|s|n|M|all count strata|count-permitted|sampled phases|actual outcome|
|--:|--:|--:|--:|--:|--:|---|
|1|3|21|1140|258|2048|selected exact positive; first128 strata|
|1|4|36|3570|534|2048|no certified finalist; rank OPEN|
|1|5|57|9240|2286|2048|no certified finalist; rank OPEN|
|1|6|85|20916|0|0|exact count obstruction|
|2|3|22|1260|0|0|exact count obstruction|
|3|3|23|1386|0|0|exact count obstruction|
|4|3|24|1518|45|720|all45 count strata sampled; rank OPEN|
|4|4|39|4218|0|0|exact count obstruction|

Counts cover all b<c, h=0,1 and nonempty J subset{2,3}. For these N>=20
and s<=4, a nonspecial first phase gives M>N nodes. With all coordinates
compatible, count is at most M/2+1<N, so the omitted empty J cannot yield
N nodes. Thus each zero row is complete for the stated continuous phase
class. Sampling rank at permitted strata is not a symbolic-rank census.

## Direct arithmetic proof of the four zero rows

Write d=gcd(M,z_j:j in J), q=M/d. The fold theorem gives K=d*gcd(2,q)
if gcd(2,q) divides h, and K=0 otherwise. It gives f=gcd(2,M) if that
integer divides h, and f=0 otherwise. Exact count N=M-s requires K-f=2s.

For odd M, K=d and f=1, hence d=2s+1. At (M,s)=(85,1),(23,3),(39,4),
the required divisors3,7,9 do not divide M. At (M,s)=(22,2), h0 requires
d3 when q is even or d6 when q is odd; h1 gives K0 for even q or requires
d4 for odd q. None is possible since d divides22. These are arithmetic
nonexistence proofs under the count theorem's assumptions, independent
of modular ranks or floating optimization.

## Positive example and measured quality

n3,N20,M21,z=(1,4,6), phase=(257,1028,10080)/10794, h1 and J={3}.
Actual folded count20; nonzero actual-node Chebyshev determinant20737
mod21589, and1259 mod43177. Both splitting primes and root orders were
verified by the frozen arithmetic implementation. The specialization
argument is PD-T?padua-3d-20261106-codex-T8-r06-04.

On the fixed21^3 Lobatto mesh: sampled Lebesgue31.231772805360976,
condition2=16.001126941219656, cardinality residual4.50e-15. Leja13.17472
and QR8.32067 at the same degree are smaller. No n>=4 positive Phi3b
quality value was obtained; the fit is INCONCLUSIVE. The D2 promising
criterion is not met. An optimizer failing to certify a finalist at n4,
n5 or cubic M24 does not prove singularity of those strata.

## Sources, checks and reproducibility

Canonical receipt evidence/t8-r06-near-orders.json is3899bytes, with
commands, rules SHA, versions, core/helper/own source hashes, selected
phases and two-prime certificates. Unique scratch JSONL is regenerable;
the receipt pins its hash and size, not a shared temporary filename.
Code: code/t8_r06_near_orders.py importing frozen t8_r06_routes.py.
No external literature theorem is a proof dependency. Relevant source
coverage and known-mechanism comparison remain in literature-T8-round06.md.
The checker is an implementation, not an independent proof audit.

Candidate disposition: each frozen s1..4 rule REJECTED: failed at its first
complete count-obstruction degree. The intermediate rank questions,
broader continuous cyclic families, and arbitrary subgroup unions remain
OPEN. No global ID is allocated by this worker.
