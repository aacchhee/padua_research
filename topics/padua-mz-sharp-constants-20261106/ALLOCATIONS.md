# ID allocations — padua-mz-sharp-constants-20261106

Owner: `codex/padua-mz-sharp-constants-20261106`, [PR31](https://github.com/aacchhee/padua_research/pull/31). Date: 2026-11-06. No previous reservation for this topic is reused or replaced.

| Namespace | Reserved range | Count | Planned assignments | Permanent unused gaps |
|---|---|---:|---|---|
| PD-T | PD-T522–553 | 32 | PD-T522–548 (27 records) | PD-T549–553 |
| IDEA | IDEA-608–615 | 8 | IDEA-608–611 (4 new consolidated candidates); existing IDEA-071/386/469/470 reused as continuations | IDEA-612–615 |
| LIT | LIT-633–635 | 3 | LIT-633 (one source report) | LIT-634–635 |
| PD-N | no range | 0 | No new negative claim | none |

Every provisional label is retained in the final map, including fourteen IDEA records consolidated into eight distinct final IDEA IDs. Consolidating records does not release unused headroom: all unused IDs above remain permanent gaps.

## Refreshed union and provenance

[Exact source identities and checked heads](reservation-check.json) cover87 head/path copies,20 unique Git blobs:15 ledger versions and5 registry versions. All ledger prose/tables, retained historical reservations and unused gaps were inspected; all four registry files at every checked head were scanned. No closed-unmerged PR required separate retirement retrieval. Used maxima were PD-T494, PD-N178, IDEA584, LIT630; reserved maxima before this reservation were PD-T521, PD-N185, IDEA607, LIT632.

| Checked head | SHA |
|---|---|
| main | `76ba4214b100c86a44941f5e9a662ce9ce48efb8` |
| PR33 | `9b8193438e2f66d7ba621dfca5cf6d71260ed172` |
| PR32 | `37547f396c42fbb201b2205de929d66ebbd6a005` |
| PR31 input | `95d0b30697d09ff42fe8445b3922cee4c57d8547` |
| PR27 | `2e4ac49fa0687a7736bc1df82c12e6483b1c7a94` |

PR32 published its new allocation while the initial scan was in progress. Its new ledger and crosswalk were refetched and verified before this reservation; PR33's refreshed tree preserved all reservation sources. This topic starts above that updated union. Old four-digit BTTB aliases are not Padua registry IDs. Historical next-free prose never overrides explicit reservations.

Priority is the first pushed commit containing this ledger, linked from PR31; the date alone grants no priority. Only the coordinator publishes this topic's reservation. The readiness check refreshes main, every open PR including drafts, closed-unmerged/retired reservations, ledgers and used IDs again before any ready-for-merge decision. No other branch's ledger or IDs are changed.

Reservation first published in commit [dd57b6439d539164cdee7ab01a11b6080a03af10](https://github.com/aacchhee/padua_research/commit/dd57b6439d539164cdee7ab01a11b6080a03af10), before assignment. [Final map](final-id-map.json) retains every original alias and the distinct eight final IDEA IDs.

## Readiness refresh (2026-11-06, Claude readiness-01)

Repeated steps 1–3 at heads main `64409c4` (PR32 merged), PR27 `389dbc1`, PR33 `d0e1bbb`, PR31 `6fdd9df`; no closed-unmerged PRs. Other owners' maxima: PD-T521, PD-N185, IDEA607 (PR32 on main); PD-T501, PD-N180, IDEA589, LIT632 (PR27/PR33). No collision with PD-T522–553, IDEA-608–615, LIT-633–635; priority commit `dd57b6439d539164cdee7ab01a11b6080a03af10` unchanged; permanent gaps PD-T549–553, IDEA-612–615, LIT-634–635 unused. [readiness-01](readiness-01.md). Repeat if any ledger changes before AC's merge.
