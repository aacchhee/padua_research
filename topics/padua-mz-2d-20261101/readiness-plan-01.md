# Readiness and merge-order plan — response-01

2026-11-01. Documentation-only plan after Claude audit-01's scoped mathematical acceptance. PR14 stays draft. This file records concrete future actions without choosing AC's merge order or requesting a merge.

## Inputs and invariants

Fresh main is `806cc7b4509fd93bae652f9545d32d95529f8281`. Relevant other drafts: PR12 at `6c6e484818b8b949ab0a6b2a4b9086b6a46528c3`, PR15 at `fa5835f6fd2c1f62cd9e34e14e90d492ac387242`. Response-01's dated scan preserves PR14's complete ranges and PR15's disjoint ranges, including permanent gaps. No existing final ID may move.

The earlier disposable rehearsal is pinned in `protocol/integration-rehearsal.json`: PR14 squashes cleanly onto main; that rehearsal found only ID_CROSSWALK.md and the allocation ledger conflicted with its then-pinned PR15. It is historical evidence, not a fresh rehearsal of later heads or this response. A new rehearsal follows the actual order selected by AC.

## If AC chooses PR14 before PR15

PR14's accepted science and response remain its own contribution. After AC integrates PR14, the PR15 orchestrator merges the new main without rebasing. In `ID_CROSSWALK.md`, retain all PR14 mappings, the historical provisional-to-PD-N045 alias and the F3 reciprocal PD-T028 mapping, and append PR15's own reservation/mapping material. In the batch ledger, preserve both original reservation publications and all permanent headroom; consolidate duplicate imported prose without dropping either owner's ranges or provenance. PR15 reruns its own required registration checks and rehearses against the new main before any merge request. No other branch is edited from this chat.

## If AC chooses PR15 before PR14

After AC integrates PR15, this topic's orchestrator merges the new main into the published PR14 branch without rebasing. Retain PR15's newly merged crosswalk/ledger entries and PR14's complete mapping, scoped parent links and unused ranges. Preserve earlier accepted registry entries and add only this topic's intended changes; do not regenerate shared files from an older copy. Recheck all current reservations, statuses, links, frozen code/evidence and the accepted audit's identity impact. Rehearse the resulting squash in a disposable branch. If only integration text changes, record that impact; material scientific changes return to the appropriate audit.

## If PR12 or another main update lands first

Refresh main and every open PR again. Merge main without rewriting history and compare the frozen A1/A2 input objects explicitly; prior matching A2 objects are not a guarantee about future commits. Preserve the audit's contextual-only A2 treatment. Resolve only the authorized topic and shared integration text, and repeat the bounded semantic checks needed by the actual diff. Do not make a readiness assertion based on stale heads.

## Ready-to-request conditions

AC's intended order is known, the relevant reconciliation and updated disposable rehearsal pass, the complete audit/response evidence and reservations remain preserved, and the current PR body names the actual resulting head and base. A draft-to-ready transition still requires AC's instruction under handoff03. Only AC performs the merge. Windows delivery and named source-version comparisons remain separately reported rather than silently treated as completed.
