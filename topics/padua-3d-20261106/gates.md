# Gates and preregistration

## Original criteria

The immutable original D0–D4 criteria are in [handoff 01](handoffs/01-work.md).
This file records implementation details and dated interpretations separately.

## 2026-11-06, before first execution

- D0: PENDING. Replay PD-T082 counts, PD-T093 factorization, two PD-N037
  baseline rows, d=2 unisolvence through 10 and PD-T101 corner values through 8.
- D1: PENDING. Use the inherited mesh/baseline construction verbatim for the
  baseline comparison; independently validate the modular-rank interpretation.
- D2: NOT RUN. Workers must preregister each family before evaluating it;
  scoped diagnostics must not be retrospectively called a D2 pass.
- D3: NOT RUN. Every obstruction needs an explicit 2-D Padua escape and
  a specified finite small-degree class where enumeration is possible.
- D4: NOT RUN. Reproduce a known exact cubature before any nonexistence claim.

Floating sample maxima are not continuous Lebesgue bounds. A finite family
failure kills only the specified family, not the entire construction route.

## D0/D1 executed verdict — 2026-11-06

**D0 PASS; D1 PASS.** [Replay record](replay-notes.md), executable
[replay](code/replay.py), compact [receipt](evidence/replay.json).
The replay includes PD-T082 counts, PD-T093 symbolic factorization and modular
draws, a PD-N035 deficient specialization, two PD-N037 rows and both controls,
and dimension-two Padua ranks through 10 / four-corner identities through 8.
All six inherited floating comparison values match exactly in this environment.
No mismatch triggered D0's stop. Receipt/code hashes and exact source inputs
are recorded. These development checks do not replace the independent audit.

T1–T6 were launched only after the replay worker reported this verdict.
Family-specific D2 preregistrations will be linked here before interpreting
their outcomes; T2/T4 workers own those separate records.

## Completed family-screen boundaries

[T2 preregistration](preregistration-T2.md) freezes the three formulas and
each later bounded census/quality step before its execution.

- K/T/O: **D2 KILL at n=2**, exact written quadratic annihilators;
  [negative record](theory/t2-cyclic-screen.md).
- Exhaustive normalized cyclic census n=2,3,4: 4,0,4 full-rank cases.
  All eight finite n=2/n=4 survivors have measured mesh maxima worse than
  the same-degree controls. **No D2-promising family.** The finite census
  is not an all-degree family and does not justify an asymptotic fit.
  [Finite record](theory/t2-finite-survivors.md).
- [T4 preregistration](preregistration-T4.md): monotone M, alternating A
  and Leja-height L stacks all **D2 KILL at n=7**, after measured losses
  against the Leja lower-set reference at both n=6 and n=7. All-n analytic
  unisolvence remains true; the kill concerns competitive quality. No
  n>=8 screen or growth-model fit was run after the registered stop.
  [Measured record](theory/t4-mesh-observations.md).

Neither stopping rule rejects arbitrary unions/corrections, skipped-degree
subsequences or all plane orderings. Those require a separately gated,
concrete mechanism before any resumed screen.

## D3 executed verdict

**Historical bounded diagnostic; see the full-class correction below.**
`t1_reflection_enum.py` checked every canonical case with coordinate
projection orders <=12 in d=3 (20,304 cases), <=10 in d=2 (450 cases),
all permitted syndromes and inactive half shifts. Exact target-count d=3
cases at n=2..6 all fail a necessary short-projection or pair-alias check.
The [hand theorem](theory/t1-minimal-obstruction.md) proves the unlimited
order/n statement and explicitly admits 2-D Padua points for every n;
the code also checks Padua through n=10. Finite enumeration does not
replace either proof or broaden the coset class.

## D4 executed verdict

**PASS before any T5 support-obstruction run.** `t5_exact.py` verified
positive degree-five product-Gauss rules in d=2,3, a positive 14-node cube
rule, and the 16-node same-parity Lobatto cube rule, with exact zero
residuals on every required monomial. The subsequent sharp 21-positive /
15-signed node bound applies only to the fixed 27-point Gaussian grid.

Separate actual reruns and their precise acceptance scope are recorded in
the independent-check files. Required Claude audit remains separate.

## Handoff 04 prospective new-direction gates — 2026-11-06

T7 and T8 read the complete prior IDEAS registry and current-main delta
before their mechanisms. T8's starting dispositions were recorded first in
[candidate retention](candidates-response-01.md).
[T7 preregistration](preregistration-T7.md) separates subgroup enumeration
from the continuous translation strata. [T8 preregistration](preregistration-T8.md)
freezes the zero-phase full finite cyclic census, omitted-degree slice and
three translated rules before execution. Each new tool must first pass
the inherited T2/H39, 2-D Padua and invariant-coset controls.

These references authorize only their written prospective scopes. Neither
finite rank success nor a generic phase sample counts as D2 promising or
an exhaustive continuous-phase result. New-direction outcomes are recorded
below as their actual executions complete.

## Audit-01 M4 correction — 2026-11-06

The original coordinate-order cap12 covered only part of the finite class
and did not meet D3(b) as written. The new developer
[full-class census](code/t1_full_enum.py), [receipt](evidence/t1-full-enum.json),
enumerates every classified code, affine syndrome and inactive half phase
with m_j<=2N at n=2..6. A target-size node set has at most N cosine levels
on each axis, which proves this finite order bound. Target-count cases are
636,1392,757,2520,4803; all fail a necessary short-axis or pair-alias screen.
**D3(b) PASS at these five full finite classes.** This is an exact formula
diagnostic of the separately accepted classification and all-n hand theorem;
it is not a claim to have computed every rank or exhausted arbitrary cosets.
D3(a)'s all-degree 2-D Padua escape remains the accepted analytic proof.

## Handoff04 completed outcomes — 2026-11-06

- New T7/T8 tool D0 controls pass before their mechanism screens. Final
  T7 diagnostics rerun those controls at its final source identity.
- T7's general-H reduction retains continuous free phases and symbolic
  minors. No n2/n3 all-coset exhaustive diagnostic is claimed. Its fixed
  20-node survivor has separate exact rank and quartic cubature certificates;
  neither activates an unregistered all-degree quality continuation.
- T8's zero-phase cyclic finite class is fully enumerated at n2/n3 with
  the proved order cap8N. Finite classifications remain MEASURED, with
  actual distinct-agent Laurent/null and actual-node checks. The all-phase
  M10 obstruction is an analytic theorem, with the 2-D Padua escape explicit.
- The prospective E selector is **D2 KILL at n9**, after the two consecutive
  admissible Leja losses at n7/n9. Degree11 was not run. Its four finite
  quality rows do not support the preregistered growth-model fit or a
  D2-promising verdict. Generator selection used rank only.
- T9 refines only the frozen old stack cases, without rescuing or extending
  a killed family. Its maxima/fits stay MEASURED. The new all-degree lower
  bounds are analytic; the n110 packing consequence stays CONDITIONAL on
  the unverified density input. No D2 construction is claimed.

The [continuation report](report-continuation-04.md) links exact scopes,
receipts, supplementary checks and remaining open targets. Required Claude
review covers PartA material changes and the new T7–T9 batch.

## Handoff06 prospective restart — 2026-11-06

The restarted counters and strict route-completion rule are in rounds.md
and immutable handoff06. New runs use separate round06 preregistrations;
no killed T4 or E family is reopened. PartA response02 precedes the first
counted PartB boundary. Prospective files are linked here before family runs.

- [T7 protocol](preregistration-T7-round06.md): complete symbolic-census
  objective, explicit measured-feasibility pilot/fallback, survivor quality,
  phase optimization and noncyclic coset unions. Incomplete coverage is
  retained as incomplete, never an exhaustive all-coset conclusion.
- [T8 protocol](preregistration-T8-round06.md): admissibility and exact
  witnesses, prospectively defined determinant-based phase optimization,
  nearby/odd moduli, mixed special phases and cyclic coset unions. A
  necessary parity condition is not sufficient without its exact witness.
- [T9 protocol](preregistration-T9-round06.md): inspected packing/Leja
  source dependencies, class-specific lower bounds, n<=16 benchmark
  measurements and their cost fallback. A budget or missing premise does
  not silently close an untried listed route.
- [T10 protocol](preregistration-T10.md): source-gated lattice seeds and
  exact small-degree search, cubature projection quality, QR/LU and
  structured extraction, and the ratio/projection theory route. Global
  determinant optimality is claimed only for an actually exhausted class.

The prospective T8 Phi3b append enumerates the gcd-based exact-count strata
for M=N+s, s1..4, then optimizes only the remaining free phases under its
frozen determinant objective. It is recorded before that new run. The
initial bounded special-phase results are disclosed starting evidence,
not unseen validation data; prior failed frozen rules remain failed.

## Retrospective audit02 E chronology correction — 2026-11-06

The old E rule's separate preregistration append and receipt are retained,
but its prospective gates.md entry was missing. This row is retrospective,
not a backdated gate. The canonical timing/allocation record is
[response-deviations-02](response-deviations-02.md). E remains killed under
its own n7/n9 quality rule and is not resumed by the new phase families.

## 2026-11-12 — handoff 19 final programme, prospective allocation

New counters, separate from the earlier D0–D4 labels and T/U/P campaigns. D1 spectral ≤6 (stop after four rounds without closing the limit), D2 determinantal ≤3, D3 cubic certificate ≤1, D4 bounds/Lee ≤2, D5 literature/paper ≤3 record rounds. No run authorized by this allocation alone: each item protocol and its specific prospective gate must be published before execution. Protocol links and run go are recorded below as they become available. Source reconnaissance and gate reading precede research execution. All old directions are frozen.

### D1 R1 and D5 R1 — before execution, 2026-11-12

- D1 R1: [gate](final-d1/gate.md), [protocol](final-d1/protocol.md), [round record](final-d1/rounds.md). Exact finite defect/lift bridge and deterministic lattice/Padua controls, intended <30 seconds. No local-limit result authorized or preclaimed by this round.
- D5 R1: [protocol](final-d5/protocol.md). Primary-source acquisition and exact statement coverage, record work only; no construction or expensive computation. Three urgent PDF excerpts were opened after the worker wrote its protocol but before this gates entry/publication; recorded once in LOG below. All remaining R1 reading follows this publication.

### D1 R2 — prospective publication, 2026-11-12

R1 completed as registered (exact finite identities plus seven deterministic controls). [R2 protocol](final-d1/protocol.md#round-2-prospective-protocol--2026-11-12-after-r1-and-before-r2) now authorizes only separation, random-translation compactness and intensity retention; no compute planned. Completeness remains a separately preregistered R3 obligation.

### D2 R1 and D3 R1 — prospective publication, 2026-11-12

- D2 [gate](final-d2/gate.md), [protocol](final-d2/protocol.md): ordered exact Padua Hilbert–Burch calibration then n2/3/4 random/structured EN and symmetric algebra over Q and p1000003, fixed seeds, per-child CPU25/wall30 seconds, total wall900/CPU750. `code/fd2_exact.py` SHA256 `975586453eb0294afb636481de2c515b2bcb4d7615203b9ad654c9362c993f62`. No rerouting after observed failure; a timeout is an implementation outcome.
- D3 [protocol/gate](final-d3/protocol.md): one fixed reconstruction and exact interval certificate attempt, seed20261112, twelve starts maximum, search180/refine300/outer450 seconds. `code/fd3_certify.py` SHA256 `b8ca61f9c46610f20e81ea234ae6a583b3003095947317951d74cf72fbd780db`. Positive degree5 rule20nodes, exact rank transfer and finite-coset exclusion required; only then measured Lambda. A failure ends its one round.
- All scientific numerical workers use one BLAS/OMP thread. Concurrent tasks mean timing stays hardware-dependent; no intrinsic impossibility follows from a cap.
