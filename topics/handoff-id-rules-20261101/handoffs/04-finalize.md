# Handoff 04 — handoff-id-rules-20261101 — final audit and PR preparation

- Status: done in 49da38c4287f132a3db3bf936f8f194954eb0ec3
- Previous handoff: [03-audit.md](03-audit.md)
- Next agent / model / effort: Codex, gpt-6-astra medium (AC-requested; resolved runtime metadata unexposed)
- Role: independent protocol auditor and integration orchestrator
- Branch: `claude/handoff-id-rules-20261101`
- Input head SHA: `fcb334c7f0ef055695b8f2633692092865366ddb`
- Main / base: `a7e123476cef761807c69e5d0af1a094c7ac3df0` (merged PR #6)
- Stage: AUDIT, then PR if accepted
- Written by / date: Codex · 2026-11-01

## Task

AC's instruction overrides handoff 03's separate Claude preparation step: "Make pr13 final, integrate merged pr6". Codex completes the focused independent audit of Claude's response-01, integrates current main, verifies preservation and prepares PR #13 in this session. Main was merged without conflicts in the input commit; do not merge the PR itself.

Read the rules and Codex role file, LOG, audit-01, response-01, handoffs 01–03, both templates and the merged ledger. Audit F1–F4 against response input `7e9504b12610682e57c57dce9ac9fd2d37dfe9a7` and published candidate `ac4ff3fd32d73880048e38d096bbcfb58df8a724`. Confirm the merged Fable amendment is the only rule difference introduced by main integration. Accept or return actual findings without rewriting Claude's rule content and self-approving it.

If accepted, write audit-02 and a PR-preparation record, confirm no PR #6 records or allocations differ from main, verify earlier audit/handoff bodies, run a disposable squash rehearsal of current main followed by this PR and record exact trees. Refresh main/open-PR reservations, keep this rule-only topic at "no range", and update PR #13 with current WORK/AUDIT/PR sections. Push and mark it ready for review only after acceptance and checks.

## Scope limits

No scientific, registry, allocation or other-topic edits. Preserve the merged PR #6 content and existing reservations, all prior reports and handoff instruction bodies. No new claims, .github/settings/tag changes, force push, published-history rewrite or live PR merge. Only AC merges.

## Acceptance and outputs

- `audit-02.md` records independent F1–F4 dispositions and the integrated input identity.
- `pr-prep.md` records merge/preservation/rehearsal results and the current transition, with no pending agent preparation work if all checks pass.
- LOG records AC's scope override, rules SHA, base/head and actual checks.
- Commit outputs first, then close this handoff with the real output-commit SHA in a following commit. When the assigned finalization is complete, leave no open successor and no continuation prompt. PR #13 remains for AC's merge decision.
