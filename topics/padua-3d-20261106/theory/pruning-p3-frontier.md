# PD-T?padua-3d-20261106-prune-P3 — measured near-minimal tradeoff transfer

ID kind: PD-T. Aliases: A-fixed-count frontier;198/546-site tradeoff.
Split from: none. Split into: none. No final ID allocated.

## Statement

In the prospectively frozen P3binary64 experiment, backward A-optimal
physical-value OLS deletion from anisotropic parity supports, stopped at
M=ceil(1.20N), yields198sites at n8and546sites at n12. At the common
integer observation budgets225/637, respectively, both actual fixed-map
noise risk and sampled/searched row-l1 norm are at least5%lower than
same-count restrictedQR from the same starting support. Neither candidate
is dominated in both these quality metrics by any tested N-site control
(globalQR/localdet at both degrees, plus the stored455-node U2set at n12).
The prescribed >=10%site-saving and <=120CPU-prefix cost gates pass.

## Definitions and assumptions

N=binom(n+3,3), starting orders(n,n+1,n+1), continuous product-Chebyshev
orthonormal output basis. Scores minimize exact known single-row trace
increase, numerically evaluated from stable QR maps; no new deletion
algorithm/priority claim. Count targets are fixed before n12execution.
The hypothetical noise model is iid equal single-observation variance;
integer repeats at B=M_start use the existing map held fixed, not GLS.
All query counts,28angular refinement starts,12targets, seeds/ties/guards,
controls and thresholds are in protocol commit650b49dc2a3d5a45a20380e238399c9a0dc24c44.
Norms are sampled/searched lower values, not certified continuous suprema.

## Status by part

Overall status: **MEASURED**. Candidate disposition: retained finite
tradeoff; minimum-count/general polylogarithmic target remains OPEN.
No measured finite nondominance is presented as global Pareto optimality.
P1/P2's strict full-grid-preservation gates remain failed.

## Depends on

[Pruning identities](../pruning-theory.md), [U1recipe](u1-parity-recipe.md),
[physical OLS convention](u1-ordinary-ls-blue.md). These prove the known
algebra and initial support, not the finite inequalities above. The
[gate](../pruning-gate.md) and [next-question note](../pruning-next-questions.md)
record calibrated matched-count scope and predecessors. The stored455-node
set's exact unisolvence proof remains separate and is not transferred to
these new subsets without a new certificate.

## Evidence

[P3receipt](../evidence/pdpr-frontier12.json) contains the complete compact
logical results, source/input identities, exact command, CPU/wall/UTC/
thread/version/seed ledger and raw inventory. Full precision raw results
contain all23distinct assessments, all target/sigma tables, source snapshots,
per-deletion IDs/maps/risks, durable prefix checkpoints and28search records
per map. All61n8IDstates equal the old P1path, an actual reproduction.

Primary risk/norm ratios against restrictedQR are0.878583/0.806103 at n8,
0.801238/0.856607 at n12. The n12primary costs1.195763CPU and saves91of637
sites. Against modern storedU2at455sites it has lower B637noise risk
(0.931100versus1.172706) but worse searched norm(35.46077versus26.00732)
and91additional sites. The stored artifact's fast load/original offline
construction are explicitly distinguished from fresh construction costs.
Against full637-node OLS it loses both noise and norm. Denser diagnostic
501/455-site Apoints are retained and are not selected post hoc.

## Checks and scope

Developer preflights check durable checkpointing preserves synthetic
paths and produces valid saved maps/complete-prefix timers; rectangular
angular scaling and derivatives pass finite differences. Consequential
independent P3review is pending. All floats remain MEASURED; exact-rank
artifact delivery is a separate future check, not an inherited proof.
The full-run38.445654CPU timing is one-machine/single-thread, without a
hardware-independent bound or repeat confidence interval.

All deterministic regressions remain explicit: six targets worsen versus
full OLS, while the uniform Gaussian RMS worsens10.54%versus storedU2.
No unknown-target data-only bias selector, universal noise/error/measure
advantage, minimum-N success or continuous norm bound is claimed.

## Open items and history

A separately registered same-rule degree16transfer, with modern969-node
control and possible compact canonical-ID/exact-rank delivery, is next if
root authorizes it. Broad adaptive extraction and uniform bounds remain
OPEN. 2026-11-07, Codex gpt-6.1-sol high developer; input rules6d894d50;
root owns Git/publication/counters and the formal independent handoff.
