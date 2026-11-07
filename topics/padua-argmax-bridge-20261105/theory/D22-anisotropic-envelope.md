# PD-T?argmax-bridge-codex-D22-anisotropic — Separable true-constant near envelopes

ID kind: PD-T. Aliases: directional fractional/log optimization; exact
radical quartic maximum; anisotropic quadratic retention. Split from:
D22 near-threshold research. Split into: the4096 application and the
unchanged-absolute-budget obstruction have separate records.

## Statement and definitions

Write x=|alpha|,y=|beta|,rho=x+y<=1/2,r2=x^2+y^2,
a=(cos x+cos y)/2,u=1-a,c0=47/192,A=15/32. Use exactly D02's
completed constant C_infty and accepted D10-relative-constant's
directional bound. Let V>=0 and kx,ky>=0 be any real constants, and
define

    qx=c0*V-89/72, qy=c0*V-23/24.

Whenever qx,qy>0,

    -u*V+C_infty(x,y)-C_infty(0)+kx*x+ky*y
      <=A*x^(3/2)-qx*x^2+(4/9)x^2 log(1/x)+kx*x
                         -qy*y^2+(1/9)y^2 log(1/y)+ky*y.       (1)

All zero logarithmic products are zero. Put Bx=77/96,By=1/12 and

    z(B,q,k)=[3B+sqrt(9B^2+32qk)]/(8q),
    Psi(B,q,k)=(B/4)z^3+(k/2)z^2.

The expression in(1) is bounded above by EACH of

    U_rad=Psi(Bx,qx,kx)+Psi(By,qy,ky),                       (2)
    U_rat=Bx^4/(4qx^3)+kx^2/qx
                         +27By^4/(32qy^3)+ky^2/(2qy).       (3)

One further valid envelope, keeping the actual log coefficients, is

    U_log=Psi(A,2qx/3,kx)+3ky^2/(8qy)
                   +(2/9)exp(-1-3qx/2)+(1/18)exp(-1-6qy).   (4)

These are three separate explicit upper bounds, not fitted values.
The4096 application uses ONLY rational bound(3), with fixed3/4 alpha
and1/2 beta quadratic allocations; (2),(4) are retained alternatives.
Overall status: **PROVED**, written analytic developer result; distinct
review required. No numerical premise or finite model-error theorem
is built into this lemma.

## Proof of the directional reduction

Accepted D10 gives exactly

    C_infty(x,y)-C_infty(0)
      <=(15/32)x^(3/2)+(19/24)r2
         +(4/9)x^2[1+log(1/x)]
         +(1/9)y^2[3/2+log(1/y)].

The alternating cosine bound and x,y<=1/2 give

    u>=(x^2+y^2)/4-(x^4+y^4)/48>=c0*r2.

Multiplication by -V is valid with the claimed direction because V>=0.
The alpha quadratic constant is19/24+4/9=89/72 and the beta constant
is19/24+1/6=23/24. This proves(1), retaining r2 instead of replacing
it by rho^2/2. Only alpha has the large fractional15/32 term.

The positive function sqrt(t)log(1/t) on0<t<=1 has maximum2/e,
at t=exp(-2). Since e>8/3, this maximum is<3/4. Hence

    (4/9)x^2log(1/x)<=(1/3)x^(3/2),
    (1/9)y^2log(1/y)<=(1/12)y^(3/2).

This yields the separated upper Bx*x^(3/2)-qx*x^2+kx*x plus
By*y^(3/2)-qy*y^2+ky*y. We may maximize on the larger quadrant
x,y>=0 instead of the original closed diamond.

## Exact algebraic optimization and fixed rational allocation

For B,k>=0,q>0 put t=sqrt(x). Then

    B*x^(3/2)-q*x^2+k*x=-q*t^4+B*t^3+k*t^2,
    derivative=t[-4q*t^2+3B*t+2k].

The nonnegative maximizing point is exactly z(B,q,k). At it,
4qz^2=3Bz+2k, so the maximum equals the nonnegative expression
(B/4)z^3+(k/2)z^2=Psi. This includes B=k=0 and both zero axes;
no numerical root solver or phase point is needed. Summing proves(2).

For a simpler rational upper, allocate3qx/4 to the alpha fractional
term and qx/4 to its linear term. The exact elementary maxima give

    Bx*x^(3/2)-(3qx/4)*x^2<=Bx^4/(4qx^3),
    kx*x-(qx/4)*x^2<=kx^2/qx.

For beta allocate qy/2 to each corresponding term:

    By*y^(3/2)-(qy/2)*y^2<=27By^4/(32qy^3),
    ky*y-(qy/2)*y^2<=ky^2/(2qy).

The fractional maximum is27B^4/(256q^3), obtained by the preceding
derivative with k=0; the linear maximum follows by completing the
square. These fixed allocations prove(3), without any parameter search.

## Optional exact-log allocation

For h>0,t>=0 the exact entropy maximum is

    sup_(x>=0) x^2[h log(1/x)-t]=(h/2)exp(-1-2t/h).

Differentiate, obtaining x=exp(-1/2-t/h), and use continuity at zero.
In(1), allocate qx/3 and qy/3 to the respective log terms. The
remaining alpha fractional-plus-linear expression has exact maximum
Psi(A,2qx/3,kx); the remaining beta linear expression has maximum
3ky^2/(8qy). The two entropy costs are precisely those in(4).
This retains the anisotropic log envelope before taking a scalar
majorant; it is not an exact maximization of the unsplit log function.

## Monotonicity and application contract

Each bound decreases when qx,qy increase or kx,ky decrease. For
Psi this follows directly from its definition as a supremum of
B*x^(3/2)-q*x^2+k*x, pointwise decreasing in q and increasing in k;
no derivative of the radical expression is required. The rational and
exponential terms have the same monotonicity.

In the unchanged absolute-error comparison use V=T(n) and add
D16's C(n)+E0(n), kx=ky=K(n), with T=(4log^2n-3logn)/pi^2.
That baseline is separately shown insufficient at4096. If a NEW proved
allowance gives S(phi)-S(0)<=model_difference+Cstar+Kstar*rho+uE0,
combine the EXACT -uT model loss with +uE0 first and use V=T-E0.
For V>=0 this is sharper than first replacing +uE0 by E0*r2/4.
This algebra does not by itself prove that new finite allowance;
the separate D22-origin-reduction owns every term of that telescope.

No full D13 relative remainder, old near correction, fixed eta0 bridge,
unknown maximizer, native/phase/board/root/quadrature/degree or scalar
execution is used. C04/D08 already use directional entropy allocations;
this is their quantitative continuation for the TRUE D10 constant,
with an added finite linear allowance and the retained anisotropic
quadratic loss, not a new general optimization mechanism. 2026-11-06,
parent-assigned Codex Sol xhigh paper helper; rules readca8d52aa2a48c941473846ab884cccb25f1bdb9f,
current integration headcc15e9ae054325b43a3608f09a16d2f0a6a29cb3,
unchanged rules; serving metadata unexposed.


## Root review closure — 2026-11-06

Distinct review [D22](../independent-checks-D22-origin.md), SHA256 `f98523cad972f8b42b500ddb7ea83877f681c779204cd58e8ccb20652098b95b`, accepts this split scope without unresolved mathematical findings. Root adopts the fully charged partial origin cancellation, anisotropic envelope, near noncorner theorem for EVERY n>=4096 with gap3/2000, and scoped unchanged-absolute-budget obstruction. D13 full relative and far/global4096 remain OPEN. No scalar/native/build job was performed. Audited proof prefix is preserved; final Claude audit remains separate.
