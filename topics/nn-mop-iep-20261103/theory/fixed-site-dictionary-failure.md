# PD-N100 — standard transfers do not commute at a fixed site

Final ID: **PD-N100**. Provisional alias: `PD-N?nn-mop-iep-codex-02`.

ID kind: PD-N. Aliases: C2 literal fixed-site dictionary counterexamples.
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

Attempted mechanism: literally identify these same-site transfers with a
commuting pair. This tests only that particular dictionary. PD-T057's interior
commuting conditions themselves couple adjacent degree blocks, so "shifted
versus fixed-site" is not the feature that separates these theories. The negative statement does
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
../gate.md and ../literature.md. The decisive mismatch with PD-T057 is
spectral: the two NN difference operators
H_j f(nu)=f(nu+e_j)+b_(nu,j)f(nu)+sum_s a_(nu,s)f(nu-e_s)
both have eigenvalue x on a consistent MOP state. Thus H_1-H_2 annihilates
that state. Bivariate coordinate multiplication instead has joint node
eigenvalues (x_l,y_l) on the full node space. A second index direction gives
no independent second spectral coordinate.
The recorded exact counterexamples give the evidence for the statement.

## Scope / open items / history

No universal impossibility or novelty claim. Other encodings remain outside
scope. Claude audit-01 accepted the finite counts/status and requested this
F2 wording correction; Claude audit-02 accepted. Preparation protocol check pending. The full-lattice H_j
are not identified with the transfer matrices; no new full-lattice measurement
is added here. 2026-11-05, Codex, metadata in LOG.md.
