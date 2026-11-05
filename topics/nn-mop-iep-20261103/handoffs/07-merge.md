# Handoff 07 — nn-mop-iep-20261103 — AC merge decision for PR22, then topic closure

- Status: open
- Previous handoff: [06-protocol-check.md](06-protocol-check.md)
- Next agent / model / effort: **AC** for the merge decision. After the merge, Claude Sonnet 5.5 medium does the mechanical closure.
- Role: AC (merge); afterwards, topic orchestrator (closure).
- Branch: `codex/nn-mop-iep-20261103` (PR #22)
- Input head SHA: `751d47debdfd716eb4054d69e4a47c6e50dcdf65` (protocol-check output). The commit publishing this file changes only handoff statuses.
- Main / base: `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`
- Stage: PR.
  - Claude audit-02 accepted the science at `5b36f8f`.
  - Codex preparation passed Claude protocol check 01 ([receipt](../preparation/protocol-check-01.md)).
  - The squash rehearsal at `1de5891` is clean, including PR21 or PR24 applied afterwards.
- Written by / date: Claude, claude-opus-5-5 (protocol checker; Sonnet 5.5 high was requested, but this session cannot switch models) · 2026-11-05

## Task

1. **AC.** Review PR #22 and, if satisfied, squash-merge it into `main`. Agents never merge.
   - Before merging, confirm that `main` is still `21dbfc9` and that the PR head is this handoff's publication commit or a later documentation-only commit.
   - If `main` has advanced (for example PR21 or PR24 merged first), do not merge yet. Ask the orchestrator to:
     - merge `main` into this branch without rebasing;
     - resolve shared-registry conflicts, keeping every topic's rows;
     - rerun `preparation/check_registration.py` (update its `BASE` pin only) and the reservation refresh;
     - replay the squash rehearsal.
   - Points for AC's review:
     - The former provisional negative PD-N?nn-mop-iep-codex-01 is withdrawn and has no final ID; its original text is kept as history.
     - PD-T290's binary64 C4 errors are finite MEASURED observations, not a general instability claim.
     - Primary-source locators are developer-verified only, because arxiv.org was blocked for the Claude auditor.
2. **After AC merges (closure agent, Claude Sonnet 5.5 medium).**
   - Read the rules at the new `main`. Do not push to `main`.
   - Report the squash SHA. Record it in `results/nn-mop-iep-20261103.md` and the root `RESULTS.md` section only through a small follow-up PR, and only if AC asks.
   - Close this handoff as `done: merged in <squash-sha>` and record topic completion in LOG.md (on the topic branch, or in that follow-up PR if AC asks). The topic then has no open handoff.

## Scope limits

- No new science, IDs, status changes or scientific runs.
- Deferred and open questions stay open: a stable coupled NN updater (IDEA-378), C4 error-source decomposition, and wider measurements.
- Never force-push, tag, touch `.github`, or edit other topics' branches. Only AC merges.

## Acceptance and outputs

AC squash-merges PR #22 and the closure is recorded. No open handoff remains for this topic after closure.
