# Readiness check 01 — PR 32

- **Checker:** Claude, Opus 5.5 high, independent auditor and readiness orchestrator (handoff [06](handoffs/06-readiness.md)). One Claude worker (Opus 5.5 high) reviewed the shared-registry diff by script and by reading. It changed no Git state or files.
- **Input:** `446b14d4ceb1e96cb8148e463872e7306f8051bb`, plus handoff publication `a16715f`. The preparation diff was reviewed from `2f23ee8` (MINOR and reservation checkpoint `37547f3`). Main is `76ba4214b100c86a44941f5e9a662ce9ce48efb8`, unchanged, so no merge was needed.
- **Rules:** read at `a16715f`. AGENTS.md, agents/ and templates/ are unchanged since `64a45b3`.
- **Scope:** this is the readiness check after the accepted [audit-02](audit-02.md), not a new audit round. The application made no material change beyond the accepted scope.
- **Decision:** **READY for AC's merge decision**, subject to the merge-time refresh rule below. Only AC merges.

## Shared-registry diff

Files changed outside the topic: PROOF_STATUS.md, state/IDEAS.md, ID_CROSSWALK.md, state/CURRENT.md, RESULTS.md, results/nn-mop-conditioning-20261106.md and the PD-T448 record topics/nn-mop-stability-20261105/theory/conditioning-growth-target.md. PAPER_MAP.md changed only through the auditor fix below.

- **Final IDs:**
  - All 33 assigned IDs (PD-T502–517, PD-N181–183, IDEA-590–603) occur exactly once as a PROOF_STATUS or IDEAS row and once as a crosswalk row.
  - None occurs on main.
  - The gaps PD-T518–521, PD-N184–185 and IDEA-604–607 are unused anywhere.
  - No LIT allocation.
- **Status and aliases:**
  - Every row's status equals its theory file's Overall status: 11 PROVED, 4 MEASURED (PD-T505/507/514/516), 1 OPEN (PD-T515), and PD-N181–183 PROVED with their candidates REJECTED: failed at subroute scope.
  - Each theory and candidate file carries its final ID and a dated alias section.
  - Every provisional alias is in ID_CROSSWALK.md, including both agentless gauge aliases and the C2 r4–r6 subforms. The one exception is the unused handoff-01 placeholder `PD-T?nn-mop-cond-codex-NN`, recorded in preparation/inventory.md.
- **Links:** all 187 added links resolve.
- **Scope of rows:** no row states a stronger claim than its audited record.
  - PD-T513 is a row rate plus a full-map liminf lower bound only.
  - PD-T517 is restricted to b-dominance and the two benchmarks.
  - PD-T515 is a distinct forward OPEN target; PD-T449 is unchanged.
  - PD-T511 is all-N benchmark Hahn normality.
- **IDEA edits** to IDEA-090/117/531/533/535 are justified by PD-T509 or the PARTIAL application, and no deferred scope is completed.
- **PD-T448 PARTIAL:**
  - The Statement section is byte-identical to main.
  - The five-part decomposition matches the accepted classification: one PROVED conjunct (PD-T509), the rest OPEN.
  - The earlier OPEN rationale is retained verbatim in History.
  - The D1 mechanism questions are declared OPEN leads outside the registered statement.
- **Process stage:** none in the shared registries.
- **RESULTS.md:** append-only. Main's bytes are an exact prefix. The new section equals the results file without its next-step line, and other sections are untouched.

## Audit-02 MINOR dispositions, confirmed by diff

| Item | Confirmation |
|---|---|
| MINOR-1 | Fixed: no pending-process text remains in attempts/C2-hard.md, the gauge theory or the gauge candidate |
| MINOR-2 | Fixed: c2-sharp-upper.md:7 and report.md point to the itemized OPEN conjuncts |
| MINOR-3 | Fixed: dated benchmark-scoped updates in c1-gauge-invariants.md, c1-hahn-gauge-lower.md and novelty-gate-C1.md |
| MINOR-4 | Fixed: LIT-507/508 shortlist row and forward/inverse distinction in the gauge gate; LIT-508 power-of-2 comparison in the gauge theory |
| MINOR-5 | Fixed: Hahn inputs identified after per-measure normalization |
| MINOR-6/7 | Optional: handled by documented limitations in external-code.md. `git diff 2f23ee8..446b14d -- code` is empty, so there is no result-bearing code change |
| MINOR-8 | Fixed: the pre-grid and exploratory M2 receipt roles are distinguished; decimal versus bit transport is recorded as a likely but unproved explanation |
| MINOR-9 | Fixed: agent-qualified gauge aliases, with the historical ones kept |

## Auditor in-place MINOR fixes

These are committed separately in `5e82abdb9c675dbcb551c923847c0f3b2cc2cafc`. They are wording, formatting and link fixes only, within the auditor-fix limits of WORKFLOW **Proportionate audit and records**.

I applied that rule because this is the topic's third review pass after audit-01 and audit-02. The developer may dispute any fix; disputes go to AC.

1. **ID_CROSSWALK.md**, the PD-T448/449 relations paragraph: added the PD-T448 → PD-T509 solved-conjunct relation and the PARTIAL status, with a link to the record. Removed the stale "OPEN" for PD-T448.
2. **PAPER_MAP.md**, the conditioning/stability note row: PD-T448 is now shown as PARTIAL, with PD-T509 PROVED and the remainder OPEN, and a link to the record.
3. **PROOF_STATUS.md**, PD-T448 row:
   - the per-part statuses moved into the "Status by mathematical part" column, matching the layout of the PD-T075 PARTIAL row;
   - the scope moved into the statement column;
   - the predecessor audit-01 and audit-02 links that the application had dropped are restored.

   Contents are unchanged.
4. **state/CURRENT.md**, the conditioning paragraph: reworded so the Krawtchouk N32 A-LU breakdown is not read as a completed solve.
5. **state/IDEAS.md**, the IDEA-602 row: "Equivalent exact-evaluator restatement abandoned" becomes "Exact-evaluator restatement abandoned". This matches attempts/C3.md and the final-ID map, which give disposition "abandoned" only.
6. **candidate-result-map.md:** added the two missing alias lines, `PD-T?nn-mop-cond-codex-C1-05` → `PD-T506` and `C1-07` → `PD-T508`. They were already correct in ID_CROSSWALK.md and final-id-map.json.
7. **response-gauge-candidate.md:45:** "(provisional ID)" becomes "(PD-T517)".

## Reservation refresh (immediately before readiness)

The live PR listing shows open PRs 27, 31, 32 and 33. All 28 closed PRs are merged, so there is no closed-unmerged reservation to retrieve.

I read every ALLOCATIONS.md and the registries (PROOF_STATUS, IDEAS, INDEX, ID_CROSSWALK, RESULTS, CURRENT) at each head:

| Head | SHA | Highest IDs used or reserved (PD-T / PD-N / IDEA / LIT) |
|---|---|---|
| main | `76ba4214b100c86a44941f5e9a662ce9ce48efb8` | 501 / 180 / 589 / 632 |
| PR33 | `d0e1bbb267db9928de97538d9b524fb0068538cd` | no new reservation |
| PR31 | `dd57b6439d539164cdee7ab01a11b6080a03af10` | ranges T522–553 / none / IDEA608–615 / LIT633–635 |
| PR27 | `d4956aea3bda9d5ff9917a5b410778fc7adf4fb7` | older ranges T392–431 / N146–161 / IDEA490–529 / LIT598–613 |
| PR32 | `5e82abdb9c675dbcb551c923847c0f3b2cc2cafc` | T502–521 / N181–185 / IDEA590–607 / none |

The 1750 maximum that a raw LIT grep returns comes from foreign BTTB aliases, not Padua LIT IDs. The INDEX row maximum on main is LIT-630, and main's ledgers reserve to 632.

PR31's ledger checked PR32's reservation at `37547f3` and starts above it. Our priority is the first commit containing our ledger, `37547f3`, which is linked from PR32.

**Conclusion: collision-free.** Our ranges are disjoint from every other reservation, all earlier priorities and permanent gaps are preserved, and no allocation in any namespace needs changing.

**Merge-time rule:** if main or any open PR's ledger changes between this check and AC's merge, repeat the check before the merge (WORKFLOW reservation step 7).

## Verification

- `python topics/nn-mop-conditioning-20261106/code/verify_evidence.py`: PASS, 89 committed identities. This is byte verification only. No code, input or evidence identity changed during preparation or in the auditor fixes.
- `git diff --check 2f23ee8..446b14d` (the preparation diff) is clean, and so is `git diff --check` on the auditor fixes.
- Whole-branch `git diff --check origin/main..HEAD` flags only:
  - deliberately pinned data bytes: the CRLF c4-tables/c1-grid.csv and the receipt's final newline;
  - one trailing blank line in the audit-01 script `audit-01/claude/C/t3_param_growth_lib.py`.

## NOTE (no action needed for readiness)

1. **PD-T448 dependencies.** The PROOF_STATUS row's Depends-on lists PD-T511/512/513 but not PD-T510. The record lists PD-T510, the general-parameter lower bound, as a supporting dependency. A dependency edit is material, so I left it unchanged; the record is canonical. It can be aligned in a later registry maintenance.
2. **Crosswalk detail.** The new PD-N181–183 rows show only "PROVED", without the candidates' `REJECTED: failed`, which PROOF_STATUS and IDEAS do carry. The crosswalk says unused headroom remains permanent without listing T518–521/N184–185/IDEA604–607; ALLOCATIONS.md lists them.
3. **Heading in the PD-T448 record.** conditioning-growth-target.md's "Final ID aliases" section lists PD-T509/511 provisional IDs, which are not aliases of PD-T448. "Identifiers mentioned" would read better.
4. **Results file.** results/nn-mop-conditioning-20261106.md keeps a next-step line, which is allowed in a topic file and was correctly dropped from RESULTS.md. It goes stale on merge.
5. **Not executed:** licensed Advanpix experiments, a fresh external source execution, and cold-storage delivery, as recorded throughout. Audit-01 and audit-02 reviewed the M2/M4 source gates from receipts only.
