# E03-joint-row-origin — Actual-origin cancellation for all six retained rows

Provisional developer paper; no global ID allocated. Aliases: linked
finite central cot vectors; relative R2 endpoints; true-origin retained
row increment. Split from: E03's complete ordinary-plus-retained joint
vanishing target, which remains OPEN. The theorem below is a supporting
retained-row result, not completion or a parameter case of full D13.

## Statement and status

For EVERY integer n>=32 put m=n+1,mu=n/m,H_n=sum_(j=1)^n1/j,H=1+logn.
On alpha,beta>=0,rho=alpha+beta<=1/2 set
a=(cos alpha+cos beta)/2,p=sin alpha,q=sin beta,P=p+q. Use EXACTLY
PD-T101/PD-T364/D05's corrected polynomial, exceptional highest first-
coordinate coefficient ONE, original endpoint weights and actual finite
polynomial collision values. Let Jend,Jcen,J6=Jend+Jcen and the SAME C2
be the four-endpoint/two-central quantities in D07/D20/E02. Define

    delta_a X=X(alpha,beta)-aX(0,0), Eret=J6-C2.

The origin values below are the ACTUAL finite rows at the same degree.
Then on the ENTIRE closed near triangle,

    |delta_a(Jend-C2)|
       <=a*rho[16/(5n)+78/n^2]+P[7/n+4/n^2],              (1)
    |delta_a Jcen|<=2rho H_n/n, Jcen(0,0)=2/m,             (2)
    |delta_a Eret|<=rho[(2H+51/5)/n+82/n^2].              (3)

The same statements hold on the full CLOSED signed near diamond by
the inherited separate-absolute-phase comparison convention. No raw
negative-beta fixed-row invariance or exchange of n,m is claimed.

Overall status of(1)--(3): **PROVED developer PAPER theorem**, pending
distinct mathematical review/root adoption. It removes the old absolute
retained-origin charge18a/n+142a/n² by actual origin subtraction BEFORE
estimates. It does not merely delete that charge from D22 or infer
relative behavior from the absolute E02 bound.

The complete joint vanishing target for delta_a Erow+delta_a Eret remains
**OPEN** because of the ordinary central-reference/weighted-pole pair
identified in section5. The full D13 remainder, any new onset and any
endpoint sign remain OPEN. No scalar/source/native/threshold/pack job.

## 1. Exact joint identity and the true finite origin

Use the fixed labels A6={0,1,2m-2,2m-1,m-1,m}, complement O6 and
the complete D05 intermediate

    K_fixed=J6+B+Delta2,
    B=(1/m)sum_(r in O6)H(logn,v_r),
    Erow=S-K_fixed,Eret=J6-C2.

Thus, BEFORE any triangle estimate,

    Erow+Eret=S-B-Delta2-C2,                       (4)
    delta_a(Erow+Eret)=delta_a[S-B-Delta2-C2].

The explicit J6 cancels algebraically, but its actual finite row values
are still IN S. Equation(4) does not prove that those values have no
increment or that a constant error can be deleted. It retains the SAME
ordinary mask, endpoint normalization, Delta2 and weighted continuation.
The full finite primitive satisfies S(0)=Lambda_c(n), the TRUE symbolic
corner value; no rounded model origin substitutes for it.

The full model conversion remains EXACTLY

    E(phi)-E(0)=delta_a E-(1-a)E(0)
                  <=delta_a E+(1-a)E0, E=S-M_infty,        (5)

with the SAME complete D16 actual-origin |E(0)|<=E0. None of(1)--(3)
removes or changes this charge in a downstream S-minus-origin theorem.

## 2. Subtract the endpoint origin inside the exact finite-h identity

D07-endpoint-finite-h supplies, on this ENTIRE closed radius, the actual
positive samples for(r,b)=(1,beta),(1,-beta),(2,-beta): {0},{0},{-1,1}.
They are all collision-free. Put w=r*pi+b,z=j*pi+alpha,u=z/n,v=w/m,

    Dh=mu^2*w^2-z^2,K=sinc((u+v)/2)sinc((u-v)/2),
    Hh=(1+cosv)/(2K),g=-p sin u+(sin b)sinv,
    e_r=R_r/(nm)-ell_r.

The SAME exact identity, including the highest corrected mode, is

    e_r=-a/m+(sin b/w)[tau(v/2)-1]
        +8a sum_j[mu/Dh-1/(w^2-z^2)]
        +8mu*a sum_j(Hh-1)/Dh+2mu sum_j g/(Dh*K),
    e_0=-a/m+sinc(beta)[tau(beta/(2m))-1],          (6)

with tau y=y cot y,tau0=1 and ell0=sinc beta. In particular the exact
closest-row beta0 value is retained. Define

    Sdisp(phi)=sum_(four samples,both signs)
                1/[(mu*w+/-z)(w+/-z)],
    QH(phi)=sum_(four samples)(Hh-1)/Dh.

The principal endpoint terms in(6) are EXACTLY
-4a/m+4a*Sdisp/m+8mu*a*QH, plus the tau and g terms. At the actual
origin tau and g terms vanish; hence their relative increment is

    delta_a(Jend-C2)
       =(4a/m)[Sdisp(phi)-Sdisp(0)]
           +8mu*a[QH(phi)-QH(0)]+Ttau(phi)+Tg(phi).        (7)

In particular the four -a/m terms cancel EXACTLY. No two independent
absolute endpoint bounds have been subtracted to get(7).

Along the straight phase path the accepted D07 denominator estimates
hold with k=r+/-j in{1,3}:

    w+/-z>=(21/8)k,mu*w+/-z>=(12/5)k,
    K>=49/50, |u|<=4/n,|v|<=7/n,
    sum_samples1/Dh<=25/54.                     (8)

Both linear denominator slopes have magnitude<=rho. A reciprocal
product has derivative magnitude at most

    rho*(10/63)*(5/12+8/21)/k^3
                   =(335/2646)rho/k^3.

The eight k values consist of six1s and two3s. Thus

    |Sdisp(phi)-Sdisp(0)|
       <=[335/2646]*(6+2/27)rho
        =54940rho/71442 <=(4/5)rho.             (9)

The exact last rational comparison is274700<285768. For QH, keep its
origin subtraction before differentiation. The sinc integral gives
|sinc' x|<=|x|/3. Along the path,

    |dot K|<=7rho/(6n^2),
    |dot Hh|<=[(50/49)(7/2)+(50/49)^2(7/6)]rho/n^2
                 <=5rho/n^2,
    |Hh-1|<=19/n^2,
    |dot(1/Dh)|<=(5/6)rho/Dh.

The first line uses |dot u|+|dot v|<=rho/n and
|(u+v)/2|+|(u-v)/2|=max(|u|,|v|)<=7/n. Therefore

    |QH(phi)-QH(0)|
       <=[5+19*(5/6)]*(25/54)rho/n^2
        =(3125/324)rho/n^2,
    8mu*a*|QH(phi)-QH(0)|<=78a rho/n^2.         (10)

Finally the COMPLETE D07 tau and sine contributions obey
|Ttau|<=4P/n²,|Tg|<=7P/n; both are EXACTLY zero at the origin.
Insert(9)--(10) in(7), using m>n, to prove(1). Every statement is weak
at rho0, where the exact relative expression vanishes. The actual
endpoint signs/mesh/reference are unchanged; no larger-radius or old
large-R derivative theorem is transferred down to n32.

## 3. Exact linked finite vectors for the ACTUAL central rows

For k modulo n define

    L_{n,k}(theta)=sin(theta)*cot((k*pi+theta)/n),
    L_{n,0}(0)=n,L_{n,k}(0)=0 if k not0modn.      (11)

The linked values are literal finite-polynomial limits; a bare cotangent
at its pole is never assigned a value. This vector is periodic in k
modulo n. Use centered representatives with |k|<=n/2.

The exact full corrected-kernel cotangent identity follows by expanding
the two coefficient cosines using parity in the finite numerator:

    F_j=[ce*sigma_-*Q_n((u-v)/2)
                   +cd*sigma_+*Q_n((u+v)/2)]/[2sin(v/2)],
    Q_n(t)=sin(nt)cot t=cos t*U_(n-1)(cos t),
    ce=cos((alpha+beta)/2),cd=cos((alpha-beta)/2),
    sigma_- =(-1)^((r-j-1)/2),sigma_+ =(-1)^((j+r-1)/2).

This is an algebraic identity for EVERY interior0<v<2pi, not an
application of an endpoint error theorem at v=pi. Q_n is a finite
polynomial through EVERY t multiple of pi. It agrees with the actual
G_n on the dense noncollision set and hence at all collisions.

For row r=m, take j=n+2k and put theta_+/-=(alpha+/-mu beta)/2.
For row r=m-1, take j=n-1+2k and put
eta_-=(alpha-mu beta-pi/m)/2,eta_+=(alpha+mu beta+pi/m)/2.
Removing the parity signs in the preceding exact identity gives

    F_(m,k)=[ce L_(n,k)(theta_-)+cd L_(n,k)(theta_+)]
                                                /[2cos(beta/(2m))],
    F_(m-1,k)=[ce L_(n,k)(eta_-)+cd L_(n,k-1)(eta_+)]
                                            /[2cos((pi-beta)/(2m))]. (12)

Each k runs over ALL n residues. The shift k-1 is a cyclic permutation,
not omission of a boundary sample. The absolute row norm is the l1
norm of this WHOLE vector, divided by nm. Both n and m stay literal.

At the origin rowm has its single nonzero finite value n. Rowm-1 has
every finite numerator positive and |u|<v=(n*pi)/m: indeed
(n-1)/n<n/(n+1). Thus all its finite signed samples are positive and
the exact signed-row identity gives R_(m-1)(0)=n as well. Consequently

    Jcen(0)=2/m EXACTLY.                         (13)

## 4. Uniform l1 derivative, coefficient motion and central increment

For |theta|<=3/10, the finite vector(11) satisfies

    ||L_n'(theta)||_1<=(4/3)nH_n.                (14)

Here is a complete elementary bound. For nonzero centered k put
x=(k*pi+theta)/n. Its distance to piZ is at least
(pi|k|-3/10)/n>(27/10)|k|/n, even at the half-period representatives.
Using |cot x|<=1/dist and sinx>=2dist/pi,

    |L'_(n,k)(theta)|
        <=10n/(27|k|)+25n/(243k^2).

The harmonic sum over nonzero representatives is<=2H_n and the square
sum<=4. For k0 use L_(n,0)=n sinc(theta)tau(theta/n). The same sinc
bound and accepted |tau'(y)|<=2|y| on |y|<=pi/4 give

    |L'_(n,0)|<=n/10+3/(5n)<=n/9.

Thus the total is at most
(20/27)nH_n+(127/243)n<=(307/243)nH_n<=(4/3)nH_n. This proves(14),
including theta0 by the linked polynomial continuation. In particular

    ||L_n(theta)-L_n(theta0)||_1
                            <=(4/3)nH_n|theta-theta0|.   (15)

All theta/eta values and their straight paths in(12) lie in this range:
rho/2<=1/4 and pi/(2m)<1/20. Write c for the corresponding central
cosine denominator. Both cosines in(12) exceed99/100, so ce/(2c),
cd/(2c) are nonnegative and their sum<=100/99. Their weighted sum of
the two theta DISPLACEMENTS from the ACTUAL origin values is therefore
at most(50/99)rho<=(3/5)rho. Equations(15) give for either row a
displacement contribution<= (4/5)nH_n rho.

It remains to pay coefficient motion relative to a times the origin.
For rowm, let A=ce/(2c),B=cd/(2c),c=cos(beta/(2m)). The exact residual
is(A+B-a)L_n(0). The accepted elementary cosine inequalities give

    0<=ce+cd-2a<=rho^2/4,
    |A+B-a|<=rho^2/4.                           (16)

For example its two terms are bounded by rho²/7 and rho²/(7m²), whose
sum is<=rho²/4. Hence its normalized contribution is<=rho²/(4m),
at most rho/(8n). With(15) and H_n>=1, this proves
|R_m(phi)/(nm)-aR_m(0)/(nm)|<=rho H_n/n.

For rowm-1 put c=cos((pi-beta)/(2m)),c0=cos(pi/(2m)),
A0=B0=1/(2c0). Since ce-a=ce(1-cd)<=rho²/8 and
cd-a=cd(1-ce)<=rho²/8, while |(1/c)'_beta|<=2/m²,

    |A-aA0|,|B-aB0|<=rho^2/15+beta/m^2.          (17)

Let epsilon=pi/(2m). From H_n<=1+logn<=n/4,n>=32, equations(14)--(15)
give ||L_n(+/-epsilon)||_1<=n+(4/3)nH_n epsilon<2n. Thus the
NORMALIZED coefficient-motion cost in(17) is at most

    4rho^2/(15m)+4beta/m^3
       <=[2/15+4/m^2]rho/n<=(1/5)rho/n.

Add the normalized displacement cost<=(4/5)rho H_n/n from(15).
This proves the SAME rho H_n/n bound for rowm-1. Their sum proves(2).
The passage from vector differences to absolute norms uses
||X|_1-a|Y|_1|<=|X-aY|_1, not differentiability of a moving row sign.
Every possible central collision and sample zero is already retained
by the linked finite vectors(11)--(12). Combine(1),(2),a<=1,P<=rho
to obtain(3). QED.

## 5. Complete ordinary-plus-retained upper and the remaining obligation

Keep the accepted D35/D22 ordinary-row increment on the CLOSED near
diamond, with its ACTUAL origin:

    delta_a Erow<=4a/n+20/n^2+40aH/(pi*n^2)
                                           +rho(8H+10)/n.

The central-reference4a/n includes BOTH parity transition rows. The
weighted pole approximations20/n²+40aH/(pi*n²) are still charged
absolutely, as their complete relative estimate is not proved here.
Adding(3) yields the valid complete ONE-SIDED joint upper

    delta_a(Erow+Eret)
      <=4a/n+20/n^2+40aH/(pi*n^2)
                          +rho[(10H+101/5)/n+82/n^2].     (18)

This removes the old retained-row origin constant and genuinely has a
vanishing retained component. But(18) still has a constant4a/n and
two pole-error costs at rho0. They must NOT be deleted. The exact
remaining finite object, away from individual reference poles initially,
is the central SYMMETRIC-reference quadrature plus its weighted-pole
approximation residual. D13 has already cancelled the fixed endpoint
reference and ENTIRE Delta2; D35 has bounded the ordinary perturbation
whose origin is zero. To obtain the full joint vanishing target one
must control the central-reference/pole pair relative to its actual
origin, keeping its discrete jumps at crossed poles BEFORE estimates.

By D05 only the COMPLETE Erow is continuous through every collision.
An individual g0/reference sample or pole-error residual need not be
continuous there. The first ordinary collision along a straight phase
path cannot occur before rho>=pi/m, since its zero-origin mismatch is
a nonzero integer multiple of pi and its phase displacement is at most
m rho. This is an exact geometric observation, NOT yet a bound on
the signed jump sum or the smooth between-jump variation. The missing
quantitative pair estimate remains OPEN; (18) is not full D13 closure.

## 6. First variation and the unavoidable finite central cusp

The positive fixed-n alpha cusp is already PROVED in accepted PD-T220:

    S_n(alpha,0)=Lambda_c+L_n|alpha|+o_n(|alpha|),
    L_n=(nm)^-1 sum_(k=1)^floor(n/2)cot(k*pi/n)>0,
    L_n<=H_floor(n/2)/(pi*m), n>=3.              (19)

Its only zero-origin sampled row is r=m. Formula(12) recovers exactly
that localization: on beta0 its nonzero-origin peak has zero first
alpha derivative, and the other zero samples have derivative
-(1/2)tan(u_j/2). The other retained endpoint/central row samples are
nonzero and smooth/even at zero; C2 is smooth/even there. Hence

    delta_a Eret(alpha,0)=L_n|alpha|+o_n(|alpha|). (20)

The same first variation survives in the COMPLETE JOINT row object(4).
For fixed n, each ordinary zero-phase v_r differs from0,pi,2pi. Its
weighted Phi pair is smooth and even in alpha near0: Phi(t)=Phi(1-t)
and the two offsets sum to1 at zero. The cancellation integral is also
smooth/even there. To see the latter without differentiating moving
roots, choose a sufficiently small FIXED-n alpha neighborhood so that
a(1+cosv)>|p|/2 and both nonzero coefficients retain their origin signs.
Then the complete numerator has its origin sign for EVERY integration
angle. The integrand is exactly affine in a and p with fixed sign pieces;
its reflection X->pi-v-X makes its integral even in p. Its p coefficient
therefore integrates to zero. Thus each ordinary H has zero alpha
derivative. Delta2 and C2 have zero derivative by their symmetric
convergent endpoint expressions. Since a'(0)=0, (4),(19) give

    delta_a(Erow+Eret)(alpha,0)
                         =L_n|alpha|+o_n(|alpha|).         (21)

The finite-n neighborhood used here is not asserted uniform in n.
Equations(20)--(21) rule out a purely quadratic retained/joint row
estimate at every fixed n>=32, exactly as the parent primitive cusp
obstruction predicts. They do NOT refute C*rho*H/n, the requested mixed
bound or physical actual-corner descent. This is a current-operator
consequence/localization of the OLD PD-T220/PD-N079 mechanism, not a new
negative theorem, global ID or historical novelty claim.

For fixed alpha>0,beta0 and THEN n tending to infinity, the actual
vectors(12) give a DIFFERENT useful asymptotic:

    Jcen(alpha,0)=2sin(alpha)*logn/(pi*m)+O_alpha(1/m),
    delta_a Jcen has the SAME leading log coefficient.      (22)

Each finite cot grid has absolute sum(2n/pi)logn+O_alpha(n). In rowm
the two channels coincide. In rowm-1 their peaks are adjacent; for
fixed alpha>0 the shifts remain bounded away from zero for large n,
and opposite signs occur on only a bounded number of adjacent pole
intervals, with total O_alpha(n) contribution. The two sine coefficients
sum to2sin(alpha/2)cos(pi/(2m)), canceling its displayed cosine
denominator and giving sin(alpha)/pi for EACH row. Origin(13) is only
2/m and has no log term. This proves(22) with the stated quantifier order.

The disjoint outer/log helper reports the MATCHING signed removed-cell
term-2sin(alpha)logn/(pi*m) in its same fixed-alpha limit. Thus no full-
sum logarithmic obstruction is asserted. Neither(22) nor that matching
coefficient is uniform at alpha~1/n; no bound for the full coupled
operator is inferred without controlling that transition and all other
finite-reference terms. The genuinely unified signed operator is owned
by the separately allocated helper, not completed by this component.

## Scope, checks and provenance

Only PAPER identities/inequalities, no numerical/scalar/endpoint/phase/
native/board/root/quadrature/degree/compile/source/control/pack job. No
old theory/source/evidence/shared/Git file or frozen E01/E02 prefix was
edited. Only the THREE assigned E03 prose paths were written. All
scientific/source jobs remain UNRELEASED; no guessed global onset.

2026-11-07, requested Codex gpt-6.1-sol xhigh, serving metadata unexposed;
inputa58be81c9f91cf175598968c8ab9b7032946b887. Rules read63c70b7 and
unchanged rule diff checked. Full registry/current/obstruction baseline
is reused with matching actual hashes; fresh immediate-predecessor
searches and full C05/D07/D13/D22/D35/PD-T220 comparisons are documented
in the idea/attempt. Endpoint differentiation is a quantitative small-R
reconstruction, not an application of C05's n1e6/R128 theorem at n32.
All fixed-n and fixed-positive-phase limit distinctions stay explicit.

Independent review must check the exact cot-vector signs/shift/mask,
nm normalization, linked collisions, derivative constants, endpoint
origin cancellation and remaining nonvanishing terms in(18). The full
ordinary/reference/pole pair and the full D13 theorem remain OPEN.


## Root adoption after distinct focused audit —2026-11-07

Root adopts EVERY n>=32, CLOSED rho<=1/2: |delta_a Eret|<=rho[(2H+51/5)/n+82/n²], exactJcen(0)=2/m and stated endpoint/central/fixed-order corollaries. The ordinary central-reference4a/n and weighted-pole20/n²+40aH/(pi*n²) remain paid. This removes the artificial retained-origin constant, not the full joint remainder.

Distinct [review](../independent-checks-E03-joint-row-origin.md), SHA256
675f4e23f238784f62d81302bc079c8189fbb729847bc6a8969bca22ef94b545, accepts the unchanged reviewed prefix
513154f54f00e1995c1fd613379b2ac6613c6e0d17c14760ce722234ea273e8a.
Full D13 remains OPEN. No numerical/source/native/pack job occurred.
Current global onset768 and residual719 are unchanged; final Claude is separate.
