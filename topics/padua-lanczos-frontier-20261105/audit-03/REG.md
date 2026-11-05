# Audit-03 family report — REG (reservations, final IDs, deduplication)

Subagent auditor: Claude Opus 5.5, effort high, working under the Claude audit-03 orchestrator. The orchestrator saved this report from the subagent's returned text, condensed. All finding IDs, evidence and remedies are preserved.

- **Audited head:** `1fb21c1` (preparation output `0299fcf`), checked out cleanly.
- **Refs:** origin/main `b4d292e`; PR27 `3dda890` (the preparation pinned `714f3ca`); PR28 `d879256` locally. A later API read found PR28 at `929ef78`.
- **Git and repository:** no changes and no writes.

**Verdicts.**
- Check 3, reservations: **PASS WITH FIX**.
- Check 4, final IDs and deduplication: **PASS WITH FIX**.
- No ID collides with any branch or PR, including PR28.

## Files read (sha256 prefix, bytes)

| File | sha256 | Bytes |
|---|---|---|
| preparation/reservation-check.md | `c043ef6b` | 7047 |
| allocation-scan.json | `c854ee74` | 8137 |
| live-prs.json | `64add41f` | 7457 |
| peer-head-recheck.json | `36a14f85` | 3491 |
| D/ALLOCATIONS.md | `4057c185` | 4802 |
| topics/padua-batch-20261031/ALLOCATIONS.md | `71556c0c` | 42273 |
| final-id-map.json | `65fcfbcc` | 9642 |
| idea-id-disposition.md | `beed95a8` | 15827 |
| state/IDEAS.md | `a3405f6e` | — |
| ID_CROSSWALK.md | `ec3cb89f` | — |
| PROOF_STATUS.md | `a696f9f6` | — |
| handoffs/11-prep-audit.md | `92fb3820` | — |

Also read:
- all 19 theory files and companions;
- the candidate ledgers;
- drift ideas-e1.md (IDEA-248/250);
- the PD-T075 theory file (claude-319);
- the IDEA-168 receipt entry;
- WORKFLOW's PD-N rule.

## Check 3 — reservations: PASS WITH FIX

- **Preparation counts reproduce.** At the four pins `b4d292e`, `95366c1`, `29a78ec` and `a3f03be` I get exactly the preparation's 57 copies, 41 ledger copies, 13 distinct ledger versions and 21 distinct versions overall.
- **Independent union** over main, PR27 at `3dda890` and `714f3ca`, PR28 at `d879256`, PR24 HEAD and `a3f03be` (89 copies, 22 distinct versions, 15 distinct ledger versions):
  - The only ranges that intersect PR24's T324–363/N116–131/IDEA414–453/LIT582–593 are PR24's own ranges and sub-ranges.
  - Every foreign mention acknowledges PR24 as owner: PR28 ALLOCATIONS:14, PR27 ALLOCATIONS:20, argmax-effective ALLOCATIONS:44–46, and the batch ledger.
  - No range straddles PR24's boundaries, and no retired reservation touches them.
- **PR27, `714f3ca → 3dda890`.** All 15 pertinent files are blob-identical and the path set is identical. Its 39 changed files add no token in PR24's ranges.
- **PR28 (new).**
  - It reserves T432–471/N162–177/IDEA530–569/LIT614–629, first published `d879256`.
  - It acknowledges PR24's full ranges and assigns nothing.
  - API compare `d879256...929ef78`: its ledger only adds a first-publication note and "peer refresh at PR24 0299fcf: no collision". The 278 KB of added patch text contains no PR24-range token.
- **Registries.** At main, PR27 and PR28, PROOF_STATUS, IDEAS, INDEX and the crosswalk contain no ID in PR24's ranges.
- **Other branches.** Grepping all 11 other remote branches for `PD-T32[4-9]|PD-T33[0-9]|PD-N11[6-8]|IDEA-41[4-9]|IDEA-42[0-4]` gives 0 hits.
- **Shared-ledger record.** Main's bytes are a prefix of the batch ledger. The appended PR24 section records:
  - owner and first publication `40b3eb6` (verified);
  - counts 40/16/40/12;
  - assignments and gaps;
  - PR27's acknowledgment with first publication `f708a83` (verified).
- **Population (API):** 27 PRs. Open: 24, 27 and 28, all draft. The other 24 are closed and merged; none is closed-unmerged.
- **Union maxima now:** T471/N177/IDEA569/LIT629.

## Check 4 — final IDs and deduplication: PASS WITH FIX

**Maps.**
- 16 PD-T records (L1-01, L2-01..05, L3-01, L4-01, L5-01..04, L6-01, L6-03, G1-01, L7-01) map one-to-one onto T324–339.
- 3 PD-N records map onto N116–118.
- 11 new candidates map onto IDEA414–424.
- 8 existing homes cover 7 IDs, because L5-02 and L5-03 both go to IDEA-168.

**Aliases.**
- Every `?lanczos-frontier` / `?frontier-l7` token in the repository is in the map. The five extra strings are templates or fragments.
- All 57 aliases appear as exact tokens in a crosswalk row that carries their final ID.
- All 19 topic map tables agree.

**Theory headers and rows.**
- Each theory or companion file has an H1 with its final ID, a "Final registration" line matching the map, and all its aliases.
- PROOF_STATUS has rows for all 19 with matching statuses. T324 and T325 link the frozen primary and its companion.
- The theory diffs against `a3f03be` delete only the title line. The frozen files are byte-unchanged.

**Predecessors.**
- In IDEAS the only deletions are ";" characters after existing alias tokens. Every old cell survives as a substring, and no row was removed.
- The IDEA-168 receipt before/after strings equal the `a3f03be` and HEAD rows byte for byte.

**Are the eight homes genuine?**
- **l1-01 → 248:** same E2 rate target. Genuine.
- **L4-02 → 250:** a full-output readout of IDEA-250's own node-sign witness. Genuine.
- **L6-02 → 262:** executes IDEA-262's resume condition. Genuine.
- **L7-03 → 266 and L7-04 → 267:** the same deferred BNT and ZN tasks. Genuine.
- **L5-03 → 168:** the withdrawn claude-313 inference. A true duplicate.
- **L5-02 → 168:** a lineage continuation of PD-T075's open-item route, which has no IDEA of its own, rather than mechanism identity. Acceptable (P3-REG-6).
- **L3-02 → 251:** its parent L3a (now IDEA-419) is itself a quantitative continuation of IDEA-251. Choosing the grandparent is a recorded judgment. Acceptable (P3-REG-5).

**PD-N records.** N116, N117 and N118 each carry a scoped REJECTED negative statement with assumptions; none is administrative. N117 is a corollary of T336 but records a refuted realization mechanism.

**Unused ranges.** T340–363/N119–131/IDEA425–453/LIT582–593 appear only as range endpoints.

## Executions (all exit 0)

- My own union scripts (`union.py`, `union2.py`) over 6 refs, plus reproduction of the four-pin counts.
- `git diff 714f3ca 3dda890`, with blob comparison on the 15 files; `git diff b4d292e d879256`.
- `git grep` across 12 remote refs.
- Python checks:
  - map against repository tokens;
  - map against crosswalk rows;
  - header, status and PROOF agreement;
  - character-level preservation of the IDEA rows;
  - IDEA-168 receipt equality.
- Read-only `gh api`: the pulls listing (state=all), compare `d879256...929ef78`, the main branch, and the PR heads.

## Findings

| ID | Severity | Location | Finding | Remedy |
|---|---|---|---|---|
| P3-REG-1 | MINOR, required before readiness | D/ALLOCATIONS.md, reservation-check.md, PR body, batch-ledger PR24 section | The recorded refresh is stale: PR27 at `95366c1`/`714f3ca`, 26 PRs, no PR28, maxima T431/N161/IDEA529/LIT613. | Append a dated readiness refresh. Note "audit-03 PASS" beside each "preparation audit PENDING". |
| P3-REG-2 | MINOR | New shared prose: the batch-ledger PR24 section, the topic ALLOCATIONS final section, and registry rows | Missing spaces between words and IDs, e.g. `published40b3eb6`, `assignmentsT324–339`, `onlyACmerges`, `committed0574c47` (14×), `exceeds1`, `criterion100U`. | Fix spacing. Registry text must go through the proposal and re-application, or be accepted as cosmetic. |
| P3-REG-3 | MINOR | IDEAS rows IDEA-250, 262, 266, 267 | Final-ID substitution made the rows refer to themselves, e.g. "IDEA-262 is this IDEA's concrete contract/continuation". | Name the consolidated local candidate. |
| P3-REG-4 | MINOR | PD-N116 row and crosswalk | Local cross-namespace labels remain ("IDEA L4-01", "PD-T L4-01", "PD-N L6-02" …), the L4-01 theorem/idea ambiguity flagged in audit-01. The L5-02/L5-03 crosswalk rows each list the other's alias. | Use final IDs. Remove the cross-listed aliases. |
| P3-REG-5 | NOTE | IDEA-419, IDEA-420 rows | They do not name the predecessor their local verdicts cite (IDEA-251/252; IDEA-250). | Optional wording. |
| P3-REG-6 | NOTE | IDEA-168 row | L5-02 → IDEA-168 is a lineage-home consolidation. | Optional note. |
| P3-REG-7 | NOTE | g1, l7 and l3 theory files, line 5 | Original "provisional; no final ID" lines survive under the dated Final-registration lines. | Acceptable as preserved text. |
| P3-REG-8 | NOTE | Batch ledger, crosswalk | PR24, PR27 and PR28 all append to the same files, so whichever merges later will hit trivial textual conflicts. There is no ID collision. | Later peers import PR24's assignments. |

## Orchestrator dispositions

- **P3-REG-1:** FIXED. A dated readiness refresh was appended to D/ALLOCATIONS.md, preparation/reservation-check.md and the batch-ledger PR24 section.
- **P3-REG-2:** FIXED in both PR24-owned ledger sections. The registry prose is left as recorded cosmetic debt; preparation/record.md says so.
- **P3-REG-3:** FIXED through the proposal and the guarded re-application.
- **P3-REG-4:** FIXED for the labels, through the proposal and re-application. The L5-02/L5-03 cross-listed aliases come from `build()` and are recorded as cosmetic: the candidates remain distinct.
- **P3-REG-5 to P3-REG-8:** recorded, no change.
