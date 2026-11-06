# Span drift on genuinely non-product families: log

- Branch: `codex/padua-lanczos-nonproduct-20261105` · Base: main `be9a831` (PR #29 merged) · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: PR — agent preparation complete; READY for AC's merge decision · Open handoff: none (last handoff [07](handoffs/07-readiness.md) done)
- Permanent reservation: [ALLOCATIONS](ALLOCATIONS.md), first publication `6b31356`: T472–501, N178–180, IDEA570–589, LIT630–632. Assigned T472–494, N178, IDEA570–584, LIT630; unused gaps remain permanent.
- Claims: P3 all-degree non-affine-product weight separation and uniform sufficient radius; P5 polynomial Padua capacities; P4 model/transfer lemmas and scoped covariance obstruction. Final IDs PD-T472–494, PD-N178, IDEA-570–584 and LIT-630 ([ALLOCATIONS](ALLOCATIONS.md)); see [report](report.md).

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- After Claude's PR #24 summary, AC said: "Yes make a handoff for nonproduct".
- Motivation: PD-T324/328/329 hold on SH_n, an affine image of a product measure. The target is an all-degree separation, or a proved obstruction, on a genuinely non-product family.
- Directions:
  - P1: the triangle (Proriol–Koornwinder and discrete Hahn/Krawtchouk);
  - P2: the disk (rotation invariance, with exact Pythagorean grids);
  - P3: non-affine perturbation of SH_n and its stability radius;
  - P4: a structural criterion;
  - P5: Padua (bounded);
  - P6: exact scans.
- Model allocation and round rule follow AC's instructions of the same day: 10 rounds per direction (P5 capped at 5), all in parallel.
- Rules read at `be9a831`. PR #29 changed WORKFLOW (proportionate audits, reservations at PR preparation, registry edits by reviewed diff). Branch created from main `be9a831`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## Runs needed

- Development and substantive audit01 are complete. The response's A3 BJ qualifier proceeds to focused diff re-audit in handoff05. Unrun algebraic bulk scans and unresolved rates are listed in the [report](report.md); they are not premises of the analytic proofs. External archival delivery remains pending.
- Optional, unrun: exact positive-Padua scan at degrees 2–16, all four rules,
  for the OPEN sharp-exponent question. A follow-up must select unsaturated
  Padua orders m>s, use exact algebraic inputs and full-source endpoints,
  and freeze the run specification before execution. No P3 scan is required.
  This is not a precondition for this PR.

## 2026-11-05 — continuation setup — Codex, requested gpt-6-astra high

- Role: coordinator/developer. Serving metadata not independently exposed.
- Rules/input head: `cafb74ab6f7738c8af83d0cd0f518b81af16f253`.
  Fetched main: `be9a8318150204711d5446d2ea26284cf1ed0819`, already an
  ancestor; no merge needed. Working tree was clean.
- Read AGENTS, WORKFLOW, Codex role, LOG and open handoff 01. Its explicit
  model allocation and six parallel directions govern this campaign.
- Initial network attempt failed with an unavailable proxy; retry with the
  execution tool's network permission succeeded. No credential changes.
- Wrote [plan.md](plan.md) before new experiments, including exact N2 slope
  conventions and the distinction between sufficient and maximal N4 radii.
- Assigned predecessor replay to a Sol medium worker; direction workers wait
  for N0. No scientific claim or novelty content is added by this setup.

## 2026-11-05 — N0 PASS and parallel launch

- [N0 replay](n0-replay.md), Sol medium: six SH degree/rule cases, 88 symbolic
  identities and all four requested degree-12 endpoints match exactly. All 44
  native degree-2–12 prefix rows also match. Actual native wall seconds:
  triangle BJ/mirror 3.54/1.66; rotated BJ/mirror 87.21/96.23.
- Receipt-only missing legacy `pivot_ties` handling was corrected; unchanged
  completed native outputs were then verified without rerunning the native
  cases. No mathematical mismatch. Full provenance remains in N0's record.
- Opened [draft PR #30](https://github.com/aacchhee/padua_research/pull/30),
  audit pending, no final-ID reservation and no shared registry change.
- After N0 passed, dispatched P1–P5 to distinct Sol xhigh mathematics workers
  and P6 to Sol medium, disjoint ownership as in plan. P4 owns the common
  affine-product definition; each direction owns its full prospective novelty
  gate and family admissions. No new family scan is authorized before N1.
- Clarification for P1: coordinate-swap symmetry alone does not identify BJ
  and mirror capacities while keeping the within-degree Gram–Schmidt order
  fixed. Any equality or separation needs a derivation in the actual model.

### Canonical protocol disclosure — P3 gate timing

The proposal was sent during the initial P3 launch on 2026-11-05, after
N0's launch checkpoint `ddb6c2f` (22:06:45 UTC) and before this disclosure
was first committed in `2ebea9a` (22:08:34 UTC). An exact message timestamp
is not preserved. It proposed a high-mode nonmultiplicative reweighting of
SH_n and observed its low-moment cancellation, aiming to retain the
all-degree separation with a uniform nonzero parameter. No experiment or
P3 file had yet been written.

Required shortlisted-entry/theory reads and complete obstruction/disposition
table reads were still incomplete. The gate record later reports recovering
ranges omitted by truncated initial previews. The exact per-entry list of
reads still outstanding at proposal time is not preserved; no worker
transcript is available, and a retrospective exact list cannot be supplied.
The coordinator stopped further derivation/testing until completion of those
reads and required preservation of this chronology.

The retained candidate uses the same high-mode rank-two mechanism:
`w_kl=v_k v_l[1+eta*(-1)^(k+l)]` on SH_n, with admitted range
`n>=2, 0<|eta|<1` and the same separation/radius target. No different initial
candidate is recorded. Identity of every formula/range detail with the
unpreserved proposal message cannot be independently established. The gate
and admission first entered Git together in `6988024` (22:15:43 UTC), so
"gate completed before admission" rests on worker self-report, not an
ordered pair of Git snapshots. The moment-cancellation observation predates
the completed gate.

Later reading cannot make the proposal prospective. **AC decision
2026-11-06: accepted**, with audit-01 A2's qualifier: disclosed, not waived,
not cured; mathematical acceptance is unaffected. The prior campaign's
acceptance did not cover this deviation; this topic's Q1 decision does.
Other records link here rather than repeat the chronology. The remaining
historical precision limits above are explicit, not reconstructed facts.

## 2026-11-05 — P1/P6 round 1 checkpoint

- P1 completed its prospective gate and proved [triangle admission](theory/p1-triangle-admission.md),
  including a self-contained falling-factorial injectivity proof and positive
  rational weight normalization. T24 uniform and a=b=c=2 reweighting meet N1
  throughout proposed scan degrees. No new P1 experiment or growth claim.
- P6 completed the [implementation gate](novelty-gate-P6.md) and froze its
  [weighted input/endpoint schema and costs](scan-methods.md). Existing
  uniform T24 degree-2–20 evidence is reused rather than regenerated; this
  will be labelled inherited-scan reanalysis. New weighted pilots remain
  gated on P4's written weighted-coordinate reduction.
- P1's next round owns the continuous triangle recurrence/moment probe; P4
  owns the shared continuous-source reduction so it is not duplicated.
- Candidate/theory records retain provisional IDs only. No shared registries
  or final allocations changed.

## 2026-11-05 — P2 round 1 checkpoint

- Completed [P2 prospective gate](novelty-gate-P2.md), then proved
  [continuous radial disk and D36x9 admission](theory/p2-01-family-admission.md).
  The finite 324-point rational ring grid is injective through17, has36
  convex-hull vertices and D4 invariance without full rotation invariance. It is a distinct finite measure,
  with no asserted cubature relation to the continuous radial disk.
- P2's tiny exact moment/creator reconstruction through 8
  executed successfully in 0.154s; its fuller IDEA record was written after
  execution, as [P2 chronology](attempts/P2.md#execution-timing-and-parked-probe)
  records. This was before the coordinator separated admission
  and structural interpretation into round boundaries. Code and compact
  evidence are preserved; interpretation is round2, not an N2 rate claim.
- No external fulltext or published recurrence theorem was used for these
  elementary admission/moment proofs. No priority claim.

## 2026-11-05 — P3/P4 round 1 and P6 round 2 checkpoint

- P3 wrote its [non-affine-product weight admission](theory/p3-01-high-mode-weight-admission.md)
  after completing the remaining gate reads. The high mode changes with n;
  one fixed nonzero eta in(-1,1) gives positive exact data for every n>=2.
  Capacity and radius are the next step, not inferred from admission.
- P4 proved the [common definition/admission lemmas](theory/nonproduct-definition.md),
  [weighted finite quotient](theory/p4-weighted-normal-quotient.md),
  [exact atomless capacity identity](theory/p4-continuous-capacity.md) and
  [moment-preserving transfer](theory/p4-moment-capacity-transfer.md).
  These distinguish arbitrary finite and atomless source models. They are
  fixed-degree analytic supporting results, not a passed cross-family
  criterion gate or an all-degree family growth theorem.
- P6 actually executed36 complete-source degree2–4 rows on T24, H24_222 and
  D36x9 (four rules each), matching independent arithmetic implementations
  exactly. T24 also matches inherited endpoint/choice evidence. Largest
  producer/checker case times were under0.07/0.22s. Receipts and code are
  committed; distinct-agent verification remains separate.
- Next P6 cost step: prospectively benchmark degree8 before degree16,
  120s per backend/rule, then scale only feasible cases within the original
  600s per-case high-scan cap. N2 thresholds/windows are unchanged. Reanalyze
  inherited T24 certified log intervals separately from new experiments.

## 2026-11-05 — P1/P2/P3 round 2 and P5 round 1

- P1's exact continuous triangle probe verified45 monic basis polynomials,
  132 creators and45 norms through8 (1.23s). This does not close the full
  capacity recursion; N3 redirects to P4. A bounded ten-minute public-source
  discovery/read round follows; no theorem is imported from an unread source.
- P2 proved whole-algorithm orthogonal covariance and an explicit degree-two
  basis-mixing obstruction to the symmetry-only BJ/mirror identification.
  Its exact finite recurrence probe remains MEASURED and restricted. Paused
  at N3 redirect, with the disk rate question OPEN rather than inventing
  redundant rounds; P4 owns the common criterion route.
- P3 proved [exact moments/creators and actual normal witness](theory/p3-02-exact-moments-creators.md),
  then the [all-degree separation and uniform sufficient eta range](theory/p3-03-uniform-capacity-radius.md).
  For every n>=2 and 0<|eta|<1, original PD-T324 BJ and mirror bounds survive
  unchanged. In particular eta_0(n)=1/2 passes N4 analytically. This is the
  authorized nonmultiplicative-weight route, with n-dependent frequency;
  no fixed-density/node-map claim, empirical N2 pass, maximal radius or
  strict small-n ordering is asserted. The direct proof does not use N2
  fits as a premise. Supplementary distinct Astra high review is underway.
- P5 proved exact Padua admission/cubature, then two-sided polynomial
  BJ/mirror capacity bounds for all m>s>=1, independently of fitted trends.
  Exact algebraic m2–5 supplementary checks pass (1.90s), including124
  source-coordinate derivative comparisons. Sharp exponent, alternating/
  pivot uppers and switching remain OPEN. Development stops after this
  substantive first round; a distinct Astra high reviewer is reconstructing
  the proof and rerunning checks.
- A second distinct Astra high checker independently verifies P6 code,
  actual scans and signed-OLS interval screens. These supplementary checks
  do not replace the required later Claude audit.

## 2026-11-05 — P4 round 2 and P6 round 3

- P4 executed an exact weighted normal-derivative comparison over370 source
  directions, then proved the scoped [fixed-covariance absolute-capacity
  obstruction](theory/p4-covariance-capacity-obstruction.md), corroborated
  by eight rational moment/Gram cases. Distinct fixed principal axes do not
  control absolute degree-two capacity. This says nothing about the original
  all-degree BJ/best ratio iff, which remains OPEN. A final bounded round
  screens a restricted final-degree block-norm candidate for duplication.
- P6 cost benchmarks matched both arithmetic paths through8 on H24_222
  and D36x9. Fresh H24 degree2–16 then completed60 rows, all four rules,
  maximum producer/checker case times3.24/10.20s. [N2 reanalysis](theory/p6-n2-screen.md)
  on inherited T24 and fresh H24 is INCONCLUSIVE under unchanged thresholds;
  signed-OLS interval extrema and independently implemented corner checks
  agree. No exact capacity or asymptotic rate was calculated.
- Disk16 is in progress under600s per case. If initial BJ/mirror cases hit
  the cap, stop remaining similar-cost cases, recording any automatically
  started case as cancelled/partial. Retain the complete independently
  matched degree8 coverage and an honest incomplete N2 mask. Per-case limits
  are not shortened because of elapsed waiting.

## 2026-11-05 — final model/source rounds and supplementary checks

- P1 round3 completed its bounded primary-source search/read within ten
  minutes: the complete Xu preprint is read, other fulltext/access limits
  are in the [source checkpoint](theory/p1-literature-checkpoint.md). The
  triangle rate target stays OPEN; no theorem is imported from an unread
  source. P1 pauses after three recorded rounds.
- P4 round3 consolidated a routine attained terminal-degree block norm
  into its existing weighted quotient record, without a new ID. It supplies
  a restricted capacity, hence an all-source lower only. Twenty-two exact
  simultaneous-source tests pass; P4 pauses with the general criterion OPEN.
- [Distinct Astra high mathematical review](independent-checks-math.md)
  accepts P3/P4/P5 and the focused terminal-block addition without unresolved
  mathematical findings. Four actual separate exact reruns pass. The
  [distinct scan review](independent-checks-scans.md) reproduces H24 through16,
  disk through8, independently reconstructs12 small formula cases and both
  N2 outcomes, and checks malformed inputs. Disk16 is outside that scope.
- Disk16 BJ/mirror fast producers completed in277.84/313.87s; other fast
  cases and independent arithmetic remain in progress. Given AC's6h/run,
  ~48h CPU authorization, prospectively extend only missing disk cases to
  3600s in a separate successor, up to four native processes. Preserve the
  original600s outcomes and source/harness hashes. Unstarted scalar600s
  cases may be superseded directly; any automatically started case is
  recorded as cancelled if stopped. This is a resource-plan extension,
  with no N2 threshold/input/model change or fabricated completion.
- A bounded Sol medium technical worker investigates exact-zero fast paths
  in the scalar checker. It owns disjoint source/note files and may not
  replace the accepted path without measured benefit and focused review.
  Current native source arithmetic and in-flight identities stay unchanged.

## 2026-11-05 — disk resource response and P2/P6 checkpoints

- The original D36x9 producer outcomes are exact: BJ277.84s, mirror313.87s,
  pivot572.90s completed; alternating timed out at600.01s with its2–9
  prefixes completed. Auto-started scalar BJ/mirror were stopped during
  basis construction, with no completed rows; scalar alt/pivot were
  deferred unstarted. [Closure receipt](evidence/p6-disk-original-cancellation.json)
  preserves actual attempted/unstarted masks and raw identities. The
  3600s successor reuses completed producers and runs only missing cases.
- P2 admitted a [distinct lower-denominator D65x9 family](theory/p2-04-low-denominator-rings.md)
  before execution, under its delta gate. Same36 directions/nine radii
  cardinality and rank proof, changed support, denominator585 instead of
  49,725. The original family and its cost evidence are never overwritten.
  A distinct Astra high reviewer accepts this admission and independently
  repeats the exact count/LCM check.
- P6's fresh D65 pilot2–8, all four rules and both arithmetic paths, matches
  28 rows. It ran as one short extra native process sharing the existing
  four-core quota, without pausing old wall-timed cases. A degree12
  alternating-only cost probe is the next step; it does not claim all-rule
  coverage or an N2 window. Full16 scheduling awaits that cost evidence.
- The [bounded scalar-checker optimization experiment](p6-speed-notes.md)
  found no useful gain: BJ8 approximately7.34 to7.29s, pivot8 approximately
  10.09 to12.47s. Exact-zero variants and six equality checks are retained
  as finite implementation evidence; they were not adopted. No independent
  representation/source reduction or negative mathematical theorem follows.
- Prepared an inventory generator for the coordinator to run after final
  code/receipts are committed. It indexes committed code/data, actual local
  artifacts and unavailable paths, without claiming external delivery or
  hash-pinning prose. Final manifest generation remains pending.

## 2026-11-05 — bounded checker cost gates and exact reflection method

- D65 alternating12 producer completed32.90s; scalar checker timed out120s
  with no endpoint rows. This is a cost-only incomplete probe, not an N2
  result or a rejection of that measure's growth behavior.
- Installed python-flint0.9.0/FLINT3.6.0 only under campaign `/tmp/deps`,
  after runtime/network checks. The independent matrix-inverse checker
  verifies the complete exported basis/creators/source scales before its
  own all-source inversion. Small cases agree, and distinct malformed-
  export controls pass, but generic and block variants time out at8 and
  are slower than the original scalar path. [Notes](flint-check-notes.md).
  Neither was promoted to16. Original native source hashes stay unchanged.
- P4 wrote the [new dated reflection method](p6-reflection-methods.md),
  distinguished from every earlier no-symmetry plan/outcome. A distinct
  Astra high mathematical reviewer accepted its sign-similarity proof and
  all seven guards before the coordinator authorized experiments. It is
  exact scalar-energy reuse, not compression of the measure or source
  domain: all324 node/normal contributions and every source position are
  retained. No coordinate swap or growth classifier is inferred.
- New scalar source `p6_reflection_scalar.cpp` is individually pinned.
  Developer paired6/8 pilots pass all ten cases and all original nonelapsed
  fields, including Gram counts. The distinct Astra scan reviewer freshly
  verifies56 degree2–8 rows on both disks against both accepted paths,
  112 full-field comparisons; malformed closure/weight cases reject.
  Actual degree8 wall-time gains are about1.7–2.2x; no16 gain is presumed.
- After those gates, authorized a separate3600s/case reflection16 successor
  for missing original D36 validations. Reuse completed producer and scalar
  cases. Old scalar alt/pivot may be superseded with explicit cancellation
  masks; BJ/mirror continue until complete/cap/replaced. Every final case
  must retain its actual checker-source identity; no incomplete original
  receipt is relabeled PASS. Disk N2 waits for all60 matched rows.

## 2026-11-05 — compact evidence and disk completion checkpoint

- P6 retained the closed incomplete scalar successor and explicit alt/pivot
  supersession receipt. Original scalar BJ/mirror completed; the new
  reflection successor checks only the missing two rules. Four-rule producer
  references are frozen independently, and active receipts remain outside
  this checkpoint until their runs close.
- The Hahn compact table retains all60 exact outward endpoint-log rows. A
  distinct checker verifies120 logarithm enclosures, all60 full-field raw
  pairs, eight provenance entries and all32 signed-OLS corners per window.
  Both windows remain INCONCLUSIVE. This small committed evidence supports
  repository-only rechecking of the screen without committing large arrays.
- Published source/receipt checkpoint `17c9d85` preserves the resumed
  collectors, compact checkers and closed attempts. Primary and separately
  launched supplementary reflection16 jobs continue in the same environment;
  reconnection did not restart any native computation. Their provenance is
  retained in the scan review.

### Canonical storage-budget observation

A coordinator check at source checkpoint `17c9d85` counted5,187,037 bytes
in1,059 tracked JSON/compressed data files repository-wide, of which358,822
bytes belong to this topic. This broad count includes inventories/receipts;
it does not establish that every byte is a regenerable scientific output.
The inherited portion is4,828,215 bytes. The final inventory will add its
actual measured footprint below. Per-file compliance alone therefore does
not establish WORKFLOW's repository-wide "well below5MB" generated-output
target. No unrelated historical evidence was altered under this topic's
limited scope. Retain this aggregate-budget issue for the substantive audit,
rather than claiming complete storage-budget compliance.

The executed repository command
`python -B tools/cold_storage.py plan topics/padua-lanczos-nonproduct-20261105`
reported zero tracked candidate files and zero bytes at its16,384-byte
threshold. This is a planning result, not external delivery or archive
verification. Raw arrays stay in local working storage with availability
recorded by the final inventory.

## 2026-11-05 — D36 full acceptance and N2 closure

- All60 D36x9 four-rule degree2–16 rows now match exactly, including Gram
  counts. BJ/mirror use original scalar GMP checks (1883.13/1980.34s);
  alternating/pivot use reviewed reflection GMP. Alternating collector wall
  time is1611.67s; pivot's retained native rounded elapsed is1172.1s, with
  its collector wall time unavailable. All reflection guards pass.
- The original collector saved seven cases and remains INCOMPLETE. Its
  precise interruption cause is unknown; an earlier output-stream hypothesis
  is not established. A separate artifact-only recovery validates the full
  retained pivot rows/guards without rerunning native code. Distinct focused
  review accepts that recovery and all60 comparisons.
- D36 N2 is INCONCLUSIVE: slope boxes are approximately
  [-.50785,1.06105] on8–12 and[-.88738,1.16247] on12–16. Both rational
  logarithm paths and32-corner OLS agree. No family rate follows.
- P6 round6 closes the planned finite completion step; unrun SH/Padua bulk
  scans remain outside the analytic theorem premises.

## 2026-11-05 — supplementary replay accepted; development complete

- The distinct Astra high reviewer collected its earlier separately launched
  disk16 alternating/pivot execution:30 rows match every nonelapsed field
  against both producer and primary checker, including Gram counts, choices,
  ties and trace. Both cases retain152 sources and all reflection guards.
  The reviewer did not freshly rerun disk16 BJ/mirror; its actual high scope
  and earlier low controls remain distinguished.
- The reviewer's original collector remains INCOMPLETE after saving pivot
  (exit0,1177.55s wall). A separate artifact-only collection verifies complete
  alternating output; its unsaved subprocess exit/timing metadata is not
  reconstructed. No native case was restarted. Distinct exact log/OLS and
  compact-table validations accept all three finite N2 outcomes.
- P1/P2/general growth targets remain OPEN, P3/P5 analytical results retain
  their explicit models/quantifiers, and no final IDs/shared registries were
  changed. The single substantive Claude Opus5.5 xhigh audit is next;
  supplementary acceptance does not replace it or waive canonical issues.

## 2026-11-05 — final evidence inventory

- Generated from committed source head
  `62668c194ea510907f7a2a9d47c33d7c67f7a4dc`:40 code files,70 receipts,
  317 unique external paths and497 references. Checked every chunk's bytes,
  SHA256, record count and source head; largest JSON16,240 bytes. All990
  available declared byte/hash comparisons MATCH; four comparisons on two
  inherited paths are unavailable because those paths lie outside the
  explicitly read campaign root. No new campaign path is unavailable.
- Two unread inherited references are the original frontier G1 full input
  manifest and source report; the accepted compact evidence/reanalysis and
  its limits remain recorded. No external archival delivery is claimed.
- The18 inventory/index JSON files add238,041 bytes. Final broad repository
  JSON/compressed-data count is5,489,510 bytes in1,087 files; this topic
  contributes661,295 bytes. This updates the canonical storage-budget
  observation above and leaves its audit obligation explicit. The inventory
  is an observational local index, not a retrievable archive/export receipt.
- Development outputs, report and small evidence are complete. Handoff02
  requests the single substantive Claude audit, including canonical protocol
  and storage-budget issues, before final IDs/registration/readiness.

## 2026-11-06 — Claude audit 01

- Claude, configured claude-opus-5-5 xhigh, auditor and topic orchestrator. Rules read at `b5d2d5de5395889e98443fc0aa4776982c41617a`, which matches main `be9a831`. Audited input `38237fe`. Five independent Opus subagents were given disjoint scopes (P3, P5, P4 with P1/P2, P6 reruns, novelty/protocol); only the orchestrator writes to Git.
- **AC decision, 2026-11-06 (canonical record):** "Do not worry about storage, this will be an own cleanup topic. As long as everything is under 10mb, do not take cleaning actions."
  - This settles handoff 02 item 7 and the [storage-budget observation](#canonical-storage-budget-observation) for this topic.
  - Measured totals are 5,489,510 bytes of JSON/compressed data and 5,868,931 bytes of all data-like files, both under 10 MB.
  - No cleanup action is taken.
- Audit report: [audit-01.md](audit-01.md).
- Verdict: WORK.
  - No BLOCKING finding.
  - All proofs in scope were reconstructed and accepted at their stated scope.
  - All consequential reruns agree, including fresh H24 degree-16 rows, D36x9 degree-16 producers for all four rules, the reflection pivot at degree 16, and an exact N2 recomputation.
- Findings: three MAJOR (A1 P3 moment-equivalence framing; A2 incomplete P3 gate-timing disclosure; A3 P1 chain holds under BJ only), eighteen MINOR and several NOTEs.
- Auditor check code is in [audit-01-checks/](audit-01-checks/).
- Questions Q1–Q3 (P3 gate timing, P3 scope intent, N2 skipped before the P3/P5 proofs) were referred to AC on 2026-11-06.
- Handoff 02 is done in `ea13ed4`. Next: [handoff 03](handoffs/03-response.md), the Codex response.
- **AC decision, 2026-11-06, on Q1:** "Q1 is accepted."
  - The disclosed P3 gate-timing deviation is accepted with the qualifier proposed in audit-01 A2.
  - The A2 record completion, items (a)–(d), still belongs to the Codex response. The qualifier's AC-decision date is 2026-11-06.
  - Q2 and Q3 remain open; AC asked for Claude's suggestions.
- **AC decision, 2026-11-06, on Q2 and Q3:** "Yes agree with both suggestions." This accepts Claude's two suggestions as AC's decision.
  - **Q2.** The P3 result is accepted as the answer to the formal goal, recorded as a weaker variant.
    - Its title and scope in the registry and paper must say "non-affine-product measures moment-equivalent to SH_n through degree 2n+1, with an n-dependent weight mode".
    - An n-independent perturbation (one fixed smooth density 1+eta*phi(s,t), or a nonlinear node map) is recorded as an OPEN, deferred target with a resume condition. Its first step is a perturbation bound for the normal-quotient map using the degree-≤2n moments, under the original N4 kill test. It is a follow-up topic, not a precondition for this PR.
    - Optionally, the report may interpret P3 and P5 together (degree-≤2n moments and the normal space, not productness, as what matters), labelled as interpretation, not theorem.
  - **Q3.** The P3/P5 proofs without the N2 screen are accepted as a dated deviation, and no new scans are required for this PR.
    - A P3 scan is not required.
    - An exact Padua scan (degrees 2–16, four rules) goes under "Runs needed" as optional evidence for the OPEN sharp-exponent question.
  - These are wording and record additions, so they need no further audit round. Handoff 03 is superseded by [handoff 04](handoffs/04-response.md).

## 2026-11-06 — Codex response setup and scope clarification

- Coordinator/developer: Codex, requested gpt-6-astra high; serving metadata
  not independently exposed. Rules read at local `b5d2d5d`, then current
  input `1f809519b353512a447661b35df9e92ad0ec6e06`; rule files are unchanged.
  Fetched main `be9a8318150204711d5446d2ea26284cf1ed0819` and the remote
  topic, then fast-forwarded the clean topic to the latter. Main is already
  an ancestor. Open handoff04 governs this response.
- The reading allowing an n-dependent weight mode was the Codex coordinator's
  decision, as recorded in attempts/P3, not AC's original scope instruction.
  AC's [Q2 decision](#2026-11-06--claude-audit-01) now accepts the result as
  the formal goal's weaker variant: non-affine-product measures
  moment-equivalent to SH_n through degree 2n+1, with an n-dependent weight
  mode. The n-independent target is OPEN/deferred to a follow-up topic.
- A3 is delegated as a mathematical statement correction (Sol high), with
  mechanical record responses on disjoint files (Sol medium). No accepted
  theorem proof, finite outcome or frozen receipt is reopened. These are
  responses to findings, not generation of a new mechanism; no new novelty
  gate or scan is required. Omitted predecessor records are read before
  adding their retrospective cross-references.

### Canonical N2 chronology correction — P3/P5 analytic proofs

This is the dated 2026-11-06 retrospective record of the coordinator's
2026-11-05 decision to proceed directly to the P3/P5 analytic proofs without
the handoff01 N2 screens or the requested P6 bulk algebraic scans. The
proofs have no screen premise, but the omitted screen-before-proof step was
a protocol deviation; it was not prospectively waived. AC's [Q3 decision](#2026-11-06--claude-audit-01)
accepts that deviation and requires no new scans for this PR. No P3 scan
is required. The optional Padua scan below concerns the OPEN sharp-exponent
question and is not an acceptance condition.

### Canonical frozen-receipt provenance qualification

The H24/D36 full16 and benchmark8 receipts record head `6988024`, while
their pinned harness `cbb3314d` is the p6_scan.py revision first committed
in `dbe5c81`: those executions used a dirty working tree, and the source
is recoverable by its pinned hash/later commit. N0's original harness
`18981aa5` is absent from committed history; its exact original harness
cannot be recovered from Git. Frozen receipts remain byte-unchanged. These
provenance limits do not alter the scientific comparisons; [audit01](audit-01.md)
records its fresh reproductions and their scope.

## 2026-11-06 — response01 complete; focused re-audit next

- [response01](response-01.md) answers A1–A3 and MINOR1–18, preserves every
  NOTE and records AC's decided Q1–Q3 without re-asking. Historical details
  not preserved for A2 are explicitly unresolved facts, not invented reads.
- A3 material correction is isolated in `3b0a990dda7a630cf4ea904639c01dad717c2ea9`
  (parent `1f80951`): the finite central-binomial source chain is explicitly
  under BJ. No mirror/alternating values or new proof were added.
- Other corrections are in `04ba07bc10a680dc2a6bc90041f5013ba11482e7` and
  this response output. MINOR16 is wording only: D4-invariant, not fully
  rotation-invariant. No additional symmetry proof or material claim was
  added. P5 checker comments have the same executable AST as before.
- Frozen evidence/inventory and audit01 remain byte-unchanged. No new scan,
  receipt rewrite, cleanup, ID reservation or shared-registry edit occurred.
  No mathematical tests were repeated: the response changes statements and
  records, and relies on the completed substantive audit's computations.
- [Handoff05](handoffs/05-focused-audit.md) requests Claude Opus5.5 high
  review of the A3 diff only, with the mechanical response/readiness inputs.
  Final-ID allocation and shared registry application remain subsequent
  preparation tasks; this branch stays draft.

## 2026-11-06 — Claude focused audit 02

- Claude, configured claude-opus-5-5 high. Rules read at `68bf172`; input `84f3d50`.
- [Audit 02](audit-02.md) **accepts** the A3 BJ-only correction. A targeted rerun of the committed probe logic for all rules confirms that the chain holds under BJ only; mirror and alternating give 1,0,…,0.
- Audit 02 reviewed response 01's other changes by diff and found them non-material.
- One MINOR wording item (B1, `p3-03:208`) is to be fixed at preparation.
- Stage PR. Handoff 05 is done in `c582791`. Next: [handoff 06](handoffs/06-preparation.md), PR preparation.

## 2026-11-06 — Codex PR preparation and fresh reservation

- Rules/input read at `72cbce7816cdd6e02e799c85cb68f79001f831f7`. Coordinator
  Codex requested gpt-6-astra high; mechanical inventory worker configured
  gpt-6.1-sol medium; serving metadata not independently exposed. Refreshed
  main `be9a8318150204711d5446d2ea26284cf1ed0819` and fast-forwarded the
  clean topic to remote72cbce7. Main is already an ancestor.
- Handoff06 governs PR preparation. Audit02 accepted A3, with only MINOR B1
  left for wording correction. No accepted proof, finite outcome or AC
  decision is reopened. This is registration of audited content, not new
  candidate generation; no new novelty gate/scientific run is needed.
- The complete29-PR all-state listing has open27/28/30 and26 closed-merged,
  none closed-unmerged. Read62 complete ledger/registry copies at the four
  heads in [ALLOCATIONS](ALLOCATIONS.md), including13 distinct full ledger
  versions. Namespace maxima T471/N177/IDEA569/LIT629 include permanent gaps.
- Reserve fresh T472–501(30), N178–180(3), IDEA570–589(20), LIT630–632(3)
  before assignment, with no collision or accepted-ID renumbering. The first
  pushed ledger commit establishes priority and is linked in PR30. No final
  ID is assigned by this checkpoint. No cleaning action is taken.

## 2026-11-06 — registry application and preparation output

- Reservation publication `6b313567702b0ec465330e2ca4b8186d8be210a4`
  was pushed and linked in PR30 before assignment. Main and PR28 are unchanged; the PR27 advance and byte-identity refresh
  are recorded below. No earlier ID or range was modified.
- Assigned PD-T472–494 (13 PROVED,4 MEASURED,6 OPEN), PD-N178 (PROVED),
  IDEA570–584 and LIT630. The full provisional-to-final namespace map and
  considered subroute aliases are in ID_CROSSWALK. N0 remains verification
  only, and terminal-block/reflection corollaries receive no new ID.
- The six new OPEN records are faithful homes for previously audited targets,
  not newly developed mathematics: triangle/disk rates, structural criterion,
  sharp Padua order, alternating/pivot uppers and fixed-perturbation robustness.
  New IDs do not promote supporting lemmas to PARTIAL.
- Applied additive entries to PROOF_STATUS, IDEAS, literature INDEX, CURRENT,
  CROSSWALK and this topic's RESULTS section; prior topic content is preserved.
  Shared registries contain content/status/dispositions and completed audit
  links, with no pending process stage. Current target records retain the
  exact aggregate model and all undecided quantifiers.
- Canonical records carry final IDs and full provisional aliases, preserving
  old heading anchors. Audit02 B1 wording now explicitly places |eta|=1
  outside the admitted positive full-support family. No accepted proof,
  status or evidence beyond the audited content changes; final-ID mapping
  and registration are the mechanical readiness diff, not a new audit batch.
- No new scan, checker change, receipt rewrite, storage cleanup or external
  archive delivery. Prepared PR remains draft pending the single Claude
  readiness diff/reservation refresh. Only AC merges.

- Immediate registration publication check: peer PR27 advanced to8dc1521
  while preparation was in progress; all16 ledger/registry copies are
  byte-identical to fc10953. Namespace maxima remain unchanged. The refreshed
  all-state API listing and the preserved initial listing both contain29
  PRs (no PR7),26 merged and open27/28/30, no closed-unmerged. Corrected
  the initial prose population count of30/27; that counting error changed
  neither which branch heads/files were scanned nor the safe ID bounds.

- Mechanical verification passes:24 unique theory/negative registry rows,
  exact23-PD-T status distribution,15 candidate IDs,1 LIT,24 matching durable
  theory IDs and598 checked local links at this checkpoint. Every prior
  shared-registry byte is preserved. Reverse mapping of the existing24
  canonical files leaves only B1 wording, one updated heading link and
  allocation-state wording; accepted statements/proofs/statuses are unchanged.
  Frozen code/data/inventories/audits remain byte-unchanged.
- [Handoff07](handoffs/07-readiness.md) pins the preparation output and exact
  registry diff against base be9a831. It requests the single Claude Opus5.5
  high readiness check: registry application, B1 and fresh reservation union.
  There is no assigned multi-PR merge order or batch integration in this
  single-topic preparation; no peer approval or merge sequence is inferred.

## 2026-11-06 — Claude readiness 01; agent preparation complete

- Claude, configured claude-opus-5-5 high. Rules read at `54b01f1`; input `418b816`.
- [Readiness 01](readiness-01.md): **READY**.
  - The registry diff only adds lines and applies the audited content faithfully.
  - B1 is fixed.
  - The fresh reservation union is clean. At main `be9a831`, PR27 `8dc1521`, PR28 `4e87fc0` and PR30 `54b01f1`, the peer maxima are T471, N177, IDEA569 and LIT629. All 29 PRs were listed; none is closed without merging. There are no collisions.
- Three MINOR auditor fixes (wording, a table and stale process text) are in `0f2d44e`, listed in the readiness record.
- Handoff 07 is done in `ee280e6`. No assigned agent work remains, so there is no open handoff.
- Decision requested from AC: squash-merge PR #30. Refresh the reservation union first if main or a peer ledger changes before the merge.
