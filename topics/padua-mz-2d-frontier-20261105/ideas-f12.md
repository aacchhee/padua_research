# F1/F2 candidate memory

Rules/input `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`; main/base
`440d1079e42c3ef21c40d1cf8870f5b206410c6a`. Codex developer, requested
gpt-6.1-sol xhigh; runtime model metadata is unexposed. No Git authority.

## Novelty gate and exact reading/search scope

Before proposing the candidates below, read AGENTS.md,
agents/WORKFLOW.md, agents/codex/CODEX.md, handoff 01 and the campaign
plan. Read all 889 lines of state/IDEAS.md in bounded `sed` slices,
including every canonical, historical, seed, current, obstruction and
disposition table. An initial combined output was truncated; the missing
portions were reread in overlapping slices, rather than counted as read.
This includes IDEA-210–227 and the complete PD-N044–053 table.

Full closest candidate records read: the M1 and M3 IDEA files; the M2
candidate file; Padua ideas-d1/d2/d4/d5 and directions/ideas-d3. Closest
full theory read for these mechanisms: PD-T013–015, PD-T018, PD-T022,
PD-T027/028, PD-T106/109–117, PD-N045–048 and PD-N050–053. Frozen
definitions and the previous report were read. Further predecessor
reading is recorded in the attempt files. No unpublished literature
record is used as a theorem dependency, and no historical novelty is
claimed.

Issued targeted `rg -n -i` searches over the MZ theory, previous Padua
topic, IDEAS and literature INDEX for `locali[sz]`, `corner`, `endpoint`,
`hankel`, `schur`, `positive.node`, `inertia`, `codimension`, `harmonic`,
`scale`; the displayed shortlist was bounded to the first 100 matches.
Then issued repository-wide `rg -l -i` over all Markdown in `state`,
`tracks`, `topics`, `literature` for `mesoscop`, `microscop`,
`harmonic.{0,35}(locali|concentr)`,
`endpoint.{0,35}(locali|concentr)`,
`codimension.{0,35}(signed|quadrature)`,
`reciprocal.{0,30}(weight|inertia)`, `inverse.{0,30}compression`,
`hankel.{0,30}(tail|core)`.
The latter returned the PD-T018 theory and three unrelated audit/handoff
records; the exact PD-T018 construction was reread in full. The INDEX
was searched for CC, MZ, Mastroianni/Russo, Hankel, Widom and localization;
this is a bounded local predecessor screen, not an exhaustive literature
search or primary fulltext reading. No PDF was opened.

## IDEA-384 — limits of the absolute-coefficient intermediary

Original provisional ID: `IDEA?mz2d-frontier-codex-10`.

Aliases: 1D uniform-gap Z-matrix barrier; central Dirichlet test;
sign-discard comparison.

- Question / scope: can the exact PD-T014 sign-discard lower bound
  `a^T A_N a >= |a|^T A_N |a|`, followed by comparison of its right
  side with `a^T M_N a`, prove a uniform endpoint gap?
- Mechanism and hypotheses: retain precisely this intermediary, with
  `A_N=2M_N-R_N` in the unnormalized Chebyshev basis on degree N−1.
- Closest registry entries (read in full): IDEA-062/063/073 and their
  linked PD-T014/015/022; PD-N002/003 distinguish the old failed routes.
- Separation criterion: the new statement concerns the best possible
  mass-normalized lower bound after erasing coefficient signs, rather
  than the known `1/N` floor or the actual spectrum of A_N. It is killed
  if no admissible sign pattern makes the intermediary ratio tend zero.
- Literature baseline and search limitations: standard Dirichlet-kernel
  concentration; bounded repository screen above; no priority claim.
- Applicable obstructions and exact hypotheses broken: no PSD inference
  for the Hankel defect is made. This addresses 1D before the separate
  2D sign-cycle obstruction PD-N045.
- Novelty gate verdict: variant with a precisely different estimate.
- Cheapest decisive test: take N=2L+1, coefficients `a_(2j)=(-1)^j`,
  all odd coefficients zero, and compare the continuous norms before
  and after absolute values by finite trigonometric identities.
- Kill criterion written before testing: a bounded-away-from-zero ratio
  on this sequence defeats this test; a ratio tending zero refutes only
  the proposed uniform intermediary inequality.
- Test discriminability: a single analytic sequence decides that
  inequality, while leaving PD-T027's true spectral gap open.
- Actual test results: the ratio is at most
  `32(2+log(2N))/L`, which tends zero; the durable proof uses an even
  simpler explicit bound. See the linked record for the final constants.
- Disposition: retained scoped PROVED obstruction; the 1D and 2D upper
  targets remain OPEN.
- Disposition reason: failed uniform sign-discard intermediary, with
  the exact quantifiers in the PD-N; no claim against other comparisons.
- Canonical record: PD-N104,
  theory/f12-1d-sign-discard-obstruction.md.
- Topic / audit / history: 2026-11-05; analytic, no computation needed;
  independent/Claude review pending.

## IDEA-385 — mesoscopic mass of the admissible harmonic witness

Original provisional ID: `IDEA?mz2d-frontier-codex-11`.

Aliases: fixed-width endpoint escape; distributed logarithmic quasimode;
Padua coordinate edge escape.

- Question / scope: does the known admissible low-Rayleigh witness
  concentrate in a fixed angular K/N endpoint layer? What happens to
  its exact Padua marginal lift?
- Mechanism and hypotheses: use the exact PD-T018 polynomial, retaining
  endpoint cancellation before taking absolute values.
- Closest registry entries (read in full): IDEA-066/072/215,
  PD-T018/021, and IDEA-218/PD-N049 for the different rotated packet.
- Separation criterion: quantify the physical continuous mass profile
  of this existing witness, rather than produce another quotient or
  assert that it is an extremal eigenvector. A fixed positive endpoint
  mass fraction along N would kill the escape conclusion.
- Literature baseline and search limitations: the witness is inherited
  locally, not newly invented; only its stated localization estimate is
  developed. No historical novelty claim.
- Applicable obstructions and exact hypotheses broken: the degree
  constraint is exactly satisfied; PD-N006's uncorrected alternating
  vector and PD-N047's inadmissible tensor product are not used.
- Novelty gate verdict: variant with a distinct quantitative property.
- Cheapest decisive test: use Lipschitz continuity of sine in each
  endpoint-cancelled summand for `theta<=K/N`, then compare with the
  proved log-cubed continuous norm lower bound in PD-T018.
- Kill criterion written before testing: uncancelled `log N` growth at
  theta=O(1/N), or failure of the endpoint mass upper bound, kills the
  proposed argument. This does not test actual extremal eigenvectors.
- Test discriminability: proves or refutes the exact witness profile;
  it cannot pass or kill campaign G3 for actual eigenvectors.
- Actual test results: endpoint mass is at most
  `pi^2 K^2` for fixed K and sufficiently large N, while total
  norm squared is at least `log^3(N)/512`. The Padua lift has vanishing
  mass in the union of all K/m edge neighborhoods.
- Disposition: retained PROVED supporting statement; no F1/F2 target
  upgraded, no extremal-vector or eigenvalue-order conclusion.
- Disposition reason: successful analytic supporting result.
- Canonical record: PD-T294,
  theory/f12-harmonic-boundary-escape.md.
- Topic / audit / history: 2026-11-05; analytic; review pending.

## IDEA-386 — reflected Hankel core and transition remainder

Original provisional ID: `IDEA?mz2d-frontier-codex-12`.

Aliases: 1D upper core-tail split; positive full reflection kernel.

- Question / scope: prove a uniform 1D endpoint upper gap, then seek a
  signed 2D analogue.
- Mechanism and hypotheses: complete the CC alias Hankel kernel
  `1/((2N-i-j)^2-1)` to its full positive moment matrix, and bound the
  removed low-sum triangle plus the direct-moment correction in the
  continuous mass metric.
- Closest registry entries (read in full): IDEA-053/060/062/071/073,
  PD-T013/014/022/027 and PD-N002; 2D IDEA-210/214.
- Separation criterion: keep a positive full Hankel core and estimate
  the *transition remainder*, rather than assert positivity of the
  truncated defect. A bound only in Euclidean coefficient norm erases
  the intended mass-metric distinction.
- Literature baseline and search limitations: classical moment-Hankel
  representation and limiting operators; historical coverage incomplete.
- Applicable obstructions and exact hypotheses broken: PD-N002 applies
  to the truncated defect, not to the completed reflected moment matrix.
  PD-N045 forbids reusing a scalar sign switch in 2D.
- Novelty gate verdict: variant with an unfulfilled metric obligation.
- Cheapest decisive test: write the full positive integral kernel and
  locate exactly the removed triangle before any large numerical run.
- Kill criterion written before testing: failure to derive a
  mass-normalized transition-remainder estimate leaves this deferred;
  a coefficient-norm estimate by itself is insufficient.
- Test discriminability: exact decomposition can validate the route,
  but does not establish a small constant or spectral convergence.
- Actual test results: the positive core identity is elementary; no
  useful mass-normalized remainder estimate obtained in this bounded
  attempt. No new theorem or negative allocated for mere deferral.
- Disposition and reason: deferred; resume only with a quantitative
  remainder estimate or a separately specified distributed limit model.
- Canonical theory: original PD-T027 stays OPEN; attempt F1 records the
  precise missing inequality.
- Topic / audit / history: 2026-11-05; no experiment performed.

## IDEA-387 — inverse nodal compression by degree-m constraints

Original provisional ID: `IDEA?mz2d-frontier-codex-13`.

Aliases: reciprocal-weight inertia reduction; codimension m+1 test.

- Question / scope: reduce positivity of signed nodal weights restricted
  to degree m−1 values to the complementary degree-m constraints.
- Mechanism and hypotheses: an invertible diagonal nodal form and a
  full-rank constraint matrix C for the admitted value space give the
  standard inertia identity involving `C^T W^(-1) C`; zero weights need
  a separate limiting or exact treatment.
- Closest registry entries (read in full): IDEA-217's positive-node
  Schur complement, PD-T111/PD-N048, and IDEA-214's block resumption.
- Separation criterion: a new result would require an explicit all-m
  inertia estimate for the smaller reciprocal-weight matrix. Merely
  changing the Schur complement from primal to dual is no separation.
- Literature baseline and search limitations: standard constrained
  inertia, no priority claim.
- Applicable obstructions and exact hypotheses broken: retains the
  admissible sample-value constraints and avoids arbitrary-data
  positivity, but does not avoid the old missing signed-metric estimate.
- Novelty gate verdict: equivalent reformulation at present.
- Cheapest decisive test: identify the two complements through the
  same constrained quadratic form before computing spectra.
- Kill criterion written before testing: if no all-m estimate appears,
  consolidate with IDEA-217 and do not pursue as a new mechanism.
- Test discriminability: the identity detects equivalence; finite
  inertia agreement would not distinguish the routes analytically.
- Actual test results: standard dual Schur inertia gives the same
  positivity obligation; no estimate of its entries/signs derived.
- Disposition and reason: equivalent; retained here, not pursued; no
  PD-N and no duplicate reduction theorem allocated.
- Canonical theory: existing PD-T028 OPEN and IDEA-217 resumption point.
- Topic / audit / history: 2026-11-05; no computation performed.

## IDEA-388 — separated endpoint Fejer packet across an alias threshold

Original provisional ID: `IDEA?mz2d-frontier-codex-14`.

Aliases: localized signed-negative witness; asymmetric endpoint packet.

- Question / scope: can a fixed total-degree ratio below one already
  produce a negative signed Padua quotient, or eventual negativity?
- Mechanism and hypotheses: use
  `F_r(cos t)=(r+1)^(-1)(sin((r+1)t/2)/sin(t/2))^2` and
  `p=F_r(x)F_s(y)`, with `r=floor(alpha*m)`,
  `s=floor(beta*m)`, `alpha>1/2`, `beta>0`, `alpha+beta<1`.
  The exact cosine coefficients are nonnegative triangular sequences;
  their squares are explicit convolutions. The continuous L2 masses
  stay bounded as the meshes grow.
- Closest registry entries (read in full): IDEA-216/217/218/226,
  PD-N047/048/049, PD-T106/111/115. Added gate: repository-wide
  searches above already included endpoint localization and harmonic
  packets; the closest actual packet is the rotated harmonic one.
- Separation criterion: asymmetric *coordinate* endpoint localization
  with one squared coordinate bandwidth crossing m, while total degree
  stays below a fixed ratio; this is not a product of two critical CC
  witnesses or the rotated harmonic product. A nonnegative quotient
  bounded away from zero along the frozen test sequence kills this
  literal candidate's proposed negative mechanism.
- Literature baseline and search limitations: Fejer kernels are
  classical; no priority claim. No literature theorem is a dependency.
- Applicable obstructions and exact hypotheses broken: PD-N047 only
  rules out two independently critical CC factors; these factors have
  fixed coordinate ratios and seek *signed alias cancellation* instead.
  PD-N048 warns that negative corner divergence alone proves nothing.
- Novelty gate verdict: variant with a distinct admissible packet and
  signed-cancellation test.
- Cheapest decisive test: evaluate the exact alias form or actual signed
  weights on `(alpha,beta)=(.65,.30)` at m=100,400,1000; compare with
  `(.80,.15)` if the first sequence remains positive. Any detected
  negative value must be replayed with a rational coefficient witness.
- Kill criterion written before testing: no negativity and no decreasing
  trend in these two specified sequences stops this literal packet;
  no universal packet-family refutation follows. A proposed logarithmic
  term must survive reflection of the x aliases analytically.
- Test discriminability: a negative float quotient is a lead only;
  exact rational evaluation could refute positivity at that one m.
  Finite positive values never establish eventual behavior.
- Actual test results: separate numerical worker's receipt
  `evidence/g1-fejer.json` records positive quotients through m2000 at
  root-requested ratios .65/.30, .55/.40, .75/.20. At .75/.20 the m1000
  and m2000 quotients were about .94329 and .93652. These are reported
  measurements, not a rerun by this developer. The frozen .80/.15
  follow-up was not executed; the other two ratios were distinct
  parent-requested probes. Positive values with a declining trend do
  not fire the stated combined kill. An exact local-weight asymptotic
  was subsequently proved in PD-T295. The original
  packet's explicit sinc-sum asymptotic was derived informally but is
  not needed or promoted here; simpler exact-parity carriers below
  provide rigorous countersequences without Poisson summation.
- Disposition and reason: deferred as an original packet; finite
  positivity retained. Resume only for an explicit finite witness or
  a separately audited exact asymptotic. No negative statement about
  this packet or family is inferred from these finite positives.
- Canonical theory: none until a proved or measured scoped result exists.
- Topic / audit / history: 2026-11-05, after root reported a new localized
  minimum-eigenvector branch at m400/600. This report is not a rerun by
  this worker and is not a dependency for any theorem.

## IDEA-389 — exact even-node carrier exposes negative logarithmic mass

Original provisional ID: `IDEA?mz2d-frontier-codex-15`.

Aliases: T_(m/2) Fejer carrier; even-even signed packet.

- Question / scope: refute all-m signed positivity by a precise
  admissible polynomial sequence; also test every fixed ratio >1/2.
- Mechanism and hypotheses: even m, `p_-=T_(m/2)(x)F_r(x)F_s(y)` with
  `r/m->a>0`, `s/m->b>0`, `a+b<1/2`. Its x samples vanish at odd j.
  Fixed-node weights from -12 are negative on the remaining even-even
  sublattice in the leading logarithmic scale.
- Closest registry entries (read in full): IDEA-216/217/218/226,
  candidate -14, and PD-N047/048/049. Same gate as -14; this is a
  refinement of that surviving packet with an exact parity invariant.
- Separation criterion: one carrier forces a definite sign in the
  logarithmic limiting sampled form. A zero leading signed coefficient
  after exact y-parity summation kills this distinction.
- Literature baseline and limitations: classical Fejer and cosine
  carriers; local proof only, no historical priority claim.
- Applicable obstructions and exact hypotheses broken: degree is
  m/2+r+s<m, not two critical coordinate factors. The whole signed
  sum is evaluated; negative-corner divergence alone is not used.
- Novelty gate verdict: variant with an exact sample-parity property.
- Cheapest decisive test: compute finite DCT sums before invoking any
  asymptotic spectrum: x energy tends a/3, y energy tends 2b/3 and its
  alternating energy is exactly zero for 2s<m+1.
- Kill criterion written before testing: any missing coefficient,
  nonzero y alternating contribution or failed global domination
  blocks the proposed negative asymptotic.
- Test discriminability: exact parity plus a uniform summable majorant
  gives a genuine asymptotic signed form, without fitting eigenvalues.
- Actual test results: exact coefficient is `Q_m(p_-²)/log m -> -16ab/9`;
  total continuous squared norms are uniformly bounded. Thus the signed
  minimum tends to minus infinity on every containing admitted space.
- Disposition and reason: retained PROVED countersequence, pending
  required Claude audit; original positivity target is refuted by
  this analytic asymptotic, with no named finite violating degree yet.
- Canonical record: PD-N105,
  theory/f12-eventual-negative-carrier.md.
- Topic / audit / history: 2026-11-05; analytic. Astra and F3 developers
  independently reconstructed the common lemma and carrier constants;
  completed reports must identify their actual scope and hashes.

## IDEA-390 — exact odd-node carrier exposes positive logarithmic mass

Original provisional ID: `IDEA?mz2d-frontier-codex-16`.

Aliases: sine-product polynomial carrier; odd-odd signed packet.

- Question / scope: refute the universal upper threshold below two.
- Mechanism and hypotheses: even m,
  `p_+=.5[T_(m/2-r)-T_(m/2+r)]F_r(x)F_s(y)`; the sine-product identity
  makes it `sin(m*t/2)sin(r*t)F_r(cos t)F_s(y)`. This is a polynomial
  and vanishes at even j. Assume r/m->a>0, s/m->b>0, 2a+b<1/2.
- Closest registry entries (read in full): candidate -15 and the same
  IDEA-216/217/218/226; PD-T110 and its boundary-zero sign warning.
- Separation criterion: flip the selected x sublattice while preserving
  polynomiality, degree and bounded norm. A residual even-node x sample
  or a zero odd energy kills the claimed positive limit.
- Literature baseline and limitations: elementary trigonometric carrier,
  no priority claim; no new external source used.
- Applicable obstructions and exact hypotheses broken: the construction
  retains signs and uses no Z-matrix or pointwise doubled-tensor bound.
  A lone sine factor would not be a polynomial; the exact product is.
- Novelty gate verdict: variant with an opposite exact parity invariant.
- Cheapest decisive test: since 4r<m eventually, the polynomial
  `sin²(r*t)F_r²` has zero alternating DCT sum; its ordinary constant
  gives odd-node x energy a/6. The y energy remains 2b/3.
- Kill criterion written before testing: degree above m−1, loss of
  polynomiality or a zero/negative limiting signed coefficient rejects
  this literal construction.
- Test discriminability: a positive logarithmic form with bounded
  continuous norm proves actual unbounded upper eigenvalues, not just
  failure of a sufficient majorant.
- Actual test results: `Q_m(p_+²)/log m -> +8ab/9`; norms uniformly
  bounded. Parent-requested floating carrier probes at other r,b,s
  parameters were positive and increasing through m2000; these are
  separate measured evidence, not this proof's dependency.
- Disposition and reason: retained PROVED analytic upper countersequence,
  pending audit. The eventual upper threshold is refuted; an explicit
  finite crossing is not named by the asymptotic proof.
- Canonical record: PD-N106,
  theory/f12-eventual-upper-carrier.md.
- Topic / audit / history: 2026-11-05; exact degree-r Fejer convention
  fixed in both packet records; supplementary Astra full-file review
  found no gap; required Claude audit pending.


## Audited preparation — current dispositions (2026-11-05)

Final allocation follows the cleared live union scan and [final-ID map](preparation/final-id-map.json). Original provisional IDs and all descriptive aliases are preserved. Earlier development-time pending, OPEN and deferred wording above is historical wherever superseded by the dated resolution or this table. [Claude audit-01](audit-01.md) accepted the mathematics and dispositions at candidate `dee638408505c9977f3febd98fdd42c9bc512c92`; [response-01](response-01.md) resolves its documentation findings. This mechanical registration adds no proof, execution, novelty claim or status upgrade.

AC’s display remains binding: PD-T028/110/116 keep Status OPEN with REJECTED: refuted disposition and PROVED negative links. Their original positive formulations are historical, not unresolved or usable assertions; PD-T027’s genuine 1D gap/limit target remains OPEN.

| Final candidate / original alias | Current disposition and exact scope |
|---|---|
| IDEA-384; `IDEA?mz2d-frontier-codex-10` | REJECTED: failed for the proposed uniform intermediary estimate; the scoped negative statement is PROVED as [PD-N104](theory/f12-1d-sign-discard-obstruction.md). The genuine 1D target PD-T027 stays OPEN. |
| IDEA-385; `IDEA?mz2d-frontier-codex-11` | Retained PROVED supporting profile, [PD-T294](theory/f12-harmonic-boundary-escape.md); no conclusion about actual extremal eigenvectors or their eigenvalue order. |
| IDEA-386; `IDEA?mz2d-frontier-codex-12` | Deferred: resume with a quantitative mass-normalized transition-remainder estimate or a specified distributed limit model; no PD-N, and PD-T027 stays OPEN. |
| IDEA-387; `IDEA?mz2d-frontier-codex-13` | Equivalent to IDEA-217’s constrained-form obligation; not pursued, no duplicate theorem or PD-N. The original positive target PD-T028 is refuted by [PD-N105](theory/f12-eventual-negative-carrier.md)/[PD-N106](theory/f12-eventual-upper-carrier.md); the equivalence itself is retained. |
| IDEA-388; `IDEA?mz2d-frontier-codex-14` | Deferred as the original unmodulated packet; audited finite positive float probes are retained in [PD-T300](theory/frontier-measurements.md). Resume only for an explicit finite witness or a separately audited exact asymptotic; no whole-family rejection. |
| IDEA-389; `IDEA?mz2d-frontier-codex-15` | Retained PROVED countersequence, [PD-N105](theory/f12-eventual-negative-carrier.md): even m, negative logarithmic signed energy and bounded continuous norm. Existence only; no feasible finite witness/onset and no explanation of the uncertified m1600 float hit. |
| IDEA-390; `IDEA?mz2d-frontier-codex-16` | Retained PROVED upper countersequence, [PD-N106](theory/f12-eventual-upper-carrier.md): even m, positive logarithmic signed energy and bounded continuous norm. Existence only; no effective finite crossing or sharp extremal rate. |

Result aliases retained after mechanical reference substitution:

| Original provisional result | Final ID |
|---|---|
| `PD-T?mz2d-frontier-codex-11` | PD-T294 |
| `PD-T?mz2d-frontier-codex-12` | PD-T295 |
| `PD-N?mz2d-frontier-codex-10` | PD-N104 |
| `PD-N?mz2d-frontier-codex-13` | PD-N105 |
| `PD-N?mz2d-frontier-codex-14` | PD-N106 |


## 2026-11-06 completed 1D continuation of IDEA-386

The historical deferred 1D route above is resumed and consolidated under IDEA-386, retaining all four candidate subrecords: [core](../padua-mz-sharp-constants-20261106/ideas/S2-core.md), [endpoint model](../padua-mz-sharp-constants-20261106/ideas/S2-endpoint.md), [compactness](../padua-mz-sharp-constants-20261106/ideas/S2-compactness.md) and [finite certificate](../padua-mz-sharp-constants-20261106/ideas/S2-certificate.md). [PD-T526](../padua-mz-sharp-constants-20261106/theory/S2-uniform-upper.md) proves λ_max≤5/3 for every N≥2 in the continuous mass metric; [PD-T527](../padua-mz-sharp-constants-20261106/theory/S2-eta-deficit.md) proves the two-sided logarithmic deficit order. The specified endpoint model [PD-T528](../padua-mz-sharp-constants-20261106/theory/S2-endpoint-model.md) is transferred by [PD-T529](../padua-mz-sharp-constants-20261106/theory/S2-fixed-trial-limit.md), [PD-T530](../padua-mz-sharp-constants-20261106/theory/S2-qualitative-limit.md) and [PD-T531](../padua-mz-sharp-constants-20261106/theory/S2-finite-certificate.md). PD-T027 is PARTIAL under AC's decomposition: the uniform-gap and convergence/Λ_edge-identification conjuncts are PROVED, while its decimal-value conjunct stays OPEN. The signed 2D analogue remains deferred; the scoped sign-erasure obstruction PD-N104 is unchanged, and no new PD-N is assigned. Completed [audit-01](../padua-mz-sharp-constants-20261106/audit-01.md), [audit-02](../padua-mz-sharp-constants-20261106/audit-02.md) and [audit-03](../padua-mz-sharp-constants-20261106/audit-03.md).
