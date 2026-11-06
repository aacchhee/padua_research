# ID allocations — nn-mop-conditioning-20261106

Owner: `codex/nn-mop-conditioning-20261106`, PR [32](https://github.com/aacchhee/padua_research/pull/32). Date: 2026-11-06.

| Namespace | Reserved range | Count | Planned assignments | Permanent unused gaps |
| --- | --- | --- | --- | --- |
| PD-T | PD-T502–521 | 20 | PD-T502–517 | PD-T518–521 |
| PD-N | PD-N181–185 | 5 | PD-N181–183 | PD-N184–185 |
| IDEA | IDEA590–607 | 18 | IDEA590–603 | IDEA604–607 |
| LIT | no range | 0 | Existing sources only | none |

The full union check read every ALLOCATIONS.md plus PROOF_STATUS.md, state/IDEAS.md, literature/INDEX.md and ID_CROSSWALK.md at each head below (86 source copies). Union maxima before this reservation: PD-T501, PD-N180, IDEA589, LIT632. All 28 closed PRs were merged; no closed-unmerged reservation required separate retrieval. Recorded retired reservations and permanent gaps remain in force. Foreign bttb LIT aliases are not Padua IDs.

| Head | SHA |
| --- | --- |
| main | `76ba4214b100c86a44941f5e9a662ce9ce48efb8` |
| PR32 | `2f23ee8f554eada30673840318db90b675baba67` |
| PR31 | `95d0b30697d09ff42fe8445b3922cee4c57d8547` |
| PR27 | `2e4ac49fa0687a7736bc1df82c12e6483b1c7a94` |
| PR33 | `9b8193438e2f66d7ba621dfca5cf6d71260ed172` |

[Source identities and counts](preparation/reservation-check.json). Priority is the first pushed commit containing this ledger, linked in PR32; the date alone grants no priority. Final alias assignments are recorded in preparation/final-id-map.json and ID_CROSSWALK.md. Readiness must refresh the union before any ready-for-merge decision.

## Readiness refresh — 2026-11-06 (Claude, Opus 5.5 high)

I repeated the full union check immediately before readiness. Every ledger and the PROOF_STATUS, IDEAS, INDEX, ID_CROSSWALK, RESULTS and CURRENT registries were read at these heads:

| Head | SHA |
| --- | --- |
| main | `76ba4214b100c86a44941f5e9a662ce9ce48efb8` |
| PR33 | `d0e1bbb267db9928de97538d9b524fb0068538cd` |
| PR31 | `dd57b6439d539164cdee7ab01a11b6080a03af10` |
| PR27 | `d4956aea3bda9d5ff9917a5b410778fc7adf4fb7` |
| PR32 | `5e82abdb9c675dbcb551c923847c0f3b2cc2cafc` |

All 28 closed PRs are merged. Since this reservation, PR31 has reserved PD-T522–553, IDEA608–615 and LIT633–635, above this range and after checking it at `37547f3`. PR33 reserves nothing. PR27's ranges are older and disjoint.

This topic's ranges, assignments and permanent gaps are unchanged and collision-free. Repeat the check before merge if main or any open PR's ledger changes. Details are in [readiness-01.md](readiness-01.md).
