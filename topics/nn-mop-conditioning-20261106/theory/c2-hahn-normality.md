# PD-T?nn-mop-cond-codex-C2-02 — all-N Hahn normality and subleading coefficients

ID kind: PD-T. Aliases: shifted-beta row basis; adjacent Cauchy kernel;
Hahn integer/half-integer normality; exact b-field formula.
Split from: none. Split into: none.

## Statement

For every integer N>=2, M=N-1, on k=0,...,M, put

    alpha1=1, alpha2=3/2,
    W_(s,k)=(alpha_s+1)_k/k! * (2)_(M-k)/(M-k)!,
    Z_s=(alpha_s+3)_M/M!, w_(s,k)=W_(s,k)/Z_s.

Here (a)_r is the rising factorial, (a)_0=1. These are exactly the
PD-T290 Hahn input weights, before z=2k/M-1 scaling. Every mixed
index of degree <=N is normal.

For n,m>=0, t=n+m<=M, the coefficient tau_(n,m) of k^(t-1) in the
monic type-II polynomial is (with tau_(0,0)=0)

    R_(n,m)=(t+alpha1+1)(t+alpha2+1)
               /((t+n+alpha1+1)(t+m+alpha2+1)),
    tau_(n,m)=-t(t-1)/2 +(M-t+1)(1-(t+1)R_(n,m)).          (1)

For total degree M+1 the polynomial is the common support polynomial,
so tau=-M(M+1)/2. All NN diagonal fields are consequently given by

    b_(nu,j)=2(tau_nu-tau_(nu+e_j))/M-1.                  (2)
In particular their field scales obey

    0<||b1||_sup, ||b2||_sup <=2M+3.                      (3)

The actual small field scales are not asserted to attain the loose
polynomial upper bound. Scaling the nodes affinely preserves normality.

## Definitions and assumptions

Finite normal common-support monic MOPs and NN arrays use PD-T286.
Normality here is a conclusion for these exact weights, not a positivity
inference for arbitrary inputs. The parameter values and gamma=1 above
are essential for the displayed adjacent-kernel formula. Exact arithmetic.

## Status by part

Overall status: PROVED (written proof).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Every N>=2, all indices through N normal | PROVED | Exact transformed determinant below |
| Formula (1), terminal tau and diagonal fields | PROVED | Rational interpolation and two residues below |
| Polynomial upper bound (3) | PROVED | Elementary coefficient estimate below |

Candidate disposition: retained standard family-formula variant within
IDEA?nn-mop-cond-codex-C2-03. This extends PD-T436's finite normality scope
by an analytic proof; it does not edit or relabel that finite theorem.
No historical-priority claim and no sharp conditioning-rate conclusion.

## Depends on

PD-T286 for monic moment systems and b=tau difference. The identities
below are derived directly from the input weights, with no unread
Hahn recurrence or normality theorem imported.

## Proof

### Transform the moment rows

The elementary convolution

    sum_(k=0)^L (u)_k/k!*(v)_(L-k)/(L-k)!=(u+v)_L/L!

follows by multiplying the Taylor series of (1-z)^(-u) and
(1-z)^(-v). Let L_s denote the unnormalized W_s functional. Replace
the i-th row test k^i by (k+alpha_s+1)_i, an invertible triangular
change, and replace the j-th column k^j by (-k)_j, another invertible
triangular change. With x=alpha_s+i, direct index shifting gives

    L_s((k+alpha_s+1)_i(-k)_j)
       =(-1)^j (alpha_s+1)_(i+j)
                    *(alpha_s+i+j+3)_(M-j)/(M-j)!
       = [Gamma(x+M+3)/Gamma(alpha_s+1)]
         *[(-1)^j/(M-j)!]
         /[(x+j+1)(x+j+2)].                              (4)

This is required only for 0<=j<=M; all factors are well defined.
Normalization by Z_s only rescales rows by positive constants.

At an index (n,m) of degree t<=M+1, the t row parameters are

    1,2,...,n; 3/2,5/2,...,m+1/2.

They are pairwise distinct and positive. Thus the moment determinant
is nonzero once the t-by-t kernel determinant for j=0,...,t-1 is.

### Exact kernel determinant

For distinct x_1,...,x_t with no denominator zero,

    det_(i=1..t,j=0..t-1) 1/[(x_i+j+1)(x_i+j+2)]
      = (prod_(r=1)^t r!)
        *prod_(i<h)(x_h-x_i)
        /prod_(i=1)^t (x_i+1)_(t+1).                     (5)

For t=0 use the empty determinant 1. To prove (5), multiply each row
by D_t(x_i)=(x_i+1)_(t+1). The j-th numerator is the degree-(t-1)
polynomial P_j(x)=D_t(x)/((x+j+1)(x+j+2)). Its evaluation determinant
is the Vandermonde in the x_i times the determinant of its coefficient
columns. To find that constant, evaluate the P_j at x=-r, r=1,...,t.
Only columns j=r-2,r-1 can be nonzero; hence the matrix is lower
bidiagonal. Its diagonal is

    P_(r-1)(-r)=(-1)^(r-1)(r-1)!(t+1-r)!.

The evaluation determinant divided by the Vandermonde at -1,...,-t
is prod_(r=1)^t r!, proving (5). In particular the constants at
t=1,2,3,4 are 1,2,12,288; the product is through t, not t-1.
Formula (4) now proves every required normality, including t=M+1.

### Recover the subleading coefficient

Fix t=n+m<=M and write the monic polynomial as

    P(k)=sum_(j=0)^t c_j(-k)_j, c_t=(-1)^t.

Define the rational function

    F(x)=sum_(j=0)^t c_j(-1)^j/(M-j)!
                                     /[(x+j+1)(x+j+2)].

By (4), F vanishes at every row parameter x_i. Its denominator is
(x+1)_(t+2), and its numerator has degree at most t. Therefore

    F(x)=C*prod_(i=1)^t(x-x_i)/(x+1)_(t+2).               (6)

Only j=t contributes a pole at x=-t-2. The residue on the sum side
is -1/(M-t)!, and that on the product side is
-C*prod_i(t+2+x_i)/(t+1)!. Thus

    C=(t+1)!/((M-t)!*prod_i(t+2+x_i)).                    (7)

At x=-t-1 the sum-side residue is

    1/(M-t)! - c_(t-1)(-1)^(t-1)/(M-t+1)!,

and the product-side residue is C*prod_i(t+1+x_i)/t!.
For t>=1, equations (6),(7) give

    c_(t-1)(-1)^(t-1)
      =(M-t+1)(1-(t+1)*prod_i (t+1+x_i)/(t+2+x_i)).       (8)

The product in (8) telescopes separately on each parameter block to
R_(n,m) in (1). The coefficient of k^(t-1) in (-1)^t(-k)_t is
-t(t-1)/2, proving (1) for t>=1. For t=0, the expression on the
right of (1) is zero directly, agreeing with the defined tau_0.
At degree M+1 the monic support polynomial is orthogonal to every
test because it vanishes at every node; normality proves uniqueness.
Its subleading coefficient is -M(M+1)/2. PD-T286 and affine scaling
then prove (2).

### A loose polynomial field-scale bound

Each factor in the untelescoped product R is in (0,1], so for t>=1

    |1-(t+1)R|<=t,
    |tau_(n,m)|<=t(t-1)/2+t(M-t+1)
                =t(2M-t+1)/2<=M(M+1)/2.

This also covers t=0 and the terminal support coefficient. Each B_j
is a difference of two such coefficients, so |B_j|<=M(M+1), and
|2B_j/M-1|<=2M+3. The b2 origin is 1/9, so its scale is positive.
For b1, if M=1 use the terminal site (0,1), whose value is -1/9.
For M>=2, formula (1) at (0,1),(1,1) gives b1_(0,1)!=0:

    b1_(0,1)=(36-91M)/(495M).

Thus both b scales in (3) are positive. The a scales are positive
from the first scalar marginal variances, so the PD-T432 relative
fieldwise metric is well defined for this family at every N>=2.

## Checks

`../code/c2_hahn_checks.py` compares (1) and (5) with exact rational
defining moments at finite sizes and checks the terminal annihilator
used by the separate lower-bound file. Actual scope, source hashes
and outputs are in `../c2-hahn-checks.json`; no check is a premise of
the written proof. Independent reruns and Claude audit are separate.

## Sources

The exact PD-T290 input definition and PD-T286. No new external source
or unread closed-form Hahn result is cited.

## Scope and open items

Only this gamma=1, alpha1=1,alpha2=3/2 family is asserted. The matrix
identity suggests parameter extensions, which are not claimed here.
It supplies normality and exact diagonal values, not a sharp Jacobian
upper or the measured conditioning base near11.8. PD-T448 remains OPEN.

## History

2026-11-06: Codex gpt-6.1-sol xhigh, local rules/source
`76ba4214b100c86a44941f5e9a662ce9ce48efb8`; coordinator topic pin
`b4a04981d42c7cd872957facf5e3995e4096ca67`. Prospective gate C2-03.
No predecessor edit, Git mutation, or shared registry write.
