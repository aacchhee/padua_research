# PD-T?padua-effective-cubature-20261112-claude-04 — packing cap: D(int 2O) ≤ 38/27, so the Delsarte/Turán route gives γ ≤ 1/18; finite torus LP ≤ lattice-rule counts

ID kind: PD-T (a proved limitation of a method; it is not a refutation of any claim).
Aliases: LP cap; lattice cap; "lattice value 1/18" of frontier S4.
Split from: none. Split into: none.

## Statement

**(a) Continuous.** T(int 2O) ≤ D(int 2O) ≤ 38/27 = (19/18)·|O|. Hence γ_A of record -03 satisfies γ_A ≤ 1/18. The plain-LP constant γ_LP = (3/4)T(int 2O) − 1 satisfies γ_LP ≤ γ_A ≤ 1/18.

**(b) Finite.** Fix n and K ≥ 2n−2. Let L ⊂ ℤ³ be any sublattice with L ∩ {k : 0 < |k|₁ ≤ 2n−2} = ∅. Then every f admissible in record -02 (a) satisfies f(0)/c₀ ≤ [ℤ³ : L]. So the finite torus Delsarte optimum R^Del_{n,K}, and with it the plain optimum R_n, is at most the least such index M_lat(n).

## Status by part

Overall status: **PROVED** (local; exact finite check of the lattice).

| Part | Status | Evidence |
|---|---|---|
| (a) | PROVED | proof below; lattice verified by `../code/cap_critical_lattice.py`, `../evidence/cap-critical-lattice.json` |
| (b) | PROVED | proof below (dual feasibility of lattice rules) |

## Depends on

- Records -02 and -03 (definitions only).
- The lattice Λ = B ℤ³ with basis columns (2/3, 1, 1/3), (−1/3, −2/3, 1), (−1, 1/3, −2/3). Betke–Henk display it as the densest lattice packing of O (LIT-640, Minkowski 1904). **Only the two finite facts below are used, and both are checked locally and exactly; the optimality in LIT-640 is not used.**
  1. |det B| = 38/27.
  2. Every nonzero λ ∈ Λ has |λ|₁ ≥ 2 (the minimum 2 is attained by 14 vectors).

## Proof

**(a).** Let φ be Delsarte admissible for U = int 2O, and first assume φ is compactly supported as in record -02 (b). Put φ_B(η) = φ(Bη). It is continuous and compactly supported, with φ_B(0) = 1, and its Fourier transform |det B|^{−1} φ̂(B^{−T} y) is ≥ 0. Apply the periodization argument of record -02 (b) to φ_B with L = 1. The trigonometric polynomial P(s) = Σ_{k∈ℤ³} φ_B(k) e^{2πik·s} is then ≥ 0 and satisfies P(0) ≥ \hat{φ_B}(0) = |det B|^{−1} ∫φ.

On the other hand, P(0) = Σ_k φ(Bk) = φ(0) + Σ_{λ∈Λ∖0} φ(λ) ≤ 1, since |λ|₁ ≥ 2 places λ outside U. Hence ∫φ ≤ |det B| = 38/27.

The approximation of record -02 (c) extends this to all KLM-admissible φ: ψ_R = φ·g_R has ∫ψ_R → ∫φ and satisfies the compact-support case. So D(int 2O) ≤ 38/27. T ≤ D holds because Turán-admissible functions are Delsarte admissible (KLM §5.2; immediate from the definitions). ∎

**(b).** Write M_L = [ℤ³:L] and L^⊥ = {t ∈ ℝ³ : k·t ∈ ℤ for all k ∈ L}. The set G = 2πL^⊥ mod 2πℤ³ is a finite group of M_L points of 𝕋³, dual to ℤ³/L. So the average of e^{ik·t} over t ∈ G is 1_{k∈L}. Take f admissible in record -02 (a). Then

  (1/M_L) Σ_{t∈G} f(t) = Σ_k c_k 1_{k∈L} = c₀ + Σ_{k∈L∖0} c_k ≤ c₀,

because every k ∈ L∖0 has |k|₁ ≥ 2n−1, so c_k ≤ 0. Since 0 ∈ G and f ≥ 0, the left side is ≥ f(0)/M_L. Hence f(0)/c₀ ≤ M_L. ∎

## Consequences recorded

- In the torus normalisation the plain LP and the Delsarte LP both have value ≤ (19/18 + o(1))·m_n asymptotically. Exact finite values of M_lat(n) are MEASURED/computed in `../evidence/lp-lattice.json`.
- **Packages.** With γ ≤ 1/18 in record -03 (ii), N ≥ (1+γ)(2n−1)³/48 excludes N = binom(n+3,3) only for n ≥ 138. Any route through 8N ≥ M and an LP of these two kinds therefore leaves 4 ≤ n ≤ 137 undecided. This is a proved limitation of these two relaxations combined with the factor-8 conversion, not of every method.
- The S4 remark "the lattice value is 1/18" (`topics/padua-3d-20261106/frontier-2026-11-08/S4.md` L78) is reconciled: 1/18 is exactly this cap.

## Checks

`python -B topics/padua-effective-cubature-20261112/code/cap_critical_lattice.py topics/padua-effective-cubature-20261112/evidence/cap-critical-lattice.json`. It was run by the orchestrator on 2026-11-12 with Python 3.13.18, giving verdict PASS, det −38/27, min nonzero ℓ₁ = 2, and 14 minimal vectors. The enumeration bound is in the script docstring: |c_i| ≤ 2·max row ℓ₁-norm of B^{−1} = 3.

## Scope

This is a limitation of the two LP relaxations as stated, with off-diagonal terms dropped and no separation input. Cohn–Elkies-type use of forbidden differences, SDP/three-point bounds and cube-native relaxations (plan.md §2) are not covered. Nor does it cover a better M ↔ N conversion than 8N ≥ M.
