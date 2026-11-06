# PD-N182 — nonterminal Hahn differences need not be positive

ID kind: PD-N.
Aliases: C2-03 round 5; unchanged arbitrary-index positivity extension;
complementary-factor sign failure.
Split from: none; standalone home for the scoped negative statement
previously written in `c2-hahn-upper-search.md`, round 5.
Split into: none.

## Statement

For the exact Hahn family alpha1=1, alpha2=3/2, gamma=1 on integer nodes
0,...,M, use the arbitrary-index polynomial factor

    U(l)=prod_(j=1)^t(l+1+x_j) (t+2-l)_(M-t),
    1<=t=n+m<=M,

where x_j are the row parameters alpha_s+i, i=0,...,n_s-1,
(n_1,n_2)=(n,m). The assertion that every relevant finite difference
`Delta^k U(0)>0`, for every such M,n,m and k=0,...,M, is false.
Specifically, at M=3,t=1,(n,m)=(1,0), k=1,

    U(l)=(l+2)(3-l)(4-l),
    U(0)=24, U(1)=18, Delta U(0)=-6<0.

Consequently the terminal proof's unchanged positive-difference premise
cannot be used across all nonterminal indices.

## Definitions

`(a)_r=prod_(i=0)^(r-1)(a+i)`, with empty product 1;
`Delta f(l)=f(l+1)-f(l)`. The relevant differences are those appearing in
the exact integer-node polynomial-value formula, equation (2) of the
[upper-search attempt](c2-hahn-upper-search.md).

## Assumptions

The family, row conventions and finite support are those of
[Hahn normality](c2-hahn-normality.md). The counterexample has t<M
and an admissible balanced one-row index. No numerical approximation,
asymptotic fit or unproved normality hypothesis is used.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Failure of universal nonterminal positive differences | PROVED | Exact displayed counterexample |

Candidate / claim disposition: REJECTED: failed for
[IDEA-597](../candidates-response-C2.md#ideann-mop-cond-codex-c2-03-r5--unchanged-positive-differences-below-terminal-degree).
Rejection reason: failed unchanged positivity extension; its universal
sign premise is refuted at the displayed parameters.

## Negative-result scope

Attempted mechanism: parent C2-03, round-5 subform C2-03-r5; extend the
terminal positive-sum comparison below terminal degree without a new
cancellation estimate.
Parameter range: the universal sign assertion is disproved by exactly
M=3,t=1,nu=(1,0),k=1. No assertion that every nonterminal index fails.

## Depends on

- [PD-T511](c2-hahn-normality.md): row parameters and
  exact family conventions, solely to identify the attempted mechanism.
- [Upper-search attempt](c2-hahn-upper-search.md), equation (2), for the
  role of U in that mechanism. The displayed arithmetic independently
  proves the sign failure once U is defined.
- [Terminal-rate theorem](c2-hahn-terminal-rate.md): context for the
  terminal positivity premise being extended, not a premise of the
  arithmetic counterexample.

## Checks

Response source/rules `3d5b29d`, Python 3.12.14. Actually executed:

    python3 topics/nn-mop-conditioning-20261106/code/c2_hahn_upper_search.py --max-m 6 > /tmp/padua-response-c2-hahn-upper-search.json

Its scientific payload equals committed `../c2-hahn-upper-search.json`
after omitting only Python version and elapsed time: 75 indices, 430
polynomial values, 860 weight coordinates, 430 common-node coordinates,
M=2,...,6. Code sha256
`5b2f7a4576bbe183e2156caa12faee0625b9eb9f3aed4a55a283e27d5b9555f3`;
helper identities remain those in the committed receipt. The response
output sha256 is
`6ccb4e0021892ed7d955230ca1a72ee56864a4513cf202233179a2bacbf2d3d9`;
it is local corroboration, not essential proof evidence.

The checker validates finite representation identities but prints the
counterexample as literal metadata. The response additionally evaluated
`U=lambda l:(l+2)*(3-l)*(4-l)` and asserted
`(U(0),U(1),U(1)-U(0))==(24,18,-6)` exactly. This elementary arithmetic
is the proof, not an all-N computer-assisted inference. The earlier
[Claude audit 01](../audit-01.md) accepted the scoped mathematics already
in the attempt; extraction into this durable record is a response change,
not a newly completed independent audit.

## Sources

No external theorem used. Literature comparison and reading limits are
in [candidate C2-03-r5](../candidates-response-C2.md).

## Proof or evidence

At t=1,nu=(1,0), the only row parameter is x_1=alpha1=1. Therefore
`prod(l+1+x_j)=l+2`. At M=3 the complementary factor is
`(3-l)_2=(3-l)(4-l)`. Substitution gives U(0)=2·3·4=24 and
U(1)=3·2·3=18, hence Delta U(0)=-6. These parameters lie inside the
universal proposed positivity range, so they refute it. This proves the
scoped negative statement.

## Scope

Only the unchanged sign-based proof extension fails. The exact Cauchy
inverse, the terminal row theorem, cancellation-sensitive arbitrary-index
upper bounds and a matching full-map Hahn upper are not refuted.

## Open items

The weighted correlated arbitrary-index inequality (3) in the
upper-search attempt remains OPEN. No revised estimate is proposed here.

## History

2026-11-06, Codex gpt-6.1-sol high, response source `3d5b29d`: extracted
the already audited round-5 counterexample without changing its statement,
proof or rejected scope, in response to MAJOR-3. The former location is
retained as attempt history and links here. Provisional ID only.

## Final ID aliases (2026-11-06)

- `PD-N?nn-mop-cond-codex-response-C2-positivity` → `PD-N182`.
- `IDEA?nn-mop-cond-codex-C2-03-r5` → `IDEA-597`.
- `PD-T?nn-mop-cond-codex-C2-02` → `PD-T511`.
