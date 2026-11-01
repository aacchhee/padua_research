# PR-preparation science-preservation and summary-scope review

Rules `a2dd845b8a231e1b00733e1361e2a9ad3bad222f`.
Interpretation: verify that PR #10 preparation preserves the accepted scientific files and evidence, and that the new published summaries accurately identify their statuses, operators, hypotheses and remaining obligations. This is an integration/identity review, not a new proof, experiment, literature or novelty audit.

Reviewer: continuing Codex subagent, explicitly launched as `gpt-6-astra`, xhigh; runtime model/effort metadata is not independently exposed. Accepted baseline: `cf01449fc96233c9074ce25efcb056535414aa1d`. Reviewed head: `a2dd845b8a231e1b00733e1361e2a9ad3bad222f`. Integrated-main comparator: `9739a0c56b7a3976422ce60a8441bfbbfd6554df`. Date: 2026-11-01 UTC. Only this report and `audit-04/science-impact/` were written; no developer file, Git state, local AC results file or external service was changed. Merge authority remains with AC.

## Verdict

**Scientific preservation passes. Published-summary corrections are required.** All 77 theory files differ from the accepted baseline only by one matching `Final ID:` line and its blank separator. All 574 other pre-existing topic/track files covered by the preservation check are byte-identical except the five explicitly enumerated administrative records. No producer, scientific checker, raw experiment input/output, historical review, handoff or accepted audit record changed. No unchanged mathematical suite was rerun.

The new `state/CURRENT.md:49` summary contains a false PROVED ID range, reverses the coordinate of the section theorem, and drops essential hypotheses from two scope summaries. These are integration-level summary defects; the underlying accepted theorems and statuses remain intact. The exact-representation (E) versus finite-precision Greenbaum (G) distinction, the per-degree radius qualification, and the OPEN universal reorthogonalization target are correctly preserved elsewhere in that paragraph and in PAPER_MAP.

Consolidation: the root audit groups the four corrections below as **A4-M3 (published-summary fidelity)**. The local labels distinguish their evidence; the root separately owns any corresponding PR-body wording.

## Findings

### SI-M1 — The new PROVED range includes a MEASURED result

Location: `state/CURRENT.md:49`, “Paige-type local relations, ω-recurrence and row-selection framing are PROVED (PD-T029–PD-T036 …)”.

PD-T035 is the final ID of T107, `tracks/bivariate-lanczos/theory/loss-regimes-node-propagator-measured.md:3`; its overall status at line 39 is **MEASURED**, and all six statement parts are measured. The allocation is correct; the summary's inclusive range incorrectly presents that record as proved.

Required correction: list only the intended proved IDs, for example PD-T029–PD-T034 and PD-T036, or use the more precise subset naming the local, Paige, omega and row-selection results. Do not upgrade PD-T035 or its empirical predictor/regime observations. This is medium severity because it changes a published claim's epistemic status without any changed proof or evidence.

### SI-M2 — The summary attributes the formed-section theorem to the wrong coordinate

Location: `state/CURRENT.md:49`, “the x-section is accurate … (PD-T046)”.

PD-T046 explicitly defines **F=Y as the full/formed operator and J=X as the injecting operator** in `tracks/bivariate-lanczos/theory/semi-orthogonality-implies-accurate-F-section.md:12`. Its section is `S=W_nᵀFW_{n−1}` (line 16), and its χ-explicit theorem concerns that F-section. Calling it the x-section reverses the operator assignment; no coordinate swap is stated in CURRENT.

Required correction: say “the formed F=Y section” (or “the formed section”) and retain the local/semi-orthogonality and χ qualifications. If naming the complementary residual section, call it the injected J=X section. The reversed x/y labels also occur in the **unchanged** accepted report at lines 10, 39 and 41; this review does not reopen the theorem but identifies the newly published CURRENT repetition. Any summary alignment should preserve history and leave the theorem/evidence unchanged. This is medium severity because the two section conclusions are deliberately different.

### SI-L1 — Restore the hypotheses in the new zero-radius and band-Krylov summaries

Location: `state/CURRENT.md:49`, the phrases “overdetermined nodes give δ = 0” and “the graded spaces are not a fixed-start band Krylov sequence of one commuting operator”.

- PD-T059(a), `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-303-moment-cone-rate-theorem.md:18`, requires **S₀={0}, equivalently Π_{2n+1}-determining nodes**, and gives zero radius for sufficiently small ε. Merely having more nodes than dim Π_n is insufficient; the theorem itself separates other cases in lines 19–22. State the determining condition, rather than the unqualified word “overdetermined”. The accepted report's overview contains the same shorthand, but its Rank 2 states the correct S₀ criterion.
- PD-T076, `tracks/bivariate-lanczos/theory/l4-band-krylov-obstruction.md:16`, requires **U(2m+1)** and forbids **both S_m and S_{m+1}** in a band sequence with m starts. It does not forbid every fixed-start description of every finite graded sequence on arbitrary distinct nodes. CURRENT should say “under the stated unisolvence hypotheses” or give the concise m-dependent formulation. The report's Rank 6 already supplies the condition at line 54.

These are low-severity summary qualifications, requiring no new proof or experiment. They should be corrected before this summary becomes the published current state; the exact-representation (E) and small-perturbation context must remain explicit.

## Preservation and allocation checks actually executed

The independent checker is `audit-04/science-impact/check_preservation.py`; it imports only Python standard-library modules and performs read-only Git queries. It does not call the developer's PR-preparation checker. Actual command from `/workspace/padua_research`:

```text
python3 -B -I topics/bivariate-lanczos-20261031/audit-04/science-impact/check_preservation.py > topics/bivariate-lanczos-20261031/audit-04/science-impact/preservation.json
```

Exit status: **0**. Environment: Python 3.12.14; platform and full version recorded in the JSON. The output was inspected. It records accepted/head Git blobs and SHA-256 values, and checks working bytes against the pinned reviewed head.

| Check | Result |
|---|---|
| Theory file inventory | Same 77 paths before/after; no added/deleted theory file |
| Theory bodies | 77/77 exactly equal after removing only the precise inserted Final ID line plus one blank line |
| Final IDs | 77/77 agree with the provisional header and `pr-prep/id-map.json`; scientific body/dependency/status wording untouched |
| Other frozen pre-existing topic/track files | 574 byte-identical files |
| Included code coverage | All 139 pre-existing files under `tracks/bivariate-lanczos/code/` frozen, including supplied inputs, producers and review checkers |
| Included direction coverage | 178 pre-existing direction files frozen |
| Included review coverage | 79 pre-existing review files frozen |
| Included audit coverage | 140 paths beginning with this topic's `audit-` prefix frozen, including audit-01/02/03 records and handoff |
| New files within this topic/track | Exactly 9, all under `pr-prep/`, administrative allocation/check/rehearsal records |
| Existing administrative changes excluded from scientific freeze | Topic LOG.md, progress.md, lit/search-log.md; track AUDIT_LOG.md and NEGATIVE_RESULTS.md |
| Reviewed summary Markdown link destinations | All existing; checker records each destination |

The 574-file test is broader than checking only code suffixes or known output extensions. It preserves all pre-existing topic/track files except the explicitly listed administrative records and the theory-ID insertions, thereby covering manifests, raw logs, reconstruction prose and supplied-source identities as well. The category counts are subsets of that total; remaining files include plans, reports, source metadata and other topic records.

Identity evidence hashes:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `science-impact/check_preservation.py` | 5,872 | `61d2a8f0d8ea43bb99ff39a70ec349f77b60a98e789171a4461de73e2a6c4aad` |
| `science-impact/preservation.json` | 217,270 | `12046497554a520f9e6a2f0e6645d9013aa0aad78c03687fcaf779a7a439f8c5` |

The script's check of links is a destination check, not a semantic acceptance of every surrounding sentence; the findings above come from the separate source/status comparison. Full global ID collision and registry completeness checks belong to the parallel registry review, and integration rehearsal belongs to the root reviewer.

## Published-summary and acceptance-context assessment

**CURRENT.** The new paragraph's PD-N007/011/012/013 references retain MEASURED scope. PD-T041 is correctly described as an exact finite triangle-versus-square propagator certificate. PD-T053 refers to the proved reference-free bound, while PD-T055 remains OPEN. The paragraph correctly restricts Padua backward obstruction to reading (E), says the radius is per-degree, retains the Padua-unisolvence dependency, and leaves radius dependence (PD-T075) and reading (G) (PD-T056) OPEN. Correct the three findings above without expanding those conclusions.

**PAPER_MAP, lines 25–26.** The two new entries are explicitly “brief only”. Their final IDs map to the intended accepted records. Reading (E) is named in the backward-obstruction brief; (G) and radius dependence remain OPEN. The loss/span brief retains the unverified identification with published V+A code, pending large-M work and OPEN universal obstruction. Listing PD-T055 under supporting result IDs does not assert it is proved because the gap column expressly retains the universal question as OPEN. No new manuscript, priority or experimentally validated general mechanism is credited by these entries.

**Report and track README.** Both are byte-identical to the accepted baseline. Their links resolve. The report retains the conditional computed-product transfer (T116→PD-T044) in Rank 5, the theorem/measurement split T114/T117→PD-T042/045, the stage-maximum span bound, and the (E)/(G) and per-degree-radius distinctions. Their older publication metadata remains stale: `report.md:3` says re-audit pending, `report.md:42` says T209 needs re-audit, and `tracks/bivariate-lanczos/README.md:3,15` says Codex audit pending/final IDs still forthcoming. These lines were not introduced by preparation and do not falsely grant acceptance; the new audit log provides the later acceptance record. They are advisory metadata reconciliation items, not grounds to rerun accepted science. This focused review does not reapprove every unchanged overview shorthand.

**AUDIT_LOG, lines 11–15.** The new entries preserve audit-01's changes-required verdict, audit-02's four qualifications and audit-03's **CLEAN within scope; proceed to PR preparation** result. They do not say integration review or merge approval has already occurred. Historical Claude reconstructions stay labelled supplementary; provisional IDs in old audit rows are expressly historical and linked to the final crosswalk. The actual audit-03 record and independent verification were read and retain the distinction between a narrow correction review and general scientific acceptance.

**OPEN/CONDITIONAL preservation.** Byte equality preserves PD-T044 CONDITIONAL, PD-T055/056/072/075 OPEN and their dependencies without any status upgrade. The unchanged T209/PD-T054 theory still has an old “requires independent audit” suffix, while audit-02's accepted record supplies that later audit; this review does not invent a fresh checker execution to reconcile historical text.

## Rules, scope exception and limits

Read at the reviewed head: AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md. AGENTS and CODEX are unchanged from the accepted baseline. WORKFLOW differs only by main's new local working-track paragraph; all three are byte-identical to the pinned main comparator. This subagent made no local working-track write.

Read the accepted audit-03 and its independent verification, current CURRENT/PAPER_MAP/report/track README/AUDIT_LOG, the relevant mapped theorem/status statements, the developer's rehearsal record for context, and the scoped accepted-to-head/main-to-head diffs. Oversized broad diff output was not treated as complete inspection: the independent tree/byte checker establishes the full scientific-file inventory, and relevant summary diffs were read separately.

No new mechanism, negative mathematical result, separation criterion, priority assertion or literature claim is evaluated here. Accordingly this identity/status-integration scope uses the explicit protocol-only exception to a new full IDEAS/INDEX read. Those catalogs are being integrated and reviewed separately; earlier full reads are not misrepresented as byte-identical current reads. This review verifies preservation and faithful summarization of already accepted statements, not their proofs anew.

No experiment, exact certificate producer or historical scientific checker was rerun. No independent integration merge/rehearsal was performed by this subagent. Root owns rehearsal, remote PR metadata and readiness; other assigned auditors own global registries and literature consolidation. The clean byte-preservation result does not extend any numerical scope, resolve any OPEN/CONDITIONAL target, certify novelty or authorize merging.

Suggested next prompt: `Claude Opus 5.5 xhigh: correct audit-04 SI-M1, SI-M2 and SI-L1 in the new CURRENT summary, preserve the accepted scientific bodies and evidence, and return the summary-only diff for Codex gpt-6-astra xhigh review before AC decides on merging PR #10.`
