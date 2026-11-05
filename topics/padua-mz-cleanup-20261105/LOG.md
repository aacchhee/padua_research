# MZ cleanup (certified indefiniteness witness, odd m, growth constants, manuscript integration): log

- Branch: `codex/padua-mz-cleanup-20261105` · Base: main `21dbfc9` (PR #23 merged) · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6.1-sol xhigh): Continue codex/padua-mz-cleanup-20261105.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none yet. Reserve when the draft PR opens: main, open PRs #21, #22, #24, the argmax phase-2 branch, and retired gaps.
- Claims: none yet.
- Open for AC: none. The sandbox compute allowance in handoff 01 (4 h wall per run, about 24 h cumulative CPU) is approved by AC (2026-11-05). Ask AC before using any machine outside the sandbox.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC: "open a topic for MZ cleanup", after Claude's frontier assessment. The scope follows that assessment and PR #23's "Remaining obligations":
  - a certified finite witness;
  - odd m;
  - sharp growth constants;
  - folding the 2-D results into the MZ manuscript;
  - housekeeping;
  - optionally PD-T027.
- Rules read at `21dbfc9` (unchanged since `440d107`). Branch created from main `21dbfc9`. Only this LOG, handoff 01 and the results stub were added.
- Claude fitted the four merged PD-T300 minima (m = 800, 1000, 1200, 1600) post hoc: λ_min ≈ 0.6519 − 0.09153 log m, residuals < 4e-5, predicting a first even crossing near m ≈ 1240. This is MEASURED steering only, recorded in handoff 01's context. No computation was run on the branch and no claim made.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — compute allowance

- AC: "sandbox limits are ok". The handoff 01 limits (up to 4 h wall per run, about 24 h cumulative CPU, sandbox only) are approved. The handoff body is unchanged.

## Runs needed

- K0–K2 and C1–C6 as in handoff 01.

## 2026-11-05 — Codex, gpt-6.1-sol xhigh — continuation and K0

- Rules read at ad503cb0603fc017444b0aa732240981eefa4d24; unchanged. Fetched main/base 21dbfc90257b952d8923f6d01739d12aa8d6e0a1 and topic ad503cb; base already reconciled. Git access needs the execution tool network permission; connector retrieval also succeeded.
- Plan and K2 diagnostic fit were written before any new computation. Replay K0 PASS with exact m60 regeneration and float m800 agreement; m1600 negative float regenerated. Commands are frozen in the scripts and receipts.
- Parallel agents own C2/C3 mathematics, C4 manuscript, C1 producer, independent witness checker, C5 housekeeping and supplementary Astra high math reconstruction. Only orchestrator controls Git.
- C3 scope correction: the handoff optima are unnormalized energies, not established Rayleigh constants. No spectral slope is inferred from them. New mechanisms are gated by the mathematics worker; numeric replay adds no novelty claim.
