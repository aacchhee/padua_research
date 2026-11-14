# E13 — A joint radius/defect envelope for the full outer phase error

Provisional developer theorem, no global ID. Aliases: joint outer geometry;
square-root displacement envelope; radius-plus-u absolute comparison.
Status: **PROVED developer PAPER support and conditional outer reduction**;
distinct mathematical audit/root adoption pending. No degree endpoint is
chosen, evaluated or certified. This is a quantitative continuation of
E08/E09, not a new model or a signed finite-error cancellation theorem.

## 1. Exact domain, actual quantities and the claimed geometric bounds

Take the original corrected primitive S_n, TRUE completed model M_infty
and actual symbolic Lambda_c(n)=S_n(0). Every finite operator retains its
original unequal n,m=n+1 meshes, highest first-coordinate coefficient ONE,
endpoint weights and polynomial-continuous collision values. Separate
absolute phases give x=|alpha|,y=|beta|,rho=x+y, without exchanging meshes.
The present phase set is the ENTIRE CLOSED outer diamond

    x,y>=0, 1<=rho<=pi.

Put

    ce=cos(rho/2),cd=cos((x-y)/2),a=ce*cd=(cos x+cos y)/2,
    u=1-a,p=sin x,q=sin y,P=p+q,d=(q-p)_+,
    u1=47/384,a_0=1-u1=337/384,w_0=1+a_0=721/384,
    v=u-u1,p_0=12/25,P_0=24/25,eta=3/2.

Here a,ce,cd,p,q,d are nonnegative, a<=1 and P<=2. The exact new
geometry is

    v>=0, a<=a_0, ce+cd<=w_0,
    p,q,max(p,q)<=p_0+eta*sqrt(v),
    d<=|p-q|<=2sqrt(2v)<=3sqrt(v),
    P<=2sqrt(2u-u^2)<=P_0+4v.                         (1)

These are assertions at ACTUAL phases, not simultaneous fake physical
parameter values. Old caps p,q<=1, E09's f(u), P<=2 and sqrt(8u) remain
valid and may be intersected separately; they are unnecessary below.

### Proof of (1), including every branch

Set c=cos(1/2),u_min=1-c. Since ce<=c and cd<=1,
a<=c. The alternating cosine polynomial gives c<337/384, so
u>=u_min>u1 and v>=0. Also (1-ce)(1-cd)>=0 gives ce+cd<=1+a<=w_0.

First bound p; the q proof follows by the actual x/y symmetry of these
TRIGONOMETRIC quantities, not by swapping any finite operator meshes.
If 0<=x<=1/2, sine is increasing here and its alternating polynomial gives

    p<=sin(1/2)<1/2-1/48+1/3840=1841/3840<12/25.

If 1/2<=x<=1, then y>=1-x and cosine decreases on[0,pi]. Writing
h=x-1/2 in[0,1/2] gives

    a<=[cos x+cos(1-x)]/2=c cos h,
    u-u_min>=c(1-cos h)>=(47c/96)h^2.

The latter follows from 1-cos h>=h^2/2-h^4/24>=47h^2/96. Concavity
of sine on[0,pi] gives sin x<=sin(1/2)+c*h. Hence

    p<=sin(1/2)+sqrt(96c/47)*sqrt(u-u_min)
       <=p_0+eta*sqrt(v),

because u-u_min<=v and 96c/47<9/4 (already 384<423 suffices).
At h0 the estimate has its literal zero factor; no division by h occurs.

If x>=1, a<=(1+cos1)/2 and the alternating cosine polynomial give
u>=(1-cos1)/2>=11/48. When u<=1/4, cos x=2a-cos y>=1-2u>=1/2,
so p<=sqrt(3)/2<9/10. But

    v>=41/384>9/100,
    p_0+eta*sqrt(v)>12/25+9/20=93/100>9/10.

When u>=1/4, v>=49/384>49/400 and
p_0+eta*sqrt(v)>12/25+21/40=201/200>1>=p. Both arguments include
u=1/4. Thus all x branches, including x=pi, are covered.

For the difference, the exact identity is

    |p-q|=2ce*|sin((x-y)/2)|=2sqrt(ce^2-a^2).

Since ce<=c<a_0 and a<=a_0,
ce^2-a^2<=a_0^2-a^2=(a_0-a)(a_0+a)<=2v. This proves the d bound
without dividing by a or assigning a divergent endpoint value.

Finally Cauchy applied first to sines and then cosines gives

    P^2<=2(sin^2x+sin^2y)
       =4-2(cos^2x+cos^2y)<=4(1-a^2)=4(2u-u^2).

Let S(u)=2sqrt(2u-u^2),0<u<=1. It has
S'(u)=2(1-u)/sqrt(2u-u^2) and S''(u)=-2/(2u-u^2)^(3/2)<0.
At the fixed symbolic phase-defect parameter u1,

    S(u1)=sqrt(33887)/192<24/25,
    S'(u1)=674/sqrt(33887)<4.

These comparisons are exactly
33887*625=21179375<21233664=36864*576 and
674^2=454276<542192=16*33887. The concave tangent inequality gives
S(u)<=S(u1)+S'(u1)v<=P_0+4v on the ENTIRE u>=u1 interval. This
completes (1) by written integer/trigonometric algebra, without a phase,
degree or numerical endpoint test.

## 2. The complete explicit absolute-error envelope

For real scalar n>=32 set m=n+1,L=log n,H=1+L and define

    b=4/pi^2,r=log(5/2)+1/18,
    Da=[(52/pi^2)H+7]/n+20H/(pi*n^2),
    KD={ [6+16/(3pi)]H+2/pi }/n,
    epsilon=3pi/(2m),ell=-log(sin epsilon),
    W=[3log m+log2+2log pi+2]/(pi*m).

These are the unchanged accepted E08/D35/D07 quantities. Define the
following explicit positive functions with FIXED constants a_0,p_0,P_0,w_0:

    C(n)=1+8a_0*m/(3pi),
    Gamma_b=p_0*[1+log(1+C(n)/p_0)],
    gamma_b=1+log(1+C(n)/p_0)-C(n)/(p_0+C(n)),
    MA_b=p_0/pi+4a_0/pi^2,
    VB_b=23+[3Gamma_b+(2p_0+6P_0)ell+26a_0+20]/pi,
    CB_b=6+(4+4a_0/exp(1))/pi,
    G_env=7L*MA_b/m+VB_b/(2m)
          +(4/m)[7+(P_0/pi)(5+2log(2m))]+2CB_b/m,
    D_env=a_0*Da+10/n^2,
    R6_env=[21+21a_0+2L+((1+48p_0)H+24p_0)/pi]/n
                                           +(317+5/12)/n^2.

For the FULL mesh define

    Dmesh_b=4w_0/pi+a_0*b*log pi,
    Zmesh_b=Dmesh_b+a_0*b/n,
    M_env=a_0*b*(2L+2r)/n
       +[Dmesh_b+a_0*b*(L+1/n)]/(4n^2-1)
       +a_0*b/(2n-1)^2
       +[Zmesh_b+a_0*b*(log(n+1/2)+2)]/[4(n-1/2)^2].

Define the three FINAL envelope coefficients

    C_b=D_env+G_env+R6_env+M_env,
    C_s=eta{7L/(pi*m)+(3gamma_b+2ell)/(2pi*m)
                                      +(48H+24)/(pi*n)}
                     +3{(log2+4log pi)/(pi*m)+W},
    C_l=[12ell+16(5+2log(2m))]/(pi*m).                  (2)

Then for EVERY integer n>=32 and EVERY actual closed outer phase,

    CEphi(n,phi)<=C_b(n)+C_s(n)sqrt(v)+C_l(n)v,
    |S_n(phi)-M_infty(phi,log n)|
       <=C_b+P_0*KD+C_s sqrt(v)+(C_l+4KD)v.             (3)

CEphi is EXACTLY the accepted E08 literal allowance. Thus (3) includes
all ordinary rows, the fixed SIX actual retained rows, the complete
regular outer operator, the full scalar mesh and scalar-log term. It is
an absolute error, not a relative error or a theorem about a changed
model. No artificial parameter tuple is inserted into a physical theorem.

### Derivation of every coefficient in (2)

Apply E08's established physical theorem FIRST, at the actual phase:

    |S-M_infty|<=CEphi+KD P,
    CEphi=Dphi+Gphi+C6phi+Mphi+dW.

Its exact formulas, normalization and collision scopes are inherited from
the accepted full E08 theorem, not from any near-only estimate. To make
the new positive majorization checkable, its terms are repeated here:

    Dphi=a Da+10/n^2,
    Gamma(p,a)=p[1+log(1+(1+8am/(3pi))/p)], Gamma(0,a)=0,
    MA=max(p,q)/pi+4a/pi^2,
    VB=23+[3Gamma+(2p+6P)ell+26a+20+2d log2]/pi,
    CB=6+(4+4a/exp(1))/pi,
    Gphi=7L*MA/m+VB/(2m)
       +(4/m)[7+(P/pi)(5+2log(2m))]
       +4d log pi/(pi*m)+2CB/m,
    C6phi=[21+21a+2L+((1+48p)H+24q)/pi]/n
                                          +(317+5/12)/n^2.

The mesh Mphi has exactly the M_env formula above with actual a and
Dbar=4(ce+cd)/pi+a*b*log pi,Zbar=Dbar+a*b/n in place of the fixed
quantities. This includes all actual U0/D0 and H2 bounds, with no U0=0
assumption, no discarded tail, and no inverse a at a=0. The term dW is
the COMPLETE scalar-log charge from the same D07 identity. It is zero
at d=0, but no other signed cancellation is taken.

All coefficients just displayed are nonnegative. Thus a<=a_0 and
ce+cd<=w_0 give Dphi<=D_env,CB<=CB_b and Mphi<=M_env. The entropy
increases with a. At a=a_0 and p>0, its p derivatives are

    Gamma_p=1+log(1+C/p)-C/(p+C)>0,
    Gamma_pp=-C^2/[p(p+C)^2]<0.

Hence its global concave tangent at p_0 gives

    Gamma(p,a)<=Gamma(p,a_0)
       <=Gamma_b+gamma_b*(p-p_0)
       <=Gamma_b+eta*gamma_b*sqrt(v).                  (4)

At p=0 this follows by the literal continuous limit Gamma=0; the tangent
intercept is p_0*C/(p_0+C)>0, so no log0 or negative zero value is assigned.
The tangent is an inequality for an explicit positive function AFTER the
actual physical bound, and does not require fixed envelope parameters to be a
realizable phase.

The p and q contributions in C6phi give
eta(48H+24)sqrt(v)/(pi*n). In Gphi, its7L*MA term gives
eta*7L sqrt(v)/(pi*m). Its VB term gives

    [eta(3gamma_b+2ell)+6log2]sqrt(v)/(2pi*m)
                                      +12ell*v/(pi*m).

The P term in its hole expression gives
16(5+2log(2m))*v/(pi*m). The separate d log pi term gives
12log pi*sqrt(v)/(pi*m). Finally dW<=3W sqrt(v).
These are EXACTLY C_s and C_l in (2), with no leftover term. The
unchanged ordinary P coefficient contributes KD P<=P_0*KD+4KD*v,
which proves (3). All SIX labels0,1,2m-2,2m-1,m-1,m and the actual
ordinary mask2,...,m-2 are unchanged; no collision is assigned an
off-grid reference value by this scalar majorization.

## 3. Explicit all-real-n directions

The functions C_b,C_s,C_l,KD in (2) are positive and decreasing on
ALL real n>=32. This is a new coefficient assertion, not an assertion
of Padua objects at noninteger degrees. Here are the required checks.

Every constant/n^j, H/n^j or positive linear-log/inverse-power term
decreases there. Also L/m and log(2m)/m decrease. The literal sine-log
has epsilon<1/7,ell>1 and m*ell'=epsilon*cot epsilon<=1; hence ell/m
decreases. These are the E08 global-domain facts, not radius-one charges.

Write C=1+c*m,c=8a_0/(3pi)>0. Then

    m*(Gamma_b)'=p_0*c*m/(p_0+C)<p_0<=Gamma_b,
    m*(gamma_b)'=c*m*C/(p_0+C)^2<1<gamma_b.

Thus BOTH Gamma_b/m and gamma_b/m decrease. This covers the only new
entropy-tangent derivative; monotonicity of Gamma alone would not
suffice. All remaining G_env,C_s,C_l terms are positive sums of the forms
already checked. The mesh proof is the same literal positive-term
calculation as E08 with fixed Dmesh_b,a_0: split
(Dmesh_b+a_0*b*L)/(4n^2-1)+a_0*b/[n(4n^2-1)], and for its last term
use (n-1/2)/(n+1/2)-2log(n+1/2)<0. Zmesh_b itself decreases. This
proves M_env, hence C_b, decreases. W and KD retain their directions.

Consequently no difference of two decreasing functions or unproved
CEphi/u ordering is used. The original E08 fixed-ACTUAL-phase CEphi
monotonicity remains separately valid and supplies an alternative
pointwise all-n transfer for any later application.

## 4. Generic completed-model/actual-origin outer gate, with NO endpoint

Let j,t0 be the SAME accepted E06/E07 global Hmax constants:

    t0=2log2/pi>0,
    j=H0+d0-(c_model-1/3)>23/250.

The full-diamond completed-model master, including its inherited PD-T271
limiting-origin/regular-constant dependency, is

    C_infty(phi)-C_infty(0)
       <=-j*u+t0*p-(H0+v0_model)(1-ce)(1-cd)
       <=-j*u+t0*p.

Here v0_model is the accepted regular constant, NOT the variable v.
This is the GLOBAL endpoint/Hmax master, not a local Ec decomposition
applied above its radius. C08's accepted full coefficient comparison
gives the complete model loss

    M_infty(0,L)-M_infty(phi,L)>=u[T(n)+j]-t0*p,
    T(n)=(4L^2-3L)/pi^2.                              (5)

The true actual-origin error E_n(0)=Lambda_c-M_infty(0,L) is charged
SEPARATELY. For an explicit all-n32 choice use accepted E08 origin:

    D=Da+10/n^2,
    Mesh=b*(2L+2r)/n+[4+b*(L+1/n)]/(4n^2-1)
       +b/(2n-1)^2+[5+b*(log(n+1/2)+2)]/[4(n-1/2)^2],
    B_origin=pi[L+25log(2m)+193/3]/(8m^2)+1/(8n^2),
    e_-(n)=D+Mesh+B_origin+[71/n^2-22/(45m)]_+,
    E_n(0)>=-e_-(n), EVERY integer n>=32.              (6)

The scalar e_- is positive/decreasing for real n>=32. Alternatively on
n>=160 use e_-=ebar=D+Mesh+1/n in EVERYTHING that follows, by the
separately accepted strict one-sided lower. These are one-sided origin
allowances, not global norms or proofs E_n(0)>=0. The full absolute E0
remains unchanged for any other theorem that needs it. In the present
ABSOLUTE comparison the WHOLE e_- is charged, not u*e_-.

For either legitimate choice in its stated domain define

    G_b(n)=u1[T(n)+j]-t0*p_0-C_b(n)-P_0*KD(n)-e_-(n),
    K(n)=T(n)+j-C_l(n)-4KD(n),
    A(n)=eta*t0+C_s(n).                                (7)

Equations (1),(3),(5),(6) give for EVERY actual closed outer phase

    Lambda_c(n)-S_n(phi)>=G_b(n)+K(n)v-A(n)sqrt(v).    (8)

The exact TRUE symbolic Lambda_c is retained throughout. For K(n)>0,
completing the square in sqrt(v) gives

    K v-A sqrt(v)=K[sqrt(v)-A/(2K)]^2-A^2/(4K),
    Lambda_c-S_n(phi)>=F(n):=G_b(n)-A(n)^2/[4K(n)].   (9)

The minimization enlarges the actual v range to ALL v>=0 and is a
conservative scalar inequality, not a rootfinder or optimizer call.
The assumption K>0 is REQUIRED before division. If K<=0, this particular
Young sufficient gate is unavailable; no negative actual-gap conclusion
follows. Dropping the last nonpositive z term in the model was explicit.

For ANY prospectively assigned real scalar base N>=32 (or N>=160 when
using ebar), the TWO exact conditions

    K(N)>0, F(N)>0                                   (10)

are sufficient to exclude EVERY actual outer phase for EVERY integer
n>=N, with strict primitive gap at least F(N). No N is chosen or tested
in this theorem. No result for the remaining near/corner/physical classes
or global argmax onset follows from the implication alone.

Indeed T increases for real n>=32, C_l and KD decrease, so K increases.
C_b,KD,e_- decrease, so G_b increases. A>0 decreases, therefore A^2/K
decreases wherever K>0; F increases on that half-line. This proves (10)'s
all-real-n transfer directly. Alternatively, apply the original fixed-
actual-phase directions to (5) and the full E08 allowance after a base
inequality, without asserting any envelope quotient order. Neither route
requires actual S or Lambda_c to be monotone in n.

The conservative rational replacements j*=23/250 and t*=221/500 may
also be used consistently in (5)--(10): they weaken the ACTUAL master
pointwise because u,p>=0. Their whole modified formula must be used,
not just a favorable coefficient. No such endpoint is evaluated here.

## Scope, novelty, provenance and execution boundary

The new statements are (1)--(3), their explicit coefficient directions,
and the conditional sufficient reduction (7)--(10). Geometry and finite
absolute-envelope proofs require no PD-T271 enclosure; the completed-
model constants used ONLY in section4 retain its named trusted origin
normalization. No source theorem, actual finite corner lower from a
limiting decimal, changed model or finite-domain transfer is introduced.
E11's closed half-pi MODEL result is reading context, not a global
finite-error premise. E12 drafts and preliminary asymptotics are unused.

This does NOT prove a smaller allowance than E09 at EVERY phase, phase
monotonicity of CEphi/u, a new signed joint telescope, full D13, true
beta monotonicity or any lower onset. The old E08 sufficient-allocation
failures and all cusp/fractional/leading-only obstructions retain their
precise scopes. E09/origin chronology findings remain disclosed and
unwaived; the present completed gate does not retrospectively cure them.

2026-11-07, requested Codex gpt-6.1-sol xhigh; serving metadata unexposed.
Read-only inputfbbd5101551cd21018bd0153519f159c51645db1, rules63c70b7.
The parent first received explicit GATE COMPLETE, then supplied a separate
durable mathematical release. The owned idea inventory was written BEFORE
the new proof. Full relevant predecessor/negative histories and literature
coverage are recorded there; no historical priority claim. Only the THREE
assigned new E13 prose paths changed. No script/import/source/scalar/
endpoint/native/phase/root/quadrature/degree/threshold/board/compile/
control/scientific/pack/shared/Git job or mutation. Distinct audit required.


## Root adoption —2026-11-07

Root adopts the exact15350B frozen general support/conditional sufficient reduction (SHA256d78a57c047853c1b57cd2153d190d991cb9a7ed961cd09ef9db709274a181715) after distinct [E13 ACCEPT](../independent-checks-E13-joint-radius.md), report21161B6272730f4f77ee8dc6894dc215e9fdc8119efd8efd73e3c9fafaa1779a0d6a6e. Original prefix remains unchanged. All actual geometry, complete error coefficients, scalar directions and K>0/F>0 conditions are accepted. No endpoint was chosen or tested here, no onset follows without its complete separate application, and no phase-quotient claim is made. No new finding or numerical/source job occurred; upstream findings and final Claude audit remain separate.
