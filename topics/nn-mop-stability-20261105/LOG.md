# NN MOP IEP: conditioning and stable algorithms: log

- Branch: `codex/nn-mop-stability-20261105` · Initial base: main `b4d292e`; reconciled main `5adc3e2` (PR #24 merged) · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: PR (response-01 accepted in audit-02; Codex audit of the Claude G5 run, then PR preparation) · Next: `Codex (gpt-6-astra, medium): Continue codex/nn-mop-stability-20261105.` · Next handoff: [handoffs/06-g5-audit-prep.md](handoffs/06-g5-audit-prep.md).
- Reserved final-ID ranges: T432–471, N=162–177, IDEA530–569, LIT614–629; reservation only, no assignments. See ALLOCATIONS.md.
- Claims: provisional analytic/exact PROVED and floating MEASURED records in theory/; general solver stability and matching sharp growth remain OPEN. [Claude audit-01](audit-01.md): no BLOCKING; four MAJOR findings answered in [response-01.md](response-01.md); [audit-02](audit-02.md) accepted the response, with eight MINOR items for preparation.
- Open for AC: none (2026-11-06 decisions below). Ask AC before using Syvert.

## 2026-11-05 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC asked for more detail on the NN-MOP open item, then said: "Yes open a topic. You may be a bit more adventurous in plans."
- The topic first separates conditioning from algorithmic instability. PD-T290 measured forward error only, while LIT-347 reports weak stability for the step-line analogue on the same families.
- Directions D1–D7:
  - D1: a conditioning theory;
  - D2: stage isolation with stable marginals;
  - D3: native NN algorithms (core transformations, lattice Lanczos, redundancy via zero curvature, a coupled updater);
  - D4: integrable-systems routes (Christoffel/Geronimus transforms, Toda flows, lattice Schrödinger spectral data);
  - D5: backward-error theory;
  - D6: a bounded bivariate return probe;
  - D7: comparison with the public IEP-MOP code and an outline of a possible note for Leuven.
- Model allocation and round rule follow AC's bridge instructions of the same day, with 10 rounds per direction (D6 capped at 3).
- Rules read at `b4d292e` (AGENTS/WORKFLOW unchanged since `440d107`). Branch created from main `b4d292e`. Only this LOG, handoff 01 and the results stub were added. No computation was run and no claim made.

## Runs needed

- G0–G5 and D1–D7 as in handoff 01.

## 2026-11-05 — Codex coordinator, requested gpt-6-astra high — resumed WORK

- Rules and source read at full head `823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`. Current main/base checked via connector: `b4d292eea5eed373002506d5e16a3761bd7ae10e`; no base reconciliation needed. Serving model/effective effort metadata are not independently exposed.
- Shell Git fetch fails before HTTP because the inherited proxy port8080 is unreachable. Used the authorized GitHub connector and isolated pinned snapshot; [complete fetched list](input-snapshot.json). Local old `work` checkout is unchanged. No network policy bypass.
- Wrote [plan.md](plan.md), including G3 prediction, before any experiment. Delegated disjoint D1–D7 scopes under handoff01's explicit parallel/model allocation; [round ledger](rounds.md). Workers read gate and predecessor evidence before generating candidates. Coordinator does not claim novel science from setup.
- Refreshed main/all open PR24/27 and all 44 ledger/registry copies; no closed-unmerged PR. [Reservation](ALLOCATIONS.md) is strictly above unionT431/N=161/IDEA529/LIT613, including permanent gaps. No final assignment/shared-registry change.
- Current outputs are development in progress. Audit PENDING. Only AC merges.


- Snapshot transport correction: the initial materializer appended one extra final LF to each fetched file. Restored all 222 unchanged inputs byte-for-byte (the topic LOG is already being updated) against their pinned Git blob SHA before final evidence collection; this changes no scientific content. Initial replay values matched exactly; code-hash receipts are refreshed after correction.

- Operational clarification: default shell sandbox networking could not reach the proxy; explicitly enabled-network execution reaches GitHub but has no CLI credentials. The connector is authenticated. AC explicitly allowed its verified GitHub noreply author address for this campaign, resolving handoff01's email requirement. Setup/reservation first published as d87925630e9e460031df319f3994ca2e7fad8ca0; draft PR28 opened. Refreshed peer heads PR27 3dda890 / PR24 0299fcf: no reservation change or collision.
- Astra ultra escalation justification (D1 hard step): the sampled induced condition norms grow by many orders while the requested all-N growth law remains unresolved; a bounded independent analytic lower-bound attempt is a decisive hard mathematics step, not a fit or routine table generation. A separate Astra ultra worker owns only D1-hard files and cannot replace Claude audit.

## Round1 checkpoint — D1, D2, D6 and D7

- D1 sampledN={4,8,12,16,24,32,48,64}, both families,180/260 dps. Exact induced row-sum formula is proved; numerical norm evaluations are MEASURED, with precision agreement, not interval certification. Independent exact Fraction derivative checks agree4416entries at N=3/4/6. Supporting local derivative and coarse allN Kraw upper-bound records are separate from the OPEN sharp-growth target.
- D2 G0PASS12/12; G1 finite threshold fails and G2 fails in HahnN8/16. Stable Lanczos marginals remain near rounding precision but layer amplification persists. Path diagnostics preserve the second-measure anchor; no full-array backward claim. See attempts/D2.md.
- D6 graph mixed-test identity is elementary background with scoped standard-grading obstructions; no faithful full NN-to-bivariate recurrence dictionary or stability transfer. The worker discloses late completion of some gate-summary reads after the prescribed probe; no retrospective prospective novelty clearance is claimed. D7 source retrieval is BLOCKED through both repository and publisher supplement routes, not reproduced.
- D3/D4/D5 and supplementary independent reports remain in progress. No scientific result is registered and Claude audit remains PENDING.

## Round1 checkpoint — D3, D4 and D5

- D3 implements direct mixed solves in an orthogonal coefficient basis and node-space constraint QR, retaining both designs and LU/QR/SVD variants. Both avoid C4 propagation; finite forward gains exceed2 digits in attainable cases, but no general new stable-algorithm theorem or novelty claim. See attempts/D3.md.
- D5 proves local gauge-fixed full-image geometry and unique nearby SPD nearest projection; a five-field dyadic certificate proves strict backward error infinite for one raw N=4LU array. Actual positive common-data correction witnesses are measured, not minima or backward-stability proofs. The original gate is preserved and a separate dated mixed metric is explicit. See attempts/D5.md.
- D4 rederives finite Christoffel transport and Toda closure, with finite boundary and normality assumptions. An exact positive three-node pair loses normality under an exterior Christoffel change and under a common exponential path. Common multipliers preserve the weight ratio and cannot reach arbitrary pairs. The predivide-C4-restore design loses at N=16 in both families and is stopped. Accurate-source transforms/flows do not solve initialization. See attempts/D4.md.
- Supplementary Astra exact checks have reproduced derivative, transform, path-diagnostic traps and the dyadic obstruction within their stated finite scopes. Final written check report and Claude audit remain pending.

## Hard conditioning step and supplementary verification checkpoint

- Astra ultra produced the self-contained parity/terminal-jet proof of the explicit all-N lower bound, including a stronger positive-coefficient sum bound with base5+2sqrt(6). A separate analytic specialization refutes the G3 O(1/d_min) prediction at fixedN>=4 as measures approach proportionality. Matching upper/sharp rate remain OPEN. Scope/failed routes retained in attempts/D1-hard.md and novelty-gate-D1-hard.md.
- Sol D1 independently reconstructed the algebra, and distinct Astra high reconstructed the final proofs and executed exact direct-moment witnesses. These supplement the still-required Claude audit.
- Supplementary reports independent-checks-01.md and independent-checks-02.md separate actual round1 and follow-up scopes. Each identifies hashes, commands, coverage and remaining limitations. Numerical projection stationarity must distinguish the optimizer from the returned rounded rational witness; developer is making that stage explicit.
- A reproducible sampled conditioning figure was rendered off Git and inspected; its code and receipt are committed. Full61-point figures await the running two-precision expansion.

## Native/projection round2 completion

- Full-Jacobian least-squares fits at N=4/8, both families, C4/LU/nodeqr,100/160 dps completed. Actual rational positive common-data witnesses were rebuilt; numerical stationarity is separated from rounding the returned witness. N=4 finite native pairs are small; N=8 does not meet100u. No global-nearest or backward-stable solver theorem is claimed.
- The independent checker reran final projection code9deb74ef at fourN4 cases, checked exact40-field moment rebuilds, and verified returned-witness stationarity. The reporting fix changes labels/added returned-stage diagnostics, not the rational witnesses or numerical pair values. Final report02 hash a4cf80cd2695c3233f49b6e1b7dc8ec6f702f925d19e4066305ba8a671bc1b23. D3/D5 close their two-round scope; general stability remains OPEN.

## Final development and main reconciliation

- All four full Jacobian runs completed every integer N=4–64 at180/260 dps, both families. The six NN/step-line input-model norm comparisons passed1e-60. Worst relative disagreements: Kraw1.7632664201e-115; Hahn1.2841742107e-93. The single61-row table, frozen commands and raw hashes are in attempts/D1.md. Timed expansion CPU5630.383305s; maximum individual wall1512.192064s, all exits0. Earlier untimed experiments are not assigned invented CPU totals.
- Coordinator executed conditioning_compare.py on the complete inputs, independently checking coverage/content identities as an integration check, not as an independent derivative rerun. It produced /tmp/conditioning-full-compare-coordinator.json, SHA977a0441f487466acb1c7d3ee4e1fadcae05bf193159d48125bca9a34b8ebc2f. The finite normality receipt verifier was also actually executed (its --help argument is ignored), PASS61/43676.
- The full61-grid PNG/PDF/SVG was generated and inspected; sampled history is retained in plot-receipt.md. No output or plot is smuggled into Git; large working artifacts remain local, with no claimed cold-storage delivery.
- Current main advanced to5adc3e2b7226e2c3c5577335058823a8e5cc3629. Topic merge e6926754cca8c9dbe0c9c75d5c350036128f115c preserves main's unrelated blobs and all existing topic blobs without rewriting history. Initial source/base provenance remains823cf6a/b4d292e; only PROOF_STATUS.md and state/IDEAS.md among initial scientific inputs changed on main. All imported NN code and rule blobs are unchanged.
- Main/open-foreign reservation refresh read44 complete ledger/registry copies at main5adc3e2, PR27c000899 and PR29 60a493a. PR29 is an unmerged rules proposal with no range; it is not applied to this task. Main's mentions of our own range are acknowledgments, not another owner's allocation. Own permanent reservation/priority is unchanged and no final IDs are assigned.
- New main PD-N118 is a related bivariate raw-array necessary-symmetry obstruction. Its full record was read at main5adc3e2. Our NN B2 dyadic witness is a separate scoped instance of the same general exact-consistency mechanism, with no historical novelty claim or proof dependency. See the integration addendum in novelty-gate-D3-D5.md.
- All direction outputs and supplementary reports are complete within their declared bounds; G5 remains objectively blocked. Development passes to mandatory Claude Opus 5.5 xhigh audit in [handoff02](handoffs/02-audit.md). The scientific output SHA will be that handoff's input SHA, distinct from its publication commit. Only AC merges.

## 2026-11-06 — Claude, Opus 5.5 xhigh — independent audit-01

- Rules read at `680dca3`; merged current main `be9a831` (PR #29 proportionate-audit rules; no topic file changed) at `67248ce`, and those rules apply from here. Audited scientific candidate `ff783d59587100ab291cb83d690ef27a09f0f154`, byte-identical to the head for every audited file.
- Orchestrator audited priority 1 (lower bound, proximity theorem, exact coefficients). Five Claude Opus xhigh subagents audited disjoint scopes (A: priority 2; B: 3–4; C: 5–7; D: 8–10; E: novelty/status/records, full `state/IDEAS.md`). All reran developer commands and wrote independent exact code; scripts in [audit-01/](audit-01/README.md). Raw outputs stayed local and are regenerable, with no archival claimed.
- Key independent reruns:
  - the full 61-size conditioning table at 180/260 dps, both families, regenerated byte-identically (0 of 244 cells differ);
  - G0 12/12 bit-identical, with the G1/G2 values reproduced;
  - Hahn normality at all 61 sizes re-certified by independent mod-p and exact recursion code;
  - the dyadic residual reproduced exactly;
  - native, projection, D4 and D6 values reproduced, with platform differences in some binary64 values;
  - G5 network block confirmed (CONNECT 403).
- Verdict [audit-01](audit-01.md): no BLOCKING; every claimed status within scope is supported. MAJOR:
  - M1: dictionary-obstructions proof arithmetic;
  - M2: undisclosed platform dependence; Krawtchouk N4 nodeqr η_c 30.78u breaks the stated ≤30u;
  - M3: rational projection witnesses neither committed nor hash-pinned;
  - M4: handoff01 D3 candidates (a)–(c) and the D1 alternatives unrecorded.
  - Also 16 MINOR items and several notes. Stage → WORK; the response's material changes get a focused re-audit.
- AC 2026-11-06: storage is a separate cleanup topic; take no cleaning action while the material stays under 10 MB. The topic is 0.58 MB committed; recorded as a NOTE only.
- Handoff: [handoffs/03-response.md](handoffs/03-response.md).

<a id="2026-11-06-ac-decisions"></a>

## 2026-11-06 — AC decisions (canonical record) — Claude orchestrator

- AC: "G5: access is allowed. Gates are OK."
- **G5.** AC authorizes retrieving and running the public IEP-MOP code and the SIAM supplement for G5. Claude created the personal environment `padua_research` (allowed hosts gitlab.kuleuven.be, epubs.siam.org, arxiv.org) and switched this session's network to it.
  - Observed at 08:02–08:05 UTC: arxiv.org 200.
  - The SIAM supplement ZIP returned 403 with a Cloudflare bot challenge, a site-side refusal; it was not bypassed.
  - The GitLab tunnel first got CONNECT 403, then opened but closed after about 10 s (`ws_closed_mid_exchange`), so no source was retrieved. G5 is no longer blocked by policy; execution is still pending.
- **Gate deviations.** AC accepts the D6 gate-timing deviation (final alias/summary coverage completed after the prescribed background probe; novelty-gate-D6-D7.md) and the post-run prospective record of D4-C1a (its prospective record was written after its first run; novelty-gate-D4.md) as disclosed. This is the canonical record for audit-01 MINOR 9. It grants no retrospective prospective clearance or novelty claim.
- Redirection: handoff03 superseded by [handoffs/04-response.md](handoffs/04-response.md), which adds G5 as step 6.

## 2026-11-06 — Codex response to audit-01 — requested gpt-6.1-sol high

- Rules and inputs read at `4e87fc0a771fc13c6d5791f0f4c2e746e4eb9a71`; current main/base `be9a8318150204711d5446d2ea26284cf1ed0819` is already an ancestor (ahead14/behind0 at session start). Runtime serving identity/effective effort are not independently exposed. Disjoint record and G5 access helpers used requested gpt-6.1-sol medium. [Pinned source inventory](response-01/source-inputs.json). No new mechanism generation: the task corrects audit findings and preserves five already named deferred candidates, so no new conceptual novelty gate is claimed.
- [Response01](response-01.md) answers M1–M4 and MINOR1–16. Corrected dictionary arithmetic; scoped platform-dependent binary64 claims; split G/C obstruction records; restored OPEN parent targets; retained all deferred alternatives; expanded the localized NN lemma and continuity argument; made the exact verifier enforce source pins with explicit exceptions. No final IDs/shared registries or auditor-owned files changed. Existing edited prose pins are refreshed in the same output commit.
- M3: original Nov5 temporary witness files are unavailable here. A fixed, untuned160-dps rerun creates a clearly dated new response reference, not recovery of historical bytes. The committed113,095-byte JSON pins all12 complete N4/N8 targets and rational witnesses. The checker reads this committed identity without running the optimizer. [Evidence and limitations](evidence/README.md).
- Actually executed dictionary probe (determinant46, moments and solution agree); normality verifier (61 sizes/43,676 checks, all source pins); projection export and separate exact checker (12 cases/1,104 coefficient fields/348 normality systems, six N4 gradient checks). Corrupted payload and source pin fail normally and under Python-O; changed projection reference fails under-O. [Check receipt](response-01/checks.json). These response runs are developer verification, not independent actor approval; no conditioning sweep or algorithm retuning was needed.
- G5 remains technically BLOCKED in this executor after the authorized retry: enabled-network GitLab Leuven/SIAM/arXiv GETs receive proxy CONNECT403, while Debian control succeeds; bounded public web routes expose no source archive. [Actual attempts](response-01/g5-access.md). No source retrieved, external runtime installed, external algorithm executed, or reproduction claimed. No access-control bypass, storage cleanup or Leuven contact.
- Stage → AUDIT for focused material-change review and full review of the new G5 access attempt; earlier accepted claims remain as supported by audit01. The conditioning-growth and general stable-solver targets remain OPEN. No readiness/merge request. Only AC merges.
- Handoff: [handoffs/05-reaudit.md](handoffs/05-reaudit.md), using the next unused number because04 is the current response handoff; its numbering typo is not copied.

## 2026-11-06 — Claude, Opus 5.5 xhigh — audit-02 (focused re-audit and G5 review)

- Rules read at `409e779`; merged main `f654e32` (PR #30; no topic file changed, and the rules are unchanged) at `8a2b65d`. Audited response output `d6760d7d593ea7e14eb9860f92ef2f3b5e0481d6`.
- Three Claude Opus subagents (R1–R3) audited disjoint scopes. The orchestrator reran the three prescribed checks, plus a `-O` rejection test, and reviewed G5. Scripts: [audit-02/](audit-02/README.md).
- [audit-02](audit-02.md): response-01 ACCEPTED; no BLOCKING or MAJOR. Stage → PR.
  - All 12 committed projection witnesses were rebuilt exactly, every stored metric matching with relative difference 0.
  - The localized lemma was reconstructed and tested exactly.
  - Checker rejection paths fail as required.
  - All 55 manifest rows match.
  - New MINOR R-1 to R-8 go to preparation. They include restoring the D6/D4 gate chronology dropped by the MINOR 9 consolidation, and marking the undated parentheticals that response-01 inserted into the AC-decision entry above as Codex text.
- G5 access at 09:19 UTC from the `padua_research` environment:
  - GitLab: the upstream reset the TLS handshake;
  - SIAM: Cloudflare challenge, not bypassed;
  - arXiv: the source bundle (`f736e8f0…`) holds the paper's experiment-1 data but no code.
- AC 10:14 UTC uploaded `IEP-MOP-main.zip` (SHA-256 `cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145`, MIT licence), which removes the source blocker. It is not committed.
- Because only this Claude session can reach the upload, the G5 run is assigned as a Claude development step, technical row: Sonnet 5.5 high. Codex audits it, then prepares the PR; Claude performs the readiness check.

## 2026-11-06 — Claude (Sonnet 5.5 high developer, Opus 5.5 xhigh orchestrator) — G5 run

- The source is AC's upload (`cdd0e98d…`), with reference values from the arXiv source bundle (`f736e8f0…`); neither is committed. Octave 8.4.0 installed from the Ubuntu apt mirrors. A headless replica driver of `experiment_Hahn_Kravchuk.m` runs N=5..30 for both families, with no edits to the third-party code.
- Pre-stated gate: Krawtchouk, paper N=10 (11 nodes in this topic's convention), IEP_CORE, |log10(ours/paper)| ≤ 1. **PASS**: 1.772147e-09 against the paper's 6.851191e-10, +0.41.
- Full table: 6 of 144 entries at N ≤ 16 exceed one decade, by ≤ 0.62 beyond it. Exceedances are frequent at N ≥ 17, where the paper reports that all digits are lost. The qualitative pattern matches. The orchestrator's re-execution was byte-identical. Receipt: [g5-run/README.md](g5-run/README.md). MEASURED; Codex audit pending.
- Handoff: [handoffs/06-g5-audit-prep.md](handoffs/06-g5-audit-prep.md).

## 2026-11-06 — Codex, requested gpt-6-astra medium — independent G5 audit

- Rules read at full source `414e781567078560b7e233aace3661abb88e37ab`; main `f654e32daff27b6846849311092f6daebbbf235b` is the merge base (ahead20/behind0). Requested medium ordinary technical audit; serving identity/effective effort not independently exposed. User supplied the Leuven ZIP to this executor; it matches the source used by Claude exactly. No new mechanisms/novelty claim, so no conceptual-generation gate is required.
- Read current handoff06 and accepted audit02. [G5 audit](audit-g5-01.md): ACCEPTED within finite scope, one MINOR enumeration omission fixed with dated attribution in a separate commit. Independently read all executed third-party files, checked their hashes and reran the full driver with isolated Octave9.4/reference BLAS on Debian13. Exit0;52 family/size cases,15.81s. Gate Krawtchouk paperN10 error2.691214553706643e-10, log10 ratio-0.4058 against the developer-quoted paper6.851191e-10, hence PASS. Entire tables vary across platforms; no all-case/platform agreement asserted.
- arXiv reference bundle remains inaccessible to this executor (CONNECT403); direct paper-table/hash verification and re-execution of cmp.py against that bundle are explicitly unresolved. Independent source execution occurred; paper reference-data comparison is review only. [Auditor receipt/outputs](audit-g5-01/receipt.json). No third-party source/data committed, access-control bypass, Leuven contact or storage cleanup.
- PartB preparation proceeds under handoff06. Bounded Solmedium helpers check reservations/record hygiene; a Solhigh helper prepares statement-bearing registry rows after reservation clearance. Root alone publishes. Existing scientific statements/results/statuses remain as independently accepted; sharp-growth/general stable-solver targets stay OPEN. PR28 stays draft; Claude readiness remains required. The approved connector noreply-author exception persists.
