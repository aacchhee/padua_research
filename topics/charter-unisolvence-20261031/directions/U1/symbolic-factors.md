# U1 exact symbolic factors, m=2,3,4

Rules/base `d36722823441dc40c6e19d69a174459348dd309c`; Codex development, 2026-10-31. This is a verification record for the proved determinant-square identity, not a new mechanism or an independent audit. Indeterminate nodes here are idealized scaffolding; the identities specialize over every field with distinct nodes within each axis.

## Compact polynomial definitions

Put d_ij(H)=h_i−h_j for i<j, C(H)=∏_(i<j, i+j odd)d_ij(H), E=H_even, O=H_odd. The following factors are polynomials, with no denominators:

- For length 4 or 6, A(H)=ΣE−ΣO.
- For length 5, put a=ΣE, b=Σ_(i<j in E)e_i e_j, u=ΣO, v=∏O and define B(H)=ua−b−u²+v.
- For length 6, put a=e1(E), b=e2(E), c=e3(E), u=e1(O), v=e2(O), w=e3(O), α=a−u, β=v−b, γ=c−w. Define Q(H)=−(β²+αaβ−αγ+α²b).

The even-index barycentric Hankel minors needed by the general formula reduce to

| Length L | H1 | H2 |
|---|---|---|
| 3 | 1/C(H) | not needed |
| 4 | A(H)/C(H) | central nonzero factor |
| 5 | B(H)/C(H) | 1/C(H) |
| 6 | Q(H)/C(H) | A(H)/C(H) |

Thus non-difference factors are A(Y) for m=2; A(X)B(Y) for m=3; B(X)A(Y)Q(Y) for m=4, each with multiplicity 1 in det V_e. In its square each multiplicity is 2. Characteristic 2 is obtained by reducing these integer polynomials, including the coefficient 2 appearing in the expanded quartic, before testing nonvanishing.

## Exact difference multiplicities

Take row order increasing (i,j), and monomials (1,x,y,x²,xy,y²,…) in increasing total degree with decreasing x-degree inside each degree. Each determinant equals the listed sign, times all listed difference powers, times the non-difference factor just given. Unlisted pair differences have exponent zero.

| m | Axis/pairs | Exponent e=0 | Exponent e=1 |
|---|---|---|---|
| 2 | X: 01,12 | 1 | 1 |
| 2 | X: 02 | 2 | 2 |
| 2 | Y: 02 | 2 | 1 |
| 2 | Y: 13 | 1 | 2 |
| 3 | X: 01,03,12,23 | 1 | 1 |
| 3 | X: 02 | 3 | 2 |
| 3 | X: 13 | 2 | 3 |
| 3 | Y: 02,04,13,24 | 2 | 2 |
| 4 | X: 01,03,12,14,23,34 | 1 | 1 |
| 4 | X: 02,04,13,24 | 3 | 3 |
| 4 | Y: 02,04,24 | 3 | 2 |
| 4 | Y: 13,15,35 | 2 | 3 |

Signs: m=2 has (−,+); m=3 has (+,−); m=4 has (+,−), in parity order (0,1).

## Exact computation actually performed

Command: `python3 topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --symbolic --output /workspace/padua-cold/charter-unisolvence-20261031/U1/symbolic-factors.json`.

The checker computed the fully multivariate direct 6×6 determinant for m=2, both parities. For m=3,4 it assembled the full multivariate factorization from the proved determinant-square identity and exact small axis polynomial determinants. It did **not** directly expand the full multivariate 10×10 or 15×15 checkerboard determinants. For every m=2,3,4 and both parities, it separately computed a direct checkerboard determinant on a one-variable slice, verified equality with the factor expression, and fixed the global sign. The squared identity in the integral domain Q[nodes] implies the unsquared determinant equals one of the two signs of the factor expression; a nonzero slice fixes that sign globally.

Slices use X=(0,1,3,…), Y=(0,2,5,9,14,t), truncated to the required length with the final entry replaced by t:

| m | X | Y | direct determinant e=0 | direct determinant e=1 |
|---|---|---|---|---|
| 2 | 0,1,3 | 0,2,5,t | −450(t−3)(t−2) | 90(t−3)(t−2)² |
| 3 | 0,1,3,7 | 0,2,5,9,t | 2000376000 t²(t−8)(t−5)² | −4000752000 t²(t−8)(t−5)² |
| 4 | 0,1,3,7,11 | 0,2,5,9,14,t | 86388604797742963752960000 (t−9)²(t−8)(t−2)²(t²−15t+20) | −959873386641588486144000 (t−9)³(t−8)(t−2)³(t²−15t+20) |

All six comparisons passed. Raw JSON contains the expanded quartic and complete factor lists. Scope is exact symbolic algebra in characteristic zero followed by the proved integral specialization, not an assumption that numeric slices alone prove a multivariate identity.

## Axis-factor conversion used to avoid expansion

Let E have a nodes, c(t)=∏_(z∈O)(t−z), and let D_r be its a×a evaluation determinant for columns 1,…,t^(r−1),c,…,t^(a−r−1)c. Then

`H_r=(-1)^(r(a−r)+r(r−1)/2) D_r/[Vand(E)∏_(z∈E)c(z)].`

To verify the sign, Laplace-expand D_r in its first r columns, over subsets I⊂E with complement J. After division by Vand(E)∏E c, its I term is (-1)^(r(a−r))/[∏_(i∈I,j∈J)(e_i−e_j)∏_(i∈I)c(e_i)]. Cauchy–Binet for H_r has the same term with sign (-1)^(r(r−1)/2). This proves the formula, including empty blocks. The only divisions are node differences. This is the classical axis-factor/Hankel bridge identified by literature/U1-COMPARISON.md, now with the sign convention fixed for this checker.

The first implementation expanded the global rational numerator/denominator and was interrupted (exit130). An intermediate implementation accumulated global factors, completed successfully, but still expanded rational moment determinants. The final implementation computes these size≤3 polynomial axis determinants and accumulates factor exponents, avoiding the costly expansion. These are computational-route corrections, not negative mathematical claims and not PD-N results. Only the final checker hash and its rerun outputs are canonical evidence.
