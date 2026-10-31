# Stochastic Galerkin with dependent inputs: spectral bounds of Galerkin matrices built from truncated bivariate recurrence matrices
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · Angle C · 2026-10-31 · Status: not returned (central question is a joint-spectrum / nearly-commuting-pair question: handed to angle B; also adjacent to (b)'s deferred R10, candidate 034)

Aliases: data-driven PCE on dependent/discrete measures; arbitrary polynomial chaos (aPC) in several variables; stochastic Galerkin matrices for non-product measures; Ernst–Ullmann bounds in two parameters; Kronecker sums of non-commuting recurrence sections; Jakeman–Franzelin–Narayan–Eldred–Pflüger dependent-variable PCE.

## Central question
For a parametric operator A(ξ) = A₀ + ξ₁A₁ + ξ₂A₂ with (ξ₁, ξ₂) jointly distributed under a non-product (possibly sample-based) measure, the stochastic Galerkin matrix in the orthonormal bivariate PCE basis is I⊗A₀ + H_x⊗A₁ + H_y⊗A₂ with (H_x, H_y) the truncated recurrence sections, which do not commute; what replaces Ernst–Ullmann's eigenvalue bounds (univariate: eigenvalues of the truncated Jacobi matrix are Gauss nodes inside the support, giving Λ(G) ⊂ Λ(A(supp)) bounds) when the sections are a nearly commuting pair, and is the answer controlled by the joint numerical range of (H_x, H_y) or by their commutator?

## Template theory
Ernst–Ullmann, "Stochastic Galerkin matrices", SIMAX 31 (2010) (UNVERIFIED: from memory and a search hit on the TUM portal, 2026-10-31; not fetched): for product measures the Galerkin matrix of a linear-in-parameters operator has eigenvalue bounds derived from the truncated Jacobi matrices, whose eigenvalues are the Gauss nodes; Powell–Elman mean-based preconditioning rests on the same facts. Bivariate version required: bounds for I⊗A₀ + H_x⊗A₁ + H_y⊗A₂ with non-commuting symmetric sections; the natural objects are the joint numerical range W(H_x, H_y) ⊂ ℝ² (which contains the support hull but may exceed it) and the commutator norm ‖[H_x, H_y]‖ (which is 0 exactly for product/tensor measures and for exact N-atomic measures with M = N, and O(1) otherwise); a Xu-type statement would relate eigenvalue-ish quantities of the pair to cubature nodes when a commuting extension exists (DST 2005).

## Sub-problems (≥3, each with a separate payoff)
| # | Sub-problem | Kind | Payoff (what paper) |
|---|---|---|---|
| 1 | Bound Λ(G) by A(W(H_x,H_y)) where W is the joint numerical range; characterise W for truncated sections of discrete bivariate measures (does W ⊂ conv(supp μ)? — yes by the numerical-range-of-a-compression argument; is it sharp?) | theory | "Eigenvalue bounds for stochastic Galerkin matrices with dependent inputs" |
| 2 | Commutator-controlled sharpening: when ‖[H_x,H_y]‖ ≤ δ, how close are Λ(G) to the Kronecker-sum spectra of a nearby commuting pair (Lin's theorem, quantitative versions — Kachkovskiy–Safarov 2016; this is (b)'s L3-Q1 mechanism) | theory | overlaps (b) L3 and R10 (deferred 034) — the reason this draft is not returned |
| 3 | Data-driven basis from samples: generating (H_x, H_y) by the seed/HL recurrence from Monte Carlo samples of the dependent measure instead of Gram–Schmidt on moments (Jakeman et al. 2019 state they "will investigate alternative strategies for producing orthonormal multivariate polynomials" because GS "is poorly conditioned"; fetched 2026-10-31) and comparison with Liu–Narayan's multivariate Stieltjes (SISC 2023) | numerics-software | an application note; the method itself is HL/seed/Liu–Narayan, not new |
| 4 | Preconditioners (mean-based, Kronecker) with proven bounds in the dependent case | algorithms | a solver paper |

## Entry points and cheap decisive tests
1. (n ≤ 6, seconds) Build (H_x, H_y) for a Gaussian-copula Beta pair from 10⁴ samples, degree 6; compute Λ(I⊗A₀ + H_x⊗A₁ + H_y⊗A₂) for a 1D finite-difference Laplacian with A₁, A₂ coefficient fields; compare with the extremes of A over conv(supp) and over W(H_x,H_y). Kill: if Λ(G) always lies inside the A(conv supp) range for random trials, the joint-numerical-range bound is the full answer and sub-problem 1 is a one-page remark.
2. (seconds) Correlate the excess of Λ(G) beyond the supp-based bound with ‖[H_x, H_y]‖ as the degree grows. Kill for sub-problem 2: no correlation.

## Plausible first paper (≈6 months)
"Spectral bounds for stochastic Galerkin matrices of dependent random inputs via joint numerical ranges of bivariate recurrence sections" — reachable, but its core is a compression/numerical-range argument that angle B (joint/multiparameter eigenvalue structure) should own.

## Closest prior work
- Ernst–Ullmann SIMAX 2010 (UNVERIFIED, not fetched); Powell–Elman IMA JNA 2009 (UNVERIFIED, memory).
- Jakeman, Franzelin, Narayan, Eldred, Pflüger, CMAME 2019 (NSF PAR copy fetched 2026-10-31): dependent-variable PCE via Gram–Schmidt with quadrature/Monte Carlo inner products; GS "poorly conditioned"; future work: alternative strategies for orthonormal multivariate polynomials.
- Rahman, "A polynomial chaos expansion in dependent random variables" (arXiv:1804.05676; JMAA 2018 per memory, UNVERIFIED venue) (fetched 2026-10-31): whitening of the monomial moment matrix (Cholesky choice), bivariate degree-3 examples; "more research is needed for robust estimation of the expansion coefficients".
- Guo–Narayan–Liu–Zhou, arXiv:2008.10121 (fetched 2026-10-31): data-driven PCE via tensorised univariate Hankel/Cholesky bases, acknowledging an "additional approximation penalty" for non-product joint samples and ill-conditioning for large K.
- Oladyshkin–Nowak, aPC (Reliab. Eng. Syst. Saf. 2012; search hit 2026-10-31, not fetched): moment-based univariate aPC; multivariate by tensorisation; Ahlfeld–Belkouchi–Montomoli SAMBA (JCP 2016, UNVERIFIED, not found in the returned results) is sparse-grid aPC. None of these treats the Galerkin spectral question.
- Liu–Narayan SISC 2023 (R2 row 4; NOTES `discrete_multivariate_OP_computation.md` Q3): multivariate Stieltjes from samples; no Galerkin analysis.
- Web searches: "stochastic Galerkin dependent random variables multivariate orthogonal polynomials recurrence matrices eigenvalue bounds Ernst Ullmann" and "stochastic Galerkin dependent OR correlated random inputs non-product measure … 2020–2024" (2026-10-31): no paper on Galerkin spectral bounds for dependent inputs found (search-negative).

## Why it is not an exclusion
- (b): sub-problem 2 is (b)'s L3-Q1 / R10 (034, deferred "keep to 2D diagnostics") mechanism applied to a Kronecker-sum matrix; adjacency is too close for angle C to own; sub-problem 1 alone (numerical-range compression) is a note.
- (a), (c), (d): untouched.
- Already judged: "f(A,B) total-degree Krylov" (Huhtanen collapse: commuting Hermitian pairs reduce to one normal matrix) — the Galerkin pair (H_x, H_y) does not commute, so the collapse does not apply, but the same obstruction table entry (OBST-12/-10) warns that nothing structural survives for non-commuting sections beyond polynomial functions. "Multivariate Stieltjes d ≥ 4" — sub-problem 3 uses it as a tool only.

## Fit with AC's expertise and 2–5-year horizon
Fit is high on the matrix side (Kronecker-structured symmetric matrices, numerical ranges, preconditioning) but the programme-scale content belongs to the joint-spectrum theory of nearly commuting pairs (angle B) and to (b)'s L3; the UQ application alone gives one or two papers, not a programme. Horizon questions: (1) numerical-range bound; (2) commutator sharpening; (3) preconditioners; (4) time-dependent/nonlinear parametric problems. Escalation beyond (3) depends on the angle-B theory.

## Risks and obstructions
- Nearest obstruction: **Computed H_x, H_y never commute exactly** and **Huhtanen 2002 collapse** (brief §3): the first is the very object of study here (non-commutation is the dependent-input signal); the second does not apply (no commuting pair). **Not flat at colength N**: relevant if one tries to interpret (H_x, H_y) as sections of an N-atomic measure's recurrences — generically impossible, which is why sub-problem 2 needs the nearby-commuting-pair machinery.
- Ownership: the UQ community (Narayan, Jakeman, Nobile, Ullmann) could write the numerical-range note quickly.

## IDEA-template record
# IDEA?programme-ideas-claude-3-4 — Stochastic Galerkin spectral bounds for dependent inputs via bivariate recurrence sections

Aliases: data-driven PCE on dependent/discrete measures; aPC in several variables; stochastic Galerkin matrices for non-product measures; Ernst–Ullmann bounds in two parameters; Kronecker sums of non-commuting recurrence sections.

- Question / scope: eigenvalue bounds for I⊗A₀ + H_x⊗A₁ + H_y⊗A₂ with (H_x, H_y) truncated bivariate recurrence sections of a dependent (possibly sample-based) measure; preconditioning; sample-generated bases.
- Mechanism and hypotheses: compression argument (joint numerical range of a compression lies in that of the full diagonal pair = conv supp); commutator-controlled sharpening via nearby commuting pairs; hypotheses: symmetric A_i, real nodes, truncation in total degree.
- Closest registry entries (read in full): LZ -004, -005, -031, -032, -034 (L3 / R10), -027 (f(A,B)), -048 (Huhtanen reduction).
- Separation criterion vs closest entry (and observation that falsifies it): vs LZ-034 (joint eigenvalues of nearly commuting sections, deferred): this candidate asks for spectral bounds of a Kronecker-sum matrix, not for joint eigenvalues; falsified if the numerical-range bound is sharp and trivial (entry point 1 kill), leaving only the commutator sharpening, which is LZ-031/034.
- Literature baseline and search limitations: Ernst–Ullmann 2010 (UNVERIFIED), Jakeman et al. 2019 (fetched), Rahman 2018 (fetched), Guo–Narayan–Liu–Zhou 2020 (fetched), Oladyshkin–Nowak 2012 (not fetched), Ahlfeld et al. 2016 (not found), Liu–Narayan 2023 (NOTES). Searches 2026-10-31 as listed.
- Applicable obstructions and exact hypotheses broken: non-commutation of sections (studied, not broken); Huhtanen collapse (hypothesis "commuting Hermitian pair" not met).
- Novelty gate verdict: not assessed (not returned: handed to angle B; adjacency to (b)).
- Cheapest decisive test: entry point 1.
- Kill criterion written before testing: Λ(G) ⊂ A(conv supp) in all random trials at degrees ≤ 6.
- Test discriminability: eigenvalues of ≤ 28·m matrices (m = FD grid size ≤ 50), exact in double precision; the comparison interval is explicit.
- Resources / cost ledger (optional, when relevant): numpy, seconds.
- Actual test results and committed evidence: (empty; no test run)
- Disposition and precise rejected scope, if any: not returned by angle C; handed to angle B as a one-line pointer.
- Disposition reason: deferred — scope belongs to angle B / (b) L3; resume if angle B does not take it and the gate wants a UQ application track.
- Canonical theory / negative-result ID: none.
- Topic / audit / history: programme-ideas-20261031, generator C, draft 4, 2026-10-31.
