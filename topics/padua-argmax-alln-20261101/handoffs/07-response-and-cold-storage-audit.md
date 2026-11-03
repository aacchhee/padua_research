# Handoff 07 — padua-argmax-alln-20261101 — Codex response to audit-01 and audit of the cold-storage move

- Status: done in 4e19a5695333db74492845e7ec33e2f479226df7
- Previous handoff: 06-response.md (superseded by this handoff)

- Next agent / model / effort: Codex, `gpt-6.1-sol` high, for the response.
  - For the protocol audit of the Claude-made cold-storage change, Codex chooses `gpt-6-astra` medium or high and records the choice.
  - The two roles are kept separate: Codex responds to Claude's audit, and audits Claude's cold-storage development.
- Role: developer (response) and independent protocol auditor (cold storage)
- Branch: `claude/padua-argmax-alln-20261101`
- Input head SHA: `6fae535df28303b27ca1d533d9afa229660a3a20`
  - This is the cold-storage output commit; the commit publishing this file comes later.
  - The audit output is `381050a5fb13051b4ea97b707767d012cc417cf5`. The audited scientific input is `c173fbf7ee66f02cc1d992e52edb43fdbd819474`.
- Main / base: `2b52b432fe59c9a50aef9deebe5152c5d6874465` (refresh and reconcile first)
- Stage: WORK
- PR: [draft 17](https://github.com/aacchhee/padua_research/pull/17)
- Written by / date: Claude, configured `claude-opus-5-5` xhigh · 2026-11-02

## Why this replaces handoff 06

After audit-01, AC instructed: "I do not think that we have to store large outputs that can be regenerated. Make sure that all needed code is in the repo, some short summaries are stored and expunge the large data files (cold storage)". AC then added: "18 mb per repo is too much."

Claude applied this to this topic in `6fae535`:
- Every generated data file of 16 KiB or more (36 files, 2,526,191 bytes) left the branch head.
- They are recorded in [COLD_STORAGE.md](../COLD_STORAGE.md) and [cold-storage.json](../cold-storage.json), each with SHA-256, Git blob at pushed `1cecd68`, generating command and summary location.
- The new tool is [`tools/cold_storage.py`](../../../tools/cold_storage.py).

The cleanup of other topics goes in a separate repository-wide branch and PR, which is out of this handoff's scope.

Handoff 06's instruction body remains valid **except** for the changes below.

## Task

### A. Response to audit-01, in `response-01.md`

Follow handoff 06, Task and "Decide or defer", item by item for F1–F15 and N1–N14, with these changes:

1. **F1.** The T1 split files are now in cold storage, not at the head.
   - Respond to the finding: correct the rationale at `attempts/T1-T5.md:62-64` with a dated note.
   - State that the full T1 output is retrievable byte-exactly as one artifact, via cold storage and the raw-replay hash `4d7792e6…` recorded in audit-01.
   - Change `code/part3/tests_analyze.py` only if the response needs to. If it changes, record that the analysis is unchanged.
   - Do **not** re-commit the large T1 data.
2. **Evidence manifest.** Refresh `evidence-manifest.json` (handoff 06 item 1) so that it reflects the cold-storage state.
   - Moved files are covered by `cold-storage.json`, which pins every moved file's hash and blob.
   - Adapt `check_evidence.py` so that its plain check either verifies the cold-storage entries through `tools/cold_storage.py verify` or excludes them explicitly.
   - If the refreshed manifest is 16 KiB or more, either keep it as the topic's single integrity manifest and justify that in the response, or move it by the same procedure. AC may set a different rule.
   - Run the plain check and record its output.
3. **N10 is superseded by AC's instruction.** Generated data stays at or below 16 KiB per file at the head, apart from `cold-storage.json` and any justified integrity manifest.
4. **New outputs must also follow this rule.** Anything larger goes to cold storage with a manifest row.

### B. Independent protocol audit of the cold-storage change, in `audit-02-cold-storage.md`

Audit Claude's commit `6fae535` against `1cecd68`.
- **Completeness:** `git diff --stat 1cecd68 6fae535`. Every deleted file must be in `cold-storage.json`, and nothing else may be deleted.
- **Exactness:** run `python tools/cold_storage.py verify padua-argmax-alln-20261101`. Then `restore` it, compare the restored bytes with `git show 1cecd68:<path>` for every entry, and `clean`.
- **Commands:** spot-check that each generating command names a committed script and the right arguments. Regenerate at least one entry and compare it.
- **Summaries:** for each moved file, check that a short committed summary or receipt still supports every record that cites it.
- **Links and records:** check the five redirected links and LOG/results wording. Confirm no claim's status changed and no scientific record was altered.
- **Tool:** review `tools/cold_storage.py` for correctness and safety. In particular, `clean` must delete only untracked restored copies whose bytes match.

Findings go to the Claude orchestrator. Do not fix Claude's change and approve it yourself.

## Read first

At the branch head:
- `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`;
- LOG, including the 2026-11-02 cold-storage entry;
- [audit-01](../audit-01.md) and its sub-reports;
- handoff 06;
- COLD_STORAGE.md, `cold-storage.json` and `tools/cold_storage.py`.

## Scope limits

Handoff 06's scope limits apply unchanged:
- no new mathematics;
- no statement or status changes;
- PD-T099 remains OPEN;
- no final IDs or shared-registry edits;
- no main mutation, merge, force-push, tag, settings or `.github/` change;
- only the orchestrator controls Git.

In addition:
- Do not re-commit cold-stored data.
- Do not rewrite history to purge blobs. Purging history is AC's decision alone.
- Do not edit the repository-wide cleanup branch from here.

## Acceptance and outputs

- **Files:** `response-01.md` and `audit-02-cold-storage.md`, plus the record fixes, the refreshed manifest with its passing plain check, and updated LOG and results.
- **If nothing material changed and the cold-storage audit passes:** set AUDIT for a Claude protocol check of the response (Sonnet 5.5 high or Opus 5.5 high), then PR preparation.
- **If the cold-storage audit has findings:** route them to Claude in the next handoff.
- **Commits:** commit the outputs first. In a following commit, set this handoff to `done in <output-sha>` and add handoff 08.
- **PR 17:** update its sections. It stays a draft; only AC merges.
