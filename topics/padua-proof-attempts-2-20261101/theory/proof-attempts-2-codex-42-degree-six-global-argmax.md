# PD-T?proof-attempts-2-codex-42 — Degree-six global Lebesgue maximum at the non-node corners

ID kind: PD-T.
Aliases: A4(d) n6; exact degree-six corner value; node/plateau value exclusion.
Split from: n6 finite-degree case of programme A4(d) / corner-argmax target.
Split into: none; n7/n8 and all-degree assertions retain separate statuses.

## Statement

For the degree-six even-checkerboard Padua function defined in41, put a=sqrt3 and b=2cos(pi/7). Its global maximum is

C=(15+8b+20b²+4a+4ab)/21,

attained exactly at(−1,−1) and(1,−1).

## Definitions

The precise field, board, cardinal ordering and physical coordinates are those of40–41. The global statement concerns all points, including non-strict local maxima and plateaus; it is not inferred from a strict-maxima list alone. FIELD coordinates of C are[5/7,8/21,20/21,4/21,4/21,0] in basis[1,b,b²,a,ab,ab²].

## Assumptions

A complete accepted count certificate plus separate exact value bounds: every flat/factor occurrence on its entire actual leaf, every accepted root enclosure, all node values and constant edge restrictions, and exact corner evaluations in the chosen embedding. Exact/outward arithmetic; separate checker and actual different-agent execution.

## Status by part

Overall status: **OPEN** pending final checker and actual different-agent execution of the complete count/value predicates.

| Mathematical part | Status | Evidence / remaining obligation |
|---|---|---|
| exact global value and complete argmax set | OPEN | full developer count/value files produced; independent full verification and rerun pending |

The analytic exclusion argument is written below, but the finite value predicates are not promoted before actual final checks. Required Claude audit remains pending.

## Depends on

40 for the specified real field;15 and18 for whole-leaf node/spatial/boundary predicates; the complete n6 certificate of41. The cardinal construction follows `PD-T?proof-attempts-codex-01 (audit pending)` with the dated accepted-audit/disposition qualification in41; direct784 node checks independently identify the implemented n6 cardinal family.

## Checks

Developer actually completed:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n6_global.py topics/padua-proof-attempts-2-20261101/outputs/a5_n6_certificate.json.gz --output topics/padua-proof-attempts-2-20261101/outputs/a5_n6_global.json
```

Code SHA256 `ab1e287b4a152975aec91056aa5326fdddb294394eecee5d5725770e1e89dcda`. Output7077bytes,SHA256 `af21a0a8f3d1e4301c3a249b6683ce61ce14436e7a2e96e71773b275a8563170`, bound to count gzipSHA256 `c7a113b9b623c47309fd186c19ee2dddb2d5a0270c01b118bd11ee1ee069f0f5`. Python3.12.14,SymPy1.14.0,python-flint0.9.0/FLINT3.6.0,112-bit outward fixed dyadics, no random seed.

Observed developer predicates: all54 flat leaf occurrences have signed-polynomial upper bound at most

8526311743724763702119888371493549 / 5192296858534827628530496329220096 < 5;

all25 interior root boxes and all14 edge root intervals have value upper endpoint below5; both non-node corners have exact FIELD valueC>5; node corners have value1. No factor or regular-point disposition occurs in this particular count certificate. Node-cone leaves require no mask-value enumeration:15 gives radial ascent away from their exact value1 nodes. Every bound must still be accepted by the separate checker and actually rerun by a different agent.

## Sources

Programme OPEN_TARGETS A4(d) and corner-argmax target at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. No general corner conjecture, numerical search or literature count is imported as proof. No novelty/priority claim.

## Proof or evidence

Exact corner evaluation gives λ_6(−1,−1)=λ_6(1,−1)=C. Since a>1 and b>9/5, the displayed positive-coefficient expression gives C>527/105>5. Thus the continuous function on the compact square has global maximum at leastC.

Suppose an interior point z is global and s is active there. Then P_s(w)≤λ_6(w)≤λ_6(z)=P_s(z), so P_s has a possibly non-strict local maximum atz. In an ordinary certificate leaf, a gradient exclusion or strict positive-curvature/negative-determinant Hessian exclusion is valid for non-strict maxima too. A root predicate identifies every stationary point of that pattern in the leaf with its uniquely enclosed root, whose λ value is below5. A flat occurrence is not automatically excluded from non-strict maximality, but its independently bounded P_s(Q)<5 contradicts P_s(z)=λ_6(z)≥C. These are all ordinary predicates used by this certificate. A node-cone leaf contains no non-node local maximum of any strictness by the positive radial derivative of15; its node has value1. Hence no interior global maximum is missed through a ridge, singular critical point or plateau.

On an open edge, the exact multiplicity-one cover makes each arrangement zero a regular tangent cardinal zero, excluding even non-strict maximality. Elsewhere the complete sampled-sign and residual derivative-root certificate applies. Its derivative/sign/outside/minimum exclusions are valid necessary-condition failures for non-strict maxima. An accepted tangential maximum with positive inward derivative would have an ascending feasible direction; an accepted edge maximum has value below5. Every constant edge signed polynomial is±1 by evaluation at an interpolation node on that edge. No zero-normal or tangent-degenerate case is unresolved in the accepted artifact. Thus no open-edge global maximum remains.

The other corners are exact interpolation nodes of value1. Therefore only the two displayed non-node corners can attain the global maximum, and both do, at valueC. This proof uses the complete count/value predicates and does not extend a cubic nonsingularity or null-line lemma to degree six. ∎

## Scope

Exactly n6, conditioned at development stage on the finite predicates actually passing. No all-degree corner theorem, neighbourhood expansion or n7/n8 global conclusion follows. The final status remains OPEN until those checks complete.

## Open items

Final separate full count/value checker, actual different-agent producer/global/checker execution and receipts; required Claude audit. Preserve every failed bound or unresolved candidate rather than inferring global maximality from the strict list alone.

## History

2026-11-01, Codex `/root/a5_n4` assignedn6, inherited gpt-6.1-sol xhigh; rules842dfaaeff524b4db4141d314afff6ad4a5b7721. Full developer values completed11:00UTC. Initial statusOPEN preserves the pending finite verification obligations; no source correction is claimed before certification.
