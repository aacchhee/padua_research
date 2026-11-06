# PD-T?padua-3d-20261106-codex-T8-02 — finite cyclic census and survivors

ID kind: PD-T. Aliases: complete unshifted quadratic/cubic census;
even-order cubic survivor; omit-n3 diagnosis. Split from: none.
Split into: none. The original all-degree quality target remains OPEN.

## Statement

The exact finite executions below report all zero-phase primitive cyclic
cosine images with N=binom(n+3,3) nodes at n=2,3, after the complete order
reduction M<=8N in T8-01. Equivalence is unit reparameterization, generator
coordinate signs and physical axis permutations, followed by exact node-set
deduplication using reduced rational angles. Each minimal-count class has
an integer dictionary full-rank certificate mod1000003 or an exactly verified
rational nullvector. These finite computations were independently reproduced in audit-02/T8;
no unbounded-degree conclusion is claimed.

## Definitions and assumptions

Use T8-01's primitive subgroup order and exact fold, T3-01's dictionary,
and the preregistered U/O scopes. U includes all primitive coordinates,
including zero/repeated/non-unit ones and every admissible M. O is only
the normalized first-unit-coordinate odd slice at the specified higher
degrees; it is not a full all-modulus census there.

## Status by part

Overall status: **MEASURED**, exact finite executions. The analytic finite
reduction is separately PROVED in T8-01. Independent reruns completed
(../audit-02/T8.md); status remains conservatively MEASURED because raw
catalogues are regenerate-only and no classification status upgrade is
asserted here. No D2 promising family.

| Screen | Generator classes | Distinct N-node sets | Full rank |
|---|---:|---:|---:|
| U, n=2, M<=80 | 15,733 | 95 | 2 |
| U, n=3, M<=160 | 112,314 | 300 | 1 |
| O, n=5, M=111, 1<=b<c<=55 | 766 from 1,485 pairs | 766 | 1 |
| O, n=6, M=167, 1<=b<c<=83 | 1,189 from 3,403 pairs | 1,189 | 5 |

Full-rank representatives (axes may be permuted):

- U n=2: M=19, z=(1,3,7),(1,7,8); exactly the two old T2 node sets.
- U n=3: M=38, z=(1,6,17); a new finite survivor outside H39's modulus.
- O n=5: M=111, z=(1,15,50).
- O n=6: M=167, z=(1,13,31),(1,15,36),(1,15,64),(1,17,22),(1,17,70).

The U invariant minimal-count classes number 10 and 12 respectively;
zero have full rank, agreeing with T1 on the complete cyclic part of U.
No new n=2 full-rank even-modulus or no-unit-coordinate set occurs.

Candidate disposition: U/O bounded diagnoses completed, with finite
survivors retained. No rank-only survivor is called promising. The n=3
M38 success disproves the extension of H39 to all cyclic subgroup orders
at cubic degree, while leaving H39 itself unchanged.

## Depends on

T8-01 finite reduction; T3-01 exact integer dictionary and modular lift.
No literature theorem or generic-axis specialization premise.

## Checks and evidence

Commands executed from repository root, with OPENBLAS_NUM_THREADS=1 and
OMP_NUM_THREADS=1:

`python topics/padua-3d-20261106/code/t8_cyclic.py controls`

`python topics/padua-3d-20261106/code/t8_cyclic.py census --n 2`

`python topics/padua-3d-20261106/code/t8_cyclic.py census --n 3`

`python topics/padua-3d-20261106/code/t8_cyclic.py odd --n 5`

`python topics/padua-3d-20261106/code/t8_cyclic.py odd --n 6`

Receipts: evidence/t8-controls.json, t8-unshifted-n2.json,
t8-unshifted-n3.json, t8-odd-n5.json, t8-odd-n6.json. Each records source
and preregistration hashes, versions, scope and raw-data path/hash/bytes.
The raw JSONL contains every quotient generator and every exact nullvector;
it stays regenerate-only in /tmp/padua-3d-20261106. U wrong-count rows
are retained too. Compact receipts are under16KiB.

D0 reproduced all 171 H39 witnesses, original T2 ranks four/zero/four,
and exact cyclic Padua node sets and full rank at n=1..10. Whole-subgroup
reflection membership is tested directly on torus residues. D0's bounded
invariant control is supplemented by full U invariant coverage.

## Proof/evidence and finite-field risk

The producer enumerates every sorted individually folded primitive triple,
marks its entire unit orbit, constructs the complete physical node set and
compares full exact reduced-fraction tuples under every axis permutation.
It never deduplicates merely by rounded coordinates or a hash. The absence
of extra node-set equivalences between retained U generator classes was an
output, not an assumption. Rank is unchanged by these symmetry operations.

A nonzero integer minor mod1000003 is nonzero over Q. A deficient image
alone could be a bad-prime artifact; the code therefore computes exact
fraction-free rational RREF, obtains a nonzero kernel vector and checks
integer Dv=0 in every deficient case. Exact RREF rank, rather than the
deficient modular rank, is recorded. The raw data are regenerable from
committed code; a separate rerun must check the finite coverage and results.

## Sources, scope and open items

Literature limits are in literature-T8.md. U covers zero phase only; P is
a separate set of fixed translated rules. Arbitrary continuous phases,
all higher degrees, unions and corrected grids remain outside U/O.
An explicit degree-uniform continuation and all of D2 are needed before
any family-quality conclusion. Finite ranks provide no Lebesgue estimate.

## History

2026-11-06, Codex T8, assigned gpt-6.1-sol high, rules e5b64450.
Preregistered after Part A M2 and full original plus main-delta gate read.
All listed commands actually executed. No Git/shared files changed.


## Dated audit-02 history correction — 2026-11-06

The preceding model/provenance header was edited in place after its first
publication. This note preserves that fact; it does not establish an earlier
execution order. See [canonical disclosure](../response-deviations-02.md).
The independent T8 executions completed in ../audit-02/T8.md; classification
status remains MEASURED with regenerate-only raw catalogues. The former
"scope exhaustion" stop is withdrawn under handoff06; special strata,
coset unions and admissible-degree phased orbits resume under new counters.
