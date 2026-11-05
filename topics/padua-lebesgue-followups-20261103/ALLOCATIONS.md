# Permanent reservation — Padua Lebesgue follow-ups

Owner: `codex/padua-lebesgue-followups-20261103`, 2026-11-03.
No final assignments yet. The first pushed commit containing this file establishes
priority; the draft PR links that commit. Unused IDs remain permanent gaps.

| Namespace | Permanent range | Count |
|---|---|---:|
| PD-T | 266–285 | 20 |
| PD-N | 092–099 | 8 |
| IDEA | 356–375 | 20 |
| LIT | 474–481 | 8 |

## Fresh union scan

- Main: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`.
- This topic input: `3f5196cf3639407c25b021fa30f70cc1d3ae113a`.
- Only other open PR: [#19](https://github.com/aacchhee/padua_research/pull/19),
  `codex/padua-argmax-effective-20261103`,
  `ed8db2fc364d0ba34c3c06815460b3b2971787b5`.
- All eighteen earlier PRs are merged; no closed-unmerged PR exists in the
  live all-state list queried by the orchestrator. Main retains inherited
  reservations and permanent gaps, including T236–245 and LIT460–465.
- Read ledger copies and final IDs in PROOF_STATUS, IDEAS, literature INDEX and
  ID_CROSSWALK on main and PR19. Maximum used/reserved IDs are respectively
  T265, N091, IDEA355 and LIT473. Foreign-project LIT aliases are not Padua IDs.
- Compact [scan receipt](allocation-scan.json) records exact pins, paths,
  hashes and parsing qualifications. Mechanical worker: gpt-6.1-sol medium;
  live PR population queried by the orchestrator.

This topic records its reservation here within handoff 01's write scope. The
existing batch ledger remains unchanged during WORK; propose an additive link
there and in ID_CROSSWALK during preparation. Future allocation scans must read
this file through this topic's open PR as required by WORKFLOW. Recheck every
open branch before assignments or readiness; never reuse or renumber a range.

## 2026-11-05 final assignments — existing reservation

The initial "no final assignments" stage above is superseded by this dated entry.
First publication remains `514e3763a827c106c5170eecd55d849b39265da2` / [PR20](https://github.com/aacchhee/padua_research/pull/20).
The [fresh complete union recheck](preparation/reservation-recheck.md) passes
at main `5db1e01dcd2258f45de2adcaef43859e59734618` and all open PR20–24.
All closed PRs returned by the live search are merged; retired and unused
reservations remain included. This imports no new range and changes no priority.

Assigned PD-T266–271 (six) and IDEA-356–358 (three), with every provisional
alias retained in the [exact map](preparation/final-id-map.json).
Existing PD-T180/184, IDEA-299 and LIT-388 are reused without renumbering.
No new PD-N or LIT entry. Permanent unused gaps: PD-T272–285, PD-N092–099,
IDEA359–375 and LIT474–481. All other owners' full ranges remain unavailable.
[Shared batch ledger](../padua-batch-20261031/ALLOCATIONS.md) imports this
reservation unchanged. Readiness requires a final head/population refresh.
