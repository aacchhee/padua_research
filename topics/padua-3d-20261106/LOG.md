# Padua-type points in three dimensions: log

- Branch: `codex/padua-3d-20261106` · Base: main `76ba421` · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: AUDIT · Next: Claude Opus5.5 xhigh · Successor at publication: [handoffs/07-audit.md](handoffs/07-audit.md)
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims: provisional records in [report.md](report.md); no final IDs allocated.

## 2026-11-06 — Claude, claude-opus-5-5 (configured; effort not exposed) — topic setup

- AC asked what is known about 3-D Padua. Claude summarized it and noted that earlier campaign-scoping documents had marked "3D Padua" out of scope (IDEA-120, IDEA-013).
- AC: "I do not remember ruling this out of scope, I guess it applied to one specific fact. Make a proper adventurous reasoning topic on 3D, write what you know and what you expect. Allow Astra Ultra when necessary, 25 rounds, otherwise usual rules".
- **3-D Padua is in scope for this topic by AC's instruction.**
- Claude wrote [BRIEF.md](BRIEF.md) and handoff 01:
  - BRIEF: the knowledge base, how the 2-D mechanism breaks in 3-D, the repository's 3-D results, expectations E1–E6 and a literature list.
  - Handoff: T1 obstruction theory, T2 aliasing-designed positive constructions, T3 proofs, T4 a proved Radon-stack baseline, T5 cubature non-existence and joint spectra (bounded), T6 Lebesgue lower bounds (bounded); gates D0–D4.
- Budget: 25 rounds per direction (Claude's reading of "25 rounds"; AC may correct it), with T5/T6 capped at 8.
- Models: Astra ultra allowed when necessary; coordinator Astra high; Sol for easier jobs.
- Rules read at `76ba421`. Branch created from main `76ba421`. No computation was run and no claim made.

## Runs needed

- D0–D4 and T1–T6 as in handoff 01.

## 2026-11-06 — Codex, gpt-6-astra high — continuation initialization

- Role: orchestrator/developer, AC's explicit model selection retained.
- Rules read in full at input head `ccd9e905d19c0c625c196c4a3f3e707058ed042a`:
  AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md.
- Fetched main `76ba4214b100c86a44941f5e9a662ce9ce48efb8` and requested topic
  head. Main is an ancestor; no reconciliation commit is necessary.
- Read BRIEF and open handoff 01. Its explicit parallel-worker instruction
  authorizes delegation. Coordinator scope is [plan.md](plan.md), written
  before research execution; [round ledger](rounds.md), [gates](gates.md).
- D0 reproduction adds no novel content. New mechanisms remain gated on D0
  and the full repository predecessor scan. No final ranges needed yet.

## 2026-11-06 — replay round 1 and research launch

- Bounded replay developer: Codex, assigned gpt-6.1-sol medium; resolved runtime
  metadata is not independently exposed. [D0/D1 both PASS](replay-notes.md).
  Exact counts, normalized symbolic determinant, modular rank controls and
  all four 2-D corner identities reproduced. Two PD-N037 fibre/baseline rows
  match all six historical binary floating values exactly. Compact receipt
  records input hashes, versions and commands; historical artifacts were
  recovered read-only from a pinned pushed Git commit.
- After clearance, launched T1–T6 with disjoint files as requested. T2 code
  developer uses assigned gpt-6.1-sol medium; T1/T3/T4/T5/T6 mathematical
  developers use assigned gpt-6.1-sol xhigh. The coordinator retains Astra high.
  Workers do not control Git or shared records. A supplementary distinct-agent
  reconstruction and Claude's substantive audit remain separate obligations.
- Opened draft [PR #33](https://github.com/aacchhee/padua_research/pull/33),
  audit PENDING, with no IDs reserved and no shared-registry edits.

## 2026-11-06 — first mathematical checkpoint

Coordinator Codex, assigned gpt-6-astra high; mathematical workers assigned
gpt-6.1-sol xhigh, T2 screen worker gpt-6.1-sol medium. Runtime model metadata
is not independently exposed. No Astra-ultra escalation has been needed.

- T1 round 1: elementary binary-code classification and a hand proof excluding
  a **single coordinate-reflection-invariant whole coset** at minimal node
  count for every n>=2. [Classification](theory/t1-reflection-classification.md),
  [scoped obstruction](theory/t1-minimal-obstruction.md). Developer PROVED;
  D3 enumeration and supplementary independent review still in progress.
  The original unrestricted C_k target remains OPEN.
- T2 round 1: three frozen cyclic formulas fail at n=2 by explicit quadratic
  annihilators, [scoped proof](theory/t2-cyclic-screen.md). Round 2: complete
  normalized generator census at n=2,3,4 finds 4,0,4 full-rank cases; all
  eight finite survivors lose to same-degree controls on the frozen mesh.
  [Attempt](attempts/T2.md). Exact computations remain conservatively MEASURED
  until a separate replay of the committed cover; no D2-promising family.
- T3 round 1: [exact cyclic rank reduction](theory/t3-cyclic-rank.md) and
  [short-relation annihilators](theory/t3-short-relations.md), developer PROVED
  analytic prerequisites. [Whole order-39 exclusion](theory/t3-degree3-extension.md)
  is CONDITIONAL on the separately checked H39 finite cover. Survivor-dependent
  T3 remains blocked on D2, not PARTIAL.
- T4 round 1: all-n stack unisolvence, exact determinant height factor, and
  a [monotone-order exponential lower bound](theory/t4-monotone-lower.md),
  developer PROVED. This contradicts the polynomial expectation only for
  the specified monotone ordering. Other orderings and actual numerical
  diagnostics remain in progress.
- T5 round 1: D4 passed by exact known degree-five cubature controls before
  any nonexistence claim; [code](code/t5_exact.py), [receipt](evidence/t5-exact.json).
  The fixed-grid sharp support theorem is being written separately.
- T6: explicit universal logarithmic-cubed lower-bound proof is being written;
  not included as a completed result in this checkpoint.
- This is an honestly unfinished development checkpoint. Claude audit is
  PENDING; no shared scientific registry, final allocation or readiness change.

## 2026-11-06 — completed development and supplementary checks

Coordinator Codex, assigned gpt-6-astra high. T1/T3/T4/T5/T6 developers
were assigned gpt-6.1-sol xhigh, T2/replay gpt-6.1-sol medium; actual runtime
metadata is unexposed. No ultra escalation was used. Direction rounds and
their bounded stops are finalized in [rounds](rounds.md).

- T1: D3 passed for 20,304 canonical 3-D cosets and 450 2-D cases.
  The classification and all-n>=2 obstruction are hand-proved. All-degree
  Padua admission is explicit, with finite sanity through n10. The original
  unrestricted class and arbitrary-weight cubature questions stay OPEN.
- T4: added an explicit Newton recursive upper majorant and an
  exp(O(n log n)) upper bound for exact-greedy heights. All three registered
  numerical orders triggered D2 KILL at n7 after consecutive n6/n7 Leja
  losses. No n8..20 screen or asymptotic fit was run after that stop.
- T5: D4 passed before obstruction testing. The fixed Gaussian-grid
  degree-five support theorem is hand-proved (21 positive / 15 signed),
  and the known all-q commutator-rank formulas are reconstructed locally.
  Nonlinear completion minimization was explicitly not executed; that
  distinct route and universal cubature remain OPEN/deferred.
- T6: universal comparison and explicit Fourier bound are hand-proved;
  the primary-source trail identified Subbotin1983's already-known general
  comparison and logarithmic order. [Actual source coverage](literature-T6.md).
  No historical novelty is claimed for these facts.
- A distinct Astra high supplementary mathematical checker reconstructed
  T1/T6 and actually reran their scripts in an isolated pinned checkout;
  it also enumerated tiny subgroups/translations independently. No
  BLOCKING/MAJOR finding; its MINOR T1 scope wording fix was made and
  reviewed. [Canonical check](independent-checks-math.md).
- A second distinct Astra high supplementary checker reconstructed T3/T4/T5
  and actually reran the replay, cyclic census/quality/cover, stack and
  cubature code in another pinned checkout. It separately reconstructed
  H39's 171 Laurent witnesses. [Canonical check](independent-checks-computation.md).
  Its exact finite-cover execution discharged H39: only the normalized
  cubic obstruction and full unshifted M39 extension were upgraded from
  MEASURED/CONDITIONAL to PROVED. Statements/scopes, rank distributions,
  quality observations and infinite-degree targets were not upgraded.
- Reading-coverage caveat: the canonical T2 disclosure is in
  [its attempt](attempts/T2.md); the substantive auditor must disposition it.
  Remaining source-comparison and novelty limits stay in their own records.
- Code/data identities are in [evidence manifest](evidence-manifest.json).
  Optional raw catalogues remain regenerable local working output;
  [storage boundary](COLD_STORAGE.md). Essential finite witnesses/code
  and small receipts are committed; no archival delivery is claimed.
- Final report and [topic results](../../results/padua-3d-20261106.md) are
  synchronized. No final ranges needed: **no range**. No shared registries,
  main, tags, workflows or repository settings were changed.
- Stage AUDIT: draft PR33 preserves the work. Required Claude Opus5.5 xhigh
  substantive audit is PENDING and is not replaced by either Astra check.
  [Handoff 01](handoffs/01-work.md) closes in the following handoff commit;
  [handoff 02](handoffs/02-audit.md) carries the exact audit scope/source pin.
  No readiness or merge decision is requested from AC at this boundary.
- Integration verification actually passed: code/data manifest (31 artifacts,
  177,823 bytes), eight producer-code/receipt identities, all topic JSON,
  every topic file below 16KiB, Markdown links (except the successor handoff
  until its following commit), and `git diff --check`. Final successor-link
  verification follows handoff publication. The manifest verifier command is
  `python topics/padua-3d-20261106/code/artifact_manifest.py --verify`.

## 2026-11-06 — Claude, claude-opus-5-5 xhigh — substantive audit 01

- Role: independent auditor of Codex development (handoff 02). Rules read at
  `d0e1bbb267db9928de97538d9b524fb0068538cd`; audited candidate
  `f1a5b0936d8fb2b033c69af59a6366550f170999`; main `76ba421` unchanged.
- [Audit 01](audit-01.md), with five Opus 5.5 xhigh subagent scope reports in
  [audit-01/](audit-01/), audit code in [audit-01/code/](audit-01/code/) and
  orchestrator receipts in [audit-01/receipts.txt](audit-01/receipts.txt).
  Full `state/IDEAS.md` read performed.
- Actually executed: manifest verify PASS before reruns; all 11 handoff-02
  producer commands in a detached `f1a5b09` worktree, every scientific field
  identical to the committed receipts (Python 3.13.18 vs 3.12.14 recorded);
  an independent third-method exact H39 checker over the 171 witnesses and all
  59,319 residue triples mod 39; T1 brute force/full-cap enumeration; T4/T5/T6
  reconstructions. Details in the audit.
- Outcome: no BLOCKING. All claimed PROVED/MEASURED/OPEN statuses accepted,
  including the two H39 PROVED upgrades. Five MAJOR record/gate findings
  (missed predecessors; candidate retention and handoff-01 item dispositions,
  including the unexecuted T5 commuting-completion probe; the T2 gate-coverage
  deviation, dispositioned as a disclosed uncurable timing deviation for AC;
  the D3(b) capped-enumeration verdict; the PD-N kind of short relations),
  15 MINOR and NOTEs. Stage returns to **WORK** for a Codex response; only
  material changes get a focused re-audit.
- No IDs reserved or allocated; no shared registry, main, tags or `.github/`
  changed. Draft PR #33 AUDIT section updated after push.
- [Handoff 02](handoffs/02-audit.md) done in `64292b5`; [handoff 03](handoffs/03-response.md) opened for the Codex development response.

## 2026-11-06 — AC redirection: new directions T7/T8/T9 (recorded by Claude, claude-opus-5-5 xhigh)

- AC: "Write a handoff for what you know about Cosets without reflection symmetry and Untested variants of cyclic orbit, and set the branch to work so that codex uses same restarted budget on those directions".
- AC: "Add also what you know on Closing the gap between log³ n and everything observed."
- New directions: T7 cosets without whole-coset reflection symmetry; T8 untested cyclic-orbit variants; T9 the log³ n gap. Budget 25 rounds each, restarted from zero, with the handoff-01 rules. Claude reads "same restarted budget" as 25 for T9 too (not T6's 8); AC may correct this.
- Stage stays **WORK**. [Handoff 03](handoffs/03-response.md) is superseded by [handoff 04](handoffs/04-work.md), which carries the audit-01 response unchanged as Part A and adds T7–T9 as Part B.
- Handoff 04 marks Claude's sketches as hypotheses, not results: the general-H short-relation lemma, the fold bound |X| ≥ |H|/8, and the octahedral lattice-packing obstruction to single-coset Padua-type cubature for n ≥ 110. Claude's two unrecorded exact checks of the 10-point example (unisolvence; a degree-2 equal-weight rule exists, no degree-3 rule) must be reproduced by the developer.

## 2026-11-06 — Codex continuation of handoff 04

- Role: developer/orchestrator. AC explicitly selected gpt-6-astra high in
  this continuation. Rules read at full input SHA
  `e5b64450fce42262dafc88ee357b72e5f203916b`; rules are unchanged from the
  initial checkout. Assigned workers: Sol high for the audit response and
  exact cyclic enumeration; Sol xhigh for T7/T9 mathematics. Two distinct
  Astra high agents supply supplementary checks. Runtime model metadata
  is not independently exposed. Required Claude audit remains separate.
- The workspace initially contained only main `76ba421`. Shell Git fetch
  failed because the configured proxy could not be reached. The GitHub
  connector recovered the branch at its pinned SHA, including its commit
  objects. The reconstructed working tree exactly matched upstream tree
  `a5df446f5056134de86693335d14530f952e8cef`.
- Refreshed main is `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb` (PRs 31/32).
  Its restored files, modes and line endings exactly matched upstream tree
  `ef88e08806081410b5392f30b26fb3dca0473eb0`. Conflict-free merge
  `120a19ee71baa8e7834b3b183798df2cf489c432` is published on this topic
  branch with both original parents preserved. Main was not modified.
- Each new-direction worker reads the full original IDEAS registry and the
  complete current-main delta before new mechanisms; the gates record
  the actual scope. Part A's T2 variant dispositions were written first in
  [candidates-response-01](candidates-response-01.md), before T8 preregistration.
- New-direction budgets restart at zero, at most 25 rounds each. Gate kills,
  proved obstructions and scoped exhaustion must be recorded; no new family
  is declared promising from ranks alone. No final ranges or IDs are needed.
- Canonical audit-response disclosures (M3 gate timing, M2 unexecuted T5
  probe, m11 model attribution and unused old budgets) are in
  [response deviations](response-deviations-01.md). AC acceptance is not
  presumed; new gates and later reading do not repair original chronology.

## 2026-11-06 — handoff04 first result boundary

- T7 round1: written general finite-H/all-real-phase character factorization
  and compatible-relation lemma (PD-T supporting results, no novelty claim).
  Actual new-tool D0 controls pass: original cyclic distributions/H39,
  2-D Padua n1..10 and full invariant-class n2/n3 diagnostics. This does
  not enumerate all continuous phase strata or settle the broad target.
- T8 round1: full zero-phase cyclic census up to |H|<=8N finds95/300
  distinct minimal sets at n2/n3 from15733/112314 generator classes.
  The n2 survivors are the two old M19 classes; n3 has one full-rank
  class, M38,z=(1,6,17), outside the accepted M39 obstruction. The omitted-
  degree odd-modulus slice has1/5 full-rank sets at n5/n6. These finite
  classifications remain MEASURED. All three frozen translated rules fail
  at n2, with exact ranks8/9/8 and separate written quadratic annihilators.
  No uniform promising family or quality improvement follows from rank.
- PartA developer diagnostics reproduce full-class D3 n2..6 counts and
  exact survivor equivalences. The response disposes the original audit's
  findings and preserves deviations for AC. Supplementary checks of the
  new computation and mathematics are running separately. Global manifest
  refresh and final report/PR integration wait for the completed new batch.

## 2026-11-06 — handoff04 completed development

- T7 round2: general-H symbolic phase reduction, explicit counterexamples
  to the rank-two/one-phase shortcuts, and the exact shifted C10×C2 cubic
  survivor. The 20 actual cosine nodes separately have rank20 modulo5051
  with primitive1010th root32. A hand quartic identity proves no signed
  weights on this survivor are exact through degree4. Broad all-coset and
  uniform quality targets stay OPEN; no n4/n5 or alternate-phase search.
- T8 round2: all-continuous-phase M10 obstruction and even-order trace
  theorem; prospective odd-degree rank-only selector loses to Leja at
  n7/n9 and triggers its frozen kill, with n11 unrun. No growth fit or
  promising-family verdict follows. Finite U/O/E classifications remain
  MEASURED; analytic obstructions retain their written PROVED scopes.
- T9 round1: Lambda>=3/4+3/(2pi)>1.2274 at every n>=1 and leading
  log³ coefficient1/(24pi³), a27-fold explicit local improvement. Haar
  packing reduction is PROVED; the density-dependent n110 obstruction is
  CONDITIONAL. All26 refined finite cases execute, with no certified sup
  or asymptotic fit claim. Upper-route transfer lemmas retain their explicit
  missing premises. Nine internal route steps are not separate rounds.
- Stops and resume conditions are in the three attempts and rounds.md.
  [Continuation report](report-continuation-04.md) and the topic results
  synchronize the final scopes. The original accepted T1–T6 statements
  are not reopened; response01 lists every material record/gate fix.
- Actual T8 worker allocation was Sol high. Its initial prose mistakenly
  combined the requested xhigh mathematics/high enumeration labels; those
  labels are corrected. A separate Sol xhigh mathematical developer
  reconstructs the four new analytic proofs in
  [mathematical development](mathematical-development-T8.md), without
  rewriting the initial worker's provenance or replacing Claude review.
- Distinct Astra high checkers reconstruct all new mathematics and actually
  rerun consequential computation: [T7/T9 check](independent-checks-new-math.md)
  and [response/T8 check](independent-checks-response-t8.md). These cover
  actual-node finite-field certificates, complete earlier selector null
  prefixes, independent mesh evaluation and separate refined-maxima replay.
  Their exact files/hashes/limits are retained; they are not Claude acceptance.
- The final manifest pins local code/data plus both inherited lattice-quality
  helpers. Its verifier additionally rejects a changed inherited helper.
  Eight new raw T8 files were observed and hashed in the regenerate-only
  ledger, with no archival delivery. All new code and essential receipts
  stay below16KiB per file; prose logs and inherited protected audit/handoff
  records are not divided to manufacture that evidence limit.
- Stage AUDIT. No final-ID reservation, shared-registry application or
  readiness/merge decision is made. Following the output commit, handoff04
  closes and handoff05 requests focused PartA re-audit plus substantive
  T7–T9 Claude review. Only AC merges.

## 2026-11-06 — Claude, claude-opus-5-5 xhigh — audit 02 (handoff 05)

- Role: independent auditor of Codex development. Rules read at
  `e14ac15fd95f557e13d9c739ae097227cdb562c8`, unchanged from `d0e1bbb`; audited
  candidate `e80e000f2ba439ea62c966d255ef1b900b608b27`; main `f70a260`.
- [Audit 02](audit-02.md): five Opus 5.5 xhigh subagent reports in
  [audit-02/](audit-02/), audit code in [audit-02/code/](audit-02/code/) and orchestrator
  receipts in [audit-02/receipts.txt](audit-02/receipts.txt). Full current
  `state/IDEAS.md` read.
- Actually executed: manifest PASS; all 14 handoff-05 commands in a detached
  `e80e000` worktree, with scientific fields identical to the receipts; fresh-prime
  exact certificates for T7-06; independent T8 census, T9 falsification
  searches and Part A actual-point census (subagents).
- Outcome: no BLOCKING; all claimed statuses accepted. Four MAJOR: C1 none
  of T7, T8 or T9 met handoff 04's stop rule (stopped after 2, 2 and 1 of
  25 rounds); C2 T9 gate gaps; C3 undisclosed T9 gate edit/timing; C4 ID kind
  of refuted T7 inferences. Several MINOR items. Stage **WORK**.
- [Handoff 05](handoffs/05-audit.md) done in `9e71858`.

## 2026-11-06 — AC: adventurous round with restarted budgets (recorded by Claude, claude-opus-5-5 xhigh)

- AC: "make then a more adventurous handoff for one more codex round, indicate what are the most promising rounds".
- AC: "one more means restarting the 25 counter".
- [Handoff 06](handoffs/06-work.md): Part A responds to audit 02. Part B restarts the counters at 0 with 25 rounds each for T7, T8, T9 and a new T10 (near-Padua Chebyshev-lattice cubature plus extraction; added as Claude's proposal, and AC may drop it). It sets a stricter stop rule and ranks the most promising routes: T10 lattice cubature and extraction; T8 phase-shifted M=N orbits on admissible degrees; T7 census, survivor quality and phase optimization; T9 unconditional packing bound and class-specific lower bounds.

## 2026-11-06 — Codex continuation of handoff06

- Role: developer/orchestrator; assigned coordinator gpt-6-astra high as
  requested in the current continuation. Rules read at full branch head
  `7afa6a54a4db4652267e38cd48658ba435d20481`. Main refreshed through the
  connector remains `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`, already an
  ancestor. Shell Git fetch still cannot reach the configured proxy. The
  connector-restored branch exactly matches upstream tree
  `f1269442917af91fa61fafbfa05cfff35d6ead71`; no history was rewritten.
- Audit02 accepts the mathematics and returns process findings C1–C4 and
  n1–n6. PartA is assigned Sol high; mathematical direction workers use
  Sol xhigh, including their code. A distinct Astra high supplementary
  checker covers new results. Assigned metadata is recorded honestly;
  runtime model identity/effort is not independently exposed.
- PartA fixes precede the first counted PartB round. Four disjoint new
  direction records use the restarted counters in rounds.md. Each worker
  completes the full prospective gate before new analytical mechanisms
  or runs. Web-connector primary-source retrieval is available this time;
  source reading and local proof remain separately labeled.
- This continuation uses handoff06's stricter stop rule: every listed route
  needs an actual result, prospective gate kill or whole-route obstruction
  before an early stop. A blocked source/computation needs measured evidence
  and its listed fallback. Unused old budgets are not a valid new stop.
- No final ranges, global IDs or shared-registry application are needed.

## 2026-11-06 — handoff06 PartA response completed

- [Response02](response-02.md) disposes C1–C4 and n1–n6 before the first
  counted PartB round. Canonical timing/edit/allocation and pilot-provenance
  limits are preserved once in [deviations02](response-deviations-02.md).
  Earlier unsupported model-attribution and stronger T9 gate-timing prose
  are withdrawn by that dated record; no missing execution history is inferred.
- The old direction-wide stop decisions are explicitly withdrawn in rounds,
  report-continuation-04 and the three historical attempts. Fresh counters
  remain zero until the next pushed result boundary. Accepted mathematical
  statements remain intact; C4 classifies scoped failed inferences separately.
- T8's code metadata/path repair pins the two historical preregistrations
  and uses unique/configurable scratch. An actual isolated D0/n2 full census
  reproduces its scientific fields and raw digest; original receipts retain
  their old executed-source hash rather than pretending to use edited code.
- T9's unchanged historical producers were actually replayed through
  code/legacy_t9_metadata.py. Scientific receipts match excluding timing;
  the new companion records current observed versions/commands/source hashes
  and26 raw arrays, without retrospectively inventing old missing versions.
  Aggregation metadata and raw inventory are updated; no archive is delivered.
- Source comparisons remain coverage-qualified and require no historical
  novelty claim. The stricter handoff06 route rule governs all resumed work.

## 2026-11-06 — handoff06 first counted research boundary

PartA was published first in7f773ebe6ca04dbfdcb743b22e92da6469741748.
The following checkpoint counts one new round per direction; no direction
is declared stopped. All initial protocols were written and linked before
their corresponding runs, with publication and execution timing distinguished.

- T10 round1: exact HNF search gives global determinant minima2/12/38
  at n1/2/3; n4..16 entries are explicitly source/seed comparisons rather
  than asserted global optima. Cubature projection and restricted extraction
  are measured through n10. Extraction hits its frozen loss gate at n6/n7;
  the projection/theory route continues. Inherited QR column/point ordering
  was restored after the independent checker found tie-dependent differences;
  the n6/n7 extraction stop is unchanged. No exact subset-singularity claim.
- T8 round1: nine exact M=N witnesses cover the parity-allowed degrees
  through12, corroborated on actual cosine nodes at independent splitting
  primes. The first determinant-optimized phase rule loses at n7/n8 under
  its registered gate. Nearby orders, special phases and cyclic unions
  have recorded initial outcomes; a separately prospective mixed-stratum
  extension remains active. Parity necessity is not an all-degree existence proof.
- T7 round1: measured fixed-survivor Lambda21 is1998.9502, with54/256
  exact full-rank n3 sample witnesses and best sampled Lambda21=12.2934.
  Sampled phase/common-subgroup unions and the hand torsion obstruction
  are retained. The orthonormal-QR secondary was distinguished from the
  inherited unscaled primary comparator and corrected without reoptimizing
  any candidate. Complete n2 symbolic-census work is not closed by its
  measured partial pilot and continues under the strict stop rule.
- T9 round1: QR and one-sweep determinant controls execute n2..16 with
  guards passing. At n16 refined lower samples are168.340 and93.6385.
  These are MEASURED samples, not certified suprema or new growth laws.
  Primary packing/Leja verification, class-bound proofs and incoming
  constructive snapshots are separate active outputs for the next boundary.
- The distinct checker has independently executed initial actual-node rank,
  sample-quality and global-HNF controls. Its final scope/hashes will be
  recorded after the new mathematical/source files are frozen. The required
  substantive Claude audit is not replaced by supplementary checking.

## 2026-11-06 — handoff06 second T7/T8 boundary

- T7 round2: phase/translation quotient, projection and trace pruning are
  hand-reduced before the complete census. The reduced120-second n2
  pilot covers10733 groups/2195749 quotient strata, with zero unresolved
  tested rank cases; complete prime-order coverage is separate. Unequal
  noncyclic unions actually yield full-rank examples at n3..6, including
  a9+75-node n6 union escaping equal-common-subgroup obstruction. Quality
  remains measured and poor; these are not a degree-uniform theorem.
  The full n2 finish is a distinct run undergoing independent replay and
  is not claimed by the partial-pilot checkpoint.
- T8 round2: the separately prospective mixed-stratum nearby-order family
  gives an exact cubic M21 witness, sampled Lambda31.2318. The fixed
  positive-offset prescriptions encounter their written count obstructions;
  intermediate rank questions stay OPEN. All handoff06 T8 listed routes
  now have actual outcomes under(a); no theorem closes the broad target.
- The new T7 reading-coverage qualification is preserved once in
  response-deviations-02.md. Later rereading is not a retrospective cure.
- T10 gate clarification: round1's restricted QR comparisons lose at n6/n7,
  but numerical ineligibility of the structured subsets did not establish
  a literal all-extracted-set norm kill. A prospective same-rule n8..16
  verification pass continues that route. The old early gate shorthand is
  superseded by this scoped statement; no killed interpolation family is rescued.

## 2026-11-06 — handoff06 final production boundary

- T7 round3: complete all-phase n2 finite classification is computer-assisted
  PROVED after both an actual full replay and an independently written full
  census. Four order16 and32 order19 representatives survive, with no free
  phase loci and no unresolved target ranks. Measured n3 infeasibility and
  the permitted complete n2/exact n3-sample fallback are delivered. Every
  n2/random/pilot survivor is quality-measured, not selectively reported.
  The initial D0 receipt's missing early source snapshot is explicitly
  retained as a limitation; a new frozen-source D0 was actually executed.
- T9 round2: the local witness extends the imported density consequence
  to arbitrary strictly positive full-support unshifted weights. Published
  R-Leja premises yield an explicit known O(N³) minimal-set upper bound.
  Class-specific method boundaries, QR/localdet and incoming snapshots,
  and exact family data through109 with timed probes all have outcomes.
  Imported source premises and unsearched global optima remain explicit.
- T10 round2 combines the two final internal deliveries: density-optimal
  folding ratio73/18, local log⁴ projection theorem, explicitly CONDITIONAL
  sharp log³ corollary, bounded4941-lattice neighborhood comparison, all
  projection meshes through16, and both frozen extraction rules through16.
  The restricted QR subsets have exact rank certificates at all15 degrees.
  Structured numerical ineligibility is not an exact singularity theorem or
  a literal all-extracted-set norm kill; the final pass removes that ambiguity.
- Current counted rounds are T7=3,T8=2,T9=2,T10=2. Each direction satisfies
  handoff06(a) by its route table and recorded fallback, not a declaration
  that the broad construction problem is exhausted. No25-round ceiling is
  used to manufacture repetition. All previous direction-wide stops remain
  withdrawn, and accepted original mathematics is not reopened.
- The distinct checker independently reconstructs the full census, exact
  ranks, local proofs and numerical comparisons. Its code is frozen and
  every own-code receipt was actually rerun at that hash. Final input/prose
  pins identify the reviewed scope; no executable pins prose acceptance.
  Primary source statements, external proof dependencies, local proofs and
  measurements remain separate. Required Claude audit07 is still due.
- The global identity manifest now uses a single lossless v2 map of filename
  stems to byte sizes/full SHA-256, with fixed .py/.json suffixes. Commands
  stay in the already pinned receipts/attempts rather than being duplicated.
  This preserves all identities within one compact file, without splitting
  evidence. Actual mutation controls reject code/data/inherited-input changes.
- Reports, results, raw inventory and source manifests are synchronized.
  Fifty-one raw identities were actually checked, with no archival delivery.
  No final IDs, reservation or shared-registry application is made. Following
  the output commit, handoff06 closes and handoff07 carries the focused
  response02 review plus substantive restarted-work audit. Only AC merges.

## 2026-11-06 — Claude, claude-opus-5-5 xhigh — audit 03 (handoff 07)

- Role: independent auditor of Codex development, third round. Rules read at
  `54d554a13e135dc99a46c38728c9a2d74897a14c`, unchanged since `7afa6a5`; audited
  candidate `696bca5fe8842b8b99ec298381c948206be79548`; main `f70a260`.
- [Audit 03](audit-03.md): six Opus 5.5 xhigh subagent scope reports in [audit-03/](audit-03/),
  audit code in [audit-03/code/](audit-03/code/), receipts in [audit-03/receipts.txt](audit-03/receipts.txt).
  Full current `state/IDEAS.md` read. Primary sources newly read: Betke–Henk, Chkifa 2015,
  Kolomoitsev–Lomako Theorem 4.1.
- Outcome: no BLOCKING; every claimed status accepted. This includes the computer-assisted
  complete n=2 coset classification (confirmed by a census using a different method) and all
  nine T8 M=N witnesses (re-certified with fresh primes up to N=455).
- Six MAJOR findings: E1 T10.1 census incomplete; E2 T10 extraction kill mis-stated;
  E3 T9 finite complement without measurement; E4 literature-dependency label convention
  (AC decides); E5 gate predecessors (LIT-391); E6 records for killed rules and candidates.
  Stage **WORK**.
- Third-round auditor MINOR fixes go in a separate commit, listed in [audit-03-fixes.md](audit-03-fixes.md).
  Pinned prose is corrected by companion note only.
- LOG correction (not an edit of history): the model-attribution withdrawal cited at the
  2026-11-06 Part A entry ("deviations-02") is in [response-deviations-01.md](response-deviations-01.md), m11.
