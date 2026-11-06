# PD-N166 — predivide-C4-restore fails the round-1 gate

ID kind: PD-N (provisional allocation).
Aliases: D4-C1a; one common Geronimus preconditioner; c=-2 restore.
Split from: D4-C1 numerical solver proposal.
Split into: none.

## Statement

For the pinned Krawtchouk and Hahn benchmark inputs at N=16, the specified binary64 algorithm C4(w/(x+2)), followed by the common Christoffel map with c=-2, has larger field-scaled NN forward error than the unmodified binary64 C4 algorithm. Thus this design fails G4's two-family N16 improvement gate. This is a measured claim about two fixed instances.

## Definitions

Input nodes x_l=2l/(N-1)-1. Exact input weights are the pinned `c4_float_baseline.inputs`: Krawtchouk p1=2/5,p2=1/2; Hahn beta1=1,beta2=3/2 with second Pochhammer parameter 2. No randomized data or seed. Error E=max_f ||computed_f-reference_f||_infinity/||reference_f||_infinity, f in a1,a2,b1,b2. Reference: C4 in mpmath at 220 decimal digits.

## Assumptions

The exact code, arithmetic, fixed shift and inputs in `attempts/D4.md`; no adjustable shift search or multi-step schedule. Reference consistency at 140 versus 220 digits was separately measured; it is not a rigorous interval certificate.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| This algorithm fails the specified N16 forward-error comparison | MEASURED | Two fixed cases, table below; independent exact replay in audit-01.md, priority8 |

Candidate / claim disposition: REJECTED.
Rejection reason: failed, only this predivide-C4-restore implementation at the frozen inputs and shift.

## Negative-result scope

Attempted mechanism: D4-C1a, easier reconstruction of a commonly predivided pair followed by O(N^2) restoration. Parameter range: N=16, the two pinned families, c=-2, binary64 C4 and restoration. The full N=4,8,12,16 observation table is in `attempts/D4.md`.

## Depends on

PD-T289 and pinned C4 code; D4-01 exact transform identifies the restoration's mathematical target. No conditioning theorem is assumed.

## Checks

Command: `python topics/nn-mop-stability-20261105/code/integrable_transport.py --mode float --sizes 4 8 12 16 --dps 220`. Producer hash and dependency hashes, raw artifact identity and version receipt: `attempts/D4.md`.

## Sources

No outside stability result. Known transformations are attributed in `literature-D4.md`.

## Proof or evidence

| Family, N=16 | Direct C4 E | Predivide-C4-restore E |
|---|---:|---:|
| Krawtchouk | 0.0966694483123344 | 0.223308958621571 |
| Hahn | 70.3138481558705 | 79.7731254890667 |

The all-size gain log10(E_C4/E_candidate) never reaches two digits; at N16 it is negative for both families. An isolation run restoring rounded 220-digit source coefficients yields errors <=3.83e-15 for these eight cases. This shows that the tested failure is compatible with a poor source reconstruction; it does not establish a uniform bound or prove that all error is attributable to one stage. No joint backward error was computed by this worker.

## Scope

Neither all common transformations nor all preconditioners are rejected. In particular, isolated transport from accurate supplied coefficients remains a viable bounded operation. G4 was checked only for this stated design; no assertion about its unrun variants is made.

## Open items

Independent replay; a useful non-C4 source-array construction; input-aware shift selection with a prospective criterion. Repeating arbitrary shifts without such a mechanism is not the next round.

## History

2026-11-05, Codex dispatched gpt-6.1-sol xhigh, source 823cf6a4, round 1. The candidate was communicated to coordinator/native-backward worker before floating tests; this durable failure record follows the run. Exact algebra remains separately PROVED.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `PD-N?nn-mop-stability-codex-D4-05` → `PD-N166`.
