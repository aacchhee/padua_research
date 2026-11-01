# Handoff file and fresh-range ID reservation rules

- Branch: claude/handoff-id-rules-20261101 · Base: main `a7e123476cef761807c69e5d0af1a094c7ac3df0` · Developer: Claude · Auditor: Codex
- Stage: PR · Next: AC's merge decision after final publication · Active finalization: [handoffs/04-finalize.md](handoffs/04-finalize.md)
- Reserved final-ID ranges: none (rule change only; no PD-T, PD-N, IDEA or LIT entry).
- Open for AC: merge decision on PR #13; transition is next continuation before allocation/readiness, preserving all existing ranges.

## 2026-11-01 — Claude (claude-opus-5-5; requested effort high)

- Rules read at main `21e620ba8b5f0e0706f3a8c6613517df04d9d469`.
- AC's request: (1) when a draft PR is made, or at any other allocation stage, check not only free IDs but also those allocated by other draft PRs, and start a new range, so that reallocation stops; (2) long next-step instructions are recorded in a handoff file in the repo, so that AC only says "continue branch".
- Changes:
  - `AGENTS.md`: the reply ends with a short `Continue <branch>.` prompt; the full instruction goes in a handoff file.
  - `agents/WORKFLOW.md`, Work cycle: the meaning of `Continue <branch>.`, and the handoff-file rule (overwrite per step, commit and push before replying, AC's message takes precedence).
  - `agents/WORKFLOW.md`, Audit and PR records: "reserve fresh ranges; never reallocate". The scan covers main and all open PRs including drafts. New ranges start above the highest used or reserved ID and are recorded at once, with headroom; gaps are permanent; more IDs come from a new range; no renumbering. The single-allocation-owner sentence is replaced by per-branch ownership of recorded ranges.
  - New `templates/HANDOFF.md`.
  - `templates/TOPIC_LOG.md` header: a handoff link and a reserved-ranges line.
- Motivation: the 2026-11-01 batch needed repeated reconciliation. PR #6's planned range was overtaken by PR #10's allocation, and then by PR #11's LIT-293–299 reservation.
- No scientific content; the novelty gate does not apply.

## 2026-11-01 — Claude (claude-opus-5-5; requested effort high), amendment before audit

- AC: "I would rather open a new handoff, not overwrite old ones. might be good to have to be able to track some things".
- Change: handoffs are now numbered files `topics/<slug>/handoffs/NN-<step>.md` that are never overwritten. Only the status line changes (`open`, then `done in <sha>`, `superseded by NN` or `withdrawn: <reason>`), and exactly one handoff is open at a time. `Continue <branch>.` reads the latest open handoff. AGENTS.md, the WORKFLOW Work cycle and both templates are updated.
- This topic's own handoff has moved to [handoffs/01-audit.md](handoffs/01-audit.md), still open. It had not been taken up yet.

## 2026-11-01 — Codex protocol audit 01

- Rules / audited head: `10f2d8592673866ed0aa5ca73cef88d7541183ed`; current main / base: `21e620ba8b5f0e0706f3a8c6613517df04d9d469`. AC invoked handoff 01 without an override. Requested allocation: `gpt-6-astra medium`; resolved runtime metadata is not independently exposed.
- [Audit-01](audit-01.md): **CHANGES REQUIRED**, F1–F4. Retain reservations beyond PR closure; resolve old ledger authority and transition timing; define active/redirect/parallel handoff ownership; reconcile log-exempt jobs and terminal completion. Exact proposed wording is in the report. No rule, template, ledger, registry, ID or scientific content was changed by the auditor.
- Read complete affected rules/templates/topic records and batch ledgers on main and all relevant open drafts, at pinned SHAs recorded in the audit. No novelty-bearing work; the full scientific novelty gate does not apply. No subagents or scientific executions.
- Refreshed main/topic through GitHub and then shell Git using supported network-enabled execution after the default sandbox proxy failure. Topic is two commits ahead of main, zero behind. Pinned ledger blob identities were recovered with `git rev-parse SHA:path`; #9/#12 ledger blobs are identical. Python arithmetic on the reported interval endpoints confirms disjoint recorded blocks and lower boundaries PD-T101, PD-N044, IDEA-210, LIT-427; this does not certify complete registry content or reserve those numbers. `git diff --check` passed.
- Transition recommendation: existing drafts comply on their next continuation before allocation/readiness. Preserve #11 LIT-293–299 and #6's recorded lattice/programme blocks; add missing provenance, without retrospective headroom or renumbering. #6 is still unmerged. #9/#12 retain their AC ownership restrictions and record ranges only if needed. No writes to other topics or AC's local files.
- Handoff 01 completion is published after the audit-output commit, so its `done in` status can name a real existing commit. The succeeding handoff will be [handoffs/02-response.md](handoffs/02-response.md); it requires Claude's dispositions and a focused independent re-audit of material rule changes. Delivery-only changes do not alter the audited candidate.
- Audit outputs committed at `19526f248554821652e517613944408c83fd19b4`; handoff 01 is done in that commit. Handoff 02 is the sole open handoff for Claude's response.

## 2026-11-01 — Claude response-01 (claude-opus-5-5; requested effort high); Stage AUDIT

- Rules read at `3b1908b`. Main `21e620b` is unchanged and already the base. Refreshed heads: #6 `37820a5`, #9 `7b8884a`, #11 `97968d2`, #12 `38db12b`. No closed, unmerged PR exists.
- [response-01.md](response-01.md): F1–F4 accepted. F1 is strengthened (the scan also reads closed, unmerged PR ledgers and retired reservations). F3 is refined: the orchestrator of the session holding the open handoff numbers the next one, which keeps audit-01's own 02 handoff valid.
- Transition: the auditor's recommendation is accepted. Existing ranges are unchanged, #9 and #12 record a range or "no range" at their next continuation, and #6 and #11 add provenance and the supersession note.
- Handoff 02 is done; [03-audit.md](handoffs/03-audit.md) is open (focused Codex re-audit).

## 2026-11-01 — Codex finalization, AC scope override

- AC: "Codex (gpt-6-astra medium): Continue claude/handoff-id-rules-20261101. Make pr13 final, integrate merged pr6". This adds main integration and replaces handoff 03's separate Claude preparation with Codex finalization in the same session. Handoff 03 is superseded by [04-finalize.md](handoffs/04-finalize.md); its instruction body is unchanged.
- Rules read at published response head `ac4ff3fd32d73880048e38d096bbcfb58df8a724`; re-read the changed Fable allocation paragraph after main integration. Requested model/effort: gpt-6-astra medium; resolved runtime metadata is not independently exposed. Codex remains independent of Claude's rule development.
- PR #6 was merged by AC at main `a7e123476cef761807c69e5d0af1a094c7ac3df0`. Merged that main into this already-published topic without rebasing, at `fcb334c7f0ef055695b8f2633692092865366ddb`, without conflicts. Main introduces only the already-accepted Fable row and its scope paragraph into the response's WORKFLOW text; the Claude response remains unchanged.
- Novelty gate not applicable: protocol audit and administrative integration only. No subagents or scientific reruns. No range is needed or reserved.
- [Audit-02](audit-02.md): **ACCEPTED**, F1–F4 closed independently against Claude's response and the integrated candidate. No material rule/template edit by Codex. [PR preparation](pr-prep.md) records preservation, transition and rehearsal; this supersedes the older unmerged-#6 snapshot for current decisions without changing historical reports.
- Actual checks: all PR #6/other-topic/registry/ledger/scientific files match main; response rules match exactly after removing only main's exact Fable addition; prior report and handoff bodies preserved; one active handoff; `git diff --check`; disposable main → #13 squash tree equality at `c544dfb` / `2e79950f1190a40d28d6575fca3553932f2f42bb`. An initial checker newline-normalization error was corrected and checks rerun, with no source change.
