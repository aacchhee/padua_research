# Reservation recheck — PR20 preparation

2026-11-05. **PASS for the pinned union.** Mechanical worker: configured
Codex gpt-6.1-sol medium; serving metadata is not exposed. Rules read at
`e8ba6f90a7421fd6dad231586843a4870bdcaf15`: AGENTS.md,
agents/WORKFLOW.md and agents/codex/CODEX.md, plus handoff04. This is a
bounded allocation check, with no mathematical development or novelty claim;
a new novelty gate is therefore inapplicable.

The six proposed theorem IDs **PD-T266–271** and three proposed candidate IDs
**IDEA-356–358** fit entirely inside this topic's already published permanent
reservation. They have no occurrence in any of the four registries at any
checked head, and no overlap with another owner's reservation. This record
makes no final assignment and reserves no new range. PR20 priority remains
`514e3763a827c106c5170eecd55d849b39265da2`; preserve its full ranges
T266–285 / N092–099 / IDEA356–375 / LIT474–481, including unused headroom.

## Population and pins

The orchestrator supplied the fresh live GitHub all-state search: 23 returned
PRs; open drafts included are PR20–24; every returned closed PR is merged;
there is no closed-unmerged PR needing recovery. I read the compact supplied
classification, without claiming an independent GitHub query. The receipt
hashes that input. A missing PR number in the returned population is not
silently filled in or treated as an additional PR.

| Input | Pinned commit |
|---|---|
| main | 5db1e01dcd2258f45de2adcaef43859e59734618 |
| PR20 | e8ba6f90a7421fd6dad231586843a4870bdcaf15 |
| PR21 | 890f56ccde35431b70b43141c224b0b8817fea7f |
| PR22 | 30a361d19a6c23fa1df950becbe73f635aa22e71 |
| PR23 | 2b489d01d443b6780ac034f4d6c20d50fffee2a6 |
| PR24 | 5e5081e991fc48f033d3ef51ee2b6e42f892d29d |

## Executed method and evidence

I used read-only `git ls-tree -r --name-only <sha>` to enumerate each pinned
tree, selected every `ALLOCATIONS.md` plus PROOF_STATUS.md, state/IDEAS.md,
literature/INDEX.md and ID_CROSSWALK.md, then read their complete bytes through
`git show <sha>:<path>`. I also searched allocation/ledger/reservation path
names to check the ledger selection. Other matching paths are scan receipts,
code or the campaign ROUND_LEDGER, rather than global allocation ledgers.
No mutable Git command was used.

There are **50 complete file copies**, deduplicating to **18 distinct blobs**.
The [compact receipt](reservation-recheck.json) lists every distinct path,
Git blob, SHA-256 and byte count, with per-head ordered blob lists and tree
identities. Thus identical files are recorded once without dropping any
branch copy. Selection-list hashes and registry table-row digests further
pin the coverage. All ID-bearing table rows were parsed, along with final-ID
mentions throughout each complete registry. Full distinct reservation tables,
prose on ranges/permanent gaps, and above-boundary registry mentions were
reviewed. The batch-ledger copies differ by main's additive PR19 import;
older branches' missing import does not release that reservation.

The receipt's semantic reservation table imports the entire historical union,
including all merged owners and permanent headroom. Within each namespace I
sorted owner intervals and checked every adjacent pair for overlap. The
interval check passes. I separately searched all four complete registry texts
for each proposed ID: zero hits at every pinned head. This is stronger than
merely checking canonical first-column maxima.

## Reservation interpretation

| Owner | PD-T | PD-N | IDEA | LIT |
|---|---|---|---|---|
| PR19, now merged | 246–265 | 084–091 | 336–355 | 466–473 |
| PR20 | 266–285 | 092–099 | 356–375 | 474–481 |
| PR21 | no range | no range | no range | 482–561 |
| PR22 | 286–293 | 100–103 | 376–383 | 562–573 |
| PR23 | 294–323 | 104–115 | 384–413 | 574–581 |
| PR24 | 324–363 | 116–131 | 414–453 | 582–593 |

The union maxima including reserved headroom are **T363 / N131 / IDEA453 /
LIT593**. These maxima concern a hypothetical new reservation; this task
uses existing PR20 ranges. Historical “next unreserved” columns and prose are
boundaries at their recorded dates, not reservations. Bare endpoints and
abbreviated ranges were interpreted from their namespace and table context;
raw prefixed-token maxima would miss them. Topic provisional aliases containing
`?` do not assign final IDs.

Four-digit LIT references 1160, 1185, 1317, 1325, 1586, 1658, 1729 and 1750
occur as foreign bttb-research catalogue aliases within canonical Padua rows
or an obstruction-table citation. They are not Padua allocations. Their
context was inspected, rather than treating the largest regex match as the
allocation maximum.

PR19's merged reservation keeps its original publication
`ed8db2fc364d0ba34c3c06815460b3b2971787b5`. Its unused T253–265 / N087–091 /
IDEA349–355 / LIT471–473 remain unavailable. Earlier T236–245 / LIT460–465
and every other earlier reserved gap also stay unavailable. No separately
missing retired reservation was found in the checked ledgers/population.

The initial topic allocation-scan.json is preserved byte for byte; its
SHA-256 is `91b55a8e7ddcaec8b336f5b5ef0ec28be2da717223c3a17906b87d542b869ab7`.

## Limits

This passes mechanical availability only at the six pinned heads and supplied
PR population. It neither approves mathematical claims nor establishes global
readiness. The orchestrator must refresh changed heads/population before
readiness. All final mapping, shared-record edits, manifest updates and Git
operations remain with the orchestrator. No repair, renumbering or collision
referral is needed for the proposed six-plus-three assignment.
