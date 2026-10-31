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

## Lattice campaign adoption and programme-ledger reconciliation

2026-10-31, lattice root orchestrator adopts this shared path. It also read the independent programme ledger at origin/claude/programme-ideas-20261031 (a02bc357e5f0eed479f7020b85fecc57fda9b47f at this fetch; its internal ledger retains earlier head observations), which records the same charter block, only provisional programme/Lanczos/MZ entries at its older observation, and the policy that the next preparing orchestrator refreshes and reserves the next free block. The later published MZ final reservations above supersede that older observation for MZ only; no programme or Lanczos final range has been inferred or overwritten. Existing final reservations are preserved. No new final range is reserved at lattice launch.

| Additional / refreshed member | Pinned base/head seen | Dependency / order / reservations |
|---|---|---|
| codex/charter-unisolvence-20261031 | original eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64; audit head 3bd9d4e8e7817eaf0abd5b7a750ea77eb8101342 | PR #2 first; mathematics accepted by Claude audit-01; protocol response now imported at317a265; IDs unchanged |
| codex/mz-constants-20261031 | remote fdf0648cbaa9fb722c611d709e638de7dfe86368, PR #3 | after charter; ranges above preserved; no lattice scientific dependency |
| claude/bivariate-lanczos-20261031 | remote 6673669103d59c4a955071dd3301408604413ed8 (launch fetch) | provisional only at fetched head; no lattice scientific dependency; refresh before allocation |
| claude/programme-ideas-20261031 | remote a02bc357e5f0eed479f7020b85fecc57fda9b47f (launch fetch) | provisional only at fetched head; ledger owner policy above; no lattice scientific dependency |
| codex/lattice-unisolvence-20261031 | starts at eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64, merges charter audit 3bd9d4e | **stacked on charter, target charter branch; must merge only AFTER charter PR #2**. C0/C3/LIT provisional namespaces only; no final reservations yet |

Order constraint: charter first, then MZ/lattice/Lanczos/programme in AC's chosen order, with shared-registry reconciliation at each integration. The MZ preference for second is preserved as a proposal, not a new dependency. Lattice does not rewrite, push, or repair other member branches. Programme rule changes are outside lattice scope and not silently adopted. Any remaining member acknowledgements and final sequential squash rehearsal remain readiness conditions; a draft may preserve work while pending.

## Lattice refresh after charter response

Lattice fetched main and all members again before preparation: main d36722823441dc40c6e19d69a174459348dd309c; charter317a26597dedc9adc9cfc6a26fa00078df7d29e4; MZ6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994; Lanczos1127f9c73903e11b56cbfe3e8c667bfcbe810beb; programmea02bc357e5f0eed479f7020b85fecc57fda9b47f. Charter response is merged into lattice without rewriting history. The parent ledger above is preserved; this annex adds the fifth member. Existing final ranges and MZ allocation ownership remain unchanged. AC explicitly requested provisional lattice theory IDs, so lattice reserves only its topic-scoped provisional namespaces through this AUDIT/draft handoff; final allocation remains with the named owner and requires coordination before readiness. No competing final range is allocated.

## Lattice provisional reservations at AUDIT preparation

AC explicitly requested provisional theory IDs; no new final global range is reserved. The named MZ allocation owner remains responsible for coordinated final allocation before readiness. These topic-scoped IDs cannot collide with another topic’s provisional namespace. Exact map: [provisional-id-map.json](../lattice-unisolvence-20261031/provisional-id-map.json).

| Namespace | Reserved provisional identifiers | Owner / status |
|---|---|---|
| PD-T | PD-T?lattice-c0-codex-01; PD-T?lattice-c0-codex-02; PD-T?lattice-c0-codex-03; PD-T?lattice-c1-codex-01; PD-T?lattice-c1-codex-02; PD-T?lattice-c1-codex-03; PD-T?lattice-c1-codex-04; PD-T?lattice-c1-codex-05; PD-T?lattice-c1-codex-06; PD-T?lattice-c3-codex-01; PD-T?lattice-c3-codex-02; PD-T?lattice-c3-codex-03; PD-T?lattice-c3-codex-04; PD-T?lattice-c3-codex-05 | lattice root; AUDIT, final allocation deferred |
| PD-N | PD-N?lattice-c0-codex-01; PD-N?lattice-c1-codex-01; PD-N?lattice-c1-codex-02; PD-N?lattice-c3-codex-01; PD-N?lattice-c3-codex-02; PD-N?lattice-c3-codex-03; PD-N?lattice-c3-codex-04 | lattice root; AUDIT, final allocation deferred |
| IDEA | IDEA?lattice-c0-codex-01; IDEA?lattice-c0-codex-02; IDEA?lattice-c0-codex-03; IDEA?lattice-c0-codex-04; IDEA?lattice-c0-codex-05; IDEA?lattice-c1-codex-01; IDEA?lattice-c1-codex-02; IDEA?lattice-c1-codex-03; IDEA?lattice-c3-codex-01; IDEA?lattice-c3-codex-02; IDEA?lattice-c3-codex-03; IDEA?lattice-c3-codex-04; IDEA?lattice-c3-codex-05 | lattice root; AUDIT, final allocation deferred |
| LIT | LIT?lattice-codex-01; LIT?lattice-codex-02; LIT?lattice-codex-03; LIT?lattice-codex-04; LIT?lattice-codex-05; LIT?lattice-codex-06; LIT?lattice-codex-07; LIT?lattice-codex-08; LIT?lattice-codex-09; LIT?lattice-codex-10; LIT?lattice-codex-11; LIT?lattice-codex-12; LIT?lattice-codex-13; LIT?lattice-codex-14; LIT?lattice-codex-15; LIT?lattice-codex-16; LIT?lattice-codex-17; LIT?lattice-codex-18; LIT?lattice-codex-19; LIT?lattice-codex-20; LIT?lattice-codex-21; LIT?lattice-codex-22; LIT?lattice-codex-23; LIT?lattice-codex-24; LIT?lattice-codex-25; LIT?lattice-codex-26; LIT?lattice-codex-27; LIT?lattice-codex-28; LIT?lattice-codex-29; LIT?lattice-codex-30; LIT?lattice-codex-31; LIT?lattice-codex-32 | lattice root; AUDIT, final allocation deferred |

Charter→lattice direct squash rehearsal and the wider batch conflict observation are recorded in [integration-rehearsal.md](../lattice-unisolvence-20261031/integration-rehearsal.md). No whole-batch merge readiness or external acknowledgement is inferred. Parent response317a265 adoption is preserved above. Only AC merges; lattice follows charter PR#2.

## Parent integrated before lattice publication

AC merged charter PR#2 at08fafe62d9798385dfafaacc9a41344272737e68 and deleted its branch. Lattice merged that main at a9e519ac3e0ff65f4ede8954d4630f2160600301 with no file changes because its parent tree already matched. Lattice now targets main; the original charter-first dependency and all reservations remain preserved. The wider MZ/later-member reconciliation is still required before batch readiness. No live PR was merged by this lattice agent.
