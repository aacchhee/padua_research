# E02-global-retained-rows — A sharper full-diamond six-row comparison

Provisional developer theorem; no global ID allocated. Aliases: direct-nm
finite endpoint chart; fixed four-index near split; collision-safe global
retained rows. Split from: E02's global non-P allowance bottleneck.
The downstream global-error/norm/far formulas below are routine direct
applications, not independently computed onsets.

## Exact statement and status

For EVERY integer n>=32 put m=n+1,L=log n and use EXACTLY the corrected
PD-T101/PD-T364 polynomial G_n=D_n-cos(nu), original endpoint weights,
exceptional highest first-coordinate coefficient ONE and actual finite
polynomial collision values. On absolute phases alpha,beta>=0,
alpha+beta<=pi let R_r be D05's actual n-sample row norms. Define the
SAME fixed six-row quantity and SAME reference C2 as D20:

    J6=[R_0+R_1+R_(2m-2)+R_(2m-1)+R_(m-1)+R_m]/(nm),
    C2=ell_0(beta)+ell_1(alpha,beta)
                            +ell_1(alpha,-beta)+ell_2(alpha,-beta),
    E6new(n)=(67+19L)/n+318/n^2.

Then on the ENTIRE CLOSED phase triangle,

    |J6-C2|<=E6new(n).                           (1)

Extend the comparison objects by separate absolute phases as in D05;
(1) holds on the full CLOSED signed diamond |alpha|+|beta|<=pi. This
includes axes, a=0, every vertex, both parities and ALL actual polynomial
collisions. Raw fixed rows at negative beta are not asserted separately
invariant. No unequal-mesh interchange is made.

Overall status: **PROVED developer PAPER theorem**, awaiting distinct
mathematical review/root adoption. All old N1/D20/D30/D37 bytes and
domains remain unchanged. No scalar, source import, native point,
numerical endpoint, threshold or finite-degree job is a premise.

## Definitions, exact operator match and accepted inputs

Write H_n=sum_(k=1)^n1/k,H=1+L and
a=(cos alpha+cos beta)/2,p=sin alpha,q=sin beta,P=p+q. For signed b
equal to beta or-beta set

    w=r*pi+b,z=j*pi+alpha,mu=n/m,v=w/m,
    delta_r=(1-r) mod2,u=z/n,
    F_j=(-1)^delta_r G_n(u,v)/2.

The n integers j of parity delta_r with-pi<=u<pi are precisely a
permutation of the actual row samples. The three endpoint cases
(r,b)=(1,beta),(1,-beta),(2,-beta) give exactly original labels
1,2m-1,2m-2 by finite evenness in v. Their row norms and normalization
are unchanged. In every case0<=w<=2pi,0<=a,p,q<=1. The fourth row
is the actual closest row r0,beta. The central labels are m-1,m.
Thus no actual special row has been dropped, added or renamed.

Accepted N1-round4-rows supplies the exact polynomial-compatible chart
and infinite reference. For w>0 put

    ce=cos((alpha+b)/2),cd=cos((alpha-b)/2),a=ce*cd,
    sigma_- =(-1)^((r-j-1)/2),sigma_+ =(-1)^((j+r-1)/2),
    sinc x=sin x/x,sinc0=1,tau y=y cot y,tau0=1,
    B=1/[2m sin(w/(2m))],
    F_j/(nm)=B[ce*sigma_-*sinc((z-mu*w)/2)*tau((u-v)/2)
                  +cd*sigma_+*sinc((z+mu*w)/2)*tau((u+v)/2)],
    f_j=[ce*sigma_-*sinc((z-w)/2)
                      +cd*sigma_+*sinc((z+w)/2)]/w.       (2)

The first identity is N1's SAME exact chart multiplied by n/m to reach
the FINAL nm normalization directly. It is not a new model or a change
to finite data. Away from removable products,

    f_j=4a/(w^2-z^2),
    sum_(all infinite parity j)|f_j|=ell_r(alpha,b),
    ell_r=sin b/w+8a sum_(j=-r+1,-r+3,...,r-1)
                                      1/[w^2-(j*pi+alpha)^2]. (3)

The sinc expression defines every removable product, and N1's uniform
tail/sign argument proves the displayed infinite ABSOLUTE norm exactly
on the full closed triangle. It does not assert that the ACTUAL finite
positive sample set stays equal to the reference positive set. At
w0,r1,b=-pi,alpha0, N1 gives ell=1,reference f0=1,all other f_j=0;
polynomial continuity supplies the actual row value. No unweighted
cotangent value is assigned at a collision.

D05's continuous fixed set A6 is the one used here. D04/D07 identify
this SAME C2 in E2=C2+D0H2+B0G2 and Delta2=E_infty-E2. Thus replacing
only its numerical bound in the D20 telescope needs no reference
change, collision-hole allowance or new endpoint weight.

## 1. The first global kill test: uniform weighted coefficients

On the FULL diamond ce,cd>=0. The stronger bound

    (ce+cd)/w<=1                               (4)

holds for all three cases with w>0. If w>=pi, ce+cd<=2 and2/pi<1.
The only remaining case is r1,b=-beta,0<w<pi. Then alpha<=pi-beta=w
and the two cosines are sin((w+alpha)/2),sin((w-alpha)/2). Their sum
is<=w by sin t<=t on these nonnegative angles. This also shows the
uniform linked limit as w tends to zero. The old N1 bound2 is safe
but unnecessarily large for this R2-only application.

The exact nm prefactor has NO O(1/n) conversion term. For x=w/(2m),
0<x<=pi/m<1/10 at n>=32, and sinx>=x(1-x^2/6) gives

    0<=B-1/w=(1/w)(x/sin x-1)
         <=w/(20m^2).                          (5)

Here x/sin x-1<=x^2/(6-x^2)<=x^2/5. These exact coefficient and
normalization checks are the first decisive separation from the old
n^2-then-nm estimate. They remain valid at a0 and near a vertex, so
no inverse phase-distance or inverse-a constant is introduced.

## 2. Fixed NEAR index set, without a phase or degree scan

For each of the three rows choose the analytic index split |j|<=4.
It is fixed BEFORE any endpoint budget, not tuned to data. All such
parity indices lie inside the actual half-open mesh for n>=32.
For r1 these are exactly-4,-2,0,2,4 (five indices); for r2 they are
-3,-1,1,3 (four). Their arguments obey

    |z|<=5pi, v<=2pi/n,
    |(u+/-v)/2|<=7pi/(2n)<1.

On |y|<=1,0<tau y<=1 and

    |tau y-1|<=2y^2/5.                         (6)

Indeed siny-ycosy=integral_0^y t sin t dt<=y^3/3 and
siny>=5y/6 for0<=y<=1; evenness handles negative y. The global
|sinc'|<=1/2 follows from sinc x=integral_0^1cos(tx)dt.

Subtract the TWO formulas(2) using, in order, the prefactor difference,
the sinc shift, and tau-1. Since |sinc|<=1,0<tau<=1,ce+cd<=2,
the prefactor contribution PER near index is at most

    (B-1/w)(ce+cd)<=w/(10m^2)<=pi/(5m^2)<2/(3n^2). (7)

The sinc arguments shift by w/(2m). Their contribution, with prefactor
1/w and the tau factor retained, is at most

    (ce+cd)/(4m)<=1/(2n).                     (8)

For the remaining tau contribution use(4),(6), obtaining after summing
the near indices

    error_tau<=(1/10)sum_near(|z|/n+v)^2.      (9)

For the even five-index set,
sum z^2=40pi^2+5alpha^2<=45pi^2 and
sum|z|=12pi+alpha<=13pi. Hence the sum in(9) is at most
(45+52+20)pi^2/n^2, and its contribution is<117/n^2 using pi^2<10.
For the odd four-index set,
sum z^2=20pi^2+4alpha^2<=24pi^2 and sum|z|=8pi;
the corresponding contribution is<72/n^2.

Combining(7)--(9), EACH r1 row contributes at most
5/(2n)+121/n^2, and the r2 row at most2/n+75/n^2. The THREE
near-row contributions therefore obey

    E_near_rows<=7/n+317/n^2.                 (10)

Every actual near collision is included by(2)'s sinc/tau polynomial
chart. No fixed signs of individual finite cardinals or finite samples
are assumed or needed for this termwise absolute-norm comparison.

## 3. ALL remaining finite indices, with the correct nm normalization

If |j|>4, then |z|>=pi(|j|-1)>=4pi>=2w and |u|>=2v. Thus there
is no denominator collision on this far index set. For

    K=sinc((|u|+v)/2)*sinc((|u|-v)/2),
    Hh=(1+cos v)/(2K),
    D=w^2-z^2,Dh=mu^2*w^2-z^2,

the accepted N1 sine-chord calculation gives

    K>1/6, |Hh-1|<=u^2.                       (11)

For clarity its arguments lie in[0,3pi/4] and[0,pi/2], respectively;
v<=2pi/33<pi/8 and |u|<=pi ensure the stated chord ranges. Also
1-K<=(u^2+v^2)/12 and v<=|u|/2 give(11) directly after division by K.

The actual numerator identity is the unchanged corrected-polynomial one:

    F_j=[2a(1+cosv)-p sin u+(sin b)sinv]
                                             /[2(cos u-cosv)]. (12)

Its a part normalized by nm is4mu*a*Hh/Dh. Compare it with f_j=4a/D.
The Hh-1 piece costs at most16a/(3n^2) per index because
|Dh|>=3z^2/4; its sum per row is<=16a/(3n).

The remaining normalization AND displacement are handled TOGETHER:

    mu/Dh-1/D
       =(1/m)*(z^2+mu*w^2)/[(z^2-mu^2*w^2)(z^2-w^2)]
       <=20/(9m z^2).                        (13)

This exact positive expression retains the n/m prefactor. It avoids
adding the old separate conversion cost after estimating the row norm.

Here are explicit uniform far sums for the new |j|>4 split:

    sum_far 1/|z|<=2H_n/pi,
    sum_far 1/z^2<=3/(8pi^2)<1/(2pi^2),
    w*sum_far 1/z^2<1/pi.                     (14)

For the middle bound the worst parity lower denominators are
4pi,6pi,8pi,... on each side. Their sum is at most
(1/(2pi^2))sum_(k=2)^infinity1/k^2
<=(1/(2pi^2))(1/4+integral_2^infinity x^-2 dx)=3/(8pi^2).
Even far indices start with larger denominators5pi,7pi,..., so obey
the same bound. The first estimate follows from |z|>=pi(|j|-1) and
the actual finite half-open mesh, whose extreme |j|-1 is at most n;
bounding each side by H_n is conservative. The third uses w<=2pi.

Multiplying(13) by4a and summing(14), the combined displacement cost is
<=40a/(9pi^2*m)<=2a/(3n) per row. These intermediate comparisons
are equalities zero if a0 and strict when a>0. With the Hh cost, ALL THREE a-part
comparisons therefore cost

    E_far_a<=18a/n.                           (15)

For the sine terms, cosv-cosu=(u^2-v^2)K/2>=u^2/16. Their exact nm
normalization and |sin u|<=|u|,|sinv|<=v give per index

    |F_sine|/(nm)<=8p/(n|z|)+8q*w/(n z^2).

Thus(14) bounds the THREE far sine contributions by

    E_far_sine<=(48pH_n+24q)/(pi*n).            (16)

Taking absolute differences before the row absolute norm is safe since
||x|-|y||<=|x-y|. This proof neither imposes the reference positive
set on F_j nor removes sample zeros; any moving finite sign changes
are retained by the actual absolute values.

## 4. Infinite-reference tails and the closest ACTUAL row

Outside the actual half-open n-point mesh, |z|>=pi n, and w<=2pi
implies w^2/z^2<=1/256 at n>=32. The accepted N1 tail spacing2pi
bound is

    sum_outside 1/z^2<=2/(pi^2 n^2)+1/(pi^2 n)<=2/(pi^2 n).

By(3), |f_j|<=1024a/(255z^2)<=81a/(20z^2). Thus each omitted absolute
reference tail costs<=81a/(10pi^2 n)<=a/n; at a0 all these terms
vanish exactly. The THREE tails cost

    E_tail<=3a/n.                             (17)

The reference's infinite sum is ell_r EXACTLY, not a newly truncated
limit. All omitted terms have been bounded in(17), including both ends
of the moving half-open mesh.

For the fourth endpoint row r0,beta use the stronger bound actually
proved in N1-round4-rows section4, valid throughout the closed triangle:

    |R_0/(nm)-sinc beta|
        <=(2+H_n/pi)/m+pi^2/(24m^2)
        <=(2+H_n/pi)/n+5/(12n^2).              (18)

This accepted whole-row inequality includes its possible positive sine
samples and exact linked beta0 polynomial limit. It is not the claim
that every closest-row finite sample has a fixed sign globally.

Adding(10),(15)--(18), the complete FOUR endpoint rows obey

    |Jend-C2|
      <=[9+21a+H_n/pi+(48pH_n+24q)/pi]/n
                                      +(317+5/12)/n^2.    (19)

Here Jend is the SAME normalized sum of rows0,1,2m-1,2m-2. All
reference identities, weights and the exceptional corrected mode match
D20/D07. No ordinary collision row is added to or deleted from A6.

## 5. BOTH central rows and full closed-domain completion

The remaining ACTUAL angles are
v_(m-1)=pi-(pi-beta)/m and v_m=pi+beta/m. The full-domain weighted
row proof already established in D20-global-retained-rows gives

    0<=Jcen=[R_(m-1)+R_m]/(nm)<=(12+2L)/n.      (20)

Its proof uses |Phi0|<=4 with WEIGHTED polynomial-continuous values at
integer offsets, sin(v/2)>99/100 and |cot(v/2)|<=pi/m, and retains
the complete actual row upper. It is the accepted full diamond bound,
not the stronger a-weighted D30/D37 small-radius estimate. No central
integral is substituted for these two finite row norms.

Since Jcen>=0,
|J6-C2|<=|Jend-C2|+Jcen. Use a,p,q<=1,H_n<=1+L and pi>3 in
(19)--(20). The 1/n coefficient is bounded by

    42+2L+(49H+24)/pi
       <42+2L+(73+49L)/3
        =(199+55L)/3 <67+19L,

while317+5/12<318. This proves(1).

At a removable near collision the exact chart(2) is already valid. At
the sole w0 vertex use N1's explicit linked sinc reference and actual
finite-polynomial continuity; all preceding bounds are phase-uniform,
so the complete inequality passes to that vertex. The central bound
uses its accepted whole weighted continuation. Thus no node, seam,
phase edge, a0 or collision is missing. Separate-absolute-phase
extension gives the complete signed diamond with no n,m exchange. QED.

## 6. Consequential global allowance, norm and outer-far applications

Let D,Gg,Mesh,W and E0 be the COMPLETE accepted D20/D16 functions,
unchanged. Let

    K35={ [6+16/(3pi)](1+L)+2/pi }/n,
    C_E02=D+Gg+E6new+Mesh+W.                    (21)

D20's EXACT whole-profile telescope is

    |S-M_infty|<=E35+E_global+|J6-C2|+Bmesh+(d/pi)Blog.

Accepted D35 gives E35<=D+K35P on the FULL closed signed diamond;
D20's full global outer and mesh/log bounds are respectively Gg,Mesh,W.
Apply(1) ONLY in its matched retained-row position. Then for every
integer n>=32, throughout the FULL signed diamond,

    |S_n-M_infty|<=C_E02+K35P.                 (22)

Every ordinary/outer/retained/mesh/log allowance is still charged. No old
fixed-strip I_n or collision-hole error is silently discarded; (22)
is the SAME already accepted D20 global telescope with ONE improved
proved component. It is not a stronger phase-relative operator theorem.

For realn>=32,E6new is positive and strictly decreasing:

    E6new'=[19-67-19logn]/n^2-636/n^3<0.

All other terms of C_E02 decrease on that SAME accepted domain, so
C_E02 is positive and decreasing there. The EXACT saving is

    Cnew-C_E02=E6old-E6new
                  =(126+2L)/n+21282/n^2>0.     (23)

No endpoint value is used to establish this uniform strict improvement.

The D27/E01 full finite period/sign adapter and completed-model global
coefficient bound now give the GLOBAL norm

    M_E02=[4L^2+(79/5)L]/pi^2+8/3+C_E02+2K35   (24)

for S on ALL real phases, actual lambda on the full physical square,
and the complete signed board/cardinal families after the actual-corner
cosine substitution for ALL real angles. This is a proved global norm,
not the sampled maximum or unknown argmax value. Its improvement over
the old M35 is exactly(23). The unchanged geometric reindexing never
interchanges n,m and preserves all polynomial collision values.

For the inherited D37 outer regionrho>=1, retain its u1=47/384,
s1=sqrt(47/48),T=(4L^2-3L)/pi^2 and SAME actual origin E0. The routine
new sufficient far gate is

    GO_E02=u1*T-Dc-C_E02-K35*s1-E0.             (25)

This uses the full true completed constant lower at the origin through
PD-T271's accepted computer-assisted enclosure/D02 uniform limit, exactly
as D37; that trusted premise is NOT needed for the finite six-row
theorem(1). The accepted P<=min(2,sqrt(8u)) and decreasing error/u
argument proves that GO_E02>0 would exclude the whole closedrho>=1
region. All positive non-P costs and the full E0 stay charged.

GO_E02 strictly increases on REAL n>=32 (T increases,C_E02,K35,E0
decrease), and its improvement over the old D35/D37 outer gate equals
(23). No sign at768,512 or any other new endpoint has been evaluated,
and no global onset or complete cover follows from this component alone.
The E02 assembly lead owns the prospective fixed768 analysis. Near,
inner-far, physical floors and actual corners require their OWN proved
domains. E01's corner512 result cannot transfer the remaining gates.

## History, novelty and execution boundary

2026-11-06, requested Codex gpt-6.1-sol xhigh, serving metadata unexposed.
Input017f8ecc45534b4a6dd38b0488020463cb914edb; rules last read63c70b7,
byte-identical rule diff checked. The E01 COMPLETE fresh registry/current/
obstruction baseline is reused with matching actual hashes; fresh E02
mechanism searches and full relevant predecessor coverage preceded the
new direct-nm candidate. Details/candidates/kill tests are in the owned
idea/attempt. This is a quantitative continuation of N1-07/D20, not a
new sinc chart, interpolation principle or historical priority claim.

The old global error E6old and its records remain intact. D30/D37 small
radius row formulas were not extended. A larger-radius relative operator
route is preserved as DEFERRED, not an unproved premise. No source,
receipt, data, E01 prefix, shared ledger, global ID, pack or Git state
was changed. ONLY the three assigned E02 prose files were written.

No scalar/endpoint/threshold/native/phase/board/root/quadrature/finite-
degree/compile/control job, mathematical script or source import ran.
No point values or performance data are asserted. Distinct mathematical
review of the exact normalization, constants, far sums, tail coverage,
w0 limit and matched six-row telescope is required before root adoption.
All later numerical/source jobs remain UNRELEASED.


## Root adoption after distinct focused audit —2026-11-06

Current full-diamond retained-six-row theorem is PROVED and adopted:
EVERY n>=32 has |J6-C2|<=(67+19logn)/n+318/n², with all four endpoint
and both central rows and collision limits retained. Distinct Astra high
[review](../independent-checks-E02-global-retained-rows.md), SHA256
1486842e34625c8a9a52fa0919dad2836615ee04ac9ed544befe7f6d2ae71ff7,
accepts the unchanged17,031-byte reviewed prefix2cd66cc0... and stated
global error/norm/conditional outer-far corollaries. The exact positive
saving is(126+2logn)/n+21282/n². No endpoint, global-onset or finite-degree
claim follows here; global onset remains1024 and all sources remain
unchanged. No numerical job. PD-T271 is retained where used by downstream
origin-loss comparisons; final Claude review remains separate.
