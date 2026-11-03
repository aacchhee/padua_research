# PD-T?lebesgue-followups-codex-t4-02 — A one-dimensional expansion with quadratic remainder

ID kind: PD-T.
Aliases: T4 Chebyshev sum; local proof of the classical endpoint constant.
Split from: supporting one-dimensional obligation for PD-T098.
Split into: none.

## Statement

For every integer n≥1, with L_n as in PD-T159, set

\[
 A_n={2\over\pi}\left(\log n+\gamma+\log{8\over\pi}\right).
\]

Then

\[
 |L_n-A_n|\le {1\over4n^2}.                                  \tag{1}
\]

## Definitions

γ=lim_m(H_m−log m); H_m=Σ_{r=1}^m1/r. All other definitions are those of t4-01 and PD-T159.

## Assumptions

Exact real arithmetic, integer n≥1. No parity restriction.

## Status by part

Overall status: **PROVED**, written analytic proof; supplementary independent reconstruction accepted; required Claude audit pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| All-n bound (1) | PROVED | Endpoint pairing, harmonic tail and composite midpoint estimates below |

## Depends on

Definition of L_n in PD-T159; the elementary cotangent partial fraction with its local Fourier proof in t4-01, §4.

## Checks

Analytic result. Supplementary finite comparisons in `../code/t4_constant.py` have MEASURED status and are not proof inputs.

## Sources

No external classical expansion is cited. The needed estimate is proved locally; literature baseline/limitations are in `../gate-t4.md`.

## Proof or evidence

Let x_r=(2r−1)π/(4n), 1≤r≤n. Pair r with n+1−r and use cot x+tan x=2csc(2x). When n is odd the central x=π/4 contributes one, exactly the half-weight endpoint of the cosecant sum. Thus, for either parity,

\[
 L_n={1\over n}\sum_{r=1}^n\cot x_r.                         \tag{2}
\]

Put v(x)=cot x−1/x and v(0)=0, on [0,A], A=π/2. Integrating log sin x−log x gives

\[
 \int_0^A v(x)dx=\log(2/\pi).                               \tag{3}
\]

The cotangent partial fraction gives, by termwise differentiation on this interval,

\[
 |v''(x)|=4x\sum_{m\ge1}{3\pi^2m^2+x^2\over(\pi^2m^2-x^2)^3}
 \le {416\over27\pi^3}\sum_{m\ge1}m^{-4}<1.                 \tag{4}
\]

For the final elementary comparison use π>3 and Σm⁻⁴≤1+∫₁∞x⁻⁴dx=4/3, giving 1664/2187<1. The midpoint-rule error on an interval of length h is ≤h³ sup|v''|/24 (integrate the second-order Taylor remainder about the midpoint). Applying it to n cells of length h=A/n, and noting 1/n=h/A, yields

\[
 \left|{1\over n}\sum_r v(x_r)-{2\over\pi}\log(2/\pi)\right|
 \le{\pi^2\over96n^2}<{1\over8n^2}.                         \tag{5}
\]

For completeness obtain a harmonic estimate without an imported Euler–Maclaurin expansion. On [r,r+1], the trapezoid error for f(x)=1/x is

\[
 0\le{f(r)+f(r+1)\over2}-\int_r^{r+1}f(x)dx
 ={1\over2}\int_r^{r+1}(x-r)(r+1-x)f''(x)dx
 \le{1\over8}\int_r^{r+1}f''(x)dx.
\]

Summing r=m,…,∞ and using H_m−log m−γ's telescoping representation proves

\[
 H_m=\log m+\gamma+{1\over2m}+r_m,
 \qquad -{1\over8m^2}\le r_m\le0.                           \tag{6}
\]

The singular part of (2) is exactly

\[
 {1\over n}\sum_r{1\over x_r}={2\over\pi}(2H_{2n}-H_n).
\]

The 1/m terms cancel in 2H_{2n}−H_n, and (6) gives

\[
 \left|2H_{2n}-H_n-(\log n+\gamma+2\log2)\right|
 \le{3\over16n^2}.
\]

Its contribution after multiplication by 2/π is less than 1/(8n²), since π>3. Add (5), and combine the logarithms 2log2+log(2/π)=log(8/π), to obtain (1).

## Scope

Both parities, with an explicit quadratic error. This bound does not identify L_n's n⁻² coefficient or imply the corner's -1/N term.

## Open items

Required Claude audit; supplementary reconstruction is complete. Optional sharper Euler–Maclaurin coefficients are outside this result.

## History

2026-11-03, Codex gpt-6.1-sol xhigh, rules `3f5196cf3639407c25b021fa30f70cc1d3ae113a`. Local proof written to avoid citing an unread classical fulltext.
