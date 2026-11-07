# Pruning target and standard deletion identities

Provisional target: `PD-T?padua-3d-20261106-pruning-target`.
ID kind: PD-T. Aliases: backward elimination; adaptive row deletion;
count versus quality. Split from:none. Split into:none. No final allocation.
Rules/input `6d894d50efd8167c5b10f3d5b0da4d8cf214b681`.
Codex mathematical developer, configured gpt-6.1-sol xhigh; provider runtime
metadata unexposed. [Prospective gate](pruning-gate.md).

## Statement, assumptions and status

**Main target OPEN:** find, by a prospectively specified finite algorithm,
useful subsets of the explicit trivariate parity grid with fewer sites,
preferably N=binom(n+3,3), while assessing actual amplification, physical
observation-noise risk, target error and cost against matched controls.
No all-degree constant, polylogarithmic bound or universally superior
algorithm is asserted. An acceptable near-minimal stopping point is a
legitimate finite outcome; a merely full-rank N-node endpoint is not a
quality theorem.

The identities below are **routine PROVED algebra**, written to verify
normalizations of established methods. They are not a new downdating
algorithm, research theorem, asymptotic estimate or claimed stability
analysis. They do not make the main target PARTIAL. A substantive future
positive/negative claim must receive its own durable file and provisional
ID. Finite construction measurements belong in the producer's result
record, separately from these exact identities.

All matrices below are real, full column rank, with positive fixed row
weights. Complex data may be applied to the resulting real linear map;
complex design matrices would require adjoints throughout. The continuous
output basis is orthonormal in product-Chebyshev probability unless a
different output mass matrix is stated. All deletion formulas assume the
remaining weights keep their old values; a common renormalization is
described separately. Numerical computations should use factorization
and explicit residual guards; normal-equation notation is for analysis.

## Raw observations, weights and physical covariance

Let a(x) be the N-vector of basis functions and A the M by N matrix whose
ith row is a_i^T=a(x_i)^T. Write

`W=diag(w_i)>0, V=W^(1/2) A, G=V^T V=A^T W A, S=G^(-1)`.

Weighted LS takes **raw physical values** y to coefficients

`B y, B=S A^T W`,

and the evaluated reconstruction has row

`c(x)^T=a(x)^T B, c_j(x)=w_j a(x)^T S a_j`.

The prewhitened data map is `S V^T`; it acts on `W^(1/2)y`, not on raw
values. For raw errors of covariance Sigma the exact coefficient covariance
is `B Sigma B^T`. In particular, independent equal-variance observations
give

`Cov(coefficients)=sigma² S A^T W² A S`,

`pointwise variance=sigma² sum_j c_j(x)²`,

`integrated variance=sigma² tr(B B^T)`.

These follow by applying the fixed linear map and continuous
orthonormality; the existing [U1 noise proof](theory/u1-noise-bound.md)
uses the same normalization. With an output mass matrix
`Q=integral a(x)a(x)^T dmu(x)`, the last trace is `tr(Q B B^T)` instead.
Gaussian noise is unnecessary; uncorrelated finite-variance errors suffice.
This variance compares noisy and noiseless reconstructions and contains
no approximation bias for a general target outside the polynomial space.

For **ordinary LS**, W=I and `B B^T=S`. For correctly specified GLS with
`Sigma=sigma² W^(-1)`, the covariance is also `sigma² S`. Arbitrary Haar
weights under equal-iid physical noise satisfy neither hypothesis.
Prewhitening changes their noise covariance to `sigma² W`; it does not
turn those observations into equal-iid prewhitened errors.

Multiplying every weight by t>0 changes G to tG and S to S/t, while B,
c(x), physical iid risk and the fitted function stay identical. This is
an immediate check that an arbitrarily normalized weighted Gram inverse
cannot alone be the physical iid covariance. Recomputing weights to be
equal at each count gives the same OLS map, but the inverse-trace risk
formula must then account for the chosen common factor.

The fixed-node OLS Gauss–Markov comparison is already proved in
[U1-OLS](theory/u1-ordinary-ls-blue.md). It compares linear reproducing
maps on the **same** observations. It does not prove deterministic error
or bounded-noise superiority, nor an ordering across different supports.

## Exact one-row deletion

For deletion of i put

`v_i=sqrt(w_i) a_i, h_i=v_i^T S v_i=w_i a_i^T S a_i, d_i=1-h_i`.

The matrix `H=V S V^T` is an orthogonal projector, so `0<=h_i<=1` and
`sum_i h_i=N`. The remaining Gram is `G_-=G-v_i v_i^T`. Congruence by
G^(-1/2) gives `I-u u^T`, with `||u||²=h_i`; hence

`G_->0 iff h_i<1`,

`det(G_-)/det(G)=1-h_i=d_i`.

For d_i>0, direct multiplication verifies the usual rank-one inverse:

`S_-=S+(S v_i)(S v_i)^T/d_i`,

`tr(S_-)-tr(S)=||S v_i||²/d_i`.

For raw unweighted OLS the latter is the exact integrated iid variance
increment divided by sigma². More generally its output-mass version is
`tr(Q(S_--S))=v_i^T S Q S v_i/d_i` for OLS or properly normalized GLS;
it is not an arbitrary weighted-map risk increment. The determinant ratio
and h_i are basis invariant; the unweighted trace objective corresponds
to the declared continuous orthonormal basis, not arbitrary column scaling.

If k is a surviving row, another direct substitution gives

`h_k^-=h_k+(v_k^T S v_i)²/d_i`.

Thus leverage values change after each deletion. A static initial ranking
is not the same finite procedure as adaptive elimination. The average
leverage N/M<1 ensures some rank-preserving deletion whenever M>N;
repeating proves that a full-rank N-row subset exists. This elementary
rank fact says nothing quantitative about its quality. At exactly M=N,
H=I and every h_i=1, so no further deletion preserves rank.

All identities presume an actual positive d_i; subtracting two nearly
equal floating numbers requires a guard and fresh factorization checks.
A positive computed d_i alone is not an exact rank certificate or a
roundoff theorem. Classical QR/R-factor downdating is background F3;
no relational-stability result is rederived or imported here.

## Actual Lebesgue/cardinal update

For every x and surviving j the raw cardinal coefficient after deleting i
is exactly

`c_j^-(x)=c_j(x)+c_i(x)c_j(x_i)/d_i`.

Indeed insert the rank-one inverse above in
`w_j a(x)^T S_- a_j`; its extra term is
`w_i w_j(a(x)^T S a_i)(a_i^T S a_j)/d_i`, which is the displayed product.
Here `c_i(x_i)=h_i`. Consequently the actual post-deletion Lebesgue
function is

`Lambda_-(x)=sum_(j!=i) |c_j(x)+c_i(x)c_j(x_i)/d_i|`.

This differs from both determinant loss and the squared-cardinal variance.
Leverage controls solvability; signs/cancellation of the raw cardinal row
determine bounded raw-data amplification. It would be incorrect to drop
the absolute values, include the deleted column, use the opposite sign,
or replace c_j(x_i) by a prewhitened coefficient without its weight factors.
For a finite training cloud, this formula evaluates its exact-model
post-deletion objective. It does not certify a continuous supremum.
Independent assessment clouds must remain excluded from candidate/stop
selection if they are described as held out.

For finite distinct nodes on a compact metric space, continuous bumps
extend their assigned signs. Therefore the reconstruction's norm from
bounded physical samples to continuous sup norm is
`sup_x sum_j |c_j(x)|`, as used in the existing T9 correction proof.
The actual weighted physical-noise variance still uses `sum c_j²`, not
this l1 row norm. Neither quantity determines the target approximation
bias.

## Frame bounds, minimal interpolation and the missing norm transfer

With the stated continuous orthonormal basis, eigenvalues of G bound
`sum_i w_i |p(x_i)|²` against `||p||_L²²`. This is an L² sampling statement.
The elementary estimate

`sum_j |c_j(x)| <= sqrt(sum_j w_j) sqrt(a(x)^T S a(x))`

follows by Cauchy–Schwarz: the weighted sum of squared kernel entries is
`a(x)^T S G S a(x)=a(x)^T S a(x)`.
Even a bounded frame constant leaves the continuous Christoffel factor
`||a(x)||²` in a generic sup-norm bound. Frame bounds therefore do not
automatically yield the desired polylogarithmic Lebesgue bound. Numerical
condition, frame constants, variance and amplification must be reported
under their own definitions.

When M=N and A is invertible, `B A=I` implies `B=A^(-1)`, independent
of positive W. Reweighting that fixed minimal set cannot improve its
interpolant, Lebesgue function or raw iid noise map. It can alter matrix
conditioning under a particular scaling, which is a different quantity.

The existing [T9-05](theory/t9-projection-extraction.md) has the precise
additional requirement: if H is a projection with coefficient functions
h_y, the N by N matrix C_ij=h_(x_j)(x_i) gives an interpolant only when
invertible, with `||I_X||<=||H|| ||C^(-1)||_infinity`. Neither full rank
nor a small initial projection norm bounds this correction factor.
The frozen T10 extraction failures concern their named rules and supports,
not all adaptive deletions; see [gate](pruning-gate.md).

A two-column exact example illustrates the rank limitation without a
pruning impossibility claim. For e>0 let

`A=[[1,0],[0,1],[1,e]]`.

Full OLS inverse trace is `(e²+3)/(e²+2)`, bounded as e tends0. Deleting
the middle row preserves rank but gives trace `(e²+2)/e²`, which diverges.
This is a routine arbitrary-matrix illustration, not a parity-grid
counterexample and not a failure theorem for minimum-leverage or
amplification-aware deletion.

## Checks actually run

2026-11-07, `python - <<'PY'` inline SymPy exact check from repository
root; no pruning construction, random sampling or numerical inversion.
The following reproduces its inputs and assertions:

```python
import sympy as s
A=s.Matrix([[1,-2,4],[1,-1,1],[1,0,0],[1,1,1],[1,2,4]])
w=list(map(s.Rational,[1,2,3,4,5]))
q=s.Matrix([[1,s.Rational(2,3),s.Rational(4,9)]])
for weights in [[s.Rational(1)]*5,w]:
    W=s.diag(*weights); G=A.T*W*A; S=G.inv()
    B=S*A.T*W; c=q*B
    for i in range(5):
        ids=[j for j in range(5) if j!=i]
        a=A.row(i).T; h=weights[i]*(a.T*S*a)[0]; d=1-h
        Am=A[ids,:]; Wm=s.diag(*[weights[j] for j in ids])
        Gm=Am.T*Wm*Am; Sm=Gm.inv(); Bm=Sm*Am.T*Wm
        assert d>0 and Gm.det()==G.det()*d
        assert Sm==S+weights[i]*(S*a)*(a.T*S)/d
        assert s.trace(Sm)-s.trace(S)==weights[i]*((S*a).T*(S*a))[0]/d
        for col,j in enumerate(ids):
            assert (q*Bm)[col]==c[j]+c[i]*(A.row(i)*B[:,j])[0]/d
    assert B*A==s.eye(3)
    if weights==w:
        assert B*B.T!=S
        assert (7*G).inv()*A.T*(7*W)==B
```

Output: PASS,10exact deletion cases and40raw-cardinal entries; weighted
iid covariance differs from Gram inverse; common weight-scale invariance.
The same invocation symbolically computed both e-example traces above.
The displayed reproducer retains the same assertions/input with cosmetic
whitespace and a list-construction change. A separate metadata command,
`python - <<'PY'` with `import sympy; print(sympy.__version__)`, returned
SymPy `1.14.0` in this environment.
These checks supplement the algebra, not a computer-assisted new theorem.
No independent rerun by this worker, pruning quality, hardware timing,
exact parity-subset rank or new source-paper verification is claimed.

## Dependencies, sources, open items and history

Depends on elementary projection/rank-one algebra and the already stated
continuous orthonormal normalization. U1 covariance/OLS proofs and T9-05
are explicitly linked above. LITERATURE background F3/IDEA027/209 and
classical downdating source coverage is recorded in pruning-gate; no
uninspected source theorem is a proof premise.

Next unresolved step: publish a concrete cheap pruning protocol with
prospective scores, thresholds, count checkpoints and matched QR/localdet/
U1 controls, then independently check actual maps and resulting
count-quality tradeoffs. Ordinary iid risk increases under OLS deletion
at fixed variance per retained observation; saving sites is the benefit
being traded against it. For a retained map B, independent repeats averaged
at site i with integer count r_i give risk
`sigma² sum_i ||B[:,i]||²/r_i`. A fixed total budget B_total gives the factor
M/B_total only for ideal balanced replication r_i=B_total/M (an actual
integer design only when divisible); it is not the optimal-integer-allocation
formula. One-observation-per-site, ideal balanced and actual integer-budget
results must stay separate.

2026-11-07: known identities verified after the current complete gate;
main target remains OPEN. No research-round count, final allocation,
shared registry, old proof, handoff or Git state changed by this worker.
