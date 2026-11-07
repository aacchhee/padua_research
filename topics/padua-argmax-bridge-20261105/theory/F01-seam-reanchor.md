# PD-T?argmax-bridge-codex-F01-seam-reanchor — Generic outer gate anchored at five fourths

ID kind: PD-T. Aliases: I07 reanchored E13; fixed-radius rational physical caps;
complete absolute outer envelope with no degree endpoint.
Split from: F01 I07 family; independent of the new finite-support estimates.
Split into: none.

## Statement and definitions

For EVERY integer n>=32 and ACTUAL phases x=|alpha|,y=|beta|>=0 with
5/4<=rho=x+y<=pi, let a=(cos x+cos y)/2,u=1-a,p=sin x,q=sin y,
P=p+q,d=(q-p)_+,ce=cos(rho/2),cd=cos((x-y)/2). Fix rational constants

    u1=3/16,a0=13/16,w0=29/16,p0=3/5,P0=6/5,eta=3/2,
    v=u-u1.

The complete explicit envelope defined below obeys

    CEphi<=C_b+C_s sqrt(v)+C_l v,
    |S_n-M_infty|<=C_b+P0*KD+C_s sqrt(v)+(C_l+3KD)v.        (1)

With the accepted GLOBAL model constants j,t0 and the COMPLETE one-sided
origin allowance e0, define

    Tmodel=(4log^2 n-3log n)/pi^2,
    G_b=u1(Tmodel+j)-t0*p0-C_b-P0*KD-e0,
    K=Tmodel+j-C_l-3KD, A=eta*t0+C_s.

For EVERY such phase Lambda_c(n)-S_n(phi)>=G_b+Kv-A sqrt(v).
If K(n)>0 this is at least F(n)=G_b-A^2/(4K). For ANY separately assigned
real base N>=32, the two conditions K(N)>0,F(N)>0 imply strict outer
exclusion for EVERY integer n>=N, with uniform primitive gap at least F(N).
No base N is chosen or evaluated here. CEphi and KD are exactly the
accepted E08 full-domain finite-error allowance, not a near-domain extension.

Overall status: **PROVED developer PAPER theorem** (including the sufficient
implication), requiring distinct mathematical review/root adoption. Exact
real arithmetic, no numerical premise. No global onset or full cover follows
from this generic implication alone.

## Depends on

Accepted E08-phase-global-error supplies the literal physical bound
|S-M_infty|<=CEphi+KD*P and its original weighted/collision normalization.
Accepted E13 repeats every positive physical component and proves the
entropy tangent and scalar derivative facts used below. Its old geometric
caps and anchor are replaced by new proofs, not transferred. Accepted C08
and E06/E07 supply the GLOBAL model loss u(Tmodel+j)-t0*p, including their
named PD-T271 limiting-origin/regular-constant enclosure dependency.
E08-origin-lower supplies e0 independently of any sign E(0)>=0.

## Proof

### 1. Actual closed-domain geometry before a scalar majorant

Put c=cos(5/8),s=sin(5/8),u_min=1-c. Alternating elementary polynomials give

    103/128<=c<13/16, 1/2<s<3/5.                         (2)

For the cosine upper the numerator is79729/98304<79872/98304.
For the sine lower use1795/3072>1/2; for its upper use
5/8-125/3072+3125/3932160<3/5. These are exact rational
inequalities in a fixed phase, not a numerical phase evaluation.

On the actual outer diamond ce<=c,a<=c<a0, so v>=0 and
ce+cd<=1+a<=w0. To bound p, first work with v0=u-u_min=c-a<=v.
If0<=x<=5/8, p<=s. If5/8<=x<=5/4, let h=x-5/8. Since
y>=5/4-x and cosine decreases on[0,pi], a<=c cos h. Hence

    v0>=c(1-cos h)>=(743c/1536)h^2,
    sin x<=s+c*h<=s+sqrt(1536c/743)*sqrt(v0)
                        <=s+(3/2)sqrt(v0).

Here0<=h<=5/8 and1-cos h>=h^2/2-h^4/24;6144<6687 proves
the last coefficient. If x>=5/4, a<=(1+cos(5/4))/2=c^2, so
v0>=c(1-c)>=3/20>1/9, using c>=4/5,c<=13/16. Since s>1/2,
s+(3/2)sqrt(v0)>1>=p. This includes x=pi and the shared boundaries.
Thus, also by symmetry for q,

    p,q,max(p,q)<=p0+eta sqrt(v).                         (3)

The exact trigonometric difference identity gives
|p-q|=2sqrt(ce^2-a^2)<=2sqrt(a0^2-a^2)<=2sqrt(2v)<=3sqrt(v),
so d<=3sqrt(v), including a=0 at the closed outer edge.

Cauchy gives P<=S(u)=2sqrt(2u-u^2). This function is concave. At
u1=3/16 its value is sqrt87/8<6/5 and its derivative is
26/sqrt87<3 (the latter is676<783). Its global tangent therefore gives

    P<=P0+3v.                                           (4)

These are inequalities at actual phases. They make no fake tuple of
independently extremized coordinates into a physical phase, do not exchange
the unequal finite meshes and require no inverse a at the closed boundary.

### 2. Complete explicit positive envelope

For real n>=32 put m=n+1,L=log n,H=1+L and define

    b=4/pi^2,r=log(5/2)+1/18,
    Da=[(52/pi^2)H+7]/n+20H/(pi*n^2),
    KD={ [6+16/(3pi)]H+2/pi }/n,
    epsilon=3pi/(2m),ell=-log(sin epsilon),
    W=[3log m+log2+2log pi+2]/(pi*m),
    C=1+8a0*m/(3pi),
    Gamma_b=p0[1+log(1+C/p0)],
    gamma_b=1+log(1+C/p0)-C/(p0+C),
    MA_b=p0/pi+4a0/pi^2,
    VB_b=23+[3Gamma_b+(2p0+6P0)ell+26a0+20]/pi,
    CB_b=6+(4+4a0/exp(1))/pi,
    G_env=7L*MA_b/m+VB_b/(2m)
              +(4/m)[7+(P0/pi)(5+2log(2m))]+2CB_b/m,
    D_env=a0*Da+10/n^2,
    R6_env=[21+21a0+2L+((1+48p0)H+24p0)/pi]/n
                                                +(317+5/12)/n^2,
    Dmesh_b=4w0/pi+a0*b*log pi,Zmesh_b=Dmesh_b+a0*b/n,
    M_env=a0*b(2L+2r)/n
       +[Dmesh_b+a0*b(L+1/n)]/(4n^2-1)+a0*b/(2n-1)^2
       +[Zmesh_b+a0*b(log(n+1/2)+2)]/[4(n-1/2)^2].

The FINAL coefficients for the new slope3 in (4) are

    C_b=D_env+G_env+R6_env+M_env,
    C_s=eta{7L/(pi*m)+(3gamma_b+2ell)/(2pi*m)
                                  +(48H+24)/(pi*n)}
                      +3{(log2+4log pi)/(pi*m)+W},
    C_l=[9ell+12(5+2log(2m))]/(pi*m).                    (5)

To check every charge, apply the E08 physical theorem FIRST:
CEphi=Dphi+Gphi+C6phi+Mphi+dW. Its literal complete formulas are repeated
in E13 section2. All a and ce+cd coefficients are nonnegative, giving
Dphi<=D_env,Mphi<=M_env,CB<=CB_b. The entropy
Gamma(p,a)=p[1+log(1+(1+8am/(3pi))/p)] increases with a and is concave
in p. Its tangent at p0, with positive slope gamma_b and positive intercept
p0*C/(p0+C), gives Gamma<=Gamma_b+eta*gamma_b sqrt(v), also at p=0.

The sqrt(v) increments of the original Gphi are
eta*7L/(pi*m), eta(3gamma_b+2ell)/(2pi*m),
3log2/(pi*m),12log pi/(pi*m). The two retained-row p,q increments give
eta(48H+24)/(pi*n). The complete scalar log gives3W. These are exactly
C_s. The P-dependent VB term gives9ell*v/(pi*m), and the P-dependent
holes give12(5+2log(2m))*v/(pi*m); these are C_l. Every base term is
in C_b. The separate ordinary KD*P gives P0*KD+3KD*v. Thus (1) follows.

The full M_env retains its U0/D0, n/m displacement, H2 and terminal
tails. All SIX original labels and every original hole are those of E08.
This is an absolute envelope; no signed cross-component cancellation or
relative-error theorem has been substituted for a physical bound.

### 3. Scalar directions, global model and the whole origin charge

All coefficients in (5),KD are positive/decreasing on real n>=32.
For completeness the only nonlinear derivative checks are
m*ell'=epsilon*cot epsilon<=1<ell,
m*Gamma_b'=p0*c1*m/(p0+C)<p0<=Gamma_b and
m*gamma_b'=c1*m*C/(p0+C)^2<1<gamma_b,c1=8a0/(3pi)>0.
Thus ell/m,Gamma_b/m,gamma_b/m decrease. All other terms are positive
linear-log/inverse-power terms. The full mesh splits into the positive
terms used in E13; its last logarithmic derivative has numerator
(n-1/2)/(n+1/2)-2log(n+1/2)<0. No difference of two decreasing functions
or CEphi/u ordering is used.

The GLOBAL accepted master, valid through rho=pi, gives

    M_infty(0,L)-M_infty(phi,L)>=u(Tmodel+j)-t0*p,
    j>23/250,t0=2log2/pi.

It drops only the known nonpositive mixed-model term. It is not E11's
local central model used outside its radius. For the WHOLE actual origin,
define EXACTLY the accepted n>=32 E08 allowance

    D=Da+10/n^2,
    Mesh=b(2L+2r)/n+[4+b(L+1/n)]/(4n^2-1)+b/(2n-1)^2
                       +[5+b(log(n+1/2)+2)]/[4(n-1/2)^2],
    Bout=pi[L+25log(2m)+193/3]/(8m^2)+1/(8n^2),
    e0=D+Mesh+Bout+[71/n^2-22/(45m)]_+.

Then E_n(0)>=-e0 and e0 is positive/decreasing for real n>=32.
The exact gap is Lambda_c-S=M_infty(0)-M_infty(phi)+E(0)-E(phi).
Insert (1),(3),(4),u=u1+v and this lower bound to obtain
Lambda_c-S>=G_b+Kv-A sqrt(v). The WHOLE e0 is charged once,
not u*e0. No finite-origin sign or limiting-origin substitution is used.

### 4. Generic implication and its all-n scope

If K>0, exact square completion gives
Kv-A sqrt(v)=K(sqrt(v)-A/(2K))^2-A^2/(4K), proving the stated F bound.
Since Tmodel increases, C_l,KD decrease, K increases. G_b increases and
A>0 decreases because their complete positive costs decrease. Therefore
F increases wherever K>0. This proves the sufficient implication for any
separately assigned legitimate N. It evaluates no sign at a base, asserts
no true-gap minimum and supplies no statement about other phase regions.
Consistent substitutions j*=23/250,t*=221/500 may weaken the ORIGINAL
master pointwise and then be used throughout the whole formula. No such
degree-specific substitution or endpoint evaluation is made here.

## Checks, scope, open items and history

No scientific source/script/import/scalar/endpoint/phase/degree/threshold/
native/quadrature/build/control/pack job. No historical priority or new model
claim. Geometry/finite envelope need no PD-T271 enclosure; the completed
model j/master retains that accepted dependency explicitly. Any later base
sign and complete physical near/corner cover need separately registered
claims and distinct review. Half-near320 remains unchanged.

2026-11-07, requested Sol xhigh, serving metadata unexposed. Supplied rule/input
4a5de2012bad94601c713b2ff5517f2e3fb80af2. Full gate, separate root release,
prospective exact caps before final proofs and all failed/deferred alternatives
are in ideas/attempts F01-seam-domain.md. Only owned new prose changed.


## Root disposition after distinct review —2026-11-07

Root adopts the written mathematical statement at its exact quantifiers and named dependencies. The original frozen proof/interface prefix is preserved and identified in [F01 independent mathematical review](../independent-checks-F01-seam.md), final13512B SHA25639dcb7fbf90e619f07a99ecb75b5f533722e9c3deec62d0b2ca0d5eb6a960313. This supplies no smaller onset, new finite degree, novelty/priority verdict, protocol waiver or readiness. Final Claude review remains separate.
