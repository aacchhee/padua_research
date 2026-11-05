# ID reservations — padua-literature-20261103

Procedure: agents/WORKFLOW.md, "Reserve fresh ranges; never reallocate". Reserved 2026-11-03 by Claude (claude-opus-5-5) when the draft PR was opened. **No final IDs are assigned yet.**

| Namespace | Range | Count | Branch | Note |
|---|---|---|---|---|
| LIT | LIT-482–LIT-561 | 80 | claude/padua-literature-20261103 | Provisional IDs `LIT?padua-literature-claude-NN` map into this range at PR preparation. Unused IDs remain permanent gaps. |
| PD-T | no range | — | — | This is a literature topic; it makes no theory claims. |
| PD-N | no range | — | — | — |
| IDEA | no range | — | — | No ideas are registered; the P4 proposals are for a later topic. |

## Heads checked (2026-11-03)

- main `440d1079e42c3ef21c40d1cf8870f5b206410c6a`: highest LIT in INDEX/PROOF_STATUS/ID_CROSSWALK/ledgers is LIT-465. LIT-1729…1750 strings are bttb-research aliases, not Padua IDs.
- PR #19 `codex/padua-argmax-effective-20261103` @ `e5149eadfe`: reserves LIT-466–473 (first pushed reservation ed8db2f).
- PR #20 `codex/padua-lebesgue-followups-20261103` @ `bb05df2f73`: reserves LIT-474–481 (first published 514e376).
- Closed, unmerged PRs: none (REST listing, 2026-11-03).
- Retired reservations in the batch ledger copies on these heads: none above LIT-465.
- Maximum in the LIT namespace: 481. This range therefore starts at 482.

Priority is the pushed commit that adds this file, as linked from the draft PR.

## Final assignment — 2026-11-05

Fresh union at main9322fba and open PR21/24: [receipt](preparation/allocation-scan.json). Assigned31 new statement IDs LIT-482–512;27 provisional aliases reuse existing statement IDs. [Exact58-alias map](preparation/final-id-map.json), [deduplication](preparation/literature-dedup.md). Permanent unused gaps LIT-513–561. No new reservation, no renumbering and no PD-T/PD-N/IDEA assignment. Original first-publication priority is unchanged. Earlier “no final IDs” prose is historical and superseded only by this preparation entry.
