# Handoff 03 — cold-storage-20261102 — Claude response to audit 01

- Status: open
- Previous handoff: 02-audit.md (done in the input commit)
- Next agent / model / effort: Claude, Sonnet 5.5, high (technical development and metadata corrections)
- Role: developer and topic orchestrator
- Branch: `claude/cold-storage-20261102`
- Input head SHA: `7ec5aad8e3050864cde88e575aae46f39ce49194` (the commit publishing this handoff comes later)
- Main / base: `2b52b432fe59c9a50aef9deebe5152c5d6874465`
- Stage: WORK
- PR: [draft 18](https://github.com/aacchhee/padua_research/pull/18)
- Written by / date: Codex, AC-requested/configured gpt-6-astra high; backend model/effort metadata not separately exposed · 2026-11-02

## Task

Respond to every finding F1–F5 in [audit-01.md](../audit-01.md), with fixes, evidence-based dispositions or explicit unresolved items. Write `topics/cold-storage-20261102/response-01.md`. The audit requires changes; do not mark the PR ready until the material fixes receive a focused Codex re-audit.

1. **F1, destination verification.** Repair `tools/cold_storage.py` so export receipts represent hashes and sizes read from actual destination files. Provide a repeatable way to verify the exported directory independently of the source Git objects, including after transfer. Missing, truncated or corrupted files must fail. Prevent stale successful receipts from surviving a failed refresh in a way that could authorize the separately planned purge. Record what the receipt proves and what it does not.
2. **F2, collision handling.** Preflight restores before writing. Preserve differing local files, tracked modifications and unrelated files. Permit absent and identical regular destinations; reject differing files, directories and symlink destinations/parents by default. If an explicit replacement mode is introduced, document it clearly. Address export collisions too. Add meaningful isolated tests for these failure cases and ordinary successful restore/export/clean; avoid writing over campaign evidence during tests.
3. **F3, complete commands.** Replace clipped generating commands/references in the proof-attempts-2 machine and human manifests with complete recorded commands or precise committed command-block links. Check all long rows. Preserve frozen inputs, historical code/environment pins, unavailable intermediates and OPEN evidence scopes. Do not invent missing executions or parameters, and do not run long scientific campaigns merely to repair metadata.
4. **F4, readers.** Correct charter's false dependency on `cold-storage-manifest.json` for `verify_cold_storage.py` (the latter reads the external bundle manifest). Explicitly list the MZ map's four working-tree readers and give the programme allocator's combined cross-topic restoration prerequisites. Distinguish historical Git readers from worktree readers; restoring files is not a claim that old point-in-time validators accept a later head. Keep all thirteen registry/source files archived with their exact pins.
5. **F5, totals.** Correct the newly authored aggregate totals in the topic log/results/PR body: first 163 files = 15,468,874 bytes; added 13 = 377,215; all 176 = 15,846,089. Individual manifest identities/totals already pass; do not change them to match the erroneous aggregates.
6. Re-run relevant new regression tests, all nine manifest verifications and a destination readback check. Record commands, candidate code/source hashes and environment. Update this topic's log and repository-only results. Update PR #18's WORK/AUDIT/PR sections truthfully; leave it draft with the new re-audit PENDING.
7. Record the effect on PR #17's copy of `tools/cold_storage.py`: after a fix it is no longer automatically identical. Its later integration must retain the corrected tool. Do not silently change or push another topic branch.

## Read first

`AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, this topic's log/results, both prior handoffs, audit 01 and `audit-01/receipt.json`, the tool, and the affected cold-storage manifests/command-source records. Refresh main and topic head before development and record the base/rules SHA. This topic needs **no range**; it changes no mathematical claims or IDs.

The audit drivers `audit-01/inventory.py` and `audit-01/safety.py` reproduce the original pinned candidate; the latter deliberately asserts that the original defects occur. Preserve the audit and its evidence. Write separate regression tests for the repaired behavior rather than editing the auditor's reproduction to count a fix as original acceptance.

## Scope limits

- No history rewrite, force-push, tag, main mutation, merge, settings or `.github/` change. AC's approved purge is a separate future plan, after hash-verified AC delivery and a locator/code preservation plan. This handoff does not execute it.
- `/tmp/padua-cold-audit-export` was independently verified cloud scratch only, not delivery to AC's Windows cold storage. No archival receipt or Windows access is inferred.
- Do not reopen the scientific campaigns, alter proof statuses/IDs, regenerate shared registries, restore large data into Git, or repair pre-existing scientific/audit-checker behavior outside this task.
- The workflow evidence wording is AC-approved and passed this audit; no further rule change is needed for these fixes.
- Do not overwrite audit 01 or earlier handoff bodies. Only this handoff's status changes when its step completes.

## Acceptance and outputs

Commit checked code/metadata fixes and `response-01.md` with a disposition for each F1–F5, log/results updates and compact test receipts. Then, in a separate commit, mark handoff 03 `done in <output-sha>` and open handoff 04 for Codex (`gpt-6-astra`, high) focused re-audit of the changed code, metadata and evidence at the exact output SHA. Link the new handoff from the log, push both commits, and update PR #18. Keep one open handoff. Only AC merges.
