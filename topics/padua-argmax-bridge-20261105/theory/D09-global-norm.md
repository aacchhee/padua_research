# PD-T?argmax-bridge-codex-D09-norm — A logarithmic global norm with degree512 choice34

ID kind: PD-T. Aliases: completed-model global signed-family norm;
all-real-phase norm34 at512; quantitative D05 norm upper.
Split from: D08 point-to-box's sharper global-norm input. Split into:
none. No successful point-to-box/corner instance is claimed.

## Exact statement and normalization

For integer n>=2, put m=n+1,N=nm,h_0=1,h_j=2 for j>0, and use
the original corrected finite kernel

    G_n(u,v)=sum_(i+j<=n) h_i*h_j*cos(iu)*cos(jv)-cos(nu),
    Gamma^-={(r,s):0<=r<2n,0<=s<2m,r+s odd},
    S_n(alpha,beta)=(1/(2N))sum_Gamma^-
         |G_n((r*pi+alpha)/n,(s*pi+beta)/m)|.

All polynomial endpoint/collision values and the exceptional coefficient
one of(n,0) are retained. For n>=32,L=log n define U_F(n) exactly
by the complete scalar formula below, and let

    Q_sharp(n)=[4L^2+(79/5)L]/pi^2+123/40+U_F(n),
    Q_requested(n)=[4L^2+19L]/pi^2+123/40+U_F(n),
    M_n=2N                                      if2<=n<32,
        min(2N,Q_sharp(n))                       ifn>=32. (1)

Then for ALL real alpha,beta, S_n(alpha,beta)<=M_n. In particular
M_n=O(log^2 n) as n tends to infinity. For every real coefficient
family |sigma_rs|<=1 the signed board polynomial

    q_sigma(alpha,beta)=(1/(2N))sum_Gamma^- sigma_rs
                    G_n((r*pi+alpha)/n,(s*pi+beta)/m)

has global norm <=M_n over all real phases. For the original corrected
Padua cardinal basis l_jk on the physical square and EVERY real
coefficient family |epsilon_jk|<=1,

    sup_[-1,1]^2 |sum_(nodes) epsilon_jk*l_jk(x,y)|<=M_n,
    lambda_n(x,y)<=M_n.                                  (2)

For the particular degree n=512 the sharper exact norm choice is

    S_512(alpha,beta)<34 for ALL real alpha,beta,
    sup_[-1,1]^2 lambda_512<34,                            (3)

and34 bounds both signed polynomial families. The requested coarser
k_shift<2 route independently gives the safe choice36 instead.
Neither uses the location/value of an unknown global maximizer.

Status: **PROVED**, analytic consequence with one ALREADY ACCEPTED
scalar certificate dependency at512; distinct review of this application
pending. No new numerical run or code is part of D09. No global-argmax
theorem, successful vertex losses, cover or runtime is a premise/result.

## Complete U_F formula and frozen mathematical dependencies

U_F is the phase-independent upper of the independently accepted
D05-outer-comparison.md(2), with auxiliary R2,delta=pi/8 and inputs
a=1,p=1,P=2,d=1,abs(U0)=8,H_n<=H=1+L. Its literal domain is n>=32.
For a reproducible formula set h=pi/m,X=m/8,r=log(5/2)+1/18 and

    C_X=[5+(1/2)log(X+1/2)]/[2(X-1/2)]
                  +[6+(1/2)log(X+1/2)]/[8(X-1/2)^2],
    E_D={ [52/pi^2+704/(3pi)]H+7+4/pi }/n
                                   +10/n^2+20H/(pi*n^2),
    e_mesh=7L/(2m)+2C_X+(8+r)/n+1/(2n^2),
    e_rows=(181+19L)/n+21600/n^2,
    e_collision=(2/m)[7+(2/pi)(3+2log(2m))]
                                   +5/(n^2*m)+1/(nm),
    D_pole=10/n^2+20H/(pi*n^2).

For the interior constants put

    delta=pi/8, sbar=1/2+32/pi, f=log8,
    Gpar=1+log(2+64/pi),
    Astar=(1+64/pi)/pi, VA=128/pi^2,
    Vstar=128/pi+6, VV=256/pi+23,
    Jstar=max(5,2sbar*f+max(1,sbar+1/2)log2),
    VJ=(128/pi+4sbar)f+3Gpar+2(sbar+1/2)log2+20,
    Wstar=Vstar+Jstar/pi, VW=VV+VJ/pi,
    I_n=[(VA/2+9Astar)L+VW/2+5Wstar+4Vstar
                              +(4+5log m)/pi]/m.

Finally let epsilon=3h/2,ell=5h/2,

    W(z)=7+(2/pi)[3+2log(4pi/z)],
    Q(z)=(2z/pi)[7+(2/pi)(5+2log(4pi/z))],
    T_Z=[32+6log(6/epsilon)]/(2m)+Q(ell)
                          +[W(delta-h/2)+2W(2h)]/m,
    U_F=E_D+e_mesh+e_rows+e_collision+I_n+D_pole+T_Z.    (4)

These are the unchanged D05 positive allowances, not discarded errors
or a new model. All denominators/log arguments are valid for n>=32.
The scalar majorization is monotone in the nonnegative phase inputs;
for its entropy factor use monotonicity of u[1+log(1+S/u)] in u,S.
Thus |S_n-M_infty|<=U_F on the full closed diamond. D05 proves
U_F=O((1+log n)/n) at these fixed auxiliary parameters. No old R64
finite representation is applied below its degree floor.

Other mathematical dependencies are independent of a global argmax:

- C08-far-weighted-coefficient.md gives the actual accepted inequality
  b_full-b_c<=3(1-a)/pi^2 on the full closed diamond. The false
  b_full-a*b_c<=5(1-a)/4 shortcut is never used.
- C08's phase-only C_far<8821/3000 and D02's exact signed cutoff bias
  give C_infty<123/40 as verified directly below.
- The scalar gamma<3/5 is proved elementarily in C06-far-full-profile
  (the harmonic comparison near its end), with no numerical premise.
- PD-T364 gives the corrected physical reflection inequality
  lambda<=S_n on a complete physical odd-center cover, for n>=2.
- The phase-period adapter is already in D08-point-box-norm.md. It is
  reconstructed below as routine finite reindexing, not a new claim.

## Proof

### 1. Bound the model on the full closed phase diamond

Write k_shift=gamma+log(8/pi), b_c=8k_shift/pi^2. Since pi>3 and
e>8/3, log(8/pi)<1. The accepted elementary gamma<3/5 therefore
gives k_shift<8/5 (and also the parent's coarser k_shift<2).
For an elementary check of the inherited gamma bound, the harmonic
comparison gives gamma<=119/60-2log2, while the first three positive
terms of2atanh(1/3) give log2>83/120. Hence gamma<3/5.
Consequently the accepted coefficient inequality gives

    b_full<=b_c+3/pi^2<(79/5)/pi^2<19/pi^2.

Also B0=4a/pi^2<=4/pi^2. For the constant, use C08's fixed R64,
delta1/100 constant C_far<8821/3000 and D02's bias inequality

    C_infty<C_far+1/63^2+Q_old(2,1/100),
    Q_old(2,1/100)<637/4805,
    8821/3000+1/3969+637/4805<123/40.                 (5)

The bound on Q_old uses only pi>31/10 and log(400pi)<8, exactly
the original envelope Q_old(P,x)=(2x/pi)[7+(P/pi)(5+2log(4pi/x))].
These are n-independent
constant statements, not an old finite-n error theorem. Thus L>=0
and the full D05 comparison imply S_n<=Q_sharp on the closed diamond;
the same argument with k_shift<2 gives Q_requested.

### 2. Globalize the phase bound by its exact period lattice

For any integers p,q with p+q even, reindex r by r+p modulo2n and
s by s+q modulo2m in the FINITE odd-board sum. Parity is unchanged
and the finite kernel is2pi-periodic in both arguments. Hence

    S_n(alpha+p*pi,beta+q*pi)=S_n(alpha,beta).         (6)

In particular the lattice contains(pi,pi) and(pi,-pi). Set
s=(alpha+beta)/(2pi),t=(alpha-beta)/(2pi) and choose integers j,k
so s'=s-j,t'=t-k belong to[-1/2,1/2]. The congruent phase pair is

    alpha'=pi(s'+t'), beta'=pi(s'-t').

Its difference from(alpha,beta) is the lattice vector
pi(j+k,j-k), and

    |alpha'|+|beta'|=2pi max(|s'|,|t'|)<=pi.

Separate evenness follows directly by r->-r or s->-s, using the
kernel's separate cosine evenness. So the full real phase pair has
the same S_n value as a point of the first closed phase triangle.
This proves Q_sharp is GLOBAL. Neither coordinate mesh is exchanged,
and all ties/lattice boundaries use finite polynomial values.

For all n>=2, the corrected kernel's sum of nonnegative cosine-product
coefficients is2N: the original triangular count is2N+1 and correcting
the highest x coefficient from2 to1 removes one. Therefore |G_n|<=2N
for all real arguments and S_n<=2N. Combining this elementary fallback
with Q_sharp proves(1) at all n>=2. The finitely many small degrees do
not affect O(log^2 n).

### 3. Both complete signed families have the same global bound

For every board coefficient family |sigma_rs|<=1,
|q_sigma(alpha,beta)|<=S_n(alpha,beta)<=M_n pointwise, including
every real phase. For actual cardinals and |epsilon_jk|<=1,

    |sum epsilon_jk*l_jk(x,y)|<=sum|l_jk(x,y)|=lambda_n(x,y).

At any physical point PD-T364 supplies a physical odd-center phase
chart and the exact nonnegative full-defect identity lambda=S_n-Delta.
Thus lambda<=S_n<=M_n, proving(2). In particular the signed cardinal
functions after the actual-corner substitutions
(-cos(alpha/n),-cos(beta/m)) have this same bound for all real phases,
because their images remain in the physical square. No bound for an
unknown maximizer or a point maximum was used.

### 4. Exact degree512 choice, without another numerical run

The ALREADY independently accepted D06 scalar certificate gives the
uniform full-phase row of its exact component allowance at512:

    U_F(512)<=4.400114125755<9/2.                     (7)

This is the UPPER_DECIMAL uniform row of
code/post_audit_D06_model_budget/evidence.csv, not its MEASURED
actual-phase rows. The accepted independent replay/source/arithmetic
review is independent-checks-D06-model-budget.md. Its numerical
trusted base is documented Decimal correct rounding with directed
interval arithmetic and a rational Machin pi enclosure. We use that
accepted bound as a dependency and perform NO new scalar execution.

The elementary accepted log2<25/36 gives L=9log2<25/4. With
pi^2>197/20, all coefficients positive, the sharper numerator obeys

    4L^2+(79/5)L<255,
    Q_sharp(512)<5100/197+123/40+9/2
                =263691/7880<34.                   (8)

The parent-requested k_shift<2 route instead gives numerator<275
and Q_requested(512)<279691/7880<36. These are exact rational
comparisons. Equations(1)--(2) prove(3) and both signed-family norms.
No inference about another degree's norm follows merely from(8).

## Use, limitations and provenance

At512 the exact integer M=34 may be substituted into BOTH D08
interpolation norm slots. For its illustrative origin rectangle the
remaining sufficient slope condition becomes c>17pi^2/96, PROVIDED
the three actual certified point-loss inequalities also hold. This
file does not supply those losses or assert the predicate passed.
The primitive's cusp remains; its squared-coordinate interpolation
is not justified by this norm. The signed cardinal family, not its
absolute sum, supplies the separate even functions required there.

No numerical/native/board/phase-grid/quadrature run, source adoption,
point enclosure, cover, global argmax, degree certificate or runtime
claim occurred. All old bounds/models/corrections remain intact.
D08's new global-argmax theorem is NOT a dependency. The useful gain
is an explicit small GLOBAL norm, a quantitative continuation of the
known logarithmic bound and the existing period adapter.

Frozen dependency identities and actual read scope are in
attempts/D09-global-norm.md. 2026-11-06, parent-requested Codex Sol
xhigh, input`d4956aea3bda9d5ff9917a5b410778fc7adf4fb7`, bounded20min
analytic block. New application awaits distinct review.


### Supplementary review closure — 2026-11-06

Distinct Astra high review ACCEPTED the preceding unchanged proof, with
no unresolved finding; [independent-checks-D09-global-norm.md](../independent-checks-D09-global-norm.md),
report SHA2566e721695a76c0a8b622ec4a04420a87b761ebec8d063ed45256333170bf4accc.
This closes supplementary mathematical review. It supplies no successful
point losses, complete cover or final Claude acceptance.
