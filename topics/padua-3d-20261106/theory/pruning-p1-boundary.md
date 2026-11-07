# PD-N?padua-3d-20261106-prune-P1 — small-degree A/D pruning quality boundary

ID kind: PD-N. Aliases: PRUNE-A; PRUNE-D; P1backward-design failure.
Split from: none. Split into: none. No final ID allocated.

## Statement

In the P1binary64 experiment fixed by protocol commit
a05fa01eefb9e187e73b870cfa74b7eb7887d42f, neither backward A-optimal
trace-increase deletion nor backward minimum-leverage determinant deletion
from anisotropic parity-grid **unweighted OLS**, at degrees4/6/8, passes
the registered useful-transfer gate. In particular, at degrees6/8 neither
selected connected training/noise prefix saves10%of starting sites, and
at n8their held-out sampled amplification ratios are1.65522/1.60783,
above1.30. All A/D numerical checks pass in this finite experiment.

## Definitions and assumptions

N=binom(n+3,3), starting nodes use m=(n,n+1,n+1), M=45/112/225.
The physical-value map uses the continuously orthonormal product-Chebyshev
basis, raw unweighted iid observations, fixed integer total observation
budget B=M_start, and repeats with the original map held fixed. The
operational prefix stops at its first training-amplification ratio>1.25
or integer-risk ratio>1.10. Training is128angular Sobol points plus
corners; assessment uses21³/41³nested angular meshes and2048queries
from each of two fresh measures. Seeds/ties/guards are protocol-fixed.
The statement covers those exact rules, ordering, float implementation,
training sets and finite degrees; it is not a continuous norm claim.

## Status by part

Overall status: **MEASURED**. Candidate disposition: **REJECTED: failed**
for these P1rules as useful-transfer routes under the frozen gate.
The broader adaptive-pruning/minimum-count target remains **OPEN**.
No floating agreement is labeled a computer-assisted proof.

## Negative-result scope

Attempted mechanisms: IDEA?padua-3d-20261106-prune-A and
IDEA?padua-3d-20261106-prune-D. Parameter range: n4/6/8only, the exact
starting supports, physical OLS solver, one start and published thresholds.
D's determinant objective and A's unit-noise trace objective are distinct.
Their failure does not reject other deletion orderings, denser training,
constraint-aware searches, weighting/noise models or larger designs.

## Depends on

[Pruning identities](../pruning-theory.md) provide exact known algebra;
[U1recipe](u1-parity-recipe.md) gives the initial support/full rank;
[U1OLS](u1-ordinary-ls-blue.md) supplies the physical noise convention.
Those proofs do not imply the finite quality outcome. The gate compares
T9extraction and prior T10frozen selectors without claiming novelty.

## Proof or evidence

[P1receipt](../evidence/pdpr-pilot.json) contains the complete compact
count/norm/noise/guard/decision object and exact original source snapshots;
its pinned raw details contain all104assessments, per-deletion trajectories,
individual target errors/calibrated MSEs, nodes/maps and full precision
margins. A and D at n6retain112/111of112sites and at n8retain223/222of225.
The final unit-noise traces are monotone along every valid OLS path.
No held-out value chooses a deletion or the reported connected prefix.
At n8N165, A/D also lose the frozen globalQR/localdet norm controls.
All numerical guard failures, notably lexN165reproduction, remain retained.

## Checks and sources

Exact command/publication/source hashes/threads/versions/seeds and the
actual17.097765CPU run ledger are in the receipt and
[results](../pruning-results.md). The separate collector only serializes
already completed unchanged science; the canonical serialization/timestamp
limitation is in that results record. No source theorem is imported as a
new local proof. Developer engineering checks are separate, and distinct
consequential independent review/rerun is pending.

## Open items and history

The broad explicit small-amplification/minimum-count target remains OPEN.
A prospective raw-cardinal constraint-aware deletion question can be
registered separately; it does not erase this failed gate. 2026-11-07,
Codex gpt-6.1-sol high developer, rules/input6d894d50; P1science source
frozen independently of the later administrative collector. Root owns
publication/counters and the formal independent handoff.
