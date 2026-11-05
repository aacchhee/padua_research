# L3/L4 candidate memory

Rules/input SHA: `8359bf7a047d9a212bd841224fb97a458cb7435e`. Developer: Codex,
`gpt-6.1-sol`, xhigh, assigned mathematical development; runtime effort is not
independently exposed. No Git, shared-registry or handoff authority.

## Gate and scope

**Gate status: incomplete when G0 stopped the campaign.** Registry headings
and aliases were scanned through the complete `state/IDEAS.md`; bounded
summary/disposition views covered every campaign, but some combined tool
outputs were truncated, so complete summary-row coverage is not claimed.
Every named obstruction table was read, including the historical bivariate,
MZ, lattice, programme and later addenda. Shortlist:
IDEA-127/130/134/140, IDEA-147/148/150/151, IDEA-246–267. The canonical drift
candidate files were inspected, with complete central L3/L4 entries
IDEA-246–253 and IDEA-256; some combined views of neighboring entries were
truncated and must be repeated before the gate can close. In particular
IDEA-251 is already the normalized inverse criterion,
IDEA-252 rejects omitting the local pivot ratio, IDEA-253 is only a trivial
pathwise-quantifier rejection, and IDEA-254/PD-N062 does not forbid O(u)
stability. IDEA-250 already contains coherent and multinode scalar witnesses.

Search scope: `state/IDEAS.md`, bivariate-Lanczos theory and negative results,
the prior drift topic (including its reports, audit/response findings),
`literature/INDEX.md` and relevant literature records. Mechanism terms and
synonyms: `selection`, `staircase`, `adaptive`, `pivot`, `normal quotient`,
`surrogate`, `inverse`, `finite-u`, `remainder`, `nonlinear`, `radius`,
`majorant`, `row bound`, `Perron`, `Collatz`, `scalar CGS2`, `multinode`,
`coherent`, `spectral` and `Frobenius`.

Closest sources read fully: PD-T142/143 and PD-T054. PD-T138/141's model,
statements and proofs, the scalar producer and exact recurrence code were
read; PD-T136/137/139/140 and PD-N013/015/062 were inspected through linked
records/summaries and still require full-source completion. Literature INDEX
metadata and relevant full rows were consulted before comparisons:
LIT-241–243 already reports triangular-substitution error bounds and variable
selection (Barrio–Peña–Sauer), LIT-280–284 records the V+A exact-span versus
orthogonality distinction, and LIT-114/255 concerns one-operator Krylov
conditioning. These are repository reading records, not newly read external
fulltexts. No new literature/priority claim, no assertion of an exhaustive
historical search, and no PDF acquisition.

Applicable obstructions: (C) implies acyclicity, not small inverse scores;
near-breakdown ratios must remain explicit; arbitrary Hres families have no
uniform second-order constant; pivot switching is outside PD-T143's frozen
selection theorem; zero errors rule out pathwise positive lower bounds;
full reorthogonalization does not imply exact spans; aggregate and scalar
source norms differ; subset upper bounds do not bound the full scalar graph;
an endpoint ratio below 100 cannot kill the unknown true ratio. Finite-u
aggregate guarantees do not establish actual IEEE error realizability.

## IDEA?lanczos-frontier-codex-L3a — Explicit-radius recurrence majorant

Aliases: nonasymptotic inverse-score transfer; quantitative pivot continuation.

- Question / scope: give the normalized inverse score a finite-u radius and
  an explicit quadratic remainder for aggregate residuals under exact full
  projection, at every fixed unisolvent degree.
- Mechanism and hypotheses: bound basis, projection, pivot and recurrence
  coefficient changes recursively from exact data; apply a Neumann inverse
  estimate and PD-T142. Local sources obey a stated finite-u norm bound,
  rather than only their derivative satisfying Hres.
- Closest entries (reading coverage qualified above): IDEA-251/252 and
  PD-T142/143; PD-T046's explicit
  non-breakdown factor; PD-N062 fixed-degree O(u) obstruction.
- Separation criterion: all constants and a positive radius depend only on
  represented exact data and local budgets, uniformly for nonsmooth and
  u-dependent admissible source choices. An unspecified compactness radius,
  a family-dependent C² norm, or a bound assuming coefficient closeness
  without deriving it erases the distinction.
- Literature baseline/limits: standard projection and inverse perturbation
  estimates; no claim that these ingredients are historically new.
- Obstructions escaped: strengthen Hres to a finite-u source inequality,
  retaining chi and positive pivots. Do not claim polynomial-in-degree scores.
- Gate verdict: variant with a quantitative uniformity distinction.
- Cheapest decisive test: prove a closed induction controlling pivot changes,
  then check every denominator and the u² coefficient symbolically.
- Pretest kill: a circular nonbreakdown hypothesis or dependence on unknown
  perturbed coefficients kills this exact-data certificate.
- Discriminability: the induction either supplies all radii explicitly or it
  does not; a numerical small-error example cannot replace this obligation.
- Actual result: analytic development, no experimental dependency; see L3.md.
- Disposition: deferred by G0 FAIL; unchecked candidate formulas retained.
- Canonical result: `PD-T?lanczos-frontier-codex-L3a`.

## IDEA?lanczos-frontier-codex-L3b — Finite decision-tree adaptive bound

Aliases: switching-safe aggregate selection; adaptive pivot without tie gap.

- Question / scope: extend a finite-u guarantee to adaptive choices, including
  exact ties, without pretending a perturbed run follows the frozen exact rule.
- Mechanism: enumerate the finite set of realized admissible selection
  sequences and take their explicit worst-case radius/bound. A pathwise run
  is one member of that set, even when it changes branch discontinuously.
- Closest entries: IDEA-151, IDEA-251 and PD-T143's explicit exclusion of
  perturbed pivot switching; PD-T054 excludes non-(C) choices only from its
  implicit-section conclusion, not from the span certificate.
- Separation criterion: quantifies over the actual adaptive policy's branches
  without a tie-margin hypothesis. Freezing choices at zero would kill it.
- Baseline/limits: elementary finite-union argument, potentially exponential
  cost; no efficient online or polynomial growth claim.
- Gate verdict: quantitative continuation of L3a; retain as a corollary, not a
  separate historical mechanism claim.
- Cheapest test/kill: check that each realized path has the same declared
  aggregate implementation and belongs to the enumerated set. An unenumerated
  parent operation or extra information injection lies outside the result.
- Actual result: analytic development only; see L3.md.
- Disposition: deferred by G0 FAIL; unchecked finite-union argument retained.

## IDEA?lanczos-frontier-codex-L4a — Positive-envelope spectral upper

Aliases: Perron scalar-graph upper; weighted row/Collatz certificate.

- Question / scope: settle the rotQ24 degree-12 factor-ten conjunct in the
  full frozen scalar-CGS2 graph, retaining the original INCONCLUSIVE test.
- Mechanism: keep every scalar source in rho, form the entrywise response
  envelope S_ki=sum_h |g_kh(z_i)|rho_hi and bound its squared spectral norm
  by max_i (Cv)_i/v_i, C_ij=sum_k S_ki S_kj/d_k, for rational v_i>0.
- Closest entries (reading coverage qualified above): IDEA-246/250,
  PD-T138/141, and PD-T139's aggregate
  row-bound improvement. The latter has a different input norm and cannot be
  substituted for this full scalar upper.
- Separation criterion: use the full scalar envelope with a rigorous spectral
  upper smaller than its Frobenius trace. A subset rho or a heuristic largest
  eigenvalue would erase the required distinction.
- Literature baseline/limits: ordinary nonnegative-matrix row scaling; no
  historical novelty claim.
- Obstructions: formal errors need not be IEEE attainable; preserving full
  rho avoids the subset-upper error. Failure of this upper to pass is only
  an inconclusive certificate, never a kill of the true factor-ten ratio.
- Verdict: quantitative certificate variant of IDEA-250.
- Cheapest test (preregistered before execution): v=1 exact row bound; then
  up to eight positive rational vectors proposed by power iteration or a
  shifted/scaled variant, followed by exact inequality checks.
- Pass: any rigorously checked U with 100U<G_R, using the existing exact BJ
  multinode gain G_R. Kill of the true comparison requires separate upper-BJ
  and lower-comparator evidence; a failed envelope is not such evidence.
- Discriminability: exact rational positive-vector inequalities certify a
  true upper for all frozen graph errors; their strict comparison with G_R
  decides the positive outcome without computing K exactly.
- Actual runs: none; G0 was pending at registration and subsequently failed.
- Disposition: deferred by G0 FAIL; no mathematical/certified result claimed.
- Canonical result: reserved provisional `PD-T?lanczos-frontier-codex-L4a`
  only if its exact checks and independent reproduction are completed.

## IDEA?lanczos-frontier-codex-L4b — Stronger BJ witness

Aliases: multiple-output scalar witness; improve beyond greedy target 90.

- Scope/mechanism: retain the full output matrix of the existing BJ node-sign
  witness; its spectral norm is at least the old target-column norm. If needed,
  search multiple output targets/sign patterns without altering the full graph.
- Closest: IDEA-250 already has target signs, greedy nodes and coherent-node
  full-output witnesses, PD-T138/141. This is a quantitative variant.
- Separation/kill: require a new exact attained gain, checked by direct
  projection. Merely reusing the old G_R or its float estimate is equivalent.
- Obstructions/limits: formal realizability only; failed lower searches cannot
  upper-bound K_BJ and cannot kill factor ten.
- Cheapest test: after L4a, inspect whether a new lower is necessary.
- Actual result/disposition: deferred until L4a's outcome; not run.

## Stop receipt — 2026-11-05

The orchestrator reported independent G0 FAIL: the prior E6 T24 n12 receipt
differs with the same identified inputs/code; BLAS sensitivity is demonstrated
but the historical discrepancy remains unexplained. The handoff's stop rule
therefore applies. No new experiment was executed by this worker. No theorem,
finite certified inequality or completed novelty gate is claimed. L3a/L3b are
unchecked candidate reductions; L4a/L4b are unexecuted preregistrations. All
development is deferred pending an explicit resolved G0 verdict and resumption
instruction. Required source reading also remains unfinished (including the
unmerged PR21 P3 comparison/addenda); no historical priority conclusion is
drawn from the preparation above.

## Handoff02 reading continuation — 2026-11-05 (G0 not yet cleared)

Rules reread at `f85c7b5c83822ff60b62c84bed1ec6ae31628422`:
AGENTS, WORKFLOW and CODEX; both frontier handoffs, and current plan/gates,
LOG/report/COLD_STORAGE and the two G0 summary/probe receipts. This is a
reading continuation only. No derivation, code or experiment was performed
in this continuation. The original candidate formulas preceded completion
of the prospective novelty gate; the timing deviation is retained and later
reading does not cure it. Claude must explicitly disposition that protocol
point during the later audit, as handoff02 requires.

The complete current `state/IDEAS.md` was now read, literally every line
1–889, in sequential bounded views: 1–52, 53–122, 123–288, 289–439,
440–516, 517–577, 578–630, 631–683, 684–763, 764–844 and 845–889.
This includes all headings, IDs, aliases, summaries, obstruction rows and
disposition tables. The scan includes the historical IDEA-127/130/134/140,
147/148/150/151 neighbors and all IDEA-246–267 entries. It is a current
coverage statement, not a claim that the original incomplete scan sufficed.

Completed full-source reads after the stop: PD-T136/137/139/140;
PD-N062/063; the complete ideas-e3-e4, ideas-e5 and ideas-e6 files; prior
plan, directions E2–E5, audits01–04 and responses01–03; PD-T144/145/146;
PD-T055, the commutator-shadow file (actually PD-T047), and the separate
reference-free-span-drift-lower-bound file (PD-T053). PD-T142/143/054,
ideas-e1 and the exact/scalar recurrence producers had already been read
fully in the first preparation. A combined directions E1/E5/E6 display was
truncated; E5 was reread alone and E1's tail reread, and no missing portion
is counted merely because its command ran.

The pinned PR21 copy `890f56ccde35431b70b43141c224b0b8817fea7f`
was consulted by read-only Git operations. P3 comparison and all three
Xu343/Xu342/Dunkl–Xu addenda were read in full. These are **PR21
(unmerged)** repository reading records; their reader's stated primary-page
coverage is not a new primary-fulltext read by this worker. P3 row15 treats
PD-T142/143 as numerical-selection statements distinct from exact-span
ordering remarks, and credits Barrio–Peña–Sauer Remark9 as closer prior art.
The Favard/truncated-converse distinctions in the addenda do not establish
a new selection-stability or scalar-capacity claim here. No historical
priority statement is added.

Exact shortlist outcomes, before any resumption:

| Saved candidate | Closest full entries and outcome | Applicable obstruction / scope |
|---|---|---|
| L3a | IDEA-251/252 and PD-T142/143: quantitative continuation, not a new inverse-score principle | PD-T143's remainder is particular-family dependent; a uniform finite-u result needs the stronger explicitly stated source budget, a noncircular pivot radius and derived coefficient control. (C) alone and omission of chi remain rejected. |
| L3b | IDEA-151/251, PD-T054/143: elementary finite-family continuation of L3a; no separate mechanism or efficiency claim | Frozen pivot choices have no switching guarantee; exact rotQ24 tie (2,1) prevents assuming a positive tie margin. No implicit-section conclusion for non-(C) paths. |
| L4a | IDEA-246/249/250 and PD-T136/137/138/139/140/141: quantitative upper-certificate variant | Aggregate Hilbert input and scalar l-infinity input differ; the full scalar rho must be retained. Spectral envelope must be proved, then certified with exact/outward arithmetic. A failed upper only fails the certificate. |
| L4b | IDEA-250 and PD-T138/140/141: already-recorded coherent/multinode witness mechanism, quantitative variant only | A stronger attained full-output witness must be checked by direct projection. Failure to improve a lower does not upper-bound the capacity. |

IDEA-253 is duplicate zero-error quantifier clarification, not a new PD-N;
PD-N062/IDEA-254 forbids exact/o(u) fixed-degree projection-only repair and
does not forbid an O(u) upper guarantee; IDEA-255's all-degree amplification
and IDEA-256's externally informed parent experiment stay outside these
candidates. PD-N063/IDEA-259–261 only reject their specified Padua witness
paths (fixed-A case eventual only), so they supply no L3/L4 obstruction.
IDEA-257/258/262 and IDEA-263–267 concern certificate radii, reading(E)/(G)
or implementation measurements; none supplies the missing finite-u or full
scalar comparison guarantee. No additional candidate was generated.

Outstanding mandatory read-first sources are still being completed;
therefore **the overall reading/gate-completion claim is still withheld**.
In particular this continuation has not yet completed the required broad
PD-T056–075 linked theory set, PROOF_STATUS ranges, track/drift README,
external-code/independent-checks, full G0 harness/manifest/source-audit read,
or the remaining literature-INDEX coverage. Mechanism terms and cheapest
tests remain those registered above; no new test ran while G0 was blocked.

## Reading completion for the saved L3/L4 routes — 2026-11-05

The orchestrator reports additive G0 RESOLVED, published at `684849d`, with
the original FAIL preserved. Read `g0-disposition-02.md` and
`independent-checks-g0-resolution.md` in full: the accepted explanation is
arithmetic sensitivity at the observed scales, not recovery of the unknown
historical rounding trajectory. This reading checkpoint performs no new
derivation, implementation, experiment or status promotion.

The previously outstanding broad read-first coverage is now complete:

- Prior drift directions E1 and E6 were reread separately in full, removing
  the earlier combined-output truncation gap. E2–E5, the prior plan/report,
  all four candidate files, audits01–04, responses01–03, external-code and
  independent-checks were read in full.
- All required `drift-codex-*` theory records PD-T136–146/PD-N062–063,
  PD-T055, and the named Claude300/302/304/305/309/316/319 and
  N301/N302/N303/N308 records were read in full. PD-T138 and PD-T141 were
  reread in full. The complete PD-T054 staircase proof and PD-T046's
  chi-explicit theorem/proof were read. The handoff's filename
  `commutator-shadow-recursion-and-span-drift-bound.md` is actually PD-T047;
  that file and the distinct PD-T053 reference-free bound were both read.
  PD-N013/015 were read in full. The historical neighboring IDEA entries
  127/130/134/140 and 147/148/150/151 were read in their complete linked
  candidate entries, including the pertinent correction/disposition text.
- Required PROOF_STATUS ranges were read in bounded untruncated ranges
  115–139 (N007–031), 140–165 (T029–054), 166–191 (T055–080), and
  238–251 (N062–063 and T136–146). This supplements the complete literal
  IDEAS1–889 coverage recorded above and the full IDEA246–267 linked entries.
- Track README and drift README were read in full. The frozen8359bf7
  drift README, `e6-provenance.json`, `e6-frozen-grids12.json`, and
  `checks/audit-02/E6.md` were read through read-only Git. Current
  `independent-checks-g0.md`, `code/g0_replay.py` and
  `evidence-manifest.json` were also read in full, as were the required
  summary/probe receipts and topic planning records.

L4 source-code coverage is exact: full `e1_exact.py`, `e1_cgs2.py`,
`e1_scalar.py`, `e1_cgs2_witness.py`, `e1_cgs2_multinode.py`,
`e1_sign_check.py`, `e1_reproduce.py`, `e1_cgs2_verify.py`,
`e1_verify.py`, `e1_fp.py`, `e1_scalar_finite_check.py`, and
`check_independent_scalar.py`. This covers the complete local rho, all
source-to-output propagation, old Frobenius upper, attained witnesses,
projection check, dual-gradient check, exact finite inequalities and the
receipt checker's trust limits. Directory inventory and README were
consulted for the remaining files. Unrelated E4/E5/E6 implementation files,
batch/integration utilities and the old trajectory-replay implementation
were not all reread; no full-directory-source claim or new execution is made.
The orchestrator explicitly scoped the implementation read to these
L4-required companions; broad theory/audit reading remains as listed above.

Literature INDEX metadata and the complete relevant rows LIT114/255,
241–243, 280–285 and 360–361 were consulted. The full stored records for
Barrio–Peña–Sauer, Paige–Van Dooren, Carpraux–Godunov–Kuznetsov, Hokanson,
Zhu–Nakatsukasa and Brubeck–Nakatsukasa–Trefethen, and the full earlier
L2-prior-art review, were read. The previously recorded pinned PR21
(unmerged) P3 comparison and all three addenda remain part of the gate.
Search terms were those in the original Gate and scope section, supplemented
by `Vandermonde`, `Arnoldi`, `Gram.Schmidt`, `rounding`, `Greenbaum`,
`Simon`, `Paige`, `Kuznetsov`, `Carpraux`, `Hokanson`, `Zhu`, `Nakatsukasa`,
`Hessenberg`, `Fischer`, `Dunkl`, `Favard` and `Xu` in the INDEX. An initial
broad INDEX search and a combined L2-candidates view exceeded output limits;
no unseen text from those views is counted. The exact relevant INDEX rows
and complete shortlisted candidate entries were subsequently read in bounded
views. This is consultation of the relevant INDEX scope, not a full literal
read of every unrelated literature row.

Outstanding external references remain explicit: no new original paper/PDF
was read. BPS's unread pages, ZN AppendixB/version/wording gaps, full
Paige–Van Dooren and Carpraux–Godunov–Kuznetsov, and the other missing
papers listed in the prior-art review are not closed by reading digests.
They are not proof premises of the proposed finite scalar certificate;
no new publication-priority claim is made. Standard positive-matrix and
spectral majorization ingredients are not claimed new.

**Gate conclusion for resumption:** the mandatory repository-source and
relaxed novelty reading for the saved L3a/L3b/L4a/L4b candidates is complete
within the exact scope above. The candidate table and obstruction outcomes
remain unchanged: L3a is a quantitative variant; L3b is its elementary
finite-path extension; L4a is a sharper-certificate variant; L4b is the
already recorded coherent/multinode witness mechanism. Repackaging existing
inverse scores, finite-family continuity or old witnesses is duplicate
content by itself. The original prospective timing deviation is **not
retroactively cured**, and Claude's explicit protocol disposition is still
required. L3 stays deferred this round. Following the orchestrator's
clearance, L4 may next verify the saved full-scalar reduction and obtain
exact/outward certified evidence with separately assigned medium-effort code
and a distinct independent check. No completed L4 result is asserted here.

## L4a analytic continuation after clearance — 2026-11-05

Root START followed the completed reading append. The finite reduction in
`theory/l4-envelope-bound.md` now proves the full scalar spectral-envelope
upper and its positive-vector certificates; the finite target stays OPEN
pending actual exact producer/independent evidence. It is a certificate
variant of IDEA250, not a new normal-quotient or selection mechanism.
The old INCONCLUSIVE result and all source-domain distinctions remain.
If the upper route is insufficient, an exact Rayleigh lower on its spectral
envelope can diagnose inability to pass with the fixed old BJ lower; that
diagnosis only concerns this certificate route. It is not a negative theorem
about the actual scalar ratio. No new envelope computation result had been
received when this continuation was written.

## L4a failure retained; L4b cheapest continuation — 2026-11-05

The exact full-envelope producer reproduced the old trace but all nine
allowed positive-vector uppers failed the threshold with the old BJ lower.
Best integer B=13462956266, proposal3; target remains OPEN and the new
certificate outcome is INCONCLUSIVE. All failed candidates are retained
externally with hashes in `evidence/l4-envelope.json`; independent checking
is separate. A possible exact Rayleigh diagnostic concerns only the
envelope combined with that fixed old lower.

Root next authorized L4b using the **same** frozen target90 BJ node and
operation signs. Its complete prospective test is now in `attempts/L4.md`:
reproduce G_R, construct every output response, then certify exact projected
monic-combination gains from at most three quantizations of one floating
leading singular-vector proposal. Acceptance is strict squared gain
greater than1346295626600, with the alternating upper independently checked.
There is no new delta sign search and no inference of a target kill from
failure. This remains a quantitative variant of IDEA250/PD-T138/141,
covered by the completed reading gate and its retained protocol qualification.

## L4a fixed-old-lower subroute — scoped diagnostic gate

After all nine original upper tests failed, root authorized a separately
labeled post hoc exact Rayleigh diagnostic from their retained envelope and
vectors, without regenerating sources. This concerns the already registered
L4a method, not a new mechanism: closest full entries are IDEA250 and
PD-T138/140/141, plus the written L4a spectral reduction. It asks whether
even the best possible upper of this **unprojected absolute envelope C**
could pass with the **fixed inherited** BJ lower G_R. It does not ask for
an upper on true K_BJ or a lower on true K_alt. The cheapest exact test is
a rational v with `100(v^T C v)/(v^T v)>=G_R`. A positive finding excludes
all envelope spectral uppers paired with this fixed lower; a negative
finding leaves the method undecided. No new historical priority or new
source model is involved. All original candidate timing qualifications stay.

Root reports floor-Rayleigh13462955378 at the retained best/final vectors;
durable diagnostic/checker evidence is still pending here. A separate
provisional scoped record `PD-N?lanczos-frontier-codex-L4-01` is authorized
for the exact negative mathematical statement, with no PROVED status until
the actual independent finite check is complete. The overall target remains
OPEN and L4b's stronger lower may still make the useful envelope upper pass.

## L4b producer passes, independent check pending — 2026-11-05

The first preregistered full-output readout quantization10^6 reports
`floor Q=2041704913997 > 100*13462956266`, with the same old target90
node/operation-sign witness and exact old target-column reproduction.
No later proposal or new sign search ran. This is a quantitative full-output
witness extension of IDEA250, not a new source model. Independent
regeneration/checking remains pending before finite theorem acceptance.
The original PD-T140 INCONCLUSIVE experiment and fixed-old-lower subroute
obstruction remain separate and unchanged.

## Final L4 dispositions — 2026-11-05

- L4a with the fixed old BJ lower: all nine upper tests failed. The
  separate exact post hoc Rayleigh certificate proves that **every** upper
  of this same absolute-envelope spectral value fails when paired with
  that fixed old lower. This scoped subroute is REJECTED:failed under
  `PD-N?lanczos-frontier-codex-L4-01`, finite computer-assisted PROVED.
  The useful envelope upper is retained for stronger lowers.
- L4b, same frozen signs and complete output: the first preregistered
  quantization10^6 passes, with the fixed integer readout independently
  checked. Final endpoints L=2041704913997 and B=13462956266 satisfy
  `L>100B=1346295626600`. Provisional
  `PD-T?lanczos-frontier-codex-L4a` is PROVED as a finite computer-assisted
  statement on the full PD-T138 graph at rotQ24 degree12, including the
  stronger named-alt comparison and hence the original minimum-comparator
  target. No second/third proposal or new error-sign search ran.

The final independent source/receipt pins and all13 rejected malformed
controls are recorded in the theory and attempt files. The accepted
91-integer readout is essential compact evidence; regenerated floating
proposals are not proof premises. This is a quantitative certificate
variant of IDEA250, not a new normal-map or selection mechanism. The old
PD-T140 MEASURED/INCONCLUSIVE experiment stays unchanged. L3 is deferred;
no actual IEEE, finite-u or all-degree statement is made. The original
prospective novelty-gate timing deviation and Claude's still-pending
explicit protocol disposition are preserved. No Git, shared-registry or
handoff mutations were made by this worker.
