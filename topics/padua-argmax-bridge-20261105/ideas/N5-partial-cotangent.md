# IDEA?argmax-bridge-codex-N5-01 — uniform truncated cotangent blocks

Aliases: two-pole extraction; corrected-midpoint partial sums;
arbitrary-offset cotangent tail; fourth-order sign-block interface.

- Question / scope: approximate every contiguous progression
  x_i=(i+delta)pi/n in (0,pi), n>=2, independently of its distance from
  either endpoint pole, with explicit error <=7 q(pi/n)^4/7200 for q samples.
- Mechanism and hypotheses: retain 1/x-1/(pi-x) exactly as shifted harmonic
  sums. Integrate the smooth residual over centered cells and subtract
  its endpoint derivative correction. All arithmetic in the theorem is real.
- Closest entries read in full: IDEA329/T226, IDEA358/T269–270,
  IDEA455/T365; context IDEA318/324/339 and their exact E-C/E-P scopes.
- Separation criterion: arbitrary block/offset, both poles removed, explicit
  fourth-order bound with a constant independent of pole distances.
  Failure of uniformity or a weighted error no better than the uncorrected
  second-order formula kills the proposed quantitative advantage.
- Literature baseline: `../literature-N5.md`; no external proof transfer
  or historical priority claim. This is a known quadrature mechanism
  applied to the precisely missing partial-sum domain.
- Applicable obstructions escaped: no coset-maximal primitive assumption,
  no equal-phase translation, no termwise cardinal sign box, and no
  dropping endpoint collision terms. The block lemma itself excludes
  a sample exactly at a cotangent pole; product continuation belongs to
  the T226/N1 assembly, which must not substitute 0*infinity.
- Novelty gate verdict: variant with difference; gate in
  `../novelty-gate-N5.md`.
- Cheapest decisive test: prove a uniform bound on the fourth derivative
  of cot x-1/x+1/(pi-x) on [-pi/4,5pi/4], and integrate the one-cell
  corrected-midpoint kernel. Then high-precision arbitrary-block checks.
- Kill criterion written before numerical tests: a counterexample outside
  the stated analytic error, or an unremoved endpoint singularity, stops
  this formula. Finite agreement is not proof.
- Test discriminability: the derivative/kernel proof decides all offsets
  and degrees; numerical checks can expose implementation/sign errors.
- Actual result: analytic all-offset theorem completed in
  `../theory/N5-partial-cotangent.md`, with the exact corrected-midpoint
  kernel and uniform fourth-derivative constant. All 130 developer
  high-precision checks lie within the bound; largest error/bound 0.11038.
  Those checks are MEASURED verification only; receipt
  `../evidence/n5-partial-cotangent.json` pins the executed sources.
- Disposition: retained PROVED supporting 1D theorem, independent review
  and later Claude audit pending. All-degree E-C remains OPEN.
- Canonical provisional theory: PD-T?argmax-bridge-codex-N5-01.
- History: 2026-11-05. N1 suggested the second-order two-pole formula;
  N5 develops the fourth-order correction and standalone proof. N1 owns
  T226 absolute-row assembly/collisions/transition, with disjoint files.

## Other considered formulations retained

1. **Direct classical local-maxima transfer**: deferred before development.
   Sources are unread here; the actual Padua edge must first be represented
   in the same norm/node family. No theorem or PD-N is inferred from this
   access/representation gap. Resume with fulltext and a matched reduction.
2. **E-C itself, renamed as cotangent ordering**: equivalent continuation
   of IDEA324/339, not a new candidate. No new scan; resume only when the
   independently optimized phases can be controlled analytically.
3. **Uncorrected two-pole midpoint formula**: retained as a second-order
   subordinate variant, supplied by N1. Its O(n^-2) weighted error can be
   sharpened by the endpoint derivative correction in the active candidate.
   No rejected theorem or separate negative result is created.
4. **Extract K nearest terms and bound the rest by monotone integrals**:
   abandoned as the present implementation choice, not refuted. It would
   leave an avoidable K-dependent accuracy/cost tradeoff; the smooth
   two-pole formula gives a fixed-order uniform remainder instead.
