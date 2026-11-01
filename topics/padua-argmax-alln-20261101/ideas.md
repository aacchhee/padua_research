# Candidates — padua-argmax-alln-20261101

All candidates are retained. Template: `templates/IDEA.md`. Gate: [gate.md](gate.md).

## IDEA?argmax-alln-claude-01 — shifted-lattice majorant maximal at the coset point

Aliases: majorant route; shift-sum S(t); triangle-inequality reduction.

- Question / scope: does λ_n ≤ S(t) := |Λ|⁻¹ Σ_λ |G_n(t+λ)|, together with "S is maximal at the non-node coset point", prove PD-T099 for all n?
- Mechanism and hypotheses: the reflected-lattice identity (R) of [plan.md](plan.md) §1 and the triangle inequality. S equals λ_n at the corners.
- Closest registry entries (read in full): IDEA-206 (programme-ideas proposal-1).
- Separation criterion: a single-kernel shift-maximisation problem in place of the four-copy absolute sum. The distinction disappears if S is not maximal at the coset.
- Literature baseline: none read (plan §5.4).
- Applicable obstructions: none registered for λ_n majorants.
- Novelty gate verdict: variant of IDEA-206 (new mechanism for its target).
- Cheapest decisive test: maximise S over one fundamental cell and compare with S(coset). This is `code/cell.py`.
- Kill criterion written before testing: kill if max S > S(coset) at any n ≥ 3.
- Test discriminability: S(coset) = Λ_c is exact (PD-T101). A cell maximum above it refutes the mechanism as stated, provided the excess exceeds the float64 error (about 1e-12 here).
- Actual test results: max S exceeds Λ_c by 1.4e-3 (n = 3) … 9.2e-5 (n = 40), at about 0.01·π/n off the coset point. See [outputs/cell.out](outputs/cell.out) and [the observations record](theory/argmax-alln-claude-01-measured-observations.md).
- Disposition: **REJECTED: failed** (MEASURED evidence, float64 plus local optimisation) as a stand-alone proof mechanism, in the precise scope "max S attained at the coset point". It is **retained as a sub-tool**: a valid upper bound, usable as the discard test away from coset neighbourhoods in IDEA?argmax-alln-claude-02 (D).
- Canonical theory / negative-result ID: none; the failure is MEASURED only. A certified version would be a PD-N.
- Topic / history: 2026-11-01, Claude.

## IDEA?argmax-alln-claude-02 — scaled local profiles, cell certificates and a finite certifier

Aliases: two-scale asymptotics; profile route; (A)–(D) architecture.

- Question / scope: prove PD-T099 for n ≥ n₀ through uniform O(1) asymptotics in every regime, and for n < n₀ by certified computation.
- Mechanism: plan §4 (A)–(D).
- Closest entries: IDEA-206, PD-T098, and part 2's A2 records 01–04 and A4(a) records 70–73. Their asymptotics concern the corner or edge only; this candidate needs all regimes uniformly.
- Separation criterion: n-independent limit profiles Φ_regime certified once on a fixed cell. Erased if profiles fail to converge or depend on n beyond o(1).
- Novelty gate verdict: variant of IDEA-206.
- Cheapest decisive test: plan §5.1 (profile convergence up to n ≈ 200).
- Kill criterion written before testing: kill (A)–(D) if the rate is no better than (log n)/n with a fitted constant giving n₀ > 200, or if R_n(ξ) does not converge at fixed ξ.
- Test discriminability: the measured gaps (interior about 1.75, edge about 0.55) set the error budget. A rate and constant estimate decide whether a feasible n₀ exists.
- Actual test results: not run. The only data so far are the interior gaps of `code/interior.py`.
- Disposition: **deferred**. It resumes after part 2 (PR #12) completes and is audited (handoff 01).

## IDEA?argmax-alln-claude-03 — Brutman-type monotone decrease of cell maxima

Aliases: monotone maxima ordering; pairing comparison.

- Question / scope: do the local maxima of λ_n decrease monotonically along rhombus directions away from the non-node corners? If so, is there an exact pairing inequality λ_n(t) ≤ λ_n(t + coset step) in (R)?
- Closest entries: IDEA-048 (contextual geometry of maxima); 1D analogues (Brutman 1978, unread).
- Separation criterion: an exact comparison without asymptotics. Erased if monotonicity fails on certified data.
- Novelty gate verdict: new within the documented search.
- Cheapest decisive test: check the ordering on part 2's certified n ≤ 7 maxima lists, and on float64 maxima up to n ≈ 50.
- Kill criterion written before testing: kill if any certified n ≤ 7 list violates the ordering in a way no pairing could respect (to be made precise when the lists are read).
- Actual test results: not run.
- Disposition: **deferred** (as above).

## IDEA?argmax-alln-claude-04 — generating-curve numerator factorisation

Aliases: 2D common-factor trick; envelope × convex sum.

- Question / scope: does the rank-1 lattice structure in rhombus coordinates make the numerators of the U-product kernel split into a lattice-independent envelope and an oscillating part? Does that yield a cell-wise envelope × convex-sum form of λ_n?
- Closest entries: IDEA-206; Bos–Caliari–De Marchi–Vianello–Xu 2006 (generating curve; read only as cited in programme-ideas records).
- Separation criterion: an exact algebraic identity. Erased if the oscillating part dominates on cells.
- Novelty gate verdict: new within the documented search; unverified.
- Cheapest decisive test: derive the identity for one cell and check it in exact arithmetic at n = 3–6.
- Kill criterion written before testing: kill if no cell-wise sign-stable envelope exists at n = 4.
- Actual test results: not run.
- Disposition: **deferred**.
