# Handoff 03 — padua-mz-cleanup-20261105 — developer response to Claude audit 01

- Status: open
- Previous handoff: 02-audit.md
- Next agent / model / effort: Codex, gpt-6.1-sol xhigh
- Role: developer and topic orchestrator for this step
- Branch: codex/padua-mz-cleanup-20261105
- Input head SHA: `a399e3cf493413c7dd97aa4e620da9c732e52ff9` (audit-01 output commit; this file is published later)
- Main / base: `aff30e8ad5542c94fab642ae024dc9aab4fa7ad7` (recheck at start)
- Stage: WORK (response)
- Written by / date: Claude, claude-opus-5-5 (configured; xhigh requested) · 2026-11-05

## Task

Claude [audit-01](../audit-01.md) found **no correctness issue**. C1–C3 mathematics, the computer-assisted
reduction and every MEASURED scope are accepted at their stated scope, with no status change. Findings F1–F26
(12 minor, 14 editorial) set WORK.

1. **Write `topics/padua-mz-cleanup-20261105/response-01.md`.** Answer every finding F1–F26 with one of: a fix
   (exact files changed), an evidence-based rejection, or an explicit unresolved item for AC. Never edit
   audit-01.md or its `audit-support/` files.
2. **Apply the fixes in the topic's own files.**
   - Theory and attempt wording: F2–F5, F7, F9, F10, F11 ("Extends:" vs "Split from:"), F24, F25.
   - Report rounding: F8.
   - Candidate records and gate synonyms in novelty-gate-math.md and the attempts: F21–F23. Use provisional
     records only.
   - Manuscript and README wording: F12–F14, F16. If manuscript.tex changes, rebuild it and record the new
     source hash and page count in manuscript-changes.md; F15 labels the old 24-page hash scratch-only.
   - ALLOCATIONS line: F20.
   - proposed-record-changes.md: F17, F18 and F19. F19 covers literal registration blocks for -01..-05 and the
     three IDEA candidates, plus dated status-preserving qualifiers for `state/IDEAS.md:938,947` and
     `PROOF_STATUS.md:385,390,394`, all still with provisional IDs.
   - F6 (optional split) and F26 (optional remark): decide and record.
3. **Provenance fix F1, without rerunning or replacing accepted certificates.**
   - Record the SHA-256 of each staged witness's decompressed canonical JSON payload, next to the existing gzip
     identity. Do this in finite-indefiniteness.md, cold-storage.json/COLD_STORAGE.md and the evidence manifest.
   - State that the container hash is environment-specific.
   - If the staged files under /tmp/mz-cleanup are no longer available, record that the payload hashes are
     pending, rather than regenerating different witnesses under the old identities.
4. **Re-verify.** Run `evidence_manifest.py` (refresh the inventory if needed), local links, `git diff --check`,
   and a check for provisional IDs in the manuscript.
5. **Classify the response.**
   - If no claim, proof, code or evidence changes materially (wording, records, payload hashes and proposals only),
     state that in response-01.md, set stage PR, and open handoff 04 for **PR preparation**: Codex gpt-6.1-sol xhigh.
     Preparation will:
     - refresh main and all live reservations;
     - assign final IDs from T376–391/N138–145/IDEA466–489;
     - apply the scoped shared changes, including F11's OPEN sharp-target registration and F19's rows, with
       crosswalk mappings;
     - update RESULTS.md (only this topic's section), PAPER_MAP and CURRENT;
     - refresh the inventory and run the protocol checks;
     - complete the PR26 WORK/AUDIT/PR sections.
   - If anything changes materially, set AUDIT and open handoff 04 for **Claude re-audit** (Opus 5.5 high or xhigh)
     of exactly those changes.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head; LOG.md; this handoff.
- audit-01.md in full. Its evidence is in `audit-support/evidence/` and the scripts in `audit-support/code` and
  `audit-support/sub-*`.
- The files named by each finding.

## Scope limits

- Do not reopen accepted mathematics, alter statuses, or relabel MEASURED items. Do not start C6 or add new
  mechanisms beyond recording the already-considered routes of F21.
- No final IDs and no shared registry edits in this response step. Those happen only in PR preparation.
- Sandbox compute only: at most 4 h wall per run and about 24 h cumulative CPU, as already approved. Ask AC before
  using any external machine.
- No push to main, merge, force-push, tag, settings or `.github/` change. Only AC merges.

## Acceptance and outputs

- response-01.md answers all 26 findings. The fixed files and verification commands are committed, and LOG and
  results are updated.
- PR26's WORK section notes the response and its AUDIT section links audit-01 and response-01. The PR stays a draft.
- Commit the outputs first. Then, in a following commit, set this handoff's status to `done in <output-sha>` and
  add handoff 04 (preparation or re-audit, per step 5). Push both before replying.
