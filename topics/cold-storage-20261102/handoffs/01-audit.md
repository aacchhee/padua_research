# Handoff 01 — cold-storage-20261102 — Codex protocol audit of the repository cold-storage cleanup

- Status: superseded by 02: AC approved the WORKFLOW wording, the move of the 13 retained files and a later force-push (LOG 2026-11-02)
- Previous handoff: none

- Next agent / model / effort: Codex, `gpt-6-astra`, medium or high (auditor's choice, recorded); a protocol and technical audit
- Role: independent auditor
- Branch: `claude/cold-storage-20261102`
- Input head SHA: `b26acf6c74b07a031b34266b64be74f63e340224` (the commit that publishes this file comes later)
- Main / base: `2b52b432fe59c9a50aef9deebe5152c5d6874465`
- Stage: AUDIT
- Written by / date: Claude, configured `claude-opus-5-5` xhigh · 2026-11-02

## Task

Audit the cleanup described in [LOG](../LOG.md) against AC's instruction and the repository rules. Write `topics/cold-storage-20261102/audit-01.md`.

1. **Completeness.**
   - `git diff --stat 2b52b43 <input head>`: every deleted file must appear in exactly one `cold-storage.json`.
   - No other file may be deleted.
   - Every generated data file of 16 KiB or more left at the head must be either a cold-storage manifest or a listed "retained" file with a valid reason.
2. **Exactness.** For each of the 9 directories:
   - run `python tools/cold_storage.py verify <slug>`;
   - on at least two topics, also run `restore`, compare the restored bytes with `git show 2b52b43:<path>`, and then run `clean`.
3. **Retained exceptions.** Judge whether each of the 13 retained files (hand- or agent-authored registry and source data) is rightly kept, or should move.
4. **Commands and summaries.**
   - Spot-check a sample of entries in each topic: does the generating command name committed code with the right arguments, and does the cited summary exist and support the records that cited the moved file?
   - Regenerate at least two cheap entries and compare them.
   - Flag any wrong command or summary.
5. **Links and edits.**
   - Confirm that the 76 link redirects changed only link targets.
   - Confirm that no theory statement, status, ID or audit verdict changed.
   - Confirm that appended `COLD_STORAGE.md` sections leave earlier text intact.
6. **Rule change.** Review the `agents/WORKFLOW.md` evidence paragraph for consistency with AGENTS.md and the rest of WORKFLOW. AC must approve it. Your audit is necessary but not sufficient.
7. **Tool.** Review `tools/cold_storage.py` for correctness and safety. In particular, `clean` must delete only untracked restored copies whose bytes match.

## Read first

`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, this topic's LOG, `templates/COLD_STORAGE.md`, the 9 `cold-storage.json` files and `COLD_STORAGE.md` sections, and `tools/cold_storage.py`.

## Scope limits

- Do not edit the change yourself and then approve it; return findings.
- No main mutation, merge, force-push, tag, settings or `.github/` change.
- Do not rewrite history.
- Do not reopen any topic's science.

## Acceptance and outputs

- **Audit file.** `audit-01.md` with model and effort, audited SHA, the commands actually run, findings by severity, and a verdict.
- **Commits.** Commit the audit, then set this handoff to done and open handoff 02:
  - if accepted, for PR readiness and AC's merge decision;
  - if there are findings, for a Claude response.
- **Merge sequencing.** This PR changes files of merged topics, and PR #17 adds the same tool file. Only AC merges. The recommended order is this PR first, then PR #17 merging main, with no conflict expected because `tools/cold_storage.py` is identical.
