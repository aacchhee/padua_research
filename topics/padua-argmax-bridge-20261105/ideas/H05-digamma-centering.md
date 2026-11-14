# IDEA?argmax-bridge-codex-H05-centering — Uniform centering of the exact harmonic row

Aliases: H05 digamma centering; first-order shifted harmonic row;
endpoint-uniform trigamma correction.

- Question / scope: for every integer m>=2 and 1<=s<=m-1, r=m-s,
  q=s/(2m), c=1-1/(2m), center H01's exact harmonic difference
  `D_s=psi(m-cs)-psi(q)-psi(m-q)+psi(cs)` with an O(m^-2)
  error uniform over the WHOLE index range. The intended main term is
  `psi(r+1/2)+psi(s)-psi(q)-psi(m)` and the intended correction is
  `-[r*psi'(r+1/2)+s*psi'(s)-s*psi'(m)]/(2m)`.
- Mechanism and hypotheses: define psi by a locally convergent harmonic
  series, prove its derivative series directly, and apply an integral
  Taylor remainder with the actual positive shifted arguments. Keep
  psi(q) exact; q can approach zero. Then sum against the actual positive
  weight `w_s=tan(pi*s/(2m))` with prefactor `4/(pi*m)`.
- Closest registry entries read in full: PD-T269/270/271; current F03
  idea/theory and H01 idea/attempt; the completed parent predecessor gate
  `../campaign-H-gate.md` including its F03/IDEA329 refinement was read.
  Parent's H01 exact D_s identity is an assigned input; H05 does not
  replace a partial cotangent row by its signed complete row.
- Separation criterion vs closest entry: an explicit degree-uniform
  O(m^-2) row error yielding O(log(m)/m^2) after the actual singular
  outer weights, including s=1 and s=m-1. Merely renaming F03's
  harmonic difference or proving a fixed-index Taylor expansion erases
  the distinction.
- Literature baseline and search limitations: the completed bounded
  parent gate supplies the existing IDEA287/288/358 continuation and
  predecessor obstruction coverage. Supplemental searches covered
  digamma, trigamma, centering/centered and harmonic difference in the
  current topic, IDEAS and INDEX. No external theorem, PDF, historical
  priority or exhaustive novelty claim is used.
- Applicable obstructions and exact hypotheses broken: F03 leaves a
  separate smooth residual, which H05 does not estimate; D03's exact
  n+1 normalization still has to be compensated by the whole assembly.
  Unlike IDEA289's nonuniform adjacent-gap estimate, this proposal must
  bound the actual derivative over each whole shifted interval.
- Novelty gate verdict: quantitative VARIANT/supporting refinement of
  existing IDEA287/288/358 and F03/H01, with no new mechanism claim.
- Cheapest decisive test: before deriving a summed asymptotic, bound
  each second-order remainder at s=1, r=1 and throughout the interval.
  In particular verify that the factors s^2 and r^2 cancel the local
  inverse-square derivative bounds. Check the sign of the m-q term.
- Kill criterion written before testing: if either endpoint remainder
  grows faster than C/m^2 for a fixed universal C, or the weighted sum
  is larger than C*(1+log(m))/m^2, retain the scoped failure and do not
  hand H01 a uniform lemma. A failure does not refute PD-T098.
- Test discriminability: the actual second derivative series and shifted
  intervals can establish or disprove index-uniform control on paper;
  fixed-index expansions and finite comparisons cannot do so.
- Actual test results: prospective registration preceded all derivation.
  The endpoint kill test PASSED: the local derivative series gives
  `D_s=M_s-J_s/(2m)-rho_s`, with
  `0<rho_s<=257/(216m^2)<5/(4m^2)` for every s,r>=1. The actual
  normalized weighted error is one-sided and at most
  `257*H_(m-1)/(27*pi^2*m^2)`. Exact J_s is positive and has a finite
  reciprocal-square tail form. Written proof is in the theory record;
  no scientific execution supplied or required.
- Disposition: RETAINED, registered centering support PROVED by the
  developer. The full corner target remains OPEN and no independent
  acceptance, novelty or whole-assembly claim is supplied.
- Canonical theory: `../theory/H05-digamma-centering.md`; work history
  `../attempts/H05-digamma-centering.md`. No global ID assigned.
- History: 2026-11-07; rules/input
  `ad257038cdff1d66f6e9c03d7ed43405c76cf6b0`; parent-released H05
  PAPER ONLY mathematical support. Requested/inherited model and effort
  are not independently exposed in this worker. Own only these three
  files; no Git/shared-state mutation, scientific executable/numerical
  job, extra round or subagent.
