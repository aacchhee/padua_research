# Batch allocation ledger — padua-batch-20261031

This single batch record reconciles the programme-ideas ledger and the later MZ reservation overlay. The charter orchestrator adopts it in response to audit-01 A1. **Allocation owner for subsequent reservations: root Codex MZ orchestrator**, the published owner of the already allocated MZ block. This charter response acknowledges existing reservations and allocates no new IDs. Programme-ideas and bivariate-Lanczos must reconcile with that owner before reserving final ranges; no absence of a PR authorizes a competing reservation. AC alone chooses and performs merges.

## Pinned reconciliation sources

- Programme-ideas ledger: [a02bc357e5f0eed479f7020b85fecc57fda9b47f](https://github.com/aacchhee/padua_research/blob/a02bc357e5f0eed479f7020b85fecc57fda9b47f/topics/padua-batch-20261031/ALLOCATIONS.md), SHA256 `5a79ae39f147e5614041b4b8bf733c3b533d99787c481c8f1f721a085b62b6b0`. It records all four topics, the charter's first block, and charter-first integration.
- MZ overlay: [fdf0648cbaa9fb722c611d709e638de7dfe86368](https://github.com/aacchhee/padua_research/blob/fdf0648cbaa9fb722c611d709e638de7dfe86368/topics/padua-batch-20261031/ALLOCATIONS.md), SHA256 `d797442980d524346846dc4bebdf46483f022e0fcd53d0bf7fd5a63134de2312`. It preserves the charter's block, reserves the next disjoint MZ block, names its allocation owner, and refines the order to charter then MZ.
- [Reconciliation receipt](../charter-unisolvence-20261031/response-01-base.json) pins complete branch heads and source blob IDs. Current main is `d36722823441dc40c6e19d69a174459348dd309c`; open PR query observed draft #2 (charter) and #3 (MZ). The earlier charter observation of no other open PR is retained only as history.

These snapshots differ in freshness, not in ownership of any allocated ID. Their compatible reservations are combined below. Programme-ideas' proposed arbitrary order after charter is narrowed by MZ's published second position; AC can choose a different later order after conflict/allocation reconciliation. The rule-file proposal described by programme-ideas is not imported by this charter response and must be audited through that topic.

## Reservations

| Namespace | Charter block (PR #2) | MZ block (PR #3) | Next unreserved |
|---|---|---|---|
| PD-T | PD-T001–PD-T012 | PD-T013–PD-T028 | PD-T029 |
| PD-N | PD-N001 | PD-N002–PD-N006 | PD-N007 |
| LIT | LIT-001–LIT-041 | LIT-042–LIT-060 | LIT-061 |
| IDEA | IDEA-001–IDEA-051 | IDEA-052–IDEA-076 | IDEA-077 |

The charter [member ledger](../charter-unisolvence-20261031/ALLOCATIONS.md) and [crosswalk](../../ID_CROSSWALK.md) retain every charter mapping. MZ mappings remain on its pinned branch; they are not appended to this PR's scientific registries. No accepted ID is renumbered.

## Integration order and responsibility

| Position | Member / pinned head | Required preparation |
|---|---|---|
| 1 | [Charter PR #2](https://github.com/aacchhee/padua_research/pull/2), audited `eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64`, audit delivery `3bd9d4e8e7817eaf0abd5b7a750ea77eb8101342` | First scientific registry block; no preceding scientific member to reconcile. Address A1–A3 before readiness. |
| 2 | [MZ PR #3](https://github.com/aacchhee/padua_research/pull/3), `fdf0648cbaa9fb722c611d709e638de7dfe86368` | Merge the charter-bearing origin/main, preserve both blocks, resolve shared registry/state conflicts, refresh this ledger, and rehearse the squash sequence before requesting its merge. |
| 3–4, order chosen by AC | bivariate-Lanczos `6673669103d59c4a955071dd3301408604413ed8`; programme-ideas `a02bc357e5f0eed479f7020b85fecc57fda9b47f` | Provisional-only registries at inspection; refresh main and owner reservations, allocate disjoint next blocks, resolve shared files, and rehearse the chosen sequence before readiness. |

The remaining multi-member sequential squash rehearsal is **deferred to the later members**, beginning with MZ. This is the first integration, and audit-01 A1 explicitly permits that disposition. The deferral is not a statement that a full batch rehearsal has passed. No merge order for the entire batch is being requested from AC yet. Before any later merge request, the relevant branch must record its actual rehearsal/conflicts/semantic checks and reconcile all active reservations with the owner. Never rewrite published history or mutate main as part of a rehearsal.

## History

2026-10-31: charter response-01 reconciled the two pinned published ledgers, acknowledged the MZ owner's disjoint block, added the fourth member, and adopted charter-first integration. No new allocation, rule change, proof change or scientific status change.
