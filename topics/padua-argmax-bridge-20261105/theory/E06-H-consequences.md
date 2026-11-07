# E06 — Exact consequences and sufficient scalar H lemmas

Provisional PD-T?argmax-bridge-codex-E06-H-consequences. Aliases:
uniform-H constant envelope; endpoint/origin correlation; required-H
frontier. Status: **PROVED parametric sufficient implication**, including
the unconditional bookkeeping corollary in section5. This is NOT an
unconditional assertion H<=H0 or C∞<9/4. Those scalar hypotheses and
their possible verification belong to the separately owned E06-H-frontier.
No new analytic onset is claimed. 2026-11-07, requested Sol xhigh,
serving metadata unexposed, input/rules5fac9e1ae77df8421279eccad57fa8ed1f416d3e.

The main theorem is the algebraic consequence system(4),(7),(10)
below, with each H hypothesis explicit. It keeps the SAME completed
constant, endpoints, origin and signed phase convention; it introduces
no new model or numerical premise. No source, scalar, endpoint or
scientific job was executed. Gate and all candidate dispositions are
in the owned idea/attempt.

## 1. Exact definitions and trusted origin constant

On the closed signed phase diamond first take x=|alpha|,y=|beta|,
x+y<=pi; the inherited separate-sign comparison gives this reduction
without exchanging n,m. Let

    e=x+y,d=x−y, ce=cos(e/2), cd=cos(d/2),
    a=ce*cd=(cosx+cosy)/2,u=1−a,
    z=(1−ce)(1−cd), p=sinx,
    C0=2gamma+4log2, b0=C0−7/2,
    B=C0²/pi², d0=C0*b0/pi², v0=7b0/(2pi²),
    g0=(4/pi²)(log²pi−log²2)=c−1/3,
    t0=2log2/pi, H0=H(0),
    j=H0+d0−g0.

Use EXACTLY the even2pi-periodic scalar H of C08-far-pole-functional,
including its finite-part counterterm and all negative derivative atoms.
All ce,cd,a,p,z are nonnegative here, including the closed boundary.
The identity2−ce−cd=u+z will be retained, not bounded in the wrong
direction. All endpoint products use their original continuous limits.

The accepted D08 limiting transfer identifies

    Cstar=C∞(0,0)=4k_shift²/pi²+kappa,
    k_shift=gamma+log(8/pi).

This equals PD-T271's constant c in the expansion of the ACTUAL corner
value, since log(n+1/2)−logn and all its polynomial/log changes vanish.
It is a comparison of limits, never the finite assertion
Lambda_c(n)>=4(logn+k_shift)²/pi²+kappa. The accepted strict outward
enclosures from PD-T271 are

    .919710118388492535099518225790 < kappa
        < .919710118388492535099518225791,
    1.846160310423926079759838737947 < Cstar
        < 1.846160310423926079759838737948.            (1)

Source: topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md,
its evidence/t4-constant.json, independent-checks-analytic.md and accepted
Claude audit/response. These retain their declared Arb outward-arithmetic
and analytic-tail trusted base. No new enclosure or special-function
evaluation is performed here. In particular Cstar<1847/1000 and
Cstar>923/500 are legitimate inherited rational consequences.

At phase0 the accepted near decomposition has Ec=0, so EXACTLY

    Cstar=B−g0+2H0,
    H0=kappa/2+(2k0/pi²)log(2/pi), k0=C0−2logpi.   (2)

The second identity follows by inserting
2k_shift=C0+2log2−2logpi into the first; no separate quadrature of H0
is needed. It yields the useful rigorous rational bounds

    7/25 < H0 <1633/5125<8/25,
    d0>39/250, g0<43/125, j>23/250,
    0<t0<221/500.                                  (3)

Here are complete elementary checks. Accepted C08/D10 constants give
161/100<k0<9/5,logpi<23/20,logpi>11/10,log2>69/100,
pi>25/8,197/20<pi²<10. Thus log(pi/2)<23/50, and(1),(2) give
H0>9/20−828/4925=5553/19700>7/25. Conversely
log(pi/2)>log(25/16)>18/41 by log s>2(s−1)/(s+1),s>1;
hence H0<23/50−(161/500)(18/41)=1633/5125.
The accepted d0>39/250 is D10's exact weighted endpoint bound.
Also

    g0<(80/197)[(23/20)²−(69/100)²]
       =677120/1970000<43/125.

This proves j>7/25+39/250−43/125=23/250. Finally the accepted
atanh rational bound log2<6932/10000 and pi>157/50 give
t0<6932/15700<221/500. These are inequalities among written exact
rationals, not numerical arithmetic previews.

## 2. Full-diamond consequence of ANY uniform H upper

**PROVED implication.** Suppose h>=0 is any real constant and
H(theta)<=h for every |theta|<=pi (periodicity then supplies all real
theta). The full completed constant satisfies

    C∞(x,y) <= B−d0+(d0−g0)a−v0*z
                         +h(ce+cd)+t0*sinx,
    C∞(x,y) <= U(h)
      :=B+h−d0+J/2+sqrt(J²/4+t0²),
    J=max(0,h+d0−g0).                               (4)

The first upper keeps the exact phase weights and endpoint/a/p
correlations. The second is a convenient full-diamond scalar consequence,
not a claimed sharp maximum. It also covers h+d0−g0<0 legally.

Proof. The accepted full D10 finite-part decomposition gives the pole
piece ceH(d)+cdH(e) and cancellation upper−c*a+t0*p. Its EXACT
weighted endpoint comparison, before dropping the mixed loss, is

    E∞<=a/3+B−d0*u−v0*z.

Indeed multiply [C0−b0(1−ce)] and[C0−b0(1−cd)] before simplifying,
as in C08/D10. Thus the first line of(4) retains all full endpoint and
counterterm contributions. Since h>=0 and ce+cd<=1+a, drop only the
nonpositive−v0*z to obtain B+h−d0+(h+d0−g0)a+t0*p.
If the coefficient of a is negative, replace it by0 because a>=0.
Otherwise a<=(1+cosx)/2 and p=sinx give the largest linear sinusoid
J/2+sqrt(J²/4+t0²). This retains the crucial a/p correlation; using
their separate maxima would give a different, weaker allocation.
Every phase-boundary zero/endpoint follows from the accepted continuous
weighted formulas. No local central identity was applied globally.

## 3. How weak a scalar bound suffices for the9/4 target?

This section is a **PROVED sufficient implication**, not a proof of
its H premise. Let epsilon>=0 and suppose

    H(theta)<=H0+epsilon, ALL |theta|<=pi.            (H-epsilon)

Write delta=9/4−Cstar>0. Since j>0, origin identity(2) rewrites(4) as

    C∞ <= Cstar+2epsilon−(j+epsilon)/2
                         +sqrt((j+epsilon)²/4+t0²). (5)

Therefore a sufficient exact scalar criterion is

    delta−2epsilon>0,
    (delta−2epsilon)²+(delta−2epsilon)(j+epsilon)>t0². (6)

This follows by moving the nonnegative square root in(5) and squaring
only after its other side is positive. In particular the WEAKER-than-
maximum assertion H<=H0+1/400 already implies

    C∞(alpha,beta)<9/4 on the ENTIRE closed diamond.  (7)

For this fixed rational excess, use delta>403/1000,j>23/250 and(3):
delta−2epsilon>199/500,j+epsilon>189/2000, so the left side in(6)
is>196015/1000000, whereas t0²<195364/1000000. The strict difference
is651/1000000. H<=H0 is stronger and hence also sufficient; the
cosine-shaped conjecture H(theta)<=cos(theta/2)H0 is unnecessary.

The quantitative threshold for THIS sufficient envelope can be stated
exactly, with no endpoint or parameter scan. Its epsilon-polynomial is

    P(epsilon)=delta²+delta*j−t0²
                          −(3delta+2j)epsilon+2epsilon².

On0<=epsilon<delta/2 it strictly decreases. If P(0)>0, the admissible
interval is bounded by its smaller root

    epsilon_crit=[3delta+2j−sqrt((delta+2j)²+8t0²)]/4. (8)

Thus0<=epsilon<min(delta/2,epsilon_crit) is an exact family of useful
H lemmas. This is the weakest condition INSIDE THE CHOSEN envelope
test(6), not a necessary condition for the true C∞<9/4 assertion or
an optimal bound on H. The explicit1/400 is a convenient proved
sufficient choice. No scalar H bound at this level is asserted here.

If(7)'s H premise is proved elsewhere, the same accepted origin lower
in(1) gives the full true-constant gap ΔC∞<101/250. It can replace
old Dc=6211/7260 in a FUTURE separately matched global outer budget,
an improvement81949/181500. All CE,KD,E0 and finite-origin charges
would remain. This is not a finite Lambda_c inequality or new onset.

## 4. Exact regular-part increment under a LOCAL H majorant

On0<=r=x+y<=R<=1 use the accepted D37 exact decomposition

    C∞=E∞+ceH(d)+cdH(e)−c*a+Ec,
    Reg=C∞−Ec.

The entire endpoint/H4 positive-numerator/root-domain proof is the
unchanged accepted D37 radius-one theorem. Suppose omega is ANY
function bounding H(theta)−H0 on |theta|<=R. Then

    Reg(x,y)−Reg(0,0)
       <=ce*omega(d)+cd*omega(e)−j*u−(H0+v0)*z.     (9)

This is the local parametric part of the theorem. Proof: subtract the
origin endpoint value from the first endpoint inequality used in(4),
add the exact−c*a difference, and write the H-piece as
H0(ce+cd−2)+ce*ΔH(d)+cd*ΔH(e). Use2−ce−cd=u+z.
All signs are retained. The result is (9). In particular no negative
coefficient times u is ever replaced using an UPPER bound on u.

If omega(theta)=kappa_H*theta² with kappa_H>=0, then
ce*d²+cd*e²<=d²+e²=2(x²+y²), while

    u>=[1/4−R²/48](x²+y²)=cR*(x²+y²).

It follows that

    ΔReg <=[2kappa_H−cR*j](x²+y²)−(H0+v0)*z.      (10)

If kappa_H<=0, simply ce*omega(d)+cd*omega(e)<=0 gives
ΔReg<=−j*u−(H0+v0)z<=0. A negative kappa_H is NOT multiplied by
the upper bound2(x²+y²). This distinction matters for any stronger
shape lemma under study by the separate helper.

On the whole R=1 domain, the weaker POSITIVE-curvature scalar lemma

    H(theta)−H0 <=(253/24000)*theta², |theta|<=1

already implies ΔReg<=0, because cR*j>(11/48)(23/250)=253/12000.
Thus a nonincreasing-from-zero scalar shape is again stronger than
needed for this useful consequence. The fractional central Ec remains;
D10's actual positive alpha^(3/2) obstruction is fully compatible.

## 5. An unconditional bookkeeping corollary of accepted D37

D37 ALREADY proves H(theta)−H0<=theta²/3 for |theta|<=1. Thus(9)
and(3), without any new scalar hypothesis, give

    ΔReg <=(2/3)(x²+y²)−j*u−(H0+v0)*z
           <=(7747/12000)(x²+y²), r<=1.            (11)

This improves old19/24 by1753/12000. It is merely the accepted
increment with its formerly discarded endpoint loss and positive H0
baseline restored; there is no new H derivative estimate. The exact
first line is stronger than the numerical coefficient and preserves
the useful correlation with actual u.

Consequently EVERY accepted central-root majorant on a subdomain of
rho<=1 may be added to(11) on precisely that domain. The old19/24
regular term is replaced by7747/12000, leaving its fractional/log
central terms unchanged. For a matched finite relative comparison
of the form

    S−Lambda_c <= ΔC∞−u*Vregion+Cregion+kx*x+ky*y,

the stronger unrelaxed consequence is

    S−Lambda_c <= Ec+(2/3)(x²+y²)
             −u*(Vregion+j)+Cregion+kx*x+ky*y−(H0+v0)z. (12)

Under Hmax0 (if proved separately), replace the2/3 quadratic term in
(12) by0. This explains concretely why the scalar frontier could matter
to a FUTURE512 assembly. It does not prove positivity of its remaining
finite allowances or floors, certify an extra degree, or remove E0.

If only the uniform(H-epsilon) premise is proved, combine it with
the EXISTING accepted local increment to use

    omega(theta)=min(theta²/3,epsilon)

in(9). A phase-blind positive epsilon by itself does NOT imply a
vanishing local curvature improvement through zero. This exact min
retains the near-origin charge and could help a farther region without
asserting Hmax0.

## 6. Unconditional correlated GLOBAL outer consequence

This is another direct consequence of the SAME exact master inequality,
using only the ALREADY ACCEPTED global H<1/2 and (3). Set
epsilon=11/50: H0+epsilon>1/2, so(H-epsilon) holds without any
new scalar hypothesis. Subtract Cstar in the first line of(4) and
use the EXACT ce+cd=2−u−z to retain

    ΔC∞ <=2epsilon−(j+epsilon)u+t0*p
                                      −(H0+v0+epsilon)z
          <11/25−(39/125)u+(221/500)p.              (13)

Only a negative z term was dropped. This full closed-diamond inequality
does not use the near Ec identity or require Hmax0. It is stronger in
the required phase correlation than replacing C∞ by a uniform number.

Define on0<u<=1

    f(u)=2sqrt[u(1−u)] if u<=1/2, and f(u)=1 if u>=1/2,
    s(u)=min(2,sqrt(8u)).

Then p<=f(u), P=sinx+siny<=s(u). For the p branch, cosx>=1−2u
follows from cos y<=1. ONLY when u<=1/2 is this lower bound
nonnegative and legitimately squared to get p²<=4u(1−u).
For u>=1/2 use the separate p<=1 bound; do not extend the first
branch. The accepted P bound follows from P²<=2(sin²x+sin²y)<=8u
and P<=2. Both piecewise bounds agree at u=1/2.

For the accepted full global representation and actual origin,

    |S_n−M∞|<=CE(n)+KD(n)P,
    |Lambda_c−M∞(0)|<=E0(n), n>=32,

with EXACT CE from accepted E02 retained rows and KD from accepted
D35, C08's coefficient loss and(13) give

    Lambda_c−S_n > G_n(u),
    G_n(u)=u[T(n)+39/125]−11/25−(221/500)f(u)
                                      −CE(n)−KD(n)s(u)−E0(n). (14)

All ordinary, retained, mesh, regular-outer and ACTUAL-origin charges
are still present. This is an absolute global comparison; no local
increment is silently used to remove the origin E0 cost.

For ANY chosen0<u0<=1, positivity of the ONE gate G_N(u0)>0 is
sufficient for all u>=u0 and every real n>=N>=32. Indeed f(u)/u
is2sqrt[(1−u)/u] below1/2 and1/u above it, hence decreasing with
the same endpoint value. Likewise s(u)/u decreases on both branches;
every positive constant/u decreases. Therefore G_n(u)/u increases
on(0,1], without needing a separate large-T derivative assumption.
Also T increases while CE,KD,E0 decrease for real n>=32 by their
accepted full formulas; (67+19L)/n+318/n² is decreasing there.
Thus G_n(u0)>=G_N(u0), and
G_n(u)>=(u/u0)G_n(u0)>0. No degree or phase evaluation is required
to prove this sufficient implication.

For the existing outer region r>=1 take u0=u1=47/384, using exactly
the accepted alternating-cosine lower proxy. Then

    f(u1)=sqrt(15839)/192<2/3,
    s(u1)=sqrt(47/48).

Let GO_old=u1*T−Dc−CE−KD*sqrt(47/48)−E0, the previous exact
uniform-Dc outer gate. Without evaluating EITHER gate at any degree,

    G_n(u1)−GO_old
      =Dc−11/25+(39/125)u1−(221/500)f(u1)
      >17/20−11/25+1833/48000−221/750
      =7369/48000>3/20.                            (15)

Here Dc=6211/7260>17/20 and15839<16384 prove the only additional
comparisons. This is a fully unconditional quantitative outer-budget
improvement, not a new onset: the endpoint G_N(u1)>0 at a future
chosen N, and every matched near/corner/physical part, remain separate.
No scientific/scalar/source job is proposed as already authorized.

## Limitations, next proof obligation and execution record

The theorem proves an explicit consequence map, not the scalar H
premise. Hmax0, stronger cosine shape and new scalar curvature remain
with the separate E06-H-frontier record at its true status. Full finite
D13/cusp-aware whole-near improvement remains OPEN; none of the finite
ordinary/reference/logarithmic, retained, mesh, outer or actual-origin
charges is deleted. The accepted fractional root obstruction rules out
calling C∞ itself a quadratic function near zero even if ΔReg<=0.

The cheapest next PAPER obligation for global9/4 is the weaker uniform
H<=H0+1/400, or any certified excess satisfying(6); for a nonpositive
regular increment it is the local curvature<=253/24000, rather than
the unnecessarily strong cosine shape. No scalar source or endpoint
job is needed to read these implications, and none is authorized here.
Any future lower-onset application needs a new complete matched
physical theorem and distinct audit, not only this consequence map.

Actual activity: read-only rules/Git/provenance/hash/text/clock checks,
fresh gate searches, hand symbolic rational arguments and owned prose
writes. No script/import/source/scalar/control/endpoint/native/phase/
quadrature/build/degree/threshold/pack job ran. Scientific CPU=0;
ordinary tool overhead unmeasured. Distinct review of this exact proof
is required before adoption of its unconditional bookkeeping corollary
or use of its conditional consequences in a new theorem.
