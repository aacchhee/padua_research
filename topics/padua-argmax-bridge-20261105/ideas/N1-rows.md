# IDEA?argmax-bridge-codex-N1-01 — Two-phase absolute-row quadrature assembly

Aliases: corrected cotangent row model; endpoint-row extraction;
moving sine-threshold sign arcs; full-diamond partial-row remainder.
Prior provisional alias: IDEA?argmax-bridge-N1-01.

- Question / scope: approximate the exact primitive S_n over the entire
  closed phase diamond with an explicit uniform remainder, retaining all
  absolute-value and collision terms.
- Mechanism: N5's pole-subtracted partial cotangent formula applied to
  exact negative-index sets in each row; retain the two closest endpoint
  rows exactly. n>=2; the exceptional (n,0) mode is retained throughout.
- Closest full entries: IDEA-329/T226, IDEA-337, IDEA-455/T365,
  IDEA-459, and IDEA-327/T217/T221.
- Separation criterion: a uniform O((1+log n)/n^4) approximation error for
  absolute two-phase rows, beyond exact signed sums and axis-only identities.
  An omitted transition or collision, endpoint divergence or failed
  remainder check erases this distinction.
- Literature baseline / limitations: [gate](../novelty-gate-N1.md);
  internal continuation only, no external theorem transfer or priority claim.
- Applicable obstructions: T226's unresolved absolute partial sums are the
  target; N079 forbids discarding the primitive cusp, N132 forbids a leading
  factor only, N086 forbids assuming every coarse diamond has fixed signs.
- Novelty verdict: quantitative variant with the specific error obligation.
- Cheapest test / prewritten kill: compare the full row formula with the
  corrected finite polynomial at generic phases, numerator zeros and exact
  collisions before any degree fit. A discrepancy beyond numerical error
  triggers algebraic review, not an automatic theorem refutation.
- Test discriminability: the exact proof gives all-n/all-phase coverage;
  finite high-precision comparisons check implementation only.
- Actual results: model written in N1-row-model.md before computation;
  N5 then supplied its proved partial-sum lemma. The complete analytic
  assembly gives the stated O((1+log n)/n^4) error. A 125-case developer
  mpmath check had maximum error/bound 0.005278 and no sign mismatches;
  it is MEASURED validation, not the proof. See attempts/N1.md and receipt.
- Disposition: active supporting reduction. The compact all-degree N1
  comparison remains OPEN; the outer sum still has O(n) rows.
- Canonical theory: PD-T?argmax-bridge-codex-N1-01 (row model), developer PROVED
  after the separately owned N5 lemma was completed and read. Initial
  CONDITIONAL status is retained in theory history; independent review pending.

## Retained variants

1. **N1-01a, all rows treated separately with coefficient absolute values:**
   abandoned as an endpoint-uniform error mechanism. At beta tending to
   zero the r=0 cot(v/2) coefficient diverges although the corrected kernel
   is finite. The two singular cotangent channels must be combined or this
   row extracted. This concerns the proposed error estimate, not S_n.
2. **N1-01b, uncorrected midpoint quadrature:** superseded by N5's corrected
   midpoint form. The initial interface had per-block error <=5 q h^2/72,
   using |w''|<5/3; it gives only O(log n/n^2) after row assembly. No run or
   negative theorem is claimed for this weaker valid alternative.
3. **N1-01c, axis-only negative-row comparison:** deferred after the N5
   interface made a full-diamond assembly possible. No claim that each
   interior row decreases from alpha=0 is made or tested. Resume only if
   it supplies a sharper final inequality rather than an identity.
4. **N1-01d, compactification of the remaining outer row sum:** deferred
   until the assembly is checked and its moving endpoints are explicitly
   controlled. Replacing n by exp(L) in a finite sum is not the required
   finite compact-parameter certificate.
5. **N1-01e, full two-phase signed/negative row identity alone:** equivalent
   to the concurrently developed N2 row decomposition. N2 owns that result;
   N1's derivation is verification material only. No separate result ID or
   negative entry is allocated for equivalence.

History: 2026-11-05, Codex, requested gpt-6-astra ultra; no Git operations.
