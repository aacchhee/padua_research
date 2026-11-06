# Handoff 03 — NN MOP conditioning — Codex response to audit 01

- Status: done in b3350adf2e7f9270f0bca8558b1ac668c7826291
- Previous handoff: [02-audit.md](02-audit.md)

- Next agent / model / effort: Codex, `gpt-6.1-sol` high (for the MAJOR-1 classification and MAJOR-3 negative-result records; medium is enough for the MINOR record edits)
- Role: developer and topic orchestrator for this step
- Branch: codex/nn-mop-conditioning-20261106
- Input head SHA: `c5f2820232885fe78504a9bae75b6da68491b1be` (audit-01 output commit; this handoff is published in the following commit)
- Audited candidate: `cc1edd20a27f955f2f028e988e525889ddfbc805`
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8` (refresh at start)
- Stage: WORK
- Written by / date: Claude, Opus 5.5 xhigh · 2026-11-06

## Task

Answer every finding of [audit-01.md](../audit-01.md) in a new `response-01.md`. For each finding give one of: a fix (with file and line), an evidence-based rejection, or an explicit unresolved item. Then hand the topic back for a focused re-audit.

1. **MAJOR-1, PD-T448 classification.** Propose explicitly whether PD-T448 becomes PARTIAL or stays OPEN.
   - For PARTIAL: decompose PD-T448's own statement into conjuncts and cases. The Krawtchouk liminf = limsup = 5+2√6 conjunct is PROVED by c2-sharp-upper.md together with PD-T437. The remaining conjuncts stay OPEN: the Krawtchouk subexponential factors and useful constants/radius, and every Hahn conjunct.
   - For OPEN: give a reason that addresses the PARTIAL criterion in agents/WORKFLOW.md.
   - Either way, write the decision as a dated addendum or history note proposal inside the topic. The predecessor PD-T448 file and PROOF_STATUS.md are shared registries and are edited only at PR preparation. Preserve PD-T448's original wording.
   - Make "Split from:" wording consistent (MINOR-6).
2. **MAJOR-2, attribution.**
   - Add a dated C1 gate addendum covering LIT-502/LIT-348 (diagonal norm-balancing scaling) and Fischer 1998 (LIT-113, LIT-112, LIT-365, IDEA-087/088). State the separation: LIT-502 measures an algorithm's residual under basis scaling, while C1 is about forward-map conditioning in the fieldwise metric.
   - Add LITERATURE-qualified attribution lines in c1-scalar-derivative.md.
   - Add one distinguishing sentence each in report.md and note-material.md.
   - No claim changes.
3. **MAJOR-3, C2 failed subroutes.**
   - Give rounds 4–6 provisional IDEA records per templates/IDEA.md, or register them explicitly as subforms of C2-03.
   - For the round-5 counterexample (ΔU(0) = −6 at M=3, t=1) and the round-6 loss bound ‖D‖∞ ≥ 2^M/[M(M+1)], either write scoped PD-N records with status and scope per templates/THEORY.md, or record why they are minor routine route notes.
   - Add a status header or attempt-record label to c2-hahn-upper-search.md.
4. **MINOR 1–11.** Fix them as listed in the audit. In particular:
   - update the results file (Hahn terminal rate, gauge ρ_H corollary, PD-N, matrix theorem, provisional IDs) and correct LOG.md:182–183;
   - repair the c1-error-comparison receipt pin and add the c1-matrix-all.json raw pin;
   - qualify the C3 "232 completed" claim and maxima as platform-specific, recording the audit rerun outcome;
   - make c4_compare.py record a native breakdown status instead of raising KeyError;
   - document the actual M2 bit-exact command and its ordering;
   - give c3-weak-stability-open.md and c4-measurements.md provisional IDs, and state the C3 target's relation to PD-T449;
   - move the C2-hard check into code/ and pin it.

   Code changes (MINOR-2, -4 and the C2-hard move) are result-bearing; rerun the affected producer or checker and show that the scientific payload is unchanged.
5. **NOTEs.** No action is required. NOTE-1 is optional: you may state the gauge-infimum attainment observation, or prove it as a new claim. If you prove it, that is new mathematics and must go to audit. Handle NOTE-2, the possible AT-system normality predecessor, at least with a qualifier in note-material.md before any external use.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- [audit-01.md](../audit-01.md) and [audit-01/claude/README.md](../audit-01/claude/README.md).
- LOG.md, the theory files named in each finding, and topics/nn-mop-stability-20261105/theory/conditioning-growth-target.md (PD-T448).
- The literature/INDEX.md rows LIT-112, 113, 348, 365 and 502, and state/IDEAS.md IDEA-087/088.

## Scope limits

- Do not reopen accepted theorems or measurements beyond the listed findings.
- Do not edit the audit report or earlier handoff bodies.
- No shared registry edits, final-ID reservation or allocation in this step. Those belong to PR preparation after re-audit.
- Do not touch `main`, `.github/`, tags or other topics. Never merge or force-push. Only AC merges.

## Acceptance and outputs

- `response-01.md` answers all 3 MAJOR and 11 MINOR findings explicitly.
- The fixes are committed, `code/verify_evidence.py` passes, and the evidence manifest is updated for any changed code or data.
- The LOG records the response.
- The MAJOR changes (classification, dispositions, PD-N records) are material, so set the stage to AUDIT and open handoff 04 for a focused Claude re-audit of those changes only, Opus 5.5 high or xhigh. Its input SHA is the response output commit. MINOR-only fixes are confirmed by diff in that re-audit or in the readiness check.
- If the response rejects a MAJOR finding with documented reasons and changes no claim, it may still go to the focused re-audit; the disagreement is preserved for AC.
- Commit the outputs first. Then, in a following commit, set this status to `done in <sha>` and add handoff 04.
