# IDEA?padua-argmax-bridge-20261105-codex-corner-01 — Actual per-degree corner energy

Aliases: N3 practical corner radius; outward W_n; quantitative IDEA-330/457.

- Question/scope: enlarge the existing finite-cover corner predicate at
  n=33,64,128 by computing actual weighted gradient energy, with an
  independently checkable exact/outward certificate.
- Mechanism/hypotheses: PD-T227 aggregate Taylor inequality, PD-T251 slopes,
  PD-T368 global norm bound, and verified 0<ell<=Lambda_c, W_n<=E.
  Put b=E/(n^4 ell), K=u/ell and kappa=min(1,1/[8(b+3K)]).
- Closest entries read: IDEA-330/454/457 and their linked bounds; precise
  reading scope in `../novelty-gate-N3-corner.md`.
- Separation: computationally larger verified per-degree physical radius,
  not a different theorem mechanism. Failure to enlarge the usable old
  radius erases the proposed practical distinction.
- Literature baseline/limits: inherited locally proved formulas only;
  no external theorem, fulltext or priority claim.
- Obstructions: N085/N086 do not apply to aggregate sign-change control;
  zero-cardinal terms are handled by the inherited inward slopes.
- Verdict: implementation/quantitative variant, consolidated with the
  existing aggregate route; no new mathematical mechanism proposed.
- Cheapest test: analytic implication, direct-kernel small-degree check,
  then outward sums n33/64/128 and distinct replay.
- Kill criterion before testing: do not use an unverified energy bound;
  record non-enlargement or impractical cost honestly. No arbitrary cap
  refutes the inherited corner theorem or PD-T099.
- Test discrimination: exact endpoint inequalities prove only this local
  predicate. Floating agreement alone supplies diagnostics; a full cover
  and independent replay are separate.
- Actual results: completed directed producer n33/64/128; all three exact
  rational candidates have kappa>1/12500. Developer numerical diagnostic
  checks 145 nonzero cardinals n2–8; distinct outward replay is pending.
  Receipt `../evidence/n3-corner-bounds.json` pins endpoints/code/commands.
- Disposition: retained implementation continuation; per-degree acceptance
  pending independent replay.
- Canonical theory: `../theory/N3-corner-radius-reduction.md` (analytic
  reduction), with computed bounds recorded separately.
- History: 2026-11-05, Codex, parent-assigned Sol xhigh,
  rules/input 714f3cad18859c07cd13f31561f2a185f9591a7f. No Git mutation.
