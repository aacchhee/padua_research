# PD-N?nn-mop-cond-codex-response-C2-node-transfer — unweighted grid differentiation has exponential loss

ID kind: PD-N.
Aliases: C2-03 round 6; common-node unweighted transfer failure;
equispaced differentiation norm obstruction.
Split from: none; standalone home for the scoped negative statement
previously written in `c2-hahn-upper-search.md`, round 6.
Split into: none.

## Statement

For every integer M>=2 let D_M be the differentiation matrix for
interpolation of real polynomials of degree<=M on the integer grid
0,...,M. In the induced infinity norm,

    ||D_M||_infinity >= 2^M/[M(M+1)].

Consequently no constants C>0 and a in R, independent of M and p, satisfy

    max_(0<=k<=M)|p'(k)| <= C M^a max_(0<=k<=M)|p(k)|

for every M>=2 and every real polynomial p of degree<=M. In particular,
the proposed universal unweighted grid-supnorm transfer cannot supply a
polynomial-cost common-node derivative step in the C2-03 Hahn upper route.

## Definitions

Let `L_j(x)=prod_(0<=a<=M,a!=j)(x-a)/(j-a)` be the cardinal polynomial,
and `D_(k,j)=L_j'(k)`. Evaluation maps degree<=M polynomials bijectively
onto R^(M+1), so the matrix norm equals the sharp uniform grid derivative
constant over that polynomial space. Use integer-coordinate derivatives.
On z=2k/M-1 the derivative acquires only M/2, a polynomial factor.

## Assumptions

Distinct equally spaced integer nodes, degree at most M, and unweighted
supnorm on grid values and grid derivatives. The constants in the rejected
inequality must be uniform in M and in all such polynomials. No Hahn
normality assumption is required for the matrix theorem.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exponential differentiation norm lower for every M>=2 and absence of a uniform polynomial bound | PROVED | Cardinal-product proof below |

Candidate / claim disposition: REJECTED: failed for
[IDEA?nn-mop-cond-codex-C2-03-r6](../candidates-response-C2.md#ideann-mop-cond-codex-c2-03-r6--polynomial-unweighted-grid-differentiation).
Rejection reason: failed polynomial-cost universal unweighted transfer;
the stated polynomial norm inequality is refuted by the all-M lower.

## Negative-result scope

Attempted mechanism: parent C2-03, round-6 subform C2-03-r6; estimate the
exact common-node forcing `P'Q_s+P Q_s'` by uniform unweighted derivative
bounds for arbitrary degree<=M polynomials, losing at most a polynomial.
Parameter range: every M>=2 for the interpolation operator. No claim that
the actual Hahn P,Q_s attain its worst case or that every weighted transfer
has exponential loss.

## Depends on

Elementary polynomial interpolation and the binomial theorem. The Hahn
[upper-search attempt](c2-hahn-upper-search.md), equation (4), identifies
the application being rejected; it is not a premise of the norm proof.
The [terminal-rate theorem](c2-hahn-terminal-rate.md) supplies rho_H as
application context, not a premise of the operator lower.

## Checks

Response source/rules `3d5b29d`, Python 3.12.14. The unchanged
`python3 topics/nn-mop-conditioning-20261106/code/c2_hahn_upper_search.py --max-m 6`
was actually rerun to `/tmp/padua-response-c2-hahn-upper-search.json`:
75 indices, 430 polynomial values, 860 weight coordinates and 430 common
node coordinates, identical scientific payload to the committed receipt.
Code sha256
`5b2f7a4576bbe183e2156caa12faee0625b9eb9f3aed4a55a283e27d5b9555f3`;
helpers are pinned in `../c2-hahn-upper-search.json`. That checker tests
the finite common-node representation, not this norm inequality.

The response also independently formed the rational product coefficients
of L_j and differentiated at zero, with j=floor(M/2), at each M=2,...,16.
All 15 entries equalled the formula below and exceeded the claimed lower.
This supplemental finite check is not a premise of the analytic all-M
proof. The earlier [Claude audit 01](../audit-01.md) accepted the existing
attempt's scoped proof. This response extraction does not claim a new
independent audit of the record.

## Sources

No external theorem used. Cardinal differentiation is classical;
repository comparison and reading limits are in
[candidate C2-03-r6](../candidates-response-C2.md).

## Proof or evidence

Differentiating the cardinal product at k!=j gives

    D_(k,j)=(-1)^(j-k) binom(M,j)/[binom(M,k)(k-j)].

Indeed only the factor x-k survives differentiation. The ratio of the
remaining factorial products gives the displayed binomial ratio. Set
k=0 and j=floor(M/2)>=1. The central binomial coefficient is a maximum
of the M+1 nonnegative coefficients whose sum is 2^M. Therefore

    ||D_M||_infinity >= |D_(0,j)|
       =binom(M,j)/j
       >=2^M/[(M+1)j]
       >=2^M/[M(M+1)].

The matrix norm dominates every entry, and grid evaluation is a
bijection, so this is a genuine lower for the required uniform derivative
constant. For fixed C>0 and a, `2^M/[C M^(a+1)(M+1)]` tends to infinity.
Thus C M^a cannot bound that constant for every M. This proves the
negative statement and its polynomial-transfer consequence.

## Scope

The rejected transfer loses weighted pointwise correlation by taking a
norm over all grid polynomials. The operator lower does not prove a larger
Hahn condition rate, reject a correlated node estimate, or refute the
full matching-rho_H upper target. The same physical node perturbation
must still act in both weight channels in any replacement estimate.

## Open items

A weighted correlated estimate for equation (4) of the upper-search
attempt, followed by transfer to every NN field, remains OPEN. This
record supplies no replacement upper bound.

## History

2026-11-06, Codex gpt-6.1-sol high, response source `3d5b29d`: extracted
the already audited round-6 norm lower and scoped route failure, with
unchanged mathematical scope, in response to MAJOR-3. The former location
is retained as attempt history and links here. Provisional ID only.
