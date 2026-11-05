# PD-N?nn-mop-stability-codex-D4-03 — common changes preserve relative spectral data

ID kind: PD-N (provisional allocation).
Aliases: pointwise ratio obstruction; common Toda orbit; common Geronimus orbit.
Split from: D4-C2 universal easy-start solver.
Split into: none.

## Statement

Fix N>=2 support nodes and two nonzero weights at each node. Any finite sequence of common nonzero pointwise multipliers, with arbitrary separate nonzero rescalings of each measure, preserves all cross ratios

    I_(l,r)=w_(2,l) w_(1,r)/(w_(1,l) w_(2,r)).

Therefore a solver restricted to such changes from a fixed starting pair cannot reach all target positive pairs on the support. Common Christoffel factors, common Geronimus division without added masses, and common exponential Toda flow belong to this class. In particular a proportional starting pair cannot become a normal two-measure triangle by this mechanism.

## Definitions

A step has w'_(s,l)=alpha_s q_l w_(s,l), with q_l,alpha_s nonzero. Support remains fixed. Normality at (1,1) means independence of the two mass/first-moment rows.

## Assumptions

Only common factors and separate scalar normalizations. Weight-dependent factors, weight mixing, moving support, and added masses (including general Geronimus masses) are outside the result.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Invariant and failure of arbitrary-target reachability | PROVED | Cancellation proof |

Candidate / claim disposition: REJECTED.
Rejection reason: refuted, only arbitrary-target reachability from one fixed pair by the stated class.

## Negative-result scope

Attempted mechanism: D4-C2, generic easy-start solve using common spectral changes. Parameter range: fixed support N>=2, nonzero weights, any finite sequence in the defined class. Continuous common flow has the same invariant by its explicit weights.

## Depends on

Elementary weight algebra; PD-T286 only for interpreting proportional-pair nonnormality.

## Proof or evidence

Substitute the step into I: the two alpha factors and q_l q_r cancel. Induction proves invariance under finite composition. Since positive target pairs can have unequal I values, no fixed orbit contains all targets. If w2=beta w1 initially, the invariant keeps their pointwise ratio constant up to alpha2/alpha1; the two functionals remain proportional, so their (1,1) rows are dependent. Both equal starting measures thus already fail normality, and common changes cannot repair them.

For a concrete restricted-family interpretation, binomial/Krawtchouk weights at l=0,...,M have ratio proportional to [p2(1-p1)/(p1(1-p2))]^l. Common exp(t l) adds t to each logit and preserves their difference. It cannot change this relative parameter from a fixed distinct initial pair. No assertion about an independent-parameter deformation follows.

## Checks

Analytic proof; no experimental premise. Actual primary literature coverage and computation receipts are in adjacent D4 files. Independent review pending.

## Sources

No external theorem used. LIT-D4-01 common flow and LIT-D4-03 more general mass-adding transformations supply context only; the latter's added masses are explicitly excluded.

## Scope

This is an input reachability obstruction. It neither rules out useful transport within an orbit nor bounds floating arithmetic errors. It does not apply to a method allowed to select a different initial pair for every target; such a method still owes a usable source-array construction.

## Open items

Explicit local generators for independent weight changes and their conditioning.

## History

2026-11-05, Codex dispatched gpt-6.1-sol xhigh; source 823cf6a4, round 1. Common-transform arbitrary-target claim rejected, independent-weight route deferred.
