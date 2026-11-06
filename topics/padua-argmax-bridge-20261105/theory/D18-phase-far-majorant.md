# PD-T?argmax-bridge-codex-D18-majorant — A positive affine full far-error envelope

ID kind: PD-T. Aliases: P/u finite-error correlation; affine entropy/max
majorization. Split from: D18 prospective global onset. Split into: none.

## Statement, definitions and status

Use exactly D02/PD-T364's corrected primitive S_n and true completed
model M_infty. Let integer n>=32,m=n+1,L=log n,H=1+L and take absolute
phases alpha,beta>=0,1/2<=rho=alpha+beta<=pi. Put

    a=(cos alpha+cos beta)/2, u=1-a, P=sin alpha+sin beta,
    u0=191/6144, s=min(2,sqrt(8u)), s0=sqrt(191/768),
    S=1/2+32/pi, f=log8, g=1+log(1+2S/s0),
    j0=max(5,2S*f+S*log2), j1=(log2)/2,
    V=128/pi+6, VV=256/pi+23,
    As=(1+64/pi)/pi, VA=128/pi^2,
    VJ0=(128/pi+4S)f+2S*log2+20,
    W0=V+j0/pi, VW0=VV+VJ0/pi.

Let e4 be the COMPLETE D05 fixedR2,delta pi/8 mesh+row+collision
allowance, unchanged. Define positive scalar coefficients

    ED0=[(52/pi^2)H+7]/n+10/n^2+20H/(pi*n^2),
    ED1=[352H/(3pi)+2/pi]/n,
    Dp=10/n^2+20H/(pi*n^2),
    I0=[(VA/2+9As)L+VW0/2+5W0+4V]/m,
    I1=[(3/2)g+3log2+4+5log m]/(pi*m),
    Z0=[72+3log(4m/pi)]/m,
    Z1=[34+10log(8m/5)+2log(32m/(m-4))+4log(2m)]/(pi*m),
    Af=ED0+e4+I0+Dp+Z0,
    Bf=ED1+I1+Z1.

Then on the FULL CLOSED FAR diamond, including axes, a=0, both parities
and finite-polynomial collisions,

    |S_n(psi)-M_infty(psi,L)|<=Af(n)+Bf(n)*s.         (1)

Af,Bf are positive and decrease for all real n>=32. For fixed n,

    u -> [Af+Bf*min(2,sqrt(8u))]/u                   (2)

decreases on u0<=u<=1. Status: **PROVED**, analytic developer supporting
result; independent review pending. No numerical premise or far exclusion
is asserted by this envelope alone.

## 1. Actual phase geometry and independent scalar majorization

On the closed phase diamond a>=0, so u<=1. As in D16, the far condition
gives u>=1-cos(1/4)>=191/6144. Cauchy and sin^2 x<=2(1-cos x) give

    P^2<=2(sin^2 alpha+sin^2 beta)<=8u,
    0<=P<=s, p=sin alpha<=s, d=(sin beta-sin alpha)_+<=s.

Also0<=a<=1 and |U0|<=8, by the unchanged accepted D05 inputs.
We FIRST apply the accepted D05 theorem to the ACTUAL phase. We then
majorize its explicit nonnegative scalar right side. No physical theorem
is applied at fictitious phase values with inconsistent p,P or a.

Every input dependence is increasing on the independent nonnegative
parameter box used here: products have nonnegative coefficients; max is
increasing; and the continuous entropy

    G(p,Sbar)=p[1+log(1+2Sbar/p)], G(0,Sbar)=0,

increases in p,Sbar>=0, since its p derivative is
1+log(1+x)-x/(1+x)>0. Replacing a<=1 makes Sbar<=S. Thus

    G(p,Sbar)<=G(s,S)<=s[1+log(1+2S/s0)]=g*s,

because s>=s0>0. This is valid even when actual P=p=0 on a far axis:
the auxiliary s is positive; no lower bound on actual p is imposed.

For the inner max in Jstar, p<=s<=2 and S>1 give
max(p,S+p/2)<=S+s/2. The outer max obeys

    max(5,2S*f+(S+s/2)log2)<=j0+j1*s.

Consequently VJ<=VJ0+(3g+log2)s, Wstar<=W0+(j1/pi)s,
VW<=VW0+[(3g+log2)/pi]s. The d term is bounded by s(4+5log m)/pi.
Insert these into the EXACT D05 I_n formula to obtain I_n<=I0+I1*s.
The displayed I1 combines(log2)/2+5(log2)/2=3log2. All constant
interior terms, including the conservative |U0|8 charges, remain in I0.

## 2. Keep every other D05 error, and derive exact strip coefficients

D04's row error is bounded by ED0+ED1*s. The whole unchanged e4
remains, including e_rows=(181+19L)/n+21600/n^2 and every collision
charge. The extra D_pole is bounded by Dp. None is discarded or merged
with an error at another phase.

For the accepted D05 signed strip put h=pi/m,epsilon=3h/2,ell=5h/2,
delta=pi/8 and use exactly

    W_P(z)=7+(P/pi)[3+2log(4pi/z)],
    Q(P,z)=(2z/pi)[7+(P/pi)(5+2log(4pi/z))],
    T_Z=[32+6log(6/epsilon)]/(2m)+Q(P,ell)
                                 +[W_P(delta-h/2)+2W_P(2h)]/m.

This expression is affine increasing in P>=0. Its constant coefficient
is Z0: the initial and remaining constants are35/m+21/m, and the BV
term is[16+3log(4m/pi)]/m. Its P coefficient is EXACTLY Z1, because
4pi/ell=8m/5,4pi/(delta-h/2)=32m/(m-4),4pi/(2h)=2m.
Thus T_Z<=Z0+Z1*s. Sum these component bounds to prove(1), retaining
the fixed R2/delta pi8/n32 geometry, all shifted floors and exact rows.
Separate absolute phases give the stated signed diamond without n,m swap.

## 3. All-degree and phase-ratio monotonicities

ED0,ED1,Dp are positive sums of(cL+d)/n^j and decrease for L>3.
The full e4 decreases on n>=32 by the accepted D16 termwise proof:
L/m decreases; the C_X shares[c+(1/2)log(X+1/2)]/(X-1/2)^q have
negative derivative for(c,q)=(5,1),(6,2),X=m/8; inverse products and
the full row/collision costs decrease. No old finite comparison floor
enters these scalar statements.

I0=(cL+d0)/m with positive fixed c,d0, so its derivative numerator is
c(1+1/n-L)-d0<0. I1's numerator is a fixed positive constant plus5log m;
its derivative after dividing by m has sign5-[(3/2)g+3log2+4+5log m]<0.
Z0 decreases since its numerator exceeds3. For Z1,34/m decreases,
log(8m/5)/m and log(2m)/m decrease for m>=33. Finally
log(32m/(m-4)) is positive with derivative-4/[m(m-4)]<0, so dividing
that term by m also decreases. Thus Af,Bf are positive decreasing.

For(2), Af/u decreases and Bf*s/u decreases: s/u=sqrt(8)/sqrt(u)
on u<=1/2, and s/u=2/u on u>=1/2, with equal values at the seam.
This proves the phase-ratio assertion, including the cap s=2.
It does not assert that the raw undivided gap is minimized at u0 when
the sufficient endpoint gap is nonpositive.

## Scope and provenance

This is a new positive-error allocation from accepted full-phase scalar
formulas, not a full relative finite remainder or a new approximation
model. The prospective7000 far gate is a separate obligation. No phase,
native, kernel, board, root, quadrature or degree computation occurred.
2026-11-06, parent-assigned Codex Sol xhigh; rules/input
0768cb93c4f829faf5f38d47cdd7e33faad8bf64, serving metadata unexposed.
