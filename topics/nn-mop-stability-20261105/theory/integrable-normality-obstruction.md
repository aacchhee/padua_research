# PD-N164 — positive common changes can cross normality

ID kind: PD-N (final ID assigned at preparation, 2026-11-06; see title).
Aliases: exterior Christoffel normality trap; positive Toda path crossing.
Split from: D4-C1/C3, unsupported normality-preservation shortcut.
Split into: none.

## Statement

There exists a positive two-measure pair on three common distinct nodes, normal at every index of total degree at most three, for which both (i) multiplication of both weights by x-c with c strictly below the support and (ii) a positive common exponential deformation at a finite positive time produce a nonnormal (1,1) moment matrix.

## Definitions

Normal means the square mixed moment determinant is nonzero, with row convention PD-T286. Common exponential flow has weights exp(t x_l)w_(s,l).

## Assumptions

Only the explicitly specified positive pair below; this is an existence counterexample, not an assertion about the benchmark families or all shifts/paths.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Both failures of automatic normality preservation | PROVED | Explicit determinants below |

Candidate / claim disposition: REJECTED.
Rejection reason: refuted, solely the claim that positivity plus an exterior common shift, or positivity along a common Toda path, automatically preserves mixed normality.

## Negative-result scope

Attempted mechanism: D4-C1/C3 normality safeguard. Parameter range: N=3, nodes 0,1,2, weights w1=(11,1,1), w2=(13,2,1), c=-1, or t=log(sqrt(13)-2). Independent-weight paths and monitored paths avoiding the crossing are outside this result.

## Depends on

PD-T286 normality definition. PD-T443 provides another way to recognize the Christoffel singularity but is not needed for the direct counterexample.

## Proof or evidence

Use nodes (0,1,2) and the stated weights. Every pure-axis determinant through degree three is positive: the ordinary Gram form is positive definite for polynomials of degree at most two on these three nodes. The remaining mixed determinants are

    D_(1,1)=4, D_(2,1)=-40, D_(1,2)=44.

These can be obtained directly from rows (13,3),(16,4) at degree two and moments at degree three. Hence the full starting triangle is normal. Directly solving the two orthogonality equations gives P_(1,1)(x)=x^2+x/2-1/2=(x+1)(x-1/2).

Multiplying by x+1 gives positive weights (11,2,3) and (13,4,3). Their mass/first-moment rows are (16,8) and (20,10). Their determinant is zero. The multiplier is strictly positive at every support node, and c=-1 is strictly exterior.

For the common exponential path put a=exp(t)>0. The mass/first-moment rows become (11+a+a^2,a+2a^2) and (13+2a+a^2,2a+2a^2). Expansion gives

    D_(1,1)(t)=a(9-4a-a^2).

It is zero at a=sqrt(13)-2>1, giving the asserted positive finite t. All weights remain strictly positive there. No claim is made that other determinants avoid zero before that time; an earlier zero would also obstruct unmonitored continuation.

## Checks

The Christoffel example was independently derived by exact moment arithmetic, then checked in `code/integrable_transport.py --mode exact`. The exponential determinant identity above is an algebraic proof, not an outcome inferred from numerical integration. Commands/hashes in `attempts/D4.md`; completed supplementary exact replay and direct determinant checks are recorded in [independent-checks-01.md](../independent-checks-01.md#d4-and-d6).

## Sources

No external theorem used. Primary sources on Christoffel/Toda transformations are attributed in `literature-D4.md`; those transformations do not assert the invalid positivity shortcut refuted here.

## Scope

Mixed normality, unlike ordinary scalar positive Gram normality, can fail under a strictly positive common multiplier. This does not refute locally valid Darboux or Toda formulas on a normality interval.

## Open items

Quantitative normality margins or certified monitored paths for useful target families.

## History

2026-11-05, Codex dispatched gpt-6.1-sol xhigh; source 823cf6a4, round 1. The shortcut is separated from the still viable local algebra.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `PD-N?nn-mop-stability-codex-D4-02` → `PD-N164`.
