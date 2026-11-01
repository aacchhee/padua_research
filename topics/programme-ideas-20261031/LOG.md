# Programme-scale research directions (ideas campaign)

- Branch: `claude/programme-ideas-20261031` · Base: `d36722823441dc40c6e19d69a174459348dd309c` (= `origin/main` at start) · Developer: Claude · Auditor: Codex (`gpt-6-astra`)
- Stage: PR (preparation) — Codex audit-03 ACCEPTED response-02 for B1–B4, with nonblocking N1/N2 notes. PR #6 remains draft pending ordinary preparation. Next: `Claude (Opus 5.5 high): Continue claude/programme-ideas-20261031 — prepare PR #6 after accepted audit-03, address N1/N2 with an exact impact check, and reconcile registry/literature work.`
- Submitted claims at `614709d`: no PD-T; 0 programmes, 1 project proposal (`proposal-1.md`, gen4-2), 19 candidates refuted/equivalent/abandoned/deferred (`gate-rejected.md`); 20 IDEA records (`ideas/candidates.md`); by-products in `report.md` §3. Audit-01 preserves finite measured evidence but rejects certification, several universal/negative claims and status/provenance overreach. The project is provisional; no certified replacement table or final PD-N is accepted.
- For the PR: the rule amendment below (material rule change, to be audited by Codex); provisional `LIT?programme-ideas-claude-NN` and `IDEA?programme-ideas-claude-NN` records; allocations through the shared ledger `topics/padua-batch-20261031/ALLOCATIONS.md`.
- Response-01 (2026-11-01, claude-opus-5-5): all of A1–A9 accepted; eight THEORY records added in `theory/` (PD-T?programme-ideas-claude-01…06, PD-N?programme-ideas-claude-01, 02); scope corrections inline in the evidence files and in the summaries; campaign inputs pinned in `sources/campaign-inputs/`. See `response-01.md`.
- Current open decisions: whether to pursue the smaller project; final-ID reservation and literature deduplication at coordinated PR preparation. The five negatives retain the accepted scopes/statuses from audit-02; audit-03 accepts the B1–B4 correction response, with N1/N2 for preparation. The certified-correction premise remains unaccepted. A9.8 is disposed by AC's acceptance recorded in the addendum; the standing model-allocation rule is unchanged.

## Rule amendment (first commit on this branch)

AC explicitly asks to change the rules (2026-10-31). The amendment adds Claude Fable 5.1 at xhigh effort as an allowed Claude model for ideas campaigns: brief writing, conceptual candidate generation, duplicate gating and adversarial idea checks. Every existing row is kept, the Codex column is unchanged, and the developer/auditor separation, evidence rules and status words remain binding. The amendment reaches `main` only through this topic's PR, and the Codex audit must cover it as a material rule change.

### agents/WORKFLOW.md — "Roles and model allocation" table

Before (last table row, followed directly by the "Use agentic orchestration" paragraph):

```
| Adversarial audit, novel mechanism, or a stalled proof | `gpt-6-astra`, xhigh; ultra only with written justification | Opus 5.5, xhigh |

Use agentic orchestration: ...
```

After (one row and one paragraph added; nothing removed):

```
| Adversarial audit, novel mechanism, or a stalled proof | `gpt-6-astra`, xhigh; ultra only with written justification | Opus 5.5, xhigh |
| Ideas campaigns: conceptual generation, gating and adversarial idea checks | unchanged (rows above apply) | Fable 5.1, xhigh (added 2026-10-31 at AC's explicit request); Opus 5.5 xhigh remains allowed |

The Fable 5.1 row is restricted to ideas campaigns: brief writing, candidate generation, duplicate gating and adversarial idea checks. It does not change the developer/auditor separation, the evidence rules, the status words or the Codex column. Where an ideas campaign runs a tiny sanity script, Sonnet 5.5 high remains the development model for it. Record the actual model and effort in every commit trailer and log entry.

Use agentic orchestration: ...
```

### agents/claude/CLAUDE_ROLES.md — "Development", first paragraph

Before:

```
Use Sonnet 5.5 high for code and technical development, Sonnet 5.5 medium for mechanical work, and Opus 5.5 high or xhigh for mathematics. Record the model and effort. Delegate bounded tasks with explicit inputs, expected artifacts, acceptance criteria, and disjoint ownership; do not delegate Git authority.
```

After:

```
Use Sonnet 5.5 high for code and technical development, Sonnet 5.5 medium for mechanical work, and Opus 5.5 high or xhigh for mathematics. For ideas campaigns (brief writing, conceptual candidate generation, duplicate gating and adversarial idea checks) Claude Fable 5.1 at xhigh effort is also allowed, as recorded in the `agents/WORKFLOW.md` allocation table (added 2026-10-31 at AC's explicit request); Opus 5.5 xhigh remains allowed for the same work. Record the model and effort. Delegate bounded tasks with explicit inputs, expected artifacts, acceptance criteria, and disjoint ownership; do not delegate Git authority.
```

### agents/claude/CLAUDE_ROLES.md — "Independent audit", first paragraph

Before:

```
The auditor chooses the model and depth: Sonnet 5.5 high or Opus 5.5 high for protocol/technical audit; Opus 5.5 high or xhigh for mathematics; Opus 5.5 xhigh for adversarial analysis or a novel mechanism. Record the choice and its reason.
```

After:

```
The auditor chooses the model and depth: Sonnet 5.5 high or Opus 5.5 high for protocol/technical audit; Opus 5.5 high or xhigh for mathematics; Opus 5.5 xhigh for adversarial analysis or a novel mechanism; for an adversarial idea check inside an ideas campaign, Fable 5.1 xhigh is also allowed. Record the choice and its reason.
```

Other rule files (`AGENTS.md`, `agents/codex/CODEX.md`, templates) are unchanged.

## 2026-10-31 — Claude, orchestrator (claude-fable-5-1; effort not exposed by the runtime)

- Rules read at the branch head before amendment: `d36722823441dc40c6e19d69a174459348dd309c` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md). `git fetch origin main` returned the same SHA; the branch starts there.
- Parallel topics seen on `origin` at start: `codex/charter-unisolvence-20261031` (head `eb7bdcd`), `claude/bivariate-lanczos-20261031` (head `55320df`), `codex/mz-constants-20261031` (head `e9761aa`). None of them changes `agents/` or `templates/`. The charter branch carries a standalone ledger reserving `PD-T001–012`, `PD-N001`, `LIT-001–041`, `IDEA-001–051`; the other two use provisional IDs only. No `topics/padua-batch-20261031/ALLOCATIONS.md` exists on any branch yet; this topic creates it.
- Roles: Claude develops (orchestrator plus Fable 5.1 xhigh reasoning subagents, Sonnet 5.5 high for tiny sanity scripts), Codex (`gpt-6-astra` xhigh) audits.
- Novelty gate: applies to the campaign; recorded per step below (`state/IDEAS.md` on `main` is empty, but the three parallel branches seed it, so the gate reads their registries too).

## 2026-10-31/11-01 — Claude, orchestrator (claude-fable-5-1): steps 0–3

Subagents are launched as background `general-purpose` agents on `claude-fable-5-1`; the effort is passed per launch and recorded in each file's `Model:` line and in the commit trailers. Sonnet 5.5 was not used: no step needed a script that a reasoning agent did not write itself as part of its check (probe scripts are preserved under `checks/code/`).

- **Step 0 — literature baseline** (`65e9441` checkpoint, `a02bc35` final; Fable 5.1 xhigh). `lit/baseline.md` with 111 rows `LIT?programme-ideas-claude-01…111`: 41 VERIFIED against a fulltext (23 against local PDFs, 8 via the Lanczos branch's complete-fulltext records, 10 partial), 70 UNVERIFIED. Three full records under `lit/records/` (Sauer 2007; Sommariva–Vianello 2015; Harris–Simanek 2021). Attribution corrections are listed in `lit/baseline.md` (HL SIMAX p. 1088 is an observation, not a conjecture; HL print no O(MN^{3/2}); Xu 1994 covers only dim Π_{n−1} nodes; BJ 1985 print no "2k+1"; Sauer Def. 2 p. 305 / open question p. 307; TW629 author order Mach, Van Barel, Vandebril). The shared registries `literature/INDEX.md`, `literature/CORPUS.md`, `literature/records/` were deliberately NOT edited; the baseline merges into them at PR preparation, after the charter/MZ blocks, with the 14 keys shared with the Lanczos branch reconciled then.
- **Step 1 — brief** (`624a7ae`; Fable 5.1 xhigh). `brief.md`: state (with a table of MEASURED facts), branch-level exclusion boundaries of (a)–(d) and the already-judged reasons, an 11-row obstruction table with exact hypotheses, 14 template theories (9 named in the inputs, 5 not), pointers. **Word count: 2228 words in total, of which 1257 prose and 965 in tables.** The 1500-word target is met by the prose and exceeded when tables are counted; the tables were kept because the generators cite them by row. (The `624a7ae` commit message says this is recorded here; it was recorded only now.)
- **Step 2 — four parallel generators** (`4ccaa6c` checkpoint; `103b8ed` A, `6bfb740` B, `dd6a3a9` C, `a8d6b7f` D; four Fable 5.1 xhigh agents, one angle each). 20 drafts in `checks/state/` (gen1-1…6, gen2-1…4, gen3-1…5, gen4-1…5); 12 returned, 8 not returned by the generators' own status lines. Probe scripts preserved under `checks/code/gen{1,2,3,4}/`; their outputs are MEASURED pre-gate evidence within the scopes stated in the drafts.
- **Step 3 — gate** (`9bf5bd3`; Fable 5.1 xhigh, one agent). `gate.md`: 9 pass items = ~~7 distinct programmes~~ 9 distinct candidates (eleven drafts; response-01, audit-01 A9.1) after two merges (gen4-draft-3 → gen1-draft-1 as M1; gen2-draft-4 → gen2-draft-2 as M2) and one absorption (gen4-draft-5 → gen4-draft-2); 6 rejected; 3 deferred; coverage statement over all 20 titles; factual flags on the drafts handed to the adversarial checkers. The gate ran no web search.
- **Shared ledger.** This topic created `topics/padua-batch-20261031/ALLOCATIONS.md` at `8f500db`. The MZ Codex orchestrator then pushed `c989031` to this branch, replacing it with the reconciled batch ledger (allocation owner: root Codex MZ orchestrator; charter PR #2 merged at `08fafe62…`; MZ PR #3 next; next unreserved `PD-T029`, `PD-N007`, `LIT-066`, `IDEA-077`). Adopted as instructed: `origin/main` (`08fafe6`, charter merged) was merged at `2554433` and the add/add conflict in the ledger resolved by keeping `c989031`'s bytes (sha256 `39dfc9a9abcffcc7e8d28caf0c537a9dcf4536b42186cc00991ee67b33516f56`). Final IDs for this topic will be requested from that owner at PR preparation, after merging main again if PR #3 has landed.
- **Trailer note.** The first commit `7eeffd8` carries `Agent:`/`Model:` in a paragraph above the `Co-Authored-By`/`Claude-Session` lines, so only the last paragraph parses as trailers. History is not rewritten; from `8f500db` on, all four lines sit in one final paragraph.

## 2026-11-01 — Claude, orchestrator (claude-fable-5-1): steps 4–7, Stage AUDIT

- **Step 4 — adversarial checks** (`d5de3af` gen4-1, `09b4e92` gen1-2, `c11ea54` gen3-1, `fc08bb1` gen2-3, `7b990bf` gen1-3, `0c561c0` gen3-3, `e5040c4` M2, `4e89c13` M1; gen4-2 final in `b18c828`/`c3313ee`). Nine agents, one per pass item: M1 and M2 on claude-fable-5-1 at **max** effort (AC allowed "a few agents at fable max"), the other seven at xhigh. Web search authorized by AC (2026-10-31 22:21); ≈ 441 logged web actions in total (per-file counts in each search log; blocked fetches included). Verdicts: KILLED (ii) M1, M2, gen1-2, gen2-3, gen3-1, gen3-3, gen4-1 (each with an independent second reason recorded); WOUNDED gen1-3, gen4-2. Scripts/outputs under `checks/code/adv/<id>/`, MEASURED within stated scopes; gen4-1's agent ran one flagged n = 24, 40 probe (0.9 s) outside the n ≤ 8 instruction to expose a tolerance artefact. Several gate adversary targets were refuted in the gate's disfavour while the candidates died for other reasons (`gate-rejected.md`, loose ends).
- **Step 5 — decisive tests** on the two wounded candidates. Pre-registrations committed before any run: gen1-3 at `a8364b9`, gen4-2 at `2310424`. Results: gen1-3 RESIDUE KILLED (`3a52a9d`; K3 fired); gen4-2 RESIDUE CONFIRMED as a 2–3-paper project (`b13f8ea`; no kill fired). Wall times exceeded the "seconds to a few minutes" budget: gen1-3 ≈ 16 min (eight 80-bit reference runs), gen4-2 T1 ≈ 14 min (n ≤ 200, chunked after an out-of-memory at n = 200), T2 ≈ 7 min, T3 ≈ 5 min; all on the orchestrator's container, declared in the files. gen4-2's T3 certified maxima counts (n = 3…8: 15, 27, 25, 41, 50, 62; margins ≥ 1.5e-6, IEEE double, no interval arithmetic) disagree with arXiv 2605.23299 at n = 6, 7, 8.
- **Step 6** — `gate-rejected.md` and 18 IDEA records (`d9c3491`, step 6a, xhigh); `report.md`, `proposal-1.md`, records 03 and 17, gen1-3 section appended to `gate-rejected.md` (`2516123`, step 6b, xhigh). Coverage verified by script: all 20 draft titles appear in `gate-rejected.md` or `proposal-1.md`; 20 IDEA records present.
- **Step 7** — `checks/state/` removed in one commit (`a7efd96`; drafts remain in history to `2516123`). This LOG entry; Stage set to AUDIT.
- **Shared state.** MZ PR #3 merged into `main` (`07c5f54`); merged into this branch at `51266b9` with no conflicts; ledger bytes unchanged (sha256 `39dfc9a9…`). Both merge commits (`2554433`, `51266b9`) carry git's default merge message without Agent/Model trailers. Final IDs are still provisional (`IDEA?programme-ideas-claude-01…20`, `LIT?programme-ideas-claude-01…111`); the reservation request to the ledger owner and the merge of `lit/baseline.md` into `literature/INDEX.md`, `CORPUS.md` and `records/` (deduplicating against the charter, MZ and Lanczos entries) are PR-preparation tasks after the audit. `state/IDEAS.md` on `main` is not edited by this topic until then.
- **Models actually used.** Every reasoning subagent: claude-fable-5-1 (xhigh; M1/M2 adversaries max). Sonnet 5.5 was not used — no step needed a standalone script outside a reasoning agent's own check. Orchestrator: claude-fable-5-1 (effort not exposed by the runtime). Subagent counts: 1 baseline, 1 brief, 4 generators, 1 gate, 9 adversaries, 2 decisive, 2 writers (step 6a/6b) = 20 agents.
- **Known irregularities for the auditor.** (i) Brief at 2228 words including tables (1257 prose). (ii) First commit `7eeffd8` trailer paragraph. (iii) Task statements to the gate and step 6a said 11 returned / 9 not returned; the drafts' status lines say 12 / 8 — the files follow the status lines. (iv) Two generator scripts are faulty and are kept as evidence of what the drafts did not measure: `checks/code/gen1/sobolev.py` does not run; `checks/code/gen4/gen4_tests16.py` uses D_{|j|} for D_{n−|j|} and the wrong target constant (corrected in `checks/code/adv/gen4-2/adv_rhombus_L1.py`). (v) In-progress checkpoint commits during steps 4–5 (stop-hook requirement) contain intermediate script states; final states are the hand-back commits named above. (vi) Step-5 wall times over budget, as above.
- **For the Codex audit**, in order of weight: the rule amendment (material rule change, first section of this file); the nine adversarial verdicts and whether any kill is unsound (the strongest claims are M2's one-page proof, M1's DST 2005 reading, gen2-3's √δ sharpness, gen4-2's certified counts); the two pre-registered decisive tests; the honesty of `report.md` §0–§2; the provisional-ID discipline.

## 2026-11-01 — Codex independent audit-01; Stage WORK

- Candidate and rules read: `614709d4a60fb0c2593b05764e8d5aceda1be381` (AGENTS, WORKFLOW, Codex role and amended Claude role). Current main fetched/checked: `07c5f5465d6de306aa81dbe8ca1f615295163864`, already an ancestor of the candidate; no base reconciliation merge needed. Original development base remains recorded above.
- Model/effort requested by AC: `gpt-6-astra xhigh`; root plus four inherited, disjoint supplementary audit agents. Resolved runtime model/effort metadata is not separately exposed. Root owns all Git operations; independent agents wrote only new audit-support files.
- Decision: **CHANGES REQUIRED**, [audit-01.md](audit-01.md), findings A1–A9. This is the requested Claude-to-Codex handoff, not a developer approving its own work. No developer proof/checker/source report was silently fixed; the current log/stage and audit artifacts are the only changes.
- Independent reruns reproduce all six candidate maxima counts (15/27/25/41/50/62); a separate Vandermonde inverse validates all 220 listed points numerically. Completeness remains unproved. Exact counterchecks refute the submitted universal Ritz/saturation converse (`s=27/175`, both residuals zero) and universal three-dimensional pattern commutant (Padua n=2 dimension 6). Preregistered fit uncertainty reproduces at approximately ±3.3e-5; ±2e-12 is a later model-conditioned fit-stability range. Primary K3 instability, AH finite examples, polygon diagnostics, M1 word identities and M2 dimensions were actually rerun; exact scopes and commands are in the four support reports/manifests.
- Novelty discipline: full state/IDEAS.md and its obstruction/disposition tables, literature index and relevant predecessors read. No new programme generated. The 20 IDEA records and all 20 historical drafts are retained; the 111 LIT rows and three source hashes verify. Nine distinct adversarial groups, not seven, need the factual correction in A9.1. Missing campaign context and unpinned transferred source records remain A8.
- Rule amendment: actual diff inspected; confined to the documented Fable campaign row and Claude role paragraphs. Codex allocations/evidence/status rules and other protected files are unchanged. The audit does not rewrite or silently waive the retained Sonnet-script sentence; the original AC amendment request is recorded in the developer log, not independently available as a primary conversation receipt.
- Access/provenance: initial default-sandbox shell fetch failed. GitHub connector fetched 155 pinned files with paths/blob identities; explicit supported executor network permission then enabled Git fetch. Snapshot bytes were compared with source Git objects without mismatch. New publication worktree: `/workspace/programme-integration`; original `/workspace/padua_research` checkout preserved. `audit-support/source-manifest.json` and `protocol-check.json` preserve input identities and structural receipts.
- Publication is a **draft, changes-required handoff**. Shared scientific state, final IDs and batch ledger remain unchanged. No readiness, final literature integration, integration rehearsal or merge is claimed. Source/checker outputs and historical audit records remain intact. External cold-storage/Windows delivery remains unclaimed.
- Next: Claude responds in `response-01.md`, fixes or narrows each unsupported claim, supplies durable result/provenance records, then returns material changes at an exact SHA for Codex re-audit. Only AC merges.

## 2026-11-01 — Claude, developer response-01 (claude-opus-5-5; effort not exposed); Stage AUDIT

- Rules read at `988f9126e9c3b6e7a378c7f60c3cd309bb3dc4a3` (unchanged rule files). AC authorised refreshing the registry against merged main (08:17 CET): `origin/main` `0d058fb` (PR #4 lattice, PR #5 MZ post-merge) merged at `04234cd`, no conflicts; ledger takes main's prose, reservations unchanged. Registry rescan: no overlap of the new lattice/MZ rows with any retained claim; closest entry for the provisional project remains charter IDEA-048; ≈ 10 duplicate LIT rows to deduplicate at PR preparation.
- Model: AC switched the session from Fable 5.1 to Opus 5.5 before this response; Opus 5.5 is the allocated Claude model for mathematical development. No subagents. One new developer script (`checks/code/response-01/inertia_two_node_family.py`, SymPy 1.14.0, exact; output beside it).
- Response: `response-01.md` (all nine findings accepted). New THEORY records `theory/programme-ideas-claude-{01..06,N01,N02}-*.md`. Corrections inline in `checks/decisive-gen4-2.md`, `checks/decisive-gen1-3.md`, `checks/adversarial-{gen4-1,M2,gen2-3,M1,gen3-1}.md` with originals struck through; `proposal-1.md` rewritten; `report.md`, `gate-rejected.md`, `ideas/candidates.md`, `gate.md`, `brief.md`, `lit/baseline.md` revised with notes pointing to `614709d`.
- Provenance (A8): `sources/campaign-inputs/` — five input files committed; `provenance.json` pins 159 snapshot files to repository blobs; cold-storage snapshot of RESULTS.md (13399-byte version) and research_notes delivered to `C:\Users\andreyac\Downloads\padua\cold_storage\programme-ideas-20261031\` and read back with matching SHA-256 (`COLD_STORAGE.md`).
- A9.8 deviation: the amended rule text keeps Sonnet 5.5 high for tiny sanity scripts in ideas campaigns; the campaign's Fable agents wrote and ran their own scripts. No AC override is on record; deviation documented; disposition open for AC. Model history is not rewritten.
- Response content committed at `6dc547b4216c8b1a98d6b8e78065bad4b695a671`; the following commit only records this SHA here. Re-audit target: the branch head containing this line.
- Not claimed: certification of the maxima counts; proofs of the corner expansion or argmax; any final ID; any registry integration; any message to external authors.

## 2026-11-01 — Claude, response-01 addendum (claude-opus-5-5; effort not exposed)

- AC (08:47 CET): "do not worry about the model. register negative results. state clearly what needs to be proven, well make a few attempts".
- A9.8: deviation accepted by AC ("do not worry about the model"); rule text unchanged.
- Registered provisionally in `PROOF_STATUS.md`, `state/IDEAS.md`, `ID_CROSSWALK.md`: PD-T?programme-ideas-claude-01…06, PD-N?programme-ideas-claude-01…05 (N03–N05 new: joint-Ritz converse refuted in general; Padua n = 2 pattern commutant of dimension 6; Fourier-basis commutation refuted on the tested instances), all 20 IDEA rows and an obstruction/disposition table. Final IDs remain for PR preparation through the batch-ledger owner.
- New exact developer scripts: `checks/code/response-02/{ritz_converse_parity,padua_pattern_commutant,padua_n3_edge_identity}.py` with outputs (SymPy 1.14.0).
- `OPEN_TARGETS.md`: precise statements of everything that still needs proof, with known evidence, done-criteria and first routes.
- Addendum committed at `c8c8eec23c16601fbf02086de4623a445fc5f1bc`; the next commit only records this SHA. Re-audit target: the branch head containing this line.

## 2026-11-01 — Codex independent audit-02 of response-01 with addendum; Stage WORK

- Candidate/rules read: `cadb35066160e466cb1704b9791ad6f374446422`; refreshed main: `9739a0c56b7a3976422ce60a8441bfbbfd6554df`, already an ancestor. The current local-results rule came from main; this audit makes no rule change. Working checkout was clean before fast-forwarding to the exact candidate.
- Auditor allocation: AC-requested `gpt-6-astra xhigh`; four inherited supplementary agents with disjoint new `audit-02-support/` ownership. Resolved runtime model/effort metadata is not separately exposed. Root alone performs Git operations. Full current ideas/obstruction/disposition tables and relevant theory/source records read; no new mechanism or historical novelty clearance.
- Decision: **CHANGES REQUIRED**, [audit-02.md](audit-02.md), B1–B4. Restricted N01/N03/N04 mathematical statements accepted as PROVED; N02/N05 accepted as MEASURED in their actual tested scopes. Positive T01–T03 accepted under their written hypotheses, subject to the minor finite-gauge terminology correction; T04/T05 remain OPEN and T06 MEASURED. These claim-level acceptances do not make the campaign ready.
- Remaining major issue: live canonical IDEA-17 still asserts certified undercounts and twelve-digit second-order precision (B1), despite corrected proposal/report/theory. IDEA-10 retains an unqualified orbit-count conclusion (B2). The computed-section target's "nearby" needs a metric/radius/constant quantifiers (B3); B4 groups minor scope, finite-dimensional target and proof-completion clarifications. No developer claim was silently fixed by the auditor.
- Actual independent executions: new exact inertia/Padua-commutant/parity/edge scripts reproduce; separate unequal-weight/non-product projector and exact nodal checks pass; commutator and M2 dimension diagnostics rerun. All 125 original campaign code/output files and 31 audit-01 files remain byte-identical to their pinned revisions. Expensive unchanged maxima/high-degree/80-bit sweeps were not repeated.
- Provenance/registration repair: all 159 history-backed sources and five context rows verify; six context checksums, eleven theory records with registry links/statuses, twenty IDEA rows and 111 LIT rows verify. Root fetched the recorded Lanczos input head to check its immutable histories. Private Windows ZIP/PDF bytes were not re-retrieved here; the audited manifest and developer-reported readback retain that explicit access limit. A9.8 is disposed by the logged AC acceptance, without another permission request or rule/history rewrite.
- New support reports, commands, output/content identities and source pins are in `audit-02-support/`. Root structural receipt and `git diff --check` pass. Original audits/checkers, developer sources and shared registries remain intact. Draft PR #6 is updated for this handoff; no final-ID allocation, readiness or merge is claimed.
- Next: Claude answers B1–B4 in `response-02.md`, preserves accepted scopes and both audit records, and returns an exact SHA for focused review. B1/B2 need record corrections, not new numerical campaigns. Only AC merges.

## 2026-11-01 — Claude, developer response-02 (claude-opus-5-5; effort not exposed); Stage AUDIT

- Rules read at `39c5ae6` (unchanged rule files plus the merged local-results rule); main `9739a0c` already an ancestor.
- `response-02.md`: B1–B4 accepted. B1/B2 canonical remnants in IDEA-17, IDEA-10 and `checks/decisive-gen4-2.md` struck or labelled historical; B3 rewritten with explicit classes, metric, gap, reference neighbourhood and constant dependence; B4.1–B4.7 scope, definition and done-criterion fixes in N03, N05, PD-T01, `OPEN_TARGETS.md` and the registry rows. No status changed; no expensive rerun.
- New exact check: `checks/code/response-02/ritz_saturated_centre.py/.out` (saturated centre, s = 1, residuals 0; SymPy 1.14.0).
- Response-02 content committed at `a8fc06cfb3c5a30cc5efe5569ed3cd5b32463aea`; the next commit only records this SHA. Focused-review target: the branch head containing this line.

## 2026-11-01 — Codex audit-03 focused review of response-02; Stage PR (preparation)

- Candidate/rules read: `0ef90edc5b4d5639474cca7fa8d6d688e684e505`; refreshed main `9739a0c56b7a3976422ce60a8441bfbbfd6554df`, already an ancestor. Rule files are unchanged from audit-02. Root fast-forwarded the clean topic checkout to the exact target; no history rewrite or new base merge.
- Reviewer allocation: AC-requested `gpt-6-astra high`, plus one independent supplementary reviewer explicitly assigned the same model/effort for the target/gauge changes. Resolved runtime metadata remains unexposed. Root alone controls Git; supplementary ownership is confined to a new audit-support report.
- Decision: **ACCEPTED for B1–B4**, [audit-03.md](audit-03.md). Canonical IDEA-17/10 remnants are superseded explicitly; the target class/metric/radius/constants and B4 refinements resolve the substantive findings. No result status or final ID changes. Expansion/argmax remain OPEN; counts/rational/Fourier observations remain MEASURED; accepted restricted proofs are preserved.
- Nonblocking N1/N2: finish legacy certified/cheap-paper wording cleanup in the historical decisive record, and state positive-gap/constant/obstruction-sequence conventions in OPEN_TARGETS B3 before using it as a proof task. These are preparation notes, not new theorem refutations or requests for numerical campaigns. The independent target review is `audit-03-support/targets-review.md`.
- Verification actually executed: new saturated-centre developer checker/output reproduced exactly; independent cardinal-polynomial/nodal and rank checks confirm s=1 and zero residuals; declared similarity/weighted-symmetry substitution checked symbolically. All 184 existing code/output and prior audit-support files compared are unchanged; both prior audit reports, rules/crosswalk and all eleven statuses are preserved. Root receipt, source hashes and commands: `audit-03-support/check-response-02.py/.json`. Python 3.12.14, SymPy 1.14.0; no expensive unchanged sweeps repeated.
- Focused scientific correction cycle is complete. Stage PR authorizes preparation, not merge or a readiness claim. PR #6 remains draft for coordinated ID decisions, literature deduplication/integration, current audit metadata and the applicable integration check/rehearsal. The reviewer did not silently repair developer files or claim external archival verification. Only AC merges.

## 2026-11-01 — Claude, PR preparation after accepted audit-03 (claude-opus-5-5; requested effort high); Stage PR

- Rules were read at the branch head. They are unchanged from audit-03 (the local-results rule is on main). Main `9739a0c` is already an ancestor.
- N1/N2 are accepted and fixed in `c93c912` (decisive record wording, OPEN_TARGETS B3 gap/constant/negative-form conventions, PD-T01 (d) stabiliser {±I}). Impact check: 3 prose files changed; statuses, registries, code, outputs, audit records, `agents/` and the ledger are byte-identical. Details are in [pr-prep.md](pr-prep.md).
- Literature and registry integration is in `ad45de2`:
  - the `literature/INDEX.md` provisional block has 109 rows (51 overlap, 58 new); rows 48 and 60 are merged into LIT-002 and LIT-010 with no new ID;
  - the `literature/CORPUS.md` provisional key block has 112 keys;
  - `ID_CROSSWALK.md` gains 20 IDEA rows and 111 LIT rows;
  - the deduplication map is `lit/integration-map.json/.md` (Sonnet 5.5 helper; spot-checked).
- Squash rehearsal from `9739a0c`:
  - PR #6 `ad45de2` is clean;
  - PR #9 `a09d910` adds 27 files under its own topic and is clean on top;
  - PR #10 `a2dd845` (Lanczos) gives five end-of-file append conflicts in the shared registries, resolved as the union with all added lines preserved. Both orders were rehearsed; the trees differ only in block order.
- PR #10 has allocated PD-T029–080, PD-N007–031, LIT-066–292 and IDEA-077–176. The next free IDs for this branch are PD-T081, PD-N032, LIT-293 and IDEA-177. If PR #10 lands first: drop the 34 duplicate CORPUS keys, and re-deduplicate the 54 INDEX rows whose sources PR #10 also registers.
- Decision for AC: keep the provisional IDs at merge (lattice precedent), or allocate final IDs after PR #10 (ledger owner or explicit authorisation). Recommended order: PR #10 → PR #6 → PR #9. PR #6 stays draft until AC decides. No final ID is allocated. Only AC merges.

## 2026-11-01 — Claude, re-integration after PR #10 merged (claude-opus-5-5; requested effort high); Stage PR

- Main `21e620b` (PR #10) is merged in `3e0100f`. The five registry append conflicts are resolved as the union, and 34 duplicate CORPUS keys are dropped.
- The second literature dedupe against PR #10's LIT-066–292 is in `af3881b`: 14 same (merged, no new ID), 38 overlap, 3 unrelated and 20 flags. The INDEX block is down to 95 rows. Row 58 was overridden to overlap. The helper was Sonnet 5.5; I reviewed all 15 of its "same" calls.
- Rehearsal from `21e620b` with #6, #11, #9 and #12 is clean in sequence, and #11-first auto-merges. Details are in [pr-prep.md](pr-prep.md).
- Next free IDs: PD-T081, PD-N032, IDEA-177 and LIT-300 (draft #11 reserves LIT-293–299). AC still has to choose between provisional IDs at merge and final allocation. No ledger edit, no final ID. Only AC merges.

## 2026-11-01 — Claude, final-ID allocation at AC's instruction (claude-opus-5-5; requested effort high); Stage PR

- AC's instructions: "allocate this block now", then "are the lattice ids allocated now? if not, do that as well". The lattice IDs were still provisional on main (66 of them, deferred), so both blocks were allocated in `6954664`:
  - lattice: PD-T081–094, PD-N032–038, IDEA-177–189 and LIT-300–331;
  - programme-ideas: PD-T095–100, PD-N039–043, IDEA-190–209 and LIT-332–426;
  - next unreserved: PD-T101, PD-N044, IDEA-210 and LIT-427.
- Generator and map: `pr-prep/allocate.py` and `id-map.json`. Registry blocks, crosswalk, records and the ledger are updated, and provisional IDs are kept as provenance. No status change. The rehearsal with #11, #9 and #12 is clean. Details are in [pr-prep.md](pr-prep.md).

## 2026-11-01 — Codex audit-04 integration review and AC-authorized bookkeeping repair

- Rules/candidate read: `37820a528c863e5cfe2dc2f1f8879b4fd40cf210`; main `21e620ba8b5f0e0706f3a8c6613517df04d9d469`. AC requested `gpt-6-astra high`; three disjoint supplementary reviewers used that explicit allocation. Runtime-resolved metadata is unavailable. Root alone controls Git and PR metadata. No new novelty-bearing work or accepted-mathematics review.
- Allocation review passed: 192 unique final IDs, 208 provisional crosswalk records, 16 aliases, canonical Final ID lines and all scientific statuses preserved; exact #11 head `97968d2` reserves LIT-293–299. Main merge preserves every main registry line, and all 49 removed branch CORPUS rows have main replacements (15 rewritten, 34 duplicate). Original audit/code/rule files are unchanged.
- Found three pipe-parsing registration defects and an incomplete description of the dependent squash rehearsal. AC then instructed: “you have to fix all bookkeeping without more claude rounds”. Root restored the baseline fields/coverage of LIT-342/369/389, removed three formula-derived CORPUS keys, repaired stale audit/allocation/frontier wording and made the allocation helper's default check work after installation. All allocated IDs/maps, mathematical statements/statuses and existing audits/checks/code/agents are preserved. The README edits affect administrative ID wording only.
- Independent repair checks pass for literature retention and the allocator's read-only positive/negative cases. Current source-comparison flags remain recorded limits, not new mathematics or cleared source claims. Rehearsal documentation now requires own-topic-only dependent changes after upstream squashes; raw #12 whole-head conflicts are explicitly recorded. No other live branch is modified.
- Detailed findings, dispositions and final integration verification will be retained in `audit-04.md` and the small new `audit-04-support/` artifacts. Only AC merges.

## Runs needed

Finish the pinned repaired-candidate rehearsal/impact receipt, write audit-04 and update draft PR #6. No Claude response round is requested: AC authorized Codex to complete the administrative repairs directly. Scientific certification/source-reading tasks remain in the canonical OPEN targets and comparison maps; no unchanged expensive replay or independent Windows-archive retrieval is claimed.
