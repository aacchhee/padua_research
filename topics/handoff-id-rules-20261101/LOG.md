# Handoff file and fresh-range ID reservation rules

- Branch: claude/handoff-id-rules-20261101 · Base: main `21e620ba8b5f0e0706f3a8c6613517df04d9d469` · Developer: Claude · Auditor: Codex
- Stage: AUDIT · Next: `Codex (gpt-6-astra medium): Continue claude/handoff-id-rules-20261101.` · Open handoff: [handoffs/01-audit.md](handoffs/01-audit.md)
- Reserved final-ID ranges: none (rule change only; no PD-T, PD-N, IDEA or LIT entry).
- Open for AC: whether existing open drafts (#9, #11, #12) should record reservations under the new rule now or at their next step.

## 2026-11-01 — Claude (claude-opus-5-5; requested effort high)

- Rules read at main `21e620ba8b5f0e0706f3a8c6613517df04d9d469`.
- AC's request: (1) when a draft PR is made, or at any other allocation stage, check not only free IDs but also those allocated by other draft PRs, and start a new range, so that reallocation stops; (2) long next-step instructions are recorded in a handoff file in the repo, so that AC only says "continue branch".
- Changes:
  - `AGENTS.md`: the reply ends with a short `Continue <branch>.` prompt; the full instruction goes in a handoff file.
  - `agents/WORKFLOW.md`, Work cycle: the meaning of `Continue <branch>.`, and the handoff-file rule (overwrite per step, commit and push before replying, AC's message takes precedence).
  - `agents/WORKFLOW.md`, Audit and PR records: "reserve fresh ranges; never reallocate". The scan covers main and all open PRs including drafts. New ranges start above the highest used or reserved ID and are recorded at once, with headroom; gaps are permanent; more IDs come from a new range; no renumbering. The single-allocation-owner sentence is replaced by per-branch ownership of recorded ranges.
  - New `templates/HANDOFF.md`.
  - `templates/TOPIC_LOG.md` header: a handoff link and a reserved-ranges line.
- Motivation: the 2026-11-01 batch needed repeated reconciliation. PR #6's planned range was overtaken by PR #10's allocation, and then by PR #11's LIT-293–299 reservation.
- No scientific content; the novelty gate does not apply.

## 2026-11-01 — Claude (claude-opus-5-5; requested effort high), amendment before audit

- AC: "I would rather open a new handoff, not overwrite old ones. might be good to have to be able to track some things".
- Change: handoffs are now numbered files `topics/<slug>/handoffs/NN-<step>.md` that are never overwritten. Only the status line changes (`open`, then `done in <sha>`, `superseded by NN` or `withdrawn: <reason>`), and exactly one handoff is open at a time. `Continue <branch>.` reads the latest open handoff. AGENTS.md, the WORKFLOW Work cycle and both templates are updated.
- This topic's own handoff has moved to [handoffs/01-audit.md](handoffs/01-audit.md), still open. It had not been taken up yet.
