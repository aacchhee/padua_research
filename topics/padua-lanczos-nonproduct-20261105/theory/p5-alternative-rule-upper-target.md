# PD-T493 — Padua alternating and frozen-pivot upper targets

ID kind: PD-T.
Provisional ID: PD-T?lanczos-nonproduct-codex-p5-04.
Aliases: all admissible parents; arbitrary X/Y switching upper.
Split from: the existing OPEN target retained in IDEA-584; this record transcribes that target without changing its scope.
Split into: none; the supporting results below keep their own statements and statuses.

## Statement

For the exact positive Padua measures nu_m with integers m>=2 and
1<=s<m, determine capacity upper bounds for alternating and frozen-pivot
parent rules in the declared aggregate model. Retain the broader IDEA-584
question of extending a polynomial upper to every admissible X/Y parent
pattern. No polynomial upper, exponent or uniform constant for those
rules is asserted. The BJ/best ratio consequence in PD-T486 uses a
universal capacity floor and does not prove these individual uppers.

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

Use PD-T485 exact data and positive weights. Each branch has fixed admissible parents; pivot ties and choices are frozen before differentiation. Adaptive switching beyond fixed branches is separate.

## Status by part

Overall status: OPEN.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| The rate/criterion/robustness target stated above | OPEN | Obtain a common bound across arbitrary parent switching, or a rule-specific proof; BJ two-chain formulas alone do not supply it. |

Candidate / claim disposition: Deferred to a concrete need following the BJ/mirror outcome; no PD-N for the undeveloped route.
Supporting results are separate dependencies, not proved parts of this target;
they do not upgrade it to PARTIAL.

## Depends on

PD-T485 admission; PD-T486 BJ/mirror result and universal floor; IDEA-584.

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

Obtain a common bound across arbitrary parent switching, or a rule-specific proof; BJ two-chain formulas alone do not supply it.

## History

2026-11-06 — Codex, mechanical registration under the coordinator's reserved
range: transcribed the previously audited OPEN target at PR preparation,
following handoff 06. No mathematical development or status upgrade.
