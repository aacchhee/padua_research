# Xu-points Lebesgue conjecture and Morrow–Patterson lower bound: log

- Branch: `claude/padua-xu-lebesgue-20261114` · Base: main `99a9b1d` (PR #34 merged)
- Developer: Claude (researcher Fable 5.2 xhigh, per-round downgrade to Opus 5.5 xhigh allowed) · Auditor: Claude, Opus 5.5 xhigh, distinct thread (AC ruling 2026-11-14)
- Stage: WORK · Open handoff: [01-work.md](handoffs/01-work.md) · PR: [#36](https://github.com/aacchhee/padua_research/pull/36) (draft, audit PENDING)
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
- AC, mid-session messages: re-authorized literature fetching without asking; authorized the institutional browser on the NTNU network and filing into `Downloads\padua\papers` (folder access to `Downloads` granted by AC through the permission prompt). AC solved one ScienceDirect captcha himself; the orchestrator never solved one.
- Literature verdicts: `literature-xu-mp.md` §3–§4. The X2 lower bound is published (Beberok, JAT 2025), so the X2 targets shift to the exact corner values, BBDM §7.1 and the sharp constant. Conj. (17) uses "≲" (BCDMV p. 319 page image).
- Novelty gates written (`novelty-gate-X1.md`, `novelty-gate-X2.md`). Draft PR #36 opened.
- G0 for both families: the developer evidence reports PASS (`evidence/xu-g0.json`, `evidence/mp-g0.json`). C-MP Path-A enclosures for even n ≤ 30: λ(±1,−1) contains n+1 and λ(1,1) ≠ λ(1,−1), certified at every n. Path-B checker output is in `evidence/mp-cmp-check.json`; independent review still to do.
- Rounds X1-2 and X2-2 started on Fable 5.2 xhigh (`rounds.md`).

## 2026-11-14 — round X1-2 result (Fable 5.2 xhigh researcher; orchestrator Opus 5.5)

- Developer claims (all PROVED, audit pending; theory/X1-01 … X1-07):
  - **tensor lift** (X1-01);
  - **Λ^Xu_n = L_n²** exactly for every n ≥ 1, where L_n = (1/n)Σ cot((2k−1)π/(4n)) is the Lebesgue constant of the n zeros of T_n (X1-03, X1-04);
  - **argmax = V*** for every n ≥ 2 (X1-05);
  - a 1-D enclosure sharpening PD-T270 (X1-06);
  - the expansion with b, c explicit, N = n, n₂ = 1, and the verdict on Conj. (17) (X1-07): both parts hold in the asymptotic sense with uniqueness of maximizers; the literal inequality is false.
- MEASURED: edge-centre deficit (X1-08).
- T0 kill test: the vertex value is not a Padua corner value. It coincides with PD-T159's F_n, so the vertex expansion alone is a corollary of merged PD-T159 + PD-T270. The new parts are the identification, the exact global constant and the argmax.
- Orchestrator's independent numerical check (not the researcher's scripts): the Sonnet path-B vertex values in `evidence/xu-vertex-values.json` equal L_n² to < 1.2e−28 for all 400 tested n ≤ 401.
- Next: an independent Opus check; a novelty re-gate (Li–Sun–Xu 2009 §3.3 lift; BdMV proof; Dencker–Erb), running.
