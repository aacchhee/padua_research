# PD-T?proof-attempts-2-codex-41 — Degree-six strict local maxima count

ID kind: PD-T.
Aliases: A5 n6 certificate;25interior/14edge/2corner;41closed-square maxima.
Split from: n6 case of programme A5 / `PD-T?programme-ideas-claude-06` (current registry IDEA206, historical programme IDEA17).
Split into: none; the n7/n8 cases retain separate statuses.

## Statement

For the degree-six even-checkerboard Padua Lebesgue function λ_6, there are exactly25 strict local maxima in the open square,14 on its open edges, and2 at corners, hence41 strict relative local maxima on the closed square. The edge counts in order(x=−1,x=1,y=−1,y=1) are(3,3,4,4). The maximum corners are(−1,−1),(1,−1).

## Definitions

Let a=sqrt3>0 and b=2cos(pi/7), with the exact principal embedding specified in40. Nodes are `(T_j(a/2),T_k(b/2))`, j=0,…,6,k=0,…,7,j+k even, in lexicographic order. The28 total-degree≤6 cardinal polynomials are reconstructed exactly; λ_6=Σ|L_i|. Maxima are strict and relative to the physical closed square. Monomials are ordered degree then decreasing x exponent.

## Assumptions

Exact field arithmetic in Q(a,b),112-bit outward fixed dyadics, complete verified finite certificate, separate independent checker and actual different-agent producer/checker execution. No source numerical count, seed or old tolerance-based discard is assumed correct.

## Status by part

Overall status: **OPEN** pending final complete checker and actual different-agent producer/global/checker execution.

| Mathematical part | Status | Evidence / remaining obligation |
|---|---|---|
| exact25/14/2 strict counts | OPEN | full developer certificate completed with zero unresolved cases; final separate checker and independent execution pending |

Supporting40,15 and18 are separately PROVED analytic implications and do not make this count PARTIAL. Required Claude audit of the Part2 branch remains pending.

## Depends on

`PD-T?proof-attempts-2-codex-40` (tensor field and principal real embedding),15 (exact physical node cones),18 (degree-independent complete spatial/edge/node certificate correctness).

The exact corrected-kernel construction follows `PD-T?proof-attempts-codex-01 (audit pending)`. Dated qualification2026-11-01: the parent reports part1 audit accepted and dispositions complete; the literal phrase preserves AC's required historical wording. For this n6 implementation ALL784 exact node values and partition of unity are independently reconstructed/checkable, so no numerical cardinal formula is inherited. No N3/N4/N5 computed result is used as a proof dependency.

## Checks

All commands below are from `/workspace/padua_research`; use `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B`. Actual environment: Python3.12.14,SymPy1.14.0,python-flint0.9.0/FLINT3.6.0,GROUND_TYPES=flint; precision112; no random seed.

Developer completed the node producer and then this full candidate command:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n6_nodes.py --output /tmp/a5-n6-nodes-pilot.json
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n6_boxes.py --boxes 200000 --seconds 2400 --depth 40 --ambiguity 8 --full-depth 40 --certificate --node-file /tmp/a5-n6-nodes-pilot.json --boundary --output /tmp/a5-n6-candidate.json.gz
```

The completed candidate gzip was copied byte-for-byte to `../outputs/a5_n6_certificate.json.gz`:414031bytes,SHA256 `c7a113b9b623c47309fd186c19ee2dddb2d5a0270c01b118bd11ee1ee069f0f5`. The embedded node data are independently checkable; the transient optional input is not an unverified exclusion authority. The different-agent producer is instructed to omit node-file and rebuild its own cones.

Developer interior phase887.948428154s:55607visited boxes,27804final leaves,1504228ordinary compatible-mask records and224node-cone leaves. Actual ordinary dispositions:1503090gradient,400strict Hessian,684root references to25 disjoint root boxes,54flat. No regular-point or common-factor fallback was used. Search profiling includes partial lists from subsequently subdivided boxes and is not certificate coverage. No missing path, depth-limit case, unresolved leaf or pending path remained; maximum depth30.

All28 exact node cones were constructed with complete feasible-side breakpoints and certified positive gaps/remainder cubes. Boundary phase142.734915733s:228actual sign masks(49,49,75,55) and all complete rational norm-root partitions; dispositions864outside,3890chosen-embedding derivative exclusions,470strict tangent minima,428incompatible signs and14accepted edge maxima. All restricted cardinals are nonzero, the multiplicity-one crease cover passed, and no zero-normal/tangent-degenerate case was left unresolved. Four corners yield two exact nodes and two all-active inward-descent maxima.

New producer modules: `a5_n6_field.py`, `a5_n6_nodes.py`, `a5_n6_boxes.py`, `a5_n6_boundary.py`; schema `a5_n6_schema.md`. Separate independently owned verifier: `a5_checker_n6.py`, which imports none of these producer modules and reconstructs its own formal field/cardinals/intervals/norms. Actual full checker command/hash/output and actual different-agent completion remain Runs needed. Pilot verifications are not represented as final acceptance.

## Sources

Pinned programme A5/source06 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e; original scientific part1a09d910. The relaxed gate, updated registry aliases and implementation diagnostics are recorded in `../attempts/T-A5-n6.md`. Source06's25interior/41total are MEASURED comparison data only. The primary Table3 row23interior/39total will be compared as a candidate correction only after certification; no author contact or current correction claim.

## Proof or evidence

The exact field is interpreted in the specified principal embedding by40. The corrected kernel gives a concrete28-polynomial coefficient array; direct exact interpolation checks prove it is the cardinal family. The finite certificate supplies a complete rational partition of the square. Each node-cone leaf passes15 on its WHOLE rectangle; each ordinary leaf lists every compatible28-bit mask, with no first-root return or escaped-Newton discard. Every exclusion is a valid necessary-condition failure for a strict maximum, and every positive root is enclosed by exact Krawczyk/contraction, strict cardinal signs and negative definite Hessian. Whole-leaf/root-hull injectivity covers all possible stationary points in each referencing leaf. Pairwise disjoint root boxes count distinct maxima once.

All boundary arrangement and residual derivative roots receive exact dispositions; regular crease/crossing exclusions follow verified multiplicity-one cover, not a proximity threshold. All corner active masks are explicitly checked. Theory18 proves that final acceptance of every one of these predicates gives exactly the stated counts, including possible singular-Hessian/cardinal-zero cases without silently discarding equality. The full developer producer has completed, but the final verification/execution obligations remain pending, so this result is OPEN here.

## Scope

Exactly n6. No n7/n8 count, general count formula, global argmax, paper correction, priority or novelty is inferred. The separate n6 global-value target is42.

## Open items

Final frozen checker/controls and actual different-agent producer/global/checker execution; exact artifact identities and receipts; required Claude audit. Any failed/unresolved final predicate blocks promotion.

## History

2026-11-01, Codex `/root/a5_n4` assignedn6, inherited gpt-6.1-sol xhigh; initial rules38db12b, refreshed fullSHA842dfaaeff524b4db4141d314afff6ad4a5b7721. Full candidate completed around10:59UTC with proposed41count; status deliberately OPEN until final independent checks. The original source MEASURED claim is preserved and is not a truth assumption.
