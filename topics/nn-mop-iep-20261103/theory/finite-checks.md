# PD-T287 — exact finite NN sanity checks

Final ID: **PD-T287**. Provisional alias: `PD-T?nn-mop-iep-codex-02`.

ID kind: PD-T. Aliases: moment-system checker; shifted flatness samples.
Split from: none. Split into: none.

## Statement

For the 14 explicitly defined rational inputs of ../exact-runs.md (two families,
N=2,...,8), all 322 defining moment systems through total degree N are
nonsingular; all 476 nearest-neighbour identities, 238 successor differences
and 70 eligible shifted 3-by-3 matrix flatness squares pass exactly. The 84
degree-N monic polynomials equal the common node polynomial. All 98 tested
degree-(N+1) moment matrices are singular. Each modified proportional-weight
example has singular M_(1,1), despite strict positivity.

## Definitions and assumptions

Exactly the nodes, rational weights, normality and transfer conventions in
../exact-runs.md. No random seed or numerical tolerance. Domain is these finite
inputs only, not generic inputs or all N.

## Status by part

Overall status: MEASURED. Exact finite observations, not a general computer
proof. A finite check here provides no all-N normality/stability theorem.

## Depends on

Committed ../code/exact_nn_mop.py and Python standard-library Fraction.
PD-T?nn-mop-iep-codex-01 supplies the independently written formulation;
the finite observations do not upgrade or weaken its analytic proof.

## Checks / proof or evidence

Producer command, source/rule pin, code/output hashes, input identities,
environment and all counts are in ../exact-runs.md. Supplementary separate
execution and independently implemented small cases: ../independent-check.md.
The receipt includes comment-only code provenance; no executable fix was needed.
Large output is local regenerable data, not falsely described as archived.

## Sources and scope

Literature identifies the standard recurrences in ../literature.md. This result
reports only performed local computations. No new algorithm, complexity rate,
digits-lost experiment or stability comparison is asserted.

## Open items / history

Claude audit-01 accepted; preparation protocol check pending. 2026-11-05, Codex; code worker allocated gpt-6.1-sol
medium, supplementary checker gpt-6-astra high. Runtime disclosure in LOG.md.
