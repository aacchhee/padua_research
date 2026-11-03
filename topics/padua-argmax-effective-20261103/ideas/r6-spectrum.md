# IDEA?argmax-effective-r6-01 — Complete positive corner-active spectrum

Aliases: all-positive inward cosine coefficients; spectral corner comparison.

- Question / scope: can every cosine coefficient of the canonical inward
  corner-active signed polynomial be made nonnegative by its existing signs?
- Mechanism and hypotheses: PD-T227 signs, including inward signs of the zero
  row; compare cosine modes directly to their values at the corner.
- Closest registry entries (read in full): IDEA-330/331, IDEA-206 and the
  quantitative corner predecessors recorded in the R6 attempt.
- Separation criterion vs closest entry: positivity of the transformed
  signed-polynomial coefficients would replace nodewise absolute Hessian
  estimates. One exact negative nonconstant coefficient kills this form.
- Literature baseline and search limitations: complete registry gate in
  attempts/r6-corner.md; INDEX coverage-qualified; no external theorem or
  historical novelty claim.
- Applicable obstructions and exact hypotheses broken: primitive cusp is
  irrelevant to the signed polynomial, but cardinal sign changes remain.
- Novelty gate verdict: variant with difference in the coefficient domain.
- Cheapest decisive test: small-degree masked cosine transform, followed
  by exact verification of any negative entry.
- Kill criterion written before testing: first exact negative coefficient
  rejects complete positivity; finite positives cannot prove it.
- Test discriminability: an exact negative answers the universal
  coefficient claim while saying nothing against grouped positivity.
- Actual test results and committed evidence: n=2 C_00=-1/6; even ignoring
  constants, n=3 C_01=(1-2sqrt(2))/6<0. Exact formula in the negative record.
- Disposition and precise rejected scope: **REJECTED: refuted**, complete
  positivity of the specified polynomial, not local or global argmax.
- Disposition reason: refuted by an exact degree-three nonconstant mode.
- Canonical theory / negative-result ID: PD-N?argmax-effective-codex-06a,
  theory/argmax-effective-codex-06-negative-spectrum.md.
- Topic / audit / history: pretest scope in the R6 attempt; 2026-11-03,
  Codex gpt-6-astra ultra; [supplementary independent review](../independent-math-checks-01.md) accepted; Claude audit pending.

# IDEA?argmax-effective-r6-02 — Positive mixed spectrum and exact edge symmetries

Aliases: diagonal-sign DCT; positive x-degree coefficients; row/column grouping.

- Question / scope: identify every coefficient exactly, retaining negative
  x-degree-zero modes and proving positivity after row/column grouping.
- Mechanism and hypotheses: finite parity-row sine sums, the corrected
  top mode, exact zero-row correction and polynomial edge interpolation.
- Closest registry entries (read in full): IDEA-330/331 and r6-01 above.
- Separation criterion vs closest entry: explicit exact formulas plus
  positivity of all a>0 modes and all row/column sums. A negative such
  coefficient or sum would kill this specified variant.
- Literature baseline and search limitations: the R6 gate; this is a
  quantitative variant with no transferred one-dimensional technique.
- Applicable obstructions and exact hypotheses broken: r6-01 forbids
  claiming every mode positive; here a=0 is retained explicitly. Primitive
  positivity and a global fixed-sign envelope are not assumed.
- Novelty gate verdict: variant with difference, within documented search.
- Cheapest decisive test: evaluate the staircase-sign DCT analytically;
  small-degree agreement tests only diagnose normalization mistakes.
- Kill criterion written before testing: this narrower variant was formed
  after the initial diagnostic, so no retrospective preregistration is
  claimed. The analytic separation test is strict positivity of its formulas.
- Test discriminability: a complete formula is an all-n statement; sampled
  positivity alone would leave the candidate OPEN.
- Actual test results and committed evidence: exact formulas and row
  symmetry proved; C_(n-b),b>=2/(n+1), C_0n>=8/15, and Lambda_c>=2.
  Float diagnostic agrees with the full coefficient kernel on its stated
  finite range but is not a proof premise.
- Disposition and precise rejected scope: retained.
- Disposition reason: exact finite-sum proof survives the narrower criterion.
- Canonical theory / negative-result ID: PD-T?argmax-effective-codex-06a,
  theory/argmax-effective-codex-06-corner-active-spectrum.md.
- Topic / audit / history: 2026-11-03, Codex gpt-6-astra ultra; distinct
  independent reconstruction completed in conversation, durable receipt
  owned by the independent worker; Claude audit remains pending.
