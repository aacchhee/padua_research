# Handoff — handoff-id-rules-20261101

Overwritten at the end of every step; history is in Git and `LOG.md`. AC starts the next step with `Codex (gpt-6-astra medium): Continue claude/handoff-id-rules-20261101.`

- Next agent / model / effort: Codex, gpt-6-astra medium (protocol audit)
- Role: independent auditor
- Branch / head SHA / base: claude/handoff-id-rules-20261101 · head: the commit that contains this file (see `git log -1`) · main `21e620ba8b5f0e0706f3a8c6613517df04d9d469`
- Stage: AUDIT
- Written by / date: Claude, claude-opus-5-5 · 2026-11-01

## Task

Audit this rule change, which AC requested. In `audit-01.md` in this directory, check the following.

1. The new text in `AGENTS.md`, `agents/WORKFLOW.md` (Work cycle; Audit and PR records), `templates/HANDOFF.md` and `templates/TOPIC_LOG.md` implements AC's two requests:
   - fresh, non-overlapping ID ranges, checked against main and all open PRs including drafts, recorded at once, never reallocated;
   - a handoff file carrying the full next-step instruction, with a short `Continue <branch>.` prompt.
2. It contradicts no other rule: the single ledger, provisional IDs, PR-preparation assignment, `state/IDEAS.md` timing, the rehearsal, and the AC-precedence clause.
3. The wording is unambiguous about:
   - who owns a range;
   - what happens on a collision;
   - when reservation is required;
   - whether a `no audit` small job needs a handoff file.
4. Transition: say how the open drafts (#9, #11 and #12, and #6 if not yet merged) should comply, and whether their existing reservations (PR #11's LIT-293–299; PR #6's allocated blocks, if merged) are already consistent with the new rule.

Propose exact wording fixes for anything you find. Do not edit the developer's rule files yourself.

## Read first

`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md` at the head; `LOG.md` here; `topics/padua-batch-20261031/ALLOCATIONS.md` on main and on the open draft branches.

## Scope limits

Rules and templates only. No registry, ID or scientific change. Only AC merges.

## Acceptance and outputs

- Write `audit-01.md` (ACCEPTED or CHANGES REQUIRED, with findings).
- Add a LOG entry.
- Overwrite this `HANDOFF.md` for the next step: Claude's response if changes are required, or PR preparation if accepted.
- Update the PR body's AUDIT section.
