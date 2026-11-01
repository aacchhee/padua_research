# Focused independent re-audit: L3 residual conventions

**Verdict: CLEAN within the scope below. LF-M1 is resolved.** The corrected T302(b1)–(b4) keep the perturbation/reference/approximant conventions consistent. The full-space and fixed-mass residual thresholds, the comparison of their inradii, and the normalization factors are valid. N309 correctly preserves the old claim's refutation and proves the new explicit positive-radius range. The T303 and N302 rate transfers are valid with fixed theta and constants depending on the convention. No unresolved mathematical finding remains in this subaudit.

Auditor: Codex, explicitly assigned `gpt-6-astra`, effort `xhigh`; these are launch assignments, not independently exposed runtime metadata. Date: 2026-11-01 UTC. Rules/head supplied by the coordinating auditor: `50b0d304001b48607527e5086a67045f534d9472`; scientific response candidate: `075d4074017445a0fd4d7443ffac97cd7f8c106b`; baseline completed audit: `5f523313b7b388cb114103734028f0a850dfeaad`. No Git operation or developer edit was performed by this subauditor. Current hashes of all four mathematical files below match `response-01.md`; the checker and original output match the L3 response's hashes. Full input/artifact identities are in [L3-conventions/manifest.json](L3-conventions/manifest.json).

## Scope, reads, and dispositions

Read current `AGENTS.md`, `agents/WORKFLOW.md`, and `agents/codex/CODEX.md`; `response-01.md` including the impact map; `directions/L3/response-audit-01.md`; `SPLITS.md`; current T302, T303, N309 and N302 in full; the new `t302b_conventions_check.py` in full and its execution evidence; the relevant updated passages of report.md, L3 SUMMARY and candidates. Prior full reads of `state/IDEAS.md` and `literature/INDEX.md` were reused after verifying both files are byte-identical to audit-01 (hashes in the manifest). This is a repair audit of existing claims, not a priority or novelty investigation. No external literature claim is newly verified.

| Prior finding or new obligation | Disposition |
|---|---|
| LF-M1: normalization mismatch in the old residual criterion | **Resolved.** T302:16–25 and 35–39 separate R1, R2 and R3; proofs at 77–86 respect those choices. Old wording and refutation are retained in History and N309. |
| New mass-slice criterion and comparison constants | **Verified.** Both directions, the fixed-mass necessity, finite infimum, zero case and small-radius equivalence reconstructed below. |
| New N309 radius `0 <= delta <= 10^-8` | **Verified independently**, including strict inequality at the upper endpoint. |
| T303 residual/mass-slice propagation, N302 residual variant | **Verified.** Transfers change constants, retain the fixed-degree rate exponents, and preserve the small-perturbation/positivity requirements. |
| LF-R1/LF-R2 report-level overstatement and incorrect annihilator paraphrase | **Resolved in the inspected current passages:** report.md:11,23,27; L3 SUMMARY:11–24. Reading G remains OPEN and the rate cases use S0, S1 and H. |
| LF-M2; new T316–T318; LC-M1/new T319; broader stale-pointer audit | Assigned to the companion re-audit/coordinator; no independent blanket disposition is made here. No unaffected certificate reruns were performed. |

The N309 scoped negative record, corrected T302 disposition, explicit original wording, and SPLITS mapping preserve the refuted claim without downgrading the surviving full-cone theorem. The global ID/registry steps remain the coordinator's PR-preparation responsibility.

## Independent mathematical reconstruction

Write `L=L_mu`, `C=C(K_delta)`, and `C*=Pos(K_delta)`. The cone is closed because its compact generating evaluations all have value 1 on the constant polynomial. In finite dimensions, every functional in C is a finite positive cubature formula. These previously audited facts justify passing between measures and functionals throughout.

**T302(b1), R1.** For a closed epsilon-ball centered at L to lie in C, every `p in C*` must satisfy `L(p) >= epsilon ||p||_*`; this is exactly `r >= epsilon`. A minimizing unit-dual-norm p exists. A negative norming functional E of norm epsilon gives `dist(L+E,C) >= epsilon-r`. If `r >= (1-theta)epsilon`, the single construction `L' = L+(1-theta)E` lies in C and has residual `theta ||E|| <= theta epsilon`. If the radius inequality fails strictly, the norming functional gives a residual strictly greater than the budget. This establishes both directions with the same constant and with unnormalized reference and free-mass approximants. For `epsilon <= epsilon_1` the entire perturbation ball has positive moment matrix, as required to interpret the functionals as sections.

The monotone-threshold statement uses only monotonicity of r. If `delta > inf{d:r(d)>=epsilon}`, an eligible radius strictly below delta exists; if delta lies strictly below that infimum, it is ineligible. No unsupported assertion at equality `delta=delta*` is made. The empty eligible set has the usual extended-real infimum `+infinity`. At epsilon=0 the original measure is feasible.

**T302(b2), R2.** Restriction of a polynomial functional to `H0={E:E(1)=0}` has dual norm `|p|_0 = inf_t ||p-t||_*`. The infimum is attained, constants are its only kernel, and a norming E in H0 exists. Thus the exact mass-preserving ball criterion is `L(p) >= epsilon |p|_0` for all nonconstant nonnegative p. Positive constants impose no further restriction. This is precisely the stated infimum defining r0; the proof needs no attainment of that infimum. It is finite for every finite delta: choose any nonconstant linear polynomial and add a sufficiently large constant to make it nonnegative on compact K_delta.

Sufficiency of the residual threshold again uses `L' = L+(1-theta)E`; it has mass m and, when `epsilon <= epsilon_1`, positive moment matrix. For necessity choose `p in C*` with `|p|_0=1` and `L(p)<(1-theta)epsilon`, and a negative norming E in H0. Every mass-m approximant yields `D=L'-L-E in H0`, so `||D|| >= D(p)/|p|_0 > theta epsilon`. This last step requires the fixed mass of the approximant. The fresh checks explicitly demonstrate why dropping that condition changes the threshold.

**Comparison constants.** Since `|p|_0 <= ||p||_*` and `L(p)>=0` on C*, `r<=r0`. For `|p|_0=1`, let t attain the quotient norm. At every original node, `|p(z_i)-t|<=||ev_zi||`, while `0<=p(z_i)<=L(p)/w_min`. Consequently

`||p||_* <= 1+||1||_* max_i||ev_zi|| + (||1||_*/w_min)L(p) = A+B L(p)`.

The function `g(s)=s/(A+Bs)` is increasing on nonnegative s, giving the lower bound g(r0) for nonconstant p. Positive constants have ratio `m/||1||_* >= 1/B > g(r0)` and therefore do not invalidate it. Hence `r0/(A+B r0) <= r <= r0`, including r=r0=0. Conversely, when `Br<1`, rearrangement gives `r0 <= Ar/(1-Br)`. In particular, for `Br<=1/2`, `r <= r0 <= 2Ar`; this proves the claimed rate equivalence as either radius tends to zero, with explicit fixed constants and no hidden dependence on delta.

**T302(b3), R3.** The bound `epsilon ||1||_* < m` makes the normalization factor positive and bounds it between `m/(m+epsilon||1||_*)` and `m/(m-epsilon||1||_*)`. Homogeneity of C gives the exact identity `dist(s_E(L+E),C)=s_E dist(L+E,C)`. Combining this with (b1) gives the stated upper and lower factors, including theta=0. As customary when writing Phi, its section interpretation applies on its defined domain `M_n(L+E)>0`; the functional scaling identity itself needs only positive mass. Optional editorial precision: T302:23 could explicitly append “when Phi is defined,” or `epsilon<=epsilon_1`, to the phrase “representative of the section pair.” The existing “Section data” framing and T301 domain already impose this restriction; this is not an unresolved mathematical finding. Positive mass alone should not be used elsewhere as a proof of moment-matrix positivity.

**T302(b4).** The chart is the mass-m slice, with `Psi=m Phi^{-1}-L`. Local Lipschitz constants in both directions can be chosen on a neighborhood small enough that `c1 eta0 <= epsilon_1`. The first inequality maps a section ball into an H0 ball of radius c2 eta, proving sufficiency; the second maps a separating H0 perturbation of radius c1 eta into the section ball, proving necessity. No exact constant is asserted after this change of norm. Choosing the neighborhood within the positive-moment domain is part of the local chart construction.

**T303 and N302 propagation.** T303:71 correctly transfers the positive interior radius, linear/quadratic rates and zero-radius obstruction using the comparison above. For fixed `theta<1`, replacing epsilon by `(1-theta)epsilon` preserves exponents; in R3 the factors tend to 1 as epsilon tends to zero. N302:44 makes these transfers explicit. Its R3 choice gives `r <= (1-theta)epsilon/8` and hence the weaker usable estimate `epsilon-r >= epsilon(1+theta)/2`; the stated smallness condition then makes the scaled residual exceed `theta epsilon`. R2 uses `r0<=2Ar` when `Br<=1/2`. All constructed perturbations may be restricted to sufficiently small epsilon to ensure Phi is defined. The resulting lower bound is worst-case over perturbations, not a claim that every perturbation requires square-root support spread.

## New independent check of N309

The ten evaluation vectors for the integer triangle of degree 3 have Vandermonde determinant 576. In their Euclidean coordinates the cone at delta=0 is the nonnegative orthant. The original weights and negative coordinate perturbation give all three stated positive leading minors, unnormalized distance `999/1000000`, and normalized distance `1/999`. These numbers were rebuilt independently rather than imported from the developer output.

The relevant Lagrange polynomial is explicitly `q(x,y)=xy(3-x-y)`. Its gradient is bounded in Euclidean norm by the sum of absolute component bounds, 120, on `[-1,4]^2`. Thus `p_delta=q+120 delta` is nonnegative on K_delta for `delta<=1`, and the dual separation lower bound is

`(1/999-120 delta)/(1+sqrt(10)120 delta)`.

For an independent rational verification use `sqrt(10)<16/5`. At delta=`1/100000000`, the resulting weaker rational lower bound is `12485015/12487547952`. Its gap above `theta epsilon=1999/2000000` is exactly

`463852747/1560943494000000 > 0`.

The bound decreases with delta and its numerator stays positive throughout the interval. Therefore the strict separation holds at every `delta in [0,10^-8]`, including both endpoints. Meanwhile `r(delta)>=r(0)>(1-theta)epsilon`, so this range genuinely contradicts the old normalized factor-1 sufficiency criterion. N309 is a valid scoped refutation; it makes no claim of an optimal failure radius.

## Executions and evidence

Both commands were actually run from `/workspace/padua_research`, with exit code **0**:

```
python3 -I tracks/bivariate-lanczos/code/L3/t302b_conventions_check.py > topics/bivariate-lanczos-20261031/audit-02/L3-conventions/developer-check-rerun.log 2>&1
python3 -I topics/bivariate-lanczos-20261031/audit-02/L3-conventions/independent_conventions.py > topics/bivariate-lanczos-20261031/audit-02/L3-conventions/independent-check.log 2>&1
```

The first is a fresh execution of developer code, not an independently written implementation. Output ends `ALL CHECKS PASS: A,B,C,D` and is byte-identical to the committed developer log, SHA256 `b829dd853361bf2af7c3bbb9d60b5f31c991bcd6a3fd161cba26eec5419c2039`. Its source SHA256 is `f8ad12db997a6c597bf3efd21bf4a1785e30ba29b63a582dbd01e9790f2c0d50`. The decisive comparisons use Python integer/Fraction arithmetic. Inspection nuance: the 500 random-direction illustrations use a floating-point initial scale followed by an exact rational correction and exact assertions; they are supplemental illustrations, not a general proof or the basis of the explicit-radius certificate.

The second is an independent implementation importing no project code or evidence data. Trusted arithmetic dependency: SymPy exact rational/symbolic operations. It reconstructs the moment and Vandermonde calculations, proves the positive-radius gap by the different rational upper bound above, and certifies simplex projections using explicit normal-cone inequalities rather than the developer's sorting routine. It checks exact threshold equality and strict failure immediately above the threshold for theta `0,1/2,9/10`, for both the full cone and mass slice. It verifies the r/r0 comparison and R3 scaling bound. Output ends `ALL INDEPENDENT CHECKS PASS`.

The fixed-mass distinction is reproduced exactly on the same perturbation:

`free-mass distance^2 = 2601/2500000000 <= budget^2 = 10201/9000000000 < fixed-mass distance^2 = 289/250000000`.

These finite checks supplement the general proof reconstruction; they are not evidence for an untested universal statement. No broad unchanged Favard, Padua or checkerboard certificate rerun was needed or performed. Environment and exact source/output hashes, sizes and retention notes are recorded in the manifest. Local evidence remains in the owned audit directory; the coordinator owns staging and repository-wide artifact-budget checks.

## Remaining limits

This clean result covers the convention repairs, their explicit counterexample and the inspected rate/scope propagations. It does not solve G, improve degree-uniform conditioning, establish an optimal counterexample radius, re-audit literature priority, or approve the companion agent's new formula/split/radius-uniformity scope. No additional execution is required for the claims verified here.
