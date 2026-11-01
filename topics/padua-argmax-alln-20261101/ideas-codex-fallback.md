# Fallback candidate records — 2026-11-01

Rules/input snapshot `328be35e55143013047ec03a70e9906e82b95353`. Codex, parent-assigned gpt-6.1-sol xhigh; runtime model metadata not independently exposed. This file supplements original [ideas.md](ideas.md); original wording and criteria remain there unchanged. Operational definitions and recorded pre-run sequence: [P3–P5/pairing attempt](attempts/P3-P5-and-pairing.md).

These are implementations or restrictions of existing IDEA03/IDEA305, without a new priority claim. Topic gate and parent campaign gate provide the complete baseline; local scoped reading covered the plan/gate/ideas, IDEA-048/206 registry descriptions and full part2 IDEA303–305 route registration, with the relevant existing obstruction tables. The literature INDEX is read; original 1-D sources remain unread. No source technique is transferred.

## IDEA?argmax-alln-codex-fallback-01 — O-R whole-diamond monotonicity

Aliases: unique-nearest-corner ordering; mesh-distance rhombus comparison.

- Question / scope: for every n≥2, do whole-diamond suprema M_a decrease for every (±1,±1) step away from the same unique closest non-node corner, in Euclidean mesh distance?
- Mechanism and hypotheses: exact comparison of adjacent cell suprema; diamond cells and corner metric fixed in the attempt. This is one reading of ambiguous original IDEA03.
- Closest registry entries: original IDEA?argmax-alln-claude-03; IDEA-048 geometry context; IDEA-206 target; IDEA-305 exact edge phase/defect mechanism.
- Separation criterion: replaces the undefined cell/order in IDEA03 by a concrete neighbor graph and whole-cell comparison, without asymptotics. A reversed adjacent pair kills this formulation; changing the graph after a reversal would be a separate candidate.
- Literature baseline/search limits: original Brutman/Günttner sources not read; no claim that they imply this order.
- Applicable obstructions: the shifted-lattice majorant S can exceed Λ_c, so comparison must control λ or its defect. Sampling does not upper-bound cell suprema.
- Novelty gate verdict: **variant of existing IDEA03** (operationalization), no novelty claim.
- Cheapest decisive test: multistart diamond maxima at n4,7,12, with exact entire-source-cell upper bounds needed for a certified refutation.
- Kill criterion written before testing: float reversal>10^−6 kills pursuit in this numerical screen; only a certified source upper bound plus target lower bound would establish exact failure.
- Test discriminability: float differences here exceed threshold by up to1.63, but a missed source maximum remains a limitation.
- Actual result:6/10,16/42,60/130 reversed comparisons at n4,7,12; interior-center reversals already at n7. [Measured record06](theory/argmax-alln-codex-06-measured-pairing.md), [output](outputs/part3/pairing_screens.json).
- Disposition: **REJECTED: failed** as this measured screening route; exact negation remains unproved. Ambiguous IDEA03 remains OPEN.
- Canonical result: PD-T?argmax-alln-codex-06 (MEASURED); no PD-N for an exact O-R assertion.
- History: operationalization written before optimizer execution; retained after screen.

## IDEA?argmax-alln-codex-fallback-02 — O-L and O-Lt certified-list pairing

Aliases: local-maxima-only grouping; tie-inclusive cut-locus comparison.

- Question / scope: replace whole-cell M_a by V_a, the greatest value among strict interior local maxima from the complete certified list located in D_a. For O-L require the same **unique** closest corner at both centers; for O-Lt permit a shared closest corner with ties.
- Mechanism and hypotheses: pair selected local maxima along the same rhombus neighbor graph. Whole-diamond artificial-boundary suprema are excluded; empty groups remain undefined.
- Closest entries: original IDEA03, previous fallback-01, IDEA-048, accepted n4 count/global PD-T165/166.
- Separation criterion: exact inherited coordinate/value certificates replace numerical optimization; it is narrower in the compared objects but broader at the cut locus than tie-excluding O-L. A reversed exact grouped pair kills only its specified order.
- Literature baseline/search limits: no 1-D theorem used; originals not read.
- Applicable obstruction: a complete list of local maxima on the physical square does **not** certify whole-diamond suprema. This restriction is essential to the statement.
- Novelty gate verdict: **variant of IDEA03**, separately specified restriction, no priority claim.
- Cheapest test: rationally assign all13 n4 interior roots to diamonds; compare inherited rational value enclosures.
- Pre-run sequence and kill criterion: O-L's unique-corner rule was written before the first grouping; grouping produced zero eligible neighbor comparisons. The attempt then added O-Lt as a separate dated formulation **after reading that grouping and the certified values but before executing the tie-inclusive comparison**. Its exact kill criterion is max(lower in b)>max(upper in a), with all coordinate assignments checked. This is an informed followup, not a blind pre-registration.
- Test discriminability: rational Machin/Taylor checks verify coordinate enclosures, and the positive rational difference is decisive conditional on accepted inherited completeness/root-value certificates.
- Actual result: O-L at n4 has zero eligible comparisons and remains untested. O-Lt has6 eligible comparisons and2 reversals, including a=(3,2),b=(2,1),c=(4,5) with reversal>.06322. Exact standard-library checker developer PASS; independent checker replay and separate rational reconstruction PASS.
- Disposition: O-L **deferred** (no eligible n4 test; resume at n7 with coordinates). O-Lt **REJECTED: refuted** in the exact finite scope, independently checked; required Claude audit pending. No universal rejection of original IDEA03.
- Canonical negative result: [PD-N?argmax-alln-codex-01](theory/argmax-alln-codex-N01-pairing-order-obstruction.md), PROVED development result with independent exact checks, required Claude audit pending.
- History: ties were not silently added to O-L after observing a failure; both formulations and their actual sequence are preserved.

## IDEA?argmax-alln-codex-fallback-03 — E-C centreward vertical-edge order

Aliases: parity-preserving step2 edge comparison; amended IDEA03 edge version.

- Question / scope: on each vertical edge, do whole complementary cells [k−1,k+1] excluded from endpoint corners have nondecreasing suprema under step2 moves toward (n+1)/2?
- Mechanism and hypotheses: compare edge-cell maxima at fixed n, ultimately reducing noncorner edge values to the central envelope PD-T192. Endpoint/corner cells must still be handled by P3. This preserves a later suggestion in the plan and differs from original away-corner order.
- Closest entries: original IDEA03's dated centreward update, IDEA303/305, PD-T185–192.
- Separation criterion: an exact all-β comparison at each fixed n would avoid effective remainders for locating the edge runner-up; an exact reversed adjacent edge-cell pair kills E-C. Pointwise phase pairing E-P is stronger and is kept separate.
- Literature baseline/search limits: no transfer from unread 1-D sources.
- Applicable obstructions: numerical edge optimization can miss sign-cell extrema; central asymptotics alone give no exact comparison at fixed n.
- Novelty gate verdict: **variant of original IDEA03's centreward update**.
- Cheapest test: 65-point grid per whole edge cell plus local scalar refinement; then exact sign-cell root enumeration at n7.
- Kill criterion before testing: target-minus-source<−10^−6 is a measured reversal. Exact proof requires enclosure of every candidate and endpoint.
- Actual result: no reversal among76 comparisons at n7,12,24,50. n4 has no eligible pair. Minimum observed adjacent gains shrink from.3800 to.00356.
- Disposition: **active; OPEN**. Next exact task: enumerate whole-cell candidates at n7, compare intervals, then test a common-phase pointwise inequality E-P independently. No E-P run was performed here.
- Canonical evidence: [measured record06](theory/argmax-alln-codex-06-measured-pairing.md).

## IDEA?argmax-alln-codex-fallback-04 — retain defect domination without raw gap convergence

Aliases: P4/P5 sufficient inequalities; phase-localized positive defect.

- Question / scope: can primitive-majorant phase localization and a uniform positive defect prove fixed-δ interior/strip gaps without an n-independent raw O(1) gap limit?
- Mechanism and hypotheses: outside a coset phase neighborhood S≤Λ_c−d; inside it S≤Λ_c+ε_n and Δ≥2d with ε_n≤d. Cover corners/interior/strips as specified in the attempt.
- Closest entries: IDEA305/PD-T189–192, original IDEA02; exactly their all-regime extension.
- Separation criterion: allows n-dependent/growing raw gaps, escaping T2's rejected raw convergence formulation. If the required defect lower bound or primitive excess control fails, these sufficient hypotheses fail; no new theorem is inferred.
- Literature baseline/search limits: no new transferred technique or literature claim.
- Applicable obstructions: S alone overshoots Λ_c; edge-only uniformity does not imply two-angle or transition-zone uniformity. T4's crude constants do not give a feasible threshold.
- Novelty gate verdict: **variant of IDEA305**, conditional reduction only.
- Cheapest next test/kill criterion: measure Δ and S−Λ_c separately near the odd coset throughout a fixed-δ interior and strips; a witnessed defect below2d or excess above d kills the chosen quantitative trial. Choose d, neighborhoods and finite grids before any new run.
- Actual results: no new quantitative run of this formulation; parent T2/T3/T4 outcomes motivate the distinction but do not establish its hypotheses.
- Disposition: **deferred, OPEN** until an explicit phase estimate and uniform defect hypothesis are specified. P3 still requires a local sign/radius proof and original 1-D reading first.
- Canonical record: conditional obligations in [the attempt](attempts/P3-P5-and-pairing.md); no new theorem/negative ID.
