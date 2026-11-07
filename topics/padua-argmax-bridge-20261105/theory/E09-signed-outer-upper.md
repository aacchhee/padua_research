# PD-T?argmax-bridge-codex-E09 — A signed finite outer coefficient and a cheaper complete upper

Aliases: monotone actual-mesh coefficient; quotient-cancelled pole error;
restricted axis outer upper. Status: **PROVED**, developer PAPER theorem;
distinct audit/root adoption required. Split from: supporting signed outer/
log part of the OPEN full D13 remainder. Split into: none.

## Statement and precise limitation

For every integer n>=32 set m=n+1,L=log n,h=pi/m. On the CLOSED near
diamond alpha,beta>=0,rho=alpha+beta<=1/2, put

    a=(cos alpha+cos beta)/2, p=sin alpha,q=sin beta,
    d=(q-p)_+, t=beta/pi,
    T_n=Eout(alpha,beta)-aEout(0)+(d/pi)Rlog.          (1)

Eout and Rlog are LITERALLY the accepted E02/E03/D07 operators, with the
same original rows, weights, offsets and finite degree. Then

    T_n <=(rho/n)[(23/3)L+47]+(beta/n^2)[17L+27]
         <=(rho/n)[(33/4)L+48].                     (2)

Unlike the previous absolute outer estimate, this upper discards an
EXACTLY nonpositive paired log-n coefficient, proved below at every finite
degree. It also removes the pole estimate's initial rho log m cost.
Every remaining cancellation, scalar-log, endpoint-hole and Shift charge
is still present. Signed phases use the inherited separate absolute-phase
convention, without exchanging n and m.

There is also a restricted logarithm-free upper for THIS
component:

    T_n(alpha,0)<=32alpha/n,
    n>=32, 0<=alpha<=pi/[2(n+1)].                   (3)

The desired fixed-near family C*rho/n+K*(1+log n)*rho^2/n remains
**OPEN**. Formula(2) retains logarithmic linear growth and is not relabeled
as that family. Formula(3) concerns only the stated shrinking axis interval.
Neither result removes the COMPLETE error's real ell_n|alpha| cusp.
No new global argmax onset or physical cover is asserted.

## 1. Literal operator, exact masks and dependencies

For0<=tau<=1 use

    Q_tau[G]=(1/m)sum_(k=2)^(m-2)G(h(k+tau))
                                  -(1/pi)integral_0^pi G(z)dz. (4)

The original removed polynomial labels are
{0,1,2m-2,2m-1,m-1,m}. The centered-cell initial holes are
h(3/2+t),h(5/2-t), total4h; central holes are h(3/2-t),h(1/2+t),
total2h. None is removed, shifted or replaced. The primitive still uses
the original endpoint weights, actual polynomial collision values,
unequal n,m parity meshes and highest first-coordinate coefficient ONE.

Let f(x)=Phi_0(1/2+x/(2pi)), e=rho,delta=alpha-beta,
ce=cos(e/2),cd=cos(delta/2),a=ce*cd, and

    N_L=ce f(z+delta)+cd f(z-e),
    N_R=ce f(z-delta)+cd f(z+e), N0=2f(z),
    V_s=N_s-aN0, V0=V_L(0)=V_R(0),
    d0(z)=1/[2sin(z/2)]-1/z,
    P_s=[V_s(z)-V0]/z+V_s(z)d0(z).

Let I_s denote the exact generic cancellation integral evaluated at the
actual D25 coefficients C(v)=(p-q-2a cot(v/2))/4 and
D(v)=(p+q+2a cot(v/2))/4, with v_L=z,v_R=2pi-z. Set

    C_s=I_s(phi,z)-aI_s(0,z)-d log(pi-z).

D25/E02/E03 give the EXACT decomposition

    T_n=L{Q_t[g_L]+Q_(1-t)[g_R]}
         +Q_t[P_L]+Q_(1-t)[P_R]
         +Q_t[C_L/pi]+Q_(1-t)[C_R/pi]
         +Shift+(d/pi)Rlog,                         (5)

where, writing Z(z)=2a cot(z/2),

    pi*g_L=max(q,p-Z),
    pi*g_R=max(-q,p-Z,q-2Z).                        (6)

The exact common-log equality remains
Rlog=(Q_t+Q_(1-t))[log(pi-z)]. Thus(5) can equivalently recombine C_s
with d log(pi-z) inside the same Q operators. Our final estimate keeps
their existing separate absolute allowances, explicitly and conservatively.

For clarity the fixed-origin shift in(5) is the literal finite sum

    Shift=(a/m)sum_(k=2)^(m-2)
      [F0(h(k+t))+F0(h(k+1-t))-F0(hk)-F0(h(k+1))],
    F0(z)=(L/pi)[2cot(z/2)-4/z]
       +[2f(z)-2f(0)]/z+2f(z)d0(z)
       +[2cot(z/2)log(sin z)-4log z/z]/pi.

Every shifted F0 sample stays on its accepted smooth open-period domain.

Trusted dependencies: accepted D25's exact max/pole/cancellation formulas
and FULL cancellation charge; E02's paired Shift; D07's complete log-mesh
bound; C04's distributional semiconcavity including negative atoms; C08's
range0<f<=1; accepted E07's endpoint-cancelled integral; and accepted E06
axis convex-root/signed-first-cell estimate, used ONLY for(3). The E03
absolute obstruction and complete-cusp theorem retain their exact scopes.
E08 phase-global bounds are comparison context, not premises. No scalar,
numerical or new special-function enclosure is used.

## 2. The entire log-n coefficient is nonpositive at finite degree

Define

    v_L=g_L-q/pi=(p-q-Z)_+/pi,
    v_R=g_R+q/pi=max(0,p+q-Z,2q-2Z)/pi.             (7)

Both are continuous, nonnegative and nondecreasing in z on[0,pi], using
their endpoint limits, because Z decreases. All coefficient switches are
included by the literal maxima; no differentiability at a switch is needed.

For ANY nonnegative nondecreasing G on[0,pi] and0<=tau<=1,

    h sum_(k=2)^(m-2)G(h(k+tau))
       <=sum_(k=2)^(m-2)integral_(h(k+tau))^(h(k+tau+1))G(z)dz
       <=integral_0^pi G(z)dz.                     (8)

The intervals are disjoint and lie within[0,pi]: the final endpoint is
h(m-1+tau)<=pi. Thus Q_tau[G]<=0. These right rectangles prove an
ordering of the EXACT sample/integral operator; they do not change its
actual centered-cell geometry or delete the previously retained holes.

Both meshes have exactly m-3 samples, so Q_tau[1]=-3/m independently
of tau. The opposite constants in (7) therefore cancel EXACTLY. It follows
from (7),(8) that

    Q_t[g_L]+Q_(1-t)[g_R]
             =Q_t[v_L]+Q_(1-t)[v_R]<=0.            (9)

Since L>=0, the first term in(5) is nonpositive. This is uniform in n and
phase, includes both axes and all max/root threshold positions, and does
not follow by exchanging the fixed-n and fixed-phase limits. It strengthens
the favorable-sign information in the old fixed-phase E03 asymptotic.

## 3. Two scalar bounds with the periodic atom retained

The accepted E07 integral reads, on the principal period,

    f(x)=f(0)cos(x/2)+2 integral_0^(1/2)
                     [cos(xt)-cos(x/2)]/cos(pi t)dt.

Its justified third derivative has numerator
t^3 sin(tx)-sin(x/2)/8, which vanishes at t=1/2. The t derivative
of that numerator has absolute value at most
3/4+pi/8<23/20 for|x|<=pi. Since cos(pi t)>=2(1/2-t), the mean
value theorem bounds the integral's quotient by23/40. Also0<f(0)<3/5.
Therefore the COMPLETE ordinary derivative obeys

    |f'''(x)|<3/40+23/40=13/20,  -pi<x<pi.        (10)

This estimate includes one-sided limits but asserts no classical third
derivative through a periodic cusp.

C04 proves, as a full periodic measure,

    mu=d f'<=(3/pi^2)dx.

Its total mass on the circle is zero, because f' is periodic and BV.
Thus the positive and negative Jordan masses agree, and

    Var_one_period(f')=|mu|(circle)
           =2mu_+(circle)<=12/pi<4.                 (11)

The negative derivative atom is included, not omitted. We also retain the
accepted bounds |f''|<1 on every open smooth period and Lip(f)<2 globally.

## 4. A full pole-pair allowance with no mesh logarithm

Set r=ce+cd-2a. The inherited elementary cosine estimate gives
0<=r<=(e^2+delta^2)/8<=rho^2/4. Using0<f<=1 and Lip(f)<2 gives

    |V_s(z)|<=2(|delta|+e)+r<=33rho/8.             (12)

At z=0, evenness, f'(0)=0 and |f''|<1 on[-1/2,1/2] give the stronger

    |V0|<=(delta^2+e^2)/2+r
          <=(5/8)(delta^2+e^2)<=5rho/8.            (13)

The last step uses rho<=1/2. On the initial half0<=z<=pi/2 all shifted
arguments remain in(-pi,pi), so ordinary smooth bounds apply. In particular

    |V_s'|<=|delta|+e+2r<=9rho/4,
    |V_s''|<=(13/20)(|delta|+e)+r<=57rho/40.       (14)

For the quotient in P_s, retain its derivative cancellation BEFORE taking
absolute values:

    d/dz[(V_s(z)-V0)/z]
       =[zV_s'(z)-V_s(z)+V0]/z^2
       =(1/z^2)integral_0^z u V_s''(u)du.

Its magnitude is at most57rho/80, including the continuous z=0 limit.
Its variation over the initial half is therefore at most
57pi*rho/160<=57rho/50, using pi<16/5. The accepted d0 is increasing,
0<=d0<=1/5. The product variation is bounded by

    Var(V_s*d0)<= (33rho/8)(1/5)
                     +(1/5)(9rho/4)(pi/2)<=309rho/200.

Consequently each side has

    Var_[0,pi/2](P_s)<=537rho/200,
    sup_[0,pi/2]|P_s|<=9rho/4+33rho/40=123rho/40. (15)

The old logarithm arose from bounding the quotient derivative's two terms
separately by O(rho/z). The exact integral in (14) removes that artificial
loss; it does not presume a missing full finite cancellation.

For the central half, use the measure translation estimate

    Var_I[f(.+b)-f(.)]<=|b| Var_one_period(f')<=4|b|,
                     I=[pi/2,pi], |b|<=1/2.

Its proof is Tonelli applied to d f' between each pair of arguments;
the expanded interval is shorter than a period. It is valid across the
actual derivative atom. The residual r*f contributes at most pi*r<=4r,
so

    Var_I V_s<=4(|delta|+e)+4r<=17rho/2.           (16)

Now use P_s=V_s/[2sin(z/2)]-V0/z. On I, the first weight has supremum
<=3/4 and variation<=1/4; the second has supremum<=2/3 and variation
<=1/3. Equations(12),(13),(16) give

    Var_I P_s <=[51/8+33/32+5/24]rho=731rho/96,
    sup_I|P_s|<=[99/32+5/12]rho=337rho/96.          (17)

Apply midpoint BV quadrature on the ACTUAL centered cells. Sum the two
variations with factor1/(2m); pay all initial holes of total4h with(15)
and all central holes of total2h with(17). The result is

    |Q_t[P_L]+Q_(1-t)[P_R]|
      <=(rho/m)[537/200+731/96+123/10+337/48]
       =(71089/2400)(rho/m)<=30rho/m.               (18)

Thus both the shifted meshes and every missing interval are included.
The bound is valid through periodic numerator cusps and polynomial
collision positions, using the same weighted profiles as the accepted
outer operator; it does not assign separate unweighted collision values.

## 5. Complete full-near upper, retaining all remaining charges

Use the unchanged accepted estimates

    |Q_t[C_L/pi]+Q_(1-t)[C_R/pi]|
                      <=rho[175/4+20log m]/(pi*m),
    |Rlog|<=[3log m+log2+2log pi+2]/m,
    |Shift|<=beta[17L+27]/m^2.                       (19)

The first includes the no-root alternative, all moving-root and
coalescing-parameter transitions, and the integrable envelopes for BOTH
initial and central holes. The second is the full scalar-log allowance
on the SAME ordinary grids. The third retains the exact paired F0 shift.
Here d<=rho. Combining (5),(9),(18),(19) proves the explicit complete upper

    T_n <=(rho/m){30+
        [23log m+175/4+log2+2log pi+2]/pi}
            +beta[17L+27]/m^2.                     (20)

For the first simplified bound in(2), use pi>3,log2<7/10,
log pi<23/20 and log m<=L+1/32. The braces are less than

    (23/3)L+30+65/4+23/96
       =(23/3)L+4463/96 <(23/3)L+47.

Replace m by n in the positive denominators. For the second bound use
beta<=rho and n>=32:

    23/3+17/32=787/96<33/4,
    47+27/32<48.

This proves(2), with literal zero at rho=0. The coefficients are explicit
and no unknown phase maximum or inverse small phase occurs. The old
absolute theorem remains valid; (2) is a new ONE-SIDED upper for T itself.
Both displayed right sides of(2) are positive and decreasing in real
n>=32 at each fixed nonzero phase. For(cL+b)/n the derivative numerator
is c-cL-b<0 here; for(17L+27)/n^2 it is17-2(17L+27)<0. At the origin
the right sides vanish identically. This is an allowance monotonicity,
not an evaluation or a new degree threshold.

## 6. A closed shrinking-axis case of the no-log upper

Set beta=0 and0<=alpha<=h/2. Since n>=32, alpha<2/5, so the accepted
E06 convex-root theorem applies. Here Shift=d=0. The cancellation
difference vanishes on the initial half. On the central half set

    E(e)=J(p/2,a tan(e/2),e)-2a tan(e/2)log(sin e).

It is exactly the SAME signed root excess as E05/E06. Extend it by zero
past its outer root threshold e*<pi/4, keeping its SIGNED inner0<e<alpha
part. E06 proves

    h sum_(s>=1)E(sh)-integral_0^infinity E(e)de
                                            <=alpha^2 log2. (21)

All cells centered at sh lie beyond alpha and are in its convex positive
outer regime; the bound preserves the signed missing inner integral.

The ACTUAL ordinary samples in (4), after e=pi-z, are s=2,...,m-2
on the left and s=1,...,m-3 on the right. Since E vanishes well before
those upper endpoints, their exact combined cancellation operator is

    Q_0[E(pi-.)/pi]+Q_1[E(pi-.)/pi]
      =(2/pi^2){h sum_(s>=1)E(sh)-integral_0^infinity E}
                                               -E(h)/(pi*m). (22)

This retains the single weight at s=1. Because h>alpha, E(h)>=0, so
the final term is favorable. Equations(21),(22) bound the cancellation
contribution by2alpha^2 log2/pi^2. Apply(9),(18) and alpha<=pi/(2m):

    T_n(alpha,0)<=30alpha/m+2alpha^2 log2/pi^2
                <=[30+log2/pi]alpha/m<=32alpha/n.

At alpha=0 all terms vanish, giving(3) with a non-strict inequality.
No finite background, retained row, central cusp or actual-origin residual
has been added to T in this proof. Those belong to the complete error.

## Remaining obligation and execution record

The fixed-near mixed target remains OPEN because (19) still pays a
logarithmic linear cancellation/log allowance. Neither the exact negative
coefficient nor (3) bounds that remainder uniformly beyond the first
convex-cell regime. The next paper task is to pair the central entropy/
moving-root profiles with their actual omitted cells for alpha>h/2 and
nonzero beta, retaining the same-sign inner integral. The earlier absolute
obstruction does not refute this one-sided task. No positive obstruction
to it is claimed here.

For the COMPLETE remainder, the unchanged true-origin conversion remains
E(phi)-E(0)=delta_a E-uE(0)<=delta_a E+uE0. This scalar origin charge,
ordinary/retained errors and the genuine finite ell_n|alpha| cusp are not
deleted or charged to another component by (2) or (3).

Requested Astra ultra, serving metadata unexposed. New bounded PAPER
block2026-11-07 01:14:17–01:34:17 UTC, prospectively justified in root LOG.
The exact gate and dispositions are in the owned idea/attempt. No source,
script/import, numerical/scalar/endpoint/native/pack job, Git operation,
shared mutation or extra agent. Only the three E09 prose files were changed.
Independent review and root adoption are separate; no onset is asserted.


## Root mathematical adoption in WORK —2026-11-07

Root adopts the exact14274B frozen mathematical proof above (SHA256850a7d4020a68e9c7d9cc5da3b1a7987bbc36fce7600469b415761109ca28183) after distinct [E09 mathematical ACCEPT](../independent-checks-E09-signed-outer.md), report18402B2c2efa0fb443c632b8f8c892d63c11e82b646d742e6d3f99e67d6c16246c6e41. Full half-diamond47/48 constants, exact nonpositive coefficient/pole bound and restricted-axis32alpha/n are adopted. Original prefix remains unchanged. The exact T operator includes the scalar-log term; it does not bound those components separately or remove any ordinary/retained/origin cost.

The report separately preserves unwaived MAJOR protocolP1, canonically disclosed in the [attempt](../attempts/E09-signed-outer-upper.md). Mathematical adoption in WORK is neither a waiver nor PR readiness. The stronger fixed-near mixed upper and fullD13 remain OPEN. No numerical/source job or onset follows without a complete matched assembly and distinct review.
