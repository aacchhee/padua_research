# IDEA?mz-sharp-codex-P1-01 — identify the accepted B by its elliptic kernel

Aliases: Schloemilch kernel; Poisson-regularized Bessel kernel; nonpositive
corner kernel; positive-vector spectral certificate.

- Question / scope: prove the exact integral-kernel formula in handoff03
  for the already accepted compact B on H=L2(D,ab da db), with the literal
  product truncation of S3-03. Then check the nonpositive-kernel spectral
  consequences, separately from numerical decimal enclosures.
- Mechanism and hypotheses: derive the Bessel product and Schloemilch
  identities locally, regularizing by Abel/Poisson damping where needed;
  identify forms first on a dense compactly supported smooth domain,
  prove boundedness of the proposed integral operator, and use uniqueness
  of the accepted norm limit. All variables retain 0<a,b,a',b'<1 and
  a+b<1, a'+b'<1; singular boundaries are treated as null sets or integrable
  limits, never silently assigned finite pointwise values.
- Closest registry entries (read in full): S3-03 and IDEA-470, IDEA-217 /
  PD-N048, IDEA-471, IDEA-058, IDEA-357 / PD-T268 and IDEA-420 / PD-T331.
  Complete gate and source coverage: ../novelty-gate-P1.md.
- Separation criterion vs closest entry: equality of this closed integral
  operator with the accepted product-truncated B, including every
  normalization and any diagonal/distributional term. Existing pointwise
  sums or Nyström agreement do not establish that property. Finding a
  nonzero omitted distributional term, a failed boundedness estimate, or
  unequal forms on the dense test domain falsifies this identification.
- Literature baseline and search limitations: supplied classical
  Schloemilch/Gegenbauer route; no historical novelty or priority claim.
  The bounded verified repository search is documented in the gate.
  Classical formulas are to be proved locally or inspected in fulltext
  before becoming dependencies; the audit's floating support is a lead.
- Applicable obstructions and exact hypotheses broken: PD-N048 forbids
  negative-corner-only control; here the complete signed B is retained.
  IDEA-471 blocks identification from unnormalized coefficients or finite
  slopes. Conditional convergence blocks an unproved rearrangement; the
  dense-domain and regularization argument is the decisive obligation.
- Novelty gate verdict: variant with difference, explicit completion of
  supplied S3-03/IDEA-470, with known kernel summation and Schur ingredients.
- Cheapest decisive test: local Fourier/Poisson derivation of the scalar
  sum, then rapid decay of smooth-test Bessel coefficients and a bounded
  integral-kernel majorant. No numerical run is needed for this test.
- Kill criterion written before testing: a demonstrably false formula or
  surviving omitted term kills that formula at its proved scope; inability
  to justify an exchange leaves the target OPEN and records the precise
  obligation. A failed proof route does not reject PD-T381.
- Test discriminability: exact dense-domain equality plus boundedness
  identifies a unique bounded operator; pointwise agreement or a finite
  spectral comparison cannot substitute for either hypothesis.
- Resources / cost ledger: up to six bounded analytic rounds, stop after
  two consecutive no-progress rounds. This worker performs no numerical
  calculations or code runs. Any numerical protocol must be separately
  published by the coordinator before execution by its code developer.
- Actual test results and evidence: rounds 1-2 supplied exact bounded
  operator identification and the positive simple ground-state/norm
  consequences in ../theory/P1-elliptic-kernel.md and
  ../theory/P1-positive-spectrum.md. The distinct supplementary
  reconstruction in ../independent-checks-P1-kernel.md found no
  mathematical gap in either frozen proof. No numerical run occurred.
- Disposition and precise rejected scope, if any: retained supplied route;
  analytic statements PROVED as new development with supplementary
  reconstruction complete, focused Claude audit and registry readiness
  still pending. Decimal certification remains OPEN.
- Disposition reason: not rejected. The local derivation controlled
  regularization mass, dense-test ordering and bounded extension; the
  common intermediate wedge supplied the exact irreducibility property.
  Response R publication clearance was
  17ca9f441cece178354e70504a6c739df501a224 before development began.
- Canonical theory / negative-result ID: provisional P1-01 and P1-02 in
  the theory files above; no final ID or PD-N allocated by this worker.
- Topic / completed audit link / history: 2026-11-06, Codex P1 developer,
  requested gpt-6.1-sol xhigh; runtime serving metadata unexposed. Input
  0205690b9c4e959a28e949083e9a1808735abf4b; this record precedes derivation.
