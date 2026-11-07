# PD-T?argmax-bridge-codex-F07-prune — Closed five-fourths primitive exclusion from256

ID kind: PD-T. Aliases: fixed256 F01 reanchor application;
five-fourths common-S pruning; regional analytic cost support.
Split from: application of F01-seam-reanchor's generic sufficient
implication, not a new finite-operator estimate. Split into: none.

## Statement and status

For EVERY integer n>=256 and EVERY real signed phase satisfying

    5/4<=rho=|alpha|+|beta|<=pi,

the SAME original corrected primitive satisfies

    Lambda_c(n)-S_n(alpha,beta)>283/2850>9/100.       (1)

Lambda_c(n)=S_n(0,0) is the TRUE symbolic finite nonnode-corner value.
All original unequal n,m=n+1 meshes, highest first-coordinate coefficient
ONE, endpoint weights, ordinary masks, SIX retained rows and continuous
finite-polynomial collision values are unchanged. Both degree parities,
both axes, rho=5/4, rho=pi and all phase vertices are included.

Overall status: **PROVED developer PAPER theorem**, requiring distinct
mathematical review/root adoption. No execution or numerical premise.
This is a REGIONAL primitive result. It certifies no new finite degree,
full argmax256, smaller global onset, measured runtime or vertex saving.
It changes no checker, source, certificate, pack or execution release.

## Definitions and accepted dependencies

Precisely PD-T101/364's corrected finite polynomial defines S: with
m=n+1, h_0=1,h_j=2(j>0), put

    G_n(u,v)=sum_(r+s<=n)h_r h_s cos(ru)cos(sv)-cos(nu),
    S_n(alpha,beta)=(1/(2nm))sum_(j+k odd,0<=j<2n,0<=k<2m)
                         |G_n((j*pi+alpha)/n,(k*pi+beta)/m)|.

The finite polynomial defines all collisions. The proof below applies
the accepted F01-seam-reanchor9429B proof prefix
9af7eb0f28a2266b0893ef4e51cb51534a344aa459b7b4d5d3d1b2d9c6c0b36a,
accepted in the complete distinct F01 mathematical review
39dcb7fbf90e619f07a99ecb75b5f533722e9c3deec62d0b2ca0d5eb6a960313.
Its root adoption was read before this application. No unaccepted F-round
draft or F03 origin sign is a premise.

F01 inherits E08's complete physical absolute error and one-sided origin
allowance; E13's coefficient calculus; C08's full log coefficients; and
E06/E07's GLOBAL model master. The latter retains its named accepted
computer-assisted PD-T271 limiting-origin/regular-constant dependency.
That dependency is not a finite Lambda_c lower bound. The elementary
constants below are accepted in E15/E14, with local rational checks
given where used. No external theorem/PDF or new computation is used.

For real scalar n>=32 put m=n+1,L=log n,H=1+L and FIX

    a0=13/16,w0=29/16,p0=3/5,P0=6/5,eta=3/2,
    j*=23/250,t*=221/500,T=(4L^2-3L)/pi^2,
    b=4/pi^2,hr=log(5/2)+1/18,
    Da=[(52/pi^2)H+7]/n+20H/(pi*n^2),D=Da+10/n^2,
    KD={ [6+16/(3pi)]H+2/pi }/n,
    epsilon=3pi/(2m),ell=-log(sin epsilon),
    W=[3log m+log2+2log pi+2]/(pi*m),
    C=1+8a0*m/(3pi),
    Gamma_b=p0[1+log(1+C/p0)],
    gamma_b=1+log(1+C/p0)-C/(p0+C),
    MA_b=p0/pi+a0*b,
    VB_b=23+[3Gamma_b+(2p0+6P0)ell+26a0+20]/pi,
    CB_b=6+(4+4a0/exp(1))/pi,
    G_env=7L*MA_b/m+VB_b/(2m)
                +(4/m)[7+(P0/pi)(5+2log(2m))]+2CB_b/m,
    D_env=a0*Da+10/n^2,
    R6_env=[21+21a0+2L+((1+48p0)H+24p0)/pi]/n
                                             +(317+5/12)/n^2,
    Dmesh_b=4w0/pi+a0*b*log pi,Zmesh_b=Dmesh_b+a0*b/n,
    M_env=a0*b*(2L+2hr)/n
       +[Dmesh_b+a0*b*(L+1/n)]/(4n^2-1)+a0*b/(2n-1)^2
       +[Zmesh_b+a0*b*(log(n+1/2)+2)]/[4(n-1/2)^2],
    Cb=D_env+G_env+R6_env+M_env,
    Cs=eta{7L/(pi*m)+(3gamma_b+2ell)/(2pi*m)
                                      +(48H+24)/(pi*n)}
                    +3{(log2+4log pi)/(pi*m)+W},
    Cl=[9ell+12(5+2log(2m))]/(pi*m).

The WHOLE accepted origin allowance is EXACTLY

    Mesh=b*(2L+2hr)/n+[4+b*(L+1/n)]/(4n^2-1)
          +b/(2n-1)^2
          +[5+b*(log(n+1/2)+2)]/[4(n-1/2)^2],
    Bout=pi[L+25log(2m)+193/3]/(8m^2)+1/(8n^2),
    Rplus=[71/n^2-22/(45m)]_+,
    e0=D+Mesh+Bout+Rplus.                            (2)

No ebar substitution, u-weighted origin charge or favorable origin sign
is used. All fixed functions above are the SAME F01 functions.

## 1. The precise generic implication used

F01 proves at EVERY actual closed signed5/4<=rho<=pi and integer n>=32,
with u=1-(cos alpha+cos beta)/2 and v=u-3/16>=0,

    Lambda_c-S_n>=G*+K*v-A*sqrt(v),
    G*=(3/16)(T+j*)-(3/5)t*-Cb-(6/5)KD-e0,
    K*=T+j*-Cl-3KD,A*=(3/2)t*+Cs.                   (3)

The consistent replacements j*,t* weaken the ORIGINAL global master
pointwise because u,p>=0; they are used throughout(3). If K*>0, its
accepted square completion gives

    Lambda_c-S_n>=F*=G*-A*^2/(4K*).                 (4)

F01 proves Cb,Cs,Cl,KD,e0 positive/decreasing on real n>=32, T increasing,
and consequently G*,K* increasing, A*>0 decreasing and F* increasing
where K*>0. These are directions for explicit scalar functions, not
monotonicity of actual S_n or Lambda_c. No new domain extension or
CEphi/u ordering is required. The ONLY base in this application is256.

## 2. Written elementary inputs at the sole base256

From this section through section6 ALL scalar bounds are at n=256,
m=257. They are NOT constant logarithmic bounds on unbounded n.
The all-n conclusion uses the ORIGINAL scalar directions in section1.

For 0<z<1 use log((1+z)/(1-z))=2sum_(k>=0)z^(2k+1)/(2k+1),
obtained by integrating its positive geometric series. A first omitted
denominator bounds its geometric tail. At z=1/3 and z=1/2 this gives

    842/1215<log2<842/1215+1/6804<111/160<7/10,
    log2>693/1000, log3>7379/6720.                  (5)

The first finite sum ends at degree5; its tail is1/6804. The second
lower finite sum ends at degree7. Thus log256=8log2 gives

    277/50<L<111/20<28/5,H<33/5,
    logm<L+1/256<28/5,log(2m)<63/10,
    log(n+1/2)<logm<6.                             (6)

For the first lower bound,8*(693/1000)=693/125>277/50; the positive
cross-product difference is25. For logm use log(1+1/256)<1/256 and
1/256<1/20. These are elementary written comparisons, not calculator
or scalar-helper output.

The accepted bracket157/50<pi<22/7 implies

    31/10<pi,197/20<pi^2<10,b<41/100,
    52/pi^2<16/3,logpi<6/5,hr<1,exp(1)>5/2.        (7)

For clarity, the pi-square lower follows from24649>24625, and its
upper from484<490. Also80/197<41/100 and1040/197<16/3.
The positive exponential sum through degree4 at6/5 exceeds22/7,
which proves logpi<6/5. At z=1/9 the same log series gives
log(5/4)<2/9+1/1080<9/40; hence
hr<7/10+9/40+1/18=353/360<1. The positive sum
1+1+1/2+1/6=8/3 proves exp(1)>5/2.

The increasing polynomial4L^2-3L and(6),(7) give

    T>[4(277/50)^2-3(277/50)]/10
       =132683/12500>21/2.                         (8)

## 3. Entire origin and separate ordinary coefficient

First bound D, retaining BOTH inverse-square terms in(2):

    D<[(16/3)(33/5)+7]/256
                  +[10+20(33/5)/3]/256^2
      =211/1280+27/32768=27143/163840<1/6.          (9)

For the three tails of Mesh, the numerators are respectively<8,<1,<9
using L,log(n+1/2)<6,b<1/2. Their denominators give respectively
<3/n^2,<1/n^2,<4/n^2, so their sum<8/n^2<14/n^2<1/4000.
In the last comparison7*4000<32768. The leading term is

    b*(2L+2hr)/n<(41/100)*(66/5)/256
                         =1353/64000<43/2000.

Therefore Mesh<87/4000<11/500. This is a base256 tail bound, not a
false all-n bound with log n held fixed.

For Bout, the complete bracket is

    L+25log(2m)+193/3<28/5+315/2+193/3=6823/30<230.

Since pi<16/5,m>n, Bout<737/(8n^2)=737/524288<1/500.
The positive part is actually zero at this base:
71*45*257=821115<1441792=22*256^2. Thus the WHOLE origin cost obeys

    e0<1/6+11/500+1/500=143/750<1/5.               (10)

No origin sign was inferred and no origin term was dropped without its
signed inequality. The accepted all-n e0 remains the literal function(2).

The ENTIRE KD, including its2/pi term, satisfies

    KD<{(6+16/9)(33/5)+2/3}/256=13/64<21/100.      (11)

## 4. Literal cutoff, entropy and base-envelope coefficients

Here epsilon<1/7. The sine Taylor lower gives

    sin epsilon>epsilon*(293/294)
       >(93/(20m))*(293/294)>23/(5m).

Moreover23/5>9/2 and(5) give

    log(23/5)>2log3-log2
       >2*(7379/6720)-111/160=631/420>3/2.

It follows that ell<logm-3/2<41/10. All sine/log quantities remain
literal F01 quantities, with no fitted cutoff.

For the entropy, its exact logarithm argument is

    1+C/p0=8/3+65m/(18pi)<8/3+65m/54<4m/3;

the last comparison is144<7m. Since log(4/3)<1/3, its log is
<28/5+1/3=89/15<6. Consequently

    Gamma_b<21/5,gamma_b<7.                        (12)

The fixed base MA_b obeys

    MA_b<30/157+533/1600<21/40;

the second comparison is48000<48199. Also CB_b<233/30<8 by
exp(1)>5/2 and pi>3. For the COMPLETE VB_b bracket,

    3Gamma_b+(2p0+6P0)ell+26a0+20
      <63/5+861/25+169/8+20=17633/200,
    VB_b<23+17633/628<52.                          (13)

The four positive numerator pieces of G_env now obey, in their ORIGINAL
order,

    7L*MA_b<1029/50<21, VB_b/2<26,
    4[7+(P0/pi)(5+2log(2m))]<8620/157<55,
    2CB_b<16.

Thus G_env<118/257<47/100. All regular-outer/hole/entropy/CB costs are
present; no d or scalar log is set to zero by a balanced fake phase.

For the ordinary component,

    D_env=a0*D+(1-a0)*10/n^2
           <13/96+5/32768<7/50.                    (14)

For the FULL six retained rows, its three numerator groups satisfy

    21+21a0<77/2,2L<23/2,
    [(1+48p0)H+24p0]/pi<10554/157<68.

Their sum is<118. The original inverse-square317+5/12<318 remains:

    R6_env<118/256+318/256^2=30526/65536<47/100.     (15)

For the FULL weighted mesh, Dmesh_b<29/12+2/5<3 and Zmesh_b<4;
in particular their uniform upper bounds4,5 allow the SAME three-tail
estimate<14/n^2<1/4000 used above. Its leading term is less than
a0*(43/2000)=559/32000<7/400. Therefore

    M_env<71/4000<1/50,
    Cb=D_env+G_env+R6_env+M_env
         <7/50+47/100+47/100+1/50=11/10.           (16)

These four bounds include the ordinary non-a remainder, all SIX actual
rows, every regular outer hole and every weighted mesh tail.

## 5. Both square-root brackets and the full slope-three coefficient

Bound the eta-bracket of Cs in its ORIGINAL order:

    7L/(pi*m)<196/3855<13/250,
    (3gamma_b+2ell)/(2pi*m)<73/3855<1/50,
    (48H+24)/(pi*n)<1065/2512<43/100.

For the separate d bracket keep BOTH terms:

    (log2+4logpi)/(pi*m)<11/1542<1/125,
    W<219/7710<3/100.

Consequently the COMPLETE coefficient satisfies

    Cs<(3/2)*(251/500)+3*(19/500)=867/1000<9/10.     (17)

Finally the actual slope-three linear coefficient is

    Cl<[9*(41/10)+12*(5+2*(63/10))]/[(157/50)*257]
       =12405/40349<1/3.                           (18)

The final comparison is37215<40349. In particular Cs's scalar log W,
Cl's full outer-hole numerator, and the separate KD are all still paid.

## 6. First and only complete gate: K before division, then F

Insert(8),(10),(11),(16)--(18) into the WHOLE fixed system(3). FIRST,

    K*>21/2+23/250-1/3-63/100
       =19/2+193/1500>19/2>0.                     (19)

Only now is division/square completion permitted. The base term obeys

    G*>(3/16)(21/2+23/250)-(3/5)(221/500)
                              -11/10-63/250-1/5
       =211/1250>1/6,
    A*<(3/2)(221/500)+9/10=1563/1000<8/5.          (20)

Thus the FIRST registered fixed256 test gives

    F*(256)>1/6-(8/5)^2/[4*(19/2)]
             =283/2850>9/100.                     (21)

All arithmetic in(5)--(21) is written rational/power/series comparison.
No script, calculator, exact-arithmetic helper, scalar endpoint execution,
phase/degree scan or numerical preview supplied a premise.

## 7. Every larger integer, closed boundaries and application boundary

Use the SAME functions and j*/t*/whole e0 for all n>=256. The accepted
F01 scalar directions give K*(n)>=K*(256)>0, G*(n)>=G*(256),
A*(n)<=A*(256), and hence F*(n)>=F*(256)>283/2850. Applying(3),(4)
at EVERY actual phase proves(1) for EVERY integer n>=256. No monotonicity
of actual S or Lambda_c, changing optimizer, new quotient order, origin
nonnegativity or extension of a near-only finite theorem is used.

The exact accepted F01 outer geometry and E08 global physical bounds
include signed phases, axes, both parities, rho5/4/rhopi, a=0 and every
polynomial collision. The fixed rational anchor is only a positive-RHS
majorization parameter, not a claimed realizable physical phase. Whole
actual-origin e0 is charged once in(3), separately from every phase cost.

E15 already excludes closedrho>=pi/2 from192; E14 outer already excludes
rho>=1 from320. This theorem is a quantitative application for the new
band5/4<=rho<pi/2 including64 residual degrees256..319. It neither
certifies those degrees nor changes the remaining global/near/corner
obligations. Existing common-S discard is IDEA320/454, not a new method.

PD-T364 gives physical lambda<=the SAME S in a legitimate physical chart.
A later whole-cell integration may use(1) only after proving the literal
closed guard for every physical point of a raw box, retaining true
symbolic Lambda_c, all13 grid premises and GRID norm whenever analytic
leaves occur. None of that source adaptation/audit/execution is released
or performed here. No vertex count, runtime or termination improvement
is claimed. Original Syvert30 scientific source proceeds independently.

## Checks, history and remaining obligations

Only hand PAPER reasoning and owned prose; ZERO script/import/calculator/
scalar/threshold/degree/phase/endpoint/native/quadrature/compiler/control/
pack jobs, no Git/shared-file/source/evidence mutation. Full proof read-back
is an author check, not independent verification. Distinct review is
required before adoption; final Claude and prior unwaived findings remain
separate. No global ID or PD-N is allocated.

2026-11-07, requested/API Codex gpt-6.1-sol xhigh. Rules/input and gate
coverage are in the owned idea/attempt. Root first received GATE COMPLETE,
durably registered this exact ONE256 gate, then supplied a SEPARATE PAPER
release. The owned idea4845B/attempt4931B were written BEFORE derivation;
their preserved prospective prefixes hash respectively
86400a5df4aee6847787a4aeb799fe28689b01ff86ab3e1ed10c3b830ee20a07
andfe40f3af869057b80576babc1e97f7756025b81bc829b586947cea11b811c6f9.
No alternate base, geometry, origin allowance or rescue branch was used.


## Root disposition after distinct mathematical acceptance —2026-11-07

Root adopts the exact mathematical statement under its written quantifiers, hypotheses and dependencies. The original frozen proof/record prefix is preserved and identified in [independent review](../independent-checks-F06-F07.md), final SHA256832ec81ce4aaba07198ecbef2bfb571f0e7011c405b622601d105dd25b9ffbec. No global-onset change, new finite degree, source integration, strict runtime saving, novelty/priority verdict, protocol waiver or readiness follows beyond the exact statement. Final Claude review remains separate.
