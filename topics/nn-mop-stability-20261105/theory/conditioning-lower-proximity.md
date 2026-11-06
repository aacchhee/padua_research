# PD-N162 — one inverse NN divisor does not govern proportionality

ID kind: PD-N. Aliases: fixed-N G3 obstruction; normalized alternating
binomial direction; higher-order measure-proximity sensitivity.
Split from: the D1 G3 single-inverse-divisor candidate. Split into: none.

## Statement

Fix any integer N>=4 and put M=N−1. On nodes z_k=2k/M−1, k=0,...,M,
use exact binomial weights with parameters

    p1=2/5,   p2=q=2/5+delta,   0<delta<=1/10.

Let kappa_N(delta) be the local induced condition of the full NN triangle,
with independent absolute node perturbations of scale one, componentwise
relative weights, and the maximum of the four relative field sup errors.
Let d_min be the smallest absolute b2−b1 among interior sites |nu|<=N−2.
Then all required indices are normal and

    d_min=2delta/M,
    kappa_N(delta)>=10 q^M/[M delta^(M−1)],
    kappa_N(delta)d_min>=20 q^M/[M^2 delta^(M−2)].             (1)

In particular kappa_N(delta)d_min tends to infinity as delta decreases to
zero at each fixed N>=4. Thus the proposed description

    kappa_N(delta)=O(1/d_min),     delta→0+, N fixed,

is false on this family. A fortiori a two-sided proportionality law with
constants independent of delta is false. The constants may depend on N;
that does not repair the disproved fixed-N upper bound.

## Status, disposition and dependencies

Overall status: PROVED (written proof; completed checks in independent-checks-02.md
and audit-01.md). Candidate disposition: REJECTED: refuted
for the single inverse-minimum-divisor growth mechanism in this exact
parameter range and input/output metric. This is a scoped negative result,
not a rejection of NN reconstruction, a sharp conditioning theorem, or
more detailed explanations involving the full recursion.

Dependencies: PD-T286/289, conditioning-local.md, and the elementary
normality/scalar-polynomial/NN-coefficient derivations in
conditioning-lower-krawtchouk.md. No primary-source theorem or numerical
fit is used. The original G3 prediction is preserved, not rewritten.

## Negative-result scope

Attempted mechanism: the pre-registered G3 single inverse-minimum-divisor
upper/proportionality law. Parameter range: every fixed N>=4, p1=2/5,
p2=2/5+delta with0<delta<=1/10, the normal common-support binomial data
and mixed-input/field-sup output metric in the statement. No singular
endpoint or Hahn conclusion is included.

## Proof

Use the integer node coordinate k first. Full normality follows from the
exponential-polynomial Chebyshev argument already written in the cited
lower-bound proof, since the ratio of distinct binomial weights is a
positive exponential. For every 0<delta<=1/10 the exact coefficients (5)
of that proof apply. Their difference and second diagonal coefficient in
z coordinates are

    d_(n,m)=(2delta/M)(M−n−m),
    b_(n,m,2)=(2q−1)(1−(n+m)/M)+(1/5)n/M+(1−2q)m/M.

The latter is an affine combination over the triangle of the vertex
values 2q−1,1/5,1−2q. All lie in [−1/5,1/5], and n=M attains 1/5.
Thus ||b2||_infinity=1/5, and the interior d minimum is 2delta/M.

Let K_j be the monic scalar polynomials for Bin(M,p1), defined by

    K_j(k)=j![t^j](1+(1−p1)t)^k(1−p1t)^(M−k).

Direct binomial summation gives

    E_q K_j=(M)_j(q−p1)^j=(M)_j delta^j.                   (2)

At the terminal index (M−1,1), orthogonality to the first measure through
degree M−2 implies

    P=K_M−c K_(M−1),    c=E_q K_M/E_q K_(M−1).

Indeed K_0,...,K_M are an orthogonal basis, leaving exactly these two
basis vectors, and monicity fixes the K_M coefficient. The denominator
is M!delta^(M−1)>0 by (2). This representation remains valid when only
the second weights are perturbed sufficiently little.

Put r=(1−q)/q>=1, and choose the relative second-weight direction

    zeta_k=(−r)^k/r^M.

Its maximum absolute value is one (attained at k=M), and

    w_(2,k) zeta_k=q^M binom(M,k)(−1)^k.

Therefore its mass is zero and it annihilates every polynomial of degree
less than M, by the elementary Mth finite-difference identity. On monic
K_M it gives (−q)^M M!. It follows by differentiating the quotient c that

    |dot c|=q^M/delta^(M−1).

The terminal successor is the fixed support polynomial. Its subleading
coefficient does not vary, and the subleading coefficient of P varies by
−dot c. Thus |dot b2|=(2/M)|dot c| after scaling to z. Dividing by the
field scale 1/5 gives the second inequality in (1). The perturbation has
input norm one, leaves the nodes and first weights fixed, preserves mass
exactly, and retains positive weights for |epsilon|<1. Hence it is
admissible for the stated induced condition. Multiply by d_min to finish.
Since q>=2/5 and M−2>=1, the final lower bound diverges as claimed.

## Scope and checks

This is an all-delta fixed-N conclusion for N>=4; no asymptotic equality,
upper growth law, statement at the singular endpoint delta=0, or theorem
for the Hahn family follows. The result applies also to a fixed-mass
restriction with the same coordinate perturbation bounds, since its
witness has exactly zero mass. It does not identify error realized by any
floating-point algorithm.

Finite independently executed checks are recorded in attempts/D1-hard.md
and the supplementary independent report when available; none is a proof
premise. 2026-11-05: coordinator supplied the normalized-parity extension;
bounded D1-hard developer reconstructed its factors and wrote this proof.
Rules/source 823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1; requested allocation
gpt-6-astra ultra under handoff01. No Git or shared-file writes.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `PD-N?nn-mop-stability-codex-D1-hard-01` → `PD-N162`.
