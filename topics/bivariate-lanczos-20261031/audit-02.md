# Codex audit-02 — focused re-audit of response-01 and its impact map

Date: 2026-11-01 (Europe/Oslo). Scientific candidate: **`075d4074017445a0fd4d7443ffac97cd7f8c106b`**. Published response/rules head: `50b0d304001b48607527e5086a67045f534d9472`. Prior audit publication: `5f523313b7b388cb114103734028f0a850dfeaad`. Fetched main: `0d058fb410166bd97b178be57910f2d256d0b529`.

Independent Codex audit orchestrator and five continuing audit workers, separate from the Claude developers. Workers retain their explicit `gpt-6-astra`, `xhigh` launch configuration; runtime model/effort is not independently exposed. Root runtime identity is separately unexposed. Only the root controls Git. The auditors change no developer theory, experiment source, response or historical audit record.

## Verdict

**CHANGES REQUIRED — four new low-severity qualifications; return to WORK.** The original audit-01 scientific findings are resolved within the focused scope, including the normalization counterexample, missing beta factors, overbroad statements, substantive status splits and evidence interpretation. The two new proofs, **T209's staircase/acyclicity theorem** and **T318's first-order commutator formula and rank reduction**, withstand independent reconstruction and new checks. No new high- or medium-severity finding was identified.

The remaining corrections below qualify a conditional bound, a zero-operator quotient, a numerical-error aside and an evidence label. They do not overturn the surviving exact theorems, the scoped measured failures, or the newly checked proofs. Preserve those statuses. This is not a clean overall/readiness verdict until the four low findings have developer dispositions.

## Dispositions and coverage

| Scope | Prior finding disposition | Focused report |
|---|---|---|
| L1/L4 | F1/F2/S1 and LL-M1/M2/L1/L2 resolved, including technical reconstruction notes; one new T116 qualification | [L1](audit-02/L1.md) |
| L2 | Original F1–F5 resolved; T201 corrected corollary and new T209 proof confirmed; two new T208 qualifications | [L2](audit-02/L2.md) |
| L3 residual conventions | LF-M1 resolved; T302(b1)–(b4), explicit N309 radius and rate propagations verified; clean in scope | [L3 conventions](audit-02/L3-conventions.md) |
| L3 formula, splits and scope | LF-M2, LC-M1/LC-L1 and report-scope findings resolved; new T318 confirmed, T316/T319 remain OPEN; one new evidence-label correction | [L3 formula/scope](audit-02/L3-formula-scope.md) |
| L5 | M1/M2/L1/L2 resolved; paired statistics and interpretation verified; clean in scope | [L5](audit-02/L5.md) |
| Protocol and impact map | Declared theory inventory complete and correct; frozen evidence preserved; preparation obligations explicitly deferred | [protocol](audit-02/protocol.md), [impact result](audit-02/impact-check.json) |

The direction reports contain item-by-item dispositions, proof reconstructions, actual commands, source/output identities and coverage limits. Original broad numerical/certificate suites are reused only where their code/evidence bytes are unchanged. The prior full IDEAS/INDEX reads are reused after exact identity checks; no fresh literature-priority claim is made.

## Required low-severity corrections

### A2-L1 — T116's univariate denominator needs its stronger hypothesis

Source: `tracks/bivariate-lanczos/theory/product-measure-computed-propagator-transfer-conditional.md:19`. Detailed finding: **L1-A2-L1**.

The hypothesis is `kappa*delta << 1`, which permits the Neumann bound `kappa/(1-kappa*delta)`. The concluding bound using `B/(1-B*delta)` additionally needs **`B*delta<1`**; `kappa<=B` does not supply that condition. Exact coefficient-level examples give arbitrarily small `kappa*delta` while `B*delta>1`, making the asserted B-bound negative. They are not claimed to be executions of a floating-point recurrence.

Qualify that concluding sentence by `B*delta<1` (or the stronger sufficient form already named), or use the valid `B/(1-kappa*delta)` bound under the existing hypothesis. Keep T116 CONDITIONAL and its correct Neumann inequalities intact. No large experiment is required.

### A2-L2 — T208's normalized defect needs a zero-operator convention

Source: `tracks/bivariate-lanczos/theory/reference-free-span-drift-lower-bound.md:14`. Detailed finding: **L2-02-L1**.

Part(a) deliberately drops unisolvence and allows `A=0`; its inequality `delta_A <= ||A||(theta_s+theta_(s+1))` remains valid, while the following quotient is `0/0`. Restrict that quotient to `||A||>0`, or define a zero operator's normalized contribution to be zero. Preserve the universal unnormalized inequality and maximum-over-stages reading. The intended unisolvent applications are unaffected.

### A2-L3 — T208's numerical projector-error aside needs a conditioning premise

Source: the same file, line18. Detailed finding: **L2-02-L2**.

Backward-stable QR of a full-rank input does not alone give a condition-free forward bound on its original column-space projector. The `O(u||A||)`/negligible-error aside needs well-conditioned or near-orthonormal input prefixes, or an explicit conditioning factor. Restrict the comment to the tested prefixes, or state the necessary conditioning dependence; no new certified computation is demanded. The exact projector inequality and previously verified drift evidence remain valid.

### A2-L4 — T318's perturbed-functional check does not establish nonrepresentability

Sources: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-318-first-order-commutator-formula.md:36` and `:47`; its checker at `tracks/bivariate-lanczos/code/L3/t318_dkappa_formula_check.py:173` and `:191`. Detailed finding: **LC2-L1**.

The checker creates a perturbed functional with positive-definite moment matrix but supplies no test excluding positive-measure representations on a stated support. Replace “non-measure functional” by “arbitrary perturbed functional” or “not constructed from an explicit measure.” T318(a) is proved for the full stated class and does not need nonrepresentability; retain its PROVED status and existing evidence.

Optional editorial notes, not additional mathematical blockers: use explicit maximum-over-stages notation for report.md's bare theta shorthand; change the L5 analysis docstring's size range from 5–7 to 4–7; the L3 section-data clause may explicitly repeat Phi's positive-moment-matrix domain. The relevant subreports already distinguish these from required findings.

## Verification actually performed

- **Impact map:** all 65 declared changed/new theory files match the candidate hashes and actual diff; ten are new and 12 original files unchanged, 77 total. All audit-01 artifact identities match. Existing producer code is unchanged; eight response checker/analysis additions are accounted for. The publication delta includes LOG and the response's self-SHA sentence; it was inspected as metadata-only rather than assumed to be literally LOG-only.
- **L1/L4:** both new developer checkers executed successfully. Independent exact stored-data reanalysis confirms N101's corrected range and absence of a factor-3 prediction on all 550/570 informative triples under the two roundoff conventions. The unchanged broad recurrence/certificate suites were not repeated.
- **L2:** new staircase proof reconstructed for all degrees; separate exact forward dependency enumeration checks all selections through n=6 and every staircase through n=14 with maximal predecessor windows. Corrected normalization runs reproduce bitwise old-ld controls on eight sets, finite chi maximum 5.2798957836, and the strict 10/12 versus registered 11/12 distinction. These measurements do not become general conditioning bounds.
- **L3 conventions:** fresh developer check is byte-identical to its output. An independent exact checker reconstructs full-cone/fixed-mass thresholds, normalization factors and N309's strict separation for every radius in `[0,10^-8]`. General proofs were checked separately from these finite examples.
- **L3 formula:** fresh six-case numerical checks reproduce the reported derivatives/ranks. A separate exact rational checker verifies all moment directions, arbitrary masses, moving-basis cancellation, row spaces and ranks for n=1–3, plus the finite Hankel basis through n=8. Its first slow symbolic-rank attempt was interrupted and is disclosed; exact DomainMatrix elimination completed the final checker. The all-n theorem rests on the analytic proof, not enumeration.
- **L5:** new analysis output is byte-identical; an independent centered-sums calculation verifies 66 paired estimates/intervals, 27 table triples, Householder invariance, and checkpoint trends. No unchanged C experiment was repeated.

The source/output manifests in the scope reports record versions, seeds, arithmetic, sizes and actual completion. Numerical observations remain MEASURED. The final audit artifact manifest separately records the small retained audit envelope and checks the cumulative output cap. No external archive/fulltext was newly retrieved, no new independent historical timestamp is claimed, and no unexecuted large-M run is reported as complete.

## Handoff and readiness boundary

Claude should address A2-L1–A2-L4 in `response-02.md`, preserving the frozen audits, proofs, accepted response dispositions and statuses. Record the narrow changed-file hashes and any propagation. The subsequent check can remain limited to those edits; unchanged broad suites need not be rerun.

Canonical source consolidation, main integration, shared-registry/batch-owner coordination, final IDs/crosswalk, rehearsal and PR-preparation checks remain as explicitly deferred obligations. No ready-to-merge conclusion or GitHub merge is authorized by this audit.

Suggested next prompt: `Claude (Opus 5.5 xhigh): Continue claude/bivariate-lanczos-20261031; address audit-02.md A2-L1–A2-L4 in response-02.md, preserve the verified proofs/statuses and frozen audit records, and return the narrow impact map for Codex verification.`
