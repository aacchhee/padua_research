# PD-T?argmax-bridge-codex-C05-corner-01 — A sharp logarithmic allocation for the actual reflected corner

ID kind: PD-T. Aliases: quarter-angle numerator-preserving bound; exact
regular separation sum; actual-corner onset exp(25). Split from: C02's
full-half-diamond corner comparison. Split into: none.

## Statement and status

Use precisely the corrected Padua cardinals and actual-corner conventions
of C02-corner-halfdiamond.md. For every integer n>=10^6, put m=n+1,
L=log m, rho=alpha+beta, r2=alpha²+beta² and
a=(cos alpha+cos beta)/2. Throughout alpha,beta>=0, rho<=1/2,

    lambda_n(-cos(alpha/n),-cos(beta/m))
                  <=a Lambda_c(n)+[L/3+38]r2.          (1)

The same estimate holds at the other parity-correct nonnode corner.
Consequently the entire punctured inward half diamond satisfies
lambda_n<Lambda_c at both corners for every integer n with log n>=25.
This is an actual-corner patch threshold, not a global argmax onset.
Strict comparison throughout this patch for every n>=10^6 remains OPEN.

**PROVED**, analytic developer helper. The proof keeps the four reflected
copies inside each cardinal absolute value. It uses no sign stability,
global norm equality, energy assumption, sampled coefficient, numerical
computation or model correction. Independent supplementary reconstruction
and formal Claude audit are separate. Gate, candidate and allocations:
../ideas/C05-corner.md. All C01–C04 and C02-corner sources are unchanged.

## 1. Exact reflection and regular geometry

Write N=nm, O={(j,r):0<=j<=n,0<=r<=m,j+r odd}, with endpoint half
weights e_j,f_r. Let

    F_jr(gamma,delta)=(-1)^j G_n((j*pi+gamma)/n,(r*pi+delta)/m)/2,

where G_n is the corrected finite polynomial. PD-T228 and C02 give the
exact identities, including the removable endpoint and repeated copies,

    lambda_n=(1/N)sum_O e_j f_r |sum_four F_jr|,
    Lambda_c=(4/N)sum_O e_j f_r |F_jr(0,0)|.           (2)

Remove B={(j,r):r=j+1,j>=2n/3} and set R=O minus B. At every signed
phase |gamma|+|delta|<=1/2, put

    u=(j*pi+gamma)/n, v=(r*pi+delta)/m,
    P=(u+v)/2, T=(u-v)/2, Z=pi-P,
    S=j+r, d=2n+1-S, g=|j-r+j/n|, tau=m/n.

On R, S,d>=1 and tau<=1001/1000. Directly from the two mesh spacings,

    P>=pi(S-1/6)/(2m), Z>=pi(d-1/6)/(2m),
    |T|>=pi(g-1/6)/(2m), 0<P<pi, |T|<8/5.           (3)

For example the phase error in P and T is at most1/(4n), and its
rescaled value m/(2pi n)<1/6. The base lower bounds for P and Z are
pi*S/(2m) and pi*d/(2m). For T the base value is exactly pi*g/(2m).
If j-r>=1 then g>=j-r; if r-j>=3 then g>=r-j-1; if r=j+1 in R,
then j<2n/3 and g=1-j/n>1/3. Thus every T denominator in (3) is
nonzero. The upper bound on |T| follows from the square and the
phase overshoot pi/2+1/(4n)<8/5.

An additional useful bound is |T|<=3Z/2. Indeed |T|-Z is at most
the largest overshoot of u or v above pi, hence at most1/(2n).
But Z>=5pi/(12m), so that overshoot is less than(2/5)Z. These
arguments cover mesh endpoints and all signed phases of the rectangle.

The exact regular formula is

    F=a f-(sin gamma/2)g_u+(sin delta/2)g_v,
    f=(1+cos v)/(cos u-cos v),
    g_u=sin u/(cos u-cos v), g_v=sin v/(cos u-cos v).  (4)

No absolute value has yet been moved inside its reflected orbit.

## 2. Numerator-sensitive second derivatives

The elementary identity

    f=-1/2-[cot(P/2)cot(T/2)+tan(P/2)tan(T/2)]/4      (5)

follows by writing cos v=cos P cos T+sin P sin T. It keeps the
vanishing upper-end numerator that a bound by |sin P|^-1 loses.

For X(P)=cot(P/2), Y(T)=cot(T/2), the sine chord and cot x<=1/x give

    |X|<=2/P, |X'|<=pi²/(2P²), |X''|<=pi²/P³,
    |Y|<=2/|T|, |Y'|<=2/T²+1/2,
    |Y''|<=4/|T|³+1/|T|.

For the Y bounds use csc²x<=x^-2+1 for |x|<=4/5. This follows from
sin x>=x(1-x²/6), since
(1+x²)(1-x²/6)²-1=x²(24-11x²+x^4)/36>=0 there.
Put U(P)=tan(P/2)=cot(Z/2), V(T)=tan(T/2). Then

    |U|<=2/Z, |U'|<=pi²/(2Z²), |U''|<=pi²/Z³,
    |V|<=|T|, |V'|<=2, |V''|<=2|T|.

The latter three follow from |T|/2<=4/5 and cos(T/2)>=17/25.
Using |T|<=3Z/2, the second-derivative contribution of UV in (5)
is bounded by 3/Z²+1. Since each u or v derivative changes P and
T by absolute value1/2, differentiation of (5) gives, for i=u or v,

    |f_ii| <=1/(2P|T|³)+pi²/(8P³|T|)
       +pi²/(8P²T²)+1/(8P|T|)+pi²/(32P²)+3/Z²+1.   (6)

This bound is uniform over the complete signed phase rectangle in (3).

## 3. Three discrete sums with the exact diagonal separation

All sums in this section are over R; endpoint weights may be dropped
upward. Define

    A1=sum 1/[(S-1/6)(g-1/6)³],
    A2=sum 1/[(S-1/6)³(g-1/6)],
    A3=sum 1/[(S-1/6)²(g-1/6)²].

We prove the numerical bounds

    A1 <=(7581/4000)L+115, A2<6, A3<7.               (7)

Let l=|j-r|, always odd. For the positive differences j-r=l>=1,
write j=r+l, so S=2r+l and g>=l. Put q=l-1/6. Integral comparison
for the decreasing functions (2x+q)^-p gives

    sum_(r=0)^m 1/(2r+q)
       <=1/q+(1/2)log(1+2m/q)<=1/q+L/2+5/8,
    sum_(r>=0) 1/(2r+q)^p
       <=q^-p+q^(1-p)/[2(p-1)], p>1.               (8)

For l=1,3,5,..., let Q_s=sum q^-s. Separating l=1 and comparing
the remaining series with its integral gives

    Q_3<29/16, Q_4<21/10.

For example Q_3<=216/125+216/4913+9/289<29/16, and
Q_4<=1296/625+1296/83521+36/4913<21/10. The tails starting at
l=3 obey Q_3,tail<2/25 and Q_4,tail<3/125.

For negative differences r-j=l>=3, g=l-j/n>=l-1. Put h=l-7/6.
Then S-1/6=2j+h+1>=2j+h. The two analogous series satisfy

    sum h^-3<=216/1331+9/121<1/4,
    sum h^-4<=1296/14641+36/1331<1/8.                (9)

Equations (8)–(9) bound the combined positive-l and negative-l>=3
contribution to A1 by

    (33/16)(L/2+5/8)+89/40.

For the remaining negative difference l=1, let q0=5/6 and
J be the largest nonnegative integer strictly below2n/3. Its A1 sum
is at most

    sum_(j=0)^J (2j+q0)^-1(q0-j/n)^-3.              (10)

The j=0 term is q0^-4<21/10. For j>=1, split (q0-j/n)^-3 into
q0^-3 plus its increment. The constant part costs at most
(108/125)(1+L). For f(x)=(q0-x)^-3, monotonicity of f' gives

    sum_(j=1)^J [f(j/n)-f(0)]/(2j+q0)
       <=(1/(2n))sum_(j=1)^J f'(j/n)
       <=(1/2)integral_0^((J+1)/n) f'(x)dx<108.

Indeed q0-(J+1)/n>=1/6-1/n>=(999/1000)/6 and
216(1000/999)^3<217; subtracting q0^-3 in that last integral gives
the stated108. Thus (10) is below(108/125)L+111. Combining it with
the previous classes proves the A1 inequality in (7).

For A2,A3 in the l=1 negative class split at j=100. On j<=100,
(q0-j/n)^-s<= (101/100)q0^-s for s=1,2 and n>=10^6. On j>100
use (q0-j/n)^-1<=6 and 2j+q0>=2j. Equation (8) and tail integrals
therefore give

    A2_(negative,l=1)
       <=(101/100)[1296/625+54/125]+3/80000<51/20,
    A3_(negative,l=1)
       <=(101/100)[1296/625+108/125]+9/100<31/10.

The positive classes cost Q_4+Q_3/4<13/5 for A2 and
Q_4+Q_3/2<31/10 for A3. For negative l>=3, with q=l-1/6,
q/(q-1)<=17/11<8/5. Multiplying the positive tail bounds respectively
by8/5 and(8/5)² gives costs below1/10 and1/5. Consequently
A2<13/5+51/20+1/10<6 and A3<31/10+31/10+1/5<7. This completes (7).

## 4. Rectangular reflection and normalized regular budgets

Denote the average of the four reflected copies by Av. Since a is
unchanged by either reflection, it factors out exactly. The rectangular
second-difference identity, applied one coordinate at a time, gives

    |Av f-f0|<=alpha²/(2n²) sup|f_uu|
                           +beta²/(2m²) sup|f_vv|.

Thus its contribution to lambda_n-a Lambda_c, after (2), is at most
(2r2/(Nn²)) times the sum of the right side of (6). No derivative
of a along a phase path is needed or charged.

By (3), the first term of (6) contributes at most

    [16tau³/pi^4]A1*r2 <=[L/3+20]r2.                (11)

To check both coefficients, tau³<101/100 and pi²>197/20 give
16tau³/pi^4<6464/38809. Its product with7581/4000 is below1/3,
and its product with115 is below20. The second and third terms
contribute respectively

    [4tau³/pi²]A2*r2<=(5/2)r2,
    [4tau³/pi²]A3*r2<=3r2,                          (12)

because 4tau³/pi²<404/985 and (7) holds.

Here are explicit harmless bounds for the remaining terms, so they are
not hidden in an O constant. Write H2=1+log(2m). For a fixed S the
number of board pairs is at most2S, and for fixed d it is at most4d.
Equation (3) implies

    sum P^-2 <=288m² H2/(25pi²),
    sum Z^-2 <=576m² H2/(25pi²).

Also g-1/6>=1/6, and sum(S-1/6)^-1<5m, so
sum(P|T|)^-1<120m³/pi². There are fewer than4n² board pairs.
After multiplication by2/(Nn²), the last four terms of (6) together
are bounded by

    30m²/(pi²n³)
       +18m H2/(25n³)
       +3456m H2/(25pi²n³)+8/(nm)<1/100.           (13)

For the last elementary comparison use tau<1001/1000,
pi>3, and the monotonicity of (1+log(2n+2))/n and its n^-2
counterpart on n>=10^6; at that endpoint H2<16. Thus the entire
regular f contribution is at most[L/3+20+5/2+3+1/100]r2.

## 5. Odd sine-channel averages

Direct cotangent identities give

    g_u=-(cot T+cot P)/2, g_v=-(cot T-cot P)/2,
    |partial_u g_u|,|partial_v g_v|
                          <=[csc²T+csc²P]/4.

The odd reflected average in the first channel is bounded by
(alpha/n) sup|partial_u g_u|, and similarly in the second channel.
Since sin alpha<=alpha and sin beta<=beta, their combined normalized
cost in (2) is at most

    r2/(2n²m) sum_R [csc²T+csc²P].                  (14)

On |T|<=8/5 the sine chord used in C02 gives
csc²T<=(25/9)T^-2. We claim

    sum_R (g-1/6)^-2 <(15/2)m.                     (15)

The positive differences cost at most m*(51/25), by
sum_(l odd>=1)(l-1/6)^-2<=36/25+3/5. Negative l>=3 cost at most
m*(69/121), by the analogous first-term-plus-integral bound at11/6.
The negative l=1 sum is at most

    n integral_0^((J+1)/n) (5/6-x)^-2 dx
       <=n[6000/999-6/5]<(481/100)n.

The three constants total less than15/2, proving (15). Its contribution
to (14) is less than

    [125tau²/(3pi²)]r2<=(9/2)r2.

Finally csc²P<=pi²(P^-2+Z^-2)/4. The preceding sums bound this part
of (14) by108m H2/(25n²)<1/100. Therefore both sine channels together
cost at most5r2. This estimate handles their reflected cancellations
directly, including cardinals initially equal to zero.

## 6. Count the finite polynomial collision family and assemble

C02 proves on exactly B and this signed half diamond, using its finite
U/V factorization of the corrected polynomial, that

    |partial_i partial_j F_jr|<=4n, |F_jr(0,0)|<=2n.

For clarity the factorization is
D_n=(-1)^n[V_n(X)U_m(T_B)+U_n(X)V_n(T_B)], with
U_k=sin(kz)/sin z understood as its finite Fourier sum and
V_n=cos((2n+1)z/2)/cos(z/2). On this B family |X|,|T_B|<1.1;
its bounds |U_k^(q)|<=k^(q+1), |V_n|<=5/4,
|V_n'|<=2n, |V_n''|<=3n² give the displayed phase derivatives.
Thus this is a finite polynomial bound also at h=0 and at every collision.

For E(s)=F_jr(s alpha,s beta)-a(s alpha,s beta)F_jr(0,0), one has
|E''(s)|<=5n rho². The two symmetric pairs in the fourfold sum cost
at most10n rho² per index. There are at most n/3+1 such indices,
so the B contribution after normalization is at most

    10(n/3+1)rho²/m <=(20/3+20/n)r2<=(27/4)r2.       (16)

All endpoint weights and repeated copies were retained in (2); replacing
weights by one only enlarges this bound. In particular the finite value
at (n,m) is included rather than assigned a rational pole value.

For every index, sum_four F=4aF0+sum_four(F-aF0). Since a>=15/16,
the triangle inequality after this identity, and (11)–(16), give

    lambda_n<=a Lambda_c
       +[L/3+20+5/2+3+1/100+5+27/4]r2
       <=a Lambda_c+[L/3+38]r2.

This proves (1), including the axes and origin. No primitive fractional
term appears because the reflections were combined before absolute values.

## 7. Explicit strict-patch onset

On this phase triangle, N1-16's elementary cosine bound gives
1-a>=47r2/192. PD-T157 gives Lambda_c>=(4/pi²)log²n-54.
For ell=log n>=25, pi²<10 and log(n+1)<=ell+1 imply

    (47/192)Lambda_c-[log(n+1)/3+38]
       >=(47/192)[(2/5)ell²-54]-(ell+1)/3-38>0.

The final polynomial has value21/16 at ell=25 and derivative at least
73/16 on ell>=25. Thus (1) is strictly less than Lambda_c whenever
r2>0, including every arbitrarily small positive inward phase. The onset
ceil(exp(25)) is above10^6 and hence lies in (1)'s proved domain.

The node-preserving x reflection for even n, or y reflection for odd n,
permutes corrected cardinals and endpoint weights and transfers (1) and
the same strict threshold to the other nonnode corner. This is exactly
the parity convention of PD-T228; no mesh interchange is used.

## Remaining sharper target and history

The fixed constant38, mostly the deliberately coarse l=-1 tail and the
polynomial B family, does not fit the desired n>=10^6 strict-comparison
budget. Improving that allocation remains useful. The theorem already
reduces the explicit full-patch logarithmic threshold from610000 to25,
with an r2 factor that handles the origin uniformly. A global conclusion
still requires the independently established complementary comparison.

No executable or mathematical diagnostic was run. Every integer/rational
comparison above is part of the analytic proof, not an empirical receipt.
2026-11-06, rules/input 4b728b04216a5490910780bc609a82b853058426.
Codex, parent-requested Astra ultra; serving metadata unexposed. Only
coordinator-authorized new C05-corner records were written.
