# Sharp MZ constants via limiting operators (PD-T020, PD-T027, PD-T381): log

- Branch: `codex/padua-mz-sharp-constants-20261106` · Base: main `76ba421` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra high): Continue codex/padua-mz-sharp-constants-20261106.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims: none yet.

## 2026-11-06 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC asked for one more substantial reasoning round alongside the argmax bridge. Claude suggested sharp MZ constants via limiting operators. AC: "yes, open sharp-constants codex topic under the suggested rules".
- Directions:
  - S1: the PD-T020 Mellin/Carleman mesoscopic model, in the Widom–Wilf Hilbert-matrix style;
  - S2: the PD-T027 microscopic Wiener–Hopf / Toeplitz-plus-Hankel endpoint limit, with a uniform B < 2;
  - S3: the PD-T381 2-D corner Mellin model, per parity;
  - S4: high-precision numerics.
- Coordinator gpt-6-astra high; up to 15 rounds per direction, in parallel.
- Claude's earlier chat remark compared the measured 2-D slope −0.0915 with 1/9. That was wrong: 1/9 belongs to the unnormalized Q(p²)/log m. The proved normalized constant is c₋ ≈ 0.0296 (PD-T379), and handoff 01 states the correct comparison.
- Rules read at `76ba421`. Branch created from main `76ba421`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## Runs needed

- K0–K5 and S1–S4 as in handoff 01.

## 2026-11-06 — Codex continuation setup

- Rules read at full input head `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`; current main is `76ba4214b100c86a44941f5e9a662ce9ce48efb8`, already the branch parent. No base merge needed.
- [Plan](plan.md), [gates](gates.md), and [rounds](rounds.md) registered before runs. K0 assigned to gpt-6.1-sol medium; remaining directions wait for K0. Model allocation and disjoint ownership follow handoff01.
- Shell Git fetch failed connecting to configured proxy port8080. GitHub connector reads work; frozen source snapshot preserves repository paths in `/workspace/sharp-work`. Input inventory records Git blobs; unchanged source bytes copied from the existing checkout are hash verified. Publication uses Git data API with expected-head lease. The older checkout is untouched.
- No novelty content added at setup; novelty gates apply before model development. No range reserved. No new result, extrapolation or independent check claimed.
