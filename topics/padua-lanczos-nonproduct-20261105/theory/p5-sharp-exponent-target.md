# PD-T492 — Sharp Padua BJ and mirror polynomial orders

ID kind: PD-T.
Provisional ID: PD-T?lanczos-nonproduct-codex-p5-03.
Aliases: sharp Padua exponent; unsaturated capacity order.
Split from: the existing OPEN target retained in IDEA-582; this record transcribes that target without changing its scope.
Split into: none; the supporting results below keep their own statements and statuses.

## Statement

For the exact positive Padua probability measure nu_m and every pair
of integers m>=2 and 1<=s<m, determine sharp polynomial orders of
kappa_BJ(s;m) and kappa_mirror(s;m), including the dependence on m or
uniformity over admitted sequences m(s)>s. PD-T486 supplies only
sqrt(ceil(s/2))<=kappa_R(s;m)<=2sqrt(2)(s+1)(N_s-1) for R=BJ,mirror.
No matching exponent, asymptotic equivalence or proposed sharper bound
is asserted here.

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

Use exactly the nodes, positive weights, coordinates and graded order of PD-T485. Remain unsaturated, s<m; saturation s=m has zero normal space and does not settle this target.

## Status by part

Overall status: OPEN.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| The rate/criterion/robustness target stated above | OPEN | Tighten the legal normal lower and all-source upper to matching orders, preserving any m dependence. |

Candidate / claim disposition: Retained unresolved refinement of the proved polynomial classification; no new candidate mechanism.
Supporting results are separate dependencies, not proved parts of this target;
they do not upgrade it to PARTIAL.

## Depends on

PD-T485 Padua admission/cubature; PD-T486 polynomial classification.

## Checks

No new scientific check or computation was executed for this transcription.
The existing results and their finite verification scopes remain in their
linked records. [Audit 01](../audit-01.md) is the completed substantive
review; [audit 02](../audit-02.md) accepts the focused correction and
response dispositions, without claiming these OPEN targets are proved.

## Sources

Existing [candidate record](../ideas/P5.md), its linked supporting theory,
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

Tighten the legal normal lower and all-source upper to matching orders, preserving any m dependence.

## History

2026-11-06 — Codex, mechanical registration under the coordinator's reserved
range: transcribed the previously audited OPEN target at PR preparation,
following handoff 06. No mathematical development or status upgrade.
