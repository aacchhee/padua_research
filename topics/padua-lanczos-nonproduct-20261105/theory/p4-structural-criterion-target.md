# PD-T491 — All-degree structural capacity criterion target

ID kind: PD-T.
Provisional ID: PD-T?lanczos-nonproduct-codex-P4-05.
Aliases: principal-axis classifier; inverse normal quotient; leading-block conditioning.
Split from: the existing OPEN target retained in IDEA-578, IDEA-579, IDEA-580; this record transcribes that target without changing its scope.
Split into: none; the supporting results below keep their own statements and statuses.

## Statement

Find and test a useful explicit all-degree structural criterion for BJ
exponential capacity growth or BJ-versus-best separation on admitted
measure families. Preserve the original proposed iff involving an
explicit quantity along the BJ chain and the retained principal-axis,
inverse-normal-quotient and leading-coefficient candidates. A proved
sufficient condition covering P1 or P2 would meet the retained direction's
stated aim. No such quantity, equivalence or sufficient hypothesis is
proved by this record. The original asymptotic covariance/axis ratio
question is not narrowed to an absolute-capacity bound.

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

Use admitted positive measures with injective polynomial evaluation and nonzero ambient normal space at each finite test degree. Keep source/output normalization and the exact normal projection.

## Status by part

Overall status: OPEN.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| The rate/criterion/robustness target stated above | OPEN | Cross-family tests and an all-degree hypothesis controlling the actual normal quotient remain missing. Covariance-only finite absolute control is separately refuted. |

Candidate / claim disposition: Original structural and family-growth targets retained; the terminal-block variant is equivalent/consolidated, and only IDEA-581 is refuted by PD-N178.
Supporting results are separate dependencies, not proved parts of this target;
they do not upgrade it to PARTIAL.

## Depends on

PD-T481 definition/admission; PD-T482 weighted quotient and terminal block; PD-T483 atomless formula; PD-T484 transfer; PD-N178 scoped obstruction.

## Checks

No new scientific check or computation was executed for this transcription.
The existing results and their finite verification scopes remain in their
linked records. [Audit 01](../audit-01.md) is the completed substantive
review; [audit 02](../audit-02.md) accepts the focused correction and
response dispositions, without claiming these OPEN targets are proved.

## Sources

Existing [candidate record](../ideas/P4.md), its linked supporting theory,
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

Cross-family tests and an all-degree hypothesis controlling the actual normal quotient remain missing. Covariance-only finite absolute control is separately refuted.

## History

2026-11-06 — Codex, mechanical registration under the coordinator's reserved
range: transcribed the previously audited OPEN target at PR preparation,
following handoff 06. No mathematical development or status upgrade.
