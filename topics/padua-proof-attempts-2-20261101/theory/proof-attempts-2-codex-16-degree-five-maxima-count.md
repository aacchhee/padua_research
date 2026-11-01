# PD-T?proof-attempts-2-codex-16 — Degree-five Padua maxima-count certification

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints.

LITERATURE attribution (audit-01 F8): arXiv 2605.23299v1, §3.3 Table 3, LIT-388. Its reported counts are source statements; the local certificate/proof and candidate-correction scope are separate.

ID kind: PD-T.
Aliases: A5 n=5; exact node-cone spatial certificate; registered reference14 interior /9 edge /2 corner /25 total.
Split from: the n=5 case of `PD-T?programme-ideas-claude-06` and programme A5.
Split into: supporting node-cone theorem15, generic certificate correctness18, and separate global-value result17.

## Statement

For the even-checkerboard degree-five Padua board

Pad_5={(cos(jπ/5),cos(kπ/6)):0≤j≤5,0≤k≤6,j+k even},

let L_b be its total-degree≤5 polynomial cardinals and λ_5=Σ_b|L_b| on the closed square. Then λ_5 has exactly **25 strict relative local maxima:14 interior,9 open-edge and2 corner maxima**. The corner maxima are(−1,−1) and(−1,1).

## Definitions

There are21 cardinals in lexicographic(j,k) order. Mask bitb determines sign+1 when set and−1 otherwise. Physical coordinates and relative-to-square strictness are used. A node-cone leaf excludes its whole rectangle by a uniform radial inequality, rather than enumerating2^20 possible node signs. Ordinary leaves enumerate every compatible mask explicitly.

## Assumptions

The board above, exact algebra overQ(sqrt3,sqrt5), outward integer dyadic intervals at96bits, complete tree/mask/edge/root predicates in a5_n5_schema.md, and a separate independent verifier and actual different-agent producer/checker run. The source's measured number is not an assumption.

## Status by part

Overall status: **PROVED** (written complete reduction, exact/outward certificate, separate independent verifier and actual different-agent producer/global/checker execution).

| A5 obligation for n=5 | Status | Evidence |
|---|---|---|
| (1) finite reduction, all strata | PROVED under separate result18 | complete spatial tree, compatible masks, exact edge arrangement and corners |
| (2) degenerate/node/boundary coverage | PROVED |21 exact physical node cones; all edge/corner cases; no old floating handler reused |
| (3) rigorous root enclosures/exclusions | PROVED | Krawczyk/contraction and whole-hull injectivity; complete exact derivative partitions |
| (4) every consistent pattern | PROVED |225656 ordinary mask dispositions plus150 whole-leaf direct λ exclusions |
| (5) exact creases/crossings | PROVED | polynomial multiplicity/derivative identities and exact node bounds; no coincidence tolerance |
| exact25=14+9+2 count | PROVED | complete disjoint accepted root IDs and independent checks |

The node-cone predicate proves a stronger uniform exclusion of λ itself on its entire leaf; it does not silently skip ambiguous signs. The count was promoted only after complete independent checks. Required Claude audit of Part2 remains **PENDING**.

## Depends on

- `PD-T?proof-attempts-2-codex-15`: exact physical node-cone exclusion, including boundary feasibility and crease zeros.
- `PD-T?proof-attempts-2-codex-18`: complete degree-independent spatial/edge/corner certificate implication.

The n4-specific result09 is a predecessor, not silently inherited as a statement for degreefive. No cubic negative-definite-Hessian necessity or quartic Taylor truncation is used. No part1 local proof is needed for this degree; old boundary-handler data is not trusted.

## Checks

All producer/checker modules are new degree-five files; n3/n4 sources were untouched. Actual developer commands, from the repository root with `PYTHONDONTWRITEBYTECODE=1`, were:

```text
python -B topics/padua-proof-attempts-2-20261101/code/a5_n5_boxes.py --certificate --boundary --boxes 100000 --seconds 3600 --depth 36 --full-depth 30 --ambiguity 6 --root-depth 12 --output topics/padua-proof-attempts-2-20261101/outputs/a5_n5_certificate.json.gz
python -B topics/padua-proof-attempts-2-20261101/code/a5_n5_global.py topics/padua-proof-attempts-2-20261101/outputs/a5_n5_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_n5_global.json
```

Both exited0. Exact QQ(sqrt3,sqrt5) algebra and outward96-bit integer dyadic intervals supply every proof inequality; only timings are floating metadata. No random seed applies. Actual developer environment: Python3.12.14, SymPy1.14.0, ordinary Python exact ground arithmetic. The final interior timer was264.460383s and boundary timer1047.255400s; these are phase timers, not a separately instrumented whole-command measurement.

The single complete developer gzip is125245bytes with SHA256 `a1238d59781733cc0d380dc513a0a642d0e24b985aeb9b90bb7233756273386e`. Its matching global JSON is3897bytes, SHA256 `57a7c9c12667b5d441cea4fc60a68563cc1accc8d8adc8ca41ccd339fa16f17d`. This is genuine compression of one artifact, not splitting; no cold-storage dependency is needed.

Frozen code identities and exact commands are recorded in `../independent-execution-a5-n5.md`. The producer modules are `a5_n5_boxes.py`, `a5_n5_nodes.py`, `a5_n5_boundary.py` and `a5_n5_global.py`. Separate independently written checker source hash is `6390d465a0e4c83f5cb75673834da4bfbda98c507266c9a81c60c85baceb7bab`; its controls source hash is `0508b79bd96f3a3b12c6f907992c5e179910f869d2fdabe3e669e8286164ef91`. The checker imports no producer and performs no spatial search or root isolation. It verifies supplied complete partitions and every predicate.

A different subagent `/root/input_manifest` actually reran the full producer with no node-file input, regenerated all21 gaps/cubes, generated a matching global file, and ran the checker and full controls. Its environment used `PYTHONPATH=/tmp/padua2-deps`, Python3.12.14, SymPy1.14.0, python-flint0.9.0/FLINT3.6.0. All six source pins matched before and after execution. It then separately checked the developer count/global pair. Every command exited0.

| Actual independent artifact/run | SHA256 / result |
|---|---|
| independent gzip,125252bytes | `d22c9b1e32728e511ca4ac20506df614b501669a37bc287ed1cde802b6c7f4b3` |
| independent global JSON | `47d50f724471904d4873c471e48a2dec9992eb537f5597afe13d07fe17152ccb` |
| checker on own pair,299.016661s | `80a33c158a9d34afdc4004f77360ce8bd36439107783a7c235d98aba5d524d76`; count/global accepted |
| checker on developer pair,257.679985s | `8dabc97c98a71c9b546caf150e53834fab8c45648d5cbbdc76e081ac236d2e98`; count/global accepted |
| full31 controls | `462377ebbe8a9ad72c00cbcd9b8c1998b3ea24b49a927cfd2b1b3a15bbbf7281`;27 negative rejected,4 positive accepted |

Decoded developer and independent certificates are identical after removing only the interior and boundary timing fields. Their global files agree after removing only their different raw-certificate SHA bindings. The raw gzips are not claimed byte-identical. Every mathematical field matches.

The independent checker implementer also actually checked the complete independent pair and ran all31 controls: full positive receipt `../outputs/a5_checker_n5_full-integration.json`, SHA256 `d9bf5b17a7c308c377be42e0df9c57d7539ce1b8a60850486bb77b6d66be943f`. Its separate record is `../independent-checks-a5-n5-checker.md`. The mathematical support implications were independently inspected in the reduction/node review record. These supplementary checks are not the required Claude audit.

Complete verified coverage:20363 visited rectangles forming10182 leaves;225656 ordinary pattern records;150 node-cone leaves;21 exact node records and738 complete directional breakpoints;139 edge sign patterns and1815 derivative-candidate dispositions; all four corners. Interior dispositions are225462 gradient,48 Hessian,4 flat and142 references to14 disjoint interior roots. Boundary dispositions are1070 derivative,216 minimum,330 outside,190 sign and9 accepted roots. No factor/regular-point fallback, unresolved case or missing path occurs in this artifact.

## Sources

Authoritative programme A5 and source06 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e; full target-specific gate and post-merge impact are in T-A5-n5.md. No novelty/priority claim.

Primary comparison: Białas-Cież–De Marchi–Suder, [arXiv2605.23299v1](https://arxiv.org/pdf/2605.23299v1), §3.3, printedp.9, Table3, reports14 interior and25 total maxima at n=5. These agree with the independently certified result. Reading coverage and limits are in `../outputs/a5_n5_literature-comparison.md`. No n=6,7,8 correction is inferred here.

## Proof or evidence

The full mathematical reduction is result18, with node leaves discharged by result15. The following finite obligations were all verified for the final artifact:

1. Independent exact reconstruction of all21 cardinals, interpolation and partition of unity.
2. Complete widest-side binary tree covering the whole square. Every leaf either has the complete ordered compatible-mask list or a strictly containing accepted node rectangle.
3. Every ordinary mask receives an exact derivative/strict-curvature/regular-point/regular-factor exclusion or a root reference with rigorous Krawczyk existence, strict signs/negative definiteness and whole-hull injectivity. No early return after one root accepts a leaf.
4. Every node record supplies all feasible unit-square direction segments, every exact gradient-zero breakpoint, positive gap, node-cardinal positivity, complete Hessian bound and valid geometry. Every referenced leaf lies strictly inside that rectangle. The integral inequality handles exact zeros and crossings without tolerance.
5. All four edge arrangements have nonzero restricted cardinals and the exact multiplicity-one regular-crease cover. Complete supplied norm-root partitions and all gap sign masks cover each edge; every reduced derivative root receives an exact disposition. Zero tangent curvature or zero inward derivative is not silently discarded.
6. All four corners are checked exactly. Root boxes/intervals have disjoint IDs and every accepted witness has a strictness proof.

The independent verifier accepted all six obligations with no unresolved record. Result18 therefore equates the strict count with its25 accepted IDs. The node evidence and source agreement were never used to replace a missing case.

## Scope

Only degreefive. Degree-three and degree-four results are separate frozen files. Cases n=6,…,8 remain outside this record. A global argmax conclusion additionally needs result17's value and non-strict-maximum checks.

## Open items

The degree-five count is complete. Required Claude audit of Part2 remains PENDING. Cases n=6,…,8 require their own complete artifacts and independent executions; neither this result nor the source's measured values certifies them.

## History

2026-11-01, Codex `/root/a5_develop`, allocated gpt-6.1-sol xhigh; rules initially44be0080c69495cc6959e3d4c2b602fa73678d76. Initial status was OPEN while finite checks ran. Promoted to PROVED only after the complete developer/independent artifacts, matching global evidence, separate verifier and31 controls all passed. Administrative handoff/allocation-rule changes were read at4bd1d65ad36ddded9bf4799c0557d4a6bb83e764; they changed no scientific input or frozen code. Required Claude audit remains PENDING. The original n=3,…,8 target is preserved by splitting this n=5 case.
