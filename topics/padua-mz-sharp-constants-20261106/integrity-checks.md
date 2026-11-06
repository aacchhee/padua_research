# Integration integrity checks

Scope: mechanical integration support only, not a mathematical audit or an independent numerical rerun. No producer, eigensolver or degree scan was executed. The novelty gate does not apply because this work adds no mathematical mechanism or novelty claim.

Rules and source corpus: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`. This is a fetched source corpus, not a Git checkout; publication belongs to the coordinator. Assigned model/effort: `gpt-6.1-sol`, medium; actual runtime model/effort metadata is not exposed to this worker.

## Current snapshot: PROVISIONAL

The [manifest](evidence-manifest.json) records topic-relative paths, byte sizes and SHA-256 for every topic Python source and JSON record, except the manifest itself and these mutable numerical receipts:

- `evidence/S4-padua-essential.json`
- `evidence/check-S4-padua-m3000.json`

The explicit exclusions are recorded in the JSON. Prose, caches, external source files and large raw outputs are outside its hashing scope. JSON provenance inventories are included, but their referenced external payloads are not recursively verified. This distinction matters: identity checks establish the current file bytes, not correctness of the numerical or mathematical claims. Final regeneration must include the completed receipts and any final fit receipts after the coordinator signals readiness.

The generator checks membership as well as hashes: an added, removed or edited code/JSON file fails verification until intentional regeneration. Generated JSON files and the manifest must each remain below 16 KiB; it does not split files. The generator itself is included in the inventory. No prose is hash-pinned.

## Executed commands

From any working directory:

```sh
python /workspace/sharp-work/topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --write --provisional --exclude evidence/S4-padua-essential.json --exclude evidence/check-S4-padua-m3000.json --checks
python /workspace/sharp-work/topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --checks
```

The first provisional run passed with 54 code/JSON identities and a 6,201-byte manifest; Python AST parsed 21 topic code files and JSON parsed 36 topic files, all below 16 KiB. Local Markdown checking examined topic prose plus the topic results file: 139 genuine local file links, zero missing targets (54 documents before this check record was added). It ignores fenced and indented code, inline code, TeX math, remote URLs and section anchors; plain path mentions are not links. File-target existence is checked, not anchor validity or remote availability.

Final commands, to execute only after the completed numerical receipts and final prose exist:

```sh
python /workspace/sharp-work/topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --write --checks
python /workspace/sharp-work/topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --checks
```

Final command results are pending. No other worker files were modified by this integration worker.
