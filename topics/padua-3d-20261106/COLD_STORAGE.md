# Working outputs and cold-storage boundary

No payload has been delivered to AC's cold storage in this session.
The compatible [ledger](cold-storage.json) consequently has zero archived
entries. Its separate `pending_local_working_outputs` inventory records
three **actually generated** T2 raw catalogues, their SHA-256, byte sizes,
generator Git blob/source commit, frozen regeneration command and summary.
These are local working outputs, not cold-storage locators or delivery receipts.

## Retained essential evidence

The cubic 171-case null cover is 8,054 bytes and is committed at
`evidence/t2-n3-null-cover.json`, with a complete standalone exact checker
`code/t2_check_cover.py`. It does not read a raw catalogue. All remaining
claimed computer evidence also has committed small receipts and code.
Hand-proved theorems have no raw-computation premise. No required proof
artifact depends on AC's computer or on the temporary files below.

## Regeneration and retrieval

From the repository root with Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0
and SymPy 1.14.0:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t2_generators.py
python topics/padua-3d-20261106/code/t2_check_cover.py
```

The first command regenerates n=2,3,4 catalogues under
`/tmp/padua-3d-20261106/`, deterministically. Compare them against the
SHA-256/bytes in the ledger or the compact generator receipt; these
identities were checked against the actual working files during integration.
The second checks the proof-essential committed cubic cover without those
catalogues. Script/input hashes and independent runs live in the evidence
manifest and independent-check records.

The current `tools/cold_storage.py` format restores previously pushed Git
blobs; these new scratch catalogues were deliberately never committed.
They are therefore not presented as tool-restorable archive entries.
`plan topics/padua-3d-20261106 --threshold 16384` reported zero tracked
oversize payloads at the development checkpoint. No export or delivery
operation was claimed.

## Retention

Keep code, small summaries and essential certificates in Git. Raw scratch
may disappear with the cloud session and is regenerated on demand; no
archival delivery is required for the stated results. If AC later requests
retention of these optional raw catalogues, use AC's established Padua
destination `Downloads\\padua\\cold_storage\\padua-3d-20261106\\`, record
actual delivered identities, and verify the archive before treating it as
retrievable. This is not a request for archival work now.

## Audit-01 m13 inventory correction — 2026-11-06

The ledger now also lists the optional T4 arrays
`/tmp/padua-3d-20261106/t4-{M,A,L}-n{1..7}-nodes.npy` and their regenerated
`t4-node-artifacts.json`. Reproduce them with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t4_stacks.py --max-degree 12`.
The registered quality stop occurs at n7, so that command creates no n>=8
family rows. Their current generating source SHA-256 is recorded. These
files were not observed or regenerated in this continuation, so no new
array bytes/hashes or archival delivery are claimed. D0 fixtures remain
restorable from the pinned Git source identities in evidence/replay.json.

## T8 continuation outputs — 2026-11-06

The ledger additionally records eight actually observed U/O/E raw JSONL
catalogues by exact byte size, SHA-256, generating code blob/hash, command
and compact summary. These are regeneration-only working outputs, with
no cold-storage delivery or raw-data premise for the analytic theorems.
The independently executed checks keep their own outputs in separate tmp
directories; their compact receipts and code are retained in the repository.
The final code/data manifest also pins the two inherited lattice-quality
helpers used by the numerical comparisons, along with all local scripts.
