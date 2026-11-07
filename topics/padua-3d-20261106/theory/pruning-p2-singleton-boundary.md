# PD-N?padua-3d-20261106-prune-P2 — initial singleton feasibility boundary

ID kind: PD-N. Aliases: PRUNE-L; exhaustive raw-cardinal constrained deletion.
Split from: none. Split into: none. No final ID allocated.

## Statement

In the binary64 P2experiment fixed prospectively by protocol commit
143b5d0e17688d835b1e0c5f61e1ed95a5e05dbe, on each initial anisotropic
parity-grid unweighted-OLS support at n6and n8, **none** of respectively
112and225rank-admissible single-row deletions passes the fixed training
amplification threshold1.25times its initial value. Every one passes the
separate integer-budget-risk threshold1.10times the initial value. Hence
PRUNE-L's exhaustive joint-feasibility search stops without deleting a row,
and the registered10%site-saving useful-transfer gate fails at both degrees.

## Definitions and assumptions

n6has N84/M112 and n8has N165/M225; starting orders are(n,n+1,n+1).
The physical-value map is unweighted OLS in the continuous product-Chebyshev
orthonormal basis. Observation noise is hypothetically iid equal variance;
integer repeats allocate a fixed B=M_start with the fitted map held fixed.
Training is a9³angular mesh plus256angular-Sobol queries, seed2026111010+n.
A row i is numerically rank-admissible when1-h_i>1e-10. All candidate maps
and training cardinal rows use the exact known deletion formula, evaluated
in binary64 from fresh Householder QR of the full starting support.
The finite statements refer precisely to those matrix/query computations.

## Status by part and disposition

Overall status: **MEASURED**. Candidate disposition: **REJECTED: failed**
for the strict singleton useful-transfer goal on these supports. The
general adaptive-pruning/minimum-count goal remains OPEN. This floating
enumeration is not an exact computer-assisted proof or a supremum bound.

## Negative-result scope

Attempted mechanism: IDEA?padua-3d-20261106-prune-L, exhaustive feasible
single-row backward removal with raw row-l1 objective. Scope: the **initial**
n6/n8supports, prescribed training queries,25%norm and10%integer-risk
constraints, fixed physical solver/measure/budget. It is a first-step
barrier under this rule, independent of any tie ordering. It does not
exclude a different support, larger allowed amplification, temporary
nonmonotone path, block deletion, direct point movement, or another
noise/measure model. It proves no general subset infeasibility.

## Depends on

[Pruning identities](../pruning-theory.md), [U1recipe](u1-parity-recipe.md),
and [U1OLSphysical noise convention](u1-ordinary-ls-blue.md) establish the
known algebra/starting definitions. They do not imply the measured
feasibility result. P1's separate failure is preserved in
[its own boundary](pruning-p1-boundary.md).

## Evidence and checks

[P2receipt](../evidence/pdpr-constrained.json) identifies all original
source snapshots, exact executed command, protocol, raw details and file
inventory. Raw tables contain every337candidate, scores, rank denominator,
noise risk and constraint reason, plus all held-out controls/target tables.
The best training-norm ratios among noise-feasible rows are1.28695579
and1.44439868. The norm-feasible set is empty, so its minimum risk is
undefined, not an invented infinity/success. No selected-candidate QR
rejection or cap event occurs. Source/metadata snapshots remained fixed.
Actual full execution cost is4.149492873process CPU seconds.

Developer engineering independently compares26generic-matrix candidate
maps/norm/noise/feasibility values against fresh QR, checks the case where
the best raw objective is noise-infeasible but another row is feasible,
and exercises36mocked caps. These are technical checks,0research rounds,
not a separate consequential P2rerun. Such independent review is pending.
The [results](../pruning-results.md) record the actual complete scope and
retain the formal Claude review obligation separately.

## Sources, open items, history

Known backward-design/projection precedents are scoped in the
[gate](../pruning-gate.md); no new source theorem or algorithmic priority
claim. The next unresolved question is whether a changed support, explicit
Pareto objective, or symmetry block can escape this exact singleton
obstruction, prospectively specified before execution. 2026-11-07,
Codex gpt-6.1-sol high developer; root owns publication/counters/audit.
