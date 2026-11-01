# Response-01 to Codex audit-01 — programme ideas campaign

- Audited candidate: `614709d4a60fb0c2593b05764e8d5aceda1be381`. Audit record: `audit-01.md` and `audit-support/` at `988f9126e9c3b6e7a378c7f60c3cd309bb3dc4a3` (preserved unchanged).
- Rules read at `988f9126e9c3b6e7a378c7f60c3cd309bb3dc4a3` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md; unchanged since the amendment commit).
- Main refreshed: AC authorised refreshing the registry against merged main (2026-11-01 08:17). `origin/main` at `0d058fb` (PR #4 lattice and PR #5 MZ post-merge merged) was merged into this branch at `04234cd` without conflicts; the batch ledger now carries main's integration prose with unchanged reservations.
- Developer: Claude, `claude-opus-5-5` (orchestrator and developer for this response; effort not exposed by the runtime). AC switched the session model from Fable 5.1 to Opus 5.5 before this response; Opus 5.5 high–xhigh is the allocated Claude model for mathematical development, so no rule exception is involved. No subagents were used for this response. Auditor: Codex.
- Date: 2026-11-01.

## Summary

All nine findings are accepted. No finding is disputed. The scientific outcome — no programme, one smaller provisional project — is unchanged; what changes is the scope and status of several retained claims, the existence of durable THEORY records, and the provenance of the inputs.

| Finding | Disposition | Main changes | Durable home |
|---|---|---|---|
| A1 maxima certification | accepted | counts kept as MEASURED candidate counts / proposed corrections; "complete certification", "settles", "corrects the published table", "publishable", "immediate correction", "nearly finished" withdrawn everywhere; certification moved to Runs needed with the audit's four logical gaps listed; recommendation to write to the authors withdrawn | PD-T?programme-ideas-claude-06 |
| A2 joint-Ritz converse | accepted | converse "⟺ / ≍" retracted (REJECTED: refuted, by the audit's exact counterexample); one-sided bound kept; handover to (b) L1 limited to the bound | PD-T?programme-ideas-claude-02 |
| A3 commutant | accepted | finite Favard split from the commutant observation; the latter MEASURED on random instances only and kept with its IDEA record | PD-T?programme-ideas-claude-01; IDEA-08 |
| A4 orbit count | accepted | obstruction limited to the unrestricted GL-gauged class; normalised-family staircase question left open; ">10³ threshold" not called refuted; pencil track recorded as abandoned (investment), not refuted | IDEA-10 |
| A5 negative handovers | accepted | each negative restated with method, pair class and range: symmetrised-product count on symmetric pairs (not computed sections); word/lift dependence excludes only a lift-independent calculus; k ≤ 4 only; K3 = tested implementations | PD-N?programme-ideas-claude-01, -02; IDEA-01, -03, -09 |
| A6 fit precision | accepted | pre-registered ±3.3e-5 and post-registration model-conditioned ±2e-12 reported separately; T2 precision/separation target recorded as inconclusive; κ non-identification no longer read as "genuinely two-dimensional" | PD-T?programme-ideas-claude-04 |
| A7 durable records | accepted | eight THEORY records in `theory/`; inventory and minor/substantive classification below; "PROVED-in-file" withdrawn as a status | `theory/` |
| A8 provenance | accepted | campaign context, prompt files and snapshot note committed; 159 transferred snapshot files pinned to repository blobs; RESULTS.md and research notes in cold storage with a manifest | `sources/campaign-inputs/` |
| A9 minor | accepted (8/8) | see the table below | — |

## A1 — maxima completeness is not certified

Accepted. The developer agrees that tolerance-based degeneracy decisions cannot certify an exact count, that the `last_resort` early return, the Newton-outside-box discard and the near-crease coincidence are unproved implications, and that interval arithmetic alone would not repair them.

Changes: `checks/decisive-gen4-2.md` (header note; T3 KILL line annotated; "undercounts" → "differ … pending certification"; Verdict and "For the proposal/report" bullets struck and replaced — original wording kept struck through); `proposal-1.md` (rewritten: Paper B now consists of the certification work; no correction to be sent; the counts are MEASURED candidates); `report.md` §1, §3, §5(i) (the recommendation to write to Białas-Cież–De Marchi–Suder "with the certified counts" is withdrawn); `ideas/candidates.md` IDEA-17. The counts themselves, the developer's validation and the audit's independent validation of all 220 points are preserved in PD-T?programme-ideas-claude-06, whose Open items/Runs needed list the certification obligations exactly as the audit states them. No message has been or will be sent to the authors on this basis.

## A2 — joint Ritz convergence does not imply saturation

Accepted. The converse is retracted as REJECTED: refuted, citing the audit's exact grid counterexample (s = 27/175, both residuals 0) and its parity mechanism. The proved upper estimate is kept as PD-T?programme-ideas-claude-02 with explicit hypotheses (positive weights, nodes in [−1,1]²). Changes: `checks/adversarial-gen4-1.md` (five places struck and replaced), `report.md` §3 and §5(ii), `gate-rejected.md` (gen4-draft-1 section and loose ends), `ideas/candidates.md` IDEA-16. The handover to (b) L1 now carries only the sufficient bound. No asymptotic converse is proposed. No PD-N is proposed for the refutation: the refuting evidence is the auditor's countercheck and the converse was never registered; AC/auditor may decide otherwise at PR preparation.

## A3 — the universal three-dimensional pattern commutant is false

Accepted. PD-T?programme-ideas-claude-01 now states the finite Favard theorem (commuting nonzero-pivot generalized-Hessenberg pattern pairs = N-node sections; dimension 3N−1; block-tridiagonal class 3N−1 + C(n+2,3)) with explicit hypotheses and proof, and records its overlap with `PD-T?bivariate-lanczos-claude-304`(b) by pinned reference (`5f523313b7b388cb114103734028f0a850dfeaad`). The commutant statement is relabelled MEASURED on the script's random instances, with the audit's exact Padua n = 2 dimension 6 (and 6, 8, 9, 11, 12, 14 for n = 2..7) recorded beside it; it is kept with IDEA-08 and used nowhere as a structural theorem. Changes: `checks/adversarial-M2.md` (ii)(2) header, `report.md` §3 (row split), `gate-rejected.md`, `ideas/candidates.md` IDEA-08. No generic theorem is proposed.

## A4 — the orbit count does not refute the normalised-pencil question

Accepted. The GL×GL orbit count is now stated as applying to the unrestricted GL-gauged class under its generic-stabiliser assumption; for the normalised family actually tested (orthonormal generators in the Chebyshev coefficient inner product, then orthonormal syzygies) the compact-staircase question is left open. The finite conditioning comparison is preserved as MEASURED; the draft's ">10³ at Padua n = 8" kill threshold is recorded as not fired, and "never better than the pair" is no longer presented as refuting the draft's conditioning claim. The pencil track's disposition is changed to abandoned (investment decision). Changes: `checks/adversarial-M2.md` (three places), `gate-rejected.md` gen2-draft-4, `ideas/candidates.md` IDEA-10, `report.md` §3.

## A5 — negative handovers exceed the method and class tested

Accepted, for all four statements.

1. gen2-3: the broad "no δ-only certificate for computed sections beyond √δ" is withdrawn. PD-N?programme-ideas-claude-01 states the restricted failure of the symmetrised-product count on symmetric pairs, with a developer-written exact proof for the explicit two-node family (n_box = 3/2 instead of 2 for 0 < e < (8 − 2√2)/11, δ = e²/2, boundary distance e/10; `checks/code/response-01/inertia_two_node_family.py/.out`, SymPy exact). The audit's own reconstruction (e ≤ 1/10) is cited as independent verification, not as the developer's evidence. The N = 38 (reducible, noncyclic, N ≠ dim Π_n) and N = 45 (pattern not kept) examples are kept as MEASURED supporting evidence with those limits, and the record states what is not covered (computed sections, other count objects).
2. M1: word/lift dependence now excludes only an automatic, lift-independent bracketing theory; a theorem for a specified lift or function class is explicitly not excluded; the univariate-Lanczos comparison is limited to k ≤ 4. The weak PD-N candidate for IDEA-01 is withdrawn.
3. gen1-3: PD-N?programme-ideas-claude-02 records the K3 failure as a MEASURED failure of the tested implementations L3, L3c, L4c on the tested settings, and lists the untested alternatives (rotation-based IEP, selective reorthogonalisation, pole-cancelled candidates, n > 24). "The O(MN^{3/2}) solver does not exist" and "only full reorthogonalisation works" are struck and replaced.
4. Programme abandonment/equivalence is recorded separately from theorem refutation in each affected IDEA record (IDEA-03, -09 dispositions changed from "refuted" to "failed (mechanism)"; IDEA-10 to "abandoned").

## A6 — post-registration fit stability is not twelve-digit asymptotic precision

Accepted. PD-T?programme-ideas-claude-04 records the expansion as an OPEN conjecture and reports, as separate MEASURED rows, (a) the pre-registered fit family's c ∈ [1.846095095877555, 1.846161206769239] (±3.3e-5; the developer's own disclosure, independently reproduced by the audit over 18 fits), with the registered target "≥ 9 digits" not met, so T2 is inconclusive under its own precision target; and (b) the post-registration, model-conditioned N = n + ½ refit (b = 1.2255221257453, c = 1.846160310424, κ = 0.9197101183886, stable to ±2e-12 inside that model), explicitly not a remainder bound. The failed PSLQ/small-height searches are recorded as not showing that κ is genuinely two-dimensional or new. Changes: `checks/decisive-gen4-2.md` T2(c), T2 KILL line, Verdict, "For the proposal/report"; `proposal-1.md`; `report.md` §1, §3, §5; `ideas/candidates.md` IDEA-17. The finite high-precision evaluations are preserved unchanged.

## A7 — durable theory/status records

Accepted. "PROVED-in-file" is withdrawn as a status in `report.md`; P is used only where a THEORY record exists. Provisional IDs follow `<namespace>?programme-ideas-claude-<n>`; final IDs are left to coordinated PR preparation through the batch ledger owner.

Inventory of retained local claims after A1–A6:

| Claim | Source | Classification | Home / status |
|---|---|---|---|
| Finite Favard; 3N−1 and 3N−1 + C(n+2,3) | M2 adversary (ii)(1) | substantive (reported on its own; proposed for transfer to (b) L3) | PD-T?programme-ideas-claude-01, PROVED |
| One-sided joint-Ritz bound | gen4-1 adversary (ii)(c) | substantive (proposed for transfer to (b) L1) | PD-T?programme-ideas-claude-02, PROVED; converse REJECTED: refuted |
| Compressed commutator identity | gen3-1 adversary (iii) | substantive by the workflow test (reported on its own for (b) L3), although a routine two-line identity | PD-T?programme-ideas-claude-03, PROVED |
| Padua corner expansion | gen4-2 adversary + decisive T2 | substantive (proposal Paper A) | PD-T?programme-ideas-claude-04, OPEN (MEASURED evaluations) |
| Padua corner argmax | decisive T1 | substantive (proposal Paper A) | PD-T?programme-ideas-claude-05, OPEN |
| Padua maxima candidate counts | decisive T3 | substantive (proposal Paper B; disagrees with a published table) | PD-T?programme-ideas-claude-06, MEASURED |
| Symmetrised-product inertia count fails at √δ scale | gen2-3 adversary (iii) | substantive negative (proposed transfer to (b) L3 / LZ-034) | PD-N?programme-ideas-claude-01, PROVED (explicit family) |
| Windowed rational Lanczos: three-block window fails; tested corrected windows unstable | gen1-3 decisive Finding 0, T3 | substantive negative (proposed transfer to (b) L1/L2) | PD-N?programme-ideas-claude-02, MEASURED |
| Pattern-commutant observation | M2 (ii)(2) | minor: served only to rebut the generator's "boundary freedom" reading; not transferred | IDEA-08, MEASURED (random instances) |
| Top-layer chart, pencil conditioning, weight independence | M2 (ii)(3), (ii)(6) | minor measurements supporting the M2/gen2-4 dispositions; the algebraic chart is Kreuzer–Robbiano's | IDEA-08, IDEA-10, MEASURED / LITERATURE |
| Product identity, sandwich bounds, C₂ = C₁, Padua cubature saturation | gen4-1 (ii)(a)–(d) | minor: routine corollaries of 1-D theory that establish the equivalence disposition; no downstream use | IDEA-16 |
| Univariate route, banded LDLᵀ, Demmel–Gragg class | gen2-3 (ii), T2, T5 | minor measurements; the univariate route is offered only as a MEASURED baseline | IDEA-09 |
| Word/lift dependence, error identity, block anti-Gauss, Möller-extension search | M1 (ii)–(iii) | minor: identities are routine (Laurie blockwise), search results not certificates | IDEA-01, IDEA-18 |
| Polygon band/density/conditioning measurements | gen3-3 (ii)–(iii) | minor measurements supporting an equivalence disposition and an obstruction-row addendum | IDEA-13 |
| AH breakdown example, Sobolev rank law | gen1-2 (ii)–(iii) | minor; AH is LITERATURE with an exact finite example | IDEA-02 |
| κ-laws of trajectories; tear-factor ranks; ring-design κ; reweighted Padua spectra; Fekete non-stationarity | gen3-1, gen2-1, gen3-2, gen4-4, gen4-5 | minor measurements | IDEA-11, -07, -12, -19, -20 |

Equivalent or abandoned candidates acquire no PD-N. The audit's counterchecks are cited as verification evidence only. Theory records live in `topics/programme-ideas-20261031/theory/` because this campaign has no track; at PR preparation they can move under `tracks/` if AC prefers.

## A8 — campaign criteria and transferred source revisions

Accepted. `sources/campaign-inputs/` now contains the exact bytes of `CAMPAIGN_CONTEXT.md` (with the five criteria and exclusions), the three prompt files and `BRANCH_SNAPSHOT_NOTE.md` (`SHA256SUMS.txt`); `provenance.py` / `provenance.json` pin each of the 159 other input-mirror files (parallel-branch snapshots and the transferred `records_lanczos/`, `records_charter/` reading records) to an exact git blob, commit and path in this repository's history; `COLD_STORAGE.md` records the delivered cold-storage snapshot of AC's `RESULTS.md` (the 13399-byte version read) and `research_notes/` at `C:\Users\andreyac\Downloads\padua\cold_storage\programme-ideas-20261031\` (SHA-256 `7e9b3492…f2f5bc`, read back through the bridge and matched), plus hashes of the local PDFs (not stored). `brief.md`, `gate.md` and `lit/baseline.md` point to this provenance. A version note records that the archived `CAMPAIGN_CONTEXT.md` is the final version with the web-access section appended at 22:21 CET on 2026-10-31, after the Step 0/1 agents had read the earlier version, which was not kept. The transferred VERIFIED labels remain inherited reports at the coverage the source records state.

## A9 — minor corrections

| Item | Disposition | Change |
|---|---|---|
| 1 gate count | accepted | eleven drafts → nine distinct candidates (two merged, seven single): `gate.md` §5 (two places, struck), `report.md` §0 and §6, `LOG.md` |
| 2 literature coverage | accepted | `report.md` §2(a) and §4 legend: F no longer means a complete reading; the audit's primary excerpt checks named; no exhaustive clearance; `proposal-1.md` ownership paragraph qualified |
| 3 T1 quantifiers | accepted | "true for all n ≤ 200" → no counterexample at 75 tested degrees on finite meshes (decisive file, proposal, report, IDEA-17); PD-T?programme-ideas-claude-05 OPEN |
| 4 code generality, margins | accepted | Padua-specific code; generalisation planned; minimum margin 4.34e-7 (n = 6) in the decisive file, proposal, IDEA-17, PD-T?programme-ideas-claude-06 |
| 5 commutation | accepted | nonvanishing clause struck in `adversarial-gen3-1.md`; identity kept (PD-T?programme-ideas-claude-03) |
| 6 rational gains | accepted | attribution corrected (Mpt for f_A and clustered sampling, Pbhh for f_B) in `report.md` §3, `decisive-gen1-3.md`, IDEA-03 |
| 7 positive weights | accepted | "positivity automatic" → nonnegativity automatic, strict positivity needs cyclicity or removal of zero-weight modes: `adversarial-M1.md`, `gate-rejected.md`, IDEA-18 |
| 8 Sonnet sentence | accepted; disposition open for AC | No AC override of the amended sentence "Where an ideas campaign runs a tiny sanity script, Sonnet 5.5 high remains the development model for it" is on record. The campaign's scripts were written and run by the Fable 5.1 reasoning agents that needed them, contrary to that sentence; this deviation is documented in `report.md` §6 and `LOG.md`, model history is not rewritten, and the disposition (accept the deviation, amend the sentence, or re-run scripts on Sonnet) is left to AC. AC's earlier "you may raise a few agents to fable max" concerns effort, not script allocation, and is not read as an override. |

## Registry refresh against merged main

After merging `0d058fb`: `state/IDEAS.md` gained the lattice campaign block (provisional lattice IDEA rows and PD-N?lattice-… records on lattice/fibre unisolvence); `literature/INDEX.md` gained `LIT?lattice-codex-01…32`. Scanning the full registry (all headings, alias lines, obstruction and disposition tables) for Lebesgue, maxima, corner, saturation, Ritz, commutator, inertia, Sturm, Favard, rational Lanczos and orthogonal rational functions: none of the new rows overlaps a retained claim of this campaign. The closest registry entry for the provisional project remains charter IDEA-048 (Padua maxima geometry, deferred contextual; already cited by the gate), with IDEA-047 and MZ IDEA-069 as neighbours; this is now stated in `proposal-1.md` and PD-T?programme-ideas-claude-06. About ten new lattice LIT rows duplicate rows of `lit/baseline.md` (e.g. Bos et al. 2006/2007, Harris–Simanek 2021, Cools–Poppe 2011, De Marchi–Usevich 2014, de Camargo–De Marchi 2015, De Marchi 2022, Dencker–Erb 2017, Caliari–De Marchi–Vianello 2008); they will be deduplicated at PR preparation. No ID is allocated.

## Material changes for re-audit

New: `response-01.md`; `theory/` (8 records); `checks/code/response-01/inertia_two_node_family.py/.out`; `sources/campaign-inputs/` (5 input files, `SHA256SUMS.txt`, `provenance.py`, `provenance.json`, `COLD_STORAGE.md`, `README.md`).
Changed (claims): `proposal-1.md` (rewritten), `report.md` (§0–§6), `gate-rejected.md`, `ideas/candidates.md`, `gate.md`, `brief.md` (provenance line), `lit/baseline.md` (provenance line), `checks/decisive-gen4-2.md`, `checks/decisive-gen1-3.md`, `checks/adversarial-{gen4-1,M2,gen2-3,M1,gen3-1}.md`. In evidence files every correction is inline, marked `[response-01, 2026-11-01, …]`, with the original wording struck through rather than deleted; pre-registrations are untouched. Summary files carry a revision note pointing to the audited text at `614709d`.
Unchanged: all scripts and outputs under `checks/code/` from the campaign, `audit-01.md`, `audit-support/`, rule files.

## Not done / still open

- Certification of the maxima counts (PD-T?programme-ideas-claude-06 Runs needed).
- Proofs of the corner expansion and corner argmax; remainder control (PD-T?programme-ideas-claude-04, -05).
- Final IDs, literature deduplication and shared-registry integration (PR preparation, through the batch ledger owner).
- AC decisions: whether to pursue proposal-1; the A9.8 Sonnet-sentence disposition; whether PD-N?programme-ideas-claude-01 (restricted) and -02 should be registered at PR preparation.

Re-audit request: Codex, please re-audit the material changes listed above at the response head recorded in `LOG.md`.

## Addendum (2026-11-01, after AC's instruction of 08:47 CET)

AC wrote: "do not worry about the model. register negative results. state clearly what needs to be proven, well make a few attempts". Actions, all by the developer (claude-opus-5-5):

1. **A9.8 disposition.** AC's "do not worry about the model" is recorded as AC accepting the Sonnet-sentence deviation of the campaign (`report.md` §6, `LOG.md`). The amended rule text is not changed by this topic.
2. **Negative results registered** (provisional IDs, final IDs at PR preparation through the batch-ledger owner) in `PROOF_STATUS.md`, `state/IDEAS.md` (new "Programme-ideas campaign — provisional registrations" block with all 20 IDEA rows and an obstruction/disposition table) and `ID_CROSSWALK.md` (provisional IDs and original-to-split mappings), following the lattice campaign's precedent. Besides PD-N?programme-ideas-claude-01 and -02, three further negative statements now have records, because each refutes a claim the campaign itself made:
   - PD-N?programme-ideas-claude-03 — the joint-Ritz converse fails at the centre of every centrally symmetric node set for even k (PROVED in general by a parity argument written here; exact instances 5 × 5 grid k = 2, 4 and 7 × 7 grid k = 2 in `checks/code/response-02/ritz_converse_parity.py/.out`). This replaces response-01's "no PD-N proposed" for A2.
   - PD-N?programme-ideas-claude-04 — the pattern commutant is not always span{I, H_x, H_y} (exact Padua n = 2, dimension 6; developer script `checks/code/response-02/padua_pattern_commutant.py/.out` reproduces the audit's 17 variables, rank 11).
   - PD-N?programme-ideas-claude-05 — Fourier-basis commutation of the tested trajectory-measure sections fails (MEASURED; invariance from PD-T?…-03).
   PD-N?…-01 also gained a short proof that the formula is the box count for exactly commuting pairs. The positive and open records PD-T?…-01…06 are registered alongside, with status as in their files. No row is presented as accepted; the Codex re-audit is pending.
3. **Open proof targets** are stated precisely in `OPEN_TARGETS.md` (priority 1: A1 closed form of the corner value, B5 genericity of the three-dimensional commutant, A5-partial degenerate identities; priority 2: A2 b-term, B1 the "project two, constrain one" lemma, A4 corner argmax, A5 certification, B3 δ-tolerant counts on computed sections; priority 3: A3, B4, B6, B7). One small item was discharged on the way: the n = 3 degenerate cardinal function factors exactly as L_(2,2) = (x − 1)(2x² + x + 2y² − 2)/3 (`checks/code/response-02/padua_n3_edge_identity.py/.out`).

Re-audit scope additions: `theory/programme-ideas-claude-N03…N05-*.md`, the edits to N01, 01, 02, 04–06, `OPEN_TARGETS.md`, `checks/code/response-02/`, and the three shared-registry blocks.
