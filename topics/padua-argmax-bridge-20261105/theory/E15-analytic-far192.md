# E15 — A strict analytic outer primitive gap from192

Provisional developer PAPER theorem, no global ID. Status: **PROVED
developer**, distinct mathematical audit/root adoption pending. This is
an application of accepted GENERAL E09 u-majorization and accepted full
phase/origin/model bounds, at ONE prospectively fixed192. It introduces
no new operator, full argmax degree, runtime claim or source adaptation.

## Statement and exact domain

For EVERY integer n>=192 and EVERY real signed phase with

    pi/2<=rho=|alpha|+|beta|<=pi,

the ORIGINAL corrected primitive satisfies

    S_n(alpha,beta)<Lambda_c(n)-79/2000
                  <Lambda_c(n)-3/100.                    (1)

Lambda_c(n)=S_n(0,0) is the TRUE symbolic actual nonnode-corner value,
not a rounded lower certificate or limiting polynomial. The original
unequal n,m=n+1 meshes, exceptional highest first-coordinate coefficient
ONE, endpoint weights, all six actual retained rows, ordinary masks and
weighted polynomial collision values remain unchanged. Separate absolute
phases reduce the signed statement; no n/m or coordinate exchange occurs.
Both phase seams and the full closed boundary, including a=0/vertices,
are included. No conclusion is asserted for rho<pi/2 or n<192.

## 1. Accepted general premises and exact absolute comparison

Write x=|alpha|,y=|beta|,rho=x+y<=pi and

    ce=cos(rho/2),cd=cos((x-y)/2),a=ce*cd=(cos x+cos y)/2,
    u=1-a,p=sin x,q=sin y,P=p+q,d=(q-p)_+,
    L=log n,H=1+L,m=n+1,T=(4L^2-3L)/pi^2.

The accepted E08 full-phase theorem has the EXACT absolute contract

    |S_n-M_infty|<=CEphi(n,phi)+KD(n)*P, n>=32,     (2)
    KD={ [6+16/(3pi)]H+2/pi }/n.

Its frozen proof8886d44e.../reviewbf146792... includes every ordinary
row, FOUR endpoint rows, TWO central rows, complete regular outer cells
and holes, scalar Mesh/log, numerator roots and continuous collisions.
The accepted E08 origin proofbba01a43.../review92775b0d... supplies ONLY

    E_n(0)=Lambda_c-M_infty(0,L)>-ebar,
    ebar=D+Mesh+1/n, EVERY integer n>=160,            (3)
    D=[(52/pi^2)H+7]/n+10/n^2+20H/(pi*n^2),
    b=4/pi^2,hr=log(5/2)+1/18,
    Mesh=b*(2L+2hr)/n+[4+b*(L+1/n)]/(4n^2-1)
       +b/(2n-1)^2+[5+b*(log(n+1/2)+2)]/[4(n-1/2)^2].

This is not an absolute norm or E_n(0)>=0 assertion. The WHOLE ebar
is charged below, not a u-weighted relative substitute. D,Mesh,KD,ebar
are positive/decreasing on their accepted real domains. No PD-T271
finite lower bound is being inferred from a limiting enclosure.

Accepted global Hmax/E06 consequences, with the unchanged named PD-T271
limiting-origin/regular-constant dependency, give on the FULL diamond

    C_infty(phi)-C_infty(0)<=-j*u+t0*p,
    j>23/250,t0=2log2/pi<221/500.

This is the GLOBAL weighted endpoint/H master, not a local central
decomposition used beyond its radius. C08's full coefficient theorem
gives the complete log-degree loss -uT. Hence, exactly as the GENERAL
E09 comparison,

    Lambda_c-S_n>u(T+j)-t0*p-CEphi-KD*P-ebar.        (4)

No E13 geometry, E14 claim, local signed T, E11 finite-domain extension
or new favorable origin sign is a premise. The proof uses the generic
lemmas in E09 sections2--3, valid n>=32; it DOES NOT apply E09's
already assembled n>=384 regional theorem below its stated onset.

## 2. Reconstruct the accepted generic u-majorant

For0<u<=1 set

    A=1-u,C=2-u,
    F=2sqrt(u(1-u)) if u<=1/2, F=1 if u>=1/2,
    Q=min(2,sqrt(8u)).

Actual phases obey a=A,p,q,max(p,q),d<=F,P<=Q,ce+cd<=C. The
F proof squares cos x>=1-2u ONLY when that lower bound is nonnegative;
the other branch uses p<=1. The same applies to q. These are the OLD
accepted E09 caps, not any E13 joint-radius bound. Put

    epsilon=3pi/(2m),ell=-log(sin epsilon),
    Da=[(52/pi^2)H+7]/n+20H/(pi*n^2),
    Dhat=A*Da+10/n^2,
    Gammahat=F[1+log(1+(1+8Am/(3pi))/F)],
    MAhat=F/pi+4A/pi^2,
    VBhat=23+[3Gammahat+(2F+6Q)ell+26A+20+2Flog2]/pi,
    CBhat=6+(4+4A/exp(1))/pi,
    Ghat=7L*MAhat/m+VBhat/(2m)
          +(4/m)[7+(Q/pi)(5+2log(2m))]
          +4Flogpi/(pi*m)+2CBhat/m,
    C6hat=[21+21A+2L+((1+48F)H+24F)/pi]/n
                                           +(317+5/12)/n^2,
    Dbarhat=4C/pi+A*b*logpi,Zbarhat=Dbarhat+A*b/n,
    Mhat=A*b*(2L+2hr)/n
       +[Dbarhat+A*b*(L+1/n)]/(4n^2-1)+A*b/(2n-1)^2
       +[Zbarhat+A*b*(log(n+1/2)+2)]/[4(n-1/2)^2],
    W=[3logm+log2+2logpi+2]/(pi*m),
    CEhat(n,u)=Dhat+Ghat+C6hat+Mhat+F*W.             (5)

The accepted E09 majorization gives CEphi<=CEhat at each ACTUAL
phase AFTER applying the physical theorem(2). Independent caps only
majorize its explicit nonnegative RHS; no fictitious physical tuple is
inserted into a theorem. Gamma is increasing in its positive p,a inputs
with its continuous zero limit. The mesh retains weighted U0/D0 and all
FOUR mesh terms; no U0=0 or discarded collision/cutoff is assumed.

For each fixed n>=32 the accepted general lemma proves

    CEhat(n,u)/u decreasing on0<u<=1.                (6)

For clarity, all nonentropy terms are positive sums of1/u,A/u,C/u,F/u,
Q/u. For entropy, Psi(r,s)=r[1+log(1+s/r)] has both partial derivatives
positive and is homogeneous, so Gammahat/u=Psi(F/u,[1+8Am/(3pi)]/u)
decreases as both arguments decrease. Every full mesh/tail coefficient
is positive. All branches meet continuously at1/2. This orders the
CONSTRUCTED majorant, not CEphi/u or its actual level-set maximum.

Thus with

    G_n(u)=u(T+j)-t0*F-CEhat(n,u)-KD*Q-ebar,

G_n(u)/u increases. A positive lower at ONE chosen u0 therefore supplies
at least that lower for every u>=u0. This part of the accepted lemma
has no degree384 restriction; only its former instance did.

## 3. Physical half-pi region and the one prospective scalar anchor

On rho>=pi/2, a=ce*cd<=ce<=cos(pi/4)<17/24. The last rational
comparison is exactly24^2<2*17^2. Therefore u>u0=7/24. At this anchor,

    A=17/24,C=41/24,F=sqrt119/12<11/12,
    Q=sqrt(7/3)<31/20.                              (7)

The final comparison is2800<2883 after squaring positive quantities.
The anchor is a scalar bounding device; it is not claimed to be an
attained physical phase. We now prove the FIRST registered gate at the
ONE base n=192,m=193, with no alternative degree or parameter scan.

### 3a. All written logarithmic/rational inputs

The positive atanh series with its geometric tail gives

    842/1215<log2<842/1215+1/6804<111/160<7/10,
    7379/6720<log3<7379/6720+1/1728<11/10.

For log2 take2atanh(1/3) through the fifth power and bound later odd
denominators below by7. For log3 take2atanh(1/2) through the seventh
power and bound later denominators below by9. The resulting tails are
precisely1/6804 and1/1728. Also842/1215>693/1000 and7379/6720>549/500
(the latter positive cross-product difference is220). Since192=3*2^6,

    21/4<657/125<L=log192<421/80<53/10,H<63/10,
    logm<L+1/192<53/10,
    log(2m)<421/80+7/10+1/192<6.                    (8)

Use the previously accepted elementary constants

    31/10<pi<22/7,197/20<pi^2<10,b<41/100,
    logpi<6/5,hr<1.                                (9)

These are not new numerical premises. For explicit simple checks,
exp(6/5)>1+6/5+18/25+36/125+54/625>22/7 gives the logpi bound.
The same atanh series gives log(5/4)<9/40; then
hr<7/10+9/40+1/18=353/360<1. Only written finite powers/rationals are
used. Since4L^2-3L increases here, (8),(9) imply

    T>(189/2)*(49/484)=9261/968>19/2.               (10)

### 3b. Complete origin and ordinary coefficient bounds

From52/pi^2<16/3 and pi>3,

    D<203/960+13/9216=9809/46080<43/200,
    Dhat<A*D+10/192^2
          <(17/24)*(43/200)+10/192^2<4/25.          (11)

The expression for D includes BOTH10/n^2 and20H/(pi*n^2). Dhat
was not bounded by an ordinary error missing its non-a pole terms.

At this base the SAME three mesh tails after the leading term have
sum<14/n^2. Here is a direct check instead of transferring a base384
tail claim: L<6,log(n+1/2)<logm<6,b<1/2 imply the second mesh
numerator<8 and denominator>3n^2, hence its term<3/n^2. The third
is<1/n^2. The last numerator<9 and denominator>9n^2/4, hence its
term<4/n^2. Their sum<8/n^2<14/n^2. The n>=2 denominator inequalities
used here hold at192; no uniform14/n^2 claim for unbounded log n is
needed for the later transfer. Therefore

    Mesh<(41/100)*(63/5)/192+14/192^2
         <27/1000+1/2500<7/250,
    ebar<43/200+7/250+1/192<1/4.                   (12)

For KD keep its entire2/pi term. The literal formula gives

    KD<[(718/93)*(63/10)+20/31]/192
       =7639/29760<13/50.                          (13)

### 3c. Every component of CEhat at the fixed anchor

The literal sine-log satisfies sin(epsilon)>4/m at alln>=32: since
epsilon<1/7, sin epsilon>=epsilon(1-epsilon^2/6)
>(9/(2m))*(293/294)>4/m. Thus

    ell<log(m/4)<53/10-69/50<4.                    (14)

Entropy increases in p,a. At p=11/12,a<=1 its log argument is
1+(12/11)(1+8m/(3pi))<23/11+32m/33<2m. Hence (8) gives
Gammahat<(11/12)*7=77/12<13/2. Also

    MAhat<55/186+170/591<3/5,
    VBhat<23+(10/31)[39/2+668/15+221/12+20+77/60]
           =23+3112/93<57,
    CBhat<8.                                      (15)

In VBhat the five terms respectively charge3Gammahat, the ENTIRE
(2F+6Q)ell,26A,20 and2Flog2. No central, logarithmic or d allowance
was discarded. In Ghat, the positive numerator pieces satisfy

    7L*MAhat<23, VBhat/2<29,
    4[7+(Q/pi)(5+2log(2m))]<62,
    4Flogpi/pi<44/31<2, 2CBhat<16.

Their sum is<132, so

    Ghat<132/193<7/10.                              (16)

The six-row numerator in(5), retaining its central2L and q term, is

    <21+119/8+53/5+3055/31<146.

Together with317+5/12<318 this proves

    C6hat<146/192+318/192^2=1575/2048<31/40.        (17)

For the FULL weighted mesh, (7),(9) give
Dbarhat<205/93+(17/24)(41/100)(6/5)<3,Zbarhat<5. Therefore its
three tails are bounded by the SAME14/n^2 just proved using the
uniform4,5 numerators; its leading A*b term is retained. Thus

    Mhat<(17/24)*(41/100)*(63/5)/192+14/192^2
         <49/2500+1/2500=1/50.                     (18)

Finally W<21/[(31/10)*193]=210/5983<9/250, so

    F*W<(11/12)*(9/250)=33/1000<1/30.              (19)

The d component is paid by its full F*W majorant; it was not set to0
merely because a convenient model phase was balanced. Equations
(11),(16)--(19) include ALL five terms in(5) and imply

    CEhat(192,u0)<4/25+7/10+31/40+1/50+1/30
                  =1013/600<17/10.                (20)

No scalar helper, floating value, actual S/Lambda call or numerical
endpoint was used. These are exact written upper comparisons.

## 4. Close the registered gate and transfer to every larger n

Using the accepted j,t0 bounds only in their safe directions,

    G_192(u0)>
      (7/24)(19/2+23/250)-(221/500)(11/12)
                         -17/10-(13/50)(31/20)-1/4
       =79/2000>3/100.                              (21)

By the accepted general quotient lemma(6), every actual u>=u0 has
G_192(u)>=(u/u0)G_192(u0)>79/2000. This includes every physical
phase in the required closed half-pi outer region by(7).

For EACH fixed actual phase, the ORIGINAL accepted CEphi,KD,ebar
decrease for real n>=192 while T increases. Hence the actual RHS(4)
at n is at least its actual RHS at192, which is bounded below by
G_192(u). This proves(1) for EVERY integern>=192. No monotonicity of
actual S_n or Lambda_c, no changing optimizer, no CEphi/u order and
no unproved n-order of a new envelope is assumed. Real-n statements
refer only to explicit scalar allowances, not noninteger Padua objects.

All zero/edge/seam conventions are inherited literally from the full
phase operator theorem: a=0, both axes, moving poles, coalescing
numerators, all original finite collisions and both parity meshes are
included. The generic F,Q branches meet at1/2 and have no inverse a.
The global H master is valid above pi/2, without invoking E11's local
model identity there. The true actual origin retains its whole allowance.

## Application boundary, preservation and execution record

This is a REGIONAL primitive theorem, not a full global argmax192
claim: the region rho<pi/2, actual-corner support, noncorner defects,
complete physical cover and equality classification remain separate.
In the explicitly pi-normalized coordinates (alpha/pi,beta/pi), the
guard is simply |alpha/pi|+|beta/pi|>=1/2. A future source adaptation/audit
could use this sufficient common-S exclusion on a whole cell inside
that guard. In a legitimate PD364 physical chart, the SAME actual
primitive obeys lambda=S-Delta<=S, so the primitive exclusion then
excludes that physical point without a noncorner floor. The chart and
whole-cell guard must still be verified by the future implementation.
This proof changes no checker, leaf predicate, collision
oracle or execution source; it proves no runtime saving or new finite
certified degree. Pack remains paused under root's allocation.

All older sufficient-allocation failures remain scoped and preserved.
No failure occurred in this first fixed192 gate, and no fallback N,
phase grid, parameter retune or scientific job was attempted. The
E09/origin chronology findings remain unwaived; this paper does not
retroactively cure them. Full D13, stronger interior finite mixed error,
origin nonnegativity and minimum global onset remain OPEN. E13/E14
are not premises, including any later acceptance or result.

2026-11-07. Requested Codex gpt-6.1-sol xhigh; serving metadata unexposed.
Rules63c70b7,inpute27e093732a306555a53725d31cd1121bdc61474. Complete
gate returned BEFORE root's separate durable mathematical release; the
owned candidate inventory preceded the first new test. Only the three
new assigned E15 prose files changed. No source/script/import/scalar/
endpoint/native/phase/root/quadrature/degree/threshold/board/compile/
control/scientific/pack/shared/Git job or mutation. Distinct paper
audit/root adoption are required before use; final Claude is separate.


## Root adoption —2026-11-07

Root adopts the exact13855B frozen regional proof above (SHA256b420adbd063a1055b1fd64f02155dd3e4d400f18cb0b7fe0760617cc0f032ec5) after distinct [E15 ACCEPT](../independent-checks-E15-analytic-far192.md), report15775B94718e23d96f875478ec9c4b7cd4713898e752756c182ecb647f7d49995b32e3. For EVERYintegern>=192 on the ENTIRE CLOSED rho>=pi/2 phase region, S_n<Lambda_c−79/2000<Lambda_c−3/100. Original prefix remains unchanged. This is an analytic pruning component, not global192, a new finite certificate, or a measured runtime claim. Future literal whole-cell/common-S checker adaptation needs its own source audit. No E13/E14 premise, new finding or numerical/source job occurred; upstream dependencies and final Claude audit remain explicit.


## Audit-02 dated current-state pointer — 2026-11-07

The header's pending-adoption wording is historical. The preceding root
adoption, following [distinct E15 ACCEPT](../independent-checks-E15-analytic-far192.md),
is the current mathematical scope: every integern>=192, closed
pi/2<=rho<=pi, exactly (1). Current global onset320 and273 residual
OPEN degrees43–62,65–158,161–319 are in [current report](../report.md)
and [E14 adoption](E14-assembly320.md). E14 remains context, not a premise
of this E15 proof. P1–P4 remain unwaived; the branch remains WORK.
