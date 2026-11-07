# PD-T?argmax-bridge-codex-F01-seam-retained — Actual-origin six rows through five fourths

ID kind: PD-T. Aliases: I07 retained-row domain continuation; wider finite-h
endpoint increments; wider cyclic cotangent vectors.
Split from: F01 complete finite relative allowance, in F01-seam-finite.md.
Split into: none.

## Statement, definitions and assumptions

For EVERY integer n>=32 let m=n+1,mu=n/m,H_n=sum_(j=1)^n 1/j. Initially
alpha,beta>=0,rho=alpha+beta<=5/4. Set ce=cos(rho/2),
cd=cos((alpha-beta)/2),a=ce*cd,p=sin alpha,q=sin beta,P=p+q.
Use EXACTLY E04-wide-retained-origin's actual corrected polynomial,
exceptional top mode ONE, n/m meshes, endpoint weights, four endpoint rows
0,1,2m-2,2m-1, two central rows m-1,m, and SAME endpoint reference C2.
Every origin is the actual finite-degree origin. Write delta_a X=X(phi)-aX(0).

On the ENTIRE CLOSED signed diamond rho=|alpha|+|beta|<=5/4,

    |delta_a(Jend-C2)|<=a*rho(9/n+183/n^2)+P(13/n+4/n^2),
    Jcen(0)=2/m,
    |delta_a Jcen|<=(9/5)*a*rho*H_n/n,
    |delta_a Eret|<=a*rho[((9/5)H_n+9)/n+183/n^2]
                                      +P(13/n+4/n^2)
                 <=rho[((9/5)(1+log n)+22)/n+187/n^2].       (1)

Exact real arithmetic; no numerical premise. Signed objects use the inherited
separate-absolute-phase comparison, not an invariance claim for a raw fixed
negative-beta row. All linked polynomial collisions and both parities remain.

Overall status: **PROVED developer PAPER theorem**, requiring distinct review
and root adoption. This is a freshly proved domain continuation, not a change
to E04's old quantifier. No degree endpoint or new argmax onset is asserted.

## Depends on

Accepted E04-wide-retained-origin supplies the exact full finite identities
(7),(8),(12),(13), their true origins and collision interpretation; D37/D07
supplies the unchanged C2. Their radius-one numerical inequalities are NOT
used on the larger domain. The elementary sinc/tau estimates used in their
proofs are applied below only inside their literal small-argument domains.
The harmonic inequalities 7/2<=H_n<=1+log n<=n/4 hold for n>=32 by the same
six dyadic groups/integral argument, without a degree computation.

## Proof

### 1. Complete positive sets and finite-h margins on the new domain

Put cR=103/128. The cosine lower polynomial gives

    ce,cd>=cR, a>=10609/16384>5/8,
    P<=rho<=5/4, 2a-P>=369/8192>0.                         (2)

For endpoint charts (r,b)=(1,beta),(1,-beta),(2,-beta) put
w=r*pi+b,z=j*pi+alpha,u=z/n,v=w/m. On the proposed positive samples
j=0,0,-1,1, respectively, pi>25/8,pi<22/7 imply

    0<w<13/2, |z|<9/2, 0<v<13/66<pi/2,
    w+/-z>=(15/8)k,
    mu*w+/-z>=(15/8)k-13/66>=(5/3)k, k=r+/-j in{1,3}.  (3)

The weakest last comparison is443/264>5/3. The doubled complete numerator
is at least2a-P because cos v>=0. It is positive by (2). The first excluded
sample satisfies |z|>w>mu*w since pi>rho; all more distant samples remain
excluded in the actual centered half-open mesh. Thus the COMPLETE positive
sets remain{0},{0},{-1,1}. The r0 chart has no positive sample and keeps its
linked beta0 value. No endpoint denominator collision occurs in (3).
Consequently the exact full finite-h identities from E04 are valid here:

    Dh=mu^2*w^2-z^2,
    K=sinc((u+v)/2)*sinc((u-v)/2),
    Hh=(1+cos v)/(2K), g=-p sin u+(sin b)sin v,
    delta_a(Jend-C2)=(4a/m)[Sdisp(phi)-Sdisp(0)]
                    +8mu*a[QH(phi)-QH(0)]+Ttau+Tg,
    Sdisp=sum_samples,signs 1/[(mu*w+/-z)(w+/-z)],
    QH=sum_samples (Hh-1)/Dh.                             (4)

The four -a/m terms cancel in this exact subtraction. Ttau,Tg vanish at the
actual origin. No derivative of a is omitted: a is outside each difference
in the exact identity (4).

### 2. Endpoint increments with every charge retained

Along the straight phase path, each linear-factor slope in (3) is bounded
by rho. A reciprocal-product derivative is therefore at most

    (8/25)(8/15+3/5)*rho/k^3=(136/375)*rho/k^3.

The eight k values are six1s and two3s, so

    |Sdisp(phi)-Sdisp(0)|<=(22304/10125)rho<(9/4)rho.

Multiplication by4a/m costs at most9a*rho/n. Here89216<91125 proves the
last comparison; this replaces, rather than assumes, E04's old displacement
coefficient6.

Since |u|<9/(2n),|v|<13/(2n), elementary sinc bounds give

    1-K<=(u^2+v^2)/12<=125/(24n^2), K>=99/100,
    |Hh-1|<=[u^2/12+v^2/3]/K<16/n^2,
    sum_samples 1/Dh<=(9/25)(8/3)=24/25.                  (5)

The K bound uses12500<24*32^2. The Hh comparison is75700<76032.
With |dot u|+|dot v|<=rho/n, the two sinc factors give
|dot K|<=13rho/(12n^2). One way to check the factor is that
sum_+/− |(u+/-v)(dot u+/-dot v)|/4 is at most
max(|u|,|v|)(|dot u|+|dot v|)/2. Hence

    |dot Hh|<=[(13/4)(100/99)+(13/12)(100/99)^2]rho/n^2
             <(9/2)rho/n^2,
    |dot(1/Dh)|<=(6/5)rho/Dh.

The first strict comparison is258050<264627. Subtracting the COMPLETE
QH before estimating yields

    8mu*a|QH(phi)-QH(0)|
       <=8a[9/2+16(6/5)](24/25)rho/n^2
       =(22752/125)a*rho/n^2<183a*rho/n^2.                (6)

The full sine remainder satisfies |g|<=(13/2)P/n. By (5),
its contribution is <=(416/33)P/n<13P/n. For the four tau terms,
sin beta>=beta(1-beta^2/6)>=71beta/96, so beta^2<=2q on
0<=beta<=5/4. The three nonzero w sum to4pi-beta. Therefore

    |Ttau|<=[q(4pi-beta)+beta^2]/(4m^2)
             <(51/14)P/n^2<=4P/n^2.

All statements are weak at P=0, where these terms vanish exactly. Combining
(4)--(6) proves the endpoint assertion of (1).

### 3. Central vectors, genuine origins and complete harmonic derivative

Use E04's linked cyclic vector L_(n,k)(theta)=sin(theta)cot((k*pi+theta)/n),
with its finite polynomial value n at k0,theta0. The exact two row charts are
the SAME as E04(13): arguments theta_+/−=(alpha+/-mu*beta)/2 in rowm and
eta_−=(alpha-mu*beta-pi/m)/2,eta_+=(alpha+mu*beta+pi/m)/2 in rowm-1;
weights ce/(2c),cd/(2c), with c=cos(beta/(2m)) or cos((pi-beta)/(2m)).
The second vector in rowm-1 is cyclically shifted by one. ALL n residues,
both parity signs and polynomial collisions remain inside these identities.
Their actual origins are0 in rowm and+/-epsilon in rowm-1,
epsilon=pi/(2m). As in the exact finite signed-sum identity, Jcen(0)=2/m.

The newly checked ranges and their entire straight paths satisfy

    |theta|<=5/8, |eta|<27/40, c>=cos(epsilon)>99/100.       (7)

For centered nonzero cyclic representatives, the cotangent argument's
distance to piZ is at least(pi|k|-27/40)/n>(12/5)|k|/n. This includes a
half-period residue. Thus

    |L'_(n,k)|<=5n/(12|k|)+75n/(256k^2).

Use |cot x|<=1/dist,csc^2x<=pi^2/(4dist^2),pi^2<10 and
|sin theta|<=27/40. Summing nonzero residues costs
(5/6)nH_n+(75/64)n. The linked k0 expression n*sinc(theta)*tau(theta/n)
has derivative <=(9/40)n+27/(20n)<=(23/100)n, using n^2>=270.
Consequently

    ||L'_n(theta)||_1<=(5/6)nH_n+(2243/1600)n
                     <=(5/4)nH_n.                        (8)

The last comparison follows from H_n>=7/2 and53832<56000. The small tau
arguments are inside pi/4. At the true shifted origins, (8) also gives
||L_n(+/-epsilon)||_1<=n+(5/4)nH_n*epsilon<(13/8)n.

### 4. Coefficient movement and both central rows

Let A=ce/(2c),B=cd/(2c). Then A+B<=128a/(103c). Each argument's movement
from its OWN origin is <=rho/2, so the vector-motion cost before nm
normalization is

    (5/4)nH_n*(rho/2)(A+B)
       <=(8000/10197)a*rho*nH_n<=(4/5)a*rho*nH_n.          (9)

For rowm the remaining multiplier satisfies0<=A+B-a<=a*rho^2/6.
Indeed 1/ce-1,1/cd-1<=16rho^2/103 and
1/c-1<=rho^2/(8m^2c), so it suffices that
96/103+3/(4m^2)<c, which follows from c>=99/100,m>=33.
Its normalized cost is <=(5/84)a*rho*H_n/n. With (9) the row costs
at most(361/420)a*rho*H_n/n<(7/8)a*rho*H_n/n.

For rowm-1 subtract its ACTUAL coefficients A0=B0=1/(2cos epsilon).
The exact identity A-aA0=(ce-a)/(2c)+(a/2)(1/c-1/c0), and its B analogue,
give

    |A-aA0|,|B-aB0|<=a[(2/25)rho^2+beta/m^2].

Here800/10197<2/25 and |(1/c)'_beta|<=2/m^2 are legal on (7).
Paying BOTH errors against the true shifted-origin vector norms gives

    a[(13/50)rho^2/m+(13/4)beta/m^3]
       <=a*rho/n[13/40+13/(4m^2)]<=a*rho/(3n)
       <=(2/21)a*rho*H_n/n.

The middle comparison only needs m^2>=390. Together with (9) this row
costs at most(94/105)a*rho*H_n/n<(9/10)a*rho*H_n/n.
The sum7/8+9/10=71/40<9/5 proves the central assertion. The reverse
triangle inequality for complete l1 norms justifies these differences
without differentiating any moving absolute-value sign or root.

Add endpoint and central estimates to obtain (1), then use a<=1,P<=rho
and H_n<=1+log n. All phase-zero statements follow directly from exact
subtraction. This proves the closed domain, including its seam and collisions.

## Checks, sources, scope and history

Paper proof only; no script/import/scalar/endpoint/degree/phase/threshold/
native/quadrature/build/control/pack job. No external theorem or priority claim.
All positive coefficients decrease for real n>=32 after H_n is majorized by
1+log n. Ordinary/pole, outer, scalar mesh and true-origin charges remain
separate. This alone neither closes full D13 nor changes the global onset.

2026-11-07, requested Sol xhigh, actual serving metadata unexposed. Rules/input
4a5de2012bad94601c713b2ff5517f2e3fb80af2. Full gate, separate root release,
local prospective registration and exact coefficient continuation are in
ideas/attempts F01-seam-domain.md. Only owned new prose changed; distinct
mathematical review and root adoption are not performed by this author.


## Root disposition after distinct review —2026-11-07

Root adopts the written mathematical statement at its exact quantifiers and named dependencies. The original frozen proof/interface prefix is preserved and identified in [F01 independent mathematical review](../independent-checks-F01-seam.md), final13512B SHA25639dcb7fbf90e619f07a99ecb75b5f533722e9c3deec62d0b2ca0d5eb6a960313. This supplies no smaller onset, new finite degree, novelty/priority verdict, protocol waiver or readiness. Final Claude review remains separate.
