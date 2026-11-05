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

## Final live-population recheck — 2026-11-05

**PASS after assignment.** The orchestrator repeated the live all-state query:
still 23 returned PRs, open PR20–24, all returned closed PRs merged, no
closed-unmerged recovery needed. The supplied compact final population has
SHA-256 `eb83758a5202f6ee718aac2f2ee1baa5a39e2d82d9d5e83ae06abb9b1c93ee63`.
I independently reread every complete ledger and all four registries from the
refreshed pinned trees using the same read-only Git method. The original JSON
receipt remains immutable; this dated entry records the new pins and changes.

Main remains `5db1e01dcd2258f45de2adcaef43859e59734618`. PR21, PR22 and PR24
remain at the exact pins in the original table. PR23 has advanced from
`2b489d01d443b6780ac034f4d6c20d50fffee2a6` to
`8fc9c1da776f85a784eead3591c02fcf4b642250`, importing main. Published PR20 is
now `d8bc03ae06b8d0cec6442716a0d3f7a6f8c7f6f9`; the additional checked own
candidate is `871e25bf918116f95a37f8c3dda3d1533810f4b3`. Every selected
ledger/registry file is byte-identical between those two own heads.

The current main/open-head union comprises **51 complete file copies**; the
additional candidate check reads nine more. The following digest pins every
selected full-file SHA-256, byte count and path without duplicating the initial
receipt. For each head select sorted `*/ALLOCATIONS.md` paths, followed in order
by PROOF_STATUS.md, state/IDEAS.md, literature/INDEX.md and ID_CROSSWALK.md;
concatenate `<sha256>\t<decimal-bytes>\t<path>\n`, then SHA-256 that UTF-8 list.

| Input | Files | Full-file inventory digest |
|---|---:|---|
| main | 8 | 65aefd240f41b5000c5b0f5bc7452776ddc9525b8f1660ad8fd0c9af4023c86a |
| PR20 / candidate | 9 each | e8fcd7d982107232d0025bb11a7d42f7b7b9b60cd90b6af29360471454295d9f |
| PR21 | 8 | 0fd263189a49455ec61232c9b99456fde1eebb752ec27409323c64e9c9a2d5a8 |
| PR22 | 9 | d2a93d4d53f922ade6e8058cf18853de3bb0deeda78f380a73bd0a66070a1ae2 |
| PR23 refreshed | 9 | 91913198e7eabe4259a2081d185bf53ba74f4fc17653dcbd021e4354c702045c |
| PR24 | 8 | e997be9324ca4f10665b58347fc9c4447df1259f05ef7e1db1e7f57b50560775 |

PR23's topic allocation ledger is **byte-identical to its former head**, SHA-256
`e9002fd2b725bdb035ee0650ed529a3f05149e27634ed890b0667d2a14352052`.
Its four registries and shared batch ledger are now byte-identical to current
main (identities already listed under main in the original JSON). Its extra
ledger copy is main's PR19 topic ledger. This import preserves PR19's ranges
and adds no reservation. All unchanged-head selections also remain exactly
those of the original receipt.

PR20 now has six canonical PROOF_STATUS rows PD-T266–271, three canonical
IDEAS rows IDEA-356–358 and all nine exact alias mappings in ID_CROSSWALK.
These same IDs occur in **none** of the four registries on main or any other
open head. LIT allocation is unchanged. The own ledger and shared batch ledger
record the same existing permanent ranges, assignments and unused gaps. The
batch ledger retains main's entire previous bytes as an exact prefix and adds
only PR20's import; the topic ledger likewise keeps its previous reservation
and dated final assignment. All owner intervals from the earlier semantic
union remain unchanged and disjoint; maxima stay T363/N131/IDEA453/LIT593.

For preservation, the 1,024 distinct qualified final-ID mentions across main's
four registries are a subset of the candidate's 1,033; the exact difference
is only the six T IDs and three IDEA IDs above. Every old table-row key
survives. The seven changed existing PROOF_STATUS rows are T098, T100, T180,
T184, T211, T212 and T230; the two existing IDEA rows are 206/299; the three
changed old crosswalk mappings are the existing aliases for T180/T184/IDEA299.
They retain IDs and provenance, with dated completion/supersession text;
T098 remains OPEN and T100 MEASURED. No old literature table row changed;
the bounded LIT388 addendum is additive. Earlier PR19 records, all permanent
gaps and all other owners' reservation text remain intact. This is a bounded
mechanical preservation check, not a new mathematical audit.

The original reservation-recheck.json SHA-256 remains
`2d886e2e4336453bf7a87bce354f601adac2a6f130d4e57e8d2d4a2bd17a93b3`.
No JSON, code, evidence, shared record or Git state was modified by this final
recheck. This appended Markdown leaves the non-record budget unchanged.

## Readiness recheck after authorized cold-storage reduction — 2026-11-05

**PASS for the refreshed complete union.** Rules were reread at published
candidate `4952cdd7e9f433ff40632d88cf2d319114ad7fdf` (the orchestrator identifies
the rules checkpoint as `40347d1`). This remains an allocation-only check, with
no new mathematics or novelty claim. The user-authorized storage reduction
changes no reservation or final-ID registration.

The orchestrator's fresh live all-state query still returns 23 PRs, with open
PR20–24 and every returned closed PR merged; no closed-unmerged reservation
needs recovery. The supplied `lebesgue-cold-prs.json` population has SHA-256
`1adb9d60988e3cd3c39eb948f6eae5d2e0fc0c53ff87a3063e931625929cedec`.
Main remains `5db1e01dcd2258f45de2adcaef43859e59734618`. PR21/22/24 remain at
their original full pins above. PR20 is now the published candidate
`4952cdd7e9f433ff40632d88cf2d319114ad7fdf`; PR23 is now
`7a8d8dd313b5370589810f4efd910ed65744f865`.

I reread all **51 complete ledger/four-registry copies** at these six heads
using read-only `git ls-tree` and `git show`, recomputed the ordered full-file
inventory digests defined in the previous recheck, and compared every PR20
selected file with candidate `871e25bf918116f95a37f8c3dda3d1533810f4b3` and
every PR23 selected file with `8fc9c1da776f85a784eead3591c02fcf4b642250`.
**Every selected file is byte-identical to the respective preceding check.**
All six inventory digests and file counts therefore equal the preceding table,
including PR20 `e8fcd7d982107232d0025bb11a7d42f7b7b9b60cd90b6af29360471454295d9f`
and PR23 `91913198e7eabe4259a2081d185bf53ba74f4fc17653dcbd021e4354c702045c`.
There is no new shared-registry or reservation delta to interpret on PR23:
its four registries/shared batch ledger still match current main exactly,
and its own ledger retains the identical ranges and gaps.

A fresh search of every complete registry again finds T266–271 only in PR20's
six PROOF_STATUS rows and corresponding crosswalk mappings, and IDEA356–358
only in its three IDEAS rows and corresponding mappings. No other checked
head uses any of the nine IDs. All earlier owner intervals, permanent unused
gaps and retained records remain byte-equivalent to the passed union above;
no overlap or priority change occurs. Maxima remain T363/N131/IDEA453/LIT593.
PR20's unused T272–285/N092–099/IDEA359–375/LIT474–481 stay permanent gaps.

The original JSON receipt was read and remains unchanged at SHA-256
`2d886e2e4336453bf7a87bce354f601adac2a6f130d4e57e8d2d4a2bd17a93b3`.
Only this Markdown entry was appended; no new generated scan receipt, shared
edit, storage operation or Git mutation was performed. This PASS covers final
ID availability/preservation at the refreshed pins, independently of the
separate storage and preparation review dispositions.
