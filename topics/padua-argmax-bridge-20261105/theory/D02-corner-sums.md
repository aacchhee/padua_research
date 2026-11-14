# PD-T?argmax-bridge-codex-D02-sums — Uniform reciprocal budgets above degree10000

ID kind: PD-T. Aliases: D02 A1 harmonic constant; exact one-offset
integrals; uniform sine envelope. Split from: supporting regular-sum
obligation for the D02 corner comparison. Split into: none.

## Statement and definitions

For every integer n>=N=10000 put m=n+1,L=log m,tau=m/n,q=5/6.
Use exactly the unweighted sums A1,A2,A3,G2,B20,C20 and complete
C_rem,C_sine definitions in D01's frozen SPEC. Thus the regular board
is the physical odd board minus B={(j,j+1):2j>=n}. Then

    A1<=(7427/4000)L+331/50,
    A2<219/50, A3<511/100,
    C_sine<339/200, C_rem<31/100000.                (1)

Overall status: **PROVED**, by the analytic reductions and explicit
rational/logarithmic comparisons below. No D01 measured value is a
premise. Distinct review is separate. The actual-function comparison,
its degree domain and its lower bound are in D02-corner-comparison.md.

Exact real arithmetic. The board and normalization do not change with
parity. No old C05 small-j comparison or old theorem below its degree
floor is used. This is a quantitative variant of C05/C07, not a
historical novelty claim.

## 1. Odd-offset series and elementary row bounds

Write k=|j-r|, always odd. Positive offsets j-r=k use j=t+k,
S-1/6=2t+b and g-1/6=b+(t+k)/n, b=k-1/6. Negative offsets r-j=k
use j=t,S-1/6=2t+b,g-1/6=b-t/n. The negative k=1 range is
0<=t<=J=floor((n-1)/2); negative k>=3 has t<=m-k<=n-2.

For k>=3 define

    Q_p=sum_(k odd>=3)(k-1/6)^(-p),
    R_p=sum_(k odd>=3)(k-7/6)^(-p).

The first three terms plus the decreasing spacing-two integral give

    Q_3<1/16,Q_4<19/1000,R_3<39/200,R_4<19/200.    (2)

Explicitly, for a=17/6 or11/6, the upper bound is
sum_(t=0)^2(a+2t)^(-p)+(a+4)^(1-p)/[2(p-1)]. These rational bounds
are respectively below the four constants in(2).

For b>0,p>1,

    sum_(t>=0)(2t+b)^(-p)
       <=b^(-p)+b^(1-p)/[2(p-1)].                 (3)

For b>=11/6 and an upper endpoint at most n, decreasing integral
comparison also gives

    sum_(t=0)^n(2t+b)^(-1)<=1/b+L/2+1/20.         (4)

Indeed its logarithm is at most log(1+2n/b)/2, and
(1+2n/b)/m<=1/10001+12/11<11/10<exp(1/10).

## 2. A1: retain the one-offset finite integral corrections

For k=1 put h=q^(-3)=216/125 and

    H8=sum_(t=0)^7(2t+q)^(-1),
    c=H8-log(95/6)/2,
    z=1/3-1/(2N), Y=2q^2/[z(q+1)]=500000/219967.

Convexity of x->1/(2x+q) shows that each unit-cell integral centered
at an integer bounds its value from above. Hence for K>=8,

    sum_(t=0)^K(2t+q)^(-1)
       <=H8+log[(2K+q+1)/(95/6)]/2.               (5)

For the negative one-offset class,2J+q+1<m; for the positive class
K=n-1,2K+q+1<2m. Thus their constant h parts together cost at most

    h L+h[2c+log2/2].                            (6)

The negative-class increment uses

    H_-(x)=[(q-x)^(-3)-q^(-3)]/x
           =q^(-1)/(q-x)^3+q^(-2)/(q-x)^2+q^(-3)/(q-x).

It is increasing. Since2t+q>=2t, right integral comparison bounds
its total increment by I_-=integral_0^(1/2+1/(2N))H_-(x)dx/2.
Its exact value is

    I_-=[(z^(-2)-q^(-2))/(2q)
              +(z^(-1)-q^(-1))/q^2+log(q/z)/q^3]/2.           (7)

For the positive class set
H_+(x)=[q^(-3)-(q+x)^(-3)]/x. It is positive and decreasing,
with H_+(0)=3q^(-4). Writing s=t+1, the denominator2t+q<=2s
shows that the decrease from the h part is at least

    I_+-3q^(-4)/(2N), I_+=integral_0^1 H_+(x)dx/2,
    I_+=[log((q+1)/q)/q^3
          +(q^(-1)-(q+1)^(-1))/q^2
          +(q^(-2)-(q+1)^(-2))/(2q)]/2.            (8)

For clarity, the right Riemann sum of a decreasing H_+ differs from
its integral by at most H_+(0)/n; this proves the direction and error
in(8). No favorable measured cancellation is assumed.

The remaining positive offsets use g-1/6>=b; negative offsets use
g-1/6>=b-1 and S-1/6>=2t+b-1. Equations(2),(4) bound their total by

    (Q_3+R_3)L/2+Q_4+R_4+(Q_3+R_3)/20.          (9)

Combining(6)–(9), the logarithmic coefficient is at most
216/125+(1/16+39/200)/2=7427/4000. The constant is below331/50.
Here is explicit arithmetic for that last comparison: combine its
logarithms into h[-log(95/6)+log Y/2]. Use

    log(95/6)>1381/500, log Y<411/500.             (10)

Writing R_- and R_+ for(7),(8) with their logarithmic parts deleted,
the remaining rational upper bound is

    2h H8+h[-1381/500+411/1000]+R_--R_+
      +3q^(-4)/(2N)+19/1000+19/200+(1/16+39/200)/20
          <331/50.                               (11)

For reproducibility,(10) follows from the positive series
T_K(x)=2 sum_(t=0)^(K-1) u^(2t+1)/(2t+1),u=(x-1)/(x+1), with

    T_K(x)<log x<T_K(x)+2u^(2K+1)/[(2K+1)(1-u^2)]

for x>1. K=40 for95/6 and K=8 forY suffice. Equations(10)–(11)
are finite rational comparisons; no floating logarithm is a premise.
This proves the A1 bound in(1).

## 3. A2 and A3: a fixed32-row split with uniform n floor

For (p,r)=(3,1) or(2,2), define the following rational numbers,
always with N=10000,M=32:

    P_pr=sum_(t=0)^M (2t+q)^(-p)q^(-r)
              +(2M+q)^(1-p)q^(-r)/[2(p-1)],
    V_pr=sum_(t=0)^M (2t+q)^(-p)(q-t/N)^(-r)
              +(2M+q)^(1-p)3^r/[2(p-1)],
    O_pr=[19/1000+1/(32(p-1))][1+(17/11)^r].       (12)

For the positive k=1 class, g-1/6>=q, so(3) bounds it by P_pr.
For negative k=1 and t<=32 use q-t/n>=q-t/N; for t>32 use
q-t/n>1/3 and the tail integral starting at32. This gives V_pr.
For other offsets,b/(b-1)<=17/11; applying(2),(3) gives O_pr.
Thus A2<=P_31+V_31+O_31 and A3<=P_22+V_22+O_22.

The individual finite rational comparisons are

| quantity | rational upper bound |
|---|---:|
|P_31|214557/100000|
|V_31|214569/100000|
|P_22|243706/100000|
|V_22|249564/100000|

Inserting these and O_pr from(12) gives respectively values below
219/50 and511/100, proving both bounds in(1). The fixed32 split avoids
the old failing(1-120/n)^(-2)<101/100 estimate. These are explicit
33-term rational inequalities, not an n-dependent finite-degree test.

## 4. Sine sums telescope across the odd offsets

The decreasing positive-offset integrand gives

    G2_positive/n
       <=sum_(k odd>=1)[1/b-1/(b+1)]
                         +(1/n)sum_(k odd>=1)b^(-2).

For negative k>=3, the exact upper index has(tmax+1)/n<1.
The increasing integral comparison therefore gives

    G2_negative,k>=3/n
       <=sum_(k odd>=3)[1/(b-1)-1/b].

The two displayed infinite series telescope jointly to1/q. The
negative k=1 sum is at most n[1/(q-1/2-1/(2n))-1/q]. Finally
sum_(k odd>=1)b^(-2)<51/25 by its first term plus integral. Hence

    G2/n<=1/(1/3-1/(2n))+51/(25n).                (13)

C07's endpoint inverse-square count, rederived from at most2S pairs
for fixed S and4d for fixed d, gives for H=1+log(2m)

    C_sine<=50tau/(9pi^2)[1/(1/3-1/(2n))+51/(25n)]
                                       +108tau H/(25n).       (14)

Every factor on the right decreases for n>=N, including H/n.
At N,H<11 and pi^2>9869/1000 give(14)<339/200. The same decreasing
ratios in the complete C_rem formula, evaluated at N with H<11 and
this pi bound, give C_rem<31/100000. These are rational checks.

For the elementary constants, exp10's positive series through degree15
exceeds20002, so H(N)<11. The identity
pi=16 arctan(1/5)-4 arctan(1/239), obtained by tangent addition,
and the alternating arctangent series give
pi>16[1/5-1/375+1/15625-1/546875]-4/239>31415/10000.
Its square exceeds9869/1000. This proves the remaining bounds in(1).

## Checks, scope and history

The proof contains all finite formulas and comparison thresholds.
Supplementary Python Fraction scalar checks of(2),(10)–(12),(14) and
the final budget are recorded in the D02 attempt; ordinary rational
comparisons here remain inspectable and do not use a measured kernel.
Root-arranged distinct reconstruction must check those constants.
No phase sample, lambda evaluation, full large board, new certificate,
old-proof edit or producer run occurred. D01's measured failures remain
unchanged. Rules/input084a64f6465956f9c75b5538f83752c30318f151;
2026-11-06, Codex parent-assigned Sol xhigh, serving metadata unexposed.
