# PR #6 preparation — programme ideas campaign

**Current status (audit-04):** the dated preparation stages below are historical. Final IDs are allocated. AC explicitly instructed Codex to fix all bookkeeping without another Claude round; the current repairs and exact squash-rehearsal scope are recorded in the final section. Scientific statuses are unchanged. AC’s current sequence is **#6 → #13 (rules update) → #11 → #9 → #12**, with later drafts refreshed against the preceding merges.

- Date: 2026-11-01. Developer/orchestrator: Claude, `claude-opus-5-5` (requested effort high; the runtime effort is not exposed). A Sonnet 5.5 helper produced the literature deduplication map, `lit/integration-map.json/.md`. I spot-checked its two same-statement mappings and its conflict flags.
- Starting point: audit-03 accepted B1–B4, with nonblocking notes N1/N2 and Stage PR (preparation), at `f4e2133`. Main is `9739a0c`, already an ancestor.
- Scope: preparation only. No status, scope or provisional ID changes. No final ID is allocated, and the batch ledger is not edited.

## Audit-03 notes

| Note | Disposition | Change (commit `c93c912`) |
|---|---|---|
| N1 legacy wording in `checks/decisive-gen4-2.md` | Accepted. | The remaining phrases ("certified pairs/list/maxima", "now on certified data", "identified numerically to 12 digits", "cheap first paper") are corrected inline with a `[PR preparation … audit-03 N1]` marker. The whole "For the proposal/report" recommendation is labelled historical and points to the operative records: PD-T04 and PD-T05 OPEN, PD-T06 MEASURED and not certified. The pre-registration text is unchanged. |
| N2 positive-gap convention in `OPEN_TARGETS.md` B3 | Accepted. | S(α) now requires 0 < C(n, p) < ∞ and g(H, Q) > 0, and says that α and C may depend on n and p. The negative form fixes n and p, takes 0 < δ → 0, names the *boundary gap* (as distinct from the pair distance) and is labelled a sufficient disproof, not the full logical negation. |
| (B4.3 wording) PD-T01 (d) | Tightened. | The stabiliser is exactly {±I} by cyclicity of e₁, as audit-03 states. The dimension and status are unchanged. |

**Impact check.** `git diff f4e2133 c93c912` touches 3 files (12 insertions, 8 deletions), all of them prose inside a topic record. No status word, registry row, code file or output changes. From `f4e2133` to the PR-preparation head, the following are byte-identical:
- every file under `checks/code/`;
- `audit-01.md`, `audit-02.md` and `audit-03.md`, and all three audit-support directories;
- `agents/`;
- the batch ledger.

## Registry and literature integration (commit `ad45de2`)

- **`literature/INDEX.md`** gains the block "Programme-ideas campaign — provisional registrations", with 109 rows. Fifty-one overlap an existing row from the same source (named in the coverage column) and 58 are new. Two baseline rows state the same fact as an existing row and are merged without a new ID:
  - LIT?programme-ideas-claude-48 → LIT-002 (also LIT?lattice-codex-14);
  - LIT?programme-ideas-claude-60 → LIT-010 (also LIT?lattice-codex-08).
- **Labels.** The baseline's statement-level verification labels are kept as they are. They do not upgrade any main row and confer no novelty clearance.
- **Conflict flags** for final allocation are listed in the block header: rows 76, 73, 49, 100, 101–102, 64 and 53.
- **`literature/CORPUS.md`** gains a provisional source-key block (112 keys not in the corpus at `9739a0c`). Five keys resolve to existing MZ entries and two are same-paper aliases of lattice keys; both are recorded in the block header.
- **`ID_CROSSWALK.md`** gains 20 IDEA rows and 111 LIT rows. The two merged rows are marked "Merged into … (same statement; no new ID)".
- No existing record or row is edited. All links in the new blocks resolve. `git diff --check` is clean.

## Squash-integration rehearsal

The rehearsal used disposable worktrees from `origin/main` `9739a0c` with the open PR heads: PR #6 `ad45de2`, PR #9 `a09d910` (base: this branch) and PR #10 `a2dd845` (`claude/bivariate-lanczos-20261031`, base main, opened after audit-03).

| Order | Result |
|---|---|
| main → PR #6 | Clean squash: 252 files. Outside this topic it changes only the 5 shared registries and `agents/WORKFLOW.md` and `agents/claude/CLAUDE_ROLES.md` (the Fable 5.1 ideas-campaign row added at AC's request on 2026-10-31). |
| → PR #9 | PR #9's diff from its merge base `cadb350` adds 27 files, all under `topics/padua-proof-attempts-20261101/`. It applies cleanly on top. After PR #6 merges, PR #9 must be retargeted to main. |
| → PR #10 | Conflicts in `ID_CROSSWALK.md`, `PROOF_STATUS.md`, `literature/CORPUS.md`, `literature/INDEX.md` and `state/IDEAS.md`. Each is a single end-of-file hunk where both PRs append a block, so the union resolution is to keep both blocks. Checked: every line either PR adds is in the result, and no main line is lost except the 14 `CORPUS.md` rows that PR #10 itself intentionally rewrites. Result tree `cc3b6e3`. |
| main → PR #10 → PR #6 → PR #9 | Same five append conflicts, same union resolution, PR #9 clean. Result tree `ff06462`, which differs from `cc3b6e3` only in the order of the appended blocks. |

Later commits on this branch touch only `pr-prep.md` and `LOG.md`, so they cannot change the rehearsal outcome. The rehearsal authorises no live merge, push to main or retarget.

## Interaction with PR #10 (bivariate Lanczos)

PR #10 allocated final IDs under AC's authorisation of 2026-11-01, recorded in its ledger block: PD-T029–080, PD-N007–031, LIT-066–292 and IDEA-077–176. It names programme-ideas as a later member that "must start from the 'Next unreserved after this block' column once this PR merges": PD-T081, PD-N032, LIT-293 and IDEA-177. The earlier plan (PD-T029–034 and so on) is therefore void.

If PR #10 merges first, this branch must do the following before final IDs:
- merge main;
- resolve the five append conflicts as above;
- drop the 34 CORPUS keys that PR #10 registers with full citations (`amsel-et-al-2026` … `zhu-nakatsukasa-2026`; the list is reproducible from the two CORPUS blocks);
- re-deduplicate against PR #10's 227 new LIT rows. Of this branch's 109 rows, 54 cite a source that also has a new PR #10 row: 35 of the 51 overlap rows and 19 of the 58 new rows.

The other 55 rows are untouched by PR #10.

## Decision requested from AC

Either:
1. **Provisional at merge** (the lattice precedent): merge with the provisional `?programme-ideas-claude-NN` IDs and allocate later through the ledger owner; or
2. **Final allocation now**: after PR #10 merges and the re-deduplication above, allocate from PD-T081 (6), PD-N032 (5), IDEA-177 (20) and LIT-293 (at most 109, fewer after merges). This needs the ledger owner, or an explicit AC authorisation like PR #10's.

Recommended order: PR #10 → PR #6 (after re-integration) → PR #9 (retargeted to main).

## Re-integration after PR #10 merged (2026-11-01)

PR #10 merged into main as `21e620b`. That makes the PR #10 section above historical, and its plan is now carried out.

- **Main merge** (`3e0100f`). The same five end-of-file append conflicts appeared and were resolved as the union. Every main line is kept. The only branch lines not kept are 15 old `CORPUS.md` rows that PR #10 rewrote. In the same commit, the provisional CORPUS block drops the 34 keys that PR #10 registers with full citations; they are listed in the block header.
- **Second literature dedupe** (`af3881b`; [integration-map-pr10](lit/integration-map-pr10.md), Sonnet 5.5 helper, developer-reviewed). The 55 rows citing a PR #10 source were compared with LIT-066–292:
  - **14 same.** These are merged without a new ID and marked in the crosswalk: 01 → LIT-193, 03 → 195, 04 → 197, 06 → 198, 09 → 199, 17 → 183, 30 → 174, 32 → 148, 33 → 149, 35 → 152, 36 → 153, 37 → 161, 44 → 099, 78 → 130.
  - **38 overlap.** Their PR #10 IDs are added to the coverage column.
  - **3 unrelated:** rows 40, 53 and 84.
  - **Row 58** stays an overlap (developer override of the helper's "same") because it carries an unsupported Pitman RN 312 attribution.
  - **20 comparison flags** are recorded for final allocation. Examples: the row 06 "4 corners" wording versus the printed "4 edges"; impossible ETNA page locators in LIT-131/132; the row 86 JAMS pages; the row 29 missing hypothesis σ(j) ≥ 2.
- **INDEX block:** 95 rows, so 16 of the 111 baseline rows are merged in total (2 into main rows, 14 into PR #10 rows).
- **Rehearsal from `21e620b`:**
  - main → #6 (`af3881b`) is clean;
  - → #11 (`97968d2`) is clean;
  - → #9 (`7b8884a`, own topic only) is clean;
  - → #12 (`c26a6ad`), using only its own topic diff after refreshing the stack, is clean. Its files outside its own topic are byte-identical to `9bd14a6` or to #9; a raw whole-head squash is not clean after upstream squashes (audit-04);
  - the other order, main → #11 → #6, auto-merges.
- **Final-ID boundary now:** PD-T081, PD-N032, IDEA-177 and LIT-300, because draft PR #11 reserves LIT-293–299 in its ledger copy. A final allocation for this PR would be PD-T081–086, PD-N032–036, IDEA-177–196 and LIT-300–394 (95). It still needs AC's choice: provisional at merge, or final allocation by the ledger owner or by explicit AC authorisation.

## Final-ID allocation (2026-11-01, AC-authorised)

AC's instructions were "allocate this block now" and, for the still-provisional lattice IDs, "if not, do that as well". Both blocks were allocated in `6954664` by `pr-prep/allocate.py`, which produced `pr-prep/id-map.json`. Lattice went first because it merged first, and the start points sit after the bivariate-Lanczos block and after draft #11's LIT-293–299 reservation.

| Namespace | Lattice-unisolvence | Programme-ideas | Next unreserved |
|---|---|---|---|
| PD-T | PD-T081–094 (14) | PD-T095–100 (6) | PD-T101 |
| PD-N | PD-N032–038 (7) | PD-N039–043 (5) | PD-N044 |
| IDEA | IDEA-177–189 (13) | IDEA-190–209 (20) | IDEA-210 |
| LIT | LIT-300–331 (32) | LIT-332–426 (95) | LIT-427 |

- **Shared registries.** The four campaign blocks in PROOF_STATUS.md, state/IDEAS.md and literature/INDEX.md are renamed "final allocation (2026-11-01)". Each block starts with an allocation note, and its rows use the final ID with the provisional ID in parentheses or as an alias. References inside the blocks are resolved to final IDs, including the bivariate-Lanczos ones. Prose that described the provisional state is rewritten. The ID_CROSSWALK.md Final ID column is filled; the 16 merged LIT rows keep "Merged into …".
- **Canonical records.** Each PD and IDEA record gets a "Final ID:" line under its heading: 21 lattice and 11 programme-ideas theory records, and the IDEA records in the three lattice `candidates.md` files and in `ideas/candidates.md`. Both literature baselines and the lattice track README get a header note. Statements, statuses, audit records and code are unchanged.
- **Ledger.** One section is appended. The lattice provisional table and `provisional-id-map.json` are kept as provenance. This makes Claude the allocator for these two members only, under AC's authorisation.
- **Checks.**
  - Each new ID appears exactly once as a primary registry row (32 PD, 33 IDEA, 127 LIT).
  - No new ID collides with an existing one.
  - Every link in the renamed blocks resolves, and `git diff --check` is clean.
  - The prepared-diff rehearsal main `21e620b` → #6 (`6954664`) → #11 (`97968d2`) → #9 (`7b8884a`, own topic only) → #12 (`c26a6ad`, own topic only) is clean, including the ledger. Refresh the dependent branches after upstream squashes before live integration; see audit-04 below.
- **Expected effect:** the lattice audit-time checkers (`topics/lattice-unisolvence-20261031/check-response-01.py`, `response-review/check_response.py`) compare earlier provisional identities/counts with their pinned baseline. They remain historical receipts at their recorded revisions, not current final-allocation checks. The second may exit 0 while reporting differences; its exit code alone does not establish a current pass.

## Audit-04 bookkeeping repairs and exact rehearsal scope

AC instructed Codex: “you have to fix all bookkeeping without more claude rounds”. Codex (`gpt-6-astra high`, requested; resolved runtime metadata unexposed) repaired only administrative integration content. Supplementary independent reviewers checked the repaired allocation helper and literature rows. No accepted mathematics, status, source-comparison verdict, allocation or audit-time evidence was changed.

- Restored the full baseline fields of LIT-342 / provisional row 16, LIT-369 / row 52, and LIT-389 / row 73. Internal formula pipes are escaped, so all seven Markdown columns survive. Source keys, locators, verification and coverage limits, overlap links and row 73's attribution warning are retained. Removed formula-derived CORPUS keys `c`, `Y`, `x±y`; the proper source entries/aliases already exist. Citation placeholders now say that source verification remains pending rather than promise completion at an already completed final allocation.
- Updated stale “re-audit pending/no row accepted” metadata to audits 02/03, the lattice provisional-only README wording, the ledger's current/historical distinction and the shared post-merge frontier. Historical rule, audit, source and provisional-ID records remain intact.
- The original allocator at `37820a5` rejects all 192 of its own installed IDs in a default dry run. A replay against preallocation inputs succeeds and reproduces the map. The repaired helper now validates the exact installed JSON, unique correctly aliased primary rows and crosswalk before returning the same blocks/next boundaries. Its default invocation is read-only; an installed allocation refuses `--apply`. No apply invocation was executed. Independent malformed-map/duplicate-ID/wrong-crosswalk checks reject bad inputs without writing.

The root's reproducible rehearsal is `audit-04-support/rehearsal-check.py`; it creates only disposable local branches/worktrees and removes them. Inputs: main `21e620ba8b5f0e0706f3a8c6613517df04d9d469`, PR #11 `97968d2c2d039cb0910e0ea50747fb2d9e01a262`, PR #9 `7b8884a2f98518784ff3698dd2f3f9c49c9cdd62`, PR #13 rules `10f2d8592673866ed0aa5ca73cef88d7541183ed` (integration compatibility only), and PR #12 both documented `c26a6adf6ebf701368f5de73fc319b0e55cdfc13` and refreshed `44be0080c69495cc6959e3d4c2b602fa73678d76`. The final receipt records the exact repaired PR #6 candidate.

| Local rehearsal | Result and live prerequisite |
|---|---|
| AC’s current order: main → #6 → #13 → #11 | Clean whole-head squashes, including the Fable amendment, rules update and reservation ledger. PR #13’s own protocol audit remains separate. |
| Earlier requested main → #6 → #11 | Also clean; retained as historical integration evidence. |
| → #9 → #12, each dependent PR's own-topic diff only | Clean for both pinned #12 heads. All 192 allocated primary rows, the seven #11 reservations and #6 canonical/audit/code/rule content are preserved. |
| main → #11 → #6 | Auto-merges. |
| Raw #12 whole-head squash after the upstream squash sequence | Conflicts in five shared registries and fifteen programme-ideas files. The upstream commits are absent from squash ancestry, so stale inherited copies collide. This is not a clean live-head claim. |

AC’s current integration order is #6, then #13 (rules update), then #11, then #9, then #12. Refresh #11 against the #6/#13-bearing main, preserving its LIT-293–299 block and all accepted allocations. After #11 lands, refresh/retarget #9 to main with only `topics/padua-proof-attempts-20261101/` as its own change. After #9 lands, refresh/retarget #12 to main with only `topics/padua-proof-attempts-2-20261101/` as its own change. Preserve the merged final-ID registries and current audit records during both refreshes. This is a recorded prerequisite for those dependent PRs; this review does not change their branches, audit their newer mathematics or authorize their merges.

Twenty second-pass comparison flags, row 58's overlap/Pitman limit, source-reading gaps and all scientific OPEN/MEASURED limits remain explicit. They are not silently cleared by the bookkeeping repairs. The original findings and corrected verification are both retained in [audit-04](audit-04.md) and its support directory. Only AC merges.
