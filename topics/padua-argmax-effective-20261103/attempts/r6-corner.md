# R6 — bounded effective local corner round

Rules/input: 8a1f394739293953e1566fd24a0a193cc78ff26f. Base: 440d107.
2026-11-03, Codex mathematical developer, gpt-6-astra ultra, explicitly
assigned by handoff02 and the orchestrator. No Git or shared registries.

## Gate and pre-test scope

Read AGENTS.md, WORKFLOW, CODEX, BRIEF and handoff02. Scanned complete
state/IDEAS.md headings, identifiers, aliases and mechanism summaries,
including every obstruction and disposition table. Full shortlist:
IDEA-206, 305, 326–331, 333 and their linked local-corner records, especially
PD-T227/228/229; IDEA-316/317 retain the primitive cusp and raw-profile
failures. Search terms across state, literature index, topic ideas,
attempts and theory: reflection, average, corner, slope, energy, sign
stability, endpoint, Taylor, Hessian, row resummation. This is a quantitative
variant of IDEA-330/331, with no historical novelty claim and no transfer
of a one-dimensional literature theorem. The INDEX's source qualifications
remain; no PDF opened.

The intended distinction is a computable small-constant local bound using
exact corner sign information, instead of the regular-kernel absolute
Hessian constants in PD-T228. Candidate records precede the first test.

## Initial candidate tests

1. Fourier positivity of the corner-active signed polynomial, including
   the canonical inward signs at zero cardinals. Kill this sufficient
   mechanism at the first rigorously negative cosine coefficient; floating
   negatives are only leads. Distinguishes a signed-polynomial spectral
   estimate from PD-T228's nodewise absolute Hessian estimate.
2. Uniform per-cardinal scaled gradient/value bounds for nonzero corner
   cardinals. First inspect the explicit PD-T227 formulas for a family
   growing faster than n². Such a family kills a uniform termwise
   sign-stability radius, but not an aggregate energy or reflected bound.
3. Aggregate exact slopes with a remainder controlled by endpoint
   interpolation. This is a retained variant of IDEA-330; a useful new
   result must remove an old hypothesis or give a materially sharper
   explicit constant. Merely restating PD-T227 is not an outcome.

Status before tests: all candidates OPEN; bounded mathematics round only.

## Outcome of the bounded round

Two separate **PROVED development theorems** were obtained:

- [Exact corner-active spectrum](../theory/argmax-effective-codex-06-corner-active-spectrum.md),
  PD-T?argmax-effective-codex-06a. The masked cosine transform of the exact
  inward sign data has a closed elementary formula. Every coefficient of
  positive x degree is positive, while the x-degree-zero coefficients may
  be negative. Exact edge interpolation supplies positive row/column sums
  and the row reflection relations. In particular Lambda_c>=2 for all n>=2.
- [Uniform slopes and local radius](../theory/argmax-effective-codex-06-uniform-slopes-local-radius.md),
  PD-T?argmax-effective-codex-06b. For every n>=2,

      A_n,B_n <= -n^2 Lambda_c/8.

  Thus the normalized all-n slope premise left OPEN in PD-T227 is closed.
  The y proof retains the even-degree endpoint defect explicitly. Also,

      lambda(c+h)<=Lambda_c-n^2(h_x+h_y)/6
      for 0<h_x+h_y<=1/(2[n(n+1)]^3).

  This is an explicit all-n local radius, but its physical scale n^-6 is
  smaller than the n^-2 scale needed for a fixed phase zone. It is not an
  effective global threshold or a replacement for all of PD-T228.

Both initial failed mechanisms have separate scoped **PROVED** negative
records:

- [Complete spectral positivity](../theory/argmax-effective-codex-06-negative-spectrum.md),
  PD-N?argmax-effective-codex-06a: n=3 has the exact nonconstant coefficient
  C_01=(1-2sqrt(2))/6<0. Mixed/grouped positivity survives.
- [Affine sign obstruction](../theory/argmax-effective-codex-06-affine-sign-obstruction.md),
  PD-N?argmax-effective-codex-06b: for original index(3,1),
  (L_x/L)(c)/n^3 tends to -5/(2pi^2). Hence every fixed kappa/n^2
  termwise affine sign-preservation box fails eventually. This does not
  claim failure of true-cardinal sign stability or aggregate methods.

The complete candidate records are [r6-spectrum](../ideas/r6-spectrum.md)
and [r6-slopes-affine](../ideas/r6-slopes-affine.md). The mixed-spectrum
variant was formed after the first diagnostic; its later derivation is
not represented as a pre-registered new numerical test.

## Mathematical diagnostics actually run

Initial short NumPy scratch commands used the independent full corrected
coefficient matrix in `topics/padua-argmax-alln-20261101/code/maj.py`.
They inspected degrees 2,3,4,8,16,32,64,128, found negative coefficients
only on x degree zero, and identified index(3,1) as the most negative
tested normalized gradient/value ratio for n=16,32,64,128. The other
observed large ratio at index(0,2) was positive; it kills a uniform
absolute ratio bound but by itself does not obstruct affine sign
preservation. The negative record uses the signed index(3,1) family.

A compact reproducible version of the coefficient identity diagnostic is
[spectrum_diagnostic.py](../code/r6/spectrum_diagnostic.py). Executed:

    OPENBLAS_NUM_THREADS=1 python -B topics/padua-argmax-effective-20261103/code/r6/spectrum_diagnostic.py

It completed n=2,3,4,5,8,16,32,64, with maximum coefficient discrepancy
4.1522341120980855e-14. At n=2 it returned Lambda=3,
A/n^2=-0.583333333333 and B/n^2=-1.166666666667. At n=64 it returned
Lambda=13.973207805351, A/n^2=-4.872349992052 and
B/n^2=-5.023812267230. All are **MEASURED diagnostic values**, not proof
premises or a new measured universal claim. The analytic finite-sum
proofs are independent of this execution. No large artifact was produced.

## Independent checking and dispositions

The distinct parent-assigned independent agent reconstructed all four
analytic records. It checked the parity row sums, exceptional modes,
row symmetry, column positivity, exact even-degree y correction, uniform
normalized slopes, smaller-radius constants, and both negative proofs.
It found two wording issues: a removed abandoned estimate's n2 comparison
said `exceeding` instead of equality, and the angular-to-physical sentence
needed to differentiate `cos(a xi)` rather than literally `T_a(-cos xi)`.
Both were corrected; neither changed the theorem. Its final suggestion
added `for all sufficiently large n` to the affine-radius obstruction,
matching the proved asymptotic scope. The durable accepted receipt is
[independent-math-checks-01.md](../independent-math-checks-01.md), which
pins the mathematical proof versions. Later review-status wording changes
are administrative only. Required Claude audit remains pending.

## Precise remaining R6 obligation

The all-degree fixed phase-zone inequality for rho<=1/64 remains OPEN.
The normalized slope premise is now proved with constant 1/8. What is
missing is an aggregate sign-change/higher-variation estimate at physical
scale n^-2 (for example the weighted-energy hypothesis in PD-T227, with
a compatible effective global-norm bound). Merely sharpening a termwise
affine sign bound cannot supply that scale: the new obstruction forces
its single-index scale down to order n^-3. No counterexample to PD-T099
was found or certified, and no new global degree is certified by R6.

Recommendation: retain this completed bounded round, integrate the exact
all-n slope theorem, and resume the fixed-radius problem only with an
aggregate remainder mechanism. No additional R6 round was launched.
