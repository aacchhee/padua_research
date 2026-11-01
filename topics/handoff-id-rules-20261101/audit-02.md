# Focused protocol audit 02 — ACCEPTED

**ACCEPTED. F1–F4 are closed; Stage PR.** No unresolved finding within the rules/templates and integration scope below.

- Auditor: Codex; AC-requested `gpt-6-astra medium`; resolved runtime metadata is not independently exposed. Claude authored response-01 and its material rule changes; this auditor has not edited those rules.
- Response input: `7e9504b12610682e57c57dce9ac9fd2d37dfe9a7`; published response/rules read at `ac4ff3fd32d73880048e38d096bbcfb58df8a724`.
- Integrated candidate: `fcb334c7f0ef055695b8f2633692092865366ddb`, merging main `a7e123476cef761807c69e5d0af1a094c7ac3df0` (AC's merged PR #6). Re-read the inherited Fable amendment. Integration adds only that exact main amendment to the response's WORKFLOW text; other rule/template bytes match Claude's response.
- Finalization instruction/metadata: `c544dfb783446f23d5f76b0577f235da6f58a6a7`. AC explicitly requested final PR preparation and main integration in the same session; handoff 04 records why handoff 03's separate Claude preparation step was superseded.

## Coverage

Read the complete affected rules and templates, Codex role instructions, LOG, audit-01, response-01 and handoffs 01–04. Reviewed the full response rule diff and the main-integration difference. Read the merged batch ledger and refreshed open-PR metadata; the closed, unmerged PR search returned no entries. No IDs are assigned or reserved by this topic. This is an administrative audit with no novelty or scientific claim; the full IDEAS novelty gate and mathematical reruns do not apply.

## Dispositions

| Finding | Independent assessment |
|---|---|
| F1 — permanent reservations | Closed. Step 2 scans closed, unmerged PR ledgers as well as retired records. The retired-reservation paragraph requires preservation and blocks allocation when provenance cannot be reconstructed. Namespace maxima, a recheck before assignment/readiness, publication priority and collision mapping are explicit. Accepted IDs cannot be renumbered; unclear priority goes to AC. A cancelled PR cannot silently free its range. |
| F2 — ledger authority / transition | Closed. The dated transition explicitly supersedes single-owner and confirmation prose, preserves it as history, and retains recorded ranges and AC instructions. Adoption is at next continuation, before allocation/readiness. No-range topics and reservation-only draft updates are distinguished from final assignment and substantive registry preparation. The inherited PR #6 ledger can remain unchanged because the supersession is explicit. |
| F3 — handoff lifecycle | Closed. The orchestrator holding the current handoff controls numbering/statuses; subagents cannot create competing handoffs. The developer's refinement correctly permits an independent auditor's orchestrator to publish the response step. Work stays open until completion, input and publication commits are distinguished, and completion/redirect/withdrawal statuses preserve earlier bodies. The actual 01→02→03 chain has real output SHAs; AC's later override is preserved by 03→04. |
| F4 — exemptions / terminal topics | Closed. Continue reads a log if present. No-audit exempts only audit/log, retaining handoffs while work remains. Completion permits zero open handoffs and no prompt; AGENTS and the handoff template agree. The general before-reply instruction applies when a successor is required; its terminal exception is expressly stated. TOPIC_LOG is a starter for logged topics, not a requirement to invent a successor after completion. |

The changes preserve provisional-ID use, final assignment at PR preparation, scientific registry timing, batch rehearsal, evidence requirements, developer/auditor separation and AC precedence. Existing model allocations are retained, including PR #6's Fable row and scope paragraph. No new scientific permission is inferred.

## Transition after merged PR #6

Response-01's statement that #6 is unmerged is historical at its pinned input. It is superseded for current preparation by main `a7e1234`, not rewritten in the original response.

- Main now contains the lattice/programme blocks through PD-T100, PD-N043, IDEA-209 and LIT-426. All those records, the crosswalk, ledger and scientific files match main byte for byte.
- Open #11 (`97968d2c2d039cb0910e0ea50747fb2d9e01a262`) retains LIT-293–299; the main ledger records that reservation as well. No shift is necessary.
- Open #9 (`7b8884a2f98518784ff3698dd2f3f9c49c9cdd62`) and #12 (`38db12bc1cee57902c67f62e022af83e0880f699`) retain their own scope restrictions and adopt this rule on next continuation. Their old inherited ledger prose does not authorize reusing occupied ranges.
- This PR records **no range**. Lower fresh boundaries remain PD-T101, PD-N044, IDEA-210, LIT-427, subject to a new scan by an actual allocator. This audit does not reserve or certify future availability.

## Checks actually executed

Git fetch and branch-head inspection refreshed main/topic. Fast-forwarded to the exact remote response SHA, then merged `origin/main` without conflicts or history rewrite. A first attempted `merge --ff-only FETCH_HEAD` selected main, correctly refused a non-fast-forward and changed nothing; the response fast-forward used its explicit SHA instead.

Python comparisons over Git blobs verified:

1. Every changed path relative to merged main is one of the four designated rule/template files or inside this topic. Thus the entire PR #6 scientific/registry/ledger/evidence content is preserved exactly.
2. AGENTS and both templates are byte-identical to the Claude response. Removing the exact inherited Fable block from WORKFLOW recovers the exact response bytes. The first checker omitted a separator newline during normalization and rejected; correcting the checker recovered exact equality without changing repository content.
3. Prior audit/response files are unchanged; earlier handoff bodies are unchanged after excluding their single status line. Handoff 04 is the sole open instruction during finalization.
4. `git diff --check origin/main HEAD` passes.

A disposable branch/worktree rehearing current main followed by a squash of this topic passed without conflict: source `c544dfb783446f23d5f76b0577f235da6f58a6a7`, result tree `2e79950f1190a40d28d6575fca3553932f2f42bb`, exactly the source tree. This is a local rehearsal, not a merge into main. Final documentation-only delivery is checked again at PR preparation.

Limits: no new scientific verification, complete global-ID validation or future-PR integration certification is claimed. Other PRs remain responsible for refreshing their stale inherited state. Audit-01 and response-01 remain immutable. Later edits confined to this topic's audit/preparation/closure metadata do not require another rule audit; any further material rule/template change does.
