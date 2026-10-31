# PD-T?charter-u1-codex-01 — Alternation Hankel criterion away from characteristic two

ID kind: PD-T. Aliases: U1b; odd-characteristic restriction of source U1a; triangular tensor Gram factorization.
Split from: supplied arbitrary-field U1a, whose original scope is refuted in `char2-refutation.md`.
Split into: none. The all-characteristic replacement is a separate statement in `all-characteristic-criterion.md`.

## Statement

Let K be any field of characteristic different from 2 and m≥0. Let X=(x_0,…,x_m) and Y=(y_0,…,y_(m+1)) have distinct entries within each list. Cross-axis coincidences are permitted. Put N=(m+1)(m+2)/2 and S_e={(x_i,y_j):i+j≡e mod 2}, e=0,1. Each S_e has N points. Let V_e be its total-degree≤m monomial evaluation matrix, in any fixed row and column order.

For a length-L list H, put ω_H(t)=∏(t-h_i), w_i=(-1)^i/ω′_H(h_i), μ_k=Σ_i w_i h_i^k, and Δ_r(H)=det[μ_(a+b)]_(a,b=0)^(r−1), with Δ_0=1. Then

`det(V_e)^2 ∏_(i+j≡e) w_i(X)w_j(Y) = 2^(−N) ∏_(r=1)^(m+1) Δ_r(X)Δ_r(Y).` (1)

Consequently S_e is unisolvent for Π_m(K) if and only if Δ_r(X)≠0 for r=1,…,m and Δ_r(Y)≠0 for r=1,…,m+1. This is exactly the source's finite-support quasi-definiteness cutoff L−1. Both parities have the same unisolvence status, for even and odd m alike.

## Assumptions and definitions

All arithmetic is exact in K. There is no order, positivity, algebraic closure, distinctness across axes, or square-root hypothesis. Empty minor ranges are vacuous. Unisolvent means evaluation Π_m(K)→K^N is an isomorphism. The finite cutoff is essential: no assertion of infinite quasi-definiteness is made.

## Status by part

Overall status: PROVED (developer proof; independent adversarial audit pending).

| Part | Status | Evidence |
|---|---|---|
| Exact identity (1), and the stated iff | PROVED | Complete proof below, no imported theorem dependency |

Candidate disposition: survives as an explicit restriction, not acceptance of the refuted arbitrary-field conjecture. Mechanism is a reformulation/direct corollary of known Padua-like axis determinant factorization; literature/U1-COMPARISON.md read in full. No novelty claim.

## Depends on

Only elementary polynomial interpolation, determinants and field arithmetic, proved as used below. No source assertion is a mathematical dependency.

## Proof

For a list H of length L, univariate Lagrange interpolation in degree≤L−1 shows

`Σ_i h_i^a / ω′_H(h_i) = 0 (0≤a<L−1), and =1 (a=L−1).` (2)

Indeed the sum is the coefficient of t^(L−1) in the interpolant of t^a. For a monomial x^a y^b of total degree≤2m, its product ordinary-barycentric sum on X×Y vanishes: a<m or b<m+1, since otherwise a+b≥2m+1. By linearity this applies to fg for all f,g∈Π_m.

Let G be the matrix of `(L_X⊗L_Y)(fg)` on the total-degree monomials, and let G_e=V_e^T diag(w_i(X)w_j(Y)) V_e. The difference G_0−G_1 is precisely the ordinary-barycentric product sum, so is zero by (2). Also G=G_0+G_1. Hence G_e=G/2 and

`det(V_e)^2 ∏_(i+j≡e) w_i(X)w_j(Y)=2^(−N) det G.` (3)

For completeness, the universal triangular product-moment determinant identity is

`det G = ∏_(r=1)^(m+1) Δ_r(X)Δ_r(Y).` (4)

Prove it first over Q in independent formal moment variables (through order 2m). Every leading minor is a nonzero polynomial: for example, specializing each moment sequence to unit weights on m+1 distinct rational nodes yields a positive definite real Gram matrix of each required order. In the fraction field, Gram–Schmidt gives monic univariate p_a,q_b, of norms Δ_(a+1)(X)/Δ_a(X) and Δ_(b+1)(Y)/Δ_b(Y). The products p_a q_b, a+b≤m, form a monic triangular change of the monomial basis, with determinant 1. Their Gram matrix is diagonal. The x-norm for degree a occurs m−a+1 times. On telescoping, each Δ_r(X), r=1,…,m+1, has exponent 1; likewise for Y. This proves (4) in the fraction field. Both sides are polynomials with integer coefficients in the formal moments, so equality holds identically over Z and specializes over every field, including when some minors vanish. Thus Gram–Schmidt is scaffolding for a polynomial identity, not an assumption at specialization.

Finally, Δ_L(H)=det(V_H)^2∏w_i =1. In fact ∏ω′_H(h_i)=(-1)^(L(L−1)/2) det(V_H)^2 and ∏(-1)^i=(-1)^(L(L−1)/2). All w_i and 2 are nonzero. Combining (3)–(4), and omitting the automatically nonzero full minor Δ_(m+1)(X), proves the iff and (1).

## Checks and sources

Exact checker: `topics/charter-unisolvence-20261031/directions/U1/exact_checker.py`; run and scope recorded separately in directions/U1/evidence.md. Source hs_ff.py was actually reproduced by U0; its agreement is measured, not a dependency. Closest source: Harris–Simanek (2021), Thm 1 and Appendix A.1 as reported in provisional LIT?charter-unisolvence-codex-01; original-source verification and De Marchi–Usevich comparison are external pending obligations.

## Scope and open items

The proof establishes every m, both parities and every field of characteristic≠2. It does not repair the original characteristic-2 functional; that functional loses the parity information. The corrected functional and all-characteristic statement are separate. Independent adversarial reconstruction and final literature/ID review remain pending.

## History

2026-10-31, Codex `gpt-6.1-sol` xhigh, rules/base d36722823441dc40c6e19d69a174459348dd309c. Original arbitrary-field wording retained in negative record; restriction stated explicitly after characteristic-2 refutation.
