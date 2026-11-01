# PD-T109 — Finite masked-tensor Padua defect architecture

Provisional alias: `PD-T?mz2d-codex-04`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-T.
Aliases: signed-degree triangular truncation; finite tensor Hankel/Toeplitz
defect; half-plane mask Fourier control.
Split from: original combined PD-T106, whose exact alias and
rational pencil remain in `mz2d-aliasing.md`. The full original combined
architecture statement is preserved below.
Split into: none. The orchestrator records the mapping at PR preparation.

## Statement

On the full moment range `a+b<=2m-2`, `E_m` is the sum of ten separable
scalar moment kernels, supported on five explicit regions, each cut
out by coordinate intervals and one scalar half-plane. Consequently
`D` is a sum of at most 160 compressed tensors of one-dimensional
Hankel or one-sided Toeplitz matrices, each subjected to a single
one-dimensional block triangular truncation in signed-degree labels.
The number 160 is independent of `m,n`; empty terms can be omitted.
Each such truncation has spectral-norm multiplier bound

\[
 1+\log(8n+1).                                     \tag{5}
\]

This is a concrete finite operator architecture with a proved norm
control. It is not a bound for `||G-I||`, a positive-definiteness result,
or a sharp estimate in the continuous Lebesgue mass metric.

Use the definitions and exact moments `q_m`, `h`, `E_m`, continuous
mass `M` and signed mass `R` of
[PD-T106](mz2d-aliasing.md). Here `D=R-M` on the
product-Chebyshev basis for `Pi_n`, `m>=2`, `0<=n<=m-1`.

## Definitions

For a scalar sequence `f`, a Hankel matrix has entries `f(i+k)`, a
symmetric Toeplitz matrix has entries `f(|i-k|)`, and one-sided Toeplitz
matrices retain respectively `i>=k` and `i<k`. A block triangular
truncation with integer row/column labels `r_alpha,s_beta` is the Schur
multiplier `A_alpha,beta -> 1_(r_alpha+s_beta<=c) A_alpha,beta`.
Repeated labels are allowed; the norm proof does not depend on their
multiplicities. The matrix norm throughout the architecture claim is
the Euclidean induced spectral norm in the **Chebyshev coefficient**
coordinates. It is not the Legendre coefficient norm.

## Assumptions

Exact real arithmetic; `m>=2`, `0<=n<=m-1`, the even checkerboard,
signed `dx dy` interpolatory rule, and total-degree conventions in
`definitions.md`. Each one-dimensional scalar sequence is extended by
zero outside its required coordinate range. Empty alias regions and
operator terms are omitted.

## Status by part

Overall status: **PROVED** in development; independent analytic audit
pending. This substantive architecture is split from the separately
PROVED alias theorem according to the workflow.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Ten separable kernels on five scalar half-plane regions | PROVED | Exact alias partition below |
| At most 160 compressed tensor H/T terms | PROVED | Four product choices and four sign sectors |
| One-dimensional mask norm `<=1+log(8n+1)` | PROVED | Exact unitary Fourier integral |

Candidate / claim disposition: retained variant/application; no novelty
claim. The spectral target PD-T028 remains OPEN.

## Depends on

PD-T106: all-degree alias formula (1) and rational defect
pencil (3)--(4). No external theorem is used. Geometric sums, the sine
chord inequality and elementary matrix norm properties are proved or
used explicitly below.

## Checks

Rules read at `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; the later main
merge at `806cc7b4509fd93bae652f9545d32d95529f8281` did not change
applicable rules, as reported by the orchestrator. No numerical or
exact-arithmetic experiment was executed by this mathematical developer
for this architecture. The D1 pre-run gate and actual analytic outcome
are in `topics/padua-mz-2d-20261101/directions/D1.md`.

## Sources

Local alias theorem PD-T106; accepted cardinal dependency
PD-T101 is needed only for existence of the rule, not for the masked
operator estimates. Separate campaign primary literature verification
is not inherited as a proof. Historical originality is unverified.

## Proof or evidence

### 3. Five alias regions, each a separable kernel under one half-plane

For `a+b<=2m-2`, one has `a<2m` and `b<2m+2`. Both `a>m` and
`b>m+1` cannot hold. Formula (1) reduces to the following disjoint
partition. All degrees are nonnegative integers; the total-degree
restriction remains in force throughout.

| Region | Coordinate and half-plane conditions | Exact `q_m(a,b)` |
|---|---|---|
| L | `a<=m`, `b<=m+1`, `a+b<=m` | `h_a h_b` |
| C | `a<=m`, `b<=m+1`, `a+b>m` | `h_(m-a) h_(m+1-b)` |
| X0 | `a>m`, `a-b>=m` | `h_(2m-a) h_b` |
| X1 | `a>m`, `a-b<m` | `h_(a-m) h_(m+1-b)` |
| Y0 | `b>m+1`, `b-a>=m+2` | `h_a h_(2m+2-b)` |
| Y1 | `b>m+1`, `b-a<m+2` | `h_(m-a) h_(b-m-1)` |

For the x-outside case `A=2m-a,B=b`, the low-degree condition is
`a-b>=m`, giving X0. Its complement gives X1. The y-outside case
`A=a,B=2m+2-b` similarly gives Y0/Y1. This proves the table, including
the boundary inequalities. The apparent degree indices in the table
are nonnegative on their indicated regions; sequences outside their
needed coordinate ranges can be extended by zero.

The defect vanishes on L. On each of the other five regions it is
the displayed product `f(a)g(b)` minus `h_a h_b`. Hence it is ten
separable kernels multiplied by masks. Coordinate-range constraints
can be absorbed into `f,g`; the sole coupled constraint in each mask
is one of `a+b>m`, `a-b>=m`, `a-b<m`, `b-a>=m+2`, or `b-a<m+2`.
Strict comparisons are non-strict integer comparisons after changing
the threshold by one. This is a bounded separable structure; an
arbitrary bivariate kernel does not have such a representation.

### 4. Pullback to tensor Hankel/Toeplitz matrices

Temporarily work on the square coefficient grid `0<=i,j<=n`, and let
`P_n` denote the coordinate inclusion of `I_n` into that grid. Fix one
of the ten kernels and one of the four product-to-sum choices

\[
 a=i+k\ \text{or}\ |i-k|,\qquad
 b=j+l\ \text{or}\ |j-l|.
\]

Without the half-plane mask, the associated matrix is exactly a tensor
product `K_f tensor K_g`. A sum choice yields a scalar Hankel matrix;
a difference choice yields a scalar symmetric Toeplitz matrix. Split
the latter into `i>=k` and `i<k` parts (and similarly in y). These are
one-sided Toeplitz matrices. At most four sign sectors result from
each of the four choices.

In any fixed sector, `a=epsilon*i+delta*k` and
`b=epsilon'*j+delta'*l`, with coefficients in `{1,-1}`. Thus a mask
`u*a+v*b<=c`, with `u,v` each `1` or `-1`, becomes

\[
 r_{ij}+s_{kl}\le c,\quad
 r_{ij}=u\epsilon i+v\epsilon'j,\quad
 s_{kl}=u\delta k+v\delta'l.                       \tag{8}
\]

This is a one-dimensional block triangular truncation in integer
labels, after ordering rows and columns by those labels. It is not a
new arbitrary two-dimensional mask. Finally compress by `P_n` to the
total-degree coefficient space. Counting ten scalar kernels, four
product choices and at most four sign sectors gives 160 terms. Every
term is multiplied by the coefficient `1/4` from (4), with its own
sign. No `m`-dependent sum of new operator types is hidden in this
count. The total-degree range need not be imposed as a further mask:
on `I_n` all four product choices already satisfy `a+b<=2n`.

### 5. A genuine one-dimensional norm bound for the coupled masks

In (8), `|r_ij|,|s_kl|<=2n`, so their sum lies in `[-4n,4n]`.
Let `F` be the consecutive integers in that range that are at most
`c`, and put

\[
 d_F(t)=\sum_{v\in F}e^{-ivt},\quad
 U_r(t)=\operatorname{diag}(e^{ir_{ij}t}),\quad
 U_s(t)=\operatorname{diag}(e^{is_{kl}t}).
\]

Coefficientwise integration gives the exact identity

\[
 \mathcal T_c(A)=\frac1{2\pi}\int_{-\pi}^{\pi}
 d_F(t)U_r(t)A U_s(t)\,dt.                         \tag{9}
\]

Both diagonal factors are unitary. Consequently

\[
 \|\mathcal T_c(A)\|_2\le
 \left(\frac1{2\pi}\int_{-\pi}^{\pi}|d_F(t)|dt\right)
 \|A\|_2.                                         \tag{10}
\]

If `F` has `L>=1` integers, the geometric-series formula and
`sin(|t|/2)>=|t|/pi` give
`|d_F(t)|<=min(L,pi/|t|)` for `0<|t|<=pi`. Integration, splitting at
`pi/L`, bounds the parenthesis by `1+log L`. Here `L<=8n+1`, proving
(5); an empty `F` yields zero. The argument also covers `n=0,L=1`.
Thus, for example, each term has Euclidean coefficient-norm bound

\[
 (1+\log(8n+1))\|K_f\|_2\|K_g\|_2,
\]

and compression by `P_n` does not increase that norm. These bounds
establish finite-family controllability in a literal operator sense.
They deliberately make no sharp claim after changing to the
Lebesgue-orthonormal basis in (7). That remaining metric problem is
where the spectral targets must be proved or refuted. ∎

## Scope

The D1 structural kill criterion passes: a finite scalar alias group
alone would not suffice, but here its error kernel has bounded
separable rank on five explicit half-plane regions, and every pulled
back mask has the controlled one-dimensional representation (9).
This licenses D2/D3 investigation; it does not predetermine success.
The generic mask estimates do not control the continuous Lebesgue
mass normalization sharply enough to prove the requested spectral
bounds. No positivity, upper gap or endpoint asymptotic is asserted.

## Open items

- Independent audit of all five-region boundaries, tensor pullback,
  term count and the Fourier multiplier normalization.
- Useful bounds in the continuous Lebesgue mass metric; D2/D3 retain
  their separately OPEN spectral targets.
- Primary literature comparison and attribution. No exhaustive
  historical novelty clearance follows from local reconstruction.

## History

2026-11-01, Codex mathematical developer `/root/d1_aliasing`, requested
`gpt-6.1-sol` xhigh; resolved runtime model/effort metadata not exposed.
The original combined alias-and-architecture statement was written in
PD-T106 before the orchestrator requested the workflow split.
Its architecture statement is preserved verbatim above, and original
proof sections 3--5 are moved intact here. The split preserves both
PROVED development claims and keeps all spectral targets OPEN; audit
pending. The orchestrator owns crosswalk and registry updates.
