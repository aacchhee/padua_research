# PD-T?argmax-bridge-E02-paired-outer — Pair the actual origin mesh shifts

ID kind: PD-T. Aliases: fixed-F0 paired translation; boundary plus disjoint
second differences; reduced regular-outer allowance.
Split from: supporting regular-outer part of D13's full joint remainder.
Split into: none. The variation calculation is a supporting step of this
single operator theorem, not a separate target or analytic round.

## Statement

Let integer n>=32, m=n+1, L=log n, h=pi/m, alpha,beta>=0 and
rho=alpha+beta<=1. Use EXACTLY D25/D37's regular-outer operator Eout,
including all of its missing intervals. Set a=(cos alpha+cos beta)/2.
Then, on the whole wide domain,

    |Eout(phi)-a Eout(0)|
       <= (rho/n)[14L+59]+(beta/n^2)[17L+27]             (1W)
       <= (rho/n)[(117/8)L+60].                         (2W)

On the restricted near domain rho<=1/2 the stronger bounds are

    |Eout(phi)-a Eout(0)|
       <= (rho/n)[(27/2)L+55]+(beta/n^2)[17L+27]         (1N)
       <= (rho/n)[(113/8)L+56].                         (2N)

The asymmetric beta factor is intentional: beta moves these actual meshes.
Signed phases use the inherited separate-absolute-phase convention, with
|beta| in its place. Both parities and both axes are included.

## Definitions and exact operator

Write e=rho, delta=alpha-beta, ce=cos(e/2), cd=cos(delta/2), a=ce cd,
p=sin alpha, q=sin beta, d=(q-p)_+, t=beta/pi. Let the unchanged weighted
periodic profile be f(x)=Phi0(1/2+x/(2pi)). In particular

    N_L=ce f(z+delta)+cd f(z-e),
    N_R=ce f(z-delta)+cd f(z+e), N0=2f(z),
    U0=N_L(0)=N_R(0), v_L=z, v_R=2pi-z,
    C(v)=(p-q-2a cot(v/2))/4,
    D(v)=(p+q+2a cot(v/2))/4,
    I(C,D,v)=integral_0^pi
       [|C cot x+D cot(x+v)|-|C cot x|-|D cot(x+v)|]dx,
    A(v)=2(|C(v)|+|D(v)|)/pi,
    F_s=L A(v_s)+N_s/(2sin(z/2))+I(C(v_s),D(v_s),v_s)/pi
           -[U0+(4a/pi)(L+log z)]/z-(d/pi)log(pi-z),
    Q_tau[g]=(1/m)sum_(k=2)^(m-2) g(h(k+tau))
                                      -(1/pi)integral_0^pi g(z)dz,
    Eout=Q_t[F_L]+Q_(1-t)[F_R].                         (3)

The ordinary bounded cancellation integral and weighted continuous Phi
values are unchanged. No separately unweighted pole is used. F's endpoint
conventions are the inherited integrable regularizations, not replacement
polynomial collision rows. At phase zero F_L=F_R=F0. The six original
removed polynomial labels are {0,1,2m-2,2m-1,m-1,m}. The original polynomial
kernel is D_n-cos(nu), with h0=1, hi=2 and exceptional top mode ONE.
The n and n+1 meshes, their parity and every endpoint numerator are exact.

The centered-cell initial holes are h(3/2+t),h(5/2-t), total4h;
the central holes are h(3/2-t),h(1/2+t), total2h. No new hole is introduced.
All retained cells lie in [h/2,pi-h/2].

## Assumptions, status and dependencies

Exact real arithmetic; no asymptotic premise or numerical input.
Overall status: **PROVED**, paper developer theorem; distinct audit needed.

| Part | Status | Evidence |
|---|---|---|
| Actual paired Shift bound and outer replacements (1)--(2) | PROVED | Finite regrouping and derivative-variation proof below |
| Full D13 joint vanishing remainder | OPEN | Its other complete increments and their cancellation are not proved here |

The OPEN original target is not made PARTIAL by this supporting result.
Dependencies: D25-outer-relative's exact (3), weighted profile bounds,
initial-half estimates, coefficient/cancellation charges and F0 derivative
estimate; D37-relative-wide's phase extension and endpoint estimate; D05/D07
operator/cells; N1 regularized-pole and round6 derivative bounds; PD-T270
equation(4), which proves |(cot x-1/x)''|<1 on[0,pi/2] locally.
The near pole improvement is rederived below from those dependencies, so
E01's separate protocol disposition is not a premise.

## Proof

### 1. Pair the finite operator before absolute values

Linearity gives the inherited exact identity, with W_s=F_s(phi)-aF0,

    Eout(phi)-aEout(0)=Q_t[W_L]+Q_(1-t)[W_R]+Shift,
    Shift=(a/m)sum_(k=2)^(m-2)
      [F0(h(k+t))+F0(h(k+1-t))-F0(hk)-F0(h(k+1))].       (4)

Put eta=ht=beta/m and x_j=hj. Regrouping this FINITE sum gives

    (m/a)Shift = F0(2h+eta)-F0(2h)
       +F0(pi-h-eta)-F0(pi-h)
       +sum_(j=3)^(m-2)[F0(x_j+eta)+F0(x_j-eta)-2F0(x_j)]. (5)

Equation(5) means its multiplied identity when a=0, so involves no division
by zero. Here a>0 on the stated domain in any event. The two boundary terms
are genuine linear first differences. The intervals [x_j-eta,x_j+eta]
are pairwise disjoint since 2beta<=2<pi and are contained in[2h,pi-h].
For absolutely continuous G with BV derivative on such an interval,

    G(x+eta)+G(x-eta)-2G(x)
       =integral_0^eta [G'(x+r)-G'(x-r)]dr,
    |this|<=eta Var_[x-eta,x+eta](G').                  (6)

Thus, with M=sup_[2h,pi-h]|F0'| and V=Var_[2h,pi-h](F0'),

    |Shift|<=(a beta/m^2)(2M+V).                       (7)

No derivative increment is charged twice. The boundary paths also stay
inside[2h,pi-h]. D25 already proves

    M<=(4/3)L+(2/3)log m+20/3.                         (8)

### 2. A uniform derivative-variation bound for this fixed F0

The inherited explicit origin profile is

    F0=L f0+P0+Q0/pi,
    f0=b/pi, b=2cot(z/2)-4/z,
    P0=[2f(z)-2f(0)]/z+2f(z)d0(z),
    d0=1/(2sin(z/2))-1/z,
    Q0=2cot(z/2)log(sin z)-4log z/z.                    (9)

There are no periodic derivative atoms in the OPEN interval (0,pi): the
nearest atoms of f' are at odd multiples of pi. We use |f|<=4, |f'|<=2,
|f''|<=1 there and f'(0)=0. Hence also |f'(z)|<=z and
|f(z)-f(0)|<=z^2/2. These are statements about this fixed origin profile;
no smoothness through the moving phase-dependent cusps is being asserted.

Let c(x)=cot x-1/x, with its regular value at zero. PD-T270's local
partial-fraction proof gives |c''|<1 on[0,pi/2]. Since b(z)=2c(z/2),
|b''|<=1/2 on[0,pi]. Therefore Var(f0')<=1/2. Also

    d0(z)=[c(z/4)-c(z/2)]/2,
    |d0''|<=5/32.                                    (10)

D25 proves d0 increasing, 0<=d0<=1/5 and 0<=d0'<=1/3. For
r(z)=[2f(z)-2f(0)]/z the preceding f bounds give |r''|<=8/z.
For the product term in P0, integrate

    |(2f d0)''|<=2|f''|d0+4|f'|d0'+2|f||d0''|.

Its integral over[0,pi] is at most
2pi/5+8/5+5pi/4<9, using pi<4. Consequently

    Var_[2h,pi-h](P0')<=8log m+9.                     (11)

For Q0, divide at pi/2. On the initial half write

    Q0=b(z)log(sin z)+g(z),
    g(z)=4log(sin z/z)/z=4 integral_0^1 c(tz)dt.

Here |g''|<=4/3. The inherited |b'|<=1, |b|<=z, cot z<=1/z
and csc^2 z<=pi^2/(4z^2)<(5/2)/z^2 show that the last two
terms of (b log sin)'' cost at most (9/2) integral dz/z.
Its first term costs less than1: |b''|<=1/2 and
integral_0^(pi/2) -log(sin z) dz=(pi/2)log2<2.
The integral identity follows by adding the sine and cosine integrals
and substituting twice the angle. The g'' integral is less than3.
Thus the initial contribution is <=(9/2)log m+4.

On the central half set u=pi-z. The first part of Q0 becomes
T(u)log(sin u), T=2tan(u/2), where T<=2u, T'<=2, T''<=2.
Its three second-derivative terms cost respectively less than4,
4 integral_h^(pi/2) du/u and 5 integral_h^(pi/2) du/u.
The other term -4log z/z has second derivative of magnitude
4|2log z-3|/z^3<=12/z^3 on[pi/2,pi]; indeed 1<z<=pi and
log pi<6/5. Its integral is18/pi^2<2. We have proved

    Var(Q0')<=(27/2)log m+10,
    V<=L/2+(25/2)log m+37/3.                         (12)

All pieces are smooth through pi/2; their first derivatives match there.
Thus no partition jump is omitted from (12). Combining (8),(12),

    2M+V <= (19/6)L+(83/6)log m+77/3
           <=17L+27,                                (13)

because log m<=L+1/32 and 77/3+83/192<27. From (7), a<=1,

    |Shift| <= (beta/m^2)[17L+27]
              <=(beta/n^2)[17L+27].                  (14)

### 3. Preserve the full phase-profile and hole charges

No phase-dependent profile pairing improvement is presumed. D25/D37 give
the unchanged coefficient charge 7rho L/(pi m) and cancellation charge
rho[175/4+20log m]/(pi m), including BOTH endpoint holes and every
root/no-root transition. On the wide domain the regular pole charge is
rho[5log m+44]/m. Their sum is bounded by

    (rho/m)[(7/3)L+(35/3)log m+703/12]
       <=(rho/n)[14L+59].                             (15W)

Here pi>3 and log m<=L+1/32 suffice; 703/12+35/96<59.

For completeness, on the near domain D37's endpoint estimate gives
|V0|<=e^2+delta^2<=2rho^2<=rho, for V_s=N_s-aN0 and
V0=U0-aU0(0). D25 gives |V_s|<=(9/2)rho and central
Var V_s<15rho, with every periodic derivative atom included.
The exact pole difference is V_s/(2sin(z/2))-V0/z. On the central
half the two weights have sup/variation respectively <=3/4,1/4 and
<=2/3,1/3. Its variation per side is <=(305/24)rho<=13rho;
its sup is <=(97/24)rho<=(9/2)rho. The inherited initial estimates
are variation <=(9/2)rho log m+2rho and sup<=4rho per side.
Thus total variation <=rho(9log m+30). Midpoint error contributes
half that divided by m; actual initial holes cost16rho/m and central
holes9rho/m. The full near pole charge is therefore

    (rho/m)[(9/2)log m+40].                           (16)

Together with the unchanged two charges this gives

    (rho/m)[(7/3)L+(67/6)log m+655/12]
       <=(rho/n)[(27/2)L+55],                        (15N)

since 655/12+67/192<55. Equations(14),(15) prove(1).
Using beta<=rho and n>=32 yields(2):
27/2+17/32<113/8, 55+27/32<56 and
14+17/32<117/8, 59+27/32<60. This proves the theorem.

## Exact first-variation diagnostic and remaining obligation

The prescribed cheapest test can also be kept without a quadratic claim.
Take (alpha,beta)=epsilon(A,B), fixed A,B>=0 and n fixed; c_*=(B-A)_+.
For each 0<z<pi, the no-root formula holds for small enough epsilon,
and a,ce,cd,U0 have zero first derivative at zero. The actual profiles obey

    D F_L=B J(z)-(c_*/pi)log(pi-z),
    D F_R=-B J(z)-(c_*/pi)log(pi-z),
    J(z)=L/pi-f'(z)/sin(z/2)+log(sin z)/pi.

The origin's f'(0)=0 is included here. Differentiation under the profile
integrals follows from D25's integrable initial envelope and central
rho[7+4(-log sin(pi-z))] envelope; the coefficient and regular pole
differences have integrable uniform bounds as well. Thus the exact
directional derivative of(4) is

    D Eout = (B/m)[J(2h)-J(pi-h)]
       -(c_*/pi)(Q_0+Q_1)[log(pi-z)]
       +(B/m^2)[F0'(2h)-F0'(pi-h)].                   (17)

The common logarithm and both boundaries remain. In particular, opposite
linear numerator profiles are insufficient to justify a full uniform
quadratic remainder. Formula(17) is a diagnostic supporting the choice
of (5), not an independently registered negative theorem or a proof of
the complete phase-profile cancellation. The singular logarithm retains
its original label and exact mesh. Full D13 remains OPEN.

## Checks, sources, scope and next paper task

Paper proof only: no source edit, scientific import, degree/phase/native/
endpoint/compile/scalar job, threshold scan or new measurement. Read-only
commands were bounded sed/rg/wc/cat reads; only the three assigned E02
paper records were written. Literature search coverage/limitations and all
candidate dispositions are in the linked idea record. No external theorem
or priority assertion is used; PD-T270 supplies its own elementary proof.

These bounds concern K_fixed-G_n only. The fixed-row error, retained six
rows, full origin conversion +u E(0), endpoint numerators and exceptional
top mode remain EXACTLY their existing terms. No new onset or coverage,
nor any reduction of the whole D13 remainder, follows by itself.

Best next PAPER task: retain the signed common logarithm in(17), then
derive a uniform two-profile remainder across the moving root transitions
and f' atoms before another BV estimate. A scalar use requires independent
proof/source/SPEC review, publication and root release first.

History: 2026-11-06, Codex mathematical developer, parent-requested
gpt-6.1-sol xhigh; actual serving metadata unavailable. Rules read at
017f8ecc45534b4a6dd38b0488020463cb914edb. This is one component of E02;
root alone controls Git/shared records and any later release.
