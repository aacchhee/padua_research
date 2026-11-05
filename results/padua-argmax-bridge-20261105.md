# padua-argmax-bridge-20261105 — closing the Padua argmax bridge

This file is written only by the topic orchestrator. Branch `codex/padua-argmax-bridge-20261105`; no PR yet.

## Status (2026-11-05): WORK, topic set up

Goal: PD-T099 for all n. It is currently certified for 2–32 and proved for n ≥ N_* with N_* not explicit.

The plan, in [handoff 01](../topics/padua-argmax-bridge-20261105/handoffs/01-work.md), is to meet in the middle:

- **finite side:** a practical outward certifier (N3: Taylor models, dyadic corner shells) pushed upward from 33;
- **analytic side:** a degree-uniform computer-assisted proof for n ≥ n₁ with explicit n₁ (N1: explicit summation remainders; N2: the phase-dependent log profile from polygonal Lebesgue-constant methods).

Side probes:

- N4: positive-translation / hypergroup contraction;
- N5/N6: 1-D classical analysis and the Lissajous curve.

No results yet.

## Next step

`Codex (gpt-6-astra high): Continue codex/padua-argmax-bridge-20261105.`

## 2026-11-05 development checkpoint

B0 PASS: fresh native n24 regeneration and separate checker replays of both
regenerated/committed certificates agree exactly; the n32 floating pilot
reproduces all deterministic counts and its unresolved902-box frontier.
[Replay record](../topics/padua-argmax-bridge-20261105/independent-checks-b0.md).

B1 **MEASURED diagnostics**: seven-degree finite map,33/48/64/96/128/192/256,
with all admissible noncorner centers at161 near phases per degree. The expanded
small-phase grid recovers positive primitive excess at128/256. Continuous
region extrema and tiny-shell signs remain unresolved.
[Margin anatomy](../topics/padua-argmax-bridge-20261105/margin-anatomy.md).

N1–N6 first rounds are running in parallel; [draft PR27](https://github.com/aacchhee/padua_research/pull/27).
No new degree or effective onset is claimed at this checkpoint. PD-T099 stays
OPEN and the inherited certified global range stays2–32.

## Independently checked extension and first analytic rounds

**PROVED development result, Claude audit pending:** exact finite argmax at
n33/34, independently accepted with full arithmetic/partition verification
and36 rejected corruption controls. The checked finite range is now2–34;
35/36 remain candidate-only at this checkpoint.
[Finite record](../topics/padua-argmax-bridge-20261105/theory/native-finite-range.md).

Analytic development supplies exact full-phase cotangent rows, a uniform
fourth-order pole-extracted block bound, and an explicit n-dependent row-model
error r(n)=[7pi^4/1800+7pi^3H_n/900]/n^4. A distinct Astrahigh supplement found
no substantive mathematics issue. This still retains outer rows/reciprocal
sums; no compact uniform-degree model or onset follows.
[Model](../topics/padua-argmax-bridge-20261105/theory/N1-row-model.md).

N3 **MEASURED** first-order float covers33/64 complete;128 capped with344
pending. B2 remains incomplete. Exact positive-translation and trace-lifting
obstructions reject specified classes only; broader N4/N6 and PD-T099 stay
OPEN/deferred. N1/N5/N3 continue their next gated steps.
