# Padua batch allocation ledger — 2026-10-31

This is the batch ledger requested by AC for the charter, MZ and bivariate-Lanczos topics. Allocation owner for this batch overlay: **root Codex MZ orchestrator**. Developers/auditors do not allocate independently. Existing reservations are immutable; this overlay imports the charter topic's already allocated IDs, then assigns disjoint ranges to MZ. No accepted ID is renumbered.

## Reconciliation evidence

Both topics use base/rules `d36722823441dc40c6e19d69a174459348dd309c`. At MZ preparation, `git fetch origin main codex/charter-unisolvence-20261031` fetched that unchanged main and charter head `eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64`. GitHub open-PR query returned draft [#2](https://github.com/aacchhee/padua_research/pull/2), whose standalone ledger at `topics/charter-unisolvence-20261031/ALLOCATIONS.md` was read in full. Its earlier empty-PR observation is historical; the present topic does not override its reservations. No batch ledger existed at that pinned charter head.

MZ scientific checkpoint before final-ID substitution: `2dc9264333cdf8372947448f4b9bdd3bb577d0e1`. Exact MZ map: [MZ final-id-map.json](https://github.com/aacchhee/padua_research/blob/fdf0648cbaa9fb722c611d709e638de7dfe86368/topics/mz-constants/final-id-map.json); original scientific file hashes: [MZ preallocation-hashes.json](https://github.com/aacchhee/padua_research/blob/fdf0648cbaa9fb722c611d709e638de7dfe86368/topics/mz-constants/preallocation-hashes.json).

| Namespace | Existing charter reservation | MZ reservation | Next unreserved |
|---|---|---|---|
| PD-T | PD-T001–PD-T012 | PD-T013–PD-T028 | PD-T029 |
| PD-N | PD-N001 | PD-N002–PD-N006 | PD-N007 |
| LIT | LIT-001–LIT-041 | LIT-042–LIT-060 | LIT-061 |
| IDEA | IDEA-001–IDEA-051 | IDEA-052–IDEA-076 | IDEA-077 |

| Member | Pinned head / ownership | Dependencies and integration order |
|---|---|---|
| codex/charter-unisolvence-20261031, draft PR #2 | eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64; previous standalone owner root Codex | first; owns the charter, which MZ must not author |
| codex/mz-constants-20261031 | scientific checkpoint above; this batch overlay owner | second; scientific proofs independent, shared state depends on preserving the first topic's rows |
| claude/bivariate-lanczos-20261031 | no published reservation or open PR observed in this check | must reconcile with this owner and refresh ledger before allocating; no range inferred from absence |

## Coordination and readiness limits

This overlay reconciles the observed reservations without changing the other branch. There is no acknowledgement from the already completed charter chat in this session, and its PR/log still point to its historical standalone ledger. Adoption of this batch ledger by that member, and reconciliation with any unpublished Lanczos reservations, remain **pending batch coordination before merge readiness**. Neither absence of a remote PR nor this overlay authorizes a competing allocation. Keep MZ draft while this remains unresolved.

Before requesting AC's squash sequence, refresh all member heads, preserve their accepted IDs, link this ledger from every member log/PR and crosswalk, rehearse the sequential squash integration, and resolve shared-registry conflicts. MZ records its actual rehearsal and conflicts in its integration record. Only AC merges; this ledger authorizes no main mutation or published-history rewrite.

## Lattice campaign adoption and programme-ledger reconciliation

2026-10-31, lattice root orchestrator adopts this shared path. It also read the independent programme ledger at origin/claude/programme-ideas-20261031 (a02bc357e5f0eed479f7020b85fecc57fda9b47f at this fetch; its internal ledger retains earlier head observations), which records the same charter block, only provisional programme/Lanczos/MZ entries at its older observation, and the policy that the next preparing orchestrator refreshes and reserves the next free block. The later published MZ final reservations above supersede that older observation for MZ only; no programme or Lanczos final range has been inferred or overwritten. Existing final reservations are preserved. No new final range is reserved at lattice launch.

| Additional / refreshed member | Pinned base/head seen | Dependency / order / reservations |
|---|---|---|
| codex/charter-unisolvence-20261031 | original eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64; audit head 3bd9d4e8e7817eaf0abd5b7a750ea77eb8101342 | PR #2 first; mathematics accepted by Claude audit-01, protocol responses pending; IDs unchanged |
| codex/mz-constants-20261031 | remote fdf0648cbaa9fb722c611d709e638de7dfe86368, PR #3 | after charter; ranges above preserved; no lattice scientific dependency |
| claude/bivariate-lanczos-20261031 | remote 6673669103d59c4a955071dd3301408604413ed8 (launch fetch) | provisional only at fetched head; no lattice scientific dependency; refresh before allocation |
| claude/programme-ideas-20261031 | remote a02bc357e5f0eed479f7020b85fecc57fda9b47f (launch fetch) | provisional only at fetched head; ledger owner policy above; no lattice scientific dependency |
| codex/lattice-unisolvence-20261031 | starts at eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64, merges charter audit 3bd9d4e | **stacked on charter, target charter branch; must merge only AFTER charter PR #2**. C0/C3/LIT provisional namespaces only; no final reservations yet |

Order constraint: charter first, then MZ/lattice/Lanczos/programme in AC's chosen order, with shared-registry reconciliation at each integration. The MZ preference for second is preserved as a proposal, not a new dependency. Lattice does not rewrite, push, or repair other member branches. Programme rule changes are outside lattice scope and not silently adopted. External member acknowledgements and final sequential squash rehearsal remain readiness conditions; a draft may preserve work while pending.
