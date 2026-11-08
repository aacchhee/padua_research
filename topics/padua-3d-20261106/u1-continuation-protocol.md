# U1 continuation: prospective operational decision protocols

2026-11-07. Developer Codex, assigned gpt-6.1-sol high; runtime metadata is
not independently exposed. Input/rules97c323bfae15cf3c76f40802c3ebabedceeb0c60.
AC authorizes up to seven further U1 rounds, separately from U2/U3; ceilings
are not spending targets. Existing U1 completed count2. API repair/checks0.
Root publishes this protocol before dependent execution and owns counters.
No new node mechanism, historical novelty or final ID is claimed.

## Reading, gate and closest records

Personally read full AGENTS/WORKFLOW/CODEX, handoff13, usable1, recipes,
current U1 recipe/noise/OLS proofs, the full shared usable-gate and full
interim U1/strategy reports, and original independent stress source.
The shared gate's complete1154-line registry and all-table read is attributed
to its worker; this continuation does not claim a new personal complete
read. Its recorded registry SHA256d7ec3aa6cf36f72e8057bcb90d8ac6eae8bf285a5b17f12526b26472ff4bddef
is unchanged at this input. Personally searched `state/IDEAS.md`,
`literature/INDEX.md`, programme candidate records and current U1 records
for least-squares/hyperinterpolation, replication, noise, budget,
A-optimal/optimal-design, ridge/regularization. Full closest IDEA208/209
bodies and the relevant108–117/402–442/508–517/776–787obstruction/
disposition ranges were read; the full shared gate controls broader scope.
Initial broad search/truncated combined reads are discovery only. No new
PDF/source coverage or exhaustive literature claim is made.

Known least squares, weighted MZ and design framing already overlap
IDEA026/055/074/075/076/208; QR extraction is IDEA027 and current T9/T10.
Square reweighting does not change interpolation. Positive projection does
not imply minimal interpolation. All following work is explicit finite
operational extension of these known routes; no fresh mechanism is proposed.

## IDEA?padua-3d-20261106-U1c-01 — degree/noise decision at a feasible budget

Aliases: fixed-observation risk envelope; integer replication with degree
selection; calibrated Chebyshev sensor-field example.

- Question/scope: how should degree, fixed linear solver and distinct-site
  family be chosen when observations are costly and repeat measurements
  are feasible? Assume product-Chebyshev probability prediction measure,
  637independent observations, equal cost per observation, no additional
  site-opening charge, arbitrary polynomial degree inside that budget.
  Each used site receives at least one observation. These are illustrative
  assumptions chosen here, not supplied facts about the user.
- Mechanism: existing anisotropic Haar/OLS at every degree1..12; unchanged
  globalQR at every degree1..13; stored optimized U2 degree12. Exactly38
  designs. Haar13 and QR14 exceed637sites and are ineligible by count.
  Values averaged over r_j independent mean-zero observations each of
  variance sigma²; sigma is known in this hypothetical calibration.
- Closest full records: usable1 C1/C2, U1 recipe/noise/OLS, interim U1 audit
  and its exact-model integer-allocation implementation. No mechanism
  separation; finite coverage differs by evaluating feasible lower degrees
  and complete target bias plus noise rather than a fixed equal degree.
  Prior complete degree/noise risk tables at this budget erase that limited
  coverage distinction; they would consolidate this record as equivalent.
- Gate verdict: known variant with an operational difference; no priority.
  No signed-weight or uniform-measure inference. Gram/reproduction needed
  before quality, and degree2n−1 cubature alone is insufficient.
- Cheapest decisive test: for each design verify M<=637, finite map and
  reproduction infinity residual<=1e−9. Reject an ineligible design without
  repairing it or assigning quality. Check integer allocation on small
  brute-force examples first. Keep all invalid cases explicitly.
- Allocation: hold each original noiseless coefficient map C fixed, set
  a_j=||C[:,j]||² and start r_j=1. Greedily add each remaining observation
  at the first maximizer of a_j/[r_j(r_j+1)]. Decreasing marginal reductions
  make this the optimum for this fixed-map separable integer objective.
  This is not joint optimization of replication and a re-fitted GLS map.
- Frozen functions: original4targets plus all8interim targets, with the
  omitted mode fixed to sqrt(2)T13(x), independent of each design's degree.
  Explicit audit targets: exp(10(x−1)), exp(10(z−1)), off-centre Gaussian
  exp(−((x−.23)²+(y+.11)²+(z−.37)²)/.04), tanh(12(x+.23y−.41z−.07)),
  abs(x−y+.02z−.15), cos(11x+7y−4z), 1/(1+40(1−x)). Preserve every target.
  Primary assumed field is exp(10(x−1)); Gaussian is the secondary case.
- Assessment: two independent scrambled Sobol angle clouds, each2^15
  points, seeds2026110711/2026110712, transformed by cos(pi*u). Build all
  maps before assessing. No fitted parameters depend on either cloud.
  Empirical squared bias b² plus exact-model sigma² sum_j a_j/r_j estimates
  total integrated expected squared error. sigma=[0,1e−5,1e−4,1e−3,.01,.1,1].
  Compute every candidate's outcome, each cloud's minimizing candidate,
  and the other cloud's regret for the first cloud's recommendation.
- Practical gate: at least one primary noise setting must have a nontrivial
  low-bias winner and a different noise-sensitive winner, with a5percent
  total-MSE gain over using degree12Haar throughout, and recommendations
  from the first cloud must incur at most5percent regret on the second.
  This tests whether calibrated degree selection matters, not whether U1
  wins every target. Preserve exact ties/machine-floor cautions.
- Stop/resume: if practical gate fails, park this assumed scenario; do not
  add seeds/degrees to obtain a win. If it passes, a distinct next round
  may test known noise-aware GLS after integer replication, or the cost
  of an explicitly changed measure/noise model. No automatic repeated suite.
- Costs: record actual process CPU, construction and assessment times,
  dense map sizes and single-thread environment. Each construction capped
  at120CPU seconds at operation boundaries; whole run600CPU seconds.
  A cap yields an unfinished retained result; no convergence claim.
- Evidence: compact receipt below16KiB retaining all design/target outcomes;
  raw fullprecision maps, counts, coefficients and detailed decisions in
  a unique/tmp directory, regenerate-only. Code and actual input hashes,
  versions, commands/seeds and any unrun work are recorded.

## Round ledger and runs needed

U1 continuation round1 (global U1 round3) executed after publication in
cb014092e71d16b77c7c2651363440d7b078eab6. Its practical gate passed;
all38designs eligible, all12x7decisions agree between the two clouds.
Root's pushed output checkpoint, not this prose, controls the counter.


## IDEA?padua-3d-20261106-U1c-02 — re-fit GLS after feasible replication

Prospective continuation round2/global U1round4, drafted only after round1's
positive degree/noise decision. No round2 execution is implied here.

- Aliases/question: noise-aware refitting; GLS of replicate averages;
  does applying the known correct covariance model improve the already
  calibrated degree/noise decision enough to justify a different map?
- Mechanism/hypotheses: same B637, nodes, measure, twelve targets, seven
  noise scales and equal iid single-observation variance. For each of the
  24Haar/OLS degree1..12cases, freeze its exact stage1 integer allocation
  r_j; fit weighted QR on sqrt(r_j)V, giving
  C_star=(V^T R V)^−1 V^T R. This is known GLS, not new design theory.
  Reusing both allocation schedules retains possible duplicates honestly.
- Closest full records/gate: same known-route gate and U1c01, plus the
  existing right-inverse covariance proof. The change is refitting after
  unequal replication, which U1c01 explicitly excluded. For a square
  interpolant refitting cannot change the map; all14QR/stored controls
  remain. No new physical node or untested asymptotic claim.
- Cheapest decisive test before quality: verify all24reproduction
  residuals<=1e−9 and weighted covariance identities. Put S=diag(1/r),
  D=C−C_star. Reproduction gives DV=0 and S C_star^T=V(V^T R V)^−1,
  hence C S C^T−C_star S C_star^T=D S D^T. Check its infinity residual
  <=1e−9 and risk_star<=risk_old+1e−10; invalid cases retained without
  quality/repair. This is the elementary existing BLUE argument in its
  stated covariance; no new substantive theorem/priority claim is proposed.
- Assessment: freeze all24maps before evaluating. Evaluate every original
  38map plus every eligible refit (62total) on two fresh32768-point Sobol
  angle clouds with seeds2026110713/2026110714. All source arrays and the
  first-round receipt are hash-pinned. Stage1clouds are not used for
  assessment or fitting; all targets/regressions remain in the pinned raw
  output, with compact receipt coverage described below.
- Practical gate/kill: compare the best total-MSE choice among the24refits
  plus38originals against the strongest old38at each sigma. Require at
  least5percent total-MSE gain for the primary boundary layer or secondary
  Gaussian at one noise setting, and <=5percent second-cloud regret for
  first-cloud primary/secondary recommendations. If this fails, park this
  fixed-allocation refit route; no repeated seeds or extra degrees merely
  to obtain a win. Covariance improvement alone is insufficient.
- Costs/evidence:120CPU-second per-map operation-boundary cap and600CPU
  whole-run operation-boundary cap, checked through final assessment block;
  honest partial output on cap. Record complete construction/assessment
  process-CPU time, descriptive wall time with possible concurrent untimed
  workers, environment/hashes/commands, full raw inventory and compact
  <16KiBreceipt. Save all24new rows of bias/noise, original38construction
  metadata by source receipt reference, and both fresh complete baseline
  lower envelopes (all12targets/sevennoise values), with every original
  fresh individual bias retained in hash-pinned raw arrays. All62maps are
  freshly assessed; compactness does not impute original-cloud bias to new
  points. No splitting
  to evade size limits. Stage1raw is regenerate-only and can be regenerated
  by its pinned driver; missing raw is not an archival promise.
- Resume after outcome: if material total-error gain survives, consider a
  separately registered site-level variance-floor/correlation calibration
  stress rather than assume independent repeats apply to physical sensors.
  If gain fails, stop this refit route and retain round1's useful decision
  endpoint; the broad weighted-design question remains OPEN.


2026-11-07 interpretation clarification before C2 execution: every bias
entry uses the known noiseless test function, so the resulting degree/noise
choices are oracle calibration benchmarks. Known sigma alone does not
identify bias for an unknown field. Real deployment needs justified prior
calibration or held-out measurements; no data-only automatic selector or
unseen-target model-selection guarantee is proposed. Agreement of two
query clouds tests numerical integration stability on the same functions.

(This paragraph was first committed with the C2 outcome in 0a98cea; it changes no registered gate, threshold, comparator or seed.)


## Executed continuation outcome ledger — 2026-11-07

U1c01/global U1round3: all38eligible, practical gatePASS, two fresh clouds;
see [results](u1-continuation.md) and [receipt](evidence/u1c-budget.json).
U1c02/global U1round4: all24GLSvariants eligible/all62freshly assessed,
practical gateFAIL, max primary/secondary MSE improvements1.64528/.758489
percent (<5). Stop this fixed-allocation refit route as preregistered;
[receipt](evidence/u1c-gls.json). No repeated seed/degrees or changed noise
model were run. New completed outcomes2/7, five unused; API/checks0.
Root publishes actual counters. No further U1 scientific run is planned
without a new stated quantitative need; the broad direction remains OPEN.
