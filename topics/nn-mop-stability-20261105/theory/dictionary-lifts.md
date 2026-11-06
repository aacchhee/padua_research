# PD-T446 — copy/pair transfer target

ID kind: PD-T. Aliases: selectors; Hermite–Padé pair lift; two sheets.
Split from: [dictionary-target.md](dictionary-target.md), its copy/pair sub-target.
Split into: none.
Parent OPEN target: [dictionary-target.md](dictionary-target.md); this is its
copy/pair sub-target, not an independent solved transfer claim.

## Statement

Target: identify an explicit positive quotient or grading of a labelled-copy
or polynomial-pair realization which represents the original whole normal
NN triangle as two symmetric bivariate coordinate sections, including the
boundary and a stable algorithm transport. This target remains OPEN.

## Definitions and assumptions

Finite common real nodes x_l, strictly positive w1,w2; normality is required
at every index needed by the original NN recurrence. Put sigma=sum_l
w_(1,l)delta_(x_l,0)+w_(2,l)delta_(x_l,1), and define
J(A,B)=A(x)(1-y)+B(x)y. A scalar P embeds as J(P,P)=P(x).

## Status by part

Overall status: OPEN. The elementary selector identities below are minor
routine facts, excluded from status aggregation. They do not establish any
conjunct of the target's symmetric-section/stability conclusion. Candidate
pair encoding is equivalent/background; the richer transfer is deferred.

## Depends on / sources

The original defining type-I/type-II moment equations; inherited LIT-347/119
is univariate context only. No unread Hermite–Padé theorem is invoked.

## Proof or evidence: routine facts

At y=0, J(A,B)=A; at y=1, J(A,B)=B. Therefore

    <J(A,B),x^k>_sigma=sum_l x_l^k(w_(1,l)A(x_l)+w_(2,l)B(x_l)),
    ||J(A,B)||²_sigma=sum_l(w_(1,l)A(x_l)²+w_(2,l)B(x_l)²).

The type-I cancellation and normalization moments are exactly scalar
pairings in this positive ambient space. Likewise
<P,(1-y)x^k>_sigma and <P,y*x^k>_sigma are the two type-II moment sums.
This is an exact finite-value encoding; polynomial pairs which vanish at
all nodes have zero norm and must be quotiented if a Hilbert space is desired.

Multiplication by x preserves the diagonal subspace D={J(P,P)} of equal
values on the sheets. Multiplication by y does not: y*J(1,1)=J(0,1)
is not diagonal. Thus D alone carries no second coordinate action by
restriction, and extra modes are required. Orthogonal compression of y to
D is possible, but it must not be silently substituted for invariant
restriction or claimed to reproduce the whole NN recurrence. For example,
on D with its induced weights w1+w2, this compression multiplies by
w2/(w1+w2), a newly specified scalar ratio, not an NN index shift.

The explicit y²-y annihilator is split into dictionary-copy-obstruction.md;
it does not invalidate these positive selector identities.

## Checks

Finite selector cancellation was actually checked in dictionary_probe.py;
see ../attempts/D6.md. No new pair algorithm was implemented or run.
Completed independent reconstruction is recorded in audit-01.md, priority9.

## Scope and open items

Specify a quotient, the two actions and a graded isomorphism preserving NN
coefficients. Standard total-degree Pi_2 without deflation is excluded by
the separate scoped annihilator statement. Other spaces remain available;
no blanket failure verdict is assigned.

## History

2026-11-05 Codex, dispatched gpt-6.1-sol medium; rules/source
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. First D6 round.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `PD-T?nn-mop-stability-codex-D6-lifts` → `PD-T446`.
