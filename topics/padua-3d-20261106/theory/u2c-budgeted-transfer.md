# PD-N?padua-3d-20261106-codex-U2C-01 — degree14 fixed-budget extension

ID kind: PD-N. Aliases: U2 C1; U2 R4; degree14 120CPU transfer.
Split from: none. Split into: none.

## Statement

In the single recorded degree14/N680 execution of the inherited200-step
U2-AB schedule with120 extra CPU-second limit and the actual operation/
checkpoint semantics below, the strict complete-cost gate fails: the
optimizer reaches the CPU cap after176 accepted steps and complete extra
construction costs120.717693505CPU seconds. Its finite searched norm
35.544330716 improves one-sweep localdet64.206906251 and cost-selected
five-total-sweep localdet62.153365193, so quality and numerical guards
pass while the combined quality/cost gate fails. This is a measured
failure of this fixed-budget extension, not a general runtime lower bound.

## Definitions and assumptions

Total-degree polynomial dimension N=binom(n+3,3), n14. Objective,
QR/localdet initialization, Neumann/separation/Armijo update and200-step
cap are inherited unchanged from [U2-AB](u2-admissible-norm.md).
[Prospective protocol](../u2-continuation-protocol.md), publication
9ceb7229be2fb938e3ce11540ed5fcde81abf259, fixes the strict120 extraCPU
gate and5% searched-norm improvement against both one-sweep and
matched-cost repeated identical localdet. Process timing is specific to
this machine/library environment. Actual code checks outer/backtrack and
completed-trial boundaries; it buffers trial arrays/events and flushes at
exit, including that work and final guards in complete extra cost.
The canonical [implementation deviation](../u2-continuation.md) records
why literal prospective operation/checkpoint adherence is not claimed.

## Status by part

Overall status: **MEASURED**.
Candidate disposition (revised 2026-11-12): **retained, hardware-dependent**.
Historical **REJECTED: failed** applies solely to the original developer
execution and its strict 120-extraCPU gate; it is not the current
disposition of the fixed 200-step recipe.
Neither the U2-AB pilot gates at degrees6/8 and holdout gates10/12 nor the general objective,
all direct optimization, shortened schedules, or all-degree target is
rejected. All-degree stable minimal interpolation remains OPEN.

## Negative-result scope

Attempted mechanism: unchanged U2-AB with200 accepted-step target,
120-extraCPU cap, degree14 one-sweep localdet start, exactly this source
and hardware execution. Parameter range: this one n14 trial only.
Failure criterion is full complete cost<120 and no CPU cap, along with
guards and5% quality; cost fails regardless of positive quality.

## Depends on

Inherited basis/QR/Leja/localdet and U2-AB code, exact source identities
in [receipt](../evidence/u2c-transfer14.json). No external theorem or
finite exact-rank claim is used. Known degree12 comparable-cost audit
is background, not evidence for degree14 or an unseen baseline.

## Checks and evidence

Actual command, full costs, five sets' source/node identities, versions,
seeds and all nine functions/two measures/16-noise-trial summaries are
in the receipt and [continuation](../u2-continuation.md). All five sets
have680 distinct cube nodes and valid numerical guards. Assessment uses
114700 fresh interior/face/edge points and140 physical-coordinate local
starts per set. These maxima are lower samples, not norm certificates.
U2's output orthonormal condition is12.60651, inverse residual1.929e-12,
and iid coefficient-risk1.745112 versus repeated-localdet1.806543.
Function and noise outcomes are retained without quality-based selection.

Matched control keeps the last whole sweep prefix within120 extraCPU:
four extra sweeps at97.413190031CPU, five total. The next sweep completes
at121.658369592 and is excluded. U2's total construction includes QR
3.762892511 and initial localdet25.119975511, totaling149.600561527.
Selected repeated-localdet total is126.296058053CPU. Different final
unused fractions and noninterleaved timing limit that comparison.

All raw trajectories/nodes/searches have a byte/hash inventory in the
unique local regenerate-only scratch directory named by the receipt.
They are not archived or sufficient for a computer-assisted exact proof.
The distinct reviewer's [executed check](../continuation-review/evidence/u2.json)
actually verifies source/raw identities, all881 events and accepted-prefix
selection, guard/Armijo trace data and strict cost failure, and independently
reconstructs maps and fresh22540-query/physical-search lower samples for
U2 and repeated localdet. It recovers U2's35.544330716 peak. This is an
independent numerical/trace check, not a new construction-timing benchmark.
Formal Claude audit remains pending.

## Open items

Further U2 research is frozen by AC’s approved narrowed plan. The fixed
120-second/200-step recipe is not intrinsically rejected or parked on
mathematical or hardware-independent cost grounds. The strong finite
benefit permitted the separately completed training-only cost calibration and
shorter-schedule degree16 holdout, recorded in
[u2c-shortened-transfer](u2c-shortened-transfer.md); those do not erase this
failure. General convergence, certified norms, all-degree stability and
broad error/noise dominance remain unresolved.

## History

2026-11-07, Codex, assigned gpt-6.1-sol high; runtime metadata unexposed.
Input97c323bfae15cf3c76f40802c3ebabedceeb0c60. C1 actually executed
following prospective publication; deviation discovered during execution
is preserved in the canonical continuation record, never silently fixed.

## History and independent timing scope — audit04 G2, 2026-11-12

Audit04 B2's unchanged rerun completes 200 steps in 116.05 CPU seconds,
with no cap and norm 33.768, ratios 0.526/0.543: the full C1 gate passes
on that execution. Its trajectory through step 176 matches the original.
The negative statement above remains MEASURED for the original run only;
it does not assert that the recipe fails on other hardware. The current
recipe disposition is retained hardware-dependent evidence. Canonical
chronology and C2 interpretation: [dated continuation revision](../u2-continuation.md#audit04-g2--hardware-dependent-c1-disposition-revision-2026-11-12).
No developer rerun was performed for this record correction.
