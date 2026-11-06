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
