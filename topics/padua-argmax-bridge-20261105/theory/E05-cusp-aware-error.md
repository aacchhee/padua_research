# PD-T?argmax-bridge-E05-cusp-aware — Complete finite error on the microscopic cusp domain

ID kind: PD-T. Aliases: full directional zero-mask cusp; odd-board L2
Taylor bound; complete microscopic actual-origin error. Split from: E05's
full near-diamond cusp-aware upper target, which remains OPEN. Split into:
none; the scalar and zero-mask calculations below support this one local
parameter-domain theorem and do not assert completion of the broad target.

## Statement and status

For EVERY integer n>=32 put m=n+1, L=log n and

    rho=|alpha|+|beta|,
    a=(cos alpha+cos beta)/2,
    ell_n=(nm)^(-1)sum_(k=1)^floor(n/2)cot(k*pi/n),
    E_n(phi)=S_n(phi)-M_infty(phi,L).

Use EXACTLY the corrected primitive and unchanged completed model of D13
and accepted E03-unified-error. Throughout the CLOSED shrinking diamond

    rho<=1/(n+1)^2,

the COMPLETE actual-origin error obeys

    E_n(phi)-E_n(0) <= ell_n*|alpha|+2*rho/n.             (1)

No ordinary row, retained endpoint, moving-pole, outer-cell, scalar mesh
or completed-constant component is omitted from E_n. This is a genuine
finite parameter case, not an asymptotic in which n is fixed or phase is
fixed. It is NOT the proposed full rho<=1/2 cusp-aware theorem and does
not by itself improve any argmax onset or finite certified range.

Overall status: **PROVED developer PAPER theorem**, distinct mathematical
audit/root adoption pending. The original full-diamond cusp-aware upper
and D13's logarithmic-linear absolute target remain **OPEN**, not PARTIAL
merely on the strength of this supporting local theorem.

The proof also determines the full principal cusp required in (1): at
every fixed n its directional functional is ell_n*|A| in direction(A,B).
There is no beta linear cusp. This follows from the actual zero mask,
not an exchange of n and m. The complete-error directional limit is
derived at the end using the TRUE model, including its fractional term.

## Definitions, dependencies and conventions

Let N=nm and Gamma^-={(j,r):0<=j<2n,0<=r<2m,j+r odd}. Define

    h_0=1,h_i=2 for i>0,
    D_n(u,v)=sum_(i+k<=n)h_i*h_k*cos(iu)*cos(kv),
    Gpoly_n(u,v)=D_n(u,v)-cos(nu),
    F_jr(alpha,beta)=(-1)^j Gpoly_n((j*pi+alpha)/n,
                                         (r*pi+beta)/m)/2,
    S_n=(1/N)sum_Gamma^- |F_jr|.

The highest first-coordinate coefficient is ONE. Apparent rational poles
always have their literal finite-polynomial values. The equivalent
physical reflection formula retains endpoint factors e_j,f_r=1/2 at
their respective endpoints and1 otherwise, and all four phase reflections:

    S_n=(1/N)sum_(0<=j<=n,0<=r<=m,j+r odd)
              e_j*f_r*sum_(sigma,tau=+/-1)|F_jr(sigma alpha,tau beta)|.

The exact same-degree origin is S_n(0)=Lambda_c(n). All model quantities
use the inherited separate-absolute-phase convention. With x=|alpha|,
y=|beta|, ce=cos((x+y)/2),cd=cos((x-y)/2), the complete model is

    M_infty=B0 L^2+b_full L+C_infty, B0=4a/pi^2,
    b_full=2U0/pi+[8a log2+4a loga+2(x sinx+y siny)]/pi^2,
    U0=ce*f(x-y)+cd*f(x+y),
    f(z)=Phi0(1/2+z/(2pi)).

Accepted dependencies: PD-T216/220 for literal normalization, numerator
and zero mask; D13 and E03-unified for the complete error/model telescope;
D10-near for the exact C_infty decomposition and local fourth derivative;
C08-far-pole-functional for f's range/minimum and scalar integral; C04-near
for the distributional second-derivative bound INCLUDING negative atoms;
C01-near-central-upper and N1-round6-central-log for the exact root/entropy
formulas. No unaccepted E04 or E05 helper assertion is a premise. E03
retained-origin and outer/log theorems are used only as comparison context.

## Proof

### 1. Full directional cusp from the literal zero mask

At the origin the physical-mesh zero mask is precisely

    Z={r=m, j<n, j+n even}.

The common endpoint(j,r)=(n,m) instead has actual polynomial value n.
Away from collisions the accepted corrected identity is

    F=[a(1+cosv)-(sin alpha/2)sin u+(sin beta/2)sin v]
                                                    /(cosu-cosv).

At each point of Z its denominator is 1+cosu>0. Differentiating the
COMPLETE numerator at the origin, with u=(j*pi+alpha)/n and
v=(m*pi+beta)/m, gives

    partial_alpha F(0)=-(1/2)tan(j*pi/(2n)),
    partial_beta F(0)=0.                              (2)

In particular the motion of v has zero first derivative in 1+cosv, and
the beta sine channel has sinv=0 there. Both unequal meshes have been
retained. There is no beta derivative hidden in a pole convention.

Every nonzero-origin polynomial sample has a smooth absolute value in
some fixed-n neighborhood. Its linear terms cancel after pairing j with
-j and r with-r on the periodic board, equivalently after the four
physical reflections. At zero samples, the first-order absolute value
is the absolute value of the linear form (2). Its endpoint factor f_m=1/2
and four reflections contribute e_j*tan(j*pi/(2n))*|alpha|/N. Set
j=n-2k; the j=0 endpoint, when present, has zero derivative. Therefore
the ENTIRE principal cusp is exactly ell_n*|alpha|, for every direction.
The common finite collision contributes only a smooth term, not a cusp.

### 2. No other finite sign changes on rho<=1/m^2

It suffices to treat signed phases on their full radial segment; all
estimates below use rho. For any periodic row r!=m, its origin distance
from pi modulo2pi is at least pi/m. After phase displacement,

    dist(v,pi+2pi Z)>=(pi-|beta|)/m>=3pi/(4m).

Here |beta|<=1/m²<pi/4. The sine chord gives
1+cosv>=9/(8m²). Also a>=15/16 on rho<=1/2 and
|sin alpha|+|sin beta|<=rho. Thus its doubled numerator satisfies

    2a(1+cosv)-sin alpha*sin u+sin beta*sin v
                   >=135/(64m²)-rho>0.              (3)

At the origin a noncentral equal-cosine collision is impossible: clearing
denominators in u+/-v=2ell*pi gives the integer mismatch
mj+/-nr-2Nell. Coprimality leaves only the common endpoint(n,m) on
Gamma^-. Every other mismatch has absolute value at least1, hence angular
gap at least pi/N. The phase perturbation is at most rho/n<=1/(nm²),
strictly below pi/N. No noncentral denominator changes sign on the radial
segment. With (3), every such sample retains its nonzero-origin sign.

For the sole nonzero-origin central sample(n,m), use its polynomial,
not that rational expression. Its complex Fourier coefficient absolute
sum is2N, as verified below. Consequently its radial derivative has
absolute value at most N*rho. The total displacement is at most
N/m²=n/m<n, so its value cannot cross zero from its origin value n.
All other central samples belong to Z and their signs need not be fixed.
Thus every nonzero-origin sample has the sign required for Taylor below.

### 3. An exact odd-board L2 estimate for the summed Taylor remainder

In complex Fourier notation, D_n has coefficient1 at every integer
frequency(k,l) in |k|+|l|<=n. There are2N+1 such frequencies.
Gpoly has instead coefficient1/2 at(+n,0),(-n,0); all others are1.
Hence its coefficient absolute sum is2N and squared sum is2N-1/2.
This is where the corrected top coefficient ONE matters.

Let mu be the probability average over Gamma^- (which has2N points).
Character summation shows that a frequency difference survives that
average only if it belongs to either

    (2n Z,2m Z), or (n+2n Z,m+2m Z).

The second class has least l1 length n+m=2n+1, exceeding the maximum
2n difference between our frequencies. In the first class the only
nonzero possible differences are(+/-2n,0), pairing the two top modes.
This argument applies to shifted meshes too: shifts only multiply an
alias cross term by a unit complex phase.

Along the radial segment(s alpha,s beta), put
theta_(k,l)=k*alpha/n+l*beta/m, so |theta_(k,l)|<=rho.
The second radial derivative multiplies the Fourier coefficient by
-theta². The diagonal squared sum is at most(2N-1/2)rho^4; the sole
possible alias pair costs at most rho^4/2. Since F=+/-Gpoly/2,

    mu[|F''(s)|²] <=(N/2)rho^4,
    (1/N)sum_Gamma^- |F''(s)| <=sqrt(2N)*rho².          (4)

Cauchy-Schwarz gives the second line. Integrate its Taylor remainder
against1-s on[0,1]. By section2, nonzero-origin absolute values have
fixed signs. For zero samples, ||z+r|-|z||<=|r| controls the absolute
value after its linear term. Section1 cancels the signed nonzero linear
sum and identifies the zero linear sum. Therefore

    |S_n(phi)-S_n(0)-ell_n*|alpha||
        <=sqrt(N/2)*rho²<=n*rho².                     (5)

The last inequality uses m<=2n. This bound is uniform on the entire
stated closed microscopic diamond, including both phase axes and all
zeros in Z. It is not a claim that the finite signs are fixed farther out.

### 4. A lower estimate for the TRUE completed constant

An upper estimate for C_infty would have the wrong sign in E=S-M.
We derive the required lower estimate from D10's exact near decomposition.
For this paragraph set x=|alpha|,y=|beta|,r2=x²+y² and e=x+y,d=x-y.
Use the scalar functional Hfun to distinguish it from logn notation:

    C_infty=E_infty+ce*Hfun(d)+cd*Hfun(e)-c*a+E_c,
    E_infty=a/3+a*C(1/2+d/(2pi))*C(1/2+e/(2pi))/pi²,
    c=1/3+(4/pi²)(log²pi-log²2)>0.                    (6)

The accepted reciprocal-pair series has C(t)>=C0=C(1/2),C0<4.
Thus E_infty>=a E_infty(0), E_infty(0)<3 and
E_infty-E_infty(0)>=-3r2/4. The -ca term has nonnegative increment.

Here are explicit lower controls for the two remaining pieces. C08 gives
f(z)>=f(0)>0 and Hfun(0)<1/2. Its exact integral and D10's local bound are

    Hfun(x)=lambda0*f(x)+(1/pi)integral_0^pi
           [f(v+x)+f(v-x)-2f(x)]K(v)dv,
    K(v)=1/[2sin(v/2)], lambda0>0,
    |D_x f(v)-D_x f(0)|<=(9/4)x²v², 0<=v<=1/2, |x|<=1/2,

where D_x f(v)=f(v+x)+f(v-x)-2f(v). C04's complete distributional
inequality f''<=3/pi² and periodicity imply
Var_period(f')<=12/pi<4: the derivative measure has mass zero, and
its positive part is bounded by(3/pi²)dv. The elementary integrated
second-difference identity therefore gives

    integral_(one period)|D_x f(v)|dv<=4x².

Moreover0<=D_x f(0)<=3x²/pi²<x²/3. In Hfun(x)-Hfun(0) the lambda0
term is nonnegative. On0<v<=1/2 use K<=pi/(2v); on[1/2,pi] use
K<3 and integral K<10. It follows that

    Hfun(x)-Hfun(0)
       >=-[9/64+(12+10/3)/pi]x²>=-6x².               (7)

This includes the negative derivative atoms through the full variation
measure; no globally smooth periodic profile is assumed. Restoring
ce,cd>=0 and their cosine losses gives

    ce Hfun(d)+cd Hfun(e)-2Hfun(0)>=-(97/8)r2.        (8)

Indeed the two increments cost6(d²+e²)=12r2, while
(2-ce-cd)Hfun(0)<=(d²+e²)/16=r2/8. If Hfun(0) were negative,
that latter term would only improve the lower bound.

For the central piece retain its ACTUAL root/entropy integral. Let
p=sinx,q=siny,u=p/2,s0=a tan(v/2),sL=s0+q/2,sR=|s0-q/2|. Then

    pi² E_c=integral_0^(pi/2)
          [J(u,sL,v)+J(u,sR,v)-4s0 log(sin v)]dv.     (9)

For s>=u, C01's exact positive root representation gives
J(u,s,v)-2s log(sin v)>=0. For s<u, N1's exact entropy formula
gives J>=-2u log2, hence J-2s log(sin v)>=-2u log2.
The set sL<u has length at most p/a<=16rho/15, and the set sR<u
has length at most(p+q)/a<=16rho/15. Their total negative entropy
charge divided by pi² is at most rho²/4.

The only additional negative baseline term is
2(sL+sR-2s0)log(sin v)=4(q/2-s0)_+log(sin v).
It is supported on0<v<b=2arctan(q/(2a)), with y<=b<=16y/15,
and its coefficient is at most2q. Using the sine chord and
log(pi/2)<1/2 gives its absolute integral divided by pi² at most

    [32/(15pi²)]y²[3/2+log(1/y)]
                       <=(1/4)y²[3/2+log(1/y)].

Vanishing logarithmic products mean zero. Thus

    E_c>=-rho²/4-(1/4)y²[3/2+log(1/y)].             (10)

This lower bound retains both coefficient-sign regimes and every root
threshold. The favorable alpha fractional term was not assigned a false
quadratic upper or differentiated through a moving zero. Combining
(6),(8),(10) and r2<=rho² yields the safe lower estimate used here:

    C_infty(phi)-C_infty(0)
        >=-16rho²-(1/4)y²[3/2+log(1/y)].             (11)

### 5. Complete model lower bound on the microscopic domain

The exact b_full formula has U0>=f(0)(ce+cd),0<f(0)<=1.
Consequently U0-U0(0)>=-r2/4. Also a loga>=a-1 and x sinx,y siny
are nonnegative. Since1-a<=r2/4, pi>3 and log2<7/10,

    b_full(phi)-b_full(0)>=-rho²,
    B0(phi)-B0(0)>=-rho²/9.                         (12)

These are inequalities for the exact coefficient identities, not an
application of the separate C06 large-degree upper theorem.
Together (11)–(12) imply

    M_infty(phi,L)-M_infty(0,L)
      >=-rho²(L²/9+L+16)-(1/4)y²[3/2+log(1/y)].     (13)

For0<rho<=1/m²<1/n², the functions z²(3/2+log(1/z)) and
z(3/2+log(1/z)) increase on the required small interval. Therefore
the magnitude of the negative bound in(13), divided by rho/n, is at most

    L²/(9n)+(3L)/(2n)+131/(8n)<1.                  (14)

For completeness, on realn>=32 the functions L/n and L²/n decrease;
log32<4 gives L/n<1/8 and L²/n<1/2<1. Thus the left side is less
than1/9+3/16+131/256=1867/2304<1. These are analytic inequalities,
not a scalar or threshold job. Hence

    M_infty(phi,L)-M_infty(0,L)>=-rho/n.             (15)

Finally (5) gives S_n(phi)-S_n(0)<=ell_n|alpha|+rho/n, since
n*rho²<=rho/n on this domain. Subtract (15) to prove (1), with equality
interpreted weakly at rho=0. Every component of the completed model has
been retained; direct use of S and M avoids separate absolute row charges.

### 6. Directional interpretation and actual-origin conversion

At fixed n, (5) gives the finite primitive's full cusp with quadratic
remainder. The accepted D10 upper modulus is o(rho), while (11) is an
o(rho) lower bound. Smooth B0,b_full have zero first variation at the
origin. Thus for every real direction(A,B),

    lim_(t down to0)[E_n(tA,tB)-E_n(0)]/t=ell_n*|A|.

In particular beta has no missing principal cusp. This diagnostic does
not assert a uniform second derivative for the complete error: the model
has its genuine fractional alpha term.

For delta_a E=E(phi)-aE(0), u=1-a, the conversion is ALWAYS

    E(phi)-E(0)=delta_a E-uE(0)<=delta_a E+uE0(n).

Conversely the proved actual-origin inequality gives only
delta_a E<=ell_n|alpha|+2rho/n+uE0(n) when using |E(0)|<=E0(n).
No origin allowance is silently deleted or assigned the wrong sign.
The directional cusp is identical for both forms because u=O(rho²).

## Limits, retained alternatives and cheapest next paper task

The theorem stops at rho=1/m². Sign stability in section2 is not proved
past that domain, and the Fourier Taylor estimate by itself does not
control the added positive-part crossing terms there. The model's root
scale and finite row crossings start on comparable shrinking scales;
the fixed-n expansion cannot be extended to a fixed diamond by continuity.

The full proposed upper ell_n|alpha|+C*rho/n+K*(1+logn)*rho²/n on
rho<=1/2 remains OPEN. The disjoint helper's beta0 transported-positive-
part and rootstrip analysis may control the next region, but is not a
premise here. The cheapest next paper task is a uniform bound for the
first active noncentral sign bands just above rho~1/m², coupling their
discrete positive parts to the SAME completed root integral before any
absolute estimate. Both ordinary collision transport and the endpoint
e-grid remainder must be included. No full near or argmax conclusion is
inferred from this microscopic parameter case.

## Checks and history

Fresh gate and all candidates are in the same-stem idea/attempt. Own E03
complete registry baseline was reused only after exact current hash match;
all new immediate predecessor/negative scopes were refreshed. No external
theorem, historical priority, new mechanism, numerical premise or source
import. No scientific script/scalar/endpoint/native/threshold/phase/degree/
compile/pack job or Git/shared mutation occurred.

2026-11-07, input/rules91b3acea226cbe77f244e0b25296929acd637e53; requested
Astra ultra, serving metadata unexposed. This is a bounded PAPER result
within00:26:21–00:46:21 UTC, pending root's distinct audit. E03 files and
their adopted scopes remain frozen. Accepted global768/residual719 are
unchanged by this theorem; it supplies no new finite-degree enumeration.
