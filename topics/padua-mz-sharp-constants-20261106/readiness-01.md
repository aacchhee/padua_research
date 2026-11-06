# Claude readiness-01 — padua-mz-sharp-constants-20261106 (PR31)

- **Decision: READY for AC's merge decision.** No BLOCKING or MAJOR finding.
  - Three MINOR wording, link and provenance items were fixed in place, in a separate commit (`0a7a00c`); see below.
  - This is the WORKFLOW readiness check (reviewed shared-file diff, final-ID verification and reservation refresh), not a new audit round. The application made no material change beyond the scope accepted in audits 01–03.
  - Agents never merge; only AC merges.
- **Inputs:**
  - Prepared candidate: `7322d4cb279fb91460faa031327509e1666ae1f4` (handoff 08).
  - Branch head at check: `6fdd9df4bf8986477c9d6e947c43d97efcad23ae`. Codex made this merge commit; it brings current main `64409c47a717aef074f611b31a9fd48b7a15101b` (PR32, merged by AC) into the branch without rewriting history. See [merge-reconciliation.md](merge-reconciliation.md).
- **Rules:** read at `6fdd9df` (`AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`); unchanged on the new main.
- **Reviewer:** Claude, configured `claude-opus-5-5`, high, as handoff 08 requests. One read-only helper (Opus 5.5 high, no Git authority) reviewed the shared diff; its scripts are in [readiness-01-support](readiness-01-support/). I am distinct from the Codex preparer.

## Reservation refresh (WORKFLOW steps 1–3, at readiness)

**Heads checked (2026-11-06, about 18:05–18:10 UTC):**

| Branch | Head |
|---|---|
| main | `64409c4` |
| PR27 draft (`codex/padua-argmax-bridge-20261105`) | `389dbc1` |
| PR33 draft (`codex/padua-3d-20261106`) | `d0e1bbb` |
| PR31 (this topic) | `6fdd9df` |

- **Closed PRs:** none are closed-unmerged. PR32 is merged; the NN ledger on main records that all 28 closed PRs are merged.
- **Which heads are new:** the PR27 and PR33 heads are newer than those Codex checked (`2e4ac49` and `9b81934`), and main has advanced to include PR32.
- **Scan:** every `ALLOCATIONS.md` and `ID_CROSSWALK.md` range on each head, plus the maximum used IDs in `PROOF_STATUS.md`, `state/IDEAS.md` and `literature/INDEX.md` ([reservation_scan.py](readiness-01-support/reservation_scan.py), [output](readiness-01-support/reservation_scan.out)):
  - **Other owners' maxima** stay below this topic's ranges: main/PR32 reserves PD-T502–521, PD-N181–185 and IDEA590–607; PR27 and PR33 reserve up to PD-T501, PD-N180, IDEA589 and LIT632.
  - **Used maxima:** PD-T517, PD-N183, IDEA603 and LIT630 on main, and PD-T548, IDEA611 and LIT633 on PR31.
  - **Matches:** the only range strings that match ours come from `topics/nn-mop-conditioning-20261106/ALLOCATIONS.md:36` on main. That line merely records PR31's reservation; it is not a competing allocation.
- **Priority:** this topic's reservation (PD-T522–553, IDEA-608–615, LIT-633–635, no PD-N) was first published in `dd57b6439d539164cdee7ab01a11b6080a03af10`. That is the commit that adds `ALLOCATIONS.md`, and it is pushed. **No collision.** The permanent gaps PD-T549–553, IDEA-612–615 and LIT-634–635 are unused.
- **If ledgers change:** if main or any open PR's ledger changes before AC merges, this check must be repeated (WORKFLOW step 7).

## Shared-diff review (`git diff origin/main 6fdd9df`)

**Scope.** Exactly thirteen files outside the topic differ from main:
- `PROOF_STATUS.md`, `ID_CROSSWALK.md`, `RESULTS.md`;
- `state/CURRENT.md`, `state/IDEAS.md`, `literature/INDEX.md`;
- the topic results file;
- the three target theory files;
- three predecessor dated addenda.

Every change is this topic's content. Specifically:
- **Targets, per AC's binding A3 decision (LOG, 2026-11-06):**
  - PD-T020: PROVED, with dependencies PD-T546 and PD-T523 (`PROOF_STATUS.md:42`).
  - PD-T027: PARTIAL. The uniform gap PD-T526 and the limit identification PD-T530 are PROVED; the decimal-value conjunct is OPEN (`:49`).
  - PD-T381: PARTIAL. PD-T534, PD-T535 and PD-T536 are PROVED; the decimal values are OPEN (`:432`).
  - The PD-N104 disposition and the frontier line are updated consistently.
- **Original statements and histories:** the Statement sections of all three target files are byte-identical to main, and each History records the dated decomposition. No added registry line carries process-stage text.
- **PR32 content:** all NN-related lines on main survive in the merged registries (57 PROOF_STATUS, 121 crosswalk, 37 RESULTS, 9 CURRENT, 49 IDEAS, 15 INDEX lines; none missing).
- **Other topics:** no other topic's RESULTS section changes, apart from one blank separator line.

**Final IDs.**
- **PD-T522–548:** each appears exactly once as a primary row, and links to a theory file whose header carries that ID. There are no duplicate primary PD-T, PD-N or LIT IDs.
- **IDEA-608–611 and LIT-633:** each appears once. IDEA-071/386/469/470 receive continuation rows, following the registry's existing multi-table practice.
- **Unused reservation:** no ID in 549–553, 612–615 or 634–635 is used.
- **Provisional records:** all 42 provisional records and their aliases are mapped in `ID_CROSSWALK.md` and `final-id-map.json`, including S3-kernel.

**Theory edits.**
- **Proofs unchanged:** after substituting the final IDs, no Proof or Derivation section differs between `95d0b30` and `7322d4c`.
- **What did change:** ID headers, aliases, dated metadata, and replacement of stale "audit pending" text.
- **Untouched since `95d0b30`:**
  - `code/`, `evidence/`, the `audit-0*.md` files and every `audit-*-support/` tree are unchanged.
  - In earlier handoffs, only status lines changed.
  - The new receipts (`preparation-inputs.json`, `merge-inputs.json`) are provenance only.

**Classification.**
- **Status counts:** 21 PROVED and 4 MEASURED (PD-T525, 532, 538, 543). PD-T524 is a historical CONDITIONAL prediction and is not a dependency of PD-T020. PD-T528 (S2-03) is a definition/prediction pointer.
- **PARTIAL is applied only where WORKFLOW allows it:** to explicit conjuncts of each target's own statement. Supporting results (PD-T379, PD-T547, PD-T539–542) are labelled as support.

**Topic summaries.**
- **RESULTS section:** this topic's section equals `results/padua-mz-sharp-constants-20261106.md` with link prefixes adjusted.
- **B1 qualification:** the audit-02 B1 note (P2 secants essentially postdictive) is preserved in every current numerical summary.
- **No overclaim:** P1 certifies no useful digits, and P4 is one-sided.
- **Manuscript:** the manuscript proper is untouched.

**Command:** `python topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --checks` exits 0 at `6fdd9df` and again after the fixes: 95 identities, 30 Python ASTs, 107 JSON files, 113 Markdown documents, 469 local links, 0 missing. All generated JSON is < 16 KiB.

## In-place MINOR fixes (commit `0a7a00c`, separate from this report)

- **R1.** In the `PROOF_STATUS.md` rows PD-T020, PD-T027 and PD-T381, the earlier audit links (mz-constants audit-01/02; cleanup audit-01 F11 and response-01) had been replaced. I restored them as "Earlier:" links and added sharp audit-01 to PD-T020. Status, dependencies and dispositions are unchanged.
- **R2.** Provenance lines that preparation removed are now preserved in History: the 2026-11-05 Checks paragraph of `sharp-growth-open.md`, and the 2026-10-31 "Review update" header notes in `m2-sharp-constant-open.md` and `open-upper-limit.md`.
  - In `open-upper-limit.md` I also recorded AC's documented A3 mapping of the Statement's "identify its exact limit" wording: existence plus exact identification is PROVED, and the decimal evaluation is OPEN.
  - The Statement text is unchanged.
- **R3.** `ID_CROSSWALK.md:1756`: "remains reserved to this topic" now reads as permanent unused gaps, matching `ALLOCATIONS.md`.

## NOTES (no action required)

- **N1.** The PD-T528 Status cell, "registered definition/prediction; proved via PD-T530/531", is the registry's only non-standard Status string. It is left unchanged because altering a Status cell is not a permitted auditor fix. AC may prefer the wording "definition/prediction record (no epistemic status); prediction resolved by PD-T530/531" in a later cleanup.
- **N2.** Two process sentences inside Statement sections were updated without a date: `P1-numeric-certificate.md:31` and `P4-certified-lower.md:20`, both "Required Claude audit is separate" → "Accepted…". They are not mathematical.
- **N3.** `manuscript-insert.md:83` still says the literature context is only search/abstract-screened, although LIT-633 records a full primary-text read. This is conservative, not an overclaim.

## Residual limitations

- **Numerical decimals:** the decimal values of Λ_edge and c_± remain OPEN, and are registered as such under AC's PARTIAL ruling.
- **What this check covered:** it verifies the application, the identities and the reservation union only. The science rests on audits 01–03.
