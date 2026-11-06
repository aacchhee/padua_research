# PD-N167 — ratio-graph standard-grade obstruction

ID kind: PD-N. Aliases: missing graph moment.
Split from: none; this file retains G from the original combined G/C record.
Split into: C, now [dictionary-copy-obstruction.md](dictionary-copy-obstruction.md).
The retained G claim concerns one explicit dictionary, not bivariate transfer in general.

## Statement

(G) For x=(0,1,2,3), w1=(1,1,1,1), w2=(1,2,4,8), the unique monic
P_(1,1) does not belong to the orthogonal complement of Pi_1 in Pi_2 for the
ratio-graph measure of dictionary-graph.md: <P_(1,1),x>_rho=-30/23.

## Definitions / assumptions

Pi_d is the full bivariate total-degree space, with polynomials regarded as
formal polynomials before evaluation. G concerns precisely the ratio-graph
mass choice and literal embedding P(x,y)=P_(1,1)(x), unchanged degree two.
It only needs the displayed (1,1) index normal; it makes no all-triangle
normality assertion. The separate C record retains its y-in-{0,1}, no-deflation scope.

## Status by part

Overall status: PROVED (direct analytic computation below).

| Part | Status | Disposition |
|---|---|---|
| G | PROVED | Literal standard-grade P_(1,1) identification REJECTED: refuted for this input |

Positive ambient encodings remain retained. Their broader transfer targets
are OPEN/deferred, not REJECTED and not PARTIAL.

## Negative-result scope

Attempted mechanism: IDEA-547 literal standard
polynomial identification.
Parameter range: the explicit four-node input in statement G. No claim against other graph masses, changed test
spaces, vector polynomials, extra sheets, boundary operators or stable NN solvers.
PD-N100's finite fixed-site scope is unchanged and not used as a proof premise.

## Depends on

Defining MOP equations (PD-T286) and the explicit ratio-graph construction;
The C comparison with PD-T057 is preserved in the separate copy-obstruction record.

## Proof

G: The first four moments of w1 are (4,6,14,36); those of w2 are
(15,34,90,250). The two coefficient equations for P=x²+c1*x+c0 are
4c0+6c1=-14 and 15c0+34c1=-90. Their determinant is 46, and their unique
solution is c0=32/23,c1=-75/23. Consequently <P,1>_rho=0,
<P,y>_rho=0, but

    <P,x>_rho=36-(75/23)*14+(32/23)*6=-30/23 != 0.

Since x is in Pi_1, orthogonality to all of Pi_1 fails. This argument does
not require rho's full Pi_2 Gram matrix to be invertible.

## Checks and sources

../code/dictionary_probe.py independently computes these explicit expressions
in Fraction arithmetic as a developer diagnostic. G's Pi_1 evaluation rank
is 3; the four-node two-sheet Pi_2 rank is 5 of 6. Those finite rank claims
remain MEASURED and are not used in this analytic proof. Receipts:
../attempts/D6.md. Completed separate checks are in [independent-checks-01.md](../independent-checks-01.md),
and the independent Claude reconstruction is in [audit-01.md](../audit-01.md), priority 9.
No external source is used for this identity.

## Scope and open items

The graph identity is still exact with mixed test spaces. Labelled copies
still give a positive ambient measure and exact selector moments. This
negative statement does not rule out a useful new quotient/regraded dictionary.
See dictionary-target.md. Do not infer a full bivariate no-go theorem.

## History

2026-11-05, Codex, gpt-6.1-sol medium as dispatched, source/rules
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. New scoped elementary statements;
PD-N100 and the original D6 target retained unchanged.

2026-11-06, Codex requested gpt-6.1-sol high, response to M1/MINOR3:
corrected the w2 moments and right-hand side without changing P or the
-30/23 conclusion. The original C statement/proof is preserved in
dictionary-copy-obstruction.md, with its own provisional record. The old
combined alias "two-sheet annihilator" is retained here as historical
provenance for C; neither negative scope was widened.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `IDEA?nn-mop-stability-codex-D6-graph` → `IDEA-547`.
- `PD-N?nn-mop-stability-codex-D6-literal` → `PD-N167`.
