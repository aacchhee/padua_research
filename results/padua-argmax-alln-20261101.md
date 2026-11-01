# padua-argmax-alln-20261101 — strategy for the all-degree Padua argmax (A4 / PD-T099)

This file is written only by the topic orchestrator. Branch `claude/padua-argmax-alln-20261101`; no PR yet.

## Status (2026-11-01, evening): WORK

Plan v2 is written after PR #12 merged ([plan](../topics/padua-argmax-alln-20261101/plan.md)). Part 3 development is handed to Codex ([handoff 02](../topics/padua-argmax-alln-20261101/handoffs/02-part3-work.md)).

## What part 2 already gives toward the all-n argmax

- **Corner value and asymptotics:** PD-T101 and PD-T156–159.
- **Global argmax certified** for n = 3…7: PD-T162/166/169/174/177. The n = 8 global maximum is OPEN (PD-T181).
- **The runner-up is identified and its gap proved in the limit:** the central vertical-edge envelope satisfies R_cen = Λ_c − g + o(1), with g ≈ 0.5485 (PD-T192).
  - The mechanism is λ = majorant − triangle defect, together with phase localization (PD-T189–191). It is the edge case of this topic's reflected-lattice identity.

## Results of this topic

- **PD-T?argmax-alln-claude-01 (MEASURED)**, [record](../topics/padua-argmax-alln-20261101/theory/argmax-alln-claude-01-measured-observations.md).
  - The four-copy majorant S ≥ λ_n is not maximal at the coset point: excess 1.4e-3 at n = 3, down to 9.2e-5 at n = 40.
  - Interior gap about 1.75 (n = 8…48).
- **PD-T?argmax-alln-claude-02 (MEASURED)**, [record](../topics/padua-argmax-alln-20261101/theory/argmax-alln-claude-02-measured-edge-profile.md).
  - Vertical-edge gap is smallest at the centre: 0.557 at n = 96, consistent with g.
  - The vertical-edge gap rises toward both ends.
  - Horizontal-edge gap is about 1.
  - Near-edge strips are dominated by edge values.
  - n = 2 has no competitor in the scans, but is uncertified.
- **Ideas:**
  - IDEA?argmax-alln-claude-01 (majorant alone): REJECTED: failed, MEASURED; retained as a sub-tool.
  - IDEA-02 (S − Δ in all regimes, plus effective n₀; a variant of IDEA-305) and IDEA-05 (global-max-only certifier): active.
  - IDEA-03 (monotonicity) and IDEA-04 (generating-curve factorization): deferred.

## Remaining obligations (plan v2 §4)

- P0: certify n = 2.
- P1: whole vertical edges.
- P2: horizontal edges.
- P3: corner neighbourhoods.
- P4: interior.
- P5: strips between edges and interior.
- P6: effective threshold n₀ and certification of 8 ≤ n < n₀.

The main risk is effectivity: the proved gap is only 0.5485, against non-effective remainders.

## Next step

`Codex (gpt-6.1-sol xhigh): Continue claude/padua-argmax-alln-20261101.` This runs the pre-registered tests T1–T5, then P0, P1/P2, the P6 estimate, P3 and P4, following handoff 02.
