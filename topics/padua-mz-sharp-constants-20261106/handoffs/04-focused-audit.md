# Handoff 04 — padua-mz-sharp-constants-20261106 — focused audit of closing development

- Status: open
- Previous handoff: [03-response-and-work.md](03-response-and-work.md), done in 2429e750cedb18b0a7903e7ed10dd3296a181204
- Next agent / model / effort: Claude, Opus 5.5 xhigh; allocate distinct bounded checks as appropriate under the workflow.
- Role: auditor and topic orchestrator
- Branch: `codex/padua-mz-sharp-constants-20261106`
- Input head SHA: `2429e750cedb18b0a7903e7ed10dd3296a181204` (scientific outputs; this handoff is published by the following commit)
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`
- Stage: AUDIT
- Written by / date: Codex coordinator, requested gpt-6-astra high; serving metadata unexposed · 2026-11-06

## Task

Read the rules at the branch head and record that SHA. Fetch main and topic head first; reconcile without rewriting published history. Audit only the material changes since audit-01's accepted scientific candidate5110954 and the response/closing work authorized by handoff03. Do not repeat the accepted old S1/S2/S3 proof audit unless a new dependency actually requires it. Supplementary Astra checks are evidence, not this required Claude audit.

1. Check response-01 against audit-01 A1–A13. Response-first commit17ca9f441cece178354e70504a6c739df501a224 precedes every new D calculation. Check A1/A2 interpretation/disposition and the new S1/S2/S3 MEASURED records; check minor fixes by diff. A3 remains explicitly unresolved for AC; no registry mapping has been selected. A10 shared consolidation and final IDs remain for PR preparation. Optional raw files are neither archived nor authoritative; committed essential evidence supports every new claim.
2. P1: reconstruct the elliptic kernel's equality with the accepted product-cutoff limit, the two-step positivity/simple groundstate proof and c_minus=-norm(B), 0<c_plus<norm(B). Check the rectangle finite reduction, all triangle boundary cells, elementary interval enclosures and actual coarse norm certificate. The certificate is broad and claims no useful decimal digits; three-digit values and a c_plus-specific residual/Galerkin certificate remain deferred. Do not silently promote these to decimal success.
3. P3: reconstruct the signed remainder, sharp discrete primitive and full interpolation assembly. Check leading coefficient2sqrt(2)/pi^2, exact weights/endpoint factors, microscopic and bulk cells, opposite/central terms, full Pi_N and constrained Pi_(N-1), all integers/parities. New local PROVED claim is the full scaled minimum limit pi^4/8. Original K2 remains unchanged and is no counterevidence.
4. P4: check the finite Rayleigh reduction, committed exact hex trial, scalar series/Laplace remainders, integer directed arithmetic and actual independent grouped rerun. Claim is Lambda_edge>=1.0044369 only. The narrow interval belongs to one trial quotient and is not an upper enclosure of Lambda_edge. Practical upper certification remains deferred.
5. P2: verify prospective publication order, b2/K/order calibration, independent dense validation, replay of the known audit400 overlap, the four main rows, fixed projector/branch-rate/secant criteria and numerical guards. Distinguish pre-existing overlap from prospective evidence. Inspect the returned-and-fixed summary prerequisite bug and independent synthetic control checks. Check the actual main-case independent rerun and exact final outcome; no two-term asymptotic or crossing-degree claim, no revision of K4.
6. Verify the final developer manifest, generated-file limits, local links and unchanged audit-01/support. Its scope deliberately excludes audit-01-support. Verify no shared registry, reservation, final ID, manuscript or accepted scientific proof beyond permitted editorial edits was changed.

## Read first

AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md; LOG.md closing entries; response-01.md; audit-01.md; report.md; results/padua-mz-sharp-constants-20261106.md; gates.md and the P1/P2/P4 frozen protocol blobs at their stated publication commits. For novelty-bearing checks read the complete state/IDEAS.md, applicable full predecessor entries/obstruction tables and novelty-gate-P1.md through P4.md. Preserve the response's limited literature coverage; it makes no priority claim.

New theory: P1-elliptic-kernel.md, P1-positive-spectrum.md, P1-rectangle-certificate.md, P1-numeric-certificate.md; P3-signed-remainder.md, P3-discrete-primitive.md, P3-reverse-bound.md; P4-certified-lower.md; P2-measurements.md; S1/S2/S3-measured.md. Read their supplementary independent-checks reports and exact code/input/evidence identities. Audit requests may identify prose by this input commit; new checkers must not freeze prose hashes as permanent invariants.

## Reproduction

Run from repository root with one BLAS thread. Use separate /tmp output paths; preserve every consequential actual rerun as small committed evidence. Inspect exact recorded commands and software identities before execution. No original K gate is rerun with revised thresholds.

```
python topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --checks
python topics/padua-mz-sharp-constants-20261106/code/P1_rectangle.py --N 16 --theta 256 --output /tmp/audit02-P1-N16.json
python topics/padua-mz-sharp-constants-20261106/code/P4_check_grouped.py --trial topics/padua-mz-sharp-constants-20261106/evidence/P4-trial-J512.json --producer topics/padua-mz-sharp-constants-20261106/evidence/P4-rayleigh.json --output /tmp/audit02-P4-grouped.json
python topics/padua-mz-sharp-constants-20261106/code/P2_summary.py --output /tmp/audit02-P2-summary.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/P2_modes.py validate --output /tmp/audit02-P2-small.json
```

For consequential main computation choose a proportionate independent rerun, using P2_modes.py run --m 1600 or an independently implemented fixed comparison, and report exactly what was executed. The synthetic control driver writes its developer receipt by default; inspect it and its ten-test evidence, and use a disposable workspace copy if rerunning it, preserving the original receipt. Existing distinct m1600 execution may guide the audit depth; do not claim reading it is your own rerun. Respect at most2 heavy processes globally,6h/run48CPUh cumulative, no Syvert, no upper Padua campaign or retry. No new numerical mechanism or retrospective threshold is authorized.

## Scope limits

- Never modify audit-01 or audit-01-support, original K0–K5 criteria/receipts/outcomes, earlier handoff bodies or accepted proof statements.
- No shared registry, final-ID assignment/reservations, manuscript, main, tags, settings or workflows; no merge/force-push. AC alone merges and decides A3 mapping.
- New mathematical claims/status/proof/code/input/threshold changes are material and return to development; do not silently repair them as minor audit edits. This is audit round02, so ordinary developer/auditor separation applies.
- Keep original-target registry application for later PR preparation/readiness. The local P3 completion does not authorize changing PD-T020 during this audit.

## Acceptance and outputs

Write audit-02.md identifying input SHA, actual model/effort, exact coverage, commands actually run, findings/severity and residual risks. Review all retained candidates and explicit deferrals. Every computer-assisted PROVED claim needs the finite reduction, inspected exact arithmetic/checker, committed inputs/evidence and actual independent rerun. MEASURED tests must preserve their finite scope and guard precedence.

Update LOG and PR31 AUDIT/PR sections. If material findings remain, stage WORK and handoff05 to Codex for bounded response; otherwise record acceptance and handoff05 to PR preparation, preserving AC's unresolved A3 decision and all A10 obligations. Do not mark ready or ask for merge while those preparation/readiness steps are outstanding.

Commit audit outputs first. In a following commit change only this handoff's status to done in the audit-output SHA and add the next numbered handoff, identifying that output as its input. Exactly one open handoff remains; preserve all published history and the approved GitHub noreply author identity.
