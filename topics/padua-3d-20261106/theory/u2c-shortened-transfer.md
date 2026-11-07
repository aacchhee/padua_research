# PD-T?padua-3d-20261106-codex-U2C-02 — calibrated degree16 finite endpoint

ID kind: PD-T. Aliases: U2 C2/C3; U2 cap40; degree16 cost-controlled transfer.
Split from: none. Split into: none.

## Statement

The fixed U2-AB update, with the **changed calibrated stopping cap40**,
produces the recorded degree16/N969 finite interpolant in65.783450517
complete extra CPU seconds on the recorded machine. Its searched norm
lower sample71.707745700 is at least5% lower than both one-sweep localdet
93.638480903 and the last whole-sweep extra-cost-matched localdet control
79.267416687. All numerical guards and that prospectively frozen C3
quality/cost gate pass. This is a finite measured statement, not an
unchanged200-step transfer, convergence, norm certificate or asymptotic
construction theorem. A separate C4 finer-row-prefix test assesses the
remaining whole-sweep cost granularity; its outcome is recorded below.

## Definitions

Total-degree3D polynomial dimension N=binom(n+3,3), n16. Objective,
Chebyshev basis order, QR/one-sweep-localdet initialization, projected
direction, separation cap, Neumann and Armijo rules are inherited U2-AB.
Only stopping schedule and explicit stage/checkpoint cost semantics
change as registered in the [continuation protocol](../u2-continuation-protocol.md).

## Assumptions

The C2 training-only calibration selected the largest eligible cap from
40/60/80, requiring20% training gain, numerical guards and a heuristic
cubic forecast<=100CPU seconds. It selected40. Training-only prefix costs
were known and not complete construction costs; the forecast was never
a guarantee. C3 is a fresh candidate degree16 with the selected fixed40
schedule, fresh queries and known function design, under120 complete
extraCPU and5% searched-norm gates against both one-sweep and comparable
whole-sweep repeated localdet. Single-thread same-machine process timing,
full source hashes, input identities and seeds are in the receipts.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / limits |
|---|---|---|
| Training-only40-step calibration | MEASURED | All3 caps retained; known n14 training/cost, no assessment selection |
| Degree16 finite C3 quality/cost/guard pass | MEASURED | Complete timed construction and fresh searched lower samples |
| General convergence, certified norm, all-degree stability | OPEN, outside statement | No proof or norm enclosure |

Candidate disposition: retained for its measured finite norm-specific
scope; C1's fixed200-step degree14 cost failure remains in its separate
[negative home](u2c-budgeted-transfer.md). This does not reject the
objective or turn any broad target into PARTIAL/PROVED.

## Depends on

Frozen inherited source chain and guarded C3 producer; no external theorem
upgrades numerical results. Historical n12 evidence is background only.
C2 protocol publication6d800dd302d5af46b7239d9b8a55a59825c3d116 and
C3 publication0ba513e27319b645b610f1075297a074d42dfd27 precede dependent
execution. Exact code/data identities are in
[calibration receipt](../evidence/u2c-calibration.json) and
[degree16 receipt](../evidence/u2c-heldout16.json).

## Checks / sources

Actual commands, versions, threads, seeds and unique raw output locations
are in [continuation](../u2-continuation.md). The new stage implementation
checks before/after each named expensive stage, checkpoints each trial
with flush/fsync before acceptance and charges final numerical guards
and output. C1's old source/deviation remains immutable. Six targeted
engineering probes and the distinct reviewer's nine staged-clock cases
check cap exits, including active-trial retention and original fallback.

The distinct [calibration rerun](../continuation-review/evidence/u2-calibration.json)
reconstructs every candidate's training maximum/guards/forecast. The
[independent degree16 check](../continuation-review/evidence/u2-heldout.json)
actually verifies all raw/source/trial hashes,604 stage records,40
accepted steps, selected event259, complete final-save cost and matched
whole-sweep selection. It independently reconstructs maps/risk and uses
22540 fresh queries plus12 physical maximization starts per set, finding
the same71.707745700 and79.267416687 peaks. This is not an independent
construction-time rerun or formal Claude audit.

## Proof or evidence

Every degree16 set has969 distinct cube nodes and passes numerical
conditioning/residual guards. U2 reaches40 accepted steps with optimizer
success=false,41 objectives,219 Neumann rejections and no fallback.
Complete extraCPU is65.783450517; total124.202551434 includes QR9.908028201
and first localdet48.511072716. There is no CPU-cap hit.

The original C3 control fits one extra full sweep at49.914188378CPU,
yielding two total sweeps and108.333289295 totalCPU. The next extra
sweep ends100.648284497, exceeds the fixed65.783450517 allowance and
is retained/excluded. The remaining15.869262139seconds (24.12%) motivate
C4, since the whole-sweep norm advantage is9.54%. Selection uses cost
boundaries, never assessment quality.

Candidate orthonormal condition25.52829 improves the whole-sweep
control28.96930, but iid coefficient-risk2.358026 is5.04% worse than
2.244970, and pooled noise RMS worsens on both assessment measures.
Eleven of16 non-machine-floor function/measure RMS combinations worsen
against that stronger control; max/RMS/noise outcomes remain in full.
Finite sampled norm improvement does not imply general approximation or
noise improvement. Producer assessment uses114700 fresh interior/face/edge
points and140 physical-coordinate starts per set. All such maxima are
lower samples, not certified suprema.

## C4 strengthened-control outcome

C4 was published at dde24e3007b2a19de520c9ee8455623a625a525e before
execution. Its [7785-byte receipt](../evidence/u2c-prefix-control.json)
records a fresh reconstruction from exactly the same one-sweep initial
nodes in one isolated timing window, with all per-row checkpoint costs
charged. The first extra full sweep costs49.127078171CPU and is byte
identical to C3's selected whole-sweep nodes. A further344 complete
rows of the next sweep fit at65.746077401CPU. The next row checkpoint completes65.791293988 and is retained/excluded;
total kernel work including final bookkeeping is65.808686473.
Only0.037373119 seconds remain unused (0.057%).

Fresh matching assessment gives U2 norm71.707745700, whole-sweep
79.267416687 and finer-row-prefix80.120124214. Ratios0.904631/0.895003
both meet the unchanged5% gate; all nodes/maps pass guards and selected
cost is within both precision representations of the budget. The more
fully spent determinant prefix slightly worsens norm despite improving
log determinant; it is retained without quality-based prefix choice.
The result therefore survives the cost granularity challenge within
this finite assessment, without implying monotone determinant/norm
behavior or superiority over all fixed-budget methods.

The candidate's iid coefficient-risk2.358026 is5.93% worse than the
finer control2.225993; both pooled noise RMS values worsen. Twelve of16
non-machine-floor function/measure RMS combinations worsen. All errors,
noise, conditioning and map setup costs remain in the receipt.
The practical gain concerns searched norm under the strict969-site limit.
No generic error/noise superiority is claimed.

The [canonical precision note](../u2-continuation.md) records the3ns
receipt-rounding discrepancy; the independent check confirms identical
prefix selection under both budget representations.

The distinct [executed C4 check](../continuation-review/evidence/u2-prefix.json)
verifies source/input/raw node identities, whole-sweep byte equality,
344 selected rows versus345 retained, both budget representations and
three row gains by fresh linear solves. Its separate22540-query and
12-physical-start assessment per set gives ratio0.89500235, preserving
the strengthened5% gate. These are actual independent checks, not an
independent hardware timing benchmark or certified continuum norm.

## Scope / open items

Finite degree16 measured behavior and same-machine costs only. There is
no exact stored-set theorem or committed essential node payload for the
new969-node output; its hash-identified raw coordinates are local
regenerate-only. Required code/compact receipts support regeneration,
not archival delivery. Formal Claude audit, global norm enclosure,
general convergence and degree-uniform stability remain open. Four further rounds are complete (C1 transfer/cost failure, C2 training
calibration, C3 shortened-schedule pass, C4 finer-control pass), leaving
three of the seven further slots unallocated. The original R1–R3 remain
unchanged; aggregate U2 count is7. This is a useful finite endpoint.
Another degree or step-count repeat would spend computation without a
new specified site/application question. Resume only for a concrete
new constraint or a genuinely distinct prospectively registered mechanism,
with the full novelty gate if needed; the wider target is not exhausted.

## History

2026-11-07, Codex, assigned gpt-6.1-sol high; provider runtime metadata
unexposed. Input97c323bfae15cf3c76f40802c3ebabedceeb0c60. C2 known-training
calibration and C3 new-degree test are separately prospectively published;
changed stopping schedule is disclosed and C1's failure is preserved.
