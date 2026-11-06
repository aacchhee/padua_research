# Handoff 07 — padua-mz-sharp-constants-20261106 — PR preparation

- Status: open
- Previous handoff: [06-focused-denominator-recheck.md](06-focused-denominator-recheck.md), done in 61c3b3f2b0fe8e6a0c93f0477c5f2b9e4f27445c

- Next agent / model / effort: Codex coordinator, `gpt-6-astra` high. Use `gpt-6.1-sol` medium for mechanical registry and ID edits, and record actual models.
- Role: developer and topic orchestrator (PR preparation)
- Branch: `codex/padua-mz-sharp-constants-20261106`
- Input head SHA: `61c3b3f2b0fe8e6a0c93f0477c5f2b9e4f27445c`. This contains audit-03 (`6011f73`) and its separately committed in-place MINOR fixes; the commit publishing this handoff comes later.
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`
- Stage: PR
- Written by / date: Claude, claude-opus-5-5 (high) · 2026-11-06

## AC decision (binding, recorded 2026-11-06)

Asked in this session to rule on audit-01 A3, AC chose **"PARTIAL (Recommended)"** for PD-T027 and PD-T381.

- **PD-T027 → PARTIAL.** These conjuncts of its own statement are PROVED under split-off IDs:
  - the uniform endpoint upper gap (S2-01);
  - existence of the sharp upper limit and its identification as Λ_edge (S2-05, with S2-02/03/04/06 and P4-02 as dependencies).

  The value conjunct (a decimal evaluation of Λ_edge) stays OPEN. P4's one-sided Λ_edge ≥ 1.0044369 is a PROVED supporting result, not a resolution of that conjunct.
- **PD-T381 → PARTIAL.** These are PROVED under split-off IDs (S3-02, S3-kernel, S3-03, with P1-01/02/03/04):
  - existence of the even/odd logarithmic limits of λ_±(m, m−1);
  - their agreement, and hence the full-integer limits;
  - their exact characterization as inf/sup σ(B).

  The values conjunct (decimal values of c_±) stays OPEN. The P1 enclosure certifies no useful digits.
- Record the decomposition explicitly in each target's History, without rewording the original target text, and record the original-to-split mapping in `ID_CROSSWALK.md`, all per WORKFLOW's split rules.

## Task

Carry out WORKFLOW step 5 (PR preparation) for this topic:

1. **Refresh and reserve.** Read the rules at the branch head and record the SHA. Fetch current main and every open PR, drafts included. Run the full reservation procedure in WORKFLOW **Reserve fresh ranges; never reallocate**: read every ledger, the used final IDs in `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md` and `ID_CROSSWALK.md`, and the retired reservations. Reserve fresh PD-T, PD-N (if any), IDEA and LIT ranges with headroom. Record them at once in `topics/padua-mz-sharp-constants-20261106/ALLOCATIONS.md` and in the PR body, with the heads checked. If main has moved, merge `origin/main` into the branch; never rebase published history.
2. **Final IDs.** Map every provisional ID in this topic to a final ID and record each mapping in `ID_CROSSWALK.md`:
   - PD-T for S1-01/02/model/measured, S2-01…06/measured, S3-01/02/03/04/kernel/measured, P1-01…04, P2-measurements, P3-01/02/03, P4-01/02;
   - IDEA for every retained, deferred or consolidated candidate;
   - LIT for any new literature record.

   Map S3-kernel's nonnumeric provisional suffix explicitly. Do not renumber accepted IDs.
3. **Registry application by reviewed diff.** Edit directly `PROOF_STATUS.md`, `state/IDEAS.md`, `state/CURRENT.md`, `ID_CROSSWALK.md`, `RESULTS.md` (this topic's section only, from `results/padua-mz-sharp-constants-20261106.md`), and literature records only if needed.
   - **PD-T020 → PROVED**, linked to P3-03 together with S1-02. Its original statement ("existence/value of sharp rescaled endpoint limit") is met in full: lim (log N)²λ_min = π⁴/8 through all N and both parities (audit-02).
   - **PD-T027 and PD-T381 → PARTIAL**, per AC's decision above.
   - Register the MEASURED records (S1/S2/S3-measured and P2) as distinct MEASURED claims.
   - Carry out the audit-01 A10 obligations: register S2-01 as the consolidated continuation of IDEA-386; S3-02/S3-03 meet IDEA-470's resume condition; update IDEA-054, IDEA-071, IDEA-466 (as predecessor of P4/P1-04), IDEA-469 and IDEA-470; update the MZ obstruction memory at `state/IDEAS.md:406` and the PD-T027 notes near lines 938/942; correct `open-upper-limit.md`'s "gaps decay like N^−1" note if it is stale.
   - The S1 equality candidate's disposition becomes resolved via P3: the deferred route's resume condition is met. Record it accordingly; no PD-N.
   - Registries carry only claim content, status, dependencies, dispositions and links (WORKFLOW **No process stage in shared registries**).
4. **Topic records.** Update `report.md`, the results file, LOG, `manuscript-insert.md` (proposal only; the manuscript proper is untouched unless AC asks) and the PR31 WORK/AUDIT/PR sections. Run `code/evidence_manifest.py --checks`. Remove completed preparation tasks from the shared frontier or describe their post-merge state.
5. **Handoff.** Commit the outputs. Then, in a following commit, close this handoff `done in <sha>` and open handoff 08 to Claude for the **readiness check**: a reviewed `git diff` of the shared files, verification of final IDs and the reservation refresh. That check is not a new audit round unless the application makes a material change beyond the audited scope.

## Read first

`AGENTS.md`, `agents/WORKFLOW.md` (Work cycle step 5, the reservation procedure, and Proportionate audit and records), `agents/codex/CODEX.md`; this handoff; `audit-01.md` (A3, A10), `audit-02.md` (N7, N8) and `audit-03.md` (N2); `LOG.md`; `results/padua-mz-sharp-constants-20261106.md`; `audit-01-support/records/novelty-records-findings.md` (F1–F5 registry details); and the current shared registries on main.

## Scope limits

- Do not change any accepted statement, proof, threshold, receipt or status beyond the registry application above.
- Do not edit `audit-0*.md`, `audit-*-support/` or earlier handoff bodies.
- Do not change another topic's `RESULTS.md` section, ledger or reservation. Do not reuse, overlap or renumber IDs.
- Do not change rules, templates, workflows, settings or `.github/`. No merge, force-push, tag or write to main. Do not mark the PR ready or request merge before Claude's readiness check passes. Only AC merges.

## Acceptance and outputs

- **Outputs:**
  - reservations recorded in the ledger and the PR body;
  - every provisional ID mapped;
  - the shared registries updated as above;
  - manifest checks pass;
  - PR31 body updated with WORK/AUDIT/PR, including audits 01–03 and AC's A3 decision.
- **Done when:** exactly one open handoff (08, readiness) remains.
