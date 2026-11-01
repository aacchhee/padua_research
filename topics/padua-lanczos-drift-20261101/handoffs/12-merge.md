# Handoff 12 — padua-lanczos-drift-20261101 — AC merge decision for PR15, then topic closure

- Status: open
- Previous handoff: [11-pr-preparation.md](11-pr-preparation.md), done in `51315a33d426bd0abce9af79f9692b3d22585709`.
- Next agent / model / effort: **AC** for the merge decision. After the merge, Claude Sonnet 5.5 medium does the mechanical closure.
- Role: AC (merge); afterwards, topic orchestrator (closure)
- Branch: `codex/padua-lanczos-drift-20261101` (PR #15)
- Input head SHA: `51315a33d426bd0abce9af79f9692b3d22585709` (prepared and validated). The commit publishing this file changes only handoff statuses.
- Main / base: `28aaa20861d08074b77efc74eaef75cdcb36234d`
- Stage: PR. Codex audit-04 accepted the final response, preparation is validated, and the squash rehearsal is clean.
- Written by / date: Claude, configured `claude-opus-5-5` high (topic orchestrator for handoff 11) · 2026-11-01

## Task

1. **AC.** Review PR #15 and, if satisfied, squash-merge it into `main`. Agents never merge.
   - Before merging, confirm that `main` is still `28aaa20`, and that the PR head is this handoff's publication commit or a later documentation-only commit.
   - If `main` has advanced (for example PR12 merged first), do not merge. Ask the orchestrator to merge `main` into this branch without rebasing, resolve shared-registry conflicts keeping every topic's rows, and rerun `preparation/validate.py` (new dated receipt) and the union scan.
   - Two points for AC's review:
     - PD-T140's separately labelled PARTIAL factor-ten target is registered as its own PROOF_STATUS row, "PD-T140 (target part)", inside the existing table schema.
     - PD-T075 changed from OPEN to PARTIAL through the approved literal blocks.
2. **After AC merges (closure agent).**
   - Read the rules at the new `main`. Do not push to `main`.
   - Record the squash SHA in `results/padua-lanczos-drift-20261101.md` and this topic's root `RESULTS.md` section through a small follow-up PR only if AC asks. Otherwise report it.
   - Close this handoff (`done: merged in <squash-sha>`) in the same way. Results are repository-only; nothing is written to AC's machine.
3. **Separate pending item, not blocking.** Codex's original development ZIP (`27476b62…`, 799968 bytes) and raw artifacts are verified in the Codex workspace but not yet delivered to `Downloads\padua\cold_storage\padua-lanczos-drift-20261101\`. Codex or AC delivers them, with a readback receipt.

## Read first

`preparation/README.md`, `preparation/validation.json`, `audit-04.md`, and LOG's last section.

## Scope limits

- No new science, IDs, status changes or scientific runs.
- OPEN targets stay open: all-degree drift, staircase safety, PD-T055, PD-T075(U2), PD-T056(G).
- Never force-push, tag, touch `.github`, or edit other topics' branches. Only AC merges.

## Acceptance and outputs

AC squash-merges PR #15 and the closure is recorded. No open handoff remains for this topic after closure.
