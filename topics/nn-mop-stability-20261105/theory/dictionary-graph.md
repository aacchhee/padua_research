# PD-T445 — positive ratio-graph encoding

ID kind: PD-T. Aliases: ratio graph; mixed-test positive measure.
Split from: none (supporting result for dictionary-target.md).
Split into: none. Elementary background result (PD-T445); no novelty claim.

## Statement

For every finite N>=1, distinct real x_l and strictly positive weights
w_(1,l),w_(2,l), define phi_l=w_(2,l)/w_(1,l) and the positive measure
rho=sum_l w_(1,l) delta_(x_l,phi_l) on R². For every real polynomial P(x)
and nonnegative integers n,m, the type-II conditions

    sum_l w_(1,l) x_l^k P(x_l)=0, 0<=k<n,
    sum_l w_(2,l) x_l^k P(x_l)=0, 0<=k<m

are exactly the equations <P,x^k>_rho=0 (k<n) and
<P,y*x^k>_rho=0 (k<m). Thus, when the usual mixed system is normal,
the original monic MOP is recovered by these two test families on a positive
bivariate measure. No normality or full total-degree positivity is implied.

## Definitions and assumptions

The inner product denotes sum_l w_(1,l)F(x_l,phi_l)G(x_l,phi_l).
It is positive definite on functions on the graph nodes, and positive
semidefinite on all polynomials; it is definite on Pi_d only if evaluation
on those nodes is injective. P is embedded as a function independent of y.
An interpolating polynomial phi(x) through the finite phi_l exists since
the x_l are distinct; no bound on its degree beyond N-1 is asserted.

## Status by part

Overall status: PROVED, elementary analytic identity (developer).
This supporting encoding does not turn the broader OPEN dictionary/transfer
target into PARTIAL. Candidate graph encoding retained; literal total-degree
identification has the separate scoped obstruction below.

## Depends on

Only the defining MOP conditions (PD-T286's notation) and elementary finite
sums. No theorem of graph orthogonal polynomials or external publication is used.

## Proof

The first inner product is the first defining sum. In the second inner
product replace phi_l by w_(2,l)/w_(1,l), so the product of the mass and phi_l
is w_(2,l). This proves both implications, for every P and every test index.
Positive masses give positivity on node-value functions. Definite total-degree
Gram matrices require injectivity of their evaluation map, a separate condition.

## Checks

../code/dictionary_probe.py checks one rational four-node instance; its finite
observations are MEASURED support only, not premises of this written proof.
Exact command, hashes and limits: ../attempts/D6.md. Completed independent reconstruction: audit-01.md, priority9.

## Sources and scope

Predecessor PD-T286 is the exact moment baseline. This is a direct encoding
of that baseline, not a new solvability theorem, stability theorem or claim
that both NN index directions multiply by the coordinates x and y.
The scalar input has a second coordinate determined by the weight ratio;
computing a bivariate orthonormal basis on that graph is a different task.

## Open items

Identify any grading, quotient and boundary map which turns the *whole* NN
array into the two symmetric coordinate sections, and prove stable transport.
See dictionary-target.md. The explicit counterexample in
[dictionary-obstructions.md](dictionary-obstructions.md) kills only the literal
standard total-degree identification for P_(1,1).

## History

2026-11-05, Codex, dispatched gpt-6.1-sol medium; rules/source
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. First D6 round; no final ID allocated.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `PD-T?nn-mop-stability-codex-D6-graph` → `PD-T445`.
