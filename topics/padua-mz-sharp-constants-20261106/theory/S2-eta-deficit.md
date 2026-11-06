# PD-T?mz-sharp-codex-S2-02 — endpoint MZ deficit has logarithmic-square order

ID kind: PD-T.
Aliases: endpoint eta tends one; true MZ deficit; upper-gap assembly.
Split from: the endpoint-deficit implication retained as an open item in
PD-T018/024/027; no sharp-constant claim is narrowed.
Split into: none.

## Statement

For every integerN>=2 let G_N be the Lebesgue CC Gram matrix on
Pi_(N−1) in an orthonormal Legendre basis and eta_N=||I−G_N||_2.
Define H_s=sum_{r=1}^s1/r, h_N=2H_(N+1)−1 and

    K_N=4*pi²*(pi+1)²*h_N*(h_N+2H_(floor(N/2)+1)).

Then

    min(1/K_N,1/3) <= 1−eta_N
                        <= min(1,128000/(logN)²).        (1)

In particular 1−eta_N is bounded above and below by positive absolute
multiples of (1+logN)^−2 and eta_N tends1 as N tends infinity.
No limiting leading coefficient or claim about practical finite-N onset
is made.

## Definitions and assumptions

Exact Lebesgue CC rule at N+1 Lobatto nodes, real polynomials of degree
at mostN−1, unnormalized measure dx on[-1,1]. lambda_− and lambda_+
are the smallest/largest eigenvalues ofG_N. The norm is the Euclidean
spectral norm; the orthonormal-basis convention makes it invariant.

## Status by part

Overall status: **PROVED** in analytic development.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact all-N bounds(1), logarithmic order and eta_N→1 | PROVED | Analytic assembly below; separate audit required |

Candidate disposition: equivalent synthesis of newly proved S2 uniform
gap with existing PD-T017/018, not a separate new mechanism.

## Depends on

PD-T017: lambda_−>=1/K_N.
PD-T018: lambda_−<=128000/(logN)².
PD-T?mz-sharp-codex-S2-01: lambda_+<=5/3 for everyN>=2.
PD-T013: exactness on constants, giving constant-polynomial quotient1.
All three complete theory files were read in full before this corollary.

## Checks and sources

No numerical run is required or claimed. Frozen input SHA:
2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861. Only local analytic theorems
are used; no external source or historical novelty claim.

## Proof

Symmetry gives eta_N=max(1−lambda_−,lambda_+−1), because the extreme
eigenvalues determine the greatest distance from1. Hence exactly

    1−eta_N=min(lambda_−,2−lambda_+).

The lower bounds lambda_−>=1/K_N and 2−lambda_+>=1/3 prove the left
side of(1). The constant polynomial has quotient1, so lambda_−<=1;
combining this with PD-T018 and 1−eta_N<=lambda_− proves the right
side of(1). Every bound applies atN2 as well as at all higherN.

H_s<=1+log s shows K_N<=C(1+logN)² for an absoluteC. Therefore
min(1/K_N,1/3)>=c(1+logN)^−2 for a positive absolutec.
For N>=2, logN/(1+logN)>=log2/(1+log2)>0, so the right side of(1)
also gives the matching upper order in (1+logN)^−2. Positivity and
the upper bound tending0 imply eta_N tends1. This proves the statement.

## Scope and open items

This resolves the logarithmic order of the actual normalized MZ deficit,
whose earlier inference was blocked by the missing uniform upper gap.
It does not determine lim(logN)²lambda_− or the sharp upper spectral
limit. Required independent/Claude audit remains separate. The precise
registry mapping to existing open-item wording belongs to the coordinator;
PD-T020 and the sharp-limit/value part ofPD-T027 remain OPEN.

## History

2026-11-06, S2 Codex developer; requested gpt-6.1-sol xhigh, runtime
metadata unexposed. Added at coordinator request after freezing the
uniform theorem. No Git or shared-registry operation.
