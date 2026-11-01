# PD-T?proof-attempts-2-codex-51 — Degree-seven Padua maxima-count certification

ID kind: PD-T.
Aliases: A5 n=7; degree12 principal-field spatial and node-cone certificate.
Split from: the n=7 case of programme source06 / PD-T100 and A5.
Split into: field support50, generic finite implication18 and node-cone15; separate global result52.

## Statement

Target: the exact number of strict relative local maxima on the closed square of

lambda_7(x,y)=sum_B |L_B(x,y)|,

where B ranges through Pad_7={(cos(j*pi/7),cos(k*pi/8)):0<=j<=7,0<=k<=8,j+k even} and L_B are the degree<=7 polynomial cardinals. No exact count is asserted while finite checks are unfinished.

## Definitions

There are36 cardinals in lexicographic(j,k) order. FIELD12 uses result50's basis; positive mask bits select+L_B, unset bits select−L_B. Physical coordinates and strictness relative to the square are used. Node-cone leaves exclude the whole leaf directly by result15; ordinary leaves require every compatible sign mask.

## Assumptions

Exact algebra over Q(2cos(pi/7),2cos(pi/8)) with the principal embedding proved in50;128-bit outward integer dyadics; complete tree/root/edge/node predicates in a5_n7_schema.md; separate independent verifier and actual different-agent execution. The source's measured count and coordinates are not assumptions or seeds.

## Status by part

Overall status: **OPEN**. Written finite reduction is PROVED under18/15/50/53; the complete finite artifact and independent executions remain pending.

| A5 obligation | Current status |
|---|---|
| (1) proved all-strata reduction | PROVED supporting implications18+53, independent of degree |
| (2) exact node/degenerate coverage | local36-node producer passed; full certificate/checker pending |
| (3) root enclosure and discarded-region injectivity | exact predicates implemented; complete verification pending |
| (4) every compatible pattern | full tree/mask coverage pending |
| (5) exact creases and crossings | exact predicates; complete edge/node verification pending |
| final strict count | OPEN |

Required Claude audit of Part2 remains PENDING.

## Depends on

Results15,18,50,53. The generic result18 explicitly allows every finite degree and finite algebraic coefficient field; result09's n4 statement is not silently generalized. Singular Hessians, zero tangent curvature and zero normal derivatives are not discarded without a proved additional predicate. No cubic/quartic Taylor classification is carried into degree7.

## Checks

Actual commands and source/output identities belong to attempts/T-A5-n7.md. New modules are a5_n7_field.py, a5_n7_nodes.py, a5_n7_boxes.py and a5_n7_boundary.py. Independently owned verifier a5_checker_n7.py reconstructs the field/cardinals and verifies supplied data without rerunning search or root isolation. Full producer/checker execution is not yet claimed.

## Sources

Programme A5/source06 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. Full refreshed target gate is in T-A5-n7.md. No novelty/priority assertion; primary literature comparisons wait for a certified reached count.

## Proof or evidence

Apply the generic certificate implication18 in the finite algebraic field whose basis and real interpretation are proved in50. The checker must independently reconstruct all36 cardinals and1296 exact node values, verify a complete widest-side tree covering the square, every ordinary compatible mask, all referenced root existence/strictness/disjointness and whole-leaf hull injectivity. Direct all_gradient leaves independently verify result53 for every compatible mask, and exclude non-strict maxima as well. Every node leaf needs the complete exact feasible-direction breakpoints, positive gap and valid radial cube from15, with strict leaf containment. All four open-edge arrangements need nonzero restrictions, multiplicity-one crease coverage, complete rational norm-root partitions, complete sampled sign masks and exact dispositions of all reduced derivative roots. Every corner and every active corner sign is checked exactly.

Every accepted witness is a strict maximum and distinct IDs have disjoint enclosures. Conversely every possible strict maximum belongs to a tree leaf and one of its covered masks or to a separately covered edge/corner stratum. The node integral inequality and regular-zero comparison cover exact creases and crossings. A complete accepted certificate therefore proves its own ID count. An unfinished tree, unresolved point, missing mask or failed predicate proves no count.

## Scope

Only degree7; no all-degree count or inference from numerical agreement. Global values additionally require52's non-strict-maximum bounds.

## Open items

Complete finite artifact, separate independent verifier, actual different-agent producer/checker rerun, source comparison after certification, required Claude audit.

## History

2026-11-01, Codex /root/a5_develop, allocated gpt-6.1-sol xhigh; rules4bd1d65. Pre-run criteria and same original15:19UTC A5 ceiling recorded before execution. Initial record intentionally OPEN.
