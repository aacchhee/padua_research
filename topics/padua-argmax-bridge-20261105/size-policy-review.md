# Committed generated-output size review — 2026-11-05

Rules/source read: `dfb0dee2d7687ab2d57e77dcb29b41f223a341ae` (`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`). Routine accounting; novelty gate not applicable. Read-only bounded Codex subagent check; actual model/effort metadata are not exposed to this worker. No Git changes or archival actions performed.

**Finding: aggregate compliance is not demonstrated.** The conservative committed-output upper bound is **6,436,822 bytes**, versus the requirement “well below 5 MB.” The inherited `origin/main` baseline already has an upper bound of **6,162,620 bytes**. Do not report the existing suffix-based receipt as aggregate-policy approval. These are upper bounds, not a claim that every conservatively counted administrative JSON byte is mechanically generated. A precise over-cap generated-output lower bound was not established.

| Scope | Counted upper bound (bytes) |
| --- | ---: |
| Baseline `be9a8318150204711d5446d2ea26284cf1ed0819` | 6,162,620 |
| Reviewed head `dfb0dee2d7687ab2d57e77dcb29b41f223a341ae` | 6,436,822 |
| Bridge topic contribution; no removed baseline outputs | 274,202 |

The bridge contribution is 232,813 JSON bytes, 38,824 gzip bytes and 2,565 bytes of `COLD_STORAGE.md`. It contains no byte-identical duplicate counted blob elsewhere in the reviewed head. Later untracked review supplements are outside this committed-head measurement and must be added before final readiness.

## Classification and limits

Inventory covers all 4,040 committed paths, using Git tree blob lengths, not working-tree sizes, `.git` history or filesystem allocation. Exclusions are source (`.py`, `.sh`, `.c`, `.cpp`, `.h`, `.tex`, `.bib`, `.diff`, `.gitignore`: 1,015 files, 5,703,992 bytes), and authored prose/static text records (`.md` other than `COLD_STORAGE.md`: 1,643 files, 17,300,446 bytes). These include theory, literature, logs, audits, handoffs, registries and short written result summaries; WORKFLOW explicitly distinguishes short handwritten results from generated outputs. Source snapshots remain source/static inputs regardless of their directory. No JSON is excluded merely for being an input, mapping, receipt or manifest. Ambiguous administrative JSON and text are deliberately counted, which makes this conservative rather than an exact generated-byte census. Markdown classification is by documentary role and inspected examples, not proof of the authorship of every line.

All remaining 1,382 files count: JSON 4,936,038; `COLD_STORAGE.md` 815,779; `.out` 196,056; `.txt` 183,365; `.gz` 163,814; `.stdout` 88,955; `.svg` 37,094; `.stderr` 11,360; `.sha256` 3,143; extensionless checksum inventory 775; `.err` 274; `.time` 87; `.exit` 77; `.flag` 5 bytes. This includes uncommon output suffixes missed by a narrow artifact-suffix sum.

Generated retention manifests count. The storage tool's `is_manifest` exclusion and `RECORD_EXT` set are planning heuristics, not an aggregate-policy exemption. `COLD_STORAGE.md` tables are counted conservatively, including human annotations. Cold-storage JSON contributes 427,821 bytes. Even exempting both retention-manifest families would leave 5,193,222 bytes at this head; that sensitivity calculation still includes ambiguous administrative/static inputs and is not a generated-output lower bound. The SVG identifies Matplotlib in its metadata and is a genuine generated figure (37,094 bytes).

The 109,206-byte `topics/padua-argmax-alln-20261101/evidence-manifest.json` is a genuine generated hash inventory. Its own `integrity_manifest_exception` records an explicit handoff-07 exception to the usual per-file limit; that does not establish an aggregate waiver. There are 19 counted files above 16 KiB, mostly retention inventories, including that manifest and the SVG. No new bridge file exceeds 16 KiB.

## Concrete options and retrieval

A bridge-only cleanup cannot establish aggregate headroom: removing its entire 274,202-byte contribution returns to the inherited 6,162,620-byte upper bound. A documented policy exception or repository-wide classification/archival pass is required before claiming compliance. This worker is not authorized to change other topics. A conservative target of 4,000,000 bytes would require reducing the present upper bound by at least 2,436,822 bytes, plus space for replacement manifests/receipts; 4 MB is a recommendation for headroom, not a new policy threshold.

Largest counted topic totals are alln 1,028,773; proof-attempts-2 1,000,973; lanczos-frontier 873,297; bivariate-lanczos 645,236 bytes. Review historical/raw/repeated run receipts in those topics first, keeping code and short necessary evidence. Repository-wide byte-identical counted output duplicates could save only 97,945 bytes before new manifests; duplication alone cannot solve this. Independence records must retain their provenance even when payload bytes match.

Large initial candidates for review are the alln 109,206-byte evidence inventory, proof-attempts-2 76,837-byte `COLD_STORAGE.md`, alln 56,236-byte `COLD_STORAGE.md`, proof-attempts-2 53,124-byte `cold-storage.json`, charter 51,092-byte `COLD_STORAGE.md`, and alln 47,950-byte `cold-storage.json`. These are candidates for compact replacement plus pinned historical retention, not instructions to delete evidence or mandatory retrieval records. Other-topic cleanup needs dependency/link checks and owned changes. Do not split payloads merely to evade the policy.

No counted current path/blob matched an existing cold-storage manifest entry's exact `path`, `git_blob` and `bytes` triple. Existing manifests therefore do not authorize treating these current bytes as already archived. All reviewed committed bytes are locally retrievable with `git show dfb0dee2d7687ab2d57e77dcb29b41f223a341ae:PATH`; this check did not establish that this integration commit is pushed or that AC cold storage is reachable. A cleanup must pin a pushed source commit/blob, SHA-256, size, commands and short summary, then verify retrieval through the repository cold-storage procedure. No archive export or deletion was run.

## Reproduction

Run `git ls-tree -rl REF` for the two full SHAs above. Split each row at its tab; take its decimal size and repository path. Exclude the source suffixes listed above and `.gitignore`; exclude `.md` except basename `COLD_STORAGE.md`; sum every other row. Subtract baseline from head. Group counted rows by blob ID to reproduce duplicate accounting. Compare counted rows to all committed `cold-storage*.json` entries by exact path/blob/size for the existing-manifest check. The inventory was executed separately from the topic's original size receipt. Read-only temporary detailed inventory: `/tmp/padua-size-inventory-review.json` (not a durable artifact; regenerate from Git).

Scope frozen after this report. Final readiness must inventory the eventual commit, including subsequent review supplements.

## Conditional expanded-scope archival budget

The following disjoint candidate groups provide an arithmetic route to headroom, **not a verified safe deletion plan**: 124 retention inventories (1,243,600 bytes); 407 completed-audit outputs (1,296,172 bytes); 147 administrative receipts (1,048,292 bytes). Total 678 files / 3,588,064 bytes. A combined replacement-record budget of 1,000,000 bytes leaves the reviewed upper bound at 3,848,758 bytes. Later essential evidence must be added. The file-level candidates and blob IDs are in temporary `/tmp/padua-size-archival-candidates.json`; regenerate from the reviewed tree before use. Grouping prioritizes retention basenames, then audit paths, then preparation/protocol/finalization paths and receipt names. This deliberately broad candidate pool requires culling and byte-budget recalculation.

Safety preconditions: keep every original byte at a verified pushed commit/blob; generate SHA-256/size/command/checker/summary entries; resolve every live code/hash/input/link dependency before removing a path. Completed audit output includes independent proof-checker receipts (for example proof-attempts-2 `audit-support/claude-audit-01/n7-checker.json`); administrative output includes result-bearing receipts (for example `outputs/a5_checker_n7_full-integration.json`), so neither class is intrinsically disposable. Final-ID maps may be runtime inputs. Old retention JSON is an active input to `tools/cold_storage.py`, which expects complete entries: replacing it with a prose index requires preserved retrieval and a loader/procedure change, not just a short URL. Existing canonical summaries and recorded generating/checking commands should be carried from topic theory, audit records and old manifest entries; this worker has not reconstructed all 678 command/dependency chains. No blanket safe or minimal archival plan has been established. Expanded-scope approval and a dependency review remain necessary before acting.
