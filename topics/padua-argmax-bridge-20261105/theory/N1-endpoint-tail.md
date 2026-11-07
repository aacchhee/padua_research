# PD-T?argmax-bridge-codex-N1-03 — Uniform endpoint cancellation tail

ID kind: PD-T. Aliases: equal-opposite-channel subtraction; logarithmic
endpoint residual; boundary-uniform cancellation perturbation.
Split from: the N1 full-diamond finite-dimensional profile, which remains
OPEN. Split into: none. Reviewed N1-01 and N1-02 are unchanged.

## Statement and definitions

Let alpha,beta>=0, alpha+beta<=pi, and put

    a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta, P=p+q,
    C(v)=(p-q-2a cot(v/2))/4,
    D(v)=(p+q+2a cot(v/2))/4.

For v not in pi*Z, use N1-02's ordinary bounded integral

    I(C,D,v)=integral_0^pi
       [|C cot x+D cot(x+v)|-|C cot x|-|D cot(x+v)|] dx.

The values at the two poles are assigned zero and do not affect the
integral. For 0<d<=pi/4 define

    J_a(d)=2a cot(d/2) log(sin d),
    f(d)=3+2log(4pi/d).

For every v in (0,pi/4] union [7pi/4,2pi), d=min(v,2pi-v),

    |I(C(v),D(v),v)-J_a(d)| <= P f(d).                 (1)

No lower bound on a, P or distance to a phase-diamond edge is assumed.
Thus the bound remains valid at a=0, where J_a is identically zero.
Separate absolute phases extend the statement to the entire diamond.

Here is its count-free discrete consequence. Let n>=2, m=n+1,
v_r=(r*pi+beta)/m, d_r=min(v_r,2pi-v_r), and 0<delta<=pi/4.
Let E_delta be any subset of the rows 1<=r<=2m-2 with d_r<=delta.
Put Z(v)=I(C(v),D(v),v)-J_a(min(v,2pi-v)) on the endpoint arcs. Then

    (1/(pi*m))*sum_{r in E_delta}|Z(v_r)|
       <= T(P,delta),                                    (2)
    T(P,delta)=(2P*delta/pi^2)*[5+2log(4pi/delta)].

The two closest rows r=0,2m-1 are excluded, as in N1-01's exact endpoint
convention. This is essential to the uniform shifted-grid bound.
For the continuous outer tail one likewise has

    (1/pi^2)*integral_{(0,delta) union (2pi-delta,2pi)} |Z(v)|dv
       <= T(P,delta).                                    (3)

In particular, the difference of the signed discrete residual tail and
the signed continuous residual tail is at most 2T(P,delta). Equation (2)
also bounds the cost of deleting the discrete residual tail altogether.
It is uniform in the degree and contains no degree-dependent sum count.

## Assumptions and status

Overall status: **PROVED**, analytic developer proof below; distinct
mathematical review pending. Exact real arithmetic. No computational or
external source-theorem premise. Equations (1)-(3) are supporting tail
estimates, not an all-degree maximum comparison or a B3 PASS.

## Dependencies and sources

N1-02 supplies the definition and Padua normalization of I. The proof of
the perturbation estimate below is elementary and independent of its
variation bound. T269/T270/T365 are methodological predecessors only.
No new external theorem is transferred. Gate and candidate:
../novelty-gate-N1.md and ../ideas/N1-endpoint.md.

## Proof

### 1. Exact reference integral

For 0<v<=pi/4 and s>=0, write

    g_0(x)=|-s cot x+s cot(x+v)|-s|cot x|-s|cot(x+v)|.

When two real summands have opposite signs, the difference between the
absolute value of their sum and the sum of their absolute values is
-2 times the smaller magnitude; otherwise it is zero. Consequently the
only nonzero pieces of g_0 are

    g_0(x)=-2s cot(x+v),  0<x<pi/2-v,
    g_0(x)= 2s cot x,     pi/2<x<pi-v.

Integrating these two pieces gives, respectively, 2s log(sin v) and
2s log(sin v). Thus

    I(-s,s,v)=4s log(sin v).                             (4)

This identity includes s=0. With s=a cot(v/2)/2, its right side is J_a(v).

### 2. Uniform perturbation, including vanishing s

We prove the following stronger elementary estimate. For 0<v<=pi/4,
s>=0, epsilon>=0, |C+s|<=epsilon and |D-s|<=epsilon,

    |I(C,D,v)-I(-s,s,v)|
       <= epsilon*[11+8log(4pi/v)].                     (5)

When epsilon=0 the claim is exact. Assume epsilon>0. On the circle of
length pi take neighborhoods of radius tau=v/8 about the poles 0 and
pi-v. They are disjoint. In either neighborhood the other cotangent's
distance from its own pole lies between 7v/8 and 9v/8<pi/2. Hence its
magnitude is at most 8/(7v), by cot y<=1/y on (0,pi/2).
The pole's own cotangent, at distance 0<y<=tau, has magnitude at least
1/(2y)>=4/v, using cos y>=1/2 and sin y<=y.

If s>=4epsilon, the signs of C,D equal the reference signs and their
magnitudes lie between 3s/4 and 5s/4. Throughout each pole neighborhood
the own-channel magnitude is at least 3s/v, whereas the other is at
most 10s/(7v). The own channel therefore dominates. On either side of
the pole, both the perturbed and reference cancellations are either zero
or -2 times the other-channel magnitude, with the same choice. Their
difference has magnitude at most 16epsilon/(7v). Each neighborhood has
length v/4, so their total integral difference is at most 8epsilon/7.

If s<4epsilon, each perturbed coefficient has magnitude at most
5epsilon, and each reference coefficient at most 4epsilon. A cancellation
is always bounded in magnitude by twice either channel's magnitude.
Using the nonsingular other channel in each neighborhood therefore bounds
the sum of the two absolute cancellations by

    2*(5epsilon+4epsilon)*8/(7v)=144epsilon/(7v).

Integrating over both neighborhoods gives 72epsilon/7<11epsilon.
This case does not assume the perturbed coefficient signs. Both regimes
are consequently bounded by 11epsilon on the pole neighborhoods.

On their complement the ordinary absolute-value Lipschitz inequality
gives pointwise

    |g(C,D,v;x)-g(-s,s,v;x)|
       <=2epsilon*(|cot x|+|cot(x+v)|).

For either cotangent, deleting its own radius-tau neighborhood bounds
its remaining absolute integral by

    -2log(sin tau)<=2log(pi/(2tau))=2log(4pi/v),

using sin tau>=2tau/pi. Deleting the other neighborhood only decreases
this integral. Thus the complementary contribution is at most
8epsilon log(4pi/v). This proves (5).

For the actual coefficients on the left endpoint, put epsilon=P/4 and
s=a cot(v/2)/2. Since a>=0 and |p-q|<=P, all hypotheses hold.
Combining (4) and (5), and using 11/4<=3, proves (1) there.

At the other endpoint write v=2pi-d. Reflection x->-x and periodicity
give I(C,D,v)=I(C,D,d), and simultaneous coefficient sign reversal leaves
I unchanged. Here

    -C=-a cot(d/2)/2-(p-q)/4,
    -D= a cot(d/2)/2-(p+q)/4.

They are within epsilon of (-s,s), with s=a cot(d/2)/2. The same estimate
proves (1) on the right endpoint. No division by a or P occurred.

### 3. Uniform mesh and integral tails

The function f(d)=3+2log(4pi/d) is positive and decreasing on
(0,pi/4]. On the left endpoint, v_r>=(pi/m)r for r>=1. Put h=pi/m.
For all rows in E_delta on that side, r h<=v_r<=delta, so positivity
and monotonicity give

    h*sum f(v_r)<=h*sum_{1<=r<=floor(delta/h)} f(rh)
       <=integral_0^delta f(d) dd
       =delta*[5+2log(4pi/delta)].                       (6)

The assertion also holds when delta<h, because the sum is empty.
On the right endpoint put k=2m-r-1>=1. Then

    d_r=((k+1)pi-beta)/m>=k h,

because beta<=pi. Distinct rows have distinct k, so (6) applies again.
Multiply the two bounds by P/pi^2, since 1/(pi*m)=h/pi^2, and use (1)
to obtain (2). Direct integration of (1) on the two endpoint arcs proves
(3). The final difference estimate follows from the triangle inequality.

## Scope and next unresolved step

The residual of the exact cancellation integral has now been removed
from arbitrarily thin endpoint strips with a proved degree-uniform cost.
This is stronger than an O(n)-term rewrite: the tail itself may be
deleted or enclosed by one explicit number independent of its row count.
The subtracted J_a is singular and must still be combined with the pole
norms. It must not be independently bounded and then dropped.

The full compact profile is OPEN. Its remaining obligations include the
joint outer pole-norm/J_a expansion, the interior outer quadrature, and
uniform charts for the finitely many exact exceptional rows. Neither this
supporting estimate nor any small chosen delta supplies an effective n1,
a complete error budget, or a pass/fail evaluation of the original B3.

## Checks and history

Analytic derivation only; no numerical integration, fit or sample is a
proof premise. Independent mathematical critique is requested separately.
2026-11-05, round 3 after pushed boundary c000899, Codex developer,
requested gpt-6-astra ultra; runtime model metadata not independently
exposed. The exact claim and kill were recorded before this proof and any
new computation in ../ideas/N1-endpoint.md.
