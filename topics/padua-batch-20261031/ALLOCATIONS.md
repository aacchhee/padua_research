# Shared allocation ledger — padua-batch-20261031

## Padua Lanczos drift reservation — 2026-11-01

Owner branch: `codex/padua-lanczos-drift-20261101`. Reservation only for an early
draft; no final IDs assigned. The current fresh-range procedure supersedes older
single-owner prose. Preserve all earlier ranges and permanent gaps, including
PR #14's imported section below.

Full ledgers and four registries checked at main
`806cc7b4509fd93bae652f9545d32d95529f8281`, PR #12
`0a300db8041fc922483bb16b2f4239fde07cc134`, and PR #14
`9f0c7710abd19ee5a0d61bce6384e7a399e838d2`. All closed PRs returned were merged;
no missing retired reservation was found. The MZ topic appeared between the
initial and final scan; the superseded recommendation was never reserved.
[Complete scan and file identities](../padua-lanczos-drift-20261101/allocation-scan.json); reservation first published in `6920ba632843597c37e1493d077c1df2e89f54cb`; copy pinned at [2d20672](https://github.com/aacchhee/padua_research/blob/2d20672f62e0130d2adbe104af6e5ee9d05d20af/topics/padua-lanczos-drift-20261101/allocation-scan.json).

| Namespace | Reserved range | Count | Estimated needs + permanent headroom |
|---|---|---:|---|
| PD-T | PD-T136–PD-T155 | 20 | 12 + 8 |
| PD-N | PD-N062–PD-N071 | 10 | 6 + 4 |
| IDEA | IDEA-246–IDEA-285 | 40 | 25 + 15 |
| LIT | LIT-445–LIT-459 | 15 | 10 + 5 |

Priority is the pushed commit introducing this reservation, linked in this
topic's draft PR. Unused IDs remain permanent gaps. Next boundaries after these
ranges: PD-T156, PD-N072, IDEA-286, LIT-460, subject to a fresh union scan.
Scientific records retain provisional IDs through development and audit.

## Padua MZ 2D reservation — 2026-11-01

Owner branch: `codex/padua-mz-2d-20261101`. This is a reservation for the early draft, not a final-ID assignment. The fresh-range procedure supersedes historical single-owner prose below. All previous allocations, permanent headroom and retired reservations remain in force.

Checked complete ledgers and final-ID uses at main `806cc7b4509fd93bae652f9545d32d95529f8281`, sole other open PR12 `12e9cf4539d0977773cad75fc74f93d1664cb429`, and retained merged PR9 head `752ba068589683afe644b505d673f8da1529cbf0`. All twelve returned repository PRs were individually classified: eleven merged, one open, none closed-unmerged. Main includes the prior PR9 reservation through PD-T105 (including permanent gaps104–105). Historical LIT provisional aliases in the1700s are not final IDs. Full scan with file identities: [reservation-scan.json](../padua-mz-2d-20261101/protocol/reservation-scan.json); [GitHub state receipt](../padua-mz-2d-20261101/protocol/github-scan.json).

| Namespace | Reserved range | Count | Estimated needs + permanent headroom | Next unreserved |
|---|---|---:|---|---|
| PD-T | PD-T106–PD-T135 | 30 | 20 +10 | PD-T136 |
| PD-N | PD-N044–PD-N061 | 18 | 12 +6 | PD-N062 |
| IDEA | IDEA-210–IDEA-245 | 36 | 24 +12 | IDEA-246 |
| LIT | LIT-427–LIT-444 | 18 | 12 +6 | LIT-445 |

Publication priority is the pushed commit first adding this section, linked in the campaign PR body. No portion of these ranges may be reused even if unused. Assignment waits for PR preparation and another current-reservations check. The campaign PR will preserve a provisional-to-final map. It does not alter PR12's scientific records or audit-pending status.

## PR #9 permanent reservation (2026-11-01)

AC requested finalization of [PR #9](https://github.com/aacchhee/padua_research/pull/9).
The current fresh-range procedure supersedes historical owner-confirmation prose
below; every earlier reservation and accepted ID remains unchanged.

| Namespace | Range | Count | Owner branch | Date |
|---|---|---|---|---|
| PD-T | **PD-T101–PD-T105** | **5** | `codex/padua-proof-attempts-20261101` | 2026-11-01 |
| PD-N / IDEA / LIT | no range | 0 | same | 2026-11-01 |

Heads checked: main `cf89b140530d5838bdb208a8c28f3e7aa676ace3`,
PR #9 `93da3be26dbddf9ec2446af578fe8015bb4eeada`, and draft PR #12
`0d9ad5b803b3fff43080586f5255bfdfcba602e8`. Both complete ledgers and all four
final-ID registries were inspected at each head; their bytes agree. All closed
PRs returned by the scan are merged; no closed-unmerged or retired reservation
is missing. [Scan receipt](../padua-proof-attempts-20261101/finalization/reservation-scan.json).

This reservation is published before any final-ID assignment; its priority is
the pushed commit adding this section, linked in PR #9's body. Intended use:
three accepted results, with two IDs of headroom. Unused IDs remain permanent
gaps. Subsequent boundaries: **PD-T106, PD-N044, IDEA-210, LIT-427**, subject to
a fresh union scan. This commit makes no scientific registry change.

## Current transition and PR #11 reservation import (2026-11-01)

Main `e24b21fe43cdd090f6dfac269147e75185f04c5b` contains PRs #10, #6 and #13 and is merged into PR #11 at `f62272c525dcb8bb802306d1010c37d93fcbf4b0`. AC directs PR #11 next. **The fresh-range procedure in agents/WORKFLOW.md, adopted 2026-11-01, supersedes every older single-allocation-owner and owner-confirmation instruction below.** Those paragraphs and their dated boundaries remain historical provenance; all existing reservations remain in force.

PR #11 imports its existing reservation unchanged: namespace LIT, range **LIT-293–LIT-299**, count **7**, branch `claude/mz-prior-art-20261101`, date 2026-11-01, owner this topic. Published source commits: LIT-293–295 at `7a0878873b47135577b165df10217dd36bc035c9`, LIT-296–298 at `4f937137f9baac5e51814964e6a83aeb2df38815`, and LIT-299 at `41bbc231be4b5ccc7c3f92e5818a53b950ccc25f`; [PR #11](https://github.com/aacchhee/padua_research/pull/11) retains the publication trail. No range is reserved again, no retrospective headroom is added, and no new range is needed for finalization.

Readiness scan: current main above; PR #11 input `848daaae2954a984aa0e98634da27f5a8e60915d`; PR #9 `7b8884a2f98518784ff3698dd2f3f9c49c9cdd62`; PR #12 `38db12bc1cee57902c67f62e022af83e0880f699`. Their ledgers and all four final-ID registries were checked; #9/#12 carry no newer final reservation. All returned closed PRs are merged, so no closed-unmerged reservation was omitted. Existing reservations across main and this branch remain authoritative.

After the preserved blocks, the lowest unused boundaries remain **PD-T101, PD-N044, IDEA-210, LIT-427**, subject to the required fresh scan at any future allocation. LIT-293–299 belongs to PR #11; the merged lattice/programme block is LIT-300–426. The integrated INDEX has 426 distinct numbered LIT rows and no collision. No final ID is assigned or renumbered here.

**Current integration snapshot (2026-11-01, audit-04):** main `21e620b` already contains PR #10. PR #6 allocates lattice PD-T081–094, PD-N032–038, IDEA-177–189, LIT-300–331 and programme-ideas PD-T095–100, PD-N039–043, IDEA-190–209, LIT-332–426 under AC's member-specific authorization to Claude (section below). PR #11 head `97968d2c2d039cb0910e0ea50747fb2d9e01a262` reserves LIT-293–299; it has no collision with this block. Next unreserved: PD-T101, PD-N044, IDEA-210, LIT-427. AC’s current merge order is #6 → #13 (rules update) → #11 → #9 → #12; refresh the later drafts against each preceding merge and preserve these ranges. PR #13’s rules are not imported into PR #6. Only AC merges.

## Earlier instructions and integration snapshots (historical)

The following instructions, status table and provisional reservations describe their dated source snapshots. They are retained as provenance; the current snapshot above and final allocation sections below supersede their “next”, “provisional” and owner wording for these authorized members.

**Earlier AC instruction (2026-11-01): PR #10 merges next into current main. All other drafts will be adjusted after PR #10 is merged.** The earlier sequence and source snapshots below retain their historical provenance. This update changes no accepted reservation or allocation owner.

This is the single authoritative batch ledger. **Allocation owner: the root Codex MZ orchestrator.** AC merged charter PR #2 and MZ PR #3. AC's 2026-11-01 instruction sets **PR #4 next, then PR #5 stacked on PR #4**. The remaining programme-ideas and bivariate-Lanczos integrations follow AC's choice and must obtain any final ranges from the same owner. No parallel allocation or accepted-ID renumbering is authorized. Lattice keeps topic-scoped provisional IDs under AC's explicit original instruction; this response allocates no final ID.

## Reconciled sources and provenance


- Merged charter source: branch head `317a26597dedc9adc9cfc6a26fa00078df7d29e4`, integrated by main commit `08fafe62d9798385dfafaacc9a41344272737e68`. Its ledger already reconciled the programme snapshot with the MZ overlay and acknowledged this owner. Its original reservations and charter content have first priority.
- MZ audit delivery: `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`; merge of charter-bearing main into MZ: `bc85509adc303126c6d8276a4457393e81d7f394`. Original scientific checkpoint: `2dc9264333cdf8372947448f4b9bdd3bb577d0e1`; original final-ID package: `fdf0648cbaa9fb722c611d709e638de7dfe86368`.
- Programme source before ledger propagation: `a02bc357e5f0eed479f7020b85fecc57fda9b47f`. Its older ledger SHA-256 is `5a79ae39f147e5614041b4b8bf733c3b533d99787c481c8f1f721a085b62b6b0`. Its records are provisional; no final block is overwritten.
- Bivariate-Lanczos source before ledger propagation: `1127f9c73903e11b56cbfe3e8c667bfcbe810beb`. Its records are provisional and it had no batch ledger at that snapshot. No scientific result from that branch is imported into MZ.

Historical source heads above remain provenance, not assertions that remote tips cannot advance. Propagation commits, exact ledger-byte identity and refreshed heads are recorded in the MZ response's reconciliation receipt. The charter's standalone member ledger is an immutable reservation/provenance record, not a competing batch allocation authority.

Current integration source: main `07c5f5465d6de306aa81dbe8ca1f615295163864`, containing both accepted blocks. Lattice audit delivery `3f369611f364c8bab41b8a48f1414f88b21937ec` was merged with that main without rebasing, preserving both sets of rows. PR #5 audit delivery is `ac61532fdbf40d50647476d87ed4e3f0b4b53802`; it will merge the completed PR #4 branch and target that branch. Exact source hashes and conflict dispositions: [PR #4 response base](../lattice-unisolvence-20261031/response-01-base.json). Earlier complete lattice-ledger prose remains retrievable at its [pinned source](https://github.com/aacchhee/padua_research/blob/3f369611f364c8bab41b8a48f1414f88b21937ec/topics/padua-batch-20261031/ALLOCATIONS.md).

## Final reservations

| Namespace | Charter block (merged PR #2) | MZ original block (PR #3) | MZ audit-response addition | Next unreserved |
|---|---|---|---|---|
| PD-T | PD-T001–PD-T012 | PD-T013–PD-T028 | none | PD-T029 |
| PD-N | PD-N001 | PD-N002–PD-N006 | none | PD-N007 |
| LIT | LIT-001–LIT-041 | LIT-042–LIT-060 | LIT-061–LIT-065 | see below (bivariate-Lanczos LIT-066–LIT-292; mz-prior-art LIT-293–LIT-299; lattice/programme-ideas LIT-300–LIT-426; next LIT-427 at main `a7e1234`) |
| IDEA | IDEA-001–IDEA-051 | IDEA-052–IDEA-076 | none | IDEA-077 |

The five new LIT entries record the targeted audit-M2 screen: Erdős–Feldheim, Askey, Nevai III, Lubinsky's converse-MZ paper, and Smith's Lobatto result. Reading coverage and unresolved weight/node/norm translations stay explicit; these reservations confer no novelty clearance. The previously next free LIT-061 is consumed openly by this response, not silently skipped. No PD-T, PD-N or IDEA is added by the response.

## Members and integration responsibilities

| Order | Member | Current integration state / next action |
|---|---|---|
| 1 — complete | charter-unisolvence, [PR #2](https://github.com/aacchhee/padua_research/pull/2) | AC merged at08fafe62d9798385dfafaacc9a41344272737e68. Preserve its accepted IDs and scientific files. |
| 2 — complete | mz-constants, [PR #3](https://github.com/aacchhee/padua_research/pull/3) | AC merged at07c5f5465d6de306aa81dbe8ca1f615295163864. Preserve PD-T013–028, PD-N002–006, LIT042–065 and IDEA052–076, including audit-response additions. |
| 3 — next, AC instructed | lattice-unisolvence, [PR #4](https://github.com/aacchhee/padua_research/pull/4) | Target main; accepted existing mathematics, unchanged-status response and focused registry reconciliation. Provisional table below is retained; no final range allocated. |
| 4 — stacked on PR #4 | mz-postmerge-frontier, [PR #5](https://github.com/aacchhee/padua_research/pull/5) | Merge the PR #4 branch without rebasing, target that branch, answer audit L1–L4 and preserve its full registry/ledger contents. After PR #4 lands, refresh main and retarget as appropriate. No IDs are allocated by this administrative follow-up. |
| Later — AC chooses | programme-ideas | Its earlier copy has the same accepted reservation table, not necessarily identical status prose. On integrating current main, preserve reservations and take main's current integration prose, then reconcile any new allocation with the owner. |
| Next — AC confirmed 2026-11-01 | bivariate-Lanczos, [PR #10](https://github.com/aacchhee/padua_research/pull/10), `claude/bivariate-lanczos-20261031` | Main `9739a0c` merged into the branch (`1167c33`); accepted reservations preserved. **Final block allocated by Claude under AC's explicit 2026-11-01 authorisation** (see "Bivariate-Lanczos block" below). Other drafts adjust after this PR merges. |

No byte-identical propagation to the later member branches is claimed by this response. Their copies can legitimately lag in integration-status prose; this does not authorize overwriting accepted reservations or reverting audit dispositions. Their historical source pins above remain provenance, not current-head assertions.

## Lattice provisional reservations (unchanged)


AC explicitly requested provisional theory IDs; no new final global range is reserved. The named MZ allocation owner remains responsible for any later coordinated final allocation. AC explicitly authorized provisional lattice IDs, so a new final allocation is not a readiness prerequisite for PR #4. These topic-scoped IDs cannot collide with another topic’s provisional namespace. Exact map: [provisional-id-map.json](../lattice-unisolvence-20261031/provisional-id-map.json).

| Namespace | Reserved provisional identifiers | Owner / status |
|---|---|---|
| PD-T | PD-T?lattice-c0-codex-01; PD-T?lattice-c0-codex-02; PD-T?lattice-c0-codex-03; PD-T?lattice-c1-codex-01; PD-T?lattice-c1-codex-02; PD-T?lattice-c1-codex-03; PD-T?lattice-c1-codex-04; PD-T?lattice-c1-codex-05; PD-T?lattice-c1-codex-06; PD-T?lattice-c3-codex-01; PD-T?lattice-c3-codex-02; PD-T?lattice-c3-codex-03; PD-T?lattice-c3-codex-04; PD-T?lattice-c3-codex-05 | lattice root; PR #4 response, final allocation deferred |
| PD-N | PD-N?lattice-c0-codex-01; PD-N?lattice-c1-codex-01; PD-N?lattice-c1-codex-02; PD-N?lattice-c3-codex-01; PD-N?lattice-c3-codex-02; PD-N?lattice-c3-codex-03; PD-N?lattice-c3-codex-04 | lattice root; PR #4 response, final allocation deferred |
| IDEA | IDEA?lattice-c0-codex-01; IDEA?lattice-c0-codex-02; IDEA?lattice-c0-codex-03; IDEA?lattice-c0-codex-04; IDEA?lattice-c0-codex-05; IDEA?lattice-c1-codex-01; IDEA?lattice-c1-codex-02; IDEA?lattice-c1-codex-03; IDEA?lattice-c3-codex-01; IDEA?lattice-c3-codex-02; IDEA?lattice-c3-codex-03; IDEA?lattice-c3-codex-04; IDEA?lattice-c3-codex-05 | lattice root; PR #4 response, final allocation deferred |
| LIT | LIT?lattice-codex-01; LIT?lattice-codex-02; LIT?lattice-codex-03; LIT?lattice-codex-04; LIT?lattice-codex-05; LIT?lattice-codex-06; LIT?lattice-codex-07; LIT?lattice-codex-08; LIT?lattice-codex-09; LIT?lattice-codex-10; LIT?lattice-codex-11; LIT?lattice-codex-12; LIT?lattice-codex-13; LIT?lattice-codex-14; LIT?lattice-codex-15; LIT?lattice-codex-16; LIT?lattice-codex-17; LIT?lattice-codex-18; LIT?lattice-codex-19; LIT?lattice-codex-20; LIT?lattice-codex-21; LIT?lattice-codex-22; LIT?lattice-codex-23; LIT?lattice-codex-24; LIT?lattice-codex-25; LIT?lattice-codex-26; LIT?lattice-codex-27; LIT?lattice-codex-28; LIT?lattice-codex-29; LIT?lattice-codex-30; LIT?lattice-codex-31; LIT?lattice-codex-32 | lattice root; PR #4 response, final allocation deferred |

## mz-prior-art-20261101 reservation (2026-11-01)

AC's task instruction for `claude/mz-prior-art-20261101` authorizes LIT allocation through this ledger after reconciling open branches. The reconciliation was done on 2026-11-01 at about 10:00. Main was `9739a0c56b7a3976422ce60a8441bfbbfd6554df`. Open PR #6 is programme-ideas. Remote heads checked: claude/bivariate-lanczos-20261031 `a2dd845`, claude/programme-ideas-20261031 `c93c912`, codex/padua-proof-attempts-20261101 `a09d910`, claude/results-track-rule-20261101 `6eeec5b`.

The bivariate-Lanczos branch already records an AC-authorized final block in its copy of this ledger: PD-T029–080, PD-N007–031, IDEA-077–176, LIT-066–292. This branch therefore reserves **LIT-293–LIT-299**, after that block: Mastroianni–Russo 1999, König–Nielsen, Niu–Liao–Ma–Wu, Xu 1994 II, Sloan–Smith 1982, Smith–Sloan 1980, and Mastroianni–Milovanović–Notarangelo 2012. LIT-296–298 were added after AC supplied fulltexts. LIT-299 was added in response-01 for the audit-01 lead, after re-checking that no open branch uses it. No PD-T, PD-N or IDEA is reserved here.

Next unreserved after both blocks, at the time of this reservation: PD-T081, PD-N032, LIT-300, IDEA-177. This is superseded by the later lattice/programme-ideas blocks below; at main `a7e1234` the next unreserved values are PD-T101, PD-N044, IDEA-210, LIT-427. Audit-02 confirmed LIT-293–299 for this branch (2026-11-01). Whichever of the two PRs merges second must merge this ledger section with the Lanczos block rather than overwrite it. The named allocation owner (root Codex MZ orchestrator) should confirm during the Codex audit.

## Readiness and history

Before AC's requested sequence, refresh the relevant heads and rehearse **current main → PR #4 → PR #5** in a disposable local branch. Record exact source/tree identities, conflict resolutions and preservation checks in the response receipts. A rehearsal authorizes no live merge, main push, force-push or tag. Only AC merges. Later member branches merge the integrated registry state and repeat their own checks before readiness.

2026-11-01 registry reconciliation preserves the canonical owner, the complete final reservation table (including LIT-061–065) and all66 lattice provisional IDs. No charter entry was found overwritten in the MZ main; the PR #4 branch was missing the newer merged MZ additions until this merge. The previous unrelated-branch ledger-copy requirement is replaced by explicit reservation preservation and current-main prose reconciliation, as PR #5 audit L3 requested.

## Bivariate-Lanczos block (allocated 2026-11-01)

AC's explicit instruction of 2026-11-01 (recorded in `topics/bivariate-lanczos-20261031/LOG.md`): for the bivariate-Lanczos PR, Claude allocates the final IDs now as the next free ranges, and records the owner change for this PR in this ledger. The Codex MZ orchestrator remains the allocation owner for every other member; this block was taken from the "Next unreserved" column above on main `9739a0c56b7a3976422ce60a8441bfbbfd6554df` after checking PROOF_STATUS.md, IDEAS.md and literature/INDEX.md there (highest used: PD-T028, PD-N006, IDEA-076, LIT-065) and the open programme-ideas PR #6 (no final reservation recorded). Lattice provisional IDs are unaffected.

| Namespace | Bivariate-Lanczos block (Claude, AC-authorised) | Count | Next unreserved after this block |
|---|---|---|---|
| PD-T | PD-T029–PD-T080 | 52 | PD-T081 |
| PD-N | PD-N007–PD-N031 | 25 | PD-N032 |
| LIT | LIT-066–LIT-292 | 227 | LIT-293 |
| IDEA | IDEA-077–IDEA-176 | 100 | IDEA-177 |

Map and generator: `topics/bivariate-lanczos-20261031/pr-prep/id-map.json`, `allocate.py`. The last column records the boundary immediately after this block at allocation time. Members integrating after PR #10 refresh main and active draft reservations and reconcile with the owner before allocating; the boundary is not permission to ignore later reservations. The 2026-11-01 review snapshot of draft PR #11 (`4f937137f9baac5e51814964e6a83aeb2df38815`) records LIT-293–298, disjoint from this PR. AC confirmed that every other draft adjusts after PR #10 merges. No accepted ID is renumbered, and no propagation to other drafts is claimed here.

## Lattice-unisolvence and programme-ideas blocks (allocated 2026-11-01)

AC's explicit instructions of 2026-11-01 in the programme-ideas session were "allocate this block now" (for PR #6) and "are the lattice ids allocated now? if not, do that as well". Under that authorisation Claude allocated both blocks in PR #6, on top of main `21e620b`. The owner change applies to these two members only; the Codex MZ orchestrator remains the allocation owner for every other member.

The boundary was the column "Next unreserved after this block" of the bivariate-Lanczos block (PD-T081, PD-N032, IDEA-177). For LIT it was LIT-300, because draft PR #11 (`claude/mz-prior-art-20261101`, head `97968d2`) reserves LIT-293–LIT-299 in its copy of this ledger. Before allocating, I checked the open PRs #9, #11 and #12: no other reservation was recorded. The script also checks that none of the new IDs already occurs in PROOF_STATUS.md, state/IDEAS.md, literature/INDEX.md or ID_CROSSWALK.md. The lattice block is allocated first, because lattice merged first (PR #4).

| Namespace | Lattice-unisolvence (66 provisional IDs) | Programme-ideas | Next unreserved |
|---|---|---|---|
| PD-T | PD-T081–PD-T094 (14) | PD-T095–PD-T100 (6) | PD-T101 |
| PD-N | PD-N032–PD-N038 (7) | PD-N039–PD-N043 (5) | PD-N044 |
| IDEA | IDEA-177–IDEA-189 (13) | IDEA-190–IDEA-209 (20) | IDEA-210 |
| LIT | LIT-300–LIT-331 (32) | LIT-332–LIT-426 (95) | LIT-427 |

- **Lattice:** its IDs are taken in (direction, number) order, and all 32 lattice LIT rows receive IDs exactly as registered. Lattice rows that overlap older sources were not deduplicated here.
- **Programme-ideas:** 16 of its 111 baseline LIT rows were merged without a new ID, into LIT-002, LIT-010 and 14 bivariate-Lanczos rows. This is recorded in ID_CROSSWALK.md.
- **Map and generator:** `topics/programme-ideas-20261031/pr-prep/id-map.json` and `allocate.py`.
- **Retained reservations:** the lattice provisional-reservation table above and `topics/lattice-unisolvence-20261031/provisional-id-map.json` are kept as provenance. No accepted ID is renumbered.
- **Members merging after PR #6** start from the last column above, after reconciling any later reservations. PR #11's LIT-293–299 reservation is unchanged.

## PR #9 assignments after reservation publication (2026-11-01)

Reservation priority: `020dcddd36fa1e3254cbf288701d5ab02d27c580`, published and linked in PR #9 before assignment. Fresh recheck of PR #12 at `12e9cf4539d0977773cad75fc74f93d1664cb429` found unchanged ledgers/registries and no collision. PD-T101 = exact corner identity; PD-T102 = generic distinct-x commutant; PD-T103 = degree-3 local certificates. PD-T104–105 remain permanent unused headroom. No other namespace reserved or assigned. [Exact map](../padua-proof-attempts-20261101/finalization/id-map.json). Earlier ledger text and all earlier ranges are preserved.

## Padua MZ 2D campaign — PR14 final registration

Own reservation unchanged, first published `9f0c7710abd19ee5a0d61bce6384e7a399e838d2`: assigned PD-T106–117 (12), PD-N044–053 (10), IDEA-210–227 (18), LIT-427–428 (2). Same-source LIT IDs reused: 312,014,379,314,045. Permanent unused headroom: **PD-T118–135, PD-N054–061, IDEA-228–245, LIT-429–444**. No ranges shift or shrink. [Map](../padua-mz-2d-20261101/protocol/final-id-map.json); [fresh scan](../padua-mz-2d-20261101/protocol/final-reservation-recheck.json).

PR15 reservation data above is imported unchanged (its unavailable local evidence link is made a pinned remote link) from `2d20672f62e0130d2adbe104af6e5ee9d05d20af`; first published commit **6920ba632843597c37e1493d077c1df2e89f54cb**, [PR15](https://github.com/aacchhee/padua_research/pull/15). Its PD-T136–155, PD-N062–071, IDEA-246–285 and LIT-445–459 remain reserved to its branch. This campaign assigns none of them. Stage AUDIT, Claude PENDING.

**Integration order (AC, 2026-11-01):** PR14 (`codex/padua-mz-2d-20261101`) before PR15 (`codex/padua-lanczos-drift-20261101`). After AC squash-merges PR14, the PR15 orchestrator merges the new main without rebasing and keeps both topics' complete reservation and mapping text and every permanent gap (see [readiness plan](../padua-mz-2d-20261101/readiness-plan-01.md)). No range changes. Receipt: [integration-pr14-first-20261101.json](../padua-mz-2d-20261101/protocol/integration-pr14-first-20261101.json).

## Padua Lanczos drift campaign — PR15 final registration

Own reservation unchanged (first published `6920ba632843597c37e1493d077c1df2e89f54cb`): assigned **PD-T136–146 (11), PD-N062–063 (2), IDEA-246–267 (22)**, no LIT. Permanent unused headroom: **PD-T147–155, PD-N064–071, IDEA-268–285, LIT-445–459**. No range shifts, shrinks or reuses another topic's IDs; PR14's assignments and gaps above are preserved. [Map](../padua-lanczos-drift-20261101/preparation/final-id-map.json); [fresh union scan](../padua-lanczos-drift-20261101/preparation/union-scan.json).

**Integration order (AC, 2026-11-01 20:55 CET):** PR15 (`codex/padua-lanczos-drift-20261101`) merges before PR12 (`codex/padua-proof-attempts-2-20261101`). After AC squash-merges PR15, the PR12 orchestrator merges the new main into its branch without rebasing and keeps PR15's registrations (PD-T136–146, PD-N062–063, IDEA-246–267) and permanent gaps (PD-T147–155, PD-N064–071, IDEA-268–285, LIT-445–459) intact. A merge-tree of PR15 head `b6980b9` with PR12 head `f4c5c9e` is clean.


## PR12 second proof campaign — permanent reservation (2026-11-01)

AC explicitly authorized final IDs and shared updates after merging PR15. Owner: `codex/padua-proof-attempts-2-20261101`. The current fresh-range procedure supersedes historical single-owner prose; all earlier reservations, assignments and permanent gaps remain unchanged.

Fresh union: main `67bd07c0867d8d49eb104942237d7f51a7d9f77d`, sole open PR12 `f4c5c9e783d2a57253142877cf6845635aaac50f`; all other14 returned PRs merged, no closed-unmerged reservation missing. Both complete ledgers and all four registries scanned at both heads. [Receipt](../padua-proof-attempts-2-20261101/preparation/reservation-scan.json); [remote classification](../padua-proof-attempts-2-20261101/preparation/pr-snapshot.json). Highest used/reserved: PD-T155, PD-N071, IDEA-285, LIT-459; next-unreserved prose is not an allocation.

| Namespace | Permanent reserved range | Count | Needs / headroom |
|---|---|---:|---|
| PD-T | PD-T156–PD-T205 | 50 | 42 durable theory records + 8 permanent headroom |
| PD-N | PD-N072–PD-N077 | 6 | 2 scoped negative records + 4 permanent headroom |
| IDEA | IDEA-286–IDEA-315 | 30 | retained route/candidate dispositions + permanent headroom |
| LIT | no range | 0 | existing LIT-312, LIT-379 and LIT-388 reused |

Reservation priority is the pushed commit introducing this section, published in PR12 before assignment. No final IDs are assigned in this reservation checkpoint. Unused IDs remain permanent gaps. PR15's registrations and headroom through155/071/285/459 remain intact. Integration order: PR15 is merged; PR12 follows on new main without rebasing. Only AC merges.
