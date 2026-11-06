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


## 2026-11-06 — Codex continuation setup and K0

- Rules read at `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`; current main/base `76ba4214b100c86a44941f5e9a662ce9ce48efb8` is already the topic parent. No base merge needed. Setup plan/gates published in6e928d9 before first run. Draft PR31 opened.
- Shell Git fetch failed connecting to configured proxy8080. Connector reads work. The pinned source corpus `/workspace/sharp-work` preserves paths; [input inventory](input-snapshot.json) verifies79 files by Git blob/SHA256. The older checkout is untouched. Publication uses Git data APIs and expected-head lease.
- Coordinator requested gpt-6-astra high; serving metadata unexposed. S4 development requested gpt-6.1-sol medium; S1–S3 requested gpt-6.1-sol xhigh, disjoint paths. A distinct gpt-6-astra high checker is rerunning K0. Required Claude audit remains PENDING.
- K0 developer replay PASS under the explicit finite-norm interpretation: six CC cases N40–1280, maximum relative difference3.997e-15; Padua minima m800/1000 bit-identical to pinned PD-T300 values. Carrier finite norm formula agrees with independently assembled composite angular quadrature within3.31e-16 throughm4096; finite-to-limit offsets remain nonzero and decrease. These are MEASURED, not new spectral proofs.
- Original K0's request for matching a carrier norm limit at1e-10 is ill-posed at a finite degree without an error allowance. We preserve that criterion and record a dated clarification in gates.md: compare exact finite norm to a separate quadrature at1e-10, then measure finite-to-limit discrepancy separately. The first global x-Gauss check lost accuracy at high degree; its code/receipt are retained, its issue explained by endpoint sensitivity, and the composite angular check replaces it. No fit was performed.
- S1–S3 cleared to develop after K0 and their novelty gates. No new mechanism proposed by coordinator; gate/predecessor reading belongs in each direction's record. No final ID range reserved.
