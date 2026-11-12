# PD-T?padua-3d-20261106-codex-T8-r08-02 — finite phased M=N existence through12

ID kind: PD-T. Aliases: finite Phi1 witnesses; nine exact cyclic coset
certificates; finite-existence PROVED split.
Split from: the nine-witness existence subsection of
PD-T?padua-3d-20261106-codex-T8-r06-05, originally contained in the mixed
MEASURED witness/quality record. Split into: none. The original record and
its measurements are preserved; no broad target or floating claim is upgraded.

## Statement

For each n in{1,3,4,5,7,8,9,11,12}, let N=binom(n+3,3). The following
explicit full cyclic cosine images

    X={cos(2pi(kz/N+a/D)):0<=k<N}

have exactly N distinct nodes and are unisolvent for the real total-degree
space Pi_n in3variables:

| n | N | z | a | D |
|---|---:|---|---|---:|
|1|4|(1,2,1)|(105,28,211)|257|
|3|20|(1,2,7)|(30,75,69)|120|
|4|35|(1,22,25)|(240,90,109)|257|
|5|56|(1,8,45)|(225,15,115)|257|
|7|120|(1,33,92)|(29,48,56)|257|
|8|165|(1,37,144)|(59,84,55)|257|
|9|220|(1,32,101)|(97,59,127)|257|
|11|364|(1,16,129)|(156,248,227)|257|
|12|455|(1,267,119)|(132,236,237)|257|

These are exactly the degrees permitted by the independently proved M=N
half-period necessity within1<=n<=12. Existence beyond12, a uniform
closed generator formula and every Lebesgue-growth claim remain OPEN.

## Definitions, assumptions and status

Cosine acts coordinatewise; phase coordinates are turns. Rank is over the
real numbers in exact arithmetic. Only the nine listed parameter tuples
are claimed. Overall status: **PROVED**, computer-assisted finite existence.
No cited external theorem is a dependency, so no literature-dependent label
convention is needed. This is explicitly a **material status change** from
the old mixed MEASURED subsection and requires focused Claude re-audit.
The independently read audit03 already accepted all9exact certificates;
this record makes the proof requirements and split scope explicit.

## Depends on and proof

Use PD-T?padua-3d-20261106-codex-T8-r06-04, the written cyclotomic
certificate reduction. For each listed tuple set L=lcm(N,D), represent each
angle by its integer residue modL and fold coordinatewise by min(v,L-v).
This is exactly real cosine equality. The producer and independent checker
both find N distinct folded triples. For an odd splitting prime p and an
exact-order-L root omega, replace each node coordinate by
(omega^v+omega^-v)/2. The map Z[zeta_L,1/2]->F_p sends every evaluation
entry to the corresponding finite-field entry. A nonzero determinant
therefore proves a nonzero characteristic-zero determinant.

The original producer uses product-Chebyshev columns; the independently
written checker uses total-degree monomials and fresh primes. These are
bases of the same Pi_n; their change-of-basis determinant is nonzero in
characteristic0 and odd characteristic. Independent node-count and
nonzero-determinant checks therefore complete each finite existence proof.
No random search success probability, numerical rank or rank deficiency
inference is used.

## Essential evidence and independent execution

Original executable/evidence, unchanged:
[t8_r06_routes.py](../code/t8_r06_routes.py),
[t8-r06-witnesses.json](../evidence/t8-r06-witnesses.json), fullhash
3482c9d054d35d5b40c03a3b7c8e8bff9fa6f421602c8556410413a4f0706f28.
It records the full finite parameters, primes, roots and nonzero determinants.
The distinct Claude audit03 reran all9 using its own primes and monomials;
see [audit03/T8](../audit-03/T8.md), Claims1/N1.

An additional independently written executed checker,
[t8_r08_check.py](../code/t8_r08_check.py), imports no project mathematics.
Its [old-witness receipt](../evidence/t8-r08-check-old.json) rechecks all9
at two distinct primes>1.7e9, each with exact-order roots, N distinct nodes
and full monomial rank. As short cross-check identities:

| n | L | p1, nonzero det1 | p2, nonzero det2 |
|---|---:|---|---|
|1|1028|1700017993,153699473|1701010013,756286609|
|3|120|1700001361,981782666|1701001321,1659336693|
|4|8995|1700001031,701307454|1701026461,414382554|
|5|14392|1700270881,1500055200|1701134401,1625895981|
|7|30840|1700270881,1450459291|1701072721,1026344891|
|8|42405|1700270881,1580634506|1701543031,739323148|
|9|56540|1700044721,1589704211|1701627841,1310724919|
|11|93548|1701825217,341524259|1702573601,95071491|
|12|116935|1700001031,1212888524|1701871991,1299848631|

## Computer-proof requirement assessment

| Requirement | Concrete satisfaction |
|---|---|
|Proved finite reduction|Written ring homomorphism/fold proof,r06-04; nine explicit tuples above|
|Exact arithmetic|Integer folding, prime/order checks, modular evaluation and elimination; full rank only from nonzero determinants|
|Committed checker and essential evidence|Both source programs, original input/certificate receipt and new independent receipt; no bulk search output is needed to check these nine witnesses|
|Actual independent rerun|Claude audit03 own-prime replay and separately executed round08 checker, not an inspection of producer output|
|Trusted dependencies and remaining scope|Listed below; floating quality/unbounded family excluded|

Trust Python integers, NumPy int64 exact operations within guarded bounds,
SymPy isprime/root construction in the producer and the checker's separately
implemented deterministic64-bit primality test/root-order tests. Producer
p<2e9 keeps2p^2<8e18; the monomial checker forms coordinate powers/products with arbitrary
Python integers before modular reduction. Its NumPy elimination guards
p<1.9e9, keeping every elimination product below signed64-bit capacity. The finite theorem needs no stored optimizer logs
or cold-storage artifact. Input/certificate identities and checker commands
are preserved in small committed receipts; independent summary is
[independent-checks-round08-t8.md](../independent-checks-round08-t8.md).

## Sources, scope, open items and history

No external source proof used. Source comparison is bounded by the existing
T8 gates/literature; no novelty or priority claim. All9old witness existence
requirements now have exact checkable evidence and independent replay, so
this narrowly split PROVED statement is proposed. The old mixed record
keeps its MEASURED quality and historical wording. Root should record the
provisional split mapping at PR preparation; no final IDs or shared edits
are made here. Required focused Claude re-audit covers this material status
change, the finite scope and trusted arithmetic.

2026-11-06,Codex assigned gpt-6.1-sol xhigh, rules9042e1c. Old inputs were
not retuned and accepted old theorems/killed rules were not reopened.
