# PD-T?argmax-bridge-codex-J02 — Elementary enclosure of the consumed model constants

ID kind: PD-T. Aliases: elementary PD-T271 replacement; K3 rational
kappa enclosure. Split from: none. Split into: none. This proves only
the inequalities actually consumed by the location argument.

## Statement, definitions and status

Let gamma be Euler's constant and let the analytic corner constant be

    kappa=(8/pi) integral_0^1 t^2*cot(pi*t/2)
                   sum_(ell odd>=1) 1/[ell*(ell^2-t^2)] dt.

Both endpoint values mean the continuous limits of the combined
integrand. With

    c1=2*(gamma+log(8/pi))/pi,
    Cstar=c1^2+kappa,
    C0=2gamma+4log2, k0=C0-2logpi,
    d0=C0*(C0-7/2)/pi^2,
    g0=4*(log(pi)^2-log(2)^2)/pi^2,
    H0=kappa/2-(2k0/pi^2)*log(pi/2),
    j=H0+d0-g0, t0=2log2/pi,

one has

    kappa>9/10, j>23/250, 0<t0<221/500,
    Cstar<4629/2500=1.8516.                              (1)

Consequently the existing analytic correlated model inequality
C_infinity-Cstar<=-j*u+t0*sin x, with
u=1-(cos x+cos y)/2, implies C_infinity<9/4 on the closed phase
triangle x,y>=0,x+y<=pi. No upper bound kappa<23/25, no upper bound
on H0, and no computational PD-T271 premise is asserted or consumed.
An upper interval for the finite kappa sum is used internally to bound
Cstar, as required by its positive dependence on kappa.

Initial status, before the registered calculation: **CONDITIONAL** on
the finite rational comparisons implemented in `check.py`. Complete
analytic reductions and proofs of its elementary brackets follow.
Execution and distinct independent review are recorded by dated
addenda; the old Arb values are not premises.

## Depends on and scope

The identification of the integral with the corner constant, and
Cstar=c1^2+kappa, are the analytic corner-limit and actual-origin
identities (PD-T269/270; paper `eq:main-kappa`, `uc:origin-identity`).
The model identity H0 and the correlated loss are the analytic E06/E07
map, proved by the scalar maximum with its cusp. These are exact
identities, not decimal inputs. This record supplies their consumed
numerical inequalities by elementary rational estimates.

Only the elementary cotangent partial fraction is inherited from the
paper's row calculus. Its use in the finite reduction is explicitly
derived below. There is no external special-function library,
Bernoulli table, numerical quadrature or finite Padua evaluator premise.

## 1. The endpoint-cancelled series and an analytic tail

For 0<=t<1 write

    ap=1-2 sum_(r=1)^p zeta(2r)/4^r, a0=1,
    b0=7*zeta(3)/8,
    bq=(1-2^(-2q-3))*zeta(2q+3)
                     -(1-2^(-2q-1))*zeta(2q+1), q>=1,
    ck=sum_(p+q=k) ap*bq.

The cotangent partial fraction

    cot(pi*t/2)=2/(pi*t)-(4t/pi)sum_(r>=1)1/(4r^2-t^2)

and 2sum_(r>=1)1/(4r^2-1)=1 give

    t^2*cot(pi*t/2)/(1-t^2)=(2t/pi)sum_(p>=0)ap*t^(2p).

In fact the same telescoping sum shows

    ap=2sum_(r>=1)(4r^2)^(-p)/(4r^2-1),
    0<ap<=4^(-p).                                       (2)

Expanding the odd reciprocal sum and multiplying by 1-t^2 cancels
its ell=1 pole, and gives

    (1-t^2)sum_(ell odd>=1)1/[ell*(ell^2-t^2)]
                         =sum_(q>=0)bq*t^(2q).

Here zeta(3)<5/4 follows directly from
1+1/8+integral_2^infinity s^(-3)ds=5/4, with strict inequality.
Hence b0<35/32<10/9. For q>=1,

    |bq|=sum_(ell odd>=3)(ell^2-1)/ell^(2q+3)
       <9^(-(q-1))*sum_(ell>=3)ell^(-3)
       <=9^(-(q-1))*(1/27+integral_3^infinity s^(-3)ds)
       <9^(-q).                                         (3)

Thus |ck|<4^(-k)*(10/9+sum_(q>=1)(4/9)^q)<2*4^(-k).
The series are absolutely and uniformly convergent on [0,1]; the
endpoint-cancelled product and its termwise integral are therefore
legitimate. Substitution into the integral yields

    kappa=(8/pi^2)sum_(k>=0)ck/(k+1),
    |kappa-(8/pi^2)sum_(k=0)^K ck/(k+1)|
           <8/[3*(K+2)*4^(K+1)].                         (4)

For the tail use 8/pi^2<1 and sum_(k>=K+1)4^(-k)=4^(-K)/3.
At the prospectively fixed K=3 the radius is 1/480. This is an
analytic remainder bound, not an estimate obtained by comparing two
numerical truncations.

## 2. Rational brackets with elementary proofs

Every bracket in the checker comes from the following finite formulas.
No decimal is accepted without a rational inequality producing it.

**Pi.** Integrating the finite geometric series for 1/(1+s^2) gives
the alternating expansion atan(z)=sum_(k>=0)(-1)^k*z^(2k+1)/(2k+1)
for 0<z<1, with the value between consecutive partial sums. Take 40
terms for z=1/5 and z=1/239, and form

    pi=16atan(1/5)-4atan(1/239).                          (5)

For completeness tan(4atan(1/5))=120/119, and subtraction of
atan(1/239) gives tangent one: both numerator and denominator reduce
to 28561/(119*239). The angle is positive and <4/5, hence lies
in (0,pi/2), so it equals pi/4. The elementary bound
pi=4integral_0^1(1+s^2)^(-1)ds>8/3 suffices for that angle range.
Therefore (5), with the alternating brackets, is exact. The checker
also verifies the coarse comparisons 157/50<pi<22/7 and
197/20<pi^2<10 used below.

**Logarithms.** For rational 1<=z<=2, x=(z-1)/(z+1) belongs to [0,1/3].
Integrating 2/(1-x^2) and expanding its positive geometric series gives

    S48(z)=2sum_(k=0)^47 x^(2k+1)/(2k+1),
    S48(z)<=log z<=S48(z)+2*x^97/[97*(1-x^2)].            (6)

For any positive rational z write z=2^e*w, 1<=w<2, and use
log z=e*log2+log w. For z<1 use log z=-log(1/z). Monotonicity
evaluates an interval at its two rational endpoints. This proves
every logarithm bracket, including logs of pi and the nested logs in
the J01 allowances. The algorithm uses rational arithmetic only.

**Euler's constant.** Put H_M=sum_(k=1)^M 1/k. The elementary sequences

    H_M-log(M+1)<gamma<H_M-log(M+1/2)                    (7)

increase and decrease respectively to gamma. The first difference is
1/(M+1)-log(1+1/(M+1))>0. For the second use
log((M+3/2)/(M+1/2))=2atanh(1/(2M+2))>1/(M+1).
Both limits equal the definition lim(H_M-log M); existence follows
also from the usual integral comparison of the harmonic sums.
Use M=256 and (6). In particular (7) proves the needed coarse
23/40<gamma<3/5; no pretabulated digits of gamma enter.

**All zeta values.** For every s>1 and rational m=10 put

    Zs=sum_(k=1)^10 k^(-s),
    Zs+1/[(s-1)*10^(s-1)]-1/[2*10^s]
          <=zeta(s)<=Zs+2^(s-1)/[(s-1)*21^(s-1)].        (8)

The function f(t)=t^(-s) is convex. Its trapezoid rule on
[10,infinity) bounds the integral from above by f(10)/2 plus the
tail sum, giving the lower bracket. The midpoint rule on the cells
[k-1/2,k+1/2], k>=11, bounds each f(k) by its cell integral,
giving the upper bracket. Infinite limits follow by monotone
convergence, or finite sums followed by f(t)->0. This argument treats
the even values zeta(2),zeta(4),zeta(6) and the odd values
zeta(3),zeta(5),zeta(7),zeta(9) uniformly. Thus even the familiar
special-value formulas are unnecessary trusted inputs.

**Trigonometric base for J01.** The alternating sine and cosine series
at 1/2 have decreasing terms. The checker uses consecutive partial
sums ending at powers 23 and 22 respectively, each preceded by the
previous same-parity sum. The integral/Taylor remainder or the
alternating-series proof bounds the exact values between them.
For the far gate it uses sin(pi/4)=cos(pi/4)=1/sqrt(2), upper-bounded
by 707107/10^6 after squaring positive numbers. No transcendental
function is evaluated by binary floating-point.

## 3. The finite reduction and rational arithmetic model

Let I_pi be (5), I_gamma be (7), and let I_s be (8) for exactly
s=2,3,4,5,6,7,9. Form intervals I_ap,I_bq by their displayed
definitions, then

    I_kappa=(8/I_pi^2)*sum_(k=0)^3
                      [sum_(p=0)^k I_ap*I_b(k-p)]/(k+1)
                         +[-1/480,1/480],
    I_Cstar=4*(I_gamma+3I_log2-I_logpi)^2/I_pi^2+I_kappa.

All input counts, cutoffs and comparisons were registered before
execution. The only consumed checks are

    lower(I_kappa)>9/10, upper(I_Cstar)<4629/2500,
    gamma in (23/40,3/5), log2 in (69/100,6932/10000),
    logpi<23/20, 161/100<k0<9/5,
    log(pi/2)<23/50, t0<221/500,
    157/50<pi<22/7, 197/20<pi^2<10.                   (9)

The checker rounds every interval endpoint outward to the rational
grid 2^(-128), by floor at the lower end and ceiling at the upper end.
Addition, multiplication (all four endpoint products), negation and
division by an interval excluding zero preserve inclusion. Positive
integer powers are iterated products. Every denominator is checked
for the required sign. These rules give a straightforward induction
that the returned intervals contain the exact expressions. The
six-place receipt is also rounded outward with integer division;
decimal strings have no mathematical role in the assertions.

## 4. Derive the consumed constants and close the global constant bound

From (9), C0>39/10 and C0-7/2>2/5. Therefore
d0>(39/10)*(2/5)/10=39/250. The exact origin identity, (1)'s
kappa lower bound and (9) give

    H0>9/20-(2*(9/5)/(197/20))*(23/50)
       =9/20-828/4925>7/25.

Also

    g0<(80/197)*[(23/20)^2-(69/100)^2]<43/125.

These are rational cross-multiplications. It follows that
j>7/25+39/250-43/125=23/250. Positivity of log2 gives t0>0,
and (9) gives its stated upper bound. No H0 upper bound is needed.

Since u>=(1-cos x)/2, the correlated model bound implies

    C_infinity<=Cstar-j/2+sqrt(j^2/4+t0^2).

Let delta=9/4-Cstar. From (9), delta>249/625>0 and

    (249/625)^2+(249/625)*(23/250)-(221/500)^2
                              =71/6250000>0.             (10)

Hence delta^2+delta*j>t0^2. Squaring the positive quantities
delta+j/2 and sqrt(j^2/4+t0^2) proves C_infinity<9/4. In
particular the weaker Cstar threshold 1.8516, rather than a
needlessly precise historical decimal, suffices for every consumer.

## Checks, limitations and history

The source is [check.py](../code/onset512_analytic/check.py); its exact
command and prospective kill rule are in
[PREREGISTRATION](../code/onset512_analytic/PREREGISTRATION.md).
The source is intentionally independent of the repository's old
Arb evaluator and exact-rational prototypes; it uses only the
standard-library Fraction and integer arithmetic. The conceptual
series is inherited from the paper and the approved audit architecture.

Runs needed at initial write: the registered developer execution,
its short receipt, and a distinct mathematical review with an actual
independent execution. The computation is a finite elementary
inequality check, not a degree search, certificate run, or precision
campaign. Existing PD-T271 and frozen E01--E15 records are not edited;
root removes their manuscript dependency only after distinct review.

2026-11-08: assigned Codex mathematical developer, requested Sol xhigh,
actual serving metadata unexposed; rules/source
`b45e29fa1fe3dbfa2517ff8043e5d9c440870530`. The approved existing
series/enclosure mechanism has no new novelty content. Preregistration
and this proof preceded every new calculation in this scope.

### Developer execution addendum — 2026-11-08

The single registered standard-library Fraction command passed every
assertion, exit 0, Python 3.12.14, observed wall time 0.16123836 seconds.
The [receipt](../code/onset512_analytic/receipt.json) pins its source and
preregistration. Its six-place outward intervals are kappa in
[0.917166,0.921489] and Cstar in [1.841232,1.847940]. The latter's broad
lower endpoint comes from the deliberately elementary gamma lower
bound and is unconsumed. All comparisons (9) passed. Unlike the audit
prototype, even zeta values also use (8), with no special-value table.

The exact finite obligations are discharged. Independent execution and
mathematical review remain pending before root adoption; the initial
CONDITIONAL status is historical and awaits that independent execution.
There was no failed assertion, revised cutoff, fallback or extra run.

### Current status after distinct review — 2026-11-08

**PROVED** for the consumed inequalities (1) and the stated consequence
C_infinity<9/4. The distinct Astra xhigh reviewer reconstructed the series,
tails and elementary brackets and independently executed the frozen Fraction
checker, exit 0. Its
[review](../independent-checks-onset512-response.md#analytic-gates-and-elementary-constants--accepted-at-the-written-scope)
pins the reviewed sources. PD-T271 remains a preserved historical result;
these inequalities supply a separate elementary replacement for its use in
the revised manuscript. The next substantive Claude audit is still required.
