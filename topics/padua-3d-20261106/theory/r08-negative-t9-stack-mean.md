# PD-N?padua-3d-20261106-codex-T9-r06-02 — the all-order stack mean comparison can return only zero

ID kind: PD-N.
Aliases: T9-R06-B; T9-R06-PDN02; permutation-mean method obstruction.
Split from: none; template completion/re-home of
[t9-r06-stack-mean-boundary.md](t9-r06-stack-mean-boundary.md), unchanged claim.
Split into: none. Existing provisional ID retained; no final allocation.

## Statement

For every integer n>=1, the established mean-determinant comparison cannot
prove a strictly positive lower bound simultaneously for every ordering
of the fixed Chebyshev–Lobatto stack heights. At least one permutation has
the displayed lower bound exactly zero. This is a method obstruction, not
a quality theorem for every stack ordering.

## Definitions

Heights h_a=cos(a*pi/n),0<=a<=n; layer sizes N_j=binom(n-j+2,2);
N=binom(n+3,3), S=binom(n+3,4). For a permutation pi define

    A_n=((n+1)log n+(3-n^2)log2)/(n(n+1)),
    log D(pi)=sum_(i<j) N_j log|h_pi(j)-h_pi(i)|.

The mean comparison is

    log Lambda(pi)>=max(0,(S*A_n-log D(pi))/N).

## Assumptions

The fixed-height Padua-stack construction and determinant comparison of
[t4-stack-determinant.md](t4-stack-determinant.md) and
[t4-monotone-lower.md](t4-monotone-lower.md); all permutations of the same
heights are allowed. No claim that the comparison is sharp is assumed.

## Status by part

Overall status: **PROVED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Mean-comparison obstruction for every n>=1 | PROVED | Exact uniform-permutation averaging below |
| True all-order stack Lebesgue lower bound | OPEN, outside statement | A zero lower estimate does not imply Lambda=1 |

Candidate / claim disposition: **REJECTED: failed** for the all-order
strictly-positive mean-comparison mechanism. Rejection reason: failed —
the comparison necessarily degenerates for at least one order.

## Negative-result scope

Attempted mechanism: use S*A_n-log D(pi) alone to force a positive
all-order lower estimate. Parameter range: every n>=1 and the complete
permutation class. Other lower-bound arguments, or a proper subclass of
orders, are not rejected.

## Depends on

The explicit determinant comparison and Lobatto pair-product identity in
the two T4 proofs above; no external source theorem.

## Checks

The old combined stack record and [audit03/T9](../audit-03/T9.md) contain
independent proof review. No new numerical run is required for this
finite expectation argument. This response worker read and reconstructed
the local proof without claiming an optimizer rerun.

## Sources

Classical determinant averaging, attributed through the existing T4/T9
records and [gate supplement](../novelty-gate-supplement-round08.md). No
novelty or external proof claim.

## Proof or evidence

Under uniform pi, every unordered height pair is equally likely at each
(i,j). Its mean log distance is A_n. Since sum_(i<j)N_j=S, exact linearity
of expectation gives E log D(pi)=S*A_n. Some pi_max must have
log D(pi_max)>=S*A_n, so the stated max(0,...) lower estimate is zero at
that order. More permutation samples cannot change this exact algebraic
loss. It does not imply Lambda(pi_max)=1 or rule out another all-order
lower-bound method. The monotone-order theorem remains a proper-subclass
result.

## Scope and D3

D3: this is a limitation of a particular three-dimensional stack comparison.
It asserts no failure of the two-dimensional Padua interpolation family.
Even an analogous vanishing lower estimate in dimension2 would be
compatible with its positive O(log^2 n) stability theorem; a failed lower
estimate is not a negative upper-bound or existence theorem.

## Open items

Resume an all-order stack lower bound only with information not averaged
away by this comparison, or an argument controlling each ordering by a
different invariant. No universal exponential lower estimate is supplied.

## History

2026-11-06 — Codex records worker, assigned gpt-6.1-sol xhigh; runtime
metadata not independently exposed; rules/input
9042e1c42964150f30fdbe8563c12ba6c6a8692a. Template completion under
handoff08 E6 and novelty m2/m3; old audited proof/status unchanged.
