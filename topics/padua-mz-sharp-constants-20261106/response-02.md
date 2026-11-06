# Response to audit-02 — bounded records response

- Input/rules head: `f3c14d7599b4bf25118ca86bc62aeb5e0fcafe29`.
- Branch: `codex/padua-mz-sharp-constants-20261106`.
- Scope: [handoff 05](handoffs/05-response-02.md); accepted statements,
  thresholds, receipts, statuses and audit/support files are preserved.
- Records worker: Codex, allocated `gpt-6.1-sol` medium; actual runtime
  model/effort metadata not independently exposed. The coordinator records
  the B2 developer/checker allocations and integration commit in LOG.
- Output commit: the scientific response input identified in handoff06,
  published immediately before the handoff-only commit. All FIXED rows
  below are included together. This is a developer response, not
  independent audit acceptance.

| Finding | Disposition | Concrete response / remaining integration |
|---|---|---|
| B1 MAJOR | FIXED | Dated addenda in [P2 measurements](theory/P2-measurements.md#2026-11-06-audit-02-b1-scope-correction), [P2 idea](ideas/P2.md#2026-11-06-audit-02-b1-scope-correction) and [protocol](ideas/P2-protocol.md#2026-11-06-audit-02-b1-scope-correction) give the exact six Q_min endpoints already published at `5110954`, before `d03e74d`. The secant-to-b2 criterion is essentially postdictive; only mode-2 weight, L-distance and branch-difference rate were prospective. Existing audit diagnostic is linked. Historical protocol prose, thresholds, receipts, PASS_FINITE_TEST and K4 remain unchanged. The same dated correction is integrated in report.md and the results file. |
| B2 MAJOR | FIXED; focused Claude recheck required | New PROVED supporting record [P4 denominator derivation](theory/P4-denominator-closed-form.md), provisional PD-T?mz-sharp-codex-P4-02, supplies all diagonal/off-diagonal cases, common cutoffs and boundary terms. S2 endpoint-model and P4 lower-bound cite it. Distinct gpt-6-astra high reconstruction [PASS](independent-checks-P4-denominator.md) follows an independent derivation from the canonical basis before reading the new proof. No numerical run was performed or needed. Material scope is this derivation only; no accepted P4 status is withdrawn, and developer/supplementary review does not replace the focused Claude recheck. |
| C1 MINOR | FIXED | [evidence_manifest.py](code/evidence_manifest.py) excludes any path component matching `audit-*-support` via `fnmatchcase`; its scope string matches. All other inventory semantics remain unchanged. Audit support is untouched. The coordinator intentionally regenerated the manifest: 91 identities; all 90 original identities preserved except the manifest code itself, plus the new pinned input receipt. All original scientific evidence bytes are unchanged. `--write --checks` and final `--checks` pass with exit0; final counts are in LOG and integrity-checks.md. |
| C2 MINOR | FIXED | Dated History entries in [S1 model](theory/S1-model.md#2026-11-06-audit-02-c2-wording-history) and [S1 idea](ideas/S1.md#2026-11-06-audit-02-c2-wording-history) preserve original “operationally rejected” wording and explain the response-01 correction to deferred. [Manuscript proposal](manuscript-insert.md) records audit-02 acceptance and P3's proved exact limit; manuscript proper is untouched. [P3 status prose](theory/P3-reverse-bound.md#status-by-part) records completed assembly acceptance and registry deferral. S2 has its explicit registered-prediction status label. Report stage/counts and report/results PD-T020 deferral are updated: local P3-03 plus S1-02 proves the original target, but registry application waits for PR preparation, separately from AC's A3 decision on PD-T027/PD-T381; add “no useful digits” beside P1's long decimal interval. |
| C3 MINOR | FIXED | [P4 gate](novelty-gate-P4.md), [P4 idea](ideas/P4-rayleigh.md) and [P1 numerical protocol](ideas/P1-numeric-protocol.md) identify IDEA-466 and link its full predecessor candidate, read for this correction. Separation is the certified object/reduction (finite signed Padua witness versus endpoint-model quotient or kernel rectangle bounds), not outward dyadic arithmetic. Existing technical-continuation verdicts stand. P4 gate now links [P1 provenance](novelty-gate-P1.md) and [P3 provenance](novelty-gate-P3.md), with delegated-coverage limits explicit. No new mechanism or priority claim. |
| C4 MINOR | FIXED by documentation/wording | [P1 numerical certificate](theory/P1-numeric-certificate.md#2026-11-06-audit-02-c4-historical-prose-hash-labels) labels both receipt prose-hash fields historical (`c1e6e59` blobs), not current acceptance conditions. [P2 prerequisite addendum](theory/P2-measurements.md#2026-11-06-audit-02-c4-summary-prerequisite-procedure) states that summary code checks calibration/main guards while validation/overlap are procedural pre-release requirements; links existing receipts and release log. No P2 code change or numerical rerun is needed or claimed. P3 wording restricts e's monotonicity to 0<z<2pi, identifies theta in [0,pi/2] as x in [0,1], and writes the physical-measure comparison dx=sin(theta)dtheta<=dtheta with endpoint reversal. |

## Scope and next review

Audit-02 accepted P1–P4 mathematics and certificates at their recorded
scopes; this response does not reopen them. No new numerical run, theory
mechanism, accepted proof step or status change is claimed. B2 adds a
supporting derivation and is material new proof text. A focused Claude
recheck of that derivation and diff confirmation of B1/C1–C4 remain the
next review. Shared registries, final IDs, reservations, manuscript proper
and AC's A3 decision remain for the authorized later preparation step.

All requested record edits and coordinator integrations are complete.
The following handoff06 identifies this exact output commit and requests
the focused Claude B2 recheck plus B1/C1–C4 diff confirmation.
