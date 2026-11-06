# D4 candidate ledger

2026-11-05, Codex dispatched gpt-6.1-sol xhigh. Local IDs provisional. Source 823cf6a4; base b4d292ee. Round 1 only. The prospective broad gate is `novelty-gate-D4.md`; implementation refinements are dated there. Registry and source coverage is documented there and in `literature-D4.md`. No candidate in this ledger establishes a stable arbitrary-input NN solver.

## IDEA-541 — common Christoffel transport (D4-C1)

Aliases: common spectral change; Darboux; finite NN ratio update.

- Question / scope: given the entire source normal NN triangle, transport both measures by x-c with finite-support boundary handled correctly.
- Mechanism and hypotheses: invariant Dtilde_nu=(-1)^|nu|P_nu(c)D_nu, evaluation-ratio recursion, h-ratio a update and subleading-coefficient b update. Both source and target triangles must be normal; c avoids support.
- Closest registry entries (read in full): IDEA-193 common Toda/qd measure modification, IDEA-378 coupled invariant requirement, IDEA-379/PD-T289 NN reconstruction; predecessor candidates C2/C4. LIT-567/568 are closer published transform baselines.
- Separation criterion vs closest entry: finite terminal formula and a bounded tested transport from supplied coefficients; a claim of a new common-transform algebra is falsified by the literature and is not retained. A stable IEP-solver distinction would require an effective source-data construction and measured gains beyond C4; that distinction is unestablished.
- Literature baseline and search limitations: common transforms and transformed NN algorithms are known; partial primary coverage listed in literature-D4. No priority claim.
- Applicable obstructions and exact hypotheses broken: source supplied explicitly avoids pretending equal initial measures are normal. Terminal successor is F, no degree N+1 reconstruction. Positivity alone still fails mixed normality (D4-02).
- Novelty gate verdict: variant with difference only in finite boundary/implementation bookkeeping; exact transformation is duplicate prior algebra.
- Cheapest decisive test: exact N4 Fraction comparison with moment-reconstructed target and determinant/polynomial identities.
- Kill criterion written before testing: any exact formula mismatch blocks floating implementation; the supplied-array transform alone cannot earn a full solver claim.
- Test discriminability: exact matching distinguishes a wrong update/boundary from the intended finite transform for the tested small cases; written proof handles the general stated domain.
- Resources / cost ledger: O(N^2) arithmetic/storage after source coefficients; constructing them is an additional cost. Float transport has ratio denominators and cancellation diagnostics, not a conditioning guarantee.
- Actual test results and committed evidence: 80 coefficient fields and 30 determinant identities at N4 both families passed. Isolated rounded-reference transport has E<=3.83e-15 over N4,8,12,16. Code and receipts in attempts/D4.md; high-precision references converged at 140/220 digits within 1.53e-121.
- Disposition and precise rejected scope, if any: retained as a bounded supplied-array tool; new transformation novelty claim equivalent to existing work; general stable solver OPEN.
- Disposition reason: equivalent algebra, with explicitly scoped finite implementation retained; no PD-N for equivalence itself.
- Canonical theory / negative-result ID: PD-T443; failed solver subcandidate below has separate PD-N.
- Topic / audit / history: round1; exact code frozen at SHA256 59043e6e...; independent check requested.

## IDEA-542 — predivide-C4-restore (D4-C1a)

Aliases: common Geronimus preconditioner; c=-2 source pair.

- Question / scope: improve the pinned benchmark full NN reconstruction using one positive common predivision.
- Mechanism and hypotheses: exact target weights w, construct w/(x+2), reconstruct source array by binary64 C4, restore with D4-01. No high-precision values are supplied to this candidate algorithm.
- Closest registry entries (read in full): IDEA-193 and IDEA-379; C1 above; predecessor C4.
- Separation criterion vs closest entry: preconditioned source C4 must improve overall target error, rather than merely factor the same exact transform. Worsened errors on both N16 families erase that proposed benefit for this design.
- Literature baseline and search limitations: common division/restoration known, LIT-567 / LIT-614; no literature-derived stability estimate.
- Applicable obstructions and exact hypotheses broken: common-ratio invariant does not prevent returning to this particular target orbit, but supplies no easier source. Source mixed normality was checked by successful reference reconstruction, not inferred from positivity.
- Novelty gate verdict: variant with difference, a concrete numerical preconditioner candidate.
- Cheapest decisive test: compare full binary64 outputs against direct high-precision references on both families at N4,8,12,16.
- Kill criterion written before testing: campaign G4 both-family N16 improvement criterion; timing and AC decision are linked from novelty-gate-D4.md.
- Test discriminability: same target, precision and metric distinguish source reconstruction plus restoration from direct C4. Isolation from rounded accurate source helps localize the issue but is not a full solver test.
- Resources / cost ledger: C4 source reconstruction plus O(N^2) restoration; no asymptotic improvement over C4 claimed.
- Actual test results and committed evidence: N16 E Krawtchouk 0.223309 vs C4 0.0966694; Hahn 79.7731 vs C4 70.3138. No two-digit gain at any tested size. attempts/D4.md and integrable-predivide-failure.md.
- Disposition and precise rejected scope, if any: REJECTED, fixed c=-2 single-step design at these benchmark instances.
- Disposition reason: failed (MEASURED), not a refutation of all transforms or shifts.
- Canonical theory / negative-result ID: PD-N166.
- Topic / audit / history: round1 frozen code; no retry schedule initiated.

## IDEA-543 — universal common-transform easy start (D4-C2)

Aliases: common-factor orbit; common Toda solve; no-mass Geronimus reachability.

- Question / scope: reach every positive target pair on fixed nodes from one easy fixed pair by common changes and separate mass normalization.
- Mechanism and hypotheses: compose common nonzero multipliers, including common Christoffel, division without added masses, and common exponential flow.
- Closest registry entries (read in full): IDEA-193, IDEA-378/379; predecessor C2; proportional-start obstruction PD-T286.
- Separation criterion vs closest entry: genuine arbitrary-input reachability; preservation of projective pointwise weight ratio kills it.
- Literature baseline and search limitations: LIT-567 common deformations; LIT-614 allows more general mass additions, which are outside this candidate.
- Applicable obstructions and exact hypotheses broken: equal/proportional measures are nonnormal and remain so under common factors; arbitrary starts also preserve cross ratios I_(l,r).
- Novelty gate verdict: duplicate mechanism with a newly explicit local reachability test; no priority claim for the invariant.
- Cheapest decisive test: cancel common factors in I_(l,r), no computation needed.
- Kill criterion written before testing: invariant forbidding arbitrary targets rejects only fixed-start common-factor reachability.
- Test discriminability: targets with different I provably lie outside the orbit; independent-weight changes or masses are not tested by this invariant.
- Actual test results and committed evidence: analytical proof in integrable-ratio-obstruction.md.
- Disposition and precise rejected scope, if any: REJECTED: arbitrary-target claim for the defined class and fixed source pair, N>=2.
- Disposition reason: refuted (PROVED). Selecting a new source pair per target is not covered but still requires source reconstruction.
- Canonical theory / negative-result ID: PD-N165.
- Topic / audit / history: round1; retained to prevent repeating the same easy-start proposal.

## IDEA-544 — common Toda finite continuation (D4-C3)

Aliases: common exp(tx) flow; finite-triangle Toda RK4.

- Question / scope: continue the actual moment-defined array at t0 under a common positive weight flow on its connected normality interval.
- Mechanism and hypotheses: D4-04 finite ODE with S_degreeN=0, valid only on a normality interval. RK4 is a numerical pilot, not an exact invariant-preserving integrator.
- Closest registry entries (read in full): IDEA-193 Toda/qd, IDEA-378 invariant, IDEA-379 baseline.
- Separation criterion vs closest entry: explicit boundary/operation count and bounded endpoint measurements. A claim of a new Toda algebra is killed by LIT-567 and not pursued. A solver distinction requires independent source availability and target reachability, still missing.
- Literature baseline and search limitations: LIT-567 §2.3 equation2.18 with reversed time sign; full source proof not read. Local finite proof supplied independently.
- Applicable obstructions and exact hypotheses broken: finite boundary correctly closed; positivity does not ensure normality, with explicit N3 flow crossing in D4-02; common-ratio invariant restricts targets.
- Novelty gate verdict: duplicate algebra, variant with difference in finite closure/implementation scope.
- Cheapest decisive test: derive closure then exp(0.1x) pilot at N4,8,12,16, 20/40 RK4 steps, against deformed moments.
- Kill criterion written before testing: a normality crossing blocks that path; a wrong endpoint/closure blocks implementation. Good oracle-initialized endpoint error does not clear a full IEP gate.
- Test discriminability: step halving tests truncation behavior at fixed initial data; it says nothing about how accurately an IEP input supplies that array or about unrelated paths.
- Resources / cost ledger: O(N^2) per RHS; pilot starts from rounded 220-digit coefficients, an explicitly unavailable oracle for a general solver.
- Actual test results and committed evidence: 40-step E 4.91e-16–7.23e-14 for eight cases. Hahn errors decrease by approximately16 on halving step, while most larger Krawtchouk runs reach the rounding floor. Exact commands and table in attempts/D4.md.
- Disposition and precise rejected scope, if any: retained local supplied-array tool; stable full solver OPEN. Positivity-only normality safeguard REJECTED separately.
- Disposition reason: equivalent known flow; missing independent-weight source generator and normal path motivate deferral of the solver application, not rejection of local equations.
- Canonical theory / negative-result ID: PD-T444; safeguard PD-N164.
- Topic / audit / history: round1, no second continuation round initiated.

## IDEA-545 — independent-weight continuation (D4-C4)

Aliases: separate Toda times; weight-specific spectral modification.

- Question / scope: change the relative node weights, escaping the common-orbit obstruction, with an efficient compatible NN updater.
- Mechanism and hypotheses: a genuinely weight-dependent local generator/augmented state, with a normal path and available initialization; no such closed generator is claimed here.
- Closest registry entries (read in full): IDEA-193, IDEA-378/379 and predecessor spectral-data candidates; LIT-568 / LIT-614 show broad transformations already exist.
- Separation criterion vs closest entry: explicit new state closure plus conditioning comparison; merely writing independent exponentials is not an algorithm. Failure to supply this closure defers round1.
- Literature baseline and search limitations: three partial primary readings above are not an exhaustive survey of independent-weight deformations. No claim this route is unknown.
- Applicable obstructions and exact hypotheses broken: common-ratio obstruction is escaped because factors differ; mixed normality and conditioning remain live. Equal starting measures still invalid.
- Novelty gate verdict: variant with difference, insufficiently specified for novelty or implementation.
- Cheapest decisive test: first derive the exact finite state/generator; no expensive sweep before it exists.
- Kill criterion written before testing: absent generator/state, defer at round1 rather than use the common Toda equations with a false interpretation.
- Test discriminability: a derivation would identify actual extra information and cost; existing common-flow code cannot test this candidate.
- Actual test results and committed evidence: no experiment run for this candidate; analytic common-orbit obstruction only motivates it.
- Disposition and precise rejected scope, if any: deferred, not rejected.
- Disposition reason: missing explicit generator and initialization. Resume only with those plus a declared path and prospective conditioning test.
- Canonical theory / negative-result ID: none; OPEN candidate, no administrative PD-N.
- Topic / audit / history: round1 deferred, not evidence of impossibility.

## IDEA-546 — lattice Schrodinger spectral input (D4-C5)

Aliases: NN lattice inverse spectrum; second spectral coordinate; integrable spectral reparametrization.

- Question / scope: obtain an input metric/finite parametrization that improves reconstruction conditioning compared with two marginal node-weight lists.
- Mechanism and hypotheses: explicit invertible finite spectral coordinates and a numerically preferable map to NN coefficients; neither is supplied here.
- Closest registry entries (read in full): IDEA-031/090/117, IDEA-193, IDEA-378/379 and predecessor spectral C2/C4 records.
- Separation criterion vs closest entry: actual finite coordinates and a bounded conditioning comparison. Renaming recurrence variables as a lattice operator or invoking compatibility erases any distinction.
- Literature baseline and search limitations: multidimensional Toda/Lax context is known (LIT-567); source Lax proof not read or imported. No new spectral datum is inferred from it.
- Applicable obstructions and exact hypotheses broken: compatibility cannot create a second input spectrum; common factors leave relative data fixed; full finite normality still required.
- Novelty gate verdict: duplicate framing unless a new finite parametrization is provided.
- Cheapest decisive test: write the inverse map and compare its Jacobian/rounding sensitivity on the pinned family; prerequisite not met.
- Kill criterion written before testing: defer without explicit parametrization and metric.
- Test discriminability: it would compare actual input perturbations, not symbolic reformulations.
- Actual test results and committed evidence: none; no numerical claim for this route.
- Disposition and precise rejected scope, if any: deferred, not rejected.
- Disposition reason: missing finite map and measurable criterion. Resume when supplied; no impossibility asserted.
- Canonical theory / negative-result ID: none.
- Topic / audit / history: round1 retained explicitly; handoff can name this unresolved route without claiming progress on a solver.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `IDEA?nn-mop-stability-codex-D4-01` → `IDEA-541`.
- `IDEA?nn-mop-stability-codex-D4-02` → `IDEA-542`.
- `IDEA?nn-mop-stability-codex-D4-03` → `IDEA-543`.
- `IDEA?nn-mop-stability-codex-D4-04` → `IDEA-544`.
- `IDEA?nn-mop-stability-codex-D4-05` → `IDEA-545`.
- `IDEA?nn-mop-stability-codex-D4-06` → `IDEA-546`.
- `LIT-D4-03` → `LIT-614`.
- `PD-N?nn-mop-stability-codex-D4-02` → `PD-N164`.
- `PD-N?nn-mop-stability-codex-D4-03` → `PD-N165`.
- `PD-N?nn-mop-stability-codex-D4-05` → `PD-N166`.
- `PD-T?nn-mop-stability-codex-D4-01` → `PD-T443`.
- `PD-T?nn-mop-stability-codex-D4-04` → `PD-T444`.
