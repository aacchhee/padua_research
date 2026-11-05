# Fresh allocation union review — 2026-11-05

Rules read at `2fb2f7502bb8d1b46c0fe1089588c46a06df258d`:
AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md; handoff 01 read.
Worker role: mechanical inventory and protocol development, gpt-6.1-sol medium.
No Git mutation, reservation or final-ID assignment was performed. This is an
allocation check, with no new mechanism or novelty claim, so a novelty gate is
not applicable. No mathematical audit is claimed.

## Pinned source population

The orchestrator supplied its live all-state GitHub connector classification:
open PRs 21, 22, 24; 21 closed PRs, all merged; no closed-unmerged PR. The
worker did not independently rerun the GitHub population query. All files were
read directly from the following immutable Git objects:

| Source | Full head SHA |
|---|---|
| origin/main | `21dbfc90257b952d8923f6d01739d12aa8d6e0a1` |
| PR21, claude/padua-literature-20261103 | `890f56ccde35431b70b43141c224b0b8817fea7f` |
| PR22, codex/nn-mop-iep-20261103 | `1de5891ee622e826d7553819152aa261b02faaa9` |
| PR24, codex/padua-lanczos-frontier-20261105 | `79c3d6a211325eca6e8311b3ae03187c100a1d8a` |

The [receipt](allocation-scan.json) enumerates every complete file version by
path, SHA-256 and byte count; each source maps to those entries. It covers 40
ledger/registry reads and 23 distinct path/content versions, including 11 ledger
versions. Every `*/ALLOCATIONS.md` found recursively at each head was included,
and each head's complete PROOF_STATUS.md, state/IDEAS.md, literature/INDEX.md and
ID_CROSSWALK.md was scanned for final identifiers. The 11 complete ledger
versions were manually reviewed. The main shared ledger was read in full;
other shared-ledger copies were reviewed through exact diffs, whose unchanged
bytes match the already read text. The registries received complete machine
reads for allocation inventory, not a full scientific/novelty review.

## Endpoint review and result

| Namespace | Maximum qualified registry mention | Maximum used or reserved | Suggested fresh range | Count / estimated need |
|---|---:|---:|---|---:|
| PD-T | 300 | 363 | PD-T364–PD-T375 | 12 / 8 |
| PD-N | 107 | 131 | PD-N132–PD-N137 | 6 / 4 |
| IDEA | 397 | 453 | IDEA-454–IDEA-465 | 12 / 8 |
| LIT | 568 | 593 | LIT-594–LIT-597 | 4 / 2 |

These are suggestions only. The highest reservation in each namespace is PR24's
unchanged T324–363, N116–131, IDEA414–453, LIT582–593, first published at
`40b3eb645c1dc066a8e646b79c67eaa00f4fa181`. PR21 retains LIT482–561;
PR22 retains T286–293/N100–103/IDEA376–383/LIT562–573, including its unused
gaps T291–293/N101–103/IDEA380–383/LIT569–573. The PR22 branch has final
assignments already; those were included through all four registries.

Main includes the complete historical batch ledger and merged PR19, PR20 and
PR23 topic ledgers/imports. Unused headroom stays unavailable, specifically
phase 1's T253–265/N087–091/IDEA349–355/LIT471–473; PR20's
T272–285/N092–099/IDEA359–375/LIT474–481; PR23's
T301–323/N108–115/IDEA398–413/LIT574–581; and the older batch gaps such as
T236–245 and LIT460–465. No closed-unmerged reservation recovery is required
under the supplied PR classification. Historical owner-only prose is explicitly
superseded by the fresh-range procedure; recorded old ranges remain permanent.

Manual endpoint review includes namespace-column ranges such as `PD-T | 266–285`
and abbreviated ranges such as `T294–323`, `N104–115`, `IDEA384–413` and
`LIT574–581`. Their final endpoints were included even where a simple
fully-qualified-token regex would miss them. Historical next-unreserved values
and superseded recommendations are not treated as actual reservations.

All four-digit LIT mentions in the registry union were inspected in context:
1160, 1185, 1317, 1325, 1586, 1658, 1729 and 1750 are foreign bttb-research
aliases, not Padua allocations. Explicit `?` provisional identifiers were not
counted as final. No unknown higher Padua identifier or unexplained retired
reservation was found within these snapshots.

## Reproduction and remaining limits

Executed from the repository root:

```sh
python topics/padua-argmax-effective-2-20261105/code/allocation_scan.py
```

The command reads complete pinned Git files, hashes them, scans registry ID
mentions, and writes the compact receipt (6,407 bytes in this run). The script
records the human-reviewed reservation maxima separately; it does not pretend
that regex extraction alone proves which ledger mentions reserve IDs. Its
fixed foreign-alias exclusions reflect the explicit context review above.

The result is conditional on the orchestrator's PR population classification
and valid only at the recorded heads. Refresh all live heads and the PR
population immediately before publishing a reservation; any changed ledger or
registry must be reread. The orchestrator must record any actual reservation
in the topic ledger and PR body with the checked heads, then link its first
pushed commit. No such publication or allocation is claimed by this review.
