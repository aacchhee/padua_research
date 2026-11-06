# PD-T490 — Continuous radial disk aggregate capacity-rate target

ID kind: PD-T.
Provisional ID: PD-T?lanczos-nonproduct-codex-P2-05.
Aliases: disk rate; rotation versus fixed-order capacities.
Split from: the existing OPEN target retained in IDEA-573; this record transcribes that target without changing its scope.
Split into: none; the supporting results below keep their own statements and statuses.

## Statement

For the probability measures dnu_mu=(mu+1)/pi (1-x^2-y^2)^mu dx dy
on x^2+y^2<1, mu>-1, determine the all-degree fixed-order aggregate
capacity rates and whether BJ loses exponentially against a comparator
or the staircase capacities admit polynomial/comparability bounds.
These are the retained alternatives, not established conclusions.
No exponent, comparison constant or parameter range with a proved rate
is selected here. The finite rational ring grids are distinct measures.

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

Keep mu>-1 and the continuous Hilbert source space. Covariance transports the entire algorithm, order and basis; it does not identify fixed-order BJ and mirror.

## Status by part

Overall status: OPEN.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| The rate/criterion/robustness target stated above | OPEN | A bounded-order all-source capacity recursion was not obtained through degree eight; the direct route is redirected to the structural criterion. |

Candidate / claim disposition: Retained for the P4 structural route; no family-rate conclusion or rejection.
Supporting results are separate dependencies, not proved parts of this target;
they do not upgrade it to PARTIAL.

## Depends on

PD-T474 admission/moments; PD-T475 covariance; PD-T476 finite probe; PD-T482/483 model.

## Checks

No new scientific check or computation was executed for this transcription.
The existing results and their finite verification scopes remain in their
linked records. [Audit 01](../audit-01.md) is the completed substantive
review; [audit 02](../audit-02.md) accepts the focused correction and
response dispositions, without claiming these OPEN targets are proved.

## Sources

Existing [candidate record](../ideas/P2.md), its linked supporting theory,
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

A bounded-order all-source capacity recursion was not obtained through degree eight; the direct route is redirected to the structural criterion.

## History

2026-11-06 — Codex, mechanical registration under the coordinator's reserved
range: transcribed the previously audited OPEN target at PR preparation,
following handoff 06. No mathematical development or status upgrade.
