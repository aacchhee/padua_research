# padua-argmax-effective-2-20261105 — effective all-degree Padua argmax, phase 2

This file is written only by the topic orchestrator. Branch `codex/padua-argmax-effective-2-20261105`; no PR yet.

## Status (2026-11-05): WORK, topic set up

Phase 1 (PR #19) left the following:

- PD-T099 is certified for 2 ≤ n ≤ 32.
- The eventual theorem PD-T229 holds with a non-effective threshold.
- The all-degree corner slopes are proved (PD-T251).

Making the existing localization chain effective would need log n ≳ 3×10⁵; this diagnosis is to be checked as gate A0. Phase 2 therefore tries a new architecture, specified in [handoff 01](../topics/padua-argmax-effective-2-20261105/handoffs/01-work.md):

- **H1:** a per-degree certifier on the fixed phase diamond, with expected cost of about n² × boxes.
- **H2:** sharp, explicit asymptotics for n ≥ N₁.
- **H3:** corner-zone control at physical scale n⁻².

No results yet.

## Next step

`Codex (gpt-6-astra ultra): Continue codex/padua-argmax-effective-2-20261105.`
