# Response 03 — technical evidence hygiene

Rules read at `9042e1c42964150f30fdbe8563c12ba6c6a8692a`. Developer: Codex, assigned `gpt-6.1-sol` high; runtime model metadata unexposed. This scope repairs evidence provenance and repeats existing computations; it introduces no mechanism or novelty claim, so a new novelty gate does not apply. No Git operations were performed by this worker.

## Dispositions

| Audit03 returned item | Resolution and evidence |
| --- | --- |
| T10 m2, hard-coded half-shift arrays | The historical arrays in `t10_lattices.py:117` are **derived values**, not eight observed rank computations. [r08-hygiene-halfshifts.json](evidence/r08-hygiene-halfshifts.json) now actually enumerates all eight π-shifted folds for all 83 historical census lattices (664 cases), using denominator 2q even when q is odd. Every count agrees. The shifted ranks follow from the exact node bijection and `T_alpha((-1)^mask x)=(-1)^(alpha dot mask) T_alpha(x)`, so row permutation and invertible column signs preserve rank. This is not a half-grid-step phase experiment. Historical producer and raw arrays stay unchanged. |
| T10 m3, n2..7 certificate/quality-selection linkage | [r08-hygiene-selections.json](evidence/r08-hygiene-selections.json) authenticates the original census and full-precision quality raw by their existing byte/hash identities, repeats the quality producer's exact selection algorithm, and matches its selected-key payload hashes to the old rank receipt at each n2..7. Both 21³/41³ quality mesh values repeat with **zero difference**. Fresh primes 73, 193, 601, 2161, 5881 and 4481 give actual-node monomial ranks 10, 20, 35, 56, 84 and 120. The original quality run did not save selected hashes; this is an executed reconstruction, not a newly invented historical log. |
| T9 m3, complement's non-reproducible prose hash | Removed the theory-file entry from `t9-r06-complement.json` inputs, with a dated correction identifying the original receipt hash and historical commit. Original command, source-code identity, versions, numerical fields and timings remain historical. Removed that prose input from the producer too, then executed it: [new producer receipt](evidence/r08-hygiene-complement-producer.json). [Supplemental replay](evidence/r08-hygiene-complement.json) verifies all n1..109 scientific rows, dense-memory figures and exact fold/rank/node hashes at n17/24/32. The theory text is not an input to this replay. |
| Supplementary checker prose pins | Removed 26 theory entries from `independent-r06-pins.json` and all 13 prose entries from `t9-r06-run-manifest.json`, with dated provenance corrections. Original versions remain in Git at the rules-read commit. Removed prose hash generation from `t9_r06_manifest.py`; [fresh manifest](evidence/r08-hygiene-t9-manifest.json) was executed. [Pin check](evidence/r08-hygiene-pins.json) validates all 31 current code identities and the 18 receipt references in the historical/current manifests. It rejects any prose pin. Historical generator hashes remain execution metadata; the historical complement receipt correctly reports a current source mismatch because its producer was subsequently changed. The current exact source identity is explicitly validated, and the fresh producer replay supplies current execution evidence. |
| Novelty m6, 51-file stream-hash command and wording | [Explicit inventory](evidence/r08-hygiene-raw-inventory.json) supplies all 51 paths, bytes, SHA-256 values and source receipts; [actual check](evidence/r08-hygiene-raw-check.json) records the command and inputs. All **54,836,138 bytes** were read and stream-hashed again. The scope is **26 legacy-T9 raw arrays plus 25 T7/T8 round06 raw paths**. It excludes all five T10 raw identities and T9-r06 records that have node payload hashes only. No missing path was claimed observed. This supersedes the old “round06/T10 receipts” scope wording and the unqualified “input hashes match exactly” wording for the complement; the old prose hash did not match. |

The only old result-bearing source changes are removal of the prose input in `t9_r06_complement.py` and removal of prose hash generation in `t9_r06_manifest.py`. The latter accepts a changed producer only when the receipt's explicit dated correction pins the **current code** hash, and reports `source_code_matches: false` for its historical execution rather than claiming an original match. The mathematical computations in these producers are unchanged. Their relevant commands were actually rerun after the source changes. `t10_lattices.py`, `t10_subset_rank.py` and `independent_r06.py` are unchanged.

## Commands actually executed

Run from repository root, with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` prefixed to each command. The scratch inputs below were present and matched their historical receipts. The new checker is [r08_hygiene.py](code/r08_hygiene.py); its receipts hash code and data only.

```sh
python topics/padua-3d-20261106/code/t9_r06_complement.py --output topics/padua-3d-20261106/evidence/r08-hygiene-complement-producer.json
python topics/padua-3d-20261106/code/t9_r06_manifest.py --output topics/padua-3d-20261106/evidence/r08-hygiene-t9-manifest.json
python topics/padua-3d-20261106/code/r08_hygiene.py halfshifts --out topics/padua-3d-20261106/evidence/r08-hygiene-halfshifts.json
python topics/padua-3d-20261106/code/r08_hygiene.py selections --out topics/padua-3d-20261106/evidence/r08-hygiene-selections.json
python topics/padua-3d-20261106/code/r08_hygiene.py complement --out topics/padua-3d-20261106/evidence/r08-hygiene-complement.json
python topics/padua-3d-20261106/code/r08_hygiene.py raw-inventory --inventory topics/padua-3d-20261106/evidence/r08-hygiene-raw-inventory.json --out topics/padua-3d-20261106/evidence/r08-hygiene-raw-check.json
python topics/padua-3d-20261106/code/r08_hygiene.py pins --out topics/padua-3d-20261106/evidence/r08-hygiene-pins.json
```

Default census input: `/tmp/padua-t10-20261106-7afa6a54/census.json`; default quality input: `/tmp/padua-t10-20261106-7afa6a54/t10-quality-raw.json`. Both can be overridden with `--census` and `--quality-raw`. The 51-path check reconstructs the inventory from source-linked committed receipts, then reads each recorded local raw path. Regeneration is required if these transient files are absent; this result does not claim cold-storage delivery or future availability. Timings are recorded per receipt; Python 3.12.14, numpy 2.3.5, scipy 1.17.0 and sympy 1.14.0 were used.

All eight new JSON files are below 16 KiB (largest 8,639 bytes). No mathematical status is upgraded by this developer replay. A separate audit remains required for the material source/evidence changes. Optional broader manifest suffix/subdirectory guard hardening is outside this worker's changes; the orchestrator owns the final manifest and its regeneration.

## Audit04 G3 — retirement of legacy current-pins replay, 2026-11-12

The `r08_hygiene.py pins` command above and its
`evidence/independent-r06-pins.json` input are **retired as a current-head
replay**. The JSON's “Current code/data audit pins” label describes its
historical revision only and is superseded by this dated note. Its bytes
are preserved, including the v5 artifact_manifest.py identity, because the
historical `r08-hygiene-pins.json` receipt records an actual earlier check.
At audit04 the command fails on the newer manifest-generator hash; this
is accepted, not a scientific failure and not evidence of a current pass.

Current artifact integrity is checked by the master manifest's documented
`artifact_manifest.py --verify` command, with the current generator and
manifest recorded by the orchestrator. The retired command is retained
above only under **Commands actually executed** as history; it is not an
instruction for current verification. Other historical execution identities
are not reattributed. No new pin-check execution is claimed.
