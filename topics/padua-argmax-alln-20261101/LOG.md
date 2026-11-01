# All-degree Padua argmax (A4 / PD-T099): strategy topic

- Branch: `claude/padua-argmax-alln-20261101` · Base: `28aaa20861d08074b77efc74eaef75cdcb36234d` (main) · Developer: Claude · Auditor: Codex (when a result is claimed)
- Stage: WORK (planning) · Next: `Claude (Opus 5.5 xhigh): Continue claude/padua-argmax-alln-20261101.` · Open handoff: [handoffs/01-update-after-part2.md](handoffs/01-update-after-part2.md)
- Reserved final-ID ranges: none yet. No PR is open; reserve by the WORKFLOW fresh-range procedure when the draft PR opens.
- Claims:
  - PD-T?argmax-alln-claude-01 — float64 majorant/gap observations — MEASURED — [theory](theory/argmax-alln-claude-01-measured-observations.md).
  - IDEA?argmax-alln-claude-01 — REJECTED: failed (MEASURED).
  - IDEA?argmax-alln-claude-02…04 — deferred. See [ideas.md](ideas.md).
- For the PR: register the IDEA and PD-T rows, `results/padua-argmax-alln-20261101.md` → `RESULTS.md` section, Codex audit.
- Open for AC: none. The plan is to be updated after part 2 (PR #12) is done.

## 2026-11-01 — Claude, claude-opus-5-5 (configured; effort not exposed)

- Role: orchestrator and developer. Rules read at `28aaa20861d08074b77efc74eaef75cdcb36234d`: AGENTS.md, agents/WORKFLOW.md (including the repository-only results rule from PR #16), agents/claude/CLAUDE_ROLES.md.
- Trigger: AC asked for ideas toward an all-n proof of the A4 argmax ("any ideas how to create complete proof for all n in pr12?"), then "write this down on a new branch, then we'll update it after part2 is done".
- Pinned inputs:
  - main `28aaa20`;
  - part 2 `codex/padua-proof-attempts-2-20261101` at `b5bba7cf1328b1f207aea001a439c3fe4af0146f` (read only; LOG claims lines and theory list; records 70–73 by title and LOG summary only);
  - programme-ideas OPEN_TARGETS A4 (on main).
- Changes and evidence:
  - [plan.md](plan.md) (strategy), [gate.md](gate.md) (novelty gate), [ideas.md](ideas.md) (four candidates), and the MEASURED [observations record](theory/argmax-alln-claude-01-measured-observations.md).
  - Code: code/maj.py, check.py, cell.py, interior.py. Outputs: outputs/*.out and environment.txt. The scripts were first run in chat exploration, then rerun on this branch to produce the committed outputs.
- Novelty gate: [gate.md](gate.md). The closest entry is IDEA-206 (owner of PD-T099). Verdicts: variants or new within the documented search. No literature claim.
- Kill criteria: written in [ideas.md](ideas.md) and plan §5 before any test, except IDEA-01, whose test (cell.py) ran in chat before this file existed. Its kill criterion ("max S > S(coset) at any n ≥ 3") is recorded retrospectively and the output is unchanged.
- Subagents: none.

## Runs needed

- Independent rerun of `code/check.py`, `code/cell.py` and `code/interior.py` (commands in the observations record), by an agent other than Claude, before any result here is used as evidence in a PR.
- The plan §5.1 profile-convergence test and the §5.2 monotonicity test: not run. They are scheduled for the post-part-2 continuation.
