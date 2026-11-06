# PD-T?argmax-bridge-codex-D24-local — A true-constant modulus through radius three quarters

ID kind: PD-T. Aliases: quarter-cutoff pole-functional increment;
extended directional root modulus; completed constant on rho<=3/4.
Split from: D24 fixed far-split candidate.
Split into: D24-far-constant gives its standalone far consequence.

## Statement and status

Use EXACTLY D02/D10's continuous completed constant C_infty, with
nonnegative phases x=alpha,y=beta,rho=x+y<=3/4. Define

    r2=x²+y², a=(cos x+cos y)/2, u=1-a,
    p=sin x,q=sin y,e=x+y,d=x-y,
    c_e=cos(e/2),c_d=cos(d/2),
    c=1/3+(4/pi²)(log²pi-log²2).

With f,H,E_infty as in the accepted C08/D10 scalar and endpoint
definitions, and E_c defined below, the SAME exact decomposition holds:

    C_infty=E_infty+c_e H(d)+c_d H(e)-c*a+E_c.     (1)

It satisfies

    [C_infty-E_c](x,y)-[C_infty-E_c](0,0)
          <=19r2/24,                             (2)
    E_c<=(8/15)x^(3/2)+(1/2)x²[1+log(1/x)]
                         +(1/8)y²[3/2+log(1/y)].  (3)

All zero logarithmic products are interpreted continuously as0.
In particular adding(2)--(3) gives a directional upper for
C_infty(x,y)-C_infty(0,0) on this NEW CLOSED domain. Separate
absolute phases give the corresponding signed statement.

Status: **PROVED analytic developer extension**, by the proof below;
distinct independent mathematical review remains necessary before
adoption. No scalar/numerical premise or finite-degree conclusion.
The old D10 near theorem and constants are unchanged on rho<=1/2.

## Dependencies and the exact domain check

D10-global-constant supplies the FULL-domain finite-part decomposition
and weighted endpoint inequality. C08-far-pole-functional supplies the
global periodic scalar functional H, f>=f(0)>0, global semiconcavity
and elementary kernel bound. D10-relative-constant's scalar reciprocal
series establishes |f''''|<9/2 on|x|<=1, independently of any two-phase
near-domain hypothesis. C06-far-compact-error section2 reconstructs
the generic J identities on ALL u,s>=0,0<epsilon<=pi/2; those full
parameter identities, not N1-14's near-only application bounds, are
used here. The positive majorant/translation proof from C01 is
reconstructed below with NEW constants and domain checks.

On rho<=3/4, cos t>=1-t²/2 gives

    a>=1-r2/4>=1-rho²/4>=55/64.                  (4)

For the two folded endpoint halves0<z<=pi/2, the complete kernel
numerator is2a(1+cos z) plus a signed q*sin z minus p*sin w.
Uniformly in its row angle w it is bounded below by

    2a-p-q>=55/32-3/4=31/32>0.                  (5)

Here p+q<=x+y<=3/4. The cotangent coefficient T=2a*cot(z/2)
also satisfies T>p+q, so both cancellation channels are opposite-
sign and in their no-root branch: (T-q)*sin z>=2a-q>p.
The FULL generic J identity therefore gives EXACTLY

    I_L(z)+I_R(z)=4a*cot(z/2)*log(sin z),
    0<z<=pi/2.                                  (6)

Thus the positive-complete-numerator identity needed in D10 is now
proved through3/4, not borrowed from its old1/2 domain.

On the central half write epsilon=pi-z,0<epsilon<=pi/2, and set

    v=p/2,s0=a*tan(epsilon/2),
    sL=s0+q/2,sR=abs(s0-q/2),
    J(v,s,epsilon)=I((v-s)/2,(v+s)/2,epsilon),
    E_c=pi^-2 integral_0^(pi/2)
       [J(v,sL,epsilon)+J(v,sR,epsilon)
                           -4s0*log(sin epsilon)]d epsilon. (7)

These parameters are the exact generic full-phase central parameters.
All root/zero cases are finite entropy/positive-part limits. Equation(6)
and(7) identify the SAME finite-part cancellation as-c*a+E_c; the
baseline antiderivative and endpoint logarithms are exactly those of
D10-global-constant. Its scalar pole part is c_e H(d)+c_d H(e) on
the whole diamond. This proves(1) with no changed cutoff/model/error.

## Scalar H increment on the larger interval

The accepted all-real functional identity is

    H(x)=lambda0*f(x)+(1/pi)integral_0^pi D_v f(x) K(v)dv,
    lambda0=(2/pi)log(4/pi),0<lambda0<1/(2pi),
    D_t f(x)=f(x+t)+f(x-t)-2f(x),
    K(v)=1/[2sin(v/2)]<=1/v+v/16.

Global semiconcavity gives D_x f(v)<=A*x²,A=3/pi²,
including the NEGATIVE periodic derivative atoms, and f>=f(0) gives
D_x f(0)>=0. For0<=x<=3/4 split the v integral at1/4, rather than
the old1/2. Subtracting the x=0 identity and using evenness gives

    H(x)-H(0)=(lambda0/2)D_x f(0)
          +(1/pi)integral_0^pi[D_x f(v)-D_x f(0)]K(v)dv. (8)

On0<=v<=1/4 every argument in the second difference of f'' lies
in[-1,1], since x+v<=1. The known |f''''|<9/2 there and the triangular
second-difference identity show |(D_x f)''(v)|<=(9/2)x². Since
(D_x f)'(0)=0, integration gives

    |D_x f(v)-D_x f(0)|<=(9/4)x²v².

On the remaining v>=1/4, use the GLOBAL upper D_x f(v)<=A*x²
and favorable subtraction D_x f(0)>=0. No derivative across an atom
is taken. The exact kernel estimates are

    integral_0^(1/4) v² K(v)dv<=1/32+1/16384=513/16384,
    integral_(1/4)^pi K(v)dv=log cot(1/16)<log16<14/5.

Also D_x f(0)<=A*x². Hence the x² coefficient in(8) is at most

    A/(4pi)+(9/(4pi))*(513/16384)+(A/pi)*(14/5)
       <9150/29791+46170/2031616
       <31/100+23/1000=333/1000<1/3.              (9)

Only pi>31/10 and log2<7/10 enter the displayed rational bounds.
Thus H(x)-H(0)<=x²/3 for|x|<=3/4. This is a NEW proof of its
enlarged domain, using the old all-real and local-scalar ingredients.
The identity at zero and f>=f(0)>0 imply H(0)>0. Since c_e,c_d
are nonnegative and<=1, (9) gives

    c_e H(d)+c_d H(e)-2H(0)<=2r2/3.

D10's full-domain weighted endpoint inequality gives
E_infty-E_infty(0)<=-u/3, and its elementary constant c-1/3<1/2
is unchanged. Finally u<=r2/4. These inequalities prove(2).

## Positive central majorant and translation on rho<=3/4

Put E(v,s,epsilon)=J(v,s,epsilon)-2s*log(sin epsilon) and

    Z(v,s,epsilon)=2 integral_epsilon^(pi/2)
                       sqrt((v²-s²sin²t)_+)/sin t dt.

The full-range generic identities prove E<=Z for ALL v,s>=0:
for s>v integrate the exact separation derivative from the no-root
threshold; for s=v use continuity; for s<v the entropy formula gives
J<=0 and sqrt(v²-s²sin²t)>=s*cos t, so Z>=-2s log(sin epsilon)>=E.
The majorant is nonnegative and decreases separately in s,epsilon.
These statements include v=0,s=0 and root thresholds, with no inverse
phase or smoothness across a moving root.

Let b=2arctan(q/(2a)),theta=2arctan(v/a). Elementary half-angle
identities give

    y<=b<=y/a, x<=theta<=x/a,
    b<=rho,theta<=rho<=3/4<pi/4.                  (10)

For the first lower bounds use cos x<=1 or cos y<=1. For the upper
rho bounds, multiply tan(rho/2) by cos x+cos y: the result is
sin x+sin y, which dominates either numerator. Thus both angles
are in the needed interval, even at the axes. In particular2theta<pi/2.

For epsilon>=b, tangent addition gives
sR>=a*tan((epsilon-b)/2), and monotonicity bounds its E by the
unshifted Z with argument epsilon-b. For epsilon<b, J<=0 and
2sR<=q bound E by-q*log(sin epsilon). The left coefficient is
bounded by the unshifted Z. Finally sL+sR>=2s0 and log sin<=0.
Integrating these facts and enlarging the positive translated interval
proves EXACTLY

    pi² E_c<=2 integral_0^(pi/2)Z(v,a*tan(epsilon/2),epsilon)d epsilon
                     +q integral_0^b -log(sin epsilon)d epsilon. (11)

All integrals converge at zero by the ensuing bounds.

## The unshifted root integral with recomputed constants

For x>0 set tau=v/a. By(4) and x<=3/4,

    0<tau<=x/(2a)<=24/55,
    a*tau^(3/2)<=x^(3/2)/(2sqrt(2a)).              (12)

For0<epsilon<2theta, the square root bound by v yields
Z<=2v*log(cot(epsilon/2))<=2v*log(2/epsilon). Hence its integral
on that interval is at most4v*theta[1+log(1/theta)]. Since
theta>=x,theta<=x/a and x<=3/4<1, its contribution after multiplying
by2/pi² in(11) is at most

    [4/(a*pi²)]x²[1+log(1/x)]
      <=[256/(55*pi²)]x²[1+log(1/x)]
      <(1/2)x²[1+log(1/x)].                      (13)

For epsilon>=2theta, put s=a*tan(epsilon/2),lambda=v/s.
Then lambda<=tau/tan(theta)=(1-tau²)/2<=1/2, positive since tau<1.
If s*sin epsilon>=v, Z=0. Otherwise the substitutions y=sin t,
z=y/lambda give, with X=(1-cos epsilon)/tau in(0,1),

    Z<=(4v/sqrt3)h(X),
    h(X)=integral_X^1 sqrt(1-z²)/z dz,
    d epsilon=sqrt(tau)dX/[sqrt(X)*sqrt(2-tau*X)].

Enlarge the positive X domain to(0,1). Tonelli gives

    integral_0^1 h(X)/sqrt(X)dX=4I4,
    I4=integral_0^1 sqrt(1-t^4)dt<9/10.

The final strict bound follows from sqrt(1-v)<=1-v/2. Combining
with(12), the coefficient of x^(3/2) after2/pi² is at most

    16I4/[pi² sqrt(6a(2-tau))].

Here6a(2-tau)>=129/16>(14/5)². With pi²>197/20,
this coefficient is<720/1379<8/15; the last cross-product is
10800<11032. This proves the fractional term of(3).

The beta shift in(11), using sin epsilon>=2epsilon/pi,b>=y,
b<=y/a,q<=y and log(pi/2)<1/2, is at most

    [1/(a*pi²)]y²[3/2+log(1/y)]
      <=[64/(55*pi²)]y²[3/2+log(1/y)]
      <(1/8)y²[3/2+log(1/y)].                    (14)

Both(13),(14) use512<55*(197/20). At x=0 the root integral is0;
at y=0 the shift is0. Continuity of t²log(1/t) handles all zero
phases. Equations(11)--(14) prove(3), hence the claimed domain
extension. No old near theorem is invoked outside its literal range.
QED.

## Limits and provenance

This proves a standalone component/domain lemma for the TRUE completed
constant, with an unavoidable directional fractional term. It does
not prove a finite S error, actual-corner result, new onset, numerical
value or executable validity. D24-far-constant separately uses it only
on rho>=1/2, preserving D10's through-origin quadratic obstruction.
All old proofs/source/evidence remain unchanged. No mathematical
computation, scalar/phase sampling, native/quadrature/degree job or
new numerical premise occurred. 2026-11-06, parent-assigned Codex
gpt-6.1-sol xhigh20min PAPER block; rules/input
476208fe080cc79cae5b2578344b2e18f442a1e8, serving metadata unexposed.
