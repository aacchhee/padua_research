# Response 01 — initialization audit and Addendum A

- Developer: Codex; Sol 6.1 medium requested by AC. Template subtask: `gpt-6.1-sol` medium, task `audit_response_templates`. Parent session effort is not independently exposed by the runtime.
- Date: 2026-10-31.
- Rules / starting head: `af9987f5da84299ecfff8ed9ceef4f7b84f2cd2e`.
- Audit: [audit-01.md](audit-01.md), including Addendum A, read in full and left unchanged.
- Base refreshed in a clone: `b2ec85f3fb2743a3b9292657fec9ac9da227d410`; already incorporated in the topic branch.
- Scope: protocol, templates and bookkeeping only. No scientific computations, claims, registrations or final ID allocations.
- Stage: AUDIT. PR #1 stays draft; Claude must check these material rule/template changes.

## M1 — Fixed, including all of Addendum A

[WORKFLOW.md](../../agents/WORKFLOW.md), both role files, [THEORY.md](../../templates/THEORY.md), [ID_CROSSWALK.md](../../ID_CROSSWALK.md) and [PROOF_STATUS.md](../../PROOF_STATUS.md) now implement:

1. **Split by default:** a substantive proved claim gets its own exact statement, file and ID and keeps PROVED. Differently classified claims and refuted side conjectures move to their own homes.
2. **No downgrade of a substantive proof:** weakest-part aggregation happens only after legitimate splitting/classification and excludes REJECTED.
3. **Minor-part exception:** routine proved steps may remain with the main statement. Dependency by another result, standalone reporting or a nonroutine proof makes a proved part substantive. The developer proposes classification, the auditor checks it, and AC resolves disputes.
4. **Preserve the target:** the original combined target remains registered with its true status and dependencies if it matters. PARTIAL requires PROVED and OPEN mathematical parts only. Referring to an independently registered proved dependency does not duplicate its substantive statement/proof. Scope changes retain original wording, changed wording and reasons in History.
5. **Split provenance:** theory records have `Split from:` / `Split into:` fields and the crosswalk has an original-to-split table.
6. **Consistent semantics:** OPEN describes the unresolved statement and does not deny proved dependencies. REJECTED is a disposition with `refuted | equivalent | abandoned` reason. A PD-N statement has its own epistemic status; a candidate's disposition cannot overwrite it.

No existing result needed splitting because the registry is empty. L5's broader question about bookkeeping-only PD-N records remains for AC; no such entry is fabricated here.

## M2 — Fixed

THEORY now includes ID kind, Aliases, Definitions, Assumptions, split fields, explicit negative mechanism and parameter range, and rejection reason separate from proof status. Existing dependencies, evidence, independent checks, scope, open items and history remain. The template matches the workflow's required fields.

## M3 — Fixed

[IDEA.md](../../templates/IDEA.md) now distinguishes the falsifiable separation criterion against the closest entry from test discriminability. The latter is expressed in terms of outcomes, scope and limits, without size-scaling assumptions. Resources/cost accounting is optional when relevant.

## L1 — Fixed for the shared frontier

[CURRENT.md](../../state/CURRENT.md) no longer carries a transient initialization-stage row. It records that there are no scientific topics and links the initialization log, which remains the authoritative pre-merge stage record. The workflow also requires post-merge-appropriate frontier text before requesting merge. The log and PR correctly remain at AUDIT for the focused reaudit.

## L2 — Fixed

The explicit reaudit trigger now includes material changes to rules, templates and registry structure, in addition to claims, proof, code and evidence. This response follows that trigger.

## L3 — Fixed

The `no audit` exemption cannot add or upgrade PD-T, PD-N, IDEA or LIT entries. It also cannot change rules, templates or registry schemas. Such changes use the ordinary audit cycle rather than silently acquiring unaudited status.

## L4 — Fixed

WORKFLOW and ID_CROSSWALK specify provisional formats for all four namespaces and a concrete authoritative ledger path, `topics/<batch-slug>/ALLOCATIONS.md`, linked from the crosswalk and member PRs/logs. Standalone reservations use the topic's own ALLOCATIONS file. One allocation owner reconciles main and all active reservations before allocating; parallel writers cannot reserve independently. No ledger is created yet because there are no reservations.

## L5 — Open for AC; no scope narrowing adopted

The current broad requirement for a PD-N file for every failed/rejected idea is retained. The proposed narrower rule—PD-N only for refuted/failed mechanisms, with equivalence and abandonment kept as IDEA dispositions—is reasonable but is AC's decision, as the audit states. Pending that decision, a bookkeeping-only record asserting no negative mathematical statement marks its statement/status fields not applicable rather than claiming a theorem or assigning REJECTED as proof status. There are no such records in this scaffold.

Decision for AC: retain the broad rule, or restrict PD-N to mathematical negative statements and keep purely equivalent/abandoned candidates in IDEA records.

## L6 — Fixed

[COLD_STORAGE.md](../../templates/COLD_STORAGE.md) now has Source commit in addition to script blob IDs, and explicit retention and retrieval sections. It retains hashes, byte sizes, commands, delivery and committed checker output requirements.

## L7 — Fixed; historical limitation retained

[technical-review.md](technical-review.md) now identifies itself as an orchestrator-written summary of the reviewer's findings. It explicitly states that the reviewer's original report and pre-fix working files were not preserved in Git. Those historical artifacts cannot be reconstructed from the committed summary and are not claimed to be available.

## I1 — Clarified

The historical LOG entries now identify the project wrapper as AC's external Codex configuration and `padua-init/` as a temporary local drafting directory. Neither is a Padua repository dependency; the pushed branch and PR are the recovery source.

## I2 — Open for AC; no settings changed

The audit reports unprotected main and multiple enabled merge methods. No settings, permissions, branch protection or workflow files are changed. The written workflow explicitly requires AC's squash integration. Whether to enforce PR-only/no-force-push protection and squash-only settings mechanically remains AC's decision; this is not an agent authorization request and does not block preserving this response.

## Verification

Checks actually run in the topic clone after integration:

- `git diff --check`: passed, no whitespace errors.
- PowerShell enumerated all 24 Markdown files (including this response), removed inline-code spans before scanning Markdown links, resolved each relative target with `Test-Path`: 33 actual relative links, zero broken. The first naive scan also matched the audit's literal link-syntax example inside inline code; the corrected scan distinguishes that example from a rendered link.
- `git diff --quiet af9987f5da84299ecfff8ed9ceef4f7b84f2cd2e -- topics/initialize-padua/audit-01.md`: exit 0; the audit and Addendum A are unchanged.
- `rg -n 'REJECTED|weakest|PARTIAL|Split from|Split into|no audit|Reaudit material|ALLOCATIONS' agents templates PROOF_STATUS.md ID_CROSSWALK.md`: inspected the resulting definitions, mirrored role text, template fields and allocation paths together.
- `.github` is absent; no repository settings or permissions were changed.

No scientific run or independent Claude acceptance is claimed. No mathematical status was assigned or upgraded. The changes to shared registry files are schema/instruction changes made while preparing the existing initialization PR, with no result or reservation rows added.

## Focused reaudit handoff

Claude should check the changed rule/template semantics and all dispositions above, with particular attention to substantive-vs-minor proof classification, preservation of original targets and independent PD-N status. L5 and I2 remain explicitly open for AC. No change to a scientific statement, proof or result status is involved.

Exact next prompt: `Claude (Opus 5.5 high): Continue codex/initialize-padua in aacchhee/padua_research; reaudit response-01.md, including M1 Addendum A and the changed rules/templates.`
