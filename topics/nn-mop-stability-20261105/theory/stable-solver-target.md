# PD-T?nn-mop-stability-codex-stability-target — general stable NN solver target

ID kind: PD-T. Aliases: original stable-algorithm target; joint backward stability.
Split from: none; durable home of the original campaign/D3/D5 target.
Split into: native-measurements.md, backward-local-manifold.md,
backward-dyadic-obstruction.md and backward-projection-measurements.md
are separate supporting, scoped-negative or measured results.

## Statement and definitions

Original target: obtain and justify a stable native algorithm for the full
nearest-neighbour inverse problem from N common distinct real nodes and
two positive weights, with every mixed index through degree N normal.
The output is the four monic fields through coefficient degree N-1.

The strict input-only target uses beta(y;p)=inf{||p'-p||_B:F(p')=y},
with ordered nodes and normalized positive masses. It is distinct from
the dated approximate-compatibility target: find an actual common input
p' and an array correction e with y+e=F(p'), bounding both ||p'-p||_B
and ||e|| in expressly declared norms by useful multiples of unit roundoff.
Any general theorem must quantify its input domain/normality margin,
precision range, N-dependent constants, norm/gauge and computational model.
A fixed-SPD nearest projection is defined in backward-local-manifold.md;
the measured field-sup correction is a different norm and is not silently
its nearest minimum.

## Assumptions and status

Overall status: OPEN. No implemented solver has a general weak- or joint
backward-stability theorem here. The dyadic obstruction refutes strict
realizability only for one displayed raw array; it does not refute every
possible native solver. Finite N4 mixed witnesses do not establish a
uniform theorem, and the measured N8 fits miss100u. The old strict target
and the amended correction/data formulation remain explicitly distinct.
Supporting geometry alone does not make this target PARTIAL.

## Dependencies, evidence and scope

PD-T286/288/289 define F; PD-T290 is the baseline measurement. Both native
designs are known reformulations with finite comparisons in attempts/D3.md;
geometry, raw exact-match obstruction and measured feasible fits are in
attempts/D5.md and the named theory records. No new candidate, algorithm,
existence theorem or empirical execution is introduced by this parent record.

## History and next step

The original campaign's stable-solver / strict joint-backward target was
previously cited without a durable file. Added for audit-01 MINOR4 on
2026-11-06, Codex requested gpt-6.1-sol high. The exact strict criterion
is preserved rather than replaced after seeing the counterexample.
Next unresolved step: a specified native algorithm and a quantified error
analysis in a declared strict or correction/data model.
