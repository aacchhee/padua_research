# PD-T?mz2d-codex-01 — Exact signed Padua aliases and rational Gram pencil

ID kind: PD-T.
Aliases: checkerboard complement alias; folded Padua moments; rational
signed Gram pencil. Historical combined aliases: masked tensor
Hankel/Toeplitz defect; signed-total-degree truncation (now split).
Split from: supporting exact representation for the OPEN signed-Padua
targets PD-T028; this is not a proved conjunct of those spectral targets.
Split into: the separately substantive masked-tensor operator architecture and
truncation norm are PD-T?mz2d-codex-04 in `mz2d-defect-structure.md`.
The orchestrator will record the crosswalk at PR preparation.

## Statement

Let `m>=1` and use exactly the even-checkerboard Padua nodes and signed
interpolatory `dx dy` rule in
[definitions.md](../../../topics/padua-mz-2d-20261101/definitions.md).
For every integer `r>=0` put

\[
 h_r=\int_{-1}^1 T_r(x)\,dx=
 \begin{cases}2/(1-r^2)&r\text{ even},\\0&r\text{ odd},\end{cases}
\]

and, for every integer `N>=1`, define the triangular fold

\[
 f_N(r)=\min\{\bar r,2N-\bar r\},\qquad
 \bar r=r\bmod 2N\in\{0,\ldots,2N-1\}.
\]

For **all** nonnegative integers `a,b`, not merely those of degree `2m`,
the exact signed-rule moment is

\[
 q_m(a,b):=Q_m(T_a(x)T_b(y))=
 \begin{cases}
 h_Ah_B,&A+B\le m,\\
 h_{m-A}h_{m+1-B},&A+B>m,
 \end{cases}
 \quad A=f_m(a),\quad B=f_{m+1}(b).                 \tag{1}
\]

In particular the algebraic degree of exactness for `dx dy` is exactly
`m`, for every `m>=1`. The first possible error cannot be delayed to
degree `2m`: the explicit degree-`m+1` identity is

\[
 Q_m(T_{m+1}(y))=2h_m\ne 2h_{m+1}
 =\int_{[-1,1]^2}T_{m+1}(y)\,dx\,dy.              \tag{2}
\]

For `0<=n<=m-1`, let `I_n={(i,j):i,j>=0,i+j<=n}` and use the
unnormalized product-Chebyshev basis `T_i(x)T_j(y)`. Its continuous mass
matrix `M` and signed quadrature mass matrix `R` are exactly

\[
 M_{(i,j),(k,l)}=
 \frac14(h_{i+k}+h_{|i-k|})(h_{j+l}+h_{|j-l|}),       \tag{3}
\]
\[
 R_{(i,j),(k,l)}=\frac14
 \sum_{u\in\{i+k,|i-k|\}}
 \sum_{v\in\{j+l,|j-l|\}}q_m(u,v).                 \tag{4}
\]

The sums in (4) are **multiset** sums, including repetitions when a
degree is zero. Thus they remain valid on the constant-mode rows.
Set `E_m(a,b)=q_m(a,b)-h_a h_b` and `D=R-M`. Replacing `q_m` by `E_m`
in (4) gives `D`. The generalized pencil `R-lambda M` has exactly the
eigenvalues of the Legendre Gram matrix `G_(m,n)`.

The separately substantive bounded masked-tensor architecture and its
one-dimensional truncation norm are split into
[PD-T?mz2d-codex-04](mz2d-defect-structure.md), which depends on these exact
aliases. They are not required for the proof of (1)--(4).

## Definitions

`T_r(cos t)=cos(rt)`. The node convention has x denominator `m`,
y denominator `m+1`, and parity `j+k` even. The signed weights integrate
all of `Pi_m` with respect to unnormalized `dx dy`. The positive
Chebyshev checkerboard weights used in a cardinal formula are denoted
`rho`, never identified with these signed weights.

The separate scalar Hankel/Toeplitz and signed-degree truncation
definitions are in PD-T?mz2d-codex-04.

## Assumptions

All polynomial identities and matrices are over the reals in exact
arithmetic. Formula (1) holds for every `m>=1,a,b>=0`; the Gram pencil
uses `0<=n<=m-1`. No weight positivity or unexplained `2m-1`
Lebesgue-exactness assumption is made. For `m=1,n=0`, the Gram statement
reduces directly to constant exactness.

## Status by part

Overall status: **PROVED** in development; independent mathematical
audit remains pending. The proof is analytic and does not rely on a
finite computation.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| All-degree aliases (1), including lower-degree errors (2) | PROVED | Nodal cosine identities and interpolatory exactness |
| Rational generalized mass/defect pencil (3)--(4) | PROVED | Product-to-sum and change of basis |

Candidate / claim disposition: retained variant/application of
classical checkerboard aliasing and the established cardinal mechanism;
no historical novelty claim.

## Depends on

The existence and unisolvence of this signed interpolatory rule may be
obtained from the elementary discrete-cosine cardinal proof in accepted
PD-T101, specifically its proof section 1. Formula (1) itself uses only
the node definition and degree-`m` exactness, so it also holds for any
real weights satisfying those exactness equations without invoking
uniqueness. No external theorem is inherited as a local proof.

PD-T013 is the one-dimensional local predecessor for product-to-sum
defects; PD-T021 is the marginal-compression predecessor. Neither
supplies the new complementary-mode formula in (1). The OPEN spectral
targets PD-T028 retain their own status.

## Checks

Rules read at `cf89b140530d5838bdb208a8c28f3e7aa676ace3`.
The orchestrator subsequently merged `main` at
`806cc7b4509fd93bae652f9545d32d95529f8281`; applicable rules were
reported unchanged. Accepted A1/PD-T101 was read from the merged file.

The developer read the prior Padua implementations
`tracks/mz-constants/code/reproduce.py`,
`topics/mz-constants/sources/padua_mz_inputs/code/padua_mz_large.py`, and
`mz_padua_cc_check.py`. Those reads are not executed reproductions.
Definitions and the D1 kill criterion were written before any campaign
numerical run was authorized. This developer has executed **no
numerical or exact-arithmetic experiment** for these claims.

The separate D0 and exact-engine workers are implementing independent
finite comparisons from these formulas; their actual executions and
receipts belong to their own records. An exact finite regression is
useful but is not necessary for this analytic theorem. Any later
computer-assisted spectral conclusion requires its own exact checker,
proved reduction, evidence, and different-agent rerun.

## Sources

Local primary dependency: accepted PD-T101,
`topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md`,
whose cardinal proof was read in full. Its source reading boundaries
remain explicit there. The campaign literature worker is separately
checking Bos et al., Caliari--De Marchi--Vianello, Sommariva--Vianello--Zanovello,
and Dencker--Erb. Reports from that worker are not treated as inspected
primary evidence in this proof. They are relevant to attribution and
to distinguishing positive Chebyshev cubature from signed Lebesgue
integration. No claim of exhaustive novelty clearance is made.

## Proof or evidence

### 1. Every mode has a low-degree nodal representative

At the x nodes `x_j=cos(j*pi/m)`, periodicity and reflection give

\[
 T_a(x_j)=T_A(x_j),\qquad A=f_m(a).
\]

The identical identity with period `2(m+1)` gives
`T_b(y_k)=T_B(y_k)`, where `B=f_(m+1)(b)`. Moreover,

\[
 T_{m-A}(x_j)=\cos(j\pi-Aj\pi/m)=(-1)^jT_A(x_j),
\]
\[
 T_{m+1-B}(y_k)=(-1)^kT_B(y_k).
\]

On the selected checkerboard their product signs cancel. Therefore

\[
 T_A(x_j)T_B(y_k)
 =T_{m-A}(x_j)T_{m+1-B}(y_k).                      \tag{6}
\]

The two total degrees are `A+B` and `2m+1-A-B`. Exactly one is at most
`m`, since their sum is odd. Its mode is in `Pi_m`, where `Q_m` is
exact. Integration of that representative gives (1), for all degrees.
This proof includes fold endpoints, zero modes, and `m=1`.

Take `a=0,b=m+1`. The folded point `(0,m+1)` has the complementary
representative `(m,0)`. Thus (2) follows. Exactly one of the consecutive
integers `m,m+1` is odd, with zero moment; the other is a positive even
integer with nonzero moment. The moments differ for every `m>=1`.
Degree-`m` exactness is given, and degree `m+1` is inexact, proving
the exact algebraic degree. When `m>=3`, this explicit error already
lies in the endpoint Gram moment range `m+1<=2m-2`.

### 2. The exact generalized defect pencil

Twice applying

\[
 T_iT_k=\tfrac12(T_{i+k}+T_{|i-k|})
\]

gives (3)--(4). The largest moment degree that occurs is
`(i+j)+(k+l)<=2n<=2m-2`, as required. `M` is positive definite because
it is the continuous squared norm of a linearly independent polynomial
basis. Let `C` be the invertible matrix mapping coefficients in an
orthonormal Legendre-product basis to these Chebyshev coefficients.
Then

\[
 C^\mathsf TMC=I,\qquad C^\mathsf TRC=G_{m,n},
 \qquad G_{m,n}-I=C^\mathsf TDC.                   \tag{7}
\]

Congruence by `C` sends `R-lambda M` to `G-lambda I`; equivalently their
determinants differ by the nonzero factor `det(C)^2`. This proves the
eigenvalue assertion without requiring signed-weight positivity.
All entries in (3)--(4) are rational numbers, notwithstanding the
generally irrational nodes or orthonormal Legendre scaling.

## Scope

The all-degree nodal representative and rational Gram pencil are proved.
The D1 structural kill criterion is decided separately by
PD-T?mz2d-codex-04, which supplies the bounded separable architecture
and its norm control. The alias formula alone does not pass that gate.

In particular the proof does not transplant the one-dimensional
entrywise-nonnegative defect or Z-matrix signs. Complementation changes
total parity, since the two degrees add to `2m+1`; mixed moment errors
and signed Gram couplings require fresh analysis. No independent
x/y-parity block reduction is asserted.

## Open items

- Independent analytic reconstruction/audit of (1)--(4). The separate
  structure record carries its own architecture/norm audit obligations.
- Spectral control of `C^T D C`, including its signs, with a useful
  upper gap below two and positive lower bound. Those are separate
  D2/D3 targets, currently OPEN.
- Primary-source attribution comparison; the architecture is treated
  as a documented variant until that comparison is complete.
- Independent finite regressions are separate verification evidence,
  not replacements for the analytic proof.

## History

2026-11-01, Codex mathematical developer `/root/d1_aliasing`, requested
`gpt-6.1-sol` xhigh (resolved runtime model/effort metadata not exposed).
Owned only the campaign definitions, D1 direction, D1 candidate record
and this theory file. No Git mutation or shared-registry edit.
Definitions and pre-run kill criterion were written first; exact
formula and structural PASS were sent to the orchestrator, D0,
exact-engine, D2 and D3 workers before their dependent proof work.

2026-11-01, orchestrator requested workflow split: the original combined
statement additionally asserted the following separately substantive
architecture, now preserved verbatim in PD-T?mz2d-codex-04:

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

The alias theorem retains (1)--(4) and exact degree of exactness. The
architecture proof sections 3--5 were moved intact to their own theory
record, with an explicit dependency on this alias theorem. This is a
split of two proved claims, not a downgrade or narrowing of an unresolved
spectral target. Both remain PROVED in development, audit pending.
