# PD-T300 — finite signed Padua frontier measurements

ID kind: PD-T. Development alias: `PD-T?mz2d-frontier-codex-92`.
Aliases: G1–G4 finite float extension; continuous angular localization;
exploratory m1600 negative Rayleigh candidate. Split from: audited report
and numerical-results finite observations. Split into: exact finite
m60/m80 brackets are separate PROVED PD-T298/299, never inferred here.

## Statement

The committed floating implementations returned the finite observations
listed below under the frozen signed Lebesgue Padua conventions. These
are measured solver/quadrature outputs, not rigorous enclosures of exact
spectral extrema. No asymptotic law or finite negative exact certificate
is asserted by this record.

- Complete paired endpoint grid m=60,80,100,120,150,200,250,300,400,
  n=m−1, with upper value at400 about1.8733622908154 and lower about
  0.1028189062339. The preregistered heldout upper600/800/1000 grid
  was not completed, so fit verdict is INCONCLUSIVE.
- At m=100,200,400 the upper eigenvector’s continuous dxdy L2 mass
  within the K=10 angular edge union is about0.4401356,0.3577649,
  0.2934516. The last value kills the original localized R1 criterion
  (<50%). The m400 lower vector instead has corner mass0.7775087
  and edge-union mass0.8813374. This does not classify all limiting
  operators or actual asymptotic eigenvector families.
- Every integer m=2..239 was screened at n=m−1 andm−2 (476 rows),
  with no floating threshold hit and maximum residual3.70e−11.
  Requested m240..300 coverage was not executed.
- Minimum-only values at m=800,1000,1200,1600 are approximately
  0.04002526215,0.01965947201,0.00297687255,−0.02341441659.
  The final two degrees are posthoc exploratory scope. At m1600,n1599,
  the saved vector has float residual1.95e−13; it is an uncertified
  negative Rayleigh candidate, not a PROVED finite counterexample.
- Additional finite Fejer, corner-kernel and carrier probes through
  m2000 remain at their explicitly stored parameters and measured
  scope. No extrapolation or global extremum follows from them.

## Definitions and assumptions

Use the unchanged definitions in topics/padua-mz-2d-20261101/definitions.md:
Pi_n total degree, unnormalized dxdy, even checkerboard with denominators
m,m+1, actual signed interpolatory weights. Coefficients are expressed
in continuously orthonormal Legendre products. Localization uses angular
edge union and corner squares defined before the runs in numerical-plan.md,
with physical dxdy L2 mass, not nodal signed mass.

## Status by part

Overall status: **MEASURED**. Every observation above is finite floating
output; no status upgrade is made by moving it into a durable home.
Candidate dispositions are separately retained in IDEA384–397. The
analytic refutations PD-N105–107 and uniform norm theorem PD-T297 have
independent analytic proofs and do not depend on this record.

## Depends on

PD-T106 exact definitions/alias context and the frozen numerical
implementation/validation conventions. No claimed numerical tolerance
is an assumption proving an exact signed spectral statement.

## Checks and evidence

This is a mechanical transcription of audit-01 accepted report and
numerical-results scopes at input7a8d8dd313b5370589810f4efd910ed65744f865.
No new computation was performed during preparation. Full commands,
code hashes, versions, seed20261105, ncv/tolerance changes, timings,
matvec counts and actual stopped jobs are in [numerical-results](../numerical-results.md).
Compact receipts: [validation](../evidence/g1-validation.json),
[scaling](../evidence/g1-scaling.json), [fits](../evidence/g1-fits.json),
[localization](../evidence/g1-localization.json),
[screen](../evidence/g1-screen.json),
[minimum-only](../evidence/g1-minimum-only.json), and the three trial
receipts g1-fejer/g1-corner-trial/g1-carrier.json. Their bytes are unchanged.
Small dense comparisons include oddm9/11; quadrature used degree-sufficient
Gauss orders with refinement (max m400 fraction discrepancy6.48e−11).
Residuals are diagnostics, not interval acceptance.

## Sources

Local audited numerical-results/report only. No primary external theorem,
priority claim, new novelty candidate or literature record is added.

## Scope and open items

Exactly the finite observations above, at the detailed receipt parameters.
The negative m1600 point needs exact or outward-rounded finite acceptance
before a finite PROVED PD-N could be asserted. Effective carrier onsets,
odd-m behavior, exact asymptotic extrema and practical witnesses remain
outside these measurements. Bulk vectors/screens are regenerable scratch,
with pending external delivery; no archival retrieval is promised.

## History

2026-11-05, Codex gpt-6.1-sol medium: registered accepted finite numerical
observations from the existing audited reports under a distinct MEASURED
ID, without rerunning, refitting, extending scope or promoting evidence.
