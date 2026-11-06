# PD-T489 — Continuous triangle aggregate capacity-rate target

ID kind: PD-T.
Provisional ID: PD-T?lanczos-nonproduct-codex-P1-03.
Aliases: continuous simplex separation; triangle BJ versus good-rule rate.
Split from: the existing OPEN target retained in IDEA-570; this record transcribes that target without changing its scope.
Split into: none; the supporting results below keep their own statements and statuses.

## Statement

Determine the all-degree aggregate capacity rates for the continuous
triangle family and whether the retained P1 aim can be established: an
exponential BJ lower and a polynomial good-rule upper at an admitted
parameter point. The explicit continuous measure already admitted is the
uniform probability measure 2 du dv on Delta={u>=0,v>=0,u+v<=1}.
The broader retained P1 direction includes simplex weights
u^alpha v^beta (1-u-v)^gamma with alpha,beta,gamma>-1, after probability
normalization. No parameter choice with a proved separation is asserted.
The corresponding discrete-family question remains in the P1 candidate;
finite T24 evidence does not settle this continuous target.

## Definitions

For a positive probability measure mu, H is L2(mu), or its weighted
Euclidean evaluation representation for a finite measure. Pi_s is the
space of total-degree-at-most-s polynomials, N_s=(s+1)(s+2)/2, and P_s is
its exact orthogonal projector. Order monomials by increasing total degree
and then increasing y exponent. Fix admissible coordinate parents and ties.
Start with the exact constant column; inject epsilon f_h immediately before
exact full projection and positive normalization. Sources are arbitrary H
vectors with ||f||src^2=sum_h ||f_h||H^2/sigma_h^2, where sigma_h is the
unperturbed normalized raw-product norm. The first-order spectral span
capacity is kappa_R(s;mu)=sup_(||f||src=1) lim_(epsilon->0+)
||(I-P_s)P_s(epsilon;f)||/epsilon. All nonconstant columns through s are
allowed sources. BJ and mirror are the fixed rules of
[p5-02-padua-polynomial-capacity.md](p5-02-padua-polynomial-capacity.md);
the weighted conventions and continuous extension are in PD-T482/483.

## Assumptions

Use the continuous Hilbert source space, positive polynomial form in every finite degree, and the declared fixed coordinate order. A finite atomic cubature source space cannot be substituted without a proved comparison.

## Status by part

Overall status: OPEN.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| The rate/criterion/robustness target stated above | OPEN | Full-capacity closure or a proved P4 sufficient criterion is missing; the BJ-only degree-eight creator chain is supporting finite evidence. |

Candidate / claim disposition: Retained family target; the direct recursion route is deferred pending full-capacity closure or a P4 criterion.
Supporting results are separate dependencies, not proved parts of this target;
they do not upgrade it to PARTIAL.

## Depends on

PD-T472 admission; PD-T473 finite probe; PD-T482/483 capacity model.

## Checks

No new scientific check or computation was executed for this transcription.
The existing results and their finite verification scopes remain in their
linked records. [Audit 01](../audit-01.md) is the completed substantive
review; [audit 02](../audit-02.md) accepts the focused correction and
response dispositions, without claiming these OPEN targets are proved.

## Sources

Existing [candidate record](../ideas/P1.md), its linked supporting theory,
[original direction](../handoffs/01-work.md), and the explicit OPEN-target
registration instruction in [handoff 06](../handoffs/06-preparation.md).
No external literature theorem is imported as a proof premise.

## Proof or evidence

No proof of this target is claimed. The cited proved model/admission results
and finite measurements establish only their own stated scopes. No new rate
or exponent is invented by creating this durable target record.

## Scope

This preserves the already documented unresolved target. It asserts no
IEEE/scalar-operation realization, typical-error law or every-source lower.
A finite measured trend does not prove an all-degree conclusion.

## Open items

Full-capacity closure or a proved P4 sufficient criterion is missing; the BJ-only degree-eight creator chain is supporting finite evidence.

## History

2026-11-06 — Codex, mechanical registration under the coordinator's reserved
range: transcribed the previously audited OPEN target at PR preparation,
following handoff 06. No mathematical development or status upgrade.
