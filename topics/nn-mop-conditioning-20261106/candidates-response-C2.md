# C2 response candidate records — retained Hahn upper subroutes

2026-11-06, Codex developer, gpt-6.1-sol high; rules and response source
`3d5b29d`. These records instantiate `templates/IDEA.md` for already
considered C2 rounds 4–6. Their parent remains
`IDEA?nn-mop-cond-codex-C2-03`; the new suffixes distinguish subforms,
not new core mechanisms. No final IDs are assigned.

## Reading scope and timing

The response read the complete 1112-line `state/IDEAS.md` inventory,
including all obstruction and disposition tables, aliases, and retained
unnumbered subroutes. The shortlist was IDEA-117, 376–379, 530–536,
554–555, their full relevant gate/candidate entries, the C2 gate and
attempt ledger, and the linked Hahn and binomial lower/upper records.
Terms screened include Hahn/Krawtchouk, terminal dual, positive
coefficients/finite differences, separate global maxima, common nodes,
grid differentiation, Vandermonde/evaluation conditioning and sharp rate.
The complete registry includes PR12/14/15/17/19/22/23/25, cleanup,
frontier and nonproduct tables; none provides an escaped hypothesis for
these three already recorded subroutes. `literature/INDEX.md` was searched
for those mechanisms and its relevant NN/MOP and interpolation rows read.
This is repository-bounded comparison, with no new primary-source read
or priority claim. Original gate coverage is [C2 gate](novelty-gate-C2.md).

The original gate and attempt ledger already describe the kill tests and
outcomes, but these full template records are written after those outcomes
and [audit 01](audit-01.md), in response to MAJOR-3. Each field headed
“Kill criterion written before testing” below reconstructs the previously
recorded intended test; this response does not independently establish its
pre-run timing or retroactively assert preregistration.

## IDEA?nn-mop-cond-codex-C2-03-r4 — separate global maxima

Aliases: C2-03 round 4; product-of-maxima envelope; Hahn center/endpoint
mismatch; nodewise correlation loss.

- Question / scope: Can the balanced Hahn terminal second-weight row be
  bounded at its known base rho_H by independently maximizing its two
  polynomial factors?
- Mechanism and hypotheses: For every integer M>=2 in the exact
  alpha1=1, alpha2=3/2, gamma=1 Hahn family, replace
  `sum W2(k)|P(k)Q2(k)|/M!` by
  `E_M=(sum W2)max|P|max|Q2|/M!`, using the balanced terminal index.
- Closest registry entries (read in full): IDEA-533/534/535, parent
  C2-03 and its round-3 positive half-grid row; IDEA-554/555 provide
  unresolved transfer/asymptotic alternatives, not this estimate.
- Separation criterion vs closest entry (and observation that falsifies
  it): A norm-matched upper at rho_H would complement the existing exact
  row lower/rate. A proved exponential lower base for E_M strictly larger
  than rho_H erases that hoped-for matching-rate distinction.
- Literature baseline and search limitations: The repository's
  LIT-347/348/562–568 NN/MOP context and IDEA-535 terminal coefficient
  summation are attribution context under the original C2 gate. No source
  theorem giving this envelope rate is inherited; no exhaustive search
  or new historical method is claimed.
- Applicable obstructions and exact hypotheses broken: A row-rate theorem
  is not a full-input/four-field upper; finite samples are not an all-N
  argument. This subform removes the pointwise P–Q2 correlation retained
  in the exact row. It escapes neither obstruction.
- Novelty gate verdict: variant with difference, an upper-envelope
  subform of parent C2-03, not a new core mechanism.
- Cheapest decisive test: Retain a center polynomial value and an
  endpoint dual term on M=4l+2; derive their exponential product base.
- Kill criterion written before testing: Reconstructed from the original
  round-4 gate: kill the matching-rate use of this decoupling if its
  analytically proved lower base exceeds rho_H. Timing qualification above.
- Test discriminability: An asymptotic lower along one infinite
  subsequence disproves every all-M `C M^a rho_H^M` envelope bound.
  A finite overshoot would not do so.
- Actual test results and committed evidence: The analytic proof in
  [upper-envelope](theory/c2-hahn-upper-envelope.md) establishes
  `limsup E_M^(1/M)>=beta>12.4>12.2>rho_H`.
  The unchanged [exact checker](code/c2_hahn_upper_search.py) corroborates
  the underlying finite identities and rational base separation.
- Disposition and precise rejected scope: REJECTED: failed, solely the
  independent-global-maxima envelope as a matching-rho_H upper.
- Disposition reason: PROVED exponential loss in that envelope. Correlated
  bounds and the full Hahn matching upper remain OPEN.
- Canonical theory / negative-result ID:
  [PD-N?nn-mop-cond-codex-C2-01](theory/c2-hahn-upper-envelope.md), PROVED.
- Topic / completed audit link / history: [attempt round 4](attempts/C2.md#round-4--full-hahn-upper-separate-global-maxima-bounded-route);
  [audit 01](audit-01.md), MAJOR-3 and accepted envelope mathematics.
  Full candidate record extracted on 2026-11-06 after that audit.

## IDEA?nn-mop-cond-codex-C2-03-r5 — unchanged positive differences below terminal degree

Aliases: C2-03 round 5; arbitrary-index positivity extension; complementary
factor U; unchanged positive-coefficient extension.

- Question / scope: Does the terminal positive-finite-difference argument
  extend unchanged to all indices `1<=t=n+m<=M` in the same Hahn family?
- Mechanism and hypotheses: In the exact arbitrary-index formula use
  `U(l)=prod_j(l+1+x_j)(t+2-l)_(M-t)` and require every relevant
  `Delta^k U(0)>0`, including below terminal degree, to retain the terminal
  positive-sum comparison without a cancellation estimate.
- Closest registry entries (read in full): IDEA-534/535, parent C2-03,
  the round-3 half-grid proof and the round-4 envelope failure.
- Separation criterion vs closest entry (and observation that falsifies
  it): Positivity for all degrees would extend the terminal comparison to
  actual nonterminal rows. One exact negative relevant difference erases
  that unchanged-positivity distinction; it does not refute the dual formula.
- Literature baseline and search limitations: The original C2 gate's
  LIT-347/348/562–568 context and the predecessor positive coefficient-sum
  method are the baseline. No Hahn formula or positivity theorem is
  imported from a citation. Search is repository bounded and no new
  primary reading or priority claim is made.
- Applicable obstructions and exact hypotheses broken: The terminal
  argument has `t=M`; this extension drops that hypothesis. The new
  complementary factor has decreasing factors and need not preserve
  finite-difference signs. Exact finite refutation is adequate for the
  universal positivity assertion, but not for an all-N sharp-rate theorem.
- Novelty gate verdict: variant with difference, a failed nonterminal
  extension of the parent C2-03 positive-sum mechanism.
- Cheapest decisive test: Evaluate the proposed U at consecutive integers
  in the smallest nonterminal cases before attempting asymptotic estimates.
- Kill criterion written before testing: Reconstructed from the original
  rounds-5–6 gate: one exact negative difference kills the unchanged
  positive-difference extension. Timing qualification above.
- Test discriminability: A single rational counterexample decides the
  stated universal sign claim; it does not decide cancellation-sensitive
  absolute-sum bounds, weighted estimates or the full Hahn upper.
- Actual test results and committed evidence: At M=3, t=1, nu=(1,0),
  `U(l)=(l+2)(3-l)(4-l)`, so U(0)=24, U(1)=18 and Delta U(0)=-6.
  [Positivity failure](theory/response-c2-positivity-failure.md) preserves
  the proof and check limitations. The response re-evaluated those values
  exactly; the unchanged checker reproduces all recorded finite identities.
- Disposition and precise rejected scope: REJECTED: failed, solely the
  unchanged positive-difference proof extension. Its universal positivity
  premise is refuted by the exact counterexample.
- Disposition reason: PROVED failure of that sign premise; the correlated
  arbitrary-index upper remains OPEN.
- Canonical theory / negative-result ID:
  [PD-N?nn-mop-cond-codex-response-C2-positivity](theory/response-c2-positivity-failure.md), PROVED.
- Topic / completed audit link / history: [attempt round 5](attempts/C2.md#round-5--arbitrary-index-cauchy-inverse-empty-for-rate);
  [audit 01](audit-01.md), MAJOR-3. Extracted from the already audited
  upper-search counterexample on 2026-11-06; no new mathematical scope.

## IDEA?nn-mop-cond-codex-C2-03-r6 — polynomial unweighted grid differentiation

Aliases: C2-03 round 6; common-node derivative transfer; equispaced
grid-supnorm derivative bound; unweighted interpolation differentiation.

- Question / scope: Can the common-node channel be controlled from the
  terminal weight-row estimate at polynomial cost by a uniform unweighted
  grid-supnorm derivative inequality for every polynomial of degree<=M?
- Mechanism and hypotheses: On integer nodes 0,...,M, posit constants
  C>0 and fixed a, independent of M and p, such that
  `max_k |p'(k)|<=C M^a max_k |p(k)|` for all degree<=M p. Apply it to
  the derivative factors in the exact common-node forcing. The same node
  displacement acts in both weight channels.
- Closest registry entries (read in full): Parent C2-03, IDEA-534/535,
  round-3 terminal row and round-5 arbitrary-index dual; IDEA-554's scaled
  evaluation transfer remains a broader deferred route.
- Separation criterion vs closest entry (and observation that falsifies
  it): A polynomial unweighted transfer would supply a missing node
  derivative step at the terminal weight rate. An exponential lower bound
  for the required differentiation operator norm destroys that distinction.
- Literature baseline and search limitations: Classical cardinal
  interpolation and the repository's evaluation-conditioning context
  (IDEA-554; LIT-112/113/365 as contextual scalar conditioning) are the
  baseline, not a newly claimed interpolation mechanism. No source theorem
  is invoked; the proof differentiates the cardinal products directly.
  No exhaustive primary-literature claim or new source reading is made.
- Applicable obstructions and exact hypotheses broken: Passing from a
  weighted correlated row to an arbitrary unweighted polynomial discards
  its structure. Degree grows with the equispaced grid; continuous-supnorm
  derivative inequalities do not provide the proposed discrete norm bound.
  Finite-support cutoff and all-common-node-channel requirements remain.
- Novelty gate verdict: variant with difference, a failed norm-transfer
  subform of parent C2-03, not a new core mechanism.
- Cheapest decisive test: Differentiate an endpoint cardinal polynomial
  indexed at the central grid point and lower-bound one matrix entry.
- Kill criterion written before testing: Reconstructed from the original
  rounds-5–6 gate: an exponential lower bound for the unweighted derivative
  norm kills a uniform polynomial-cost transfer. Timing qualification above.
- Test discriminability: An all-M operator lower with exponential base 2
  disproves the universal polynomial norm inequality. It does not establish
  that the actual P,Q_s products attain this worst case or exclude weighted
  correlation-sensitive estimates.
- Actual test results and committed evidence: The analytic proof in
  [node-transfer failure](theory/response-c2-node-transfer-failure.md) gives
  `||D||_infinity>=2^M/[M(M+1)]` for every M>=2. The response independently
  differentiated exact cardinal products for M=2,...,16 (15 endpoint
  checks); the unchanged checker separately replays the common-node formula.
- Disposition and precise rejected scope: REJECTED: failed, solely the
  universal polynomial unweighted grid derivative transfer.
- Disposition reason: PROVED exponential operator lower; the weighted
  correlated common-node estimate and full-map Hahn upper remain OPEN.
- Canonical theory / negative-result ID:
  [PD-N?nn-mop-cond-codex-response-C2-node-transfer](theory/response-c2-node-transfer-failure.md), PROVED.
- Topic / completed audit link / history: [attempt round 6](attempts/C2.md#round-6--common-node-derivative-transfer-empty-for-rate-stop);
  [audit 01](audit-01.md), MAJOR-3. Extracted from the already audited
  upper-search proof on 2026-11-06; no new mathematical scope.

## Candidate-to-result mapping (namespace-qualified, provisional)

Local numeric suffixes are not a one-to-one candidate/result ID map.
These rows preserve every existing alias; final allocation is deferred to
PR preparation. The parent candidate and its retained subforms are not
renumbered as new independent methods.

| Candidate ID or preserved alias | Result ID(s) | Durable result / status and relationship |
|---|---|---|
| IDEA?nn-mop-cond-codex-C2-01 | PD-T?nn-mop-cond-codex-C2-hard-01 | [sharp upper](theory/c2-sharp-upper.md), PROVED benchmark full-map upper/rate; with PD-T437 solves the benchmark rate conjunct of PD-T448 |
| IDEA?nn-mop-cond-codex-C2-02 | PD-T?nn-mop-cond-codex-C2-01 | [parameter lower](theory/c2-krawtchouk-parameter-lower.md), PROVED supporting lower; general-pair matching upper OPEN |
| IDEA?nn-mop-cond-codex-C2-03 | PD-T?nn-mop-cond-codex-C2-02; PD-T?nn-mop-cond-codex-C2-03 | [normality](theory/c2-hahn-normality.md) and [base-two lower](theory/c2-hahn-lower.md), PROVED supporting results; no full Hahn case solved |
| C2-03 round 3; historical C2-04 ledger alias | PD-T?nn-mop-cond-codex-C2-04 | [terminal row rate](theory/c2-hahn-terminal-rate.md), PROVED row-rate/full-map-liminf lower under parent C2-03; matching full-map rate OPEN |
| IDEA?nn-mop-cond-codex-C2-03-r4 | PD-N?nn-mop-cond-codex-C2-01 | [envelope failure](theory/c2-hahn-upper-envelope.md), negative statement PROVED; candidate REJECTED: failed |
| IDEA?nn-mop-cond-codex-C2-03-r5 | PD-N?nn-mop-cond-codex-response-C2-positivity | [positivity failure](theory/response-c2-positivity-failure.md), negative statement PROVED; candidate REJECTED: failed |
| IDEA?nn-mop-cond-codex-C2-03-r6 | PD-N?nn-mop-cond-codex-response-C2-node-transfer | [node-transfer failure](theory/response-c2-node-transfer-failure.md), negative statement PROVED; candidate REJECTED: failed |

The parent-target classification proposal is in
[classification-proposal.md](classification-proposal.md); supporting Hahn
and general-parameter lowers are dependencies, not resolved full target
cases. The predecessor's registered OPEN display is historical and remains
unchanged in this response, pending audited application at PR preparation.
