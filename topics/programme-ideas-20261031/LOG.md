# Programme-scale research directions (ideas campaign)

- Branch: `claude/programme-ideas-20261031` · Base: `d36722823441dc40c6e19d69a174459348dd309c` (= `origin/main` at start) · Developer: Claude · Auditor: Codex (`gpt-6-astra`)
- Stage: AUDIT · Next: `Codex (gpt-6-astra xhigh): Continue claude/programme-ideas-20261031.`
- Claims: no PD-T. Outcome: 0 programmes, 1 project proposal (`proposal-1.md`, gen4-2), 19 candidates refuted/equivalent/abandoned/deferred (`gate-rejected.md`); 20 IDEA records (`ideas/candidates.md`); MEASURED and PROVED-in-file by-products listed in `report.md` §3. One PD-N candidate (below), not registered by the developer.
- For the PR: the rule amendment below (material rule change, to be audited by Codex); provisional `LIT?programme-ideas-claude-NN` and `IDEA?programme-ideas-claude-NN` records; allocations through the shared ledger `topics/padua-batch-20261031/ALLOCATIONS.md`.
- Open for AC: (1) whether to pursue `proposal-1.md` (a 2–3-paper classical-approximation project with a criterion-5 fit flag; its immediate deliverable is the certified maxima-count correction to arXiv 2605.23299 at n = 6, 7, 8); (2) whether the gen2-3 √δ-sharpness negative (`checks/adversarial-gen2-3.md` §(iii)) becomes a PD-N scoped for (b) LZ-034/L3 — the developer leaves this to the audit; (3) final-ID reservation from the MZ ledger owner at PR preparation (20 IDEA, up to 111 LIT minus duplicates with the charter/MZ/Lanczos blocks, 0–1 PD-N).

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
- **Step 3 — gate** (`9bf5bd3`; Fable 5.1 xhigh, one agent). `gate.md`: 9 pass items = 7 distinct programmes after two merges (gen4-draft-3 → gen1-draft-1 as M1; gen2-draft-4 → gen2-draft-2 as M2) and one absorption (gen4-draft-5 → gen4-draft-2); 6 rejected; 3 deferred; coverage statement over all 20 titles; factual flags on the drafts handed to the adversarial checkers. The gate ran no web search.
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

## Runs needed

None. Everything ran on the orchestrator's container; the step-5 scripts under `checks/code/decisive/` take 5–16 minutes each if rerun.
