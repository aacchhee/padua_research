# results-in-repo-20261101 — log

- Branch `claude/results-in-repo-20261101` from main `e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9`. Rules read at `e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9`.
- Role: Claude orchestrator/developer, Opus 5.5 xhigh.
- Stage: AUDIT. This is a rules change, so it follows the ordinary audit cycle (Codex audits Claude work).
- Open handoff: [02-audit.md](handoffs/02-audit.md). [01-audit.md](handoffs/01-audit.md) is superseded.

## 2026-11-01 — AC instructions and the rule change

AC gave two instructions:
- 16:22 Europe/Oslo: "I want `agents/WORKFLOW.md` that says each topic keeps `results/<topic-slug>.md` in repo."
- 16:23 Europe/Oslo: "results.md should be also repo-only. (check that most stuff should work from claude code cloud, only papers and cold storage need the machine)".

**Rule change.** In `agents/WORKFLOW.md` (Computation and evidence), the local-working-track paragraph is replaced:
- Results tracking is repository-only.
- Each topic keeps `results/<topic-slug>.md` on its branch, written only by its orchestrator.
- The repository-root `RESULTS.md` is the merged view, with one section per topic, which each topic updates in its own PR at PR preparation. Integration conflicts are reconciled keeping every section.
- All agent work must be possible from a cloud session. AC's machine is needed only for unfetchable papers (`Downloads\\padua\\papers`) and cold storage (`Downloads\\padua\\cold_storage\\<slug>\\`); when the machine is unreachable, agents record the item as pending and continue.

**Check of the rule files.** I searched AGENTS.md, WORKFLOW.md, CLAUDE_ROLES.md, CODEX.md and the templates for machine dependencies. Apart from the replaced paragraph, the only one is the cold-storage procedure, which is retained.

**Files.** I added `results/README.md` and `RESULTS.md`, and migrated the merged PR #14 topic's results file to `results/padua-mz-2d-20261101.md`. The first commit, `f19bd03`, added that file empty because of a substitution error; `e793105` fills it.

**Not done.** Other topics' local-only results files (bivariate-lanczos, mz-prior-art, programme-ideas, padua-lanczos-drift) and AC's local `Downloads\\padua\\RESULTS.md` were not migrated or edited. Their migration needs AC's go-ahead or their orchestrators. No IDs, science or registries changed.

## Handoffs

- 01: superseded by 02, because of AC's 16:23 follow-up instruction.
- 02: [02-audit.md](handoffs/02-audit.md) is open.
