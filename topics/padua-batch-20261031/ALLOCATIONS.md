# Shared allocation ledger — padua-batch-20261031

This is the single authoritative batch ledger. **Allocation owner: the root Codex MZ orchestrator.** AC explicitly confirmed the integration order for shared registries: charter first, MZ second. PR #2 was merged by AC into main at `08fafe62d9798385dfafaacc9a41344272737e68`; PR #3 was merged by AC into main at `07c5f5465d6de306aa81dbe8ca1f615295163864`; the charter/MZ integration sequence is complete. Programme-ideas and bivariate-Lanczos follow in AC's chosen order and must obtain a disjoint reservation from this owner before assigning final IDs. The previous programme rule that the next branch reaching PR preparation becomes owner is superseded. No parallel allocation or accepted-ID renumbering is authorized.

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
| 2 — complete | `codex/mz-constants-20261031`, [PR #3](https://github.com/aacchhee/padua_research/pull/3) | AC merged the accepted MZ package after audit-02 and the clean main rehearsal. The merged tree exactly matches ready head `8ee04f4e5db46dd25fe5752ce605dde27098aae6`. See [post-merge frontier](../mz-constants/POST_MERGE.md); no new allocation is made. |
| 3–4 — AC decides | `claude/programme-ideas-20261031` | Adopt these exact ledger bytes. Merge charter/MZ-bearing main before final allocation and PR preparation. Its proposed Fable rule amendment remains on its own branch for its own audit; it is not imported by this reconciliation. |
| 3–4 — AC decides | `claude/bivariate-lanczos-20261031` | Adopt these exact ledger bytes. Merge charter/MZ-bearing main, then reconcile final reservations with this owner and rehearse integration before readiness. |

At the audit-response checkpoint, only the ledger was propagated to the two active Claude member branches; their proofs, source records, rules and other working files remain untouched. The already merged charter branch needs no retroactive rewrite. MZ is now integrated. This administrative follow-up changes only integration-status prose; the owner and reservation table are unchanged. Later member branches must refresh from current main and reconcile this ledger before final allocation; no propagation of this follow-up to those branches is claimed.

## Readiness and history

Before requesting any later merge, refresh main and all active heads, verify ledger identity and reservations, and rehearse the relevant sequential squash integration in a disposable local branch. Preserve registry instructions, actual dependencies, dispositions and reciprocal split links. A passed local rehearsal does not authorize a main mutation or a PR merge; only AC merges.

The initial programme ledger, MZ overlay and charter response remain inspectable at their pinned source commits. This response replaces the split-owner/add-add ambiguity with one named owner, one reservation table and AC's explicit priority. The MZ response receipt records the actual propagation and semantic checks; no unexecuted propagation is counted as completed.

2026-10-31 post-merge receipt: GitHub reports PR #3 merged at 22:20:47 UTC; main `07c5f5465d6de306aa81dbe8ca1f615295163864` has the exact ready-head tree. Completed preparation/re-audit/merge tasks are historical. Reservation blocks and next-free IDs above are preserved.
