# PD-T?argmax-bridge-codex-C07-corner-02 — Strict actual-corner half diamonds from degree one million

ID kind: PD-T. Aliases: wider finite collision strip; exact Fourier
moments; actual-corner quadratic loss at n>=10^6. Split from: quantitative
continuation of C05-corner-01. Split into: the supporting corner-value
lower bound is C07-corner-01, in C07-corner-positive-deformation.md.

## Statement and status

Use exactly the corrected Padua cardinal polynomials, physical odd board
and actual-corner conventions in C02-corner-halfdiamond.md. For every
integer n>=10^6, set m=n+1, L=log m and

    z_n=(-cos(alpha/n),-cos(beta/m)),
    Lambda_c(n)=lambda_n(-1,-1),
    rho=alpha+beta, r2=alpha^2+beta^2,
    a=(cos alpha+cos beta)/2.

For every alpha,beta>=0 with rho<=1/2,

    lambda_n(z_n)<=a Lambda_c(n)+[L/3+16]r2,             (1)
    lambda_n(z_n)<=Lambda_c(n)-r2.                      (2)

The identical conclusions hold in inward phases at the other nonnode
corner. In particular both entire punctured inward half diamonds satisfy
lambda_n<Lambda_c, at every integer degree n>=10^6. The origin is
included in (1) and (2), with equality there in (2).

**PROVED**, complete analytic developer proof below. This does not assert
that every global maximizer lies in these corner patches. Global argmax
and the remaining degree/phase ranges are separate. No energy assumption,
per-cardinal sign stability, global norm equality, sampled coefficient,
numerical computation or approximation-model correction is used.
Distinct mathematical reconstruction and formal Claude audit are separate.

Dependencies: PD-T101/185 and C02 give the exact corrected polynomial and
four-copy normalization. C05-corner-quarterangle-bound.md gives its
numerator-sensitive regular derivative majorant and discrete sums;
their unchanged estimates are explicitly identified below. The enlarged
collision strip and every new numerical allocation are proved here.
C07-corner-positive-deformation.md supplies the corner lower bound for
(2). All C01–C05 proof bytes remain frozen. Gate: ../ideas/C07-corner.md.

## 1. Exact normalization and the enlarged split

Put N=nm, O={(j,r):0<=j<=n,0<=r<=m,j+r odd}. Endpoint weights e_j,f_r
are1/2 at their own mesh endpoints and1 otherwise. Define the finite
polynomials

    P_n=T_(n+1)+T_n,
    D_n(u,v)=[P_n(cos u)-P_n(cos v)]/[cos u-cos v],
    G_n(u,v)=D_n(u,v)-cos(nu),
    F_jr(gamma,delta)=(-1)^j G_n((j*pi+gamma)/n,(r*pi+delta)/m)/2.

The divided difference is its polynomial extension at collisions.
In particular the exceptional first-coordinate mode is retained.
C02, section1, proves the exact identities

    lambda_n=(1/N)sum_O e_j f_r |sum_four F_jr|,
    Lambda_c=(4/N)sum_O e_j f_r |F_jr(0,0)|.             (3)

The four copies use phases (+/-alpha,+/-beta), with multiplicities.
The absolute value is after their sum. Initial zero cardinals, repeated
copies, and the finite (n,m) endpoint are part of (3).

This time remove the larger family

    B={(j,r) in O:r=j+1,j>=n/2}, R=O minus B.           (4)

Every index in R belonged to C05's regular set. For signed phases
|gamma|+|delta|<=1/2, use its notation

    u=(j*pi+gamma)/n, v=(r*pi+delta)/m,
    P=(u+v)/2, T=(u-v)/2, Z=pi-P,
    S=j+r, d=2n+1-S, g=|j-r+j/n|, tau=m/n.

C05 section1 proves, on the entire signed phase rectangle,

    P>=pi(S-1/6)/(2m), Z>=pi(d-1/6)/(2m),
    |T|>=pi(g-1/6)/(2m),
    0<P<pi, |T|<8/5, |T|<=3Z/2, tau<=1001/1000.        (5)

These remain true on the smaller regular set R. Its only changed case
is r=j+1, where now j<n/2 and g=1-j/n>1/2. All denominators in
(5) are nonzero. The exact regular formula is

    F=a f-(sin gamma/2)g_u+(sin delta/2)g_v,
    f=(1+cos v)/(cos u-cos v),
    g_u=sin u/(cos u-cos v), g_v=sin v/(cos u-cos v).    (6)

## 2. Sharpen the one changed regular sum

The exact quarter-angle identity is

    f=-1/2-[cot(P/2)cot(T/2)+tan(P/2)tan(T/2)]/4.

C05 section2 differentiates this identity, preserving the vanishing
upper-end numerator, to give for i=u or v

    |f_ii|<=1/(2P|T|^3)+pi^2/(8P^3|T|)
      +pi^2/(8P^2 T^2)+1/(8P|T|)+pi^2/(32P^2)+3/Z^2+1. (7)

Define over the new R, with weights omitted upward,

    A1=sum 1/[(S-1/6)(g-1/6)^3],
    A2=sum 1/[(S-1/6)^3(g-1/6)],
    A3=sum 1/[(S-1/6)^2(g-1/6)^2].

The new bounds are

    A1<=(7581/4000)L+21, A2<6, A3<7.                  (8)

For A2,A3 the summands are positive and R is a subset of C05's set,
so its section3 bounds6 and7 carry over unchanged. For completeness,
the positive differences j-r=l>=1 cost less than13/5 and31/10,
respectively. Negative differences r-j=l>=3 cost less than1/10
and1/5. The negative l=1 class costs less than51/20 and31/10,
using its j<=100 and j>100 split. These total less than6 and7.

For A1 the positive differences and negative differences l>=3 have
the same C05 bounds, whose combined contribution is at most

    (33/16)(L/2+5/8)+89/40.                         (9)

Here the reciprocal odd sums used are
sum_(l odd>=1)(l-1/6)^(-3)<29/16,
sum_(l odd>=1)(l-1/6)^(-4)<21/10,
sum_(l odd>=3)(l-7/6)^(-3)<1/4 and the fourth-power sum<1/8;
each follows from its first term plus the spacing-two integral.
The row sum is at most1/q+L/2+5/8 for q=l-1/6 or l-7/6.

It remains to replace the negative l=1 estimate. Let q0=5/6 and
J be the largest nonnegative integer strictly below n/2. Its A1 sum
is bounded by

    sum_(j=0)^J (2j+q0)^(-1)(q0-j/n)^(-3).          (10)

The j=0 term is less than21/10. For j>=1 the constant part obtained
by replacing (q0-j/n)^(-3) with q0^(-3) costs at most
(108/125)(1+L). Put h(x)=(q0-x)^(-3). Since h' is increasing,

    sum_(j=1)^J [h(j/n)-h(0)]/(2j+q0)
       <=(1/(2n))sum_(j=1)^J h'(j/n)
       <=(1/2)integral_0^((J+1)/n) h'(x)dx<14.      (11)

Indeed q0-(J+1)/n>=1/3-1/n>=(999/1000)/3 and
27(1000/999)^3<28, so the last integral is at most
(28-216/125)/2<14. Consequently (10) is less than
(108/125)L+17. Adding (9) gives (8): the log coefficient is exactly
33/32+108/125=7581/4000, and the constant is less than21.

## 3. Normalize the regular coordinate second differences

Write Av for the average over the four signed phase copies. Since a
is constant on these copies, it factors out before taking a derivative.
Rectangular symmetric differences give

    |Av f-f0|<=alpha^2/(2n^2) sup|f_uu|
                        +beta^2/(2m^2) sup|f_vv|.

After (3), the regular f contribution to lambda_n-a Lambda_c is
therefore at most2r2/(Nn^2) times the sum of (7)'s majorant. By (5),
its first three terms have costs

    [16tau^3/pi^4]A1*r2<=[L/3+7/2]r2,
    [4tau^3/pi^2]A2*r2<=(5/2)r2,
    [4tau^3/pi^2]A3*r2<=3r2.                       (12)

For explicit rational checks, tau^3<101/100 and pi^2>197/20 give
16tau^3/pi^4<6464/38809 and4tau^3/pi^2<404/985.
The former times7581/4000 is less than1/3, and times21 is less
than7/2. The latter times6 and7 are less than5/2 and3.

The last four terms of (7) have the unchanged combined cost less
than r2/100 from C05 section4. To specify that bound completely,
put H2=1+log(2m). Counting fixed S and d gives

    sum P^(-2)<=288m^2 H2/(25pi^2),
    sum Z^(-2)<=576m^2 H2/(25pi^2),
    sum(P|T|)^(-1)<120m^3/pi^2, #R<4n^2.

These bounds on C05's larger set apply to the present R. The normalized
last-four-term coefficient is bounded by

    30m^2/(pi^2 n^3)+18m H2/(25n^3)
       +3456m H2/(25pi^2 n^3)+8/(nm)<1/100.         (13)

Use tau<1001/1000, pi>3, and the decreasing functions H2/n and
H2/n^2 on n>=10^6; at the endpoint H2<16. Thus the entire regular
f contribution is bounded by

    [L/3+7/2+5/2+3+1/100]r2=[L/3+901/100]r2.       (14)

## 4. The improved odd sine-channel budget

The exact cotangent identities give

    g_u=-(cot T+cot P)/2, g_v=-(cot T-cot P)/2,
    |partial_u g_u|,|partial_v g_v|
                              <=(csc^2 T+csc^2 P)/4.

Pair each sine-odd channel in its own coordinate before taking absolute
values. Since sin alpha<=alpha and sin beta<=beta, the normalized
cost of both channels in (6) is at most

    r2/(2n^2 m) sum_R(csc^2 T+csc^2 P).             (15)

Now the sharper strip cutoff gives

    sum_R(g-1/6)^(-2)<(9/2)m.                     (16)

Positive differences cost at most(51/25)m and negative differences
of size>=3 cost at most(69/121)m, as in C05. In the remaining class,
monotonicity and the same J as in (10) give

    sum_(j=0)^J(q0-j/n)^(-2)
      <=n integral_0^((J+1)/n)(q0-x)^(-2)dx
      <=n[3000/999-6/5]<(181/100)n.

Since51/25+69/121+181/100<9/2, this proves (16).
On |T|<=8/5, csc^2 T<=(25/9)T^(-2); therefore the T part of
(15) is less than25tau^2/pi^2 times r2, which is less than(8/3)r2.
For example tau^2<101/100 and pi^2>197/20 suffice. For the P part,
csc^2 P<=pi^2(P^(-2)+Z^(-2))/4 and the preceding sums give the
unchanged bound108m H2/(25n^2)<1/100. Both channels together thus
cost less than3r2. This includes every regular cardinal initially zero.

## 5. Exact Fourier moments on the enlarged finite family

For (j,r) in B put h=n-j, so0<=h<=n/2, and define

    x=(h*pi-gamma)/n, y=(h*pi-delta)/m,
    X=(x+y)/2, T_B=(x-y)/2.

C02 section5 gives the exact finite identity

    D_n=(-1)^n[V_n(X)U_m(T_B)+U_n(X)V_n(T_B)],
    U_k(z)=sin(kz)/sin z,
    V_n(z)=cos((n+1/2)z)/cos(z/2).                 (17)

It is an identity of finite trigonometric polynomials; U_k is evaluated
at sine zeros by its finite Fourier sum. For every real z,

    U_k(z)=sum_(r=0)^(k-1) exp(i(k-1-2r)z),
    |U_k|<=k,
    |U_k'|<=k^2/2,
    |U_k''|<=k(k^2-1)/3<=k^3/3.                  (18)

The first absolute frequency moment is k^2/2 for even k and(k^2-1)/2
for odd k; the second moment is exactly k(k^2-1)/3. These identities
follow by pairing positive and negative frequencies and summing the
first two powers. Thus (18) is uniform at every collision as well.

The signed phase geometry on B yields

    |X|<=pi/2+1/(4n)<8/5,
    |T_B|<=pi/(4m)+1/(4n)<8/5.                    (19)

For |z|<=8/5 put s(z)=sec(z/2). The elementary bounds
cos(z/2)>=17/25 and |tan(z/2)|<=6/5 imply

    |s|<=3/2, |s'|<=1, |s''|<=3/2.

Indeed use s'=s tan(z/2)/2 and
s''=s(tan^2(z/2)+sec^2(z/2))/4. With q=n+1/2, differentiating
V_n=s cos(qz) therefore gives, for n>=10^6,

    |V_n|<=3/2,
    |V_n'|<=3n/2+7/4<=(151/100)n,
    |V_n''|<=3n^2/2+7n/2+23/8<=(151/100)n^2.    (20)

Each first phase derivative of X or T_B has absolute value at most
1/(2n); their second phase derivatives vanish. Apply the product rule
to (17), using (18),(20). For either i,j in{gamma,delta},

    |D_n,ij| <=(n/4)[(151/100)tau+(151/100)tau^2
                                     +(1/2)tau^3+88/25]
              <(71/40)n.                         (21)

The first three terms are the costs of V_n(X)U_m(T_B). For the
second product the three coefficients are1/2,151/100,151/100,
whose sum is88/25. At tau<=1001/1000 the whole bracket is less
than71/10. The correction -cos(nu) has phase second derivatives
bounded by1. Hence the corrected F satisfies

    |F_jr,ij|<=(71/80)n+1/2<=(9/10)n.             (22)

We also need the finite baseline, with no sign assumption nearby:

    |F_jr(0,0)|<=n on B.                          (23)

At h=0 this is exactly F0=n by the polynomial endpoint value. For
h>=1 put x0=h*pi/n, y0=h*pi/m, X0=(x0+y0)/2 and T0=(x0-y0)/2.
Then0<X0<=pi/2 and0<T0<=pi/(4m). The exact baseline rational
formula is valid at these noncolliding points and gives

    F0=(1-cos y0)/(cos y0-cos x0)
       =sin^2(y0/2)/(sin X0 sin T0).

Use sin X0>=2X0/pi, sin T0>=(99/100)T0, and
sin(y0/2)<=y0/2. It follows that

    0<F0<=(50pi/99)*y0^2/(x0^2-y0^2)
          =50pi n^2/[99(2n+1)]<25pi n/99<n.

This proves (23); only the baseline, not its phase perturbations,
has been assigned a sign.

## 6. Charge the complete enlarged strip and assemble

For either signed direction (alpha0,beta0) with absolute phase sum rho,
put E(s)=F_jr(s alpha0,s beta0)-a(s alpha0,s beta0)F_jr(0,0).
Here E(0)=0. From (22),(23), and |a''(s)|<=rho^2/2,

    |E''(s)|<=(7/5)n rho^2, -1<=s<=1.             (24)

The two symmetric pairs in the fourfold sum each have Taylor integral
weight1. They therefore cost at most(14/5)n rho^2 per B index.
There are at most n/2+1 such indices. Dividing by N and bounding
endpoint weights upward by1 gives a total at most

    (14/5)(n/2+1)rho^2/m
       <=[14/5+28/(5n)]r2<3r2.                    (25)

This charges every index moved from the old regular set into B, as
well as the removable endpoint and all repeated copies.

For each physical odd index,
sum_four F=4aF0+sum_four(F-aF0). Since a>0, apply the triangle
inequality only after this identity, and use (3), (14), (15)–(16),
and (25). The result is

    lambda_n<=a Lambda_c+[L/3+901/100+3+3]r2
             <=a Lambda_c+[L/3+16]r2.

This proves (1) on the full closed triangle, including both axes
and the origin. No absolute error independent of r2 is present.

## 7. Strict comparison at every n>=10^6

Cosine Taylor on this triangle gives1-a>=47r2/192. By C07-corner-01,
with ell=log n,

    Lambda_c>=(2/5)(ell+3/2)^2-1/1000.

Since L<=ell+1 and ell>69/5 for n>=10^6, it follows that

    (47/192)Lambda_c-L/3-16
      >=p(ell):=(47/192)[(2/5)(ell+3/2)^2-1/1000]
                                             -(ell+1)/3-16>1. (26)

For a fully explicit check,
p(69/5)=381645/192000>1, and
p'(ell)=(47/240)(ell+3/2)-1/3>0 for ell>=69/5.
For an elementary check of log10>23/10, use
log10=3log2+log(5/4) and the positive geometric-integral expansions

    log10>6(1/3+1/81+1/1215+1/15309)+2/9>23/10.

Thus ell=6log10>69/5 at the left endpoint; larger n only increases
it. Combining (1) and (26) yields
lambda_n<=Lambda_c-r2, proving (2) and strictness whenever rho>0.

For even n, reflection in x permutes the original even-board cardinals
and their weights; for odd n, reflection in y does so because m is
even. C02 section6 proves that this is the second nonnode corner in
each parity, with the same inward phase magnitudes and same Lambda_c.
Thus (1),(2) transfer there without interchanging the exceptional mode.

## Checks, scope and history

All steps are analytic. No executable, phase sample, numerical integral,
energy extrapolation or fitted constant was used. The main improvement
over C05 is the exact Fourier moment budget for a wider finite collision
strip and the resulting reduction in its regular l=-1 sum. No frozen
C05 theorem is edited. The finite corner lower bound is split into its
own substantive result; it is not inferred from PD-T271's coarse rate.

This supplies an actual-corner predicate throughout the stated patches.
It does not by itself prove global argmax, cover smaller n, improve the
finite certified global range2–40, or establish the all-n energy target.
Independent review must check the changed split, uniform moments,
baseline endpoint, all numerical allocations and (26). The developer
does not self-approve this result or any global assembly using it.

2026-11-06, rules/input 4b728b04216a5490910780bc609a82b853058426.
Codex, coordinator-requested Astra ultra; serving metadata unexposed.
