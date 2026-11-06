# T8 preregistration — 2026-11-06

Written after Part A M2 dispositions and the complete original registry plus
main-delta read, before T8 runs. Rules `e5b64450fce42262dafc88ee357b72e5f203916b`;
reconciled head `120a19ee71baa8e7834b3b183798df2cf489c432`.
This prospective document supplements the coordinator's gates.md.

## D0 before every new mechanism screen

New t8_cyclic.py must reproduce original T2 rank distributions at n=2,3,4,
including four/zero/four full-rank generators, and the existing H39 integer
null cover for all 171 normalized pairs. It must realize 2D Padua as cyclic
M=2n(n+1), z=(n+1,n), at every n=1..10, with exact count, exact node-set
equality to the parity grid and full dictionary rank. On its cyclic inputs,
the coordinate-reflection-invariant n=2,3 exact-cardinality part must have
zero full-rank survivors, reproducing T1. Any discrepancy stops new runs.
The invariant control is checked across the full cyclic finite class during
the census, in addition to small pre-screen controls; it is not a claim to
rerun T1's noncyclic class with the cyclic tool.

## Screen U — full zero-phase finite class

Degrees 2,3; M=1..8*binom(n+3,3), all primitive generators including zeros,
repeated coordinates and generators with no unit coordinate. Exact signed
folded residues identify nodes. Quotient by units and coordinate signs and
permutations, then deduplicate exact node sets up to axis permutations using
reduced rational angles. Class reductions and the M cap must be proved before
execution. Track rejected counts, every exact-cardinality class, rank and
invariance; full raw census in /tmp, hashes/counts in compact receipts.

Use prime 1000003 on integer dictionaries; full modular rank certifies full
real rank. Every deficiency must be confirmed by exact rational RREF and a
nonzero rational kernel checked by exact multiplication. No modular-zero
negative proof. Status stays MEASURED until independent rerun; no all-n claim.
Census is finite coverage, not a degree-uniform positive construction.
No quality-selected continuation or quality optimization is permitted.

## Screen O — n=5,6 odd normalized slice

For n=5,6 use M=2N-1, all 1<=b<c<=N-1. Deduplicate unit/permutation orbits
and exact node sets. Same exact dictionary/rank/null protocol as U. This is
a finite diagnostic, never an automatically chosen family or subsequence.
Record all full-rank survivors. No quality run unless a separate prospective
uniform rule provides a structural continuation.

## Screen P — three fixed phase rules

At every integer n>=2 set N=binom(n+3,3), M=N and
phi=(pi/2,pi/3,pi/4), with generators reduced modulo M:

- PK: z=(1,n+1,(n+1)^2).
- PT: z=(1,n+1,(n+1)(n+2)/2).
- PO: z=(1,2n+1,2n^2+2n+1).

These are new translated rules, not reopening the killed zero-phase rules.
Rational phases allow exact folded-angle node counts in order lcm(24,M).
Use the full M-row character dictionary with coefficients in Q(zeta_24).
Full rank at an exact splitting prime lifts by T3-01. A deficient modular
matrix requires an exact Q(zeta_24) kernel verification before a rank kill.
The field polynomial is Phi_24(t)=t^8-t^4+1; no floating rank is used.

Ascending n=2..12; count mismatch kills that minimal family immediately;
first certified deficiency kills that fixed rule under D2. Surviving
full-rank rules get the inherited 21^3 Lobatto mesh maxima and same-degree
Leja/QR controls with fixed basis/order. Two consecutive Leja losses at
n>=6 kill that rule. Floating mesh values are lower bounds on the true sup,
and remain MEASURED. No ties between rules are used to splice a family.
Any exact node-set tie is consolidated with the lexicographically earliest
(M,z,phase) representative; no floating roundoff tie-breaking.

D2 promising requires exact unisolvence at every admissible n<=12 (or stated
largest feasible degree), sampled Lambda below QR at every tested n>=4,
and a preregistered fit favoring C log^k n, k<=4, over C n^alpha, alpha>=1,
on n<=20. Fits, if reached, compare least-squares residuals in log Lambda
for fixed k=1,2,3,4 against the constrained log-linear power fit alpha>=1,
same n>=4 rows; fewer than six rows is INCONCLUSIVE. A family failing any
conjunct is never promising. No fit will be used after a rank/count kill.

## Stop and retention

Each screen is a bounded step; round ceiling 25 is not a target. Complete U/O,
apply P kills literally, and record all deferred phase strata, unions,
corrections and mod-6 with structural prerequisites. Stop on the resulting
gate kills/proved finite obstructions and recorded exhaustion of separated
uniform rules. The broader cyclic/union/polylog target remains OPEN.
Large raw data are regenerate-only under /tmp; code and each small receipt
must remain below 16 KiB. No inherited/shared file is changed by the worker.
