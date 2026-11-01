# Audit 01: padua-lanczos-drift-20261101

- **Auditor.** Claude, independent auditor and audit orchestrator. The configured model is `claude-opus-5-5` at xhigh effort, as requested in handoff 02; the runtime does not expose the serving variant. The auditor is a different agent from the developer (Codex).
- **Reviewer subagents.** Each part was reviewed by a Claude Opus 5.5 subagent, run read-only on Git:
  - E1: xhigh;
  - E3/E4: xhigh;
  - E5: xhigh;
  - E6, the full IDEAS.md read, novelty and protocol: high.

  Why these depths: the E1–E5 parts are mathematical or adversarial audit (WORKFLOW requires Opus xhigh). E6 and protocol are measurement, technical and protocol audit (Opus high). The orchestrator wrote this record and spot-checked material findings itself.
- **Rules.** `AGENTS.md`, `agents/WORKFLOW.md` and `agents/claude/CLAUDE_ROLES.md` were read at the branch head `36c93794ce02f92c76c89e5a9ec8095eb238d91d`.
- **Candidate.**
  - Branch `codex/padua-lanczos-drift-20261101`. Audited head `36c93794ce02f92c76c89e5a9ec8095eb238d91d`, which equals input head `664ae23` plus handoff 02 only.
  - Scientific source `b09e1dbe0baafd666cf0d779a671a40f55de2d75`. `git diff b09e1db HEAD -- tracks` is empty. After b09e1db only topic metadata changed (archive receipt, LOG, plan, report, COLD_STORAGE, handoffs).
  - Main/base `806cc7b4509fd93bae652f9545d32d95529f8281`. Draft PR #15.
- **Pinned content.**

  | Content | Hash |
  |---|---|
  | Git tree `tracks/bivariate-lanczos/code/drift` | `59633ab623f14db072afc54997b88e8775425caf` |
  | Git tree `topics/padua-lanczos-drift-20261101/evidence` | `0bd2e017c72933517f2dff78ad85af1c93ecf07a` |
  | Git tree, topic directory | `e98f428f2b26804525d4b9f21d251fcf40969114` |
  | Git tree, theory directory | `ba9dbaeace5875127e99d892b2cf0c6ebea5bd03` |
  | `state/IDEAS.md` sha256 (identical on main) | `de45820ecb33f8694b0ed4a13177fc2d91094729dc2f164e3d26034fada4d4a0` |

  The record sha256s are in the disposition table below.
- **Date.** 2026-11-01. Detailed reviewer reports, with every location and command, are in [checks/audit-01/](checks/audit-01/). They form part of this audit record.

## Verdict

**CHANGES REQUIRED. No claimed PROVED or MEASURED statement is refuted.** All thirteen records were reconstructed independently, and every decisive number was reproduced by audit executions.

The result is 0 high findings, 10 medium and 32 low. The medium findings concern scope, title, attribution, quantifier, disclosure and registry-vehicle defects that must be answered in `response-01.md` before PR preparation. Stage returns to **WORK**.

Material rescoping of records 15 and 14 (E34-F1/F3), of record 32 (E5-F1), and of any record-05 status change (E1-F5) needs re-audit. Purely editorial responses may proceed with a documented resolution.

## Read coverage

- **Rules and handoffs:** rules, handoffs 01–02, LOG, plan, report, directions E1–E6, ideas-e1, ideas-e3-e4, ideas-e5, ideas-e6, proposed-record-changes, independent-checks, local-results-entry, COLD_STORAGE, external-code, checks/independent-math-01, all topic evidence JSON (structure and decisive fields), the e1-summary, and the manifests.
- **Validation receipts:** final-validation, protocol-check, and the two allocation scans.
- **Novelty:** the **complete `state/IDEAS.md`** (736 lines, sha above) was read in full by the E6/protocol reviewer. Mechanism-specific greps and full entries were read by the other three reviewers.
- **Theory:** all 13 new theory records and all new code.
- **Predecessors:** PD-T032, 041, 042, 043, 046, 047, 050, 051, 053, 054, 055, 056, 058–061, 069 and 075; PD-N013, 015, 020, 021 and 022.
- **Old campaign:** its records; `literature/INDEX.md` and the L2 prior-art review, in relevant parts.
- **External code:** polyrat source at the pin.
- **Not read:** source fulltexts (Hokanson, ZN, BNT). Literature statements stay at their recorded digest/UNVERIFIED level.

## Executions actually performed by this audit

Environment: Linux; Python 3.13.18, not the recorded 3.12.14; python-flint 0.9.0, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0 and mpmath 1.3.0, installed into `/workspace/padua-drift-runs/python-deps`; `OPENBLAS_NUM_THREADS=1`. polyrat was cloned fresh at `6903d7af9995c9d88e661fb229626696e00fdfba`, with backports.cached-property 1.0.2.

**Orchestrator reruns of the handoff commands.** The script is [scripts/orchestrator_run_all.sh](checks/audit-01/scripts/orchestrator_run_all.sh). The output hashes are in [manifest.json](checks/audit-01/manifest.json).

| Command | Result |
|---|---|
| `e1_check.py` on e1-full-sweep.json | 88 records. Original frozen verdict INCONCLUSIVE. Interval and projector checks PASS. Byte-identical to committed e1-exact-check.json. The first attempt failed only because this host lacks `/usr/bin/time`, and the rerun succeeded. |
| `e1_exact.py`, degree 12, all sources: T24 bj, T24 pivot, rotQ24 bj, rotQ24 alt | Knode², KHS², Urow² and upper² are exactly equal, as rationals, to the committed sweep records ([orchestrator_cmp_e1.py](checks/audit-01/scripts/orchestrator_cmp_e1.py)). The T24 squared ratio of 1269287.03 exceeds 1126². rotQ24 Urow ratio² = 137.365 > 11.72² > 100. KHS-only ratio² = 62.164 < 100. |
| `e1_verify.py` | PASS, with the same checks as the committed derivative verification. |
| `e1_reproduce.py --set rotated` / `--set triangle` | PASS / PASS. Capacities and signs regenerated without the 3.6 MB raw artifact. |
| `e5_exact_checks.py` | PASS. Identical to committed e5-exact-checks.json except the `python` field. |
| `e6_benchmark.py`: `--sets rotpi4 triangle`, the full suite, `--sets T24 Q24 --grid-degree 12`; `e6_smooth.py` | All match committed evidence case by case. Gaps are 0.004105469352 (rotpi4, n = 24, upstream `[y,x]` = dev) and 0.010163571396 (triangle, n = 20). |

**Independent reviewer executions** (their own code, not importing producers except where labelled comparison):
- **E1.**
  - An implementation-independent exact/arb recomputation of all 88 aggregate cases. This used an exact Gram LDLᵀ basis, a per-node Λ⁻¹ response and exact BᵀB = D at degree 12.
  - First-principles dual-number derivatives on small generic sets.
  - A **full normalized-trajectory replay** of the record-03 scalar CGS2 graph at degrees 3 and 4. It formalizes 5454 scalar operations per case and agrees to 1e-80.
  - An independent record-05 bound and sign recomputation, covering all 625 rotQ24 greedy signs.
  - A pivot-tie detector and a DEAD-quantifier history check.
- **E3/E4.**
  - An exact-rational reconstruction of record 15's ten-node example: span equality over sampled rules, (7)–(9), and δ_Y with controls.
  - The record-14 zero-error case.
  - E3 checks: an exact surrogate triangularity check and the node-row identity, plus float64 corroboration of (2) and (3) and the staircase K_R/χ_R.
  - The campaign's `check_e4`.
- **E5.**
  - Exact series confirming both limits, −6400π¹²/729 and 20√2π⁴/9.
  - A 130-digit sweep to n = 10⁵. The nearest node is always (1,1).
  - An Arb certificate that P_n(ζ_n) < 0 for 4 ≤ n ≤ 300. This is an extra finite check, not a claim.
  - Rebuilding record 31's matrices from the four atoms.
  - Failed-path checks and a fixed-A finite-window scan.
- **E6.**
  - Hash checks on the polyrat checkout, plus re-implementations of both orderings that match polyrat exactly.
  - An independent long-double reference span. It reproduces both gaps to ≤ 2e-15.
  - Uniform-interior off-sample tests and non-ridge smooth targets.
  - A numpy ≥ 2.5 compatibility probe.
  - Hashes of every in-repo manifest entry.
  - A diff check against main.

**Spot-checks by the orchestrator:** the E4 exact script was rerun (δ_X² = 672/3295 and δ_Y² = 504/3295 reproduced), and the reviewer's general-a limit formula reproduces the claimed limit at a = 20π³/9.

**Untested:**
- no independent rerun of the degree-16 grids;
- no degree-12 scalar trajectory replay;
- no actual IEEE realization testing (none is claimed);
- the off-repo ZIP, the raw capacity artifact, root-independent-e6.json and 46 manifested `/workspace/padua-drift-runs` files are not present in this workspace (P-F1).

## Claimed-status dispositions

| Record | sha256 (prefix) | Claimed | Disposition |
|---|---|---|---|
| PD-T?drift-codex-01 span derivative | 757cf4ba | PROVED | CONFIRMED (editorial E1-F9) |
| PD-T?drift-codex-02 rational span bounds | 4651684a | PROVED | CONFIRMED |
| PD-T?drift-codex-03 scalar-operation bridge | 38a58ef2 | PROVED (formal model) | CONFIRMED. The full trajectory replay now exists at degrees 3–4. Wording E1-F8; predecessors P-F6 |
| PD-T?drift-codex-04 finite aggregate separation | 622e76b5 | PROVED, computer-assisted | CONFIRMED-WITH-CORRECTIONS (E1-F1, F4 medium; F2, F3 low). The decisive inequalities hold exactly |
| PD-T?drift-codex-05 scalar CGS2 capacities | a2ea9a62 | MEASURED; factor10 INCONCLUSIVE | CONFIRMED-WITH-CORRECTIONS (E1-F5, F6). The labels are correct. The status rationale must be stated |
| PD-T?drift-codex-10 polynomial span certificate | 611d40f1 | PROVED | CONFIRMED (E3.md editorial E34-F7) |
| PD-T?drift-codex-11 selection criterion | 30c30050 | PROVED fixed-degree; safety OPEN | CONFIRMED-WITH-CORRECTIONS (E34-F4, F5) |
| PD-N?drift-codex-14 noiseless quantifier refutation | 5f58acc4 | PD-N, PROVED | Mathematics CONFIRMED. **PD-N vehicle not endorsed** (E34-F3) |
| PD-N?drift-codex-15 projection-only closure obstruction | 2b3f5c74 | PD-N, PROVED | CONFIRMED-WITH-CORRECTIONS. Title, scope and attribution need changes (E34-F1, F2). (8) holds with equality |
| PD-T?drift-codex-30 Padua radius O(n⁻⁵) | 54f90362 | PROVED, named certificate | CONFIRMED (editorial E5-F4, F8) |
| PD-T?drift-codex-31 √ε square family | 50ddbc5d | PROVED, not reading (G) | CONFIRMED |
| PD-N?drift-codex-32 failed witness paths | 12e8cbfb | PD-N, PROVED | CONFIRMED-WITH-CORRECTIONS (E5-F1, F2) |
| PD-T?drift-codex-50 public V+A drift | 0c82b965 | MEASURED | CONFIRMED-WITH-CORRECTIONS (E6-F1–F7) |

The handoff states that the report claims neither an all-degree exponential/matching theorem, actual IEEE activation, general staircase safety, the original PD-T055, a uniform optimal Padua radius, nor reading (G). The audit confirms all six disclaimers hold throughout report.md, local-results-entry.md and the records.

## Findings, severity-ranked

Full evidence and exact file:line locations are in the four reviewer reports in `checks/audit-01/`. Codex must answer every item in `response-01.md`.

### Medium

1. **E34-F1. Record 15's obstruction is generic, not a "missing J-product" phenomenon.**
   - The source sits in the formed product v₂₁ = Yq_x. The formed operator Y carries a defect of the same order, δ_Y = (√3/2)δ_J; exactly, δ_X² = 672/3295 and δ_Y² = 504/3295 at η = 1.
   - Product grid Q₃ and the mirror selection give the same kind of defect.
   - Neither non-product support nor formed/unformed status enters the proof.
   - The fix: retitle and rescope it as a generic fixed-degree lemma, with T₃/BJ as the instance. State δ_F and the equality in (8). Remove the "never formed" interpretation from record 15, E4.md, IDEA-15, report.md and the PD-T055 proposal.
2. **E34-F2. Record 15's every-rule span identity is uncredited.** It is PD-T055's own recorded heuristic (bj-universal-…-open.md:49). Credit it, and redo the IDEA-15 novelty verdict (likely: variant, an exact instance of the heuristic).
3. **E34-F3. Record 14 is the wrong registry vehicle.**
   - It refutes a developer-introduced reading in one line from admissible zero error.
   - Its "attempted mechanism" text describes something the proof does not engage.
   - It omits PD-T032 part 2.
   - Recommended: convert it to an IDEA disposition (REJECTED: ill-posed formalization), with the PD-T055 note. Otherwise retitle it as a quantifier clarification and fix lines 43 and 48.
   - Record 15 depends on record 14 for U(3): move that lemma into record 15, or cite unisolvence.
4. **E34-F4. Record 11's O(t²) remainder also depends on the particular perturbation family.** For example, f(t) = t·d + t²G·g. Add this, and state that no uniform remainder is asserted. Mirror the change in E3.md.
5. **E1-F1. rotQ24 has an exact pivot tie at column (2,1) at every degree.**
   - The tie is caused by the grid's 90° symmetry. It is undetected by `e1_exact.py:77-78` and undisclosed.
   - Breaking the tie the other way changes the pivot KHS² by +12% and Urow² by +3.8%.
   - No decisive claim changes: rotQ24 uses alt, and T24 pivot has no tie (minimum margin 0.0084).
   - Required: detect and record ties; disclose this one; label the rotQ24 pivot rows as X-tie-broken frozen values.
6. **E5-F1. Record 32's title, preamble (:1, :14) and attempted mechanism (:54) say more than item 3 proves.**
   - Only eventual positivity along fixed-A/n³ paths is proved.
   - Fixed-A paths do contain finite-n negative points: η_{n₀}(a/n₀) = ζ_{n₀}, and numerically A = 1 is negative for n ∈ [44, 92].
   - Reword so that case 3 rejects only the eventual-witness mechanism, and add the remark above.
7. **E6-F1. Off-sample test points are midpoints of two uniform samples, so they cluster at the centre.**
   - On uniform interior points the errors are larger: triangle adversarial 7.45e-3 (reported 1.57e-3), and rotpi4 exp(x+y) 3.6e-14 (reported ≈ 2e-15).
   - The qualitative conclusion stands.
   - State the test distribution, or add a uniform or boundary-inclusive test set.
8. **P-F6. Record e1-03 and IDEA?drift-codex-04 omit the closest coefficient-error mechanisms.** These are PD-T042/IDEA-141 (the first-order coefficient-map derivative) and PD-T043/IDEA-142–144 (dot-product rounding through that map), plus IDEA-139. Add them with a separation (span-normal quotient versus Gram defect; formal l∞ graph versus Gaussian/dot64 models).
9. **P-F1. Off-repo artifacts are unverifiable from the audit workspace.** This covers the scientific ZIP (handoff 02 sha `27476b62…`), the 3.6 MB raw capacity file, root-independent-e6.json and 46 manifested run files. Before readiness, either deliver them with a readback receipt, or state explicitly that verification rests on committed compact evidence plus regeneration, which this audit did execute. The archive identity stays unverified by this audit.

10. **E1-F4. The freeze provenance is overstated.**
   - The earliest committed freeze (6920ba6) already contains the Urow certificate while marked `frozen_before_run`; no KHS-only pre-run snapshot is committed.
   - E1.md:53/67 and record02:90 ("before receiving results") conflict with the freeze's own notes ("after initial n2 restricted-source run"; "after full T24 final and standalone rotated alt were known").
   - The `dead` field was edited in place.
   - Required: per-field frozen flags, reconciled wording, and disclosure that the sharpened-U DEAD rule would fire at low degrees (T24 2–4, rotQ24 2–6).
   - Exact check: the original any-degree KHS DEAD rule never fires, so the original test and every claim are unaffected. It is ranked medium because it misstates what was pre-registered.

### Low

- **E1-F2.** The "projector trace" check is a tautology whenever d_k = ‖b_k‖². Replace it with an exact BᵀB = D check, or relabel it.
- **E1-F3.** Record 04's six stated inequalities have no committed checker; the audit verified them from the rationals. Commit a checker and its output. The rotQ24 margin U_alt² < 6.42e8 is exact but only 0.02% from the threshold.
- **E1-F5.** Stale "pending independent reproduction" text appears in record05 (:67, :77, :85), E2.md (:9, :13), ideas-e1.md (:95–96), plan.md (:20) and the scalar manifest. Also P-F8. Either state why MEASURED is retained, or propose a finite computer-assisted PROVED for the exact inequalities, keeping factor10 INCONCLUSIVE and the post-hoc labels. Either choice needs re-audit if the status changes.
- **E1-F6.** The regeneration path omits the `e1_cgs2.py` comparator-upper commands, and the `input_sha256` in `e1_reproduce`'s output hashes a temporary file, so it is not reproducible.
- **E1-F7 / P-F7.** Shortlist omissions:
  - IDEA-087/088 (Fischer-type conditioning);
  - LIT-114 and LIT-255 (Krylov subspace/Hessenberg sensitivity);
  - PD-T061 and PD-N021/IDEA-161 for IDEA-31;
  - IDEA-086 and IDEA-116 for E6.
- **E1-F8 / E1-F9.** Record 03's alias reads as an IEEE/causal claim. Record 01 should state "for s ≤ n".
- **E34-F5.** Record 11's staircase restriction is unused in the proof of (6) and excludes the pivot rule. Consider making it a corollary of record 10. "Settles the computable-criterion subproblem" overstates.
- **E34-F6.** Stale integration and independence text: record 15:64, record 11:54, ideas-e3-e4:91. The untracked SymPy calculation should be marked non-evidence.
- **E34-F7.** E3.md:14: (2) needs only full rank and σ_min, not near-orthogonality.
- **E34-F8.** The E3 polynomial-safety target has no durable OPEN record. Map it to an existing item at preparation.
- **E34-F9.** Parent-repair/reference-basis rules, including PD-T055's suggested experiment, are not retained as a deferred candidate.
- **E34-F10.** local-results-entry omits record 14, and the PD-T055 proposal text inherits F1's wording.
- **E5-F2.** Record 32 (:42, :132, :140), E5.md:53 and the e5 manifest still say reconstruction is pending, but independent-math-01 Supplement 01 performed it.
- **E5-F3.** `e5_exact_checks.py` covers less than records 30 and 31 state (the leading-term identity, node reduction, and matrices typed in rather than built from the atoms). State the exact coverage.
- **E5-F4.** ζ_n lies in (−1,1)² for every n, not only for large n (record30:40).
- **E5-F5.** Proposed changes lack literal blocks for PD-T075's "Split into", its Open item (2) and History, and for PD-T069:66.
- **E5-F6.** report.md never names PD-N?drift-codex-32.
- **E5-F7.** IDEA?drift-codex-31's closest predecessor should be PD-T061/IDEA-157. Its (E) and (G) dispositions are mixed in one entry.
- **E5-F8.** Optional: the same construction gives limsup n⁵ρ_n ≤ 2√2π⁴(10−2√2)/9 ≈ 219.5, from the general limit a²(81a² − 360π³a + 368π⁶)/18.
- **E6-F2.** The adversarial training residual equals the gap by construction.
- **E6-F3.** The Gram-error metric is the (0,0) normalization entry; the off-diagonal is ≤ 2.8e-16.
- **E6-F4.** exp(x+y) is a ridge function aligned with the rotpi4 frame, and its selection chronology is undocumented. Generic targets confirm the conclusion.
- **E6-F5.** ideas-e6 entries are not in template or provisional-ID form, and their disposition words are missing or wrong.
- **E6-F6.** Pinned polyrat fails under numpy ≥ 2.5, and the handoff's representative E6 command omits PYTHONPATH.
- **E6-F7.** Independent-coverage text is stale. The degree-16 grids are still not independently rerun.
- **P-F2.** final-validation.json lists no registry changes, but `ID_CROSSWALK.md` gains a reservation-link section and the shared ledger changes. Both are permitted, but they should be listed.
- **P-F3.** The "AC relaxed novelty gate" (ideas-e1:3, ideas-e5:8) has no recorded AC instruction. The executed gate meets the WORKFLOW minimum.
- **P-F4.** LOG has no one-line link to handoff 02.
- **P-F5.** The allocation scan used an orchestrator-supplied PR inventory with superseded heads. A ref-level recheck found no collision. Refresh at preparation.

### Checked without finding

These checks found no defect:
- normal-quotient versus raw inverse entry; gauge and source scaling;
- spectral versus Frobenius output; all-source versus restricted bounds;
- the fixed-data remainder; separation of aggregate Hilbert and scalar l∞ inputs;
- float-free decisive comparisons;
- no PD-N for inconclusive outcomes;
- the U1/U2 logic everywhere (ρ ≤ δ_obs cannot refute U2);
- record 31's moments, constants, norm and γ < 1/3 argument;
- the polyrat pin, file hashes and unchanged imports; `[y,x]` = dev including order, `[x,y]` = mirror with reversed order;
- reference conditioning and rank exclusions; no BNT/ZN substitution;
- file limits (no file over 1 MB; evidence ≈ 2.0 MB; branch additions 2.7 MB);
- the 77 old theory files unchanged; no `.github/`, `state/`, PROOF_STATUS or literature changes; nothing third-party vendored;
- reserved ranges collision-free against PR12 and PR14 refs;
- commit trailers present;
- the handoff-01 body unchanged in history.

## Corrections to the audit brief

The orchestrator's brief to the E3/E4 reviewer mislabelled PD-T058–060 as the (C)/(W) staircase records. They are moment-cone/backward results; the staircase predecessors are PD-T050/054, which the reviewer read. This is an audit-side error, not a campaign finding.

## Remaining uncertainty

- **Trusted software.** The audit trusts CPython, python-flint (fmpq, arb), SymPy, mpmath, NumPy 2.3.5 and single-threaded OpenBLAS.
- **rotQ24 checks.** These rely on arb ball soundness at 512 bits, with balls about 1e-147 wide around the committed rationals.
- **Independence.** The independent code was written by one auditor per part, in one session.
- **Record-15 span claim.** It rests on the analytic span identity; 48 sampled rules corroborate it, which is not a proof.
- **E3 constants.** E3's K_R/χ_R evaluations are float64 corroboration only. No certified staircase acceptance on the frozen grids exists.
- **Chronology.** The order of the Urow addition and the degree-12 inspections cannot be verified from durable records.
- **External state.**
  - Literature remains at digest level.
  - The PR's open or closed state was read from refs only: the GitHub API was unavailable to this session, which also lacks push credentials for this repository.
  - The off-repo artifacts listed in P-F1 were not seen.

## Outputs and storage

Committed:
- this file;
- the four reviewer reports;
- the audit scripts under `checks/audit-01/scripts/` (about 100 KB; scratch paths inside them are the audit workspace's);
- [checks/audit-01/manifest.json](checks/audit-01/manifest.json), which records byte counts and sha256 for all 63 off-Git audit outputs (583 KB).

The off-Git outputs are delivered to AC cold storage at `C:\Users\andreyac\Downloads\padua\cold_storage\padua-lanczos-drift-20261101\audit-01\`; the delivery result is recorded in LOG.

## Text for PR #15's AUDIT section

> AUDIT — audit-01 (Claude Opus 5.5 xhigh, with Opus 5.5 xhigh/high reviewer subagents) of `36c93794` (scientific `b09e1db`): CHANGES REQUIRED. 0 high, 10 medium, 32 low; no PROVED or MEASURED claim refuted. All 13 records were reconstructed. All handoff commands were rerun: decisive E1 rationals are exactly equal to the evidence; E5 and E6 are identical; both scalar reproductions PASS. Independent recomputation covered all 88 aggregate cases, the record-15 example, the E5 limits and the E6 gaps. Main changes required: rescope record 15 (generic, not "missing J-product"; credit the PD-T055 heuristic); move record 14 out of PD-N; correct the record-32 case-3 wording; disclose the rotQ24 pivot tie; correct the E1 freeze provenance; add the record-11 remainder quantifier; fix the E6 test distribution; add the PD-T042/043 predecessors; resolve the cold-storage verification. Stage WORK; Codex response-01 required. See audit-01.md.
