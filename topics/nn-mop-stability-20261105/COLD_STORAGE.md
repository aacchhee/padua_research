# Working artifacts and pending cold storage

No file has been delivered to external cold storage. No Padua cold-storage location is mounted in this cloud task. The actual local files in `cold-storage.json` are working artifacts, with byte counts and SHA-256 digests; that inventory explicitly has `delivered: false`. It is not a `tools/cold_storage.py` export receipt or an assertion that files survive this task environment.

## Committed evidence

The repository contains code, the hand-checkable dyadic witness, compact direction receipts, the complete61-size table, proof records, and independent checker reports. `evidence-manifest.json` pins code/proof/checker content. Written analytic proofs do not depend on the large floating logs. The finite normality reduction and exact checker can regenerate their small essential summary; the independent run is recorded separately. Large raw outputs are not promoted into proof premises without a named reduction/checker.

## Regeneration and verification

Run the frozen commands in `attempts/D1.md` through `attempts/D7.md`, `attempts/D1-hard.md`, `plot-receipt.md`, and `independent-checks-01.md` / `independent-checks-02.md`. They give code hashes, inputs, actual environments, precisions, scope and observations. Timing, platform and run-path fields can change raw byte hashes on a rerun; compare numerical payloads and content/input identities as the receipts specify. A matching hash identifies bytes, not mathematical correctness.

`code/evidence_receipts.py` collects local identities without copying data into Git. Its working-artifact JSON is deliberately labelled as pending and is not the historical-Git-blob schema consumed by `tools/cold_storage.py`. The latter was inspected at the pinned source and its help executed; export/restore were not run without a retrievable archive/source-blob arrangement. Do not count an empty archive verification as delivery.

## Retention and retrieval

Keep the local working files through the Claude audit while this environment exists. External archival/retention remains pending rather than being invented on an unrelated machine. AC's established Padua-specific cold-storage destination can be used when accessible, with a proper delivery manifest and `verify-archive` result; no such delivery is claimed here. All large outputs are regenerable from committed code, and no new remote compute or message to another person was used.
