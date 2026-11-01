# Handoff 03 — handoff-id-rules-20261101 — focused audit

A new numbered file for each step, opened by the orchestrator holding the previous handoff. Never overwrite an earlier handoff or alter its body; only the status line changes. AC starts this step with `Codex (gpt-6-astra medium): Continue claude/handoff-id-rules-20261101.`

- Status: superseded by 04: AC requested Codex to finalize PR13 and integrate merged PR6, including the focused audit and PR preparation in this session
- Previous handoff: [02-response.md](02-response.md)

- Next agent / model / effort: Codex, gpt-6-astra medium
- Role: independent auditor (focused re-audit)
- Branch: `claude/handoff-id-rules-20261101`
- Input head SHA: `7e9504b12610682e57c57dce9ac9fd2d37dfe9a7` (response-01 outputs; the following commit only closes handoff 02 and publishes this file)
- Main / base: `21e620ba8b5f0e0706f3a8c6613517df04d9d469`
- Stage: AUDIT
- Written by / date: Claude, claude-opus-5-5 (requested effort high) · 2026-11-01

## Task

Run a focused re-audit of [response-01.md](../response-01.md) against [audit-01.md](../audit-01.md) F1–F4, at the input head. Check the following.

1. **Diff.** The diff from `10f2d85` to the input head (`AGENTS.md`, `agents/WORKFLOW.md`, `templates/HANDOFF.md`, this topic's files) resolves each finding with one consistent, implementable policy.
2. **F1.**
   - The strengthened scan (closed, unmerged PR ledgers plus retired reservations) and the per-namespace maxima are correct.
   - So are the step-7 recheck and the **Priority and collisions** and **Retired reservations** paragraphs.
3. **F2.** The **Transition (adopted 2026-11-01)** paragraph supersedes the single-owner prose without shifting any recorded range, and its import/no-headroom/no-range rules are clear.
4. **F3.** Assess the developer's refinement: the orchestrator holding the open handoff numbers the next one, rather than "the topic orchestrator alone". Check that the open-while-in-progress, completion-commit, `superseded by NN: <reason>` and `withdrawn` lifecycle and the **Input head SHA** field are unambiguous. This handoff chain (01 → 02 → 03) should itself conform.
5. **F4.** The no-audit exemption, the terminal topic with zero open handoffs, and AGENTS.md "while work remains" agree across all files.
6. **Transition statement.** It matches the refreshed heads (#12 advanced to `38db12b`; no closed, unmerged PR). No ID is reserved or changed.

Do not edit the developer's rule files. Propose exact wording for any remaining issue.

## Read first

- `AGENTS.md`, `agents/WORKFLOW.md` and `agents/codex/CODEX.md` at the input head;
- this topic's `LOG.md`, `audit-01.md` and `response-01.md`;
- handoffs 01–03;
- `templates/HANDOFF.md` and `templates/TOPIC_LOG.md`.

## Scope limits

Rules, templates and this topic's records only. No registry, ledger, ID, scientific or other-topic change. Do not reopen points accepted in audit-01 unless the response changed them. Only AC merges.

## Acceptance and outputs

- Write `audit-02.md`: ACCEPTED (Stage PR) or CHANGES REQUIRED, with findings and the checks you actually ran.
- Add a LOG entry and update the PR #13 AUDIT section.
- Commit the outputs. Then, in a following commit, set this handoff to `done in <output-commit-sha>` and open `04-<step>.md`: PR preparation for Claude if accepted, or a response if changes are required. Keep exactly one handoff open.
