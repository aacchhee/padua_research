# C02 — bounded-work partial cotangent sums and their all-row charge

Rules 4b728b0; 2026-11-06. Local C02 alias, technical reduction variant
of N2/N5/N1-01; no historical novelty claim. Preregistration and the full
current novelty gate are recorded in [ideas/C02-row.md](../ideas/C02-row.md).

**Status: PROVED analytic developer lemma.** This is a partial-sum theorem
and exact-real row reduction, not an implemented certifier. Independent
review is pending. Numerical roundoff, whole-box branch selection,
gradients and the final corner/defect interfaces remain OPEN as specified
below. No computation is a premise of the proof.

## 1. Statement and operation model

Let n>=2 be an integer, h=pi/n, and x_i=h(i+t), i=b,...,e, satisfy
0<x_b<=x_e<pi. Put q=e-b+1, L=x_b-h/2, R=x_e+h/2. Empty blocks have
sum zero. In particular [L,R] lies in [-pi/4,5pi/4]. Define

    w(x)=cot x-1/x+1/(pi-x),
    W(x)=log(sin x/[x(pi-x)]),       W'=w.

Both functions are defined by continuity at 0 and pi; the logarithm's
argument is positive on the entire stated interval. Their removable data
include W(0)=W(pi)=-log pi and w'(0)=w'(pi)=-1/3+1/pi^2.

For J>=1 let z=x/pi-1/2 and

    a_j=sum_(ell=1)^infinity (ell+1/2)^(-2j-2),
    P_J(x)=-(2/pi)*sum_(j=0)^J a_j*z^(2j+1).

The coefficients have the finite construction in section 2; an infinite
sum is not an implementation instruction. Define the corrected formula

    A_J(block)=(1/h)*[H(q,b+t)-H(q,n-e-t)]
       +sum_(i=b)^e P_J(x_i)
       +[W(R)-W(L)-integral_L^R P_J(x)dx]/h
       -(h/24)*[w'(R)-w'(L)-P_J'(R)+P_J'(L)],           (1)

where H(q,y)=sum_(i=0)^(q-1) 1/(y+i), y>0. The polynomial sum in
(1) is evaluated by a fixed-degree telescoping polynomial, not a loop
over q. Then

    |sum_(i=b)^e cot(x_i)-A_J(block)|
         <=(7*q*h^4/5760)*M_J,
    M_J=389120/(19683*pi^5)*(2J+3)^4*4^(-J).           (2)

Use the finite harmonic approximation H_(K,Lh) in section 3, with at most
K explicit reciprocal terms and Lh Euler–Maclaurin correction terms. If
its uniform absolute error is eta, the resulting Atilde satisfies

    |sum cot(x_i)-Atilde_J(block)|
         <=(7*q*h^4/5760)*M_J + 2*eta/h.               (3)

For fixed J,K,Lh this has a number of real arithmetic and elementary
function calls independent of n,q and proximity of a sample to a pole.
Integer bit lengths, floating-point precision and coefficient preparation
are counted separately. This is an arithmetic-operation statement;
it does not claim constant bit complexity for an unbounded input integer.

For the N1-01 full-diamond row problem, retain exactly the four rows
{0,2m-1,m-1,m}, m=n+1, and apply (3) to every other row using at most
12 blocks per cotangent channel. With a=(cos alpha+cos beta)/2 in [0,1],
the normalized analytic truncation error obeys

    E_n <= [7*pi^4*M_J/(2880*n^4)+48*eta/pi]
                        *[2+(4a/pi)*H_n].              (4)

This charges ALL approximated rows, not only four special rows. The
retained rows have zero analytic truncation error and require at most
4n bounded-work primitive evaluations using C01. Thus the exact-real
representation requires O(n) bounded-work row/block operations, plus
O(n) retained-point operations, for fixed J,K,Lh. It has not yet been
implemented with outward arithmetic or released for a cover.

The concrete choices J=96,K=64,Lh=32 have

    M_96<2^-165,      eta<2^-256,
    E_n<2^-166       for 2<=n<=2^64.                   (5)

These analytic inequalities are proved below; an optional exact rational
control may check them after this text. For any finite declared ceiling
N*, (4) can be made arbitrarily small with J,K,Lh depending on the target
accuracy and N*, not on a particular degree or block length. Formula (4)
does not give a fixed uniform absolute error at all unbounded n from a
fixed nonzero eta. No such claim is made.

## 2. Smooth residual, geometric tail and exact polynomial summation

The ordinary cotangent partial fraction, with the poles 0 and pi deleted,
is absolutely convergent in symmetric pairs on the compact cell domain.
Centering at pi/2 pairs the remaining poles at +/-pi(ell+1/2), ell>=1.
Consequently, for |z|<=3/4,

    w(x)=-(2/pi)*sum_(ell>=1) z/[(ell+1/2)^2-z^2]
        =-(2/pi)*sum_(j>=0) a_j*z^(2j+1).             (6)

The nearest remaining poles are at |z|=3/2; the geometric ratio is at
most 1/2 before taking even powers. Absolute uniform convergence of (6)
and its first four derivatives follows by the same geometric majorant.

A finite coefficient recipe avoids hidden zeta or harmonic sums. Let
t_0=1 and, for j>=1, set

    t_j=(1/(2j+1))*sum_(r=0)^(j-1) t_r*t_(j-1-r).

These rational numbers are the coefficients of tan s, by differentiating
tan s and comparing coefficients in tan'=1+tan^2 near zero. The identity

    w(pi(1/2+z))=-tan(pi*z)+(2z/pi)/(1/4-z^2)

therefore gives the coefficient of z^(2j+1) as

    b_j=2^(2j+3)/pi-t_j*pi^(2j+1)=-(2/pi)*a_j.        (7)

Although the tangent series alone has radius 1/2 in z, its local Taylor
coefficients in (7) agree with (6); analytic identity fixes those
coefficients. Formula (6), rather than the uncancelled tangent series,
proves convergence on |z|<=3/4. Coefficient construction takes O(J^2)
scalar operations once, independent of n. Cancellation in (7) must be
resolved with outward precision or an independently validated coefficient
method; treating inaccurate coefficients as exact is not permitted.

For j>=1, comparison with an integral gives

    a_j <=(3/2)^(-2j-2)*[1+(3/2)/(2j+1)]
         <=2*(3/2)^(-2j-2).

For J>=1, differentiate the tail in (6) four times and bound its falling
factorial by (2j+1)^4. Since |z|<=3/4,

    ||(w-P_J)''''||_infinity
       <=1024/(243*pi^5)*sum_(j>=J+1) (2j+1)^4*4^(-j).

Writing j=J+1+s, use 2j+1<= (2J+3)(s+1) and

    sum_(s>=0) (s+1)^4/4^s=1520/81.

This proves the bound M_J in (2), including the constants. The first two
odd monomials cause no issue because their fourth derivatives vanish.

For any polynomial P of degree d, there is a polynomial B of degree
at most d+1 satisfying B(t+1)-B(t)=P(h(t+t0)). Its coefficients are
obtained successively from the highest power downward, dividing the
leading coefficient by the relevant positive integer. Hence

    sum_(i=b)^e P(h(i+t0))=B(e+1)-B(b).              (8)

This requires fixed-degree polynomial preparation/evaluation, not q
iterations. Equivalently one can use the ordinary Bernoulli polynomial
power-sum identity, with its chosen B_1 convention made explicit.
The integral and derivative of P are likewise finite polynomials.
Large endpoint cancellation in (8) is a numerical-conditioning obligation,
not a mathematical source of additional truncation error.

N5's corrected midpoint functional on a single centered cell has error
at most (7*h^4/5760)*sup|f''''|. Apply it to f=w-P_J, add the polynomial
sum (8), and retain the two pole terms exactly. The pole decomposition is

    cot x=1/x-1/(pi-x)+w(x),

and reversing the second positive progression gives exactly the H
difference in (1). Summing the disjoint cell error bounds proves (2).
In particular the error is proportional to q, not the number of blocks.

## 3. A uniform finite shifted-harmonic formula

Let K>=1,Lh>=1 be integers. For q<=K evaluate H directly (including
H(0,y)=0). For q>K put x=y+K, z=y+q and set

    H_(K,Lh)(q,y)=sum_(i=0)^(K-1) 1/(y+i)
       +log(z/x)+(1/(2x)-1/(2z))
       +sum_(r=1)^Lh [B_(2r)/(2r)]*(x^(-2r)-z^(-2r)). (9)

The Bernoulli numbers here are rational coefficients of t/(exp t-1);
they can be prepared once with finite rational arithmetic. Formula (9)
has no digamma call or hidden harmonic loop. Every potentially tiny
initial denominator is included explicitly in the prefix.

Euler–Maclaurin for f(t)=1/t on [x,z], with the endpoint convention
sum_(i=0)^(q-K-1) f(x+i), has integral log(z/x), endpoint term
(f(x)-f(z))/2 and the corrections displayed in (9). Its periodic
Bernoulli remainder obeys

    |remainder| <= [sup_(t in [0,1])|B_(2Lh)(t)|/(2Lh)!]
                              *integral_x^z |f^(2Lh)(t)|dt
       <= |B_(2Lh)|/(2Lh)*(x^(-2Lh)-z^(-2Lh)).        (10)

For completeness the Bernoulli supremum inequality used in (10) follows
from the absolutely convergent Fourier series

    B_(2s)(t)=(-1)^(s+1)*[2(2s)!/(2pi)^(2s)]
                    *sum_(k>=1) cos(2pi*k*t)/k^(2s).

Taking absolute values gives the endpoint value |B_(2s)|. Integrating
|f^(2s)|=(2s)!/t^(2s+1) gives precisely (10). This proof also works
for s=1 by its convergent Fourier series. Since x>K, a uniform bound is

    eta_(K,Lh)=|B_(2Lh)|/[(2Lh)*K^(2Lh)].             (11)

It is independent of q,y and remains valid as y tends to zero, because
only the explicitly retained prefix then grows. Exact q<=K cases have
zero tail error. Applying (11) to the two positive harmonic sums proves
(3). For fixed Lh, increasing K decreases (11) to zero; more efficiently,
K=2Lh and the elementary bounds zeta(2Lh)<2, pi>3 give

    eta_(2Lh,Lh)<4*(2Lh-1)!/[6^(2Lh)*(2Lh)^(2Lh)]
                   <=2/[Lh*36^Lh].                 (12)

Thus arbitrary analytic accuracy has a finite explicit degree-independent
prefix/order for every declared target. Choosing Lh=32,K=64 and retaining
the sharper factorial in (12) gives eta<2^-256. The rational comparison
is `4*63!*2^256 < 6^64*64^64`.

## 4. Exact and guarded arc-to-integer block selection

Use separate phase evenness from N2/N1; work on alpha,beta>=0,
alpha+beta<=pi. In row r define delta=(1-r) mod 2 and

    sigma=frac[(delta*pi+alpha)/(2pi)],
    u_k=2pi*(k+sigma)/n,             0<=k<n.

This relabels the same circular row even at the exceptional sigma=0
endpoint. Put v=(r*pi+beta)/m, A=cos alpha+cos beta, p=sin alpha,
qphase=sin beta, and c=A(1+cos v)+qphase*sin v. N2's exact negative
regular set is the symmetric difference of

    D={cos u<cos v},       I={p*sin u>c}.              (13)

D is the arc (v*,2pi-v*), v*=min(v,2pi-v); I is the elementary sine
superlevel set. For p>0, c/p>=1 makes I empty, c/p<-1 makes it full,
and c/p=-1 makes it the circle with the single equality point removed.
For -1<c/p<1 use the two sine roots and the strict inequality. At c/p=1
I is empty. For p=0, I is full if c<0 and empty if c>=0. If p=c=0,
every regular numerator is exactly zero, so it is excluded, regardless
of a formal symmetric-difference membership. All equality points are
handled as numerator zeros or collisions by the finite polynomial.

There are at most four distinct D/I boundary points on the circle.
On every intervening open arc the sign is fixed by (13). For an open
selected arc (a,b) in [0,2pi], its grid points are exactly

    k_low=max(0, floor[n*a/(2pi)-sigma]+1),
    k_high=min(n-1, ceil[n*b/(2pi)-sigma]-1).          (14)

If k_low>k_high the block is empty. No grid scan is present. The circle
cut u=0 is treated once as a separate possible grid sample; strict-zero
and collision points are excluded from the cotangent blocks. Each channel
x=(u+/-v)/2 modulo pi has at most one additional wrap inside (0,2pi).
Its wrap gives a single additional split, and its exact zero is a grid
collision. Thus a conservative 12 contiguous blocks per channel covers
the circle cut, tangent/coincident boundaries and every excluded point.
For a chosen block the integer wrap is constant, and x=h(k+t) satisfies
the exact hypotheses of sections 1–3. The two positive H arguments are
k_low+t and n-k_high-t; they must be strictly positive.

Formula (14) is exact-real mathematics, not permission to round a floor
without a guard. A validated alternative is as follows. Supply disjoint
outward enclosures for the distinct boundary points (coincident points
are merged), each of angular width less than one grid spacing, with
certified arc labels on their complement. Select only the definitely
negative open cores, using the upper enclosure endpoint for a left
boundary and the lower one for a right boundary in (14). A boundary
enclosure contains at most one grid point. Put all such unresolved samples
and the possible seam sample u=0 into a direct set B; it has at most five
members. Exact collisions occur at D boundaries and are therefore in B;
if collision coordinates are supplied directly they are merged, never
double counted. The negative cores remain a union of a bounded number
of intervals; channel wraps still give fewer than 12 blocks.

For B evaluate the finite polynomial F and add 2*max(-F,0) to the signed
row. This avoids deciding whether an unresolved boundary sample is a
zero, a collision, positive or negative. The complement of the cores and
B is certified nonnegative. Hence the exact row decomposition is

    R_r=T_r-2*C_r*sum_core cot((u-v)/2)
             -2*D_r*sum_core cot((u+v)/2)
             +2*sum_(k in B) max(-F_rk,0),            (15)

with any known collision outside B explicitly merged into B. In exact
selection, B instead consists of the seam sample and at most two exact
collisions; exact numerator zeros contribute zero. Interval max is a
valid enclosure even when its argument straddles zero. No `0*infinity`
substitution is made in any formula. Positive H arguments and reduced
block range (0,pi) are mandatory guards.

The boundary enclosure hypothesis in this outward construction is
substantive. It is sufficient for a bounded inner-work evaluator; it is
not proved for arbitrary phase boxes. Overlapping endpoint enclosures
can instead be merged if their union still contains only a bounded
number of grid samples. A wide unresolved branch must use a proved
fallback, split/refine its phase box, or report failure. It cannot silently
round to one arc. Exact degenerate p=c=0 and the stated full/empty cases
are mathematical branches, not numerical smallness tests.

## 5. Row assembly, global error and scope

Use N1-01's normalization F=(-1)^delta G_n/2, S=(nm)^-1 sum|F|,
coefficients C=(p-qphase-A*cot(v/2))/4,
D=(p+qphase+A*cot(v/2))/4 and signed row
T=n*[a-(qphase/2)*cot(v/2)]. This fixes the factor of two in (15).
The finite polynomial defines every retained point and collision.

Retain rows 0,2m-1,m-1,m exactly by n direct evaluations each. These
include every possible v in pi*Z on the closed phase triangle: v=0 or
2pi can occur only in the endpoint rows; v=pi occurs at r=m or m-1
when beta=0 or pi. No singular coefficient is evaluated there.
For the remaining rows the cotangent coefficients are finite. The N1-01
bound, applied to any subset of interior rows, gives

    sum_r (|C_r|+|D_r|)<=m*[2+(4a/pi)*H_n].           (16)

Indeed |C|+|D|<=1+a|cot(v/2)|, and the distance of an interior v from
{0,2pi} is at least pi*min(r,2m-r-1)/m; the integers 1,...,n occur
twice. Direct sets B add O(n) primitive evaluations in total and no
analytic truncation error. Their points are excluded from both channels,
so each remaining channel has at most n samples and at most 12 blocks.

Summing (3) over disjoint blocks gives per channel

    error <= 7*n*h^4*M_J/5760+24*eta/h.

Equation (15) multiplies this by 2(|C|+|D|). Sum (16), divide by nm,
and use h=pi/n. This proves (4), without a block-count multiplier on
the smooth sample-count term and with the full 12-block multiplier on
the harmonic tail. In particular N1-15's four-special-row H8 charge
has not been reused.

For all n>=2 use H_n<=n, pi>3, pi<4, a<=1. The smooth prefactor in
(4) is less than M_J/5: the decreasing expression
(2+(4/3)n)/n^4 is at most 7/24, and
(7*4^4/2880)*(7/24)<1/5. Also

    M_96 < [389120/(19683*3^5)]*195^4*4^-96 <2^-165.

For n<=2^64, H_n<=1+log n<65, so the harmonic coefficient in (4)
is at most 16*[2+(4/3)*65]<2^11. Together with eta<2^-256 this
gives E_n<2^-167+2^-245<2^-166, proving (5).

For a general finite ceiling N*, replace 65 by 1+log N* and choose
J and Lh (with K=2Lh) until the two explicit terms in (4) fit the
requested accuracy. The limits M_J->0 and (12)->0 prove termination
of this order selection. The resulting arithmetic count is independent
of the degree within that declared range. Actual outward arithmetic
also needs enough precision for endpoint subtraction, coefficients,
power sums and the weighted final sum. Its interval error is added to
(4); it is not absorbed into the analytic tail.

## 6. Obligations before a full certifier

* Implement and review a validated partial-sum backend with no hidden
  q-sized loop; freeze coefficient identities, precision and guards.
* Implement certified endpoint-to-integer conversion and the bounded
  direct set B. Provide a total, recorded fallback when endpoint balls
  cover too many grid samples. Whole-box phases can move a boundary
  through many indices; the pointwise O(n) representation alone does
  not provide an O(n) whole-box interval enclosure.
* Enclose W and w' at their removable points with stable outward series
  or a reviewed library routine; direct interval subtraction of divergent
  terms is not a removable-point definition.
* Supply phase-gradient/mean-value bounds appropriate to the production
  box test. Differentiating a moving selected block without its boundary
  terms is invalid, and a uniform value error does not bound its gradient.
  One option is to retain the C01 gradient backend while accelerating
  only point values; that is an implementation tradeoff, not this theorem.
* Preserve the odd-board parity, factor 1/2, separate phase evenness,
  exceptional coefficient and exact collision convention when assembling
  corner orbits. Do not introduce an x/y mesh exchange symmetry.
* Show the final whole-box upper bound and defect comparison spend the
  complete value, arithmetic, gradient and symmetry budgets exactly once.

Until those interfaces and distinct review close, the **supporting
partial-sum lemma is PROVED; the production row certifier is OPEN**.
