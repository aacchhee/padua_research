# IDEA-611 — exact finite-trial Rayleigh lower bound

2026-11-06 ID history: `IDEA?mz-sharp-codex-P4-01` → `IDEA-611` (retained record consolidated under this ID); statements, original registrations and historical dispositions are preserved.

Aliases: dyadic interval Gram; certified endpoint lower decimal.

- Question / scope: certify only Lambda_edge >= 1.0044369, with accepted
  fixed-J model and J=512. No numerical upper bound is proposed.
- Mechanism and hypotheses: accepted S2 finite-trial Rayleigh inequality;
  exact binary-rational trial; integer interval scalar evaluation.
- Closest registry entries: IDEA-466 (dyadic outward-enclosure certifier;
  fixed-point trial-energy witness), IDEA-058, accepted S2 continuation of IDEA-386;
  reading/provenance limits in ../novelty-gate-P4.md.
- Separation criterion: finite check with rigorous outward rounding rather
  than a high-precision floating Rayleigh value. Missing enclosures erase
  this distinction; no new analytic model is asserted.
- Literature baseline and search limitations: local accepted formulas and
  elementary Taylor/Laplace integral identities only; no priority claim.
- Applicable obstructions: retain the actual C,D and degree-constrained
  f_j; do not infer norm convergence from floats or discard signs.
- Novelty gate verdict: consolidated technical continuation.
- Cheapest decisive test: a single exact trial quotient enclosure.
- Kill criterion before testing: denominator interval must be positive and
  the quotient lower endpoint at least 10044369/10000000. Failure after
  at most two successive no-progress rounds stops this direction; no
  theorem or trial family is refuted by such failure.
- Test discriminability: exact rational comparisons decide this threshold;
  approximate solver output only supplies the trial and has no proof role.
- Resources: one single-threaded float trial solve, one producer check,
  one distinct-agent rerun/check; at most 6 h/run, cumulative shared 48
  CPU-h, at most 2 heavy processes globally. No Syvert/network install.
- Actual test results and committed evidence: one planned round executed
  after protocol/source publication d03e74dcf94020ba26d9fae84d3ff6c5519db901;
  producer and grouped form checker pass. q(u) is enclosed near
  1.00443691886466728045777, strictly above the target. See ../attempts/P4.md
  and evidence/P4-rayleigh.json. Distinct actual rerun and scalar/code/
  reduction review PASS: ../independent-checks-P4.md. Required Claude
  focused audit remains separate; root controls theorem/status integration.
- Disposition: retained lower certificate; practical upper deferred.
- Disposition reason: accepted finite-J reduction makes the lower cheap;
  existing upper certificate has a documented prohibitive discretization
  error/cost at three digits. Resume upper only with a justified finite
  reduction and costed refreshed candidate.
- Canonical theory: accepted S2-04/05 dependencies; new decimal claim
  requires a separately reviewed finite reduction and independent rerun.
- Topic/history: 2026-11-06 after R publication, before evaluation.

## 2026-11-06 audit-02 C3 predecessor clarification

Full IDEA-466 [candidate](../../padua-mz-cleanup-20261105/novelty-gate-math.md#idea-466--dyadic-outward-finite-witness-certifier)
was read for this correction. It already supplies the exact dyadic
finite-witness/outward-energy pattern with positive norm and independent
checking. P4 applies this pattern to the accepted S2 endpoint-model
quotient and its continuum denominator, rather than the finite Padua
polynomial's complete signed nodal energy. Only that object/reduction
separates the implementations; missing endpoint reduction or rigorous
scalar bounds invalidates this instance. The consolidated technical
continuation verdict remains unchanged; no new mechanism is claimed.
