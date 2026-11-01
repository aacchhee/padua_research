# Shared allocation ledger — padua-batch-20261031

This is the single authoritative batch ledger. **Allocation owner: the root Codex MZ orchestrator.** AC explicitly confirmed the integration order for shared registries: charter first, MZ second. PR #2 was merged by AC into main at `08fafe62d9798385dfafaacc9a41344272737e68`; PR #3 is next. Programme-ideas and bivariate-Lanczos follow in AC's chosen order and must obtain a disjoint reservation from this owner before assigning final IDs. The previous programme rule that the next branch reaching PR preparation becomes owner is superseded. No parallel allocation or accepted-ID renumbering is authorized.

## Reconciled sources and provenance

- Merged charter source: branch head `317a26597dedc9adc9cfc6a26fa00078df7d29e4`, integrated by main commit `08fafe62d9798385dfafaacc9a41344272737e68`. Its ledger already reconciled the programme snapshot with the MZ overlay and acknowledged this owner. Its original reservations and charter content have first priority.
- MZ audit delivery: `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`; merge of charter-bearing main into MZ: `bc85509adc303126c6d8276a4457393e81d7f394`. Original scientific checkpoint: `2dc9264333cdf8372947448f4b9bdd3bb577d0e1`; original final-ID package: `fdf0648cbaa9fb722c611d709e638de7dfe86368`.
- Programme source before ledger propagation: `a02bc357e5f0eed479f7020b85fecc57fda9b47f`. Its older ledger SHA-256 is `5a79ae39f147e5614041b4b8bf733c3b533d99787c481c8f1f721a085b62b6b0`. Its records are provisional; no final block is overwritten.
- Bivariate-Lanczos source before ledger propagation: `1127f9c73903e11b56cbfe3e8c667bfcbe810beb`. Its records are provisional and it had no batch ledger at that snapshot. No scientific result from that branch is imported into MZ.

Historical source heads above remain provenance, not assertions that remote tips cannot advance. Propagation commits, exact ledger-byte identity and refreshed heads are recorded in the MZ response's reconciliation receipt. The charter's standalone member ledger is an immutable reservation/provenance record, not a competing batch allocation authority.

## Final reservations

| Namespace | Charter block (merged PR #2) | MZ original block (PR #3) | MZ audit-response addition | Next unreserved |
|---|---|---|---|---|
| PD-T | PD-T001–PD-T012 | PD-T013–PD-T028 | none | PD-T029 |
| PD-N | PD-N001 | PD-N002–PD-N006 | none | PD-N007 |
| LIT | LIT-001–LIT-041 | LIT-042–LIT-060 | LIT-061–LIT-065 | LIT-066 |
| IDEA | IDEA-001–IDEA-051 | IDEA-052–IDEA-076 | none | IDEA-077 |

The five new LIT entries record the targeted audit-M2 screen: Erdős–Feldheim, Askey, Nevai III, Lubinsky's converse-MZ paper, and Smith's Lobatto result. Reading coverage and unresolved weight/node/norm translations stay explicit; these reservations confer no novelty clearance. The previously next free LIT-061 is consumed openly by this response, not silently skipped. No PD-T, PD-N or IDEA is added by the response.

## Members and integration responsibilities

| Order | Member | State and required next action |
|---|---|---|
| 1 — complete | `codex/charter-unisolvence-20261031`, [PR #2](https://github.com/aacchhee/padua_research/pull/2) | AC merged the charter and first registry block. Historical audited branch is retained; later topics preserve its accepted IDs and scientific files. |
| 2 — next | `codex/mz-constants-20261031`, [PR #3](https://github.com/aacchhee/padua_research/pull/3) | Charter main merged with additive registry reconciliation. Answer audit-01 and request focused re-audit of the changed corollary, literature and metadata; update the rehearsal against current main before readiness. |
| 3–4 — AC decides | `claude/programme-ideas-20261031` | Adopt these exact ledger bytes. Merge charter/MZ-bearing main before final allocation and PR preparation. Its proposed Fable rule amendment remains on its own branch for its own audit; it is not imported by this reconciliation. |
| 3–4 — AC decides | `claude/bivariate-lanczos-20261031` | Adopt these exact ledger bytes. Merge charter/MZ-bearing main, then reconcile final reservations with this owner and rehearse integration before readiness. |

Only the ledger is propagated to the two active Claude member branches; their proofs, source records, rules and other working files remain untouched. The already merged charter branch needs no retroactive rewrite. Until MZ merges, main retains the charter's earlier reconciled ledger, and this updated version is the proposed successor on the next-priority PR.

## Readiness and history

Before requesting any later merge, refresh main and all active heads, verify ledger identity and reservations, and rehearse the relevant sequential squash integration in a disposable local branch. Preserve registry instructions, actual dependencies, dispositions and reciprocal split links. A passed local rehearsal does not authorize a main mutation or a PR merge; only AC merges.

The initial programme ledger, MZ overlay and charter response remain inspectable at their pinned source commits. This response replaces the split-owner/add-add ambiguity with one named owner, one reservation table and AC's explicit priority. The MZ response receipt records the actual propagation and semantic checks; no unexecuted propagation is counted as completed.

## Lattice provisional reservations at AUDIT preparation

AC explicitly requested provisional theory IDs; no new final global range is reserved. The named MZ allocation owner remains responsible for coordinated final allocation before readiness. These topic-scoped IDs cannot collide with another topic’s provisional namespace. Exact map: [provisional-id-map.json](../lattice-unisolvence-20261031/provisional-id-map.json).

| Namespace | Reserved provisional identifiers | Owner / status |
|---|---|---|
| PD-T | PD-T?lattice-c0-codex-01; PD-T?lattice-c0-codex-02; PD-T?lattice-c0-codex-03; PD-T?lattice-c1-codex-01; PD-T?lattice-c1-codex-02; PD-T?lattice-c1-codex-03; PD-T?lattice-c1-codex-04; PD-T?lattice-c1-codex-05; PD-T?lattice-c1-codex-06; PD-T?lattice-c3-codex-01; PD-T?lattice-c3-codex-02; PD-T?lattice-c3-codex-03; PD-T?lattice-c3-codex-04; PD-T?lattice-c3-codex-05 | lattice root; AUDIT, final allocation deferred |
| PD-N | PD-N?lattice-c0-codex-01; PD-N?lattice-c1-codex-01; PD-N?lattice-c1-codex-02; PD-N?lattice-c3-codex-01; PD-N?lattice-c3-codex-02; PD-N?lattice-c3-codex-03; PD-N?lattice-c3-codex-04 | lattice root; AUDIT, final allocation deferred |
| IDEA | IDEA?lattice-c0-codex-01; IDEA?lattice-c0-codex-02; IDEA?lattice-c0-codex-03; IDEA?lattice-c0-codex-04; IDEA?lattice-c0-codex-05; IDEA?lattice-c1-codex-01; IDEA?lattice-c1-codex-02; IDEA?lattice-c1-codex-03; IDEA?lattice-c3-codex-01; IDEA?lattice-c3-codex-02; IDEA?lattice-c3-codex-03; IDEA?lattice-c3-codex-04; IDEA?lattice-c3-codex-05 | lattice root; AUDIT, final allocation deferred |
| LIT | LIT?lattice-codex-01; LIT?lattice-codex-02; LIT?lattice-codex-03; LIT?lattice-codex-04; LIT?lattice-codex-05; LIT?lattice-codex-06; LIT?lattice-codex-07; LIT?lattice-codex-08; LIT?lattice-codex-09; LIT?lattice-codex-10; LIT?lattice-codex-11; LIT?lattice-codex-12; LIT?lattice-codex-13; LIT?lattice-codex-14; LIT?lattice-codex-15; LIT?lattice-codex-16; LIT?lattice-codex-17; LIT?lattice-codex-18; LIT?lattice-codex-19; LIT?lattice-codex-20; LIT?lattice-codex-21; LIT?lattice-codex-22; LIT?lattice-codex-23; LIT?lattice-codex-24; LIT?lattice-codex-25; LIT?lattice-codex-26; LIT?lattice-codex-27; LIT?lattice-codex-28; LIT?lattice-codex-29; LIT?lattice-codex-30; LIT?lattice-codex-31; LIT?lattice-codex-32 | lattice root; AUDIT, final allocation deferred |

Charter→lattice direct squash rehearsal and the wider batch conflict observation are recorded in [integration-rehearsal.md](../lattice-unisolvence-20261031/integration-rehearsal.md). No whole-batch merge readiness or external acknowledgement is inferred. Parent response317a265 adoption is preserved above. Only AC merges; lattice follows charter PR#2.

Historical lattice ledger/source observations: [pinned topic ledger](https://github.com/aacchhee/padua_research/blob/3f369611f364c8bab41b8a48f1414f88b21937ec/topics/padua-batch-20261031/ALLOCATIONS.md). All provisional reservations above are retained; the canonical main ownership and final reservations above take precedence over older snapshots.
