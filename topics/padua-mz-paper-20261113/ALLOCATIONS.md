# Allocation ledger — padua-mz-paper-20261113

Owner: `claude/padua-mz-paper-20261113`, [PR35](https://github.com/aacchhee/padua_research/pull/35). This topic has no separate integration batch. Authority is the fresh-range procedure in agents/WORKFLOW.md (rules read at `c0e57a9`, unchanged on the branch). Earlier foreign ownership, reservations, retired ranges and permanent gaps remain unchanged, and no accepted ID is renumbered.

## Reservation — 2026-11-14

| Namespace | Reserved range | Count | Owner |
|---|---|---:|---|
| PD-T | PD-T684–689 | 6 | claude/padua-mz-paper-20261113 |

No PD-N, IDEA or LIT range is reserved.

**Provisional inventory.** The range has headroom over the 2 provisional PD-T claims. These were found by a grep of every provisional ID in this topic, both paper directories, the M7 manuscript record and the results file:
- `PD-T?mz-paper-claude-01` (CC endpoint defect, condition number and five-thirds factor);
- `PD-T?mz-paper-claude-02` (analytic lower bounds for the corner-operator extrema).

No provisional PD-N, IDEA or LIT ID exists in this topic. The other provisional strings that occur here are the historical `PD-T?mz2d-codex-*` and `PD-N?mz2d-codex-*` aliases quoted from earlier records, and those already have final IDs. The canonical LIT-045 and LIT-056 addenda extend existing records and need no new ID.

Every unused ID remains a permanent gap. No range is shifted, reused or enlarged retrospectively.

The reservation's priority is the pushed commit that first adds this ledger. Locate it with `git log --diff-filter=A --format=%H -- topics/padua-mz-paper-20261113/ALLOCATIONS.md`; it is also linked from the PR body.

## Fresh union check (at reservation)

| Scope | Checked head |
|---|---|
| main | `99a9b1d161e41a80c4fd425b63022c681fbe8779` |
| PR35, this topic before reservation (main merged in) | `fa956deae97f463010d8bd62b6143b08352a84e6` |
| PR27 (open draft), `codex/padua-argmax-bridge-20261105` | `656c15b758c3cf49782adb3af8b1bced361179e6` |

**PR population.** I read the GitHub all-PR collection (REST, state all, 34 records) on 2026-11-14:
- open: PR27 and PR35;
- every closed PR is merged, so no closed-unmerged reservation needs reconstruction.

**Sources read at each head.**
- Every `topics/*/ALLOCATIONS.md` ledger: 17 at each of the three heads.
- All four canonical registries: `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md` and `ID_CROSSWALK.md`.
- Before this ledger, PR35 changes no ledger and none of the four registries relative to main. The merge of main `99a9b1d` was clean.

**Results.**
- **Reserved maxima.** The highest reservation is PR34's, recorded on main in `topics/padua-effective-cubature-20261112/ALLOCATIONS.md` as PD-T674–683, with assigned PD-T674–679 and permanent gap PD-T680–683. Its readiness refresh states the union T683/N250/IDEA765/LIT720.
- **PR27.** Its ledger (T392–431/N146–161/IDEA490–529/LIT598–613) lies below that.
- **Highest PD-T in the registries on main.**
  - PROOF_STATUS, IDEAS and INDEX: T679.
  - ID_CROSSWALK: T680, which comes only from the gap range PD-T680–683.

  At PR27 the highest are PROOF_STATUS T643 and ID_CROSSWALK T644.
- **New range.** It starts strictly above the union maximum T683.

**Foreign or non-ID strings excluded, with context checked:** `PD-T999` is the test-fixture string in `topics/bivariate-lanczos-20261031/audit-05/check_integration_independent.py`, already documented in the PR34 ledger. None of these overlaps the new range.

No collision and no unknown retired reservation was found. The check is repeated at readiness, and again if main or another open PR's ledger changes before AC merges. Only AC merges.
