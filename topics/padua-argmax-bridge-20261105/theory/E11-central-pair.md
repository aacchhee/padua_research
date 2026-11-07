# E11 central pair — A joint root upper with the exact negative beta baseline

Provisional developer theorem, no global ID. Aliases: even decreasing
two-channel convolution; entropy-free central upper; signed beta baseline.
Split from the joint central-pair target after accepted E10. The separate
radius-five-fourths completed-model domain has its own theory file.

## Exact statement

Use the SAME corrected completed model and central functional as E10.
For x=|alpha|,y=|beta|,rho=x+y<=1 put

    a=(cos x+cos y)/2, p=sin x,q=sin y,v=p/2,delta=q/2,
    s0(e)=a tan(e/2),sL(e)=s0(e)+delta,sR(e)=|s0(e)-delta|,
    J(v,s,e)=I((v-s)/2,(v+s)/2,e),
    E(v,s,e)=J(v,s,e)-2s log(sin e),
    Z(v,s,e)=2 integral_e^(pi/2)
                    sqrt((v²-s²sin²t)_+)/sin t dt,
    Ec=pi^-2 integral_0^(pi/2)
            [J(v,sL,e)+J(v,sR,e)-4s0(e)log(sin e)]de.

All generic J values retain the accepted complete cancellation integral,
including same-sign entropy, opposite-sign roots and zero-coefficient
limits. Define

    I4=integral_0^1 sqrt(1-t^4)dt,kappa=4I4/pi²,
    b=2arctan(delta/a),
    Bbeta(a,q)=(4/pi²)integral_0^b
                    [delta-a tan(e/2)][-log(sin e)]de.       (1)

At q0 set b=Bbeta=0 directly. On this ENTIRE CLOSED signedrho<=1,
a>=49/64>0,b<=rho<pi/2 and Bbeta>=0. Then

    Ec(x,y)<=kappa*p^(3/2)/sqrt(a)-Bbeta(a,q)
           <=kappa*p^(3/2)/sqrt(a).                       (2)

Useful elementary consequences, with NO beta-entropy term, are

    Ec<=(3/8)x^(3/2)-Bbeta<=(3/8)x^(3/2), rho<=1/2,
    Ec<=(5/12)x^(3/2)-Bbeta<=(5/12)x^(3/2), rho<=1.    (3)

At x0 the stronger bound recovers the EXACT identity

    Ec(0,y)=-Bbeta(a,q),                                (4)

strictly negative for y>0 on the stated domain. At y0,Bbeta0, the
unchanged C01/D10 alpha-axis leading term is kappa*x^(3/2)>0. Thus
the fractional coefficient in(2) is asymptotically exact there.

Status: **PROVED developer PAPER theorem**, distinct audit/root adoption
pending. No finite-n operator, endpoint/degree, new onset, actual beta
monotonicity or quadratic-through-zero theorem is asserted.

## 1. Dependencies and exact closed-domain guards

Accepted E10-central-model supplies the EXACT E,Z and Ec definitions,
E<=Z for every v,s>=0,0<e<=pi/2, and its full-root inequality

    F(v,a):=integral_0^(pi/2)Z(v,a tan(e/2),e)de
                  <=4sqrt2 I4 v^(3/2)/sqrt(a),0<=v<=a.  (5)

It also supplies the rational conversions3/8 onrhohalf and5/12 onrho1,
and accepted C01/D10 identifies the SAME Ec axis limit with kappa. Its
proof needs no new scalar-H or PD-T271 enclosure. D37-constant-wide
already identifies this same central Ec in the TRUE completed constant
throughrho<=1, using its full positive-numerator/no-root endpoint check.
The generic full-parameter J identities are C06's accepted identities,
not an extrapolation of a near-only entropy statement.

The actual phase guards are exactly

    a>=49/64,v<=1/2,v/a<=32/49<1,
    0<=b=2atan(q/(2a))<=rho<=1<pi/2.                    (6)

The last inequality follows from
(cos x+cos y)tan(rho/2)=p+q>=q; all denominators are positive. The
new pair proof below is actually a generic inequality for a>0,v>=0,
delta>=0. The restriction v<=a is only needed when applying(5).
Closed signed phases use separate absolute phases, without any n,m
exchange. Actual finite polynomial rows/weights/collisions are untouched:
this theorem concerns an existing continuous-model functional only.

## 2. Exact negative baseline BEFORE an upper bound

For any s0,delta>=0,

    sL+sR=2max(s0,delta),
    sL+sR-2s0=2(delta-s0)_+.

Substitute J=E+2s log(sin e) in the ORIGINAL Ec integral. The exact
identity is

    Ec=pi^-2 integral_0^(pi/2)[E(v,sL,e)+E(v,sR,e)]de
                     +(4/pi²)integral_0^(pi/2)
                                   (delta-s0(e))_+ log(sin e)de
      =pi^-2 integral_0^(pi/2)[E(v,sL,e)+E(v,sR,e)]de-Bbeta. (7)

Indeed s0 is increasing and s0(b)=delta, so the last nonzero support
is EXACTLY0<e<b, with no extra root interval or moving floor. On this
support delta-a tan(e/2)>0 and -log(sin e)>=0; hence Bbeta>=0. Its
integrand is bounded by delta*(-log(sin e)), which is integrable at0,
and it vanishes at b. The q0 case is handled directly. There is no
new model correction: Bbeta is a retained term of the SAME identity.

Accepted E<=Z now gives

    Ec<=P(v,a,delta)/pi²-Bbeta,
    P(v,a,delta)=integral_0^(pi/2)
       [Z(v,a tan(e/2)+delta,e)+Z(v,|a tan(e/2)-delta|,e)]de. (8)

No sign assumption on E itself is used. All same-sign entropy remains
inside E until the valid upper by Z. The baseline's negative sign has
NOT been lost by separately replacing sL+sR with2s0.

## 3. First decisive test: the exact paired positive-root measure

We prove, for EVERY a>0,v>=0,delta>=0,

    P(v,a,delta)<=P(v,a,0)=2F(v,a).                    (9)

For0<t<=pi/2 define on the REAL line

    At=a tan(t/2),
    Wt(w)=[2a/(a²+w²)]*1_(|w|<=At),
    Rt(w)=sqrt((v²-w²sin²t)_+).

Both are nonnegative, even and nonincreasing in |w|. Wt has its
actual sharp truncation at At; smoothing or enlarging it is unnecessary.
Rt has its complete positive-part support, so root thresholds remain.

Insert the definition of Z into P. Tonelli applies to its nonnegative
integrands, retaining0<e<t<pi/2. At fixed t set

    w=a tan(e/2), de=2a dw/(a²+w²), 0<w<At.

The two channels combine EXACTLY as follows:

    P=2 integral_0^(pi/2) (1/sin t)
           integral_0^At [2a/(a²+w²)]
                    [Rt(w+delta)+Rt(w-delta)]dw dt
      =2 integral_0^(pi/2) (1/sin t)
           integral_REAL Wt(w)*Rt(w-delta)dw dt.        (10)

In the negative-w half of the second integral use w->-w and the
EVENNESS of both functions. This gives Rt(w+delta) with the original
Jacobian. The factor2 before the t integral is precisely the factor2
in each original Z. No1/pi² has yet been applied. This is the first
normalization/sign/domain kill: all factors match without replacing
a signed true E integral by an equality to a positive-root one.

## 4. Elementary interval-overlap maximum on the REAL line

For fixed t, the full convolution in(10) is at most its value at delta0:

    integral_REAL Wt(w)Rt(w-delta)dw
                   <=integral_REAL Wt(w)Rt(w)dw.        (11)

Here is a direct proof, not an imported unverified rearrangement theorem.
For nonnegative measurable f,g write their layer-cake identities
f(w)=integral_0^infinity1_(f(w)>r)dr and similarly for g. Tonelli
expresses their product integral as an integral over r,s of the lengths
of the intersections of these superlevel sets. For even radially
nonincreasing functions on the REAL line, each nonempty superlevel set
is an interval centered at0, up to irrelevant endpoints. After shifting
one by delta, the intersection length is at most the smaller interval
length. Concentric intervals attain EXACTLY that smaller length.
Integrating these inequalities proves(11).

For every fixed t>0, Wt is bounded with finite support; Rt is bounded
by v and, if v>0, has finite support because sin t>0. Their layer-cake
integrals are therefore ordinary finite nonnegative integrals. At v0
Rt is identically0, so(11) holds directly. Cutoff endpoint values and
root endpoints do not affect lengths or integrals. This is a REAL-line
interval argument, not an unproved periodic convolution transfer.

Apply(11) in(10) and use the original definition at delta0. This proves
(9) with no extra factor. Finiteness follows without presuming any
Tonelli interchange for a signed integral: for0<e<=pi/2,

    Z(v,s,e)<=2v log cot(e/2)<=2v log(2/e),

whose e integral is finite. Hence F is finite for every a>0,v>=0;
the new inequality bounds P by this finite quantity. The single t0
endpoint in(10) is interpreted improperly, not as0 times an assigned
infinite value. All zero/coalescing cases are already included.

This completes the parent's cheapest paired-root test. Only AFTER it
closes can the optional larger completed-model domain be considered;
that second proof is split separately and needs its own guards.

## 5. Sharp fractional consequence and boundary identities

Combine(8),(9),(5), with v=p/2 and the actual tau guard(6):

    Ec <=(2/pi²)F(v,a)-Bbeta
       <=(2/pi²)*4sqrt2*I4*(p/2)^(3/2)/sqrt(a)-Bbeta
        =kappa*p^(3/2)/sqrt(a)-Bbeta.

This proves(2). The same rational I4<319/360 and a/pi bounds accepted
in E10 give(3), multiplying NONNEGATIVE p^(3/2) before subtracting
the UNCHANGED Bbeta. There is no beta-entropy upper charge left.

At x0,v0 and E=Z0 for all s,e by the exact generic J formula.
Equation(7) therefore gives Ec(0,y)=-Bbeta EXACTLY. If y>0, then
delta>0,b>0, and its integrand is strictly positive on0<e<b, apart
from immaterial endpoints; hence Bbeta>0. At y0,Bbeta0. The accepted
C01/D10 limit Ec(x,0)/x^(3/2)->kappa>0 and p/x->1,a->1 show

    Ec(x,0)/[kappa*(sin x)^(3/2)/sqrt(a)]->1.

The new bound keeps the exact leading coefficient. No false pure
quadratic modulus is asserted, and no finite-degree limit is exchanged.

The inequality P(v,a,delta)<=P(v,a,0) concerns a POSITIVE MAJORANT
at fixed a,v. It DOES NOT establish Ec(x,y)<=Ec(x,0), or actual Ec
monotonicity in y: the actual a changes and E<=Z need not be equality.
No equality of Ec and the Z pair is inferred except the directly checked
v0 zero case. The negative baseline is an exact signed term, not a fit.

## Scope, provenance and execution record

The accepted E07 Hmax/E06 regular-part map may be combined with(2) on
rho<=1, retaining its named PD-T271 origin/regular-constant dependency.
The new root-pair theorem itself needs no such computational enclosure.
The full completed log²/log coefficients, every actual finite ordinary/
retained/outer/mesh/log error, true symbolic Lambda_c/origin allowance,
physical cover/corners and finite ell_nalpha cusp remain separate.
Full D13 and stronger finite mixed-error targets stay OPEN. No new
argmax onset, endpoint comparison, minimum threshold or source domain.

2026-11-07, requested Codex gpt-6.1-sol xhigh, serving metadata unexposed.
Gate-only input1ebd7a8ac542ee522a112802454fc3fea8d47e1d; root's separate
durable mathematical release and baseline-strengthening paragraph were
read after the completed8110B gate return. The exact gate prefix remains
unchanged; all candidates are root-supplied prospectively in LOG and
recorded in the idea before the written proof. New mechanism-specific
searches/full relevant predecessor reads completed before associated
development. This is a quantitative continuation of E10/C01, using an
elementary interval argument already familiar from E07, not a new
interpolation/kernel/rearrangement principle or priority claim.

Only assigned new E11 prose files changed. No scientific script/import,
source/scalar/endpoint/native/phase/root/quadrature/degree/threshold/
board/compile/control/pack/shared/Git job or mutation occurred. All old
accepted files remain frozen. Distinct mathematical audit is required.


## Root adoption —2026-11-07

Root adopts this exact10942B frozen proof (SHA256dea44db88f3a1bacc51b585b32f1666a6f138bcfdcb094981473da3827edeeb7) after distinct [E11 same-batch ACCEPT](../independent-checks-E11-central-pair.md), report22172B3407c50d16d23001e5a2532af80dd82d920263366d9091af1877b3d6c9ab29d2. Original proof prefix remains unchanged. The exact paired-root upper/negative baseline and model-domain scopes are accepted; no actual beta-monotonicity, finite-error domain or new onset is inferred. The weaker5/4 domain remains a preserved successful subset of the new closedpi/2 theorem. Optional kernel-moment sharpening remains deferred. No numerical/source job occurred; final Claude audit is separate.
