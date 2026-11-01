# Codex audit-04 — PR #6 integration and bookkeeping

- **Decision: ACCEPTED after the directly authorized bookkeeping repairs. Stage PR; no unresolved integration finding within this scope. Only AC merges.** The scientific acceptances and OPEN/MEASURED limits from audits 02/03 remain unchanged.
- Requested candidate/rules: `37820a528c863e5cfe2dc2f1f8879b4fd40cf210`. Main boundary: `21e620ba8b5f0e0706f3a8c6613517df04d9d469`. Previous audit delivery: `f4e213390f66a8c9f0c6bd65131b97b78db873c8`.
- Administrative repair: `60e8ecf7bf5a171af02fec589583fa135dee2709`. Later delivery changes record this review, evidence and AC's updated integration order; they do not change the repaired allocation/literature inputs or accepted mathematics.
- Reviewer/orchestrator: Codex, AC-requested `gpt-6-astra high`; three supplementary reviewers explicitly received that allocation for disjoint allocation, literature and preservation checks. Resolved runtime model/effort metadata is not independently exposed. Date: 2026-11-01 UTC. Root alone controls Git and the PR.
- AC's follow-up authorizations: **“you have to fix all bookkeeping without more claude rounds”** and **“make pr6 clean without any history lost. the next one will be pr13 with rules update, then 11, 9 and 12 that need refreshment”**. Root made the administrative repairs under those instructions; separate supplementary reviewers checked the allocator and literature repairs. No further Claude response is required for this scope. This is not presented as a new Claude audit of Codex scientific development.

## Scope and dispositions

This review covers final-ID installation, main/registry integration, literature registration retention/deduplication, preservation and the squash rehearsal. It does not reopen the accepted mathematics, introduce a mechanism, certify maxima completeness, clear novelty, or reread unavailable source/archive bytes. A fresh full-IDEAS novelty gate is therefore inapplicable; complete registry inventories and the affected full records/maps were read or parsed for the integration checks.

| Item | Finding at the requested source | Final disposition |
|---|---|---|
| Final allocation and AC authorization | Ranges/map/provenance/records/ledger agree; no collision | Accepted; IDs and map retained byte-for-byte |
| LIT-I1, P2 — imported literature fields | Inner formula pipes corrupted three INDEX rows and created three bogus CORPUS keys | Repaired and independently checked; closed |
| INT-I2, P2 — squash rehearsal description | The whole-head #12 squash is not clean after upstream squashes; clean results require the dependent topic-only changes | Documentation corrected; both prepared heads rehearsed, including AC's updated #13 order; closed for PR #6 |
| ADM-I3 — allocator rerun | Default dry run at `37820a5` rejects its own 192 installed IDs | Read-only installed-state validation repaired; positive and malformed-input checks pass |
| ADM-I4 — current audit/allocation metadata | Live registry text still said re-audit pending/no row accepted, with stale provisional and merge-next wording | Current metadata/frontier corrected; historical snapshots and rules retained |
| Preservation | No unexplained change to accepted science or prior evidence | Accepted, with the precise historical-checker caveat below |

The original source findings/reports/receipts remain in `audit-04-support/`; repair receipts supplement them. Existing audit reports were not edited to erase a finding. All Git publication is additive: no rebase, reset, force-push, tag change or live PR merge. Removing the three bogus *current* source-key rows does not remove their Git history, and the original finding receipt retains their exact text.

## Allocation

Claude allocated `6954664` under AC's 2026-11-01 member-specific authorization: “allocate this block now” and “are the lattice ids allocated now? if not, do that as well”. That owner exception is explicit in the ledger; the old single-owner/provisional instructions are retained as dated history.

| Namespace | Lattice | Programme-ideas | Next unreserved |
|---|---|---|---|
| PD-T | PD-T081–094 (14) | PD-T095–100 (6) | PD-T101 |
| PD-N | PD-N032–038 (7) | PD-N039–043 (5) | PD-N044 |
| IDEA | IDEA-177–189 (13) | IDEA-190–209 (20) | IDEA-210 |
| LIT | LIT-300–331 (32) | LIT-332–426 (95) | LIT-427 |

The independent inventory reconstructs the exact map, not only the endpoints. **192 new IDs are unique and each has one primary registry row**: 32 PD, 33 IDEA and 127 LIT. All 208 provisional entries have the proper crosswalk disposition, comprising 192 allocations and 16 literature aliases. All 32 PD records and 33 IDEA entries have the proper canonical Final ID line immediately below the provisional heading; provisional headings, baselines, aliases and the lattice provisional map remain provenance. The ledger's ranges, counts and boundary agree.

Main `21e620b` ends the Lanczos block at PD-T080, PD-N031, IDEA-176 and LIT-292. Exact PR #11 head `97968d2c2d039cb0910e0ea50747fb2d9e01a262` has seven primary rows and reserves **LIT-293–299**. Neither its reservation nor main's IDs collide with these allocations. The checked allocation map remains unchanged by the repairs.

The original script's default invocation was actually executed in isolated snapshots: at `37820a5` it exits 1 on its own installed IDs, while allocation-parent inputs with the identical script exit 0 and reproduce the blocks/next values. Both snapshots remain unchanged. The repaired helper now recomputes the map, requires exact equality with the installed JSON, validates unique correctly aliased primary rows and crosswalk targets, and returns before every write. It refuses reapplication of an installed map. **No invocation used `--apply`.**

Independent repair testing executes nine isolated cases: valid installed and preallocation snapshots pass; altered map, duplicate primary ID, wrong ordinary/merged crosswalk target, missing primary row, wrong alias and absent map with allocated registries reject. All nine leave bytes unchanged. This is administrative validation, not a new mathematical checker. [Original allocation review](audit-04-support/allocation-report.md); [repair review](audit-04-support/allocation-repair-report.md).

## Main merge and literature

Merge `3e0100f` has the declared main parent `21e620b`. Every line of main's five shared registries survives in original order at the merge. The 49 removed branch CORPUS rows all have main replacements: 15 older rewritten citations and 34 duplicate registrations. The inherited Lanczos scientific subtrees match main exactly; they are not unexplained new programme science.

The two dedupe maps and applied crosswalk agree: first pass `ad45de2` merges rows 48→LIT-002 and 60→LIT-010; second pass `af3881b` merges fourteen more (01→193, 03→195, 04→197, 06→198, 09→199, 17→183, 30→174, 32→148, 33→149, 35→152, 36→153, 37→161, 44→099, 78→130; targets have prefix LIT-). There are **16 aliases, 95 remaining programme rows and 32 lattice rows**. The bounded statement/record comparisons support those aliases with their retained coverage qualifications; no inherited source fact becomes a locally proved theorem.

**Row 58 remains an overlap**, final LIT-375, with the unsupported Pitman RN 312 attribution flag retained. The second map has 14 same, 38 overlap, 3 unrelated and **20 explicit open comparison flags**. Nineteen retained INDEX rows link the flag; merged row 06 retains its corners/edges discrepancy in the map. First-pass flags also remain explicit. These are accepted source-reading/attribution limits, not cleared claims. No new fulltext acquisition or priority adjudication is claimed.

LIT-I1 concerned registration corruption, separate from those flags. Baseline rows 16/52/73 contain absolute-value/cardinality pipes. Their INDEX registrations LIT-342/369/389 lost statement/source/locator/verification fields; CORPUS gained formula fragments `c`, `Y`, `x±y` as keys. Root restored the exact baseline content and coverage, escaped internal pipes, retained overlaps and row 73's paper/book warning, and removed the three bogus keys. Correct source entries/aliases already exist. Placeholder gap wording now honestly leaves citation verification pending after final allocation.

Independent repaired-input checks verify all **95 retained programme rows**, seven valid Markdown cells per row, complete statement/source/locator/verification and reading-coverage retention, all aliases/flags, row 58 and the 34 cleanup replacements. The original pinned receipt exits 1 for twelve field mismatches; the repaired committed-input receipt exits 0 with none. Maps, baseline and ID JSON are byte-identical. [Original finding](audit-04-support/literature-review.md); [repair review](audit-04-support/literature-repair-review.md).

## Squash integration and AC's current order

AC's sequence is **#6 → #13 (rules update) → #11 → #9 → #12**. PR #13 is pinned at `10f2d8592673866ed0aa5ca73cef88d7541183ed`; this review checks its integration compatibility only, not its separate protocol-audit acceptance. Its rules are not imported into PR #6.

The root executed real squash steps/checkpoint commits only in disposable local branches/worktrees, then removed them. PR #9 is pinned at `7b8884a2f98518784ff3698dd2f3f9c49c9cdd62`. PR #12's documented head is `c26a6adf6ebf701368f5de73fc319b0e55cdfc13`; its refreshed head is `44be0080c69495cc6959e3d4c2b602fa73678d76`.

- Main → #6 → #11 and reverse #11 → #6 auto-merge, including the ledger.
- Prepared #9/#12 **own-topic diffs** apply cleanly for both #12 heads. Their stale inherited topic/registry copies are not reapplied.
- AC's updated sequence through #13, #11 and the prepared #9/#12 changes also passes. It preserves all 192 allocated primary rows, all seven #11 rows, #6's scientific/audit/code content and its Fable rule amendment. The only expected rule differences are the separate #13 changes to AGENTS/WORKFLOW.
- A raw whole-head #12 squash after the upstream squash sequence gives **20 conflicts**: five shared registries and fifteen programme files. The documentation now states this limitation and the refresh prerequisites instead of promising a clean whole-head merge. This remains visible in the receipt.

After AC merges #6 and the separately audited #13, refresh #11 against that main without moving its reserved block. After #11 lands, refresh/retarget #9 to main with its own topic changes only; after #9 lands, do the same for #12. Refreshes must preserve the merged final-ID registries and audit records. This is a prerequisite for those later PRs, not an unresolved PR #6 bookkeeping defect. Their branches were not rewritten or modified here. [Exact instructions](pr-prep.md); [rehearsal receipt](audit-04-support/rehearsal-repaired.json).

Whole-squash whitespace diagnostics retain pre-existing trailing whitespace in historical scientific scripts. The actual administrative diff passes `git diff --check`; scientific scripts were not reformatted to conceal those diagnostics.

## Preservation and evidence

All **197 protected programme audit/support/code/rule files** are byte-identical from `f4e2133` to the repaired candidate. All `agents/` and AGENTS are unchanged on PR #6 since that baseline. Against main, only the already disclosed Fable ideas-campaign amendment differs in `agents/WORKFLOW.md` and `agents/claude/CLAUDE_ROLES.md`.

Allocation itself only inserts Final ID paragraphs in the 36 canonical PD/IDEA homes; removing those paragraphs restores allocation-parent bytes. The post-audit T01 stabilizer clarification predates allocation and is the disclosed audit-03 preparation refinement. The bookkeeping repair preserves 35 canonical homes byte-for-byte; the remaining lattice README changes exactly two administrative provisional-ID sentences. All scientific statements/statuses, primary IDEA dispositions, accepted proof content, numerical producers/outputs and previous audits remain unchanged.

The lattice audit-time checkers and stored results remain historical receipts at their pinned revisions. More precisely, they compare earlier provisional row identities/counts; they do not literally contain an “Unallocated” assertion. One may exit 0 while reporting differences. Neither that exit code nor the old stored output is represented as a current final-allocation pass. New integration checks provide that current evidence. [Preservation review](audit-04-support/preservation-review.md).

Executed commands from repository root include:

```text
python3 -I topics/programme-ideas-20261031/audit-04-support/allocation-check.py
python3 -I topics/programme-ideas-20261031/audit-04-support/preservation-check.py
python3 -I topics/programme-ideas-20261031/audit-04-support/literature-check.py
python3 -I topics/programme-ideas-20261031/audit-04-support/allocation-repair-check.py
python3 -I topics/programme-ideas-20261031/audit-04-support/literature-repair-check.py 60e8ecf7bf5a171af02fec589583fa135dee2709
python3 -I topics/programme-ideas-20261031/audit-04-support/integration-repair-check.py
python3 -I topics/programme-ideas-20261031/audit-04-support/rehearsal-check.py 60e8ecf7bf5a171af02fec589583fa135dee2709
python3 -I topics/programme-ideas-20261031/pr-prep/allocate.py
git diff --check
```

Receipts identify inputs by Git revision/blob or SHA-256/size, Python version, actual outputs and limitations. The root pinned literature rerun binds the independent working-tree approval to repair commit `60e8ecf`; the impact receipt verifies protected files and the authorized path set. The final support manifest binds evidence files by size/SHA-256. All new evidence is small; no large numerical output or external cold-storage claim is added. No unchanged expensive mathematical sweep was repeated.

The review is complete for PR #6. No further Claude bookkeeping round is requested. Source comparison flags, OPEN targets and dependent-PR refreshes remain explicit continuing work. Only AC merges.

Suggested next prompt: `Codex (gpt-6-astra high): Audit PR #13's rules update after AC merges the clean PR #6, then refresh the integration plan for #11, #9 and #12 without renumbering or losing history.`
