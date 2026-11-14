# PD-T?padua-effective-cubature-20261112-claude-05 — explicit constant for Theorem A via a certified Delsarte function (target)

ID kind: PD-T. Aliases: E1 explicit γ; certified φ.
Split from: the explicit part of BRIEF §1.7 outcome 2. Split into: record -07 (`explicit-gamma.md`), the general-L¹ explicit constant (Gaussian-type witness). The compact-support statement below is proved in this record (2026-11-13), using -07 (L).

## Statement (target)

Exhibit an explicit φ satisfying record -02 (b) (continuous, compactly supported, φ(0)=1, φ ≤ 0 for |ξ|₁ ≥ 2, φ̂ ≥ 0) with ∫φ = (4/3)(1+γ₁), γ₁ > 0 explicit and rigorously certified. Then record -03 gives, for every n ≥ 1, N ≥ (1+γ₁)(2n−1)³/48, and an explicit n₀(γ) for each γ < γ₁.

A sufficient finite route: a certified torus Delsarte polynomial at a single level L converts into such a φ. One construction: ψ(ξ) = Σ_k c_k B(ξ − k), with B = 1_P ∗ 1_{−P} for a fundamental domain P of ℤ³, rescaled. It gives (3/4)∫φ = 6R^Del/(2L+r)³ = ρ^Del_L·6m_{L+1}/(2L+r)³, with 6m_{L+1} = (2L+1)³ + 5(2L+1). Here r is the ℓ₁-diameter of P, i.e. the ℓ₁-radius of P − P (r ≥ 6^{1/3} ≈ 1.817 by Brunn–Minkowski), and ρ^Del_L = R^Del/m_{L+1} at level n = L+1. A conservative sufficient condition is ρ^Del_L ((2L+1)/(2L+r))³ > 1. It is neither the exact loss nor a necessary condition. *(Wording corrected 2026-11-13, audit-01 A4/T2; the previous text said the construction "loses" exactly this factor and that the level "must" satisfy it.)*

## Status

Overall status: **PROVED (computer-assisted, local)**, 2026-11-13. The target statement above is met as written, with the explicit compactly supported witness ψ_R below (R = 10⁵), γ₁ ≥ 0.0278115 > 1/36.

**Status history (kept).**
- 2026-11-12, session 1: OPEN. Existence of some admissible φ with ∫φ > 4/3 was proved (record -03 (i), LITERATURE-dependent); an explicit certified one was not.
- 2026-11-12, explicit-γ campaign: marked "CLOSED by record -07". That was premature. Record -07's witness is Gaussian-type, not compactly supported, and the qualitative cutoff of record -02 (c) supplies no explicit certified cutoff. Audit-01 A1 / T1 found this; the status was not an allowed epistemic status.
- 2026-11-13, response-01: PROVED by the explicit compact-support construction below.

## Theorem (compact-support witness)

Let φ be the record -07 function, φ(ξ) = f(αξ/2)/f(0) with f = P·e^{−π|x|²} and α = 1001/1000, so that γ₁(φ) := (3/4)∫φ − 1 ≥ 0.0278415686907 (record -07 (L)).

Let β = (3/2)·M₄ with M₄ = 1_{[−1/2,1/2]}^{∗4} the centred cubic B-spline. Put g(η) = Π_{i=1}^3 β(η_i) and ψ_R(ξ) = φ(ξ)·g(ξ/R). Then for R = 10⁵:
- ψ_R satisfies record -02 (b): it is continuous, supported in [−2R, 2R]³, ψ_R(0) = 1, ψ_R ≤ 0 for |ξ|₁ ≥ 2, and ψ̂_R ≥ 0;
- (3/4)∫ψ_R − 1 ≥ 0.02781152574 > 1/36.

**Proof.**
- **Properties of β.** M₄(0) = 2/3, so β(0) = 1. Moreover 0 ≤ β ≤ 1, supp β = [−2,2] and β̂ = (3/2)·sinc⁴ ≥ 0, where sinc(ω) = sin(πω)/(πω).
- **Quadratic bound.** 1 − β(t) ≤ (3/2)t² for all t:
  - for |t| ≤ 1, β(t) = 1 − (3/2)t² + (3/4)|t|³;
  - for |t| ≥ 1, 1 − β(t) ≤ 1 ≤ t².
- **Product bound.** Since every factor lies in [0,1], 1 − g(η) ≤ Σ_i(1 − β(η_i)) ≤ (3/2)|η|².
- **Admissibility.** ψ_R is a product of continuous functions and is compactly supported. ψ_R(0) = φ(0) = 1. ψ_R ≤ 0 wherever φ ≤ 0, because g ≥ 0. Finally ψ̂_R = φ̂ ∗ (R³ĝ(R·)) ≥ 0, since φ̂ ≥ 0 is integrable (Schwartz) and ĝ = Πβ̂ ≥ 0 is integrable.
- **Integral.** ∫ψ_R = ∫φ − ∫φ(1−g(·/R)) ≥ ∫φ − (3/(2R²))∫|φ(ξ)||ξ|²dξ.
- **Second-moment bound.** By the change of variables x = αξ/2,

  ∫|φ||ξ|² = (2/α)⁵ P(0)^{−1} ∫|P(x)||x|²e^{−π|x|²}dx ≤ (2/α)⁵ P(0)^{−1} Σ_a |p_a| Σ_i m(a + e_i),

  where P = Σ_a p_a x^{2a} and m(b) = ∫x^{2b}e^{−π|x|²}dx = Π_i (2b_i − 1)!!/(2π)^{b_i}.
- **Evaluation.** `../code/gamma_compact.py` evaluates this in Arb from the exact coefficients. The bound is ∫|φ||ξ|² ≤ 267048.437, so the loss is (3/4)(3/(2R²))·267048.437 ≤ 3.0043·10⁻⁵ at R = 10⁵. There are two separate calculations:
  - **Coarse, from the rounded loss:** (3/4)∫ψ_R − 1 ≥ γ₁ − 3.0043·10⁻⁵ ≥ 0.0278115256 > 1/36. The subtraction is 0.027811525690…, so 0.0278115256 is a safe rounding.
  - **Precise, from the receipt:** with the Arb loss bound 3.00429491…·10⁻⁵, the lower bound is 0.0278115257416687…. This supports the 0.02781152574 stated in the theorem.

  *(Display corrected 2026-11-13, audit-02 B2: the earlier one-line chain ended at 0.0278115257, which the coarse subtraction does not support.)* ∎

**Run.** 2026-11-13, PASS:

  `python3 -B code/gamma_compact.py --anc <scratch>/octa_double.func.cpp --gamma-receipt evidence/gamma-certificate.json --R 100000 --out evidence/gamma-compact.json` (cwd = topic directory).

The receipt is `../evidence/gamma-compact.json`. γ₁ is read as the certified lower end of the revised -07 receipt, minus 10⁻⁴⁰.

**Depends on.** Record -07 (L) (computer-assisted, local; developer and independent checkers) and record -02 (b). The cutoff argument is elementary.

## Plan and obligations (session 1; historical)

1. Measure ρ^Del_{n,K} for n ≤ 12–16 (by `../code/lp_torus.py`) and estimate D(int 2O)/|O| (MEASURED only). Done in part, session 1: ρ^Del ≈ 1.08 at n = 5…8 with K = 3n−2 (`../evidence/lp-torus.json`); this is a finite-n value, below the finite lattice caps and not an estimate of the limit (`../gates.md` Q2).
2. If the measured excess is ≳ 0.01, solve the continuous problem directly in a parametric class, e.g. φ = p·(1_A ∗ 1_{−A}) combinations or B3-symmetric splines on a fine grid with φ̂ ≥ 0 checked analytically. Certify φ̂ ≥ 0 with exact or interval arithmetic and an analytic tail bound.
3. Independent rerun of the certificate (Q3).

## Scope

γ ≤ 1/18 by record -04, so no finite exclusion below n = 110 can follow from any such φ (record -03 (iv), exactness 2n−1 form). With the certified γ₁ > 1/36, packages are excluded for n ≥ 218 (record -07 (d)). The compact witness is not needed for that conclusion, since record -02 (c) admits general L¹ functions; it meets the target as originally stated.
