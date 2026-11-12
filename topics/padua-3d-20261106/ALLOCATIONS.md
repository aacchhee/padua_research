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

## Final assignments and permanent gaps

| Namespace | Assigned | Assigned count | Permanent unused headroom | Gap count |
|---|---|---:|---|---:|
|PD-T|PD-T554–643|90|PD-T644–673|30|
|PD-N|PD-N186–225|40|PD-N226–245|20|
|IDEA|IDEA-616–723|108|IDEA-724–755|32|
|LIT|LIT-636–673|38|LIT-674–715|42|

Six additional literature groups reuse existing accepted facts, with all local aliases retained. Nine previously unnumbered but already retained source records receive identities directly; no retrospective provisional ID is invented. [Exact map](pr-preparation/final-id-map.json) and the global crosswalk give every canonical/alias/source identity. All status, disposition, scope and source-coverage wording follows the accepted canonical records.

First published reservation commit: [`512f63b02ce9b7436092729f53efcc883860a10a`](https://github.com/aacchhee/padua_research/commit/512f63b02ce9b7436092729f53efcc883860a10a), linked in PR33 before assignment.

## Readiness refresh — 2026-11-12

The [final readiness check](pr-preparation/readiness.md) refreshed main f70a260e5b5f9a01209dc8a05faabdcf8db1feeb, own application050f882026ef9df729b7b78c3bc18bf4cf6c2b7e and peer PR27 head8a94ce610594e9f52a23ca6b74b5751719f0d89e against the32-PR population. Complete reads covered59 copies,47 ledger copies,17 distinct ledger blobs and25 distinct blobs overall. Foreign maxima remain T553/N185/IDEA615/LIT635; the union including this reservation is T673/N245/IDEA755/LIT715. No collision or unrecorded closed-unmerged reservation was found. All assignments and permanent gaps above remain unchanged.
