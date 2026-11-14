# Allocation ledger — padua-effective-cubature-20261112

Owner: `claude/padua-effective-cubature-20261112`, [PR34](https://github.com/aacchhee/padua_research/pull/34). This topic has no separate integration batch. Authority is the fresh-range procedure in agents/WORKFLOW.md (rules read at `40179a5bae9a0619e7615c877f7afc246452d5c8`). Earlier foreign ownership, reservations, retired ranges and permanent gaps remain unchanged, and no accepted ID is renumbered.

## Reservation — 2026-11-14

| Namespace | Reserved range | Count | Owner |
|---|---|---:|---|
| PD-T | PD-T674–683 | 10 | claude/padua-effective-cubature-20261112 |
| PD-N | PD-N246–250 | 5 | claude/padua-effective-cubature-20261112 |
| IDEA | IDEA-756–765 | 10 | claude/padua-effective-cubature-20261112 |
| LIT | LIT-716–720 | 5 | claude/padua-effective-cubature-20261112 |

The ranges include headroom over the provisional inventory: 6 PD-T, 1 PD-N, 7 IDEA and 2 LIT, verified by a grep of every provisional ID in the topic. Every unused ID remains a permanent gap. No range is shifted, reused or enlarged retrospectively.

The reservation's priority is the pushed commit that first adds this ledger. Locate it with `git log --diff-filter=A --format=%H -- topics/padua-effective-cubature-20261112/ALLOCATIONS.md`; it is also linked from the PR body.

## Fresh union check (at reservation)

| Scope | Checked head |
|---|---|
| main | `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3` |
| PR34, this topic before reservation | `40179a5bae9a0619e7615c877f7afc246452d5c8` |
| PR27 (open draft), `codex/padua-argmax-bridge-20261105` | `f4e8d8d313b1fec0cd4976de98524552fbdc94dd` |
| PR35 (open draft), `claude/padua-mz-paper-20261113` | `a0206a801e1d032175405db6ac7505e0691559fc` |

**PR population.** I read the GitHub all-PR collection (state all, 34 records) on 2026-11-14:
- open: PR27, PR34 and PR35;
- every closed PR is merged, so no closed-unmerged reservation needs reconstruction.

**Sources read at each head.**
- Every `topics/*/ALLOCATIONS.md` ledger: 16 on main and PR35, 17 on PR27, the extra one being PR27's own ledger.
- All four canonical registries: `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md` and `ID_CROSSWALK.md`.
- PR35 adds no ledger and changes none of the four registries relative to main.

**Results.**
- **Reserved maxima.** The highest reservation is PR33's, recorded on main in `topics/padua-3d-20261106/ALLOCATIONS.md` as PD-T554–673, PD-N186–245, IDEA-616–755 and LIT-636–715. Its readiness refresh states the union T673/N245/IDEA755/LIT715.
- **PR27.** Its ledger (T392–431/N146–161/IDEA490–529/LIT598–613) lies below that.
- **Highest assigned registry IDs.** PROOF_STATUS T643/N225; IDEAS IDEA-723; crosswalk T644/N226/IDEA723/LIT673; INDEX below 716 apart from the foreign references noted below.
- **New ranges.** They start strictly above the union maxima T673/N245/IDEA755/LIT715.

**Foreign or non-ID strings excluded, with context checked:**
- `PD-T999` is a test-fixture string in `topics/bivariate-lanczos-20261031/audit-05/check_integration_independent.py`.
- `PD-N303/N304` occurs only in the prose of `topics/padua-literature-20261103/audit-support/p3.md` L15 and has no registry row.
- Four-digit `LIT-1658…1750` are bttb-research record aliases, as earlier ledgers record.

None of these overlaps the new ranges.

No collision and no unknown retired reservation was found. The check is repeated at readiness, and again if main or another open PR's ledger changes before AC merges. Only AC merges.

## Final assignments and permanent gaps (2026-11-14)

| Namespace | Assigned | Count | Permanent unused headroom | Gap count |
|---|---|---:|---|---:|
| PD-T | PD-T674–679 | 6 | PD-T680–683 | 4 |
| PD-N | PD-N246 | 1 | PD-N247–250 | 4 |
| IDEA | IDEA-756–762 | 7 | IDEA-763–765 | 3 |
| LIT | LIT-716–717 | 2 | LIT-718–720 | 3 |

The exact map is `pr-preparation/final-id-map.json`, and the global crosswalk section is "Effective positive-cube cubature excess and Padua Lebesgue corollary — PR34" in `ID_CROSSWALK.md`. Assignments were made only after the reservation commit `de39dabc7301b0de1463aaf2dab99365c4d7789e` was pushed and linked from the PR body.

## Readiness refresh — 2026-11-14

[Readiness 01](readiness-01.md) and its independent reservation report confirm the same uncontested reservation and assignments. Heads checked: main `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`; PR27 initially `b918c1d5bedba60e8255d7d2b985dd6c70f4690a`, then `4ed88e9b811180fa9f88fd629b4f93027c7bfe95` with identical ledger/ID-registry blobs; PR34 preparation `b4e00bdaf2ea391489523c28a7f25f0f4fc24c49` plus the two reviewed MINOR summary/map fixes; PR35 `be28d3267bf6117878190b10f2d29840e524eac7`.

All 34 PRs were enumerated: open 27/34/35, 31 closed all merged, no closed-unmerged reservation. The full scan read 66 ledger copies and 16 canonical registry copies. Foreign maxima remain T673/N245/IDEA755/LIT715; including this reservation the union is T683/N250/IDEA765/LIT720. No collision or unknown retired range was found. Ranges, publication priority and permanent gaps are unchanged. Repeat the refresh if main or another open PR's allocation/identifier sources change before AC merges.
