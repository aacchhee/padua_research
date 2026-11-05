# padua-lebesgue-followups-20261103 — small follow-ups for the Padua Lebesgue-function paper

This file is written only by the topic orchestrator. Branch `codex/padua-lebesgue-followups-20261103`; [draft PR #20](https://github.com/aacchhee/padua_research/pull/20).

## Status (2026-11-05): registration checked — draft awaiting AC budget decision

Four bounded targets, specified in [handoff 01](../topics/padua-lebesgue-followups-20261103/handoffs/01-work.md):

- **T1:** certified n = 8 maxima count (PD-T180/184; PROVED 44/16/2 = 62; certified candidate correction of LIT-388 v1 Table 3’s numerical 38/56).
- **T2:** centre-minimality of the edge-defect integrals g_v and g_h.
- **T3:** a general-β series for them.
- **T4:** the constant term c (κ = c − c₁²) of the corner expansion (PD-T098).

T1: PD-T184 and PD-T180 are PROVED: exactly 44 interior and 62 total strict
maxima. Both complete original interior and boundary predicate blocks were
independently replayed; fresh generation, exact proof identity, literal joining
and both original-accounting compositions completed. No developer monolithic joined run
is claimed; Claude subsequently completed one as audit evidence. [Count proof](../topics/padua-lebesgue-followups-20261103/theory/t1-closed-count.md).
T2–T4 core analytic targets are complete and accepted by Claude audit-01.

- **PROVED PD-T266, Claude audit-01 accepted:** both limiting
  edge defects have unique centre minima, vertical `g` and horizontal exactly
  `1`. [Theory](../topics/padua-lebesgue-followups-20261103/theory/t2-01-edge-centre-minima.md).
- **PROVED PD-T267, Claude audit-01 accepted:** common
  logarithmic endpoint expansion with explicit errors.
  [Theory](../topics/padua-lebesgue-followups-20261103/theory/t2-02-common-endpoint-expansion.md).
- **PROVED PD-T268, Claude audit-01 accepted:** general-position
  geometric series with rigorous tails, exact-Fraction enclosures and direct
  outward quadrature independently rerun at five positions.
  [Theory](../topics/padua-lebesgue-followups-20261103/theory/t3-01-general-position-series.md).
- **PROVED PD-T271, Claude audit-01 accepted:** parity-independent
  corner constant `c`, with an explicit vanishing remainder and independently
  reproduced enclosure
  `1.846160310423926079759838737947 < c < 1.846160310423926079759838737948`.
  [Constant](../topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md),
  [PD-T269 defect limit and series](../topics/padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md),
  [PD-T270 one-dimensional bound](../topics/padua-lebesgue-followups-20261103/theory/t4-02-one-dimensional-remainder.md), sharpening the predecessor PD-T158 estimate.

Final registration assigns PD-T266–271 to t2-01/02, t3-01 and t4-01/02/03,
respectively; every provisional alias is retained. IDEA-356/357/358 retain the
T2/T3/T4 candidates; T1 reuses IDEA-299 and existing PD-T180/184.
The full PD-T098 expansion, including `-1/N` and `O(log N/N²)`, stays
OPEN. No finite-degree or all-degree argmax conclusion is added here.

Protocol qualification: some linked full T2/T3 candidate/attempt reads were
completed after the first mechanisms. Later reading and supplementary review
do not retroactively cure that timing deviation. Claude confirmed minor impact,
with acceptance of the recorded deviation left to AC. Physical cold-storage delivery remains pending.

## Claude audit-01 (2026-11-05)

Mathematics ACCEPTED for all four targets ([audit-01](../topics/padua-lebesgue-followups-20261103/audit-01.md)). Independent auditor evidence:
- a monolithic original n=8 `Verifier.run` (archived interior + independently regenerated boundary) certified 44 + 16 + 2 = 62 in one process;
- an Arb digamma-route enclosure of κ confirmed the κ and c brackets.

All nine MINOR findings (wording, proposal format, provenance/budget notes) are answered by editorial fixes in [response-01](../topics/padua-lebesgue-followups-20261103/response-01.md). Registration, fresh reservation checks, integration rehearsal and independent preparation review are complete. PR20 remains draft because the aggregate storage budget needs an explicit AC decision. The T2/T3 gate-timing deviation is recorded with minor impact and left for AC's decision.

## Current boundary and post-merge frontier

Stage: PR, readiness blocked by the aggregate storage budget. Final registration,
fresh reservation checks, integration rehearsal and independent preparation review
are complete. The conservative non-record total is 4,851,736 bytes, only 2.97%
below 5 MB; the workflow requires “well below.” [Independent review](../topics/padua-lebesgue-followups-20261103/preparation/independent-review.md)
records this as the sole readiness blocker. AC must explicitly accept this budget
or authorize a scoped reduction before readiness. The accepted mathematics is
unchanged. No further mathematical campaign is assigned.

Dated 2026-11-05 supersession: earlier CURRENT/RESULTS center-minimality and
general-β-series OPEN clauses are historical and superseded only at the proved
limiting-integral scopes PD-T266/268. Earlier exact n8 count OPEN clauses are
superseded only by PD-T184/180; failed/deadline attempts remain history.
PD-T100 remains MEASURED, PD-T183 remains the separate lower bound, and
PD-T181 remains the separate accepted global theorem. After merge, these
registrations and completed results remain the topic's outcome; PD-T098's sharp
expansion and PD-T099's all-degree bridge retain their separate OPEN scopes.
Finite PSLQ nulls remain MEASURED. No finite-degree ordering, broader count,
priority, manuscript or author-contact claim follows. The certified 44/62 is
only a candidate correction of the inspected LIT-388 v1 Table 3 numerical 38/56;
no accepted erratum or later-version coverage is claimed.

The T2/T3 prospective-gate deviation remains confirmed, not waived or cured;
[audit-01](../topics/padua-lebesgue-followups-20261103/audit-01.md) and
[response-01](../topics/padua-lebesgue-followups-20261103/response-01.md) preserve
its minor-impact assessment for AC's decision. Physical cold-storage delivery
remains pending. Only AC merges.
