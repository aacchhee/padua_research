# Explicit O(dim) stable least-squares designs on the square: Chebyshev-lattice arrays as a deterministic sampling theory
Model: claude-fable-5-1, effort xhigh · Angle D · 2026-11-01 · Status: not returned (straddles angle C/(d); core question partly collapses — see bottom)

## Central question
Is there an explicit, closed-form family of M = O(dim Π_n) points on [−1,1]² with weights for which weighted least squares in Π_n is provably stable (Gram spectrum in [1−η, 1+η], η < 1 fixed) for the *uniform* (Legendre) measure — the deterministic counterpart of the Dolbeault–Krieg–Ullrich O(n) sampling bound, which Krieg–Ullrich (Acta Numer. 2026) say has no explicit algorithm?

## Template theory
Random/greedy sampling theory for least squares (Cohen–Migliorati 2017: Christoffel sampling, m ≍ n log n; Dolbeault–Krieg–Ullrich ACHA 2023: O(n) via Kadison–Singer, non-constructive; Bartel–Schäfer–Ullrich: BSS deterministic polynomial-time; Bartel–Kämmerer–Pozharska–Schäfer–Ullrich, SMAI JCM 11 (2025): D-optimal designs give exact L² discretization with ≤ n²+1 atoms — web-fetched 2026-10-31). Explicit deterministic families prove only quadratic scaling (Zhou–Narayan–Xu Weil-sum grids). In 1D the template is Gauss quadrature (exact Gram with M = n+1) and Chebyshev–Lobatto/CC rules with MZ constants (owned by (d)). The bivariate version must deliver: explicit points + weights, M ≤ C·dim Π_n, Gram eigenvalues bounded away from 0 and ∞ uniformly in n, for a *non-Chebyshev* target measure.

## Sub-problems
| # | Sub-problem | Kind | Payoff |
|---|---|---|---|
| 1 | Chebyshev target: Pad_{n'} with n' ≥ n+1 gives Gram = I exactly for Π_n (MEASURED: λ_min = λ_max = 1.000, M/N = 1.05–1.18). This is a one-line corollary of cubature exactness 2n'−1 ≥ 2n (NOTES optimal_point_sets §5 inference, "no paper states this"). | theory (remark) | a remark, not a paper |
| 2 | Uniform target by density reweighting (w_B·(π²/4)√(1−x_B²)√(1−y_B²)): MEASURED λ_min → 0 at M/N ≈ 1.1 (useless), 0.84–0.88 at M/N ≈ 3.5–3.9, 0.93–0.95 at M/N ≈ 7.5–8.6, λ_max ≤ 1.003; constants appear n-independent (n = 10, 20, 40). Theorem target: η(M/N) < 1 for M/N ≥ c with c explicit, uniformly in n — a weighted MZ inequality for Padua arrays against the uniform measure. | theory | Paper A: "Padua arrays are stable deterministic designs for the uniform measure at linear oversampling" |
| 3 | Christoffel-weighted Padua (w = 1/K_n^{Leg}(B,B)): MEASURED λ_min 0.96, λ_max 1.44–1.67 at M/N ≥ 3.5; worse upper constant than density reweighting. | numerics | section of Paper A |
| 4 | General measures / domains via mapped Padua (fake nodes) and BSS pruning seeded by Padua candidates. | algorithms | Paper B |

## Entry points and cheap decisive tests
1. Gram spectra of reweighted Pad_{n'} for Legendre Π_n (seconds). Kill: λ_min → 0 as n grows at fixed M/N ⇒ no uniform stability. **Outcome: at M/N ≈ 3.7–3.9 λ_min = 0.838, 0.865, 0.876 (n = 10, 20, 40) — increasing with n, stable.** Survives.
2. Exact Chebyshev Gram at n' = n+1 (1 s). **Outcome: exact.** Trivial.

## Plausible first paper
Paper A as above: a weighted MZ inequality for Padua arrays against the uniform measure with explicit oversampling constant. Reachable (the Gram is a structured Chebyshev-aliasing matrix; the proof template is the weighted Schur test C4-T03(ii) used by (d) M2).

## Closest prior work
- Krieg–Ullrich Acta Numer. 2026 (arXiv 2602.02066): "we do not know of an explicit algorithm that achieves these bounds" (NOTES optimal_point_sets §5, [OPEN-stated]).
- Bartel et al. SMAI JCM 2025 (web-fetched 2026-10-31): D-optimal exact discretization with ≤ n²+1 points; deterministic but quadratic.
- Zhou–Narayan–Xu Weil-sum grids: quadratic scaling proved, linear observed.
- An–Sommariva–Vianello 2026 (weak MZ constants; (d) territory): η for Padua *Lebesgue-measure* rule of ADE m against Legendre Π_n.
- Xu–Narayan "Randomized weakly admissible meshes" (arXiv 2101.04043; web-fetched 2026-10-31): random WAMs; no deterministic explicit family.

## Why it is not an exclusion — and why it is not returned
- (d) MZ constants: M4 is "Padua signed-weight rule and 2-D Schur" and M3 is fixed-ratio η(θ); M5 "other rules … measure dependence". Sub-problem 2 here (Padua arrays with positive density-reweighted weights against the Legendre basis, oversampling ratio M/N as the parameter) is a weighted MZ inequality — exactly the kind of object (d) M5 lists under "measure dependence". The separation ("deterministic design theory for the uniform measure" vs "MZ constants of a given rule") is a framing difference, not a mathematical one: the theorem to prove is an MZ inequality. This fails the "no renaming" rule against (d).
- Angle C (applications: sampling/least squares) owns the applied side; the theory core is (d)'s.
- Sub-problem 1 is a remark.
- Therefore: **not returned** — handed to angle C for the applied framing and flagged to (d) as an M5 instance ("positive density-reweighted Padua arrays vs Legendre, linear oversampling"). The measured spectra above are offered as a seed.

## Fit / horizon / risks
Fit high (structured Gram matrices, Schur-test templates), but ownership by (d) makes it a sub-track there, not a programme here.

## Actual test results (MEASURED, scratchpad gen4_tests23.py, 2026-11-01)
See sub-problems 1–3; n = 10, 20, 40; n' = n+1, 2n, 3n.

## IDEA-template record
# IDEA?programme-ideas-claude-4-4 — Explicit stable least-squares designs from Padua arrays (uniform measure)

Aliases: deterministic Christoffel sampling; Padua arrays as designs; density-reweighted Padua; linear oversampling; weighted MZ for Padua vs Legendre.

- Question / scope: explicit O(dim) stable weighted least-squares designs on the square for the uniform measure, from Chebyshev-lattice arrays.
- Mechanism and hypotheses: cubature exactness + density reweighting gives n-uniform Gram bounds at fixed oversampling.
- Closest registry entries (read in full): MZ IDEA?mz-constants-codex-05 (M4), -06 (M5), -04 (M3); CH IDEA-026; R1 Problem 8 / NOTES optimal_point_sets §5 inferences.
- Separation criterion vs closest entry (and observation that falsifies it): claimed separation "design theory vs MZ constant of a rule" — judged to be a renaming (the theorem is a weighted MZ inequality); falsified already by inspection of (d)'s M5 scope.
- Literature baseline and search limitations: Krieg–Ullrich 2026, Bartel et al. 2025, Xu–Narayan 2021 web-checked 2026-10-31.
- Applicable obstructions: none.
- Novelty gate verdict: variant with difference against (d) M5; duplicate in mechanism.
- Cheapest decisive test: Gram spectra at fixed M/N (done).
- Kill criterion written before testing: λ_min → 0 at fixed M/N.
- Test discriminability: eigenvalues are exact; n-trend over a factor 4 in n is visible.
- Actual test results and committed evidence: above.
- Disposition and precise rejected scope, if any: not returned; handed to angle C (applied) and flagged as (d) M5 seed.
- Disposition reason: equivalent (mechanism owned by (d) M5; applied framing belongs to angle C).
- Canonical theory / negative-result ID: none.
- Topic / audit / history: programme-ideas-20261031, angle D, draft 4, 2026-11-01.
