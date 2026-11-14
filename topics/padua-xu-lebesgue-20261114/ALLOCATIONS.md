# Allocation ledger — padua-xu-lebesgue-20261114

Owner: `claude/padua-xu-lebesgue-20261114`, [PR36](https://github.com/aacchhee/padua_research/pull/36). This topic has no separate integration batch. Authority is the fresh-range procedure in agents/WORKFLOW.md (rules read at `8fdd0392bf53e076b0ebef7ca4eec1a2549e7076`). Earlier foreign ownership, reservations, retired ranges and permanent gaps remain unchanged. No accepted ID is renumbered.

## Reservation — 2026-11-14

| Namespace | Reserved range | Count | Owner |
|---|---|---:|---|
| PD-T | PD-T690–719 | 30 | claude/padua-xu-lebesgue-20261114 |
| PD-N | PD-N251–257 | 7 | claude/padua-xu-lebesgue-20261114 |
| IDEA | IDEA-766–795 | 30 | claude/padua-xu-lebesgue-20261114 |
| LIT | LIT-721–745 | 25 | claude/padua-xu-lebesgue-20261114 |

The ranges include headroom over the provisional inventory: 20 PD-T, 3 PD-N, about 15 IDEA and about 12 LIT (handoff 03). Every unused ID remains a permanent gap. No range is shifted, reused or enlarged retrospectively.

The reservation's priority is the pushed commit that first adds this ledger. Locate it with `git log --diff-filter=A --format=%H -- topics/padua-xu-lebesgue-20261114/ALLOCATIONS.md`; it is also linked from the PR body.

## Fresh union check (at reservation)

| Scope | Checked head |
|---|---|
| main | `99a9b1d161e41a80c4fd425b63022c681fbe8779` |
| PR36, this topic before reservation | `8fdd0392bf53e076b0ebef7ca4eec1a2549e7076` |
| PR27 (open draft), `codex/padua-argmax-bridge-20261105` | `fd82e593cd73019601fb00dea9844db09f8601c0` |
| PR35 (open), `claude/padua-mz-paper-20261113` | `a045b8e9b2b4d92813a9b8e2832b2f8254e7397e` |

**PR population.** I read the GitHub all-PR collection (state all, 35 records) on 2026-11-14:
- open: PR27, PR35 and PR36;
- every closed PR is merged, so no closed-unmerged reservation needs reconstruction.

**Sources read at each head.**
- Every `topics/*/ALLOCATIONS.md` ledger: 17 on main, 18 on PR27 and PR35.
- The four canonical registries: `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md` and `ID_CROSSWALK.md`.
- The scan is a per-namespace regex maximum, including the upper ends of written ranges.

**Results.**
- **main:** T683/N250/IDEA765/LIT720 (PR34's reservation T674–683/N246–250/IDEA756–765/LIT716–720).
- **PR35:** its ledger `topics/padua-mz-paper-20261113/ALLOCATIONS.md` reserves PD-T684–689 and nothing in the other namespaces.
- **PR27:** its ledger lies below main's maxima.
- **Union:** T689/N250/IDEA765/LIT720. The new ranges start strictly above it.

**Foreign or non-ID strings excluded, with context checked against PR34's ledger notes:** `PD-T999` (test fixture), `PD-N303/N304` (prose only), and four-digit `LIT-1658…1750` (bttb-research aliases). None of these overlaps the new ranges.

No collision and no unknown retired reservation was found. The check is repeated at readiness, and again if main or another open PR's ledger changes before AC merges. Only AC merges.
