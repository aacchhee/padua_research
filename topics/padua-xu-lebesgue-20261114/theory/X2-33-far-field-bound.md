# PD-T?padua-xu-lebesgue-20261114-claude-33 — far-field bounds for the Morrow–Patterson Lebesgue function and localization of its maximizers near the vertices

ID kind: PD-T.
Aliases: X2-33; far-field bound; localization of the MP argmax; step P4 ("outside the windows") of the X2-28 plan, with explicit constants.
Split from: X2-28 plan item P4.
Split into: none.

## Statement

Let n ≥ 2 be even, M = n + 2, L := log M, and Γ_M := (1 + 1/M)(2 + L)(5 + 2L). For all θ₁, θ₂ ∈ (0, π):

(a) **Interior bound.** λ_n(cos θ₁, cos θ₂) ≤ Γ_M / (sin θ₁ sin θ₂).

(b) **Edge-layer bound.** λ_n(cos θ₁, cos θ₂) ≤ (π/2)(2M+1) Γ_M / sin θ₁ and λ_n(cos θ₁, cos θ₂) ≤ (π/2)(2M+1) Γ_M / sin θ₂. By continuity the first holds also for θ₂ ∈ {0, π} and the second for θ₁ ∈ {0, π}.

(c) **Localization.** Put ϑ_n := (π/2)(2M+1)Γ_M/(c* n²) with c* the constant of X2-25. If (x, y) = (cos θ₁, cos θ₂) ∈ Q satisfies max(sin θ₁, sin θ₂) > ϑ_n, then λ_n(x,y) < c* n² < λ_n(1,1) ≤ Λ_n. Hence every maximizer of λ_n on Q satisfies sin θ₁ ≤ ϑ_n and sin θ₂ ≤ ϑ_n, i.e. it lies in one of the four vertex boxes {θ̂₁ ≤ arcsin ϑ_n, θ̂₂ ≤ arcsin ϑ_n}, θ̂ := min(θ, π − θ). ϑ_n is decreasing in n, ϑ_n < 1 for every even n ≥ 1030, and ϑ_n ≤ 21.5·log²(n+2)/n for n ≥ 1030; in particular the maximizers lie within angular distance O(log² n / n) of the vertices.

(d) **Lattice-sum lemma (tool).** For all real u₀, v₀: Σ_{r=0}^{2N−1} m(u₀ − (2M+1)hr) m(v₀ − hr) ≤ (M+1)²(2 + L)(5 + 2L), where N = M(M+1), h := π/(2N), m(γ) := min(M+1, 1/|sin γ|).

## Definitions

As in X2-21. D_M(α,β) := Σ_{(k,l)∈ℤ², |k|+|l|≤M} e^{i(kα+lβ)} (diamond Dirichlet kernel, = 4Φ_M of X2-21 Lemma 1). 𝔡_k(γ) := sin(kγ)/sin γ. ‖γ‖ := dist(γ, πℤ).

## Assumptions

n even, n ≥ 2. (c) uses X2-26 (λ_n(1,1) > c*n²).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (d) lattice-sum lemma | PROVED | below |
| (a), (b) | PROVED | below; constants are crude (measured λ/bound ≤ 0.12 resp. ≤ 0.008 on grids) |
| (c) localization | PROVED | (b) + X2-26 |

Candidate / claim disposition: none.

## Depends on

X2-21 Lemma 1 (closed form of the diamond sum), X2-21 definitions; X2-26 for (c).

## Checks

- `python3 code/mp/research/x2r3_checks.py transl` (mpmath 30 digits, n = 2, 4, 6): four-term diamond formula (K1) against the kernel double sum at all nodes, two points: max error 3.0e−29; rotated product form (R) of D_M: 1.2e−29.
- `python3 code/mp/research/x2r3_checks.py farfield` (float64; angle grids 41² (n ≤ 100), 25² (n = 200) on [0.02, π−0.02]²): max λ_n/bound(a) = 0.070, 0.089, 0.108, 0.113 and max λ_n/bound(b) = 0.0070, 0.0056, 0.0034, 0.0015 for n = 10, 40, 100, 200; `bounds_hold_on_grid: true`.
- Arithmetic for (c): ϑ_n = 1.0226 (n = 1000), 0.9991 (n = 1030), 0.5905 (n = 2000), 0.1596 (n = 10⁴), 0.0230 (n = 10⁵).
- Independent rerun: pending.

## Sources

LITERATURE (context, not used): BBDM, Constr. Approx. 63 (2026), Thm 4 (Λ_n = O(n²), no constant; proof read at structure level only).

## Proof or evidence

**Step 0 (two formulas).** Let P = (cos θ₁, cos θ₂), a = (p,q) ∈ 𝒩, w = pπ/M, v = qπ/(M+1). As in X2-28 Lemma K (U_i(cos γ) = sin((i+1)γ)/sin γ; sin kθ sin kw = ½Σ_{σ=±1}σ cos k(θ − σw); terms of D_M with k = 0 or l = 0 cancel in the alternating sum):

ℓ_a(P) = (sin w sin v / (2N sin θ₁ sin θ₂)) Σ_{σ₁,σ₂=±1} σ₁σ₂ D_M(θ₁ − σ₁w, θ₂ − σ₂v). (K1)

By X2-21 Lemma 1, (cos α − cos β)D_M(α,β) = F̃(α) − F̃(β), F̃(γ) = cos((M+1)γ) + cos(Mγ). With u := (α+β)/2, v' := (α−β)/2: cos α − cos β = −2 sin u sin v' and cos kα − cos kβ = −2 sin ku sin kv'. Hence, first for sin u sin v' ≠ 0 and then everywhere by continuity,

D_M(α,β) = 𝔡_{M+1}(u)𝔡_{M+1}(v') + 𝔡_M(u)𝔡_M(v'). (R)

Bounds: |𝔡_k(γ)| ≤ min(k, 1/|sin γ|) (𝔡_k = U_{k−1}(cos γ)). Also |𝔡_k'(γ)| ≤ 2k·min(k, 1/|sin γ|): indeed 𝔡_k is a trigonometric polynomial of degree k − 1 with sup norm k, so |𝔡_k'| ≤ k(k−1) (Bernstein), and 𝔡_k' = (k cos kγ sin γ − sin kγ cos γ)/sin²γ gives |𝔡_k'| ≤ k/|sin γ| + 1/sin²γ; if 1/|sin γ| ≤ k the second bound is ≤ 2k/|sin γ|, otherwise the first is ≤ 2k·k. For k ∈ {M, M+1}: |𝔡_k| ≤ m, |𝔡_k'| ≤ 2k·m. Therefore

|D_M(α,β)| ≤ 2 m(u)m(v'), |∂_βD_M(α,β)| = ½|(∂_u − ∂_{v'})D_M| ≤ ½[2·2(M+1) + 2·2M] m(u)m(v') = (4M+2) m(u)m(v'), (B)

and the same bound for ∂_αD_M.

**Step 1 (lattice parametrisation).** Let 𝒯 := {(p̃, q̃) ∈ ℤ/2M × ℤ/(2M+2) : p̃ + q̃ odd} (parity is well defined; |𝒯| = 2N). The map r ↦ (r mod 2M, r + M + 1 mod 2M+2), ℤ/2N → 𝒯, is well defined (2M | 2N, (2M+2) | 2N), lands in 𝒯 (2r + M + 1 is odd), and is injective (r ≡ r' mod 2M and mod 2M+2 forces r ≡ r' mod lcm = 2N), hence bijective. For real offsets c₁, c₂ put α_r := c₁ − πr/M, β_r := c₂ − π(r+M+1)/(M+1). Then u_r = u₀ − (2M+1)hr and v'_r = v₀ − hr with u₀ = (c₁ + c₂ − π)/2, v₀ = (c₁ − c₂ + π)/2 (because 1/M + 1/(M+1) = (2M+1)/N, 1/M − 1/(M+1) = 1/N). So for every function g that is 2π-periodic in each variable,

Σ_{(p̃,q̃)∈𝒯} g(c₁ − w_{p̃}, c₂ − v_{q̃}) = Σ_{r=0}^{2N−1} g(α_r, β_r). (P)

**Step 2 (proof of (d)).** m is π-periodic and even. Split {0,…,2N−1} into the 2(M+1) blocks 𝔅_i := {iM, …, iM+M−1}.
*Inner sums.* In a block the points u_r form an arithmetic progression of M points with step δ := (2M+1)h, and π/(M+1) < δ < π/M (δM/π = (2M+1)/(2M+2), δ(M+1)/π = (2M+1)/(2M)). Since Mδ < π, the M points are pairwise at circular distance ≥ δ in ℝ/πℤ. So at most 2ρ/δ + 1 of them satisfy ‖u‖ ≤ ρ; ordering them by ‖u‖, the j-th one therefore has ‖u‖ ≥ (j−1)δ/2. With 1/|sin γ| ≤ π/(2‖γ‖): Σ_{r∈𝔅_i} m(u_r) ≤ (M+1) + Σ_{j=2}^{M} π/((j−1)δ) ≤ (M+1) + (M+1)(1 + log(M−1)) ≤ (M+1)(2 + L).
*Outer sum.* The arcs 𝔄_i := (v'_{(i+1)M}, v'_{iM}] have length Mh = π/(2(M+1)) =: η', are consecutive, and tile ℝ/πℤ (2(M+1)·η' = π); v'_r ∈ 𝔄_i for r ∈ 𝔅_i. Let 𝔄_{i₀} be the arc containing 0 mod π. An arc at cyclic index distance k ≥ 2 from i₀ has all its points at ‖·‖ ≥ (k−1)η', so m ≤ π/(2(k−1)η') = (M+1)/(k−1) there; for k ≤ 1 use m ≤ M+1. The cyclic distances are 0 (once), 1,…,M (twice each), M+1 (once). Hence Σ_i max_{𝔄_i} m ≤ 3(M+1) + 2Σ_{k=2}^{M+1}(M+1)/(k−1) ≤ (M+1)(5 + 2L).
Multiplying, Σ_r m(u_r)m(v'_r) ≤ Σ_i (max_{𝔄_i} m)·Σ_{r∈𝔅_i} m(u_r) ≤ (M+1)²(2+L)(5+2L). ∎

**Step 3 (proof of (a)).** In (K1) use sin w sin v ≤ 1. The points (σ₁w_p, σ₂v_q), (p,q) ∈ 𝒩, σ ∈ {±1}², are distinct points (w_{p̃}, v_{q̃}) with (p̃,q̃) ∈ 𝒯 (p̃ = ±p, q̃ = ±q, same parity of the sum). So, by (P) with c = (θ₁, θ₂), (B) and (d),
λ_n(P) ≤ (2N sin θ₁ sin θ₂)⁻¹ Σ_𝒯 |D_M(θ₁ − w_{p̃}, θ₂ − v_{q̃})| ≤ (2N sin θ₁ sin θ₂)⁻¹·2(M+1)²(2+L)(5+2L) = Γ_M/(sin θ₁ sin θ₂). ∎

**Step 4 (proof of (b)).** D_M is even in each variable, so Σ_{σ₂}σ₂D_M(α, θ₂ − σ₂v) = D_M(α, v − θ₂) − D_M(α, v + θ₂) = −∫_{−θ₂}^{θ₂} ∂_βD_M(α, v + s) ds. If θ₂ > π/2 put θ₂* := π − θ₂, v* := π − v; by evenness and 2π-periodicity the same sum equals D_M(α, θ₂* − v*) − D_M(α, θ₂* + v*) = −∫_{−θ₂*}^{θ₂*} ∂_βD_M(α, v* + s) ds. So in both cases, with θ̂₂ = min(θ₂, π−θ₂) and v̂ ∈ {v, π − v},
|ℓ_a(P)| ≤ (sin w sin v/(2N sin θ₁ sin θ₂)) Σ_{σ₁} ∫_{−θ̂₂}^{θ̂₂} |∂_βD_M(θ₁ − σ₁w, v̂ + s)| ds.
∂_βD_M is odd in β, so |∂_βD_M(α, v̂ + s)| = |∂_βD_M(α, −v̂ − s)|, and the s-range is symmetric; therefore Σ_{σ₁}∫|∂_βD_M(θ₁ − σ₁w, v̂ + s)|ds = ½Σ_{σ₁,σ₂}∫_{−θ̂₂}^{θ̂₂}|∂_βD_M(θ₁ − σ₁w, s − σ₂v̂)| ds. The points (σ₁w_p, σ₂v_q) are distinct points of 𝒯 as in Step 3; if v̂ = π − v, the points (σ₁w_p, σ₂(π − v_q)) are distinct points of 𝒯' := {p̃ + q̃ even}, and Σ_{𝒯'} g(c₁ − w, c₂ − v) = Σ_𝒯 g(c₁ − w, (c₂ − π/(M+1)) − v), so (P) applies with a changed offset. Using sin w sin v ≤ 1, (P), (B) and (d) (which is uniform in the offsets):
λ_n(P) ≤ (2N sin θ₁ sin θ₂)⁻¹·½·2θ̂₂·(4M+2)(M+1)²(2+L)(5+2L) = (θ̂₂/sin θ̂₂)·(2M+1)Γ_M/sin θ₁ ≤ (π/2)(2M+1)Γ_M/sin θ₁,
since θ/sin θ ≤ π/2 on (0, π/2] and sin θ₂ = sin θ̂₂. The second inequality of (b) is the same argument with the roles of the two variables exchanged (integrate ∂_αD_M in α; the bound (B) is symmetric). λ_n is continuous on Q, which gives the boundary cases. ∎

**Step 5 (proof of (c)).** If sin θ₁ > ϑ_n, (b) gives λ_n(P) ≤ (π/2)(2M+1)Γ_M/sin θ₁ < c*n²; likewise if sin θ₂ > ϑ_n (boundary cases included by (b)). By X2-26, c*n² < λ_n(1,1) ≤ Λ_n. Monotonicity: ϑ_n = (π/(2c*))·[(2M+1)(M+1)/(M−2)²]·[(2+L)(5+2L)/M]; the first bracket is decreasing for M > 2, and d/dL of (2+L)(5+2L)e^{−L} is (4L+9 − (2+L)(5+2L))e^{−L} < 0 for L ≥ 1. With c* ≥ 0.51695 (X2-25), ϑ_1030 ≤ 0.99910 < 1. For n ≥ 1030 (M ≥ 1032, L ≥ 6.939): ϑ_n·n/L² = (π/(2c*))·[(2M+1)(M+1)/(M(M−2))]·[(1 + 2/L)(2 + 5/L)] ≤ 3.0387·2.011·3.505 ≤ 21.5. ∎

## Scope

Upper bounds valid for every even n ≥ 2 and every point of Q; they are far from sharp (the measured size on the open edges is O(n log n) or smaller) and are designed only to confine the maximizers to four vertex boxes of angular size O(log²n/n). Nothing is claimed inside the boxes; in particular (c) does not exclude the lower vertices' boxes and does not prove Λ_n = λ_n(±1,1).

## Open items

- Inside the two upper boxes: λ_n ≤ λ_n(1,1); inside the two lower boxes: λ_n < c*n² (X2-28 addendum, items W-top, W-bot).
- Sharper constants (not needed).

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-3; uncommitted at writing. First version.
