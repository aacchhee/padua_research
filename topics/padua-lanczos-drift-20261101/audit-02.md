# Audit 02 — response-01 and PR14/PR16 integration

- Auditor/orchestrator: Codex. Requested allocation `gpt-6-astra`, xhigh;
  resolved root variant/effort is not independently exposed. Five distinct
  Astra xhigh reviewer agents covered E1, E3/E4, E5, E6 and protocol/artifacts.
- Scientific response candidate: `cef79d66321a93d93d53e53efcb7e6744c387481`.
- Published input/handoff head: `2fd5456066de08094a35542f2ff6443c27d8c149`.
- Previously audited candidate: `36c93794ce02f92c76c89e5a9ec8095eb238d91d`.
- Initial rules read at 2fd5456. During this audit AC reported PR16 merged.
  Current main `28aaa20861d08074b77efc74eaef75cdcb36234d` was merged without
  rewriting history at `7a6dd1f7f8f10d0f9c2568e89d693b7d04cd571b`; the changed
  WORKFLOW was read there. Audit-start bookkeeping is `1776029`.
- Scientific code, theory and response evidence remain byte-identical to the
  response candidate. PR16 adds repository-only results rules and documents.
- Date: 2026-11-01. PR15 remains draft. No final IDs assigned.

## Verdict

**CHANGES REQUIRED: 0 high, 2 medium, 8 low findings. Stage WORK.**

The new checkers and measurements reproduce. The generalized closure lemma's
core, the named Padua radius theorem and its sharper constant, the finite
aggregate certificate, and the measured public-code results remain supported.
One ancillary limit assertion in the generalized record15 is false as written;
its correct factor does not invalidate the lemma or its no-o(u) conclusion.
Record05 also needs the split-result classification addressed below. No
developer proof, code, response report or audit-01 text was fixed in this audit.

The detailed reports and actual commands are part of this audit:

| Scope | Reviewer record | Essential evidence |
|---|---|---|
| E1 | [E1.md](checks/audit-02/E1.md) | [audit-02-e1-checks.json](evidence/audit-02-e1-checks.json) |
| E3/E4 | [E34.md](checks/audit-02/E34.md) | [audit-02-e34-checks.json](evidence/audit-02-e34-checks.json) |
| E5 | [E5.md](checks/audit-02/E5.md) | [audit-02-e5.json](evidence/audit-02-e5.json) |
| E6 | [E6.md](checks/audit-02/E6.md) | [audit-02-e6-checks.json](evidence/audit-02-e6-checks.json) |
| Protocol/artifacts | [Protocol.md](checks/audit-02/Protocol.md) | [artifact receipt](evidence/audit-02-protocol-artifacts.json), [text receipt](evidence/audit-02-protocol-text.json) |

## New findings

### Medium

**A02-M1 / E34-R1 — the generalized creator-defect limit drops a factor.**

Location: `tracks/bivariate-lanczos/theory/drift-codex-e4-15-projection-only-closure-obstruction.md:48`.
Equation (12) gives δ_A=κ_Aθ. With ε=u||v_m|| and a unit normal source, the
actual limit is

    lim δ_(A_m)(t)/u = (κ_(A_m)/b)||v_m||,

not the asserted ||v_m|| unless κ_(A_m)=b. The lemma establishes only
κ_(A_m)≥b. An independently constructed exact counterexample already lies
within the record's controls: uniform T3, BJ, source in v20=X[x−1]. Here
||v20||²=22/5, b²=7/15 and κ_X²=28/45. The squared relative-source limit is
88/15, whereas the displayed assertion would give 22/5. The independent
checker computes the complete spectral closure operator, not just one vector.

Correct the equality to its proper factor or state the consequent lower
limit. Preserve the qualitative no-exact/o(u) obstruction and the original
T3 v21 instance, where κ_Y=b. The core generalized parts (a)–(d) are accepted;
the stronger equality is not. See E34 report and its exact symbolic witness.

**A02-M2 / E1-R1 — separate the substantive finite scalar inequalities from
the inconclusive experimental target.**

Locations: record05:43–51, E2's status rationale and associated IDEA text.
The response acknowledges that the explicit finite >800/>7 inequalities meet
the computer-proof obligations, but retains them under a whole-file MEASURED
label because the factor10 target is inconclusive and the thresholds were
chosen post hoc. Post-hoc discovery does not make a proved finite proposition
nonmathematical; the unrelated unresolved target does not lower its status.
The result is substantive: full-operation comparator uppers, explicit
325/625-node witnesses, and a different source norm from the aggregate result.

Fresh independent exact/Arb reconstruction confirms squared certificate ratios
657331.0774535049 and 62.08553668985878, with all950 signs agreeing. Apply
WORKFLOW's split-by-default rule: preserve the MEASURED experiment and its
post-hoc history, and put the supported finite mathematical inequalities in a
separate, precisely scoped computer-assisted PROVED record with the written
reduction, committed checker/evidence and independent execution references.
Keep the actual both-grid factor10 target unresolved and the current test
INCONCLUSIVE. Do not upgrade the measured implementation experiments or claim
actual IEEE activation. If the developer disputes substantiveness, record
the disagreement for AC rather than silently changing the target or status.

### Low

| ID | Location | Correction / acceptance criterion |
|---|---|---|
| A02-L1 / E1-R2 | record03:103, record05:87; E1/E2 and IDEA coverage | Full scalar-trajectory replay was executed at degree3 only. Unchanged `first_principles.py:415–416` calls partC only if n==3. Degree4 runs records01/02 checks. Correct active coverage, or actually execute and record the missing degree4 replay. Preserve audit-01 unchanged and annotate its summary error. |
| A02-L2 / E34-R2 | ideas-e3-e4.md, IDEA?drift-claude-17 | The stored parent lies in the previous computed space, so subtracting its projection onto that whole space gives zero. Keep the candidate deferred, but specify a nonzero repair/replacement, the exact reference prefix and where new information enters before any experiment. No new experiment is requested now. |
| A02-L3 / E5-R2-F1 | record30:146 | `a_(±)=(4pi³/9)(5∓sqrt(2))` reverses the stated lower/upper labels. Define a_-=(4pi³/9)(5−sqrt(2)), a_+=(4pi³/9)(5+sqrt(2)); keep the correct interval, limit and sharper constant. |
| A02-L4 / E5-R2-F2 | record30:146 | For a≤0 the leading limit rules out an eventual negative-witness mechanism, not all finite witnesses. At n=4, fixed a*=20pi³/9−512pi gives the same point as the main positive-a witness by 2pi periodicity; Arb384 certifies P4=−0.10421866…<0. Qualify “no witness” as eventual; the main theorem is unaffected. |
| A02-L5 / E6-R1 | record50:14/24, E6:25, e6_offsample.py:14 | Separate the midpoint laws. The iid-square midpoint has product triangular density; the iid-triangle midpoint has overlap-area/piecewise-quadratic density. T24/Q24 midpoint sets are deterministic. Retain the explicit midpoint construction and sample-specific measured conclusions. |
| A02-L6 / E6-R2 | README:110, external-code:17, record50:29, E6:64, IDEA55 | `numpy<2.5` is insufficient: pinned polyrat also fails under separately installed non-yanked2.4.1. Document tested2.3.5, or a correct exclusion covering2.4; preserve unchanged upstream source and the successful exact pin. |
| A02-L7 / E6-R3 | ideas-e6.md:69, IDEA57 | Its kill criterion has the wrong direction. One accurately fitted target on the same nodes/code falsifies “drift implies all fits fail”; a target losing accuracy supports it. Actual evidence and REJECTED disposition are already correct. |
| A02-L8 / P02-F1 | proposed-record-changes:143, plan:35, report:164 and current results frontier | Carry PR16's rule through active preparation instructions: topic results live in the repository; only this topic's root RESULTS section changes at preparation. Remove/supersede active Windows-results-write obligations while preserving historical receipts/handoffs. Windows cold-storage delivery is a separate pending item. |

## Disposition of every audit-01 finding

Resolved-by-proposal means the literal change is valid but deliberately
unapplied until preparation. It does not mean the registry was updated.

| Finding | Re-audit disposition |
|---|---|
| E1-F1 | RESOLVED: exact tie and X-tie convention disclosed; independent pivot/alternative-tie checks pass. |
| E1-F2 | RESOLVED: trace is a consistency identity; exact degree12 BᵀB=D verified independently. |
| E1-F3 | RESOLVED: committed six-inequality checker and fresh independent comparisons pass. |
| E1-F4 | RESOLVED within reconstructible history: first committed freeze already has Urow; in-place changes and low-degree sharpened-DEAD behavior disclosed. Unlogged chronology is not used. |
| E1-F5 | PARTLY RESOLVED: stale reproduction text fixed; A02-M2 classification and A02-L1 coverage remain. |
| E1-F6 | RESOLVED: full comparator commands and temporary-file input-hash limitation are explicit. |
| E1-F7 | RESOLVED: omitted conditioning/Krylov predecessors and source-reading limits now disclosed. |
| E1-F8 | RESOLVED: formal-model title/aliases corrected; A02-L1 is a separate coverage correction. |
| E1-F9 | RESOLVED: s≤n stated. |
| E34-F1 | Generic-scope correction RESOLVED; new ancillary equality A02-M1 remains. |
| E34-F2 | RESOLVED: PD-T055's heuristic credited; variant, not new-mechanism, verdict explicit. |
| E34-F3 | RESOLVED: full IDEA14 content preserved; withdrawn PD-N file is a tombstone for preparation deletion. |
| E34-F4 | RESOLVED: particular-family remainder and appropriate compact smooth-family uniformity explicit. |
| E34-F5 | RESOLVED: admissible scope and staircase non-use explicit; separate criterion file is defensible. |
| E34-F6 | RESOLVED: correct independent receipts cited; unrecorded scratch is non-evidence. |
| E34-F7 | RESOLVED: full rank/σ_min versus near-orthogonality separated. |
| E34-F8 | RESOLVED BY PROPOSAL: durable OPEN-home mapping to PD-T054/IDEA151 awaits preparation. |
| E34-F9 | Retention RESOLVED; deferred recipe needs A02-L2 clarification before execution. |
| E34-F10 | RESOLVED: report, local entry and proposal reflect generic closure and IDEA14 withdrawal. |
| E5-F1 | RESOLVED: fixed-A coarse path rejects only eventual witnesses; finite windows and exact coincidence remark retained. |
| E5-F2 | RESOLVED: stale reconstruction wording annotated; frozen evidence preserved. |
| E5-F3 | RESOLVED: exact checker coverage and analytic-only steps accurately distinguished. |
| E5-F4 | RESOLVED: square-interior scope for every n≥4 justified. |
| E5-F5 | RESOLVED BY PROPOSAL: PD-T069/075 split/history/open-item anchors match uniquely. |
| E5-F6 | RESOLVED: report names scoped negative32. |
| E5-F7 | RESOLVED: correct predecessors; retained E instance and deferred G realization separated. |
| E5-F8 | Mathematical enhancement ACCEPTED as minor routine corollary; A02-L3/L4 correct its notation/scope. |
| E6-F1 | Material off-sample issue RESOLVED; midpoint-law wording A02-L5 remains low. |
| E6-F2 | RESOLVED: training residual equals gap by construction, not independent corroboration. |
| E6-F3 | RESOLVED: Gram normalization entry distinguished from off-diagonal maximum. |
| E6-F4 | RESOLVED: ridge target and unknown original chronology disclosed; new generic-target evidence remains measured. |
| E6-F5 | Format/dispositions RESOLVED; IDEA57 kill sentence A02-L7 remains. |
| E6-F6 | Tested pin/PYTHONPATH RESOLVED; compatibility bound A02-L6 remains. |
| E6-F7 | RESOLVED; this audit also executes both previously unrerun n16 grids. |
| P-F1 | Artifact integrity RESOLVED in this workspace; original Windows archival pending. One earlier theory working-byte pin remains unavailable, as qualified below. |
| P-F2 | RESOLVED by explicit disclosure of both reservation-only shared-file edits. |
| P-F3 | Executed gate accepted; removing “relaxed” changes no check. Original AC prompt did explicitly allow a relaxed gate; audit-01 lacked that source context. |
| P-F4 | RESOLVED: numbered handoff chain linked in LOG. |
| P-F5 | RESOLVED at current pinned union scan, main28aaa/PR12=9a75747; repeat before allocation/readiness. |
| P-F6 | RESOLVED: PD-T042/043 and coefficient-map/channel predecessors credited with valid separations. |
| P-F7 | RESOLVED across E1/E5/E6, with explicit digest/fulltext coverage limits. |
| P-F8 | Reproduction staleness RESOLVED; finite-claim split remains A02-M2. |

For P-F3 the original supplied task says “adventurous and less gated” and
“Relaxed novelty gate at start and before each new mechanism.” This audit
does not edit audit-01's available-record conclusion or invent omitted runs.
The actual documented gate meets the ordinary minimum, so the clarification
does not change a scientific disposition.

## Claimed-status dispositions

| Record | Disposition at the audited scope |
|---|---|
| 01 | PROVED confirmed: fixed-choice normal derivative, s≤n and fixed-degree remainder. |
| 02 | PROVED confirmed: spectral node/HS/row certificates. |
| 03 | PROVED analytic formal-model map confirmed; replay coverage needs A02-L1. |
| 04 | PROVED finite aggregate certificate confirmed with exact/rigorous independent computations; original KHS-only test INCONCLUSIVE. |
| 05 | Full scalar endpoints independently reproduced; whole-file classification not accepted as written, A02-M2. The factor10 certificate remains INCONCLUSIVE. |
| 10 | PROVED computed-polynomial upper certificate confirmed. |
| 11 | PROVED fixed-degree/fixed-family implication confirmed; polynomial-score existence/safety OPEN. Separate file and routine-corollary classification accepted. |
| 14 | IDEA-only disposition accepted; no final PD-N; remove tombstone at preparation. |
| 15 | PROVED core (a)–(d), T3 instance and qualitative obstruction confirmed; ancillary creator-limit assertion refuted, A02-M1. |
| 30 | PROVED O(n^-5) and sharper constant confirmed; minor routine corollary classification accepted; A02-L3/L4 wording corrections needed. |
| 31 | PROVED explicit residual-aware square family confirmed; no reading(G) implication. |
| 32 | PROVED scoped path failures confirmed, including eventual-only case3. |
| 50 | MEASURED implementation/fit claims confirmed, including new distributions and n16; A02-L5–L7 are corrections, not theorem upgrades. |

The all-degree exponential/matching drift theorem, actual IEEE activation,
unconditional staircase safety, original PD-T055, optimal uniform Padua radius
and PD-T056(G) remain OPEN. The main rho_n theorem is not weakened by the
notation correction in its auxiliary sharper-constant remark.

## Executions and evidence independence

Exact full commands, software versions, code/input hashes, output identities,
metadata masks and numerical tolerances are in the five reviewer reports and
their compact evidence. Reading a prior receipt is never counted as a rerun.

- **E1:** new full response checker PASS in141.9s; mathematical JSON identical.
  Independent canonical-Gram LDL/pivot code confirms all22 prefixes, ties and
  exact orthogonality. Separate exact/Arb inverse/scalar implementations verify
  all four decisive aggregate cases, the Y-tie variant, both scalar comparator
  uppers/lower witnesses and all950 signs. Reused audit-01 independent code is
  explicitly distinguished from newly authored checks. The fresh first-principles
  execution confirms scalar replay at n3, not n4.
- **E3/E4:** response checker28 cases reproduced exactly; a separate SymPy
  implementation checks15 cases and186 rule/order combinations, polynomial
  source components, α=−1, and complete spectral closure operators. An exact
  symbolic counterexample establishes A02-M1. Finite examples corroborate,
  rather than prove, the general every-rule span identity.
- **E5:** response checker scientific fields identical; independent raw-product
  series and atom-built matrices confirm both limit calculations and residual
  constants. Arb384 supplies a strict finite counterexample for A02-L4. The
  main analytic proof and general-a infimum argument were reconstructed.
- **E6:** all388 response leaves and422 n16 leaves match after narrowly listed
  command/Python/time masks. Separate long-double reference evaluation and
  QR recover the hard gaps within9.56e−16 and5.38e−17. Sampling, norms and
  vertices are independently checked. Actual polyrat2.4.1 compatibility failure
  is executed in an isolated dependency directory; the pinned2.3.5 environment
  and upstream source are unchanged. BNT source is inspected, not executed;
  no ZN run or original-paper reading is invented.
- **Root integration:** actually executed `integration_check.py` against head
  7a6dd1f, main28aaa and PR12=9a75747. PASS: current main ancestor, both
  crosswalk/ledger sections preserved, no final assignment of reserved IDs,
  clean merge-tree with PR12 and disposable squash tree identical to head.
  No live main branch or PR was merged by the auditor. Main-to-topic merging
  applied AC's PR16 update; it did not change scientific bytes.

Original scientific/response checkers remain developer inputs, not independent
implementations merely because they ran again. Independent reconstruction and
analytic review are identified separately in every subreport. Trusted software
includes CPython3.12.14, python-flint0.9.0/Arb, SymPy1.14.0, mpmath1.3.0,
NumPy2.3.5, SciPy1.17.0 and single-threaded OpenBLAS. Approximate trajectory,
reference and fit checks are corroboration, not exact proofs.

## Reading, novelty and upstream integration

The scientific reviewers each read complete783-line `state/IDEAS.md`, including
obstruction/disposition tables, then relevant full records. Root integration/
protocol review is administrative; its original-source coverage is not claimed
to be the scientific reviewers' coverage. Read scope includes all changed own
theory/code, audit-01 and its four reports, response-01 and its four reports,
local candidates/directions, proposed changes and results summaries. Full
per-reviewer source lists/hashes are in the receipts.

Important predecessor checks include PD-T032/042/043/050/053/054/055,
PD-T059/061/069/075, IDEA139/141–144, Fischer/Krylov entries, IDEA086/116,
and the square-case predecessors. Separations in output space, source norm,
fixed-choice scope and mechanism are justified. Original paper fulltexts were
not newly read; repository digests remain coverage-qualified. No exhaustive
historical novelty claim follows from this audit.

The full Git delta from36c9379 was classified into Claude's response/audit
changes and accepted upstream PR14/PR16 imports. MZ mathematics imported from
main was checked for preservation, not scientifically re-audited as new PR15
work. Current original bivariate theory files77 and protected scientific
registries are byte-identical to main. Both topics' reservation/crosswalk text
survives; the own-section changes are publication-provenance additions, not
allocation or renumbering. All15 literal OLD blocks plus one optional History
anchor match current targets uniquely, including sequential dry replacement;
none was applied.

The fresh remote inventory has only PR12 and PR15 open; PR16 is merged at
28aaa208 and all13 returned closed PRs are merged. Complete ledgers and four
registries were read/scanned at main28aaa, PR15=7a6dd1f and PR12=9a75747.
No final use of the topic's T136–155/N062–071/IDEA246–285/LIT445–459 ranges
was found. This is a pinned snapshot, not a promise that future PRs cannot
advance. Repeat the fresh union scan at preparation/readiness.

## Original artifacts and PR16 results rules

The original 799968-byte ZIP has the advertised SHA256
`27476b624d424f082a71779618b9e1f9b06d6fba7db6b662755cf886637dd3a4`.
CRC passes; all81 source entries match b09e1dbe byte-for-byte, plus SNAPSHOT.
The raw3.626MB capacity file and root E6 output also match their old identities.
The broader original run-reference scan verifies160 occurrences/147 distinct
paths. The old “46 off-repo files” count includes25 repository inputs and
duplicates: those rows cover19 distinct actual off-repository output paths,
all verified. Of46 historical SHA/path rows,45 are recoverable: one earlier
record05 working-byte metadata pin is not in available Git history. This audit
does not manufacture that file or claim its old bytes were compared. Current
record05 and all computational dependencies are independently reviewed.

No Windows bridge is available, so no Windows delivery/readback is claimed.
P-F1's artifact-integrity uncertainty is now resolved locally; archival custody
remains pending. The large raw file is nonessential: compact committed inputs
and deterministic regeneration supply the verification path. audit-01's own
Windows delivery is an attributed historical receipt, not a newly observed copy.

PR16's current rule makes topic results repository-only. This topic's results
file is present and accurately retains bounded scientific outcomes; its status/
next step is synchronized to this audit. Root RESULTS has no drift section yet;
adding only this topic's section remains a PR-preparation action. Other topics'
sections are preserved. Active obsolete Windows-results instructions are
returned as A02-L8 rather than followed.

## Next step and limits

Claude must answer all10 new findings in response-02.md; accepted old findings
need not be reopened. Material proof/status/scope changes require another
independent Codex audit. Preserve disagreements and the original measured
outcomes; do not rename an inconclusive test into a theorem or a refutation.
No final IDs, scientific registry changes, original-theory updates or readiness
decision occur here. PR15 remains draft and only AC merges.

No degree12 scalar-trajectory replay, actual IEEE realization, general stability
theorem, complete fresh literature survey, or Windows delivery was performed.
Audit outputs are committed compact evidence plus reproducible checkers; large
working/dependency files remain outside Git. The root manifest records final
pins, storage limits, integration receipt and the scientific-byte impact check.
