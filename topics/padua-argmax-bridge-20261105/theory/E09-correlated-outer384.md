# E09 — A correlated full outer exclusion from384

Provisional PD-T?argmax-bridge-codex-E09-outer384. Split from the
E09 global384 assembly. Status: **PROVED developer PAPER support**,
distinct independent review/root adoption required. Requested Sol xhigh,
serving metadata unexposed,2026-11-07; rules5fac9e1, metadata554b9755.
The canonical gate-timing limitation is in attempts/E09-assembly384.md;
mathematical proof does not waive it or imply readiness. ONE fixed384;
no source/script/scalar/native/endpoint/phase/degree/threshold/pack job.

For EVERY integer n>=384 and every real signed phase pair satisfying

    1<=|alpha|+|beta|<=pi,

the original corrected primitive obeys

    S_n(alpha,beta)<Lambda_c(n)−7/50.                (1)

This is an outer primitive theorem, not a complete global argmax. It
uses ONLY the accepted Hmax/consequence map, full E08 phase error and
one-sided ACTUAL-origin lower allowance. E09's signed near operator and
E10's new central model are not premises.

## 1. Accepted objects and exact global comparison

Take x=|alpha|,y=|beta|,x+y<=pi,a=(cosx+cosy)/2,u=1−a,
p=sinx,q=sin y,P=p+q,d=(q−p)_+. The accepted E08 phase-global theorem
8886d44e27cdb70bb4169c5e23ac09d82f8e8d63391ec33059424a2fd007cdfa,
reviewbf1467923e034ea648e41673657fa9edf671932a92f5e73f3828b5944f6a8f43,
gives |S−M∞|<=CEphi(n,phi)+KD(n)P on the FULL closed signed diamond,
every n>=32. Its exact formula and all actual six rows, scalar meshes,
regular-outer cells/holes and polynomial collisions remain unchanged.

The accepted E08-origin-lower bba01a431ce3d7f4bfc4345eb693eb605fc3e82883cb7466a5ec597e1456d979,
mathematical review92775b0dce5f79cb3d06ef2cee998b63ce1f026013666bf714709e787a1f8625,
supplies for n>=160

    E_n(0)=Lambda_c−M∞(0,logn)>−ebar(n),
    ebar=D+Mesh+1/n,

positive/decreasing on its real domain. It is used ONLY as this
one-sided LOWER error, not as an absolute norm or E_n(0)>=0. Its
separate protocol finding remains in its canonical record.

Accepted Hmax461214a5 and consequence mapb6a9db93 give the exact
full-phase upper

    C∞(phi)−C∞(0)<=−j*u+t0*p,
    j>23/250,t0=2log2/pi<221/500.

This retains the full weighted endpoint/H0 loss and drops only an
additional nonpositive mixed-cosine term. It uses no local Ec equality
on the full diamond. The original C08 coefficient theorem supplies the
complete log-degree loss−uT,T=(4L²−3L)/pi². Thus

    Lambda_c−S>u(T+j)−t0*p−CEphi−KD*P−ebar.        (2)

All actual-origin and absolute finite charges are present. The accepted
PD271 limiting-origin computational dependency remains as in the
consequence map; it is not a finite Lambda inequality.

## 2. A NEW explicit u-majorant, not a quotient theorem for CEphi

For0<u<=1 define

    A=1−u,C=2−u,
    F=2sqrt[u(1−u)] if u<=1/2, F=1 if u>=1/2,
    S=min(2,sqrt(8u)).

Actual phases satisfy a=A,p,q,max(p,q),d<=F,P<=S,ce+cd<=C.
For p, cosx>=1−2u can be squared ONLY below1/2, where the RHS is
nonnegative. Above1/2 use p<=1; the same argument applies to q.
For P use P²<=8u,P<=2. The cosine sum bound is ce+cd<=1+ce*cd.
All pieces agree continuously at1/2.

Fix any n>=32,m=n+1,L=logn,H=1+L,b=4/pi²,hr=log(5/2)+1/18,
epsilon=3pi/(2m),ell=−log(sin epsilon). Define an explicit majorant
by the following positive RHS substitutions AFTER applying the actual
phase theorem:

    Dhat=A*Da+10/n²,
    Da=[(52/pi²)H+7]/n+20H/(pi*n²),
    Gammahat=F[1+log(1+(1+8Am/(3pi))/F)],
    MAhat=F/pi+4A/pi²,
    VBhat=23+[3Gammahat+(2F+6S)ell+26A+20+2Flog2]/pi,
    CBhat=6+(4+4A/exp(1))/pi,
    Ghat=7L*MAhat/m+VBhat/(2m)
           +(4/m)[7+(S/pi)(5+2log(2m))]
           +4Flogpi/(pi*m)+2CBhat/m,
    C6hat=[21+21A+2L+((1+48F)H+24F)/pi]/n
                                         +(317+5/12)/n²,
    Dbarhat=4C/pi+A*b*logpi,Zbarhat=Dbarhat+A*b/n,
    Mhat=A*b*(2L+2hr)/n
      +[Dbarhat+A*b*(L+1/n)]/(4n²−1)+A*b/(2n−1)²
      +[Zbarhat+A*b*(log(n+1/2)+2)]/[4(n−1/2)²],
    W=[3logm+log2+2logpi+2]/(pi*m),
    CEhat(n,u)=Dhat+Ghat+C6hat+Mhat+F*W.            (3)

Every positive factor is monotone in the replaced phase variables,
including Gamma in p,a. Hence CEphi(n,phi)<=CEhat(n,u). We do NOT
apply a physical theorem to an inconsistent tuple a=p=q=...; (3)
only majorizes its already valid positive RHS at an actual phase.
No new standalone six-row estimate is inferred from combined savings.

## 3. Prove the required phase quotient ordering

For fixed n, CEhat(n,u)/u is decreasing on0<u<=1. This is a NEW
majorant proof; it asserts NOTHING about CEphi/u or its exact level-set
maximum. The elementary ratios A/u=1/u−1,C/u=2/u−1,F/u and S/u
are decreasing on their respective continuous branches and across1/2.
The only nonlinear term requiring care is the entropy.

Let Psi(r,s)=r[1+log(1+s/r)],r,s>0. Both partial derivatives are
positive: Psi_s=r/(r+s)>0 and
Psi_r=1+log(1+s/r)−s/(r+s)>0. EXACT homogeneity gives

    Gammahat/u=Psi(F/u, [1+8Am/(3pi)]/u).

Both arguments decrease with u: the second is a positive multiple of
1/u plus a constant. Thus the entropy quotient decreases, including
the continuous1/2 seam. Every remaining term of CEhat/u is a sum
of positive constants times1/u,A/u,C/u,F/u,S/u or Gammahat/u.
This includes the FULL weighted scalar mesh: Dbarhat/u,Zbarhat/u
decrease separately, and their logarithmic/inverse-power coefficients
are positive fixed-n constants. It also includes CBhat/u and all
literal ell and W charges. Therefore the asserted order follows.

Consequently, for fixed n,

    Ghat_n(u)=u(T+j)−t0F−CEhat(n,u)−KD*S−ebar

has Ghat_n(u)/u increasing. One base phase parameter u0>0 with
Ghat_N(u0)>g>0 implies Ghat_N(u)>=(u/u0)g>=g for u>=u0.
To transfer to n>=N, use the ORIGINAL pointwise accepted monotonicity:
for each actual phase CEphi decreases, KD and ebar decrease, T
increases. Thus the actual RHS(2) at n is at least its value at N,
which is bounded below by Ghat_N(u). We need not assume that an
unproved phase-dependent optimizer or CEphi/u itself is monotone.

## 4. Entirely rational ONE-base384 comparison

Actualrho>=1 gives u>=u1=47/384 by the accepted cosine lower proxy.
At u1,A=337/384<22/25,F=sqrt(15839)/192<2/3,S=sqrt(47/48)<1,
C=721/384<19/10. E08-corner384's complete paper bounds give

    119/20<L384<6,H<7,T>25/2,
    D<3/25,Mesh<2/125,KD<3/20,W<1/50,
    ebar=D+Mesh+1/384<7/50.                        (4)

No norm or point is recomputed. Use pi>31/10,pi²>197/20,b<41/100,
hr<1,log2<7/10,logpi<6/5,log(2m)<34/5,logm<601/100. All are
written elementary inequalities at this fixed base, not numerical
previews. For ell, sin epsilon>4/m for n>=32: epsilon<1/7 and
sin epsilon>=epsilon(1−epsilon²/6)>(9/(2m))(293/294)>4/m.
Thus ell<log(m/4)<601/100−69/50<14/3.

The explicit component majorants in(3) satisfy

    Dhat<(22/25)(3/25)+10/384²<11/100,
    Gammahat<(2/3)[1+log(2m)]<26/5,
    MAhat<20/93+1760/4925<29/50,
    VBhat<54,CBhat<8,
    Ghat<122/385<8/25,
    C6hat<132/384+318/384²<7/20,
    Mhat<(22/25)(41/100)*14/384+14/384²<7/500,
    F*W<1/75,
    CEhat(384,u1)<1211/1500<81/100.                (5)

To inspect the nontrivial rows, Gamma increases separately in p,a;
at p2/3,a<=1 its logarithm argument is<5/2+4m/3<2m. For VBhat
the pi-bracket is less than
78/5+308/9+572/25+20+14/15<96; divide bypi>31/10, then add23.
For Ghat,7LMAhat<609/25<25,VBhat/2<27, the Q share is<52
because(5+2log2m)/pi<6 and S<1,2CBhat<16, and
4Flogpi/pi<16/15<2. Their sum is<122 before division by385.
For C6hat the n-numerator is<52+2470/31<132. For Mhat,
Dbarhat<76/31+5412/12500<3,Zbarhat<5, so its remaining THREE
terms are bounded by the SAME14/n² tail as the original Mesh.
Every term of the original operator is included.

Finally j>23/250,t0<221/500,so

    Ghat_384(u1)>
      (47/384)(25/2+23/250)−221/750−81/100−3/20−7/50
       =3517/24000>7/50.                          (6)

All comparisons in(4)--(6) are written rational inequalities. Applying
the quotient and n-transfer from section3 to every actual outer phase
proves(1), including both axes, closed boundaryrho1, a0 and vertices.

## Scope and execution boundary

This theorem leaves near/annular/far and actual-corner classification
to the separate full assembly. It does not extend a near relative
theorem to the full diamond, assume E_n(0)>=0, or alter any absolute
global norm. The phase caps are a legitimate positive-RHS relaxation,
and their quotient proof is separate from the original E08 operator.
Original E08 old-allocation failures remain valid at their exact scope.
Distinct math/protocol review is required; the canonical timing record
is linked above and is not retrospectively cured. No scientific job,
scalar/phase/source/threshold/degree/native call or pack work ran;
scientificCPU0, ordinary tool overhead unmeasured. Root owns adoption.
