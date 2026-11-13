# Audit 04 — auditor MINOR fixes (dated companion note), 2026-11-08

Auditor: Claude, claude-opus-5-5 xhigh audit; edits applied by a mechanical subagent from the audit04 sub-reports.

These are the third-round-onward auditor in-place fixes allowed by `agents/WORKFLOW.md`, "Proportionate audit and records". They are limited to wording and formatting, links, stale process text and recording an already documented decision. They are committed separately from the audit report. No claim, status, ID, ID kind, disposition, `Split from/into` header, threshold, code, input or evidence JSON is changed. Hash-pinned prose is not edited; its corrections are in this companion note ("companion" below). Pin check: `grep -l <path> evidence/*.json evidence-manifest.json` before each edit. Pinned: `pruning-results.md`, `pruning-artifacts.md` only.

Source IDs: A1/A2/A3 = sub-reports on lattice, T8 half-shift and response-03 records; B1/B2/B3 = U1/U2/U3; D = pruning; NV = novelty/protocol. Line numbers are post-edit approximate positions in the file.

## Applied fixes

| ID | File:line | Kind | Summary |
|---|---|---|---|
| A1-W1 | `attempts/T10-round08.md:31` | direct | "Exact-N positive unshifted lattice sets" becomes "Exact-N positive unshifted Padua-type (rank-N) lattice sets ... ; positive exact-N rules of lower rank exist at n3 and n4". (LOG part returned.) |
| A1-W2 | `theory/r08-lattice-complement.md:1,15,17,26`; `theory/r08-lattice-reduction.md:62`; `attempts/T10-round08.md:31`; `independent-checks-round08-lattice.md:164,173,232` | direct | "unisolvent" for sets with more than N nodes becomes "full-rank"; :15 reads "requires exact Pi_n evaluation rank N (Pi_n-determining; unisolvent exactly when \|X\|=N)". |
| A1-W3 | `theory/r08-lattice-higher.md:46,63` | direct | "full independent coverage" becomes "full coverage; independence comes from the separate complete replay"; n6 continuation sentence reworded to "q673..720 ... after completing q673..703". |
| A2-F1 | `theory/t8-r08-halfshift-measurements.md:17`; `attempts/T8-round08.md:77`; `novelty-gate-T8-round08.md:139` | direct | D2 trigger "not met" becomes "cannot be assessed (not fired)". (The "has not fired" wording at measurements:30ff already conforms.) |
| A2-F2 | `theory/t8-r08-halfshift-measurements.md:44,63` | direct | Header "scan seconds" becomes "degree seconds"; residual sentence now "1.16e-13; all three conditions are far below the 1e12 guard". |
| A2-F3 | `theory/t8-r06-measurements.md:8` | direct | Dated pointer paragraph added below the header block (header lines themselves untouched) linking the split to `PD-T?...-T8-r08-02` ([t8-r08-old-finite-existence.md](theory/t8-r08-old-finite-existence.md)); quality rows stay MEASURED. |
| A2-F4 | `attempts/T8-round08.md:86` | direct | Original half-shift receipt SHA256 `87561592b48fcdcf062568b2e5a0a5586108e33d66c6f1518d24744f2d6c755b` inserted after "13,097bytes,". |
| A3-m1 | `response-03.md:41` | direct | Dated Audit04 note after the E4 text gives audit-03's alternative CONDITIONAL reading and the Chkifa preprint caveat. No label changed. |
| A3-m2 | `attempts/T10.md` (end); `theory/t10-quality.md` (end); `theory/t10-parity-log4.md` (end) | direct | Dated notes: round06 "CONDITIONAL sharp corollary" / "log³ remains OPEN" are old labels; current proposed labels are in `t10-log3-*.md`, pending AC's E4 decision. |
| A3-m3 | `theory/t9-r06-phase-weight-boundaries.md:76` | direct | The replaced q2 sentence (9042e1c line 11) is quoted in the History note. |
| A3-m4 | `literature-round06/t10-kernel-sources.md` (end) | direct | Note: inspected artifact is arXiv 1801.00608v1; "published theorem statement" means the posted v1 statement. |
| A3-m5 | `novelty-gate-supplement-round08.md:21` | direct | Link to the dated gate coverage qualification added. |
| B1-M1 | `theory/u1-ordinary-ls-blue.md:60` | direct | Scope note: "fixed total replication budget" means balanced replication (B/M per node); unequal optimized repeats are a different normalization. |
| B1-M2 | `theory/u1-operational-comparison.md:114` | direct | "per-observation variance is smaller" becomes "raw unit-noise trace tr(CC^T), with one observation per node, is smaller". |
| B1-M3 | `u1-continuation-protocol.md:174` | direct | Note: the "interpretation clarification" paragraph was first committed with the C2 outcome in 0a98cea; no gate, threshold, comparator or seed changed. |
| B2-m1 | `usable2.md:387`; `theory/u2-admissible-norm.md:115` | direct | Regression summaries now also list n4 rational Sobol RMS +0.33%, n2 Gauss cosine RMS +2.47%, n2 Sobol absolute-value RMS +6.45%. |
| B2-m2 | `theory/u2-degree12-unisolvence.md:38` | direct | Assumptions addendum: checker verifications are `assert` statements; trusted execution is CPython without -O; receipt does not record `sys.flags.optimize`; audit rerun used default flags. |
| B3-m1 | `theory/u3-quality-failures.md:55`; `usable-report.md:110` | direct | n8 QR 45.54 depends on floating pivot ties; alternative resolution gives 35.61/35.82 ([audit-03/T10](audit-03/T10.md)); every U3 loss is larger against it; n3..7 tie-invariant. |
| D-m2 | `theory/pruning-exact12.md:85` | direct | Producer-row note: historical creator revision at e761a12; current shared checker 16024 B, SHA256 `ab3b092c...0241`; link to compatibility section. |
| D-m3 | `pruning-summary.md:51` | direct | One-observation-per-site traces added (1.0595/1.3304/0.6961 at degree 12; 1.0864/1.3584/0.6888 at degree 16); fixed-B values repeat 91/214 sites twice. |
| NV-F2 | `rounds.md:23` | direct | Dated auditor pointer (no count change) to continuation results (U1 4/10, U2 7/10, U3 5/20) and pruning 5/15. |
| NV-F4 | `COLD_STORAGE.md` (end) | direct | Pointer section: continuation and pruning batches have no cold-storage delivery; raw inventories are in the evidence receipts; essential payloads committed. `cold-storage.json` untouched. |
| NV-F5 | `usable-campaign.md:26`; `usable3.md:28`; `report-round08.md:50`; `theory/r08-lattice-complement.md:93` | direct | Attribution of the half-shift cubic / n2 Padua-type leads to Claude audit-03 (handoff08 item 7), with links. |
| D-m1 | `pruning-results.md:10-11` (pinned) | companion | Correct to: "P1 consumes **1 research round** (root publishes count boundaries); the completed campaign count after P5 below is 5/15." The "4/15" there is stale; actual count is 5/15 (see `pruning-summary.md`). |
| D-m4 | `pruning-artifacts.md` after line 76 (pinned) | companion | Chronology note: the degree12 build (09:48:29 UTC) followed P3's published pass 5623097 but preceded the commit of `pruning-certificate.md` and the P4 appendix (55a6a11, 09:52:00 UTC); the "If P4 passes ... deliver" condition therefore governed only the degree16 export in practice. IDs, rank and measurements are unaffected. |

Total: 23 direct fix IDs (about 45 individual text edits across 31 files), 2 companion corrections.

## Returned to developer or orchestrator

Returned to developer:
- A2 MAJOR-1 (n7 selection `(1,17,212)` vs exact-tie rule), A3 M1 (stale pin in `evidence/independent-r06-pins.json`), A3 M2 (Split from/into disagreements), B2 MAJOR-1 (C1 cost-gate non-reproducibility; addendum or disposition change), NV N-M1 (pruning gate omits LIT-385/386 and design sources), NV N-M2 (candidate/negative records, P5 PD-N, IDEA records, provisional-ID agent component), NV N-M3 (repository generated-output budget; AC decision).
- B3 MINOR-2 (F tie tolerance relative vs absolute): a threshold deviation disclosure, outside auditor-fix limits.
- All NOTEs in every report (no action required), including A1 N1/N3 (packing-free minima, auditor n6/n7/n8 runs; any LITERATURE-dependency change is material).

Returned to orchestrator:
- A1-W1 LOG part: `LOG.md:539-540` "no exact-N positive full-support unshifted rule" becomes "no exact-N Padua-type (rank-N) positive full-support unshifted rule at n3..7".
- NV-F1: stale next-step line `results/padua-3d-20261106.md:319` (repo-root results file).
- NV-F3: LOG handoff links (`LOG.md:842` link to handoff 15; new line after `LOG.md:895` for handoffs 16/17).
- NV-F6: missing word spaces (example `results/padua-3d-20261106.md:8`; LOG 845-895): LOG and root results are orchestrator-owned; the generic "summaries" occurrences were not enumerated by the report and were not edited here.
- LOG entry for these fixes.
