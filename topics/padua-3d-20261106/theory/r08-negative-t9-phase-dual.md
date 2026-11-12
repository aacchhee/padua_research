# PD-N?padua-3d-20261106-codex-T9-r06-01 — translated positive cubature does not force the unshifted short-dual threshold

ID kind: PD-N.
Aliases: T9-R06-PB; phased Gauss tensor counterexample.
Split from: PD-T?padua-3d-20261106-codex-T9-r06-02, t9-r06-phase-weight-boundaries.md section “A phase destroys…”; this record gives an already named claim its own durable home.
Split into: none. Provisional ID retained; no final allocation or shared crosswalk edit.

## Statement

For every integer q>=2 there is a finite subgroup H and phase a such that the positive Haar pushforward on X=cos(a+H) is exact on Pi_(2q-1), although the shortest nonzero l1 vector of its annihilator is q<2q. Thus the unshifted implication “degree-(2n-1) positive cosine cubature forces dual minimum>=2n” is false if arbitrary phases are added.

## Definitions

H is a finite subgroup of (R/(2pi Z))^3, L its annihilator in Z^3, a a phase in radians, X=cos(a+H) coordinatewise, and mu is normalized product Chebyshev measure. Pi_n means total degree<=n.

## Assumptions

q=n>=2; take H=(2pi/q Z)^3 modulo2pi and a=(pi/(2q),pi/(2q),pi/(2q)); equal positive Haar weights pushed to the q^3 distinct cosine nodes.

## Status by part

Overall status: **PROVED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Failure of the phase-blind short-dual implication for every q>=2 | PROVED | Explicit positive tensor rule and exact character averages |

Candidate / claim disposition: **REJECTED: refuted** for the phase-blind implication only. Rejection reason: refuted — explicit all-q counterexample.

## Negative-result scope

Attempted mechanism: apply the unshifted Haar shortest-dual criterion unchanged to translated positive rules. Parameter range: all q=n>=2 in this explicit tensor family. This does not refute a translated-rule cardinality obstruction under additional hypotheses.

## Depends on

Elementary finite character averaging, no external theorem. The unshifted positive-weight lemma PD-T?padua-3d-20261106-codex-T9-r06-02 remains valid within its actual zero-phase hypotheses.

## Checks

No new numerical or optimizer run by this response worker. The local proof was read and reconstructed from the old combined body. [Audit03/T9](../audit-03/T9.md) independently accepted these scoped statements; [independent-checks-round06](../independent-checks-round06.md) records supplementary checks. The exact-algebra controls are [t9-r06-exact.json](../evidence/t9-r06-exact.json), with source/command identities in the old receipt manifest. Reading a historical output is not a new independent execution.

## Sources

[Round08 gate/source supplement](../novelty-gate-supplement-round08.md) records the actual predecessor bodies, source aliases and limits. External source dependencies appear explicitly below; no cited proof is inherited by citation.

## Proof or evidence

In one dimension the numbers cos(pi/(2q)+2pi*j/q),0<=j<q, are distinct: a reflected equality would require 1+2(j+l) to be divisible by2q, impossible by parity. They are roots of T_q because q times every angle is pi/2 modulo2pi. For1<=m<=2q-1, the average cos(m theta) vanishes unless q divides m; the only remaining m=q gives cos(q*pi/(2q))=0. Thus the equal positive weights are exact in one variable through degree2q-1. Tensoring proves total-degree exactness through2q-1. Its annihilator is q Z^3, of shortest l1 norm q.

This does not yield a Pi_q-unisolvent minimal set: T_q(x1) is a nonzero degree-q annihilator of the tensor nodes. In particular q=2 gives8<dim Pi_2=10, so the old blanket phrase “q^3 exceeds the minimal cardinality” must not be used. The non-unisolvence argument is valid for every q>=2 and is the appropriate limitation.

## Scope and D3

D3: this disproves extending a zero-phase criterion to arbitrary phases; the standard unshifted two-dimensional Padua representation still has dual minimum2n. The example does not exclude Padua or any fixed well-conditioned minimal phase sequence.

## Open items

Sharp translated positive-rule density/cardinality bounds remain OPEN. No count-only contradiction is inferred from this rank-deficient tensor example.

## History

2026-11-06 — Codex records worker, assigned gpt-6.1-sol xhigh; runtime metadata not independently exposed. Rules/input `9042e1c42964150f30fdbe8563c12ba6c6a8692a`. Response08 completes audit03 novelty m2/m3 by splitting already named statements from combined bodies. Statements/statuses are retained; E4's source-label criterion belongs to root and AC. Old pinned bodies are unchanged by this worker.
