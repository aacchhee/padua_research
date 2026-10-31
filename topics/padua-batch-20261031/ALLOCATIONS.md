# Batch allocation ledger — padua-batch-20261031

Created 2026-10-31 by the `claude/programme-ideas-20261031` orchestrator (Claude, claude-fable-5-1), as AC instructed, because four topics are open in parallel against base `d36722823441dc40c6e19d69a174459348dd309c` (`origin/main`). This is the single shared ledger for the batch; `ID_CROSSWALK.md` and every member PR/log must link it once the member branches adopt it. Until then, each row below records what the member branch publishes on its own head; nothing here overrides a member's standalone ledger, and conflicts are to be reconciled by the allocation owner before any affected PR becomes ready.

## Members

| Branch | Developer / auditor | Head seen on origin (2026-10-31 ~21:00 UTC) | Allocation state |
|---|---|---|---|
| `codex/charter-unisolvence-20261031` | Codex / Claude | `eb7bdcd` | Standalone ledger `topics/charter-unisolvence-20261031/ALLOCATIONS.md` reserves `PD-T001–012`, `PD-N001`, `LIT-001–041`, `IDEA-001–051` (owner: its root Codex orchestrator). Treated here as the first block. |
| `claude/bivariate-lanczos-20261031` | Claude / Codex | `55320df` | Provisional IDs only (`LIT?bivariate-lanczos-claude-NNN`, `IDEA?bivariate-lanczos-claude-NNN`); no final IDs reserved yet. |
| `codex/mz-constants-20261031` | Codex / Claude | `e9761aa` | Provisional IDs only (`IDEA?mz-constants-codex-NN`); no final IDs reserved yet. |
| `claude/programme-ideas-20261031` | Claude / Codex | this branch | Provisional IDs `LIT?programme-ideas-claude-NN`, `IDEA?programme-ideas-claude-NN`; final ranges to be reserved at PR preparation in the block after the charter's (see below). |

## Allocation owner and order

- Allocation owner for this ledger: the orchestrator of whichever member branch next reaches PR preparation refreshes `origin/main` and the open PRs, then reserves the next free block here and records it in its own `ID_CROSSWALK.md` rows. Parallel writers must not reserve the same block.
- Reserved blocks (final IDs), in integration order:

| Namespace | Range | Owner branch | Content | Status |
|---|---|---|---|---|
| PD-T | 001–012 | charter-unisolvence | see its standalone ledger | reserved by that branch |
| PD-N | 001 | charter-unisolvence | see its standalone ledger | reserved by that branch |
| LIT | 001–041 | charter-unisolvence | see its standalone ledger | reserved by that branch |
| IDEA | 001–051 | charter-unisolvence | see its standalone ledger | reserved by that branch |
| LIT, IDEA, PD-T, PD-N | next free blocks | programme-ideas (this branch) | to be filled at PR preparation | not yet reserved |

- Integration order proposed: charter-unisolvence first (it carries the first final blocks), then the remaining three in whatever order AC merges; each later branch merges `origin/main` before PR preparation and re-checks this ledger.

## Shared rule-file change (affects all members)

Commit `7eeffd8907a8f08a3264a6869594f50e2b930300` on `claude/programme-ideas-20261031` amends `agents/WORKFLOW.md` ("Roles and model allocation" table) and `agents/claude/CLAUDE_ROLES.md`: Claude Fable 5.1 xhigh is added as an allowed Claude model for ideas campaigns (brief, conceptual generation, gating, adversarial idea checks), at AC's explicit request on 2026-10-31. Every existing row is kept and the Codex column is unchanged. The before/after text is in `topics/programme-ideas-20261031/LOG.md`. Member branches may rebase onto or merge this commit; it reaches `main` only through this topic's PR, and the Codex audit of that PR must cover it as a material rule change.

## History

- 2026-10-31: ledger created; member heads and the charter's standalone reservations recorded; rule-file change noted.
