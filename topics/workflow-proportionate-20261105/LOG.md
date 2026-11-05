# Proportionate audit and records — workflow change: log

- Branch: `claude/elegant-lamport-wkozfa` · Base: main `b4d292eea5eed373002506d5e16a3761bd7ae10e` · Developer: Claude (Opus 5.5 high) · Auditor: Codex · Stage: AUDIT · Open handoff: [handoffs/02-audit.md](handoffs/02-audit.md)
- Scope: `agents/WORKFLOW.md`, both role files, `templates/HANDOFF.md`, `templates/IDEA.md`, and this topic’s records. No scientific record, registry or ID is touched; no range.

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
- **Audit:** a cross-family Codex audit is required. When the rules note above was first written it said that audit had not been run; AC then confirmed: "Well this rules change should be audited by codex yes". The PR stays draft with AUDIT PENDING until Codex audits it. Only AC merges.

## 2026-11-05 — supplementary Claude review and revisions

- A separate Claude Opus 5.5 high subagent reviewed `b4d292e..c049f51` read-only. Verdict REVISE: three MAJOR wording issues and several MINOR ones.
- This review is supplementary. It does not replace the Codex audit.
- All findings were applied in the following commit:
  1. "Material change" now has one tight definition, used by the re-audit rule, step 5 and the auditor-fix limits. In doubt, a change is material.
  2. Registries may still carry links to theory, evidence and completed audit records. Only pending or in-progress process is excluded.
  3. "Disclose once" covers protocol and process limitations only. A claim's scope and limitations stay in its theory record.
  4. A response that changes no claim and rejects a finding with reasons proceeds to PR, with the disagreement preserved. A MINOR-only response that turns out to contain a material change returns to AUDIT.
  5. The in-place auditor fixes are limited to:
     - wording and formatting;
     - links;
     - stale process text;
     - recording an already documented decision.

     They are committed separately from the audit report. The developer may dispute them, and uncertain cases return as MAJOR.
  6. The general disagreement and draft sentences are back in their own paragraph.
  7. The handoff rules are aligned throughout: the opening sentence, the HANDOFF template, and a definition of "passes work on".
  8. The hash-pin rule no longer contradicts itself. Evidence may be pinned whatever its format, audited prose is identified by SHA, and an already pinned record is corrected by re-pin or companion.
  9. The severity scale is defined.
  10. The readiness recheck is a full rerun of steps 1–3, repeated if heads change before AC merges.
  11. This log no longer reports the review before it existed.
  12. "Batch" is defined.
  13. The IDEA template no longer invites pending process stage into the shared registry.

## 2026-11-05 — AC confirms the interpretations

- AC: "Confirm the readings". Two readings of AC's request are now confirmed:
  - "after 3rd" includes the third audit round, so the auditor fixes MINOR findings in place from round three onward;
  - draft-time reservation is dropped, in favour of reserving when final IDs are first needed and the full recheck at readiness.
- The rules text already implements both, so no rules file changes.
- Handoff 01 had not been started by Codex and is superseded by [handoff 02](handoffs/02-audit.md), which drops the request for Codex's view on these two choices. The Codex audit remains required.
