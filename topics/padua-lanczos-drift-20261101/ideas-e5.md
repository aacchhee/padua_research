# E5 candidate memory

Rules/base: `806cc7b4509fd93bae652f9545d32d95529f8281`.
Developer: Codex, requested `gpt-6.1-sol`, xhigh (runtime does not independently expose resolved variant/effort). Git, shared registries, and handoffs are orchestrator-owned.

## Gate and reading scope

Applied AC's relaxed gate: complete registry headings/aliases/summary scan and obstruction/disposition tables, then mechanism searches, rather than claiming a new full-text reading of every linked unrelated entry. Searches: `Padua|moment|Favard|Greenbaum|backward|Turan|radius|Hessian|certificate|square|consistency` across `state/IDEAS.md` and `literature/INDEX.md`, with targeted theory/topic searches. Closest entries: IDEA-156–168, especially IDEA-162/168, PD-T056/058/059/060/069/075, PD-N020/022. Read those theory records in full, plus old L3 SUMMARY/STATUS/R05/R06. Existing derivative/inradius and local-Hessian mechanisms are predecessors, not new claims. Literature index consulted before source comparisons; no PDF acquired and no historical priority claim.

Applicable obstruction memory: a positivity radius for one certificate does not upper-bound the best obstruction radius; decreasing certified lower bounds prove no decay; arbitrary functional perturbations in reading (E) need not be produced by a floating-point recurrence (G); scalar Lin/Greenbaum transfer does not preserve graded sections; completed-pair consistency and raw formed-coefficient consistency differ; residuals proportional to perturbation can be met trivially by the original measure.

## IDEA?drift-codex-30 — explicit corner negative witness for P_n

Aliases: E5 corner scaling; upper bound on rho_n; boundary-layer sign.

- Question/scope: find explicit points zeta_n at distance O(n^-a), a>0, from Padua nodes, with P_n(zeta_n)<0 for all sufficiently large n.
- Mechanism/hypotheses: exploit the near-coincident first interior angles pi/n and pi/(n+1); derive an exact trigonometric identity or a Taylor expansion with a strictly negative leading coefficient. n>=4; the polynomial P_n is precisely PD-T069's.
- Closest entries read in full: IDEA-168/PD-T069 and PD-T075; their node Hessians and finite sampled negative points do not give an all-n upper witness.
- Separation/kill criterion: an all-n explicit sign is the distinguishing property. A nonnegative leading form on a proposed path kills that path, not U1. A numerical slope is insufficient.
- Literature baseline: local double-zero/Hessian mechanism already in PD-T059 and LIT-263 (source coverage qualified); no new literature claim.
- Cheapest decisive test: simplify g_m in angular coordinates before numerical searches, then inspect exact Taylor coefficients.
- Pretest observation: equal phase n theta=(n+1)phi gives g_0=0 and g_m=sin(n theta)sin(m(theta-phi)); hence P_n=10 sin^2(n theta)sin^2(theta-phi)>=0. Square edges x=1 or y=1 likewise have a nonnegative Turan reduction. These paths cannot supply a negative witness.
- Actual result: common-angle increment `a/n^4`, `a=20*pi^3/9`, gives `n^7 g_m->-a^2-(2/3)a*pi^3*m^3`, hence `n^14P_n->-6400*pi^12/729<0`. The physical displacement is asymptotic to `(20sqrt(2)pi^4/9)n^-5`. Written analytic theorem settles U1. An earlier common increment `A/n^3` gave positive leading term `(9/2)A^4*n^-10` for fixed nonzero A, so that coarser proposed scale failed the negative-witness aim and prompted the finer scale; this failed parameter regime is retained here.
- Disposition: retained, quantitative variant with difference: explicit all-n eventual negative witness/rate. The failed equal-phase, square-edge, and fixed-A/n^3 mechanisms are split into their own IDEA?drift-codex-32/33/34 entries below and the scoped PD-N?drift-codex-32; they do not reject the corner method or U1. No historical novelty claim.
- Canonical theory: PD-T?drift-codex-30, `tracks/bivariate-lanczos/theory/drift-codex-e5-30-padua-positivity-radius-upper-bound.md`.

## IDEA?drift-codex-31 — residual-aware nonexact reading-(G) construction

Aliases: square-root support spread; actual computed section data; tolerance constants.

- Question/scope: determine what a nonexact representation at Padua n=3/4 or a square case with sqrt(epsilon) support scale actually proves about (G).
- Mechanism/hypotheses: compare the distance of a specified data functional to the localized moment cone with actual recurrence consistency/local residuals. Preserve mass convention (R1/R2/R3).
- Closest entries: PD-T056/058/059/060 and PD-N020/022; L3 R06 consistency tests and completed-pair versus raw-data distinction.
- Separation/kill criterion: a result must control a family arising from the specified finite-precision local relations whose forward error exceeds its O(u) residual. Merely using mu on the original nodes for forward-accurate data is the already proved trivial reading (L).
- Cheapest decisive test: check whether residual allowance is smaller than the perturbation and whether the computed data are consistent before invoking a support theorem.
- Actual result: explicitly constructed a square n=1 three-node triangle family with four positive split atoms, moment-infinity perturbation exactly epsilon, noncommuting exact sections, radius upper sqrt(6epsilon), and lower sqrt((1-3gamma)epsilon/3) for unit-mass fits with residual gamma*epsilon and gamma<1/3. Exact matrices/moments and written bounds are recorded. This tests the authorized square sqrt(epsilon) alternative; no Padua n=3/4 fit was run.
- Disposition: retained concrete known-mechanism refinement for the square case; original (G) realization target deferred/OPEN. Resume (G) only with actual recurrence/formed data, quantified consistency correction, and local error u such that the target residual is smaller than the forward perturbation. Original mu already has radius zero and residual epsilon, so epsilon=O(u) with an unspecified residual constant does not decide G.
- Canonical theory: PD-T?drift-codex-31, `tracks/bivariate-lanczos/theory/drift-codex-e5-31-explicit-square-root-spread-family.md`. No PD-N: deferred G realization is not a refuted mechanism and no theorem about actual floating-point errors was tested.

## IDEA?drift-codex-32 — equal-phase negative-witness path

Aliases: equal high-frequency phases; `n*theta=(n+1)*phi`.

- Question/scope: can the points `(cos(alpha/n),cos(alpha/(n+1)))`, alpha real, give P_n<0 for n>=4?
- Mechanism/hypotheses: cancel the phase difference in the generators, seeking a corner witness at an explicit angle.
- Closest entries read in full: IDEA-168/PD-T069, PD-T075; originating candidate IDEA?drift-codex-30.
- Separation criterion/kill test: a strict negative value on this exact path would distinguish it as an upper-witness mechanism; exact nonnegativity on the whole path kills that stated mechanism.
- Literature baseline/search limits: same relaxed gate and source scope recorded above; this is a direct trigonometric test of the known P_n, with no historical novelty claim.
- Applicable obstruction: a positive-Hessian certificate is locally nonnegative; the test must leave its positive locus. This path does not do so.
- Novelty gate verdict: variant with a specified path, now failed within that path; not a new general mechanism.
- Cheapest decisive test/test discriminability: use the exact Chebyshev cosine identities; they decide every real alpha, rather than a finite sample.
- Actual result: `P_n=10*sin^2(alpha)*sin^2(alpha/[n(n+1)])>=0` for every n>=4 and real alpha.
- Disposition: **REJECTED: failed**, solely as a negative-witness path. This says nothing about off-path points or other certificates.
- Canonical negative result: PD-N?drift-codex-32, part 1, `tracks/bivariate-lanczos/theory/drift-codex-e5-32-failed-negative-witness-paths.md`.
- History: considered during E5 corner development; scoped split recorded 2026-11-01 at AC's explicit instruction. Proof/independent audit status is in the negative record.

## IDEA?drift-codex-33 — negative witness on either edge x=1 or y=1

Aliases: positive square-edge paths; sine-sequence edge reduction.

- Question/scope: can `(1,y)`, y in [-1,1], or `(x,1)`, x in [-1,1], supply P_n<0 for n>=4?
- Mechanism/hypotheses: move on these exact edges near the corner and simplify the generators.
- Closest entries read in full: IDEA-168/PD-T069, PD-T075; originating candidate IDEA?drift-codex-30.
- Separation criterion/kill test: strict negativity on one of these edges would supply an explicit witness; an exact nonnegative formula on both stated edges kills this path choice.
- Literature baseline/search limits: same recorded gate; direct test of the known certificate, no historical novelty claim.
- Applicable obstruction: nonnegative values cannot furnish a positivity-radius upper witness. Other edges and off-edge perturbations are outside this test.
- Novelty gate verdict: specified-path variant, failed in the stated ranges.
- Cheapest decisive test/test discriminability: product-to-sum gives `g_m=b*sin(C-m*d)` on either edge and an exact identity for all angles.
- Actual result: `P_n=b^2*[(9/2)sin^2(C-d)+(11/2)sin^2 d]>=0`, with the explicit b,C,d for each edge in PD-N?drift-codex-32 part 2.
- Disposition: **REJECTED: failed** for these two edge loci as negative-witness mechanisms. No rejection of arbitrary boundary or interior paths.
- Canonical negative result: PD-N?drift-codex-32, part 2.
- History: considered during E5 corner development; fully written identity and scoped split recorded 2026-11-01 at AC's explicit instruction.

## IDEA?drift-codex-34 — fixed nonzero A/n^3 common-angle increment

Aliases: coarse common-angle scale; fixed-A corner perturbation.

- Question/scope: for fixed real A!=0, can `(cos(pi/n+A/n^3),cos(pi/(n+1)+A/n^3))` give eventual negative P_n as n tends to infinity?
- Mechanism/hypotheses: move both angles by the same fixed-A/n^3 amount from the `(j,k)=(1,1)` node. A is fixed before the limit; n>=4.
- Closest entries read in full: PD-T069/PD-T075 and originating IDEA?drift-codex-30. The successful a/n^4 refinement is PD-T?drift-codex-30.
- Separation criterion/kill test: a strictly negative asymptotic leading coefficient would make this prescribed scale work. A strictly positive coefficient kills eventual negativity at that fixed A, without excluding n-dependent A_n.
- Literature baseline/search limits: same recorded gate; an asymptotic path test for the known certificate, no historical novelty claim.
- Applicable obstruction: positive dominant terms can hide the finer negative scale. The fixed-A hypothesis is essential; `A_n=a/n` escapes it.
- Novelty gate verdict: quantitative parameter variant, failed under the fixed-nonzero-A hypothesis.
- Cheapest decisive test/test discriminability: exact first/second derivatives and an O(n^3) third-derivative bound determine the n^-10 leading coefficient for every fixed A.
- Actual result: `n^5*g_m->-A^2` for m=0..3, so `n^10*P_n->(9/2)A^4>0`; eventual positivity holds with a threshold depending on A.
- Disposition: **REJECTED: failed** as an eventual negative-witness mechanism for every fixed A!=0. No failure claim for varying A_n, including the successful a/n^4 path.
- Canonical negative result: PD-N?drift-codex-32, part 3.
- History: the positive coarse-scale result prompted the finer successful increment; scoped split recorded 2026-11-01 at AC's explicit instruction.
