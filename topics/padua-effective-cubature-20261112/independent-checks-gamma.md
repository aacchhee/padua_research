# Independent check: gamma_1 certificate for the DGOV octahedron function

The checker was a Claude subagent, Opus 5.5 (`claude-opus-5-5`). It worked as an independent verifier with its own code path. This check supplements the cross-agent audit and does not replace it.

- I ran no Git command.
- I did not read `code/gamma_certificate.py`, `code/gamma_ft_check.py`, `evidence/gamma-certificate.json` or the developer's scratch directory.
- I wrote only three repository files: `code/gamma_certificate_indep.py`, `evidence/gamma-certificate-indep.json` and this report.
- I read the rules (AGENTS.md, agents/WORKFLOW.md) in the working tree. `.git/HEAD` → `refs/heads/claude/padua-effective-cubature-20261112` = `889000e65e47934302a7d5b2e0cddb4c66e5dee9`. I read this file directly, without Git.

## Verdict: PASS

All three claims are verified rigorously. The trust base is listed at the end. Every claim was proved with a strict inequality.

| Claim | Result |
|---|---|
| (G) G(u) ≥ 0 on R³ | **Verified** (in fact G > 0). The rigorous lower bound on [0,3]³ is ≥ 0.00203, and the tail is > 0 for max-norm ≥ 3. |
| (P) P(x) ≤ 0 for \|x\|₁ ≥ 1001/1000 | **Verified** (in fact P < 0). The rigorous upper bound is ≤ −2.03e−5 on the bulk and ≤ −3.5e−4 on the face slab, and the tail is < 0. |
| (V) γ₁ = 6G(0)/(α³P(0)) − 1 | **γ₁ ∈ [0.0278415686907765546295935969422 ± 2.6e−32]**. γ₁ − 1/36 ∈ [6.37909129988e−5 ± 2.4e−17] > 0, so γ₁ > 1/36. |

Further values:
- G(0) = ∫f = [1.00000016634359579709980445022 ± 1.1e−30].
- P(0) = c_0_0_0 exactly (5.8199990323245262545…).

## Input

The input is `octa_double.func.cpp`, which I downloaded myself from https://arxiv.org/src/1510.02331v3/anc/octa_double.func.cpp into scratch (not committed).
- SHA-256 `034a1aea4fafbf29743bded0812723ac8c9cf95274225213578145d016a7bc47` matches the expected value.
- It has 123 `c_i_j_k` literals and 123 accumulation lines.

The parser checks the whole function body against the expected structure: the s1, s2, s3 definitions, the `x_pow`/`y_pow`/`z_pow` recurrences, `ret = 0`, and every line `ret += c_i_j_k * x_pow[i] * y_pow[j] * z_pow[k];` with matching indices. Each literal is read as an exact `Fraction`. P has degree 26 and, in x², y², z², 560 monomials. The coefficient tensor p_ijk is checked to be exactly permutation-symmetric.

## Method (independent of the developer's y = x² Taylor-shift approach)

**1. Exact derivation of G.** FT[x^{2m} e^{−πx²}](u) = g_m(u) e^{−πu²}, where g_m(u) = Σ_{l≤m} (−1)^l (2m)!/((2l)!(m−l)!) (4π)^{l−m} u^{2l}. This follows from FT[x^n g] = (i/2π)^n ∂^n ĝ and d^n e^{−πu²} = (−√π)^n H_n(√π u) e^{−πu²}. The transform factorizes over coordinates, so G = Σ p_ijk g_i(u₁) g_j(u₂) g_k(u₃). Each coefficient of G is held exactly as a rational combination of (4π)^{−d}. The G tensor is checked to be exactly permutation-symmetric, and G is even in each variable by construction.

The coefficients were evaluated in python-flint `arb` at 256 bits. Each was then converted to a double plus a rigorous radius, using exact dyadic arithmetic on the arb midpoint and radius.

Numerical sanity checks (not part of the proof):
- The 1D transform by mpmath quadrature matches g_m (m = 1, 3, 6, 13; three values of u each) with maximum relative error 5.8e−27.
- A 90³-node Gauss–Hermite evaluation of f̂ at 5 points matches G(u)e^{−π|u|²} with maximum absolute error 9.5e−14. This includes f̂(0) = 1.00000016634.

**2. Symmetry reduction.** P is a function of the even power sums, and G has the same symmetry. So it suffices to check the region F = {x ≥ y ≥ z ≥ 0}, and |x|₁ is invariant under the same symmetries.

**3. Enclosure.** The enclosure uses tensor-product Bernstein bounds of degree 26 per axis on boxes with nonnegative coordinates, using the convex-hull property. The Bernstein matrices of t^m on [t₀, t₀+w] with t₀ ≥ 0 are sums of nonnegative terms, so rounding has only relative effects. The coefficients are then contracted in three batched matmuls.

The rigorous floating-point error bound (derived in the docstring) is:

E = 1e−13·Σ|c|·hi^m + 1.01·Σρ·hi^m + 1e−250.

- The proved worst-case factor is ≤ 2.9e−14, so 1e−13 has a safety margin of more than 3×.
- ρ is the rigorous coefficient radius.
- The term 1e−250 covers gradual underflow. A multiplier bound is asserted on every call.
- Box endpoints are dyadic, so widths are exact.

A box is accepted for (P) only if max b + E < 0, and for (G) only if min b − E > 0. Unverified boxes are bisected along all three axes.

**4. Face chart (no straddling).** The part of F with α ≤ x+y+z ≤ α+1/8 uses coordinates (σ, y, z) with x = σ + α − y − z and σ ∈ [0, 1/8]. Here Q(σ,y,z) = P(σ+α−y−z, y, z) is expanded exactly in rationals and has 3654 monomials. Every point with σ, y, z ≥ 0 has |x|₁ ≥ x+y+z ≥ α, so each chart box lies inside the domain.

The rest of the domain, F ∩ {x+y+z ≥ α+1/8, x ≤ R}, uses x-space boxes in [0,R]³. These may straddle the plane x+y+z = α+1/8, because P < 0 is required on the whole box. Boxes are discarded only by necessary conditions for meeting the target set, with conservative float slack.

**5. Tails (proved reduction).** In F with x ≥ R, write the point as r(1,v,w) with r ≥ R and 0 ≤ w ≤ v ≤ 1. Set r² = R²(1+t) with t ≥ 0. Then

P = Σ_n t^n K_n(v,w), where K_n = Σ_{d≥n} C(d,n) R^{2d} P_d(1,v,w)

and P_d is the homogeneous part of degree 2d. If K_n < 0 on [0,1]² for every n = 0..13, then P < 0 on the whole tail. The same holds for G with K_n > 0. Each K_n is checked with 2D Bernstein bounds. P's coefficients are exact rationals, and G's are arb balls, so the 2D check carries the same rigorous error term as step 3.

R = 3 suffices for both P and G: every K_n is verified on the initial 1/4-grid. R = 4 also passes. R = 2 fails this sufficient test, for K_1..K_n of P and for G; that is a failure of the test, not a counterexample.

**6. (V).** The γ₁ value is computed in arb from exact rationals and π, using G(0) = Σ p_ijk Π_axes (2m)!/(m!(4π)^m).

## What was executed (this session, 4-core Linux container)

Versions: Python 3.13.18, numpy 2.5.3 (OpenBLAS 0.3.34), python-flint 0.9.0, mpmath 1.3.0. The script SHA-256 is `635077161ada17c14c8e866ba36dc6d90ea971b52f7b47073431a6a4cc826f76`.

**Certificate run** (wall time 5.4 s in total):

```
python3 -I code/gamma_certificate_indep.py --input <scratch>/octa_double.func.cpp \
    --out evidence/gamma-certificate-indep.json          # defaults R = RG = 3
```

| Part | Initial boxes | Processed | Verified | Max depth | Worst verified bound |
|---|---|---|---|---|---|
| P bulk [0,3]³ | 524 | 940 | 855 | 3 | −2.03e−5 |
| P face slab | 15 | 23 | 22 | 1 | −3.54e−4 |
| P tail, R=3, K₀..K₁₃ | | 182 | | | |
| G tail, R=3, K₀..K₁₃ | | 182 | | | |
| G bulk [0,3]³ | 528 | 1244 | 1144 | 4 | +2.03e−3 |

The output is `claims {G: True, P: True, V: True}; verdict PASS`. The receipt is 2.9 KB. The spec expected up to about 2 hours; the run is this fast because degree-26 Bernstein enclosures are already tight at width 1/32 to 1/64.

**Robustness and controls.** Each control is the same script with exact shifts, run with `--only VPTG`, taking 1.7 to 8.2 s of wall time. Each witness is evaluated exactly in rationals, or in arb for G.

| Run | Expected | Observed |
|---|---|---|
| `--R 4 --RG 4` | pass | PASS |
| `--pshift 1/10000` (prove P < −1e−4) | pass | PASS; bulk worst −7.6e−6 |
| `--pshift 1/5000` (prove P < −2e−4) | fail | Fails with exact witness x = (95813631, 95682559, 262143)/2²⁷, \|x\|₁ = 1.4287, P(x) + 2e−4 = +7.58e−5 |
| `--alpha 1` | fail | Fails with exact witness (176193537, 46137343, 46137343)/2²⁸, \|x\|₁ = 1.000122, P = +0.00271 |
| `--gshift 8/100` (prove G > 0.08) | pass | PASS |
| `--gshift 9/100` | fail | Fails with witness (199360511, 175243263, 262143)/2²⁷, G − 0.09 = −0.0032993 (arb) |
| `--R 2 --RG 2` | — | The tail sufficient test fails (see above) |

**Further non-proof audits (scratch scripts).**
- Float Bernstein bounds were compared with exact-rational Bernstein coefficients on 3 boxes. One box was the critical box [0.6875, 0.71875]² × [0, 0.03125], where float ub = −6.2232124e−5 and exact max = −6.2232688e−5; the difference is within E. The other two boxes were [1, 1.25]×[0.25, 0.5]×[0, 0.25] and a far box with \|P\| ~ 5e12. In every case the float enclosure contained the exact one.
- 2000 random points in 400 random boxes showed no enclosure violation.
- For coverage, the verified boxes were recorded. All 433,995 sampled bulk points and 63,580 sampled face-slab points of the domain lay in verified boxes. All 300,000 sampled points of F ∩ [0,3]³ lay in verified G boxes, with no enclosure violations.
- Measured extremes (local optimization; the brackets are rigorous):
  - sup P on the domain ≈ −1.1597e−4, at (0.71333, 0.71333, 0) up to symmetry. Exactly, P(0.71333, 0.71333, 0) = −1.15972e−4. Together with the `pshift 1/10000` run this gives sup P ∈ [−1.1598e−4, −1e−4].
  - min G ≈ 0.086427, at (1.48617, 1.30497, 0) (arb value 0.0864270681529). With the `gshift 8/100` run this gives min G ∈ [0.08, 0.08643].
  - The maximum of P on the face \|x\|₁ = 1.001 is ≈ −6.12e−4, near (0.663, 0.169, 0.169).

## Issues found in the specification

None of them affects the claims:

1. **Hint on max P.** The hint gives max P on the domain as about −1.8e−4 near (0, 0.707, 0.72). The true local maximum near there is at (0, 0.71333, 0.71333) and has value −1.1597e−4, so the actual margin is about 35% smaller than stated. It is still comfortably resolved.
2. **P near \|x\|₁ = 1.** P is positive slightly outside \|x\|₁ = 1 as well as on it: P = +0.0027 at \|x\|₁ = 1.000122, at an exact point. So the 1/1000 slack in α is necessary and not cosmetic. P is negative throughout \|x\|₁ ≥ 1.001.
3. **Tail radius.** R = 3 is enough for the ray-shift tail test; the hint said around 4, and 4 also works.

## Trust base and remaining obligations

The proof relies on the following:
- Python `fractions` and integer arithmetic.
- python-flint/arb for π and the ball enclosures.
- IEEE-754 binary64 round-to-nearest with gradual underflow, the numpy/OpenBLAS defaults with no FTZ/DAZ, for the Bernstein float pipeline.
- The standard bound |fl(Σaᵢbᵢ) − Σaᵢbᵢ| ≤ γ_k Σ|aᵢbᵢ| for any summation order, FMA included.
- The convex-hull property of Bernstein coefficients.
- The written reductions: symmetry, the face chart, and the ray-shift tail lemma.

The code itself must also be correct. That is supported by the exact-arithmetic cross-checks, the coverage audits and the controls above, but it is not formally verified.

No claim depends on the developer's certificate. Nothing remains open for (G), (P) or (V) within this check.
