# PD-T?padua-xu-lebesgue-20261114-claude-25 — λ_n(±1,1) = c*(n+5/2)² − (n+1) + O(log² n) for Morrow–Patterson points, with explicit constants

ID kind: PD-T.
Aliases: X2-25; upper-vertex asymptotics; sharp vertex constant c*; target T3 of round X2-2.
Split from: none.
Split into: none. Consequences are registered separately: X2-26 (explicit lower bound for Λ_n), PD-N…-30 (vertex value versus (n+1)(n+2)/2). The measured finer behaviour of the remainder is X2-27 (MEASURED).

## Statement

Define, for τ > 0,
h̃(τ) := sin²(2τ)(tan τ − τ)/τ³ = 4 sin²τ cos τ (sin τ − τ cos τ)/τ³ (an entire function of τ), ĥ := max(h̃, 0), and

**c\* := (4/π) ∫_0^∞ ĥ(τ) dτ = (2/π) ∫_0^∞ |sin 2τ| · |d/dτ (sin τ/τ)²| dτ.**

Then for every even n ≥ 2, with M := n + 2,

**−(0.4053 log²M + 2.9833 log M + 15.82) ≤ λ_n(1,1) − c*(n + 5/2)² + (n + 1) ≤ 7.66,**

and λ_n(−1,1) = λ_n(1,1). In particular

λ_n(1,1) = c* n² + (5c* − 1) n + O(log² n), lim_{n→∞, n even} λ_n(±1,1)/n² = c*,
|λ_n(1,1)/n² − c*| ≤ 1.585/n + (0.4053 log²(n+2) + 2.9833 log(n+2) + 15.82)/n² for every even n ≥ 2.

The constant has the convergent series (Lemma C)
c* = (4/π) Σ_{j≥0} [Φ(a_j) − Φ(b_j)], Φ(τ) := sin 2τ sin²τ/τ² + 2 cos 2τ sin²τ/τ + 2 Si(2τ) − 2 Si(4τ),
with b_j := jπ + π/2, Φ(a_0) := 0 and a_j ∈ (jπ, b_j) the root of tan τ = τ (j ≥ 1); the j-th term is at most 8/(π⁶ j⁵) for j ≥ 1. The first term is c₀ := 16/π² − (8/π)(Si(π) − Si(2π)) = 0.516513294709857…, and

c* = 0.51695365336… , certified enclosure c* ∈ [0.5169536533663, 0.5169536533677].

So 2c* = 1.03390730673… = lim λ_n(±1,1)/((n+1)(n+2)/2), and 5c* − 1 = 1.58476826683….

## Definitions

- MP_n, 𝒩, ℓ_{p,q}, λ_n as in X2-21; A_{p,q} and the band formula as in X2-23.
- Si(x) := ∫_0^x (sin s/s) ds. [·]_+ := max(·, 0). log is the natural logarithm.
- Constants of the proof: N := M(M+1), η := π(2M+1)/(4N), c_M := (M+½)³/N, ς := π/(4(M+1)), S* := (1 − (M+½)⁻²)^{−1/2}, ζ₊(V) := [1 − V]_+/V³ for V > 0, I := ∫_0^∞ ĥ = πc*/4.

## Assumptions

n even, n ≥ 2 (M ≥ 4 even). No unproved hypothesis. The two-sided inequality is proved analytically for every such n; only the numerical value of c* (not its definition, and not the inequality) rests on a computation, which is rigorous ball arithmetic (see Checks).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Lemma C (structure of h̃, formulas for c*, tail bound) | PROVED | below |
| Two-sided inequality for every even n ≥ 2 | PROVED | Steps A–E below; every per-node inequality and every block bound also checked numerically (Checks) |
| Limit, two-term expansion, explicit rate | PROVED | immediate corollaries |
| Enclosure c* ∈ [0.5169536533663, 0.5169536533677] | PROVED, computer-assisted (ball arithmetic on the proved series with the proved tail bound); independent rerun pending | `x2_corner_arb.py` |
| True order of the remainder (measured ≈ −(2/π²) log² n) | not claimed here | see X2-27 (MEASURED) |

Candidate / claim disposition: none.

## Depends on

- X2-23 (a), (c), (e): closed form of A_{p,q}, band formula λ_n(1,1) = −(n+1) + 2Σ[−A]_+, hyperbolic form.
- X2-21 part 4 (λ_n(−1,1) = λ_n(1,1)).

## Checks

All runs 2026-11-14 on the topic machine (python 3.13.18, numpy 2.5.3, mpmath 1.4.1, python-flint 0.9.0); outputs in /tmp/x2r2/ (not committed).

- `python3 code/mp/research/x2_corner_checks.py cstar`: series with 60 terms 0.51695365331673 (proved tail ≤ 1.6e−10); accelerated sum 0.516953653366806272706422282045; independent quadrature of ĥ over the first 13 bumps 0.5169536292 (tail ≤ 1.0e−7); c₀ by quadrature and by the Si formula agree to 30 digits; max |Φ' + h̃| = 2.6e−41 at 7 points; max |h̃''| on [0.05, 60] = 2.892 (proved bound 68/15 = 4.533); numerical total variation of ĥ' on [0.05, 60] = 3.80 (proved bound T₂ ≤ 9.0121).
- `python3 code/mp/research/x2_corner_arb.py --nmax 60`: c* ∈ [0.516953653366381…, 0.516953653367681…] (200 terms, all roots a_j enclosed by certified sign changes); for every even n ≤ 60 the ball for R_n := λ_n(1,1) + (n+1) − c*(n+5/2)² lies inside the proved interval (flag `two_sided_X2-25`); e.g. R_2 = −1.62275, R_10 = −2.85556, R_30 = −4.49009, R_60 = −5.83016.
- `python3 code/mp/research/x2_corner_checks.py decomp` (float64, M ∈ {4,6,8,10,12,16,22,32,52,102,202,402,802,1202}): all node-wise inequalities of Step B hold at every node (S ≥ V̂; S ≤ V̂/(1−ε_s); 0 ≤ e₁ ≤ bound; 𝓜 ≤ c_M ĥ; 𝓜 ≥ c_M ĥ − L_c − L_s; L_c, L_s ≤ bounds; ε_s < ¼ on V̂ < 1), and all block bounds of Steps C–D hold with room: Σe₁ ∈ [0.567, 0.815] (bound 2.012); ΣL_s ∈ [1.38, 1.78] (bound 4.28); ΣL_c from 0.275 (M=4) to 6.41 (M=1202) (bound 2.45 … 18.44); 2c_M·|Σ_{r≥1}ĥ(ηr) − I/η| ≤ 0.149 (bound 3.63); 2c_M·Σ_miss from 1.53 to 2.30 (bound 3.33 … 8.22). `all_checks: True` for every M.
- `python3 code/mp/research/x2_corner_checks.py table`: R_n = −1.623, −2.000, −2.325, −2.606, −2.856, −3.807, −4.490, −5.456, −6.971, −8.703, −10.641, −12.787, −15.140, −17.686, −20.420 for n = 2, 4, 6, 8, 10, 20, 30, 50, 100, 200, 400, 800, 1600, 3200, 6400 (float64 band sums); all inside the proved interval.
- Independent rerun: pending (auditor).

## Sources

- LITERATURE (context only): BBDM, Constr. Approx. 63 (2026), Thm 4 p. 53: Λ_n = O(n²) without constant; Beberok, JAT 311 (2025) 106191, Thm 0.1: Λ_n ≥ c n² with existential c via λ_n(1,1). Neither gives the limit, a constant, or the second term. No source read states c*.

## Proof or evidence

### Lemma C (the function h̃ and the constant c*)

(i) *Sign.* On (jπ, jπ + π/2), j ≥ 0, h̃ = 4 sin²τ cos²τ (tan τ − τ)/τ³ and τ ↦ tan τ − τ is increasing (derivative tan²τ) from −jπ to +∞; so for j ≥ 1 there is a unique zero a_j, h̃ < 0 on (jπ, a_j) and h̃ > 0 on (a_j, b_j); for j = 0, h̃ > 0 on (0, π/2). On (jπ + π/2, (j+1)π) one has tan τ < 0 < τ, so h̃ = 4 sin²τ cos²τ(tan τ − τ)/τ³ < 0. Hence ĥ = h̃ on ∪_{j≥0}[a_j, b_j] (a_0 := 0) and ĥ = 0 elsewhere. For j ≥ 1, ε := b_j − a_j satisfies cot ε = tan a_j = a_j > jπ, so 0 < b_j − a_j < tan ε < 1/(jπ).

(ii) *Size.* For τ ∈ [a_j, b_j] with μ := τ − jπ: ĥ(τ) = 4 sin²μ cos²μ (tan μ − τ)/τ³ ≤ 4 sin³μ cos μ/τ³ ≤ 4(b_j − τ)/τ³ (cos μ = sin(b_j − τ) ≤ b_j − τ). For j ≥ 1 this gives ĥ ≤ 4(b_j − τ)/(jπ)³ ≤ 4/(jπ)⁴ and ∫_{a_j}^{b_j} ĥ ≤ 2(b_j − a_j)²/(jπ)³ < 2/(jπ)⁵.

(iii) *Antiderivative.* Φ' = sin 2τ · d/dτ(sin τ/τ)² = −h̃. Indeed d/dτ[sin 2τ sin²τ/τ²] = 2cos 2τ sin²τ/τ² + sin 2τ (sin²τ/τ²)', d/dτ[2cos 2τ sin²τ/τ] = (−4 sin 2τ sin²τ + 2 cos 2τ sin 2τ)/τ − 2 cos 2τ sin²τ/τ², d/dτ[2Si(2τ) − 2Si(4τ)] = (2 sin 2τ − 2 sin 4τ)/τ; the 1/τ² terms cancel and the 1/τ terms sum to sin 2τ[−2(1 − cos 2τ) + 2cos 2τ + 2]/τ − 2 sin 4τ/τ = 0. And sin 2τ (sin²τ/τ²)' = 2 sin 2τ sin τ (τ cos τ − sin τ)/τ³ = −h̃. Moreover Φ(0+) = 0 and Φ(τ) → 2·(π/2) − 2·(π/2) = 0 as τ → ∞.

(iv) *Formulas.* By (i)–(iii), I = Σ_{j≥0} ∫_{a_j}^{b_j} h̃ = Σ_{j≥0} [Φ(a_j) − Φ(b_j)], with j-th term < 2/(jπ)⁵ by (ii); so c* = (4/π)I has the stated series, with terms ≤ 8/(π⁶j⁵) and tail Σ_{j>J} ≤ 2/(π⁶J⁴). ∫_0^∞ h̃ = Φ(0+) − Φ(∞) = 0 (absolutely convergent: |h̃| ≤ τ⁻² + 1.3τ⁻³), so ∫|h̃| = 2∫ĥ and c* = (2/π)∫_0^∞|h̃| = (2/π)∫_0^∞ |sin 2τ||(sin²τ/τ²)'| dτ. For j = 0: Φ(π/2) = −4/π + 2Si(π) − 2Si(2π), which gives c₀. At a root tan a = a one has sin²a = a²/(1+a²), so Φ(a_j) = 2a_j(2 − a_j²)/(1 + a_j²)² + 2Si(2a_j) − 2Si(4a_j), and Φ(b_j) = −2/b_j + 2Si(2b_j) − 2Si(4b_j).

(v) *Second derivative.* h̃ = P − Q with P := (sin 2τ − ½ sin 4τ)/τ³ and Q := (1 − cos 4τ)/(2τ²). From sin a = a − (a³/2)∫_0^1 (1−x)² cos(ax) dx and 1 − cos a = a²∫_0^1 (1−x) cos(ax) dx: P = ∫_0^1 (1−x)²[16 cos(4τx) − 4 cos(2τx)] dx, Q = 8∫_0^1 (1−x) cos(4τx) dx, hence
h̃''(τ) = ∫_0^1 x²(1−x)[128(2x−1) cos(4τx) + 16(1−x) cos(2τx)] dx, |h̃''| ≤ 128·∫_0^1 x²(1−x)|2x−1| dx + 16·∫_0^1 x²(1−x)² dx = 128/32 + 16/30 = 68/15 on ℝ.
Also, writing h̃ = Aτ⁻³ − Bτ⁻² with A = sin 2τ − ½ sin 4τ = 4 sin³τ cos τ (|A| ≤ 3√3/4 < 1.3, |A'| ≤ 4, |A''| ≤ 12) and B = (1 − cos 4τ)/2 (|B| ≤ 1, |B'| ≤ 2, |B''| ≤ 8): |h̃''| ≤ 8τ⁻² + 20τ⁻³ + 30τ⁻⁴ + 15.6τ⁻⁵ for τ > 0.

(vi) *One-sided derivatives at the breakpoints.* h̃'(b_j) = −4 sin⁴b_j/b_j³ = −4/b_j³ and, for j ≥ 1, h̃'(a_j) = sin²(2a_j) tan²a_j/a_j³ = 4 sin⁴a_j/a_j³ ∈ (0, 4/(jπ)³).

(vii) *Total variation of ĥ'.* ĥ is continuous, equal to the smooth h̃ on each [a_j, b_j] and to 0 elsewhere, so T₂ := ∫_{∪[a_j,b_j]} |h̃''| + Σ (jumps of ĥ') satisfies, by (v), (vi), (i),
T₂ ≤ (π/2)(68/15) + 32/π³ + Σ_{j≥1} (1/(jπ))(8/(jπ)² + 20/(jπ)³ + 30/(jπ)⁴ + 15.6/(jπ)⁵) + Σ_{j≥1} [4/(jπ)³ + 4/((j+½)π)³]
= 7.12095 + 1.03205 + (8ζ(3)/π³ + 2/9 + 30ζ(5)/π⁵ + 15.6/945) + (32/π³)(ζ(3) − 1) ≤ 7.12095 + 1.03205 + 0.65053 + 0.20854 < 9.0121.
(Σ_{j≥1}(j+½)⁻³ = 7ζ(3) − 8.) ∎

### Lemma R (trapezoid rule with kinks)

Let f be continuous on [a, a+η] and C² on each of finitely many closed subintervals whose union is [a, a+η]. Then
|∫_a^{a+η} f − (η/2)(f(a) + f(a+η))| ≤ (η²/8) [ ∫_a^{a+η} |f''| + Σ_{interior breakpoints x} |f'(x+) − f'(x−)| ].

*Proof.* K(x) := ½(x − a)(a + η − x) has 0 ≤ K ≤ η²/8, K(a) = K(a+η) = 0, K'' = −1. On a smooth piece [c, d]: ∫_c^d K f'' = [K f']_c^d − [K' f]_c^d − ∫_c^d f. Summing over the pieces, the K'f terms telescope (K', f continuous) to K'(a+η)f(a+η) − K'(a)f(a) = −(η/2)(f(a) + f(a+η)), and the Kf' terms give −Σ_x K(x)(f'(x+) − f'(x−)). Hence ∫f − (η/2)(f(a)+f(a+η)) = −∫K f'' − Σ_x K(x)(f'(x+) − f'(x−)). ∎

*Consequence.* Apply Lemma R to ĥ on the cells [rη, (r+1)η], r ≥ 0, and sum over r < R: the trapezoid values add up to η Σ_{r=1}^{R−1} ĥ(ηr) + (η/2)ĥ(ηR) (ĥ(0) = 0), and the right sides add up to at most (η²/8)T₂ (a jump located at a grid point belongs to no cell's interior). Let R → ∞; ĥ(τ) ≤ 4/τ⁴ for τ ≥ π and ĥ is integrable by Lemma C(ii). Hence

|η Σ_{r≥1} ĥ(ηr) − I| ≤ (η²/8) T₂. (R1)

### Step A (exact reduction)

Reindex the nodes as in X2-23 (d): p' := M − p ∈ [1, M−1], q' := M + 1 − q ∈ [1, M], p' ≡ q' (mod 2), and put t := πp'/(2M), θ := πq'/(2(M+1)); then t, θ ∈ (0, π/2), X = sin²t, Y = sin²θ, and X > Y ⟺ θ < t ⟺ q' ≤ p' (if q' ≤ p' then q'M < p'(M+1); if q' ≥ p' + 2 then q'M > p'(M+1)). By X2-23 (b), (c), [−A]_+ vanishes unless X > Y, so with 𝒩₊ := {nodes with q' ≤ p'}:

λ_n(1,1) + (M − 1) = 2 Σ_{𝒩₊} [−A]_+. (A1)

For a node of 𝒩₊ put b := t − θ ∈ (0, π/2), μ := (t + θ)/2 ∈ (0, π/2), j := (p' − q')/2 ∈ ℤ_{≥0}, r := p'(M+1) − q'M = 2jM + p'. Then b = πr/(2N), b/2 < μ < π/2 − b/2 (because θ > 0 and t < π/2), and

τ̃ := (M+½) b = η r = jπ + μ, (A2)

since (M+½)(p'/M − q'/(M+1))·π/2 = (π/2)[(p' − q') + p'/(2M) + q'/(2(M+1))]. The map 𝒩₊ → R₊ := {2jM + ρ : j ≥ 0, 2j + 1 ≤ ρ ≤ M − 1}, (p', q') ↦ r, is a bijection (ρ = p', q' = p' − 2j ≥ 1). By (A2), with V̂ := τ̃ cot μ > 0,

ĥ(τ̃) = 4 sin²μ cos²μ [tan μ − τ̃]_+/τ̃³ = 4 cos⁴μ · ζ₊(V̂). (A3)

### Step B (node-wise sandwich)

Fix a node of 𝒩₊. Let u := log(sin t/sin θ) > 0, ε_s := sin²(b/2)/sin²μ ∈ (0,1), ε_c := sin²(b/2)/cos²μ ∈ (0,1). Using sin t sin θ = sin²μ − sin²(b/2), cos t cos θ = cos²μ − sin²(b/2), sin²t − sin²θ = sin 2μ sin b:

sinh u = (sin²t − sin²θ)/(2 sin t sin θ) = sin b cot μ/(1 − ε_s), cos t cos θ = cos²μ (1 − ε_c).

Put S := (M+½) sinh u = V̂ · (sin b/b)/(1 − ε_s). Then

V̂ ≤ S ≤ V̂/(1 − ε_s). (B1)

(The right inequality is sin b ≤ b. For the left one, 1 − ε_s ≤ cos²(b/2), so (sin b/b)/(1 − ε_s) ≥ tan(b/2)/(b/2) ≥ 1.)
By X2-23 (e), −A = (2/N) cos²t cos²θ [2cosh u − (2M+1) sinh u]/sinh³u = 4c_M cos²t cos²θ (cosh u − S)/S³. Define

𝓜 := 4 c_M cos²t cos²θ ζ₊(S) = 4c_M cos⁴μ (1 − ε_c)² ζ₊(S), e₁ := [−A]_+ − 𝓜.

*Upper side.* Since cosh u ≥ 1, e₁ ≥ 0. If cosh u ≤ S then e₁ = 0. If S < cosh u, i.e. S < S* (S < cosh u ⟺ tanh u < 1/(M+½) ⟺ S < S*), then [cosh u − S]_+ − [1 − S]_+ ≤ cosh u − 1 ≤ ½ sinh²u = S²/(2(M+½)²). Hence, with (B1), cos t cos θ ≤ cos²μ and (M+½)/N < 1/M:

0 ≤ e₁ ≤ (2(M+½)/(N S)) cos²t cos²θ · 1[S < S*] ≤ (2/M) · sin μ cos³μ/τ̃ · 1[τ̃ < S* tan μ]. (B2)

Since ζ₊ is non-increasing, (1 − ε_c)² ≤ 1 and S ≥ V̂, (A3) gives

𝓜 ≤ c_M ĥ(τ̃). (B3)

*Lower side.* ζ₊ is convex on (0, ∞) (on (0,1], ζ'' = 6V⁻⁵(2 − V) > 0; ζ'(1−) = −1 < 0 = ζ'(1+)). If V̂ < 1, the tangent at V̂ and (B1) give ζ₊(S) ≥ ζ₊(V̂) − ((3 − 2V̂)/V̂⁴)(S − V̂) ≥ ζ₊(V̂) − 3ε_s/((1 − ε_s)V̂³); if V̂ ≥ 1, ζ₊(S) ≥ 0 = ζ₊(V̂). With (1 − ε_c)² ≥ 1 − 2ε_c:

𝓜 ≥ c_M ĥ(τ̃) − L_c − L_s, L_c := 8c_M cos⁴μ ε_c ζ₊(V̂), L_s := 4c_M cos⁴μ · 3ε_s/((1 − ε_s)V̂³) · 1[V̂ < 1]. (B4)

Bounds: ε_c ≤ b²/(4cos²μ), ε_s ≤ b²/(4 sin²μ), b = τ̃/(M+½), ζ₊(V̂) ≤ 1[V̂<1] tan³μ/τ̃³, (M+½)/N < 1/M. On {V̂ < 1}: sin(b/2) ≤ τ̃/(2M+1) < tan μ/(2M+1) and cos μ > cos t ≥ sin(π/(2M)) ≥ 1/M, so ε_s < M²/(2M+1)² < ¼ and 1/(1 − ε_s) < 4/3. Therefore

L_c ≤ (2/M) · sin³μ/(cos μ · τ̃) · 1[τ̃ < tan μ], L_s ≤ (4/M) · sin μ cos μ/τ̃ · 1[τ̃ < tan μ]. (B5)

Altogether, for every node of 𝒩₊:

c_M ĥ(τ̃) − L_c − L_s ≤ [−A]_+ ≤ c_M ĥ(τ̃) + e₁. (B6)

### Step C (sums of the error terms over 𝒩₊)

Group the nodes by j ("block j"); in block j the values τ̃ = ηr are distinct points of ηℤ in (jπ, jπ + π/2) and μ = τ̃ − jπ. Block 0 has exactly the M − 1 nodes q' = p', with τ̃ = μ. For j ≥ 1 and y > 0, the nodes of block j with tan μ > y have τ̃ in an open interval of length arctan(1/y) < 1/y, so their number is at most 1/(yη) + 1 < (2M+1)/(πy) + 1 (as 1/η = 4N/(π(2M+1)) < (2M+1)/π); for them cos μ < 1/y. Use (2M+1)/M ≤ 9/4, 1/M ≤ ¼, S* ≤ (77/81)^{−1/2} < 1.02565.

- Σ e₁. Block 0: e₁ ≤ (2/M)(sin μ/μ)cos³μ ≤ 2/M, total < 2. Block j ≥ 1 (τ̃ ≥ jπ, y = jπ/S*): total ≤ (2/(Mjπ))(S*/(jπ))³[S*(2M+1)/(π²j) + 1] ≤ 0.00518/j⁵ + 0.00554/j⁴. Hence Σ_{𝒩₊} e₁ ≤ 2 + 0.00518 ζ(5) + 0.00554 ζ(4) < 2.012.
- Σ L_s. Block 0: L_s ≤ (4/M)(sin μ cos μ/μ) ≤ 4/M, total < 4. Block j ≥ 1 (y = jπ): total ≤ (4/(M(jπ)²))[(2M+1)/(π²j) + 1] ≤ (9/π⁴)/j³ + (1/π²)/j². Hence Σ_{𝒩₊} L_s ≤ 4 + (9/π⁴)ζ(3) + 1/6 < 4.28.
- Σ L_c. Block 0: L_c ≤ (2/M)(sin²μ/μ) tan μ ≤ (1.4494/M) tan t, because sup_{0<x<π/2} sin²x/x < 0.7247 and μ < t; and Σ_{p'=1}^{M−1} tan(πp'/(2M)) = Σ_{p=1}^{M−1} cot(πp/(2M)) < (2M/π)(1 + log M). Block-0 total < 0.9228 (1 + log M).
  Blocks j ≥ 1: with p := M − p', tan μ < tan t = cot(πp/(2M)) < 2M/(πp), so L_c ≤ (2/(Mjπ)) tan t · 1[jπ < tan t] ≤ (4/(π²pj)) · 1[j < P/p], P := 2M/π². Each node is a distinct pair (p, j), so the total is at most (4/π²) Σ_{p<P} (1/p)(1 + log(P/p)) ≤ (4/π²)(1 + 2 log P + ½ log²P) (if P ≥ 1; the sum is empty if P < 1, i.e. M = 4). With log P = log M − 1.596313 this is ≤ 0.202642 log²M + 0.163608 log M − 0.372262, which is also ≥ 0 at M = 4.
  Hence Σ_{𝒩₊} L_c ≤ 0.2027 log²M + 1.0864 log M + 0.5505.

### Step D (the main sum)

By the bijection of Step A, Σ_{𝒩₊} ĥ(τ̃) = Σ_{r∈R₊} ĥ(ηr) =: 𝔖. Trivially 𝔖 ≤ Σ_{r≥1} ĥ(ηr). Conversely 𝔖 = Σ_{r≥1} ĥ(ηr) − Σ_miss with Σ_miss := Σ_{r≥1, r∉R₊} ĥ(ηr), and we claim

Σ_miss ≤ 1.1119/(M+1) + 0.4053 (0.307 + log M)/(M+1) + 0.386/M³. (D1)

Write r = 2jM + ρ, 0 ≤ ρ ≤ 2M − 1; then ηr = j(π − 2ς) + ηρ because 2Mη = π − 2ς; also ηM = π/2 − ς and 2ς < η = ς(2M+1)/M, η − ς = π/(4M).
- Points in (0, π/2) = (a_0, b_0): r = 1, …, M (j = 0); only r = M is not in R₊, and ĥ(ηM) = ĥ(π/2 − ς) ≤ 4 sin ς/(π/2 − ς)³ ≤ 1.41571 ς < 1.1119/(M+1) (Lemma C(ii), ς ≤ π/20, 4/(π/2 − π/20)³ < 1.41571).
- Points in (a_i, b_i), 1 ≤ i ≤ M/2 − 1. They have j = i (block j − 1 = i − 1 ends below iπ; block i + 1 starts at (i+1)π − 2(i+1)ς ≥ b_i). Those not in R₊ have ρ ≤ 2i or ρ ≥ M. If ρ ≤ 2i: ηr ≤ iπ + 2i(η − ς) = iπ + iπ/(2M) < iπ + π/4 < b_i − 1/(iπ) < a_i, so ĥ(ηr) = 0. If ρ = M + k ≥ M: ηr < b_i forces kη < (2i+1)ς, so 0 ≤ k ≤ i, and b_i − ηr = (2i+1)ς − kη ≤ (2i + 1 − 2k)ς; by Lemma C(ii) the contribution is ≤ (4/(iπ)³) Σ_{k=0}^{i} (2i+1−2k)ς = 4(i+1)²ς/(iπ)³ ≤ 16ς/(π³ i). Summing over i: ≤ (16ς/π³)(1 + log(M/2)) ≤ (4/(π²(M+1)))(0.307 + log M).
- Points in (a_i, b_i), i ≥ M/2 (all of them, in R₊ or not): at most (b_i − a_i)/η + 1 < (2M+1)/(iπ²) + 1 points, each with ĥ ≤ 4/(iπ)⁴; with Σ_{i≥m} i⁻⁵ ≤ ¾m⁻⁴ and Σ_{i≥m} i⁻⁴ ≤ (5/6)m⁻³ for m = M/2 ≥ 2 the total is ≤ (0.1124 + 0.2738)/M³.
This proves (D1). Dividing (R1) by η:

I/η − ηT₂/8 − Σ_miss ≤ 𝔖 ≤ I/η + ηT₂/8. (D2)

### Step E (assembly)

Constants: 2c_M/η = 4(M+½)²/π, so 2c_M I/η = c*(M+½)²; 2c_M η = π((M+½)²/N)² = π(1 + 1/(4N))² ≤ π(1.0125)² < 3.2207, so 2c_M·ηT₂/8 < 3.2207·9.0121/8 < 3.629; 2c_M/(M+1) ≤ 2 (as (M+½)³ ≤ M(M+1)²) and c_M ≤ M + 0.6, so by (D1) 2c_M Σ_miss ≤ 2.2238 + 0.8106(0.307 + log M) + 0.056 ≤ 2.529 + 0.8106 log M.

*Upper bound.* By (A1), (B6), Step C, (D2):
λ_n(1,1) + (M−1) ≤ 2c_M 𝔖 + 2Σe₁ ≤ c*(M+½)² + 3.629 + 4.024 < c*(M+½)² + 7.66.

*Lower bound.* By (A1), (B6), Step C, (D2):
λ_n(1,1) + (M−1) ≥ 2c_M 𝔖 − 2ΣL_c − 2ΣL_s ≥ c*(M+½)² − 3.629 − (2.529 + 0.8106 log M) − (0.4054 log²M + 2.1728 log M + 1.101) − 8.56 ≥ c*(M+½)² − (0.4054 log²M + 2.9834 log M + 15.819).

Keeping one more digit in Step C (2ΣL_c ≤ 0.405284 log²M + 2.172656 log M + 1.100916) gives the stated constants 0.4053, 2.9833, 15.82. Since M + ½ = n + 5/2 and M − 1 = n + 1, this is the two-sided inequality. λ_n(−1,1) = λ_n(1,1) is X2-21 part 4. ∎

### Corollaries

c*(n+5/2)² − (n+1) = c*n² + (5c* − 1)n + (25c*/4 − 1), with 5c* − 1 = 1.58477 and 25c*/4 − 1 = 2.23096 (enclosure of c*). With ℓ(M) := 0.4053 log²M + 2.9833 log M + 15.82 ≥ 15.82:
1.58476 n + 2.23 − ℓ(n+2) ≤ λ_n(1,1) − c*n² ≤ 1.58477 n + 2.24 + 7.66,
hence |λ_n(1,1)/n² − c*| ≤ (1.585 n + ℓ(n+2))/n² for every even n ≥ 2, the limit and the two-term expansion follow, and λ_n(1,1)/((n+1)(n+2)/2) → 2c*.

### Remark (why the natural variable is n + 5/2)

The point of the proof is that, in the midpoint variables (μ, τ̃) of Step A, the exact summand is c_M ĥ(τ̃) up to *second-order* relative corrections ε_c, ε_s = O(b²/cos²μ), O(b²/sin²μ) and the node values τ̃ form an equispaced grid of step η with 2c_M/η = 4(M+½)²/π. A first-order parametrisation (by t instead of μ) gives O(n) errors per unit and obscures the second term; see `attempts/X2-round2.md`, Route 1.

## Scope

A two-sided explicit estimate of the vertex value λ_n(±1,1) for every even n ≥ 2. It does not locate the maximum of λ_n: lim Λ_n/n² ≥ c* follows, equality is open (X2-28). The remainder bounds are not sharp: measured R_n lies in [−20.5, −1.6] for n ≤ 6400.

## Open items

- Sharp order of R_n := λ_n(1,1) + (n+1) − c*(n+5/2)²: measured R_n ≈ −(2/π²) log²n − 0.54 log n + O(1) (X2-27). The proof above loses a factor 2 in the log² coefficient (it bounds L_c by dropping the factor 1 − V̂ and the upper side by 0). Not needed for the consequences.
- Independent rerun of the ball-arithmetic enclosure of c* and of the numerical checks (auditor).

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-2; uncommitted at writing. First version.
