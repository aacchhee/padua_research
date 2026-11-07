# E02 assembly — A matched fixed768 univariate sufficient system

Provisional claim: PD-T?argmax-bridge-codex-E02-assembly.
Aliases: fixed tangent radial certificate; half-near/bridge/annulus/far
assembly; exact phase-floor matching. Split from: the E02 paper round.

## Statement, proof status and execution boundary

Status: **PROVED developer analytic global theorem**, under the explicitly
inherited accepted premises below; distinct assembly review/adoption is
required. The ONE prospectively chosen baseN768 closes by the complete
RATIONAL PAPER comparisons in the final verification section. No scalar,
endpoint or polynomial-checker job was needed or executed.

For EVERY integer n>=768, with the original corrected Padua cardinals,

    max_[-1,1]^2 lambda_n=Lambda_c(n)=lambda_n(-1,-1),
    argmax lambda_n={(-1,-1),(1,-1)} for even n,
                   {(-1,-1),(-1,1)} for odd n.          (1)

HPAIR is the complete E02 regular-outer bound, frozen developer proof
`E02-paired-outer.md`, SHA256
`dfe4c1c84d9fc8887d11c2e84117f4e924061965282f59a8121cec02bc3b959f`:

    near rho<=1/2: |delta_a Eout|
             <=rho[(27/2)L+55]/n+|beta|[17L+27]/n^2,
    wide rho<=1:  |delta_a Eout|
             <=rho[14L+59]/n+|beta|[17L+27]/n^2.       (2)

HROW is the complete full-diamond retained-six-row bound, frozen
developer proof`E02-global-retained-rows.md`, SHA256
`2cd66cc0b8214ef79206ca3381f9028e2c8e3d3f9add8fde0157670451136fb8`:

    E6new=(67+19L)/n+318/n^2, for EVERYn>=32.           (3)

Both are now accepted exact operator statements. HPAIR's final review is
`3556b5ff4ce1d7d253256bd0d104f6f13e558191397cb8dad7531df1b6e48773`;
HROW's is
`1486842e34625c8a9a52fa0919dad2836615ee04ac9ed544befe7f6d2ae71ff7`.
Their first frozen proof prefixes remain preserved in the linked records.
The paired proof's MINOR closing-notation clarification changes no
operator/constant/domain: the exact origin identity is minus uE(0),
upper bounded by plus uE0. The old allowances are reference predecessors,
not alternate postfailure executions. This paper runs nothing and supplies
no source. The conditional reduction and initially proposed checker are
retained below as history; the actual proof uses the complete uniform
wide-FAR radial argument instead of requiring the old separate far gates.

Accepted supports: E01 actual corners from512, review
`e9a2d5cac242f36303f68b8be7898ae80fdde71d0b97b40d740754c176fc8a83`;
E01 floor/frontier, review
`a0853a1e9675bcb841348edb2aaa8ae5a3c8776e2bced63a5c6326da27665db3`,
accepting theory`cc8e328405706f6cc5a5ea3fe8122818fb59482c8ac4841e0b6036252b775f11`;
and unchanged D22/D35/D37, D16/D20, PD-T101/364 and upstream constant
premises. The new small bridge-domain lemma is proved below and itself
needs independent review. No uncomputed D31/D33 endpoint is a premise.

## Exact common scalar functions: no missing origin or global charge

For real n>=32 set m=n+1,L=logn,H=1+L,b=4/pi^2,
hr=log(5/2)+1/18. Use EXACTLY the accepted D16/D20 quantities:

    D=[(52/pi^2)H+7]/n+10/n^2+20H/(pi*n^2),
    MA=1/pi+4/pi^2, g=1+log(2+8m/(3pi)),
    VB=23+[3g+14logm+46+2log2]/pi,
    Qg=(4/m)[7+(2/pi)(5+2log(2m))],
    Gg=(2L*MA+VB)/(2m)+6L*MA/m+Qg+4logpi/(pi*m)+16/m,
    Mesh=b(2L+2hr)/n+[4+b(L+1/n)]/(4n^2-1)
             +b/(2n-1)^2+[5+b(log(n+1/2)+2)]/[4(n-1/2)^2],
    W=[3logm+log2+2logpi+2]/(pi*m),
    CE=D+Gg+E6new+Mesh+W,
    G0=[(28/pi^2)L+111/2+23/pi]/m,
    E0=D+G0+Mesh+14/n+71/n^2,
    KD=[(6+16/(3pi))*H+2/pi]/n,
    T=(4L^2-3L)/pi^2, V=T-E0.                        (4)

CE uses HROW ONLY in the one global E6 term. All ordinary, outer,
singular-mesh and logarithmic charges remain. KD is accepted D35's
global ordinary coefficient; E0 remains the SAME actual finite-origin
allowance. Global validity of(3) is needed here; a near-row bound would
not suffice. Relative estimates below do not replace E0 by zero or a
model-origin equality.

## Collect the complete paired relative allowances

Put

    AN=22/n+142/n^2+40H/(pi*n^2), CN=AN+20/n^2,
    AW=23/n+184/n^2+40H/(pi*n^2), CW=AW+20/n^2,
    dbeta=(17L+27)/n^2,
    kNx=[8H+(31/2)L+226/3]/n+4/n^2, kNy=kNx+dbeta,
    kWx=[8H+16L+250/3]/n+4/n^2, kWy=kWx+dbeta,
    VN=V+AN, VW=V+AW.                               (5)

Under HPAIR the ACTUAL finite increment satisfies

    near: S(phi)-S(0)<=model_difference+CN+kNx*x+kNy*y
                                                    +u(E0-AN),
    wide: S(phi)-S(0)<=model_difference+CW+kWx*x+kWy*y
                                                    +u(E0-AW), (6)

where x=|alpha|,y=|beta|,rho=x+y,a=(cosx+cosy)/2,u=1-a.
The near domain is the CLOSED rho<=1/2 diamond; the wide domain is
the CLOSED rho<=1 diamond. Signed phases use the inherited separate
absolute-phase comparison; n,m are never exchanged.

To check EVERY coefficient, D35's unrelaxed fixed-row and retained-row
charges are

    delta_a Erow<=4a/n+20/n^2+40aH/(pi*n^2)+rho(8H+10)/n,
    delta_a Eret<=[18a+P(8+L)]/n+(142a+4P)/n^2,

while D37 wide replaces the second line by

    delta_a Eret<=[19a+P(12+L)]/n+(184a+4P)/n^2.

The SAME mesh/log charge is rho(L+7/3)/n. Insert the corresponding
line of(2), use P<=rho only in its nonnegative terms, and collect:
near log coefficient1+1+27/2=31/2, constant10+8+7/3+55=226/3;
wide log1+1+14=16, constant10+12+7/3+59=250/3. The asymmetric
dbeta is retained rather than replaced by a fitted common K.
The constants are exactly aAN+20/n^2 or aAW+20/n^2.
Finally E(phi)-E(0)=delta_a E-uE(0), with |E(0)|<=E0,
proves(6). This restores the justified a factors and pays the full
actual-origin conversion before combining with model loss-uT.
The full row expression, not individual cotangent references, supplies
the accepted collision-continuity extension.

## Paper scalar domains and real-n monotonicity from768

AtN768, L>13/2 follows fromlog3>1,log2>69/100; L<7,H<8.
The E01 rechecked E0 bound at512 is<1/2 and decreases thereafter.
With pi^2<10,

    T>299/20, V>289/20.                              (7)

These are paper inequalities, not an endpoint preview. All AN,AW,CN,CW
are positive/decreasing. Each k in(5) is positive/decreasing:
kNx=[(47/2)L+250/3]/n+4/n^2, kWx=[24L+274/3]/n+4/n^2,
and dbeta'=[-34L-37]/n^3<0.

The restored mixed coefficients VN,VW also increase; here is a NEW
explicit check rather than an assumption. For n>=768,H<=n/4,

    AN'=-22/n^2-[284+(40/pi)(2H-1)]/n^3,
    AW'=-23/n^2-[368+(40/pi)(2H-1)]/n^3,
    |AN'|<30/n^2, |AW'|<31/n^2,
    T'=(8L-3)/(pi^2*n)>49/(10n)>31/n^2.

Use pi>3,284/n<1,368/n<1 for the two derivative bounds.
Since E0 decreases, (V+AN)' and(V+AW)' are strictly positive.
This proof is not inherited from E01's deliberately unasserted mixed
monotonicity. It covers all realn>=768.

The paired kWx,kWy are no larger than old D37 KW:

    KW_old-kWx=(4L+14)/n,
    KW_old-kWy=[(4n-17)L+14n-27]/n^2>0.

The old paper boundKW_old<2/5 at768 persists thereafter. All far
positive-q/tail domains below therefore follow from(7) before any job.

## Floor functions and the NEW21/40 bridge-domain lemma

Set p=22/7,R=pi/4,rB=21/40 and a_r=1-r^2/4. Reuse the EXACT
accepted E01 functions, with their own n/radius hypotheses:

    eta=a_r*[1-(4p+r)/n]-r/2,
    Fn=[2eta/(p+r)]*[n/(n+1)]*(1/4-1/n),
    Fs=(35/286)*(1-6/n)^2*(a_r-r/2),
    A0=97a_r/100-r/2,
    Ih=2303a_r/5000-471r/1250,
    Rh=4837a_r/1875-5r/3,
    Iw=5369a_r/15000-7379r/30000,
    Rw=37621a_r/15000-3r/2,
    Fh=(539/1936)Ih-140A0/(157n)-400Rh/(157n)-800A0/(3n^2),
    Fw=(539/1936)Iw-140A0/(157n)-400Rw/(157n)-800A0/(3n^2).
                                                               (8)

Fn/Fs/Fw apply for n>=64,ACTUALrho<=r<=R. Originally Fh was
proved only through1/2. It extends to rB by this COMPLETE additional
domain check. On its original physical band[pi/100,pi/4],

    A(b)=a_r-r/2-a_r sinb
             > (29/100)(1-r^2/4)-r/2
             >=4811/640000>0 at0<=r<=21/40.          (9)

Here sin(pi/4)<71/100 follows by squaring; the displayed polynomial
decreases in r, and at rB it is exactly4811/640000. The whole domain
is below R. E01's rebuilt nearest straddling/parity/count proof and
small-angle concavity proof already hold through R. In the middle
case, A and A/sinb remain positive/decreasing in b under(9), so the
SAME two-open-arc layer-cake and finite physical mesh inequalities
hold. The exact T=4log2,A0/integral/log bounds used in Fh depend on
the fixed band, not on r<=1/2; their sign substitutions stay correct
because the exact positive integrals remain positive. The horizontal
fixed-v numerator is the SAME actual baseline; no mesh swap occurs.
This proves min(Fn,Fs,Fh) as a projected floor for ALLn>=64 and
ACTUALrho<=r<=rB. Both signed phases, both parities, original endpoint
weights and all finite-polynomial collisions retain E01's treatment.
No uniform3/50 claim is extended beyond its half-radius guard.

For n>=768 define the chosen same-degree physical NONCORNER floors

    DH(r)=max(3/50,min(Fn,Fs,Fh)),     0<=r<=1/2,
    DB(r)=min(Fn,Fs,Fh),              1/2<=r<=rB,
    DU(r)=min(Fn,Fs,Fw),              rB<=r<=R.       (10)

The new bridge lemma justifies DB; accepted E01 justifies DH and DU.
Use r=rho ACTUALLY, not a rational outer proxy. All pieces increase
with realn at fixed r: eta and its positive nearest factors increase;
Fs increases; Fh/Fw have positive loss coefficients with decreasing
1/n,1/n^2. Their min/max preserve ordering. No monotonicity in r of
Fh/Fw is assumed. Actual corners NEVER get a projected floor.

## Fixed tangent and exact clipped radial maximum

The PRIMARY paper choice is c=1/2 in BOTH coordinates and all regions.
For every t>=0, (sqrt t-1/2)^2>=0 gives

    sqrt t<=t+1/4,
    B*t^(3/2)<=B*t^2+(B/4)*t, B>=0.                (11)

This is a standard tangent inequality, selected before any endpoint.
It is a sufficient relaxation, not an asserted optimum. The registered
c=1/3 alternative is deferred and is not an automatic fallback job.

For d1,d2>0,linear coefficients l1,l2>=0,fixedrho r and CLOSED
0<=u<=v<=r define

    z0=[2d2*r+l1-l2]/[2(d1+d2)],
    z*=min(v,max(u,z0)),
    Rad(d1,d2,l1,l2;r;u,v)
       =-d1*z*^2-d2*(r-z*)^2+l1*z*+l2*(r-z*).      (12)

This is EXACTLY the maximum of the concave quadratic on that interval:
complete the square or differentiate once. It retains the correlation
x+y=r. Endpoints/ties/r=0 use the same closed formula. Its interior
branch is

    -[d1d2/(d1+d2)]r^2+[(d2l1+d1l2)/(d1+d2)]r
                                     +(l1-l2)^2/[4(d1+d2)].

The endpoint branches are the same quadratic evaluated at u or v.
Thus if u,v are affine in r, Rad is piecewise QUADRATIC with affine
branch conditions, not a phase sample or a numerical root maximum.
It decreases if d1,d2 increase or l1,l2 decrease, by pointwise ordering
on the SAME interval; no derivative of a moving clipped vertex is needed.

### Half-near radial bound

Let c0=47/192,bx=77/96,by=1/12, and set

    qNx=c0*VN-89/72, qNy=c0*VN-23/24,
    dNx=qNx-bx, dNy=qNy-by,
    lNx=kNx+bx/4, lNy=kNy+by/4,
    NH(r)=CN+Rad(dNx,dNy,lNx,lNy;r;0,r).             (13)

Accepted D22 and(6), combined FIRST with-uT, give the complete
near bound with coefficients qNx/qNy. Apply(11), then(12):

    S_n(phi)-Lambda_c<=NH(rho) onrho<=1/2.          (14)

All origin charges remain in VN; favorable a-constant restoration is
justified by(6). The fractional/log constant was not declared purely
quadratic at zero; (11) includes its compensating linear term.

### Three closed coordinate classes for the annulus

On1/2<=r<=R, E01/D37's radius-one constant gives coefficients1 and
1/10 for the two fractional terms, and53/40,119/120 for quadratics.
Where x,y<=1/2 use c=c0. In either LARGE-coordinate class use
c=cR=91/384, justified by

    u>=(x^2+y^2)/4-(x^4+y^4)/48
      >=[1/4-r^2/48](x^2+y^2)>=cR*(x^2+y^2),

because r<=pi/4,pi^2<10. For either c put

    dx(c)=c*VW-53/40-1, dy(c)=c*VW-119/120-1/10,
    lx=kWx+1/4, ly=kWy+1/40,
    NB(r)=CW+Rad(dx(c0),dy(c0),lx,ly;r;r-1/2,1/2),
    NX(r)=CW+Rad(dx(cR),dy(cR),lx,ly;r;1/2,r),
    NY(r)=CW+Rad(dx(cR),dy(cR),lx,ly;r;0,r-1/2).     (15)

The coordinate intervals correspond respectively to BOTH coordinates
<=1/2, x>=1/2, and y>=1/2. They cover[0,r] with shared endpoints,
since r<1; at r=1/2 the large classes are retained tangencies. The
stronger47/192 cosine coefficient is NEVER used outside its legal
coordinate class. Each Nj is an upper for S-Lambda_c in its own class
by(6), the radius-one true-constant bound, (11) and exact(12). No
unproved large-coordinate derivative/tail bound is substituted here.

All quadratic domains are proved already at768 using(7):

    dNx>17269/11520>7/5, dNy>2,
    dx(c0)>931/768>6/5, dy(c0)>2,
    dx(cR)>8443/7680>1, dy(cR)>2.                   (16)

The q's/d's increase thereafter by the mixed monotonicity proof above.

## The fixed768 sufficient reduction and original far alternative

Require EVERY one of the following strict conditions atN768:

    H: DH(r)-NH(r)>0                       ALLr in[0,1/2];
    Bj: DB(r)-Nj(r)>0, j=B,X,Y             ALLr in[1/2,rB];
    Uj: DU(r)-Nj(r)>0, j=B,X,Y             ALLr in[rB,R]. (17)

These are seven univariate sign families, not single evaluated points.
Min/max and clipped-vertex branches must be certified explicitly.
Uniform3/50 alone is not presumed to dominate NH. The radius-dependent
floors remain inside the SAME r comparison throughout.

One sufficient FAR alternative is the FOUR old scalar gates below, with
fixedeta=1/2. Their signs are NOT claimed or needed in the final rational
application; the new complete wide-FAR proof below replaces this entire
alternative, including all its coordinate branches:

    qBx=c0*VW-53/40, qBy=c0*VW-119/120,
    qLx=(11/48)*VW-53/40, qLy=(11/48)*VW-119/120,
    GB=pi/8-CW-Psi(1,qBx,kWx+1/2)-Psi(1/10,qBy,kWy+1/2),
    Ex=1/(2sqrt2)-qLx/4+kWx/2,
    Ey=1/(20sqrt2)-qLy/4+kWy/2,
    GX=-CW-Ex-Psi(1/10,qLy,kWy),
    GY=-CW-Ey-Psi(1,qLx,kWx),
    GO=(47/384)T-6211/7260-CE-KD*sqrt(47/48)-E0,
    GB>0, GX>0, GY>0, GO>0.                         (18)

Here Psi is EXACTLY D22/D37's nonnegative radical maximum:

    z=[3B+sqrt(9B^2+32qk)]/(8q),
    Psi(B,q,k)=(B/4)z^3+(k/2)z^2,
                         B,k>=0,q>0.

The tail domains are qLx>3/(2sqrt2)+kWx and
qLy>3/(20sqrt2)+kWy. They follow on paper from
qLx>1907/960>19/10 and kWx,kWy<2/5, since
3/(2sqrt2)<15/14 and15/14+2/5<19/10. The other q's are larger.
All coefficients and denominators in(12)--(18) are therefore in domain
at768 and throughout realn>=768, before any scalar execution.

On the inner-FAR boxx,y<=1/2 withrho>=R, adding
eta*(rho-R)>=0 gives exactly penaltyetaR=pi/8. This is the ONLY
change from D37's fixed multiplier construction. The two large-coordinate
FAR bounds use its proved derivative tails, with their separate k's and
VW; actual-coordinate half thresholds and every constant are retained.
No parameter is fitted. These gates exclude S>=Lambda_c on the CLOSED
inner-FAR domainR<=rho<=1 without a defect floor.

On the full outer domainrho>=1, the SAME global telescope gives

    Lambda_c-S>uT-Dc-CE-KD*min(2,sqrt(8u))-E0,
    u>=47/384, Dc=6211/7260=8/3-4383/2420.

Dividing by u shows the right side is at least(u/(47/384))*GO.
Every global charge in(4) and actual E0 is paid; only HROW replaces
the complete old E6 term. The limiting-origin numerical premise behind
Dc and all accepted global constant dependencies remain explicit.
This is an analytic/model branch, not a model-free finite certificate.

## All-real-n transfer and complete physical assembly

At every fixed legal r and coordinate interval, NH,NB,NX,NY decrease
with n: C decreases, every d increases, every l decreases, and the
optimization domain is the SAME closed interval. The floors in(10)
increase, so ALL gaps in(17) increase pointwise. Compactness and
continuity of the clipped maxima and min/max floors turn strict(17)
into a positive margin atN; every larger integer inherits it. No
monotonicity in r or of the location of a maximizer is assumed.

For the original optional far alternative, GB/GX/GY increase by accepted
Psi pointwise order and the proved VN/VW/k/C monotonicities. CE is
positive/decreasing: HROW's new term
has derivative[19-67-19L]/n^2-636/n^3<0, while all other D20
components are unchanged. Thus GO increases as well. The scalar and
quadratic domains persist. This proves real-n transfer of the ENTIRE
fixed system, not just selected endpoint terms.

Every physical point belongs to a legitimate CLOSED PD364 odd-center
chart with signedrho<=pi. The two odd-vertex normalized L1 distances
in a mesh cell sum to2; choose one<=1, including boundaries/ties.
Use separate primitive evenness without exchanging n,m. If actual
rho<=R at a NONCORNER center, identify its correct actual radius and
coordinate class, then apply(17) and lambda=S-Delta with(10). Actual
corners use accepted E01's BOTH closed inwardpi/4 squares for n>=512,
loss(A^2+B^2)/16. Their inwardA+B<=R diamond lies in those squares;
strict descent holds unless A=B=0. No projection is applied there.
If actualrho>=R, apply the complete inner/outer FAR comparison, using
Delta>=0: either the original optional gates(18) or the new wide-FAR
lemma and GO proved below.
The new uniform wide-FAR proof below covers the SAME entire inner-FAR
strip if used in place of those old separate gates. The seams
rho=1/2,rB,R,1 and all coordinate ties are retained on both
sides. Nodes, edges, axes, original endpoint multiplicities, initially
zero cardinals and every finite-polynomial collision remain covered.

Only the two parity-correct odd endpoint-pair origins remain: (n,m)
and(0,m) for even n, or(n,m) and(n,0) for odd n. Their physical
images are exactly(1), haveDelta=0 and valueTRUE Lambda_c. The
node-preserving x/even or y/odd reflection gives their equal values.
All other physical points are strictly below. Thus the stated
component hypotheses and a complete matched fixed system imply(1).

## Complete RATIONAL PAPER verification at the single base768

The following completes the application without any endpoint/source job.
Every comparison is an explicit rational inequality or a written
logarithmic-series bound. Decimal shorthand in the motivating draft is
replaced here by fractions. No phase values, computer-evaluated budgets
or performance observations are used.

### A. Logarithmic and full baseline bounds

The positive atanh series gives

    log2>2*(1/3+1/(3*3^3)+1/(5*3^5))=842/1215>693/1000,
    log3>1+1/12+1/80+1/448=7379/6720>137/125.

The integer comparisons are842000>841995 and922375>920640.
Since768=3*256, L>8*(693/1000)+137/125=166/25. Conversely
log2<7/10 is the accepted positive-series upper bound. The first six
positive terms of exp(11/10) sum to36015101/12000000>3, proving
log3<11/10 and henceL<67/10. Thus

    166/25<L<67/10, H<8.                             (19)

From pi^2<(22/7)^2=484/49,

    T>4790926/302500>791/50,

the last comparison being239546300>239277500. The SAME coarse D37
component estimates, now checked at768, give

    D<479/(9*768)+190/(3*768^2)<7/100,
    G0<1529/[18*769]<9/80,
    Mesh<17/(2*768)+14/768^2<3/250,
    14/768+71/768^2<15/768<1/50.

For the first two strict comparisons use36844200<37158912 and
122320<124578. For the mesh comparison multiply the displayed
rational fractions; all denominators are positive. The origin tail
uses71<768 and250<256. Their sum is429/2000<11/50. Therefore

    E0<11/50, V=T-E0>78/5.                          (20)

All six near/wide q/d domains are stronger than(16) at this base.
The paired coefficients obey the following rational bounds, including
the full asymmetric dbeta:

    CN<11/384+403/884736<73/2500,
    CW<23/768+233/442368<1/32,
    kNx<=kNy<1869097/5898240<8/25,
    kWx<=kWy<1956265/5898240<1/3.                    (21)

The k numerators follow by usingH<8,L<67/10 in(5), then adding
4/768^2 and(17L+27)/768^2 before comparison. The final comparisons
are46727425<47185920 and5868795<5898240. CN's last step follows
from96720000<117669888; CW's follows from178944<442368.
No beta term is removed or assigned an old common K without this bound.

### B. Explicit coefficient bounds for the two floor polynomials

At768 write Fh=Ah*(1-r^2/4)-Bh*r and
Fw=Aw*(1-r^2/4)-Bw*r. Their EXACT rational coefficients are

    Ah=1241317/9680000-679/602880-4837/565200-97/221184,
    Bh=253869/2420000-35/60288-125/22608-25/110592,
    Aw=2893891/29040000-679/602880-37621/4521600-97/221184,
    Bw=3977281/58080000-35/60288-25/5024-25/110592.
                                                               (22)

Direct positive-denominator cross multiplication gives

    59/500<Ah<3/25, Bh<99/1000,
    89/1000<Aw<23/250, Bw<63/1000.                   (23)

For an inspectable small rational certificate, use the following
one-sided comparisons, all with denominator100000 on the right:

| Coefficient piece | Lower numerator | Upper numerator |
| --- | ---: | ---: |
|1241317/9680000|12823|12824|
|679/602880|—|113|
|4837/565200|850|857|
|97/221184|—|44|
|253869/2420000|—|10491|
|35/60288|58|—|
|125/22608|552|—|
|2893891/29040000|9965|10000|
|37621/4521600|800|833|
|3977281/58080000|—|6848|
|25/5024|497|—|
|25/110592|22|—|

For example Ah>(12823-113-857-44)/100000>59/500 and
Ah<(12824-850)/100000<3/25. Bh<(10491-58-552)/100000<99/1000.
Similarly Aw>(9965-113-833-44)/100000>89/1000,
Aw<(10000-800)/100000<23/250, and
Bw<(6848-58-497-22)/100000<63/1000. These statements are
ordinary rational inequalities, not a script output or a fitted table.
It follows for EVERYr>=0 that

    Fh(r)>Lh(r)=59/500-99r/1000-3r^2/100,
    Fw(r)>Lw(r)=89/1000-63r/1000-23r^2/1000.          (24)

The functions are consumed only on their actual legal radius domains.

For0<=r<=rB, eta>(49/50)a_r-r/2, p+r<15/4 and
2[n/(n+1)](1/4-1/n)=382/769. Hence

    Fn>(13/100)*[(49/50)a_r-r/2]>(3/25)(a_r-r/2).

The first step uses152800>149955; the second subtracts to
37a_r/5000-r/200>183/50000 usinga_r>9/10,r<3/5.
Fs>(3/25)(a_r-r/2), since its coefficient is
564515/4685824>3/25 (14112875>14057472).
Both lower bounds exceed Lh by at least1/500+39r/1000.
Thus DH,DB are greater than Lh throughout their respective domains.
In particular the attained uniform half-radius support is>61/1000,
but the matching comparison below uses the STRONGER function Lh(r).

For0<=r<=R, eta>(49/50)a_r-r/2,p+r<4 and191/1538>3/25,
so Fn>(3/25)*[(49/50)a_r-r/2]>(9/100)(a_r-r/2).
The last difference is69a_r/2500-3r/200>126/12500 using
a_r>4/5,r<4/5. Fs has the same stronger lower coefficient as above.
Their common bound exceeds Lw by1/1000+18r/1000+r^2/2000.
Consequently DU>Lw on the whole ACTUAL upper annulus. All center
classes, not merely the middle class, participate in these minima.

### C. The half-near comparison actually closes with the phase-aware floor

To bound(13), weaken its curvatures to149/100 and249/100 and
its linear coefficients to4997/9600 and409/1200, respectively.
These are legitimate upper relaxations by(7),(16),(21). Maximizing
on the ENTIRE line x+y=r, which further enlarges[0,r], gives

    NH(r)<313/10000+(91/200)r-(93/100)r^2.           (25)

Here the three exact quadratic coefficients satisfy

    [(149/100)(249/100)]/[(149+249)/100]
                                      =37101/39800>93/100,
    [249*(4997/9600)+149*(409/1200)]/398
                                      =1731781/3820800<91/200,
    [(23/128)^2]/[4*(398/100)]
                                      =13225/6520832<21/10000.

Add CN<73/2500 for the constant313/10000. The negative quadratic
and upper linear coefficients have their displayed directions forr>=0.
Combine(24),(25) and the all-center floor comparison:

    DH(r)-NH(r)>
       (9/10)r^2-(277/500)r+867/10000
       >=1301/900000>0.                             (26)

The last minimum is obtained by completing the square over ALL realr;
equivalently4ac-b^2=1301/250000>0. Therefore the ENTIRE closed
half-near family H is PROVED at768. A uniform3/50 floor was never
substituted for this matched radius comparison.

### D. The annulus: one boxed radial bound and complete large-coordinate cases

For the boxed class use curvatures149/100 and27/10 as lower
relaxations: (20) gives dx(c0)>239/160>149/100 and
dy(c0)>1309/480>27/10. The linear coefficients are at most
7/12 and43/120. Enlarge to the whole line as above. Then

    NB(r)<11/320+(51/100)r-(19/20)r^2.              (27)

The exact effective curvature is4023/4190>19/20, effective linear
coefficient25307/50280<51/100, and constant from the linear difference
is81/26816<1/320. Together withCW<1/32 these give(27).

On the bridge[1/2,rB], subtract(27) from Lh:

    DB(r)-NB(r)>
       (23/25)r^2-(609/1000)r+669/8000
       >=73/8000>0.                                (28)

This quadratic increases onr>=1/2; the final value is its value at1/2.
On the upper annulus[rB,R], use Lw instead:

    DU(r)-NB(r)>
       (927/1000)r^2-(573/1000)r+437/8000
       >=14887/1600000>0.                           (29)

Its derivative is positive fromrB=21/40, and the final fraction is
its exact value there. Thus both CLOSED boxed annulus families pass.

The two large-coordinate cases have an even stronger floor-free upper.
At the same base, (20) gives dx(cR)>439/320,dy(cR)>2501/960.
For x>=1/2, the relaxed x-quadratic decreases beyond1/2 because
439/320>7/12. Its maximum is at1/2; maximize the y-quadratic
over the larger domainy>=0. This yields

    S-Lambda_c< -77/3840+1849/150060<-1/200.           (30)

For the last comparison use35500800<43367340 after moving1/200.
For y>=1/2 the analogous y-quadratic decreases beyond1/2:

    S-Lambda_c< -1693/3840+245/3951
                         <-2/5+1/10=-3/10.         (31)

These optimizations enlarge domains ONLY AFTER the actual wide
model bound with legalcR has been established. They do not claim a
physical inequality outside rho<=R. Both radii floors are positive
on their actual domains (DB>Lh>0, DU>1/200 by E01), so(30),(31)
also discharge all four remaining X/Y inequalities in(17). Every
annular coordinate case and seam is therefore covered.

### E. A NEW complete wide-FAR radial argument, with no omitted old branch

For the ENTIRE CLOSED stripR<=rho<=1, each coordinate is<=1,
so u>=(11/48)(x^2+y^2) is valid everywhere. Use that coefficient
and the SAME tangent(11), retaining the complete wide allowance(6).
By(20),(21), the curvatures exceed5/4 and149/60; the linear
coefficients are at most7/12,43/120, andCW<1/32. Maximize the
relaxed quadratic over the whole line x+y=r. Its effective curvature
is745/896>4/5; its effective linear coefficient is2731/5376<21/40;
its constant from the linear difference is243/71680<1/250. Hence

    S-Lambda_c<141/4000+(21/40)r-(4/5)r^2.           (32)

This polynomial decreases forr>=3/4. SinceR=pi/4>3/4, its maximum
on the actual FAR strip is less than or equal to its value at3/4,

    141/4000+63/160-9/20=-21/1000.                   (33)

This is a complete replacement of the ORIGINAL optional GB/GX/GY
alternative: it proves the upper on ALLx,y>=0,R<=x+y<=1 at once.
No branch, large coordinate or constraint is dropped. No change of a
multiplier or tangent parameter is fitted; c=1/2 is unchanged. The
old separate gate signs remain uncomputed and are not asserted needed.

### F. The full outer GO also closes by paper

For the SAME768 baseline, MA<7/9. Also
2+8m/(3pi)<6170/9<768, so g<8; logm<7,log(2m)<8,
log2<7/10 andlogpi<6/5. These giveVB<80,Qg<84/m, and

    Gg<[409/9+98/3+84+8/5+16]/m
       =8087/(45m)<180/769<15/64.

No ordinary or outer contribution to Gg has been omitted. The new
global six-row term satisfies

    E6new<200/768+318/768^2<21/80.

Further, W<87/(10*769)<3/250. Combining these with D<7/100
and Mesh<3/250 gives

    CE<7/100+15/64+21/80+6/250
       =4727/8000<3/5.                              (34)

The full ordinary coefficient is
KD<566/(9*768)<1/12; sqrt(47/48)<1 andDc<6/7.
Together with(19),(20) this proves

    GO>(47/384)*(791/50)-6/7-3/5-1/12-11/50
       =23631/134400>1/6.                           (35)

The comparison with1/6 is141786>134400. This uses the COMPLETE
actual-origin allowance, new full-domain E6 and all global charges.
No approximate corner constant, unknown maximizer or omitted E0 is
introduced. All upstream model/PD-T271 premises remain inherited.

### G. Conclusion and all-n propagation

Equations(26),(28)--(31) prove the COMPLETE near/annulus families(17).
Equations(32),(33) give a NEW complete inner-FAR proof in place of
the optional separate GB/GX/GY predicates. Equation(35) proves outer
GO. All scalar domains and real-n monotonicity were established above;
the pointwise bounds improve for every larger realn. The complete
physical/parity/corner assembly therefore proves(1) for EVERY integer
n>=768. Near actual corners use the accepted(A^2+B^2)/16 loss;
the two origins retain the exact TRUE Lambda_c. No uniform positive
gap is asserted as a physical point approaches an actual maximizer.

This finishes the DEVELOPER PAPER theorem. Root adoption and distinct
assembly acceptance remain separate; no numerical job is implied.

## Original checker proposal — now deferred because the paper proof closes

The next step is distinct PAPER audit of the bridge-domain proof,
unrelaxed allowance collection, mixed monotonicity, radial domains and
EVERY rational comparison in the completed proof above. HPAIR/HROW now
have their separately completed independent acceptance. No unfinished
lemma or merely favorable coefficient is an executable premise.

The initial conditional draft proposed, only if useful after those
checks, a SEPARATE technical assignment for ONE fixedN768 directed
scalar/polynomial checker. That proposal is now DEFERRED, since the
paper proof closes without it. The unexecuted design was: at fixedN,
each Rad branch in(12) is quadratic and branch tests are affine in r.
Fn's sole radius denominator p+r is positive. After multiplying by
p+r and4(d1+d2), each required floor-minus-radial comparison is a
polynomial of degree at most3. Near max(3/50,min(...)) is a genuine
branch alternative; annular min floors require ALL constituent bounds,
not an arbitrarily chosen stronger floor. A finite exact interval/
Bernstein argument on the fixed closed r intervals can certify the
branches, including ties/tangencies, without S/lambda/kernel calls or
a two-dimensional phase cover.

An outer enclosure[ rB,p_upper/4 ] may be used for the LAST polynomial
sign interval if its proof applies only afterward to ACTUALr<=pi/4.
This is an algebraic domain enlargement, never a physical floor claim
outside its actual guard. The FAR penalty remains actualpi/8, not a
replaced radius that could omit an actual seam. All actual scalar
constants need validated outward enclosures and independent replay.

Historical proposed execution scope, never authorization: oneN768, no degree/c/
multiplier/precision/cap search or fallback, finite predeclared proof
cap, complete first-failure artifact and<=5CPU including imports and
finalization. Exact source/SPEC/controls/output/resource contracts are
for that later technical assignment. If a fixed paper/rational witness
kills this tangent relaxation, preserve that scoped failure and defer
the exact two-variable z=sqrtx,w=sqrty route to a new prospective task;
do not rescue a numerical attempt by changing c or the partition.

No endpoint, scalar, synthetic numeric control, phase, native, kernel,
quadrature, compiler/build, finite-degree or pack job was run here.
Only read-only provenance/text/hash inspections and these THREE owned
Markdown writes occurred. E01/old proof/source/evidence/shared/Git
bytes are unchanged. Requested Sol xhigh, serving metadata unexposed;
rules/inputfd17f683965eb501d9c9a4fd05b9b5ce4838d7f6. Initial conditional
draft2026-11-06; completed rational proof2026-11-07. The global768
theorem is PROVED at developer paper scope with inherited accepted
premises; distinct assembly acceptance and root adoption are pending.
No source/endpoint job ran or is needed for these written comparisons.


## Root adoption of analytic global768 —2026-11-07

Current theorem is PROVED and adopted for EVERY integer n>=768.
Distinct Astra high [assembly review](../independent-checks-E02-assembly768.md),
SHA256 b9e2d76c4bac54ec52b54f1de3fb2629291c9f05549eaf9f7e9c63c016e06c83,
accepts the unchanged31,981-byte prefix0ef1880f... including every written
log-series/rational comparison, physical closed chart/seam/zero/node/
collision/parity/corner case and real-n transfer. No source, scalar,
endpoint, native or finite-degree computation was required or executed.
The new matched partition uses phase-aware ACTUAL noncorner floors in
the annulus and a complete uniform wide-FAR inequality; it does not
relabel the old primitive FAR bound on its larger domain. PD-T271 and
accepted upstream dependencies remain explicit; final Claude is separate.
Root residual is now719degrees:43–62,65–158,161–510,513–767.
Global512 and fullD13 remain OPEN. Pack stays PAUSED during E03–E15.
