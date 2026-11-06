# Handoff 06 — padua-mz-sharp-constants-20261106 — focused denominator recheck

- Status: open
- Previous handoff: [05-response-02.md](05-response-02.md), done in 99fd6c0e7a0d8912e087c81bfd9bbd6654ca6330
- Next agent / model / effort: Claude, Opus 5.5 high (mathematical audit); record actual model/effort and any bounded delegated checks.
- Role: auditor and topic orchestrator
- Branch: `codex/padua-mz-sharp-constants-20261106`
- Input head SHA: `99fd6c0e7a0d8912e087c81bfd9bbd6654ca6330` (response outputs; this handoff is published in the following commit)
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`
- Stage: AUDIT
- Written by / date: Codex coordinator, requested gpt-6-astra high; serving metadata unexposed · 2026-11-06

## Task

Read current rules and record their SHA. Fetch main and the topic head before acting; reconcile without rewriting published history. Carry out the focused recheck required by audit-02 B2 and handoff05. The mathematics and certificates of P1–P4 were already accepted by audit-02; do not reopen them wholesale or launch a new numerical campaign.

1. Independently reconstruct the new durable proof in theory/P4-denominator-closed-form.md (PD-T?mz-sharp-codex-P4-02). Canonical basis is F_j(t)=2(-1)^j a_j² sin(t)/[t(t²-a_j²)], a_j=pi*j, with t dt denominator. Check every positive integer i,j, all removable singularities and absolute convergence, common finite-cutoff cancellations proving I(a)=-Cin(2a)/(2a²), both off-diagonal index orders, direct diagonal partial fractions, integration-by-parts boundary limits, and the translated sine integral yielding K(a)=Si(2a)/(2a). Check the finite quadratic-form conclusion and the unchanged S2/P4 application. The distinct Astra supplementary proof check passed, but does not replace this Claude recheck.
2. Confirm B1 and C1–C4 by the response diff against f3c14d7599b4bf25118ca86bc62aeb5e0fcafe29, guided by response-02.md. In particular:
   - B1 dated corrections in all five requested records distinguish essentially postdictive Qmin secants from the three prospective criteria. Pre-existing m1400/1401,1800/1801,3000/3001 values at5110954 predate the protocol; no threshold/receipt/PASS or K4 outcome changes.
   - C1 excludes any audit-*-support path component; all audit/support bytes remain unchanged. Only manifest code and the new pinned input receipt differ among developer inventory members; every original scientific evidence byte remains unchanged.
   - C2 preserves original S1 disposition wording in History, restores the S2 definition/prediction label, updates stale local-proposal/report/P3 status text, and distinguishes PD-T020 preparation deferral from AC's A3 decision on PD-T027/381. P1's broad interval certifies no useful digits.
   - C3 adds IDEA-466 with the finite signed Padua witness versus endpoint quotient/kernel rectangle separation and the promised delegated P1/P3 gate provenance. Existing continuation verdicts stand.
   - C4 documents P1 prose hashes as historical, and documents that P2 validation/overlap are procedural main-release prerequisites rather than enforced by standalone summary code. This permitted documentation alternative changes no result-bearing code or receipt. P3 wording changes only the requested z range, physical-half coordinates and dx=sin(theta)dtheta<=dtheta.
3. Run the manifest/integration checker below and review publication scope. No new numerical rerun is needed: result-bearing code, inputs and receipts are unchanged, and all consequential numerical reruns are already accepted by audit-02. If a concrete concern justifies an additional check, document its exact purpose and actual execution; keep existing resource/scope limits.

## Read first

AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md; handoff05; audit-02.md findings B1/B2/C1–C4; response-02.md; LOG.md handoff05 entries; theory/P4-denominator-closed-form.md and independent-checks-P4-denominator.md. Read the exact canonical S2 definition and the changed S2/P4 citations. The accepted earlier derivations are in independent-checks-S2-model.md:66–100 and independent-checks-P4.md.

For diff checks read the five B1 records, audit-02-support/P24/P2-preexisting-predictivity.json, IDEA-466 and the three changed novelty records, the S1 history addenda, P3 wording diff, local manuscript proposal and integrity-checks.md. The new proof is a durable writeup of already accepted algebra, not a new mechanism or priority claim; scope the novelty read accordingly and state the exception. No external literature theorem is imported.

## Verification

From repository root:

```
python topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --checks
```

The response output snapshot verifies91 identities,30 Python ASTs,103 JSON files and430 local links across106 Markdown documents; the handoff-only commit adds this Markdown document and is separately checked. The generator parses/sizes audit support JSON while excluding audit-*-support from developer hash inventory. Compare any current counts to the actual published head rather than treating historical counts as invariants. Prose records are not checker-pinned.

## Scope limits

- No edit to audit-01, audit-02, any audit-*-support, accepted statement/proof, original registered protocol body, numerical receipt, threshold or outcome.
- No new numerical campaign, upper Padua run or Syvert. No shared registry, final ID, reservation, manuscript proper, main, tag, workflow or settings change; no merge/force-push. AC alone merges.
- This is the third audit round. Apply WORKFLOW's proportionate-audit rule: fix each MINOR wording/link/stale-text/already-documented-decision issue in place when it fits the permitted limits; list every fix and commit those fixes separately from the audit report. Do not silently repair material mathematical/proof/code/status changes; return such findings to the developer.
- A3 remains AC's decision for PD-T027/PD-T381. PD-T020's full target is already proved by P3-03+S1-02; its registry application belongs to PR preparation and readiness, not this audit.

## Acceptance and outputs

Write audit-03.md identifying the exact input SHA, actual model/effort, coverage, independent reconstruction, commands actually executed, findings and remaining scope. Confirm B1/C1–C4 by diff; accept B2 if all cases are supported, or return concrete material findings. This is a focused recheck, not another audit of all prior mathematics.

Update LOG and PR31 AUDIT/PR sections. If accepted, stage PR and hand off07 to preparation: current-main/open-PR reservation refresh, final IDs and registry application by reviewed diff, A10 obligations, AC's A3 decision and subsequent readiness verification. Do not mark ready or request merge until those later steps are complete. If material findings remain, stage WORK and hand off07 for a bounded developer response.

Commit outputs first. In the following commit change only this handoff's status to done in the audit-output SHA and add the next numbered handoff with that output as input. Exactly one open handoff remains. Preserve published history and AC's approved GitHub noreply author identity.
