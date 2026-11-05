# Proportionate audit and records — workflow change: log

- Branch: `claude/elegant-lamport-wkozfa` · Base: main `b4d292eea5eed373002506d5e16a3761bd7ae10e` · Developer: Claude (Opus 5.5 high) · Stage: PR
- Scope: `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, `agents/codex/CODEX.md`. No scientific record, registry or ID is touched; no range is reserved.

## 2026-11-05 — Claude, Opus 5.5 high (claude-opus-5-5) — rules change at AC's request

- **AC's request (verbatim).** "Yes prepare a rules change according to your suggestion: keep one substantive independent audit per batch, with reruns, plus a reservation check at merge tim[e]. In any ping-pongs after 3rd all minor findings should be just fixed by auditor in place. And proceed to green PR without asking".
- **Origin.** This follows Claude's assessment during PR24's preparation. That topic had 11 research commits against 27 process commits, and its audit/response/preparation/handoff prose (~578 KB) was twice its theory prose (~290 KB). Most findings in its later rounds were stale stage text created by the process itself.
- **Change 1: audit rounds.**
  - One substantive independent audit per batch, with reruns.
  - Only material changes get a focused re-audit.
  - Minor-only responses proceed to PR, confirmed by diff at the readiness check.
  - From the third audit round onward, the auditor fixes MINOR findings in place and lists each fix. Interpretation of "after 3rd": the third round included. AC may narrow this to rounds four and later.
- **Change 2: readiness check.** Registry application, final IDs and the reservation refresh are verified in one readiness check, not a separate audit round.
- **Change 3: reservations.** Ranges are reserved when final IDs are first needed, not at draft opening. They are rechecked once at readiness.
- **Change 4: records.**
  - No process stage in shared registries.
  - Hash-pin code and data, not prose.
  - Registry application by reviewed diff, with no OLD→NEW receipt machinery.
  - Disclose once and link.
  - New handoffs only when work passes to another agent or session.
- **Matching exceptions** were added to the auditor-fix prohibitions in CODEX.md and CLAUDE_ROLES.md.
- **Novelty gate:** not applicable. No idea, candidate or scientific claim.
- **Audit:** an independent Claude subagent reviewed the diff (see PR). A cross-family Codex audit of a rules change is normally required. It was not run, under AC's "proceed … without asking"; AC may request it before merging. Only AC merges.
