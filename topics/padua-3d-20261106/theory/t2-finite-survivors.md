# PD-T?padua-3d-codex-T2-02 — Finite cyclic survivors and measured quality

ID kind: PD-T. Aliases: normalized rank-one survivor screen. Split from: none. Split into: none.

## Statement / definitions / assumptions

For n=2 and4, use the exact-cardinality normalized odd-cyclic nodes from T3-01, N=binom(n+3,3), M=2N−1 and1≤b<c≤N−1. The exhaustive screen finds four full-rank generators in each degree. Their measured21³ tensor-Lobatto Lebesgue samples all exceed both inherited same-degree QR approximate-Fekete and discrete-Leja lower-set controls.

## Status by part

Overall status: MEASURED. Exact finite ranks use integer dictionary determinants and direct algebraic-root witnesses; finite computer-proof acceptance still needs independent execution. Quality, conditions and selection are floating measurements only. No asymptotic fit or all-degree formula is claimed. Candidate disposition: finite survivors retained; none meets D2 promising. They are not killed solely for being above Leja at n4: immutable D2's quality kill requires two consecutive n≥6.

## Depends on / sources

Canonical PD-T?padua-3d-codex-T3-01; immutable inherited c3_lebesgue.py and c3_rank.py; D0/D1 receipt replay.json. Literature background not load bearing.

## Evidence

| n | generator z | measured mesh Λ | Leja | QR |
|---|---|---:|---:|---:|
|2|(1,3,7)|8.1340690371|7|7|
|2|(1,4,6)|8.1340690371|7|7|
|2|(1,5,8)|8.1340690371|7|7|
|2|(1,7,8)|7.0532561591|7|7|
|4|(1,11,15)|45.7151239480|19.4981750446|11.2448776896|
|4|(1,15,19)|37.4870129676|19.4981750446|11.2448776896|
|4|(1,21,29)|37.4870129676|19.4981750446|11.2448776896|
|4|(1,25,30)|45.7151239480|19.4981750446|11.2448776896|

The exact-rank screen covers36 generators n2 and561 n4, with maximum ranks10 and35 respectively. Detailed distributions in evidence/t2-generators.json; complete catalogues regenerable by committed checker/producer. Quality code checks direct V=CD/8 in splitting fields at p191 (M19) and p139 (M69), with nonzero V determinants for all eight survivors. These specialize the actual cosine axes. Measured n4 conditions about24.96 for the better pair and30.97 for the other pair; cardinality residuals<1.6e−14. The two better n4 values differ only at floating noise; report the pair together. Under the preregistered strict measured-value ordering the selected representative is (1,21,29), whose floating value is smaller by about5e−13; no exact tie or robust strict ordering is claimed. No claimed exact equality between their true Lebesgue constants.

## Checks

Executed OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t2_quality.py. All source/data hashes and direct-root parameters in evidence/t2-quality.json; no randomness. Evaluator/mesh/controls are exactly those declared in preregistration-T2.md and validated by D0/D1. This is a sampled lower-bound diagnostic, not a certified maximum. Fits INCONCLUSIVE: fewer than four n≥4 degrees and no surviving every-degree normalized rule. No asymptotic evidence inferred.

## Scope / open items / history

Strongest tested n4 representative under strict measured ordering z=(1,21,29) remains a finite unisolvence/quality data point, not a family. Even-degree subsequences remain OPEN, deferred because n4 quality does not favor extending an exhaustive search. Resume with an explicit structural correction or different phase/coset rule and a preregistered bounded test, rather than ad hoc degree skipping or generator fitting. Parent-directed stop after productive bounded screen. 2026-11-06, rules ccd9e905d19c0c625c196c4a3f3e707058ed042a, gpt-6.1-sol medium.
