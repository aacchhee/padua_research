# PD-N053 — direct rectangular Fejér reconstruction aliases

Provisional alias: `PD-N?mz2d-codex-40`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-N. Aliases: tensor M3 checkerboard filter failure; complementary
high-high spurious mode. Split from: none. Split into: none.

## Statement

For every integer `m>=3` and `2<=n<m`, the normalized checkerboard
convolution with the product of the scalar M3 plateau kernels of cutoffs
`m-1` and `m` does **not** reproduce all polynomials of total degree at
most n. For the single input `q(t,s)=cos(t)cos(s)`, its output has Fourier
coefficient

\[
 \widehat{\mathcal Rq}(1-m,-m)
 =\frac1{4(m-n)(m+1-n)}>0,                         \tag{1}
\]

whereas the input coefficient there is zero.

## Definitions and assumptions

For `N>n>=0`, let `F_N` be the Fejér kernel and define

\[
 K_{N,n}(t)=\frac{NF_N(t)-nF_n(t)}{N-n},\quad
 \kappa_{N,n}(r)=
 \frac{(N-|r|)_+-(n-|r|)_+}{N-n}.                \tag{2}
\]

The convention `nF_n=0` holds at n=0. Thus `K` has Fourier coefficient
`kappa`, degree `N-1`, and multiplier one for `|r|<=n`.
Use the periodic even checkerboard

\[
 \Gamma_m=\{(j\pi/m,k\pi/(m+1)):
 0\le j<2m,\ 0\le k<2(m+1),\ j+k\equiv0\pmod2\}.
\]

Its size is `2m(m+1)`. Samples of `p(cos t,cos s)` on it are determined
by the campaign's physical Padua samples. For this statement the exact
operator being rejected is

\[
 \mathcal Rq(t,s)=\frac1{|\Gamma_m|}
 \sum_{(t_j,s_k)\in\Gamma_m}
 K_{m,n}(t-t_j)K_{m+1,n}(s-s_k)q(t_j,s_k).       \tag{3}
\]

No Lebesgue nodal weight is used in (3); this tests the earlier exact
reconstruction step before any norm estimate or signed conversion.

## Status by part

Overall status: **PROVED** in development; independent mathematical audit
pending. Candidate IDEA-224: **REJECTED: failed** for this precise
operator and parameter range. The signed Padua fixed-ratio target remains
OPEN. This is not a negative statement about other filters.

## Negative-result scope

Attempted mechanism: direct tensor transfer of the one-dimensional M3
filtered reconstruction to the checkerboard average, exactly (3).
Parameter range: every integer `m>=3`, `2<=n<m`. No conclusion is asserted
for n=0,1, for a full rectangular grid, or for diamond-supported filters.

## Depends on

Only the finite geometric-series identity, the node convention and the
kernel definition (2). PD-T023/IDEA-074 is the inspected local predecessor;
no part of its positive-weight lower bound is assumed here.

## Proof

Let `A_m(r,s)` be the average of `exp(i(rt_j+ss_k))` over `Gamma_m`.
On the full periodic rectangular grid, the checkerboard indicator is
`(1+(-1)^(j+k))/2`, and its density is one half. Summing two geometric
series therefore gives

\[
 A_m(r,s)=1_{2m\mid r,\ 2(m+1)\mid s}
 +1_{r\equiv m\ (2m),\ s\equiv m+1\ (2m+2)}.   \tag{4}
\]

The two indicator cases are disjoint. Expanding (3) in finite Fourier
sums gives, at output frequency v,

\[
 \widehat{\mathcal Rq}(v)
 =\kappa_{m,n}(v_1)\kappa_{m+1,n}(v_2)
   \sum_u\widehat q(u)A_m(u_1-v_1,u_2-v_2).     \tag{5}
\]

The four input frequencies of q are `(+-1,+-1)`, each of coefficient
`1/4`. Set `v=(1-m,-m)`. The first alias case in (4) is impossible:
`u_1-v_1` is m or m-2, neither a multiple of 2m for m>=3.
The second case holds exactly when `u=(1,1)`: its coordinate differences
are then `(m,m+1)`; the alternative first difference m-2 and second
difference m-1 fail the respective congruences. Thus the sum in (5) is
exactly `1/4`.

At `|v_1|=m-1` and `|v_2|=m`, the respective coefficients in (2) are
`1/(m-n)` and `1/(m+1-n)`. This proves (1). The frequency v is absent
from q because `m>=3`. Also q corresponds to `p(x,y)=xy`, of total degree
two, so it belongs to the stated input space for every n in the claim. ∎

## Checks, sources and scope

The test and kill criterion are recorded in
`topics/padua-mz-2d-20261101/ideas-d4.md`. This is an analytic coefficient
proof; this worker executed no numerical or exact-arithmetic program for
it. D1's complementary alias explains the obstruction, but the character
sum is rederived above. The direct predecessor is classical product
filtering and local PD-T023. No historical novelty claim is made.

The output contains an inadmissible high-high component even for a
low-degree input; a subsequent total-degree projection could remove it,
but would define a different operator requiring its own localization and
norm analysis. The corrected diamond filter is treated separately in
PD-T115.

## Open items and history

Independent audit of normalization, endpoint coefficients and parameter
scope. Original D4 target stays OPEN.

2026-11-01, Codex `/root/d4_ratio`, requested gpt-6.1-sol xhigh, rules read
at supplied main `806cc7b4509fd93bae652f9545d32d95529f8281`; no Git changes.
