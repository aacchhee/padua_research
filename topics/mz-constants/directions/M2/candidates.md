# M2 retained candidates

Rules/base d36722823441dc40c6e19d69a174459348dd309c. Codex gpt-6.1-sol xhigh, explicitly assigned by orchestrator. Provisional IDs only; no shared registry edited. Acceptance awaits prior-art disposition and independent Astra review.

Before generation: read the complete state/IDEAS.md and literature/INDEX.md (both empty), plan.md, literature-search.md and literature/records/mz-input-reports.md. Searched `cardinal`, `Schur`, `D1`, `log^2`, `log²`, `testvec`, `lambda_min`, `endpoint` throughout topics, tracks, literature and state. The closest local scientific records are the supplied B2/B2b scripts and the input reports. No registry predecessor exists; that says nothing exhaustive about external literature. Historical Lobatto interpolation norm theorems remain the principal duplicate risk.

## IDEA?mz-constants-codex-21 — weighted cardinal-cell Schur estimate

Aliases: interpolation operator with endpoint weight; critical weighted convolution.

- Question / scope: explicit all-N lower λ_min in Π_(N−1).
- Mechanism and hypotheses: pointwise cardinal kernel domination, angular cells, floor w_k≥(1+distance-to-endpoint)/N², weighted Schur with h_k=m_k^−1/2.
- Closest registry entries (read in full): none; supplied B2 Schur code read in full.
- Separation criterion vs closest entry: avoids the supplied unproved mass-defect entry bound by proving a cardinal interpolation operator bound directly. A proof requiring that entry bound would erase the distinction.
- Literature baseline and search limitations: historical interpolation norm screen pending; this is a variant with a different local proof route, not claimed new in literature.
- Applicable obstructions and exact hypotheses broken: endpoint L1 column domination fails (candidate 25); no such domination is used.
- Novelty gate verdict: variant with difference, external duplication unresolved.
- Cheapest decisive test: derive endpoints and verify the two Schur sums symbolically.
- Kill criterion written before testing: failure of the weight floor or emergence of polynomial rather than harmonic Schur growth kills this route.
- Test discriminability: both calculations concern every integer N and actual CC weights, rather than finite spectra.
- Actual test results and committed evidence: analytic proof PD-T?mz-constants-codex-21; diagnostic floor checks N=8,…,1024 in developer-run.jsonl.
- Disposition and precise rejected scope, if any: survives local development; acceptance pending.
- Disposition reason: no rejection.
- Canonical theory / negative-result ID: PD-T?mz-constants-codex-21.
- Topic / audit / history: M2 rounds 1–2; independent Astra requested with pinned file hashes.

## IDEA?mz-constants-codex-22 — endpoint-cancelled harmonic U witness

Aliases: parity-exact harmonic trial; admissible log-cubed continuous mass.

- Question / scope: matching λ_min≤C/log²N with degree≤N−1.
- Mechanism and hypotheses: harmonic sum of same-parity U polynomials, subtracting their exact endpoint multiples of U_(N−1).
- Closest registry entries (read in full): none; supplied B2b full-space trial and cc_mz_large.py read in full.
- Separation criterion vs closest entry: exact degree≤N−1 and endpoint cancellation; either failure would kill the claimed distinction.
- Literature baseline and search limitations: harmonic interpolation extremizers may be classical; fulltext screen incomplete and no priority claim.
- Applicable obstructions and exact hypotheses broken: strictly alternating positive-amplitude full-space trial misses degree constraint (candidate 26); U alone only gives reciprocal-log decay (candidate 23).
- Novelty gate verdict: variant with difference relative to supplied trials, external status unresolved.
- Cheapest decisive test: evaluate degree, endpoints and interior values exactly before norm estimates.
- Kill criterion written before testing: nonzero endpoints of order NlogN or a degree-N term would destroy the intended Q=O(logN) argument.
- Test discriminability: exact symbolic cancellation settles admissibility and the source of endpoint mass.
- Actual test results and committed evidence: all cancellations hold; analytic log-cubed lower mass and logarithmic discrete upper mass in PD-T?mz-constants-codex-22. Diagnostics N=8,…,1024 recorded, not promoted to proof.
- Disposition and precise rejected scope, if any: survives local development; acceptance pending.
- Disposition reason: no rejection.
- Canonical theory / negative-result ID: PD-T?mz-constants-codex-22.
- Topic / audit / history: M2 round 4; independent Astra requested.

## IDEA?mz-constants-codex-23 — exact simpler U witness

Aliases: U_(N−1) endpoint polynomial.

- Question / scope: reconstruct its exact square norm and finite quotient.
- Mechanism and hypotheses: U product identity plus exact endpoint weights.
- Closest registry entries (read in full): none; explicitly supplied in cc_mz_large.py.
- Separation criterion vs closest entry: none as a novel witness; this is necessary verification of a supplied result.
- Literature baseline and search limitations: no novelty claim; original attribution unverified.
- Applicable obstructions and exact hypotheses broken: does not achieve matching log-squared order.
- Novelty gate verdict: duplicate as a mechanism; retained as independent reconstruction, not pursued for novelty.
- Cheapest decisive test: derive the exact integral as an odd harmonic sum.
- Kill criterion written before testing: erroneous endpoint normalization would invalidate the reported quotient.
- Test discriminability: both discrete and continuous norms are exact identities.
- Actual test results and committed evidence: PD-T?mz-constants-codex-23; rational N=512 diagnostic agrees.
- Disposition and precise rejected scope, if any: equivalent to supplied witness; mathematical reconstruction retained for dependencies.
- Disposition reason: equivalent; no PD-N created for equivalence.
- Canonical theory / negative-result ID: PD-T?mz-constants-codex-23.
- Topic / audit / history: M2 round 3, verification rather than novelty exploration.

## IDEA?mz-constants-codex-24 — uniform endpoint eta≤3/4

Aliases: three-quarter endpoint bound.

- Question / scope: does a uniform bound include N=512,n=511?
- Mechanism and hypotheses: assume the stated endpoint eta bound in the exact CC/Lebesgue convention.
- Closest registry entries (read in full): none; F7 input attribution report and supplied U witness.
- Separation criterion vs closest entry: exact finite counterexample with node count and degree explicit; no source theorem attribution is inferred.
- Literature baseline and search limitations: precise source hypotheses remain for literature worker to check.
- Applicable obstructions and exact hypotheses broken: U quotient below 1/4 violates the asserted eta ceiling.
- Novelty gate verdict: reported mechanism; independent exact local certificate, no novelty claim.
- Cheapest decisive test: rational U quotient at N=512.
- Kill criterion written before testing: RQ≥1/4 would fail to refute this bound at this case.
- Test discriminability: variational principle converts strict RQ<1/4 directly to eta>3/4.
- Actual test results and committed evidence: exact rational diagnostic true; standalone analytic certificate in PD-N?mz-constants-codex-24.
- Disposition and precise rejected scope, if any: REJECTED: refuted for any uniform assertion covering N=512,n=511.
- Disposition reason: refuted; no conditional theorem is rejected.
- Canonical theory / negative-result ID: PD-N?mz-constants-codex-24.
- Topic / audit / history: M2 round 5; acceptance pending Astra and attribution check.

## IDEA?mz-constants-codex-25 — ordinary Lebesgue bound plus cardinal L1 columns

Aliases: absolute-cardinal Cauchy route.

- Question / scope: can Λ_N=O(logN) and ∫|ℓ_k|≤Cw_klogN prove the lower order?
- Mechanism and hypotheses: the displayed uniform column domination in all k and N.
- Closest registry entries (read in full): none; local elementary alternative to supplied Schur route.
- Separation criterion vs closest entry: would avoid endpoint-weight Schur analysis using two ordinary absolute-value bounds; k=0 tests that distinction.
- Literature baseline and search limitations: no external theorem claimed; the needed hypothesis is checked directly.
- Applicable obstructions and exact hypotheses broken: ∫|ℓ_0|/w_0 grows linearly in N.
- Novelty gate verdict: local failed mechanism, no novelty claim.
- Cheapest decisive test: integrate the explicit endpoint cardinal function.
- Kill criterion written before testing: superlogarithmic endpoint ratio kills the uniform-column route.
- Test discriminability: exact formula addresses its required hypothesis for arbitrarily large N.
- Actual test results and committed evidence: ∫|ℓ_0|=1/N, exact; PD-N?mz-constants-codex-25.
- Disposition and precise rejected scope, if any: REJECTED: failed for this absolute-column mechanism.
- Disposition reason: failed; the lower-bound target survives and is proved by candidate 21.
- Canonical theory / negative-result ID: PD-N?mz-constants-codex-25.
- Topic / audit / history: M2 round 1; independently flagged also by Astra during discussion.

## IDEA?mz-constants-codex-26 — direct transfer of full-space alternating trial

Aliases: uncorrected alternating normalized-node vector.

- Question / scope: can supplied y_k=(−1)^km_k^−1/2 directly prove the degree-N−1 upper bound?
- Mechanism and hypotheses: direct use of its full Π_N inverse Rayleigh quotient.
- Closest registry entries (read in full): none; supplied B2b code read in full.
- Separation criterion vs closest entry: degree restriction must be satisfied to transfer from full space; coefficient of T_N is the falsifiable test.
- Literature baseline and search limitations: no literature novelty claim; this screens a supplied calculation's applicability.
- Applicable obstructions and exact hypotheses broken: top Chebyshev coefficient has strictly positive summands after alternating signs cancel.
- Novelty gate verdict: supplied full-space candidate; attempted direct transfer fails.
- Cheapest decisive test: exact top-coefficient constraint before any eigenvalue experiment.
- Kill criterion written before testing: nonzero T_N coefficient kills the direct transfer.
- Test discriminability: an exact necessary and sufficient condition for degree≤N−1.
- Actual test results and committed evidence: all-N positivity proof in PD-N?mz-constants-codex-26.
- Disposition and precise rejected scope, if any: REJECTED: failed only as an uncorrected direct transfer; no claim against its full-space model.
- Disposition reason: failed; corrected witnesses remain possible and candidate 22 supplies one.
- Canonical theory / negative-result ID: PD-N?mz-constants-codex-26.
- Topic / audit / history: M2 round 3; independently flagged also by Astra.

## IDEA?mz-constants-codex-27 — a sharp rescaled endpoint limit

Aliases: exact leading logarithmic constant.

- Question / scope: does (logN)²λ_min converge to an explicit positive constant?
- Mechanism and hypotheses: none selected; retain the sharper portion of the user's target.
- Closest registry entries (read in full): none; supplied polynomial-fit code is only measured evidence.
- Separation criterion vs closest entry: a two-sided order bound does not identify a limit; a later route must prove convergence and sharpness.
- Literature baseline and search limitations: same incomplete historical screen; no novelty assertion.
- Applicable obstructions and exact hypotheses broken: finite eigenvalue fits and a single trial cannot identify the minimizing asymptotic constant.
- Novelty gate verdict: deferred target, not a developed mechanism.
- Cheapest decisive test: not selected; do not spend another conceptual round on fits.
- Kill criterion written before testing: not applicable to an undeveloped target; no test claimed.
- Test discriminability: not applicable.
- Actual test results and committed evidence: none beyond separately proved comparison bounds.
- Disposition and precise rejected scope, if any: deferred.
- Disposition reason: resume only after order theorem audit and prior-art comparison, with a concrete sharpness mechanism.
- Canonical theory / negative-result ID: PD-T?mz-constants-codex-27, OPEN.
- Topic / audit / history: split out at M2 completion; not counted as a new conceptual mechanism round.
