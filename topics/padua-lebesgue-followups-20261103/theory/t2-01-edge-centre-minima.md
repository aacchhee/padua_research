# PD-T?lebesgue-followups-codex-t2-01 — Unique centre minima of both edge-defect integrals

ID kind: PD-T.
Aliases: T2; strict centreward integral monotonicity; horizontal central value one.
Split from: the centre-minimality obligations explicitly excluded by PD-T211,
PD-T212 and PD-T230; no finite-degree argmax claim is split or upgraded.
Split into: endpoint asymptotics and general-position evaluation in separate records.

## Statement

Let g_v and g_h be exactly the integrals of PD-T211 and PD-T212, with
their different respective numerators. Both obey

\[
 g_e(\pi-\beta)=g_e(\beta)\quad(e=v,h),
\]

and are strictly decreasing on \((0,\pi/2]\). Consequently

\[
 \min_{0<\beta<\pi}g_v(\beta)=g_v(\pi/2)=g,
 \qquad \min_{0<\beta<\pi}g_h(\beta)=g_h(\pi/2)=1,
\]

each attained only at the centre. Here g is PD-T187/188's exact constant.
In particular the horizontal central value is exactly 1, which is stronger
than a decimal enclosure.

## Definitions

For \(\beta\in(0,\pi)\), put \(p=|\cos\beta|\), \(q=\sin\beta\), so
\(p^2+q^2=1\). For \(0\le r<1\), define

\[
 A(r)=\operatorname{arsinh}r+\frac{r}{1+\sqrt{1+r^2}},\qquad
 F(r)=\frac{2\{\log(1+\sqrt{1+r^2})-r\operatorname{arsinh}r\}}{1-r^2}.
 \tag{1}
\]

Continue \(F(1)=A(1)\). Define the complete elliptic integral directly by
\(K(k)=\int_0^{\pi/2}(1-k^2\sin^2t)^{-1/2}\,dt\), \(0\le k<1\).
Its logarithmic value at 1 is used only under an integrable improper integral.

The exact comparison formulas are

\[
 g_v(\beta)=g+\frac{4p}{\pi^2}\int_q^1
                 \frac{F(r)}{\sqrt{r^2-q^2}}\,dr
 =g+\frac{4p^2}{\pi^2}\int_0^1
 \frac{F(\sqrt{q^2+p^2x^2})}{\sqrt{q^2+p^2x^2}}\,dx,       \tag{2}
\]

where the excess is 0 when p=0, and

\[
 g_h(\beta)=\frac8{\pi^2}\int_0^1
 \frac{K(\sqrt{p^2+q^2y^2})}{1+y}\,dy.                    \tag{3}
\]

These identities are proved here as part of the comparison argument;
T3 may use them without reinterpreting the inherited functions.

## Assumptions

Exact real arithmetic and the literal PD-T211/212 definitions. No finite-n
profile, numerical comparison, external elliptic-integral theorem,
monotonicity conjecture or formal audit is a premise.

## Status by part

Overall status: **PROVED**, by the written analytical proof; distinct
supplementary reconstruction and required Claude audit pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact representations (2)/(3), symmetry, strict monotonicity and unique minima | PROVED | Proof below |
| Exact horizontal central value 1 | PROVED | Elementary square integral below |

Candidate disposition: retained variant with explicit position comparison;
no historical novelty or priority claim.

## Depends on

PD-T211/212 only for the definitions of g_v/g_h; PD-T187/188 for the name
and central normalization of g. The displayed identities can also be
read as standalone integral statements independent of finite-degree limits.

## Checks

The development scratch double-quadrature diagnostic was executed at
beta=pi/2, pi/3, pi/4, pi/10 and .01. It suggested the formulas but supplies
no proof premise. Frozen reproducible checks and outputs will be linked
from T3. Independent reconstruction by a distinct agent is pending.

## Sources

No external source theorem used. Repository novelty gate:
[gate-t2-t3.md](../gate-t2-t3.md). Standard elementary changes of variables,
Tonelli's theorem and the odd reciprocal-square sum are justified below.

## Proof

### Symmetry and notation

The simultaneous substitution beta->pi-beta, b->pi-b preserves both
z_+=cos(beta+b) and z_-=cos(beta-b). It preserves the vertical integral.
The same substitution in the horizontal integration angle a preserves
both z endpoints and its unchanged numerator 1+B. Thus both functions
are reflection symmetric. It suffices henceforth to assume beta<=pi/2,
so p=cos beta>=0. All substitutions below first take place away from the
measure-zero degeneracies; nonnegative integration justifies the limits.

### Horizontal reduction

Write c=cos a, s=sin a, M=pc, D=qs>0. In the band |B-M|<D,
the horizontal integrand is (1+B)/(D+|B-M|). Reflection
(a,B)->(pi-a,-B) preserves its band, denominator and angular measure;
averaging replaces the numerator 1+B by 1 in the entire double integral.
Then set B=pc+q sin(a)y, -1<y<1. The angular measure db equals
|dB|/sqrt(1-B²), so the D factor cancels and the integral becomes

\[
 \frac2{\pi^2}\int_{-1}^1\frac{dy}{1+|y|}
 \int_0^\pi\frac{da}{\sqrt{1-(p\cos a+qy\sin a)^2}}.
\]

For fixed y in (-1,1), write the linear combination as
R cos(a-d), R²=p²+q²y²<1. The integrand has period pi, so its integral
on any interval of length pi is 2K(R). Evenness in y proves (3).
For every y in [0,1), R²=y²+p²(1-y²) strictly increases with p².
The defining integral makes K strictly increasing in its squared modulus.
Thus (3) strictly increases with p², proving the horizontal monotonicity
and uniqueness once its central value is evaluated.

At beta=pi/2, reflection of both angles reduces the original integral to

\[
 g_h(\pi/2)=\frac8{\pi^2}\int_0^{\pi/2}\int_0^b
                  \frac{dx\,db}{\sin b+\sin x}
 =\frac4{\pi^2}\int_0^{\pi/2}\int_0^{\pi/2}
                  \frac{dx\,db}{\sin b+\sin x}.
\]

With t=tan(x/2), u=tan(b/2), the latter double integral is

\[
 2\int_0^1\int_0^1\frac{dt\,du}{(t+u)(1+tu)}
 =2\int_0^1\frac{-\log t}{1-t^2}\,dt
 =2\sum_{j\ge0}\frac1{(2j+1)^2}=\frac{\pi^2}{4}.
\]

The middle equality follows by partial fractions; the positive series
is Tonelli. The final odd-square identity follows, for example, from
Parseval applied to the sine series of the constant function on (0,pi):
its odd sine coefficients are 4/[pi(2j+1)], giving
pi=(pi/2)(16/pi²)sum(2j+1)^(-2). This proves the exact value 1.

### Vertical reduction with a fixed switch

Fix b in (0,pi) and set z_+=cos(beta+b)<z_-=cos(beta-b). Let
L=sqrt((1-z_-)/(1+z_-)), U=sqrt((1-z_+)/(1+z_+)), 0<=L<U.
Put x=tan(u/2), so the band has L<x<U. The two vertical fractions times
du become 2 dx/(U²-x²) and 2 dx/(x²-L²). Their minimum therefore has
the exact expression

\[
 \frac{2\,dx}{\max(U^2-x^2,x^2-L^2)}.
\]

Set y=(2x²-U²-L²)/(U²-L²). This sends the band to -1<y<1 and,
including its Jacobian, sends that expression to dy/[x(1+|y|)].
Writing c=cos b and s=sin b, direct algebra gives

\[
 U^2+L^2=\frac{2(s^2+q^2)}{(p+c)^2},\qquad
 U^2-L^2=\frac{4qs}{(p+c)^2},\qquad
 x=\frac{\sqrt{s^2+q^2+2qsy}}{|p+c|}.                     \tag{4}
\]

The exceptional b=pi-beta is a single null row and is not divided by zero.
Thus the vertical integral is

\[
 \frac2{\pi^2}\int_{-1}^1\frac{dy}{1+|y|}
 \int_0^\pi\frac{|p+\cos b|\,db}{\sqrt{\sin^2b+q^2+2q\sin b\,y}}.
\]

Pair b with pi-b, and then set s=sin b on (0,pi/2). Since
|p+c|+|p-c|=2max(p,c), split at s=q to obtain the inner integral

\[
 2\int_0^q\frac{ds}{\sqrt{s^2+q^2+2qsy}}
 +2p\int_q^1\frac{ds}{\sqrt{1-s^2}\sqrt{s^2+q^2+2qsy}}.
 \tag{5}
\]

The first term, after s=qr, is independent of q. The second, after r=q/s,
equals 2p int_q^1 [1/sqrt(1+r²+2ry)] dr/sqrt(r²-q²).
Define equivalently

\[
 F(r)=\int_{-1}^1\frac{dy}{(1+|y|)\sqrt{1+r^2+2ry}}.       \tag{6}
\]

At q=1,p=0, (5) gives g=(4/pi²)int_0^1 F(r)dr. Hence (5) gives the
first formula (2); r=sqrt(q²+p²x²) gives the second. In particular its
strictly positive excess proves the unique vertical minimum directly.

For completeness, integrate (6) on y>=0 and y<=0 with
v=sqrt(1+r²+-2ry). The two elementary integrals give

\[
 \frac{2}{1-r}\log\frac{1-r+\sqrt{1+r^2}}{\sqrt2}
 +\frac{2}{1+r}\log\frac{1+r+\sqrt{1+r^2}}{\sqrt2},
\]

which reduces to (1), since the sum of the two logarithms is
log(1+sqrt(1+r²)) and their difference is asinh r. Continuity gives
r=0 and r=1. This also independently identifies the central integral
with PD-T188's representation.

### Strict vertical monotonicity

Put H(r)=log(1+sqrt(1+r²))-r asinh r. Then H(1)=0 and H'(r)=-A(r).
Consequently

\[
 F(r)=\frac{2\int_r^1 A(t)\,dt}{1-r^2}
 =\frac{\int_r^1 [A(t)/t],2t\,dt}{\int_r^1 2t\,dt}.       \tag{7}
\]

The continuous value at t=0 is A(t)/t=3/2. Both asinh(t)/t and
1/(1+sqrt(1+t²)) strictly decrease for t>0: the first is
int_0^1 (1+t²z²)^(-1/2) dz. Thus A(t)/t strictly decreases, and (7)
shows F positive and strictly decreasing. In particular F(r)/r is
strictly decreasing for 0<r<=1.

In the last formula (2), r=sqrt(1-p²(1-x²)) decreases as p² increases
for every x<1. The integrand F(r)/r therefore increases, while the
prefactor p² increases and is nonnegative. This proves strict increase
with p², including the centre, and completes the theorem. ∎

## Scope

Only the limiting defect integrals. Finite-degree whole-cell ordering,
common-phase ordering, effective convergence and all-degree argmax are
not consequences asserted here.

## Open items

Distinct supplementary reconstruction, reproducible T3 evaluations and
the required cross-family audit. No mathematical minimum case is left open.

## History

2026-11-03, Codex gpt-6.1-sol xhigh, rules/input 3f5196c. Gate and stopping
rules preceded derivation at 11:18 UTC. Both numerator distinctions were
kept; horizontal exact central value replaces the requested decimal target.
