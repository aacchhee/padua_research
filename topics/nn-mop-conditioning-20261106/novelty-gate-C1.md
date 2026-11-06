# C1 gate and retained candidates

Rules/input snapshot: `b4a04981d42c7cd872957facf5e3995e4096ca67`,
2026-11-06. Developer allocation: Codex, gpt-6.1-sol xhigh.
No Git or shared-record authority. Local IDs below are provisional.

## Search and scope

Scanned the complete 1112-line `state/IDEAS.md` inventory in consecutive
chunks, including aliases and campaign summary, obstruction and disposition
tables. Shortlisted index entries are IDEA-031/090/117, 376–379 and
530–555. Read the D1/D1-hard candidate records, PD-T432/437 and the older
`nn-mop-iep-20261103/candidates.md` and linked PD-T286/289 proof bodies.
The reading-timing qualification is recorded once in the [topic LOG](LOG.md);
this record does not claim full prospective completion of every linked read.
Searched gauge, diagonal scaling, normalization, fixed mass, log weights,
spacing, Jacobian, and conditioning across this inventory and predecessor
candidate/theory records. Read `literature/INDEX.md`'s relevant
LIT-347/348/562–568 rows. No new primary fulltext or literature claim is
made by C1; C4 owns the LIT-347 normalization fidelity gate.

Closest predecessors already provide the exact derivative, weighted row
norm, full-grid monic measurements, scalar marginal reconstruction, and
the terminal signed-weight witness. This direction specializes those
results to explicitly defined diagonal gauges and input constraints; no
new reconstruction algorithm or historical-priority claim is proposed.
Terminal d=0 is a boundary identity, positivity alone does not prove mixed
normality, and a measured finite rate does not prove an all-N rate.

2026-11-06 response clarification (audit-01 MINOR-10): the literature,
obstruction, kill-criterion timing and discriminability fields below were
completed retrospectively. Existing cheapest-test text is retained; this
repair supplies no evidence that a separate kill criterion was written
before testing and claims no preregistration.

## IDEA?nn-mop-cond-codex-C1-01 — diagonal invariant lower bound

Aliases: frozen gauge; differentiable gauge section; invariant b field;
terminal beta sensitivity; gauge-infimum screen.

- Question/scope: does diagonal rescaling remove the exponential local
  condition in the PD-T432 fieldwise norm?
- Mechanism/hypotheses: write all rescaled forward/backward coefficients;
  retain each diagonal b field with its own sup scale. Both fixed and
  differentiable input-dependent positive scales leave b unchanged.
- Closest entries: IDEA-530/534/535, PD-T432/437 and the explicit open
  normalization question in PD-T432.
- Separation: quantify over all diagonal gauges, rather than fix monicity.
  A gauge changing b, or a denominator mixing b with arbitrarily scaled
  offdiagonals, kills that stated conclusion.
- Literature baseline and search limitations: LIT-502/LIT-348 supplies
  norm-balancing in a residual-based updating method; it does not supply
  the PD-T432 fieldwise gauge-infimum statement. See the dated attribution
  addendum below for exact coverage; no exhaustive search is claimed.
- Applicable obstructions and exact hypotheses: fieldwise normalization
  prevents a common scalar shrink from changing a field-relative norm;
  dropping structural fields changes the metric. This candidate retains
  each b field and its own scale, so it does not escape that invariance.
  Positive weights alone supply no mixed normality; the family-specific
  normality assumptions/dependencies remain necessary.
- Kill criterion written before testing: timing is not established by
  this response. Retrospectively, any nonzero gauge contribution to a b
  derivative, or a changed b-field denominator, would kill the claimed
  invariant lower-bound transfer in this metric.
- Test discriminability: symbolic substitution can decide invariance for
  the declared gauge class before fitting rates. Finite samples can
  falsify an implementation but cannot certify the all-gauge quantifier;
  the written algebra supplies that step.
- Verdict: variant with explicit larger quantifier domain.
- Cheapest test/kill: symbolic coefficient substitution before computation;
  derive the terminal balanced-path bound directly from PD-T437.
- Actual outcome: written theorem in `theory/c1-gauge-invariants.md`;
  completed finite Hahn lower/upper measurements through one terminal row.
  Final C2 bounds subsequently yield the sharp Krawtchouk gauge-rate
  squeeze and the stronger all-N Hahn gauge-infimum liminf lower
  rho_H=12.1136005841..., with dependencies explicit in
  `theory/c1-gauge-sharp-rate.md` and the stronger dated corollary in
  `theory/c1-hahn-gauge-lower.md` (from `theory/c2-hahn-terminal-rate.md`).
  The original base-two Hahn bound remains a valid simpler bound;
  no matching full-map Hahn upper or sharp full-map equality is claimed.
- Disposition: retained; exact gauge infima and sharp Hahn all-N rates
  remain open. No literature novelty asserted.

## IDEA?nn-mop-cond-codex-C1-02 — scalar/control and constrained derivatives

Aliases: scalar Jacobi control; orthonormal square-root beta; natural
spacing; logarithmic weights; weighted median fixed-mass dual norm.

- Question/scope: measure scalar controls and declared input variants,
  N=4,...,64, for both exact rational benchmark marginals.
- Mechanism: orthogonality differentiates each scalar coefficient into
  one polynomial linear functional; its node/weight derivative is O(N).
  Fixed-mass weight-box support is a weighted-median minimization.
- Closest entries: IDEA-530/PD-T432 already states the derivative and mass
  null directions, while explicitly leaving constrained norms open.
- Separation: actual fixed-mass tangent support, and data-dependent
  orthonormal normalization, rather than a renamed monic row norm.
- Literature baseline and search limitations: Fischer 1998 (LIT-113,
  Lemmas 4–5; related LIT-112/365 and IDEA-087/088) is the scalar
  derivative baseline. The dated addendum below records the limited
  source checks; its polynomial-bound report is not transferred to the
  benchmark metric or inferred from these finite controls.
- Applicable obstructions and exact hypotheses: near-zero relative
  denominators can fabricate large conditions, and unconstrained row sums
  do not impose fixed mass. Exactly symmetric zero alpha fields therefore
  use scale one; the fixed-mass variant uses its separate tangent support.
  Slow finite fits cannot evade the need for an all-N upper proof.
- Kill criterion written before testing: prior written timing is not
  established here. The existing AD comparison is retained; retrospectively,
  a derivative discrepancy beyond the declared numerical agreement or
  failure to enforce the mass tangent would block that control screen.
- Test discriminability: a separately differentiated recurrence tests
  the scalar functional implementation, while the weighted-median proof
  identifies the constrained support. N4/N8 agreement can expose code
  errors but cannot establish asymptotic growth or literature novelty.
- Verdict: standard analytic/computational variant.
- Cheapest test/kill: compare all scalar derivative entries against frozen
  forward AD at N4 and N8; discrepancy blocks the screen.
- Actual runs: recorded in `attempts/C1.md` as completed.
- Disposition: retained control; finite fits cannot establish polynomial
  growth. Symmetric first-weight Hahn alpha is identically zero; use the
  prescribed absolute scale one, with that exception explicit.

## IDEA?nn-mop-cond-codex-C1-03 — suppressing omitted fields

Aliases: degree-geometric scaling; hidden structural shift; arbitrary
normalization; entrywise scaling cancellation.

- Question/scope: can arbitrary fieldwise renormalization itself make the
  gauge optimization meaningless?
- Mechanism: distinguish scaling all entries of a field by one constant
  (which cancels) from nonuniform site scales and data-dependent gauges.
- Closest: PD-T432's explicit distinction between componentwise and
  fieldwise output, and IDEA-530's near-zero-output reporting limitation.
- Separation/kill: derive the exact transformed metric; an assertion that
  shrinking an entire field changes its field-relative condition fails
  by direct cancellation.
- Literature baseline and search limitations: PD-T432/IDEA-530 supplies
  the metric baseline; LIT-502/LIT-348 supplies the distinct practical
  norm-balancing context. Neither comparison asserts a historical-priority
  claim for cancellation; bounded literature coverage is stated below.
- Applicable obstructions and exact hypotheses: common field scaling
  cancels only with the corresponding homogeneous field-relative scale;
  site-dependent or input-dependent changes require their actual
  derivatives. Omitting forward structural coefficients changes the
  observable metric and does not remove an included invariant b field.
- Kill criterion written before testing: no separate pre-test written
  record is established here. Retrospectively, failure of the claimed
  common-factor cancellation in the exact defined metric would kill the
  explanatory statement; a different output denominator would instead
  fall outside its hypotheses.
- Test discriminability: derive numerator and denominator under the same
  constant scaling. Exact cancellation separates that case from a changed
  metric; it cannot decide arbitrary site-dependent gauges or prove that
  every gauge optimization is ill-posed.
- Verdict: explanatory variant, retained. The blanket interpretation
  "all gauge optimization is ill-posed" is abandoned as too broad.
- Scope: excluding structural shifts can hide large representation costs;
  it does not remove the invariant b-field lower bound. No new PD-N is
  assigned to an abandoned interpretation.

## 2026-11-06 attribution addendum — audit-01 MAJOR-2

This is an attribution repair under handoff 03, at response input
`3d5b29d7aa8c1274793139d7040695035e1bda22`, not a new candidate or claim.
The initial search above omitted the closest scaling and scalar literature;
its historical coverage statement is retained rather than retroactively
expanded. The bounded source checks and limits are in
[response-literature.md](response-literature.md).

- **LITERATURE — LIT-502 / LIT-348:** Faghih–Van Barel–Vandebril,
  arXiv:2608.25758v1, §3.1 (PDF pp. 10–11) balances corresponding W/V
  column norms; §5.1 / Fig. 2 (PDF pp. 20–21) reports improved recurrence
  residuals with scaling and incremental updating. This is algorithmic
  residual performance. C1 quantifies the forward map in the declared
  fieldwise metric; the retained b fields impose its lower bound. These
  statements concern different quantities and do not contradict one another.
- **LITERATURE — Fischer 1998, LIT-113:** *On Generating Orthogonal
  Polynomials for Discrete Measures*, Z. Anal. Anwend. 17, 183–205,
  Lemmas 4–5, pp. 190–191, is the closest scalar node/weight derivative
  predecessor. Theorem 2 and Corollaries 1–2, pp. 192–193, address
  conditioning. LIT-113's secondary account reports O(N²) for regular
  discretizations; the exponent and exact hypotheses are not relied on here.
  A bounded direct text check in this response confirms the derivative
  subject, not a complete fulltext reading or equivalence of condition norms.
  LIT-112 (Fischer 1996, modified moments) and LIT-365 are related
  secondary records; IDEA-087/088 already classify the Fischer-type
  conditioning extension as settled background.

C1-02 is an implementation/control variant of that scalar baseline; the
present proof supplies the stated fixed-mass support and input-coordinate
conventions. No novelty or source-priority claim is made for scalar
coefficient differentiation, the slow finite-grid control, or norm balancing.
No external polynomial growth bound is imported into these benchmark results.
