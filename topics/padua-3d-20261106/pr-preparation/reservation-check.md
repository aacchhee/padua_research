# Reservation union check — 2026-11-12

Rules read at `c8691c5d4afcbb17506cb052ea48313c865eff35`: AGENTS.md,
agents/WORKFLOW.md, agents/codex/CODEX.md and handoff23. Scope is mechanical
PR preparation; no novelty, research, proof or scientific-status claim is added.
The novelty gate therefore does not apply. Worker: independent Codex subagent;
runtime model and effort were not independently exposed to this worker.

**PASS at the pinned heads below.** No new range or ID is chosen or assigned
by this check. No Git mutation was performed. The coordinator owns allocation,
publication and the subsequent distinct Claude readiness handoff.

| Source | Full head |
|---|---|
| main | `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb` |
| PR33, this topic | `c8691c5d4afcbb17506cb052ea48313c865eff35` |
| PR27, argmax bridge | `8a94ce610594e9f52a23ca6b74b5751719f0d89e` |

The coordinator supplied [the actual REST population snapshot](pr-snapshot.json),
observed at 2026-11-12 13:07:04 UTC:32 PRs, open27/33,30 closed and merged,
none closed-unmerged. This worker checked that input and its open-head identities;
it did not execute the API request. No closed-unmerged ledger needed recovery.

Every `ALLOCATIONS.md` and PROOF_STATUS.md, state/IDEAS.md,
literature/INDEX.md and ID_CROSSWALK.md was read in full at each head:
19+19+20=58 source copies,46 ledger copies,16 distinct ledger blobs and20
distinct blobs overall. The compact [JSON receipt](reservation-check.json)
records the full head/path inventory, Git blob, byte size, line count and SHA-256
for every source version, plus the supplied population-file identity.

| Namespace | Highest assigned row | Highest permanent used/reserved endpoint | Endpoint source |
|---|---:|---:|---|
| PD-T | 548 | 553 | MZ sharp constants:522–553;549–553 unused |
| PD-N | 183 | 185 | NN MOP conditioning:181–185;184–185 unused |
| IDEA | 611 | 615 | MZ sharp constants:608–615;612–615 unused |
| LIT | 633 | 635 | MZ sharp constants:633–635;634–635 unused |

Assigned-row maxima scan the first cell of each numbered row in the three
primary registries. The four-file mention maxima also include crosswalk
reservation acknowledgments and therefore reach the permanent endpoints.

The independent parser includes qualified three-digit IDs, abbreviated ledger
prefixes, omitted-prefix upper endpoints (for example PD-T522–553), and bare
namespace-table ranges (for example PD-T |266–285). Ledger prose/tables retain
all historical blocks and permanent unused gaps. Historical next-free prose and
repeated ownership acknowledgments do not create fresh reservations. No unknown
retired reservation or conflicting owner was found in the checked sources.

PR27 retains T392–431/N146–161/IDEA490–529/LIT598–613; its unchanged ranges
are included even where main merely acknowledges them. Foreign four-digit
literature strings are BTTB source identifiers/aliases, not local assigned IDs:
1160,1185,1317,1325,1586,1658,1729 and1750. In particular the explicit
LIT-1729/1750 citation-correction context does not enlarge Padua's namespace.
The JSON receipt lists every observed four-digit alias; provisional `?` IDs
are excluded from final-ID maxima.

Verification executed: recursive `git ls-tree`, full `git show` for all58
copies, `git rev-parse` for source blobs, SHA-256 on full bytes, independent
namespace/range extraction, and assertions for the population, endpoint maxima
and assigned-row maxima. This is a frozen preparation check; repeat the complete
live main/open-PR/closed-unmerged refresh at readiness, and again if source
ledgers change before AC's merge. No readiness approval is inferred here.
