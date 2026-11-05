# PD-T268 — General-position geometric series with explicit tails

Dated 2026-11-05 PR registration: Final ID: PD-T268. Preserved provisional alias: `PD-T?lebesgue-followups-codex-t3-01`. [Claude audit-01](../audit-01.md) accepts the mathematics; [response-01](../response-01.md) answers its minor findings. Earlier pending-audit wording below records the development stage and is superseded by this dated status. T2/T3 prospective-gate timing remains unwaived; physical cold-storage delivery remains pending. See [final map](../preparation/final-id-map.json). Mathematical text below is unchanged.

ID kind: PD-T.
Aliases: T3; general-beta defect evaluation; two horizontal expansion charts.
Split from: T3 general-position series obligation extending PD-T188.
Split into: finite execution receipts are verification records, not new theorems.

## Statement and definitions

Use p=|cos beta|, q=sin beta, m=p², L=atanh p, 0<beta<pi, and F,A,K,g
as defined in [t2-01](t2-01-edge-centre-minima.md). That theorem supplies
one-dimensional formulas for both inherited defect integrals. This record
supplies geometrically convergent series with explicitly computable terms.
Let c_k=binom(2k,k)/4^k, and put

\[
 a_j=\frac1{2j+1}+\frac1{2j+2},\quad
 P_k(z)=\sum_{j=0}^k(-1)^j\binom kj\frac{a_j}{j+1}
                      \sum_{l=0}^jz^l.
\]

Let M_0=L and, for l>=1,

\[
 M_l=\frac{p}{2l}+\frac{(2l-1)q^2}{2l}M_{l-1}.
\]

Define

\[
 V_k=\sum_{j=0}^k(-1)^j\binom kj\frac{a_j}{j+1}
            \sum_{l=0}^j\left\{\frac1{2l+1}+pM_l\right\}.
\]

Then, for every N>=0,

\[
 G_N^v=\frac4{\pi^2\sqrt2}\sum_{k=0}^N c_k2^{-k}V_k,
 \quad 0<g_v(\beta)-G_N^v
 \le \frac6{\pi^2\sqrt2}\,2^{-N}(1+pL).                  \tag{1}
\]

At p=0 set L=0. The formula specializes exactly to the same g as PD-T188,
with a geometric rather than alternating algebraic remainder.

For the horizontal centre chart, define, for k>=1,

\[
 I_k=\sum_{j=0}^{k-1}\frac{(-1)^j\binom{k-1}{j}}{2j+1}
             \left\{\frac\pi2c_j-\frac1{2j+1}\right\}.
\]

Then

\[
 G_N^h=1+\frac8{\pi^2}\sum_{k=1}^N c_km^k I_k,
 \qquad 0\le g_h(\beta)-G_N^h
 \le\frac{m^{N+1}}{1-m}.                                 \tag{2}
\]

At m=0 the series is identically 1. Use (2) for m<=1/2.

For the endpoint chart put z=q², d_k=2(H_{2k}-H_k), H_0=0, and

\[
 U_k=\int_0^1\frac{(1-y^2)^k}{1+y}\,dy,\quad
 W_k=\int_0^1\frac{(1-y^2)^k\log(1-y^2)}{1+y}\,dy.
\]

Here U_0=log2, W_0=-pi²/12+log²2. For k>=1 the weight
(1-y²)^k/(1+y)=(1-y)^k(1+y)^{k-1} is a polynomial; hence U_k and W_k
are finite computable combinations of rationals and log2. Explicit
monomial rules, with Q_0=log2 and Q_j=1/j-Q_{j-1}, are

\[
 \int_0^1y^jdy=\frac1{j+1},\quad
 \int_0^1y^j\log(1-y)dy=-\frac{H_{j+1}}{j+1},\quad
 \int_0^1y^j\log(1+y)dy=\frac{\log2-Q_{j+1}}{j+1}.
\]

Then

\[
 \widetilde G_N^h=\frac8{\pi^2}\sum_{k=0}^N c_k^2 z^k
       \{(\log(4/q)-d_k)U_k-W_k/2\},
\]

\[
 0\le g_h(\beta)-\widetilde G_N^h
 \le \frac{z^{N+1}}{1-z}
 \frac8{\pi^2}\{\log(4/q)\log2-W_0/2\}.                 \tag{3}
\]

Use (3) for z<1/2. Thus every fixed interior angle has a vertical series
with ratio at most 1/2 and a horizontal chart with ratio at most 1/2.
The prefactors need not be bounded uniformly as beta approaches an endpoint.

## Assumptions

Exact real arithmetic; the elementary functions and pi have their usual
definitions. For a numerical enclosure their values must themselves be
outward enclosed. Formulas cover all beta in (0,pi), not only rational
angles or rational p². The accompanying evaluator takes rational p².

## Status by part

Overall status: **PROVED**, written analytic series and tails.
Supplementary distinct reconstruction and numerical reruns completed at
their recorded hashes; required Claude audit pending.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| General-position geometric series (1)–(3), computable moments and tails | PROVED | Proof below |

Candidate disposition: retained variant of PD-T188 with arbitrary position
and geometric tails; no historical novelty claim.

## Depends on

t2-01 exact 1D formulas; t2-02's directly proved leading K logarithm and
logarithmic moment W_0. PD-T188 identifies the inherited central constant.

## Proof

### Vertical geometric expansion

Write a(x)=A(x)/x, continued at 0. Direct integration gives

\[
 a(x)=\int_0^1\frac{1+t}{\sqrt{1+x^2t^2}}dt
 =\frac1{\sqrt2}\sum_{k\ge0}c_k2^{-k}
                          \int_0^1(1+t)(1-x^2t^2)^kdt.    \tag{4}
\]

Indeed (1+x²t²)^(-1/2)=2^(-1/2)(1-(1-x²t²)/2)^(-1/2), with expansion
argument in [0,1/2]. All terms are nonnegative, and the tail after N is
at most (3/(2sqrt2))2^(-N), since c_k<=1 and int_0^1(1+t)dt=3/2.
By t2-01, F(r) is the 2x-weighted tail average of a(x) on [r,1].
Averaging the polynomial in (4) produces exactly P_k(r²). Its remainder
has the same bound, uniformly on [0,1]. Substitute this F series into

\[
 g_v=(4/\pi^2)\{\int_0^1F(r)dr+p\int_q^1F(r)dr/\sqrt{r^2-q^2}\}.
\]

Positive integration justifies the interchange. The first moments are
1/(2l+1); the second are M_l=int_q^1 r^{2l}dr/sqrt(r²-q²).
Differentiating r^{2l-1}sqrt(r²-q²) proves the recurrence above.
M_0=arcosh(1/q)=atanh p. The total remainder weight is
(4/pi²)(1+pL), yielding (1). This proves central agreement by identity,
independently of any decimal comparison with PD-T188.

### Horizontal centre expansion

Insert the defining integral for K in t2-01's horizontal formula.
Its denominator squared is

\[
 1-y^2\sin^2t-m(1-y^2)\sin^2t.
\]

Expand around m=0. The expansion ratio without m is
(1-y²)sin²t/(1-y²sin²t)<=1, so positive integration gives coefficients

\[
 I_k=\int_0^1\frac{dy}{1+y}\int_0^{\pi/2}
 \frac{(1-y^2)^k\sin^{2k}t}{(1-y^2\sin^2t)^{k+1/2}}dt.
 \tag{5}
\]

The k=0 term is pi²/8 by t2-01. Each I_k<=I_0, so the omitted
terms after multiplication by 8/pi² are at most sum_{k>N}m^k,
proving (2). To evaluate I_k, first set u=cot t in (5), then
u=sqrt(1-y²)v. The inner y integral is

\[
 \int_0^1\frac{dy}{(1+y)\sqrt{1+(1-y^2)v^2}}
 =\log\left(1+\frac1{\sqrt{1+v^2}}\right).
\]

For example y=(1-w)/(1+w) reduces it to
int_0^1 dw/sqrt(w²+(2+4v²)w+1), whose logarithmic endpoint difference
is the displayed value. Now v=tan t gives

\[
 I_k=\int_0^{\pi/2}\cos^{2k-1}t\log(1+\cos t)dt.
\]

For k>=1 integrate by parts using the primitive
sum_{j=0}^{k-1}(-1)^j binom(k-1,j)sin^{2j+1}t/(2j+1).
Since -(d/dt)log(1+cos t)=sin t/(1+cos t), the resulting moments are
int sin^{2j}t dt=(pi/2)c_j and int cos t sin^{2j}t dt=1/(2j+1).
This is precisely the finite sum defining I_k.

### Horizontal endpoint expansion and its justification

For 0<w<1 the directly defined K satisfies

\[
 K(\sqrt{1-w})=\sum_{k\ge0}c_k^2w^k
              \{\log(4/\sqrt w)-d_k\}.                  \tag{6}
\]

A self-contained ODE verification fixes its normalization. Differentiation
under K's integral shows that Y(w)=K(sqrt(1-w)) solves
w(1-w)Y''+(1-2w)Y'-Y/4=0. One way to verify the integration step is to
put s=sin t, h=1-(1-w)s². After a common denominator 4h^(5/2), the ODE
integrand numerator is
-1+2ws²+(1-w)s^4. It is the negative derivative in t of
sin t cos t /h^(3/2), after multiplying by h^(5/2); the endpoint term
vanishes. [This identity may also be checked by direct differentiation.]

Substitute a logarithmic power series into this ODE. The coefficient
recurrences are c_{k+1}²/c_k²=((k+1/2)/(k+1))² and
d_{k+1}-d_k=1/((k+1)(2k+1)), d_0=0, precisely d_k=2(H_{2k}-H_k).
These determine the series solution (6), convergent for 0<w<1 since
c_k²<=1 and d_k<=2log2. Its leading form is log(4/sqrt w)+o(1),
which agrees with t2-02's direct logarithm estimate.

For completeness, matching the leading constant determines the solution:
the analytic series A(w)=sum c_k²w^k solves the same ODE and tends to1.
Reduction of order makes any independent solution
A(w)int dw/[w(1-w)A(w)²], which has a nonzero logarithmic leading term.
Thus a difference o(1) with zero leading logarithm cannot contain either
independent solution, proving (6) for the integral-defined K.

To check the asserted bound d_k<2log2, observe
H_{2k}-H_k=sum_{j=k+1}^{2k}1/j<int_k^{2k}dt/t=log2 for k>=1.
Hence every bracket in (6) is positive. Set w=z(1-y²) and integrate
termwise. This proves the endpoint series with U_k,W_k above. Its
omitted integrand is bounded by

\[
 \sum_{k>N}z^k\{\log(4/q)-\tfrac12\log(1-y^2)\}/(1+y),
\]

which proves (3). The polynomial monomial rules follow respectively from
elementary integration, the positive series for -log(1-y), and integration
by parts plus division by 1+y. Thus every term is explicitly computable. ∎

## Checks and sources

No external fulltext theorem or numerical fit is a premise. The committed
[exact rational evaluator](../code/t3_series.py) uses Fraction arithmetic,
integer square-root bounds, positive logarithmic-series tails and Machin
arctangent pi bounds (whose normalization is proved in PD-T188). Its
72-term developer receipt encloses both functions at m=0,1/4,1/2,3/4,99/100
to 16 decimal places; the central vertical enclosure is
[0.5485148423995582,0.5485148423995583], and the horizontal value is exactly 1.

The separate [outward quadrature](../code/t3_quadrature.py) evaluates the
positive one-dimensional formulas directly, without the T3 F/K series.
All five series intervals lie inside its deliberately coarse Darboux
enclosures. Its square roots and logarithms use correctly rounded Decimal
functions enlarged by adjacent decimals; all arithmetic and sums round
outward. This is a numerical implementation comparison; the analytic
reduction from the inherited double integrals is proved in t2-01.

Exact commands, dependencies, source/receipt identities, the finite value
table and quadrature bounds are in [verification](../evidence/t3-verification.md).
Distinct Astra independently reconstructed the mathematics and executed
both numerical routes; its separate floating diagnostic of the original
double integrals remains MEASURED, not a premise. Current hashes and the
small adaptive-sqrt robustness review are in the separate
[independent report](../independent-checks-analytic.md).

## Scope and open items

These are pointwise-in-angle computable enclosures, with a selected
horizontal chart ensuring geometric ratio <=1/2. Uniform endpoint
prefactors are not claimed. Required cross-family audit remains pending;
the supplementary distinct checks do not replace it.

## History

2026-11-03, Codex gpt-6.1-sol xhigh; rules/input 3f5196c. Candidate and
stopping plan preceded derivation. The uniform positive vertical expansion
replaces the slow unshifted alternating Taylor route, which is retained
as an equivalent central check rather than pursued as a new mechanism.
