# Handoff 13 — padua-lanczos-drift-20261101 — AC squash-merge of PR15 (first, before PR12), then closure

- Status: open
- Previous handoff: [12-merge.md](12-merge.md) (superseded by this file: AC's order)

- Next agent / model / effort: **AC** for the merge. Afterwards, Claude Sonnet 5.5 medium does the mechanical closure.
- Role: AC (merge); afterwards, topic orchestrator (closure)
- Branch: `codex/padua-lanczos-drift-20261101` (PR #15, marked ready for review)
- Input head SHA: `3df6179da5b453d70153f081d4869dfa1f6e49ca`. The publication commit of this file and a later re-validation receipt are documentation only.
- Main / base: `28aaa20861d08074b77efc74eaef75cdcb36234d`
- Stage: PR, ready
- Written by / date: Claude, configured `claude-opus-5-5` high · 2026-11-01

## Task

AC's instruction (2026-11-01 20:55 CET): "finalize pr15, it goes in først". PR15 merges **before PR12**.

1. **AC: squash-merge PR #15 into `main`.** Agents never merge.
   - Before merging, confirm that `main` is still `28aaa20` and that the PR head is this file's publication commit or a later documentation-only commit. The last re-validation receipt is `preparation/validation-3.json` (PASS).
   - If `main` has advanced, do not merge. Ask the orchestrator to merge `main` into the branch without rebasing and rerun `preparation/validate.py`.
2. **PR12 afterwards (its own orchestrator).** Merge the new `main` into `codex/padua-proof-attempts-2-20261101` without rebasing. Keep PR15's registrations (PD-T136–146, PD-N062–063, IDEA-246–267) and its gaps (PD-T147–155, PD-N064–071, IDEA-268–285, LIT-445–459). A merge-tree of PR15 `b6980b9` with PR12 `f4c5c9e` is clean. The batch ledger records this order.
3. **Closure (after the merge).** Record the squash SHA in `results/padua-lanczos-drift-20261101.md` and in this topic's `RESULTS.md` section, through a small follow-up PR only if AC asks; otherwise report it. Close this handoff with `done: merged in <squash-sha>`. Results are repository-only.
4. **Separate pending item.** Deliver Codex's original ZIP (`27476b62…`) to cold storage, from the Codex workspace or by AC.

## Scope limits

No new science, IDs or status changes. Never force-push, tag, touch `.github`, or edit other topics' branches. Only AC merges.

## Acceptance and outputs

PR #15 is squash-merged, and the closure is recorded. After closure no open handoff remains for this topic.
