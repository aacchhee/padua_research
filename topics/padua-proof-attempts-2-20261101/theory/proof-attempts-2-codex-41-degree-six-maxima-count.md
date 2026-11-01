# PD-T?proof-attempts-2-codex-41 — Degree-six strict local maxima count

Final ID: **PD-T173**. Provisional ID `PD-T?proof-attempts-2-codex-41` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T100 / OPEN_TARGETS A5 (exact finite case, supporting result or separately OPEN obligation; source measurement retained).

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints.

LITERATURE attribution (audit-01 F8): arXiv 2605.23299v1, §3.3 Table 3, LIT-388. Its reported counts are source statements; the local certificate/proof and candidate-correction scope are separate.

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

Overall status: **PROVED** by the complete exact certificate, separately implemented checker, and actual different-agent producer/global/checker execution. Required Claude audit remains PENDING.

| Mathematical part | Status | Evidence / remaining obligation |
|---|---|---|
| exact25/14/2 strict counts | PROVED | complete finite coverage accepted by the frozen separate checker; fresh different-agent producer and matching full replay plus all38 controls passed |

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

New producer modules: `a5_n6_field.py`, `a5_n6_nodes.py`, `a5_n6_boxes.py`, `a5_n6_boundary.py`; schema `a5_n6_schema.md`. Separate independently owned verifier: `a5_checker_n6.py`, which imports none of these producer modules and reconstructs its own formal field/cardinals/intervals/norms. Pilot verifications are not represented as final acceptance.

Completed verification update: the frozen separate checker `34d8c0b7afb261d5f082022f49a84ec6e741f50de31904da5f4221f02f9673c8` actually accepted the full count/global pair in952.450290653seconds, exit0. Its separate controls harness `fd926f0d390ab2336476d054bfcee89aba97c624487f8acd0e64491c664633e0` actually passed all38 controls in1093.837045029seconds, including another full positive count/global replay. The exact commands and output identities are in `../independent-checks-a5-n6-checker.md`. The different executor's fresh producer, with no node-file, also completed and its matching full checker actually accepted41 and the global predicates in590.993498943seconds. Its decoded count artifact equals the developer artifact after removing only the two phase timers. The executor's sequential full controls actually completed with exit0 in564.364826564seconds: all38 cases passed,33negative and5positive, including a full developer-pair count/global replay. All eight source/schema/checker identities matched after exit. The final frozen `../independent-execution-a5-n6.md` records every exact command, the interrupted resource-control attempts separately, decoded mathematical equality, artifact identities and final source closure. No finite verification obligation remains pending.

## Sources

Pinned programme A5/source06 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e; original scientific part1a09d910. The relaxed gate, updated registry aliases and implementation diagnostics are recorded in `../attempts/T-A5-n6.md`. Source06's25interior/41total are MEASURED comparison data only. The direct post-certification primary Table3 comparison is `../outputs/a5_n6_literature-comparison.md`: certified25/41 versus printed23/39 is a bounded candidate correction, with no author contact or novelty claim.

## Proof or evidence

The exact field is interpreted in the specified principal embedding by40. The corrected kernel gives a concrete28-polynomial coefficient array; direct exact interpolation checks prove it is the cardinal family. The finite certificate supplies a complete rational partition of the square. Each node-cone leaf passes15 on its WHOLE rectangle; each ordinary leaf lists every compatible28-bit mask, with no first-root return or escaped-Newton discard. Every exclusion is a valid necessary-condition failure for a strict maximum, and every positive root is enclosed by exact Krawczyk/contraction, strict cardinal signs and negative definite Hessian. Whole-leaf/root-hull injectivity covers all possible stationary points in each referencing leaf. Pairwise disjoint root boxes count distinct maxima once.

All boundary arrangement and residual derivative roots receive exact dispositions; regular crease/crossing exclusions follow verified multiplicity-one cover, not a proximity threshold. All corner active masks are explicitly checked. Theory18 proves that final acceptance of every one of these predicates gives exactly the stated counts, including possible singular-Hessian/cardinal-zero cases without silently discarding equality. The complete developer artifact and the independently regenerated artifact both passed the final frozen checker. The executor also completed the full developer-pair positive replay and all counterfeit controls. Thus the written reduction and finite predicates establish the stated exact count.

## Scope

Exactly n6. No n7/n8 count, general count formula, global argmax, accepted erratum, priority or novelty is inferred. The separate n6 global-value target is42.

## Open items

Required Claude audit of the Part2 branch. Exact finite verification, artifact identities and supplementary independent execution are complete; no n7/n8 case is inferred.

## History

2026-11-01, Codex `/root/a5_n4` assignedn6, inherited gpt-6.1-sol xhigh; initial rules38db12b, refreshed fullSHA842dfaaeff524b4db4141d314afff6ad4a5b7721. Full candidate completed around10:59UTC with proposed41count; status deliberately OPEN until final independent checks. The original source MEASURED claim is preserved and is not a truth assumption.

2026-11-01 final verification checkpoint: promoted the unchanged count statement OPEN→PROVED only after the actual different-agent fresh producer, matching full checker and sequential full controls all completed with exit0 and unchanged frozen sources. The separate required Claude audit remains PENDING.
