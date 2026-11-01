# Padua–Lanczos drift campaign report

Rules SHA `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; synchronized main
`806cc7b4509fd93bae652f9545d32d95529f8281`, with unchanged Lanczos inputs and
rules. Draft [PR #15](https://github.com/aacchhee/padua_research/pull/15).
Identifiers below remain provisional. Claude Opus 5.5 xhigh audit is PENDING;
supplementary independent Codex checking does not replace it.

## E1 verdict and E2 drift theorem

**E1's factor-10 comparison in the declared full scalar-rounding model is
INCONCLUSIVE. The aggregate-residual comparison is PROVED with a sharper
certificate; its original KHS-only sufficient test is also INCONCLUSIVE.**
These outcomes remain distinct. All 88 aggregate rational cases ran: degrees
2–12, two grids, four selections. Independent exact reruns confirm the decisive
inequalities. The grids are the uniform 325-point T24 triangle and 625-point
Q24 product grid rotated with rational cosine 3/5 and sine 4/5. Choices are
BJ/dev, mirror, alt staircase and exact pivot-adaptive selections.

The derivative projects out coefficient changes that remain in the polynomial
space. Its input budget is the joint Euclidean norm of preprojection residuals
relative to their product norms; its output is the spectral span graph. This
model is stated separately from a full scalar-operation rounding model.

| Degree-12 set | BJ lower κ² | Good-rule full upper κ² | Certified κ ratio |
|---|---:|---:|---:|
| T24 | 2.0494e14 | 1.6146e8, pivot | greater than 1126 |
| rotated Q24 | 8.8171e10 | 6.4187e8, alt | greater than 11.72 |

The rotated-square original KHS upper gives squared ratio 62.16, below the
sufficient threshold 100; the sharper row bound gives 137.36. The extra
certificate, final-degree clarification and corrected DEAD quantifier are
disclosed in `evidence/e1-freeze.json` and `directions/E1.md`. An improved
certificate is never represented as the original frozen test.

An additional explicitly specified, left-to-right scalar CGS2 graph uses
independent relative operation errors bounded by u. Its normal Jacobian is
derived analytically in record03; dot/coefficient/norm scalar errors lie in
the polynomial quotient kernel, while vector products, updates and divisions
supply the stated local sources. This is a formal upper-bound rounding model;
admissible errors need not be attained by actual IEEE arithmetic.

Exploratory exact finite bounds for that full graph give a triangle squared
BJ/pivot ratio lower bound about 657000 and a rotated-square BJ/alt ratio
lower bound about 62.09. The latter proves a factor greater than 7, but its
intervals do not settle the factor-10 comparison. It is neither a pass at 10
nor a kill of the mechanism. Subset-map upper bounds are not substituted for
full implementation bounds. Record05 labels this finite follow-up MEASURED;
the large raw capacity output remains outside Git, with compact signs/gains,
hashes and a deterministic regeneration/check path.

Analytic **PD-T?drift-codex-01/02** prove the normal-quotient derivative and
rational certificates. The finite certificate and scalar-operation extension
have separate records/evidence in E1. **E2 remains OPEN:** no explicit non-product
family has an all-degree exponential BJ drift lower bound and matching upper
bound in the full required model. Finite ratios, selected scalar channels and
worst-case admissible errors do not prove a theorem about all degrees or actual
IEEE outputs. PD-T053 still supplies a lower bound on the maximum drift over
stages, rather than an a priori all-degree growth theorem.

## Selection principle and universal reorthogonalization

**PD-T?drift-codex-10** proves an a posteriori span certificate using a
polynomial surrogate built from computed recurrence coefficients. It assumes
no coefficient accuracy; the normalized inverse recurrence, local residuals
and smallest singular value of the computed basis enter explicitly.

**PD-T?drift-codex-11** proves a computable filtered minimax criterion over the
2^(s−1) staircase selections and a fixed-degree first-order implication.
Polynomial score bounds, accepted staircases for every degree, a usable
finite-u radius and efficient online selection remain OPEN. Condition (C)
and full reorthogonalization alone have not been proved sufficient.

**PD-T055 remains OPEN in its original scope.** **PD-N?drift-codex-14** refutes
a positive lower bound for every admissible error realization in a model
allowing zero errors. It refutes neither a fixed IEEE implementation nor a
worst-case-over-errors assertion. **PD-N?drift-codex-15** gives a ten-point
triangle, exact degree-one prefix and one degree-two source for which every
rule restricted to prior-vector subtractions has the same drifted span and
nonzero J-closure defect. This is an O(u) aggregate-source obstruction with
fixed parents/products. Exponential growth, parent repairs, implicit-section
accuracy and actual IEEE realization lie outside that result.

## Padua radius and backward interpretation

**PD-T?drift-codex-30 proves PD-T075(U1): ρ_n→0, with ρ_n=O(n^−5).** It is an
analytic upper bound for the named certificate P_n. Put a=20π³/9 and

    ζ_n = (cos(π/n+a/n⁴), cos(π/(n+1)+a/n⁴)).

The proof gives n¹⁴P_n(ζ_n)→−6400π¹²/729 and
limsup n⁵ρ_n≤20√2π⁴/9. No explicit finite threshold or matching lower rate
is claimed. Independent reconstruction checks both derivative identities,
the Taylor remainder, negative limit and distance argument.

**PD-T075(U2) remains OPEN:** the radius uniform over all obstruction
certificates is a different question. The comparison ρ_n≤δ_obs(n) cannot
turn an upper bound on ρ_n into an upper bound on δ_obs(n).

**PD-T?drift-codex-31** gives an explicit square n=1 positive four-atom split:
moment perturbation exactly ε, support spread at most √(6ε), and a √ε lower
bound allowing residual γε, γ<1/3, in a specified fixed-mass moment norm.
At allowance ε, the original measure has radius zero. This makes residual
constants concrete but leaves **PD-T056 reading (G) OPEN**: no actual recurrence
realizing this family with smaller local u is proved. Padua n=3/4 reading (G)
is also unresolved.

## Public Vandermonde-with-Arnoldi code

**PD-T?drift-codex-50 is MEASURED.** Actual unchanged polyrat 0.2.2 numerical
source, commit `6903d7af9995c9d88e661fb229626696e00fdfba`, ran on all twelve L2
benchmarks and both rational grids at degrees 12 and 16. Third-party source
stays outside this repository; URL/version/file hashes are in `external-code.md`.

Upstream `[y,x]` has the campaign dev selection and column order and agrees
entrywise with its implementation here. Default `[x,y]` gives mirror with
reversed within-degree order, which is numerically different from forward
mirror. All parents were checked through degree 47.

| Case | Span gap | Worst-polynomial training relative residual | Test relative error |
|---|---:|---:|---:|
| rotated square, n=24 | 0.004105 | 0.004105 | 0.001014 |
| triangle, n=20 | 0.010164 | 0.010164 | 0.001569 |

A separate root execution reproduced both complete case records exactly.
Gram errors remain below 6.9e−15; polynomial references have condition numbers
about 3778 and 101. These are numerical diagnostics, not rigorous floating
enclosures. The polynomial targets were chosen after inspecting missing span
directions. The independently fixed target exp(x+y) has errors about 2e−15 on
the same hard sets. The finding therefore concerns particular polynomial
directions; it does not establish general failure on smooth data.

Several full-suite references, especially the clustered checkerboard, are
poorly conditioned or numerically rank deficient. Their raw gaps do not
certify exact-space drift. Their off-sample errors retain this separate
conditioning limitation.

BNT's author-attributed public example is univariate and supplies no
two-variable selection; MATLAB execution remains unrun here. An identifiable
public Zhu–Nakatsukasa code source was not obtained in the bounded search.
Code-page denials/search limits are documented; polyrat results do not replace
those missing runs. No new paper fulltext was retrieved or represented as read.

## Remaining obligations

Tighten the declared full scalar-operation comparison if pursuing that route;
its factor-10 result remains inconclusive. The all-degree drift theorem, unconditional selection
theorem, original universal reorthogonalization target, optimal uniform Padua
radius and reading (G) remain OPEN. Claude audit, final-ID assignment/registry
integration and Windows archival/results delivery remain separate acceptance
steps. Literal proposed changes are in `proposed-record-changes.md`; existing
theory files remain unchanged.
