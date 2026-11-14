# PD-T?argmax-bridge-codex-C08-far-05 — A uniform half-unit pole-functional bound

ID kind: PD-T. Aliases: semiconcave periodic pole envelope; exactly
integrated range/curvature bound. Split from: C08 far integral control.
Split into: none. The joint cancellation integral is independently owned.

## Statement and status

Let f(x)=Phi_0(1/2+x/(2pi)), where Phi_0 is exactly N1-04's continuous
periodic regularized-pole function. For every real x define

    H(x)=(1/pi)lim_(delta->0+)
       [integral_delta^(2pi-delta) f(x+v)/(2sin(v/2))dv
                                      +2f(x)log(delta/pi)].    (1)

The limit exists, and

    H(x)<749/1500<1/2, every real x.                   (2)

For the same expression without taking the limit, denoted H_delta(x),
at delta=1/100 one also has

    H_delta(x)-H(x)<(12/pi^2)(delta+delta^3/48).       (3)

These assertions include all integer-offset cusp positions. **PROVED**,
written analytic developer lemma; distinct reconstruction and formal audit
are separate. No numerical integration, sampling or fitted constant is
a premise.

Dependencies: N1-04's C/Phi series and global Lipschitz bound; C04-near-01
section1's full-period distributional second-derivative inequality,
whose statement there explicitly includes all integer atoms; C06-far-profile
section6's global Phi_0<=1 proof. Only those globally stated scalar
lemmas are used, not a near-domain two-phase theorem. The lower range
bound and every new integral estimate are proved below.

## 1. The exact scalar range and curvature

We first prove

    1/2<=f(x)<=1,                                      (4)
    f(x+v)+f(x-v)-2f(x)<=3v^2/pi^2.                  (5)

The upper bound in (4) is C06-far-profile section6. The full-period
distributional inequality Phi_0''<=12 dt, proved in C04-near-01
section1, includes negative derivative jumps at every integer. Scaling
its triangular-kernel second-difference bound gives exactly (5).

For the lower bound, by symmetry and periodicity write0<=y<=1,
c=cos(pi*y/2), and k0=C(1/2)-2log pi. The reciprocal-pair series gives

    f(pi*y)=(c/pi)[k0+4y^2 sum_(l odd>=1)1/(l(l^2-y^2))].     (6)

For0<=y<1 it follows that
pi*f(pi*y)>=c*k0+4c*y^2/(1-y^2). We use the elementary inequality

    cos(pi*y/2)>=(3/4)(1-y^2).                       (7)

To verify (7), set t=1-y and
q(t)=sin(pi*t/2)-(3/4)t(2-t). Then q(0)=0,
q'(0)=pi/2-3/2>0, q'(1)=0, and
q''(t)=3/2-(pi^2/4)sin(pi*t/2) is decreasing and crosses zero once.
Thus q' first increases and then decreases to zero, so q'>=0 and
q>=0 on[0,1]. This proves (7).

The elementary constants in C06 and N1-16 give C(1/2)<4, log pi>1,
so k0<2. Since1-c<=pi^2 y^2/8 and pi^2<10,

    4c*y^2/(1-y^2)>=3y^2>=k0(1-c).

Therefore f(pi*y)>=k0/pi=f(0); endpoint y=1 follows continuously.
Finally gamma>23/40, log2>69/100 and log pi<23/20 imply
k0=2gamma+4log2-2log pi>161/100>pi/2, using pi<22/7.
For the displayed log-pi upper, exp(23/20)>22/7 follows already
from its positive series through degree5. Hence f(0)>1/2 and (4)
is proved. The weak form suffices throughout.

## 2. Remove the endpoint singularity before bounding the integral

The function f is even,2pi-periodic and globally Lipschitz, with
Lip(f)<=6/pi from N1-04. Pair v with2pi-v in (1). The constant
part can be integrated exactly because

    integral_delta^(2pi-delta) dv/(2sin(v/2))
                                              =2log cot(delta/4).

It follows that

    H(x)=lambda0*f(x)+(1/pi)integral_0^pi
        [f(x+v)+f(x-v)-2f(x)]/(2sin(v/2))dv,
    lambda0=(2/pi)log(4/pi)<1/(2pi).                 (8)

The integral exists absolutely: the Lipschitz bound makes the numerator
O(v), while the denominator is comparable to v. The bound on lambda0
uses pi>25/8 and exp(1/4)>32/25, the latter following from the first
four positive exponential-series terms. Thus log(4/pi)<1/4.

Let q=1-f(x). By (4),0<=q<=1/2. Its second difference is bounded
above both by (5) and by2q. Thus the integrand numerator is bounded by

    min(Kv^2,2q), K=3/pi^2.                           (9)

Negative second differences are not discarded as an unaccounted error;
replacing them by the nonnegative upper (9) is a one-sided inequality.

## 3. An elementary kernel bound and its exact integral

For0<v<=pi,

    1/(2sin(v/2))<=1/v+v/16.                        (10)

Indeed with x=v/2 and t=x^2<=pi^2/4<5/2, the alternating lower
Taylor polynomial through-x^7/5040 gives

    (1+t/4)(sin x/x)-1
       >=t/12-t^2/30+19t^3/10080-t^4/20160>=0.

The first two terms have nonnegative sum for t<=5/2, and the last
two have positive sum for0<t<=5/2. Rearranging is exactly (10).

If q>0, the two branches in (9) meet at
t_q=sqrt(2q/K)=pi*sqrt(2q/3)<pi. Split the integral there and
integrate each power and reciprocal exactly. The result is

    integral_0^pi min(Kv^2,2q)(1/v+v/16)dv
       =q+q log(3/(2q))+(pi^2/16)(q-q^2/3).         (11)

The formula extends to q=0 by qlog q=0. Substituting (9)–(11) in
(8), and using f(x)>=0 with lambda0<1/(2pi), yields

    H(x)<(1/pi)[(1/2)(1-q)+q+q log(3/(2q))
                                      +(pi^2/16)(q-q^2/3)].  (12)

The bracket's derivative in q is
log(3/(2q))-1/2+(pi^2/16)(1-2q/3), which is positive on0<q<=1/2.
Thus its largest value is at q=1/2, giving

    H(x)<[3/4+(1/2)log3+5pi^2/192]/pi
          <[3/4+11/20+25/96]/(25/8)=749/1500<1/2. (13)

Here log3<11/10, pi^2<10 and pi>25/8 are elementary scalar
bounds. This proves (2) uniformly, including the negative cusp atoms.

## 4. A signed finite-cutoff bound

For H_delta, the constant coefficient in (8) is instead

    lambda_delta=(2/pi)log[(delta/pi)cot(delta/4)].

Since z cot z<1 for0<z<pi/2, lambda_delta<lambda0. By f>=0,
this coefficient difference is favorable in an upper estimate. The
remaining difference is the negative of the integral in (8) from0
to delta. Its numerator has absolute value at most12v/pi by the
global Lipschitz bound. Using (10) gives

    H_delta(x)-H(x)
      <=(12/pi^2)integral_0^delta(1+v^2/16)dv
       =(12/pi^2)(delta+delta^3/48),

which proves (3). In particular two channels with nonnegative weights
whose sum is at most2 cost less than27/1000 at delta=1/100.
No endpoint derivative or a positive atom has been assumed away.

## Scope and history

The stronger possible shape inequality H(x)<=cos(x/2)H(0) was not
needed and is not asserted. The uniform half-unit upper is sufficient
for the complementary full-phase cancellation estimate when combined
with the separately proved finite corner margin. This file does not
itself assert the final far-model comparison.

All integrals in the proof are evaluated or bounded analytically with
explicit constants. No quadrature executable or phase evaluation was run.
The full-period C04 scalar lemma is used at exactly its proved scope.

2026-11-06, rules/input4b728b04216a5490910780bc609a82b853058426.
Codex, coordinator-requested Astra ultra; serving metadata unexposed.
