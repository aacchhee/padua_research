# PD-T020 — sharp endpoint leading constant

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T.
Aliases: limit of logarithm-squared minimum eigenvalue.
Split from: the original M2 request for endpoint order with an explicit constant if possible.
Split into: proved comparison estimates PD-T017 and PD-T018; they do not settle this sharper statement.

## Statement

Determine whether there exists c_*∈(0,∞) such that

    lim_(N→∞)(log N)² λ_min(CC,N−1)=c_*,

and, if the limit exists, determine c_* explicitly.

## Definitions

CC nodes, weights, measure and degree convention as in PD-T017. Natural logarithm.

## Assumptions

All integers N≥2; no restriction to one parity or a selected subsequence.

## Status by part

Overall status: OPEN.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Limit exists and can be identified | OPEN | Comparison bounds do not prove convergence or identify an extremizer |

Candidate / claim disposition: deferred; no rejection. This target is retained explicitly and no new mechanism is launched.

## Depends on

The precise definitions only. PD-T017 and PD-T018 supply positive finite comparison bounds but are supporting results, not proved cases of the limit statement.

## Checks

No new run is claimed. Supplied finite eigenvalue tables are provenance reports only; harmonic-witness diagnostics in the M2 log are not eigenvalue asymptotics.

## Sources

Incomplete historical interpolation and matrix screen documented in topic literature-search.md; no novelty claim.

## Proof or evidence

No proof of this statement. The two comparison theorems show the scaled quantities are bounded away from zero and infinity (after harmless conversion of 1+log N to log N), which alone leaves both convergence and the exact value unresolved.

## Scope

Separate sharper target; it does not weaken the independently PROVED comparison-order theorems.

## Open items

After independent acceptance of the order theorem and literature comparison, decide whether a sharper rescaled limiting operator is a justified later direction. No such exploration is undertaken here.

## History

2026-10-31, Codex gpt-6.1-sol xhigh (explicit orchestrator assignment), rules/base d36722823441dc40c6e19d69a174459348dd309c. Split to preserve the unanswered meaning of an exact leading constant while keeping proved nonsharp comparisons separate.
