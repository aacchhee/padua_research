# PD-T?nn-mop-stability-codex-D1-02 — explicit coarse Krawtchouk conditioning bound

ID kind: PD-T. Aliases: rational-height NN bound; exponential Chebyshev
normality; finite all-N conditioning upper bound.
Split from: D1 sharp growth-law target (OPEN). Split into: none.

## Statement

For every integer N>=2 put M=N−1, x_l=2l/M−1 (l=0,...,M), and
w_(s,l)=binom(M,l)p_s^l(1−p_s)^(M−l), p1=2/5,p2=1/2.
Every multi-index of degree <=N is normal. For the mixed-input,
fieldwise-output condition of conditioning-local.md, define the integers

    D=10^M M^(2N), B=N^N D^N, R=2N+1,
    C=B(NB+1)R, H=NB+1, T=NC+HR.

Then the completely explicit bound

    kappa_N <= 5M max(2C, B*T*(1+H*B))

holds. The componentwise-input condition obeys the same bound because
|x_l|<=1. This is deliberately very coarse; it proves no growth lower
bound, exponential rate, useful attainable accuracy or algorithmic
stability. The D1 sharp growth target remains OPEN.

## Definitions and assumptions

The coefficients are monic in x=z in [−1,1], with PD-T286 h/t conventions
through degree N−1. Exact real arithmetic. Arbitrary independent relative
weight perturbations and absolute node perturbations of scale one are
allowed locally. These input perturbations can leave the binomial family.

## Status by part

Overall status: PROVED (written proof; independent audit pending).
Candidate disposition: retained coarse standard rational-height variant;
no novelty claim. This bound is not offered as a sharp D1 growth theorem.

## Depends on

PD-T286; local derivative formulas in conditioning-local.md. The proof of
normality and all constants are supplied below, so no unread classical
closed-form NN recurrence is used.

## Proof or evidence

First prove normality. The weight ratio is a positive constant times
(3/2)^l, hence a positive constant times exp(lambda*x_l), lambda>0.
For n+m=k, the functions

    1,x,...,x^(n−1), exp(lambda*x),...,x^(m−1)exp(lambda*x)

form a Chebyshev system on the real line. Indeed, a nonzero combination
P+exp(lambda*x)Q with deg P<n and deg Q<m has at most k−1 distinct real
zeros. If Q!=0, its nth derivative is exp(lambda*x)(D_x+lambda)^n Q,
whose polynomial factor is nonzero of degree <=m−1. Rolle's theorem
then bounds the number of zeros by n+m−1. If Q=0 the polynomial bound
suffices; the case n=0 is direct as well.

Consequently every k-by-k evaluation determinant on increasing distinct
nodes is nonzero and has a constant sign: the domain of ordered tuples
is connected and its determinant is continuous and never zero. Factor
the mixed moment matrix as the evaluation matrix of these k functions,
times diag(w1), times the transpose of the ordinary monomial evaluation
matrix. In the Cauchy–Binet expansion every k-node term has the same
nonzero sign: the weights are positive and the monomial Vandermonde is
positive. The sum cannot vanish. This works for every k<=N.

For the quantitative bound, moments mu_(s,r), 0<=r<=2N, have absolute
value at most one. Their rational denominators divide D: weights have
denominators dividing 5^M or 2^M and x_l^r has denominator dividing M^r.
Thus every k-by-k moment determinant, k<=N, has nonzero numerator with
denominator dividing D^k, giving |det M_nu|>=D^(−k). Hadamard's bound
on (k−1)-minors gives

    ||M_nu^(−1)||_infinity
       <= k (k−1)^((k−1)/2) D^k <= B,

where the k=1 empty minor is one. Thus each coefficient of the monic
P_nu other than the leading one is bounded by B. Under a mixed-input
direction of norm at most one,

    |dot mu_(s,r)| <= 1+r <= R,
    ||dot c_nu||_infinity <= B(R+k R B) <= C.

These estimates apply through degree N. For h_(nu,s) needed by an a
coefficient, |nu|=k<=N−1. Its absolute value is at most kB+1<=H and its
directional derivative at most kC+(kB+1)R<=T. A bordered-determinant
(Schur-complement) identity, with a possible row-order sign, gives

    |h_(nu,s)|=|det M_(nu+e_s)|/|det M_nu|.

The numerator is at least D^(−(k+1)); Hadamard bounds the denominator
by k^(k/2)<=N^N. Therefore every such h has |h|>=1/B (the empty
degree-zero determinant is one). The derivative ratio rule yields

    |dot a_(nu,s)| <= B*T+H*B^2*T,
    |dot b_(nu,j)| <= 2C.

Finally each of the four output field scales is at least 1/(5M).
For a1,a2 use their degree-one marginal coefficients, the binomial
variances 24/(25M) and 1/M in z; b1_(0,0)=−1/5. For b2 use site (1,0).
The binomial means and second moments are

    mu_11=−1/5, mu_21=0,
    mu_12=1/25+24/(25M), mu_22=1/M.

Solving the two orthogonality equations for P_(1,1)=z^2+t*z+c gives
t=(M−1)/(5M). Since t_(1,0)=1/5, b2_(1,0)=1/(5M).
These elementary binomial moment formulas follow by differentiating
(1−p+pt)^M once and twice at t=1 and applying z=2l/M−1.
Dividing the derivative bounds by these field-scale lower bounds proves
the stated condition-number bound.

## Checks and sources

This is a written proof, without a computational premise. Inputs are the
Krawtchouk inputs of PD-T290. No new literature attribution is made.
Numerical derivative tables independently describe the much smaller
observed values; they are not a verification of all-N normality or bounds.

## Scope

Only the exact rational parameters p1=2/5,p2=1/2 are covered by the
displayed constants. Normality argument alone extends to distinct
binomial parameters in (0,1). The height estimate is pessimistic and
cannot distinguish intrinsic growth mechanisms or predict digits lost.

## Open items

An explicit exponential lower bound, sharp upper bound, and a formula
with usable constants predicting the observed growth. The local derivative
and this coarse bound are substantive supporting results, not a PARTIAL
classification of that unresolved target.

## History

2026-11-05: D1 Codex mathematical developer, gpt-6.1-sol xhigh as allocated;
rules/input 823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. No Git operations.
