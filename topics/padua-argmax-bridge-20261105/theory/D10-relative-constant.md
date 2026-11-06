# PD-T?argmax-bridge-codex-D10-near — A true near-origin fractional constant modulus

ID kind: PD-T. Aliases: local scalar-functional curvature; completed near constant increment.
Split into: none; global and negative scopes have separate records.

Rules/input `9d5e8c7a1a8fab6017d5dd9406daec0d834b0bbf`; latest main
`64409c47a717aef074f611b31a9fd48b7a15101b`. Parent-assigned Sol xhigh;
serving metadata unexposed. **PROVED**, analytic developer result, distinct
review required. Exact real arithmetic; no numerical premise.

Split from: original combined D10-relative-constant first freeze, whose
EXACT complete text is preserved at
[attempts/D10-relative-constant-first-freeze.md](../attempts/D10-relative-constant-first-freeze.md),
SHA256 `56c69c6e39fc0fddf9ada3505c99c293d89fe56d74c2c1a7aa1d643d30c697af`.
This is a substantive split, with no new mathematics or altered constants.
Mapping/history: [attempt](../attempts/D10-relative-constant.md).

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
root correction of C01-near-central-upper.md. On the CLOSED near domain rho<=1/2, define E_c exactly as in accepted
C01-near-central-upper.md. Then

    C_infty(phi)=E_infty(phi)+c_e H(d)+c_d H(e)-c*a+E_c(phi), (2)
    [C_infty-E_c](phi)-[C_infty-E_c](0)<=19r2/24.           (3)

Consequently,

    C_infty(phi)-C_infty(0)
      <=(15/32)alpha^(3/2)+(19/24)r2
        +(4/9)alpha^2[1+log(1/alpha)]
        +(1/9)beta^2[3/2+log(1/beta)]
      <=(15/32)rho^(3/2)+(113/72)r2+(4/9)r2 log(1/rho)
      <=(4/3)rho.                                         (4)

Vanishing logarithmic products have value zero. This is a one-sided
origin-relative upper, not absolute Lipschitz continuity between all phases.
A scalar ingredient is H(x)-H(0)<=x^2/3 for |x|<=1/2.       (5)

## Dependencies

The exact full-domain finite-part decomposition and endpoint loss are in
[D10-global-constant.md](D10-global-constant.md). Accepted C01 supplies the
central correction bound; C04 supplies full-period distributional Phi_0''<=12,
including negative derivative atoms; N1-13 supplies finite variation of Phi_0'.
All weighted values have their original collision limits. No finite-n or
fixed eta0 bridge is a premise.

## Exact near decomposition

In the global proof K_V,0=c_e H(d)+c_d H(e), and the baseline K_I,0
has the common coefficient c defined above. Its near-only equality is:

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

## Local scalar-functional proof preserved from first freeze

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

## Scope and history

The numbers(5),(9),(13),(14) in the preserved proof refer respectively to
the scalar increment, the global endpoint loss and the two displayed
second-difference/weighted estimates; the needed global endpoint loss
is in the global companion. No theorem is applied past rho1/2. An
extension to rho<1 requires a fresh central positivity/root argument.
No global onset follows, and the full finite S-aS(0) error stays OPEN.
The exact axis obstruction is in D10-axis-obstruction.md. No mathematical
run or old-source change. 2026-11-06 substantive split, exact first text
preserved at the link above; no new constants or claim extension.


### Supplementary review closure — 2026-11-06

Distinct Astra xhigh reconstruction ACCEPTED the preceding unchanged
final split scope; no unresolved findings. See
[independent-checks-D10-relative-constant.md](../independent-checks-D10-relative-constant.md),
report SHA256bdcadf119fb905f898612ad25b9123bf8ff58184d6ef573e1503a740d987964c.
The substantive split, inherited-Arb provenance and cutoff-domain wording
findings are closed there. This records no new analytic onset or finite
certificate. Final Claude review remains pending.
