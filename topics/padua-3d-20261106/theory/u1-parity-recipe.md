# PD-T?padua-3d-20261106-codex-usable-U1-recipe — an explicit parity moment solver

ID kind: PD-T. Aliases: known parity WLS recipe; retain extra measurements.
Split from: none; operational restatement of the known T10 parity theorem.
Split into: none. No final ID allocated.

## Statement

For every integer n>=1 set m=(n,n+1,n+1). Enumerate lexicographically

`I_m={i:0<=i_j<=m_j, i_1=i_2=i_3 (mod2)}`.

Set `x_i=(cos(pi i_1/m_1),cos(pi i_2/m_2),cos(pi i_3/m_3))` and
`w_i=product_j b_j(i_j)/(2 product_j m_j)`, where b_j is1 at0 or m_j,
and2 otherwise. Every weight is positive and their sum is1. Let
`φ_α=2^(#{j:α_j>0}/2) product_j T_αj`, |α|<=n. Then weighted
least-squares coefficients are exactly

`c_α=sum_i w_i φ_α(x_i)y_i`, followed by halving only `c_(n,0,0)`.

This reproduces every polynomial of total degree<=n. The node count is

`M=(n+1)(n+2)^2/4` for even n,

`M=(n+1)(n²+4n+5)/4` for odd n.

Thus M/N<3/2 for all n>=1 and M/N tends3/2, where N=binom(n+3,3).
For equal orders m=(n+1,n+1,n+1), the same enumeration/weights have
Gram I and need no halving. Both operators P satisfy
`||P f||_(L²(product Chebyshev))<=||f||_infinity` and, for continuous f,
`||f-Pf||_L²<=2 inf_(p in Pi_n)||f-p||_infinity`.

## Definitions and assumptions

All functions and data are real. Continuous norms use product Chebyshev
probability, and the displayed φ form its orthonormal basis. P is the
linear map from finite samples using precisely the displayed coefficients.
The cube is [-1,1]^3. Positive point masses are the folded Haar measure,
not Lebesgue cubature weights. No observation-noise assumption is required.

## Status by part

Overall status: **PROVED**, known-mechanism consequence with no novelty
claim. Every displayed quantifier is analytic, not a floating rank claim.
The equal-order family is an explicit control. Its finite implementation
and practical errors are separate MEASURED claims.

## Depends on

[The existing local parity Gram theorem](t10-parity-log4.md): the
anisotropic Gram is I+ee^T with e indexing(n,0,0); equal orders have I.
Its locally written annihilator argument is the only mathematical
dependency. No log³ source theorem is needed for this statement.

## Proof

The source theorem's Haar group is the union of rectangular angle grids
`2pi r_j/m_j` and `pi(2r_j+1)/m_j`. A folded angle in[0,pi] is
`pi i_j/m_j`; its index has even parity in the first grid and odd parity
in the second. Interior angles have two preimages in each relevant axis,
endpoints one. Thus each physical node has exactly product b_j preimages
in the group of size2 product m_j, proving the weight formula, positivity
and unit mass. Coordinatewise strict monotonicity of cosine on[0,pi]
shows all enumerated physical nodes are distinct.

The number of even indices along an axis is floor(m_j/2)+1 and of odd
indices is ceil(m_j/2). Therefore M is the product of even counts plus
the product of odd counts. Substituting n=2r or2r+1 gives the stated
formulas. Dividing by N gives respectively
`(3/2)(n+2)/(n+3)` and
`(3/2)(n²+4n+5)/((n+2)(n+3))`, both below3/2 with limit3/2.

Writing V_iα=φ_α(x_i), W=diag(w_i), the source Gram identity gives
`G=V^T W V=I+ee^T`. Hence `G^−1=I−ee^T/2`, proving the coefficient
formula, uniqueness and exact reproduction. Equal orders use G=I.

For either family G>=I. Put Q=W^(1/2)V G^(−1/2), so Q^T Q=I. The
coefficient vector is `G^(−1/2) Q^T W^(1/2)y`, whose Euclidean norm is
at most `||W^(1/2)y||_2<=||y||_infinity`. Continuous orthonormality
identifies this norm with ||Pf||_L². For any p inPi_n, reproduction and
the probability-measure bound imply
`||f-Pf||_L² <= ||f-p||_L² + ||P(f-p)||_L² <=2||f-p||_infinity`.
Taking the infimum completes the proof.

## Checks and sources

Protocol: [usable1](../usable1.md), C1. The producer
`code/u1_usable.py` exposes `parity_nodes`, `parity_fit` and `basis`.
Numerical checks and independent reruns are recorded in the separate
operational/comparison record; they are not premises of this proof.
LIT322/323/381 identify known cubature/hyperinterpolation predecessors
with their inherited coverage limits. No historical novelty claim.

## Scope and open items

This is explicit oversampled approximation. It is not N-node interpolation,
an optimal-node theorem, a uniform-measure result, or a new hyperinterpolation
mechanism. Dense construction/application costs O(MN) arithmetic and O(MN)
storage in the supplied implementation; the formula can stream columns,
but no implemented streaming/FFT speedup is claimed. Exact formulas do
not certify a binary64 implementation's errors. Independent checking of
the current implementation and the actual practical tradeoff remain separate.

## History

2026-11-07, Codex developer, assigned Sol xhigh; input/rules
38227202bc6908d5a5a874950145761a8ca4312f. Gate published before generation;
the initial proof draft preceded experiments. Actual protocol publication
and executed outcomes are recorded in usable1.md.
