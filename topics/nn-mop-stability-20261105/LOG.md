# NN MOP IEP: conditioning and stable algorithms: log

- Branch: `codex/nn-mop-stability-20261105` · Base: main `b4d292e` (PR #21 merged) · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: WORK · Next: `Codex (gpt-6-astra high): Continue codex/nn-mop-stability-20261105.` · Open handoff: [handoffs/01-work.md](handoffs/01-work.md)
- Reserved final-ID ranges: T432–471, N162–177, IDEA530–569, LIT614–629; reservation only, no assignments. See ALLOCATIONS.md.
- Claims: none yet.
- Open for AC: none at setup. Ask AC before using Syvert.

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
- Refreshed main/all open PR24/27 and all 44 ledger/registry copies; no closed-unmerged PR. [Reservation](ALLOCATIONS.md) is strictly above unionT431/N161/IDEA529/LIT613, including permanent gaps. No final assignment/shared-registry change.
- Current outputs are development in progress. Audit PENDING. Only AC merges.


- Snapshot transport correction: the initial materializer appended one extra final LF to each fetched file. Restored all222 unchanged inputs byte-for-byte (the topic LOG is already being updated) against their pinned Git blob SHA before final evidence collection; this changes no scientific content. Initial replay values matched exactly; code-hash receipts are refreshed after correction.

- Operational clarification: default shell sandbox networking could not reach the proxy; explicitly enabled-network execution reaches GitHub but has no CLI credentials. The connector is authenticated. AC explicitly allowed its verified GitHub noreply author address for this campaign, resolving handoff01's email requirement. Setup/reservation first published as d87925630e9e460031df319f3994ca2e7fad8ca0; draft PR28 opened. Refreshed peer heads PR27 3dda890 / PR24 0299fcf: no reservation change or collision.
- Astra ultra escalation justification (D1 hard step): the sampled induced condition norms grow by many orders while the requested all-N growth law remains unresolved; a bounded independent analytic lower-bound attempt is a decisive hard mathematics step, not a fit or routine table generation. A separate Astra ultra worker owns only D1-hard files and cannot replace Claude audit.

## Round1 checkpoint — D1, D2, D6 and D7

- D1 sampledN={4,8,12,16,24,32,48,64}, both families,180/260dps. Exact induced row-sum formula is proved; numerical norm evaluations are MEASURED, with precision agreement, not interval certification. Independent exact Fraction derivative checks agree4416entries atN3/4/6. Supporting local derivative and coarse allN Kraw upper-bound records are separate from the OPEN sharp-growth target.
- D2 G0PASS12/12; G1 finite threshold fails and G2 fails in HahnN8/16. Stable Lanczos marginals remain near rounding precision but layer amplification persists. Path diagnostics preserve the second-measure anchor; no full-array backward claim. See attempts/D2.md.
- D6 graph mixed-test identity is elementary background with scoped standard-grading obstructions; no faithful fullNN-to-bivariate recurrence dictionary or stability transfer. The worker discloses late completion of some gate-summary reads after the prescribed probe; no retrospective prospective novelty clearance is claimed. D7 source retrieval is BLOCKED through both repository and publisher supplement routes, not reproduced.
- D3/D4/D5 and supplementary independent reports remain in progress. No scientific result is registered and Claude audit remains PENDING.

## Round1 checkpoint — D3, D4 and D5

- D3 implements direct mixed solves in an orthogonal coefficient basis and node-space constraint QR, retaining both designs and LU/QR/SVD variants. Both avoid C4 propagation; finite forward gains exceed2digits in attainable cases, but no general new stable-algorithm theorem or novelty claim. See attempts/D3.md.
- D5 proves local gauge-fixed full-image geometry and unique nearby SPD nearest projection; a five-field dyadic certificate proves strict backward error infinite for one raw N4LU array. Actual positive common-data correction witnesses are measured, not minima or backward-stability proofs. The original gate is preserved and a separate dated mixed metric is explicit. See attempts/D5.md.
- D4 rederives finite Christoffel transport and Toda closure, with finite boundary and normality assumptions. An exact positive three-node pair loses normality under an exterior Christoffel change and under a common exponential path. Common multipliers preserve the weight ratio and cannot reach arbitrary pairs. The predivide-C4-restore design loses atN16 in both families and is stopped. Accurate-source transforms/flows do not solve initialization. See attempts/D4.md.
- Supplementary Astra exact checks have reproduced derivative, transform, path-diagnostic traps and the dyadic obstruction within their stated finite scopes. Final written check report and Claude audit remain pending.
