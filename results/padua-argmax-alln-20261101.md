# padua-argmax-alln-20261101 — strategy for the all-degree Padua argmax (A4 / PD-T099)

This file is written only by the topic orchestrator. Branch `claude/padua-argmax-alln-20261101`; no PR yet.

## Status (2026-11-01): WORK (planning)

The strategy note is written. It is to be updated after part 2 (PR #12) finishes and is audited ([handoff 01](../topics/padua-argmax-alln-20261101/handoffs/01-update-after-part2.md)).

## Results

- **PD-T?argmax-alln-claude-01 (MEASURED)**, [record](../topics/padua-argmax-alln-20261101/theory/argmax-alln-claude-01-measured-observations.md). Float64 observations:
  - The shifted-lattice majorant S ≥ λ_n is not maximal at the coset point. It exceeds Λ_c by 1.4e-3 (n = 3) down to 9.2e-5 (n = 40).
  - The corner beats the deep interior only by O(1), about 1.75 for n = 8…48, and the edge by about 0.55. No log-scale separation exists.
- **IDEA?argmax-alln-claude-01** (majorant maximal at the coset): REJECTED: failed, MEASURED. Retained as a discard tool.
- **IDEA?argmax-alln-claude-02** (scaled local profiles + n-independent cell certificates + finite certifier), **-03** (Brutman-type monotonicity / pairing) and **-04** (generating-curve factorisation): deferred, untested.

## Next step

After part 2 is done: `Claude (Opus 5.5 xhigh): Continue claude/padua-argmax-alln-20261101.` That step revises the plan and writes the part 3 Codex prompt.
