# PD-T?proof-attempts-2-codex-52 — Degree-seven global Padua argmax

ID kind: PD-T.
Aliases: A4(d) n=7; value certificate with node leaves; plateau exclusion.
Split from: finite-degree corollary of programme corner-argmax target.
Split into: none; all-n corner argmax remains OPEN.

## Statement

The function lambda_7 in51 attains its global maximum exactly at(−1,−1),(−1,1), with value C given by result50's FIELD12 vector

[83/28,−5/7,−4/7,2/7,−2/7,0,2/7,0,−2/7,1/7,2/7,0].

Equivalently,28C=83−20b−16b²+8b³−8a+8ab²−8a²+4a²b+8a²b², where a=2cos(pi/7),b=2cos(pi/8). In particular C>11/2.

## Definitions

Use results15/18/50/51/53. An exceptional ordinary-leaf occurrence is a compatible pattern disposition flat or factor: those exclude a strict maximum but can admit a non-strict stationary ridge. Every occurrence requires its own whole-leaf value bound.

## Assumptions

A complete accepted degree-seven count certificate, plus independently verified exact fields proving every exceptional occurrence and every accepted interior/open-edge root has value below11/2; every constant edge restriction equals±1; nodes have value1; both non-node corners have exact common value C>11/2. The separate value artifact is bound to the SHA256 of the stored count file, including its XZ encoding. No numerical list or agreement is a premise.

## Status by part

Overall status: **PROVED**, by the complete accepted51 certificate, the additional exactly verified value predicates and the written non-strict-maximum argument below. Required Claude audit of Part2 remains PENDING.

| Part | Current status |
|---|---|
| exact common corner value and C>11/2 | PROVED: independent exact corner identity and strict outward rational separation |
| non-strict-global-maximum case argument | PROVED by the exhaustive case argument below, including direct53 leaves |
| all exceptional/root/constant-edge bounds | PROVED: all33 interior and15 edge bounds; zero exceptional occurrences and zero constant-edge patterns |
| corner-only argmax | PROVED: exactly(−1,−1),(−1,1) |

## Depends on

Results15,18,50,53 and a complete accepted51 certificate. Strict-count completeness alone is insufficient, so exceptional values are an additional obligation.

## Checks

New producer a5_n7_global.py; schema a5_n7_schema.md. Exact native corner diagnostic is outputs/a5_n7_corner-diagnostic.json. The separate checker independently reconstructed C and both nodecorner values in outputs/a5_checker_n7_corner-values.json (8.66s). Subsequently the complete count/global pair passed the separate checker's full verification (1840.064621s) and52 controls (1934.381991s). A different executor regenerated all field/cardinal/node/tree/edge/value data, passed its own full pair (1899.927920s), and passed52 developer-pair controls (1481.931319s), including an actual complete developer count/global verification. Each controls run rejected42 deliberate defects and accepted10 positive controls. All current-stage source pins matched after the actual final exit.

The essential value artifact is outputs/a5_n7_global.json (9493bytes, SHA256b309483ba2b1c7dc5c83bc23d9cfcb0dfb68191fb8b3677f0d0124e0655a17cb). It binds the whole outputs/a5_n7_certificate.json.xz (436960bytes, SHA2569338e01c89482acd4e3e948812a62b5511ca6d9afcf87672fad053ee28cfaa85), with exact decoded identity in outputs/a5_n7_repack.json. The different executor's matching pair and output identities are in independent-execution-a5-n7.md. Completed machine receipts are outputs/a5_checker_n7_full-integration.json, outputs/a5_checker_n7_controls-full.json, outputs/a5_independent_n7_checker.json and outputs/a5_independent_n7_controls.json; both full receipts set global_argmax_verified, global_no_nonstrict_plateau_above_cut, node_leaf_global_exclusion_verified and all_gradient_global_exclusion_verified to true. Actual full commands and frozen pins are in T-A5-n7.md and both independent receipts.

Both complete verifications check the occurrence list against every ordinary leaf: there are zero flat/factor occurrences. The placeholder exception_upper=−10 is consequently unused and is not a bound on lambda. There are also zero constant-edge patterns in this certificate; the verifier nevertheless enforces the general constant-edge identity±1. Every one of the33 interior and15 edge root IDs has its own outward value interval strictly below11/2. Both left-corner values equal the stated FIELD12 vector exactly, and their rational lower enclosures exceed11/2. Thus the global argument has extra weak-maximum coverage beyond the strict count.

## Sources

Registered A4(d) finite-case corollary reached while solving A5, programme source05/source06 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. The post-certification primary count comparison is outputs/a5_n7_literature-comparison.md; it supplies no premise for this proof. No all-degree claim or novelty assertion.

## Proof or evidence

Continuity gives at least one global maximum. The exact corner value C>11/2 excludes nodes and every candidate whose certified value is below11/2.

Suppose a global maximum z is interior. Every active signed polynomial P_s has a non-strict local maximum there, so its gradient vanishes and Hessian is negative semidefinite. Select any leaf containing z and any active compatible mask. A node leaf excludes any non-node local maximum by strict radial ascent; the node itself has value1. A direct all_gradient leaf excludes non-strict maxima by53. In an ordinary leaf, derivative and strictly wrong-curvature predicates exclude non-strict maxima as well. A regular-point injection identifies z with an exact node or an impossible regular-zero local maximum (or a boundary point, impossible for interior z). A root reference and whole-hull injection identify z with the accepted root, whose value is below11/2. A flat/factor occurrence is bounded below11/2 on the entire leaf by the separate value artifact. Thus a global maximum cannot be interior.

On an open edge, regular-crease points are excluded by tangent sign flipping, and all noncrease patterns and all reduced derivative roots are covered by18. A constant edge restriction equals±1; otherwise the exact derivative/sign/strict-positive-curvature/positive-inward tests exclude non-strict maxima, or the candidate is an accepted root with value below11/2. No unresolved zero-curvature or zero-normal case is assumed away. Hence a global maximum cannot lie on an open edge.

The remaining four corners have exactly computed values: the two node corners have1, and the two non-node corners both C. All the additional finite predicates just used have passed complete independent verification and the actual different-executor replay. Therefore the global maximum is C and precisely those two corners attain it. This argument does not infer global completeness from a strict-maxima list. ∎

## Scope

Only the degree7 board and square-relative function of51, with complete finite checks recorded above. No all-n proof follows.

## Open items

Required Claude audit of Part2. All degree-seven finite predicates and required actual independent executions are complete; the all-degree corner-argmax target remains OPEN.

## History

2026-11-01, Codex /root/a5_develop, allocated gpt-6.1-sol xhigh; rules4bd1d65. Written as OPEN before finite evidence completion. Exact corner diagnostic uses direct native polynomial evaluation; an earlier slow scalar-symbolic diagnostic was terminated without producing a mathematical result.

2026-11-01 after13:33UTC: promoted to PROVED following the actual final different-executor developer-pair controls exit0, without changing any frozen scientific source or certificate. Required Claude audit remains PENDING.
