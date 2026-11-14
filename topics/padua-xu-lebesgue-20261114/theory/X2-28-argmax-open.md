# PD-T?padua-xu-lebesgue-20261114-claude-28 — where is the Morrow–Patterson Lebesgue constant attained? (OPEN; plan, tools and measured support)

ID kind: PD-T.
Aliases: X2-28; MP argmax problem; target T5 of round X2-2; second half of novelty-gate candidate X2-C3.
Split from: none.
Split into: none yet. Proved supporting results live under their own IDs (X2-21 … X2-26, PD-N…-29, -30).

## Statement

**Target (OPEN).** For every even n ≥ 2 the Lebesgue function λ_n of the Morrow–Patterson points attains its maximum over Q = [−1,1]² exactly at the two vertices (±1, 1); equivalently Λ_n = λ_n(±1,1). Consequence, if true: lim_{n→∞} Λ_n/n² = c* = 0.51695365336… and Λ_n = c*(n+5/2)² − (n+1) + O(log² n) (by X2-25).

What is known (other records): Λ_n ≥ λ_n(±1,1) > c*n² (X2-26, PROVED); Λ_n > λ_n(±1,−1) = n+1 (PD-N…-29, PROVED); Λ_n = O(n²) (BBDM Thm 4, LITERATURE, no constant).

## Definitions

As in X2-21, X2-25. Angles: (x, y) = (cos θ₁, cos θ₂). Scaled vertex variables: at the upper vertex (1,1), θ₁ = ξ/M, θ₂ = ζ/M; at the lower vertex (1,−1), θ₁ = ξ/M, θ₂ = π − ζ/M (M = n + 2). sinc x := sin x/x. α := (ξ+ζ)/2, β := (ξ−ζ)/2.

## Assumptions

n even, n ≥ 2.

## Status by part

Overall status: OPEN.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Target: argmax set of λ_n equals {(±1,1)}, every even n ≥ 2 | OPEN | no proof; plan below |
| Grid maximum of λ_n equals the vertex value at (±1,1); no other local maximum reaches 0.9·λ_n(1,1); even 2 ≤ n ≤ 60 | MEASURED (orchestrator's G1-MP screen) | `evidence/mp-g1-summary.json`: `grid_max_is_vertex_value_all: true`, relative gap g_n ∈ [0.444, 0.599]; best non-vertex local maximum on the edge x = ±1 near the lower vertex, ≈ 0.403·λ_n(1,1) |
| Lemma K: four-term closed form of ℓ_{p,q}(cos θ₁, cos θ₂) | PROVED (minor supporting step, proof below; not part of the target's statement) | numerical check 1.1e−28 |
| Scaling limits L_top, L_bot (formulas below) | OPEN (heuristic derivation; conjecture) | MEASURED agreement at n = 100, 400 to 3 digits |
| First variation at (1,1): D_x := Σ sgn(ℓ_a(1,1)) ∂_xℓ_a(1,1) > 0 and D_y > 0 | MEASURED for n ∈ {2,4,6,8,10,20,30,40,60,80} | D_x/M⁴ from 0.0193 to 0.0495, D_y/M⁴ from 0.0274 to 0.0509; no proof |

PARTIAL is not used: the proved items are supporting lemmas, not conjuncts of the target.

Candidate / claim disposition: none (candidate X2-C3 stays open).

## Depends on

X2-21 (Lemma 1 for Lemma K), X2-23 (f) (ℓ_a(1,1) ≠ 0, used in the local-maximum remark), X2-25 (vertex value).

## Checks

- `python3 code/mp/research/x2_corner_scaling_limits.py` (2026-11-14; float64/mpmath; 3 s): (a) Lemma K against the kernel double sum at all nodes, n ∈ {2,4,6}, three points: max error 1.1e−28 (30 digits). (b) λ_n/M² versus the conjectured limits:

  | vertex | (ξ, ζ) | n = 100 | n = 400 | conjectured limit |
  |---|---|---|---|---|
  | top | (0.5, 0.5) | 0.49918 | 0.50305 | 0.50376 |
  | top | (1.0, 0.3) | 0.48510 | 0.48862 | 0.48923 |
  | top | (2.0, 2.0) | 0.33770 | 0.33973 | 0.34016 |
  | top | (3.0, 0.01) | 0.32806 | 0.32932 | 0.32947 |
  | top | (5.0, 5.0) | 0.06136 | 0.06209 | 0.06225 |
  | top | (12.0, 0.01) | 0.07941 | 0.08209 | 0.08289 |
  | bottom | (0.01, 5.0) | 0.20654 | 0.20891 | 0.20939 |
  | bottom | (3.0, 3.0) | 0.00228 | 0.00058 | 0 |
  | bottom | (2.0, 4.0) | 0.11751 | 0.11763 | 0.11748 |

  (c) On the grid {0.25, 0.75, …, 11.75}² the largest value of L_top is 0.5122 at (0.25, 0.25) (c* = 0.51695; L_top(0.01, 0.011) = 0.5154 with the quadrature truncated at T = 200); along the edge ζ ≈ 0: L_top = 0.509, 0.490, 0.423, 0.230, 0.143, 0.093, 0.041 at ξ = 0.5, 1, 2, 4, 8, 16, 32. sup L_bot on the same grid ≈ 0.2083 at (0.25, 5.25); on the edge ξ ≈ 0 the maximum is 0.2088 at ζ = 5.0, i.e. 0.4038·c*, matching the G1 observation 0.403. L_top is not monotone along every coordinate line (flag `Ltop_on_grid_decreasing…: false`). (d) First variation: D_x, D_y > 0 for all sampled n.
- Quadrature caveat: the L values use a midpoint rule with step 0.004–0.01 truncated at T = 200–600; integrands decay like τ⁻²; estimated absolute error ≤ 2e−3. Not certified.
- Independent rerun: pending.

## Sources

- LITERATURE: BBDM, Constr. Approx. 63 (2026): Lemma 6 and estimates (18)–(27) (structure of the proof of O(n²), read at structure level only); §7.1 (corner attainment posed as open). Padua analogue: PR #27 of this repository (unmerged; methods only, no lemma used).

## Proof or evidence

### Lemma K (four-term formula; PROVED, minor)

Let (p, q) ∈ 𝒩, w = pπ/M, v = qπ/(M+1), θ₁, θ₂ ∈ (0, π), and assume cos(θ₁ − σ₁w) ≠ cos(θ₂ − σ₂v) for all σ₁, σ₂ ∈ {±1}. Then

ℓ_{p,q}(cos θ₁, cos θ₂) = (−1)^p · (sin w sin v)/(2N sin θ₁ sin θ₂) · Σ_{σ₁,σ₂=±1} σ₁σ₂ · [cos((M+1)θ₁ − σ₁w) + cos(Mθ₁) + cos((M+1)θ₂) + cos(Mθ₂ + σ₂v)] / [cos(θ₁ − σ₁w) − cos(θ₂ − σ₂v)].

*Proof.* K_n = (sin θ₁ sin w sin θ₂ sin v)⁻¹ Σ_{a,b≥1, a+b≤M} sin(aθ₁) sin(aw) sin(bθ₂) sin(bv), and sin(aθ₁) sin(aw) = ½ Σ_{σ₁} σ₁ cos(a(θ₁ − σ₁w)). So the double sum is ¼ Σ_{σ₁,σ₂} σ₁σ₂ Ψ(θ₁ − σ₁w, θ₂ − σ₂v) with Ψ(α, β) := Σ_{a,b≥1, a+b≤M} cos(aα) cos(bβ). The function Φ_M of X2-21, Lemma 1, equals Ψ plus terms depending on α alone or on β alone, and those cancel in the alternating sum. By that lemma Φ_M(α, β) = ¼[F̃(α) − F̃(β)]/(cos α − cos β), F̃(γ) = cos((M+1)γ) + cos(Mγ). At α = θ₁ − σ₁w: Mw = pπ gives F̃(α) = (−1)^p[cos((M+1)θ₁ − σ₁w) + cos(Mθ₁)]; at β = θ₂ − σ₂v: (M+1)v = qπ gives F̃(β) = (−1)^q[cos((M+1)θ₂) + cos(Mθ₂ + σ₂v)], and (−1)^q = −(−1)^p. Multiply by ω_{p,q} = 8 sin²w sin²v/N. ∎

### Conjectured scaling limits (heuristic; OPEN)

Insert θ₁ = ξ/M, θ₂ = ζ/M in Lemma K and keep, for a node with w = π − 2t, v − w = 2τ/(M+1), τ = jπ + t (the lattice of X2-25, Step A), the leading terms cos(θ₁ − σ₁w) − cos(θ₂ − σ₂v) ≈ sin w·(2τ + σ₁ξ − σ₂ζ)/M and numerator ≈ cos σ₁ξ + cos σ₂ζ − cos(2τ + σ₁ξ) − cos(2τ − σ₂ζ) = 4 sin τ cos((σ₁ξ+σ₂ζ)/2) sin(τ + (σ₁ξ−σ₂ζ)/2). Summing over the lattice as in X2-25 suggests

lim λ_n(cos(ξ/M), cos(ζ/M))/M² = **L_top(ξ, ζ) := (2/π) ∫_0^∞ |𝒦_top(τ)| dτ**,
𝒦_top(τ) := (2 sin²τ cos τ/(α² − β²)) · { cos α [sinc(τ+β) + sinc(τ−β)] − cos β [sinc(τ+α) + sinc(τ−α)] },

and, at the lower vertex (nodes near the anti-diagonal, parity class "even"),

lim λ_n(cos(ξ/M), −cos(ζ/M))/M² = **L_bot(ξ, ζ) := (1/π) ∫_{−∞}^{∞} |𝒦_bot(τ)| dτ**,
𝒦_bot(τ) := (2 sin τ cos²τ/(α² − β²)) · { sin α [sinc(τ+β) − sinc(τ−β)] − sin β [sinc(τ+α) − sinc(τ−α)] }.

Consistency: 𝒦_top → −h̃(τ) as (ξ, ζ) → 0, so L_top(0,0) = c* (X2-25); 𝒦_bot ≡ 0 for ξ = ζ and 𝒦_bot → 0 as (ξ, ζ) → 0, matching λ_n(1,−1) = n + 1 = o(M²). Equivalent Fourier form: sinc(τ+x) + sinc(τ−x) = ∫_{−1}^{1} cos(τs) cos(xs) ds, so the brace in 𝒦_top is ∫_{−1}^{1} cos(τs)[cos α cos(βs) − cos β cos(αs)] ds. The errors of these approximations have not been estimated; the limits are conjectures.

### Remark (local structure at the vertex)

By X2-23 (f) no ℓ_{p,q} vanishes at (1,1), so on a neighbourhood of (1,1) in Q the function λ_n equals the polynomial P_n := Σ sgn(ℓ_{p,q}(1,1)) ℓ_{p,q} ∈ Π_n. The vertex is a strict local maximum of λ_n on Q as soon as D_x := ∂_xP_n(1,1) > 0 and D_y := ∂_yP_n(1,1) > 0. These are finite sums of the type treated in X2-23/X2-25 (with U_i'(1) = i(i+1)(i+2)/3 in place of U_i(1)); measured D_x/M⁴ → ≈0.050, D_y/M⁴ → ≈0.051, consistent with L_top(ξ, 0) ≈ c* − (D_x/M⁴) ξ²/2. The neighbourhood has angular size O(1/M), i.e. it is of the order of the scaling window; the local statement alone does not give the global one.

## Scope

An open target with a proved tool (Lemma K), conjectured limit profiles and measured support. Nothing about the argmax is claimed.

## Open items

Plan for the next rounds (details and effort estimates in `attempts/X2-round2.md`, §T5):

1. **P1 — first variation (closed form).** Prove D_x, D_y > 0 for every even n (or n ≥ n₁ plus certificates) by a closed form for ∂_xℓ_{p,q}(1,1), ∂_yℓ_{p,q}(1,1) (differentiate Lemma K at the vertex, or repeat X2-21 with T_a''(1)) and the method of X2-25. Gives: (±1,1) are strict local maxima. Self-contained; one round.
2. **P2 — scaling limit with error.** Prove λ_n(cos(ξ/M), cos(ζ/M)) = M² L_top(ξ, ζ) + O(M^{2−δ}) uniformly for |(ξ, ζ)| ≤ R (and the analogue at the lower vertices), by the lattice/midpoint method of X2-25 applied to Lemma K.
3. **P3 — profile inequality.** Prove L_top(ξ, ζ) < c* for (ξ, ζ) ≠ (0, 0) with a quantitative margin (quadratic near 0, uniform away), and sup L_bot < c* (measured sup ≈ 0.209 ≈ 0.404 c*). The Fourier form above is the natural starting point; a computer-assisted enclosure of L_top on a compact set plus an analytic tail is the fallback.
4. **P4 — outside the windows.** A global bound λ_n(cos θ₁, cos θ₂) ≤ (c* − δ)M² when (θ₁, θ₂) is at distance ≥ R/M from all four vertices, with explicit constants, from Lemma K (BBDM's estimates give the order only). Measured: the decay of L_top along the edges is slow (0.093 at ξ = 16, 0.041 at ξ = 32), so R cannot be taken small; the bound must cover the edges y = 1 and x = ±1.
5. **P5 — finite degrees.** Interval certificates of the argmax for n below the analytic onset, as in the Padua argmax topic (independent checker required, gate G3).

Next unresolved step: P1.

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-2; uncommitted at writing. First version. The G1-MP screen is the orchestrator's (developer run), reported to the researcher during the round.
