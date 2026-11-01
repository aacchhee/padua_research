# PD-N051 — endpoint Padua hyperinterpolation does not reproduce quadratics

Provisional alias: `PD-N?mz2d-codex-31`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-N. Aliases: endpoint E2 obstruction; endpoint projection
obstruction. Split from: IDEA-223. Split into: none.

Rules/base `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; 2026-11-01.
Codex, allocated xhigh; runtime model metadata unexposed.

## Statement / negative-result scope

Use the actual signed Lebesgue Padua rule and coefficient operator
`H_(m,m-1)` from definitions.md and PD-T113. For every integer
`m>=3`, this operator reproduces `Pi_1` but fails to reproduce `Pi_2`.
More explicitly set

\[
(q,p)=
\begin{cases}
(T_2(x),T_{m-1}(x)),&m\text{ odd},\\
(T_2(y),T_{m-1}(y)),&m\text{ even}.
\end{cases}
\]

Then, with `h_j=integral_(-1)^1 T_j`,

\[
\langle H_{m,m-1}q-q,p\rangle_{L^2(dx\,dy)}
=\begin{cases}
h_{m-1}-h_{m+1},&m\text{ odd},\\
h_m,&m\text{ even},
\end{cases}\ne0. \tag{1}
\]

Consequently no finite constant C can make
`||f-H_(m,m-1)f||_2<=C E_r(f)` hold for all continuous f for any `r>=2`.
In particular, an E_(m-1)-only error bound fails for every `m>=3`.

Attempted mechanism: promote endpoint reproduction from affine polynomials
to quadratics or to all `Pi_(m-1)` using the cubature exactness. This does
not reject a bound using E1, a separate aliasing term, or convergence of the
operator on each fixed function.

## Assumptions and status

Parameter range: all integers `m>=3`, even checkerboard and coordinate order
as in definitions.md, unnormalized measure `dx dy`. Overall status:
**PROVED** in development. Candidate disposition: **REJECTED: refuted**
for the stated higher-reproduction / E2-only mechanism. Independent audit
pending.

## Depends on

Degree-m cubature exactness, the fixed Padua nodes, and the elementary
Chebyshev product identity. PD-T113 proves affine reproduction.
No external theorem or numerical evidence is needed for (1).

## Proof

For every `p in Pi_(m-1)` and every continuous q, coefficient expansion in
the continuous orthonormal basis gives

\[
\langle H_{m,m-1}q,p\rangle=Q_m(qp). \tag{2}
\]

At `x_j=cos(j pi/m)`, `T_(m+1)(x_j)=T_(m-1)(x_j)`. For odd m the product
identity gives
`q p=(T_(m+1)(x)+T_(m-3)(x))/2`. The second term has degree at most m and
is integrated exactly. The first has the same nodal values as
`T_(m-1)(x)`, which is also integrated exactly. Since integration of a
function of x alone has a factor two from the y interval,

\[
Q_m(qp)-\int_{[-1,1]^2}qp=h_{m-1}-h_{m+1}\ne0.
\]

Both indices are even and `m-1>=2`; their moments
`h_j=2/(1-j^2)` are distinct.

For even m, checkerboard parity gives at every node

\[
T_{m+1}(y_k)=(-1)^k=(-1)^j=T_m(x_j).
\]

Now `q p=(T_(m+1)(y)+T_(m-3)(y))/2`. Again the lower term is exact, and
the high term has quadrature value `Q_m(T_m(x))=2h_m`, by degree-m
exactness. Its continuous integral is zero because `m+1` is odd. The
product defect is therefore `h_m`, which is nonzero. Equation (2) proves
(1) in both cases. Here q and p both belong to `Pi_(m-1)` because `m>=3`.

Affine reproduction was already proved using `(m-1)+1=m`. Thus the
largest complete total-degree space reproduced is exactly `Pi_1`.
Finally the explicit q is in `Pi_2`, so `E_r(q)=0` for every `r>=2`,
whereas (1) forces `||q-Hq||_2>0`. This refutes every asserted E_r-only
bound in the stated scope.

## Checks, sources, scope, history

The odd/even cases include the smallest m=3 and m=4 respectively; all
moments and factors are written explicitly. No numerical execution is
claimed. The source convention checks are recorded in literature.md;
neither a primary-source theorem nor the main Padua MZ target is refuted.
2026-11-01, Codex xhigh: exact endpoint kill test retained as a separate
scoped negative result.
