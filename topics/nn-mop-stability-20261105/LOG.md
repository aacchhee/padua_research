# NN MOP IEP: conditioning and stable algorithms: log

- Branch: `codex/nn-mop-stability-20261105` · Base: main `b4d292e` (PR #21 merged) · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra high): Continue codex/nn-mop-stability-20261105.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: T432–471, N162–177, IDEA530–569, LIT614–629; reservation only, no assignments. See ALLOCATIONS.md.
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

## 2026-11-05 — Codex coordinator, requested gpt-6-astra high — resumed WORK

- Rules and source read at full head `823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`. Current main/base checked via connector: `b4d292eea5eed373002506d5e16a3761bd7ae10e`; no base reconciliation needed. Serving model/effective effort metadata are not independently exposed.
- Shell Git fetch fails before HTTP because the inherited proxy port8080 is unreachable. Used the authorized GitHub connector and isolated pinned snapshot; [complete fetched list](input-snapshot.json). Local old `work` checkout is unchanged. No network policy bypass.
- Wrote [plan.md](plan.md), including G3 prediction, before any experiment. Delegated disjoint D1–D7 scopes under handoff01's explicit parallel/model allocation; [round ledger](rounds.md). Workers read gate and predecessor evidence before generating candidates. Coordinator does not claim novel science from setup.
- Refreshed main/all open PR24/27 and all 44 ledger/registry copies; no closed-unmerged PR. [Reservation](ALLOCATIONS.md) is strictly above unionT431/N161/IDEA529/LIT613, including permanent gaps. No final assignment/shared-registry change.
- Current outputs are development in progress. Audit PENDING. Only AC merges.


- Snapshot transport correction: the initial materializer appended one extra final LF to each fetched file. Restored all222 unchanged inputs byte-for-byte (the topic LOG is already being updated) against their pinned Git blob SHA before final evidence collection; this changes no scientific content. Initial replay values matched exactly; code-hash receipts are refreshed after correction.
