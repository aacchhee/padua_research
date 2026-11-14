# PD-T?argmax-bridge-codex-D35-ordinary — Sharper ordinary cancellation perturbation

ID kind: PD-T. Aliases: two-support-interval variation; sign-stable
symmetric-reference difference. Split from: D35 lower ordinary-row
coefficient target. Split into: the complete near allowance is a separate
application. This quantitatively strengthens D03; its old proof is unchanged.

## Statement and definitions

Let v be real, v not in pi*Z, e=dist(v,pi*Z) in (0,pi/2]. For real
w,c,d and E>=0 with |c|,|d|<=E define on R/(pi*Z)

    g(C,D,v;x)=|C cot x+D cot(x+v)|-|C cot x|-|D cot(x+v)|,
    f(x)=g(-w+c,w+d,v;x)-g(-w,w,v;x).

Give both g functions value zero at either cotangent pole. Then

    Var_per(f)<=24E/|sin v|.                              (1)

For every integer n>=1 and every shifted n-point mesh x_k=x0+k*pi/n
avoiding both poles,

    |sum_k f(x_k)-(n/pi) integral_0^pi f(x)dx|
                         <=12E/|sin v|.                  (2)

No coefficient-sign assumption, root separation, or lower bound on |w|
is made in (1)-(2). The statement includes roots coinciding with sampled
points, derivative zeros, double roots, and coefficient sign changes.

For every integer n>=2, m=n+1, 2<=R<=n, alpha,beta>=0 with
alpha+beta<=pi, put

    a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta, P=p+q,
    w(v)=a cot(v/2)/2,
    C(v)=-w(v)+(p-q)/4, D(v)=w(v)+(p+q)/4,
    delta_r=(1-r) mod2,
    u_rk=(delta_r*pi+alpha+2k*pi)/n,
    v_r=(r*pi+beta)/m, x_rk=(u_rk-v_r)/2.

Use exactly D03/N1's A_R: the first R and last R row labels, m-1,m,
and every actual polynomial-collision row. A collision means
u_rk-v_r or u_rk+v_r belongs to 2pi*Z. Let O be ANY subset of its
complement. Define the actual cancellation quadrature errors

    T_r=sum_k g(C(v_r),D(v_r),v_r;x_rk)
                          -(n/pi) integral_0^pi g(C(v_r),D(v_r),v_r;x)dx,
    T0_r=sum_k g(-w(v_r),w(v_r),v_r;x_rk)
                          -(n/pi) integral_0^pi g(-w(v_r),w(v_r),v_r;x)dx.

Then, with H_n=sum_(j=1)^n 1/j,

    |(nm)^(-1) sum_(r in O)(T_r-T0_r)|<=6P H_n/n.         (3)

The old D03 coefficient 112/pi is therefore replaced by6, strictly
smaller since pi<4. Signed phases use separate absolute phases and the
established phase-even primitive convention, without exchanging n,m.

Overall status: **PROVED**, complete analytic developer proof below;
distinct independent review is required before adoption. No computation,
fit, external source theorem or new onset is a premise or conclusion.

## Dependencies and exact operator scope

N1-cancellation-quadrature supplies Var_per(g)<=8max(|C|,|D|)/|sin v|,
the centered-cell shifted BV inequality, the actual ordinary-row mesh,
and its sine-denominator sum. These are restated where used below.
D03 supplies the existing reference/operator definitions. The improved
variation count is proved here, not assumed from D03.

The actual corrected polynomial is

    D_n(u,v)=sum_(i+j<=n) h_i h_j cos(iu)cos(jv),
    h_0=1, h_i=2 (i>0), G_n=D_n-cos(nu),
    F_rk=(-1)^delta_r G_n(u_rk,v_r)/2.

On ordinary rows its exact identity is
F_rk=C(v_r)cot(x_rk)+D(v_r)cot(x_rk+v_r). The highest first-coordinate
correction is retained. Neither g0 nor a separately unweighted pole is
assigned a value for an actual polynomial collision. All such rows are
excluded in (3); complete-expression continuity is used only in the
separate fixed-row application.

## Proof of the universal variation bound

The case E=0 is immediate. Periodicity in v and reflection x ->-x reduce
to v=e in (0,pi/2]; the reflection preserves absolute values, variation,
and the coefficient-perturbation hypotheses. Put A=|w|.

If A<=E, the perturbed coefficients have magnitude at most A+E.
N1's full variation theorem, including all its pole jumps and roots,
and the triangle inequality give

    Var_per(f)<=8[(A+E)+A]/sin e<=24E/sin e.              (4)

This regime includes w=0 and every possible coefficient-sign switch.
It is not passed through the sign-preserved argument.

Suppose A>E. The reference and perturbed coefficient signs are opposite
and agree respectively. A simultaneous sign reversal leaves g unchanged,
so their magnitudes can be denoted b1,b2 in [A-E,A+E], both positive.
Write X=cot x, Y=cot(x+e). The cancellation identity gives

    f=-2[min(b1|X|,b2|Y|)-A min(|X|,|Y|)]

when X,Y have the same sign, and f=0 when they have opposite signs.
For 0<e<pi/2 the two support intervals in one period are precisely

    I1=(0,pi/2-e),       I2=(pi/2,pi-e).                 (5)

On I1, X>Y>0 and the reference selects Y. On I2, Y<X<0 and the
reference selects |X|. Consequently

    |f|<=2E min(|X|,|Y|)<=2E cot e=:M                 (6)

on both supports: on I1, Y decreases from cot e to0; on I2, |X|
increases from0 to cot e. Outside (5) the difference is zero. At e=pi/2
both support intervals are empty and f=0, which proves this case directly.
Thus below assume e<pi/2. Both pole one-sided limits are finite by (6).

### Count only the roots and stationary points actually needed

On the two supports a change of the selected perturbed branch requires
the numerator b1 cot x-b2 cot(x+e) to vanish. After multiplication by
sin x sin(x+e), this numerator is

    [(b1-b2)sin(2x+e)+(b1+b2)sin e]/2.                  (7)

It has at most TWO distinct zeros in a pi-period. It is not identically
zero because b1+b2>0 and sin e>0. Tangent roots only reduce this count.
No zeros outside the supports need to be added.

On I1, when the perturbed branch agrees with the reference branch,
f=-2(b2-A)Y, which is monotone or constant. On its other branch,

    f=-2b1 X+2A Y.

The derivative of this last fixed expression has at most ONE zero in
the ENTIRE interval I1: its equation is
[sin(x+e)/sin x]^2=A/b1, and the positive sine ratio has derivative
-sin e/sin^2 x<0. The same expression applies on every disconnected
piece where that branch is selected, so it does not receive one new
stationary point per piece.

On I2 the reference branch is |X|. On the agreeing branch f is a
constant multiple of X. On the other branch f=2b2 Y-2A X, whose
derivative has at most ONE zero in the ENTIRE I2 by the same sine-ratio
argument (both sines are positive on I2 as well).

Therefore, partition the supports at the roots in (7) and these at-most-
two stationary points. If N_i is the number of interior cuts in I_i,

    N1+N2<=4.                                          (8)

On each remaining piece f is monotone. No extra cut is required for a
flat agreeing branch, a double root, or a stationary point at a root.
The function is continuous at every finite branch crossing and cot zero.

### Charge the complete path and its pole jumps

Each support interval has one end at a cot zero, where f tends to0,
and its other end at a pole, with finite limit a_i satisfying |a_i|<=M.
The function is identically zero on the other side of that pole, and its
assigned pole value is zero. Thus the only pole jump for that interval
has size |a_i|. A path through N_i interior cut values in [-M,M],
from a_i to0 (or reversed), has variation at most

    |a_i|+2N_i M.

For N_i=0 this is the exact monotone bound |a_i|. For N_i>=1, bound the
first edge by |a_i|+M, the N_i-1 interior edges by2M each, and the last
edge by M. Adding the pole jump gives at most2(N_i+1)M. Hence (8) gives

    Var_per(f)<=2(N1+N2+2)M<=12M=24E cot e
                                         <=24E/sin e. (9)

All variation is inside these support paths and their two pole jumps;
the remaining arcs are zero. Together with (4), this proves (1).

## Shifted quadrature and the actual ordinary-row sum

For any pi-periodic BV function continuous at the n sample points,
center cells of length pi/n at those points. The centered-cell Stieltjes
kernel has absolute value at most1/2, including jumps inside a cell.
Summing the cells therefore bounds the sample-sum minus scaled integral
by Var_per/2. The only possible jumps of f are at the two poles, avoided
by hypothesis. Numerator roots are continuity points and may be sampled.
This proves (2), for every actual mesh shift and both parities.

In the Padua setting E=P/4 bounds both (p-q)/4 and (p+q)/4. Thus the
r-th quadrature difference is at most3P/|sin v_r|. For ordinary r let

    k_r=min(r,2m-r-1),
    l_r=m-r-1 (r<=m-2), or l_r=r-m (r>=m+1).

All are positive and at most n. The distances d0 to {0,2pi} and dpi
to pi obey d0>=pi*k_r/m and dpi>=pi*l_r/m. The sine chord bound gives

    1/|sin v_r| <=(pi/2)(1/d0+1/dpi)
                    <=(m/2)(1/k_r+1/l_r).

Each positive k or l occurs at most twice among ordinary rows. Therefore

    sum_(r outside A_R) 1/|sin v_r|<=2m H_n.

Restricting to O lowers this positive sum. Multiply by3P and divide
by nm to obtain (3). The actual mesh avoids both poles exactly because
collision rows were retained in A_R. Endpoint/central exclusions also
ensure v_r is not a multiple of pi. No row reindexing between n and m,
pairing of opposite beta phases, or missing endpoint removal is used. QED.

## Scope, checks and history

The result is linear in P and uniform even when |w| is arbitrarily small.
It does not assert a quadratic phase modulus, an n-independent root-free
central region, or cancellation between distinct shifted rows. The regime
switch A=E has a complete absolute allowance, so near-central roots and
coefficient degeneracies need no additional term. Any more refined paired
or quadratic estimate remains a separate OPEN route.

At the actual origin P=0, T_r-T0_r vanishes exactly. All other finite
reference, retained polynomial-row, weighted-pole, outer and mesh errors
remain part of a complete primitive comparison. A new global onset does
not follow from (3) alone. No scalar/native/root/quadrature/threshold job
was run. Gate/attempt: ../ideas/D35-ordinary-perturbation.md and
../attempts/D35-ordinary-perturbation.md. Written 2026-11-06 in the bounded
30min parent-assigned Astra-ultra paper block; serving metadata unexposed.


## Root review closure — 2026-11-06

Distinct adversarial [D35 review](../independent-checks-D35-ordinary.md), SHA256 `781e1077eb52c87e4f9f1718a0d658c3f8a342b0db3733c15c8ac1851c31083e`, accepts all three frozen scopes without unresolved findings. Root adopts the6PH_n/n ordinary perturbation, its fixed-row application and complete near allowance at their exact stated domains/exclusions. All pole jumps, roots, actual shifted-grid sampling and unchanged Cnear/uE0 charges were reconstructed. No new onset or numerical job follows from this support alone; D13 full relative remains OPEN. Reviewed prefix is preserved; final Claude audit is separate.
