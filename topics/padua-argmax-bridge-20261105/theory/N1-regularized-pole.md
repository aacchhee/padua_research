# PD-T?argmax-bridge-codex-N1-04 — All-integer regularized pole profile

ID kind: PD-T. Aliases: single-pole norm expansion; odd-cell cusp
correction; uniform regularized shifted cotangent profile.
Split from: N1 full-diamond compactification, still OPEN. Split into: none.

## Statement and definitions

Let n>=2 be an integer and 0<t<1. Define

    B_n(t)=sum_{k=0}^{n-1}|cot(pi*(k+t)/n)|,
    C(t)=2gamma+1/t+1/(1-t)
          +sum_{k=1}^infinity[1/(k+t)+1/(k+1-t)-2/k],
    Phi_L(t)=(sin(pi*t)/pi)*[2L+C(t)-2log pi].

The constant C is exactly the absolutely convergent series in PD-T365,
and gamma=lim(H_j-log j). Then

    |B_n(t)/n-[2log n+C(t)-2log pi]/pi| <=5/n^2.       (1)

Define F_n(t)=sin(pi*t)*B_n(t)/n for 0<t<1. Both F_n and Phi_L extend
continuously with value 1 at t=0,1; extend them periodically to the real
line. For every real t,

    |F_n(t)-Phi_(log n)(t)|
       <=5*|sin(pi*t)|/n^2 <=5/n^2.                    (2)

There is no parity restriction. In addition the periodic Phi_0 obeys

    sup |Phi_0| <=4,       Lip(Phi_0)<=12.              (3)

The Lipschitz bound is with respect to ordinary real distance, so it also
handles a segment crossing an integer offset. These bounds regularize a
pole coefficient times its norm; they do not assign a value to an actual
Padua polynomial collision row.

## Status, assumptions and dependencies

Overall status: **PROVED**, analytic developer proof; distinct review
pending. Exact real arithmetic, with no fit or computational premise.
PD-T365 supplies the elementary uniform harmonic tail estimate proved in
its section 3, and PD-T270 supplies the locally proved bound
|(cot x-1/x)''|<1 for 0<=x<=pi/2. Their full proofs were read. The cusp
treatment and the explicit periodic bounds are proved below. No external
source theorem is imported. Candidate: ../ideas/N1-endpoint.md.

## Proof

### 1. Both endpoint poles and the central cusp

Put h=pi/n and A=pi/2. Define on (0,pi)

    b(x)=|cot x|-1/x-1/(pi-x).

It extends continuously with b(0)=b(pi)=-1/pi, is symmetric about A,
and direct integration gives integral_0^pi b(x) dx=-2log pi.
For example, integrate from epsilon to pi-epsilon and let epsilon->0:
the two terms are -2log(sin epsilon) and
2log((pi-epsilon)/epsilon), respectively.

For x<A, b(x)=(cot x-1/x)-1/(pi-x). T270 and reflection therefore give

    |b''(x)|<=1+16/pi^3<2,       x!=A.

At A the one-sided derivatives of b are -1 and 1. Consequently

    b_tilde(x)=b(x)-|x-A|

is C^1 with globally Lipschitz derivative and second derivative bounded
in magnitude by 2 almost everywhere. The endpoint extensions have the
same regularity. Taylor's integral remainder with this bound is valid
even on a cell crossing A.

On each cell [kh,(k+1)h], the paired samples at relative locations t and
1-t and the cell average have identical constant and linear Taylor
terms about its midpoint. If |f''|<=M, their difference is bounded by

    M*h^2/8+M*h^2/24=M*h^2/6.

Apply this to b_tilde with M=2. For |x-A|, all cells are linear if n is
even, so their error is zero. If n is odd, only the central cell fails
to be linear. There the paired-sample average minus cell average is

    h*(|t-1/2|-1/4),

whose magnitude is at most h/4. Since b(pi-x)=b(x), its two global
shifted sample sums are identical. Summing the paired estimates gives

    |(1/n)*sum_k b(h*(k+t))-(1/pi)*integral_0^pi b|
       <=pi^2/(3n^2)+pi/(4n^2).                        (4)

This includes the odd-n zero/cusp crossing without omitting its error.

### 2. Harmonic part and endpoint limits

Writing H_n(t)=sum_{k=0}^{n-1}1/(k+t), T365's exact tail identity is

    H_n(t)+H_n(1-t)-2log n-C(t)
      =sum_{k=n}^infinity
         [2log(1+1/k)-1/(k+t)-1/(k+1-t)].

Convexity and midpoint/trapezoid error bounds for 1/x on [k,k+1]
bound the summand in magnitude by 1/(3k^3). Thus its tail is at most
1/(6n^2)+1/(3n^3)<=1/(2n^2), uniformly in t. The contribution of both
endpoint poles to B_n(t)/n is exactly [H_n(t)+H_n(1-t)]/pi.
Together with (4) and the integral of b, this gives (1), since

    pi^2/3+pi/4+1/(2pi)<5.

Multiplication by sin(pi t) proves (2) for 0<t<1. At t->0 the k=0
cotangent term alone gives F_n->1; at t->1 the k=n-1 term does so.
The series for C gives sin(pi t)C(t)/pi->1 at either end. The other
terms of Phi_L vanish in those limits. Continuity and periodicity give
the claimed extension and its exact zero endpoint error.

### 3. Uniform bounds on the constant profile

By symmetry it suffices to consider 0<t<=1/2. Rearranging the absolutely
convergent series gives

    C(t)=1/t+2gamma+R(t),
    R(t)=2t^2*sum_{k=1}^infinity 1/[k*(k^2-t^2)].

Using k^2-t^2>=3k^2/4 and sum k^-3<=1+integral_1^infinity x^-3 dx=3/2,
termwise differentiation yields

    0<=R(t)<=4t^2,
    0<=R'(t)=4t*sum_{k=1}^infinity k/(k^2-t^2)^2
                 <=(32/3)*t.                          (5)

The termwise operations are justified by these uniform summable bounds.
Now

    Phi_0(t)=sin(pi*t)/(pi*t)
          +(2gamma-2log pi)*sin(pi*t)/pi
          +R(t)*sin(pi*t)/pi.

Elementary integral comparison gives 0<=gamma<=1, and log pi<3/2.
The three displayed terms have absolute bounds 1, 5/pi, and 1/pi,
so their sum is less than 3<4. For the first derivative, express the
first term as integral_0^1 cos(pi*t*u)du; its derivative is bounded by
pi^2*t/3<=pi^2/6<2. The second term has derivative magnitude <5.
For the third term, sin(pi t)<=pi t and (5) give

    |[R(t)*sin(pi*t)/pi]'|<=R(t)+t*R'(t)
       <=(44/3)*t^2<=11/3<4.

Thus the derivative magnitude is <11<12 on the half-interval. Reflection
gives the other half. The continuous periodic endpoint matching gives
the global Lipschitz bound by partitioning any segment at half-integers.
This proves (3).

## Scope and checks

This result supplies an all-integer pole profile, including odd-n cusp
and endpoint-offset limits. It alone does not eliminate the outer sum.
The actual polynomial collision convention remains that of N1-01/N2.
No effective n1 or B3 evaluation follows. A bounded independent analytic
critique reconstructed the cusp and constants and found no gap; that
supplements but does not replace distinct mathematical review or Claude
audit. No numeric fit, quadrature or finite sample is used as evidence.

## History

2026-11-05, round 3 at c000899; Codex requested gpt-6-astra ultra,
runtime metadata not independently exposed. Exact claim and odd-cusp
kill were recorded in ../ideas/N1-endpoint.md before the proof or any
new computation. Reviewed N1-01 and N1-02 bodies remain frozen.
