# padua-lebesgue-followups-20261103 — small follow-ups for the Padua Lebesgue-function paper

This file is written only by the topic orchestrator. Branch `codex/padua-lebesgue-followups-20261103`; [draft PR #20](https://github.com/aacchhee/padua_research/pull/20).

## Status (2026-11-03): AUDIT, core development complete; Claude review pending

Four bounded targets, specified in [handoff 01](../topics/padua-lebesgue-followups-20261103/handoffs/01-work.md):

- **T1:** certified n = 8 maxima count (PD-T180/184; PROVED 44/16/2 = 62 against the numerical source 38/56).
- **T2:** centre-minimality of the edge-defect integrals g_v and g_h.
- **T3:** a general-β series for them.
- **T4:** the constant term c (κ = c − c₁²) of the corner expansion (PD-T098).

T1: PD-T184 and PD-T180 are PROVED: exactly 44 interior and 62 total strict
maxima. Both complete original interior and boundary predicate blocks were
independently replayed; fresh generation, exact proof identity, literal joining
and both original-accounting compositions completed. No monolithic joined run
is claimed. [Count proof](../topics/padua-lebesgue-followups-20261103/theory/t1-closed-count.md).
T2–T4 core analytic targets are complete; required Claude audit is pending.

- **PROVED, supplementary check accepted; Claude audit pending:** both limiting
  edge defects have unique centre minima, vertical `g` and horizontal exactly
  `1`. [Theory](../topics/padua-lebesgue-followups-20261103/theory/t2-01-edge-centre-minima.md).
- **PROVED, supplementary check accepted; Claude audit pending:** common
  logarithmic endpoint expansion with explicit errors.
  [Theory](../topics/padua-lebesgue-followups-20261103/theory/t2-02-common-endpoint-expansion.md).
- **PROVED, supplementary check accepted; Claude audit pending:** general-position
  geometric series with rigorous tails, exact-Fraction enclosures and direct
  outward quadrature independently rerun at five positions.
  [Theory](../topics/padua-lebesgue-followups-20261103/theory/t3-01-general-position-series.md).
- **PROVED, supplementary check accepted; Claude audit pending:** parity-independent
  corner constant `c`, with an explicit vanishing remainder and independently
  reproduced enclosure
  `1.846160310423926079759838737947 < c < 1.846160310423926079759838737948`.
  [Constant](../topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md),
  [defect limit and series](../topics/padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md),
  [one-dimensional bound](../topics/padua-lebesgue-followups-20261103/theory/t4-02-one-dimensional-remainder.md).

The new records currently use their provisional IDs in the linked titles.
The full PD-T098 expansion, including `-1/N` and the sharper remainder, stays
OPEN. No finite-degree or all-degree argmax conclusion is added here.

Protocol qualification: some linked full T2/T3 candidate/attempt reads were
completed after the first mechanisms. Later reading and supplementary review
do not retroactively cure that timing deviation; Claude must give an explicit
protocol disposition. Physical cold-storage delivery remains pending.

## Next step

`Claude (Opus 5.5 xhigh): Continue codex/padua-lebesgue-followups-20261103.`
