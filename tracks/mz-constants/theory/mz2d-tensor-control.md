# PD-T117 — Exact tensor-CC extrema on a total-degree space

Provisional alias: `PD-T?mz2d-codex-50`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-T.
Aliases: disjoint coordinate defects; total-degree tensor spectral
reduction; one logarithmic loss for the rectangular tensor control.
Split from: the D7 request for one structural transfer theorem for a
precisely specified Chebyshev-type family.
Split into: none. The interval/order consequences below are direct
applications of the exact reduction and the accepted one-dimensional
theorems, rather than independently proposed mechanisms.

## Statement

Let m>=2 and 0<=n<=m-1 be integers. Let C_N be the positive Lebesgue
Clenshaw--Curtis rule on `cos(j pi/N)`, j=0,...,N, mass two. Define

\[
 R_m=C_m\otimes C_{m+1}
\]

on the full rectangular coordinate grid, mass four, and restrict its
Gram matrix `G^R_(m,n)` to real bivariate polynomials of **total degree**
at most n, with continuous orthonormal Legendre products for dxdy.
Let `lambda_-(N,k),lambda_+(N,k),eta(N,k)` denote the corresponding
one-dimensional CC extreme eigenvalues and deviation on degree k.
Then

\[
 \lambda_{\min}(G^R_{m,n})
  =\min\{\lambda_-(m,n),\lambda_-(m+1,n)\},                 \tag{1}
\]
\[
 \lambda_{\max}(G^R_{m,n})
  =\max\{\lambda_+(m,n),\lambda_+(m+1,n)\},                 \tag{2}
\]
\[
 \|G^R_{m,n}-I\|_2=\max\{\eta(m,n),\eta(m+1,n)\}.         \tag{3}
\]

In particular the full total-degree spectrum is positive and below two.
Writing

\[
 \rho_{m,n}=\max(2n/m-1,0)^2,\quad
 C_*=12(1+\pi)^4(1+2/\pi),
\]

its explicit fixed-ratio interval is

\[
 \operatorname{spec}G^R_{m,n}\subset
 \left[\frac{(1-n/m)^2}{C_*},\ 1+\rho_{m,n}\right].        \tag{4}
\]

At the endpoint n=m-1, if K_N is the explicit constant from PD-T017,

\[
 \frac1{K_{m+1}}\le\lambda_{\min}(G^R_{m,m-1})
 \le\frac{128000}{(\log m)^2},\qquad
 \lambda_{\max}(G^R_{m,m-1})
 \le2-\frac4m+\frac4{m^2}<2.                               \tag{5}
\]

Consequently

\[
 \lambda_{\min}(G^R_{m,m-1})\asymp(1+\log m)^{-2},
 \qquad \|G^R_{m,m-1}-I\|_2\longrightarrow1.              \tag{6}
\]

These statements concern one family, the **positive rectangular tensor
control on a total-degree space**. No signed Padua comparison is part
of them.

## Definitions and assumptions

Write `ell_a=sqrt((2a+1)/2)P_a`, so `int ell_a ell_c=delta_ac`, and
`I_n={(a,b):a,b>=0,a+b<=n}`. Define the one-dimensional Legendre Gram
matrix `A_N^(k)=(C_N(ell_a ell_c))_(0<=a,c<=k)`. It is a principal
submatrix of `A_N^(n)` whenever k<=n. The degree-N exactness of C_N
implies

\[
 (A_N^{(n)}-I)_{a,c}=0\quad\text{whenever }a+c\le N.        \tag{7}
\]

All exactness and interval conclusions use dx or dxdy, with no change
of measure or node count. No rectangular tensor-degree polynomial space
is substituted for `Pi_n`.

## Status by part

Overall status: **PROVED**, written analytic proof; required independent
and Claude audits pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact defect decomposition and extrema (1)--(3) | PROVED | Vanishing mixed term, disjoint supports and principal-submatrix comparison |
| Interval and endpoint consequences (4)--(6) | PROVED | Direct applications of PD-T017/018/022/023 to (1)--(3) |

Candidate disposition: retained, IDEA-227. This is a variant
of classical tensor quadrature with an explicit total-degree support
property. No exhaustive priority or all-family claim is made.

## Depends on

PD-T013: exact CC moments, aliasing and positivity; PD-T017: full-space
lower bound `1/K_N`; PD-T018: endpoint harmonic upper bound;
PD-T022/023: fixed-ratio upper/lower bounds. Their accepted scientific
dispositions are recorded in the current canonical MZ registry; stale
development-stage pending lines inside those files are historical.
The new support proof needs only their elementary exactness statement.
No A1/A2 or signed Padua spectral result is assumed.

## Proof

### 1. The mixed coordinate defect is absent

Set `X=A_m^(n)-I`, `Y=A_(m+1)^(n)-I`. Product weights give exactly

\[
 (G^R_{m,n})_{(a,b),(c,d)}
  =(\delta_{ac}+X_{ac})(\delta_{bd}+Y_{bd}).                \tag{8}
\]

If `X_ac Y_bd` were nonzero, (7) would require
`a+c>=m+1` and `b+d>=m+2`. But the total-degree cutoffs imply

\[
 a+b+c+d\le2n\le2m-2<2m+3,
\]

a contradiction. Thus, on exactly `I_n`,

\[
 G^R=I+E_x+E_y,\qquad
 (E_x)_{(a,b),(c,d)}=X_{ac}\delta_{bd},\quad
 (E_y)_{(a,b),(c,d)}=\delta_{ac}Y_{bd}.                    \tag{9}
\]

The analogous unnormalized product-Chebyshev pencil makes the Hankel
transfer explicit. Let `M_N,R_N` be its continuous/discrete one-variable
mass matrices and `D_N=2(M_N-R_N)`, as in PD-T013. If J is the injection
of the total-degree coefficient set into the rectangular coefficient
set, then

\[
 R^{\rm Cheb}_{m,n}=J^T\left[
 M_m\otimes M_{m+1}
 -\tfrac12(D_m\otimes M_{m+1}+M_m\otimes D_{m+1})\right]J.
                                                               \tag{10}
\]

The omitted `D_m tensor D_(m+1)` term is zero by exactly the same
degree count: a nonzero D entry needs the sum of its two indices to
exceed its mesh denominator. Here every product mode has degree at most
2n<=2m-2, matching the campaign's frozen range. Formula (9) is (10) in
the continuously orthonormal product basis; it also follows directly
from (8), without assuming any Loewner sign for a Hankel defect.

### 2. The two remaining operators have disjoint active supports

If row (a,b) of E_x is nonzero, there exists c<=n-b with `a+c>m`.
Therefore

\[
 a-b>m-n.
\]

Similarly, a nonzero row of E_y must satisfy

\[
 b-a>m+1-n.
\]

These two inequalities cannot both hold for n<=m-1. Define the two
coordinate wedges by these strict inequalities. Each defect has both
its rows and columns in its own wedge, since it is symmetric. Thus the
coefficient space splits orthogonally into the x wedge, the y wedge,
and their complement; G is `I+E_x`, `I+E_y`, and I on these three
pieces. In particular `E_x E_y=E_y E_x=0`. This is the structural fact
that prevents multiplying two critical endpoint losses.

### 3. Identify the extreme eigenvalues

At fixed b, the matrix of `I+E_x` on a=0,...,n-b is exactly the
principal matrix `A_m^(n-b)`. Its rows outside the x wedge are identity
rows by the preceding support argument. Removing those identity rows
therefore leaves just its active block, with no coupling to the removed
part. Every eigenvalue in that active block lies between the minimum
and maximum of `A_m^(n)` by the variational principle for principal
submatrices. The same argument for `I+E_y` uses the principal matrices
`A_(m+1)^(n-a)`.

The remaining spectrum consists of ones, which are also between these
coordinate extrema: the constant polynomial is an exact eigenvector
with eigenvalue one for either coordinate Gram matrix, since n<m.
This proves that the full extrema are bounded by the right sides of
(1)--(2).

Conversely, the full coordinate subspace `span{ell_a(x)ell_0(y):a<=n}`
is invariant under G. Its Gram block is exactly `A_m^(n)`: E_x
preserves b=0 and E_y vanishes there, including all row/column couplings,
by its support inequality. Likewise `span{ell_0(x)ell_b(y):b<=n}`
is invariant and has block `A_(m+1)^(n)`. Each coordinate spectrum is
therefore contained in the full spectrum. This proves the reverse
extreme inequalities and establishes (1)--(2). The symmetric spectral
formula for `||G-I||` proves (3).

### 4. Apply the accepted one-dimensional bounds

PD-T023 gives each coordinate minimum at least
`(1-n/N)^2/C_*`. Since N is m or m+1, their minimum is at least
`(1-n/m)^2/C_*`. PD-T022 similarly bounds the larger coordinate maximum
by `1+max(2n/m-1,0)^2`. This proves (4), with positive lower endpoint
and upper endpoint strictly below two.

At n=m-1, PD-T017 gives both coordinate minima at least `1/K_(m+1)`:
K_N is nondecreasing because all of its defining harmonic sums are
nondecreasing. Explicitly

\[
 K_N=4\pi^2(\pi+1)^2s_N
       (s_N+2H_{\lfloor N/2\rfloor+1}),\qquad
 s_N=2H_{N+1}-1.
\]

The x coordinate and PD-T018 give the upper minimum bound in (5).
The upper endpoint in (5) follows by substituting n=m-1 into (4).
Since `K_(m+1)=O((1+log m)^2)`, (5) proves the two-sided order in (6),
with harmless finite small-m adjustment between log m and 1+log m.
Finally every such tensor deviation is below one, while
`eta>=1-lambda_min` and the minimum tends to zero. These two inequalities
give its limit one. No rate for `1-eta` is inferred. ∎

## Checks and provenance

The analytic mixed-term/support kill test was performed before any
numerical regression and passed by the two explicit contradictions in
sections1--2. A deterministic float64 regression then compared the
extrema from the directly formed tensor Legendre matrix against the
two separately formed one-dimensional spectra for m=2,3,4,5,8,10,16,
and each distinct n in `{0,floor(m/2),m-1}`. There were 20 distinct
(m,n) cases; maximum extreme discrepancy was `1.12e-15`.

Executed from `/workspace/padua_research`, Python3.12.14,
NumPy2.3.5, SciPy1.17.0; no random seed. The inline command formed
`Cx=Vx.T @ (cc_weights(m)[:,None]*Vx)` and the analogous Cy, with
continuous orthonormal Legendre columns through n. It formed every
total-degree entry as `Cx[a,c]*Cy[b,d]`, ran `scipy.linalg.eigvalsh`
on this matrix and each coordinate matrix, and compared their extrema.
The weight producer `mz2d_spectra.py` had SHA256
`623acdf06e4ad1c50c3c0562f47f037b8efa15fcc332c2f1ee7a7d0f88ee8b76`.
These floating values are diagnostic MEASURED comparisons, not finite
proof obligations or rigorous eigenvalue enclosures. The theorem is
analytic and has no computer-assisted dependency.

## Sources and limits

Closest local predecessors and complete gate: D7.md and ideas-d7.md.
Classical product quadrature supplies the tensor factorization; the
total-degree support calculation is written out rather than assumed.
Historical overlap is not exhaustively cleared. Other Xu, Morrow--
Patterson and Lissajous--Chebyshev families remain deferred pending
their exact primary-source convention checks.

The signed Padua rule has additional checkerboard complement aliases.
Neither its lower bound nor a comparison to this control follows from
(10). D2's pointwise tensor-majorant counterexample and D3's signed
corner corrections remain applicable. PD-T028 stays OPEN.

## Open items and history

Required independent/Claude mathematical audit; optional independent
replay of the diagnostic. No sharper one-dimensional limiting constant
or endpoint eta-deficit rate is asserted.

2026-11-01, Codex D7 developer, requested gpt-6.1-sol xhigh; rules
`806cc7b4509fd93bae652f9545d32d95529f8281`. Activated only after D2
and D3 stopped. One structural family was selected; the prewritten
mixed-support test preceded the proof and diagnostic. No Git mutations.
