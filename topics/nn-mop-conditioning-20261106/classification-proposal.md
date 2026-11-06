# PD-T448 classification proposal — audit-01 MAJOR-1

2026-11-06 · Codex, requested gpt-6.1-sol high · rules/source
3d5b29d7aa8c1274793139d7040695035e1bda22.

**Decision proposed for reviewed PR preparation: PARTIAL.** This file
records the material classification decision for focused re-audit. It
assigns no final ID and does not change the predecessor file or a shared
registry. The currently registered OPEN status is therefore unchanged
until the audited proposal is applied.

## Original wording retained

PD-T448, `topics/nn-mop-stability-20261105/theory/conditioning-growth-target.md`,
Statement and definitions, says:

> For the exact Krawtchouk and Hahn input families of handoff01/PD-T290,
> with N common nodes z_k=2k/(N-1)-1 and the induced condition kappa_N
> defined in conditioning-local.md, determine matching all-N growth bounds
> with explicit useful constants and a sharp exponential rate if one exists.
> In particular determine liminf and limsup of kappa_N^(1/N), whether they
> are equal and finite, and the required subexponential factors. A usable
> digit-loss expression must state its input/output norms and finite-perturbation
> radius; it cannot predict every algorithm's actual rounding error.

No wording or input/output convention is narrowed by this proposal.

## Decomposition of the target's own content

| Direct target part | Proposed status | Durable home / remaining obligation |
|---|---|---|
| Exact benchmark Krawtchouk: determine liminf and limsup, their equality and finite value | PROVED | PD-T?nn-mop-cond-codex-C2-hard-01, [sharp upper](theory/c2-sharp-upper.md), together with PD-T437; both limits are 5+2sqrt(6) |
| Krawtchouk: determine the required subexponential factors and useful sharp constants | OPEN | Current lower polynomial factor and loose upper 3,000,000 N^13 do not determine a matching prefactor or sharp polynomial correction |
| Krawtchouk: an informative finite-perturbation radius and useful finite-error digit allowance | OPEN | A local first-order capacity alone does not supply this radius/remainder control |
| Exact benchmark Hahn: determine full-map liminf and limsup, equality and finite exact value | OPEN | The terminal-row rate and full-map lower liminf at rho_H do not supply a matching full-map upper or equality |
| Hahn: matching subexponential factors, useful constants and finite-perturbation radius | OPEN | Same missing upper/prefactor/radius obligations |

These are conjuncts/cases of PD-T448 itself. Its Krawtchouk exact-rate
part has now been solved; it is not merely an auxiliary lemma. Every
other part in this decomposition is OPEN. There is no MEASURED or
CONDITIONAL part in this status aggregation. Thus the workflow's explicit
PROVED-plus-OPEN decomposition criterion applies and yields PARTIAL.

Normality, derivatives, finite measurements, and nonsharp lower bounds
remain separate supporting results. Their existence alone would not have
changed OPEN to PARTIAL. The earlier OPEN decision was appropriate before
the matching Krawtchouk upper was proved; this dated proposal records the
new reason for changing it without rewriting that history.

## Split and dependency map for later application

- Split the solved exact Krawtchouk rate conjunct from PD-T448 into
  PD-T?nn-mop-cond-codex-C2-hard-01. Keep that theorem PROVED. The remaining
  original-target conjuncts stay registered under the PARTIAL parent.
- The general-parameter lower, the simple Hahn lower, the Hahn terminal-row
  rate/full-map lower, and Hahn normality are supporting dependencies.
  Their `Split from:` is none; they do not solve the full Hahn conjunct.
- Gauge and monic matrix results concern separately specified metrics or
  gauge domains. Their relations are dependencies/corollaries, not a
  silent redefinition of PD-T448.
- At PR preparation, after reservation/allocation and review, add this
  dated decomposition/history to the predecessor home, add the two-way
  split mapping in the shared crosswalk/registry, and retain its original
  wording. No shared file is edited in this response.

## Scope and audit

This proposal changes a classification, not any accepted proof or measured
payload. Audit-01 accepted the exact rate theorem. The classification and
record application remain subject to the focused re-audit requested in
handoff03; no readiness or merge approval is asserted here.
