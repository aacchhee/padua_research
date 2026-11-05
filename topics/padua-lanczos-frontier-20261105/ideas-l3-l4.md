# L3/L4 candidate memory

Rules/input SHA: `8359bf7a047d9a212bd841224fb97a458cb7435e`. Developer: Codex,
`gpt-6.1-sol`, xhigh, assigned mathematical development; runtime effort is not
independently exposed. No Git, shared-registry or handoff authority.

## Gate and scope

**Gate status: incomplete when G0 stopped the campaign.** Registry headings
and aliases were scanned through the complete `state/IDEAS.md`; bounded
summary/disposition views covered every campaign, but some combined tool
outputs were truncated, so complete summary-row coverage is not claimed.
Every named obstruction table was read, including the historical bivariate,
MZ, lattice, programme and later addenda. Shortlist:
IDEA-127/130/134/140, IDEA-147/148/150/151, IDEA-246–267. The canonical drift
candidate files were inspected, with complete central L3/L4 entries
IDEA-246–253 and IDEA-256; some combined views of neighboring entries were
truncated and must be repeated before the gate can close. In particular
IDEA-251 is already the normalized inverse criterion,
IDEA-252 rejects omitting the local pivot ratio, IDEA-253 is only a trivial
pathwise-quantifier rejection, and IDEA-254/PD-N062 does not forbid O(u)
stability. IDEA-250 already contains coherent and multinode scalar witnesses.

Search scope: `state/IDEAS.md`, bivariate-Lanczos theory and negative results,
the prior drift topic (including its reports, audit/response findings),
`literature/INDEX.md` and relevant literature records. Mechanism terms and
synonyms: `selection`, `staircase`, `adaptive`, `pivot`, `normal quotient`,
`surrogate`, `inverse`, `finite-u`, `remainder`, `nonlinear`, `radius`,
`majorant`, `row bound`, `Perron`, `Collatz`, `scalar CGS2`, `multinode`,
`coherent`, `spectral` and `Frobenius`.

Closest sources read fully: PD-T142/143 and PD-T054. PD-T138/141's model,
statements and proofs, the scalar producer and exact recurrence code were
read; PD-T136/137/139/140 and PD-N013/015/062 were inspected through linked
records/summaries and still require full-source completion. Literature INDEX
metadata and relevant full rows were consulted before comparisons:
LIT-241–243 already reports triangular-substitution error bounds and variable
selection (Barrio–Peña–Sauer), LIT-280–284 records the V+A exact-span versus
orthogonality distinction, and LIT-114/255 concerns one-operator Krylov
conditioning. These are repository reading records, not newly read external
fulltexts. No new literature/priority claim, no assertion of an exhaustive
historical search, and no PDF acquisition.

Applicable obstructions: (C) implies acyclicity, not small inverse scores;
near-breakdown ratios must remain explicit; arbitrary Hres families have no
uniform second-order constant; pivot switching is outside PD-T143's frozen
selection theorem; zero errors rule out pathwise positive lower bounds;
full reorthogonalization does not imply exact spans; aggregate and scalar
source norms differ; subset upper bounds do not bound the full scalar graph;
an endpoint ratio below 100 cannot kill the unknown true ratio. Finite-u
aggregate guarantees do not establish actual IEEE error realizability.

## IDEA?lanczos-frontier-codex-L3a — Explicit-radius recurrence majorant

Aliases: nonasymptotic inverse-score transfer; quantitative pivot continuation.

- Question / scope: give the normalized inverse score a finite-u radius and
  an explicit quadratic remainder for aggregate residuals under exact full
  projection, at every fixed unisolvent degree.
- Mechanism and hypotheses: bound basis, projection, pivot and recurrence
  coefficient changes recursively from exact data; apply a Neumann inverse
  estimate and PD-T142. Local sources obey a stated finite-u norm bound,
  rather than only their derivative satisfying Hres.
- Closest entries (reading coverage qualified above): IDEA-251/252 and
  PD-T142/143; PD-T046's explicit
  non-breakdown factor; PD-N062 fixed-degree O(u) obstruction.
- Separation criterion: all constants and a positive radius depend only on
  represented exact data and local budgets, uniformly for nonsmooth and
  u-dependent admissible source choices. An unspecified compactness radius,
  a family-dependent C² norm, or a bound assuming coefficient closeness
  without deriving it erases the distinction.
- Literature baseline/limits: standard projection and inverse perturbation
  estimates; no claim that these ingredients are historically new.
- Obstructions escaped: strengthen Hres to a finite-u source inequality,
  retaining chi and positive pivots. Do not claim polynomial-in-degree scores.
- Gate verdict: variant with a quantitative uniformity distinction.
- Cheapest decisive test: prove a closed induction controlling pivot changes,
  then check every denominator and the u² coefficient symbolically.
- Pretest kill: a circular nonbreakdown hypothesis or dependence on unknown
  perturbed coefficients kills this exact-data certificate.
- Discriminability: the induction either supplies all radii explicitly or it
  does not; a numerical small-error example cannot replace this obligation.
- Actual result: analytic development, no experimental dependency; see L3.md.
- Disposition: deferred by G0 FAIL; unchecked candidate formulas retained.
- Canonical result: `PD-T?lanczos-frontier-codex-L3a`.

## IDEA?lanczos-frontier-codex-L3b — Finite decision-tree adaptive bound

Aliases: switching-safe aggregate selection; adaptive pivot without tie gap.

- Question / scope: extend a finite-u guarantee to adaptive choices, including
  exact ties, without pretending a perturbed run follows the frozen exact rule.
- Mechanism: enumerate the finite set of realized admissible selection
  sequences and take their explicit worst-case radius/bound. A pathwise run
  is one member of that set, even when it changes branch discontinuously.
- Closest entries: IDEA-151, IDEA-251 and PD-T143's explicit exclusion of
  perturbed pivot switching; PD-T054 excludes non-(C) choices only from its
  implicit-section conclusion, not from the span certificate.
- Separation criterion: quantifies over the actual adaptive policy's branches
  without a tie-margin hypothesis. Freezing choices at zero would kill it.
- Baseline/limits: elementary finite-union argument, potentially exponential
  cost; no efficient online or polynomial growth claim.
- Gate verdict: quantitative continuation of L3a; retain as a corollary, not a
  separate historical mechanism claim.
- Cheapest test/kill: check that each realized path has the same declared
  aggregate implementation and belongs to the enumerated set. An unenumerated
  parent operation or extra information injection lies outside the result.
- Actual result: analytic development only; see L3.md.
- Disposition: deferred by G0 FAIL; unchecked finite-union argument retained.

## IDEA?lanczos-frontier-codex-L4a — Positive-envelope spectral upper

Aliases: Perron scalar-graph upper; weighted row/Collatz certificate.

- Question / scope: settle the rotQ24 degree-12 factor-ten conjunct in the
  full frozen scalar-CGS2 graph, retaining the original INCONCLUSIVE test.
- Mechanism: keep every scalar source in rho, form the entrywise response
  envelope S_ki=sum_h |g_kh(z_i)|rho_hi and bound its squared spectral norm
  by max_i (Cv)_i/v_i, C_ij=sum_k S_ki S_kj/d_k, for rational v_i>0.
- Closest entries (reading coverage qualified above): IDEA-246/250,
  PD-T138/141, and PD-T139's aggregate
  row-bound improvement. The latter has a different input norm and cannot be
  substituted for this full scalar upper.
- Separation criterion: use the full scalar envelope with a rigorous spectral
  upper smaller than its Frobenius trace. A subset rho or a heuristic largest
  eigenvalue would erase the required distinction.
- Literature baseline/limits: ordinary nonnegative-matrix row scaling; no
  historical novelty claim.
- Obstructions: formal errors need not be IEEE attainable; preserving full
  rho avoids the subset-upper error. Failure of this upper to pass is only
  an inconclusive certificate, never a kill of the true factor-ten ratio.
- Verdict: quantitative certificate variant of IDEA-250.
- Cheapest test (preregistered before execution): v=1 exact row bound; then
  up to eight positive rational vectors proposed by power iteration or a
  shifted/scaled variant, followed by exact inequality checks.
- Pass: any rigorously checked U with 100U<G_R, using the existing exact BJ
  multinode gain G_R. Kill of the true comparison requires separate upper-BJ
  and lower-comparator evidence; a failed envelope is not such evidence.
- Discriminability: exact rational positive-vector inequalities certify a
  true upper for all frozen graph errors; their strict comparison with G_R
  decides the positive outcome without computing K exactly.
- Actual runs: none; G0 was pending at registration and subsequently failed.
- Disposition: deferred by G0 FAIL; no mathematical/certified result claimed.
- Canonical result: reserved provisional `PD-T?lanczos-frontier-codex-L4a`
  only if its exact checks and independent reproduction are completed.

## IDEA?lanczos-frontier-codex-L4b — Stronger BJ witness

Aliases: multiple-output scalar witness; improve beyond greedy target 90.

- Scope/mechanism: retain the full output matrix of the existing BJ node-sign
  witness; its spectral norm is at least the old target-column norm. If needed,
  search multiple output targets/sign patterns without altering the full graph.
- Closest: IDEA-250 already has target signs, greedy nodes and coherent-node
  full-output witnesses, PD-T138/141. This is a quantitative variant.
- Separation/kill: require a new exact attained gain, checked by direct
  projection. Merely reusing the old G_R or its float estimate is equivalent.
- Obstructions/limits: formal realizability only; failed lower searches cannot
  upper-bound K_BJ and cannot kill factor ten.
- Cheapest test: after L4a, inspect whether a new lower is necessary.
- Actual result/disposition: deferred until L4a's outcome; not run.

## Stop receipt — 2026-11-05

The orchestrator reported independent G0 FAIL: the prior E6 T24 n12 receipt
differs with the same identified inputs/code; BLAS sensitivity is demonstrated
but the historical discrepancy remains unexplained. The handoff's stop rule
therefore applies. No new experiment was executed by this worker. No theorem,
finite certified inequality or completed novelty gate is claimed. L3a/L3b are
unchecked candidate reductions; L4a/L4b are unexecuted preregistrations. All
development is deferred pending an explicit resolved G0 verdict and resumption
instruction. Required source reading also remains unfinished (including the
unmerged PR21 P3 comparison/addenda); no historical priority conclusion is
drawn from the preparation above.
