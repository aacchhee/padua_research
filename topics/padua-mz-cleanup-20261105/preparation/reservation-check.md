# Handoff04 allocation union recheck — PASS

2026-11-05. Administrative preparation worker: Codex, actual inherited
`gpt-6.1-sol`, xhigh. Rules/role read at
`a930f32fbf4568fbc431ddcf0b0fd689f5fa8201`.
This check adds no scientific claim or novelty claim and assigns no identifier;
the scientific novelty gate is therefore outside its scope.

The [compact receipt](allocation-scan.json) pins all heads, every source path,
Git blob, complete-file SHA-256, size, line count and namespace maxima.
The parent orchestrator refreshed main and all open PRs (drafts included),
reported open PRs **21, 24, 25, 26**, and reported no result for the GitHub
closed `is:unmerged` search. PR25 is the argmax phase-2 branch; there is no
additional separate argmax phase-2 branch in that population. This worker
used those live population observations rather than independently querying
GitHub.

| Pin | Complete head SHA |
|---|---|
| main | `aff30e8ad5542c94fab642ae024dc9aab4fa7ad7` |
| PR21 | `3ed6c94246f21353350f82712b6628b39db6f65a` |
| PR24 | `60126006dcc7c814680ed87d4fef8d9f9404a3d7` |
| PR25 | `3fe945e54a2666b8ec0004d90ec1dfa54ae80703` |
| PR26 | `a930f32fbf4568fbc431ddcf0b0fd689f5fa8201` |

Executed the [reproducer](scan_allocations.py) from the repository root:

```sh
python topics/padua-mz-cleanup-20261105/preparation/scan_allocations.py
```

It read **59 complete ledger/registry copies**, comprising **15 distinct
blobs: 11 ledgers and four canonical registries**. Every `ALLOCATIONS.md`
found recursively at each pin was included, together with the complete
`PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md` and
`ID_CROSSWALK.md`. Each canonical registry is byte-identical across all five
pins. The full-file parser checks every qualified three-digit ID token and
bare namespace-table range; complete unique ledgers were also reviewed for
compressed ranges, inherited history, permanent unused headroom and retired
reservation obligations. Foreign four-digit BTTB LIT aliases are excluded.
Historical next-free boundaries confer no reservation and do not increase
the final maxima below. No unrecorded retired range was identified in these
ledgers, and the parent found no closed-unmerged PR requiring recovery.

| Namespace | Foreign used/reserved maximum | Union including cleanup | Cleanup permanent reservation | Eligible assignment now |
|---|---:|---:|---|---|
| PD-T | 375 | 391 | 376–391 (16) | 376–381 (6) |
| PD-N | 137 | 145 | 138–145 (8) | none |
| IDEA | 465 | 489 | 466–489 (24) | 466–471 (6) |
| LIT | 597 | 597 | no range | none |

The upper foreign blocks are PR24's T324–363/N116–131/IDEA414–453/
LIT582–593 and PR25's T364–375/N132–137/IDEA454–465/LIT594–597.
PR21's LIT482–561 remains reserved. All earlier accepted blocks and permanent
gaps in the shared and topic ledgers remain binding, including ranges left
unused by merged PRs. No other branch or canonical registry reaches any
cleanup ID. Thus the entire cleanup reservation, as well as the proposed
six theory and six idea assignments, has **zero foreign overlaps**.

Cleanup's reservation was first added in
[`ee490356ce51d5e2f4a84f2c45e6ccb98a19bd90`](https://github.com/aacchhee/padua_research/commit/ee490356ce51d5e2f4a84f2c45e6ccb98a19bd90),
as verified by read-only Git addition history and the complete ledger at
that commit. Its original range/count rows exactly match the current ledger.
The current ledger attests that pushed first publication and links
[PR26](https://github.com/aacchhee/padua_research/pull/26); this check preserves
that priority and makes no new reservation. Git alone establishes the
addition commit, while the existing ledger supplies the pushed-publication
attestation. There is no collision requiring a priority repair.

**Disposition:** the orchestrator may assign only PD-T376–381 and
IDEA466–471 from the existing reservation during this preparation step.
After that assignment, T382–391, N138–145 and IDEA472–489 remain permanent
unused gaps. No LIT or PD-N assignment is needed. No accepted ID is
renumbered, no range is moved, and no headroom is added. Readiness still
requires the orchestrator's final live-head/population refresh; any changed
foreign allocation evidence must be rechecked before readiness.

The JSON receipt is 6,749 bytes. The optional bulk inventory under
`/tmp/mz-prep-allocation/full-inventory.json` is local convenience, with its
hash/size recorded in the receipt; it is not required for durable retrieval.
All source identities are compactly represented in the committed receipt
and the bulk inventory is reproducible from pinned Git objects. No bulk
output was split into repository files or represented as archived cold storage.
