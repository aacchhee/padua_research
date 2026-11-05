# NN MOP IEP: conditioning and stable algorithms: log

- Branch: `codex/nn-mop-stability-20261105` · Base: main `b4d292e` (PR #21 merged) · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra high): Continue codex/nn-mop-stability-20261105.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none yet. Reserve when the draft PR opens: main, open PRs #24 and #27, and retired gaps.
- Claims: none yet.
- Open for AC: none at setup. Ask AC before using Syvert.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC asked for more detail on the NN-MOP open item, then said: "Yes open a topic. You may be a bit more adventurous in plans."
- The topic first separates conditioning from algorithmic instability. PD-T290 measured forward error only, while LIT-347 reports weak stability for the step-line analogue on the same families.
- Directions D1–D7:
  - D1: a conditioning theory;
  - D2: stage isolation with stable marginals;
  - D3: native NN algorithms (core transformations, lattice Lanczos, redundancy via zero curvature, a coupled updater);
  - D4: integrable-systems routes (Christoffel/Geronimus transforms, Toda flows, lattice Schrödinger spectral data);
  - D5: backward-error theory;
  - D6: a bounded bivariate return probe;
  - D7: comparison with the public IEP-MOP code and an outline of a possible note for Leuven.
- Model allocation and round rule follow AC's bridge instructions of the same day, with 10 rounds per direction (D6 capped at 3).
- Rules read at `b4d292e` (AGENTS/WORKFLOW unchanged since `440d107`). Branch created from main `b4d292e`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## Runs needed

- G0–G5 and D1–D7 as in handoff 01.
