# PD-T?argmax-bridge-codex-D02-comparison — Actual-corner descent from degree10000

ID kind: PD-T. Aliases: D02 rectangular strip comparison;7.8 corner
bracket; actual half-diamond descent at10000.
Split from: D02 prospective uniform corner target.
Split into: the substantive strip and reciprocal-sum dependencies are
D02-corner-strip.md and D02-corner-sums.md.

## Statement

For every integer n>=10000, m=n+1, and alpha,beta>=0 with
alpha+beta<=1/2, set

    z_n=(-cos(alpha/n),-cos(beta/m)),
    r2=alpha^2+beta^2, a=(cos alpha+cos beta)/2,
    L=log(n+1), Lambda_c=lambda_n(-1,-1).

Then, for the corrected Padua Lebesgue function,

    lambda_n(z_n)<=a Lambda_c+[L/3+39/5]r2,          (1)
    lambda_n(z_n)<=Lambda_c-r2/4.                   (2)

Both conclusions hold at the other parity-correct nonnode corner,
using x reflection for even n and y reflection for odd n. The origin
has equality in(2); every positive inward phase is strictly below
Lambda_c. This is a local actual-corner statement, not global argmax.

## Status and dependencies

Overall status: **PROVED**, by the analytic proof below, with separate
substantive dependencies [D02 strip](D02-corner-strip.md) and
[D02 sums](D02-corner-sums.md). Distinct review is separate. No
measurement is a premise and the developer does not self-approve.

Other dependencies: the exact corrected four-copy identities in C02
§1; C05's quarter-angle calculus identity and derivative majorant;
C07-corner-positive-deformation(1), which is already stated for every
n>=2; and PD-T270's all-n one-dimensional remainder. Their exact
algebraic hypotheses are rechecked below. No frozen C07/C13 higher-floor
comparison theorem is invoked below its degree domain or changed.

## 1. All lower-domain regular geometry and normalization

Let O={(j,r):0<=j<=n,0<=r<=m,j+r odd}, with the original endpoint
half weights e_j,f_r, and let B={(j,j+1):2j>=n},R=O\B. Use the
same corrected finite F as D02-corner-strip. The exact identities are

    lambda=(1/(nm))sum_O e_j f_r |sum_four F_jr|,
    Lambda_c=(4/(nm))sum_O e_j f_r |F_jr(0,0)|.     (3)

They include repeated copies, the finite(n,m) endpoint, initially
zero cardinals and the exceptional first-coordinate mode.

For signed phases |gamma|+|delta|<=1/2 put
u=(j*pi+gamma)/n,v=(r*pi+delta)/m,P=(u+v)/2,T=(u-v)/2,Z=pi-P,
S=j+r,d=2n+1-S,g=|j-r+j/n|. Direct mesh geometry, with n>=1000,
gives

    P>=pi(S-1/6)/(2m), Z>=pi(d-1/6)/(2m),
    |T|>=pi(g-1/6)/(2m), 0<P<pi, |T|<8/5,
    |T|<=3Z/2, tau=m/n<=1001/1000.                (4)

Here S>=1,d>=1 on R. Positive differences have g>=1; negative
differences of size>=3 have g>=2; negative difference one has j<n/2,
hence g>1/2. Thus every regular denominator is separated. The phase
error in P,T is<=1/(4n), and its rescaling m/(2pi n)<1/6 follows
from3tau<pi. The upper T bound follows from pi/2+1/(4n)<8/5.
Also |T|-Z<=1/(2n) and Z>=5pi/(12m), giving |T|<7Z/5<3Z/2.
These are explicit lower-domain checks, not a transfer of C05's
theorem at n>=1000000.

The exact regular identity is

    F=a f-(sin gamma/2)g_u+(sin delta/2)g_v,
    f=(1+cos v)/(cos u-cos v),
    g_u=sin u/(cos u-cos v),g_v=sin v/(cos u-cos v).

C05's quarter-angle differentiation is valid under(4) and gives

    |f_ii|<=1/(2P|T|^3)+pi^2/(8P^3|T|)
       +pi^2/(8P^2 T^2)+1/(8P|T|)+pi^2/(32P^2)+3/Z^2+1,
                                                        i=u,v. (5)

For clarity its derivation uses
f=-1/2-[cot(P/2)cot(T/2)+tan(P/2)tan(T/2)]/4,
the chord bounds on P,Z, and |T|<=3Z/2. All of those hypotheses
were re-established in(4); no n-dependent discrete sum is transferred.

Rectangular symmetric differences commute with the invariant a in
the four copies. After(3), the regular f part is bounded by r2 times
2/(nm n^2) times the sum of(5). Its first three terms give exactly

    C_f=16tau^3 A1/pi^4+4tau^3(A2+A3)/pi^2.        (6)

Endpoint weights were omitted upward in these positive regular sums.
For the remaining four terms put H=1+log(2m). Counting at most2S
pairs for fixed S and4d for fixed d gives

    sum_R P^(-2)<=288m^2H/(25pi^2),
    sum_R Z^(-2)<=576m^2H/(25pi^2).

Also g-1/6>=1/6,sum_R(S-1/6)^(-1)<5m and#R<4n^2, so
sum_R(P|T|)^(-1)<120m^3/pi^2. The exact normalized majorant for
these terms is therefore at most the complete C_rem formula in
D02-corner-sums, without rounding a charge to1/100.

The sine-odd coordinate averages give normalized cost
r2/(2n^2m) sum_R(csc^2 T+csc^2 P). The elementary bounds

    csc^2 T<=(25/9)T^(-2),
    csc^2 P<=pi^2(P^(-2)+Z^(-2))/4

give exactly C_sine of D02-corner-sums. The first follows from
sin t/t>=3/5 on |t|<=8/5; the alternating sine polynomial through
t^7 proves it directly. The second is the sine chord on[0,pi].
Both channels and all initially zero regular cardinals are included.

Finally the new strip lemma gives the separate charge

    C_B=(14/5)[floor(n/2)+1/4]/m<7/5.              (7)

Every floor used for this strip, including its finite Fourier moments,
V derivatives, corrected F derivative, baseline and endpoint count,
is checked in that lemma on n>=1000. The old small-j estimate
(1-120/n)^(-2)<101/100 is not used; the new uniform reciprocal-sum
proof instead has a fixed32-row split valid at n>=10000.

## 2. Uniform bracket constant, not inferred from samples

Define the new fully charged allocation

    K_new=C_f+C_rem+C_sine+C_B-L/3.                (8)

For each cardinal sum_four F=4aF0+sum_four(F-aF0), with a>0.
Applying the triangle inequality only after this identity, (3)–(8)
and the separate sum theorem show lambda<=a Lambda_c+[L/3+K_new]r2.

To bound(8) uniformly, put t=(10001/10000)^3,p=9869/1000 and
f1=16t/p^2,f2=4t/p. The sum theorem gives

    K_new<= (f1*7427/4000-1/3)L
                  +f1*331/50+f2*949/100
                  +339/200+7/5+31/100000.          (9)

The coefficient of L is negative. Since L>46/5 for n>=10000,
the right side is bounded by its value with L=46/5. Direct rational
comparison gives that value<1943/250=7.772<39/5. Hence (1).
The small numerical headroom was not estimated from D01's table:
every constant and monotonic comparison in(9) is uniform in n.

## 3. Unrounded corner lower bound and strict comparison

Put ell=log n,kappa=gamma_E+log(8/pi), and

    A_n=(2/pi)(ell+kappa)
        =(2/pi)[L+kappa-log(1+1/n)].              (10)

The kappa shift in the L variable is retained exactly. C07's finite
paired deformation and PD-T270 give, for n>=10000,

    Lambda_c>=n/(n+1)*(A_n-1/(4n^2))^2+1/(n+1).   (11)

The subtracted one-dimensional error is not rounded to a constant;
the finite prefactor and endpoint term are kept. This is a supporting
lower bound already valid from their all-n statements, with positive
quantity inside the square on this domain.

For an elementary uniform comparison, kappa>3/2 as in C07 §2:
gamma_E>23/40 and log(8/pi)>37/40. Their proofs use respectively
H_10-log10-1/20 and the positive logarithm series with pi<22/7;
these degree-independent inequalities do not inherit a high n floor.
Also kappa<2, since gamma_E<1 and log(8/pi)<1, so A_n<=ell+2.
Expanding(11) and discarding only positive terms yields

    Lambda_c>=(2/5)(ell+3/2)^2-E(n)+1/(n+1),
    E(n)=(ell+2)^2/(n+1)+(ell+2)/(2n^2).          (12)

This retains the error as a degree-dependent expression; it does not
round a positive deformation d(n) to a heuristic limit. Both terms
in E(n) decrease for n>=10000. Since ell(10000)<10,

    E(n)<144/10001+6/100000000=:E0.               (13)

Cosine Taylor on the phase triangle gives1-a>=47r2/192. Moreover
L<=ell+1/n, and ell>=46/5 since log10>23/10. The latter elementary
logarithm inequality is proved by the positive series recalled in C07
§7. From(1),(12), the strict-loss coefficient is at least

    p(ell)-(47/192)E(n)-1/(3n),
    p(ell)=(47/480)(ell+3/2)^2-ell/3-39/5.

p increases on ell>=46/5, and p(46/5)=5501/16000. Thus the coefficient
is greater than

    5501/16000-(47/192)E0-1/30000>1/4.            (14)

This last comparison is rational. Combining it with1-a and(1)
proves(2). It covers the axes and every arbitrarily small positive
phase; the origin is included without division by r2. Reflection as
in(3) gives the parity-correct second patch.

## Scope, checks and history

This result supplies only the two actual inward corner patches.
Far/near noncorner comparisons and global localization remain separate.
It neither certifies a new finite global degree nor changes any old
C07/C13 quantifier, proof, model or correction. D01 remains a failed
trial for its old allocation. The n>=10000 theorem is a separate
quantitative candidate with an analytically changed strip charge.

Supplementary exact rational arithmetic and the permitted scalar
subtraction from D01 are recorded in the attempt; neither is a sampled
onset premise. Root-arranged distinct reconstruction is required before
accepting the new batch. Rules/input084a64f6465956f9c75b5538f83752c30318f151;
2026-11-06, Codex parent-assigned Sol xhigh, serving metadata unexposed.
