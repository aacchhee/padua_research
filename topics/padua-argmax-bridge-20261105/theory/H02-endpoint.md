# PD-T?argmax-bridge-codex-H02-upper — Matched adjacent endpoint slice

ID kind: PD-T. Aliases: H02 upper adjacent-gap matching; two endpoint
scales of the signed deformation. Split from: supporting endpoint
obligation for the original OPEN PD-T098 sharp expansion. Split into:
none. This record does not assert the full sharp expansion.

## Statement

Use exactly PD-T159/269's f, angles and endpoint weights. For n>=2,
m=n+1, R=floor(n/2), define the actual upper adjacent-offset slice

    U_n=4/(nm) sum_(r=1)^R
      [f(pi*(n-r)/n,pi*(n-r+1)/m)
       -f(pi*(n-r)/n,pi*(n-r+1)/n)].

All weights on this slice are exactly one, including its k=n term.
There is an absolute constant C such that, for EVERY integer n>=2,

    U_n=C_U+[ (1+(-1)^n)/pi-1+4*log(2)/pi^2 ]/n+E_n,
    |E_n|<=C*log(n)/n^2,                                      (1)

where

    C_U=4 integral_0^(1/2) (1-t)*tan(pi*t/2)/(pi*t) dt.

The integrand at t=0 is its continuous value 1/2. The parity term in
(1) comes from the artificial halfway cut, not from a claim that the
complete deformation has a parity-dependent coefficient.

Also, for every fixed pair of distinct nonnegative integers j,k with
j+k odd, as n tends to infinity through integers larger than max(j,k),

    [f(pi*j/n,pi*k/m)-f(pi*j/n,pi*k/n)]/n
       ->8*sign(k-j)*k^2/[pi^2*(k^2-j^2)^2].                  (2)

In particular, at k=j+l (fixed positive odd l) the right side is
8(j+l)^2/[pi^2*l^2*(2j+l)^2], and at k=j-l>=0 it is
-8(j-l)^2/[pi^2*l^2*(2j-l)^2]. These are lower endpoint profiles;
they differ from simply extending PD-T269's bulk profile to j=0.

## Definitions and assumptions

Exact real arithmetic; the actual first-family Padua convention,
f(a,b)=(1+cos b)/abs(cos a-cos b), and its original weights. The
upper slice contains no polynomial collision. Its actual smallest
angular gap is pi/[n(n+1)], and no lower bound of order 1/n is used.
Natural logarithms. Big-O constants in the proof are absolute.

## Status by part

Overall status: **PROVED**, written developer supporting lemma, with
independent review still separate. Both (1) and (2) have complete
analytic proofs below. The complete PD-T098 target remains OPEN;
supporting endpoint lemmas do not give it PARTIAL status.

Candidate disposition: H02's complete summed-deformation target is
DEFERRED at this round's boundary. This proved slice is retained.

## Depends on

PD-T159/269 for the exact signed-deformation convention and original
endpoint weights. The calculations use elementary trigonometric
identities, Taylor's formula and the elementary trapezoid error estimate,
all developed below. No external theorem or numerical fit is a premise.

## Checks and sources

PAPER ONLY; zero executable/import/scalar/numerical/native/quadrature
jobs. This proof has no computational dependency. Required distinct
mathematical reconstruction is pending. Predecessor gate and literature
coverage limitations: ../campaign-H-gate.md. No new literature claim.

## Proof

### 1. Exact scaled adjacent term

Write q=1/n, t=r/n, c=pi/2, w=c*t, so q<=t<=1/2. Let A be the
actual f value in U_n and B its same-mesh reference. Upper endpoint
deficits give exactly

    A=sin^2(w/(1+q)) /
       [sin((2+q)*w/(1+q))*sin(q*w/(1+q))],
    B=sin^2(c*(t-q)) / [sin(c*(2*t-q))*sin(c*q)].       (3)

Define sinc(z)=sin(z)/z, sinc(0)=1. The FIRST expression satisfies

    q*A=G(t,q)
       =sinc^2(w/(1+q)) /
        [(2+q)*sinc((2+q)*w/(1+q))*sinc(q*w/(1+q))].   (4)

Thus G is smooth on the complete rectangle 0<=t,q<=1/2. Every sinc
argument lies in [0,pi/2], so no denominator vanishes. In particular
all its q derivatives through order two are bounded there, including
t=0. Put

    g(t)=tan(w)/(2*w), g(0)=1/2.

Taylor's formula applied to (4), followed by direct differentiation
for t>0 and continuity at t=0, gives

    q*A=g(t)+q*g(t)*(1-2*w*cot(w)+w*cot(2*w))+O(q^2).   (5)

The displayed products at t=0 have their continuous limiting values.

### 2. Reference term and the retained endpoint remainder

The exact identity

    q*B=(q/2)*tan(c*(t-q))
                   *[cot(c*q)-cot(c*(2*t-q))]          (6)

follows from cot(u)-cot(v)=sin(v-u)/(sin(u)*sin(v)). Its first
product is smooth on 0<=t,q<=1/2 and has expansion

    (q/2)*tan(c*(t-q))*cot(c*q)
      =tan(w)/(2*c)-(q/2)*sec^2(w)+O(q^2).             (7)

For the second product write u=t-q and v=2*t-q=t+u. On q<=t,

    M(t,q)=tan(c*u)*cot(c*v)
           =(u/v)*[tan(c*u)/(c*u)]*[c*v*cot(c*v)].      (8)

The bracketed factors extend smoothly to 0<=u<=1/2,0<=v<=1.
The derivative in q of u/v is -t/v^2, bounded in absolute value
by 1/t, because v>=t. All derivatives of the bracketed factors
needed here are bounded on that compact rectangle. Consequently

    M(t,q)=tan(w)*cot(2*w)+O(q/t)                     (9)

uniformly for q<=t<=1/2. Combining (6)--(9) proves

    q*B=tan(w)/(2*c)
          -(q/2)*[sec^2(w)+tan(w)*cot(2*w)]+O(q^2/t). (10)

The O(q^2/t) term is RETAINED; no Taylor expansion with a uniform
O(q^2) reference remainder has been asserted. It treats r=1 as well.

Subtract (10) from (5). The leading coefficient is
e(t)=(1-t)*g(t). The coefficient of q simplifies EXACTLY to g(t),
since tan(w)*cot(2*w)=(1-tan^2(w))/2. Hence uniformly

    q*(A-B)=e(t)+q*g(t)+O(q^2/t).                    (11)

This verifies the preregistered smallest-gap screen at r=1. Equation
(4), rather than an expansion dividing by that gap, supplies uniformity.

### 3. Sum before bounding the remainder

The original epsilon_(n-r) and eta_(n-r+1) both equal one for
1<=r<=R. In particular eta_n=1 at r=1; replacing it by the
same-mesh half weight would change the result. The exact normalization
and (11) give

    U_n=4*q sum_(r=1)^R e(r*q)
          +4*q^2 sum_(r=1)^R (r*q)*g(r*q)
          +O(q^2*H_R),                              (12)

where H_R=sum_(r=1)^R 1/r. To see the error directly, division by
1+q in 4*q/(1+q) times (11) replaces the first two coefficients by
e+q*(g-e); g-e=t*g. Its additional O(q^2) is absorbed in O(q^2/t).
Then q sum q^2/(r*q)=q^2 H_R. The estimate H_R<=1+log R makes
this O(log(n)/n^2), including the finitely many small n.

Both e and t*g are smooth on [0,1/2]. Integrating their Taylor
remainders on mesh cells proves the composite trapezoid estimate

    q sum_(r=1)^R e(r*q)
      =integral_0^T e(t)dt+(q/2)*(e(T)-e(0))+O(q^2),
    q sum_(r=1)^R (r*q)*g(r*q)
      =integral_0^T t*g(t)dt+O(q), T=R*q.            (13)

For completeness, on any mesh cell the error of the endpoint
trapezoid is bounded by its length cubed times a bound for the second
derivative, with an absolute constant; summing at most n cells gives
O(q^2). The second formula also follows by integrating the first
derivative bound. These estimates use no parity convention.

Write chi=0 for even n and chi=1 for odd n, so
T=1/2-chi*q/2. Taylor's formula at 1/2 in (12)--(13) gives

    U_n=4 integral_0^(1/2) e
       +q*[2*(1-chi)*e(1/2)-2*e(0)
                    +4 integral_0^(1/2) t*g(t)dt]
       +O(q^2*log n).

Finally e(0)=1/2, e(1/2)=1/pi, and
integral_0^(1/2) t*g(t)dt=log(2)/pi^2, by integrating tan(c*t)/pi.
Since 2*(1-chi)=1+(-1)^n, this is exactly (1).

### 4. Fixed-index lower endpoint layer

Fix j,k as in (2). With a=pi*j/n and b=pi*k/m, both angles tend
to zero. The elementary expansion at zero gives

    f(a,b)=4/[pi^2*abs(k^2/m^2-j^2/n^2)]+O_(j,k)(1).

Indeed expand the numerator and both sine factors in the exact identity

    f(a,b)=cos^2(b/2)/[sin((a+b)/2)*abs(sin((b-a)/2))].

The relative correction is O_(j,k)(n^-2), whereas the quadratic
fraction is O_(j,k)(n^2). The same estimate holds for the reference
mesh. Their two O(1) errors vanish after division by n. Thus the
coefficient of n in the difference comes entirely from the quadratic
fraction. Its exact difference, writing d=k^2-j^2, is

    4*n^2/pi^2 *[ (1+1/n)^2 /
             abs(k^2-j^2*(1+1/n)^2)-1/abs(d)].

For sufficiently large n the denominator sign is sign(d), since d
is nonzero. Differentiate this elementary rational expression at
1/n=0. The derivative is 2*sign(d)*k^2/d^2. Division by n proves
(2). If k=0 the original difference is exactly zero, agreeing with
the formula.

For fixed odd l and then large j, the two profiles in (2) have tails

    plus:   2/(pi^2*l^2)+2/(pi^2*l*j)+O_l(j^-2),
    minus: -2/(pi^2*l^2)+2/(pi^2*l*j)+O_l(j^-2).       (14)

These follow by expanding their explicit rational functions. In
contrast, PD-T269's fixed-t bulk profiles tend at t=0 to the first
constant in each line. Equation (2) thus identifies a second boundary
layer that cannot be omitted in a sharp summed argument. No uniformity
in l is claimed in (14).

## Scope and remaining obligation

Equation (1) completely controls the upper adjacent-offset slice at
the target summed remainder scale, with its actual endpoint weight.
Equation (2) identifies the lower endpoint correction responsible for
harmonic tails. Neither proves the full signed correction. To complete
H02's original target one still needs a single uniform estimate for
ALL odd offsets and the lower endpoint layer, including offsets of
order n, their missing-pair boundaries, and all remaining half weights.
Fixed-l versions of (14) may not be summed over l without that estimate.
The exact log^2(n)/n normalization charge remains in place.

## History

2026-11-07, requested/API Codex Sol ultra; serving metadata unexposed.
Rules/input 2c69ba538473b8fdd9147635256289f74e75ccbb. Root released
PAPER ONLY after ../campaign-H-gate.md. Prospective candidate and kill
test were recorded in ../ideas/H02-endpoint.md before derivation.
No Git, shared registry/log, new round or experiment by this worker.
