# PD-T296 — explicit positive reference MZ from a smooth diamond filter

Development alias: `PD-T?mz2d-frontier-codex-f3-01`. Final ID assigned during audited preparation; [mapping](../preparation/final-id-map.json).

ID kind: PD-T.
Aliases: squared-Fejér diamond plateau; quartic diagonal localization;
lifted-checkerboard product-sine sampling equivalence.
Split from: supporting weighted-localization obligation of PD-T116;
this is not a proved parameter case of that signed target.
Split into: none.

## Statement

For integers `m>=1,0<=n<m`, let

\[
 \Gamma_m=\{(j\pi/m,k\pi/(m+1)):0\le j<2m,\ 0\le k<2(m+1),\ j+k\text{ even}\},
 \qquad N_m=2m(m+1),
\]
\[
 \nu_m(t,s)=(|\sin t|+m^{-1})(|\sin s|+m^{-1}),
 \quad S_m(p^2)=\frac{\pi^2}{N_m}
   \sum_{z\in\Gamma_m}\nu_m(z)\,p(\cos z_1,\cos z_2)^2.
\]

The sum uses the reflected copies of the physical even-checkerboard
Padua values. It is a **positive reference rule**, not the signed
interpolatory Lebesgue rule `Q_m`. Define

\[
 A=512(1+\pi)^4,\qquad B=1+2/\pi,\qquad C_2=2+\pi/2,
 \qquad C(\epsilon)=A^4B^4\epsilon^{-16}.
\]

Then every real `p in Pi_n`, with `epsilon=1-n/m`, satisfies

\[
 C(\epsilon)^{-1}\|p\|_{L^2(dx\,dy)}^2
 \le S_m(p^2)
 \le C_2^2 C(\epsilon)\|p\|_{L^2(dx\,dy)}^2.       \tag{1}
\]

In particular the same inequalities hold with `C(1-theta)` for every
fixed `0<=theta<1` and every integer `n<=theta*m`. All constants are
explicit and intentionally loose. No inequality for `Q_m` follows
without a further signed comparison.

An explicit exactly reconstructing diamond kernel is supplied below;
it has fourth-order localization in each diagonal angle before the
weight ratio, and third-order summable envelopes after it.

## Definitions

`Pi_n` is real bivariate total degree at most n. Ordinary circle distance
is `d(a,b) in [0,pi]`. Write `dmu=dt ds/(4pi^2)` for normalized torus
measure and `dmu_Gamma` for normalized counting measure on Gamma.
For `p in Pi_n`, set `q(t,s)=p(cos t,cos s)`; its Fourier support is
the integer diamond `|a|+|b|<=n` and it is even in each angle.

Let

\[
 F_L(t)=\frac1L\left|\sum_{h=0}^{L-1}e^{iht}\right|^2,
 \quad D_M(t)=\sum_{r=-M}^M e^{irt},
\]
\[
 L=\lceil(m-n)/4\rceil,\quad M=n+2L-2,
 \quad K(t)=D_M(t)\left(\frac{F_L(t)}{L}\right)^2,
\]
\[
 H(t,s)=\frac12\{K((t+s)/2)K((t-s)/2)
  +K((t+s)/2+\pi)K((t-s)/2+\pi)\}.             \tag{2}
\]

## Assumptions

Exact real arithmetic, integer `m>=1,0<=n<m`, fixed even checkerboard
with adjacent denominators m,m+1, unnormalized physical Lebesgue
measure dxdy of mass four. No signed-weight positivity, sampled-space
spectral hypothesis, computer check or external MZ theorem is assumed.

## Status by part

Overall status: **PROVED** in development; supplementary independent
reconstruction complete, Claude mathematical audit-01 accepted.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Positive-reference equivalence (1), including explicit constants | PROVED | Analytic proof below |
| Exactly reconstructing smooth diamond kernel with weighted localization | PROVED | Constructive steps of the same supporting theorem |

Candidate disposition: retained, `IDEA-391`.
This is a variant of classical smoothing and PD-T115, with explicit
weighted localization previously unproved there. No historical novelty
claim. This theorem initially left signed PD-T116 OPEN and is not a
resolved parameter part of that target. Subsequent separate carrier
countersequences refute PD-T116’s positive assertion above half-exactness;
see `f3-fixed-ratio-threshold.md`. The positive reference theorem here
remains valid and is not used as a signed comparison.

## Depends on

PD-T115's checkerboard character geometry and parity projection, whose
elementary proof is repeated here for the changed kernel. The scalar
Fejér finite sum is proved by pair counting. The elementary Legendre
point-evaluation bound used for regularization is recalled below.
No published source is inherited as a proof. PD-N045/048/053 delimit
excluded transfer steps; they are context, not assumptions in (1).

[Claude audit-01](../audit-01.md) accepted the mathematics at its stated scope; [response-01](../response-01.md) addresses the editorial findings. Supplementary reconstruction is recorded in [independent-checks-math.md](../independent-checks-math.md).

## Checks

The proof checks the smallest gap `m-n=1`, the edge `m=1,n=0`, the
Fourier plateau and cutoff, two-sheet lift, square packing and all
normalizations. No mathematical program or numerical regression was
executed by this developer for this analytic result. Source/rules SHA
`83cf6f1ee244f2e72057332a7ec04ee74db1f0de`. Parent G0 PASS was received
before any computation was contemplated.

Supplementary verification subsequently completed by the distinct
independent-math worker: no gap found in analytic reconstruction;
its separately executed exact Fraction checker passed all 300 degree
pairs at m=1..24 (379900 coefficient tests), 205311 alias-pair tests at
m=1..10, and 92064 pairwise lift-separation tests at m=1..8. Lift counts
were checked through m=24. The frozen checker is
`../code/independent_f3_check.py`; receipt
`../evidence/independent-f3-check.json` records the supplementary worker’s
then-current metadata version at SHA-256
`a55b401d450fe3e0510eb605051fd7ea99ee59743a1a3fc46ee14de992773aaa`;
that version was not committed, so it is not a Git-replayable proof identity.
The auditor reran the same checker on the committed audited version
`dfbc44a3ec0589f794457fe14c3212b730d62a26c66bffa3e1d4a7295e62550d`,
with PASS (300 degree pairs, 379900 frequency tests, 205311 alias tests,
92064 lift-separation tests), as recorded in [audit-01](../audit-01.md)
and [the diamond audit](../audit-01-support/subagent-f3/audit-diamond.md).
This response cites that actual auditor execution and does not rerun it.
These finite regressions supplement the accepted analytic proof; no
all-m computer proof or signed-energy transfer is inferred.

## Sources

Local fully read predecessors PD-T023/115 and IDEA-074/226. The complete
idea gate and literature-index scope are in `../ideas-f3.md`.
Classical smoothing and Schur methods are acknowledged as ancestry;
no new primary source was opened, no priority claim is made, and
literature attribution coverage remains limited to the documented screen.

## Proof

### 1. A scalar plateau with quartic decay

Put `g=m-n>=1`. The choice `L=ceil(g/4)` gives

\[
 4(L-1)\le g-1,\qquad L\ge g/4=\epsilon m/4.       \tag{3}
\]

The Fejér coefficients are `1-|r|/L` on `|r|<L`, and zero otherwise:
expand the squared finite geometric sum and count pairs with a given
difference. All coefficients of `F_L^2` are nonnegative, its degree is
`b=2L-2`, and their sum is `F_L(0)^2=L^2`. Therefore

\[
 \widehat K(k)=\frac1{L^2}\sum_{r=-M}^M\widehat{F_L^2}(k-r).
\]

When `|k|<=M-b=n`, the interval in this sum contains the entire support
of `F_L^2`, so the coefficient is exactly one. It vanishes when
`|k|>M+b=n+4L-4<=m-1`. This proves the plateau and cutoff, including
L=1, where `F_1=1` and `K=D_n`.

For `d=d(t,0)>0`, the geometric-sum formula and
`sin(d/2)>=d/pi` give

\[
 0\le F_L(t)/L\le\min\{1,\pi^2/(Ld)^2\}.
\]

Also `|D_M|<=2M+1<=2m`, by (3). The elementary inequality
`min(1,pi^4/x^4)<=(1+pi)^4/(1+x)^4` follows by splitting x at pi.
Since `1+Ld >= (epsilon/4)(1+md)`, we obtain

\[
 |K(t)|\le A\epsilon^{-4}m(1+m d(t,0))^{-4}.       \tag{4}
\]

It holds at zero by continuity. This estimate is deliberately generous
when L=1, so no special small-gap exception is needed.

### 2. Diamond support and both reconstruction identities

Put `u=(t+s)/2,v=(t-s)/2`. In (2), the simultaneous shift by pi removes
opposite-parity scalar frequency pairs. The surviving original frequency
is `(a,b)=((r+k)/2,(r-k)/2)` and has coefficient
`Khat(a+b) Khat(a-b)`. Thus H is 2pi-periodic in each original variable,
its coefficient is one on `|a|+|b|<=n`, and its support is contained in
`|a|+|b|<=m-1`, since
`max(|a+b|,|a-b|)=|a|+|b|`.

The normalized checkerboard character average is one on

\[
 \Lambda_m=(2m\mathbb Z\times2(m+1)\mathbb Z)
 \cup((m,m+1)+(2m\mathbb Z\times2(m+1)\mathbb Z)),
\]

and zero elsewhere. Insert `(1+(-1)^(j+k))/2` into the full-grid
geometric sums to check this. Every nonzero alias has l1 length at
least 2m. Input and output support differences have length at most
`n+m-1<=2m-2`; only the zero alias survives. Consequently

\[
 q(t)=\int H(t-z)q(z)\,d\mu_\Gamma(z),\qquad
 q(t)=\int H(t-z)q(z)\,d\mu(z).                    \tag{5}
\]

The second identity is ordinary Fourier reproduction. Both hold for
every diamond-supported trigonometric polynomial, hence for the q in
the theorem. At `m=1,n=0`, K=H=1 and both statements are constant
reproduction. Reflection extension to Gamma preserves checkerboard
parity and uses only physical Padua values.

### 3. The weight ratio in the actual diagonal geometry

For either of the two branches in (2), choose representatives of its
diagonal differences with absolute values `d_u,d_v` in `[0,pi]`.
Modulo 2pi, the original-coordinate differences are their sum and
difference, so their circle distances are at most `d_u+d_v`.

Each `|sin t|+1/m` is one-Lipschitz and at least 1/m. Therefore

\[
 \sqrt{\nu_m(t)/\nu_m(z)}
 \le1+m(d_u+d_v)\le(1+md_u)(1+md_v).              \tag{6}
\]

The same estimate holds with t and z interchanged. Put
`J(x)=(1+m d(x,0))^-3` and, for a difference `(t,s)`,

\[
 E(t,s)=\tfrac12\{J(u)J(v)+J(u+\pi)J(v+\pi)\}.
\]

Combining (4) and (6) gives the symmetric envelope

\[
 |H(t-z)|\sqrt{\nu_m(t)/\nu_m(z)}
 \le A^2\epsilon^{-8}m^2 E(t-z).                 \tag{7}
\]

The pre-ratio decay exponent four survives the one-power loss in each
diagonal variable, leaving exponent three, which is greater than one
and therefore summable. This is a bound in the actual diagonal geometry,
not a coordinatewise assumption transferred from a rectangle.

### 4. Continuous and discrete envelope bounds

The map `(u,v)->(t,s)=(u+v,u-v)` is a degree-two homomorphism of the
two-dimensional torus. It sends normalized Haar measure to normalized
Haar measure. Since
`int_0^(2pi) J(x) dx <= 2 int_0^infty(1+mx)^-3 dx =1/m`,

\[
 \sup_t\int E(t-z)\,d\mu(z)\le\frac1{4\pi^2m^2}. \tag{8}
\]

For the discrete bound let `Gamma'_m` be the full inverse image of
Gamma under that degree-two map. It contains exactly `2N_m` points,
two lifts per original point. In a half-open square of side

\[
 a=\frac\pi{2(m+1)},
\]

there is at most one lift. Indeed two lifts in such a square have
original-coordinate differences of absolute value less than `2a`,
strictly smaller than either grid spacing `pi/m,pi/(m+1)`. Their
original nodes must coincide. Two lifts of the same node differ by
`(pi,pi)` on the torus and cannot be in that square. This argument is
also valid for squares crossing a fundamental-domain boundary by using
their local representatives.

Around any center, use distance shells k defined by
`d in [ka,(k+1)a)` for k=0,...,2(m+1)-1; each is contained in the union
of two half-open intervals of length a. Put the antipode in its own
degenerate shell k=2(m+1), already included in the infinite sum below.
A pair of shells k,l is contained in at most four such squares (or
degenerate subsets of them) and contains at most four lifts. Since
`ma>=pi/4`, the total envelope sum over all lifts is at most

\[
 4\left(\sum_{k\ge0}(1+k\pi/4)^{-3}\right)^2
 \le4(1+2/\pi)^2=4B^2.                           \tag{9}
\]

The series bound uses its first term plus the integral of the decreasing
function, whose integral is 2/pi. The two terms in E correspond exactly
to the two lifts. Hence

\[
 \sup_t\int E(t-z)\,d\mu_\Gamma(z)
 \le\frac{2B^2}{N_m}.                            \tag{10}
\]

As `m^2/N_m=m/[2(m+1)]<=1/2`, (7)–(10) show that integration of the
weighted kernel against either normalized continuous measure or
normalized checkerboard measure is at most

\[
 M_\epsilon=A^2B^2\epsilon^{-8}.                 \tag{11}
\]

This holds uniformly in the remaining variable, in either source/target
orientation; the inverse weight ratio also satisfies (6).

### 5. Schur in both directions

For completeness, if a kernel has absolute row and column integrals
at most M between two positive measure spaces, Cauchy–Schwarz gives

`|Tf(x)|^2 <= (int |L(x,y)|dy)(int |L(x,y)||f(y)|^2dy)`.

Integrate in x and use the column bound to get operator norm at most M.
Apply this to the weighted kernel in (7), first to discrete-to-continuous
reconstruction in (5), then to continuous-to-discrete reconstruction.
For `V=int nu_m|q|^2 dmu` and `D=int nu_m|q|^2 dmu_Gamma`,

\[
 V\le M_\epsilon^2D,\qquad D\le M_\epsilon^2V.    \tag{12}
\]

These are estimates for positive measures only; signed weights are not
inserted into Cauchy–Schwarz anywhere.

### 6. Compare the regularized continuous measure with dxdy

For a univariate polynomial f of degree at most r, its Legendre
expansion and Cauchy–Schwarz give

\[
 \|f\|_\infty^2\le\frac{(r+1)^2}{2}\int_{-1}^1 f^2.
\]

We use the standard Legendre bound `|P_k(x)|<=1` on `[-1,1]`.
The classical Laplace identity, for `x=cos t`, is
`P_k(cos t)=pi^-1 int_0^pi(cos t+i sin t cos phi)^k dphi`;
its integrand has modulus at most one. We invoke this classical identity
as a standard fact, rather than treating the earlier generating-series
sketch as a separate derivation. Summing `(2k+1)/2` gives the displayed
evaluation bound.

Put `delta=1/(r+1)<=1`. The two endpoint angular intervals of length
delta contribute at most `(r+1) int f^2` to
`int_0^pi f(cos t)^2dt`. On the middle interval,
`sin t>=2delta/pi`, so its contribution is at most
`pi(r+1)/2 int f^2`. Therefore

\[
 \int_0^\pi f(\cos t)^2dt
 \le(1+\pi/2)(r+1)\int_0^\pi\sin t\,f(\cos t)^2dt.
\]

For r<=n<=m-1, adding `m^-1 int f^2` to the sine-weighted angular
integral thus increases it by a factor at most `C_2=2+pi/2`.
Apply this inequality one coordinate at a time (each slice has degree
at most n), and use separate angular evenness. The change of variables
from each half-circle to `[-1,1]` gives

\[
 \|p\|_2^2\le\pi^2 V\le C_2^2\|p\|_2^2.        \tag{13}
\]

Finally `S_m=pi^2D`. Combining (12) and (13) proves (1), because
`M_epsilon^2=C(epsilon)`. Monotonicity in epsilon gives the fixed-theta
version. This completes the analytic proof. ∎

## Scope

The theorem establishes compatible weighted localization for an exactly
reconstructing diamond filter and a positive coercive sampled form.
It supplies no direct lower or upper bound for the signed Q_m. Its
constants are not intended for sharp spectra or endpoint asymptotics.
As theta tends to one the explicit bound diverges; no uniform endpoint
norm equivalence is claimed.

## Open items

- Claude audit-01 accepted. Supplementary reconstruction of the lift,
  packing constant, weight ratio and normalized Schur bounds found
  no gap; its finite exact regression has the scope stated above.
- The initial intended signed comparison is superseded by the separate
  negative classification in `f3-fixed-ratio-threshold.md`. There is
  no uniform signed eta(theta)<1 for any theta>1/2. The
  positive-reference statement and proof here are unchanged.
- Primary-source attribution and possible historical overlap; no
  exhaustive novelty clearance is supplied by the local gate.

## History

2026-11-05, Codex F3 developer, requested gpt-6.1-sol xhigh, rules/input
`83cf6f1ee244f2e72057332a7ec04ee74db1f0de`. Constructed after the
complete documented novelty gate. No Git, numerical program, claimed
independent verification or final-ID allocation. The original signed
target is retained verbatim in its own OPEN continuation record.

2026-11-05: mechanical final-ID registration after accepted Claude audit-01 and response-01. The earlier audited source/receipt identities are historical; proof content changes only by ID substitution.
