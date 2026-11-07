# F09 — Full signed outer expansion: coefficient ledger and uniform remainder

Status: PROVED developer PAPER theorem, distinct review/root adoption pending.
Rules/input4a5de2012bad94601c713b2ff5517f2e3fb80af2,
2026-11-07. Root's prospective registration, separate release and the local
idea/attempt preceded all algebra. PAPER only; no scientific execution.

## 1. Literal operator and complete first-order ledger

Take the inherited separate absolute phases alpha,beta>=0,rho=alpha+beta<=1,
n>=32,m=n+1,h=pi/m,L=log n,t=beta/pi,p=sin alpha,q=sin beta,
d=(q-p)_+,e=rho,delta=alpha-beta,ce=cos(e/2),cd=cos(delta/2),a=ce cd.
Signed phases are covered by the original separate-absolute convention.
The unchanged actual operator is F01/E12/E14's

    T=L sum_s Q_tau_s[g_s]+sum_s Q_tau_s[P_s]
      +(1/pi)sum_s Q_tau_s[B_s]
      +(q/pi)(Q_t-Q_(1-t))[log z]+Shift
      +(d/pi)(Q_t+Q_(1-t))[log(pi-z)],
    Q_tau[F]=(1/m)sum_(k=2)^(m-2)F(h(k+tau))
                                      -(1/pi)integral_0^pi F,
    tau_L=t,tau_R=1-t.

All six original removed labels{0,1,2m-2,2m-1,m-1,m}, all polynomial
collision values, exceptional highest coefficient ONE, original unequal
n,m meshes/parities and endpoint weights remain. T INCLUDES Rlog and
EXCLUDES Rmesh. Neither the full finite error nor origin conversion is T.

Write lambda_tau=3/2+tau,mu_tau=3/2-tau. The ACTUAL initial hole is
h lambda_tau and central hole h mu_tau. Thus

    lambda_L=3/2+t,lambda_R=5/2-t,
    mu_L=3/2-t,mu_R=1/2+t.

For a finite continuous profile F define its boundary ledger

    E_tau[F]=lambda_tau F(0)+mu_tau F(pi).

A boundary-corrected second-order estimate, proved below before any final
assembly, gives Q_tau[F]=-E_tau[F]/m+remainder. The following is the
complete exact ENDPOINT inventory, not a fixed-phase uniformity assumption.

For pi*g_L=max(q,p-Z),pi*g_R=max(-q,p-Z,q-2Z),Z=2a cot(z/2),

    g_L(0)=q/pi,g_R(0)=-q/pi,
    g_L(pi)=max(p,q)/pi,g_R(pi)=max(p,q)/pi.

Equivalently subtract the cancelling opposite constants and put
pi*v_L=(p-q-Z)_+,pi*v_R=max(0,p+q-Z,2q-2Z). Then

    sum_s E_tau_s[g_s]=A/pi,
    A=(3/2-t)(p-q)_++(1/2+t)(p+q+d).

Consequently the L-profile contribution is -A L/(pi m) plus a second-order
L-weighted remainder. No initial constant or max switch was discarded.

Use E14's same periodic continuous f and define

    V0=ce f(delta)+cd f(e)-2a f(0),
    w=ce f'(delta)-cd f'(e),
    W=ce f(pi+delta)+cd f(pi-e)-2a f(pi),
    Pc=W/2-V0/pi.

The arguments of f' in w lie in[-1,1], within its smooth principal period.
P_s=(V_s-V0)/z+V_s d0(z),d0=1/(2sin(z/2))-1/z gives

    P_L(0)=w,P_R(0)=-w,P_L(pi)=P_R(pi)=Pc,
    sum_s E_tau_s[P_s]=(2t-1)w+2Pc.

The central equality uses BOTH evenness and2pi periodicity of f. It uses
continuous f values at its cusp, never a smooth derivative through an atom.

For eta(x)=x log x,eta(0)=0, put u=p/2 and define the finite entropy

    if p>=q: c=(p-q)/4,b=(p+q)/4,
             H=2[eta(c)+eta(b)-eta(u)];
    if q>=p: c=(q-p)/4,b=(q+p)/4,
             H=2[eta(c)+eta(u)-eta(b)].

Both formulas give0 when p=q, including the double zero. These are exactly
the generic J finite central limits R(u,q/2,0), from C06 section2/N1-14;
the wide parameter range was independently established in C06/D37. The
origin's central cancellation tends to0. E12's B_L=C_L-q logz,
B_R=C_R+q logz therefore have the finite endpoint values

    B_L(0)=B_R(0)=-d logpi,
    B_L(pi)=H-q logpi,B_R(pi)=H+q logpi,
    sum_s E_tau_s[B_s]=-4d logpi+2H+(2t-1)q logpi.

The finite log products in F01 give, uniformly after the explicit remainder
proof below,

    Q_tau[log z]=[(3/2+tau)logm+Alog(tau)]/m+O(m^-2),
    Q_tau[log(pi-z)]=[(3/2-tau)logm+Dlog(tau)]/m+O(m^-2),
    Alog(tau)=log(2pi)/2-logGamma(2+tau)-3logpi,
    Dlog(tau)=log(2pi)/2-logGamma(2-tau)-3logpi.

The q log term contributes q(2t-1)logm/(pi m); the d term contributes
2d logm/(pi m). Now EXACTLY

    -A+q(2t-1)+2d=-2p.

Indeed for p>=q, A=2p+(2t-1)q,d=0. For p<q,
A=(1+2t)q,d=q-p. These cases include all axes and equality boundaries.
The logm-to-L difference is second order and will be charged explicitly.
E02's Shift satisfies |Shift|<=beta(17L+27)/m^2 on the whole rho<=1,
so adds no first-order constant and is NOT asserted to vanish.

The resulting explicit phase-only coefficient is

    Gamma_T=-(2t-1)w-2Pc+(1/pi){-2H
       +q[logGamma(3-t)-logGamma(2+t)-(2t-1)logpi]
       +d[log(2/pi)-logGamma(2-t)-logGamma(1+t)]}.       (G)

Every Gamma argument is positive and bounded away from0. All other terms
are finite endpoint/profile values or elementary entropy expressions. This
is not a numerical fit, uncomputed integral, or a definition by asymptotic
limit. At zero phase each term is0. No Rmesh or origin term is in(G).

## 2. Explicit extension of the entropy theorem through the origin band

We prove, on the ENTIRE closed0<=rho<=1, the exact same boundary-corrected
entropy estimate as F04:

    |sum_s Q_tau_s[B_s]+(1/m)sum_s E_tau_s[B_s]|
                         <=120000(1+logm)/m^2.         (B)

For1/32<=rho<=1 this is the accepted F04 theorem. The following argument
explicitly proves the missing0<=rho<1/32 part; it actually applies on the
whole radius-one domain. No F04 quantifier is extended merely by assertion.

First the analytic premises are uniform even at the origin. Since
ce,cd>=1-rho^2/8>=7/8, we have a>=49/64>3/4; also p+q<=rho<=1,
so a-(p+q)/2>=17/64>0. The initial no-root identities are consequently
the same ones proved on the wide domain in D37/E14, and give

    B_L=q log(sinz/z)-d log(pi-z),
    B_R=-q log(sinz/z)-d log(pi-z), 0<=z<=pi/2.

Their derivatives satisfy |B_s'|<2 and Var(B_s')<3 on this half. These
follow from0<=csc^2z-z^-2<1,|cotz-z^-1|<1 and the smooth d term;
the bounds have no inverse q,d or rho. Endpoint values mean continuous
limits. At rho=0 the full profiles B_s vanish identically.

For the central half let epsilon=pi-z,x=tan(epsilon/2),u=p/2 and

    s0=a x,s_L=s0+q/2,s_R=|s0-q/2|,
    k_s=2(s_s-u)_+,b_s=k_s-2s0-d,
    R=J-2(s-u)_+log(sin epsilon).

The full-range generic J formulas established in C06 section2 give

    B_s(pi-epsilon)=R(u,s_s,epsilon)+b_s log(sin epsilon)
                   +d log(sin epsilon/epsilon)+sigma_s q log(pi-epsilon),
    sigma_L=-1,sigma_R=1.                            (C)

Here b_s(0)=0,|b_s'|<=4,|b_s|<=4epsilon, and all limits at0 are finite
by the eta formulas in section1. This includes p0,coefficient zero and
double zero without division by a phase.

The finite feature set F_s contains0,pi/2,pi, every s_s=u, every s_R=0,
and every zero of

    P(x)=u^2(1+x^2)^2-4s(x)^2 x^2.

On the right, s^2=(q/2-ax)^2, so there is ONE quartic across the absolute
value switch. The leading coefficient u^2-4a^2 is negative even when
u=0; therefore P is never identically zero. At most four roots per side,
at most one/two coefficient zeros and at most one right absolute switch
give |F_L|<=8,|F_R|<=10, with coincidences merged. This count stays valid
at rho=0. Any redundant algebraic root can safely remain a feature.

Off features, the generic formulas are

    |R_s|<=log((u+s)/|u-s|), R_s=0 when u=0,
    R_epsilon=2[u cos epsilon-sqrt((u^2-s^2sin^2epsilon)_+)]/sin epsilon
                    if s>u, and0 if s<=u.

They imply0<=R_epsilon<=2s<=3. For the root regime, subtract squares
to obtain u cos epsilon-D<=sin epsilon*sqrt(s^2-u^2); in the no-root
regime u<=s sin epsilon. These estimates are valid down to u0.
Each affine-sign piece of s_s(epsilon) has derivative magnitude between
a/2>1/3 and a<=1. If s=u occurs, integrating this lower slope bounds
|s-u| below by one third of distance from that feature. If it does not
occur on a piece, integrate from the piece endpoint where |s-u| is least;
that endpoint is itself in the ledger. Since u+s<=2, with
D_s(z)=dist(z,F_s) we get

    |R_s|<=log(6/D_s),
    |B_s'(z)|<=9+5log(6/D_s(z)).                     (D)

The last bound follows by differentiating(C): R_s*s' costs its displayed
logarithm, R_epsilon costs3, b'logsin costs at most4log(2/epsilon),
b cot costs4, and the final two smooth terms cost1 each. Since the
central endpoint is a feature,D_s<=epsilon, (D) follows. The initial
half also satisfies(D). There is no lower-rho premise in any step.

For any interval I of length ell and any point r, integration on the two
sides of r gives

    integral_I log(6/|z-r|)dz<=ell[1+log(12/ell)].

The centered r maximizes this integral. Bound the maximum over sites by
the sum over at most10 sites. Then(D) implies

    integral_I |B_s'|<=60ell[1+log(12/ell)].           (E)

Continuity, piecewise smoothness and this integrable derivative envelope
prove global absolute continuity by truncating at each finite feature and
passing to its continuous limit. Thus(E) also bounds the crossing-cell
modulus. No globally finite Var(B_s') is being asserted.

For completeness the truncated-variation step remains uniform as features
merge. Retain any union G_s of intervals at distance at least v,0<v<=h,
from F_s, and put A0=log(6/v)>1. On an affine piece s=A+b x, b=+a or-a,
the same-sign R_s is monotone. In the root regime, with X=s(1-x^2),

    R_s=log[(X-sqrt(P))/(X+sqrt(P))],
    critical equation 2X'P-XP'=0.

The critical polynomial has degree at most6. If it is identically zero,
the derivative is identically zero on that connected root regime. Adding
the at most1 coefficient and4 quartic boundaries gives at most12 monotone
pieces per affine piece, at most24 per side. Its retained range is at most
2A0 by(D), so Var_(G_s)(R_s)<=48A0. With sup|s'|<=1,Var(s')<=4,
the product R_s*s' costs at most52A0 per side.

For R_epsilon the root-regime expression is

    R_epsilon=[u(1-x^2)-sqrt(P)]/x,
    critical equation 2P-xP'=2u(1+x^2)sqrt(P).

Squaring yields degree at most8. If this squared polynomial is identically
zero,2P-xP' has constant sign on a connected P>0 interval, and the actual
derivative either vanishes identically or has fixed sign. Hence the
exception does not create uncounted oscillations. The no-root expression
2u cot epsilon is monotone. Including the1+4 boundaries gives at most14
monotone pieces per affine piece,28 per side. Range[0,3] gives retained
variation at most84. At u=0 all R derivative terms are absent. At s=u,
P0 and root/no-root transitions the derivative factors have the same
continuous limits described by the generic formula; the integrable R_s
singularities were excluded as features. At s_R0,u>0 the entropy derivative
is0. No hidden jump appears as p tends to0.

Finally Var(b_s')<=20,sup|b_s'|<=4 by its at most four coefficient pieces
0,-a,-2a times sec^2(epsilon/2). Therefore

    Var_(G_s)(b_s'logsin)<=24A0,
    Var_(epsilon>=v)(b_s cot epsilon)<=14A0.

The latter follows by integrating4cot epsilon+4epsilon*csc^2epsilon.
The two smooth derivatives in(C) cost at most2 and1; the initial-half
variation costs3 and even an extra joining jump costs at most4. Per side
the total is at most90A0+94. Thus, uniformly including the omitted band,

    sum_s Var_(G_s)(B_s')<=400log(6/v).              (F)

Restricting a monotone piece to disconnected retained intervals costs no
more than its full retained range, so(F) does not bridge omitted gaps.

Now use the ACTUAL centered cells. Mark a cell bad if its distance from
its own F_s is less than h. A site can affect at most5 such cells; the
two feature counts sum to at most20, so at most100 cells are bad. Exact
sample/feature or cell-boundary equality can be included in that class.
By(E) each unnormalized bad-cell midpoint error is at most
60h^2[1+log(12/h)]. All good cells lie at distance at least h; the centered
Peano kernel has magnitude h^2/8, so(F) bounds their total error by
50h^2 log(6/h). Normalize by pi.

After adding E_tau[B]/m, each missing interval contributes only the
integral of B minus its own endpoint value. By(E) a hole of length ell
costs at most30ell^2[3/2+log(12/ell)] before normalization. The four
ACTUAL lengths lie in[h/2,5h/2], and sum ell^2<=25h^2. Their total cost
is at most1125h^2[1+log(24/h)]. With the bad and good cells, the full
normalized error is at most

    (7175h^2/pi)[1+log(24/h)]
                <120000(1+logm)/m^2.

Indeed h=pi/m,pi<4,24/pi<8 and log8<3 give the last inequality.
This proves(B) explicitly through the omitted origin band, all coalescences,
axes, p0 and exact sample equality. F04's infinite-variation obstruction
stays valid: only a finite atlas and truncated variation were used.

## 3. Boundary-corrected lemma and uniform max-profile remainder

If F is absolutely continuous with BV derivative on[0,pi], put
M=sup|F'| and V=Var(F'), with one-sided endpoint values. Midpoint Peano
integration against dF' gives error at most h^2 V/8 on a union of disjoint
actual cells, including any derivative atoms. Subtracting an endpoint value
from each missing-hole integral costs at most M ell^2/2. For our pair of
meshes, each tau lies in[0,1] and

    sum_(s,end)ell_s^2<=13h^2.

Thus if a common M bounds both derivatives and Vsum is their summed full
variation,

    |sum_s Q_tau_s[F_s]+(1/m)sum_s E_tau_s[F_s]|
                <=(pi/m^2)[Vsum/8+(13/2)M].         (H)

This is an actual-cell and actual-hole formula. It does not suppose equal
offsets or identify samples on different meshes.

Apply(H) to g_s or equivalently v_s, whose opposite constants cancel since
Q_tau[1]=-3/m and lambda_tau+mu_tau=3. On[0,pi/2],Z>=2a>1>=p+q,
so both v_s are0. On[pi/2,pi],|Z'|<=2 and Var(Z')<=1. Each active
branch is an affine function of Z with coefficient0,-1 or-2, divided by pi.
As Z decreases the active coefficient changes monotonically from0 to-1
and possibly-2. There are at most two switches per side, total jump
magnitude in the coefficient at most2. Consequently each derivative has
variation at most(2/pi)*1+(2/pi)*2<6, including its switch atoms.
Both have derivative supremum at most4/pi<2. The initial/central join
lies in the strictly zero region. We may therefore use Vsum<=12,M<=2 in
(H), obtaining

    |sum_s Q_tau_s[g_s]+A/(pi m)|<=64/m^2.          (I)

All switches may coalesce or hit a sample without changing this proof.
The L-weighted remainder is at most64L/m^2 uniformly through rho0.

## 4. Pole derivative variation with the periodic atom INCLUDED

Use the full accepted periodic measure bound |df'|(circle)<4, proved in
C04/E14 by its negative atom and positive density. Each translated interval
of length pi occupies less than a whole period. With weights
ce+cd+2a<=4 this gives, on[0,pi],

    |V_s|<=4, |V_s'|<=8 a.e., Var(V_s')<=16.         (J)

Every phase-dependent cusp is counted by the last measure estimate,
including coincident atoms. This step would be invalid if f were treated
as globally smooth. Atoms at a one-sided interval endpoint may also be
charged in full, which only enlarges the bound.

On the initial half, all translated arguments remain in(-pi,pi) because
pi/2+1<pi. Here |V_s''|<=4 and |V_s'''|<=13/5<3 by the accepted
smooth principal-period bounds. Set R0(z)=(V_s(z)-V0)/z. Keeping this
quotient intact gives

    R0(z)=integral_0^1 V_s'(vz)dv,
    |R0'|<=2, |R0''|<=1.

The uniform regular weights satisfy0<=d0<=1/5,0<=d0'<=1/3 and
|d0''|<=5/32. Hence P_s=R0+V_s d0 has

    |P_s'|<=2+8/5+4/3<5,
    |P_s''|<=1+4/5+16/3+5/8<8.

This includes z0 by the continuous quotient limits, with no 1/z loss.
Its initial-half derivative variation is less than16.

On the central half write w0(z)=1/[2sin(z/2)] and
P_s=V_s w0-V0/z. Direct differentiation gives

    sup w0<=1, Var(w0)<=1,
    sup|w0'|<=1/2, Var(w0')<=1/2.

The last equality bound follows from w0''>=0; its endpoint derivative is
at most1/2. Also Var(V_s)<=8*pi/2<16 and |V0|<=4. Thus

    sup|P_s'|<=8+2+16/9<12,
    Var(V_s' w0)<=16+8=24,
    Var(V_s w0')<=8+2=10,
    Var(V0/z^2)<16/9<2.

This charges all dV_s' atoms in the first product. The central derivative
variation is at most36. At the joining point pi/2 the shifted profiles
are smooth, so P_s' has no artificial partition jump. Therefore both
full P_s are absolutely continuous with BV derivative, with

    M<=12,Vsum<=104.

Equation(H),pi<4 now gives the complete paired pole estimate

    |sum_s Q_tau_s[P_s]+[(2t-1)w+2Pc]/m|
                      <=400/m^2.                  (P)

The estimate is uniform on the closed rho1 diamond. The BV derivative
assertion concerns P_s ONLY, not the entropy B_s.

## 5. Uniform finite log-Gamma expansion, without endpoint sampling

We use the elementary real Stirling remainder for x>0,

    logGamma(x)=(x-1/2)logx-x+log(2pi)/2+r(x),
    0<r(x)<1/(12x).

One explicit remainder proof is Binet's identity

    r(x)=integral_0^infinity e^(-xv)
       [1/(e^v-1)-1/v+1/2]dv/v.

This identity follows by inserting the Euler product for Gamma, integrating
the elementary difference exponentials (Frullani's identity), and taking
the limit; the normalization constant is fixed by the Wallis product.
No numerical Gamma or integral evaluation is used. To verify the bound
directly, put y=v/2. The bracket is(coth y-1/y)/2, between0 and v/12.
The lower inequality follows from y coshy-sinhy>=0. For the upper one,
(3+y^2)sinhy-3y coshy has derivative y(y coshy-sinhy)>=0 and vanishes
at0. Integrating the bracket bound gives0<r(x)<1/(12x).

For m>=33 and c in[-2,0], put s=c/m. Then |s|<=2/33<1/16, and

    |log(1+s)-s|<=s^2/[2(1-|s|)].

On replacing x=m+c in Stirling's formula, the difference from

    (m+c-1/2)logm-m+log(2pi)/2

equals(m+c-1/2)log(1+c/m)-c+r(m+c). Its linear part has magnitude
|c(c-1/2)|/m<=5/m, its logarithmic remainder is less than3/m,
and r(m+c)<1/m. Therefore the total is less than10/m, UNIFORMLY in c.
Apply this to c=tau-1 and c=-1-tau in F01's exact finite products.
For EVERY0<=tau<=1 it proves the formulas from section1 with

    |Q_tau[log z]-[(3/2+tau)logm+Alog(tau)]/m|<=10/m^2,
    |Q_tau[log(pi-z)]-[(3/2-tau)logm+Dlog(tau)]/m|
                                                       <=10/m^2. (Jlog)

All finite Gamma arguments lie in[1,3]. The actual arguments to which
Stirling is applied are at least m-2>=31. No singular endpoint is sampled,
no asymptotic constant depends on a moving phase, and all four holes were
already preserved by the exact products.

The q,d weighted combined remainder in(Jlog) is at most
20(q+d)/(pi m^2)<14/m^2. Finally put C=q(2t-1)+2d. Since |C|<=3,
pi>3 and logm-L=log(1+1/n)<=1/n<2/m,

    |C(logm-L)/(pi m)|<2/m^2.                      (Lm)

Thus the log products and the logm-to-L replacement together cost at most
16/m^2. E02 supplies the EXACT separately retained Shift charge
beta(17L+27)/m^2; no first-order term was hidden in it.

## 6. Uniform theorem and complete assembly

For EVERY integer n>=32, BOTH degree parities and the entire CLOSED signed
rho=|alpha|+|beta|<=1 diamond, the literal full signed outer block satisfies

    |T_n-[-(2sin|alpha|/pi)logn+Gamma_T(phi)]/(n+1)|
                    <=41000[1+log(n+1)]/(n+1)^2.    (T)

Gamma_T is the explicit finite expression(G), with separate absolute phases
as in section1. All axes,p0,p=q,zero,coalescing features and exact sample or
polynomial collisions retain their original conventions.

Indeed the complete error ledger is

    max-profile:          64L/m^2,
    pole profile:         400/m^2,
    entropy profile:      (120000/pi)(1+logm)/m^2,
    finite logs and Lm:   16/m^2,
    fixed-origin Shift:   beta(17L+27)/m^2.

There is one charge for every term of the literal decomposition and none
for Rmesh. Since beta<=1,L<=logm and pi>3, this is at most

    [40000(1+logm)+81logm+443]/m^2
                       <=41000(1+logm)/m^2.

The coefficient identity in section1 then proves(T). At rho0 all exact
profiles and(G) vanish, so no separate limiting interpretation is needed.

This is a feasibility theorem with a deliberately conservative K. It is
not a useful onset budget, whole finite-error estimate, physical floor,
actual-origin allowance, new finite-degree certificate or global theorem.
The actual finite alpha cusp in other components remains. Root controls
distinct review, adoption and any later use; no source implementation or
scientific execution is supplied by this proof.

## Provenance and verification limits

The complete adaptive gate preceded root's prospective campaign/LOG scope
and separate mathematical release. The LOCAL idea and attempt were the
FIRST tool action following release, before any F09 algebra. Section1's
ledger was written before the later uniform proof. Its initial OPEN-status
paragraph was then replaced when sections2--6 completed the obligations;
the actual sequence is preserved in the attempt. No earlier F04/F06 local
chronology is waived or rewritten by F09's order.

Only read-only text commands, hand algebra and owned same-stem prose writes
occurred. No scripts/imports, calculator, numerical/scalar/phase/degree/
endpoint/native/quadrature/source/compiler/pack job, extra agent, shared
file or Git mutation. All frozen predecessors remain unchanged. Serving
model metadata is unexposed beyond requested/API Sol xhigh. Distinct
mathematical review, novelty/protocol judgment and final readiness remain
separate; no independent approval is claimed by this developer proof.


## Root disposition after distinct mathematical acceptance —2026-11-07

Root adopts the exact mathematical statement under its written quantifiers, hypotheses and dependencies. The original frozen proof/record prefix is preserved and identified in [independent review](../independent-checks-F08-F10.md), final SHA2561e63875c450d08f87b4b2b24934bf8baad67958f727b8df3e789998757db9d72. No global-onset change, new finite degree, source integration, strict runtime saving, novelty/priority verdict, protocol waiver or readiness follows beyond the exact statement. Final Claude review remains separate.
