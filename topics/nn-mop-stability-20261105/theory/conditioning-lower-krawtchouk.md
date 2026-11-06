# PD-T437 — exponential NN conditioning lower bound

ID kind: PD-T. Aliases: alternating binomial weight witness; terminal Hermite
interpolation; explicit Krawtchouk sensitivity growth.
Split from: [D1 sharp growth target](conditioning-growth-target.md), OPEN. Split into: none.

## Statement

For every integer N>=2 put M=N−1 and, for k=0,...,M,

    z_k=2k/M−1,
    w_(1,k)=binom(M,k)(2/5)^k(3/5)^(M−k),
    w_(2,k)=binom(M,k)2^(−M).

Let F be the full normal NN coefficient triangle through degree N−1,
monic in z, with the conventions of PD-T286. Equip input perturbations
with |dot z_k|<=1 and |dot w_(s,k)|<=w_(s,k). Equip output with the maximum
of the four field sup norms, each divided by that base field's sup norm,
as in conditioning-local.md. Its induced derivative norm satisfies

    kappa_N >= 5^(N−1)/(N−1),                       N>=2,       (1)
    kappa_N >= (4 sqrt(6))^(N−1)
                  /[4(N−1)(N−2)],                 N>=3.       (2)

In particular liminf_(N→infinity) kappa_N^(1/N)>=4 sqrt(6)>9.79.
A literal constant-times-exponential corollary is

    kappa_N >= ((4 sqrt(6)/9−1)^2/72) 9^N,        N>=3.       (3)

The stronger exact finite witness is as follows. For n>=0, m>=1, n+m=M,
perturb only the second weights by

    w_(2,k)(epsilon)=w_(2,k)(1+epsilon (−1)^k).

At the terminal site (n,m), both b fields have directional derivative with

    |dot b_(n,m,2)| / ||b2||_infinity
      = (5^M/M) [v^(m−1)] ((1−v/25)/(1−v))^n.                (4)

Here ||b2||_infinity=1/5 exactly. This witness preserves the second mass
exactly, has input norm one, and leaves nodes and first weights fixed.
Consequently (1)–(2) also hold for the componentwise-node input convention
and for the fixed-mass restriction with the same coordinate bounds.

## Status and dependencies

Overall status: PROVED (written analytic proof; completed independent checks in
independent-checks-02.md and audit-01.md, priority1). No computation is a
premise. Retained quantitative continuation of the existing D1 growth
candidate; no priority claim. The sharp exponential rate and a matching
useful upper bound remain OPEN in the original target.

Dependencies: PD-T286/288/289 for the defining coefficient map and exact
layer reconstruction; the induced row-norm interpretation in
conditioning-local.md. Normality, the explicit coefficient scales and
all analytic estimates used here are proved below. No external source
theorem or unread classical formula is imported.

## Proof

### Normality and scalar binomial polynomials

The weight ratio w2/w1 is a positive constant times (3/2)^k. The functions
1,x,...,x^(n−1), exp(lambda x),...,x^(m−1)exp(lambda x), lambda>0,
form a Chebyshev system: if P+exp(lambda x)Q has n+m distinct real zeros,
its nth derivative has at least m distinct zeros by repeated Rolle, but
is exp(lambda x)(D+lambda)^n Q, with a nonzero polynomial factor of
degree at most m−1. The case Q=0 is immediate; n=0 is direct. Thus every
ordered evaluation determinant of size n+m is nonzero, and continuity
on the connected ordered-node domain makes its sign constant. Factor the
mixed moment matrix as this evaluation matrix, positive diagonal weights,
and the ordinary monomial evaluation transpose. Cauchy–Binet expresses
its determinant as a sum of nonzero terms with the same sign, since all
ordinary ordered Vandermondes are positive. Hence every index through
N is normal. This repeats the elementary normality proof in the D1 coarse
bound to make the lower-bound assumptions explicit.

For a scalar binomial parameter p, define

    G_p(k,t)=(1+(1−p)t)^k(1−pt)^(M−k),
    K_r(k)=r! [t^r] G_p(k,t),           0<=r<=M.

As polynomials in k, the K_r are monic: write G as
(1−pt)^M exp(k log((1+(1−p)t)/(1−pt))); the logarithm starts with t.
For k distributed as Bin(M,p), direct multiplication and the binomial
formula give

    E_p[G_p(k,s)G_p(k,t)]=(1+p(1−p)st)^M.

Thus E_p K_r K_l=0 for r!=l and
E_p K_r^2=r!(M)_r[p(1−p)]^r. The coefficient of k^(r−1) in K_r is
−rMp−r(r−1)(1−2p)/2, by expanding the same logarithm through t^2.
The ordinary monic recurrence consequently has

    alpha_r=r p(1−p)(M−r+1),
    beta_r=Mp+(1−2p)r.

Indeed orthogonality gives the three-term recurrence, its subleading
coefficient gives beta, and pairing with K_(r−1) gives the norm ratio
alpha. At r=M the monic successor is the support polynomial; the same
beta follows from its subleading coefficient and alpha from the norm
ratio. This also covers r=0 with alpha_0=0.

### Exact NN coefficient scales

In the unscaled node variable k, for general distinct p1,p2 in (0,1),
put d=p2−p1, q_s=p_s(1−p_s), and t=n+m. The actual NN coefficients are

    A_(n,m,1)=n q1(M−t+1),
    A_(n,m,2)=m q2(M−t+1),
    B_(n,m,j)=p_j(M−t)+(1−p1)n+(1−p2)m.                     (5)

Here is a verification rather than an appeal to a classical formula.
The axis values coincide with the scalar recurrence just proved. The
proposed difference is D_(n,m)=d(M−t), nonzero whenever t<=M−1.
For a mixed a update, the two D factors in PD-T289 cancel the factors
M−t+2 and M−t+1 to give (5). For the b update based at nu of degree t,

    (A1+A2)_(nu+e1)−(A1+A2)_(nu+e2)=(q1−q2)(M−t),
    (q1−q2)/d=−(1−p1−p2).

Hence its computed B_(nu+e2,1) is B_(nu,1)+1−p1−p2, precisely (5),
and adding D_nu gives B_(nu+e1,2). Induction in the exact layer recursion
proves every coefficient through degree M, including the terminal layer.
Under z=2k/M−1, a is multiplied by 4/M^2 and b becomes 2B/M−1.
For p1=2/5,p2=1/2 this gives

    b_(n,m,2)=n/(5M),     ||b2||_infinity=1/5.               (6)

All four field scales are positive: the a fields have nonzero first
marginal coefficients, b1 at the origin is −1/5, and (6) supplies b2.

### Terminal generating polynomial and its derivative

Fix n+m=M, m>=1. Work in the integer node variable. Let P be its monic
degree-M type-II polynomial and define

    H(z)=sum_(k=0)^M binom(M,k) P(k) z^k,     a=2/3.

Orthogonality for the first weight says H has a zero of order n at a;
for the second it has a zero of order m at 1. Indeed the conditions use
(zD_z)^j H at these nonzero points, and these derivative jets are related
to the ordinary jets by an invertible triangular transformation. Thus

    H(z)=C(z−a)^n(z−1)^m.                                  (7)

The leading coefficient of a polynomial f of degree at most M equals
(1/M!) sum_k (−1)^(M−k)binom(M,k)f(k). This finite-difference identity
follows by applying M differences to each monomial; each difference
lowers degree by one and multiplies the leading coefficient by its degree.
Consequently monicity gives H(−1)=(−1)^M M!, so C!=0.

Write tau for P's coefficient of k^(M−1). Apply the same identity to
kP(k)−product_(j=0)^M(k−j), which has degree at most M. Its degree-M
coefficient is tau+M(M+1)/2, and its values are kP(k). Therefore

    tau+M(M+1)/2=−H'(−1)/H(−1).

At a terminal site the successor is that support polynomial, so the
terminal recurrence coefficient is

    B_(n,m,2)=−H'(−1)/H(−1).                                (8)

Now apply the parity weight perturbation in the statement. It remains
positive for |epsilon|<1 and has mass one since E_2(−1)^k=0. Normality
persists on a sufficiently small neighborhood, so P and H are analytic
there. A dot denotes their derivative at epsilon=0. The differentiated
first constraints, second constraints and monicity give respectively

    (z−a)^n divides dot H(z),
    (z−1)^m divides dot H(z)+H(−z),
    dot H(−1)=0.                                           (9)

The second identity is the differentiated second-weight jet system:
parity changes evaluation at z=1 into evaluation of H(−z) at z=1,
including every (zD_z)^j jet.

Write dot H(z)=(z−a)^n S(z), where deg S<=m. The first m Taylor
coefficients of S at z=1 are those of

    −C(−1)^M ((z+a)/(z−a))^n (z+1)^m.

Also S(−1)=0. If T is that Taylor polynomial of degree m−1, then

    S(z)=T(z)−T(−1)(z−1)^m/(−2)^m,
    S'(−1)=T'(−1)+(m/2)T(−1).                              (10)

Put

    A(y)=(1+3y/5)^n(1+3y)^(−n)(1+y/2)^m,
    R=sum_(j=0)^(m−1) (m−j)(−2)^j [y^j]A(y).

Substituting z=1+y into (10), then differentiating (8) and using
(7) and dot H(−1)=0, gives

    dot B_(n,m,2)=(−1)^n (5^n/2) R.                         (11)

For clarity, the scalar factor follows from
S'(−1)=−C(−1)^M 5^n 2^(m−1) R and
 dot B=−S'(−1)/(C(−2)^m).

### Positive coefficient reduction and the all-N estimate

The finite sum in (11) can be simplified exactly:

    R=[t^(m−1)] (1−t)^(m−2)
                       ((1−6t/5)/(1−6t))^n
     =[u^(m−1)] ((1−u/5)/(1−5u))^n
     =5^(m−1) [v^(m−1)] ((1−v/25)/(1−v))^n.               (12)

The first equality uses the generating series (1−t)^−2 for the weights
m−j. The second uses, for r>=0 and any formal power series F,

    [t^r](1−t)^(r−1)F(t)=[u^r]F(u/(1+u)).

One can verify this without analysis: by linearity take F(t)=t^j;
both coefficients equal (−1)^(r−j)binom(r−1,r−j) for 1<=j<=r,
and the constant term cases agree separately (including r=0).
Thus the formal substitution in (12) is justified also at m=1.
Equations (6), (11), (12), and z scaling prove (4).

Taking n=M−1,m=1 in (4) gives (1). To get (2), let M>=2,

    r=floor((M−1)/2),   m=r+1,   n=M−1−r,   c=24/25.

The coefficient Q=[v^r](1+c v/(1−v))^n is one when r=0. For r>=1,

    Q=sum_(j=1)^min(n,r) binom(n,j)c^j binom(r−1,j−1)
      >=c^r binom(n+r−1,r)
       =c^r binom(M−2,r).

The equality for the unweighted sum follows from the coefficient of v^r
in (1+v/(1−v))^n=(1−v)^−n. The same bound holds when r=0.
The binomial coefficient is central and therefore at least the average
2^(M−2)/(M−1). Since c<1 and r<=(M−1)/2,

    (5^M/M) Q
      >= (4 sqrt(6))^M/[4 sqrt(c) M(M−1)]
      >= (4 sqrt(6))^M/[4 M(M−1)].

This proves (2). Finally put q=4 sqrt(6)/9>1. The binomial theorem gives
q^M>=(M(M−1)/2)(q−1)^2 for M>=2; substituting into (2) proves (3).

## Interpretation and limits

The mechanism is a signed relative-weight direction applied to an exactly
normal input. Formula (9) exposes its amplification through a Hermite
interpolation problem between the distinct weight-ratio points 2/3 and 1;
it does not reduce to one inverse minimum NN divisor. The parity direction
is admissible under both independent-mass and fixed-mass conventions.

The logarithm of (2) gives an explicit lower bound on worst-case
first-order amplification in decimal digits:

    (N−1) log10(4 sqrt(6))−log10(4(N−1)(N−2)).

This is a capacity, not a prediction for every perturbation or an algorithm's
actual rounding error. No finite-epsilon radius uniform in N, sharp rate,
matching upper bound, or backward-stability conclusion is asserted.

## Checks and history

2026-11-05: bounded Codex hard-step developer; requested gpt-6-astra ultra
under handoff01, coordinator justification in LOG; rules/source
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1, base
b4d292eea5eed373002506d5e16a3761bd7ae10e. Prospective gate and retained
routes: ../novelty-gate-D1-hard.md. Execution receipt and independent
check references are added in ../attempts/D1-hard.md when completed.

## Dated addendum — summed terminal coefficients, 2026-11-05

A sharper consequence of the same exact witness is PROVED:

    kappa_N >= 5/[2(N−1)^2] *
       [(5+2 sqrt(6))^(N−2)+(5−2 sqrt(6))^(N−2)],   N>=2.   (13)

In particular liminf kappa_N^(1/N)>=5+2 sqrt(6)>9.89. This strengthens
the lower rate without replacing or altering (1)–(4). A matching upper
bound, and hence the actual exponential rate, remain OPEN.

Here is a self-contained summation argument. For n,r>=0 define

    Q_(n,r)=[v^r]((1−v/25)/(1−v))^n,
    S_L=sum_(n+r=L) Q_(n,r).

All Q_(n,r) are nonnegative by the positive expansion already proved.
As a formal power series,

    sum_(L>=0) S_L z^L
      =sum_(n>=0) z^n ((1−z/25)/(1−z))^n
      =(1−z)/(1−2z+z^2/25).

Hence S_0=S_1=1 and S_L=2S_(L−1)−S_(L−2)/25 for L>=2.
The sequence

    S_L=((1+sqrt(24/25))^L+(1−sqrt(24/25))^L)/2

has those same initial values and recurrence, proving the identity by
induction. Set L=M−1. There are M nonnegative summands, corresponding
exactly to the terminal pairs n+m=M with m=r+1>=1 in (4). Their maximum
is at least S_(M−1)/M. Multiplying by the prefactor 5^M/M in (4) proves
(13), including M=1. Its positive leading exponential term proves the
stated liminf. This is the same fixed parity perturbation across every
terminal pair; no independently incompatible row directions are combined.

The initial file hash before this addendum was
409f625a57d6c0e004781f666ef35f71fbcd25b447f0cc5c938da74d77340b0f.
That proof was reviewed independently and its small-N identities replayed;
the final hash including this addendum is submitted separately for recheck.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `PD-T?nn-mop-stability-codex-D1-hard-01` → `PD-T437`.
