# Handoff09 — Codex storage repair under AC continuation

- Status: open
- Previous handoff:08-response-review-and-storage-repair.md (superseded; instruction body preserved)
- Next agent/model/effort:Codex,gpt-6.1-sol high
- Role:storage developer; independent Claude review of Codex work remains separate/pending
- Branch:claude/padua-argmax-alln-20261101
- Input head SHA:`93169ab6e193fbbef91af16914cd1191e7564420`
- Main/base:`2b52b432fe59c9a50aef9deebe5152c5d6874465`, unchanged
- Stage:WORK
- Written by/date:Codex,gpt-6.1-sol high,2026-11-02

AC selected “Codex (gpt-6.1-sol, high): Continue” while08 assigned a
Claude developer/reviewer. Carry out08's storage-development task as
Codex. Do not self-approve Codex response-01 or the new Codex repair;
preserve08A for the next independent Claude protocol review. No earlier
handoff body or audit verdict is overwritten, and no pending review is
treated as complete.

Read rules/role, LOG,08 in full, audit-02-cold-storage and all support,
response-01 and its response-code review, current tools/cold_storage.py,
both cold manifests and PR_PREPARATION.md. Use the GitHub connector.
The current mathematics is accepted at its recorded scope; PD-T099
remains OPEN. No new research, scientific predicate/certificate/status,
final ID or shared scientific registry change.

Implement08B's CS1/CS2/CS3 repairs and active-versus-historical manifest
semantics. Preserve differing/tracked destinations, block unsafe
symlink/path traversal in restore/export/clean, preflight writes, retain
tracked/hash cleanup guards, and document safe idempotence/concurrency
limits. Record exact generating interfaces or retrieval-only provenance,
including omitted T1 analyzer prerequisites. Keep all archival identities
unchanged. Do not edit old audit/support records or silently approve a
repair as its auditor.

Use disjoint bounded workers if useful; only the orchestrator changes
Git. Independently check targeted safety refusals and normal real36-file
source/restore/compare/clean/export behavior. No destructive probe against
user data. Keep generated head evidence<16KiB per file, except the two
explicit metadata exceptions; large scratch stays off head. Refresh the
current integrity manifest/explicit receipt only after covered records
stop changing, then run plain read-only checks.

Write response-02-cold-storage.md with each finding disposition,
implementation/source identities, exact executions and residual limits.
Update LOG/own results/PR. A distinct Astra high review may supplement
development, but cannot replace Claude's review of Codex-authored work.
Do not write response-review-01 as an independent acceptance of your own
response. Do not change repository-wide PR18 or merge either PR. Preserve
the recorded integration context and reconcile later base changes without
discarding the fixes. No force-push/history purge/settings/.github change.

Commit completed development outputs first. In a following commit close09
at that real output SHA and add10 for Claude Opus5.5 high independent
protocol review of both response-01 and this storage repair, including
targeted tests, source pins and acceptance criteria. Claude may request a
further distinct Codex check if its own later repairs require one. Keep
PR17 draft until those gates pass; only AC merges. Publish before replying.
