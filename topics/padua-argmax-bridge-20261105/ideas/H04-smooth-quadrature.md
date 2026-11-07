# IDEA?argmax-bridge-codex-H04 — Endpoint-complete smooth-residual quadrature

Aliases: H04; F03 two-pole smooth residual; centered partial-row quadrature.

- Question / scope: determine the complete expansion through 1/n of
  4 V_n/[n(n+1)], where V_n is EXACTLY F03 equation (8), for every
  integer n>=2 of either parity, with a concrete uniform remainder
  O(log n/n^2) or better. This support lemma does not include the
  harmonic contribution in F03 (7) or prove the full corner expansion.
- Mechanism and hypotheses: subtract BOTH cotangent poles as in F03,
  apply a locally proved midpoint/trapezoid formula with its actual
  displaced cell endpoints, and remove the outer t=0 cotangent pole
  by multiplying it by the inner integral before estimating. Retain
  m=n+1 exactly. Do not rename the nested residual as an evaluation.
- Closest entries read in full: completed campaign-H-gate.md; F03
  idea/attempt/theory; PD-T269/270/271. H01/H02/H03 prospective scopes
  were read for ownership coordination. The parent gate supplies the
  inventory, obstruction and literature comparison coverage; no new
  historical priority, external theorem or exhaustive novelty claim.
- Separation criterion: a proved endpoint-complete finite-n expansion
  with a uniform summed O(log n/n^2) remainder, escaping F03's
  nonvanishing coarse sup|B| bound. A formal sequence, omitted endpoint,
  or error larger than the target erases the distinction.
- Applicable obstructions: F03's nested residual is still a real sum;
  its bound by a constant is insufficient. PD-T270's scalar midpoint
  bound does not itself control this triangular, weighted residual.
  D03's normalization charge remains another lane's full-corner duty.
- Novelty gate verdict: quantitative VARIANT of the existing gated
  F03/IDEA-287/288/358 route, restricted to a sharply stated support lemma.
- Cheapest decisive test BEFORE proof: compute the exact center and
  cell union for the r samples; retain the first endpoint displacement
  and the outer t=0 trapezoid term. Check whether their signed 1/n
  coefficient cancels, rather than assuming centering eliminates it.
- Kill criterion BEFORE proof: an unremoved pole, wrong sample center,
  missed endpoint/parity term, uncontrolled outer derivative, or summed
  error larger than O(log n/n^2) stops promotion. A nonzero 1/n term
  refutes only the zero-coefficient subguess, not the expansion route.
- Test discriminability: exact sample algebra determines the endpoint
  displacement; a finite derivative bound and quadrature remainder
  determine uniformity without numerical evidence.
- Actual results: after preregistration, exact cell algebra and uniform
  quadrature proved 4V_n/[n(n+1)]=C_B+beta_B/n+R_n with |R_n|<=17/n^2
  for every n>=2. Explicit endpoint-removed integrals define C_B,beta_B
  in the theory. Also -4/pi^2<beta_B<0, so the zero-coefficient subguess
  is disproved. Both parities and every row endpoint are included.
- Disposition: support target PROVED by written PAPERONLY analysis;
  distinct review/adoption remains the root's responsibility. No full
  corner target, harmonic aggregate or exact evaluator is claimed.
- Canonical records: ../attempts/H04-smooth-quadrature.md and
  ../theory/H04-smooth-quadrature.md if the result is established.
- History: 2026-11-07; parent-assigned Codex mathematical developer,
  requested/API inherited serving metadata not independently exposed.
  Rules/input ad257038cdff1d66f6e9c03d7ed43405c76cf6b0. Own only
  this H04 idea/attempt/theory trio; root owns Git and shared records.
  No jobs, code, numeric evidence, PDF, extra H round or delegation.
