# PD-N?padua-3d-codex-T3-02 — Full unshifted order-39 class reduction

ID kind: PD-N.
Aliases: nonunit-coordinate reduction; normalized cubic cyclic obstruction.
Split from: none. Split into: none.

## Statement

Let z be any integer triple and

    X(z)={(cos(2*pi*k*z_j/39))_(j=1)^3:0<=k<39}.

Evaluation of Pi_3(R^3) on X(z) is never injective. The finite-cover
obligation H39 below has been discharged by committed exact witnesses and
distinct-agent execution. In particular no such unshifted image with 20
nodes is unisolvent for Pi_3. This is degree 3 and parameter modulus 39
only; it is not an all-degree cyclic-family exclusion.

H39: for each 1<=b<c<=19, the integer dictionary D of T3-01 with
M=39, I={alpha:|alpha|_1<=3}, z=(1,b,c) has a displayed nonzero rational
kernel vector, verified exactly against all 20 rows. T2 owns this finite
cover, code, certificates and its own scoped normalized-class result.

## Definitions and assumptions

Pi_3 has dimension 20. The full cyclic image may have fewer than 20
points; no assumption of primitive z or a unit coordinate is imposed.
There is no phase shift and no union of cosets. H39 is the named finite
obligation, not a literature assertion or an inherited proof.

## Status by part

Overall status: **PROVED**, computer-assisted finite statement, using the
hand reduction below and the now-discharged H39 finite cover. The original
all-degree construction target is not upgraded. Computation trust and
independent-replay identities are explicit in the normalized-cover record.

Candidate disposition: retained scoped negative extension of the T2
screen; not a surviving-family result.

## Negative-result scope

Attempted mechanism: minimal-cardinality degree-three interpolation on
an unshifted cyclic cosine orbit with parameter modulus 39. The normalized
finite search is T2's candidate; this record covers arbitrary generator
triples via elementary reparameterizations and axis polynomials.
Parameter range: n=3, M=39, every z in Z^3, zero phase. Other moduli,
shifted cosets, growing-degree subsequences and unions remain outside it.

## Depends on

PD-T?padua-3d-codex-T3-01 for D-to-real-kernel equivalence. H39 inputs and
check: `evidence/t2-n3-null-cover.json` and T2's finite-cover checker,
whose exact command is:

`python topics/padua-3d-20261106/code/t2_check_cover.py`

Input SHA-256: `ab78e752e646a880d305fc76c711808b7f8ac31e37546a25c5c05f623300eb2a`.
Checker SHA-256: `3b52ba33640a3f46971d4e86ab345d68af653fcf011fc25600ac631d4eb2a59f`.
T2's original same-agent run passed; T3 did not execute that checker.
The subsequent distinct-agent execution and separate reconstruction have
discharged the obligation. Its canonical normalized claim is
`PD-N?padua-3d-codex-T2-02`,
[normalized screen](t2-normalized-screen.md). The proof uses the checked
nonzero null polynomials, not the maximum-rank report. See the separate
[independent check](../independent-checks-computation.md).

## Proof of reduction

Reduce every coordinate modulo 39. If no coordinate is a unit, every
coordinate is divisible by 3 or by 13. If at least one coordinate is
divisible by 13, its cosine values belong to {1,-1/2}; the nonzero
quadratic (x_j-1)(2x_j+1) annihilates X(z), including the constant case.
If none is divisible by 13, all three coordinates are divisible by 3.
The parameter period is then at most 13. Global inversion k->39-k
pairs its nodes, leaving at most (13+1)/2=7 distinct points. Evaluation
of the 20-dimensional Pi_3 into R^7 cannot be injective. This argument
also covers nonprimitive triples; primitivity is unnecessary.

Now suppose z has a unit coordinate. Permute axes to put that coordinate
first. Multiplication of the parameter k by its inverse modulo 39 is a
bijection, replacing the generator by (1,b',c') without changing X.
Coordinatewise sign changes of the integer generators do not change
cosines, so fold b',c' into [0,19] and permute the last two axes to get
0<=b<=c<=19. These parameter and axis changes preserve total degree and
evaluation injectivity.

If b=0 or c=0, x_j-1 is an annihilator. If b=1 or c=1, x_j-x_1 is an
annihilator. If b=c, x_2-x_3 is an annihilator. Otherwise
2<=b<c<=19, which lies inside H39's 171-row list 1<=b<c<=19. A nonzero
kernel vector there gives a nonzero Pi_3 polynomial vanishing on X by
T3-01. In every case evaluation fails to be injective. ∎

## Checks, sources and scope

This reduction is hand-proved and requires no extra generator search.
No new external source is invoked; no historical novelty is claimed.
H39 code/evidence identities and actual separate replay are recorded in
the linked independent check and in `t2-normalized-screen.md`. The
all-degree total-degree polylog target remains OPEN. Required Claude
audit remains separate from these supplementary checks.

## Open items

The finite obligation is discharged. No extension from M=39 to all odd
moduli is justified by this reduction; arbitrary phases and unions also
remain outside its scope. Required Claude audit remains due.

## History

2026-11-06, Codex T3, rules ccd9e905; assigned model `gpt-6.1-sol` xhigh; resolved runtime metadata not
exposed. Parent and T2 independently suggested the nonunit split; this
file supplies the complete normalization and boundary cases without
claiming an independent rerun of T2's certificates.

2026-11-06, coordinator Codex Astra high: changed CONDITIONAL to PROVED
after the distinct Astra checker actually executed H39 and separately
reconstructed all 171 witnesses. The statement's n=3/M=39/zero-phase scope
and the analytic reduction are unchanged. This does not upgrade an
infinite-degree target.
