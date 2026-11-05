<a id="idea-347"></a>

# IDEA-347 — Uniform per-cardinal affine sign preservation

Provisional alias: `IDEA?argmax-effective-r6-03`.

Aliases: termwise O(n-squared) gradient/value bound; fixed scaled sign radius.

- Question / scope: can the affine corner model of every nonzero cardinal
  preserve its sign throughout a physical box of radius kappa/n^2, with
  fixed kappa>0 for all degrees?
- Mechanism and hypotheses: bound each absolute physical gradient/value
  ratio by M n^2, then preserve all affine corner signs before a Taylor bound.
- Closest registry entries (read in full): IDEA-330 and PD-T227's aggregate
  alternative; IDEA-331 preserves the actual reflected absolute values.
- Separation criterion vs closest entry: an all-n termwise ratio bound
  would remove the weighted-energy premise. An explicit ratio growing
  faster than n^2 kills that sufficient step.
- Literature baseline and search limitations: R6 documented registry gate;
  no external source transfer or historical priority claim.
- Applicable obstructions and exact hypotheses broken: individual ratios
  were already flagged as potentially unbounded; this round makes the
  obstruction explicit for one admissible family, not a new broad ban.
- Novelty gate verdict: quantitative variant with a concrete obstruction.
- Cheapest decisive test: asymptotically expand the exact PD-T227 ratio
  at fixed small source indices.
- Kill criterion written before testing: any growing normalized ratio
  kills uniform ratio control; negative growth is needed to obstruct
  affine sign preservation itself.
- Test discriminability: the written limit proves failure for all large
  degrees; finite measured growth would be only a lead.
- Actual test results and committed evidence: at index(3,1), q_n/n^3
  tends to -5/(2pi^2). Hence every fixed kappa/n^2 affine sign box fails
  eventually; the single-index maximum radius is asymptotic to
  (2pi^2/5)n^-3.
- Disposition and precise rejected scope: **REJECTED: failed**, only the
  stated affine sign-preservation/termwise ratio mechanism.
- Disposition reason: proved superquadratic negative gradient/value ratio.
  True-cardinal sign stability, aggregate control and argmax are not refuted.
- Canonical theory / negative-result ID: PD-N085,
  theory/argmax-effective-codex-06-affine-sign-obstruction.md.
- Topic / audit / history: registered before first test in the R6 attempt;
  2026-11-03, Codex gpt-6-astra ultra; [supplementary independent review](../independent-math-checks-01.md) accepted; Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the stated scope.

<a id="idea-348"></a>

# IDEA-348 — Exact spectral proof of all-degree normalized slopes

Provisional alias: `IDEA?argmax-effective-r6-04`.

Aliases: corner derivative moment bound; edge-mode pairing; explicit shrinking radius.

- Question / scope: establish the old all-degree slope premise
  A_n,B_n<=-n^2 Lambda_c/8 with explicit hypotheses, then a valid local radius.
- Mechanism and hypotheses: use r6-02's positive row/column sums and
  exact edge mode pairing; retain the even-n y-edge endpoint defect.
- Closest registry entries (read in full): IDEA-330/331, PD-T227, and r6-02.
- Separation criterion vs closest entry: prove the all-n normalized slopes,
  rather than finite negativity or a non-effective eventual bound. A
  missing even-n endpoint correction would invalidate the result.
- Literature baseline and search limitations: R6 gate; no 1-D source
  theorem imported, only finite geometric series and polynomial roots.
- Applicable obstructions and exact hypotheses broken: no full spectral
  positivity, raw-profile convergence or termwise n^-2 sign radius is
  used. The slope proof alone does not establish weighted energy.
- Novelty gate verdict: quantitative variant closing one old explicit
  obligation, not a new historical mechanism claim.
- Cheapest decisive test: exact edge symmetries and moments of positive
  coefficient rows/columns; then check every radius constant algebraically.
- Kill criterion written before testing: initial aggregate-slope candidate
  appears in the R6 pretest note. The later spectrum is its discovered
  implementation; no backdated separate numerical preregistration.
- Test discriminability: complete inequalities decide all n>=2; a finite
  screen of slopes or energies would not establish this result.
- Actual test results and committed evidence: A_n,B_n<=-n^2 Lambda_c/8
  proved for all n>=2, with sharper individual inequalities. Also
  lambda(c+h)<=Lambda_c-n^2(h_x+h_y)/6 for
  0<h_x+h_y<=1/(2[n(n+1)]^3).
- Disposition and precise rejected scope: retained all-n theorem; desired
  fixed phase-zone comparison remains OPEN, not rejected.
- Disposition reason: slope premise is proved; the explicit radius has
  physical scale n^-6, insufficient to replace the fixed-phase bound.
- Canonical theory / negative-result ID: PD-T251,
  theory/argmax-effective-codex-06-uniform-slopes-local-radius.md.
- Topic / audit / history: 2026-11-03, Codex gpt-6-astra ultra; separate
  analytic reviewer has checked the proof; [durable independent receipt](../independent-math-checks-01.md)
  accepted and Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the stated scope.

## Final registration — 2026-11-05

Final IDs and preserved provisional aliases: [id-map](../final-id-map.json). Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the existing stated scopes; no claim, proof or epistemic status changes at registration.
