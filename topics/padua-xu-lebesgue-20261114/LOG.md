# Xu-points Lebesgue conjecture and Morrow–Patterson lower bound: log

- Branch: `claude/padua-xu-lebesgue-20261114` · Base: main `99a9b1d` (PR #34 merged)
- Developer: Claude (researcher Fable 5.2 xhigh, per-round downgrade to Opus 5.5 xhigh allowed) · Auditor: Claude, Opus 5.5 xhigh, distinct thread (AC ruling 2026-11-14)
- Stage: WORK · Open handoff: [01-work.md](handoffs/01-work.md) · PR: none yet
- Claims: none yet. Provisional IDs will be `PD-T?padua-xu-lebesgue-20261114-claude-NN`.

## 2026-11-14 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC asked: "I have resources for one rather extensive Fable round. Do you see any remaining padua-related problems that might be worth it?"
  - The orchestrator recommended:
    - X1, the Xu-points conjecture (BCDMV 2006, Conj. (17), LIT-486);
    - X2, the Morrow–Patterson lower bound (LIT-378).
  - AC replied: "make a brief for fable 5.2. same branch for both directions 1 and 2. Research on fable 5.2 xhigh, audit opus 5.5. xhigh. Up to ten rounds per direction, researcher in each round may be downgraded to opus 5.5 if the problem does not look challenging".
- **AC rulings of 2026-11-14, applying to this topic only:**
  1. Fable 5.2 xhigh is used for mathematical development. The workflow table otherwise restricts Fable to ideas campaigns.
  2. A per-round downgrade of the researcher to Opus 5.5 xhigh is allowed when the problem does not look challenging.
  3. The audit is done by Claude, Opus 5.5 xhigh, in place of Codex. The auditor is a distinct thread; the developer never approves its own work.
  4. The budget is up to 10 rounds per direction, with both directions on one branch.
- Rules read at `99a9b1d`; AGENTS, WORKFLOW and CLAUDE_ROLES are unchanged since `76ba421`. The branch was created from main `99a9b1d`. Only BRIEF.md, handoff 01, this LOG and the results stub were added.
- The BRIEF's literature statements beyond LIT-486 are Claude's recollection and are marked "verify". These include the Xu 1996 and BdMV 2006 citations, the parity conventions and the MP definitions.
- No computation was run and no claim was made.

## 2026-11-14 — Claude, claude-opus-5-5 (thread model; effort not exposed) — session 1, handoff 01, round 0 (setup)

- Rules read at branch head `2d60e22253d270868c21a49c57648c064204df4d` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md; unchanged since `76ba421`). Role: orchestrator. Base: main `99a9b1d` (no newer main at session start; checked with `git ls-remote`).
- **Model check (handoff 01, setup 1).** AC's prompt named "Claude (Fable 5.2, xhigh)", but this thread runs on **Opus 5.5** (claude-opus-5-5). A probe subagent requested with model `fable` reported "Fable 5.2, model ID claude-fable-5-2", so Fable 5.2 is available to this thread **as a subagent**. Disclosure sent to AC before any mathematics. Arrangement adopted unless AC redirects: Opus 5.5 orchestrates (Git, records, integration; round-0 literature/bookkeeping is a BRIEF §4 downgrade case); mathematical research rounds run as Fable 5.2 xhigh subagents, the per-round model recorded in `rounds.md`. This is a deviation from handoff 01's "orchestrator on Fable 5.2" and is disclosed here once.
- AC rulings of 2026-11-14 (Fable for mathematical development; Opus 5.5 xhigh Claude auditor in place of Codex; per-round downgrade; 10 rounds per direction) are recorded in the setup entry above and apply.
- `gates.md` (G0–G5) written and pushed before any run.
- Literature reads delegated to two Opus 5.5 readers (X1: Xu 1996, BdMV 2006, BCDMV 2006 §§1–2,4, Kolomoitsev–Lomako 2021 on Xu points, forward citations; X2: Beberok–Białas-Cież–De Marchi arXiv 2412.14595, Morrow–Patterson 1978, Caliari–De Marchi–Vianello 2005, forward citations). Outputs `lit-notes/X1-sources.md`, `lit-notes/X2-sources.md`; merged into `literature-xu-mp.md` by the orchestrator.
