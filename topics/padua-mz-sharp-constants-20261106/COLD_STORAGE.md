# Optional raw provenance — not retained

Audit A11 disposition, 2026-11-06: no optional raw receipt is claimed retained as authoritative evidence,
staged or delivered to archival storage. The historical hashes, sizes,
commands and original producer paths remain in cold-storage.json as provenance
only. They are not retrieval locators or a padua-cold-storage-v1 archive.
The tool format is for actual archived Git blobs; inventing entries for
unretained timing-bearing /tmp output would misstate storage.

## Committed checker output

The essential CC and Padua rows are evidence/S4-essential-cc.json and
evidence/S4-padua-essential.json. Their repository-only fit replays and
independent checks are recorded in attempts/S4-essential-replay.md and
audit-01.md. No result depends on optional raw retrieval.

## Regeneration and handoff

Producer/checker commands and hashes remain in cold-storage.json. Numerical
rows regenerate using the committed code and essential records; timing-bearing
raw byte identity is not promised on regeneration. No delivery receipt exists.

## Retention and retrieval

No custodian, archive destination or retention promise has been established.
The two original working files currently survive in this environment; they
are not archived or delivered and do not provide guaranteed cross-session
retrieval. No authoritative raw-retention promise is made.
Future archival requires an AC-designated Padua location and actual delivery
before a tool-format archive manifest can truthfully be written.

Format source inspected: templates/COLD_STORAGE.md and tools/cold_storage.py
at 0205690b9c4e959a28e949083e9a1808735abf4b via pinned GitHub connector.
The audit explicitly permits declaring optional raw not retained instead of
converting fictitious storage entries.
