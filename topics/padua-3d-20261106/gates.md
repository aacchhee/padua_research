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
