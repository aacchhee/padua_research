# PD-N?nn-mop-stability-codex-31 — a frozen raw NN array has no joint-data inverse

ID kind: PD-N. Aliases: binary64 compatibility obstruction; strict backward
error infinity witness. Split from: none. Split into: none.

## Statement

Consider the N4 Krawtchouk LU native output from `code/native_mixed.py`
in the recorded environment. Regard its stored binary64 entries as exact
dyadic real numbers. Its five fields are

| Field | Exact stored value |
|---|---|
| b_((0,0),2) | 0 |
| b_((0,0),1) | -3602879701896397/18014398509481984 |
| b_((0,1),1) | -4803839602528527/36028797018963968 |
| a_((1,0),1) | 5764607523034235/18014398509481984 |
| a_((0,1),2) | 6004799503160661/18014398509481984 |

No pair of positive common-support N4 measures, normal through degree4,
has this entire stored array as its exact NN array. Hence its strict
joint-data backward error beta, as defined in backward-local-manifold.md,
is +infinity, for every reference input and every finite input norm.

## Definitions and assumptions

Use the monic convention of PD-T286/289 and the full triangle through
degree3. The obstruction tests exact stored data, not decimal printouts,
nor an unspecified perturbation within a rounding cell. Positivity and
normality are the prescribed input domain, not arbitrary complex functionals.

## Status by part

Overall status: **PROVED** for the explicitly displayed dyadic array,
by the exact necessary-identity reduction and arithmetic below.
The separate producer-identification rerun is recorded in independent-checks-02.md
and audit-01.md, priority6. Producer reproduction is platform-dependent;
the exact displayed certificate is not. Candidate disposition: REJECTED: refuted for the literal input-only exact backward
interpretation of this raw array. No native accuracy theorem is rejected.

## Negative-result scope

Attempted mechanism: interpret the uncorrected rounded array as F(p')
for a nearby positive common-node input. This is one explicit raw-array
counterexample, not an impossibility of stable native algorithms with a
compatibility correction or an enlarged output representation.

Parameter range: exactly the five displayed dyadic fields from the recorded
N=4 Krawtchouk LU output in its original producer environment, interpreted
in the monic triangle through degree3 and normal common-support domain.
Closest predecessor: PD-N118 / IDEA-262, a variant of the same necessary
exact-consistency obstruction for a different bivariate raw-output model.
No historical novelty or new general obstruction mechanism is claimed.

## Depends on and proof

PD-T289's compatibility B2 at nu=(0,0), together with the structural
zeros a_((1,0),2)=a_((0,1),1)=0, requires every exactly realizable array
to satisfy

    (b_00,2-b_00,1)(b_01,1-b_00,1)+a_10,1-a_01,2 = 0.

The five displayed rational values give instead

    25700541873527631 / 649037107316853453566312041152512 > 0.

This follows by multiplying and adding the displayed dyadic fractions;
the denominator is positive and the numerator is a positive integer.
Therefore the necessary identity fails, the exact preimage is empty,
and beta=+infinity by definition. The reduction is analytic and all
essential certificate data are displayed here; the checker uses exact
integer Fraction arithmetic and no numerical tolerance.

## Checks

`python topics/nn-mop-stability-20261105/code/backward_dyadic.py`
checks the stored certificate without numerical libraries.
`python topics/nn-mop-stability-20261105/code/backward_dyadic.py --reproduce`
also regenerates the array and checks exact equality of these five fields.
Developer commands and hashes are in attempts/D5.md. Completed separate
replays and exact rebuilds are recorded in independent-checks-02.md and
audit-01.md, priority6; they are executions, not just code inspection.

## Sources, scope and open items

No external primary source is used. The general nearby-image geometry
is separate. A small nonzero compatibility residual can coexist with
excellent forward accuracy; beta=+infinity says that the literal strict
metric is unsuitable for generic rounded outputs. It supplies no lower
bound for an explicitly allowed coefficient-correction metric.

## History

2026-11-05, Codex requested gpt-6.1-sol xhigh. Rules/source
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. The original G4 strict
backward criterion is preserved; this certificate explains why a dated
mixed-metric amendment must be reported separately, never silently applied.

Parent unresolved target: [stable-solver-target.md](stable-solver-target.md); supporting results do not establish its general stability conclusion.
