# E08 phase-global error — Retain the actual phase before absolute majorization

Provisional developer theorem; no global ID. Aliases: correlated D35/D07/
E02 allowance; full-diamond absolute phase envelope; combined three-H
saving. Quantitative continuation of E01-C5 and the accepted E02 global
row estimate. This is NOT a new signed-cancellation theorem.

## Statement and exact definitions

For EVERY integer n>=32 put m=n+1,L=log n,H=1+L,e=exp(1). Initially
alpha,beta>=0,alpha+beta<=pi. Define the SAME actual phase quantities

    ce=cos((alpha+beta)/2),cd=cos((alpha-beta)/2),
    a=ce*cd=(cos alpha+cos beta)/2,
    p=sin alpha,q=sin beta,P=p+q,d=(q-p)_+.

All these quantities are nonnegative; ce,cd,a,p,q,d<=1,P<=2. Use the
UNCHANGED corrected primitive S_n and TRUE completed M_infty from D02,
the exceptional highest first-coordinate coefficient ONE, original
endpoint weights, actual finite polynomial collision values and unequal
n,m meshes. Every signed comparison is evaluated at separate absolute
phases, exactly as in D05, without interchanging coordinates.

The following are explicit scalar functions, with no unknown maximum:

    b=4/pi^2,r=log(5/2)+1/18,
    Da=[(52/pi^2)H+7]/n+20H/(pi*n^2),
    K35={ [6+16/(3pi)]H+2/pi }/n,
    Dphi=a*Da+10/n^2,

    epsilon=3pi/(2m),ell=-log(sin epsilon),
    Sbar=1/2+2a/epsilon,
    Gamma=p[1+log(1+2Sbar/p)] if p>0, Gamma=0 if p=0,
    MA=max(p,q)/pi+4a/pi^2,
    VA=2max(p,q)/pi+8a/pi^2=2MA,
    VB=23+[3Gamma+(2p+6P)ell+26a+20+2d log2]/pi,
    CB=6+(4+4a/e)/pi,
    Gphi=(L*VA+VB)/(2m)+6L*MA/m
          +(4/m)[7+(P/pi)(5+2log(2m))]
          +4d log pi/(pi*m)+2CB/m,

    C6phi=[21+21a+2L+((1+48p)H+24q)/pi]/n
                                         +(317+5/12)/n^2.       (1)

For the FULL scalar mesh, retain the actual cosine weights in the
accepted |Phi_0|<=4 bound. Set

    Dbar=4(ce+cd)/pi+a*b*log pi,
    Zbar=Dbar+a*b/n,
    Mphi=a*b*(2L+2r)/n
        +[Dbar+a*b*(L+1/n)]/(4n^2-1)
        +a*b/(2n-1)^2
        +[Zbar+a*b*(log(n+1/2)+2)]/[4(n-1/2)^2],
    W=[3log m+log2+2log pi+2]/(pi*m),
    CEphi=Dphi+Gphi+C6phi+Mphi+d*W.                       (2)

Then on the ENTIRE CLOSED signed diamond |alpha|+|beta|<=pi,

    |S_n(phi)-M_infty(phi,L)|<=CEphi(n,phi)+K35(n)*P.      (3)

The entropy has its literal zero value at p=0. Formula(3) includes axes,
a=0, vertices, both parities, ordinary weighted collisions, retained-row
polynomial collisions, moving sample zeros and numerator-root thresholds.
It is an ABSOLUTE error at each phase, not a phase-relative remainder.

There is also a material UNIFORM consequence. Let D,Gg,Mesh,W and
CEold be exactly the accepted E02/D20 uniform functions:

    D=Da+10/n^2,
    MAg=1/pi+4/pi^2,g=1+log(2+8m/(3pi)),
    VBg=23+[3g+14log m+46+2log2]/pi,
    Gg=7L*MAg/m+VBg/(2m)
       +(4/m)[7+(2/pi)(5+2log(2m))]
       +4log pi/(pi*m)+16/m,
    Mesh=b*(2L+2r)/n+[4+b*(L+1/n)]/(4n^2-1)
         +b/(2n-1)^2+[5+b*(log(n+1/2)+2)]/[4(n-1/2)^2],
    CEold=D+Gg+(67+19L)/n+318/n^2+Mesh+W.

For all real n>=32 and every actual phase in the full closed diamond,

    CEphi(n,phi)<CEold(n)-3H/n=CEbar(n),
    CEbar=D+Gg+(64+16L)/n+318/n^2+Mesh+W.                (4)

Thus(3) remains true with CEphi replaced by CEbar. This saving uses
correlation between DIFFERENT component bounds. In particular this paper
DOES NOT claim |J6-C2|<=(64+16L)/n+318/n^2. The unchanged standalone
E02 six-row theorem is still (67+19L)/n+318/n^2.

For each FIXED phase, CEphi,K35 and CEbar are positive and decreasing
on the entire real domain n>=32. Consequently the bound is suitable for
separate all-n sufficient reductions; no degree endpoint is evaluated.

Status: **PROVED developer PAPER theorem**, distinct audit/root adoption
pending. No384/256/onset/global-argmax sign or numerical premise. Neither
E07 Hmax nor its pending assembly is a dependency of this operator result.

## 1. Literal operator match and all six actual rows

D35-fixed-row-reduction, applied at the ACTUAL phase with R=2, gives

    |S-Kfixed|<=Dphi+K35*P, n>=32,                         (5)

after only H_n<=H. The ordinary labels remain k=2,...,m-2 on both
folded sides. Its complete weighted-pole error10/n^2+20aH/(pi*n^2),
symmetric-reference matching and all actual ordinary collisions remain.
There is no additional collision charge for this literal fixed set.

D07-global-outer(2), at the same actual phase, is EXACTLY Gphi in(1):
the term Q(P,2h) equals the expanded (4/m) expression because h=pi/m.
It bounds |Kfixed-Gintermediate| on the FULL diamond, not only rho<=1.
The actual ordinary centered cells still have initial lengths
h(3/2+t),h(5/2-t) and central lengths h(3/2-t),h(1/2+t),t=beta/pi.
Their paired lengths4h and2h, every gap, the BV midpoint allowance and
the continuous regularized endpoint values are all charged in Gphi.
No actual retained row is evaluated by an off-grid regularized profile.

E02-global-retained-rows(19), BEFORE independent maxima, proves

    |Jend-C2|
     <=[9+21a+H_n/pi+(48pH_n+24q)/pi]/n
                                          +(317+5/12)/n^2.      (6)

This is the complete FOUR original rows0,1,2m-2,2m-1, compared with
the SAME C2=ell0(beta)+ell1(alpha,beta)+ell1(alpha,-beta)
+ell2(alpha,-beta). It retains the exact direct nm sinc/tau chart,
near-index collisions, all far finite indices, both infinite-reference
tails, the closest row and its linked beta0 value. No finite actual
positive set is assumed to equal a reference positive set globally.

The remaining TWO actual rowsm-1,m obey E02(20), namely

    0<=Jcen<=(12+2L)/n.                                  (7)

Its full-domain proof is D20's weighted polynomial-continuous estimate;
it includes v=pi and every collision, both parities and all n residues.
We do not transfer E03/E04's stronger relative small-radius constants to
the full diamond. Add(6),(7) and use H_n<=H to obtain C6phi exactly.
All six labels and the matching Delta2/E2/C2 normalization are unchanged.

## 2. Full singular meshes, log and origin charges

D07-global-mesh gives the signed identity at the actual phase

    Gintermediate-M_infty=(J6-C2)+Rmesh+(d/pi)Rlog,
    |Rmesh|<=Bmesh, |Rlog|<=Blog.                          (8)

Here B0=a*b,D0=U0/pi+B0 log pi,Z_n=D0-B0 log(m/n), and the literal
Bmesh contains |D0|,|Z_n| and |H2|. Its exact h_j,g_j constants and
positive-argument Gamma product are unchanged. The actual final ordinary
index is m-2. No strip cutoff, old I_n, omitted fixed bias, extra near
correction or silent parameter transfer enters(8).

The actual numerator is U0=ce*Phi_0(eta_-)+cd*Phi_0(eta_+). Since
ce,cd>=0 and the accepted full-period weighted bound is |Phi_0|<=4,

    |D0|<=Dbar,
    |Z_n|<=Dbar+a*b*log(1+1/n)<=Zbar.                     (9)

Use B0=a*b and |H2|<=2r in the COMPLETE D07 Bmesh expression. Equations
(9) give Bmesh<=Mphi exactly. In particular no assertion U0=0 is made at
the origin or at a moving root. At a=0 the B0 terms are literally zero;
the remaining weighted U0 terms are still bounded, with no inverse a.

The full scalar log estimate is (d/pi)Blog=d*W. At d=0 it vanishes
exactly. Absolute values at the actual phase are taken AFTER(8), so no
signed cancellation between Rmesh,Rlog or retained rows is assumed.
Add(5)--(9) and the triangle inequality to prove(3).

For later comparison with the accepted uniform Mesh, note using pi>3,
b<1/2,log pi<6/5 and ce+cd<=2 that

    Dbar<8/3+3/5=49/15<4,
    Zbar<49/15+1/64<5.                                 (10)

Thus Mphi<=Mesh componentwise. This only majorizes a nonnegative scalar
allowance after the physical theorem was applied at an ACTUAL phase.

The independent ACTUAL-origin allowance remains the COMPLETE D16 one:

    G0=[(28/pi^2)L+111/2+23/pi]/m,
    E0=D+G0+Mesh+14/n+71/n^2,
    |S_n(0)-M_infty(0,L)|<=E0.                          (11)

It has its literal p=q=P=d=0 evaluation, including its U0/D0 definitions;
we do not replace it by a full-phase maximum, by CEphi(0), or by a
conjectured favorable sign. For E=S-M_infty,u=1-a the exact relative
conversion remains E(phi)-E(0)=delta_aE-uE(0)<=delta_aE+uE0. In an
absolute comparison of S(phi) with the true symbolic Lambda_c=S(0),
the whole E0 is still charged. A separately assigned one-sided origin
study is not a premise of this theorem.

## 3. First decisive correlation test and a uniform three-H saving

The accepted uniform functions dominate the phase ones, but keeping only
their componentwise differences would miss the main quantitative fact.
First, D-Dphi=(1-a)Da. For the outer entropy, let

    Gamma(p,a,m)=p[1+log(1+(1+8am/(3pi))/p)].

It increases separately in p,a>=0, with its continuous zero value at p0:
for x>0 the p derivative is1+log(1+x)-x/(1+x)>0. Thus Gamma<=g,
ell<=log m,CB<8,MA<=MAg, and every remaining positive term of Gphi
is bounded by its corresponding Gg term. Keep the a portion of MA:

    Gg-Gphi >= [28L/(pi^2*m)]*(1-a).                    (12)

There is no application of a physical theorem at inconsistent values
a=p=q=1. Only the explicit positive RHS was majorized after its validity
at the actual tuple had been established.

The same comparison in(6)--(7) gives

    (67+19L)/n+318/n^2-C6phi
      >=[21(1-a)+(48H/pi)(1-p)+(24/pi)(1-q)]/n.          (13)

Indeed at independent maxima the remaining coefficient is
42+2L+(49H+24)/pi<67+19L, exactly the accepted E02 final simplification;
also317+5/12<318. We only need the p term in(13). Equations(10),d<=1
and(12)--(13) imply

    CEold-CEphi
      >={[52H/(pi^2*n)+28L/(pi^2*m)](1-a)
                                       +(48H/(pi*n))(1-p)}.    (14)

This is the cheapest substantive test. It couples ordinary, regular-
outer and endpoint-row charges at the SAME phase before maximizing.
On real n>=32, L>3 and n/m>=32/33, so L/H>3/4 and

    52+28*(n/m)*(L/H)>52+224/11=796/11.

The actual trigonometric relation gives
1-a>=(1-cos alpha)/2,p=sin alpha. Set

    A=398/(11pi^2),B=48/pi.

Then(14), divided by H/n, is at least

    A(1-cos alpha)+B(1-sin alpha)
       >=A+B-sqrt(A^2+B^2)>3.                          (15)

The norm inequality is global, including alpha outside the first
quadrant. To prove the strict last comparison entirely on paper, use
pi^2<10 and pi<16/5 to get A>199/55>18/5 and B>15. Hence A+B-3>0
and

    (A+B-3)^2-(A^2+B^2)
       =2(A-3)(B-3)-9>2*(3/5)*12-9=27/5>0.

Thus(15) proves(4). The elementary L>3 follows from e<3 and
e^3<27<32. There was no scalar/degree evaluation, fitted phase or tuned
threshold in this argument. The saving exceeds3H/n everywhere on the
full diamond and does not rely on the small rounding gap19 versus55/3.

The exact phase allowance(1)--(2) remains primary: it generally retains
additional useful a,p,q,max(p,q),d,entropy and mesh correlations that the
uniform corollary deliberately does not quantify. No optimality claim
or universal sharp coefficient is made.

## 4. Fresh all-real-n monotonicity and sufficient reductions

Fix an ACTUAL phase. Dphi and K35 are positive sums of(cL+d)/n^j or
nonnegative inverse-power terms and decrease for n>=32. C6phi has the
same property, with positive coefficient independent of n. W decreases
since the derivative numerator is3-[3log m+log2+2log pi+2]<0.

For Gphi use the positive expansion in(1). L/m decreases because
1+1/n-L<0. The terms log(2m)/m and constants/m decrease. For ell,
epsilon=3pi/(2m)<1/7, so ell>1; moreover

    m*(d ell/dm)=epsilon*cot epsilon<=1.

Therefore ell/m decreases. For p>0 the entropy obeys, with
c=8a/(3pi),

    m*(d Gamma/dm)=p*c*m/(p+1+c*m)<p<=Gamma,

so Gamma/m decreases; at p=0 it is identically zero. This proves
Gphi decreases without replacing its literal sine-log by an invalid
near-domain constant. Coefficient switches max(p,q),d are fixed phase
numbers, not differentiations in phase.

For Mphi, Dbar is fixed in n and Zbar=Dbar+a*b/n decreases. The leading
(2L+2r)/n decreases. Split the second term into
(Dbar+a*b*L)/(4n^2-1)+a*b/[n(4n^2-1)]; each nonzero term decreases
for L>3. The last term is a positive sum of a constant,1/n and
log(n+1/2), divided by4(n-1/2)^2. Its logarithmic derivative has sign
bounded by(n-1/2)/(n+1/2)-2log(n+1/2)<0. The remaining inverse-square
term decreases. Thus CEphi decreases on ALL real n>=32.

The uniform CEbar in(4) has only the OLD positive D,Gg,Mesh,W plus
(64+16L)/n+318/n^2. This is positive and decreasing, as are its old
components by their accepted full-domain proofs. We do NOT infer
monotonicity merely by subtracting two decreasing functions.

For any fixed, n-independent closed phase set Omega, the supremum of
CEphi+K35P over Omega consequently decreases. This does NOT assert that
CEphi/u or its maximum over level sets of u decreases. The old D18
quotient reduction cannot silently be applied to this new multi-parameter
formula. A later application may instead retain an analytic phase bound
on Omega, or use the explicit uniform CEbar.

More explicitly, suppose a SEPARATE correctly matched completed-model
theorem supplies M_infty(0,L)-M_infty(phi,L)>=u*T(n)-Q(phi), with
u=1-a>=0,T increasing and Q independent of n. Then a paper inequality

    u*T(N)-Q(phi)-CEphi(N,phi)-K35(N)*P-E0(N)>0
                                                for EVERY phi in Omega

implies the corresponding primitive exclusion for every integer n>=N.
Every term has its proved real-n direction. No sign at N, choice of N,
physical/noncorner floor, actual-corner bridge or complete cover follows
from this implication alone. Any PD-T271 premise needed by that separate
model/origin-constant theorem remains explicit there; (3)--(4) need none.

The existing D17/D27 full period/sign adapter and completed-model bound
also permit the ROUTINE global signed-family norm with CEbar in place
of CEold, an improvement3H/n in that bound on n>=32. This uses the SAME
global8/3 constant,4L^2+(79/5)L coefficient and2K35 as E02(24), not an
unknown argmax norm, E07 Hmax or a sampled finite maximum.

## Limitations, frozen predecessors and execution boundary

The full signed block (J6-C2)+Eout+Rmesh+(d/pi)Rlog still has NO new
cancellation theorem here. Every component is bounded absolutely in(3).
E03's fixed-alpha central-log match is not made uniform or extended to
all phases by this paper. E03's complete-error cusp and its no-log-linear
obstruction are unchanged; full D13 and broader cusp-aware finite bounds
remain OPEN. Neither a phase-relative remainder nor a new E0 sign has
been asserted. CEbar's smaller combined coefficient is not relabeled as
a six-row theorem.

2026-11-07, requested Codex gpt-6.1-sol xhigh, serving metadata unexposed.
Input3cdaaaf157c7de9c2c9954fc71cf3f5a62b3fdec; rules fully read63c70b7
and unchanged diff checked. Full unchanged complete registry/table/current
baseline verified by actual hashes, fresh E08 searches and full relevant
predecessors read BEFORE candidates; details/dispositions in the owned
idea/attempt. No historical priority or new interpolation/kernel claim.
Only the THREE assigned E08 prose paths changed. No accepted proof/source,
data, shared ledger, Git, pack or global ID changed. No script/import,
scalar/endpoint/threshold/native/phase/board/root/quadrature/degree/
compile/control/scientific job ran. All such jobs remain UNRELEASED.
Distinct mathematical audit is required before any assembly consumes it.


## Root adoption —2026-11-07

Root adopts full closed signed diamond, every integern>=32, exactCEphi and combined uniform saving3H/n with fixed-phase real-n monotonicity, after distinct [independent-checks-E08-phase-global.md](../independent-checks-E08-phase-global.md), SHA256bf1467923e034ea648e41673657fa9edf671932a92f5e73f3828b5944f6a8f43. The exact frozen15281B proof prefix8886d44e27cdb70bb4169c5e23ac09d82f8e8d63391ec33059424a2fd007cdfa remains unchanged. No new onset follows from this support alone. Final Claude audit remains separate; no numerical/source job occurred.
