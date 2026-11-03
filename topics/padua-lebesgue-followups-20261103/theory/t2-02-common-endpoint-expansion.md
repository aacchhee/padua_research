# PD-T?lebesgue-followups-codex-t2-02 — Common logarithmic endpoint expansion

ID kind: PD-T.
Aliases: T2 endpoint behaviour; common vertical/horizontal endpoint constant.
Split from: T2 endpoint-growth obligation; no finite-n corner transition asserted.
Split into: none.

## Statement

For beta in (0,pi), let d=min(beta,pi-beta), q=sin beta, and set

\[
 C=\frac{8\log2}{\pi^2},\qquad
 B=\frac13+\frac{12\log^2 2}{\pi^2}.
\]

Then the inherited edge-defect integrals satisfy

\[
 \left|g_h(\beta)-C\log(1/q)-B\right|
 \le \frac{4q}{\pi^2}\left(\frac\pi2-1\right),             \tag{1}
\]

\[
 \left|g_v(\beta)-C\log(1/q)-B\right|
 \le \frac{4d}{\pi}
       +\frac{4q}{\pi^2}\left(\frac\pi2-1\right).          \tag{2}
\]

Thus both equal C log(1/d)+B+O(d) at either endpoint, with a fully
explicit bound given by (1)/(2) plus C|log(d/sin d)|. The weaker
C log(1/d)+O(1) statement follows in particular.

## Definitions and assumptions

Exact g_v/g_h definitions in PD-T211/212, and K as defined directly in
[t2-01](t2-01-edge-centre-minima.md). Exact real arithmetic, 0<beta<pi.

## Status by part

Overall status: **PROVED**, analytical. Independent reconstruction and
required Claude audit pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Common logarithmic coefficient and constant, explicit (1)/(2) | PROVED | Proof below |

Candidate disposition: retained consequence of the exact T2 formulas.

## Depends on

PD-T211/212 definitions; t2-01 horizontal K representation and symmetry.
No elliptic-integral asymptotic is imported from a source.

## Checks and sources

No numerical calculation is a proof premise. No external theorem used
beyond elementary integration and the reciprocal-square identity proved
in t2-01. Reproducible supplementary numerical checks are a T3 output.

## Proof

### A direct uniform logarithmic estimate for K

For 0<t<=1, tangent substitution in K gives

\[
 K(\sqrt{1-t^2})=\int_0^\infty
          \frac{dx}{\sqrt{(1+x^2)(1+t^2x^2)}}
 =2\int_0^{1/\sqrt t}
          \frac{dx}{\sqrt{(1+x^2)(1+t^2x^2)}}.             \tag{3}
\]

The last identity follows by x->1/(tx) on the tail. The inequalities
1-z/2<=(1+z)^(-1/2)<=1, z>=0, imply

\[
 0\le 2\operatorname{arsinh}(1/\sqrt t)-K(\sqrt{1-t^2})
 \le t^2\int_0^{1/\sqrt t}\frac{x^2\,dx}{\sqrt{1+x^2}}
 \le t/2.
\]

Also

\[
 0\le2\operatorname{arsinh}(1/\sqrt t)-\log(4/t)
 =2\log\frac{1+\sqrt{1+t}}2\le t/2,
\]

using sqrt(1+t)<=1+t/2 and log(1+t/4)<=t/4. Hence

\[
 |K(\sqrt{1-t^2})-\log(4/t)|\le t/2.                   \tag{4}
\]

In t2-01's horizontal formula take t=q sqrt(1-y²). Its main integral is

\[
 \frac8{\pi^2}\left\{
 \log(1/q)\log2+\log4\log2
 -\frac12\int_0^1\frac{\log(1-y^2)}{1+y}\,dy\right\}.
\]

The elementary logarithmic integral is

\[
 \int_0^1\frac{\log(1-y^2)}{1+y}\,dy
 =-\frac{\pi^2}{12}+\log^2 2.                            \tag{5}
\]

One self-contained verification: define Li_2(z)=sum_{k>=1}z^k/k².
Termwise positive/absolute integration gives
int_0^1 log(1-y)/(1+y)dy=-Li_2(1/2), while
int_0^1 log(1+y)/(1+y)dy=(log²2)/2.
Differentiating the series on (0,1) proves
Li_2(z)+Li_2(1-z)=pi²/6-log z log(1-z): both derivatives agree
and the endpoint constant is the reciprocal-square sum. At z=1/2 this
gives Li_2(1/2)=pi²/12-(log²2)/2 and proves (5).
Thus the main value is C log(1/q)+B. Its error from (4) is at most

\[
 \frac{4q}{\pi^2}\int_0^1\frac{\sqrt{1-y^2}}{1+y}\,dy
 =\frac{4q}{\pi^2}(\pi/2-1),
\]

where y=sin u makes the last integrand (1-sin u)du. This proves (1).

### The two defects differ by at most the shrinking band's area

Write the double integrals with common variables beta,b,A=cos u and
common endpoints z_+<A<z_-. In this band put

\[
 X=(1+z_+)/(A-z_+),\qquad Y=(1+z_-)/(z_--A).
\]

The vertical integrand is min(X,Y). The horizontal integrand, after
renaming its dummy variables, is min(X+1,Y-1), because its numerator
is 1+A. For any real X,Y, changing the two entries by amounts of
absolute value at most 1 changes their minimum by at most 1.
Both integrands vanish off the common band. The band's angular width
in u is 2min(beta,b,pi-beta,pi-b)<=2d. Therefore

\[
 |g_h(\beta)-g_v(\beta)|
 \le(2/\pi^2)(2d\pi)=4d/\pi.                             \tag{6}
\]

Combine (1) and (6) for (2). Finally log(d/sin d)=O(d²), for example
sin d>=d-d³/6 for small d. This proves the stated endpoint expansion. ∎

## Scope

The endpoint limit takes beta to an endpoint in the already-defined
macroscopic integral. No interchange with n->infinity is asserted.

## Open items

Distinct supplementary reconstruction and required cross-family audit.

## History

2026-11-03, Codex gpt-6.1-sol xhigh; rules/input 3f5196c. Derived after
the centre-minimum proof; logarithmic coefficient and constant are exact,
not fitted from the inherited measured gaps.
