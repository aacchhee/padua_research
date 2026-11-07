# E10 central model — Integrate the entire moving-root majorant before splitting

Provisional developer theorem, no global ID. Aliases: unsplit positive-root
integral; sharp fractional coefficient with actual a,p; remove the artificial
alpha entropy charge. Quantitative continuation of C01/D24/D37's SAME
central correction. No completed-model or finite-row definition is changed.

## Exact statement and status

Let x=|alpha|,y=|beta|,rho=x+y<=1, and define the ACTUAL phase quantities

    a=(cos x+cos y)/2, p=sin x, q=sin y, v=p/2,
    s0(e)=a*tan(e/2), sL(e)=s0(e)+q/2,
    sR(e)=|s0(e)-q/2|, 0<e<=pi/2.

Use exactly N1/C06's normalization

    J(v,s,e)=I((v-s)/2,(v+s)/2,e),
    Ec(x,y)=pi^-2 integral_0^(pi/2)
       [J(v,sL(e),e)+J(v,sR(e),e)-4s0(e)log(sin e)]de.   (1)

This is D37's TRUE central correction in the exact completed constant,
not a new nonnegative model. Ec itself need not have an inferred sign.
Let

    I4=integral_0^1 sqrt(1-t^4)dt,
    kappa=4I4/pi^2,
    b=2arctan(q/(2a)),
    Lsin(b)=integral_0^b -log(sin e)de, Lsin(0)=0.

On the ENTIRE CLOSED signed rho<=1 domain,

    Ec(x,y)<=kappa*p^(3/2)/sqrt(a)+(q/pi^2)*Lsin(b)       (2)
       <=kappa*p^(3/2)/sqrt(a)
             +(q*b/pi^2)[1+log(pi/(2b))].                (3)

The b0 term is its continuous0 value; no logarithm is evaluated at0.
Here a>=49/64>0 and b<=rho<=1<pi/2, so all other denominators and
logarithms have their stated signs. The fractional coefficient kappa
is the SAME positive coefficient proved in C01/D10's actual alpha-axis
asymptotic. Thus(2) has the exact leading coefficient on that axis as
x decreases to0, without making a quadratic assertion through0.

Useful completely elementary forms are

    Ec <=(3/8)x^(3/2)+(1/9)y^2[3/2+log(1/y)], rho<=1/2, (4)
    Ec <=(5/12)x^(3/2)+(2/15)y^2[3/2+log(1/y)], rho<=1. (5)

In particular, after the accepted sqrt(t)log(1/t)<=3/4,

    Ec <=(3/8)x^(3/2)+(1/12)y^(3/2)+(1/6)y^2,
                                                        rho<=1/2,
    Ec <=(5/12)x^(3/2)+(1/10)y^(3/2)+(1/5)y^2,
                                                        rho<=1. (6)

All zero powers/log products have their continuous values. These bounds
remove C01/D37's additional positive x^2[1+log(1/x)] term; they do not
remove the genuine positive fractional term or any finite-n cusp/error.

Status: **PROVED developer PAPER theorem**, distinct mathematical audit
and root adoption pending. No degree endpoint,384/global-onset sign,
scalar/root/phase/native/quadrature job or source execution is a premise.

## Dependencies, exact model and first root-domain kill

C06-far-compact-error section2 reconstructs the generic J formulas on
ALL v,s>=0,0<e<=pi/2, including zero coefficients and root thresholds.
C01-near-central-upper introduces their nonnegative positive-root
majorant. D24 and D37 reconstruct its use on larger actual phase domains;
D37-constant-wide proves the SAME exact completed-constant identity

    C_infty=E_infty+ce*H(x-y)+cd*H(x+y)-c*a+Ec,
    ce=cos((x+y)/2),cd=cos((x-y)/2),a=ce*cd,             (7)

through rho<=1 with a fresh complete-numerator/no-root endpoint-half
proof. This theorem uses that accepted domain as stated, never the old
half-radius theorem beyond its quantifier. Every signed comparison uses
separate absolute phases. No n,n+1 interchange, top-mode change, altered
endpoint weight, unweighted pole value or finite-collision substitution
is made. Ec is an existing continuous improper integral of the complete
cancellation expression; it is not an actual finite row norm.

The first decisive PAPER test for the new root integration is

    a>=49/64, 0<=v/a<=32/49<1, 0<=b<=rho<=1.            (8)

The first inequality is D37's ce,cd>=7/8; v<=1/2 gives the second.
The half-angle identity (cos x+cos y)tan(rho/2)=p+q shows
b<=rho; also q/(2a)>=tan(y/2), hence b>=y. Finally arctan t<=t
gives b<=y/a. These assertions include x0 or y0. Their proof precedes
any integral substitution. In particular the condition v/a<=1 needed
below is ACTUALLY proved on the whole requested domain, rather than
assumed from a small-alpha picture.

No PD-T271 computational enclosure, scalar-H maximum or finite-origin
allowance is needed for(2)--(6). If(7) is later combined with the accepted
Hmax consequence, that separate consequence retains its stated origin/
PD-T271 dependencies. The exact limiting-model and finite-n obstructions
remain distinct.

## 1. Preserve all coefficient-sign regimes and the beta translation

Put E(v,s,e)=J(v,s,e)-2s log(sin e), and define the nonnegative function

    Z(v,s,e)=2 integral_e^(pi/2)
                   sqrt((v^2-s^2 sin^2 t)_+)/sin t dt.          (9)

The FULL generic identities give E<=Z for all v,s>=0. For s>v,
integrate the exact separation derivative from its no-root threshold:
the result is E=Z. The same equality holds at s=v by continuity.
For s<v the same-sign entropy formula gives J<=0, whereas
sqrt(v^2-s^2sin^2t)>=s cos t. Thus
Z>=-2s log(sin e)>=E. At v=0 the generic formula is
J(0,s,e)=2s log(sin e), so E=Z=0 directly. No division by a vanishing
coefficient and no smooth derivative through a moving root is assumed.

Z decreases separately in s and e. Set q/2=a tan(b/2). For e>b,

    sR=a[tan(e/2)-tan(b/2)]>=a tan((e-b)/2).

Consequently

    E(v,sR,e)<=Z(v,a tan((e-b)/2),e-b).

When b>0, the single point e=b is handled by improper integral limits;
no finite value is assigned to Z at a zero lower endpoint. If b0, all
displayed comparisons hold at every original e>0 directly.

For 0<e<b use J<=0 and 2sR<=q. This gives
E(v,sR,e)<=-q log(sin e). Also the left channel obeys
E(v,sL,e)<=Z(v,a tan(e/2),e). Since sL+sR>=2s0 and log(sin e)<=0,
the exact integrand(1) is at most E(v,sL,e)+E(v,sR,e). Integrate,
translate the right interval and enlarge only a NONNEGATIVE integral:

    pi^2 Ec <=2F(v,a)+q*Lsin(b),
    F(v,a)=integral_0^(pi/2)Z(v,a tan(e/2),e)de.           (10)

This is the accepted C01/D37 translation, with the SAME exact parameters
and sign regimes. Its charge is retained, not declared cancelled.
The new step is to integrate ALL of F without a short/tail split.

## 2. An exact unsplit representation for the whole root majorant

Let a>0,0<v<=a and tau=v/a in(0,1]. The following auxiliary formula
is exact and independent of any finite degree:

    F(v,a)=4v*tau integral_0^1 sqrt(1-z^2)*K(tau*z)dz,
    K(k)=integral_(arccos(1-k))^(pi/2)dt/(sin^2t+k^2),
                                                    0<k<=1.   (11)

Proof. All integrands in(9) are nonnegative. Tonelli therefore first
interchanges the triangular region0<e<t<pi/2, without presupposing
finiteness. At fixed t substitute

    z=tan(e/2)*sin t/tau,
    de=2tau*sin t*dz/(sin^2t+tau^2z^2).

The complete transformed expression is

    F=4v*tau integral_0^(pi/2)
          integral_0^min(1,(1-cos t)/tau)
              sqrt(1-z^2)/(sin^2t+tau^2z^2) dz dt.

Here tan(t/2)sin t=1-cos t is EXACT. The positive part supplies z<=1;
the original e<=t supplies tau*z<=1-cos t. Because tau<=1 and
0<=z<=1, the latter is equivalent to

    arccos(1-tau*z)<=t<=pi/2.

A second Tonelli interchange gives(11), with every original threshold
and both boundary constraints retained. No majorant is extended beyond
pi/2 and no claim2theta<pi/2 is made. The point z0 is handled as an
improper endpoint, not by assigning a finite value to K(0).

For0<k<=1 put w=cot t. The exact one-dimensional kernel becomes

    K(k)=integral_0^[(1-k)/sqrt(k(2-k))]
                      dw/[1+k^2+k^2*w^2]
       <=(1-k)/[(1+k^2)*sqrt(k(2-k))]
       <=1/sqrt(2k).                                  (12)

The first bound preserves the denominator before making it smaller.
For the second, it is enough to drop1+k^2>=1 and observe
2(1-k)^2<=2-k on0<=k<=1, since k(2k-3)<=0. The kernel is0 at k1,
consistent with its collapsed integration interval. These are the exact
root/sign/domain kill checks; no numerical rootfinder is involved.

Insert(12) into(11). The only remaining integral is

    integral_0^1 sqrt(1-z^2)/sqrt(z)dz=2I4,

by z=t^2. Therefore

    F(v,a)<=4sqrt(2)*I4*v^(3/2)/sqrt(a).                 (13)

This also proves the finiteness left open by Tonelli. At v0 both the
original integrand and the RHS vanish exactly, so(13) extends directly.
Every positive-part threshold was carried through an exact change of
variables; it was not differentiated or discarded. In particular no
separate small-e logarithmic estimate is needed.

## 3. Return to the TRUE two-phase correction and prove the constants

Apply(13) to(10), with v=p/2. Its factor is

    (2/pi^2)*4sqrt(2)*I4*(p/2)^(3/2)/sqrt(a)
                         =kappa*p^(3/2)/sqrt(a).

This proves(2). Since sin e>=2e/pi on0<=e<=pi/2 and b<=1,

    Lsin(b)<=b[1+log(pi/(2b))],

which proves(3), including b0 by b log(1/b)->0. Every factor on the
RHS is nonnegative on its claimed domain.

For explicit fractional constants, a slightly sharper ELEMENTARY I4
upper is useful and involves no quadrature. For0<=z<=1 the polynomial
P(z)=1-z/2-z^2/8 is positive and

    P(z)^2-(1-z)=z^3/8+z^4/64>=0.

Thus sqrt(1-z)<=P(z), strictly away from0. Substitute z=t^4 and
integrate to get

    I4<1-1/10-1/72=319/360,
    kappa<319/(90pi^2).                               (14)

On rho<=1/2, a>=1-rho^2/4>=15/16>(29/30)^2. Hence with
pi^2>197/20,

    kappa/sqrt(a)<319/(87pi^2)<6380/17139<3/8,

where the final cross-product is51040<51417. On rho<=1, (8) gives

    kappa/sqrt(a)<1276/(315pi^2)<25520/62055<5/12,

where306240<310275. Replacing p<=x in these NONNEGATIVE terms is
legitimate. No phase Taylor approximation or fitted I4 value is used.

For the beta charge, b>=y,b<=y/a,q<=y,log(pi/2)<1/2 and y<=1 give

    (q/pi^2)*Lsin(b)
       <=[y^2/(a*pi^2)]*[3/2+log(1/y)].                (15)

All factors have the proper sign. On the half domain1/(a*pi^2)<1/9;
on the whole radius-one domain1/(a*pi^2)<2/15, the latter being the
same19200<19306 comparison already used in D37. Equations(14)--(15)
prove(4)--(5). The accepted sqrt(t)log(1/t)<=3/4 gives(6). QED.

## 4. Boundary diagnostics, material improvement and exact application scope

At x=y=0, Ec=0 and all bounds have value0. At x0 the generic formula
J(0,s,e)=2s log(sin e) gives the exact sign check

    pi^2 Ec(0,y)=4 integral_0^(pi/2)
                    (q/2-a tan(e/2))_+*log(sin e)de<=0.

Thus the theorem does not infer a false positive sign from its positive
upper. At y0 its translation cost is0. Accepted C01/D10 proves
Ec(x,0)/x^(3/2)->kappa>0; since p/x->1,a->1,

    [kappa*(sin x)^(3/2)/sqrt(a)-Ec(x,0)]/x^(3/2)->0,
    Ec(x,0)/[kappa*(sin x)^(3/2)/sqrt(a)]->1.

Thus the fractional leading coefficient in(2) is asymptotically exact
on this actual axis. This is the accepted C01 root-scaling limit as
identified with the SAME Ec by D10, not a priority or whole-domain
optimality claim and not an exchange with a finite-degree limit.
A pure quadratic upper
still fails, precisely as recorded in the unchanged D10 obstruction.

The improvement is structural. The old C01 proof split F at2theta and
paid4v*theta[1+log(1/theta)] on its short interval (its v is named u
in C01). That charge was an
upper on an ARTIFICIALLY SEPARATED part of F. Equations(11)--(13) keep
the triangle e<=t and the root inequality together and bound the ENTIRE
F by one fractional expression. No signed contribution of Ec or a finite
row was deleted. Consequently(4) strictly improves the old
(15/32)x^(3/2)+(4/9)x^2[1+log(1/x)] beta-identical envelope for every
x>0 on rhohalf. Equation(5) likewise improves the old D37
(3/5)x^(3/2)+(8/15)x^2[1+log(1/x)] beta-identical envelope on rho1.
At x0 they retain the same conservative beta charge. No point/degree
comparison is required to prove these statements.

Accepted E07 Hmax and E06's exact consequence map may now be combined
with(2), or(4)--(6), on their LITERAL common rho<=1 domain:

    Delta C_infty <=Ec-j*(1-a)-(H0+v0)*(1-ce)*(1-cd),
    j>23/250,H0+v0>0.

This is a routine application of the SAME exact decomposition(7).
Those regular-part constants/normalization retain their named PD-T271
trusted dependency; the new root bound itself uses none. The completed
log^2 and log coefficients, true symbolic Lambda_c, finite-n ordinary/
retained/mesh/outer/log errors, actual-origin conversion and physical
corner/noncorner cover remain separately charged. No error theorem,
new degree threshold, minimum onset or full D13 conclusion follows here.
E09's signed outer work is a different finite operator, not a premise.

The possible stronger claim that the beta shift NEVER increases Ec is
NOT proved. The sign at x0 does not imply that joint monotonicity. Its
beta translation is still paid explicitly in(2), and a joint cancellation
could be a later separate paper obligation. The entire unchanged finite
error has a real ell_n|alpha| cusp, which this continuous model theorem
neither removes nor contradicts.

## Provenance, gate and execution limits

2026-11-07, requested Codex gpt-6.1-sol xhigh; actual serving metadata
unexposed. Input102abde583927c82680e5a94fea77b5e97540641. Rules fully
read63c70b7 and unchanged diff checked. The complete previously read
registry/current/all-table baseline was verified unchanged by actual
hashes, followed by fresh E10 mechanism searches and ALL full closest
idea/theory/obstruction reads BEFORE candidate generation. The exact
scope and concurrent newly appearing context are in the idea/attempt.
This is a quantitative continuation of the existing C01 positive-root
integral, not a new interpolation principle or historical priority claim.

Only THREE assigned E10-central-model prose files were changed. No old
proof/source/data, shared record, Git, pack or global ID changed. No
mathematical/scalar/script/import/source/native/endpoint/phase/root/
quadrature/finite-degree/threshold/board/compile/control job occurred.
No integral or endpoint value was numerically evaluated or previewed.
Distinct mathematical audit is required before assembly use/adoption.


## Root adoption —2026-11-07

Root adopts the exact13972B frozen proof above (SHA25628ff45c1316e36d07125431e5bd64fa308ba71439d3a82e73ca6ad3502d3e38d) after distinct [E10 central ACCEPT](../independent-checks-E10-central.md), report15080B5e18efd10e22d3a700722a47bbe905d61c2f8bb6ccc16a2edde8e7270e25d094. The full closedradius1 bound, half3/8/wide5/12 simplifications and exact axisleading sharpness are adopted. Original proof prefix is preserved. Beta translation remains charged, finite error and any lower onset remain separate. No numerical/source job occurred; final Claude audit remains separate.
