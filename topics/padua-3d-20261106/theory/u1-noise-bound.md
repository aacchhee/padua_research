# PD-T?padua-3d-20261106-codex-usable-U1-noise — covariance of the parity solver

ID kind: PD-T. Aliases: iid observation risk; fixed total sampling budget.
Split from: none. Split into: none. No final ID allocated.

## Statement and definitions

Use either explicit parity recipe of [U1 recipe](u1-parity-recipe.md),
with M nodes, orthonormal evaluation matrix V, positive W, Gram G and
coefficient map `C_W=G^−1 V^T W`. Suppose observations are
`y_i=f(x_i)+epsilon_i`, with independent, mean-zero errors of common
finite varianceσ². Then the continuous integrated squared difference
between noisy and noiseless reconstructions has expectation

`sigma² tr(C_W C_W^T) <= sigma² w_max tr(G^−1)`.

For anisotropic orders m=(n,n+1,n+1),

`tr(G^−1)=N−1/2`,

`tr(C_W C_W^T) <= 4(N−1/2)/(n(n+1)^2)`.

For equal orders m=(n+1,n+1,n+1), the corresponding upper bound is
`4N/(n+1)^3`. These hold for every integer n>=1. The upper bounds tend
2/3 as n tends infinity; this is a bound on iid noise error variance,
not on deterministic approximation bias.

For a common integer total budget B divisible by all compared node
counts, average B/M independent observations at each node. Then the
preceding exact risk becomes
`(sigma²/B) M tr(C_W C_W^T)`. The factor M is essential when comparing
different counts at equal total sampling effort. No equality of
function-evaluation or solver costs is inferred from a noise normalization.

## Assumptions and status

Overall status: **PROVED**, elementary known covariance algebra applied to
the explicit known parity family. Independence may be weakened to an
uncorrelated diagonal covariance; no Gaussian assumption is needed.
Gaussian simulation in the experiment is an explicit narrower model.
The exact-model identities are separate from binary64 measurements.

## Depends on

The explicit construction and exact Grams in [U1 recipe](u1-parity-recipe.md),
which depend on the local T10 parity proof. No external noise theorem,
finite computation or imported log³ theorem is used.

## Proof

The coefficient perturbation is C_W epsilon. Continuous orthonormality
gives its integrated squared norm as `||C_W epsilon||²`; expectation is
σ² times the trace of C_W C_W^T. Since positive diagonal W satisfies
`W²<=w_max W`, congruence gives

`C_W C_W^T =G^−1 V^T W² V G^−1 <=w_max G^−1`.

Taking traces proves the first inequality. For anisotropic G=I+ee^T,
one inverse eigenvalue is1/2 and all N−1 others are1. For equal orders
all N eigenvalues are1. Each folded multiplicity is at most8, so
`w_max<=8/(2 product m_j)=4/product m_j`; substitution gives the two
bounds, including n=1 even when that multiplicity bound is not attained.
The limits follow from N=binom(n+3,3).

Averages of B/M independent observations have varianceσ²M/B. Substituting
this variance proves the fixed-total-budget identity. Common B values
exist, for example any multiple of the least common multiple of the
finite node counts under comparison. This interpretation makes no
fractional-observation assumption.

## Checks, sources and evidence

Protocol: [usable1](../usable1.md). Producer receipts report the trace
directly from the actual coefficient arrays, its M-normalized version,
the analytic bound and one seeded realization. Independent reruns are
separate. No computation is a premise of this analytic proof. Known
least-squares/MZ/Christoffel context is attributed in the shared gate;
no priority claim is made.

## Scope and open items

This proves a risk upper bound for common independent observation noise,
not universal dominance over an interpolant or an asymptotic lower bound.
It does not imply that every target function has smaller approximation
error, nor cover correlated/adversarial noise or arbitrary cost per node.
The finite comparator risks and practical costs are MEASURED elsewhere.

## History

2026-11-07, Codex, assigned Sol xhigh. Gate published before generation;
protocol publication and actual runs are recorded in usable1.md.
