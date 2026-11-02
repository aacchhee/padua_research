# Handoff 04 — cold-storage-20261102 — focused Codex re-audit of response-01

- Status: open
- Previous handoff: 03-response.md (done in the input commit)

- Next agent / model / effort: Codex, `gpt-6-astra` high
- Role: independent auditor
- Branch: `claude/cold-storage-20261102`
- Input head SHA: `8c3a2c466ef0f7c2a7a5b4bf454df9ea7d52687c` (the commit that publishes this file comes later)
- Main / base: `2b52b432fe59c9a50aef9deebe5152c5d6874465`
- Stage: AUDIT
- PR: [draft 18](https://github.com/aacchhee/padua_research/pull/18)
- Written by / date: Claude, configured `claude-opus-5-5` high · 2026-11-02

## Task

Re-audit [response-01](../response-01.md) at the input SHA and write `audit-02.md`. Keep your audit-01 and its evidence unchanged; write a separate report.

1. **Code: `tools/cold_storage.py` and `tools/test_cold_storage.py`.**
   - Confirm that the base is byte-identical to Codex's PR #17 repair at `b70edfc` (`d12fc95d…` and `0aac0194…`) apart from Claude's additions, using `diff <(git show b70edfc:tools/cold_storage.py) tools/cold_storage.py`.
   - Review the additions:
     - destination readback before the v2 receipt, and receipt readback;
     - no receipt on mismatch;
     - receipt fields and wording;
     - the new `verify-archive` command, offline and with `--manifest`;
     - the four new tests.
   - Write your own fault tests: corruption after write; transfer and truncation; a stale receipt; a changed manifest; v1 receipts.
   - Confirm that no guarantee is overclaimed. In particular, a receipt must never be treated as proof of current presence or as purge authorization.
2. **F3/F4 metadata.**
   - Check that no identity tuple changed in any of the nine `cold-storage.json` files, against `1a9220c`.
   - Check that no clipped or ellipsis values remain.
   - Sample the proof-attempts-2 commands against their cited records: n3–n8 producers, checkers and controls; the n8 five-step chain; the n4 independent environment.
   - Check the charter, MZ, allocator and 13-row reader claims at their `file:line` evidence.
3. **F5.** Recompute the three Git-measured totals.
4. **Regression.** Run `tools/test_cold_storage.py`, all nine `verify` runs, and an export → `verify-archive --manifest` → `verify --dest` → clean cycle on at least two directories.

## Read first

`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, this topic's LOG, audit-01, response-01, and PR #17's `topics/padua-argmax-alln-20261101/audit-03-storage-repair.md` (context for the adopted base).

## Scope limits

- Return findings; do not fix and approve.
- No history rewrite, force-push, tag, main mutation, merge, settings or `.github/` change.
- The purge AC approved waits for a hash-verified AC delivery checked with `verify-archive` at that time, and for both PRs to be merged.
- Do not change PR #17's branch.

## Acceptance and outputs

- Commit `audit-02.md`, then mark this handoff done.
- Open handoff 05:
  - if accepted, for PR readiness and AC's merge decision (draft lifted only if all gates pass);
  - if there are findings, for a Claude response.
- Update PR #18. Only AC merges.
