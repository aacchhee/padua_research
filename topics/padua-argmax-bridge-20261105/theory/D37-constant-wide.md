# PD-T?argmax-bridge-codex-D37-constant — A directional completed-constant modulus through radius one

ID kind: PD-T. Aliases: radius-one central/H extension; scalar quarter
cutoff with f4 through5/4. Split from: D37 global1024 candidate.
Split into: optimization/assembly and guarded floor have separate files.

## Exact statement and status

Use EXACTLY D02/D10's TRUE completed constant C_infty. Put
x=|alpha|,y=|beta|,rho=x+y<=1,r2=x²+y²,a=(cosx+cosy)/2,
u=1-a. Phases are RADIANS, not turn-normalized inputs. Then

    C_infty(alpha,beta)-C_infty(0,0)
      <=(3/5)x^(3/2)+(19/24)r2
          +(8/15)x²[1+log(1/x)]
          +(2/15)y²[3/2+log(1/y)].             (1)

Zero logarithmic products mean their continuous0 value. Status:
**PROVED analytic developer domain extension**, with all new
domain/coefficient obligations below; independent review pending.
No finite-n error, onset, numerical premise or source execution.
Old D24 rho<=3/4 bounds are not extrapolated and remain unchanged.

## Exact decomposition and the complete numerator

As in D24, writee=x+y,d=x-y,c_e=cos(e/2),c_d=cos(d/2),a=c_e*c_d,
c=1/3+(4/pi²)(log²pi-log²2). The SAME full-domain finite-part
identity has scalar pole piecec_e H(d)+c_d H(e) and endpointE_infty.
Herec_e,c_d>=cos(1/2)>=7/8,soa>=49/64,P=sinx+siny<=1.
On0<z<=pi/2 the COMPLETE kernel numerator is>=2a-P>=17/32>0.
AlsoT=2a*cot(z/2)>P and(T-q)sinz>=2a-q>p, wherep=sinx,q=siny.
The full-parameter generic J no-root identity consequently gives

    I_L(z)+I_R(z)=4a*cot(z/2)*log(sinz).

This proves the positive baseline on the enlarged domain. The central
half uses the SAME exact parametersv=p/2,s0=a*tan(epsilon/2),
sL=s0+q/2,sR=|s0-q/2|. Define

    E_c=pi^-2 integral_0^(pi/2)
      [J(v,sL,epsilon)+J(v,sR,epsilon)
                             -4s0*log(sinepsilon)]d epsilon.

Thus the exact D24 decomposition is now freshly proved throughrho1:

    C_infty=E_infty+c_e H(d)+c_d H(e)-c*a+E_c.   (2)

The baseline antiderivative and endpoint logarithms are the identical
accepted D10 full finite-part objects. No new cutoff or model is defined.

## Scalar fourth derivative on the NEW interval

Let f(t)=Phi0(1/2+t/(2pi)),k0=C0-2logpi in(0,2). Its accepted
reciprocal-pair series is

    f(t)=cos(t/2)[k0+W(t)]/pi,
    W(t)=4 sum_(j>=1) A_j(t/pi)^(2j),0<A_j<10/9.

On|t|<=5/4,pi>25/8 gives|t/pi|<=2/5. Termwise derivatives are
uniformly dominated by the positive geometric series
(40/9)g(s),g(s)=s²/(1-s²), with chain factors(8/25)^j. The
exact derivative values ofg are

    g'=2s/(1-s²)²,
    g''=2(1+3s²)/(1-s²)³,
    g'''=24s(1+s²)/(1-s²)^4,
    g''''=24(1+10s²+5s^4)/(1-s²)^5.

At s2/5 these rational majorants give

| Derivative | Rational upper from the series | Convenient bound |
|---|---|---|
| W |160/189|<1|
| W' |6400/3969|<5/3|
| W'' |189440/83349|<7/3|
| W''' |5701632/1750329|<10/3|
| W'''' |1340866560/183784545|<15/2|

Each comparison is a direct positive-denominator integer inequality.
The cosine product rule therefore yields, throughout|t|<=5/4,

    |f''''|<(1/pi)[15/2+2*(10/3)+(3/2)*(7/3)
                                      +(1/2)*(5/3)+3/16]
           =(299/16)/pi<299/50<6.               (3)

No periodic atom occurs on this local interval; all atoms remain
present in the GLOBAL semiconcavity used outside it below.

## H increment through|t|<=1

The accepted all-real scalar functional is

    H(t)=lambda0*f(t)+(1/pi)integral_0^pi D_v f(t)K(v)dv,
    0<lambda0<1/(2pi),K(v)=1/[2sin(v/2)]<=1/v+v/16.

HereD_t f(v)=f(v+t)+f(v-t)-2f(v). Accepted global semiconcavity
including NEGATIVE derivative atoms givesD_t f(v)<=3t²/pi²;
the global minimumf>=f(0)>0 givesD_t f(0)>=0. By evenness,

    H(t)-H(0)=(lambda0/2)D_t f(0)
          +(1/pi)integral_0^pi[D_t f(v)-D_t f(0)]K(v)dv.

For|t|<=1 and0<=v<=1/4, all arguments needed by the triangular
second-difference formula forf'' lie in[-5/4,5/4]. Equation(3)
and(D_t f)'(0)=0 give|D_t f(v)-D_t f(0)|<=3t²v². Forv>=1/4
use the GLOBAL semiconcavity and favorable subtractionD_t f(0)>=0;
no derivative through an atom is taken. As

    integral_0^(1/4) v²K(v)dv<=513/16384,
    integral_(1/4)^pi K(v)dv=logcot(1/16)<log16<14/5,

the resulting t² coefficient is at most

    183/(20pi³)+1539/(16384pi)
       <93696/312500+1539/51200
       <3/10+31/1000=331/1000<1/3.             (4)

This is stronger than the tentative3/8 target, proved with explicit
NEW derivative/domain bounds. H(t)-H(0)<=t²/3 now holds on|t|<=1.
SinceH(0)>0 andc_e,c_d<=1, its weighted increment is<=2r2/3.
Accepted full endpoint lossE_infty-E_infty(0)<=-u/3,
c-1/3<1/2 andu<=r2/4 then give

    [C_infty-E_c](x,y)-[C_infty-E_c](0,0)<=19r2/24. (5)

## Central root majorant with the truncated short interval

The full-range generic J identities of C06 give, for ALLv,s>=0,

    J(v,s,epsilon)-2s*log(sinepsilon)
       <=Z(v,s,epsilon)
       :=2 integral_epsilon^(pi/2)
                        sqrt((v²-s²sin²t)_+)/sint dt.

Z is nonnegative and decreases separately ins,epsilon, including
root thresholds/zero parameters. This is the accepted positive-part
majorant reconstructed in C01/D24, not a smooth moving-root derivative.
Letb=2arctan(q/(2a)),theta=2arctan(v/a),tau=v/a. The SAME half-angle
algebra gives

    y<=b<=y/a,x<=theta<=x/a,
    b,theta<=rho<=1<pi/2,tau<=x/(2a)<=32/49<1. (6)

In contrast to the smaller D24 domain,2theta MAY exceedpi/2.
No assertion2theta<pi/2 is used here. The beta translation argument
is still valid sinceb<pi/2 and retains ALL coefficient signs, giving

    pi²E_c<=2 integral_0^(pi/2)Z(v,a*tan(epsilon/2),epsilon)d epsilon
                        +q integral_0^b -log(sinepsilon)d epsilon. (7)

For x>0, split the unshifted root integral at
epsilon_short=min(2theta,pi/2). On that SHORT part,
Z<=2v log(2/epsilon). Its integral can be enlarged to2theta<=2,
because this ELEMENTARY logarithmic majorant is nonnegative up to2.
Only the majorant is extended; Z is never defined pastpi/2. Thus its
contribution after the2/pi² factor in(7) is bounded by

    [4/(a*pi²)]x²[1+log(1/x)]
       <=[256/(49pi²)]x²[1+log(1/x)]
       <(8/15)x²[1+log(1/x)].                  (8)

The interval beyond2theta is empty when2theta>=pi/2. Otherwise
the exact SAME root substitutions as C01 apply:lambda=v/s<=
tau/tantheta=(1-tau²)/2<=1/2,X=(1-cosepsilon)/tau, and the positive
tail has coefficient at most

    16I4/[pi² sqrt(6a(2-tau))],
    I4=integral_0^1 sqrt(1-t^4)dt<9/10.

Here6a(2-tau)>=99/16>(49/20)². Withpi²>197/20 the coefficient
is<5760/9653<3/5. For y>0 the beta shift in(7) is, usingb>=y,b<=y/a,
q<=y andlog(pi/2)<1/2, at most

    [1/(a*pi²)]y²[3/2+log(1/y)]
       <=[64/(49pi²)]y²[3/2+log(1/y)]
       <(2/15)y²[3/2+log(1/y)].                (9)

The exact coefficient comparisons are76800<77224 for(8),
28800<28959 for the fractional term, and19200<19306 for(9).
Atx0 the root integral vanishes, aty0 the shift vanishes, and all
zero logarithmic products have their continuous values. Combining
(5),(7)--(9) proves(1) on the COMPLETE closedrho1 domain. QED.

## Scope and trusted dependencies

This is an exact scalar/central domain extension using accepted local
series and global complete functional identities; there is no new
phase sample, integral evaluation or finite-n error theorem. The full
relative operators and every finite/actual-origin charge remain separate.
No quadratic bound through zero is inferred; the positive fractional
axis obstruction stays explicit. No n,m symmetry is assumed. Old
D24/C01/D10 files and parameters remain unchanged. No mathematical
job, scalar/native/phase/board/root/quadrature/degree run or code
execution occurred. 2026-11-06, Codex gpt-6.1-sol xhigh45min paper
lead,inputeb9329c28be18d77eeb817f634202d626ee11f92,
serving metadata unexposed. Distinct review required before adoption.
