# PD-T?argmax-bridge-codex-H01-harmonic — The harmonic triangle through its first correction

ID kind: PD-T; provisional supporting result, no global allocation.
Aliases: H01 finite harmonic triangle; compensated partial-cotangent sum.
Split from: proposed sharp continuation of PD-T098 through IDEA287/288/358.
Split into: H04 owns the smooth B quadrature; H05 owns uniform digamma
centering. The final corner theorem belongs to the parent integration.

## Statement

Put m=n+1, a=2/pi, c=gamma+log(8/pi), A_m=a(log m+c), and, for
1<=r<=m-1, set x=r/m, s=m-r and

    w(x)=cot(pi*x/2),
    D_(m,r)=psi(r+(1-x)/2)+psi(s-(1-x)/2)
                         -psi(m-(1-x)/2)-psi((1-x)/2),
    Hcal_m=(4/(pi*m))*sum_(r=1)^(m-1) w(r/m)*D_(m,r).

Here psi is defined by the convergent harmonic series in H05, not by an
unread external theorem. There is a real constant C_H such that, over
ALL integers m>=3,

    Hcal_m=A_m^2+C_H+[-a^2*log m+beta_H]/m
                                      +O(log(m)/m^2), (1)
    beta_H=-2-a^2*(gamma+2log2)-a*(I1+I2),
    I1=integral_0^1 [w(x)/(1-x)-a/x] dx,
    I2=integral_0^1 x*w(x) dx.

The O constant is absolute and degree-independent; no parity subsequence
is taken. Both integrands are understood by their finite endpoint limits.

## Assumptions, dependencies and status

Exact real arithmetic; original corrected Padua convention throughout.
Dependencies: F03's exact partial-cotangent and two-pole decomposition,
PD-T159's endpoint normalization, PD-T270's harmonic estimate, and H05's
uniform centering lemma with its local psi definitions. This file proves
the aggregate analysis and evaluates the first-correction sequences.

Overall status: **OPEN during development / not yet adopted**. The complete
candidate proof below is submitted for distinct reconstruction; the parent
requested that no full sharp-target status be upgraded before that check.
No numerical evidence is used. In particular this is not a new claim of an
exact one-index O(n) evaluator. The finite cotangent-collapse attempt did
not eliminate the nested mass; its usable replacement is the proved-form
uniform asymptotic analysis below, subject to independent review.

## 1. Exact finite reduction and the failed collapse

F03 gives exactly, with its actual endpoint rows,

    Lambda_c=1-2n/m+(4/(n*m))*sum_(r=1)^n w(r/m)*T_(n,r),
    T_(n,r)=(n/pi)*D_(m,r)+sum_(l=0)^(r-1) B((l+(1-r/m)/2)/n),
    B(t)=cot(pi*t)-1/(pi*t)+1/(pi*(1-t)).              (2)

To identify D, the two harmonic partial sums in F03 are respectively
psi(r+(1-x)/2)-psi((1-x)/2) and
psi(m-(1-x)/2)-psi(s-(1-x)/2). This proves the displayed D exactly.
All r=1,...,n occur. In particular r=n is retained; the separate
polynomial endpoint contribution in PD-T159 has not been discarded.
The scalar base in (2) is EXACTLY -1+2/m, an essential first correction.

Cotangent product/complement algebra does not replace the r-term partial
by a complete signed row. It leaves the same triangular mass; an exact
O(n) collapse is not obtained or claimed. The following analysis instead
keeps that mass and controls its aggregate error at the requested scale.

## 2. Elementary psi estimates and summable endpoint sequences

The H05 series and recurrence give, for real t>=1,

    psi(k)=log k-1/(2k)+O(k^-2)                    (k integer),
    psi'(t)=sum_(j=0)^infty (t+j)^-2,
    psi'(k)=1/k+O(k^-2).                           (3)

The first identity is PD-T270's harmonic estimate and
psi(k)=H_(k-1)-gamma. The last follows from the integral comparison for
the positive decreasing series, with an absolute uniform constant.

Define on t>=1

    e(t)=psi(t+1/2)-log t,
    u(t)=t*psi'(t+1/2)-1.

The unit-cell midpoint rule applied to y^-2 on [t,infinity) gives

    psi'(t+1/2)=1/t+O(t^-3).                         (4)

For a detailed bound, on [t+j,t+j+1] its midpoint error is at most
sup(6y^-4)/24; the sum of these suprema is O(t^-3), uniformly for
t>=1. Thus u(t)=O(t^-2). Monotonicity of psi and its integer values
squeeze psi(t+1/2)-log t to zero as t tends to infinity. Integrating
e'(t)=psi'(t+1/2)-1/t from infinity in (4) gives e(t)=O(t^-2).
Consequently the following two constants converge absolutely:

    S_e=sum_(r>=1) e(r)/r,
    S_u=sum_(r>=1) u(r)/r.

Only S_u must be evaluated. Finite recurrence summation gives EXACTLY

    sum_(r=1)^R psi'(r+1/2)
      =(R+1/2)*psi'(R+1/2)+psi(R+1/2)
                                      -psi(1/2)-psi'(1/2)/2.  (5)

For example, obtain (5) by subtracting the first r terms of the series
for psi'(1/2), summing the resulting finite triangle, and writing
k=(k+1/2)-1/2. The harmonic recurrence and the integer limit imply
psi(1/2)=-gamma-2log2. Also psi'(1/2)=4*sum_(odd j>=1)j^-2=pi^2/2,
using the same elementary odd-square sum as PD-T159/269. By (3)--(4),
(R+1/2)psi'(R+1/2) tends to 1 and psi(R+1/2)-H_R tends to -gamma.
Subtract H_R in (5), then let R tend to infinity:

    S_u=1+2log2-pi^2/4.                             (6)

## 3. Weighted uniform remainder after the H05 reanchor

H05 proves for every 1<=r,s<=m-1 with r+s=m,

    D=psi(r+1/2)+psi(s)-psi((1-x)/2)-psi(m)
       -[r*psi'(r+1/2)+s*psi'(s)-s*psi'(m)]/(2m)+E,
    abs(E)<=2/m^2.                                 (7)

Let

    F(x)=log x+log(1-x)-psi((1-x)/2).

Use (3), while keeping e(r) and u(r) exact. Straight subtraction in (7)
then gives

    D=log m+F(x)+e(r)-1/[2m(1-x)]-x/(2m)-u(r)/(2m)+R_(m,r),
    abs(R_(m,r))<=C*[s^-2+(m*s)^-1+m^-2].            (8)

This is a pointwise inequality with a single absolute C, not a formal
fixed-index expansion. To check its first-order arithmetic, the integer
psi(s), -psi(m) contribute -1/(2s)+1/(2m). The derivative bracket is
1+u(r)+1-(1-x)+O(1/s+1/m)=1+x+u(r)+O(1/s+1/m).
Thus its scalar first correction is -x/(2m), as displayed.

The elementary bounds

    0<w(r/m)<=a*m/r,
    w(r/m)<=C*s/m                   (r>=m/2)         (9)

give

    (1/m)*sum_(r=1)^(m-1) w(r/m)*abs(R_(m,r))
                                  =O(log(m)/m^2).   (10)

Indeed on r<=m/2 use s>=m/2 and the first bound in (9); on r>=m/2
use the second. The s^-2 term becomes respectively O(H_m/m^2) and
O(H_m/m^2). The (m*s)^-1 and m^-2 terms are no larger. This handles
both endpoint layers without an excluded strip or a parity assumption.

Put v(x)=w(x)-a/x, v(0)=0. It is smooth on [0,1] and |v(x)|<=C*x.
Since e(r),u(r)=O(r^-2), absolute convergence and (9) imply

    (1/m)*sum_(r<m) w(r/m)*e(r)=a*S_e+O(log(m)/m^2),
    (1/m)*sum_(r<m) w(r/m)*u(r)=a*S_u+O(log(m)/m^2). (11)

The omitted tails are O(m^-2); the v contributions are bounded by
C*m^-2*sum_(r<m)r^-1. In particular the e sequence contributes NO
1/m term; dropping the u sequence would instead lose a genuine one.

The functions w(x)/(1-x)-a/x and x*w(x) extend smoothly to [0,1].
The ordinary trapezoid estimate therefore gives

    (1/m)*sum_(r<m) w(r/m)/(1-r/m)
                         =a*log m+a*gamma+I1+O(1/m),
    (1/m)*sum_(r<m) (r/m)*w(r/m)=I2+O(1/m).           (12)

All estimates in (10)--(12) are degree-uniform. Applying (8) now gives,
with M_m=(1/m)sum w(r/m)[log m+F(r/m)],

    Hcal_m=(4/pi)*[M_m+a*S_e
       -(a*log m+a*gamma+I1+I2+a*S_u)/(2m)]
                         +O(log(m)/m^2).             (13)

## 4. The singular trapezoid calculation for M_m

Write c0=gamma+2log2 and c1=pi^2/4-1, and set

    R(x)=w(x)*F(x)-a*(log x+c0)/x.

At x=0, psi is analytic near 1/2 and
F(x)=log x+c0+c1*x+O(x^2). At x=1, writing y=1-x,
psi(y/2)=-2/y-gamma+O(y) and w(x)=pi*y/2+O(y^3).
These follow directly from the convergent psi series. Consequently

    R(0)=a*c1,          R(1)=pi-a*c0,                (14)
    abs(R''(x))<=C*[1+x^-1+(1-x)^-1]       (0<x<1),
    R(x)-R(0)=O(x*abs(log x)),
    R(1-y)-R(1)=O(y*abs(log y)).                     (15)

For clarity, near zero R=a*(J(x)-c0)/x+v(x)[log x+J(x)],
J(x)=log(1-x)-psi((1-x)/2), where the first term is analytic and
v=O(x); its only second-derivative singularity is O(1/x).
Near one the only nonsmooth term is a constant times y*log y plus
terms with weaker derivatives. This proves (15) uniformly by compactness
on the remaining central interval.

It follows that the endpoint-excluded trapezoid rule has error

    (1/m)*sum_(r<m)R(r/m)
       =integral_0^1 R-(R(0)+R(1))/(2m)+O(log(m)/m^2). (16)

Here is a direct error justification at the claimed scale. Each of the
two endpoint cells costs O(log(m)/m^2) by the last two bounds in (15).
On the other cells the elementary local trapezoid error is at most
C*m^-3 times the supremum of |R''|; summing (15) costs O(log(m)/m^2).
No smoothness assumption across an endpoint pole is being imported.

The needed harmonic formulas are

    H_(m-1)=log m+gamma-1/(2m)+O(m^-2),
    sum_(r<m) log(r)/r
       =(log m)^2/2+C_K-log(m)/(2m)+O(log(m)/m^2).     (17)

The first was already proved in PD-T270. For the second, apply the
trapezoid identity to f(t)=log(t)/t on each unit interval from 1 to m.
The sum of its local errors converges because
f''(t)=(2log t-3)/t^3 is absolutely integrable at infinity, and its
tail is O(log(m)/m^2). Since f(1)=0, the endpoint-excluded sum is the
integral plus a constant minus f(m)/2 and that tail. This proves (17)
with an actual constant C_K, not an unproved asymptotic assertion.

Also, with I_v=integral_0^1v=a*log(2/pi), smooth trapezoid and
v(0)=0, v(1)=-a show

    (1/m)*sum_(r<m)w(r/m)
        =a*(log m+gamma)+I_v+O(m^-2).                (18)

The 1/m terms cancel between a*H_(m-1) and the v endpoint correction.
Combining (14)--(18), and retaining the separate logarithmic harmonic
sum before cancellation, yields a real constant C_M with

    M_m=(a/2)*(log m)^2+a*c*log m+C_M
                           -(pi+a*c1)/(2m)+O(log(m)/m^2). (19)

In particular the log(m)/m terms in the singular sum cancel exactly:
the term -a*log(m)/(2m) from sum log(r)/r cancels the corresponding
endpoint term of -a*log(m)*H_(m-1). The remaining 1/m coefficient is
-(a*c0+R(0)+R(1))/2=-(pi+a*c1)/2.

Substitute (19) and (6) into (13). Since c1+S_u=2log2 and 4/pi=2a,
the resulting coefficient is

    -(2/pi)*[pi+a*c1+a*gamma+I1+I2+a*S_u]
       =-2-a^2*(gamma+2log2)-a*(I1+I2).

The logarithmic first correction in (13) is -a^2*log(m)/m; it remains
separate from the constant beta_H. The constant independent of m absorbs
4(C_M+a*S_e)/pi-a^2*c^2. This proves the candidate supporting expansion
(1), with every stated
remainder established uniformly over all integers.

## 5. Exact first-correction integral cancellation for parent assembly

Let I_B=integral_0^1 x*w(x)*B(x) dx, as in H04. Then

    2*I_B-a*I1=a^2-1+a^2*log(pi/2).                  (20)

To prove this without separating divergent integrals, first integrate
over [epsilon,1]. Double-angle gives cot(pi*x)=(w-1/w)/2, so the
combined integrand on the left of (20) is exactly

    x*(w^2-1)-2a*w+a^2/x.

Since w'=-(1+w^2)/a, its integral is

    a*epsilon*w(epsilon)-1+epsilon^2
                       +a^2*log(sin(pi*epsilon/2)/epsilon).

The combined integrand is integrable at both endpoints. Let epsilon
tend to zero to obtain (20). This checks every sign and endpoint term.

H04's separate theorem gives

    4V_n/(n*m)=C_B+beta_B/n+O(n^-2),
    beta_B=-a^2+2*I_B+a*I2.                          (21)

Because beta_B is constant, replacing beta_B/n by beta_B/m costs only
O(m^-2). Combining (1), (2), (20), (21) gives the candidate full form

    Lambda_c=A_m^2+C- [1+a^2*c+a^2*log m]/m
                                  +O(log(m)/m^2).    (22)

The +2/m in the EXACT base -1+2/m is essential to (22). By accepted
PD-T269/270, Lambda_c-A_m^2 tends to kappa, so C=kappa. Finally, for
N=n+1/2=m-1/2,

    A_N^2=A_m^2-a*A_m/m+O(log(m)/m^2),
    1/N=1/m+O(m^-2),

which converts (22) to the original requested
Lambda_c=A_N^2+kappa-1/N+O(log(N)/N^2).
This assembly is submitted to the parent for integration and independent
checking; no full-target adoption or registry status change is made here.

## Checks, scope and open items

PAPER only: no script, finite-degree, numerical/scalar, endpoint,
quadrature, native, compiler, source/import or fitting job occurred.
No actual O(n) finite evaluator was derived. No signed full-row substitute,
argmax theorem or fitted asymptotic coefficient is used. Parity has not
entered any step because all sums use every r=1,...,m-1 directly.

Distinct reconstruction of the aggregate coefficients and remainders is
requested; H04 and H05 maintain their own supporting proofs. The parent
must preserve their exact dependency scopes and the accepted kappa
identification before promoting the original sharp target.

## History

2026-11-07, rules/input 2c69ba538473b8fdd9147635256289f74e75ccbb.
Parent-assigned mathematical developer, inherited serving model/effort
metadata not independently exposed. Candidate/separation/kill record was
written after RELEASEH01 and before derivation. H01 only, owned prose
files only; no shared log, registry, Git or subagent action.

Before the candidate was frozen for distinct review, H06 identified that
the first displayed statement had omitted -a^2*log(m)/m although (13)
and (22) retained it. The displayed statement (1) and its final deduction
were corrected before the review hash. This is a material pre-audit
statement correction; no earlier acceptance is claimed.

## Dated status addendum — 2026-11-08 (Claude audit-03 MINOR fix H-C01)

The words "OPEN during development / not yet adopted" in the status line
above describe the state at first freeze and are historical. The enclosing
theorem [H-sharp-corner-expansion](H-sharp-corner-expansion.md) is PROVED,
and this file's aggregate analysis was accepted without conditions by the
distinct reviews [independent-checks-H-main.md](../independent-checks-H-main.md) and
[independent-checks-H-support.md](../independent-checks-H-support.md). The
Claude audit that reconstructed it independently, with high-precision
numerical corroboration, is [audit-03](../audit-03.md). No statement,
constant or proof text above changed.
