# Response 01: developer answers to audit-01

- **Developer.** Claude, assigned by AC's redirection on 2026-11-01 at 16:13 CET (handoff 04, then the correction recorded in handoff 05). The orchestrator ran on the configured `claude-opus-5-5`. The developer subagents were:
  - E3/E4: Opus 5.5 xhigh;
  - E5: Opus 5.5 high;
  - E1: Sonnet 5.5 high;
  - E6: Sonnet 5.5 high.
- **Independence.** Claude was also audit-01's auditor. These fixes are therefore Claude development and **are not independent acceptance**. A Codex re-audit (`gpt-6-astra` xhigh) is required. audit-01.md and `checks/audit-01/` are unchanged.
- **Audited candidate.** `36c93794ce02f92c76c89e5a9ec8095eb238d91d`.
- **Response commits:**

  | Commit | Content |
  |---|---|
  | `e53c10d` | E6 |
  | `1d7a922` | E5 |
  | `0b5ec28` | E1 |
  | `fc30ede` | shared text and the integration checker |
  | `30fba24` | E3/E4 and the remaining shared text |
  | `0f819a3` | PR14 merge, integration only |

  The re-audit candidate SHA is in handoff 06.
- **Developer reports.** These give exact line ranges, commands and proposed texts: [checks/response-01/](checks/response-01/).

## Dispositions

FIXED means changed in the files listed in the developer report. "Proposal" means literal OLD/NEW text in `proposed-record-changes.md`, applied at preparation. **M** marks a material scientific change that the re-audit must judge.

| Finding | Disposition | Where / note |
|---|---|---|
| E34-F1 (medium) | FIXED **M** | Record 15 is rewritten as a **general fixed-degree lemma, PROVED**. The setting is any positive measure with U(t+1) and M > N_(t+1), any admissible selection, and one raw-product source with f_⊥ ≠ 0. Every projection-only rule gives the same span, θ in closed form, and δ_A = κ_Aθ, with κ_(A_m) ≥ b. T₃/BJ is kept as the instance: (8) is now an equality, and δ_Y(1) = (√3/2)δ_X(1) is added. The "unformed J-product" reading is removed; its wording is kept in History. A new exact checker `e4_closure_check.py` passes on 28 instances, which corroborates but does not prove the every-rule claim. |
| E34-F2 (medium) | FIXED | PD-T055's heuristic span identity is credited in record 15, IDEA-15, E4.md and report.md. The IDEA-15 verdict is now "variant: exact fixed-prefix instance". |
| E34-F3 (medium) | FIXED **M** | Record 14 becomes **IDEA?drift-codex-14, REJECTED: refuted (ill-posed formalization)**; there is no PD-N, and PD-T032 part 2 is cited. Its full content moves to ideas-e3-e4.md, and U(3) is proved inside record 15. The record-14 file carries a withdrawal banner and is removed at preparation. One fewer PD-N final ID is needed. |
| E34-F4 (medium) | FIXED **M** (scope) | Record 11's remainder now depends on the particular family, with the example f = td + t²Gg. No uniform remainder is asserted, and compact-family uniformity is stated precisely. |
| E34-F5 | FIXED | Record 11 now says the staircase restriction is unused in (6) and excludes the pivot rule. The separate file is kept, with reasons. |
| E34-F6, F7 | FIXED | Stale check text now cites independent-math-01 and audit-01. The SymPy scratch is marked as non-evidence. The E3.md wording is corrected. |
| E34-F8 | FIXED (proposal) | The E3 polynomial-safety target goes to PD-T054's open item, with an IDEA-151 note at preparation. |
| E34-F9 | FIXED | New deferred **IDEA?drift-claude-17**: parent-repair and reference-basis rules, including PD-T055's extended-precision parent experiment. |
| E34-F10 | FIXED | The report, local-results-entry, plan and PD-T055 proposal text are updated, including record 14's new disposition. |
| E5-F1 (medium) | FIXED **M** (scope) | Record 32's case 3 now rejects only the eventual-witness mechanism. A new Remark covers finite-n negative points on fixed-A paths: η_{n₀}(a/n₀) = ζ_{n₀} is rigorous, and the windows are MEASURED. Item 3's theorem is unchanged. |
| E5-F2, F3, F4 | FIXED | Stale reconstruction text is corrected. The exact coverage of `e5_exact_checks.py` is stated. ζ_n ∈ (−1,1)² for all n ≥ 4, so the theorem also holds for the square-restricted radius. |
| E5-F5, F6 | FIXED (proposal / report) | Literal blocks are added for PD-T075 (title, Split into, Open item (2), History), for PD-T069:66 and its History, and optionally for PD-T061. The report paragraph on PD-N?drift-codex-32 is added. |
| E5-F7, P-F7 (E5) | FIXED | IDEA-31 now names PD-T061/IDEA-157 and PD-N021/IDEA-161 as predecessors. It is split into the (E) instance and a new deferred **IDEA?drift-codex-35** for (G). |
| E5-F8 (optional) | FIXED **M** | A new Remark in record 30, labelled a PROVED minor routine corollary: limsup n⁵ρ_n ≤ 2√2π⁴(10−2√2)/9 ≈ 219.54. It comes from the general-a limit a²(81a² − 360π³a + 368π⁶)/18, and is checked by `response01_e5_checks.py` (PASS). The main Statement is unchanged. Whether this should be a split is the re-audit's call. |
| E1-F1 (medium) | FIXED | New `e1_response_checks.py`, which imports the producer and so is not independent, with evidence `response-01-e1-checks.json` (PASS). The rotQ24 (2,1) tie is disclosed with its 90° symmetry cause: breaking it toward Y changes KHS² by +12.4% and Urow² by +3.8%. The rotQ24 pivot rows are labelled X-tie-broken. T24 has no tie (margin 0.008426). The producer is unchanged to preserve evidence hashes; tie detection lives in the checker. |
| E1-F4 (medium) | FIXED | The freeze chronology is reconciled with e1-freeze.json's own notes. The record discloses that 6920ba6 already contains Urow and that `dead` was edited in place. The sharpened-U DEAD rule would fire at T24 degrees 2–4 and rotQ24 degrees 2–6; the original rule never fires. "Preregistered" becomes "frozen". |
| E1-F2, F3 | FIXED | The trace check is relabelled a consistency identity. Exact BᵀB = D at degree 12 passes, and record 04's six inequalities and the factor-100 criterion now have a committed checker. |
| E1-F5, P-F8 | FIXED (status unchanged) | Record 05 **stays MEASURED**, with the rationale stated: its frozen factor-10 target is INCONCLUSIVE, and the >7/>800 thresholds were chosen post hoc. A separate finite PROVED record for the exact inequalities is possible but is not created; this is flagged for AC and the re-audit. Stale "pending" lines are reconciled. |
| E1-F6 | FIXED | The README and record 05 list the `e1_cgs2.py` comparator commands, and note that `input_sha256` is not reproducible. |
| E1-F7, P-F7 (E1), P-F6, P-F3 | FIXED | Predecessors added: IDEA-087/088, LIT-114, LIT-255, PD-T042/IDEA-141, PD-T043/IDEA-142–144 and IDEA-139, each with a separation. "Relaxed" is dropped from ideas-e1 and ideas-e5. |
| E1-F8, F9 | FIXED | Record 03's title and alias wording, and "for s ≤ n" in record 01. |
| E6-F1 (medium) | FIXED | New `e6_offsample.py` with evidence `response-01-e6-offsample.json`. The midpoint control is equal to the committed values. On 4000 uniform points the adversarial error is about 15 times larger: 1.49e-2 on rotpi4 and 2.45e-2 on the triangle, dominated by the vertices. Boundary-inclusive samples and a generic entire target are added. The test distribution is stated, and the report table is relabelled. |
| E6-F2, F3, F4 | FIXED | The training residual equals the gap by construction. The Gram error is the (0,0) entry, with an off-diagonal maximum ≤ 2.8e-16. exp(x+y) is a ridge function, and its selection chronology is undocumented. |
| E6-F5 | FIXED | ideas-e6 uses the template, with **IDEA?drift-codex-55…59** and an old-to-new label map. The disposition words are corrected. |
| E6-F6, F7, P-F7 (E6) | FIXED | The numpy < 2.5 requirement and PYTHONPATH are documented, the coverage text is updated, and IDEA-086 and IDEA-116 are added. The degree-16 grids are still not independently rerun. |
| P-F1 (medium) | **UNRESOLVED (for AC/Codex)** | Claude cannot reach Codex's workspace, so the scientific ZIP (`27476b62…`), the 3.6 MB raw capacity file, root-independent-e6.json and the 46 `/workspace/padua-drift-runs` files can only be delivered by Codex, or regenerated. Until then, verification rests on committed compact evidence plus regeneration. audit-01 executed that regeneration: `e1_reproduce` PASS for both sets, exact degree-12 reruns equal, E5 and E6 identical. The audit-01 outputs are in AC's cold storage (`audit-01/`, readback verified). |
| P-F2 | FIXED (disclosure) | `final-validation.json` is an immutable receipt. The two reservation-only registry edits are recorded here and in LOG: the `ID_CROSSWALK.md` reservation section and the batch `ALLOCATIONS.md` section. The integration receipt lists them explicitly. |
| P-F4 | FIXED | LOG now links handoffs 02–06. |
| P-F5 | FIXED | A fresh ref-level recheck after PR14's merge, against main `e0d9e3d`, PR12 `3062f77` and PR16 `f628a1f`: no final assignment of any reserved ID anywhere. See `evidence/response-01-integration-20261101.json`. The full union scan is repeated at preparation. |

## Immutable files with stale content (annotated, not rewritten)

- `evidence/e1-summary.md`, `e1-scalar-manifest.json`, `e5-manifest.json`, `final-validation.json`, `protocol-check.json`, `independent-math-01.json` and `independent-scalar-01.json` are frozen snapshots.
- Handoffs 01–02 and LOG:52 still describe record 14 as a PD-N and give the earlier statuses and pins.
- The record hashes pinned in independent-math-01 and e5-manifest apply to pre-response content.

## Material changes for the Codex re-audit

1. **Record 15.** Check the generalized lemma: hypotheses U(t+1) and M > N_(t+1), the proof of (a)–(d), κ_(A_m) ≥ b, and the U(3) proof moved in from record 14. Also check that the sampled-rule checker is not presented as a proof.
2. **Record 14.** Its conversion to an IDEA disposition, and the removal of the file at preparation.
3. **Record 11.** The family-dependent remainder and the compact-family uniformity statement.
4. **Record 32.** The case-3 scope and the new Remark.
5. **Record 30.** The general-a Remark (PROVED minor corollary, ≈ 219.54), its classification versus a split, and the square-restricted extension.
6. **Record 50.** The new off-sample measurements and the changed wording, including the generic target chosen before running.
7. **Records 04 and 05.** The tie disclosure, the freeze-provenance rewording, and the decision to keep record 05 MEASURED.
8. **New IDEA entries.** IDEA?drift-codex-35, IDEA?drift-codex-55…59 and IDEA?drift-claude-17.
9. **New checkers and evidence.** `e1_response_checks.py`, `e4_closure_check.py`, `response01_e5_checks.py`, `e6_offsample.py` and `integration_check.py`, with their JSON outputs.
10. **PR14 merge `0f819a3`.** Its conflict resolution, verified by `integration_check.py` (PASS: squash tree equals head tree; protected paths and the 77 old theory files unchanged).
