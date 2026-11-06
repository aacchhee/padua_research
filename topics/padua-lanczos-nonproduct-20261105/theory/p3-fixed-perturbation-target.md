# PD-T494 — n-independent SH perturbation robustness target

ID kind: PD-T.
Provisional ID: PD-T?lanczos-nonproduct-codex-P3-04.
Aliases: fixed smooth density; fixed nonlinear node map; moment-visible perturbation.
Split from: the existing OPEN target retained in IDEA-577; this record transcribes that target without changing its scope.
Split into: none; the supporting results below keep their own statements and statuses.

## Statement

Determine whether BJ/comparator aggregate separation persists for one
n-independent perturbation of the SH_n family: either one fixed bounded
smooth nonmultiplicative density 1+eta phi(s,t), or one fixed smooth
nonlinear node map applied to SH_n for every n. Preserve the original
robustness/radius question and the distinction between a sufficient-radius
estimate and an obstruction to every larger radius. No fixed phi, node
map, successful radius, exponent or separation theorem is supplied here.
The proved changing-high-mode, moment-invisible construction PD-T480
is a distinct weaker variant and does not resolve this target.

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

Keep the aggregate source/output model, positivity and injective finite measures. The perturbation function or node map is fixed independently of n; perturbed low moments and the actual normal space must both be controlled.

## Status by part

Overall status: OPEN.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| The rate/criterion/robustness target stated above | OPEN | First bound the actual normal-quotient map using degree-<=2n moments and creator control, then examine the original N4 polynomial-radius question. A sufficient estimate decaying faster than every polynomial kills that estimate, not the robustness target. Refresh the gate in the follow-up. |

Candidate / claim disposition: Deferred; resume only in a follow-up explicitly assigned to the n-independent perturbation; no proof status is attached to the deferred IDEA.
Supporting results are separate dependencies, not proved parts of this target;
they do not upgrade it to PARTIAL.

## Depends on

PD-T478/479/480 weaker variant; PD-T482/484 framework; PD-T324 predecessor; IDEA-577.

## Checks

No new scientific check or computation was executed for this transcription.
The existing results and their finite verification scopes remain in their
linked records. [Audit 01](../audit-01.md) is the completed substantive
review; [audit 02](../audit-02.md) accepts the focused correction and
response dispositions, without claiming these OPEN targets are proved.

## Sources

Existing [candidate record](../ideas/P3.md), its linked supporting theory,
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

First bound the actual normal-quotient map using degree-<=2n moments
and creator control, then examine the original N4 polynomial-radius
question. A sufficient estimate decaying faster than every polynomial kills
that estimate, not the robustness target. Refresh the gate in the follow-up.

## History

2026-11-06 — Codex, mechanical registration under the coordinator's reserved
range: transcribed the previously audited OPEN target at PR preparation,
following handoff 06. No mathematical development or status upgrade.
