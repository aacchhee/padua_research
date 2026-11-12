# Allocation ledger — padua-3d-20261106

Owner: `codex/padua-3d-20261106`, [PR33](https://github.com/aacchhee/padua_research/pull/33). This topic has no separate integration batch. Authority is the fresh-range procedure in agents/WORKFLOW.md; earlier foreign ownership, reservations, retired ranges and permanent gaps remain unchanged. No accepted ID is renumbered.

## Reservation — 2026-11-12

| Namespace | Reserved range | Count | Owner |
|---|---|---:|---|
| PD-T | PD-T554–673 |120|codex/padua-3d-20261106|
| PD-N | PD-N186–245 |60|codex/padua-3d-20261106|
| IDEA | IDEA-616–755 |140|codex/padua-3d-20261106|
| LIT | LIT-636–715 |80|codex/padua-3d-20261106|

These ranges include headroom. Every unused ID remains a permanent gap; no range is shifted, reused or enlarged retrospectively. Final assignments and unused gaps are listed below after mechanical application. The reservation’s priority is the pushed commit that first adds this ledger; locate it by `git log --diff-filter=A --format=%H -- topics/padua-3d-20261106/ALLOCATIONS.md` and the PR body.

## Full fresh union check

| Scope | Checked head |
|---|---|
| main | `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb` |
| PR33, this topic before reservation | `c8691c5d4afcbb17506cb052ea48313c865eff35` |
| PR27, other open draft/PR | `8a94ce610594e9f52a23ca6b74b5751719f0d89e` |

Root fetched all three heads and read the GitHub all-PR collection twice, confirming the same32 records: open27/33,30closed and merged, none closed-unmerged. No closed-unmerged reservation needs reconstruction. [API population snapshot](pr-preparation/pr-snapshot.json).

The independent Sol-medium scan read58 complete ledger/registry copies, including46 ledger copies,16 unique ledger blobs and all four canonical ID registries at every checked head. It retains all historical/retired reservations and unused gaps. Permanent maxima before this reservation: **PD-T553, PD-N185, IDEA615, LIT635**; highest assigned row IDs: T548/N183/IDEA611/LIT633. The new starts are strictly above those reserved maxima. Eight four-digit bttb-research literature aliases are foreign references, not assigned Padua IDs; each was checked in context and earlier ledgers explicitly preserve that distinction.

[Full scan](pr-preparation/reservation-check.md) and [source-copy identities](pr-preparation/reservation-check.json) preserve every path/head/Git-blob identity and the exclusion rationale. No collision or unknown retired reservation was found. PR27’s T392–431/N146–161/IDEA490–529/LIT598–613 reservation remains unchanged.

Repeat the fresh check at readiness and if main or another open PR’s ledger changes before AC merges. Only AC merges; this ledger grants no research-round extension or scientific status change.
