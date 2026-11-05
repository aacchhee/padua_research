# Cold-storage manifest — Lanczos frontier round 2

No external delivery is claimed. [cold-storage.json](cold-storage.json) inventories only actual local G0 outputs by absolute path, SHA-256 and byte size. [Independent report](independent-checks-g0.md) gives frozen commands, source SHA, package pins, restored historical Git blobs and verification outcomes; [short receipt](evidence/g0-summary.json) and [kernel receipt](evidence/g0-kernel-probes.json) are committed. Third-party code, HTML and raw outputs stay outside Git. L7 source-access hashes are separately in [its preparation receipt](evidence/l7-preparation.json); those are retrieval metadata, not scientific evidence.

## Regeneration and checks

Run code/g0_replay.py with the report's pinned dependencies and unchanged polyrat checkout. It exports the frozen source commit, restores four historical blobs with SHA/size checks, checks upstream/local source pins and runs five replay commands. Optional diagnostics repeat E6 and vary BLAS kernels. Current controlled E6 values recur on this runtime; kernel sensitivity and missing historical dispatch constrain interpretation. Programmatic inequality/identity outcomes are separate from the checker's dated G0 stop disposition. Raw timestamps, output paths and run durations are not promised to regenerate byte for byte.

## Retention and retrieval

Actual local path is /tmp/padua-lanczos-frontier-g0; sandbox retention is not guaranteed. Desired Windows destination from handoff01 is Downloads/padua/cold_storage/padua-lanczos-frontier-20261105/, but no access or transfer took place. AC remains archive custodian; physical delivery is pending. If local files survive, hash and size must match the JSON before use. Otherwise regenerate from committed code and pinned Git history; do not claim to have recovered original timed receipts. These outputs support replay diagnosis, not a new computer-assisted theorem.
