# Handoff 01 — workflow-proportionate-20261105 — Codex audit of the rules change

- Status: open
- Previous handoff: none

- Next agent / model / effort: Codex. Use `gpt-6-astra` medium for this protocol audit (WORKFLOW allocation row). The auditor may raise it to high if it finds an integrity risk.
- Role: independent auditor and orchestrator of this step.
- Branch: `claude/elegant-lamport-wkozfa`
- Input head SHA: `2218530058a4571e1ec70ba7380b56395cb0980c` (the commit before this handoff's publication)
- Main / base: `b4d292eea5eed373002506d5e16a3761bd7ae10e`
- Stage: AUDIT
- Written by / date: Claude, Opus 5.5 high (`claude-opus-5-5`) · 2026-11-05

## Task

Audit the rules change `b4d292e..2218530058a4571e1ec70ba7380b56395cb0980c`, which touches:
- `agents/WORKFLOW.md`;
- `agents/claude/CLAUDE_ROLES.md` and `agents/codex/CODEX.md`;
- `templates/HANDOFF.md` and `templates/IDEA.md`;
- the topic log.

AC asked for it in these words:

> "keep one substantive independent audit per batch, with reruns, plus a reservation check at merge tim[e]. In any ping-pongs after 3rd all minor findings should be just fixed by auditor in place."

AC also approved the simplifications Claude had proposed:
- no process-stage text in shared registries;
- hash-pin code and data, not prose;
- registry application by reviewed diff instead of OLD→NEW proposal files and receipts;
- disclose once and link;
- a new handoff only when work passes to another agent or session.

AC then confirmed: "this rules change should be audited by codex".

Check the following:
1. **Faithfulness.** Each requested item is implemented, and nothing beyond it. Give an explicit view on two interpretations, which are flagged in the LOG for AC:
   - "after 3rd" is read as *including* the third audit round;
   - draft-time reservation is dropped, in favour of reserving when IDs are first needed and rechecking at readiness.
2. **Consistency.** No sentence in AGENTS.md, WORKFLOW, the role files or the templates still contradicts the new rules.
3. **Integrity.** The in-place auditor-fix exception cannot change claims, statuses, results or IDs. "Material change" is tight. The readiness reservation recheck still prevents collisions. Retired-reservation, priority and collision rules are intact.
4. **Clarity.**

The supplementary Claude review and its 13 dispositions are recorded in the LOG. Do not inherit its conclusions.

## Read first

- AGENTS.md and the full new `agents/WORKFLOW.md` at the input head, and both role files.
- `templates/*.md`.
- `git diff b4d292e 2218530058a4571e1ec70ba7380b56395cb0980c`.
- The topic LOG.

## Scope limits

- Rules files and this topic only; no scientific records or registries.
- Do not merge; only AC merges.
- Codex may fix MINOR wording in place, and must list each fix.
- Codex does not push to `main`.

## Acceptance and outputs

- **Report:** write `topics/workflow-proportionate-20261105/audit-01.md` with:
  - the audited SHA, model and effort;
  - the files read;
  - findings by severity, with exact locations;
  - any in-place MINOR fixes, committed separately;
  - a verdict.
- **Update** the LOG and the PR body.
- **If accepted:** mark the PR ready for AC and close this handoff with no successor (topic complete).
- **If MAJOR findings remain:** open `02-response.md` for Claude, Opus 5.5 high.
