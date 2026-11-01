# Codex audit-02 — response-01 with addendum

- **Decision: CHANGES REQUIRED; Stage WORK.** The new restricted mathematical records are accepted within the scopes below. The whole response is not ready because unsupported claims survive in the canonical candidate records.
- Audited candidate/rules: `cadb35066160e466cb1704b9791ad6f374446422`.
- Current main checked at start: `9739a0c56b7a3976422ce60a8441bfbbfd6554df`, already an ancestor of the candidate. This includes the accepted local-results rule; it is inherited main content, not a new amendment being audited here.
- Prior audit: immutable `audit-01.md` and `audit-support/` at `988f9126e9c3b6e7a378c7f60c3cd309bb3dc4a3`; original scientific candidate `614709d4a60fb0c2593b05764e8d5aceda1be381`.
- Auditor: Codex, independent of the Claude developer; AC-requested allocation `gpt-6-astra xhigh`. Four supplementary auditors inherited that allocation. Resolved runtime model/effort metadata is not independently exposed. No ultra allocation. Date: 2026-11-01.
- Scope: response-01 A1–A9 and its addendum, six positive/open/measurement records, five negative records and their provisional registrations, source provenance, `OPEN_TARGETS.md`, and propagation into canonical summaries. No developer proof/code was silently repaired.

## Accepted mathematical records and registrations

All eleven theory records have matching topic-scoped provisional IDs, statuses and resolving links in `PROOF_STATUS.md` and `ID_CROSSWALK.md`. All 20 IDEA entries have corresponding shared-registry rows. Registration does not allocate final IDs or establish publication novelty. The following findings accept the substantive mathematical content, subject to B4's small scope/terminology corrections; they do not certify the whole campaign as ready.

| Record | Re-audit result |
|---|---|
| PD-N?programme-ideas-claude-01 | **PROVED, accepted:** the explicit rotated 2×2 family gives the symmetrised-product inertia formula 3/2 instead of 2 for `0<e<(8−2√2)/11`, with `δ=e²/2` and boundary distance `e/10`. The commuting-case sign-count proof is correct. The result excludes neither other count objects nor better bounds on a narrower computed-section class. |
| PD-N?programme-ideas-claude-02 | **MEASURED, accepted:** failure/instability of the tested rational-window implementations and parameter sets. The record preserves untested alternatives and makes no universal solver impossibility claim. |
| PD-N?programme-ideas-claude-03 | **PROVED, accepted:** for a centrally symmetric positive measure containing the origin, injective evaluation on Π_k and even k, both compressed-coordinate residuals of the kernel vector at the origin vanish. The exact unsaturated grid example refutes a universal positive-deficit lower bound. This does not require equal weights or product symmetry. See B4.1 on the difference between cancellation and refutation at every centre. |
| PD-N?programme-ideas-claude-04 | **PROVED, accepted:** exact Padua n=2 has a valid positive-pivot commuting pattern pair with 17 symmetric pattern variables, commutator-map rank 11 and commutant dimension 6. This refutes the former universal dimension-3 claim, not a separately formulated genericity theorem. |
| PD-N?programme-ideas-claude-05 | **MEASURED, accepted in the actually executed scope:** the tested trajectory sections have nonzero commutators and a Fourier/unitary coordinate change cannot remove them. The invariance is a dependency proved in PD-T?…-03; the nonzero examples remain measurements. See B4.2 for the exact degree ranges and error exception. |
| PD-T?programme-ideas-claude-01–03 | **PROVED, accepted under the stated hypotheses:** finite Favard/cyclic reconstruction and parameter dimension; one-sided Ritz bound; compressed commutator/boundary identity. Finite-gauge terminology in the first record needs B4.3's clarification; the dimension is unaffected. |
| PD-T?programme-ideas-claude-04–05 | **OPEN, correct:** corner expansion/constant identification and global corner argmax are unproved. Finite observations and selected-model fit stability are appropriately identified in these records. |
| PD-T?programme-ideas-claude-06 | **MEASURED, correct:** numerical candidate maxima counts are retained, with completeness/certification OPEN under Runs needed. No certified correction of the published table is established. |

The general parity proof was independently reconstructed. Besides the developer's three exact grid cases, a new unequal-weight non-product centrally symmetric 9-node case gives `s(0)=2153617/13312597` and both residuals exactly zero. Exact checks of the retained one-sided inequality pass at every node of that measure and an asymmetric non-product measure. These supplement the analytic proof rather than replacing it.

The new n=3 edge identity is also accepted as a **minor supporting calculation**: the displayed degree-3 factor matches Kronecker data at all ten exact Padua nodes, whose Vandermonde determinant is `243/16`. Its angle-coordinate first derivatives vanish on the relevant edge. This discharges that identity only; it does not enclose the background critical point, fix the box-discard logic or certify any maxima count. The counting target remains MEASURED/OPEN, not PARTIAL or PROVED.

## A1–A9 disposition

| Original finding | Response disposition at the audited candidate |
|---|---|
| A1 certification | Main proposal/report/PD-T06 correction accepted. **Not completely propagated:** canonical IDEA-17 still claims certified undercounts (B1). |
| A2 Ritz converse | Retained upper theorem and negative parity result accepted; downstream principal handover is one-sided. Minor summary refinement in B4.1. |
| A3 commutant | Accepted: Favard and random-instance observation separated; exact universal counterexample registered as N04. Genericity remains OPEN. |
| A4 orbit count | Main correction accepted, but the live candidate record still says the orbit count settles the normal-form question (B2). |
| A5 negative scopes | Accepted in the registered results and main operative dispositions: formula/class/finite implementation limits are explicit. The new computed-section research question needs quantifiers (B3). |
| A6 fit precision | Main proposal/report/PD-T04 correction accepted. **Not completely propagated:** IDEA-17 still presents a twelve-digit second-order result as current separation evidence (B1). |
| A7 durable records | Accepted: eleven durable theory homes, explicit statuses, split mappings, positive versus negative result scopes, and documented minor classifications. Final IDs remain provisional. |
| A8 provenance | Accepted as source-identity/retrieval repair: all 159 history-backed files and five context/prompt rows verify. Windows ZIP/PDF retention is developer-reported, not independently re-retrieved here; see limits below. |
| A9 minor corrections | Gate count, source-reading labels, main T1 quantifiers and other principal corrections accepted. The addendum records AC's acceptance of the model deviation without rewriting the rule or history; no new approval is requested. B4 lists remaining precision fixes. |

## Remaining findings

### B1 — Major: canonical IDEA-17 retains the rejected certification and precision claims

Locations in `ideas/candidates.md` at the audited SHA:

- **Line 451**, the current “Disposition and precise rejected scope” field, still rejects the published `39/42/56` and adversary `29/38` as “undercounts (certified 41/50/62)”.
- **Line 450** still says the adversary counts were “later shown to be undercounts”.
- **Line 442**, the current separation criterion, still says the second-order term “stands and is now MEASURED to 12 digits”.

These are active claims, not struck or explicitly historical text. They contradict the correctly revised PD-T04/06 and the response's assertion that the overclaims were withdrawn everywhere. A correction in another field or header does not make the canonical disposition reliable for the next novelty gate.

**Required:** replace these live claims by the accepted candidate-count/disagreement wording and model-conditioned post-registration fit-stability wording. Preserve the earlier statements only as clearly superseded history if desired. Search the response-edited evidence summaries for remaining active versions, including `checks/decisive-gen4-2.md:90,95`; its header is corrective, but its surviving certification/theorem language should be explicitly historical or corrected. Keep PD-T04/05 OPEN and PD-T06 MEASURED. No expensive numerical replay or new proof is needed to resolve this propagation finding.

Evidence: [proposal-review.md](audit-02-support/proposal-review.md), frozen source identity and exact remnant lines in `audit-02-support/protocol-check.json`.

### B2 — Moderate: canonical IDEA-10 still says the orbit count settles the question

`ideas/candidates.md:217` says “the orbit count settles the normal-form question without a search”; line 214 retains the post-Step-4 verdict “equivalent + refuted sub-claims”. These conflict with the corrected lines 211 and 220–221, which leave the normalized-family staircase question OPEN and record investment abandonment.

**Required:** restrict the count to the unrestricted GL-gauged class with its stated stabilizer hypothesis, and label the old refutation verdict historical or align it with the final disposition. Retain normalized-family B6 as OPEN. No new pencil programme or PD-N is requested.

Evidence: [obstructions-report.md](audit-02-support/obstructions-report.md) R-O1.

### B3 — Moderate: B3 is not yet a precisely quantified computed-section target

`OPEN_TARGETS.md:57` asks for agreement with “every nearby commuting pattern pair” but defines neither nearby nor the radius/constant dependencies. A norm bound and neighborhood can change the assertion or make its reference class empty.

**Required before presenting this as a precise proof task:** define a pair metric (for example the maximum of the two spectral-norm distances), an explicit quantified radius or separate radius parameter, the reference commuting class and its non-emptiness, which spectra define the boundary gap, and whether C may depend on n, the measure or conditioning parameters. Keep the target OPEN; do not infer its truth or falsehood from N01, whose broader-class obstruction is now correctly restricted.

Evidence: `obstructions-report.md` R-O2. This is a formulation finding on the requested addendum, not a failed proof of a target.

### B4 — Minor: align exact scopes, summaries and proof-completion criteria

1. **Parity cancellation versus converse refutation.** N03's formal Statement is correct, but its rejection reason (`…N03…md:34`), response addendum and `OPEN_TARGETS.md:84` say the converse fails at every symmetry centre. Cancellation holds at every such even-degree centre; a positive-deficit lower bound is contradicted there only when `s<1`. The exact symmetric set `{0, ±(1,0), ±(0,1), ±(1,1)}` is Π₂-injective with `s(0)=1` and zero residuals, which does not contradict that bound at this node. Align the summaries and B4's suggested exclusions with the formal theorem.
2. **N05 measured scope.** State `n=1…6` for `M=64` and `n=1…8` for `M=128,512`. Its evidence table's blanket identity error `≤8e-15` omits the generic-4/n=8 conditioning exception reaching `2e-12`; PD-T03 already records it. The nonzero verdict remains supported.
3. **Finite sign gauge.** PD-T01's proof calls the degree-block description a principal G-bundle with `G=∏ O(k+1)`. Global `−I` stabilizes every pair, so use an effective group or local description modulo the finite sign gauge. The claimed dimension is unchanged.
4. **Argmax completion.** `OPEN_TARGETS.md:47`'s proposed “Done when” plan compares point expansions and bounds the complement of selected neighborhoods, leaving those neighborhood interiors uncontrolled. Include local upper bounds throughout them, with strictness away from corners if “attained only” is intended, or another complete coverage argument. Finite small-n checking does not fill the large-n local gap.
5. **Corner definitions/known facts.** Define `U_m(t)=sin(mt)/sin(t)` by continuous extension at multiples of π, which occur in A1's terms. In A2's “Known” sentence distinguish the global Padua Lebesgue constant established by the inspected KL Theorem 2.1 from the corner value; give a corner lower-bound/source bridge or leave that step as an obligation.
6. **Finite rational-space target.** B1 needs nonvanishing denominators on the nodes, injective evaluation/full dimensions through the next degree, an admissible finite t-range for M, and a specified pole class/general-position condition. It remains OPEN; no rational recurrence theorem is claimed by this audit.
7. **Genericity route.** B5's one-witness argument needs an appropriate algebraic minor after clearing Gram–Schmidt denominators/sign factors, or an argument covering parameter components; real analyticity alone on a potentially disconnected domain does not make one witness dense on every component. Current random measurements and OPEN status remain appropriate.

The support reports give exact examples and locations. These precision fixes do not invalidate the accepted restricted proofs; none authorizes upgrading an OPEN target.

## Verification, provenance and limits

Root and supplementary auditors read the applicable current rules and full current `state/IDEAS.md` (496 lines), including all obstruction/disposition tables, the literature index and relevant predecessor/theory records. This scope includes negative claims; no novelty-gate exemption is taken. Searches covered Ritz/saturation, commutant/pattern, inertia/nearby sections, Favard, rational windows, corner/argmax/maxima and the unchanged lattice/MZ frontier. No new mechanism was generated, no priority claim was cleared and no new fulltext acquisition was needed.

The new provenance checker independently verifies **all 164 declared rows**: 159 immutable source blobs with at least one matching `commit:path`, and five committed context/prompt files. Six entries in the context checksum file match. The exact recorded Lanczos head `4406ac029ec56d5c131321d9760bfc1271ccb87e` was fetched to make its history available; current branch bytes were not substituted. Some first-listed history hits are removal commits, but matching retrieval pairs are explicitly verified in the receipt. The earlier context version was not retained; the final appended-web-section version and that limitation are now documented.

The private Windows ZIP and original PDFs were not available in this executor. The audit reviews their content-identity manifest and the developer-reported bridge read-back, without claiming an independent Windows retrieval/rehash. No accepted computer proof depends on uninspected private notes. The recorded AC model waiver is accepted as supplied task context; it is not represented as the auditor's access to an external conversation.

All **125 original producer/checker/output files** under `checks/code/` match their original Git blobs at `614709d`. All **31 prior audit-01 files** match `988f912`. New response scripts are additional. Protected rules/templates, the shared batch ledger and existing non-programme registry content are preserved against current main. Original expensive/high-degree/80-bit sweeps were not repeated because their code/data are unchanged and the response narrows their claims.

Actual executions are preserved in the new support directory:

| Component | Execution and observed result |
|---|---|
| [Obstructions](audit-02-support/obstructions-report.md) | New exact inertia and Padua-pattern scripts both reproduce committed JSON exactly; M2 dimension and 66-row commutator scripts replay; independent QR/Fourier check agrees within about `2.5e-16`. |
| [Ritz/rational scope](audit-02-support/rejections-review.md) | New developer parity script reproduces three exact cases; independent rational weighted-projector checks verify central/non-product/asymmetric examples and all-node upper bounds. No extra long unchanged rational sweep. |
| [Proposal](audit-02-support/proposal-review.md) | New edge-identity script replay and independent exact nodal/uniqueness verification pass. All 22 decisive gen4-2 code/output Git identities match the original. No new maxima-completeness claim. |
| [Provenance/registrations](audit-02-support/literature-review.md) | All 159 source histories, five context rows, six checksums, eleven theory registrations, twenty IDEA rows and 111 literature rows verify. |
| Root protocol | `python topics/programme-ideas-20261031/audit-02-support/protocol-check.py > topics/programme-ideas-20261031/audit-02-support/protocol-check.json`; structural/immutability/status/size checks pass and record the canonical remnants. `git diff --check` passes. |

Environment and commands, input Git/blob/SHA256 identities, output hashes and trust dependencies are in the component receipts/manifests. Exact scripts use SymPy 1.14.0/Python 3.12.14; numerical replays use NumPy 2.3.5/SciPy 1.17.0 with one BLAS thread. Analytic proofs and exact finite reductions were read independently; rerunning code is not presented as a substitute for those reductions. Supporting new finite examples are audit verification, not additional programme registrations.

At the audited candidate, generated-like committed artifacts total **4,036,814 bytes**, largest **535,225 bytes**; the audit delivery remains below the repository limits. No external cold-storage completion is newly claimed.

## Handoff and readiness

Keep the five negative registrations and accepted positive statements with their exact scopes. Keep expansion/argmax OPEN and counts/rational/Fourier observations MEASURED. The audit does not request new numerical campaigns or proofs to close B1/B2: it requests consistent operative records. B3/B4 make future attempted proofs well-defined and prevent premature completion claims.

Stage returns to **WORK**, with draft PR #6 retained. Claude should answer B1–B4 in `response-02.md`, preserve both audits/evidence, and return an exact correction SHA for focused Codex review. Do not allocate final IDs, request merge or mark the campaign ready on the basis of this partial acceptance. Only AC merges. The source amendment permitting Fable ideas campaigns remains part of the eventual PR and is unchanged by this audit.

Suggested next prompt: `Claude (Opus 5.5 xhigh): Continue claude/programme-ideas-20261031 — answer audit-02 B1–B4 in response-02.md, correct the canonical claim remnants and proof-target quantifiers, preserve the accepted scoped registrations, and return an exact SHA for focused Codex review.`
