# PD-T434 — full-grid NN and monic step-line conditioning

ID kind: PD-T. Aliases: analytic AD table; D1 rounds 1 and 2.
Split from: D1 sharp all-N growth target. Split into: none.

## Statement

For every integer N=4,...,64, both exact rational PD-T290 families were evaluated
at 180 and 260 decimal digits. All full 3N-column analytic Jacobians were formed;
weighted absolute row sums give the induced condition. No directional estimate
or finite difference replaces this norm. The single compact 61-row table,
commands, timing and raw hashes are in [attempts/D1](../attempts/D1.md).
It reports NN and monic step-line mixed-input conditions for both families.

## Definitions and assumptions

The [local theorem](conditioning-local.md) defines the normality domain,
input scales and output norms. Primary mixed input uses absolute node scale one
and componentwise relative weights, independently, without a mass constraint.
NN output is baseline E: the maximum of four fieldwise relative sup errors.
SL is the monic alternating first-e1 four-term path with separately scaled
beta/gamma/delta fields; equivalence to a diagonally scaled literature output
is not asserted. Raw results also contain componentwise-input and block-normwise
input conditions. All three use fieldwise normwise output. Fully componentwise
output is infinite for both benchmark families and is excluded: Krawtchouk
has sensitive b2_(0,0)=0 (also b1_(1,1)=0 atN4); symmetric Hahn w1 gives
sensitive marginal b1 zeros. No floating near-zero division is substituted.

Krawtchouk normality is proved for all N in the
[coarse-bound theorem](conditioning-krawtchouk-bound.md). For precisely the
specified Hahn inputs N=4,...,64, the separate
[finite computer-assisted theorem](conditioning-hahn-normality-finite.md)
proves normality using exact rational checks and the
[noncircular converse](conditioning-normality-certificate.md).
No all-N Hahn normality theorem is asserted.

## Status by part

Overall status: MEASURED. The local analytic derivative and induced-norm
formulation are PROVED separately. Evaluating that formula in arbitrary
precision is not an outward enclosure. Exact finite normality has its own
PROVED computer-assisted status and is not inferred from floating convergence.

All four full runs completed all 61 cases, exit 0. Across six target/input-model
norms per case, the maximum relative 180/260-dps difference is
1.763266421e-115 Krawtchouk and 1.284174211e-93 Hahn, below checker threshold
1e-60. This is precision-convergence evidence, not a rigorous error bound.
The checker verifies coverage, exact input hashes, precision/family metadata,
and common frozen producer/baseline hashes. The displayed seven-digit values
come from the 260-dps runs; the receipt contains the unique compact table.

## Depends on

PD-T286/288/289; exact PD-T290 inputs; conditioning-local.md; mpmath 1.3.0.
Frozen conditioning.py SHA256:
11c4b49be8541697e74d383b908db47b42480e11c60f92c35821340eacea929c.
Pinned c4_float_baseline.py SHA256:
9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8.
No new primary-source claim or imported classical NN closed form is used here.

## Checks and scope

The independent moment-system Fraction derivative agrees exactly with the
frozen AD graph on all 4416 entries at both families N=3,4,6; Krawtchouk N4
has exact kappa=4126/25 and a signed maximizing-row witness. See
[independent checks 01](../independent-checks-01.md). The distinct exact finite
Hahn receipt and source pins were independently replayed and every essential
table cell checked: [independent checks 03](../independent-checks-03.md).
Full larger-N moment Jacobians and outward enclosures have not been rerun
independently. Completed audit scope is recorded in audit-01.md; response/re-audit process is in LOG.md.

The original N8 G3 finite screen, preserved in the D1 receipt, rejects literal
constant-product proportionality only on its sampled gaps. It alone says
nothing about an asymptotic Theta model. A separate written
[proximity obstruction](conditioning-lower-proximity.md) proves the scoped
fixed-N Krawtchouk failure of O(1/min|d|); it is not extrapolated from the screen.
Angelesco is NOT APPLICABLE here: positive weights on the same N nodes cannot
have disjoint supports. Permitting disjoint nonnegative supports makes an axis
singular at support-size+1<=N, violating the required normal full triangle.
A normal rectangle is a different target.

Worst-case local sensitivity does not require an algorithm to realize that
error. The heuristic digits-lost allowance log10(kappa) is only first order;
there is no uniform finite-epsilon radius. The gate uses u=2^-53, while the
predecessor epsilon=2^-52 differs by two. Once kappa*u exceeds one, the ratio
E/(kappa*u) alone is uninformative. No stability verdict follows from this table.

## Open items and history

Every requested integer size and second precision is complete. Remaining:
mandatory audit, raw cold-storage archival, certified large-N derivative
enclosures, and a sharp matching growth bound. The separate
[exponential lower theorem](conditioning-lower-krawtchouk.md) closes the
informative lower-law subtarget; it does not give the sharp exponential base.

2026-11-05, D1 allocation gpt-6.1-sol xhigh, pinned rules/input SHA
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. Python 3.12.14; mpmath 1.3.0.
The eight-point round-1 table was checkpointed at f75964b before authorization
of the full integer round 2. Main derivative code remained frozen across both.

Parent unresolved target: [conditioning-growth-target.md](conditioning-growth-target.md).

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `PD-T?nn-mop-stability-codex-D1-03` → `PD-T434`.
