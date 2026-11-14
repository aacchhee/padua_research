# IDEA?bridge-N3 — whole-sum mean-value implementation

Aliases: N3; signed derivative accumulation; reflection-first Taylor enclosure.

- Question/scope: finish the existing finite phase-cover design at n33/64/128.
- Mechanism/hypotheses: PD-T364 acceptance with interval-AD primitive gradients,
  center values and whole-sum mean-value bounds, retaining zero-crossing hulls.
- Closest full entries: IDEA-320/343/344/454; inherited baseline and the precise
  gate in `../novelty-gate-N3.md` record reading limits.
- Separation: only enclosure/implementation improvement; no new mathematics.
  A failed complete-cover B2 test removes the claimed practical advantage.
- Literature: no external source imported, no historical novelty claim.
- Obstructions: PD-N079 requires defect/corner predicates; PD-N085/086 forbid
  assumed affine/coarse signs. The implementation does not assume either.
- Verdict: implementation variant, retained for the exact bounded test.
- Cheapest test and kill: direct-polynomial agreement, then complete B2 counts;
  handoff01 B2 is unchanged, including one order escalation after its kill.
- Actual results: pending; `../attempts/N3.md` owns executed outcomes.
- Disposition: retained/OPEN. No new negative result or global ID allocated.
- Canonical dependency: PD-T364 (phase) and PD-T210 (frozen native extension).
- History: 2026-11-05 Codex Sol medium development; independent replay pending.
