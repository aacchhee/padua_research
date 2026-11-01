# PD-T?proof-attempts-2-codex-17 — Degree-five global Padua argmax

ID kind: PD-T.
Aliases: A4(d) n=5; value certificate with node-cone leaves; non-strict plateau exclusion.
Split from: the degree-five finite case of `PD-T?programme-ideas-claude-05`, A4(d).
Split into: none; the all-n conjecture remains OPEN.

## Statement

For the degree-five board defined in result16, the certified statement is

max_{[−1,1]²} λ_5=(38+8sqrt3+10sqrt5)/15,

with equality exactly at(−1,−1) and(−1,1). The complete count and additional value fields passed the separate independent checker and actual different-agent producer/checker execution.

## Definitions

Use the physical coordinates, cardinals, compatible masks and node-cone leaves of results15,16,18. An exceptional ordinary-leaf occurrence here means a compatible P_s disposition of type`flat` or`factor`, which excludes a strict maximum but can admit a non-strict stationary ridge. Each such occurrence needs a separate value bound for the global argument.

## Assumptions

A complete accepted degree-five count certificate, plus exact additional fields proving:

- every exceptional flat/factor occurrence has P_s(Q)<19/4 on its entire leaf;
- every accepted interior and open-edge root has a rigorous value enclosure below19/4;
- every constant edge restriction equals±1;
- both non-node corners have the exact value C=(38+8sqrt3+10sqrt5)/15>19/4, while the other corners are exact nodes of value1.

These are finite obligations to be verified, not assumptions inherited from a numerical fit or the source count.

## Status by part

Overall status: **PROVED** (written non-strict-global-maximum argument, complete exact value evidence and actual independent producer/global/checker executions).

The global conclusion does not follow from a strict list alone. The proof explicitly treats node leaves and flat/factor ridges. Every additional finite predicate passed independently on both the developer and independently regenerated artifact pairs. Required Claude audit of Part2 remains **PENDING**.

## Depends on

- Result15: positive radial ascent on accepted node rectangles, except at the exact node of value1.
- Result18: complete degree-independent spatial/edge/corner certificate implication and its individual predicate proofs.
- Result16: actual complete degree-five count artifact and separate verification, when finished.

No cubic or quartic singular-Hessian classification is used. All n3/n4 files are frozen.

## Checks

The new value producer `../code/a5_n5_global.py` and separate `a5_checker_n5.py --global-file` verify the `a5-n5-global-v1` evidence. Full actual commands, frozen source hashes and independent receipts are recorded in result16 and `../independent-execution-a5-n5.md`.

Developer count gzip:125245bytes, SHA256 `a1238d59781733cc0d380dc513a0a642d0e24b985aeb9b90bb7233756273386e`. Developer global JSON:3897bytes, SHA256 `57a7c9c12667b5d441cea4fc60a68563cc1accc8d8adc8ca41ccd339fa16f17d`. A different subagent actually regenerated the full count and global evidence, then checked both its own pair and the developer pair. Both exited0 with `count_certified`, `global_argmax_verified`, `global_no_nonstrict_plateau_above_cut` and `node_leaf_global_exclusion_verified` true. Own-pair checker299.016661s; developer-pair checker257.679985s. The separate checker implementer's full run also passed. All27 negative controls were rejected and all4 positive controls accepted.

The certificate verifies every one of the4 exceptional flat/factor occurrences with common upper bound

15008010243903610701266445927/9903520314283042199192993792 <19/4.

It separately encloses every one of the14 interior and9 edge root values below19/4. All21 node rectangles have the exact radial exclusion and node value1. Constant edge restrictions, if present, must be±1; none occurs among this artifact's actual edge masks. Exact evaluation at both non-node corners gives field coefficients[38/15,8/15,2/3,0], i.e. the stated C. Each corner lower bound is strictly above19/4. Every source/output identity and code pin is preserved in the evidence manifest and actual execution records. No numerical fit supplies a proof predicate.

## Sources

Programme A4(d), THEORY-05 and A5 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. This is one finite-degree case, not the all-n theorem. The bounded observed corner gap is motivation only. No literature priority claim.

## Proof or evidence

Let C be the stated corner value. The identity for C is one of the finite exact cardinal checks. Its strict separation from19/4 is also elementary: sqrt3>5/3 and sqrt5>11/5 by rational squaring, giving C>44/9>19/4. Compactness gives a global maximum M≥C.

### Interior global maxima, including non-strict ones

At any interior global maximum z, every active signed polynomial P_s has a non-strict local maximum at z, because P_s≤λ and equality holds there. Therefore ∇P_s(z)=0 and H_s(z) is negative semidefinite.

If z belongs to a node-cone leaf, result15 gives a feasible ascending radial direction unless z is the exact node. At that node λ=1<C. Hence no global maximum is in a node leaf.

Otherwise choose an ordinary leaf containing z and any active compatible mask. Completeness ensures its disposition is present. A derivative interval excluding0 or a strictly positive second direction/negative Hessian determinant contradicts necessary maximality. A regular-point witness identifies the only possible stationary point on the entire leaf: an interior regular zero cardinal excludes even a non-strict λ maximum by the active-gradient flip argument, while a node has value1<C. An exact witness on the square boundary cannot equal the interior candidate.

A flat or regular-factor disposition alone would not exclude a non-strict ridge. This is why the additional certificate bounds P_s on the entire leaf strictly below19/4. Since P_s(z)=λ(z)≥C, that bound excludes both exceptional types from global maximality.

A root disposition identifies the only stationary point on the leaf with its accepted strict λ maximum, by injectivity on a convex hull containing the whole leaf and root box. Its independently verified value enclosure is below19/4<C. Thus no interior point attains the global maximum, regardless of whether it was initially assumed strict.

### Open-edge global maxima

At an open-edge global maximum, every active restricted polynomial q_s has a non-strict one-dimensional local maximum. A constant restriction is±1 because the edge contains an interpolation node and each signed cardinal sum evaluates to±1 there. Thus a constant cannot be active at valueM≥C>1.

For a nonconstant restriction, its derivative is zero. A regular edge-cardinal zero is excluded exactly by active tangent-gradient flips; every other derivative candidate is included in the complete arrangement/norm-root certificate. The derivative and sign exclusions contradict activity/stationarity, and a strictly positive q_s'' contradicts local maximality. A strictly positive inward derivative also supplies an ascending feasible direction. No zero-curvature or zero-normal candidate is assumed away: completeness requires an actual valid disposition. Every remaining accepted root has negative tangent curvature, strict signs and negative inward derivative, hence is a strict relative maximum. Its separate value enclosure is below19/4<C. Therefore no open-edge point is global.

### Corners and equality set

The continuous function λ attains its maximum somewhere on the closed square. The two node corners have value1, and every interior/open-edge point was excluded. Exact cardinal evaluation gives C at each of the remaining corners(−1,±1). Thus the maximum is C and these are exactly its equality points. ∎

## Scope

Only the degree-five case. Additional exceptional-leaf value bounds are essential; a strict-list-only argument would leave non-strict plateaus uncovered. The proof is degree-independent once the stated predicates are verified, but no higher-degree finite result is asserted here.

## Open items

This degree-five finite case is complete. Required Claude audit remains PENDING. Other finite degrees and the all-n corner-argmax conjecture require separate proofs and evidence.

## History

2026-11-01, Codex `/root/a5_develop`, allocated gpt-6.1-sol xhigh. Initially OPEN during the exact finite runs; promoted to PROVED after matching developer/independent count and global pairs, full separate verifier and controls passed. The proof treats node-cone and exceptional-leaf cases explicitly, repairing the non-strict-maximum gap. Administrative rule changes did not affect frozen mathematics. Required Claude audit remains PENDING.
