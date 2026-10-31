# PD-T?bivariate-lanczos-claude-111 — Measures that agree with a product measure up to degree 2n have product-type window coefficients up to degree n; Harris–Simanek checkerboards agree with half a product measure up to degree 2m

ID kind: PD-T.
Aliases: moment-matching extension of the product factorisation; checkerboard lemma; divided-difference cancellation.
Split from: none.
Split into: none.

## Statement

[EXACT]

1. **(Moment matching.)** Let μ be a positive discrete measure satisfying U(n) and μ⁰ = c·(μ_X ⊗ μ_Y) (c > 0, μ_X, μ_Y positive univariate measures with at least n+1 support points each) such that ∫p dμ = ∫p dμ⁰ for all p ∈ Π_{2n}. Then the graded orthonormal vectors of μ up to degree n are (node values of) p_{t−j}(x) r_j(y) (orthonormal polynomials of μ_X, μ_Y, normalised for μ⁰), and every window coefficient creating a column of degree ≤ n has the product-type values of PD-T?…-105 part 1 (with the univariate Jacobi coefficients of μ_X, μ_Y). Consequently the factorisation of the node propagator (PD-T?…-105 part 2) holds up to degree n at every node z = (ξ, η) of μ, with the univariate impulse responses of μ_X at ξ and of μ_Y at η.
2. **(Checkerboards.)** Let x_0 < … < x_m and y_0 < … < y_{m+1} be real, a_i := 1/|ω_X′(x_i)|, b_j := 1/|ω_Y′(y_j)| (ω_X(t) = Π(t − x_i), ω_Y likewise), e ∈ {0, 1}, and μ_e := Σ_{i+j ≡ e (mod 2)} a_i b_j δ_{(x_i, y_j)}. Then for every polynomial p of total degree ≤ 2m,
  μ_e(p) = ½ (μ_X ⊗ μ_Y)(p), μ_X := Σ_i a_i δ_{x_i}, μ_Y := Σ_j b_j δ_{y_j},
  so part 1 applies with n = m (|S_e| = N_m); in particular the window coefficients of every column of degree ≤ m are product-type, and the recurrence on S_e is, in exact arithmetic, a direct sum of univariate Jacobi chains of μ_X and μ_Y up to completion.
3. **(Padua with cubature weights)** is the case x_i = −cos(iπ/m), y_j = −cos(jπ/(m+1)) of part 2 (Chebyshev–Lobatto grids; 1/|ω′| are, up to normalisation, the Lobatto weights with ½ at the end points).

## Definitions

Divided difference f[t_0, …, t_r] = Σ_i f(t_i)/ω′(t_i) (ω = Π(t − t_i)); it vanishes for deg f < r.

## Assumptions

Distinct ordered abscissae; exact arithmetic. Part 1 needs U(n) for μ (true for S_e with n = m by |S_e| = N_m and the positive-definite Gram of the products, which follows from part 2).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. moment matching ⇒ product-type coefficients and factorisation | PROVED | proof below |
| 2. checkerboard lemma | PROVED (elementary, self-contained) | numerical check: window coefficients vs product reference ≤ 8.9e-16 (Chebyshev–Lobatto), 5.3e-15 (equispaced) in double; clustered family 1.0e-6 in double, 9.4e-10 in long double — a precision effect (ratio ≈ ε-ratio), see PD-T?…-112 |
| 3. Padua cubature as a special case | PROVED (identification; the Lobatto-weight formula is classical background) | |

## Depends on

PD-T?…-105 (factorisation), PD-T?…-101 (graded basis). The statement of the codex branch (`codex/charter-unisolvence-20261031@eb7bdcd`, PD-T001/PD-T003, not accepted) that the checkerboard basis is a product basis is **not** used: part 2 is proved here independently.

## Checks

`tracks/bivariate-lanczos/code/L1/l1_r04_checkerboard.py` ((C1) column), `l1_r04_checkerboard_diag.py` (long-double re-check).

## Proof or evidence

*1.* Inner products of polynomials of degree ≤ n are integrals of polynomials of degree ≤ 2n, so the Gram–Schmidt basis of the monomials in graded order is the same for μ and μ⁰ (as polynomials); for μ⁰ it is the product basis (PD-T?…-105 part 1, whose proof only uses orthonormality of products under a product functional). A window coefficient creating a column of degree t+1 ≤ n is ⟨A q_p, q_l⟩ with deg(A q_p) ≤ t+1, deg q_l ≤ t+1, or a norm of a residual of degree t+1: integrals of degree ≤ 2t+2 ≤ 2n. So they coincide with μ⁰'s. PD-T?…-105 part 2 uses only the coefficients and the point z, with |r_l(η)| ≤ 1/√(μ_Y-weight at η) when η is a node of μ_Y.
*2.* Signs: for ordered abscissae sign ω_X′(x_i) = (−1)^{m−i}, so 1/ω_X′(x_i) = (−1)^{m−i}a_i; likewise 1/ω_Y′(y_j) = (−1)^{m+1−j}b_j. The indicator of i + j ≡ e is ½(1 + (−1)^{e}(−1)^{i}(−1)^{j}). For p = f(x)g(y),
  μ_e(fg) = ½[Σ_i a_if(x_i) Σ_j b_jg(y_j) + (−1)^e Σ_i (−1)^i a_i f(x_i) Σ_j (−1)^j b_j g(y_j)],
  and Σ_i (−1)^i a_i f(x_i) = (−1)^m Σ_i f(x_i)/ω_X′(x_i) = (−1)^m f[x_0, …, x_m], which is 0 for deg f ≤ m − 1; Σ_j (−1)^j b_j g(y_j) = (−1)^{m+1} g[y_0, …, y_{m+1}], 0 for deg g ≤ m. For a monomial x^a y^b with a + b ≤ 2m, either a ≤ m − 1 or b ≤ m, so the second term vanishes. Extend by linearity. |S_e| = ⌈(m+1)(m+2)/2⌉ for either parity e with these lengths: exactly half of the (m+1)(m+2) grid points, i.e. N_m.
*3.* For Chebyshev–Lobatto points 1/|ω′(x_i)| ∝ 1 for interior points and ½ at the end points.

## Scope

Gives a family of exact product-type measures with M = N on non-tensor supports, with conditioning dialled by the abscissae (weights down to 1e-33 for the cubic clustering). It says nothing about finite precision: the measured behaviour on these sets (stable for Chebyshev–Lobatto, mild growth for equispaced, strong growth for clustered abscissae) is PD-T?…-112.

## Open items

None for the statements.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R04).
- 2026-10-31T23:05Z (re-check after reconstruction 01): not affected by B1/B2 (exact algebra). Note: on product-type measures the mirror rule gives the same product structure by x ↔ y symmetry; the alt/adapt rules of PD-N?…-105 are not covered by part 1's chain description.
