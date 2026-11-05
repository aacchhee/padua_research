# PD-N?nn-mop-iep-codex-02 — standard transfers do not commute at a fixed site

ID kind: PD-N. Aliases: C2 literal dictionary; fixed-site versus shifted products.
Split from: none. Split into: none.

## Statement

On the 112 sites n,m>=1, n+m<=N-1 of the 14 rational examples in
../exact-runs.md, the explicitly displayed matrices L1(n,m;0) and L2(n,m;0)
have a nonzero commutator. In contrast the shifted flatness identity passes at
all 70 eligible squares n,m>=1, n+m<=N-2. In the independently constructed
N=4 input of ../independent-check.md, both a nonzero fixed-site commutator
and shifted flatness occur at (1,1).

## Definitions / assumptions

Only the standard 3-component state, transfers, common-support examples and
index domains explicitly recorded in the linked receipts; x=0 for commutators,
full polynomial identities for shifted flatness. Exact rational arithmetic.

## Status by part

Overall status: MEASURED, finite exact counterexamples. Candidate disposition:
REJECTED: refuted for C2's literal identification on these samples.

## Negative-result scope

Attempted mechanism: identify these same-site transfers with the commuting
finite symmetric coordinate sections of PD-T057. The negative statement does
not exclude a global covariant-shift operator realization, a redundant lift,
another gauge, or any stable nearest-neighbour update.

## Depends on / checks

../code/exact_nn_mop.py and ../code/independent_nn_mop.py; exact commands,
source identities, rational witness and independent replay are in
../exact-runs.md and ../independent-check.md. These observations are sufficient
to falsify the named universal dictionary but are retained conservatively as
finite MEASURED evidence, not a claimed computer-assisted general theorem.

## Sources / proof or evidence

The shifted transfer interpretation is existing literature, documented in
../gate.md and ../literature.md. The two multiplication operators of PD-T057
are a different precise object; mere lattice indexing gives no dictionary.
The recorded exact counterexamples give the evidence for the statement.

## Scope / open items / history

No universal impossibility or novelty claim. Other encodings remain outside
scope. Claude audit PENDING; 2026-11-05, Codex, metadata in LOG.md.
