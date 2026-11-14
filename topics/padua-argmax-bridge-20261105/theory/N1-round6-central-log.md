# PD-T?argmax-bridge-codex-N1-14 — Uniform coalescing-pole logarithm

ID kind: PD-T. Aliases: central entropy formula; vanishing-coefficient
central remainder. Split from: round-6 outer compactification.
Split into: none. All old central special-row conventions remain.

## Statement

Assume alpha,beta>=0, alpha+beta<=1/2. Use N1-05's a,p,q,C,D,I and
put d=(q-p)_+. For 0<epsilon<=pi/2 define

    Z_L(epsilon)=I(C(pi-epsilon),D(pi-epsilon),pi-epsilon)
                       -d*log epsilon,
    Z_R(epsilon)=I(C(pi+epsilon),D(pi+epsilon),pi+epsilon)
                       -d*log epsilon.

Both functions have finite continuous limits at epsilon=0, including
q=p and p=q=0. Uniformly in the stated phases,

    ||Z_L||_infinity,||Z_R||_infinity<3,
    Var(Z_L)+Var(Z_R)<15.                             (1)

In particular the exact central logarithmic coefficient of I is
(sin beta-sin alpha)_+, with the N1 half-kernel normalization. There
is no inverse d or inverse p in the conclusion or its proof bounds.
The value at epsilon=0 means the displayed subtracted limit, not an
evaluation of separate cotangent channels on an actual collision row.

## Status and dependencies

Overall status: **PROVED**, analytic developer proof; distinct review
pending. N1-02 supplies only the definition of I and N1-05 the actual
coefficients. The integral formulas and uniform variation bounds are
proved below. No external theorem, computation or fitted coefficient
is used. Candidate: ../ideas/N1-round6.md.

## Proof

### 1. A two-parameter cancellation integral

For u,s>=0 and 0<epsilon<=pi/2 write

    J(u,s,epsilon)=I((u-s)/2,(u+s)/2,epsilon).

The integral is unchanged by exchanging its two coefficients, by
simultaneously reversing their signs, or by replacing epsilon by
-epsilon. These facts follow by x -> -x-epsilon or x -> -x on the
cotangent circle. If 0<=s<=u, put c=(u-s)/2,b=(u+s)/2. Then

    J=2[c log(c/u)+b log(b/u)],                       (2)

with 0 log 0=0 and J=0 when u=s=0. Thus this same-sign integral is
independent of separation. This is a finite entropy expression; its
limit need not equal the separate-channel value at zero separation.

For verification, the cancellation is -2 times the smaller channel on
the two short opposite-sign cotangent intervals. Put
theta=arcsin((s/u)sin epsilon), y0=(epsilon-theta)/2 and
y1=(epsilon+theta)/2. Direct integration of cot and tan gives

    -2u log(sin epsilon)
      +2[c log(sin y0 cos y1)+b log(sin y1 cos y0)].

The two products equal c*sin(epsilon)/u and b*sin(epsilon)/u;
the logarithms of sin epsilon cancel, proving (2). End cases follow
by continuous limits.

Suppose s>u and put c=(s-u)/2,b=(s+u)/2. The coefficients now have
opposite signs, (-c,b). Define

    R(u,s,epsilon)=J(u,s,epsilon)-2(s-u)log(sin epsilon).

If s*sin epsilon>=u, there are no internal channel-equality roots on
the long cancellation interval and

    J=2s log(sin epsilon), R=2u log(sin epsilon).       (3)

If s*sin epsilon<u, let theta=arcsin(s*sin(epsilon)/u),
x1=(theta-epsilon)/2 and x2=(pi-theta-epsilon)/2. Splitting the
positive long interval at x1,x2 gives instead

    J=2s log(sin epsilon)
       +2[b log(cos x1/sin(x1+epsilon))
                      -c log(cos(x1+epsilon)/sin x1)]. (4)

The negative long interval always uses the smaller coefficient c.
Its contribution is 2c log(sin epsilon); integrating the three pieces
on the positive interval proves (3)-(4). All endpoint products are
interpreted by their continuous limits.

Extend R to s<=u by R=J, so in all cases

    J=2(s-u)_+ log(sin epsilon)+R(u,s,epsilon).        (5)

### 2. Derivative and entropy bounds without division by a phase

For s>u, put D=sqrt((u^2-s^2 sin^2 epsilon)_+). Differentiating the
piecewise integral (the moving-root boundary terms cancel) gives

    R_epsilon=2[u cos epsilon-D]/sin epsilon>=0.       (6)

For s<=u this derivative is zero. At a root threshold both formulas
join continuously. For fixed u, the quantity in (6) is increasing in
s until it reaches the value 2u cot epsilon. Moreover R(u,s,pi/2)=0
when s>u, and (4) gives the finite limit

    R(u,s,0)=2[c log c+u log u-b log b].               (7)

It follows that |R|<=2b log 2=(s+u)log 2 in this case. For s<=u,
equation (2) gives |R|<=2u log 2.

The other parameter derivative, away from the integrable singularity
s=u, satisfies

    |R_s|<=log((u+s)/|u-s|).                          (8)

For s<u this follows directly from (2). For s>u in the root regime,
differentiating (4) gives

    R_s=log[(s cos epsilon-D)/(s cos epsilon+D)].

Since D<=u cos epsilon, this lies between log((s-u)/(s+u)) and zero.
In the no-root regime (3), R_s=0. When u=0 all these remainders vanish;
that case is used directly rather than divided by u.

For 0<u<=1/4 and S=5/4, integration of (8) yields

    integral_0^S log((u+s)/|u-s|)ds
      =(S+u)log(S+u)-(S-u)log(S-u)-2u log u
      <=2u[1+log((S+u)/u)]<3/2.                     (9)

The final majorant increases with u and at u=1/4 is
(1+log 6)/2<3/2. The bound extends as zero at u=0. Equations (6)-(7)
also give, for any measurable s(epsilon) in [0,S],

    integral_0^(pi/2) |R_epsilon(u,s(epsilon),epsilon)|d epsilon
      <=-R(u,S,0)<(S+u)log 2<21/20.                 (10)

This uses monotonicity in s before integrating; it does not incur a
logarithm of a small phase or a small central cutoff.

### 3. Apply the uniform bounds along the actual two folded curves

The actual central parameters, after the permitted coefficient exchange
and separation reflection, are

    u=p/2,
    s_L(epsilon)=q/2+a tan(epsilon/2),
    s_R(epsilon)=|q/2-a tan(epsilon/2)|.              (11)

They lie in [0,5/4]. The left curve is monotone; the right has at most
two monotone pieces. Hence (9) bounds the sum of their parameter-motion
variations by 9/2. Equation (10) adds less than 21/10. Consequently

    sum_s Var[R(u,s_s(epsilon),epsilon)]<33/5.        (12)

This can first be applied away from s=u and root thresholds, then
passed to the endpoints using the integrable bounds in (8)-(9).
Thus no differentiability is assumed across those transitions.

Let k_s(epsilon)=2(s_s(epsilon)-u)_+. Its common endpoint value is
k_s(0)=d. From (11), for almost every epsilon,

    |k_s'|<=2a,
    |k_s(epsilon)-d|<=2a tan(epsilon/2).

By (5) the exact central residue is

    Z_s=R(u,s_s(epsilon),epsilon)
       +(k_s(epsilon)-d)log(sin epsilon)
       +d*log(sin epsilon/epsilon).                 (13)

The last two terms have variation at most

    2a*integral_0^(pi/2) -log(sin epsilon)d epsilon
      +2a*integral_0^(pi/2) tan(epsilon/2)cot epsilon d epsilon
      +d*log(pi/2)
    <=a*pi*log 2+a*pi/2+d*log(pi/2)<81/20.           (14)

Here the first integral equals (pi/2)log 2: compare the integral with
its reflected cosine version and use sin(2x)=2sin x cos x. The second
integrand is cos epsilon/(1+cos epsilon)<=1/2. Also a<=1,d<=1/2,
pi*log2<11/5,pi/2<8/5 and log(pi/2)<1/2. Combining two copies of
(14) with (12) gives total variation below 147/10<15.

The sup bound follows from |R|<21/20, the estimate
tan(epsilon/2)<=epsilon, and
epsilon*[-log(sin epsilon)]<=epsilon*log(pi/(2epsilon))<3/5.
The final term in (13) has magnitude below 1/4. Thus |Z_s|<5/2<3.
The last two terms tend to zero at epsilon=0, whereas (7) or (2) gives
a common finite entropy limit for R. This also proves the asserted
continuity, including u=0, q=p and the double zero phase.

## Scope, verification and history

This proves the specific central subtraction and a uniform BV remainder.
It is not a claim about an actual sampled pole: those finite polynomial
rows stay in the special set. A finite-count outer model must still
include the log-mesh/cell error, the other profile components and the
special-row evaluation error. No onset or B3 PASS follows in isolation.

No mathematical computation or fit was run. 2026-11-06 after published
88e7023, requested gpt-6-astra ultra. All older proof bodies remain
unchanged. This closes the preregistered first logical test.
