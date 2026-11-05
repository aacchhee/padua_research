# PD-N?nn-mop-stability-codex-D6-literal — two scoped standard-grade failures

ID kind: PD-N. Aliases: missing graph moment; two-sheet annihilator.
Split from: none. Split into: none. These two elementary obstructions concern
explicit dictionaries, not bivariate transfer in general. Final allocation
and possible claim-level split are coordinator/auditor decisions.

## Statement

(G) For x=(0,1,2,3), w1=(1,1,1,1), w2=(1,2,4,8), the unique monic
P_(1,1) does not belong to the orthogonal complement of Pi_1 in Pi_2 for the
ratio-graph measure of dictionary-graph.md: <P_(1,1),x>_rho=-30/23.

(C) For every N>=1, distinct real x_l and strictly positive w1,w2, the
labelled-copy measure sigma=sum_l w_(1,l)delta_(x_l,0)+
w_(2,l)delta_(x_l,1) has singular Gram matrix on the full standard Pi_2.
It cannot directly meet PD-T057's full Pi_d positive-definiteness hypothesis
for any d>=2 without quotienting, deflation or changing the representation.

## Definitions / assumptions

Pi_d is the full bivariate total-degree space, with polynomials regarded as
formal polynomials before evaluation. G concerns precisely the ratio-graph
mass choice and literal embedding P(x,y)=P_(1,1)(x), unchanged degree two.
It only needs the displayed (1,1) index normal; it makes no all-triangle
normality assertion. C concerns precisely y in {0,1} and no deflation.

## Status by part

Overall status: PROVED (direct analytic computations below; audit pending).

| Part | Status | Disposition |
|---|---|---|
| G | PROVED | Literal standard-grade P_(1,1) identification REJECTED: refuted for this input |
| C | PROVED | No-deflation full Pi_d (d>=2) two-sheet realization REJECTED: failed |

Positive ambient encodings remain retained. Their broader transfer targets
are OPEN/deferred, not REJECTED and not PARTIAL.

## Negative-result scope

Attempted mechanism: IDEA?nn-mop-stability-codex-D6-graph literal standard
polynomial identification; IDEA?nn-mop-stability-codex-D6-copies with full Pi_2.
Parameters: one explicit four-node instance for G; arbitrary positive finite
two-sheet inputs for C. No claim against other graph masses, changed test
spaces, vector polynomials, extra sheets, boundary operators or stable NN solvers.
PD-N100's finite fixed-site scope is unchanged and not used as a proof premise.

## Depends on

Defining MOP equations (PD-T286) and the explicit ratio-graph construction;
PD-T057 supplies only the positivity hypothesis against which C is compared.

## Proof

G: The first four moments of w1 are (4,6,14,36); those of w2 are
(15,34,86,232). The two coefficient equations for P=x²+c1*x+c0 are
4c0+6c1=-14 and 15c0+34c1=-86. Their determinant is 46, and their unique
solution is c0=32/23,c1=-75/23. Consequently <P,1>_rho=0,
<P,y>_rho=0, but

    <P,x>_rho=36-(75/23)*14+(32/23)*6=-30/23 != 0.

Since x is in Pi_1, orthogonality to all of Pi_1 fails. This argument does
not require rho's full Pi_2 Gram matrix to be invertible.

C: The nonzero formal polynomial q=y²-y belongs to Pi_2 and vanishes on
every support point. Hence <q,q>_sigma=0. Its coefficient vector is a
nonzero Gram null vector; the same polynomial belongs to every Pi_d,d>=2.
This proves exactly the specified singularity and no broader impossibility.

## Checks and sources

../code/dictionary_probe.py independently computes these explicit expressions
in Fraction arithmetic as a developer diagnostic. G's Pi_1 evaluation rank
is 3; the four-node two-sheet Pi_2 rank is 5 of 6. Those finite rank claims
remain MEASURED and are not used in either analytic proof. Receipts:
../attempts/D6.md. No independent rerun or Claude audit yet. No external
source is used for either analytic identity.

## Scope and open items

The graph identity is still exact with mixed test spaces. Labelled copies
still give a positive ambient measure and exact selector moments. Neither
negative statement rules out a useful new quotient/regraded dictionary.
See dictionary-target.md. Do not infer a full bivariate no-go theorem.

## History

2026-11-05, Codex, gpt-6.1-sol medium as dispatched, source/rules
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. New scoped elementary statements;
PD-N100 and the original D6 target retained unchanged.
