# E04-wide-retained-origin — Actual finite-origin increments through radius one

Provisional developer theorem, no global ID allocated. Aliases: wide
relative R2 endpoints; cosine-weighted central cot vectors; vanishing
six-row wide allowance. Split from: E04's larger-near-region assembly.
The full ordinary/reference/pole remainder remains a separate OPEN
obligation, not a part proved by this retained-row theorem.

## Exact statement and status

For EVERY integer n>=32 put m=n+1,mu=n/m,L=logn,H=1+L and
H_n=sum_(j=1)^n1/j. Initially alpha,beta>=0,rho=alpha+beta<=1. Set

    ce=cos(rho/2),cd=cos((alpha-beta)/2),a=ce*cd,
    a=(cos alpha+cos beta)/2,p=sin alpha,q=sin beta,P=p+q.

Use EXACTLY PD-T101/PD-T364's corrected Padua polynomial G=D-cos(nu),
exceptional highest first-coordinate coefficient ONE, original endpoint
weights, unequal n,m meshes and actual finite-polynomial collision values.
Jend is the normalized sum of FOUR endpoint rows0,1,2m-2,2m-1; Jcen is
the TWO actual central rowsm-1,m; J6=Jend+Jcen and C2 is the SAME
N1/D04/D07/D20/E03 endpoint reference. Define delta_a X=X(phi)-aX(0).

Throughout the ENTIRE closed radius-one phase triangle,

    |delta_a(Jend-C2)|
       <=a*rho(6/n+148/n^2)+P(11/n+4/n^2),                 (1)
    |delta_a Jcen|<=(3/2)*a*rho*H_n/n,
    Jcen(0)=2/m EXACTLY,                                  (2)
    |delta_a(J6-C2)|
       <=a*rho{[(3/2)H_n+6]/n+148/n^2}+P(11/n+4/n^2)     (3)
       <=rho{[(3/2)H+17]/n+152/n^2}.                       (4)

Signed comparison objects use their separate absolute phases as in D05,
so these bounds hold on the CLOSED signed diamond |alpha|+|beta|<=1,
including its axes, seam, both parities, every sample zero and actual
polynomial collision. No raw negative-beta fixed-row invariance or
n,m interchange is assumed. Every origin value is the SAME ACTUAL
finite-degree origin, not a limiting model or rounded value.

Overall status: **PROVED developer PAPER theorem**, pending distinct
mathematical review/root adoption. This is a reconstructed WIDE-domain
bound, not an assertion that E03's near-half constants hold unchanged.
No640/512/onset sign, code, scalar, numerical endpoint or native job.

## 1. Fresh wide domain and complete endpoint sample set

The elementary radius-one inequalities are

    ce,cd>=7/8,a>=49/64,P<=rho<=1,
    2a-P>=17/32>0.                              (5)

The complete row numerator for(r,b)=(1,beta),(1,-beta),(2,-beta),
w=r*pi+b,z=j*pi+alpha,u=z/n,v=w/m, is the SAME corrected one:

    F_j=[a(1+cosv)-(p/2)sin u+(sin b/2)sinv]/(cosu-cosv).

Here0<w<7,0<v<7/33<pi/2. Its doubled numerator is>=2a-P>0 by(5).
Using pi>25/8 and k=r+/-j in{1,3}, the proposed samples satisfy

    w+/-z>=k*pi-rho>=(17/8)k,
    mu*w+/-z>=(17/8)k-7/33>=(19/10)k.           (6)

The last comparison is505/264>19/10. At the first excluded sample
|z|>w>mu*w because pi>rho, and all more distant ones are excluded.
Thus the COMPLETE positive samples remain{0},{0},{-1,1} on this NEW
domain. They all lie in the actual signed half-open mesh. The closest
rowr0 has no positive sample and retains its linked exact beta0 value.
There are no endpoint collisions on this domain. This is the already
accepted D37-wide sign geometry freshly checked here, not E03's weaker
half-radius geometry transferred by notation.

Consequently, with Dh=mu²w²-z²,

    K=sinc((u+v)/2)sinc((u-v)/2),
    Hh=(1+cosv)/(2K),g=-p sin u+(sin b)sinv,

the exact E03/D07 finite-h algebra is valid on all four endpoint rows:

    e_r=R_r/(nm)-ell_r
       =-a/m+(sin b/w)[tau(v/2)-1]
        +8a sum[mu/Dh-1/(w²-z²)]
        +8mu*a sum(Hh-1)/Dh+2mu sum g/(Dh*K),
    e_0=-a/m+sinc(beta)[tau(beta/(2m))-1].        (7)

All four signed-a/m terms and their TRUE origin values are retained.
The reference C2 and its linked sinc0=1 are unchanged.

## 2. Subtract the endpoint origin FIRST and bound NEW wide derivatives

Let Sdisp=sum_samples,signs1/[(mu*w+/-z)(w+/-z)] and
QH=sum_samples(Hh-1)/Dh. The EXACT subtraction is

    delta_a(Jend-C2)
       =(4a/m)[Sdisp(phi)-Sdisp(0)]
           +8mu*a[QH(phi)-QH(0)]+Ttau(phi)+Tg(phi).        (8)

The four-a/m terms cancel identically. The tau and g terms vanish at
the actual origin. No absolute endpoint allowance is deleted by fiat.

Along the straight phase path every denominator bound(6) remains valid,
and both linear-factor slopes have magnitude<=rho. A reciprocal product
therefore has derivative at most

    rho*(80/323)*(10/19+8/17)/k^3
                       =(25760/104329)rho/k^3.

The eight k values are six1s and two3s. Hence

    |Sdisp(phi)-Sdisp(0)|
       <=[25760/104329]*(6+2/27)rho
        =4224640rho/2816883 <=(3/2)rho.          (9)

This last exact comparison is8449280<8450649. Thus the principal
displacement contribution in(8) is<=6a rho/n. This uses the WIDE
margins, not the old16/5 near-half coefficient.

On the same domain |z|<pi+1<17/4,|u|<17/(4n),|v|<7/n. The sinc
bounds give

    K>=49/50, |Hh-1|<=19/n²,
    sum_samples1/Dh<=800/1083.                 (10)

For example1-K<=(u²+v²)/12 and n>=32 give the first inequality;
[(17/4)²/12+49/3]*(50/49)<19 proves the second. The k pair products
give(100/361)(1+1+1/3+1/3)=800/1083 for the third.

Use |sinc' x|<=|x|/3 and |dot u|+|dot v|<=rho/n. As in a direct
wide calculation, |dot K|<=7rho/(6n²) and

    |dot Hh|<=[(50/49)(7/2)+(50/49)²(7/6)]rho/n²
                 <=5rho/n².

The wider inverse-Dh derivative is now

    |dot(1/Dh)|<=(20/19)rho/Dh.

Thus after integrating the COMPLETE difference QH-QH0,

    |QH(phi)-QH(0)|
       <=[5+19*(20/19)]*(800/1083)rho/n²
        =(20000/1083)rho/n²,
    8mu*a*|QH(phi)-QH(0)|<=148a rho/n².         (11)

The last comparison is160000<148*1083=160284. Keeping the actual
a outside the difference is justified by the exact subtraction(8);
no derivative of a is incorrectly omitted.

The whole sine term in(7) obeys |g|<=7P/n. With(10),
2mu sum1/(Dh*K)<=2*(50/49)*(800/1083), giving

    |Tg|<=560000P/(53067n)<=11P/n.

The three nonzero w sum to4pi-beta. On0<=beta<=1, the NEW bound
sinbeta>=5beta/6 implies beta²<=6q/5; beta²<=q is not assumed.
The complete four tau terms therefore give

    |Ttau|<=[q(4pi-beta)+beta²]/(4m²)<=4P/n².

These are weak inequalities at P0, where both sides vanish exactly.
Combining(8)--(11) proves(1) throughout the full closed radius.

## 3. The ACTUAL central finite vectors, unchanged origin and wider range

Let the linked cyclic vector, k modulo n, be

    L_(n,k)(theta)=sin(theta)cot((k*pi+theta)/n),
    L_(n,0)(0)=n,L_(n,k)(0)=0 if k not0modn.      (12)

The exact corrected-kernel identity Q_n(t)=sin(nt)cot t
=cos t*U_(n-1)(cos t) supplies its actual polynomial limits, not a
value assigned to a bare cotangent. Rebuilding the parity signs with
j=n+2k for r=m and j=n-1+2k for r=m-1 gives exactly

    F_(m,k)=[ce L_(n,k)(theta_-)+cd L_(n,k)(theta_+)]/(2c),
    theta_+/-=(alpha+/-mu beta)/2,c=cos(beta/(2m)),
    F_(m-1,k)=[ce L_(n,k)(eta_-)+cd L_(n,k-1)(eta_+)]/(2c),
    eta_-=(alpha-mu beta-pi/m)/2,
    eta_+=(alpha+mu beta+pi/m)/2,c=cos((pi-beta)/(2m)).   (13)

Each vector contains ALL n residues. The k-1 shift is a cyclic
permutation; no finite endpoint/mask is removed. The actual row norm is
the l1 norm of its whole vector divided by nm. These identities follow
from the full finite polynomial, not from an endpoint error formula
evaluated outside its radius. They include every central collision.

At the actual origin rowm has its one nonzero finite collision value n;
rowm-1 has all positive finite samples and exact signed sum n. Hence
Jcen(0)=2/m for BOTH parities. In(13) rowm has theta0=0, whereas
rowm-1 has eta0=+/-epsilon,epsilon=pi/(2m). These are the origins
actually subtracted, not two artificial zero-shift vectors.

For the NEW rho<=1 range,

    |theta_+/-|<=1/2,
    |eta_+/-|<=1/2+pi/(2m)<11/20,
    c>=cos(epsilon)>99/100,
    ce,cd>=7/8.                                (14)

Here pi/(2m)<1/20 follows from pi<22/7<33/10,m>=33. The straight
parameter paths stay in these ranges. The old E03 |theta|<=3/10 bound
is not applied at a wider argument.

## 4. NEW uniform derivative with the actual harmonic lower bound

For EVERY n>=32,

    7/2<=H_n<=1+logn<=n/4.                    (15)

The lower bound follows by grouping1,2,3..4,5..8,9..16,17..32:
the first contributes1 and each remaining group>=1/2. The upper
integral bound is standard, and n/4-1-logn increases from n32 where
log32<4. These are paper inequalities, not a degree computation.

For |theta|<=11/20, center the cyclic representatives with |k|<=n/2.
For k nonzero, the cotangent argument's distance to piZ is at least

    [pi|k|-11/20]/n >=(5/2)|k|/n,

because pi>25/8 and25/8-11/20=103/40>5/2. The same lower bound
holds at the half-period residues. Consequently

    |L'_(n,k)(theta)|<=2n/(5|k|)+11n/(50k²).

Indeed |cot x|<=1/dist, csc²x<=pi²/(4dist²)<=2n²/(5k²), and
|sin theta|<=11/20. Summing nonzero indices costs
(4/5)nH_n+(22/25)n. The linked k0 component is
n sinc(theta)tau(theta/n). Since |sinc' theta|<=|theta|/3 and
|tau'(y)|<=2|y| on the small argument,

    |L'_(n,0)|<=11n/60+11/(10n)<=n/5, n²>=66.

Thus the full derivative is bounded by

    ||L'_n(theta)||_1<=(4/5)nH_n+(27/25)n
       <=(194/175)nH_n<=(9/8)nH_n.             (16)

The last comparison is1552<1575 and uses H_n>=7/2. In particular
||L_n(theta)-L_n(theta0)||_1<=(9/8)nH_n|theta-theta0|.
This estimate explicitly rebuilds the l1 harmonic constant on the WIDE
domain and uses the actual available n32 harmonic lower bound.

At the two actual origin shifts+/-epsilon,

    ||L_n(+/-epsilon)||_1
       <=n+(9/8)nH_n epsilon <(25/16)n.        (17)

Here H_n<=n/4 and pi<4 give1+9pi n/(64m)<25/16. No origin norm or
coefficient-motion contribution is discarded.

## 5. Preserve the cosine multiplier in both central increments

For either row write A=ce/(2c),B=cd/(2c). Since a=ce*cd and(14),

    A+B=(a/(2c))(1/ce+1/cd)<=8a/(7c).

Each theta/eta displacement from its OWN origin in(13) has magnitude
<=rho/2. From(16) their weighted vector displacement therefore costs

    (9/8)nH_n*(rho/2)(A+B)
       <=[9/(14c)]a rho nH_n<=(2/3)a rho nH_n. (18)

The last inequality uses c>=99/100, so9/(14c)<=50/77<2/3.

For rowm the residual coefficient is(A+B-a)L_n(0), with

    0<=A+B-a<=a*rho²/6.                       (19)

To verify it, (1/ce-1),(1/cd-1)<=rho²/7 and
1/c-1<=rho²/(8m²c). Thus(A+B-a)/a is at most
rho²[1/(7c)+1/(8m²c)]<=rho²/6: the latter follows from
6/7+3/(4m²)<7/8<c. This uses the ACTUAL positive ce,cd,c on this
domain; it is not a substitution into a fake independent phase tuple.
After nm normalization, (19)'s cost is<=a rho²/(6m), at most
a rho H_n/(21n) by rho<=1,H_n>=7/2. Together with(18) it is
<=(5/7)a rho H_n/n<=(3/4)a rho H_n/n.

For rowm-1 put c0=cos(epsilon),A0=B0=1/(2c0). The exact coefficient
errors after subtracting a times origin are A-aA0 and B-aB0. Since
ce-a=a(1/cd-1)<=a rho²/7 and likewise cd-a<=a rho²/7, while
|(1/c)'_beta|<=2/m², one obtains

    |A-aA0|,|B-aB0|<=a rho²/13+a beta/m².       (20)

Here2*7*c>13 justifies the first denominator. Multiplying their SUM
by(17), and dividing by nm, gives coefficient-motion cost

    <=a[(25/104)rho²/m+(25/8)beta/m³]
    <=a rho/n[25/104+25/(8m²)]
    <=a rho/(4n)<=a rho H_n/(14n).             (21)

The comparison in the third line is2600<=8m² at m>=33. Adding(18)
gives at most(31/42)a rho H_n/n<=(3/4)a rho H_n/n for this row.
Thus EACH actual central row obeys that bound; their SUM proves(2).
The norm inequality ||X||1-a||Y||1 in absolute value is bounded by
||X-aY||1, so no differentiability of a moving absolute-value sign is
assumed. All linked zeros, shifts, origins and residue weights remain.

Combining(1),(2) proves(3), and a<=1,P<=rho,H_n<=H gives(4). QED.

## Complete wide assembly consequence, with ordinary costs still explicit

The accepted D37-wide Erow estimate on its LITERAL rho<=1 domain is

    delta_a Erow<=4a/n+20/n²+40aH/(pi*n²)+rho(8H+10)/n.

Adding(3) gives a complete valid ONE-SIDED ordinary-plus-retained bound
with the SAME actual origins:

    delta_a(Erow+Eret)
     <=4a/n+20/n²+40aH/(pi*n²)
        +rho{[8H+10+a((3/2)H_n+6)]/n+148a/n²}
        +P(11/n+4/n²)                            (22)
     <=4a/n+20/n²+40aH/(pi*n²)
                         +rho{[(19/2)H+27]/n+152/n²}.

The ordinary central-reference4a/n and weighted-pole20/n²+40aH/(pi*n²)
are STILL charged. Removing the old19a/n+184a/n² retained constant
does NOT complete the true-origin joint ordinary/reference/pole theorem.
All full D13 and unified cusp-aware bounds remain OPEN.

The exact final conversion for E=S-M_infty is always

    E(phi)-E(0)=delta_a E-(1-a)E(0)
                      <=delta_a E+(1-a)E0.

The same COMPLETE D16 actual-origin E0 must be retained in any complete
S-minus-origin comparison. No rounded model-origin replacement or
additional near-model correction is inserted.

For a fixed actual phase the explicit scalar coefficients in(3)--(4)
are positive and decreasing on realn>=32 when H_n is safely majorized
by H=1+logn. No unproved monotonicity of actual finite rows is asserted.
D14 owns any matched640 endpoint/geometry/floor/global assembly; these
supporting inequalities do not assert its success or a lower global onset.

## Cusp, failed shortcuts and provenance

The real finite central alpha cusp remains: PD-T220 and accepted E03
give slopeell_n~logn/(pi*n)>0. This theorem RETAINS an H_n-linear phase
charge and so does not conflict with the accepted E03-unified obstruction
to a uniform C*rho/n+K*H*rho²/n upper. No purely quadratic smoothing,
interchange of fixed-n/fixed-phase limits or full signed cancellation is
claimed. The old E03 rhohalf theorem and E02 full-diamond bound stay
unchanged; neither alone supplied this wider relative result.

2026-11-07, requested Codex gpt-6.1-sol xhigh, serving metadata unexposed;
input1045157b45f6ede45802975656a06ecf064dc21a, rules read63c70b7 with
unchanged diff checked. Complete registry/current/table baseline reused
with identical actual hashes; fresh E04 searches/full relevant predecessor
reads, all candidates and kill tests are recorded in the owned idea/attempt.
This is a quantitative domain continuation, not a new kernel principle or
historical-priority claim. Distinct mathematical review/root adoption is
required. Only the THREE assigned new E04 prose paths changed; no
source/code/script/scalar/endpoint/threshold/native/phase/board/root/
quadrature/degree/compile/control/pack/shared/Git action or global ID.
No scientific job or source import ran; all such jobs remain UNRELEASED.


## Root adoption of reviewed support —2026-11-07

EVERY n>=32, CLOSED signedrho<=1: |delta_aEret|<=a*rho{[(3/2)H_n+6]/n+148/n²}+P(11/n+4/n²). Endpoint/central split, exact origin, coefficient motion and masks/collisions are retained; ordinary/pole and actual-origin charges remain separate.

Distinct [review](../independent-checks-E04-wide-retained-origin.md), frozen support-report identity
ea0297b364849b338303339a2d076a8b1e8d9ca3f45eb4b74d8df94549412ca7, accepts the unchanged reviewed prefix
c561f1f119b94bd517eafa4000a8b2af7a659af10f7954e35d66717c97dcbb59.
No scalar/source/native/finite-degree/pack job occurred. Global onset
remains768, residual719; fullD13 and matched640 remain OPEN here.
