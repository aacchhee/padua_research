# IDEA?argmax-bridge-codex-H02 — Matched signed endpoint correction

Aliases: H02; odd-offset endpoint matching; adjacent upper-endpoint layer.

- Question / scope: prove the original PD-T098 sharp corner expansion by
  sharpening PD-T269's exact signed deformation, for every sufficiently
  large integer n of both parities. Write m=n+1, a=2/pi and
  A_n=a(log n+gamma+log(8/pi)). The exact proposed estimate is
  Delta_n=kappa+(A_n^2+a*A_n-2)/m+O(log n/n^2).
- Mechanism and hypotheses: retain the exact PD-T159/269 summands,
  endpoint half weights and exceptional 1/m. Expand paired odd offsets
  only after subtracting the singular endpoint pieces exactly; handle
  l=1,j=n-r,k=j+1 using its true gap pi*r/(nm). The error must be
  bounded after summation uniformly in all indices, rather than merely
  for each fixed offset away from endpoints.
- Closest entries read in full: PD-T159; PD-T269/270/271; current C07
  finite nonnegative pairing; F03 origin sign idea/theory; IDEA-329
  original/final records and PD-T226. Full preparatory scope and relevant
  D03 normalization obstruction are in ../campaign-H-gate.md, read in
  full after root's release. D02 strip/sum records were also read.
- Separation criterion: an endpoint-complete finite signed correction
  with a proved summed O(log n/n^2) remainder distinguishes this from
  PD-T269's n^-1/5 convergence and F03's uncontrolled residual. A fixed
  offset formal coefficient, discarded endpoint strip, or untreated
  O(log^2 n/n) normalization erases the distinction.
- Literature baseline / limitations: inherit only the documented gate
  coverage; no PDF opened, external theorem imported, historical
  priority claim, or exhaustive literature assertion.
- Applicable obstructions: IDEA-289's adjacent endpoint mean-value
  overestimate; D03's uncancelled -(L_n^2-1)/m; F03/IDEA-329's invalid
  replacement of partial absolute rows by full signed rows. None is a
  theorem excluding signed endpoint matching. No full-row substitution
  or exact one-index evaluator is assumed.
- Novelty gate verdict: quantitative VARIANT/resume of IDEA-287/288/358
  toward the already registered OPEN PD-T098 target.
- Cheapest decisive test, written BEFORE derivation: derive the exact
  l=1 upper-endpoint summand in r=n-j and check its first uniform
  subtraction, including r=1 and the k=n weight. In parallel, check
  whether the remaining paired-offset expansion admits an absolutely
  summable remainder at the required scale.
- Kill criterion, written BEFORE derivation: any endpoint/parity/weight
  defect, or a proved residual estimate larger than the target that
  cannot be cancelled exactly, stops promotion of this route. Failure
  to obtain the bound leaves the target OPEN and the candidate deferred;
  it does not refute PD-T098.
- Test discriminability: the adjacent gap is O(n^-2), so a bound uniform
  only for bulk j/n cannot pass the first test. The second test checks
  precisely the unjustified interchange between a fixed-offset
  expansion and the full finite sum.
- Actual tests and disposition: pending at registration; PAPER ONLY,
  zero executable/scalar/numerical/native/quadrature jobs.
- Canonical record: ../attempts/H02-endpoint.md; a substantive proved
  result, if obtained, will be split into ../theory/H02-endpoint.md.
- History: 2026-11-07; requested/API Codex Sol ultra, serving metadata
  unexposed. Rules/input 2c69ba538473b8fdd9147635256289f74e75ccbb.
  Root released H02 after the completed gate. Hard-mathematics reason
  is recorded in ../campaign-H-20261107.md. This record precedes H02
  derivation. No Git/shared log/registry/other-round ownership.
