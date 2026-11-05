# PR22 permanent-reservation recheck — 2026-11-05

Mechanical preparation under rules read at
`4270d34abffdb83f33bbb811fb5b18e71809b14c` and handoff05. No new
candidate, novelty assessment, mathematical claim, scientific run, range or
final assignment is made. The orchestrator retains Git and final-ID authority.

The [compact receipt](reservation-scan.json) hashes **35 complete file copies**
(**23 unique byte contents**): 10 at main, 8 at PR21, 9 at PR22 and 8 at PR24.
At each pin, `git ls-tree -r --name-only` identified every `**/ALLOCATIONS.md`;
`git show SHA:PATH` read each entire ledger plus `PROOF_STATUS.md`,
`state/IDEAS.md`, `literature/INDEX.md` and `ID_CROSSWALK.md`. Hashes cover
complete file bytes, including inherited ranges, retired-reservation references
and permanent gaps. This is a registry/reservation scan, not a novelty gate.

| Source / branch | Pinned head |
|---|---|
| main | `21dbfc90257b952d8923f6d01739d12aa8d6e0a1` |
| PR21 / claude/padua-literature-20261103 | `890f56ccde35431b70b43141c224b0b8817fea7f` |
| PR22 / codex/nn-mop-iep-20261103 | `f4c41acb665f4ea35b5db05ec45ae8ba34fe6b96` |
| PR24 / codex/padua-lanczos-frontier-20261105 | `5e5081e991fc48f033d3ef51ee2b6e42f892d29d` |

The orchestrator supplied the refreshed live all-state PR classification:
exactly PR21, PR22 and PR24 are open, drafts included; all returned closed PRs
are merged, with no closed-unmerged reservation requiring another ledger.
This worker did not repeat the API query. Merged PR23's reservation and final
assignments are included through current main rather than treated as open.

## Findings

**The existing NN-MOP ranges remain uncontested:** PD-T286–293 (8),
PD-N100–103 (4), IDEA376–383 (8), LIT562–573 (12), owned by
`codex/nn-mop-iep-20261103`, first published at
`a0abe8b7b5af6e8c53dc8b0353934537f891f1c9` and linked from PR22.
No scanned scientific registry/crosswalk at any pin uses a final ID from these
ranges yet. The ledgers reserve them for this topic; no competing owner
reserves an overlapping range. This recheck preserves that priority and adds
no range or retrospective headroom.

| Source | T reserved through | N reserved through | IDEA reserved through | LIT reserved through |
|---|---:|---:|---:|---:|
| Prior reservations before PR22 (including PR21 literature) | 285 | 99 | 375 | 561 |
| PR22 unchanged topic reservation | 293 | 103 | 383 | 573 |
| PR23, now merged into main | 323 | 115 | 413 | 581 |
| PR24, open | 363 | 131 | 453 | 593 |

The **union maxima including permanent unused ranges are T363, N131,
IDEA453 and LIT593**. These are occupied/reserved maxima, not instructions to
allocate new IDs. The later PR23 ranges T294–323/N104–115/IDEA384–413/
LIT574–581 were first published at `e79c5767ff1e354b018861d827f67a481ee65cdf`;
main now assigns T294–300, N104–107 and IDEA384–397 and retains permanent gaps
T301–323/N108–115/IDEA398–413/LIT574–581. PR24 first publication
`40b3eb645c1dc066a8e646b79c67eaa00f4fa181` reserves the strictly later disjoint
T324–363/N116–131/IDEA414–453/LIT582–593. Neither changes PR22's older priority.

Earlier full reservations and gaps remain in force. In particular the scan
retains T104–105; T118–135/N054–061/IDEA228–245/LIT429–444;
T147–155/N064–071/IDEA268–285/LIT445–459;
T198–205/N074–077/IDEA312–315; T236–245/LIT460–465;
T253–265/N087–091/IDEA349–355/LIT471–473; and
T272–285/N092–099/IDEA359–375/LIT474–481. This list highlights recorded
unused headroom; the complete pinned ledgers, not this abbreviated list,
remain the reservation authority. PR21 retains LIT482–561 even though its
pinned scientific registries still use provisional literature identifiers.
Same-source deduplication must consult PR21's source aliases before assignment.

Qualified **textual mention** maxima across the four registries at each pin
are main T300/N107/IDEA397/LIT470; PR21 T236/N083/IDEA335/LIT460;
PR22 T252/N086/IDEA348/LIT470; PR24 T236/N083/IDEA335/LIT460.
These are neither assignment counts nor reservation maxima: for example the
T236 and LIT460 historical gap references are not canonical new claims.
Foreign bttb literature aliases (including LIT1729/1750 and older four-digit
source references) are excluded from Padua maxima. Historical “next
unreserved” columns and prose are preserved as chronology and never treated
as additional reservations or permission to reuse an earlier gap.

Verification performed: complete pinned file reads and SHA-256 hashing;
qualified numeric mention extraction; exact overlap search for all four
NN-MOP ranges across every scanned registry/crosswalk; comparison of the
existing reservation endpoints and the later PR23/24 blocks. No competing
use, collision or ambiguous priority was found within these pinned inputs.
Readiness still requires the orchestrator's final live-head check if refs move.
