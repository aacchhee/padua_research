# PD-T?proof-attempts-2-codex-62 — Degree-eight global corner maximum

ID kind: PD-T.
Aliases: A4(d) n=8; non-strict stationary-plateau value coverage.
Split from: finite-degree corollary of the n8 A5 certificate.
Split into: strict-local count61 and field support60 are separate results.

## Statement

Target: for degree8, max_{[-1,1]²}λ_8 equals the common value at(−1,−1),(1,−1), attained only at these two non-node corners.

## Definitions

The cardinals, physical embedding and complete count-certificate conventions of60/61. An exceptional occurrence is one ordinary compatible leaf-mask record excluded by flatness or a regular common-gradient factor; these can admit non-strict stationary ridges and therefore need explicit value bounds.

## Assumptions

A complete independently accepted count certificate, plus exact corner values and outward upper bounds for every accepted interior/edge root, every exceptional occurrence on its whole leaf, every edgeconstant value and node value1. A rational cut must lie strictly between all noncorner upper bounds and the exact non-node corner lower bound. No conclusion is inferred from a list of strict maxima alone.

## Status by part

Overall status: **OPEN**.

| Target part | Status | Outstanding obligation |
|---|---|---|
| the finite n8 global argmax assertion | OPEN | complete61 and separately verified value artifact |

Required Claude audit pending. No root/corner numerical estimate is promoted to proof.

## Depends on

60/61, generic15/18 and universal-gradient53. A1 dependency is named literally `PD-T?proof-attempts-codex-01 (audit pending)` where used; independent finite cardinal reconstruction is still required. The source's all-degree A4 remains OPEN regardless of this finite case.

## Checks

New optional producer `../code/a5_n8_global.py` is prepared but unexecuted. It computes all value enclosures first, then chooses an exact rational cut between their largest upper bound (including1) and the exact corner lower bound; it must fail if they overlap. An independent checker must replay every bound and the entire occurrence census; its output cannot be trusted merely because the producer reports complete.

## Sources

Programme A4/A5 and the current gate in `../attempts/T-A5-n8.md`. No novelty or priority claim; no published comparison is certified at this checkpoint.

## Proof or evidence

Once a valid count and value certificate exists, continuity gives an attained global maximum. If it were interior, every active signed polynomial would have a weak local maximum there, hence zero gradient and negative semidefinite Hessian. A direct53 leaf excludes even weak local maxima. A node leaf excludes all non-node maxima by strict radial ascent; the node has value1 below the corner. Ordinary derivative/wrong-curvature predicates exclude necessary maximality; whole-hull injectivity identifies a surviving stationary point with a verified root, node or regular zero. Regular zero-cardinal points cannot be λ maxima by the active-gradient flip argument. Every root and every flat/factor occurrence has its separately checked value below the cut.

On an open edge, regular crease points are excluded by tangent active-sign flips; every noncrease stationary candidate is covered by the complete edge arrangement/derivative certificate. Accepted tangent roots have separately bounded values and flat edge patterns have exact values below the cut. Strictly positive inward derivative excludes a relative maximum; unsupported zero-normal cases must not exist in an accepted certificate. Finally the two other corners are nodes, while the two stated non-node corners have equal exact value above the cut. This proves the target only after all finite obligations are verified; they remain OPEN here.

## Scope

Degree8 only. No all-degree neighbourhood/global estimate and no conclusion from a strict count without non-strict plateau bounds.

## Open items

Complete61; run the value producer and independent checker; actual different-agent execution and required Claude audit.

## History

2026-11-01, Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh. Written OPEN, separately from61, before any global-value run. The universal53 leaf's weak-maximum exclusion is stated explicitly rather than inferred from a strict count.
