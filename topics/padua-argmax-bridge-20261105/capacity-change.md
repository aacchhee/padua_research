# Consolidated evidence-index capacity exception candidate

Technical metadata maintenance at input HEAD
`0174900a19087d728f3f947b52f205e5b76b0a41`; rules unchanged from the prior read.
Requested developer model/effort: Sol medium; serving identity is not exposed.
No scientific claim, evidence identity, research run, or novelty content changes.

The candidate copies the canonical helper, adds `INDEX_LIMIT=32768`, and changes
only its two CLI index-size guards/messages to the strict 32KiB limit. `LIMIT`
remains 16384 for every declared and physical evidence file. V2/V3/V4 schemas,
full SHA256 digests, metadata, compaction, and atomic replacement are unchanged.
This relies on the root's explicit single consolidated-index exception; it does
not grant a broader evidence-file exception or change the aggregate 10MB limit.
Canonical helper and index remain untouched pending distinct Astra review.

Reproduction:
`python topics/padua-argmax-bridge-20261105/code/evidence_index_capacity_checks.py`

PASS: 194 independently decoded rows and all 194 files rehashed; exact candidate
patch and V2/V3/V4 API/metadata equality; eight temporary CLI checks. Checks accept
16385- and 32767-byte valid indexes, reject 32768 and 32769, exercise both compact
actions above 16KiB and reject outputs above 32KiB, reject both declared and
physical 16384-byte evidence, and accept 16383-byte evidence. Actual index stays
16086 bytes. Successful suite used 0.6411 CPU seconds, within the preregistered
2 CPU-second budget. An earlier fixture attempt stopped because fixed padding
made V3 output exceed 32KiB; the fixture now targets 22000 bytes for either schema
(earlier command wall time 0.2986 seconds). No scientific code was imported.

SHA256 identities:

- Canonical input helper: `ca6b511e4eb1282f587407cd8c2d81b542f498fcca401d7daeb075132a57025d`.
- Candidate, 10944 bytes: `d9d4590d59f44cbfc1627a4a0cab0b6bda398f327c0e755eb0c19c48aa063e2f`.
- Checker, 6614 bytes: `30a80befd96e47275436f1be78425e8efe1177e96429713d53505348ed6fdbcd`.
