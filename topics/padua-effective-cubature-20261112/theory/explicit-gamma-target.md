# PD-T?padua-effective-cubature-20261112-claude-05 — explicit constant for Theorem A via a certified Delsarte function (target)

ID kind: PD-T. Aliases: E1 explicit γ; certified φ.
Split from: the explicit part of BRIEF §1.7 outcome 2. Split into: none yet.

## Statement (target)

Exhibit an explicit φ satisfying record -02 (b) (continuous, compactly supported, φ(0)=1, φ ≤ 0 for |ξ|₁ ≥ 2, φ̂ ≥ 0) with ∫φ = (4/3)(1+γ₁), γ₁ > 0 explicit and rigorously certified. Then record -03 gives, for every n ≥ 1, N ≥ (1+γ₁)(2n−1)³/48, and an explicit n₀(γ) for each γ < γ₁.

A sufficient finite route: a certified torus Delsarte polynomial at a single level L converts into such a φ. One construction: ψ(ξ) = Σ_k c_k B(ξ − k), with B = 1_P ∗ 1_{−P} for a fundamental domain P of ℤ³, rescaled. It loses a factor ((2L+1)/(2L+r))³, where r is the ℓ₁-diameter of P, i.e. the ℓ₁-radius of P − P (r ≥ 2(3/4)^{1/3} ≈ 1.817 by Brunn–Minkowski; corrected after independent check note). Here ρ^Del_L = R^Del/m_{L+1} at level n = L+1. Hence the level must satisfy ρ^Del_L ((2L+1)/(2L+r))³ > 1.

## Status

Overall status: **OPEN**. Existence of some admissible φ with ∫φ > 4/3 is proved (record -03 (i), LITERATURE-dependent); an explicit certified one is not.

## Plan and obligations

1. Measure ρ^Del_{n,K} for n ≤ 12–16 (by `../code/lp_torus.py`; pending) and estimate D(int 2O)/|O| (MEASURED only).
2. If the measured excess is ≳ 0.01, solve the continuous problem directly in a parametric class, e.g. φ = p·(1_A ∗ 1_{−A}) combinations or B3-symmetric splines on a fine grid with φ̂ ≥ 0 checked analytically. Certify φ̂ ≥ 0 with exact or interval arithmetic and an analytic tail bound.
3. Independent rerun of the certificate (Q3).

## Scope

Even if completed, this gives γ ≤ 1/18 (record -04) and no finite exclusion below n = 138.
