# Fixed conventions for the two-dimensional Padua MZ campaign

Rules read at `cf89b140530d5838bdb208a8c28f3e7aa676ace3`.
Developer: Codex, requested `gpt-6.1-sol`, xhigh mathematical effort.
These conventions were fixed before campaign numerical runs.

For every integer `m >= 1`, put

\[
 x_j=\cos(j\pi/m),\quad 0\le j\le m,\qquad
 y_k=\cos(k\pi/(m+1)),\quad 0\le k\le m+1,
\]
\[
 \operatorname{Pad}_m=\{(x_j,y_k):j+k\equiv0\pmod2\}.
\]

This is exactly `padua(m)` in
`topics/mz-constants/sources/padua_mz_inputs/code/mz_padua_cc_check.py`,
called by `tracks/mz-constants/code/reproduce.py`. Its cardinality is
`(m+1)(m+2)/2`. The coordinate order and the even checkerboard are fixed.
The unused second return value of `padua` consists of Chebyshev cubature
weights; it is **not** the Lebesgue quadrature weight vector below.

Write `Pi_n` for real bivariate polynomials of total degree at most `n`.
The signed interpolatory Lebesgue rule is

\[
 Q_m f=\sum_{j+k\ {\rm even}}w_{jk}f(x_j,y_k),\qquad
 Q_m q=\int_{-1}^1\!\int_{-1}^1 q(x,y)\,dx\,dy
 \quad(q\in\Pi_m).
\]

The weights are the unique real solution of these equations (equivalently,
the integrals of the Padua cardinal polynomials). Their signs are not
assumed positive. In particular `sum(w)=4`. All integrals use the
unnormalized measure `dx dy`, of mass four.

Let `T_r(cos t)=cos(rt)` and

\[
 h_r=\int_{-1}^1T_r(x)\,dx=
 \begin{cases}2/(1-r^2),&r\text{ even},\\0,&r\text{ odd}.\end{cases}
\]

Then the weight equations may be written `V.T w = (h_a h_b)_{a+b<=m}`
for unnormalized products `V_{(j,k),(a,b)}=T_a(x_j)T_b(y_k)`.
Replacing each positive-degree `T_r` by `sqrt(2) T_r`, as in `reproduce.py`,
does not change the weights.

For the Legendre polynomial `P_r` with `P_r(1)=1`, put
`ell_r=sqrt((2r+1)/2) P_r`. The orthonormal basis of `Pi_n` is

\[
 \phi_{ab}(x,y)=\ell_a(x)\ell_b(y),\qquad a,b\ge0,\quad a+b\le n.
\]

The ordering matches `total_degree(n)`: increasing `a+b`, and decreasing
`a` within each degree. With `B_{(j,k),(a,b)}=phi_ab(x_j,y_k)`, define

\[
 G_{m,n}=B^\mathsf T\operatorname{diag}(w)B,\quad
 \lambda_-(m,n)=\lambda_{\min}(G_{m,n}),\quad
 \lambda_+(m,n)=\lambda_{\max}(G_{m,n}),
\]
\[
 \eta(m,n)=\|G_{m,n}-I\|_2
 =\max\{1-\lambda_-(m,n),\lambda_+(m,n)-1\}.
\]

These are symmetric-form eigenvalues even when some weights are negative.
The campaign endpoint is `n=m-1`; exact aliasing only up to total degree
`2m-2` suffices for that Gram matrix. The condition `eta<1` is equivalent
to `0<lambda_-` and `lambda_+<2`.

For the control, `C_N` is the one-dimensional Clenshaw--Curtis rule on
`cos(j*pi/N)`, exact on degree at most `N`, with respect to `dx` (mass two).
The default matching rectangular tensor control is `C_m tensor C_(m+1)`
on the full grid used above, restricted to the **same total-degree**
Legendre basis `Pi_n`. Its weights have sum four. It is distinct from a
square tensor-degree polynomial space. If `C_m tensor C_m` is also used,
label it explicitly as the square control. Compare controls at the same
`m,n`; a node-count-matched comparison needs its own stated convention.

The isometric marginal embedding is `p(x) -> p(x)/sqrt(2)`, not `p(x)`.
The signed Padua form compresses under this embedding to `C_m(p^2)`.
No equality of the full `y` marginal with `2 C_(m+1)` is assumed: there
are `m+2` distinct y levels but only `m+1` prescribed univariate moments.
Both rules integrate y polynomials of degree at most `m`, which alone
does not identify their weights or their higher-degree moments.

No numerical evidence, positivity claim, spectral theorem, or novelty
claim is asserted by this definitions file.
