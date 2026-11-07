# PD-T?argmax-bridge-codex-D10-constant — Phase-aware bounds for the true limiting constant

ID kind: PD-T. Aliases: completed constant gap; local scalar-functional
curvature; cutoff-free weighted endpoint loss.
Split from: D10 practical phase-relative constant target.
Split into: none. This is not a finite-degree relative-error theorem.

## Statement and definitions

Use EXACTLY D02's continuous completed constant C_infty on the signed
phase diamond |alpha|+|beta|<=pi. First take alpha,beta>=0 and put

    rho=alpha+beta, r2=alpha^2+beta^2,
    a=(cos alpha+cos beta)/2, u=1-a, p=sin alpha,
    e=alpha+beta, d=alpha-beta,
    c_e=cos(e/2), c_d=cos(d/2),
    C0=2gamma+4log2,
    c=1/3+(4/pi^2)(log^2 pi-log^2 2).

Let f(x)=Phi_0(1/2+x/(2pi)) and H(x) be exactly the scalar finite-part
functional of C08-far-pole-functional.md. Let E_c be the central
root correction of C01-near-central-upper.md. Then:

1. On the ENTIRE closed phase diamond,

       C_infty(phi)<320/197+66/125+49/100<8/3.               (1)

   The proof retains the stronger phase-aware upper

       C_infty(phi)<320/197+43/125+(46/125)a+(9/20)sin alpha.

2. On the CLOSED near domain rho<=1/2,

       C_infty(phi)=E_infty(phi)+c_e H(d)+c_d H(e)
                                             -c*a+E_c(phi), (2)
       [C_infty-E_c](phi)-[C_infty-E_c](0)<=19r2/24,          (3)

   and therefore

       C_infty(phi)-C_infty(0)
        <=(15/32)alpha^(3/2)+(19/24)r2
          +(4/9)alpha^2[1+log(1/alpha)]
          +(1/9)beta^2[3/2+log(1/beta)]                    (4)
        <=(15/32)rho^(3/2)+(113/72)r2
                                      +(4/9)r2 log(1/rho).

   All vanishing logarithmic products have value zero. In particular
   the one-sided increment is at most(4/3)rho on this domain.
   This is an origin-relative linear upper, not an absolute Lipschitz
   assertion between arbitrary pairs of phases.

3. On the CLOSED FAR domain 1/2<=rho<=pi, with the accepted
   PD-T271 origin normalization,

       C_infty(phi)-C_infty(0)<22(1-a).                    (5a)

   This bound is restricted away from the fractional axis singularity.

The scalar ingredient, useful independently within this same proof, is

    H(x)-H(0)<=x^2/3, |x|<=1/2.                          (5)

There is an exact fractional axis obstruction through the origin:

    C_infty(alpha,0)-C_infty(0,0)
      =k_frac alpha^(3/2)+o(alpha^(3/2)),
    k_frac=(4/pi^2)integral_0^1 sqrt(1-y^4)dy>0.           (6)

Thus no finite K gives C_infty(phi)-C_infty(0)<=K(1-a) on a full
neighborhood of zero. The far-only version(5a) remains consistent
with(6). The coefficient k_frac is neither kappa_shift=gamma+log(8/pi)
nor PD-T269's limiting deformation D_infty.

## Status, assumptions and dependencies

Overall status: **PROVED**, analytic developer proof, distinct review
required. No numerical premise or executable calculation. All definitions
include their original continuous weighted collision values. Other
quadrants use the inherited separate phase evenness; no mesh exchange.

Dependencies: accepted D02 bias identity and uniform identification of
C_infty; accepted C08 weighted coefficient, endpoint constant, scalar
pole functional and paired integral bounds; C04's full-period
distributional Phi_0''<=12 and N1-13's finite variation of Phi_0';
accepted C01 central correction upper and exact axis calculation.
The D04/D05/D07 finite-row reductions are contextual: none is altered
or needed as a finite-degree premise. PD-T271 and D02 fix C_infty(0)
for(5a); they are not finite-degree lower-bound premises.

## Proof

### 1. A cutoff-free decomposition, with every divergent term paired

D02 defines C_infty=E_infty+K_0 with

    E_infty=a/3+a C(t_d)C(t_e)/pi^2,
    t_d=1/2+d/(2pi), t_e=1/2+e/(2pi).

For ANY positive cutoff epsilon, expand K_epsilon exactly as in C08:

    K_epsilon=K_V,epsilon+K_I,epsilon,
    K_V,epsilon=c_e H_epsilon(d)+c_d H_epsilon(e),
    K_I,epsilon=(4a/pi^2)(log^2 epsilon-log^2 pi)
                   +(1/pi^2)integral_epsilon^pi(I_L+I_R)dz.

Take epsilon down to zero, using D02's EXISTING finite-part limit
and C08's scalar H limit. Thus

    K_V,0=c_e H(d)+c_d H(e).                             (7)

For the cancellation piece the global pointwise inequality proved in
C08 is

    I_L(z)+I_R(z)<=4a cot(z/2)log(sin z)
                                         +2p|log(sin z)|.

Its baseline antiderivative is

    4a log^2(2sin(z/2))-4a log^2 2
                                      -2a Li2(sin^2(z/2)).

At z=pi it equals -a*pi^2/3. The value at epsilon, combined with
the displayed logarithmic counterterm, tends exactly to -c*a:
log(2sin(epsilon/2)/epsilon)=O(epsilon^2), its product with
log epsilon tends to zero, and Li2(sin^2(epsilon/2)) tends to zero.
Also integral_0^pi |log sin z|dz=pi log2. Therefore

    K_I,0<=-c*a+(2log2/pi)p.                            (8)

This rederives the limit for variable epsilon. It is not an application
of C08's FIXED epsilon=1/100 theorem at an unauthorized new cutoff.

On rho<=1/2 the accepted positive complete-numerator identity makes
I_L+I_R EXACTLY the baseline on0<z<=pi/2. On the central half put
epsilon_c=pi-z. Its two actual generic-J parameters are

    sin(alpha)/2,
    a tan(epsilon_c/2)+sin(beta)/2,
    |a tan(epsilon_c/2)-sin(beta)/2|.

Consequently the difference from that same baseline on the central
half is EXACTLY pi^2 E_c. Hence (8) strengthens there to the equality
K_I,0=-c*a+E_c. Together with(7) this proves(2). No moving-root
Taylor expansion is used; E_c retains the actual positive-part roots.

### 2. Keep the full-phase weighted endpoint loss

The accepted C08 scalar inequality gives, with b=C0-7/2>0,

    cos(theta/2)C(1/2+theta/(2pi))
                <=C0-b[1-cos(theta/2)], |theta|<=pi.

Both sides are nonnegative. Set x_e=1-c_e, x_d=1-c_d. Their product
is at most

    C0^2-C0*b*u-(7/2)*b*x_e*x_d<=C0^2-C0*b*u,
    u=x_e+x_d-x_e*x_d=1-a.

Thus

    E_infty<=a/3+C0^2/pi^2-[C0(C0-7/2)/pi^2]u.          (9)

The following strict elementary bounds are already proved in the
dependencies: C0<4, C0>391/100>39/10, pi^2>197/20, pi^2<10,
log pi>11/10, log2<7/10, log2>69/100, pi>25/8. They give

    C0^2/pi^2<320/197,
    C0(C0-7/2)/pi^2>39/250,
    c-1/3>36/125,
    2log2/pi<9/20.                                     (10)

C08's global H<1/2 and c_e+c_d<=1+a imply from(7)--(10)

    C_infty<320/197+43/125+(46/125)a+(9/20)sin alpha.

Since a<=(1+cos alpha)/2,

    (46/125)a+(9/20)sin alpha
       <=23/125+sqrt((23/125)^2+(9/20)^2)
       <23/125+49/100.

The square comparison is rational; (23/125)^2+(9/20)^2=0.236356
is strictly below(49/100)^2=0.2401 (these are exact decimals).
This proves the first inequality(1). The exact remaining difference
8/3-[320/197+66/125+49/100]=7181/295500 is positive. All
phase weights, including a=0 and vertices, remain in the proof.

### 3. Local fourth derivative for the scalar periodic profile

C08 proves f(x)>=f(0)>0 globally. Its inherited C04 semiconcavity is

    f(v+x)+f(v-x)-2f(v)<=M*x^2, M=3/pi^2, all real v,x.   (11)

The negative periodic derivative atoms are INCLUDED in(11). On
|x|<=1 there is no atom. Put k0=C0-2log pi, so0<k0<2. The exact
reciprocal-pair series is

    f(x)=cos(x/2)[k0+W(x)]/pi,
    W(x)=4sum_{j>=1} A_j(x/pi)^(2j),
    A_j=sum_(l odd>=1)l^(-2j-1)<=7zeta(3)/8<10/9.

Termwise differentiation is justified on |x/pi|<=1/3 by uniform
geometric convergence. Bound its derivative absolute values by those
of (40/9)y^2/(1-y^2), at y=1/3, including the pi^-j chain factors
bounded by3^-j. This gives, in order0 through4,

    |W|<=5/9, |W'|<=5/4, |W''|<=15/8,
    |W'''|<=75/32, |W''''|<=165/32.

The product rule consequently gives

    |f''''|<(1/3)[165/32+2(75/32)+(3/2)(15/8)
                                      +(1/2)(5/4)+(23/9)/16]
             =3871/864<9/2, |x|<=1.                       (12)

### 4. A phase increment of H, not two absolute estimates

Pair the two endpoints in C08's exact scalar functional:

    H(x)=lambda0*f(x)+(1/pi)integral_0^pi
           [f(x+v)+f(x-v)-2f(x)] K(v)dv,
    lambda0=(2/pi)log(4/pi), 0<lambda0<1/(2pi),
    K(v)=1/[2sin(v/2)].

Let D_x f(v)=f(v+x)+f(v-x)-2f(v), and0<=x<=1/2.
Subtract twice the x=0 value from H(x)+H(-x). The result is

    lambda0*D_x f(0)
          +(2/pi)integral_0^pi[D_x f(v)-D_x f(0)]K(v)dv.    (13)

For v>=1/2, D_x f(v)<=M*x^2 by(11), and D_x f(0)>=0 since
f has its minimum at zero. For0<=v<=1/2, evenness and(12) give

    |D_x f(v)-D_x f(0)|<=(9/4)*x^2*v^2.

Indeed |(D_x f)''|<= (9/2)x^2 by the triangular second-difference
formula for f'', and (D_x f)'(0)=0; all its arguments lie in[-1,1].
Also D_x f(0)<=M*x^2. The elementary kernel bound from C08 yields

    integral_0^(1/2) v^2 K(v)dv
       <=integral_0^(1/2)(v+v^3/16)dv=129/1024,
    integral_(1/2)^pi K(v)dv=log cot(1/8)<log8<21/10.

Since H is even, divide(13) by2. With pi>31/10, the coefficient
of x^2 in the resulting H(x)-H(0) bound is at most

    M/(4pi)+(9/(4pi))(129/1024)+(M/pi)(21/10)
       <7050/29791+5805/63488<1/3.

Its left side in(13) is2[H(x)-H(0)]. This proves(5),
including x=0. A global atom was never replaced by a positive derivative
bound or omitted from the far part of the integral.

The same representation at zero and f>=f(0) imply H(0)>0. Therefore
on the near phase triangle, |d|,|e|<=1/2,

    c_e H(d)+c_d H(e)-2H(0)
       <=(d^2+e^2)/3=2r2/3.                            (14)

Equation(9) also gives E_infty-E_infty(0)<=-u/3. Since
c-1/3<1/2, using log pi<6/5, log2>69/100 and pi>3, and
u<=r2/4, (14) implies(3). Apply C01's exact directional and radial
E_c upper bounds to obtain(4). Finally rho<=1/2 gives
rho^(3/2)<=(3/4)rho, r2<=rho/2 and
r2 log(1/rho)<=rho/e_Euler<(3/8)rho. Hence its radial upper is
at most(1501/1152)rho<(4/3)rho, as claimed.

### 5. A useful quadratic factor on the closed FAR domain

The accepted D08 normalization, using PD-T271 and kappa_shift>3/2,
gives C_infty(0)>4383/2420. The phase-aware upper above therefore
implies

    C_infty(phi)-C_infty(0)<8/15-(46/125)u+(9/20)p,

because320/197+89/125-4383/2420<8/15. Here no finite
Lambda_c inequality is inferred from a limiting constant. For rho>=1/2,
the cosine alternating bound gives u>=191/6144>31/1000. Also
u>=sin^2(alpha/2), hence p<=2sqrt(u). Consequently

    [C_infty(phi)-C_infty(0)]/u
        <(8/15)/u+(9/10)/sqrt(u)-46/125
        <8000/465+36/7-46/125<22.

For the middle inequality use u>31/1000>(7/40)^2. The last
comparison is rational. This proves(5a) on the entire closed FAR
domain, including a=0. No extension through u=0 is asserted.

### 6. The genuine axis term and the failed quadratic form

For beta=0, C01-near-axis-limit.md section3 computes the exact central
root correction by scaling epsilon_c=sqrt(alpha)y. Its justified
dominated limit is

    E_c(alpha,0)/alpha^(3/2)
                ->(4/pi^2)integral_0^1 sqrt(1-y^4)dy.

This is the actual E_c in(2), not a bound inferred from a root width
or from the approximate T bridge. All other terms in(2) change by
O(alpha^2). E_infty and a are smooth even functions locally. For H,
the same near part of(13) is O(x^2) in absolute value. On v>=1/2,
the accepted finite variation V of f' gives
integral |D_x f(v)|dv<=V*x^2 by the elementary L1 second-difference
identity used in C01's axis proof; the kernel is bounded there and
D_x f(0)=O(x^2). Thus |H(x)-H(0)|=O(x^2) locally as well.
This proves(6) directly from the exact decomposition. Since
1-a(alpha,0)=alpha^2/4+O(alpha^4), every finite quadratic K(1-a)
upper through zero contradicts the positive coefficient in(6).
No conclusion is transferred to the physical Lebesgue function.

## Scope and remaining obligations

The global constant allowance improves by at least49/120 relative to
the previous123/40 upper, with the same origin lower if desired. This
is an analytic improvement of a limiting-constant budget. A new finite
global onset still requires separate all-degree finite errors, near
noncorner and actual-corner cases and distinct review. No new onset or
degree certificate is claimed here.

The precise near increment is valid only for rho<=1/2. Extending it
to a larger near region needs a new root/positivity-domain argument.
The far constant22 is an explicit upper, not an optimized constant.
The full finite relative
S_n(phi)-a(phi)S_n(0) target is still OPEN. No fixed eta0 is silently
discarded, no old near correction is added and no finite-row model
or previously accepted proof is edited.

Checks: paper proof only; no numerical scalar, quadrature, root,
board/native or degree job. The exact rational comparisons are written
in the proof, not reported as an executed check. Independent review
is required. 2026-11-06, rules/input9d5e8c7a1a8fab6017d5dd9406daec0d834b0bbf,
main64409c47a717aef074f611b31a9fd48b7a15101b; Sol xhigh assigned,
serving metadata unexposed. Gate/attempt are in the D10-owned records.
