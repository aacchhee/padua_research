# PD-T020 — sharp endpoint leading constant

ID kind: PD-T.
Aliases: limit of logarithm-squared minimum eigenvalue.
Split from: the original M2 request for endpoint order with an explicit constant if possible.
Split into: [PD-T546](../../../topics/padua-mz-sharp-constants-20261106/theory/P3-reverse-bound.md), [PD-T523](../../../topics/padua-mz-sharp-constants-20261106/theory/S1-sharp-one-sided.md) settle the unchanged sharp limit; PD-T017 and PD-T018 remain separate comparison estimates.

## Statement

Determine whether there exists c_*∈(0,∞) such that

    lim_(N→∞)(log N)² λ_min(CC,N−1)=c_*,

and, if the limit exists, determine c_* explicitly.

## Definitions

CC nodes, weights, measure and degree convention as in PD-T017. Natural logarithm.

## Assumptions

All integers N≥2; no restriction to one parity or a selected subsequence.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Limit exists over all integers N, hence both parities | PROVED | [PD-T546](../../../topics/padua-mz-sharp-constants-20261106/theory/P3-reverse-bound.md) with the matching one-sided result [PD-T523](../../../topics/padua-mz-sharp-constants-20261106/theory/S1-sharp-one-sided.md) |
| Exact value c_*=pi⁴/8 | PROVED | The same sharp limit theorem |

Candidate / claim disposition: resolved at the original statement's full scope.

## Depends on

[PD-T546](../../../topics/padua-mz-sharp-constants-20261106/theory/P3-reverse-bound.md), [PD-T523](../../../topics/padua-mz-sharp-constants-20261106/theory/S1-sharp-one-sided.md). Their own files carry the proofs and dependencies. PD-T017 and PD-T018 remain supporting comparison results.

## Checks

The sharp limit is accepted in [audit-02](../../../topics/padua-mz-sharp-constants-20261106/audit-02.md). No new computation is claimed by this target record.

## Sources

Incomplete historical interpolation and matrix screen documented in topic literature-search.md; no novelty claim.

## Proof or evidence

The reverse all-input interpolation estimate in [PD-T546](../../../topics/padua-mz-sharp-constants-20261106/theory/P3-reverse-bound.md) gives the liminf pi⁴/8. The admissible degree-(N−1) trial in [PD-T523](../../../topics/padua-mz-sharp-constants-20261106/theory/S1-sharp-one-sided.md) gives the matching limsup through all N. The split records contain the substantive proofs; none is duplicated here.

## Scope

Separate sharper target; it does not weaken the independently PROVED comparison-order theorems.

## Open items

No unresolved part remains in the original target. Practical finite-N rates are outside its statement.

## History

2026-10-31, Codex gpt-6.1-sol xhigh (explicit orchestrator assignment), rules/base d36722823441dc40c6e19d69a174459348dd309c. Split to preserve the unanswered meaning of an exact leading constant while keeping proved nonsharp comparisons separate.

2026-11-06: Original Statement preserved verbatim. Its existence and explicit-value obligations are both resolved by [PD-T546](../../../topics/padua-mz-sharp-constants-20261106/theory/P3-reverse-bound.md), [PD-T523](../../../topics/padua-mz-sharp-constants-20261106/theory/S1-sharp-one-sided.md). Overall status OPEN → PROVED; earlier comparison-only limitations describe the prior state. See [canonical decision](../../../topics/padua-mz-sharp-constants-20261106/LOG.md).

2026-11-06 (readiness-01 fix R2): the removed header note read “Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md.” Its pending-audit wording is superseded by the completed audits linked in PROOF_STATUS.md.
