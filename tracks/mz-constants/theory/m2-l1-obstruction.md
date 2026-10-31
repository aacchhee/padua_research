# PD-N005 — absolute-cardinal column domination fails

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-N.
Aliases: endpoint cardinal L1 obstruction.
Split from: the naive absolute-cardinal Cauchy route considered during M2 round 1.
Split into: none.

## Statement

For each N≥2, ∫[-1,1]|ℓ_0(x)| dx=1/N. Consequently there is no constant C independent of N such that ∫|ℓ_k|≤C(1+log N)w_k for all CC cardinal functions and all N.

## Definitions

The node and cardinal conventions of PD-T017.

## Assumptions

All integers N≥2, unnormalized Lebesgue measure.

## Status by part

Overall status: PROVED (development; audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact endpoint absolute integral and obstruction | PROVED | Direct trigonometric integration |

Candidate / claim disposition: IDEA-069 REJECTED: failed.
Rejection reason: failed for this specific column-domination mechanism, not for the lower-bound target.

## Negative-result scope (PD-N only)

Attempted mechanism: combine the ordinary Lebesgue constant with uniform logarithmic domination of the cardinal L1 columns by CC weights.
Parameter range: all N≥2; the endpoint k=0 alone obstructs the claimed uniform column estimate.

## Depends on

Only the explicit cardinal formula and endpoint weights in PD-T017.

## Checks

Analytic; no computational dependency. Rules/base d36722823441dc40c6e19d69a174459348dd309c. Independent proof audit needed.

## Sources

No external claim used. This was a local failed mechanism.

## Proof or evidence

The endpoint cardinal formula yields

    ∫|ℓ_0|dx=(1/(2N))∫_0^π(1+cosθ)|sin(Nθ)|dθ.

Reflection θ↦π−θ makes the cosine term zero. The remaining absolute sine integral equals 2, since it consists of N equal half-waves. The result is 1/N. Its ratio to w_0 is N for odd N and (N²−1)/N for even N. This grows faster than 1+log N.

## Scope

Only the stated absolute-cardinal L1 column route fails. The weighted cell Schur argument of PD-T017 escapes this assumption.

## Open items

Independent acceptance; no broader negative statement proposed.

## History

2026-10-31, Codex subagent, gpt-6.1-sol xhigh (explicit orchestrator assignment). Preserved rather than silently discarded when the weighted-cell mechanism replaced it.
