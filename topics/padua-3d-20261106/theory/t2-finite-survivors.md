# PD-T?padua-3d-20261106-codex-T2-02 — Finite cyclic survivors and measured quality

ID kind: PD-T. Aliases: normalized rank-one survivor screen. Split from: none. Split into: none.

## Statement / definitions / assumptions

For n=2 and4, use the exact-cardinality normalized odd-cyclic nodes from T3-01, N=binom(n+3,3), M=2N−1 and1≤b<c≤N−1. The exhaustive screen finds four full-rank generators in each degree. Their measured21³ tensor-Lobatto Lebesgue samples all exceed both inherited same-degree QR approximate-Fekete and discrete-Leja lower-set controls.

## Status by part

Overall status: MEASURED. Exact finite ranks use integer dictionary determinants and direct algebraic-root witnesses; finite computer-proof acceptance still needs independent execution. Quality, conditions and selection are floating measurements only. No asymptotic fit or all-degree formula is claimed. Candidate disposition: finite survivors retained; none meets D2 promising. They are not killed solely for being above Leja at n4: immutable D2's quality kill requires two consecutive n≥6.

## Depends on / sources

Canonical PD-T?padua-3d-20261106-codex-T3-01; immutable inherited c3_lebesgue.py and c3_rank.py; D0/D1 receipt replay.json. Literature background not load bearing.

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


## Completed-audit process addendum — 2026-11-06 — m5

[Claude audit-01](../audit-01.md) completed the substantive independent audit
of candidate f1a5b0936d8fb2b033c69af59a6366550f170999, including the recorded
independent executions, after the supplementary Astra checks. Its accepted
mathematical scopes supersede earlier “audit/replay/rerun pending” and
“planned, no run claimed” process descriptions where those refer to that
completed work. This addendum changes no mathematical statement or status;
MEASURED observations remain MEASURED and OPEN targets remain OPEN. The
response dispositions, ID-kind mappings and evidence changes were covered
by [Claude audit-02](../audit-02.md); its accepted mathematical scope is
recorded there. This dated correction changes no statement or status.


## Symmetry, selection and scope correction — 2026-11-06 — m3/m4

The former strict-floating-order selection is superseded. Exact folded
residue sets identify the following classes up to coordinate permutation:

- n=2: (1,3,7)~(1,4,6)~(1,5,8), with (1,7,8) in the other survivor class.
- n=4: (1,15,19)~(1,21,29), and (1,11,15)~(1,25,30).

Cosine equality at odd modulus is exactly residue equality up to sign.
Parameter reindexing by a unit and coordinate permutation preserves the full
node set up to a cube isometry, so the true Lebesgue constants are exactly
equal within each class. The tensor-Lobatto evaluation mesh is invariant
under those permutations as well. The ≈5e−13 gap is rounding. Apply the
preregistered lexicographic tie rule: **(1,15,19)** is the n4 best-class
representative, not (1,21,29).

Developer executed:
`python topics/padua-3d-20261106/code/t2_symmetry_check.py --output topics/padua-3d-20261106/evidence/t2-symmetry-check.json`.
It enumerates complete integer folded-residue sets and all coordinate
permutations, with no floats. PASS; normalized pair counts 36/171/561 at
n=2/3/4 give 18/100/301 node-set classes. These finite census values are
recorded as MEASURED, not a new all-n symmetry theorem. The four generators
at each survivor degree represent two node sets. Existing rank/quality
receipts and statuses are unchanged.

The unshifted cubic obstruction leaves any degree sequence omitting n=3
outside its scope, including odd n≥5 as well as even degrees. Such variants
are deferred with explicit resume conditions in ../candidates-response-01.md.
