# PD-T?argmax-bridge-E06-axis-boundary — A signed first boundary and complete first-root limit

ID kind: PD-T. Aliases: convex central excess; fixed-sign cosine background;
complete cusp-subtracted first-active-row limit.
Split from: E05's OPEN cusp-aware full alpha-axis upper. Split into: none.
The finite root comparison and background estimates support this one
restricted-axis continuation; they do not make full D13 PARTIAL.

## Statement

Let n>=2,m=n+1,h=pi/m, beta=0, 0<=alpha<=min(2/5,h/2), and use
the EXACT E05 transported excesses Y_r, fixed-sign background B_n,
ell_n=(nm)^-1 sum_(k=1)^floor(n/2)cot(k*pi/n), and signed model E_c.
Then the COMPLETE central positive-excess comparison obeys the FINITE
one-sided estimate

    (4/(nm))sum_(r=1)^(m-1)Y_r(alpha)-E_c(alpha,0)<=2alpha². (1)

No separate absolute theta E(k0h) charge is used. For n>=10^6 the
COMPLETE actual-origin error E_n=S_n-M_infty consequently satisfies

    E_n(alpha,0)-E_n(0)<=ell_n sin(alpha)+32H² alpha²,
    H=1+log n.                                           (2)

This is a weaker finite family than the desired C alpha/n+K H alpha²/n
remainder. The degree floor in(2) is solely an inherited supremum bound;
it asserts no new global argmax onset.

In particular the COMPLETE cusp-aware finite inequality

    E_n(alpha,0)-E_n(0)<=ell_n sin(alpha)+alpha/n          (2a)

holds for every n>=10^6 on the CLOSED axis interval
0<=alpha<=1/(32nH²). This interval lies inside the domain of(2), and
32H²alpha²<=alpha/n there. It is a shrinking parameter case, not the
full fixed-near target or a new global degree threshold.

There is also a complete first-active-root limit. Put

    A(x)=integral_x^1 sqrt(1-z²)/z dz for0<x<1,
    A(x)=0 for x>=1,
    I4=integral_0^1 sqrt(1-y^4)dy,
    Psi(c)=(2c/pi²)[sum_(s>=1)A(s²/c)-2sqrt(c)I4], c>0.   (3)

The displayed sum is finite. For EVERY compact interval
0<c0<=c<=c1<infinity, set alpha_n(c)=c h². Uniformly on that interval,

    [E_n(alpha_n(c),0)-E_n(0)-ell_n sin(alpha_n(c))]/h³
                                          -->Psi(c)<0.   (4)

Every threshold c=s² and both degree parities are included. No fixed-n
derivative or fixed-positive-alpha asymptotic is exchanged with this limit.
There is no explicit onset or whole-near-diamond assertion. The stronger
complete cusp-aware axis target and full D13 remain **OPEN**.

Overall status of(1)--(4): **PROVED**, paper developer theorem, distinct
audit needed. The strict negative sign concerns this coupled shrinking
scale after the REAL cusp is retained; it is not a negative theorem.

## Exact objects and dependencies

Use E05's literal finite kernel D_n-cos(nu), exceptional top mode ONE,
actual n,n+1 parity meshes and polynomial collision values. For folded
1<=r<m, u_rk^0=(delta_r*pi+2k*pi)/n, u_rk=u_rk^0+alpha/n,
v_r=r*pi/m, delta_r=(1-r)mod2, set

    F_rk=(-1)^delta_r [D_n(u_rk,v_r)-cos(nu_rk)]/2,
    sigma_rk=sign F_rk(0),
    B_r=-sum_(cos u_rk^0<cos v_r)F_rk,
    Y_r=sum_k(-sigma_rk F_rk)_+,
    B_n=1+(2n/m)a+(4/(nm))sum_r B_r, a=(1+cos alpha)/2.

Every original fixed-six label is in this exact full primitive. None is
deleted or replaced by a regularized collision row. E05 proves

    S_n=B_n+ell_n p+Rcen+(4/(nm))sum_r Y_r,
    p=sin alpha, 0<=Rcen<=alpha²/(3m), B_n(0)=S_n(0).      (5)

Its natural denominator/root split has opposite finite jumps at
alpha=pi-v_r; Y transports the crossed original j=r-1 sample. We keep
that definition. On the domain alpha<=h/2 no such denominator crossing
occurs because every noncentral e_s=s h>=h; numerator roots still move.

For u=p/2,s(e)=a tan(e/2), use the SAME N1/C01 cancellation integral J and

    E(e)=J(u,s(e),e)-2s(e)log(sin e),
    E_c(alpha,0)=(2/pi²)integral_0^(pi/2)E(e)de,
    M_nc=M_infty-E_c.

The inner e<alpha integral is SIGNED and retained. The exact full-error
identity is

    E_n(alpha,0)-E_n(0)-ell_n p
      =B_n(alpha)-B_n(0)-M_nc(alpha)+M_nc(0)
                   +Rcen+(4/(nm))sum_rY_r-E_c.            (6)

Dependencies: accepted PD-T220/226 and E05 axis decomposition (distinct
D29 report eccd2cfd...); C01 central/axis root formulas and scaling;
D10 exact completed constant and local fourth-derivative estimate;
N1 periodic derivative-variation bounds; C08 pole functional;
PD-T227's locally proved endpoint polynomial functional;
C06 full-diamond primitive upper. No new scalar-H shape/maximization
claim or unreviewed E06 helper theorem is assumed. No external theorem,
numerical premise or priority claim. Gate/limits are in the idea record.

## Proof

### 1. The outer root profile is convex before any cell estimate

Fix alpha>0. On e>alpha, s>u and C01 gives E(e)>=0, decreasing in e;
it vanishes for e>=e*=arccos(1-tan(alpha/2)). Here e*<pi/4: indeed
tan(alpha/2)<=8alpha/15<=16/75<1/4, while cos(pi/4)<3/4.
On the nonzero open strip define

    D=sqrt(u²-s²sin²e), q=D/(s cos e), 0<q<1.

N1's EXACT root derivatives give E_s=-2atanh q and E_e at fixed s
equal to -2D/sin e. Along the actual s(e),

    E'=-2s'atanh q-2D/sin e,
    E''=-2s''atanh q-2s'q'/(1-q²)
                         -2D'/sin e+2D cos e/sin²e.      (7)

Both last terms are nonnegative: D'<0 and cos e>0. Moreover

    s'q=D/(sin e cos e).

The numerator decreases and the denominator increases on e<e*<pi/4.
Thus (s'q)'<=0, or -s'q'>=s''q. Since s''>=0 and
atanh q<=q/(1-q²), the first two terms of E'' are nonnegative together.
Hence E''>=0. At e* its left derivative tends to0, so extension by zero
preserves convexity. Continuity at e=alpha gives a finite convex function
on[alpha,infinity); its one-sided slope at alpha may be infinite. No
smoothness through that parameter singularity is asserted.

### 2. Keep the signed missing inner interval

When alpha<=h/2, each actual positive row center e_s=s h has centered
cell[(s-1/2)h,(s+1/2)h] inside[alpha,infinity). Convexity therefore gives

    h sum_(s>=1)E(s h)<=integral_(h/2)^infinity E(e)de.     (8)

Only finitely many samples/integrals are nonzero; zero extension beyond
e* adds no fictitious physical row. The inner SAME-SIGN entropy formula
gives J(u,s,e)>=-2u log2=-p log2 for0<e<alpha. Since the subtracted
baseline is nonpositive, E(e)>=-p log2 there. On alpha<=e<h/2 it is
nonnegative. Subtract the FULL signed integral from(8):

    h sum_sE(sh)-integral_0^infinity E
       <=-integral_0^(h/2)E<=p alpha log2<=alpha² log2.   (9)

This is the first-cell cancellation that a separate theta E(k0h) upper
does not preserve. The signed inner integral has not been replaced by a
positive majorant or dropped.

### 3. Retain the actual first-coordinate error

Here alpha<h, so every nonempty transported row lies in E05's OUTER
strip alpha<e_s<e*. There are no inner grid rows. Its density K_e obeys
the literal actual-u-grid BV estimate

    |n^-1 sum_kK_e(u_rk)-(2pi)^-1 E(e)|
                                      <=(6/5)alpha²/(n e²).

The coefficient4/m and sum_(s>=1)s^-2<2, m/n<=3/2 give the refined bound

    |(4/(nm))sum_rY_r-(2/(pi*m))sum_sE(sh)|
       <=[48m/(5pi²n)]alpha²<=(8/5)alpha².              (10)

The actual parity and displaced first-coordinate cells remain inside
this estimate. Combine(9),(10), and E_c=(2/pi²)integral E. Since
8/5+2log2/pi²<8/5+2/9<2, this proves(1), including alpha=0.

### 4. Bound the SIGNED background without an n-sized Taylor estimate

The background B_n is a fixed-sign finite polynomial sum: take sign -1
on row0, sign +1 on row m, and the origin signs on every other row.
Reflecting j to -j preserves those signs. Thus B_n is an EVEN
trigonometric polynomial in theta=alpha/n of degree<=n, and

    B_n(alpha)=P_n(cos(alpha/n))

for an algebraic polynomial of degree<=n. At every real theta its absolute
value is at most S_n(n theta,0). The latter is2pi-periodic in its phase
(shift j by2), so C06's full-domain bound implies, for n>=10^6,

    ||P_n||_[-1,1]<=3H².                                (11)

Indeed C06 gives sup S<=L²/2+3L+200, and L>10 implies this is<3H².
The inequality L>10 follows already from e<3 and3^10<10^6.

PD-T227 proves locally, by the Lobatto endpoint functional, that
|P_n^(j)(1)|<=n^(2j)||P_n|| for1<=j<=n. Taylor at1 and
n²[1-cos(alpha/n)]<=alpha²/2 yield

    |B_n(alpha)-B_n(0)|
       <=3H²[exp(alpha²/2)-1]<=3H²alpha².                (12)

No new global Markov/Bernstein theorem is imported, and no fixed-sign
claim about the displaced primitive is needed: only the background
polynomial has fixed coefficients.

For completeness the exact smooth noncentral model obeys

    |M_nc(alpha)-M_nc(0)|<=20H²alpha².                   (13)

Here are sufficient elementary details, independent of a new H shape
conjecture. From a=(1+cos alpha)/2,
|Delta B0|<=alpha²/9. U0=2cos(alpha/2)f(alpha), f(0)<=1 and |f''|<=1
near0 give |Delta U0|<=5alpha²/4. The exact C06 b_full identity, together
with -a loga<=1-a and log2<1, gives |Delta b_full|<=25alpha²/18.

The exact C_nc=C_infty-E_c is E_infty+2cos(alpha/2)Hfun(alpha)-c_const*a.
D10 gives its upper increment<=19alpha²/24. A lower bound>=-19alpha²
follows directly from the same accepted functional: write D_xf(v) for its
second difference. D10 gives |D_xf(v)-D_xf(0)|<=(9/4)x²v² for v<=1/2;
N1 gives integral_period|D_xf(v)|<=7x²; and0<=D_xf(0)<=x².
In the paired Hfun formula the constant coefficient is favorable for a
lower bound. K(v)<=pi/(2v) gives the near cost9x²/64. On v>=1/2,
K<=pi and integral K<3, giving costs7x² and x². Thus
Hfun(x)-Hfun(0)>=-9x². C08 proves0<Hfun(0)<1/2, so the two cosine
weighted terms cost at most(145/8)alpha². E_infty>=aE_infty(0) and
E_infty(0)<3 add at most3alpha²/4; -c_const*a is favorable. Their sum
is151alpha²/8<19alpha². This proves the two-sided C_nc bound and(13)
from its explicit logarithmic coefficients. None of these is a global
Hfun maximum/shape assertion beyond already accepted premises.

Insert(1),(12),(13) and Rcen<=alpha²/(3m) into the exact identity(6).
The coefficient is <=23H²+2+1/(3m)<32H², proving(2).

### 5. The complete first-active-root limit, with one coupled scale

Fix0<c0<=c<=c1<infinity and set alpha=c h² throughout the argument.
For sufficiently small h, alpha<h/2 uniformly in c. Equations(12),(13)
show the full background difference is O_c1(H²h^4)=o(h³), uniformly.
Rcen=O_c1(h^5), and the ABSOLUTE error(10) is O_c1(h^4). Consequently
the limit in(4) is exactly the limit of

    (2/pi²)h^-3[h sum_sE_alpha(s h)-integral_0^infinity E_alpha(e)de]. (14)

This step retains the complete model, not merely one cancellation channel.
The signed inner entropy region is still inside the integral in(14).

For e>=2alpha, C01's exact positive-root formula is

    E_alpha(e)=p integral_x^1 sqrt(1-z²)/[z sqrt(1-lambda²z²)]dz,
    x=(1-cos e)/tau, lambda=tau/tan(e/2),

with value0 when x>=1. On the finite grid e=s h, x->s²/c,
lambda->0, p/h²->c, uniformly for c in the compact interval and each
fixed positive integer s. Therefore

    h^-2 E_alpha(s h)->c A(s²/c).                        (15)

Only finitely many s can be active, uniformly: sine chords imply
1-cos(sh)>=2s²h²/pi² while tau<=8c1h²/15; hence s²<3c1.
The integral defining A is continuous at x=1 with value0. Its lower
argument for each such s is bounded away from0 uniformly in c, so the
convergence in(15), including every threshold c=s², is uniform. Summing
this bounded finite set proves uniform convergence of the sum in(14).

For the FULL integral, C01's proved scalar scaling gives

    alpha^(-3/2)integral_0^infinity E_alpha(e)de ->2I4.    (16)

Its proof splits0<e<2alpha, whose absolute contribution is
O(alpha²[1+log(1/alpha)]), then sets e=sqrt(alpha)y. The remaining
integrand converges to A(y²) and is bounded by a constant times
log(6/y²) on0<y<sqrt3, zero beyond; this is integrable. Thus(16)
includes the SIGNED inner strip. Since it is a scalar alpha-down-to-zero
limit, substitution alpha=c h² is uniform on[c0,c1]. Equations(15),(16)
in(14) prove the explicit uniform limit(3),(4).

Finally x->A(x²/c) is nonnegative, integrable, strictly decreasing where
positive, and zero for x>=sqrt c. Its integral is2sqrt(c)I4, by Tonelli
or the same C01 integration by parts. The right rectangles of width1
therefore satisfy

    sum_(s>=1)A(s²/c)<integral_0^infinity A(x²/c)dx
                                             =2sqrt(c)I4.

The strict sign already follows on the first nonempty interval. This
proves Psi(c)<0 for every c>0 without evaluating a scalar integral.

## Limits, remaining obligation and checks

Finite(1) controls the central comparison up to alpha=h/2 and resolves
its first centered boundary with sign. The background remains too coarse
to prove the sharper fixed-near C alpha/n+K H alpha²/n family; (2) records
the actual weaker complete envelope instead. The region alpha>h/2,
especially actual transported inner rows at alpha~h, remains OPEN.
Natural denominator/root jumps must still cancel there before estimates.
No global convexity through e=alpha, arbitrary collision deletion, finite
degree threshold or global argmax improvement is inferred from(4).

Actual-origin subtraction in(6) uses S_n(0),M_infty(0) at the SAME degree.
For delta_a E the separate conversion remains -uE(0), safely bounded by
+uE0 with |E(0)|<=E0; no such allowance is silently removed.

Paper only: bounded complete read/search/hash metadata and written
inequalities; only the three assigned E06 prose records. No script/source/
scientific import/scalar/endpoint/native/threshold/phase/degree/compile/
pack/shared/Git action. E05 files remain frozen for their audit. Distinct
review/root adoption required; no onset/coverage change. 2026-11-07,
requested Sol xhigh, actual serving metadata unavailable; root controls
shared IDs, publication and any later release.


## Root adoption —2026-11-07

Root adopts the exact frozen13759B proof above (SHA256 cfd6275bece17c3347cbe3ed35237047fc035ece9dda2b5061851000de89dbe6), after distinct [E06 axis ACCEPT](../independent-checks-E06-axis.md), report e7b503c1aea3eaefeec5b62a817a1e2e41c34d2e0538a6a60ce914eb3772e84e. All three exact scoped statements are adopted, including uniformcompactc first-root negativity; full fixed-near/D13 and any onset remain outside their scope. Original prefix is preserved. Final Claude audit remains separate. No numerical job occurred.
