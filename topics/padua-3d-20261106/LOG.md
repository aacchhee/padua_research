# Padua-type points in three dimensions: log

- Branch: `codex/padua-3d-20261106` · Base: main `f70a260` (setup base `76ba421`) · Developer: Codex · Auditor: Claude (Opus 5.5 xhigh)
- Stage: AUDIT · Next: formal combined Claude audit04 of pruning and preserved material · Successor: [handoffs/17-pruning-audit.md](handoffs/17-pruning-audit.md)
- Reserved final-ID ranges: none. Reserve when first needed (PR #29 rules).
- Claims: provisional records in [report.md](report.md), [report-continuation-04.md](report-continuation-04.md), [report-round06.md](report-round06.md); no final IDs allocated.

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
- [Handoff 07](handoffs/07-audit.md) done in `a74c1b1` (report `c681ba0`, auditor fixes `a74c1b1`); [handoff 08](handoffs/08-response.md) opened for the Codex response and the reopened T10.1 and T9-complement routes. Counters continue (T7=3, T8=2, T9=2, T10=2 of 25).

## 2026-11-06 — Codex, gpt-6-astra high — handoff08 initialization

- Role: developer/orchestrator. Rules read at full input head
  `9042e1c42964150f30fdbe8563c12ba6c6a8692a`: AGENTS, WORKFLOW, CODEX.
- Refreshed GitHub main and topic: main remains
  `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`; recovered the three
  audit/handoff commits with their exact original objects and tree.
  Shell proxy remains unavailable; repository connector performs permitted
  topic publication without rewriting history. PR33 remains draft, no range.
- Read handoff08, audit03 and its scope reports/fixes. Accepted mathematics
  is retained. T10.1 and the unrestricted T9 complement reopen; T8 half-shift
  M=2N is the new prospectively gated route. Counters continue at
  T7=3,T8=2,T9=2,T10=2 of25 until actual result checkpoints.
- Assigned mathematical workers gpt-6.1-sol xhigh to the shared lattice
  census/complement, T8 half-shifts, records, and two distinct supplementary
  checks. Code/receipt hygiene uses gpt-6.1-sol high. Root alone holds Git.
  Model/effort are configured assignments; runtime metadata is unexposed.
- Existing-route completion and correction add no novelty claim. New T8
  selectors await a complete registry gate and a published prospective
  protocol before execution. Worker file ownership is disjoint.

- Prospective T8 gate/protocol are published before dependent execution.
  The reopened T9/T10 replication protocols were written before their new
  enumerations, but this checkpoint follows the first executions; that
  timing remains worker attestation, not a publication-before-run claim.

## 2026-11-06 — handoff08 progress checkpoint — Codex, Astra high

- New exact lattice implementation and supplementary independent checks
  extend the small catalogue; the producer has completed determinant
  windows through16, with a5772 witness improving the old5792 seed at16.
  Full complement scans through6 and higher-degree feasibility are being
  finalized. These are an unfinished checkpoint, not the final scoped
  computer-assisted status or a claim that independent coverage is complete.
- New half-shift screen completed the prescribed3..8 degrees: exact trace
  excludes even degrees; odd-degree determinant selection has finite
  measured outcomes. The cubic floating tie is corrected separately using
  exact determinants and the registered lexicographic tie-break. Source
  snapshots and both runs are preserved; final interpretation/checks follow.
- Technical hygiene replay is complete; response-03-hygiene records the
  actual shifts, selected-node linkage, current code-only pins and51raw
  identities. The manifest v3 losslessly uses base64 SHA-256 and recursively
  includes arbitrary code/data suffixes (including the new C++ source).
  Eight mutation controls pass; this snapshot's manifest is generated
  against its staged tree, so ongoing worker edits are not misattributed.
- response03 and records/theory remain in progress. Handoff08 stays open.

## 2026-11-06 — handoff08 completed output — Codex, gpt-6-astra high

- [Report](report-round08.md), [response03](response-03.md), records and
  technical-hygiene companions dispose E1–E6 and every returned item.
  Accepted old mathematics is retained; audit/handoff instruction bodies
  are protected. Missing-home corrections and scoped failures are explicit.
- T10/T9 now separate determinant, folded count and full-rank count. Exact
  determinant minima through16 include5772 at16, independently enumerated
  by a different method; n4..16 use explicit imported packing. Local
  computer-assisted global folded/full-rank minima through5 and no exact-N
  positive full-support unshifted rule at n3..7 follow from q/8 and exact
  ranks. Small positive rules at n3/4/5 can be singular. No all-phase or
  all-degree theorem is inferred; global larger minima stay OPEN.
- Actual higher cost is preserved: n7's producer caps after q881 and921,
  then its final922..960 segment completes88.0856seconds. Every per-q
  scientific count agrees with the checker's separate complete304.789s
  replay. This covers584906253HNFs and21354010admissible lattices, zero
  at-most120-node sets. n8 was not run; no unmeasured infeasibility claim.
- T8 new3..8 scope completes: every even degree is excluded analytically,
  exactly8cubic normalized triples survive a complete exact741census, and
  measured n3/5/7 corrected scores are9.7888/70.3729/136.6904. QR losses
  exclude promising status; the literal two-Leja-loss trigger is not met.
  The post-quality exact-tie correction is disclosed, original run retained.
  Old-nine finite existence is a narrowly split material PROVED proposal.
- Two distinct Sol xhigh supplementary checkers actually rerun consequential
  computation. Lattice checks include alternate congruence windows through16,
  complete low-degree alternate enumerations, independent monomial rational
  ranks, exact actual-node witnesses and separate full higher replays.
  T8 checks include all741exact ranks, fresh-prime witnesses and qualities.
  These do not replace Claude's required focused audit.
- E4 convention is proposed uniformly: PROVED with explicit LITERATURE
  dependency when exact primary statement/normalization and application
  have been checked. AC decides; no external proof is claimed local.
  T10 log3 relabel, finite status upgrades, q2cardinality repair, tie repair
  and result-bearing source/evidence changes are material for re-audit.
- Canonical chronology limits stay in deviations01/02. The new T8 gate
  reading qualification is canonical in attempts/T8-round08.md. A published
  pre-run protocol is not retroactive full-table reading compliance.
- The single v4 recursive code/data manifest stores lossless RFC1924base85
  SHA-256 identities and covers new C++/nested/other suffixes. Eight actual
  mutation controls reject changes; current code/data pins pass. Prose pins
  are removed with dated historical metadata, not fabricated source matches.
- Validation: all scientific receipts parse and remain below16KiB; current
  source/data identities and owned links are checked. Protected audit reports
  retain quoted example-relative links; they are not edited or counted as
  newly introduced link defects. Raw outputs are local regenerate-only with
  byte/hash identities, no cold-storage delivery. Final IDs/ranges: none.
- Counted rounds continue T7=3,T8=3,T9=3,T10=3/25. Each new direction
  boundary has actual required-route outcomes under handoff06(a); no
  all-degree exhaustion or budget-target repetition is claimed.
- Stage AUDIT. After publishing this output, close handoff08 by status only
  and publish handoff09 for Claude Opus5.5 xhigh focused material re-audit.
  Main refreshed unchanged f70a260; only AC merges.

- Final executed integration checks: manifest204artifacts,994297code/data
  bytes,15804-byte single manifest;104existing-path identities in new
  receipts match exactly, zero owned-link errors, all topic JSON parse/size
  checks pass, diff whitespace clean, scope/protected-body checks pass.

## 2026-11-07 — AC authorizes usable point-set campaign — Codex, Astra high

- Rules read at fullinput38227202bc6908d5a5a874950145761a8ca4312f:
  AGENTS,WORKFLOW,CODEX. Runtime skill refreshed; attached environment
  matches the executor and policy is enforced. Main/topic refreshed:
  f70a260/3822720 unchanged, clean local branch.
- AC: write the three discussed ideas and work on them, up to10rounds
  each for extra-point least squares and direct optimization, up to20
  for shifted/folded/mixed constructions. [Campaign](usable-campaign.md)
  records exact scope, starting0/10,0/10,0/20, evidence and stop discipline.
  Previous T7/T8/T9/T10counts stay3/25. No new research round consumed.
- New instruction redirects pending [handoff09](handoffs/09-audit.md)
  into [handoff10](handoffs/10-usable-work.md). Its independent Claude
  audit04 scope remains pending and will accompany new material audit.
- Solxhigh shared gate reader and disjoint U1/U2/U3 developers prepare
  existing-source readings; two separate Solxhigh checkers cover U1/U2
  and U3. Root alone controls Git. No mechanism generation/research
  execution is released until the shared gate is complete and published.
  Dependent protocols are then separately published before experiments.
  Configured model/effort recorded; runtime metadata is unexposed.

- The shared [usable gate](usable-gate.md) completes all1154current
  IDEAS lines and34table runs before clearance; literal bounded outputs
  repaired every initial truncation before new mechanism generation.
  Relevant full closest proofs/source records and precise reading limits
  are recorded. Root verified its8inherited code/data identities. This
  published gate releases registration only; experiments await separately
  published protocols. No old chronology qualification is erased.

- U1's two-route operational/solver protocol, U2's fixed direct-norm
  pilot/conditional holdout, and the separate U1/U2 fresh-check protocol
  are published before dependent execution. U3 registration is still
  being written and remains unreleased. No research round counted yet.
- Evidence manifest v5 preserves the complete v4 identity map losslessly
  inside one zlib/base85 JSON payload, with --list for inspection. This
  leaves room for new campaign artifacts under16KiB without splitting
  or dropping old identities. The decoded map and eight mutation controls
  actually pass; current generator code pin is updated transparently.
  Coverage is unchanged: recursive code/data, inherited helpers, no prose.

- U3's four full candidate/protocol records are published before dependent
  execution: exact sparse DCT/support-triangular structure; explicit
  coherent rank-two folded cosets; folded-cyclic plus generic noncyclic
  correction; reversed folded-noncyclic plus cyclic correction. Each has
  exact count/action checks, finite parameter scope, frozen selection and
  validation rules and actual-outcome requirements. Separate U3 check
  protocol is published with it. All stream research counts still start0.

- U3 F exact-completion append is published after the initial modular
  screen and before exact completion. For coherent half-cosets, equal
  character classes have phase ratio±1; stripping row phases leaves an
  integer dictionary of the actual real rank. This closes the previously
  unresolved modular defects without inferring real deficiency from them.
  It completes the existing F round, not an artificial extra round.

## 2026-11-07 — first usable result checkpoint — Codex, Astra high

- U1two registered routes are complete and count2/10on this push:
  explicit operational recipe/all24cases and same-node OLS comparison.
  Currentsource50da9061 remains unchanged. All76raw/sourceidentities and
  local links pass; direct API/RHS-shape check maximum9.33e−15. Known
  analytic covariance/reproduction proofs are separate from measurements.
- U2first pilot counts1/10: all16sets have nonzero dyadic modular minors,
  gradient check5.84e−10, all overlap controls repeat. n4quality improves
  11.1401to5.43472; nonsmooth RMS loss retained. n6/8fallback fails gate,
  no holdout executed. Source/receipt serialization failure is disclosed;
  unchanged mathematics actually reran with compact valid evidence.
- The exact training trace diagnoses singular first trials and return to
  initial points. New U2admissible-step protocol is published before its
  run, with geometric separation and exact-model Neumann sufficient guard.
  Pilot assessments are reused/known, not relabelled unseen; conditional
  n10/12remains unseen. Old frozen source is now in this pushed checkpoint.
- Supplementary checker has actually replayed all24U1and16U2cases with
  matching scientific arrays/traces and fresh exact dyadic ranks; final
  independently assessed receipts are still being frozen/integrated.
  This is not Claude audit. U3continues uncounted until its four actual
  route records and exact-F completion are ready.
- [Progress report](usable-report.md) and results synchronize the genuine
  gains, failures and tradeoffs. No final IDs/ranges or merge.

## 2026-11-07 — shifted/folded/mixed checkpoint — Codex, Astra high

- U3S/F/M/Rall have actual outcomes and count4/20when pushed here.
  The exact cubic inverse has norm-infinity4, entrysum52and bound103;
  inverse amplification splits old determinant ties52versus78. Sparse
  unique-support counts8/8/0at3/5/7, complete35287matrix census.
- F's coherent rephased integer matrix decides every460QQcase in the
  6976parameter universe. Only2quintic tuples are full rank, but exact
  folded lists and a pointwise sign proof show1physical56-node set.
  Both M/Rorientations give exact N-node witnesses at all3..8.
- All four frozen selectors fail their precise finite quality gates;
  M/Rn8is post-kill validation after Lejalossn6/7. No general class or
  asymptotic rejection, cubature assertion or extra-budget repetition.
  Four route records include all tested candidates and resume conditions.
- Independent U3code actually checks every support matching predicate,
  all460exact ranks and fresh actual-node ranks, plus all15selected
  quantities on21/41meshes/controls. Differences<=3.92e−11/4.3e−14.
  M/Rcompleteoptimizer schedules were inspected, not independently rerun.
  The scoped distinction is explicit; these checks do not replace Claude.
- Current counted results U1=2/10,U2=1/10,U3=4/20. Revised U2pilot has
  passed; registered unchanged n10/12holdout and its proof/data artifact
  checks continue before that route is counted. No ceiling is reset.

## 2026-11-07 — completed usable batch — Codex, gpt-6-astra high

- U2R2pilot and unchanged reserved n10/12transfer both pass registered
  quality/cost/guard criteria. At n12 refined lower sample55.6779to
  26.0073, extra60.48/total73.17CPU seconds. Allsix runs stop at200steps,
  not convergence. Sampling/function/noise regressions are retained;
  pilot clouds are reused and only candidate higher-degree outputs were
  unseen. Initial failed-rule sources/diagnoses stay immutable.
- U2counts3/10on this final result+LOGpush, with R1alreadycounted.
  U1stays2/10,U3stays4/20. Total9actual research rounds; no count for
  API/packing/format fixes, analytic substeps or supplementary reruns.
  All registered routes have actual outcomes, with8/7/16unused budgets.
- Essential degree12payload14853bytes stores every actual coordinate
  losslessly; exact independent integer-bit cube/distinctness checks and
  determinant318086at verified prime1000037 establish this455-node
  dyadic set's finite unisolvence. The actual byte bridge matches the
  measured .npyarray. No optimization replay/raw retrieval is needed
  for that theorem. Floating quality/all-degree claims remain separate.
- Distinct Solxhigh U1/U2checker replays64actual scientific cases and
  allcandidate traces, plus fresh basis/SVD, function/noise, API,
  Neumann/geometry and monomial checks. U3checker independently covers
  all support/count/rational-rank cases, selected witnesses and meshes.
  No mathematical discrepancy remains within these bounded supplements;
  full M/Roptimizer schedules inspected, not independently replayed.
- [Usage guide](usable-recipes.md) includes direct Haar/OLS/stored-set
  examples. Root actually executed their complete paired API path on
  64query points, RNG20261107, polynomial2+x−yz: errors3.55e−15,
  2.66e−15,1.33e−15. Stored payload hashade51c2e459b2d3161eddab564e1ada2233d2f841b5dd64bf808b2e607f7140f.
  These are usability checks, not extra research rounds or a proof premise.
- [Final report](usable-report.md), campaign, ledger, results and all
  candidate dispositions/resumes are synchronized. Source-freeze and
  serialization/reading limitations stay canonical in stream/check
  records and previous deviations. Current new gate completed before
  generation; all protocols/addenda were pushed before dependent runs.
- Stage AUDIT. Preserve pending handoff09scope and combine it with this
  new material batch in handoff11 for Claude Opus5.5xhigh. No final IDs,
  reservations/shared registry application, readiness or merge. E4and
  earlier AC decisions stay pending. Only AC merges.

- Final integration checks executed: v5single manifest261artifacts,
  1408182code/data bytes,16259manifest bytes; all31legacycurrentcode
  pins match. Root directly verified139existing-path identities in new
  receipts (zero mismatch/missing temporary identity), all owned links,
  all topic JSON parse/size, protected audit/handoff instruction bodies
  and whitespace. Supplementary checker separately verified265identities.
  Main/topic refreshed f70a260/93c605c before final publication.

- Final prose integration clarifies registration-time versus current
  candidate dispositions and replaces U1's stale awaiting-checker note
  with its actually completed independent scope. No source/data or
  scientific claim changes; completed scientific output remains53d11b9.

## 2026-11-07 — AC requests adversarial interim audit — Codex, Astra high

- Rules read at5440555cf326afdbd66b75bed195802013901c2d: AGENTS,
  WORKFLOW, CODEX. Clean pinned branch/main refreshed unchanged. Runtime
  skill/status refreshed; attached executor matches and policy is enforced.
- AC says Claude is unavailable and explicitly requests our adversarial
  interim audit and a decision on further directions. [Handoff11](handoffs/11-usable-audit.md)
  is superseded only by status into [handoff12](handoffs/12-interim-audit.md);
  the exact formal combined audit scope remains pending. No formal
  Claude approval/readiness or changed source status is asserted.
- Root coordinates five distinct cold-context Astraxhigh auditors: U1,
  U2, U3, prior pending material and strategic/novelty assessment. Runtime
  model/effort are configured; provider metadata is unexposed. They own
  disjoint interim-audit-01reports/code/evidence; no producer edits/Git.
- New stress/counterexample checks are audit probes, consume no research
  rounds and do not authorize a new unregistered construction search.
  Current counters stayU1=2/10,U2=3/10,U3=4/20, remaining8/7/16.

## 2026-11-07 — completed adversarial interim audit — Codex, Astra high

- [Interim audit01](interim-audit-01.md) integrates five cold-context
  Astraxhigh reviews and actual independent stress/exact checks at
  science5440555. No proof-level BLOCKING finding in covered scope;
  oneMAJORoperationalinput-shape bug returned to development. Minor
  stale-tense/support-count wording fixed separately in55f103b and
  [fix list](interim-audit-01-fixes.md). Science/code/data unchanged.
- U1proofs and valid-input data pass. Wrong-leading-dimension values
  silentlybroadcast; requiredfix before unqualified API recommendation.
  Strong feasible-budget noise controls still favor Haar/OLS, while
  higher-degree feasible QR wins fresh deterministic cases and non-iid
  noise can reverse OLS's small advantage. No universal winner.
- U2stored455-point proof/check passes again. Fresh114700queries and
  140physical-starts/family find unchanged maximum26.0073. Comparable
  extra-cost localdet reaches48.5833after six total sweeps; U2gain
  survives while noise advantage shrinks3.29percent. Step200remains
  nonstationary, with nontrivial last20-step progress; correctly disclosed.
- U3all6976Fparameters/2750exact-Nranks and all35287support predicates
  pass without original pruning. Outside unique matching, n7has28full-
  rank cases; their blocks23–34/inverse sums3297–5253are not gentle
  control or norm lower bounds. Selected mixed failures do not reject
  broad families. Preserve structural resumes; stop identical selectors.
- Prior covered lattice/phase assertions pass fresh checks, including
  alln7det1..960 and n16window5772/24minimizers. Uncovered8..15window
  reruns, old floating reruns and new primary reading remain explicit;
  E4and other AC decisions/formal Claude audit still pending.
- Rootfreshintegrity checks all261developer identities and seven
  mutations/restored baselines. Each reviewer records frozen code/data,
  commands/versions/seeds and compact evidence; raw regeneration-only.
  Full current IDEAS/table strategic read completed personally before
  judgments, with relevant closest proof/source scope recorded.
- Decision: fixU1API first; U1keepoperational/no generic new round;
  atmostone U2unchanged-rule higher-degree/cost round next, then atmost
  one U3retainedstructural diagnostic with positive gate before another.
  Initial future release≤2researchrounds, not consumed now. Counters
  unchanged2/10,3/10,4/20,unused8/7/16; no audit/fix rounds.
- Stage WORK for explicit developer response. This is an interim Codex
  assessment, not formal Claude audit04/readiness. No final IDs/ranges
  or shared registry application. Handoff13 gives precise next work.

## 2026-11-07 — AC authorizes further usable-construction work

- Rules read at97c323bfae15cf3c76f40802c3ebabedceeb0c60 (AGENTS, WORKFLOW, CODEX). Main/topic refreshed unchanged f70a260/97c323b. Runtime skill/status refreshed, attached executor connected/running, policy enforced.
- AC: “continue, up to 7 rounds in each of the three directions”. [Handoff13](handoffs/13-interim-response.md) is superseded by status into [handoff14](handoffs/14-seven-round-continuation.md). Interpret as seven further rounds EACH, with audit stop criteria retained, not mandatory spending. Starts at2/3/4 cumulative; this campaign ceilings9/10/11 stay inside original10/10/20.
- Root Astrahigh coordinates Solhigh U1/U2, Solxhigh U3 and Solmedium lossless manifest maintenance. Scope owners have disjoint files; root alone Git/shared summaries/manifest generation. Actual configuration disclosed; provider metadata unexposed. U1 API repair and independent checks use0rounds. Full novelty gate before new mechanisms; no novelty claim from old-rule transfer.
- Formal Claude combined handoff11/09 remains pending; interim and new supplementary reviews do not replace it. No IDs/ranges, shared registry updates, readiness or merge.

### API response and prospective continuation checkpoint

- Observation-shape MAJOR is corrected in parity_fit. Distinct [focused review](api-response-review.md) PASS:140valid inputs bitwise equal to baseline,110malformed inputs reject, fresh cosine-basis checks pass. Original24case producer replay has144saved arrays unchanged; that replay is explicitly developer work, not mislabeled independent execution. Additional degree-domain hardening stays a NOTE outside this narrow closure. [Combined response](response-interim-01.md) preserves all findings and scope. Repair/review count0rounds.
- Prospective protocols published before execution: U2degree14/cost9ceb722, U3all28septic739982c, U1fixed637budget/degree/noise cb014092. Executions are in progress or await timed CPU windows, so no new research outcome is claimed at this checkpoint. Independent reviewer checks implementation and consequential outcomes.
- [Manifest v6](manifest-v6.md) losslessly compacts complete path/size/SHA identities using canonical binary prefix paths and raw32byte hashes. Frozen-copy tests pass28controls and preserve v5 decoded map/backward support. The261entry baseline shrinks16259→15132bytes; capacity is finite, not waived. Final master regeneration uses the actual checkpoint code/data tree. No hashes are dropped and no prose acceptance pins added.

### First continuation outcomes — one round per direction

- [Continuation results](continuation-results.md) records actual completed U1C1/U2C1/U3C1. Each consumes1newround; cumulative3/4/5, current allowance1/7each, six each unused. Receipt identities/source code preserve exact execution inputs; protocols preceded execution.
- U1all38feasible designs pass; primary optimal degree falls with assumed noise, all12x7recommendations agree on both fresh clouds. Practical gate passes; preregistered known GLS-refit follow-up is next.
- U2degree14searched norm35.5443versus64.2069one-sweep/62.1534five-sweep localdet, quality/guards pass but120.7177extraCPU at176steps fails the strict cost gate. The canonical timing/checkpoint deviation is in u2-continuation.md; no literal protocol pass or convergence claimed. Consider a separately registered cheaper stopping question only with positive training evidence.
- U3all28exact/numerical checks pass,0competitive, bestboth-mesh ratio5.07481. Stop only this complete finite degree7route; six further current slots unused, broader families stayOPEN.

### Second U1/U2 continuation rounds

- U1GLSrefit round2passes covariance/reproduction checks but fails useful-total-MSE gate: bestprimary1.6453percent/secondary0.7585percent below5percent. Retain deterministic regressions and all62freshassessments; stopfixed-allocationrefit. Degree choices use known-target bias calibration, not data-only selection of unknown field.
- U2training-only calibration round2selects fixed40steps (20percenttraining gain/guards/cubicforecast gate). Forecast89.1653CPUatdegree16is heuristic, not proof or actualcostpass. Caps60/80fail; no freshassessment used to choose. Prospective degree16transfer next.
- Actual newroundcounters2/2/1, cumulative4/5/5; currentunused5/5/6. No extra U1/U3run merely to spend ceiling.

### U2 third continuation round — finite degree16 gate passes

- Fixed40accepted-step schedule completes at969sites: extra65.78345CPU (<120), total124.20255includingQR/firstsweep, numericalguards pass, unfinished optimization explicitly retained. Searched norm71.70775versus93.63848one-sweep/79.26742whole-sweep-prefix control; registered5percent gain gate passes. Distinct reviewer actual-data/selection/training/risk/freshnorm checks corroborate.
- Full-sweep control spends49.91419of65.78345extra allowance,24.12percent unused. Because9.54percent normmargin is modest, preregister one stronger per-row-prefix comparison before recommending a full-cost advantage. That follow-up is not yet executed/count-consumed.
- Actualnewcounters2/3/1, cumulative4/6/5, currentunused5/4/6. U1/U3specificroutes parked; no blanket family failure. OriginalU2C1strictcostfailure remains distinct from C3newstage/checkpoint implementation.
- Manifest envelope metadata wording condensed only; exactv6codec/payload/decodedidentitymap and requiredmetadata are unchanged. Dated followup in manifest-v6.md; originaltestreceipt stays historically pinned.

### Completed continuation endpoint and stronger-control review

- U2C4fine-row control uses65.74608of65.78345extraCPU (99.94percent). U2searchednorm71.70775versus80.12012, ratio0.89500: stronger5percent gatepasses. Independent actual-row/clock-budget/hash/update/freshquery checks reproduce the result; no independenthardwaretimingrerun claimed. The3nanosecond receipt-rounding difference selects the identical prefix under both precise budgets.
- Retain adverse outcomes: U2iidrisk5.93percentworse and12of16non-floor target/measure RMS cases worse than fine control. This is a finite strict969-site/amplification endpoint, not general error/noise dominance or certified supremum. No more automatic degree/cost/seed escalation.
- Final newroundcounts2/4/1of7each, cumulative4/7/5within original10/10/20. Current unused5/3/6retained; old overallroom6/3/15is not silently added to this campaign. U1refit/U3specified route stop at failed gates; U2finite endpoint retained. All allocated experiments actually finished.
- [Complete continuation record](continuation-results.md), [independent supplement](continuation-review.md) and [usable recipes](usable-recipes.md) cover outcomes/limits. APIresponse is narrowly fixed/independentlyPASS; degree-domainhardening staysNOTE. Formal combinedClaude audit04remainsPENDING, preserving handoff11/09scope and old explicit uncovered/source/E4obligations.
- Stage AUDIT. No IDs/ranges, shared scientificregistry application, ready/merge or archivaldelivery. Publish all outputs before status-only closing14 and opening15 for the formal audit when available. Only AC merges.

## 2026-11-07 — AC authorizes adaptive point-removal campaign

- Rules read at6d894d50efd8167c5b10f3d5b0da4d8cf214b681 (AGENTS, completeWORKFLOW, CODEX); main/topic refreshed unchangedf70a260/6d894d5. Runtime skill/status refreshed, executor connected/running, currentobservations/policyenforced.
- AC proposes starting with a larger set and removing points while possible, then authorizes up to15total researchrounds on this approach. [Brief](pruning-brief.md) and [handoff16](handoffs/16-pruning-campaign.md) record authority. Handoff15is superseded by status only; exact formalClaude scope remains pending. Old U1/U2/U3completed4/7/5 and stops unchanged. Newpruning0/15, not15perrule or15deletions.
- RootAstrahigh coordinates Solxhigh fullpredecessor/theory gate, Solhigh pruningdeveloper, Solmedium manifestcodec headroom, distinct supplementary review. OnlyrootGit/sharedfiles. Configuredmodelmetadata disclosed; provider metadata unexposed. Newgate reads completecurrentIDEASandalltables, closestdowndate/extraction records; no historicalnoveltyclaim.
- Every construction question awaits publishedprospective protocol. Physicaliidnoise OLS, actualweightedcovariance, realintegerreplication and idealbalancedcoefficients staydistinct. Numericalrank alone is notquality; retainfullcount/noise/amplification/target/costfrontier. Exact455payload/oldscience preserved. FormalClaudepending, no IDs/ranges/registryapplication/readiness/merge.

### Pruning P1 — completed adaptive A/D pilot

- Prospective protocola05fa01preceded allscience. One newresearchround P1covers degrees4/6/8 and four frozen rules. Actual17.0978CPU/17.1110wallseconds,104assessmentcases; A/Dnumericalrank/update guards pass. Both usefulness gates FAIL.
- Noise-oriented/determinant-oriented paths lose accepted amplification after few removals: n8selected223/222of225, and freshheldoutamplification about1.65/1.61ofinitialOLS. At10percentsiteremoval Ainteger-budget risk rises21.24/21.54percent at6/8; no operational re-entry on the existing fullcurves. These specific paths fail, not adaptive pruning generally.
- ExactNdiagnostics also lose the practical controls: n8A/Damps78.187/56.248versus45.536globalQR/23.973localdet. Retainalltarget/noise losses and failedlexreproductionguard. Distinct actual-path/SVD/map/freshcloud/XZinventory checks reproduce the failedgates; no unresolved materialfinding in P1scope.
- Initial compactreceipt serialization exceeded16KiB after complete science; newreceipt-onlycollector packs a six-significant-digit summary withXZ intoone16349byteJSON, fullprecisionraw retained/hashidentified. No science rerun or rewritten scientificsource provenance. This administrative repair counts0; no lossless-fullprecision claim.
- Fullproduceridentitymasterv7keeps completepath/size/SHA/inheritedinputs inoneframe/master and backwardsv4/v5/v6support; codec/CLI/mutationchecks completed independently. Codecworkcounts0; no identities dropped or prose acceptancepins.
- [Pruning results](pruning-results.md) and [P1scopednegative](theory/pruning-p1-boundary.md) preserve rules, failedcriteria and exactNcomparisons. Counter1/15completed,14unused. Nextregisteredquestion may use actualcardinal-amplification-aware feasible deletion with densertraining; no retuning or rerun of failed A/Dgates. FormalClaudepending unchanged.

### Pruning P2 — exhaustive first-step amplification barrier

- P2protocol99a9f47was prospectively corrected to unused assessmentseeds in143b5d0before scientificexecution; originalseedscollided with prior independentclouds. No P2result usedtheoldseeds. Acceptance/cap-recording code fixed and engineeringmockchecks rerunbeforeexecution.
- One completed researchround P2at6/8: exhaustive actualcardinal feasible-deletion search, dense9cubed+256Sobol training. Every112/225singleton meets10percent integer-risk bound, ZERO meet25percent training-amplification bound. Minimumamp ratios1.2869558/1.4443987; stopsunchanged112/225, guardsPASS and strictusefulgateFAIL. No numericalrejection/cap/serializationfailure. Actual4.14949CPU/4.15058wall.
- Distinct independent337fresh-SVD candidate refits, actualtwo-degree reruns, tenmaps/fulltarget/noisetables/meshes and independentfreshclouds reproduce finitefirst-stepbarriers. This says nothing about nonnested subsets, batch deletions, changedstartinggeometry or differentdeclaredquality/costtradeoffs.
- [P2record](pruning-results.md), [scopednegative](theory/pruning-p2-singleton-boundary.md), [independentreview](pruning-review.md) preserve exactscope. Counter2/15,13unused. [Next-question gate](pruning-next-questions.md) retains distinct alternatives; no newexperimentpre-consumed. A cheapreflection-pair test can escape the individual-deletion hypothesis if a joint deletion passes the originalbounds.

### Publication integrity correction and next prospective transfer

- Rootomitted pdpr-p2-engineering.json from the P2output commit although the identitymanifest already referenced its unchanged bytes. Commit812e721adds that receipt; science/decisions are unchanged. Rootnow independently reconstructs producerfiles/master/inheritedinputs from the Gitindex into a disposable tree and executes --verify there before checkpoints, detecting untracked-file omissions instead of relying only on the workingtree. The corrected published/index299artifact snapshot verifiesPASS. This is a publication correction,0researchrounds.
- P3calibrated near-minimal tradeoff protocol650b49dprospectively freezes A atceil1.20N and degree12transfer+n8pathreplay, with same-size QR and modernstored455U2control, independentquery/refinementrules and complete-prefix cost. Earlier P1/P2stricttolerance failures remainfailed. Construction implementation/engineering checks are a prospective checkpoint; P3outcome not yet claimed.

### Pruning P3 — degree12 near-minimal tradeoff succeeds

- Calibrated A rule at prespecifiedceil1.20N, protocol650b49d, actual source46d1e2b. n8complete61state trajectory exactly reproducesP1; newdegree12primary546of637sites saves14.2857percent. Completevalidated/fsyncedprefix1.195763CPU; fullallocatedP3all23maps/28starts/targets38.445654CPU. Allnumerical/cost/reproduction/matchedcount/nondominationgatesPASS.
- n12searchedamplification35.46077versus41.39678same-countrestrictedQR (14.339percentlower); fixedB637risk0.9310998versus1.1620764 (19.876percentlower). Storedmodern455U2has26.00732amp/1.172706risk:91fewerpoints+betternorm, but546candidate20.603percentlowernoise. This is a finite tradeoff, not general domination or certifiednorm.
- Oldstrictfull-grid preservation stillFAIL: fullOLS637amp10.59258/risk0.6961037. All12ChebRMSimprovevstestedstoredU2butuniformGaussianworsens10.54percent;6RMSregressionsvsfullOLS(worst75percent). DiagnosticN455Aprunedamp128.02964/risk3.275852losesstoredset. PreserveallunfavorableoutcomesandN/1.1Ndiagnostics.
- Distinct actualprefix/hash/checkpoint/score/fresh-SVD/gradient/strongcontrol/freshquery/refinement checksPASS; no independenthardwaretimingrerun. [P3record](pruning-results.md), [durableMEASUREDhome](theory/pruning-p3-frontier.md), [review](pruning-review.md). Counter3/15,12unused. A separatelyregistereddegree16transferisnowjustified, thencompactcanonical-ID exact-rankdeliveryifqualitysupported. NoP4resultpre-consumed.

### Pruning P4 — larger-degree finite tradeoff and portable n12 proof

- P4protocol55a6a11, frozen4766e79d driver and unchangedP3core/collector. n16primary1163of1377sites saves15.54percent; completevalidated/durablesavedprefix14.231638CPU, fulltoNdiagnostic25.301732CPU. All13allocatedmapassessments/controls/targets/refinements complete152.343048CPU/152.433746wall. PracticalgatePASS.
- A1163searchedamp40.88506/B1377risk0.9480039 versusmatchedrestrictedQR1163amp61.04459/risk1.1858454 (~33.02percent/20.06percentlower). Modern969U2amp71.70775/risk1.6745872 andfineDet96980.12014/1.5851507 use194fewersites; primaryqualityimprovesat20percenthighercount. No scalarall-purposewinner.
- Preserveadverseoutcomes: full1377OLSamp12.74056/risk0.6888394 remainsbetter; primaryrisk+37.62percent/norm3.209timesvsfull. SixRMSregressionsvsfull(worst+51.22percent); no>1percentRMSregressionvsmodern969butoneCheb-queryMAXerror+25.70percent. Diagnostic1066amp88.51708/risk1.258704 andN969326.69193/4.401260are notprimarysuccesses.
- [P4MEASUREDhome](theory/pruning-p4-transfer.md) and [results](pruning-results.md) keepcost/function/pointcounttradeoffs. Counter4/15,11unused. DistinctP4actualchecks inprogressatthischeckpoint; no independenttimingreplicationclaimed.
- Compactessential[n12nodeartifact](evidence/pdpr-pruned12-nodes.json) uses546canonicalIDs, no bulkcoordinates. Completeexactmodularcheck rank455/prime313/root10/minor106 and distinctmonomialprime937/root15/minor702 plusrepository-onlyreplays establish [PROVEDidealcosinedetermination](theory/pruning-exact12.md). M546>N455, so uniqueLS, not arbitrary546-valueinterpolation. RoundedqualityremainsMEASURED; actualP3coordinatehashlinkverified. Artifactverification0researchrounds; n16artifactawaitsitsownvalidatedcheck.

### Completed five-round pruning outcome and portable exact sets

- P5protocol0e26f3e, finaldriver5133f213/core12456d1a. All48/100reflectionpairs rank-admissible; zero training-feasible,45/100noise-feasible. No operational deletion. Best training ratios1.405160/1.438422 exceed1.25; diagnostic searchedratios1.45646/1.53205alsofail1.30. All17distinctfits(18aliases) and targets/searches complete3.946726CPU. Distinct148fresh-SVDpair checks, frozenreruns and freshrefinements confirm the scopedfailure. No fullpairedtrajectory follows.
- P4actualsupplement completesPASS: source/input/raw/prefix/map/targets/noise andfreshrefinement checks agree. Reviewerfixed its own finite-differenceoracle sign crossing at h1e-6; sign-stable stepsconverge and no producerdefect found. Failed/lost harness executions remain disclosed inreview/receipt, never claimed successful. No independenthardwaretimingreplication.
- Essential[n16nodeartifact](evidence/pdpr-pruned16-nodes.json) now12581bytes; exactrank969at1163cosine nodes via p5441/root4639/minor330 and distinctmonomialp6529/root58/minor1257. Both geometry/roundedP4linkage and portableproducer/independent exactreplaysPASS. [PROVEDapplication](theory/pruning-exact16.md) is determining/uniqueLSonly; rounded qualityremainsMEASURED. Degree12artifact remainsunchanged/backwardsverifiable. Allproof-artifactwork0researchrounds.
- [Summary](pruning-summary.md) and [usable recipes](usable-recipes.md) give the two deliveredsets and theirlimits. Publicload+physicalOLSexampleactuallyran for12/16, ranks455/969, errors7.99e-15/7.11e-15on64seededqueries. No newconstructionround.
- Final counter5/15completed,10unused; oldU1/U2/U3counts4/7/5unchanged. P1/P2/P5specific preservationroutes stop; P3/P4usefulfixed-count endpointsretained. No further experimentregistered/running; no quota spending. Widerchanged-support/block/all-degree questions remain OPEN/deferred as documented, not rejected by these tests.
- Ordinarychat1Dcontext: computed classic Chebyshev-Lobatto and endpoint-scaled Chebyshev-root examples with barycentricweights and scalar maximization perinterval, degrees10/16/100. Numericalvalues2.42097/2.72471/3.89419 and2.06874/2.34498/3.47786 respectively; not certified exactoptima or a pruningresearchround. Classical families/readinglimits in existingBrutman/Ehlich-Zellerrecords; no newliterature/ID/priorityclaim.
- StageAUDIT, formalClaudeaudit04stillPENDING preservinghandoff15/11/09scope, oldsource/E4decisions and explicituncovereditems. Publishalloutputs beforestatus-onlyclose16/new17. OnlyACmerges; no IDs/ranges/sharedregistry/readiness/merge/archivaldelivery.
