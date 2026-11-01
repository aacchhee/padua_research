# Handoff 01 — padua-proof-attempts-2-20261101 — ordered development

- Status: done in 4265bb94f987ce77d89cd5e15a8c435cbd1411d0
- Previous handoff: none (numbered-handoff rule adopted during this session)
- Next agent / model / effort: Codex, gpt-6.1-sol xhigh for mathematics; medium for mechanical work
- Role: orchestrator / developer
- Branch: codex/padua-proof-attempts-2-20261101
- Input head SHA: `842dfaaeff524b4db4141d314afff6ad4a5b7721`
- Main / base: current main `e24b21fe43cdd090f6dfac269147e75185f04c5b`; original part1 base `a09d910ae7d5526b1e216066421a0bee7fc20da4`
- Stage: WORK
- Written by / date: Codex, requested gpt-6.1-sol xhigh/medium (root runtime metadata unexposed) · 2026-11-01

## Task

Continue the user's second proof campaign in order. A2 is complete: results01–04. A5 n3/n4 and their separate global argmax corollaries are complete:05–11. Do not reopen these absent a concrete finding. A5 started09:19UTC; its six-hour ceiling remains15:19UTC today. Finish n5 independent verification, then extend n6,…,8 as feasible before the ceiling. Full producer artifacts, a separately implemented certificate checker and actual regeneration/checks by a different subagent are required before a finite count becomes PROVED. Every consistent mask and every discarded region needs a rigorous disposition; node/crease/crossing and physical boundary cases cannot inherit numerical tolerances. Any count discrepancy gets a scoped local PD-N; compare certified n6/7/8 results to the primary arXiv2605.23299 Table3 only after certification, without contacting authors. Prove each reached global corner argmax separately, including exclusion of non-strict plateaus.

At A5 stop, continue A4(a) (about3h), then B3 (about2h), then B1 (about2h), each with its gate and written kill criteria before work. A4(a): derive exact edge formula, positive limiting midpoint gap or best two-sided rigorous bound; (b),(c) only route notes. B3: read pinned local Lanczos304(a), seek fixed-n,p computed-section counterexample with positive boundary gap of order sqrt(delta), or write the precise obstruction. B1: express lower-block leakage through top-form functional and prove W[t-2] detects it for one precise pole class under current hypotheses, using structural proof or exact nonzero witness polynomial; alternatively a general-position counterexample. Optional B4/B7 only after all five stops.

Only root changes Git. Coordinate disjoint files with existing agents. Mathematical work uses gpt-6.1-sol xhigh; mechanical execution medium. No ultra used. Every consequential exact/interval computation requires another subagent's actual run and own output. Independent checks supplement the pending Claude audit. Use PYTHONDONTWRITEBYTECODE=1 and python -B; installed FLINT is exposed by PYTHONPATH=/tmp/padua2-deps. Example new N5 checker: python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n5.py CERTIFICATE --global-file GLOBAL --output OUTPUT. Record exact actual commands and backend versions in receipts, never infer completion from a running process.

## Read first

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md at the branch head; topic LOG.md, plan.md, inputs-review.md, evidence-manifest.json, attempts and current independent receipts. Scientific initial pins: programme9bd14a6d2c4da69139a10107d8a787f2be0c5c9e; part1a09d910ae7d5526b1e216066421a0bee7fc20da4; Lanczosa2dd845b8a231e1b00733e1361e2a9ad3bad222f. Later authoritative pins and impacts are in LOG: part1 audit95279b8/response7b8884a, final programmeb46b4de, main/rulese24b21f. Original scientific input pins stay preserved. Before each target repeat the complete relaxed registry gate and read shortlisted theory plus literature/INDEX.md before sources.

## Scope limits

All new authored files are inside topics/padua-proof-attempts-2-20261101/. Local PD-T?/PD-N? IDs only; **no range**, no final IDs/shared registry edits. Propose literal old→new blocks in proposed-record-changes.md, checked against pinned input. Keep required part1 dependency phrase “PD-T?proof-attempts-codex-0N (audit pending)” with the dated qualification that audit01 accepted and response7b8884a disposed minors. Part2 audit remains PENDING. No .github edits, third-party PDFs/fulltext, author contact, force pushes, tags or PR merges. Only AC merges. Merge upstream/main only after a depended-on input/rule change and prior impact entry, never rebase published history. PR12 remains draft against codex/padua-proof-attempts-20261101. Subagents create no handoffs or Git mutations. Freeze source hashes during consequential runs.

## Acceptance and outputs

Each target has an attempt record and each substantive result its own THEORY-template file, exact status, proof, assumptions, dependencies, limitations and checks. Preserve failed/deferred routes. Maintain LOG/plan/proposals/independent-checks and blob/output identity manifest. Stage new durable files before running code/evidence_manifest.py; do not commit unfinished stdout as completed evidence. Committed generated artifacts <=1MB each, <=5MB total; no splitting. Push each degree/target boundary and about every10min with changes using Andrey Chesnokov <aacchhee@gmail.com>, Agent: Codex and honest exact model/effort trailers. Keep draft PR WORK / AUDIT(PENDING) / PR current.

At all ordered stops, record outcomes and open obligations, Windows intended results entry under Runs needed (no bridge is exposed), and set Stage AUDIT. Commit final development outputs first; in a later commit change only this status to done in OUTPUT_SHA and create02-audit.md with full candidate input SHA/scope/commands and Claude Opus5.5xhigh instruction. Push before the final reply. User explicitly requires final short report and exact final prompt “Claude (Opus 5.5 xhigh): Audit codex/padua-proof-attempts-2-20261101.”; that overrides generic Continue wording. Required Claude audit is not completed by these Codex checks.
