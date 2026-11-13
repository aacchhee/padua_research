# MZ paper finalization (MZ-CC and MZ-SP): log

- Branch: `claude/padua-mz-paper-20261113` · Base: main `b5388c2` · Developer: Claude · Auditor: Codex (gpt-6-astra)
- Stage: WORK · Next: `Claude (Opus 5.5 xhigh): Continue claude/padua-mz-paper-20261113.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: none (no new mathematics expected).
- Open for AC: companion document only (default none). Venues are decided; the Zenodo deposit will come later, from AC.

## 2026-11-13 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC: "make a brief for a thread to finalize MZ paper".
- Rules read at `b5388c2`. Branch created from main `b5388c2`. Only BRIEF.md, handoff 01, this LOG and the results stub were added.
- BRIEF contents:
  - the manuscript today (25 pages, sections, scope);
  - the PR #31 results to integrate (PD-T522–548: π⁴/8 limit, uniform 5/3, Λ_edge operator limit, signed Padua corner-operator limits), with exact OPEN parts;
  - the literature state after PR #21;
  - AC's manuscript criteria, as recorded in the argmax-manuscript audit brief;
  - reserved decisions and pitfalls.
- No manuscript edit was made, no build run and no claim made.

## 2026-11-13 — Claude, claude-opus-5-5 (configured; effort not exposed) — split decision

- AC asked whether to split; Claude recommended it. AC: "yes let's split. call the one MZ-CC and another one MZ-SP".
- BRIEF §0 (new) and handoff 01 were amended in place before any work began:
  - **MZ-CC** (Clenshaw–Curtis) stays in `tracks/mz-constants/paper/`. It takes current §2–§5 plus PR #31's CC results (π⁴/8, 5/3, η_N, Λ_edge).
  - **MZ-SP** (signed Padua) goes in a new `tracks/mz-constants/paper-sp/`. It takes current §6 plus PR #31's corner operator results, and cites MZ-CC.
  - MZ-CC is finished first.
  - A new task 0a splits the draft with a `split-map.md` (gate W0). Correspondence, plan, notation and response files are now per paper.

## 2026-11-13 — Claude, claude-opus-5-5 (configured; effort not exposed) — venues

- AC: "let's decide on venues now. zenodo will come later."
- AC's choices, from Claude's recommended options:
  - **MZ-CC → SIAM J. Numer. Anal.** (fallback Math. Comp.);
  - **MZ-SP → J. Approx. Theory** (fallback Adv. Comput. Math.).
- BRIEF §0/§5 and handoff 01 task 0 were amended in place: journal classes `siamart` and `elsarticle`, a deposit-DOI placeholder, and only the companion question left for AC.

## Runs needed

- Tasks 0–9 and gates W0–W4 as in handoff 01.
