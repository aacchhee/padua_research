# Handoff 11 — padua-argmax-alln-20261101 — PR preparation

- Status: open
- Previous handoff: 10-claude-response-and-storage-review.md (done in the input commit)

- Next agent / model / effort: Codex, `gpt-6.1-sol` high. The work is shared-registry, final-ID and record preparation with semantic content, so high rather than medium.
- Role: developer (PR preparation). A distinct reviewer audits the preparation afterwards.
- Branch: `claude/padua-argmax-alln-20261101`
- Input head SHA: `d18ebdaba2672201b1b5e0bc5f1bd92366c08eea` (the commit that publishes this file comes later)
- Main / base: `2b52b432fe59c9a50aef9deebe5152c5d6874465`. Refresh it first: PR #18 may merge before or during this step.
- Stage: PR (preparation)
- PR: [draft 17](https://github.com/aacchhee/padua_research/pull/17)
- Written by / date: Claude, configured `claude-opus-5-5` high · 2026-11-02

## Accepted state you start from

- **Mathematics:** accepted by [audit-01](../audit-01.md).
- **Codex response-01:** accepted by [response-review-01](../response-review-01.md).
- **Codex storage repair:** CS1–CS3 resolved by [audit-03](../audit-03-storage-repair.md).
- **What remains:** the preparation work assigned in [PR_PREPARATION.md](../PR_PREPARATION.md), plus the residues listed below.
- **No scientific change.** No statement or status changes. PD-T099 stays OPEN, and the 6/2/1 campaign stays closed.

## Task

1. **Reconcile main.** If PR #18 has merged, merge `origin/main` into this branch; never rebase or force-push.
   - For `tools/cold_storage.py` and `tools/test_cold_storage.py`, keep the Codex-repaired guards from this branch.
   - Take PR #18's audited readback and offline-verification additions (fix for audit-03 S1 / PR #18 F1) only after PR #18's Codex re-audit accepts them.
   - Record the resolution and run `tools/test_cold_storage.py` plus `verify padua-argmax-alln-20261101`.
   - If PR #18 has not merged, leave the tool unchanged here and record S1 as an open item that blocks only delivery and purge.
2. **Fix the record residues from response-review-01.**
   - R1: normalize the stale "Claude audit pending" labels, with dated notes, at:
     - gated-07:46-47, gated-08:54, gated-16:87,219, gated-N02:49,162;
     - codex-01:99, codex-02:37,67, codex-04:79,218, codex-08:38,138,165, codex-N01:29, codex-07:48.
   - N-a: add a platform-dependence note to `t1-restoration.json`/`response-code-check` wording about the "977 exactly equal" leaves.
   - N-b: restore claude-01's earlier label in the LOG header alongside the new one.
3. **Do the PR_PREPARATION work.**
   - Run the fresh union reservation scan (main plus all open PRs, including #18 with "no range").
   - Assign final IDs from the permanent ranges: PD-T206–245, PD-N078–083, IDEA316–335, LIT460–465. Reuse PD-T181 for codex-07 (F8).
   - Make the literal shared-registry edits: PROOF_STATUS, state/IDEAS, ID_CROSSWALK, literature/INDEX if needed, and the RESULTS.md section from the topic results.
   - Create the MEASURED homes and scoped PD-N records (F11), and split the IDEA records (F12).
   - Leave Claude's own candidate close-outs (claude-01 → REJECTED: refuted via gated-N01; claude-02's measured-scope close-out) as **literal proposals for Claude to apply**. Do not apply them yourself.
   - N1: harden the scientific checkers against `python -O` (explicit failures, or refuse when `not __debug__`). Rerun every affected checker and its controls, and record that the predicates are unchanged.
4. **Refresh the integrity manifest.** Run `check_evidence.py --refresh` (updating its hard-coded status text) once covered files freeze, then the plain check, and record the output. The plain check currently stops only because of the three handoff-10 review outputs.

## Read first

At the branch head:
- `AGENTS.md`, `agents/WORKFLOW.md` (including the AC-approved evidence paragraph if PR #18 has merged), `agents/codex/CODEX.md`;
- LOG;
- PR_PREPARATION;
- audit-01, response-01, response-review-01, audit-02-cold-storage, response-02-cold-storage and audit-03;
- proposed-record-changes;
- ALLOCATIONS.

## Scope limits

- **No research.** No new mathematics, rounds or scans.
- **Branches and Git.**
  - Do not edit PR #18's branch.
  - No main mutation, merge of PRs, force-push, history purge, tag, settings or `.github/` change.
- **Cold storage.**
  - Do not restore cold-stored data into Git.
  - Generated files stay under 16 KiB, except `cold-storage.json` and the single active integrity manifest.
- **History purge.** AC's purge approval is a separate step after hash-verified AC delivery and after both PRs merge.

## Acceptance and outputs

- **Outputs.** The preparation output commit includes:
  - registry edits and final-ID mappings;
  - fresh allocation-scan evidence;
  - the refreshed manifest with its passing plain check;
  - LOG, results and the RESULTS.md section.
- **Next handoff.** Then, in a separate commit, close this handoff and open handoff 12 for a distinct Claude review of the preparation: Claude Opus 5.5 high. That review also applies Claude's own candidate close-outs, which Codex then reviews.
- **PR #17.** Update its WORK/AUDIT/PR sections. It stays a draft until the preparation review passes. Only AC merges.
