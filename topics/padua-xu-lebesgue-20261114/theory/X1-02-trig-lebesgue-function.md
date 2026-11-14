# PD-T?padua-xu-lebesgue-20261114-claude-02 — The one-dimensional factor: Lebesgue function of 2n equispaced trigonometric nodes

ID kind: PD-T.
Aliases: X1-02; ω_n; midpoint maximum; L_n is the Chebyshev-zero Lebesgue constant.
Split from: none (one-dimensional lemma for X1-03, X1-04, X1-05).
Split into: none.

## Statement

Let n ≥ 1, let C be one of the two parity classes of ℤ/4nℤ (all odd, or all even residues), u_p = pπ/(2n), d_n as in X1-01, and

  ω_n^C(u) = Σ_{p∈C} |d_n(u − u_p)|,  L_n = (1/n) Σ_{k=1}^n cot((2k−1)π/(4n)).

Call u a *midpoint of C* if u = iπ/(2n) with i an integer of the parity opposite to C.

**(a) Symmetries.** ω_n^C(u + π/n) = ω_n^C(u), ω_n^C(−u) = ω_n^C(u), and ω_n^{even}(u) = ω_n^{odd}(u − π/(2n)).

**(b) Midpoint values and signs.** If u = iπ/(2n) is a midpoint of C, then for every p ∈ C, with m = i − p (odd),
 d_n(u − u_p) = sin(mπ/2) cot(mπ/(4n)) / (2n) ≠ 0,
 its sign is χ(m) := (−1)^{(m₀−1)/2}, where m₀ ∈ {1, 3, …, 2n−1} is the unique element with m ≡ ±m₀ (mod 4n), and ω_n^C(u) = L_n. Moreover, for every odd m,
 χ(−m) = χ(m), χ(m + 4n) = χ(m), χ(m + 2n) = −(−1)^n χ(m).   (χ)

**(c) Maximum.** ω_n^C(u) ≤ L_n for every real u. For n ≥ 2 equality holds if and only if u is a midpoint of C. (For n = 1, ω_1^C ≡ 1 = L_1.)

**(d) Chebyshev interpretation.** Let t_k = cos((2k−1)π/(2n)), k = 1..n (the zeros of T_n), and ℓ_k the Lagrange polynomials of degree ≤ n−1 for these nodes. Then Σ_k |ℓ_k(t)| ≤ L_n on [−1, 1], with equality at t = ±1. So L_n is the Lebesgue constant of polynomial interpolation at the n zeros of T_n.

## Definitions

As in X1-01 for d_n. Natural logarithm is not used here. cot is the cotangent.

## Assumptions

Exact real arithmetic, integer n ≥ 1.

## Status by part

Overall status: **PROVED** (written proof below; audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a), (b), (χ) | PROVED | §§1–2 |
| (c) maximum and equality set, n ≥ 2 | PROVED | §3 |
| (d) | PROVED | §4 |

## Depends on

X1-01 §0 only (the two forms of d_n and d_n(u_p − u_{p′}) = δ_{pp′} within a class). Elementary: a real polynomial with n−1 real zeros below t₁ is monotone to the right of t₁.

## Checks

`python3 code/xu/research/x1_1d_check.py --nmax 2000`, part (d) of its output (mpmath, 40 digits, n = 2..12, 21 points of [0, π/(2n)] each): ω^{odd}(u) = P(cos u), π/n-periodicity, ω(0) = L_n, ω(π/(2n)) = 1 to `1.8826e-39`; `monotonicity failures: 0`. MEASURED, verification only.

## Sources

LITERATURE (context, not used): the formula Λ(T_n zeros) = (1/n)Σ cot((2k−1)π/(4n)) and the fact that the Chebyshev Lebesgue function is maximal at ±1 are classical (Ehlich–Zeller 1966; Rivlin's book); unread here, and re-proved in (d). PD-T270 on main uses the same L_n (its eq. (2)).

## Proof or evidence

**§1. (a).** u + π/n − u_p = u − u_{p−2} and p ↦ p − 2 permutes C, so ω^C(u + π/n) = Σ_{p∈C}|d_n(u − u_{p−2})| = ω^C(u). C = −C and d_n is even, so ω^C(−u) = Σ|d_n(u + u_p)| = Σ|d_n(u − u_{−p})| = ω^C(u). Finally p ↦ p − 1 maps the even class onto the odd class and u − u_p = (u − π/(2n)) − u_{p−1}.

**§2. (b).** For u = u_i and p ∈ C, u − u_p = mπ/(2n) with m = i − p odd, so by X1-01 §0, d_n(u − u_p) = sin(mπ/2) cot(mπ/(4n))/(2n). Here sin(mπ/2) = ±1; mπ/(4n) ∉ πℤ since m is odd; and cot(mπ/(4n)) = 0 would need m ∈ 2n + 4nℤ, impossible for odd m. So the value is finite and nonzero. Let χ(m) ∈ {±1} be its sign, for every odd integer m.

The functions m ↦ sin(mπ/2) and m ↦ cot(mπ/(4n)) are 4n-periodic in m and both odd, so χ is 4n-periodic and even. The odd residues mod 4n are exactly ±m₀, m₀ ∈ {1, 3, …, 2n−1}, and for such m₀: 0 < m₀π/(4n) < π/2, so the cotangent is positive and χ(m₀) = sin(m₀π/2) = (−1)^{(m₀−1)/2}. Finally sin((m+2n)π/2) = (−1)^n sin(mπ/2) and cot((m+2n)π/(4n)) = −tan(mπ/(4n)), whose sign is opposite to that of cot(mπ/(4n)); this gives χ(m+2n) = −(−1)^nχ(m).

As p runs over C, m = i − p runs once over all odd residues mod 4n, and |cot| is even and π-periodic, so
 ω^C(u_i) = (1/(2n)) Σ_{m odd mod 4n} |cot(mπ/(4n))| = (1/(2n)) · 2 Σ_{m₀} cot(m₀π/(4n)) = L_n. ∎(b)

**§3. (c).** By (a) it suffices to treat the odd class and u ∈ [0, π/(2n)]: every real u is mapped into this interval by a shift from (π/n)ℤ and a sign change, and it is mapped to 0 exactly when u ∈ (π/n)ℤ, i.e. when u is a midpoint of the odd class; for the even class use the last identity of (a).

Let 0 ≤ u < π/(2n) and p ∈ {1, 3, …, 2n−1}, ε_p = sin(pπ/2) = ±1. Since cos(pπ/2) = 0,
 sin(n(u − u_p)) = −ε_p cos(nu), sin(n(u + u_p)) = +ε_p cos(nu), and cos(nu) > 0.
Also −π < u − u_p < 0 (because u < π/(2n) ≤ u_p < π) and 0 < u + u_p < π, so cot((u − u_p)/2) < 0 < cot((u + u_p)/2). Hence d_n(u − u_p) and d_n(u + u_p) = d_n(u − u_{−p}) both have the sign ε_p (and are nonzero). The odd class is {±p}, so, with k = (p+1)/2 and ε_p = (−1)^{k−1},

  ω^{odd}(u) = Σ_{k=1}^n (−1)^{k−1} c_k(u), c_k(u) := d_n(u − u_{2k−1}) + d_n(u + u_{2k−1}),   (1)

for 0 ≤ u < π/(2n), and for u = π/(2n) by continuity. From the cosine form of d_n and cos(n u_{2k−1}) = 0,
 c_k(u) = (1/n)(1 + 2 Σ_{j=1}^{n−1} cos(ju) cos(j u_{2k−1})) = q_k(cos u), q_k(t) := (1/n)(1 + 2 Σ_{j=1}^{n−1} T_j(t) T_j(t_k)),
a polynomial of degree ≤ n−1. By the cardinality of d_n, c_k(u_{2k′−1}) = δ_{kk′} + [2k′−1 ≡ −(2k−1) mod 4n] = δ_{kk′} (the bracket is false because 2 ≤ (2k−1)+(2k′−1) ≤ 4n−2). So q_k(t_{k′}) = δ_{kk′}, i.e. q_k = ℓ_k.

Put P = Σ_k (−1)^{k−1} ℓ_k, so that ω^{odd}(u) = P(cos u) on [0, π/(2n)], deg P ≤ n−1 and P(t_k) = (−1)^{k−1}, where 1 > t₁ > t₂ > … > t_n > −1. Let n ≥ 2. P changes sign on each of the n−1 intervals (t_{k+1}, t_k), so it has n−1 distinct real zeros ζ₁, …, ζ_{n−1}, all < t₁; hence deg P = n−1 and P(t) = a Π(t − ζ_k) with a ≠ 0. P(t₁) = 1 > 0 forces a > 0. On [t₁, ∞) every factor is positive and strictly increasing, so P is strictly increasing there. Since cos u ∈ [t₁, 1] for u ∈ [0, π/(2n)] and cos is strictly decreasing, ω^{odd}(u) = P(cos u) < P(1) = ω^{odd}(0) for 0 < u ≤ π/(2n). By (b), ω^{odd}(0) = L_n. For n = 1, d_1(t) = cos²(t/2) and ω_1 ≡ 1 = L_1. ∎(c)

**§4. (d).** For any real u, by the computation in §3, ℓ_k(cos u) = c_k(u) = d_n(u − u_{2k−1}) + d_n(u − u_{−(2k−1)}) (this identity between trigonometric polynomials holds for all u). Therefore Σ_k |ℓ_k(cos u)| ≤ Σ_{p odd mod 4n} |d_n(u − u_p)| = ω^{odd}(u) ≤ L_n by (c), and at u = 0 equality holds by (1) and (b). The value at t = −1 equals the value at t = 1 because the node set {t_k} is symmetric. ∎

## Scope

One-dimensional statements for every n ≥ 1. (c) identifies the full equality set for n ≥ 2. Nothing here is specific to Xu points.

## Open items

Audit only.

## History

2026-11-14, Claude Fable 5.2 (xhigh), round X1-2 researcher. Written to make the product bound of X1-04 and the equality analysis of X1-05 self-contained; (d) is included so that "L_n = Chebyshev Lebesgue constant" does not rest on an unread classical source.
