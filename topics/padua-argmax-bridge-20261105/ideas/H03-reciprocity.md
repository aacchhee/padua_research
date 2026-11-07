# IDEA?argmax-bridge-codex-H03 — Consecutive-mesh Cauchy reciprocity

Aliases: H03; global checkerboard resummation; numerator reciprocity;
consecutive Chebyshev meshes; triangular cotangent mass.

- Question / scope: prove the original sharp corner expansion for every
  integer n tending to infinity, both parities, with N=n+1/2 and
  Lambda_c=A_N^2+kappa-1/N+O(log N/N^2). Equivalently, with a=2/pi,
  Delta_n=kappa+(A_n^2+a*A_n-2)/(n+1)+O(log n/n^2).
- Mechanism and hypotheses: use only the endpoint-complete PD-T159
  positive Cauchy formula and elementary exact algebra on the two
  consecutive meshes n,n+1. Test a global transpose/numerator reciprocity
  and triangular reindexing before any local Taylor expansion. Preserve
  checkerboard parity, actual half weights, and the exceptional1/(n+1).
  No exact one-index evaluator, global cancellation or uniform remainder
  is assumed.
- Closest registry entries read in full: IDEA-286/287/288 and their T-A2
  attempt/PD-T159; IDEA-358/PD-T269--271; IDEA-329 original/final records
  and PD-T226; complete F03-origin-sign idea/attempt/theory; C07's finite
  nonnegative deformation. The shared completed gate is
  ../campaign-H-gate.md. Root released PAPER work only after its completion.
- Separation criterion: an exact global relation that removes or sharply
  controls the actual triangular partial-row mass left by F03, and retains
  the finite normalization correction at O(log n/n^2). A transpose of the
  old double sum, an incomplete cotangent product under a new name, or an
  uncontrolled remainder of order log^2 n/n erases this distinction.
- Literature baseline and limits: existing-route quantitative variant;
  no external theorem, PDF, historical priority or exhaustive novelty
  claim. Root's full registry gate and the scoped predecessor reads above
  cover the current mechanism.
- Applicable obstructions: F03/IDEA-329 show that substituting signed full
  rows for absolute partial rows deletes order log^2 n mass. That
  substitution is excluded. PD-T269's fixed-offset convergence does not
  justify a uniform first correction. The upper adjacent endpoint has
  mesh separation O(n^-2), so no uniform local Taylor estimate is assumed.
- Novelty gate verdict: quantitative variant of IDEA-287/288/358, with
  global reciprocity as the proposed new proof step; not a new mechanism
  or a claim that an existing deferred route was refuted.
- Cheapest decisive test: write the exact difference between the two
  transposed Cauchy numerators on the whole endpoint-weighted odd board,
  and determine whether its ordering sum and remaining symmetric sum
  genuinely simplify. Then test triangular cotangent reindexing against
  the exact F03 positive partial-row formula, with all endpoint terms.
- Kill criterion BEFORE testing: stop a proposed reciprocity collapse if
  it only reproduces the old two-index partial sum or replaces it by a
  signed full row. Retain a precise residual if no sharp uniform signed
  bound follows. Failure of this route does not refute PD-T098 or all
  possible resummations. Formal coefficients do not pass the target.
- Test discriminability: an algebraic correction/count can be checked
  without numerics; a surviving triangular mass is displayed explicitly.
  Completion additionally requires its summed remainder at the stated
  scale and the exact denominator n+1.
- Actual results: exact transpose count C=-(2n-1)/4 gives
  Lambda_c=(2/[n(n+1)])sum' epsilon eta(2+x+y)/|x-y|+1/[2n(n+1)].
  CRT converts this to an equivalent2n(n+1)-1 term absolute correlation.
  Removing its absolute sine factor gives exactly(2n+1)/(n+1), deleting
  order log^2 n mass. Thus ordinary signed reciprocity repeats the OLD
  IDEA-329/F03 collapse obstruction; it is not a new escape. Proof and
  exact unresolved residual: ../theory/H03-reciprocity.md.
- Disposition: DEFERRED after exact screen; sharp target OPEN, supporting
  finite identity PROVED in the owned theory, independent review separate.
  No impossibility theorem or faster evaluator is asserted. Resume only
  with an actual sharp bound for the surviving absolute residual.
  No executable/import, numeric,
  native, quadrature, compiler, source/control or degree job authorized.
- Canonical theory: ../theory/H03-reciprocity.md if substantive.
- History: 2026-11-07; Codex requested/API gpt-6.1-sol xhigh; rules/input
  2c69ba538473b8fdd9147635256289f74e75ccbb. Root alone owns Git/shared
  records. H01 handles rowwise/fixed-offset algebra, H02 signed endpoint
  analysis, H03 global reciprocity/reindexing. No new round or delegation.
