# PD-T?proof-attempts-2-codex-52 — Degree-seven global Padua argmax

ID kind: PD-T.
Aliases: A4(d) n=7; value certificate with node leaves; plateau exclusion.
Split from: finite-degree corollary of programme corner-argmax target.
Split into: none; all-n corner argmax remains OPEN.

## Statement

Target: prove that lambda_7 attains its global maximum exactly at(−1,−1),(−1,1), with value C given by result50's FIELD12 vector

[83/28,−5/7,−4/7,2/7,−2/7,0,2/7,0,−2/7,1/7,2/7,0].

Equivalently,28C=83−20b−16b²+8b³−8a+8ab²−8a²+4a²b+8a²b², where a=2cos(pi/7),b=2cos(pi/8). Only the exact corner evaluation has been executed; no global conclusion is asserted until all finite predicates pass.

## Definitions

Use results15/18/50/51. An exceptional ordinary-leaf occurrence is a compatible pattern disposition flat or factor: those exclude a strict maximum but can admit a non-strict stationary ridge. Every occurrence requires its own whole-leaf value bound.

## Assumptions

A complete accepted degree-seven count certificate, plus independently verified exact fields proving every exceptional occurrence and every accepted interior/open-edge root has value below11/2; every constant edge restriction equals±1; nodes have value1; both non-node corners have exact common value C>11/2. The separate value artifact is bound to the raw count artifact SHA256. No numerical list or agreement is a premise.

## Status by part

Overall status: **OPEN**. The drafted conditional argument below requires the complete finite certificate/global bounds and independent executions, all pending. Required Claude audit remains PENDING.

| Part | Current status |
|---|---|
| exact common corner value and C>11/2 | actual exact developer diagnostic; independent check pending |
| non-strict-global-maximum case argument | conditional draft; all finite value checks pending |
| all exceptional/root/constant-edge bounds | OPEN finite checks |
| corner-only argmax | OPEN |

## Depends on

Results15,18,50,53 and a complete accepted51 certificate. Strict-count completeness alone is insufficient, so exceptional values are an additional obligation.

## Checks

New producer a5_n7_global.py; schema a5_n7_schema.md. Exact native corner diagnostic is outputs/a5_n7_corner-diagnostic.json. The separate checker must reconstruct C and all additional bounds itself. Actual full commands, hashes and completed execution status belong to T-A5-n7.md and the final independent execution record.

## Sources

Registered A4(d) finite-case corollary reached while solving A5, programme source05/source06 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. No all-degree claim or novelty assertion.

## Proof or evidence

Continuity gives at least one global maximum. The exact corner value C>11/2 excludes nodes and every candidate whose certified value is below11/2.

Suppose a global maximum z is interior. Every active signed polynomial P_s has a non-strict local maximum there, so its gradient vanishes and Hessian is negative semidefinite. Select any leaf containing z and any active compatible mask. A node leaf excludes any non-node local maximum by strict radial ascent; the node itself has value1. In an ordinary leaf, the uniform-gradient53 predicate, derivative and strictly wrong-curvature predicates exclude non-strict maxima as well. A regular-point injection identifies z with an exact node or an impossible regular-zero local maximum (or a boundary point, impossible for interior z). A root reference and whole-hull injection identify z with the accepted root, whose value is below11/2. A flat/factor occurrence is bounded below11/2 on the entire leaf by the separate value artifact. Thus no interior point can attain C.

On an open edge, regular-crease points are excluded by tangent sign flipping, and all noncrease patterns and all reduced derivative roots are covered by18. A constant edge restriction equals±1; otherwise the exact derivative/sign/strict-positive-curvature/positive-inward tests exclude non-strict maxima, or the candidate is an accepted root with value below11/2. No unresolved zero-curvature or zero-normal case is assumed away. Hence no open-edge point attains C.

The remaining four corners have exactly computed values: the two node corners have1, the two non-node corners both C. If the complete additional finite predicates pass, precisely those two corners are global maximizers. This argument does not infer global completeness from a strict-maxima list. ∎

## Scope

Only degree7, conditional on the complete finite checks recorded above. No all-n proof follows.

## Open items

Complete51 certificate and every additional finite value predicate, independent verifier and actual different-agent full execution, required Claude audit.

## History

2026-11-01, Codex /root/a5_develop, allocated gpt-6.1-sol xhigh; rules4bd1d65. Written as OPEN before finite evidence completion. Exact corner diagnostic uses direct native polynomial evaluation; an earlier slow scalar-symbolic diagnostic was terminated without producing a mathematical result.
