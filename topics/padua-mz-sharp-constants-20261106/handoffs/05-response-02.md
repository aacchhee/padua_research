# Handoff 05 — padua-mz-sharp-constants-20261106 — bounded response to audit-02

- Status: done in 99fd6c0e7a0d8912e087c81bfd9bbd6654ca6330
- Previous handoff: [04-focused-audit.md](04-focused-audit.md), done in d8b028649011da11c567bccfcb037ca53d2b93f9

- Next agent / model / effort: Codex coordinator, `gpt-6-astra` high. Allocate:
  - the B2 derivation record to `gpt-6.1-sol` high;
  - record edits to `gpt-6.1-sol` medium;
  - one distinct `gpt-6-astra` high supplementary check of the B2 derivation.

  Record actual models.
- Role: developer and topic orchestrator
- Branch: `codex/padua-mz-sharp-constants-20261106`
- Input head SHA: `d8b028649011da11c567bccfcb037ca53d2b93f9` (audit-02 output commit; the commit publishing this handoff comes later)
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`
- Stage: WORK (bounded response)
- Written by / date: Claude, claude-opus-5-5 (xhigh) · 2026-11-06

## Task

Read the rules at the branch head and record the SHA. Fetch main and the topic head first. Then write `response-02.md` answering every finding of [audit-02](../audit-02.md) (B1, B2, C1–C4): fixed (file and commit), rejected (with an evidence-based reason), or explicitly unresolved.

Audit-02 accepted all the mathematics and certificates at their stated scopes:
- P3 full CC limit π⁴/8 PROVED;
- P1 kernel, positivity, reduction and coarse enclosure PROVED;
- P4 Λ_edge ≥ 1.0044369 PROVED;
- P2 MEASURED.

Only records work remains:

1. **B1 (MAJOR).** Add dated scope addenda to `theory/P2-measurements.md`, `ideas/P2.md`, `ideas/P2-protocol.md`, `report.md` and the results file.
   - They must state that Q_min at m = 1400/1401, 1800/1801 and 3000/3001 was already committed at `5110954` before the protocol. The registered secant-to-b₂ criterion was therefore essentially postdictive (see `audit-02-support/P24/P2-preexisting-predictivity.json`).
   - Only the mode-2 weight, L-distance and branch-difference-rate criteria were prospective.
   - Do not change thresholds, receipts or the PASS_FINITE_TEST outcome. Remove or qualify the word "fresh" in the dated addendum, not by rewriting the original protocol text.
2. **B2 (MAJOR).** Write the derivation of the closed-form denominator entries C_ij/C_jj (∫₀^∞ t F_iF_j dt for the S2 endpoint basis) as a durable PROVED supporting theory record (`theory/P4-denominator-closed-form.md`), or as a separately statused proved section of `P4-certified-lower.md`. Use `templates/THEORY.md`.
   - Base it on the derivations in `independent-checks-S2-model.md:66-100` and `independent-checks-P4.md`. Make every case explicit: diagonal partial fractions, I(a) = −Cin(2a)/(2a²), and the Si(2a)/(2a) integral.
   - Update `theory/S2-endpoint-model.md:136-141` and `theory/P4-certified-lower.md:24,35` to cite it.
   - Get one distinct supplementary check.
   - This is material new proof text. It returns to Claude for a focused recheck of this derivation only.
3. **C1.** Generalize the `code/evidence_manifest.py` exclusion to `audit-*-support/` and regenerate the manifest intentionally, recording why. Do not edit any audit support file.
4. **C2–C4.** Make the listed history, status-label, stale-text, PD-T020-deferral wording, "no useful digits", IDEA-466 novelty and gate-link edits. Label the prose-hash fields in P1 receipts' documentation as historical in the records; do not rewrite committed receipts. Add the P2_summary prerequisite check, or document why procedure enforces it; if the check changes code, rerun the summary and preserve both receipts. Make the P3-reverse-bound wording fixes.

None of these may change a statement, quantifier, proof step, threshold, receipt or status, except adding the B2 record.

Update LOG, the results file and the PR31 WORK section.

## Read first

`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`; this handoff; `audit-02.md`; `audit-02-support/P24/` (B1 and B2 evidence); `LOG.md`; and the files named in each finding.

## Scope limits

- Do not edit `audit-01.md`, `audit-02.md` or any `audit-*-support/` file, or earlier handoff bodies.
- No change to accepted statements or proofs, registered gates and receipts, thresholds or outcomes.
- No shared registries (`PROOF_STATUS.md`, `state/`, `ID_CROSSWALK.md`, `RESULTS.md`, `literature/`), final IDs, reservations or manuscript. Leave PR preparation and the PD-T020/PD-T027/PD-T381 registry application to the later preparation step; A3 remains AC's decision.
- No new numerical campaign, upper Padua run or Syvert use. Only AC merges.

## Acceptance and outputs

- **Outputs:** `response-02.md`; the B2 theory record with its supplementary check; the record edits; and a manifest check passing with exit 0.
- **Commit order:** commit the outputs first. Then, in a following commit, set this handoff to `done in <output-commit-sha>` and add handoff 06 to Claude, asking for a focused recheck of the B2 derivation and confirmation of B1 and C1–C4 by diff.
- **Next step after Claude acceptance:** PR preparation. That covers reservations, final IDs, registry application by reviewed diff, and AC's A3 decision. PD-T020 → PROVED via P3-03 + S1-02 is to be verified at readiness.
