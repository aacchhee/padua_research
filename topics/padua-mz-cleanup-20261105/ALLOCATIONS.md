# Permanent reservation — MZ cleanup

Owner: `codex/padua-mz-cleanup-20261105`, 2026-11-05.
Reservation only; no final assignments during WORK.

| Namespace | Range | Count |
|---|---|---:|
| PD-T | PD-T376–PD-T391 | 16 |
| PD-N | PD-N138–PD-N145 | 8 |
| IDEA | IDEA-466–IDEA-489 | 24 |
| LIT | no range | 0 |

The full [union scan](allocation-scan.json) inspected all complete ledgers
and canonical registries at pinned main, PR21/22/24 and the parallel
argmax phase-2 branch, including permanent unused and retired ranges.
An immediate recheck found argmax phase 2 advanced from 2fb2f75 to
ce17564ea1c185fea0be109b8ebb38efe25bceec and had reserved
T364–375/N132–137/IDEA454–465/LIT594–597. Its new ledger and four
unchanged registries were read before this reservation. Therefore the
live union maxima are T375/N137/IDEA465/LIT597. Every new range above
starts strictly above its namespace maximum. No literature range needed.

First publication: [`ee490356ce51d5e2f4a84f2c45e6ccb98a19bd90`](https://github.com/aacchhee/padua_research/commit/ee490356ce51d5e2f4a84f2c45e6ccb98a19bd90), linked from [draft PR26](https://github.com/aacchhee/padua_research/pull/26).
That first pushed commit containing this ledger establishes priority.
Unused IDs remain permanent gaps.
No accepted or reserved identifier is renumbered. Shared batch/crosswalk
updates wait for audited PR preparation under handoff01's write scope.
The fresh-range procedure supersedes historical single-owner prose;
existing reservations remain binding. Recheck again before assigning IDs
or declaring readiness.

## Audited preparation assignments — 2026-11-05

The [fresh full-file union](preparation/reservation-check.md) reads main and
all open PR21/24/25/26 at their pinned heads; no closed-unmerged reservation
is missing. Union maxima including this reservation: T391/N145/IDEA489/LIT597.
Foreign union excluding this topic: T375/N137/IDEA465/LIT597. No range conflict.
This is assignment from the original block, not re-reservation.

Assigned PD-T376–381 (six: four PROVED, one MEASURED, one OPEN) and
IDEA466–471 (six: four active PROVED outcomes, one deferred, one abandoned).
No PD-N or LIT assigned. Permanent unused gaps: T382–391, N138–145,
IDEA472–489. [Exact alias map](preparation/final-id-map.json).
Original priority remains ee490356ce51d5e2f4a84f2c45e6ccb98a19bd90.
All old ledger prose above is preserved as dated reservation provenance.
