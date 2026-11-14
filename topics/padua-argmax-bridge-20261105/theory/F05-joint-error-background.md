# PD-T?argmax-bridge-codex-F05-joint-error-background — Signed background curvature at the first transport scale

ID kind: PD-T. Aliases: fixed-origin partial-cotangent curvature; joint
background/model logarithmic cancellation. Split from: F05 complete crossover.
Split into: none.

## Statement and definitions

Use EXACTLY E05-axis-central-excess's fixed-origin-sign background B_n and
M_nc=M_infty-E_c on beta=0. For EVERY integer n>=32 set m=n+1,h=pi/m,
L=log n,alpha=c*h with c in CLOSED[1/2,3/2]. Then

    |B_n(alpha)-B_n(0)-M_nc(alpha)+M_nc(0)
                               +(alpha^2/pi^2)L|<=2000h^2.       (1)

Both parities and actual corrected top mode ONE are retained. Exact real
arithmetic; no numerical premise. Overall status: **PROVED developer PAPER
support**, distinct review/root adoption required. This does not itself bound
the positive root excess or the complete error.

## Depends on

Accepted E05 gives B_n=1+(2n/m)a+(4/(nm))sum_(r=1)^n B_r,
a=(1+cos alpha)/2, B_r=-sum_(D_r^0)F_rk, with actual finite polynomial
F=(-1)^delta G/2. E06 proves B_n=P_n(cos(alpha/n)),deg P_n<=n and
PD-T227's local endpoint derivative functional. E08/E02's accepted full-domain
absolute error/norm bounds are used at their n>=32 scope, not C06's
n>=10^6 supremum theorem. E06's exact noncentral-model estimate gives
|C_nc(alpha)-C_nc(0)|<=19alpha^2 on alpha<=2/5, independently of n.
D16's COMPLETE absolute origin allowance is used, not an origin-sign premise.
The cotangent partial fraction and reciprocal C series are locally proved
PD-T270/N1/C08 facts; no external theorem is imported.

## Proof

### 1. An exact fixed-mask curvature, with no transported pole assignment

For r=1,...,n put q=n-r,nu_r=(1+r/m)/2,v_r=r*pi/m and

    T_r(z)=sum_(k=0)^(q-1)cot([pi(k+nu_r)+z/2]/n).

An empty sum is zero. The origin negative mask consists precisely of
j=r+1,r+3,...,2n-r-1. Reflecting this SAME finite mask sends its second
cotangent sum to minus T_r(-alpha). Thus the complete fixed-mask identity is

    B_r(alpha)=(a/2)cot(v_r/2)[T_r(alpha)+T_r(-alpha)]
                       -(sin alpha/4)[T_r(alpha)-T_r(-alpha)].  (2)

These fixed-mask samples stay away from a denominator pole for
|alpha|<=2/5: their first possible boundary crossing has phase magnitude
greater than pi. No formula is assigned to the transported j=r-1 sample,
which is OUTSIDE this mask. At r=n the mask and T_r are empty.

Differentiating the finite identity at zero gives

    B_n''(0)=-(Lambda_c-1)/2+R_n,
    R_n=(4/(nm))sum_(r=1)^n[cot(v_r/2)T_r''(0)-T_r'(0)].       (3)

Here B_n(0)=Lambda_c is the SAME actual finite corner. This step uses
neither a continuous model at a collision nor an asymptotic row value.

### 2. Uniform finite tails in the curvature functional

Let Z_j(v)=sum_(k>=0)(k+v)^(-j), and put
A3=28*zeta(3)/pi^4. Absolute convergence of the differentiated cotangent
partial fraction gives, with t_k=pi(k+nu_r)/n,

    T_r''(0)=n/(2pi^3) S3_r,
    -T_r'(0)=n/(2pi^2) S2_r,
    Sj_r=sum_(k=0)^(q-1)sum_(ell in Z)(k+nu_r+ell*n)^(-j).     (4)

For j=2 all terms are positive. The following elementary tail bounds include
q=0 and every r up to n:

    |S3_r-Z_3(nu_r)|<=12/(q+1)^2+5/r^2,  S2_r<8.             (5)

For clarity, the missing positive cubic tail is <=12/(q+1)^2, since
nu_r>=1/2. The image ell=-1 is bounded by sum_(j>=r)j^-3<=3/(2r^2).
The two more distant image tails together are <=3/n^2; these prove the
first assertion. For the square sum the principal positive part is
<=Z_2(1/2)=pi^2/2<5, the ell=-1 tail is <=2/r, and the two distant
tails together are <=4/n. Thus S2_r<8 at n>=32. These bounds use
disjoint subsets of the shifted integer lattice, not a count of crossings.

The cubic part of R_n is
(2/(m*pi^3))sum_r cot(r*pi/(2m))*S3_r. Its error from replacing S3_r
by Z_3(nu_r) is <3. Here is a fully uniform bound: the 5/r^2 term,
using cot x<=1/x and zeta(3)<3/2, costs <1. For the other term split
r<=m/2 and r>m/2. In the first range q+1>=m/2 and the bound is at most
192H_n/(m^2*pi^4)<1; in the second put s=q+1 and use
cot(r*pi/(2m))=tan(s*pi/(2m))<=pi*s/m, giving at most
24H_n/(m^2*pi^2)<1. H_n<=n is sufficient for these strict comparisons.

Next, Z_3(1/2)=7zeta(3),Z_4(1/2)=15zeta(4)<30, so
|Z_3(nu_r)-7zeta(3)|<=45r/m. This replacement costs <3.
The locally proved inequality0<=1/x-cot x<=pi*x/6 on[0,pi/2]
shows that replacing cot(r*pi/(2m)) by2m/(pi*r) costs <1.
Finally |H_n-log n|<=1 costs <1. Therefore the cubic part differs
from A3*L by <8. The square part of R_n is <2, by (4),(5):

    (2/(n^2*m))sum_r sum_(k=0)^(q-1)csc^2(t_k)<2n/m<2.

Consequently

    |R_n-A3*L|<10.                                           (6)

This is a finite uniform estimate, not merely the leading coefficient at a
fixed r. Both endpoint-distance and macroscopic r ranges are charged.

### 3. Actual origin, exact model curvature and their logarithms

The COMPLETE D16 absolute origin estimate implies

    Lambda_c=(4/pi^2)L^2+b_c*L+C_infty(0)+epsilon_n,
    |epsilon_n|<=E0(n)<10, |C_infty(0)|<4.                    (7)

These coarse constants need no new enclosure: in D16 write
E0=D+Mesh+G0+14/n+71/n^2. For n>=32, the explicit accepted formulas give
D<2,Mesh<1,G0<3,14/n<1,71/n^2<1. Use H/n<5/32,L/n<1/8,
r=log(5/2)+1/18<2; each of the four Mesh terms is <1/4. For the
constant, C_infty(0)=E_infty(0)+2Hfun(0)-c_const, with
0<E_infty(0)<3,0<Hfun(0)<1/2,0<c_const<1. This proves its stated
absolute bound. No limiting-to-finite sign promotion is used.

The unchanged full logarithmic coefficient on this axis is exactly

    b(alpha)=(4a/pi^2)[C(1/2+alpha/(2pi))+2log(2/pi)+log a]
                                                   +2alpha*sin alpha/pi^2.

Here C=-psi(t)-psi(1-t), C(1/2)=2gamma+4log2. Its reciprocal series gives
C'' with respect to alpha at zero equal to7zeta(3)/pi^2. Therefore

    b''(0)=-b_c/2+A3+2/pi^2.                              (8)

All factors are differentiated: the a*log a term contributes -2/pi^2,
and2alpha*sin alpha/pi^2 contributes +4/pi^2. In particular omitting
the latter would erase the decisive remaining logarithm.

Equations (3),(6),(7) imply the finite estimate

    |B_n''(0)+(2/pi^2)L^2-(-b_c/2+A3)L|<20.             (9)

### 4. Uniform Taylor remainders and the complete background/model difference

One may use ||P_n||_[-1,1]<=1000H^2 for EVERY n>=32. This is a deliberately
loose consequence of the accepted E08/E02 global norm, with every error
charge retained. To verify it without an endpoint evaluator, use
log m<=H,log(2m)<=2H,g<=2H,b<1/2,r<2 in E08(4).
Its D,Gg,retained,Mesh,W terms are respectively bounded by
30H,100H,398H,16H,4H, hence CEbar<600H. Also KD<9H.
The accepted full model/norm upper has leading4L^2/pi^2, linear coefficient
at most8/3 and constant at most8/3. Adding CEbar+2KD is <1000H^2.
Periodic phase reduction and the fixed-sign domination |B_n|<=S_n
give this bound for P_n on ALL[-1,1].

PD-T227's endpoint functional then yields, at |alpha|<=3/20,

    |B_n(alpha)-B_n(0)-(alpha^2/2)B_n''(0)|<=1000H^2 alpha^4.   (10)

Indeed n^2[1-cos(alpha/n)]<=alpha^2/2 and the derivative bounds sum
to the exponential Taylor remainder; the adjustment of the linear term
from cos(alpha/n)-1 to -alpha^2/(2n^2) costs still less. Its total
coefficient is below ||P_n||, since
1/24+exp(alpha^2/2)/8<1.

For the exact b in (8), its reciprocal series and elementary cosine/log
series give
|b(alpha)-b_c-(alpha^2/2)b''(0)|<=alpha^4 on this interval.
Explicit safe checks are |a-1+alpha^2/4|<=alpha^4/48,
|a log a+alpha^2/4|<=alpha^4/8,
|C-C(1/2)-(7zeta(3)/(2pi^2))alpha^2|<=alpha^4/10,
|alpha sin alpha-alpha^2|<=alpha^4/6, and
|C(1/2)+2log(2/pi)|<10. Substitution gives a coefficient below1.
The leading model coefficient has remainder <=alpha^4. E06's
|C_nc(alpha)-C_nc(0)|<=19alpha^2 consequently gives a model Taylor
error at most19alpha^2+(L^2+L)alpha^4.

Combine this with (8)--(10). The L^2 and A3 logarithms cancel and
the COMPLETE difference obeys

    |B_n(alpha)-B_n(0)-M_nc(alpha)+M_nc(0)
                       +(alpha^2/pi^2)L|
       <=29alpha^2+1002H^2 alpha^4<600alpha^2<=1350h^2.     (11)

Here alpha<=3h/2<3/20 and H^2*h^2<1/4, because pi^2<10 and
H/n<5/32. This proves (1) with the prospectively allocated2000 margin.
All estimates are uniform over the closed c interval and both parities.

## Scope, checks and history

This controls the signed smooth background against the SAME true noncentral
model; the transported roots, signed entire E_c and central cusp are separate.
No source/script/import/scalar/phase/degree/endpoint/native/quadrature/build/
pack job. Exact hand proof and owned prose only. The root gate/release and
emergent coefficient registration precede this complete proof; see
ideas/attempts F05-joint-error-crossover.md.2026-11-07, requested Sol xhigh,
serving metadata unexposed, supplied rules4a5de2012bad94601c713b2ff5517f2e3fb80af2.
Distinct audit/root adoption and the complete F05 target remain separate.


## Root disposition after distinct mathematical acceptance —2026-11-07

Root adopts the exact mathematical statement under its written quantifiers, hypotheses and dependencies. The original frozen proof/record prefix is preserved and identified in [independent review](../independent-checks-F04-F05.md), final SHA256ccdb1d774bd3653aadb26df3382be462043a5a7256bba2f41c909967fcf080f4. No global-onset change, new finite degree, source integration, strict runtime saving, novelty/priority verdict, protocol waiver or readiness follows beyond the exact statement. Final Claude review remains separate.
