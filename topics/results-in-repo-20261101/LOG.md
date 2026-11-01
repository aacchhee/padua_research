# results-in-repo-20261101 — log

- Branch `claude/results-in-repo-20261101` from main `e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9`. Rules read at `e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9`.
- Role: Claude orchestrator/developer, Opus 5.5 xhigh.
- Stage: WORK. Codex audit-01 accepts the rule change and returns three summary findings for Claude's response. PR #16 stays draft.
- Handoff chain: [handoffs/](handoffs/). The numbered status lines identify the one open step. [01-audit.md](handoffs/01-audit.md) is superseded.

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
- 02: [02-audit.md](handoffs/02-audit.md), audit output below; its status is closed in the following publication commit.
- 03: Claude response to audit-01, published after the audit output commit.

## 2026-11-01 — Codex protocol audit

- Role: independent auditor and this step's orchestrator. Requested model/effort: gpt-6-astra medium; runtime serving metadata is not independently attested.
- Rules read at full SHA `f628a1f873572d43a625befda422ba0af49d5c48`; audited candidate `715b1823bee0c5053c8376310a39b1f12c48e3ac`. Refreshed main `e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9` is already an ancestor; no merge needed. PR14 head and squash trees match exactly.
- [audit-01.md](audit-01.md): repository-only storage, cloud rules and unchanged evidence limits PASS. F1 P2 restores the source norm/reproduction constraints; F2 P3 corrects m40 certification-method provenance; F3 P3 adds the required durable-record/evidence links. No developer deliverable was edited by the auditor.
- [audit-checks-01.json](audit-checks-01.json) records mechanical checks and source hashes. No scientific computation was rerun or mathematical status upgraded. No novelty content, so the full ideas read is omitted. **No range**; no IDs allocated or reassigned.
- Next: Claude response-01 and preparation checks; only exact source transcriptions and links are authorized by this disposition. Wider changes return to AUDIT. PR16 remains draft. Other topics' migrations and AC's machine are outside scope.

## 2026-11-01 — response-01 (handoff 03)

Claude acted as developer and topic orchestrator. AC requested Sonnet 5.5 medium; the configured session model is `claude-opus-5-5`, recorded truthfully. Rules were read at `e62b19d8152c54ffd84eb824c94666a1590962e6`, and main `e0d9e3d` is unchanged.

- **Findings.** Answered Codex audit-01 F1–F3 in [response-01.md](response-01.md).
  - F1: transcribed the PD-T112 unit-L² domain and the PD-T113 range 0 ≤ r ≤ n, n+r ≤ m.
  - F2: separated the m10–30 Sylvester-minor checks from the m40 Addendum A1 congruence certificate, keeping A1's caveat.
  - F3: added a grouped source trail and per-ID record links.
  - Also fixed a stale merge-status line.
- **Results files.** Added [results/results-in-repo-20261101.md](../../results/results-in-repo-20261101.md) and this topic's root `RESULTS.md` section. The PR14 section is preserved.
- **Checks.**
  - 57 local links resolve, including the A1 anchor.
  - `git diff --check` is clean.
  - No rule, template, theory, code or evidence file changed in the response.
- **Next.** Readiness decision for AC ([handoff 04](handoffs/04-readiness.md)). No ID range is needed.
- 03 → done in `9c4a69c41f0e7355a8c6768cee94693ffad6106d`; [04-readiness.md](handoffs/04-readiness.md) is open for AC.
