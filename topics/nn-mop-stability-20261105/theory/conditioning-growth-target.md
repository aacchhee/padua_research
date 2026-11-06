# PD-T?nn-mop-stability-codex-D1-target — sharp conditioning growth target

ID kind: PD-T. Aliases: D1 sharp growth-law target; useful matching rate.
Split from: none; durable home of the original D1 target.
Split into: conditioning-local.md, conditioning-krawtchouk-bound.md,
conditioning-lower-krawtchouk.md and conditioning-measurements.md are
separate supporting results, not a decomposition into solved target cases.

## Statement and definitions

For the exact Krawtchouk and Hahn input families of handoff01/PD-T290,
with N common nodes z_k=2k/(N-1)-1 and the induced condition kappa_N
defined in conditioning-local.md, determine matching all-N growth bounds
with explicit useful constants and a sharp exponential rate if one exists.
In particular determine liminf and limsup of kappa_N^(1/N), whether they
are equal and finite, and the required subexponential factors. A usable
digit-loss expression must state its input/output norms and finite-perturbation
radius; it cannot predict every algorithm's actual rounding error.

## Assumptions and status

Overall status: OPEN. The input model allows unit-scale absolute node
perturbations and componentwise relative weights; the output uses four
field-sup relative norms. Full mixed normality is required. Krawtchouk
normality is proved for all N; Hahn normality is certified here only for
the finite N4–64 scope unless an additional theorem is supplied.

The original handoff requested, for example, an explicit exponential lower
bound. That example is now proved separately with lower base at least
5+2sqrt(6). A coarse rational-height upper bound is also proved. Neither
is a matching sharp growth law, so this parent target remains OPEN, not
PARTIAL on the strength of supporting results. The Hahn and finite-radius
questions likewise remain unresolved. No candidate is rejected here.

## Dependencies, evidence and scope

PD-T286/288/289 define the exact map. The local derivative, coarse upper
bound, lower/proximity proofs, finite Hahn certificate and measured tables
retain their own statements and statuses in their linked theory files.
Their commands/checks are in attempts/D1.md and attempts/D1-hard.md.
No computation or new mathematical mechanism is added by this record.

## History and next step

The phrase 'D1 sharp growth-law target (OPEN)' was previously used without
a durable home. Added for audit-01 MINOR4 on2026-11-06 by Codex, requested
gpt-6.1-sol high. Original target wording is retained above; no silent
narrowing or upgrade. Next unresolved step: an informative matching upper
rate or a proof that the proposed sharp-rate formulation fails.
