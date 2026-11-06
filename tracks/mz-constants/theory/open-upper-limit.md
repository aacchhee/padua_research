# PD-T027 — sharp endpoint upper spectrum

ID kind: PD-T. Aliases: 1.004437 limit; uniform endpoint upper gap.
Split from: M1 supplied strengthened target beyond the strict threshold.
Split into: [PD-T526](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-uniform-upper.md) (uniform-gap conjunct) and [PD-T530](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-qualitative-limit.md) (existence and exact operator identification of the sharp limit). The decimal-value conjunct remains OPEN. [PD-T014](m1-upper-bound.md) remains supporting strict-threshold background.

## Statement

For the Lebesgue CC rule at N+1 Lobatto nodes, determine whether λ_max(G_(N,N−1)) converges, identify its exact limit if it does, and prove a uniform constant B<2 independent of N. The supplied decimal near 1.004437 is a numerical lead, not an exact proposed value.

## Definitions and assumptions

N≥2; continuous Legendre orthonormal basis through degree N−1; Gram matrix of Q_N. Measure and normalization are those of the track README.

## Status by part

Overall status: PARTIAL.

| Mathematical part of the original target | Status | Split result / remaining gap |
|---|---|---|
| Uniform constant B<2 independent of N | PROVED | [PD-T526](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-uniform-upper.md) gives B=5/3 for every N>=2 |
| Convergence and exact limit identification as Lambda_edge | PROVED | [PD-T530](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-qualitative-limit.md), through all N and both parities |
| Decimal evaluation of Lambda_edge | OPEN | [PD-T547](../../../topics/padua-mz-sharp-constants-20261106/theory/P4-certified-lower.md) is one-sided only; no certified two-sided decimal value |

Candidate disposition: retained sharpening; no rejection. This is an explicit PROVED-plus-OPEN decomposition of the original target's own statement.

## Depends on

[PD-T526](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-uniform-upper.md), [PD-T530](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-qualitative-limit.md), with [PD-T527](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-eta-deficit.md), [PD-T528](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-endpoint-model.md), [PD-T529](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-fixed-trial-limit.md), [PD-T531](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-finite-certificate.md), [PD-T548](../../../topics/padua-mz-sharp-constants-20261106/theory/P4-denominator-closed-form.md) as the linked definitions and supporting results. [PD-T547](../../../topics/padua-mz-sharp-constants-20261106/theory/P4-certified-lower.md) proves only Lambda_edge>=1.0044369. PD-T014/022 remain background; PD-T026 and [PD-T532](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-measured.md) are finite MEASURED leads.

## Checks and sources

[audit-01](../../../topics/padua-mz-sharp-constants-20261106/audit-01.md), [audit-02](../../../topics/padua-mz-sharp-constants-20261106/audit-02.md) and [audit-03](../../../topics/padua-mz-sharp-constants-20261106/audit-03.md) accept the linked results at their stated scopes. No new run or literature claim is made here.

## Proof or evidence

[PD-T526](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-uniform-upper.md) supplies the uniform gap 2−lambda_max>=1/3; the earlier N^−1 gap description is superseded. [PD-T530](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-qualitative-limit.md) proves convergence to the frozen variational norm Lambda_edge, and [PD-T531](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-finite-certificate.md) supplies a computable vanishing finite-to-limit error. [PD-T527](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-eta-deficit.md) establishes the reciprocal-log-squared order of 1−eta. These split proofs do not give a certified decimal value.

## Scope and open items

The original statement and all-N quantifiers are unchanged. Decimal evaluation of Lambda_edge remains OPEN; the proved operator characterization and one-sided lower bound do not resolve that obligation.

## History

2026-10-31, Codex orchestrator, runtime metadata unexposed: preserves the supplied sharp strengthening as a distinct OPEN target rather than silently dropping it after the strict theorem.

2026-10-31, audit-01 P4 response, Codex gpt-6.1-sol xhigh (explicit assignment), rules `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`: named the reciprocal PD-T014 link and PD-T022 background by ID; clarified supporting-target separation rather than a proved portion of the present statement. The original target and OPEN status are unchanged.

2026-11-06: Original Statement preserved verbatim. The uniform-gap and limit-existence/operator-identification conjuncts are PROVED under [PD-T526](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-uniform-upper.md), [PD-T530](../../../topics/padua-mz-sharp-constants-20261106/theory/S2-qualitative-limit.md); the decimal-value conjunct remains OPEN. Overall status OPEN → PARTIAL. PD-T014 was and remains supporting background. See [canonical decision](../../../topics/padua-mz-sharp-constants-20261106/LOG.md).
