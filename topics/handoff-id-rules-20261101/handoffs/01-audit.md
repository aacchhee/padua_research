# Handoff 01 — handoff-id-rules-20261101 — audit

AC starts this step with `Codex (gpt-6-astra medium): Continue claude/handoff-id-rules-20261101.`

- Status: open
- Previous handoff: none

- Next agent / model / effort: Codex, gpt-6-astra medium (protocol audit)
- Role: independent auditor
- Branch / head SHA / base: claude/handoff-id-rules-20261101 · head: the commit that contains this file (see `git log -1`) · main `21e620ba8b5f0e0706f3a8c6613517df04d9d469`
- Stage: AUDIT
- Written by / date: Claude, claude-opus-5-5 · 2026-11-01

## Task

Audit this rule change, which AC requested. In `audit-01.md` in this directory, check the following.

1. The new text in `AGENTS.md`, `agents/WORKFLOW.md` (Work cycle; Audit and PR records), `templates/HANDOFF.md` and `templates/TOPIC_LOG.md`, as amended in the second commit (numbered handoffs that are never overwritten, at AC's 2026-11-01 request), implements AC's two requests:
   - fresh, non-overlapping ID ranges, checked against main and all open PRs including drafts, recorded at once, never reallocated;
   - numbered handoff files carrying the full next-step instruction, never overwritten, with a short `Continue <branch>.` prompt.
2. It contradicts no other rule: the single ledger, provisional IDs, PR-preparation assignment, `state/IDEAS.md` timing, the rehearsal, and the AC-precedence clause.
3. The wording is unambiguous about:
   - who owns a range;
   - what happens on a collision;
   - when reservation is required;
   - whether a `no audit` small job needs a handoff file;
   - how "exactly one open handoff" and the status line work when AC redirects mid-step or when two agents work in parallel.
4. Transition: say how the open drafts (#9, #11 and #12, and #6 if not yet merged) should comply, and whether their existing reservations (PR #11's LIT-293–299; PR #6's allocated blocks, if merged) are already consistent with the new rule.

Propose exact wording fixes for anything you find. Do not edit the developer's rule files yourself.

## Read first

`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md` at the head; `LOG.md` here; `topics/padua-batch-20261031/ALLOCATIONS.md` on main and on the open draft branches.

## Scope limits

Rules and templates only. No registry, ID or scientific change. Only AC merges.

## Acceptance and outputs

- Write `audit-01.md` (ACCEPTED or CHANGES REQUIRED, with findings).
- Add a LOG entry.
- Set this handoff's status to `done in <sha>`.
- Open `handoffs/02-<step>.md` for the next step: Claude's response if changes are required, or PR preparation if accepted.
- Update the PR body's AUDIT section.
