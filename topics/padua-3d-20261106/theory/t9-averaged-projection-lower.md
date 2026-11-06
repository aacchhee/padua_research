# PD-T?padua-3d-20261106-codex-T9-01 — retained-kernel projection lower bound

ID kind: PD-T. Aliases: T9-K; practical all-degree lower bound.
Split from: none. Split into: none. Supports: T9-SQ logarithmic estimate.

## Statement and definitions

Let P:C([-1,1]^d;R)→Π_n^d be a bounded real linear projection,
d≥1,n≥0, where Π denotes total degree. On the probability-Haar torus set

K_n^d(t)=Σ_{k∈Z^d,|k|₁≤n}2^{-s(k)}e^{ik·t}
        =Σ_{α∈N₀^d,|α|₁≤n}∏_j cos(α_jt_j),

where s(k) counts nonzero coordinates. Then ||P||≥||K_n^d||₁.
For d=3,n≥1 this implies

**||P||≥3/4+3/(2π)>1.2274.**

For d=2,n≥1 the corresponding bound is 1/2+2/π>1.1366.
Every total-degree interpolation Lebesgue constant obeys these inequalities.

## Assumptions and status

Overall status: PROVED (analytic developer proof; independent check separately).
No cubature, positivity or geometric node hypothesis. Norms are uniform
operator norm and probability-Haar L1 norm. No sharpness or priority claim.
Candidate disposition: retained quantitative variant of T6.

## Depends on / sources

T6 universal lower proof, steps1–3, reproduced below; no external theorem
used. literature-T9.md records the Subbotin/T6 known-mechanism comparison.

## Proof

Let Jf(t)=f(cos t₁,…,cos t_d), an isometry onto coordinatewise even
continuous torus functions. Its polynomial range is spanned by products of
cosines indexed by |α|≤n. Reflection averaging E has norm1. Thus
Q=JPJ^{-1}E has norm≤||P|| and fixes that cosine space. For translations
τ_u define R=∫τ_{-u}Qτ_u dμ(u), a real bounded operator of norm≤||P||.
This Bochner integral exists because the integrand applied to each continuous
function varies continuously in uniform norm.

Translation averaging retains only the diagonal Fourier coefficient.
For |k|≤n, Ee_k=∏cos(k_jt_j) is reproduced by Q, whose coefficient at k
is2^{-s(k)}; for |k|>n, Q's polynomial range has no k coefficient.
Consequently R is convolution by the real even polynomial K_n^d.
Character calculations use the algebraic complex extension only; the norm
estimate remains on real functions. Density of real trigonometric polynomials
identifies the operators. Convolution has norm exactly||K||₁: the upper
bound is the triangle inequality, and the real continuous inputs
K(-t)/sqrt(K(-t)^2+ε²), evaluated at0 and followed by dominated convergence,
give the lower bound. This proves the first assertion.

For n≥1 average K_n over translations by (2π/n)r, r∈{0,…,n−1}^d.
This is an L1 contraction, retaining frequencies in nZ^d only. Their
intersection with |k|≤n is {0,±ne₁,…,±ne_d}. The averaged polynomial is
1+Σcos(nt_j), whose L1 norm equals that of K_1 by Haar preservation of
the torus covering t↦nt. Hence ||K_n||₁≥||K_1||₁.

For d=3 let B=[π/2,3π/2]^3. Its normalized measure is1/8;
∫_{π/2}^{3π/2}cos t dt/(2π)=−1/π. Therefore
∫_B K_1 dμ=1/8−3/(4π)<0. Since ∫K_1=1,
||K_1||₁≥∫K_1−2∫_B K_1=3/4+3/(2π).
The identical d2 calculation gives∫_B K_1=1/4−1/π and the stated bound.
Interpolation is a projection; its operator norm equals its Lebesgue
constant by extending finitely many nodal signs with continuous bumps.

## Checks / scope / open items

Analytic proof needs no executable premise. t9_checks.py checks constants
and related rational formulas; receipt t9-checks.json is supporting evidence.
This improves the previous coarse practical lower1 but is far from the
optimal constant. A matching O(log³ n) minimal-node interpolation family
and the sharp universal coefficient remain OPEN.

## History

2026-11-06 Codex: retain the T6 averaged multiplier instead of correcting
it with a norm≤27 operator. Finite subgroup averaging supplies an all-n
practical consequence. No original T6 statement or historical stop is changed.
