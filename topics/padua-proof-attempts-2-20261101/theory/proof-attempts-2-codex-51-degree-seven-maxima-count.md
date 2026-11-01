# PD-T?proof-attempts-2-codex-51 — Degree-seven Padua maxima-count certification

ID kind: PD-T.
Aliases: A5 n=7; degree12 principal-field spatial and node-cone certificate.
Split from: the n=7 case of programme source06 / PD-T100 and A5.
Split into: field support50, generic finite implication18, node-cone15 and universal-gradient53; separate global result52.

## Statement

The exact number of strict relative local maxima on the closed square of

lambda_7(x,y)=sum_B |L_B(x,y)|,

where B ranges through Pad_7={(cos(j*pi/7),cos(k*pi/8)):0<=j<=7,0<=k<=8,j+k even} and L_B are the degree<=7 polynomial cardinals, is **50**: **33 interior, 15 on open edges and 2 at corners**. The corner maxima are exactly(−1,−1),(−1,1).

## Definitions

There are36 cardinals in lexicographic(j,k) order. FIELD12 uses result50's basis; positive mask bits select+L_B, unset bits select−L_B. Physical coordinates and strictness relative to the square are used. Node-cone leaves exclude the whole leaf directly by result15, and direct all_gradient leaves use the universal bound53. Ordinary leaves require every compatible sign mask.

## Assumptions

Exact algebra over Q(2cos(pi/7),2cos(pi/8)) with the principal embedding proved in50;128-bit outward integer dyadics; complete tree/root/edge/node predicates in a5_n7_schema.md; separate independent verifier and actual different-agent execution. The source's measured count and coordinates are not assumptions or seeds.

## Status by part

Overall status: **PROVED**, by the written finite reduction18/15/50/53 and the complete exactly verified finite certificate. Required Claude audit of Part2 remains PENDING.

| A5 obligation | Current status |
|---|---|
| (1) proved all-strata reduction | PROVED by18+53 and the case argument below |
| (2) exact node/degenerate coverage | PROVED: all36 cones,2220 complete breakpoints,204 node leaves; no unresolved case |
| (3) root enclosure and discarded-region injectivity | PROVED:33 disjoint interior root enclosures and every referenced whole-leaf hull verified |
| (4) every compatible pattern | PROVED:54898-leaf complete tree;50412 universal leaves and96438 ordinary mask records |
| (5) exact creases and crossings | PROVED: active-polynomial comparison, node cones and all4 exact edge arrangements |
| final strict count | PROVED:50=33+15+2 |

Required Claude audit of Part2 remains PENDING.

## Depends on

Results15,18,50,53. The generic result18 explicitly allows every finite degree and finite algebraic coefficient field; result09's n4 statement is not silently generalized. Singular Hessians, zero tangent curvature and zero normal derivatives are not discarded without a proved additional predicate. No cubic/quartic Taylor classification is carried into degree7.

## Checks

Actual commands and all frozen source/output identities are in attempts/T-A5-n7.md, independent-checks-a5-n7-checker.md and independent-execution-a5-n7.md. New producer modules are a5_n7_field.py, a5_n7_nodes.py, a5_n7_boxes.py and a5_n7_boundary.py; additional global values use a5_n7_global.py. The separately implemented a5_checker_n7.py and its formal-field helper reconstruct the field and cardinals independently and verify supplied identities, partitions and predicates without rerunning search or root isolation. Arithmetic is exact field/Fraction arithmetic or128-bit outward integer dyadics. Arb only proposes outward rational root intervals; exact Sturm coverage is independently verified.

The developer producer, global constructor and mechanical repacker all actually exited0. The following independent executions also actually exited0, with their source guards unchanged:

| Execution | Seconds | Completed result |
|---|---:|---|
| checker implementer's full developer-pair verification |1840.064621| count, all coverage and global predicates accepted |
| checker implementer's developer-pair controls |1934.381991|42 deliberate defects rejected;10 positive controls accepted |
| different executor's full verification of its fresh own pair |1899.927920| count, all coverage and global predicates accepted |
| different executor's developer-pair controls |1481.931319|42 deliberate defects rejected;10 positive controls accepted, including full developer count/global verification |

The different executor rebuilt all36 node cones, ran the complete producer without a supplied node file, constructed its own values and losslessly packed its own whole certificate. Its own full verification and its developer-pair full-positive control are distinct actual runs. All six producer/schema hashes remained fixed during production, and all ten current producer/schema/checker/codec pins matched after the final controls. The controls are finite tests of the checker, not an exhaustive proof of its implementation.

Essential developer artifacts are outputs/a5_n7_certificate.json.xz (436960bytes, SHA2569338e01c89482acd4e3e948812a62b5511ca6d9afcf87672fad053ee28cfaa85) and the matching outputs/a5_n7_global.json (9493bytes, SHA256b309483ba2b1c7dc5c83bc23d9cfcb0dfb68191fb8b3677f0d0124e0655a17cb). The single standardXZ preserves every decoded JSON byte; outputs/a5_n7_repack.json verifies identity and only the global file's count-archive hash rebinding. No evidence is split. The independent whole XZ is436504bytes, SHA256a8a78bc7d206507103710d52e5279842b70d5bc1f38dd6c3fe2eca6a5e4fc00a, with its own matching global. Independent acceptance, rather than agreement between outputs or a producer summary, discharges the finite proof obligations.

## Sources

Programme A5/source06 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. Full refreshed target gate is in T-A5-n7.md. After certification, root directly reread arXiv2605.23299v1 §3.3/Table3, printedpage9: the degree7 row is27 interior/42 total. The certificate gives a scoped candidate correction of+6interior/+8total; outputs/a5_n7_literature-comparison.md records the direct primary read, board/square-isometry scope and pending audit. The programme's MEASURED33/50 agrees, so no PD-N against that measured claim is inferred. No novelty/priority or all-degree assertion; no author contact.

## Proof or evidence

First apply the generic implication18 in the finite algebraic field proved in50. The independently reconstructed Vandermonde cardinals satisfy all1296 exact node interpolation identities and partition of unity, so the verified polynomials are the stated L_B. The principal brackets and native-to-tensor inverse establish the real meaning of every outward coefficient bound.

For completeness, let z be an interior strict local maximum. Since lambda=max_s P_s and P_s<=lambda, every active P_s is a strict local maximum atz. It has zero gradient and negative-semidefinite Hessian. Every active sign is compatible with every leaf containingz, including when one or more cardinals vanish. Thus the argument applies on exact creases and arbitrary crossings, without differentiating lambda.

The verifier accepted a complete widest-side binary partition with109795 visited boxes and54898 leaves, with no missing prefix, pending path or unresolved record. Of these leaves,50412 have a result53 universal gradient exclusion and204 lie strictly inside a verified result15 radial cube. The former exclude all compatible masks simultaneously. In the latter, radial ascent excludes every non-node maximum, and a node has value1 and is not a strict maximum because lambda>=1. All36 ordered nodes and all2220 required feasible-direction breakpoints were verified, even if a particular cube is unused.

The remaining4282 leaves cover every compatible mask by96438 ordinary records:96094 strict gradient exclusions,146 verified wrong-curvature exclusions, and198 references to root witnesses. There are no flat, factor or regular-point records. Consequently a stationary compatible polynomial with an unresolved singular Hessian is not silently discarded: it would prevent certificate acceptance. For each root reference, whole-leaf/root-hull gradient injectivity identifies any such stationary point with the supplied root. Exact Krawczyk inclusion establishes existence in its box; strict cardinal signs and negative-definite Hessian establish a strict maximum of lambda there. The verifier accepted33 distinct interior IDs and checked their pairwise disjoint enclosures. Multiple leaf references do not add to this count.

For each of the four open edges, all36 restricted cardinals are nonzero polynomials. Their exact squarefree union has a verified multiplicity-one cover: every crease point is regular for at least one restricted cardinal. At an edge local maximum, flipping that cardinal's active sign would force its tangent derivative to be both zero and nonzero, a contradiction. Complete exact Sturm partitions of the rational norm cover all arrangement breakpoints. Every sign pattern on the intervening intervals is included, and all reduced tangent-derivative norm roots receive exact dispositions. In edge order x=−1,x=1,y=−1,y=1 there are83,52,99,99 patterns and3,4,4,4 accepted roots. Across the333 patterns, all19863 point records are accounted for:15472 derivative exclusions,836 strict minima,2766 outside the physical edge,774 incompatible signs and15 accepted roots. There is no unresolved tangent-curvature or zero-normal case. Each accepted root has strict sign consistency, negative tangent curvature and strictly negative physical inward derivative; it is a strict square-relative maximum. Isolating partitions and disjoint root boxes ensure no double count.

Finally all four corners are accounted for exactly. The two right corners are nodes and are excluded by lambda>=1. At the two left corners the verifier checks all16 active sign choices in total: every active polynomial has strictly negative inward coordinate derivatives, so their finite maximum has a strict relative maximum there. These produce exactly two corner maxima.

Every accepted witness is therefore a distinct strict maximum, and the exhaustive interior/edge/corner argument excludes every other one. Summing the verified IDs gives33+15+2=50. Neither numerical agreement nor a producer's count is used in this implication. ∎

## Scope

Only degree7; no all-degree count or inference from numerical agreement. Global values additionally require52's non-strict-maximum bounds.

## Open items

Required Claude audit of Part2. The degree-seven count, complete finite evidence, actual independent executions and post-certification primary comparison are complete. Other degrees and the all-degree count remain separate targets.

## History

2026-11-01, Codex /root/a5_develop, allocated gpt-6.1-sol xhigh; rules4bd1d65. Pre-run criteria and same original15:19UTC A5 ceiling recorded before execution. Initial record intentionally OPEN.

2026-11-01 after13:33UTC: promoted to PROVED only after the different executor's final developer-pair controls actually exited0. No frozen scientific source or certificate was changed for promotion. Required Claude audit remains PENDING.
