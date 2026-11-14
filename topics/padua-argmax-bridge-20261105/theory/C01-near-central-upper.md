# PD-T?argmax-bridge-codex-C01-near-01 — An explicit two-phase central cancellation modulus

ID kind: PD-T. Aliases: positive root integral; translated coalescing pole;
fractional/entropy central upper. Split from: N1-19's OPEN continuous residual
comparison. Split into: none. This is a supporting component estimate, not a
proved phase case of the complete Q_n comparison.

## Statement

Let alpha,beta>=0, rho=alpha+beta<=1/2, r2=alpha²+beta²,
a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta, u=p/2. For
0<epsilon<=pi/2 set

    s0=a*tan(epsilon/2), sL=s0+q/2, sR=abs(s0-q/2),
    J(u,s,epsilon)=I((u-s)/2,(u+s)/2,epsilon),

where I has exactly N1-14's normalization. Define the finite improper integral

    E_c(alpha,beta)=pi^-2 integral_0^(pi/2)
       [J(u,sL,epsilon)+J(u,sR,epsilon)
                         -4s0*log(sin epsilon)] d epsilon.

With vanishing terms defined as zero at a zero phase, the directional bound is

    E_c <= (15/32)*alpha^(3/2)
         +(4/9)*alpha²[1+log(1/alpha)]
         +(1/9)*beta²[3/2+log(1/beta)].                 (1)

In particular

    E_c <= (15/32)*rho^(3/2)
                    +(7/9)*r2+(4/9)*r2*log(1/rho).   (2)

For the actual two folded central cancellation integral

    Ic(alpha,beta)=pi^-2 integral_0^(pi/2)
                   [J(u,sL,epsilon)+J(u,sR,epsilon)] d epsilon,

one consequently has

    Ic(alpha,beta)-Ic(0,0)
       <= (15/32)*rho^(3/2)+r2+(r2/2)*log(1/rho).     (3)

All bounds are uniform on the closed phase triangle. These are bounds for the
specified whole central integrals; the fixed finite-n model's retained central
cell endpoints and exact central rows still need a combined phase estimate.

## Status and dependencies

Overall status: **PROVED**, analytic developer result. Independent review and
the formal Claude audit are separate. Dependencies: N1-14's exact same-sign
entropy and opposite-sign integral formulas and their separation derivative;
N1-05 for normalization. All algebra needed for the new bound is below.
No fitted constant, external theorem or mathematical computation is a premise.
The model is unchanged; this is an inequality for one of its existing integrals.

## Proof

### 1. A positive majorant valid on both coefficient-sign regimes

Put E(u,s,e)=J(u,s,e)-2s log(sin e), and for u,s>=0 define

    H(u,s,e)=2 integral_e^(pi/2)
                  sqrt((u²-s² sin² t)_+)/sin t dt.    (4)

For fixed positive e this is finite, nonnegative and decreasing separately in
s and e. Its positive-part square root handles root collisions continuously.
We claim E<=H everywhere. If s>u, N1-14 gives J=2s log(sin e)
when s sin e>=u. Otherwise its derivative identity gives exactly

    E_e=-2 sqrt(u²-s² sin² e)/sin e,
    E(u,s,arcsin(u/s))=0.

Integration proves E=H for s>u. The same equality holds at s=u by continuity
(both sides then equal -2u log(sin e)). For s<u, N1-14's entropy formula
gives J<=0, independent of e. Also

    sqrt(u²-s² sin² t)>=s cos t,  0<t<=pi/2.

Thus H>=-2s log(sin e)>=E. The case u=0 follows directly, including s=0.
These arguments also establish integrability of all quantities below; bounds
of the form constant times 1+abs(log e) suffice at zero.

### 2. Translate the right coefficient without enlarging the fractional constant

Let b=2 arctan(q/(2a)). Since cos alpha<=1 and sin beta>=0,

    beta<=b<=16 beta/15,                              (5)

where the upper bound uses a>=15/16 and arctan x<=x. At beta=0 set b=0.
For e>=b, tangent addition implies

    sR=a[tan(e/2)-tan(b/2)]>=a*tan((e-b)/2).

Monotonicity of H in its two arguments gives

    E(u,sR,e)<=H(u,a*tan((e-b)/2),e-b).               (6)

For 0<e<b, use J<=0 and 2sR<=q to obtain E(u,sR,e)<=-q log(sin e).
The left coefficient always has E(u,sL,e)<=H(u,a*tan(e/2),e).
Finally sL+sR>=2s0 and log(sin e)<=0, so

    J(u,sL,e)+J(u,sR,e)-4s0 log(sin e)
                     <=E(u,sL,e)+E(u,sR,e).

Integrating (6), translating e-b, and enlarging a positive integral gives

    pi² E_c <=2 integral_0^(pi/2) H(u,a*tan(e/2),e) de
                      +q integral_0^b -log(sin e) de. (7)

No phase derivative across a moving root was taken. In particular the right
pole shift costs a quadratic entropy term, without doubling a root width or
introducing a term linear in beta.

### 3. Bound the unshifted root integral

For alpha>0 put tau=u/a and theta=2 arctan tau. The exact inequalities are

    alpha<=theta<=16 alpha/15,
    0<tau<=8 alpha/15<=4/15,
    a*tau^(3/2)=u^(3/2)/sqrt(a)<=2 alpha^(3/2)/sqrt(30). (8)

The first lower bound follows from
tau=sin alpha/(cos alpha+cos beta)>=tan(alpha/2). We have 2theta<pi/2.
On 0<e<2theta, (4) and sqrt((u²-...)_+)<=u imply

    H(u,a*tan(e/2),e)<=2u log(cot(e/2))<=2u log(2/e).

Hence

    integral_0^(2theta) H de
       <=4u theta[1+log(1/theta)]
       <=(32/15) alpha²[1+log(1/alpha)].              (9)

For e>=2theta put s=a tan(e/2), lambda=u/s. Then
lambda<=tau/tan theta=(1-tau²)/2<=1/2. If s sin e>=u, H=0.
Otherwise substitute y=sin t, then z=y/lambda, into (4). With
x=s sin e/u=(1-cos e)/tau in (0,1), this gives

    H=2u integral_x^1 sqrt(1-z²)/[z sqrt(1-lambda²z²)] dz
      <=(4u/sqrt(3))*h(x),
    h(x)=integral_x^1 sqrt(1-z²)/z dz.                (10)

The change x=(1-cos e)/tau has
de=sqrt(tau) dx/[sqrt(x)*sqrt(2-tau*x)]. Enlarging the positive x-domain to
(0,1), and using 2-tau*x>=2-tau, bounds the remaining integral by

    4a*tau^(3/2)/sqrt(3*(2-tau)) * integral_0^1 h(x)/sqrt(x) dx.

Tonelli's theorem for the nonnegative elementary integrand gives

    integral_0^1 h(x)/sqrt(x) dx
       =2 integral_0^1 sqrt(1-z²)/sqrt(z) dz
       =4 I4,  I4=integral_0^1 sqrt(1-y^4)dy<9/10.    (11)

The last inequality follows from sqrt(1-v)<=1-v/2, integrated at v=y^4.
After the factor 2/pi² from (7), (8)--(11) give a fractional contribution
strictly below

    [64 I4/(pi² sqrt(156))]*alpha^(3/2)
                    <(15/32)*alpha^(3/2).           (12)

For the final numerical inequality, pi²>197/20 and sqrt(156)>312/25 give
64*(9/10)/(pi² sqrt(156))<1200/2561<15/32; the last comparison is
38400<38415. Thus no decimal or numerical integral is used for this constant.
The contribution of (9), including 2/pi², is below
(4/9)alpha²[1+log(1/alpha)], since pi²>48/5.

### 4. The beta translation cost and the origin normalization

By sin e>=2e/pi on [0,pi/2], (5), q<=beta and log(pi/2)<1/2,

    q integral_0^b -log(sin e) de
       <=q*b[1+log(pi/(2b))]
       <=(16/15) beta²[3/2+log(1/beta)].              (13)

Division by pi² and pi²>48/5 gives the last term of (1). All zero-phase
cases follow directly or by x²log(1/x)->0, proving (1) everywhere.

To obtain (2), use alpha^(3/2)<=rho^(3/2) and

    sum_(x=alpha,beta) x² log(rho/x)<=rho²/e<3r2/4.

Indeed (x/rho)log(rho/x)<=1/e, rho²<=2r2 and e>8/3. The two logarithmic
coefficients in (1) are at most 4/9; its nonlogarithmic quadratic part is at
most (4/9)r2. Therefore the total quadratic bound is (7/9)r2 and its
log(1/rho) coefficient at most 4/9, as stated.

At the origin Ic(0,0) is the integral of 4tan(e/2)log(sin e)/pi² and is
nonpositive. Since tan(e/2)<=e and -log(sin e)<=log(pi/(2e)),

    -Ic(0,0)<=4/pi² integral_0^(pi/2) e log(pi/(2e))de=1/4.

The baseline in E_c is a*Ic(0,0), so

    Ic(alpha,beta)-Ic(0,0)=E_c+(a-1)Ic(0,0)
                         <=E_c+r2/16.

Use 7/9+1/16=121/144<1 and 4/9<1/2 to prove (3).

## Budget meaning and remaining work

The explicit fractional coefficient 15/32 is less than one half. Together
with the stated quadratic and entropy coefficients, this central integral
has a small enough scalar envelope to be useful against N1-16's loss at
n=10^6. This sentence does not charge that entire loss to this component:
the other Q_n components still need bounds and a joint allocation.

The endpoint finite-h rows, both retained strip constants, the regularized
pole numerator integrals, endpoint cancellation residue, jump integrals,
finite central cells/rows and seam corrections have not been bounded in
phase here. The complete Q_n-G_n inequality, C1 and any argmax onset remain
OPEN. No finite energy extrapolation, second correction or model replacement.

## Checks, sources and history

Analytic development only; no mathematical computation or numerical integral.
Only existing locally proved identities are used. Independent checking is
requested on this new file; it does not replace the formal Claude audit.
2026-11-06, rules/input `4b728b04216a5490910780bc609a82b853058426`;
Codex, parent-assigned Astra ultra, serving metadata unexposed. Candidate
and unexecuted computational contract: ../ideas/C01-near.md.
