# PR24 preparation reservation union — 2026-11-05

**PASS at the pinned inputs below.** The permanent T324–363 / N116–131 /
IDEA414–453 / LIT582–593 ranges are uncontested. Their first publication remains
`40b3eb645c1dc066a8e646b79c67eaa00f4fa181`, linked from PR24. No fresh range,
final assignment, accepted-ID renumbering or Git mutation is performed here.

Worker: Codex, gpt-6.1-sol medium; rules read at
`a3f03be58be6819d833523ef26ccff69f5bc184a` (AGENTS, WORKFLOW and CODEX),
plus handoff10 and audit02's reservation/preparation instructions. This bounded
mechanical inventory adds no scientific claim, mechanism or novelty verdict;
the scientific novelty gate does not apply. No scientific runs were executed.

## Population and full-file coverage

The orchestrator supplied [live-prs.json](live-prs.json) from
`GET /repos/aacchhee/padua_research/pulls?state=all&per_page=100`: 26 PRs,
open 24/27, 24 closed and merged, none closed-unmerged. This worker performed
no independent network query. PR21 is now merged, superseding the stale open
label in handoff10's reservation subsection. PR25/26/21 are included via main.

| Input | Complete SHA |
|---|---|
| main | `b4d292eea5eed373002506d5e16a3761bd7ae10e` |
| remote PR24 | `29a78ec132d94d253816fd103d6ffb574de25e3b` |
| remote PR27 | `f708a83c705a8e8c61ce8fc9ff94e2e531b62951` |
| own main integration | `a3f03be58be6819d833523ef26ccff69f5bc184a` |

Executed from repository root:
`python topics/padua-lanczos-frontier-20261105/preparation/scan_allocations.py`.
The checker reads every complete `*/ALLOCATIONS.md` and all four complete
registries (PROOF_STATUS, state/IDEAS, literature/INDEX and ID_CROSSWALK) at each
pin: **57 complete file copies: 41 ledgers and 16 registries; 13 distinct ledger
versions and 21 distinct versions overall**. The
[compact receipt](allocation-scan.json) records each path/blob, per-head file
indices, SHA256, bytes, line counts and maxima. Receipt size is 8,137 bytes.
Complete raw file snapshots and the full per-copy manifest remain outside Git
under `/tmp/padua-lanczos-frontier-preparation/`; the receipt records the
manifest identity and the script regenerates these temporary conveniences
from pinned Git. No external archive or independent audit is claimed.

All 13 unique complete ledger texts were reviewed, including both shared-batch
versions, historical owner prose, imported reservation tables, priority and
permanent gaps. The fresh-range procedure supersedes historical owner-only
instructions; no existing reservation is changed. No unreconstructed retired
range was found. The complete supplied PR population has no closed-unmerged
PR requiring another ledger recovery.

The token inventory includes abbreviated namespace/endpoints such as
`T364–375` and bare table ranges such as `PD-T | 266–285`. Bare T/N forms are
interpreted only in ledgers: registry EX-T852/EX-T516 are source aliases and
N512 is a numerical parameter. Four-digit BTTB literature references are
foreign aliases, excluded from the Padua namespace. Historical next-free
boundaries do not establish reservations. Numeric maxima supplement the
complete ledger review; they do not establish ownership by themselves.

## Union and preserved ownership

| Namespace | Maximum used or permanently reserved | Own unchanged range | PR27 range |
|---|---:|---|---|
| PD-T | 431 | 324–363 (40) | 392–431 (40) |
| PD-N | 161 | 116–131 (16) | 146–161 (16) |
| IDEA | 529 | 414–453 (40) | 490–529 (40) |
| LIT | 613 | 582–593 (12) | 598–613 (16) |

PR27 explicitly acknowledges PR24's ranges and reserves strictly above the
previous maxima T391/N145/IDEA489/LIT597. Its local ledger is included even
though shared-ledger import remains deferred. Repeated foreign mentions of
PR24's ranges acknowledge their original owner, rather than claiming them.
The checker verifies every own range at first publication and integration,
and verifies that **every ID in the own four ranges is absent from
PROOF_STATUS, IDEAS and INDEX at all four pins**. Crosswalk reservation
acknowledgments are included in the union and reviewed as prose. There is no
foreign assignment or competing reservation in the own ranges.

Merged PR25 reserves T364–375/N132–137/IDEA454–465/LIT594–597 and assigns
T364–370/N132/IDEA454–461, no LIT. Merged PR26 reserves
T376–391/N138–145/IDEA466–489, no LIT, and assigns T376–381/IDEA466–471,
no N or LIT. Merged PR21 reserves LIT482–561 and assigns LIT482–512;
LIT513–561 remain permanent gaps. These unchanged neighboring reservations
are disjoint from PR24, as are PR23's earlier T294–323/N104–115/
IDEA384–413/LIT574–581 and every earlier historical allocation.

Explicit permanent unused ranges preserved by the complete ledgers include:

| PR | T gaps | N gaps | IDEA gaps | LIT gaps |
|---|---|---|---|---|
| 9 | 104–105 | — | — | — |
| 14 | 118–135 | 054–061 | 228–245 | 429–444 |
| 15 | 147–155 | 064–071 | 268–285 | 445–459 |
| 12 | 198–205 | 074–077 | 312–315 | — |
| 17 | 236–245 | — | — | 460–465 |
| 19 | 253–265 | 087–091 | 349–355 | 471–473 |
| 20 | 272–285 | 092–099 | 359–375 | 474–481 |
| 21 | — | — | — | 513–561 |
| 22 | 291–293 | 101–103 | 380–383 | 569–573 |
| 23 | 301–323 | 108–115 | 398–413 | 574–581 |
| 25 | 371–375 | 133–137 | 462–465 | 594–597 |
| 26 | 382–391 | 138–145 | 472–489 | — |

This check allocates none of the own ranges. They have sufficient headroom
for handoff10's stated 16 T / 3 N / 19 IDEA proposals; L6-02 and L4b reuse
existing IDEA records. Final mapping and any eventual own unused gaps belong
to the orchestrator's following preparation step. No fresh range is needed
for that stated count. PASS applies to these pins; any changed live foreign
reservation requires a refresh before assignment/readiness.

## Immediate preassignment refresh — 2026-11-05

**PASS refreshed.** The orchestrator's Git-ref check found PR27 advanced to
`95366c19562e88c11138f88aab0a6617d6b15305`; main b4d292e and remote PR24
29a78ec are unchanged. The population record now preserves the original API
snapshot head separately and records this Git-ref refresh. The checker pins
PR27's new head and was rerun against all four complete head inventories,
reading every ledger and all four registries again. All 15 PR27 ledger/registry
files have the same complete bytes and path set at its old and new heads;
this comparison was executed separately from the full union rerun. The
reservation-changing inputs are therefore unchanged. Coverage remains
57 complete copies / 41 ledgers / 13 distinct ledger versions / 21 distinct
versions overall. Union maxima remain T431/N161/IDEA529/LIT613, with no
collision or foreign assignment in PR24's ranges. The compact receipt and
temporary raw snapshots/full manifest now identify PR27 at the new head.
The earlier pin table above records the original scan; this dated refresh
supersedes its PR27 pin for the preassignment result.
