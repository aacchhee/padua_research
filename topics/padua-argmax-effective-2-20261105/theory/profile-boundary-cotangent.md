# PD-T365 (PD-T?argmax-effective-2-codex-03) — Exact boundary primitive and uniform profile

ID kind: PD-T.
Aliases: diamond-edge CRT; shifted cotangent boundary profile;
midpoint primitive equals L at degree n(n+1).
Split from: H2's full-diamond uniform-profile obligation, which remains OPEN.
Split into: the rejected leading-factor-only profile has its own negative record.

## Statement

Let n>=2, m=n+1, N=nm. For 0<t<1 define the absolutely convergent series

\[
C(t)=2\gamma+\frac1t+\frac1{1-t}
 +\sum_{k=1}^{\infty}\left(\frac1{k+t}+\frac1{k+1-t}-\frac2k\right)
\]

and the explicit profile

\[
P_N(t)=\frac{\sin(\pi t)}\pi
       \left[2\log\frac{2N}\pi+C(t)\right].                 \tag{1}
\]

Set P_N(0)=P_N(1)=1, the continuous limiting values. Then for every
choice of signs and every t in [0,1],

\[
\left|S_n(\pm\pi t,\pm\pi(1-t))-P_N(t)\right|
 \le \frac7{12N^2}.                                      \tag{2}
\]

For 0<t<1 the exact expression is

\[
S_n(\pi t,\pi(1-t))
=\frac{\sin(\pi t)}{2N}
 \sum_{q=0}^{2N-1}\left|\cot\frac{\pi(q+t)}{2N}\right|.    \tag{3}
\]

At either endpoint this equals 1 by continuity, not by substituting
zero times an infinite cotangent. At every diamond midpoint,

\[
S_n(\pm\pi/2,\pm\pi/2)=L_N,
\quad
\left|L_N-\frac2\pi\left(\log N+\gamma+\log\frac8\pi\right)\right|
\le\frac1{4N^2}.                                        \tag{4}
\]

## Definitions

Use the corrected finite polynomial kernel
\(G_n(u,v)=D_n(u,v)-\cos(nu)\), with D_n as in PD-T185, and

\[
\Gamma^- =\{(j,r):0\le j<2n,\ 0\le r<2m,\ j+r\text{ odd}\},
\quad
S_n(\alpha,\beta)=\frac1{2N}\sum_{\Gamma^-}
\left|G_n\left(\frac{j\pi+\alpha}n,
                    \frac{r\pi+\beta}m\right)\right|.
\]

L_M is PD-T159's one-dimensional odd-cosecant sum, in the equivalent
cotangent form of PD-T270 equation (2),
\(L_M=M^{-1}\sum_{k=0}^{M-1}\cot(\pi(k+1/2)/(2M))\).
It is unrelated to the cusp-slope L_n of PD-T220. N=n(n+1) here is
the mesh product, not the node-count notation used in PD-T101.
All logarithms are natural; gamma is Euler's constant.

## Assumptions

Exact real arithmetic, all integer n>=2, and the stated corrected mode,
odd periodic board and normalization. No global argmax or fitted profile.

## Status by part

Overall status: **PROVED** by the analytic proof below. Dated review note,
2026-11-05: Claude [audit-01](../audit-01.md) accepted the original scope;
the record response check is pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Boundary identity, all endpoints and parities | PROVED | Finite kernel cancellation and explicit two-element CRT fibers |
| Uniform absolute remainder (2) | PROVED | Paired quadrature and convergent harmonic tail |
| Midpoint evaluation and remainder (4) | PROVED | Exact identity and inherited PD-T270 |

Candidate disposition: retained boundary result. H2 on the entire diamond
is OPEN; (2) is a boundary theorem only.

## Depends on

PD-T185's finite corrected kernel; PD-T216's exact numerator identity;
PD-T159's definition of the odd-cosecant L_M and PD-T270 equation (2)
for its equivalent cotangent form;
PD-T270's elementary bound |v''|<1 on [0,pi/2] for
v(x)=cot(x)-1/x, v(0)=0, and its all-integer L_M estimate (4).
The finite CRT and the new paired remainder are proved here.

## Checks

No computation, fit, numeric integration or computer-assisted proof is
a premise. Candidate defined before any A3 fitting run; no such run has
occurred. Independent checker to receive this exact file hash from root.

## Sources

No external source theorem is transferred. Gate and reading limitations:
`../novelty-gate-H2-H3.md`. Nearest repository predecessors are
IDEA-329/PD-T226 and IDEA-358/PD-T270, on different parameter loci.

## Proof or evidence

### 1. Boundary cancellation and all removable collisions

Write u=(j*pi+alpha)/n and v=(r*pi+beta)/m. The exact numerator from
PD-T216, at unequal cosines, is

\[
(-1)^jG_n(u,v)
=\frac{(\cos\alpha+\cos\beta)(1+\cos v)
      -\sin\alpha\sin u+\sin\beta\sin v}{\cos u-\cos v}.
\]

On alpha=pi*t, beta=pi*(1-t), cos(alpha)+cos(beta)=0 and
sin(alpha)=sin(beta)=sin(pi*t). Since

\[
\frac{\sin v-\sin u}{\cos u-\cos v}
=\cot\frac{u+v}2,
\]

we obtain (-1)^j G_n=sin(pi*t) cot((u+v)/2). For 0<t<1,

\[
\frac{u+v}2=\frac{\pi(mj+nr+n+t)}{2N}                    \tag{5}
\]

is never a cotangent pole. At cos(u)=cos(v), the original polynomial
and the simplified expression agree by continuity in t: the unequal-
cosine points are dense, since u-v has nonzero t derivative
pi*(1/n+1/m), while u+v has nonzero t derivative pi/N.
Thus no collision term is omitted or assigned a formal zero.

### 2. Odd-board CRT and endpoints

The homomorphism (j,r) -> mj+nr mod 2N from
Z/(2n) times Z/(2m) onto Z/(2N) is surjective, because gcd(n,m)=1.
Its kernel is exactly {(0,0),(n,m)}: reducing mj+nr=0 modulo n
forces j=0 or n; modulo m forces r=0 or m; substitution retains just
the two listed pairs. Adding (n,m) changes j+r by 2n+1, an odd number.
Each two-element fiber therefore contains exactly one odd-board element.
Consequently mj+nr, on Gamma^-, visits each residue modulo 2N exactly
once. The integer shift n in (5) permutes these residues. The cotangent
has period pi, and substitution proves (3).

As t tends to zero only the q=0 term is singular, and
sin(pi*t) cot(pi*t/(2N))/(2N) tends to 1. All other terms tend to zero.
At t tending to one the q=2N-1 term gives the same limit. S_n is a
finite sum of continuous polynomial absolute values, so its endpoint
values are exactly 1. Finally S_n is even in each phase separately:
reflect j to -j modulo 2n, or r to -r modulo 2m, and use evenness of
G_n in the corresponding angle. This proves the identity on all four
closed diamond edges, including their shared vertices.

### 3. Uniform harmonic and regular-part remainders

For 0<t<1, reflection of the negative half of the cotangent sum gives

\[
\sum_{q=0}^{2N-1}|\cot(\pi(q+t)/(2N))|
=\sum_{k=0}^{N-1}\left[
 \cot\frac{\pi(k+t)}{2N}+\cot\frac{\pi(k+1-t)}{2N}\right]. \tag{6}
\]

Let H_N(t)=sum_{k=0}^{N-1}1/(k+t). The definition of gamma and absolute
convergence of the defining series give
H_N(t)+H_N(1-t)-2log N -> C(t). Hence the exact tail is

\[
H_N(t)+H_N(1-t)-2\log N-C(t)
=\sum_{k=N}^{\infty}\left[
2\log(1+1/k)-\frac1{k+t}-\frac1{k+1-t}\right].             \tag{7}
\]

For f(x)=1/x on [k,k+1], convexity places the paired value
f(k+t)+f(k+1-t) between the doubled midpoint value and the endpoint
sum. The midpoint and trapezoid errors, obtained by integrating the
second-order Taylor remainder, bound its difference from 2 integral f
by sup|f''|/6 <=1/(3k^3). Therefore, uniformly in t,

\[
|H_N(t)+H_N(1-t)-2\log N-C(t)|
\le\frac1{6N^2}+\frac1{3N^3}\le\frac1{2N^2}.             \tag{8}
\]

Put A=pi/2, h=A/N, and v(x)=cot x-1/x, continuously at zero.
PD-T270 proves |v''|<1 on [0,A], and direct integration gives
integral_0^A v=log(2/pi). In each cell [kh,(k+1)h], the average
of v((k+t)h),v((k+1-t)h) and the cell average both have the same
constant and linear Taylor terms about the midpoint. Their remainder
difference is at most h^2/8+h^2/24=h^2/6. Thus

\[
\left|\frac1{2N}\sum_{k=0}^{N-1}
 [v((k+t)h)+v((k+1-t)h)]-\frac2\pi\log\frac2\pi\right|
\le\frac{\pi^2}{24N^2}.                                 \tag{9}
\]

Insert cot x=1/x+v(x) in (6) and then (3). Equations (8) and (9)
give exactly (1) and the uniform error
sin(pi*t)*(1/(2pi)+pi^2/24)/N^2 < 7/(12N^2), using pi>3 and
pi^2<10. The defining series for C(t) shows sin(pi*t) C(t)/pi ->1
at both endpoints; its other terms after the explicit endpoint poles
are bounded there. Continuity extends the bound to t=0,1.

### 4. Midpoints

At t=1/2 the two sums in (6) coincide, proving S_n=L_N exactly.
PD-T270 with its degree parameter equal to N proves (4). No assertion
about the physical Lebesgue function attaining this primitive value
away from corners is used or follows.

## Scope

This controls the entire boundary of the phase diamond, all n>=2, with
a uniform absolute error of order n^-4. It does not control any open
neighborhood inside the diamond, locate a primitive maximum, compare
class-wise defects, or establish an effective global argmax threshold.

## Open items

Full-diamond logarithmic and constant profiles, with compatible interior
and boundary transition remainders. The original scope was accepted by
audit-01; the record response check remains pending. H2 and PD-T099 remain OPEN.

## History

2026-11-05, Codex, AC-requested gpt-6-astra ultra. Input/rules
ed21cc0bf205549936fccde90244a291bc6de324. Candidate selected after the
documented gate and before any fits. No final ID allocated.

2026-11-05 audit response, Codex, gpt-6-astra ultra: E2/E3 disambiguate
N and L_M and cite the csc definition and cotangent identity separately.
The first-writing pending-review description is superseded by audit-01's
acceptance at the original scope. Statement, proof and status are unchanged.

## Registration — 2026-11-05

Final ID: **PD-T365**. Preserved provisional alias: `PD-T?argmax-effective-2-codex-03`.
Registration input/rules: `5821c3f130ec0b1e33ad1d01620b67620e1f0be1`.

The exact diamond-boundary primitive and its existing uniform remainder are registered at the written boundary-only scope; the full-diamond H2 target remains OPEN.

[Claude audit-01](../audit-01.md) accepted the mathematical scope;
[response-check-01](../response-check-01.md) accepted the record response.
Earlier provisional/no-final-ID and pending-response-check wording above
is retained as history and is superseded only administratively by this
registration. Every pre-existing paragraph after the heading, including
Statement, proof, status, displays and History, is preserved byte for byte.
The [final-ID map](../preparation/final-id-map.json) and
[registration notes](../preparation/registration-notes.md) record the mapping
and preparation limits. PD-T099 remains OPEN; the global certified range
remains exactly 2–32.
