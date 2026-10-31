# M1 retained candidates and round ledger

Rules/base: `d36722823441dc40c6e19d69a174459348dd309c`, read 2026-10-31. Developer: Codex, assigned gpt-6.1-sol xhigh. The complete `state/IDEAS.md`, `literature/INDEX.md`, supplied report record and frozen plan/literature baseline were read before exploration. Global registries are empty. Searches actually issued via `rg` covered Hankel, defect, alias, Schur, positivity, upper spectrum, lambda_max, D1 and T_N throughout ideas/state, tracks, topics and literature. The supplied Hankel formula is the sole local mathematical predecessor. Historical literature screening remains incomplete; no candidate is accepted or claimed novel before that screen and a separate reconstruction.

## IDEA?mz-constants-codex-11 — infer PSD from the active defect signs

Aliases: nonnegative Hankel defect; direct Loewner domination.

- Question/scope: could the exact defect establish the stronger \(Q_N(p^2)\le\int p^2\) on \(\Pi_{N-1}\) for all \(N\ge2\)?
- Mechanism/hypotheses: promote entrywise positivity on the active **even** anti-triangle to positive semidefiniteness. Odd entries are zero.
- Closest entries: no registry entries; supplied F7 Hankel suggestion read. The source did not itself assert PSD.
- Separation criterion: a genuine Gram/moment representation of the truncated Hankel defect would distinguish this mechanism from mere signs. A negative principal determinant kills that distinction.
- Literature baseline/limits: source reports and preliminary M0 screen only.
- Applicable obstruction: a zero diagonal incident to a positive off-diagonal entry cannot occur in a PSD matrix.
- Novelty verdict: source variant considered only as a kill test, no priority claim.
- Cheapest decisive test/kill criterion written before testing: inspect exact 2-by-2 principal minors for N=2..20; any negative minor refutes PSD in that scope.
- Discriminability: one negative minor disproves a universal PSD conclusion; finitely many positive tests could not prove it.
- Actual result: N=5 already kills it. General minor with i=floor(N/2), j=i+2 proves indefiniteness for every N>=5; finite checker also checks this minor.
- Disposition: **REJECTED: refuted** for N>=5, not a refutation of the threshold-two target.
- Canonical negative result: PD-N?mz-constants-codex-11, `m1-failed-psd.md`.

## IDEA?mz-constants-codex-12 — direct row diagonal dominance

Aliases: Gershgorin of 2M−R; plain Chebyshev mass rows.

- Question/scope: does unweighted row diagonal dominance prove 2M−R positive definite for every N>=2?
- Mechanism/hypotheses: exact moment/alias formulas in the unscaled Chebyshev basis; diagonal versus sum of absolute off-diagonal entries.
- Closest entries: IDEA?…-11 and source exact defect. This tests the target matrix itself, rather than inferring PSD of D.
- Separation criterion: every row must have nonnegative dominance margin. A negative exact margin kills this particular sufficient criterion.
- Literature baseline/limits: no external comparison theorem used; no priority claim.
- Applicable obstruction: none inherited; this property requires testing.
- Novelty verdict: standard criterion/source variant, not claimed new.
- Cheapest decisive test/kill criterion written before testing: calculate margins for N=2..20; one negative margin kills universal plain diagonal dominance.
- Discriminability: a negative margin refutes the property, while it does not refute positive definiteness.
- Actual result: floating exploratory matrix calculation at N=5 found a negative margin. Exact row 2 margin is −2/35. See executed check record.
- Disposition: **REJECTED: failed**, solely for the universal unweighted row-dominance proof route.
- Canonical negative result: PD-N?mz-constants-codex-12, `m1-failed-diagonal-dominance.md`.

## IDEA?mz-constants-codex-13 — absolute-coefficient comparison for a Z-matrix

Aliases: sign replacement; Z-matrix upper MZ proof; 2M−R comparison.

- Exact question: prove the frozen Q_N(p²)<2∫p² for all nonzero p in Pi_(N−1), N>=2.
- Mechanism: show A=2M−R has nonpositive off-diagonal entries; replace a by |a|. Then |a|^T A|a|=|a|^T M|a|+|a|^T D|a|/2>0 because D is entrywise nonnegative.
- Closest entries: IDEA?…-11 uses the same defect but falsely needs D PSD; IDEA?…-12 seeks plain row dominance. Both failed tests are read and retained.
- Separation criterion: the simultaneous exact properties A_ij<=0 for i≠j and D_ij>=0 remove the PSD obligation. A single positive A off-diagonal entry, or negative active D entry, kills this exact proof.
- Literature baseline/limits: inherited exact identity independently reproved; historical priority screen pending. No C4 theorem imported.
- Applicable obstructions escaped: D indefiniteness is irrelevant because only nonnegative vectors enter its quadratic form; failed row dominance is unnecessary.
- Novelty verdict: variant with a mathematically specified difference within the documented local search; external duplicate verdict pending.
- Cheapest decisive test/kill criterion written before proof: inspect A off-diagonal entries from d=|i−j|, s=i+j, r=2N−s, especially n=N−1 and the nearest active entries. If r<d, the proposed sign comparison can fail.
- Actual test: r−d=2(N−max(i,j))>=2 proves the required sign for every allowed pair. Exact checks N=2..40 supplement the proof.
- Verification plan/outcome: self-contained analytic proof in PD-T?…-12; adversarial reconstruction provisionally confirms the sign argument; pinned audit and prior-art screen pending.
- Disposition: development complete, acceptance pending. The strict theorem is PROVED in development; it is not merely a finite measurement.
- Canonical theory: PD-T?mz-constants-codex-12, `m1-upper-bound.md`.

## IDEA?mz-constants-codex-14 — quantify the gap through a telescoping mass floor

Aliases: half-constant coefficient scaling; weighted mass dominance.

- Question/scope: strengthen the established strict bound to lambda_max<=2−2/(pi N), every N>=2.
- Mechanism: b=(1/2,1,…,1) makes the exact continuous mass row sum a positive rational tail; weighted Z-matrix decomposition yields M>=diag(2,1,…)/N, while sin(theta)<=1 yields the opposite upper comparison by pi/2.
- Closest entries: IDEA?…-12 fails plain row dominance of A, whereas this uses a different positive vector and applies to M; IDEA?…-13 supplies A(a)>=M(|a|).
- Separation criterion: exact floor coefficients (Mb)_i/b_i must dominate (2,1,…)/N. Any smaller row quotient kills this stated constant, without refuting the qualitative theorem.
- Literature baseline/limits: elementary trigonometric mass comparison; no novelty claim or external dependency.
- Applicable obstructions escaped: the b0=1/2 normalization cancels the extra constant-mode term that obstructs plain row sums.
- Novelty verdict: standard weighted-diagonal-dominance refinement with a distinct exact coefficient calculation; external duplicate screen pending.
- Cheapest decisive test/kill criterion written before development: derive exact row tails and check i=0, i=N−1 and N=2. An erroneous endpoint normalization or nonpositive tail kills the formula.
- Actual result: k_i in {N−1,N}, (Mb)_0=1/k0, (Mb)_i=k_i/(k_i²−i²); all satisfy the floor. Exact checks N=2..40 pass.
- Disposition: PROVED development, separate audit/prior-art pending.
- Canonical theories: PD-T?…-13 `m1-coefficient-floor.md`; quantitative conclusion in PD-T?…-12.

## IDEA?mz-constants-codex-15 — source-reported full-degree top mode

Aliases: T_N obstruction; codimension-one endpoint exclusion.

- Question/scope: independently reconstruct why the theorem cannot extend to Pi_N.
- Mechanism: T_N²=1 at every node but has integral 1−1/(4N²−1).
- Closest entry/source: supplied mapping note O4 reports this exact calculation. It is a known source report to be verified, not an independently novel candidate.
- Separation criterion: none claimed versus the report. Reproduction must use exactly N+1 Lobatto nodes and Lebesgue integration; different conventions would invalidate the match.
- Literature baseline/limits: source report only; no external priority claim.
- Applicable obstruction: this is the full-degree obstruction itself, not a failure of M1.
- Novelty verdict: equivalent to source report, retained as an independently checked substantive dependency of the degree restriction.
- Cheapest decisive test/kill criterion: evaluate T_N on nodes and integrate the product identity; a normalization other than sum weights=2 kills the supplied formula.
- Actual result: exact ratio 2(4N²−1)/(4N²−2)>2, all N>=2; rational finite checks pass.
- Disposition: equivalent source reconstruction, PROVED result; no PD-N merely for equivalence.
- Canonical theory: PD-T?…-14 `m1-full-degree-obstruction.md`.

## Round count and remaining scope

| Round | Changed mechanism / decisive test | Outcome |
|---|---|---|
| 1 | Defect PSD from active signs; first principal-minor kill test | Refuted for every N>=5 |
| 2 | Plain row diagonal dominance of 2M−R | Failed at exact N=5 |
| 3 | Absolute-coefficient comparison using Z-matrix signs | Frozen strict target PROVED in development |
| 4 | Half-constant normalization and telescoping mass floor | Explicit gap 2/(pi N) PROVED in development |

No more M1 conceptual rounds are necessary to close the frozen first target. The sharp upper limit near 1.004437 remains OPEN; its source provenance and measurements do not establish a theorem. That separate sharpening is queued rather than promoted to a new active direction. The lower spectrum and fixed-ratio MZ target are not inferred from the upper theorem.

## Provisional split map / handoff

| Provisional ID | Durable file | Development status |
|---|---|---|
| PD-T?mz-constants-codex-11 | tracks/mz-constants/theory/m1-cc-foundation.md | PROVED |
| PD-T?mz-constants-codex-12 | tracks/mz-constants/theory/m1-upper-bound.md | PROVED |
| PD-T?mz-constants-codex-13 | tracks/mz-constants/theory/m1-coefficient-floor.md | PROVED |
| PD-T?mz-constants-codex-14 | tracks/mz-constants/theory/m1-full-degree-obstruction.md | PROVED |
| PD-N?mz-constants-codex-11 | tracks/mz-constants/theory/m1-failed-psd.md | PROVED scoped refutation |
| PD-N?mz-constants-codex-12 | tracks/mz-constants/theory/m1-failed-diagonal-dominance.md | PROVED scoped mechanism failure |

All acceptance decisions are pending; the orchestrator will integrate final IDs and shared crosswalks at PR preparation. No Git state, shared registry, or manuscript was mutated by this worker.
