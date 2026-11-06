# NN MOP conditioning: intrinsic or metric? Sharp rates, weak stability, IEP-MOP comparison: log

- Branch: `codex/nn-mop-conditioning-20261106` · Base: main `76ba421` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra high): Continue codex/nn-mop-conditioning-20261106.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims: none yet.

## 2026-11-06 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC asked what can still be done on the IEP/Leuven line. Claude proposed step 1, a focused round, and then a note. AC: "yes open a codex branch for step 1".
- Claude's reading of PD-T434 (arithmetic only) shows the step-line κ has the same exponential base as NN, about 4 times smaller. The open question is therefore whether the exponential survives the 1-D control, diagonal gauges and the LIT-347 normalization.
- Directions:
  - C1: the metric question;
  - C2: sharp rates (Krawtchouk upper, Hahn lower, ρ(p₁, p₂));
  - C3: weak stability;
  - C4: the IEP-MOP field-by-field comparison.
- Up to 8 rounds per direction, in parallel; coordinator gpt-6-astra high.
- Rules read at `76ba421`. Branch created from main `76ba421`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## Runs needed

- M0–M4 and C1–C4 as in handoff 01.
