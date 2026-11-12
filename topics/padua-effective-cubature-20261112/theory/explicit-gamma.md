# PD-T?padua-effective-cubature-20261112-claude-07 — explicit constant: γ_A ≥ 1/36, so N ≥ 37n³/216 for every positive closed-cube rule exact on Π_{2n−1}

ID kind: PD-T.
Aliases: explicit Theorem A; explicit γ; certified Delsarte function for the octahedron.
Split from: target record -05, which this completes in LITERATURE-dependent form.
Split into: none. The local re-verification is part (L) below.

## Statement

**(a)** D(int 2O) ≥ (4/3)·(1/b) with b = 0.972912750. Hence γ_A = (3/4)D(int 2O) − 1 ≥ 1/b − 1 > 0.02784 > 1/36.

**(b)** Every positive cubature rule for the normalized product Chebyshev measure on [−1,1]³ with all nodes in the closed cube satisfies:
- if it is exact on Π_{2n−1}: N ≥ (37/36)·n³/6 = 37n³/216, for every n ≥ 1;
- if it is exact on Π_{2n−2}: N ≥ (37/36)(2n−1)³/48, for every n ≥ 1.

**(c) Explicit Theorem A.** For rules exact on Π_{2n−1}:
- N ≥ (1+γ)·binom(n+2,3) whenever 37n³ ≥ 36(1+γ)n(n+1)(n+2). In particular N > binom(n+2,3), strictly above the classical bound, for every n ≥ 109.
- For each γ < 1/36, the explicit n₀(γ) is the least n from which 37m² ≥ 36(1+γ)(m+1)(m+2) holds for every m ≥ n. For example, γ = 1/72 gives n₀ = 220 (Checks).

**(d) Packages.** No positive Padua package (N = binom(n+3,3), exact on Π_{2n−1}, nodes in the closed cube) exists for any n ≥ 218.

**(e) Consistency.** 1/36 ≤ γ_A ≤ 1/18 (record -04).

## Status by part

Overall status: **PROVED with explicit LITERATURE dependency** (computer-assisted literature certificate). Part (L), the local re-verification of that certificate, is **in progress**; see Open items.

| Part | Status | Evidence |
|---|---|---|
| (a) | PROVED with LITERATURE dependency | DGOV Table 6 and §6 (LIT?…-claude-02); local transcription below |
| (b) | PROVED given (a) | record -03 (ii), (ii′) |
| (c), (d) | PROVED given (b) | exact integer arithmetic (Checks) |
| (e) | PROVED | record -04 (a) |
| (L) local certificate | OPEN (campaign rounds 2+) | `../attempts/E1-gamma.md` |

## Depends on

- Records -02 (c), (d) and -03 (ii), (ii′), which are local.
- **LITERATURE: Dostert–Guzmán–de Oliveira Filho–Vallentin, arXiv:1510.02331v3** (LIT?…-claude-02). Used is their rigorous, computer-assisted claim (§6, Table 6) that there is a continuous L¹ function f with f̂ = g·e^{−π‖u‖²}, g a polynomial and:
  - g(0) ≥ 1;
  - f̂ ≥ 0;
  - f(x) ≤ 0 for |x|₁ ≥ α = 1.001;
  - α³f(0)/6 = 0.972912750 to the printed nine digits.
  
  Their K−K is {|x|₁ ≤ 1}, so vol K = 1/6. Their ancillary `README_SOSChecking` states the bound as F[g](0)·vol K·α³. Rounding: we use only b ≤ 0.972913, which is safe whatever the rounding direction of the ninth digit.

## Proof

**(a).** Let f be the DGOV function. Put φ(ξ) = f(αξ/2)/f(0). Note f(0) > 0, since f(0) = b·6/α³.
- φ is continuous, real and in L¹, with φ(0) = 1.
- If |ξ|₁ ≥ 2, then |αξ/2|₁ ≥ α, so φ(ξ) ≤ 0.
- φ̂(u) = (2/α)³ f̂(2u/α)/f(0) ≥ 0.

So φ is Delsarte-admissible for int 2O in the sense of record -02 (c), and

  ∫φ = φ̂(0) = (2/α)³ g(0)/f(0) ≥ 8/(α³f(0)) = (4/3)/b.

Hence D(int 2O) ≥ (4/3)/b and γ_A ≥ 1/b − 1. With b ≤ 0.972913, 1/b − 1 ≥ 0.0278411 > 1/36 = 0.0277…, by exact rational comparison.

**(b).** Record -02 (d) with E = 2n−1 gives N ≥ n³D(int 2O)/8 ≥ n³(4/3)(37/36)/8 = 37n³/216. With E = 2n−2, record -02 (c) gives N ≥ (n−½)³(4/3)(37/36)/8.

**(c)** follows from (b), since binom(n+2,3) = n(n+1)(n+2)/6. **(d)** follows from (b), since binom(n+3,3) = (n+1)(n+2)(n+3)/6, by the arithmetic below. ∎

## Checks

- **Package threshold (d).** The condition is 37n³ > 36(n+1)(n+2)(n+3), i.e. n³ − 216n² − 396n − 216 > 0. Exact values:
  - n = 218: 37·218³ = 383328584 > 383320080 = 36·219·220·221;
  - n = 217: 378077581 < 378116640.
  
  The cubic has one sign change, hence one positive root, in (217, 218).
- **Fisher crossover (c).** The condition 37n² > 36(n+1)(n+2) is n² − 108n − 72 > 0. At n = 109: 439597 > 439560. At n = 108 it fails.
- **n₀(1/72).** The condition 74m² ≥ 73(m+1)(m+2) is m² − 219m − 146 ≥ 0, whose root is ≈ 219.7. Hence n₀(1/72) = 220. Exact check: 74·220² = 3581600 ≥ 73·221·222 = 3581526, while 74·219² = 3549114 < 73·220·221 = 3549260.
- **Consistency.** 1/36 < 1/18 (G4). At n = 3, (b) gives N ≥ 37·27/216 = 4.625, consistent with the 20-node D3 rule.
- **Numerical reproduction (MEASURED).** From the ancillary F[g] coefficients: F[g](0) = 5.8199990323 and g(0) = 1.00000017 (exact transform, floating evaluation), so α³F[g](0)/(6g(0)) = 0.9729128. See LIT?…-claude-02.

## Scope

- Positive weights; nodes in the closed cube; Chebyshev product measure.
- No finite n < 218 is decided for packages. The uniform method cannot decide n ≤ 109 (record -03 (iv)), and the torus LP cannot either (record -06).
- 110 ≤ n ≤ 217 remains OPEN: excluded if γ_A is larger than the certified 1/36, but not decided by this record.
- The certified value is not the optimum of the Cohn–Elkies/Delsarte LP for O; DGOV's class has degree 26.

## Open items

- **(L) Local certificate.** Re-verify the DGOV function locally from its ancillary coefficients, on separate code paths:
  - f̂ ≥ 0, i.e. g ≥ 0 on ℝ³;
  - F[g] ≤ 0 on {|x|₁ ≥ α′};
  - the exact value.
  
  A success turns (a) into PROVED (computer-assisted, local); see gates.md addendum G.
- Improve 1/36 toward the cap 1/18 with a better certified φ (optional).

## History

2026-11-12, Claude (Opus 5.5 xhigh, orchestrator). Explicit-γ campaign round 1 (AC authorised up to seven rounds). Codex audit pending.
