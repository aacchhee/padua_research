# Audit 01 — repository cold-storage cleanup

Verdict: **CHANGES REQUIRED**. The 176 removals preserve exact, retrievable bytes, and the sampled scientific regenerations pass. Repair the export receipt, restore collision handling and clipped regeneration instructions before readiness. No science is reopened or rejected.

Auditor/orchestrator: Codex; AC requested/configured `gpt-6-astra`, high. Backend model/effort metadata is not separately exposed. Date: 2026-11-02.

## Pins and scope

- Rules read at `1d90af5d58fca87f240a04c18c427e8f59e2d6b8`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`.
- Scientific/technical candidate requested by handoff 02: `b519233d461985dfee6cecbbb55c31c165ee4ec7`; inspected published head: `1d90af5d58fca87f240a04c18c427e8f59e2d6b8`. The latter adds handoff 02 and supersedes handoff 01 only.
- Base and freshly fetched main: `2b52b432fe59c9a50aef9deebe5152c5d6874465`, already an ancestor. No base integration is needed for this audit.
- Read both handoffs, the topic log/results, the cold-storage template, all nine machine manifests and their human records, the complete tool, and sampled generator/checker sources and summaries listed below. AC's approvals are recorded in handoff 02 and the log; they do not authorize a purge during this audit.
- Protocol, bytes, retrieval, tool safety and preservation only. No new mathematical, novelty or priority claim; the full ideas/literature gate is inapplicable. No IDs/reservations: **no range**. No developer code, manifest, theory, historical audit verdict or rule was repaired by this auditor.

## Findings

### F1 — P1 — export receipt asserts destination verification without readback

Location: `tools/cold_storage.py:110–118,139–145`.

`write_entries` hashes the source `data` buffer, writes it, and records that same buffer's size/hash. `cmd_export` then unconditionally sets `all_hashes_match_manifest: True`. No exported path is reopened. The receipt therefore does not establish the hash-verified cold-storage export required before the approved history purge. `verify` cannot fill that gap: it checks Git objects and repository paths, not the export destination.

Reproduction: the committed [safety harness](audit-01/safety.py) injects destination corruption immediately after an otherwise successful `Path.write_bytes`; export still returns success and writes a receipt with the flag true. This is a controlled fault injection, not an observed filesystem failure. Ordinary exports were also independently read back and passed.

Required response: hash and count the destination bytes after writing, issue success only after all destinations pass, and provide a repeatable destination verification operation so AC can verify a transferred archive independently. Failed export/reverification must not leave a stale successful receipt usable for a purge. Test corruption, missing/truncated files and an ordinary export. No purge is authorized by this audit or its cloud scratch exports.

### F2 — P2 — restore silently overwrites differing local and tracked files

Location: `tools/cold_storage.py:110–125`.

The default restore writes every manifest path with `write_bytes`, regardless of an existing file's content or index state. A researcher who restores, regenerates/edits an output, and repeats restore loses that work. A reintroduced tracked file's local modifications are overwritten too. The safety harness reproduces both cases in a disposable repository. `clean` correctly preserves differing and tracked files; restore should preserve those protections as well.

Required response: preflight the entire restoration, allow absent paths and byte-identical regular files, refuse differing files, directories and symlink destinations/parents, and avoid partial mutation on a known collision. An explicit overwrite option, if supplied, must be deliberate. Apply equivalent collision protection to exports or document and test a deliberate replacement policy. Preserve unrelated files.

### F3 — P2 — generator instructions are clipped in the new manifests

Location: `topics/padua-proof-attempts-2-20261101/cold-storage.json`, rows for `outputs/a5_n7_certificate.json.xz` and `outputs/a5_n8_interior_candidate.json.gz`; the corresponding `COLD_STORAGE.md` rows repeat the clipped strings.

The n8 four-step chain stops during step 3 at `--…`; it omits the remaining continuation arguments and the reflection/final retention step. The n7 entry also ends with a clipped reference. These are newly authored archival instructions, not complete frozen commands. Source and output hashes remain correct, so retrieval is unaffected, but the instructions do not meet the approved rule's regeneration requirement. The n8 file remains future-work evidence for an OPEN target; this finding does not change its scientific status.

Required response: provide the full recorded commands or precise links to complete committed command blocks, preserving unavailable intermediate inputs and historical environment limitations explicitly. Do not truncate command metadata to a fixed string length. Check the other long rows for clipping too; the n3 row contains an abbreviated theory filename rather than a clipped shell invocation.

### F4 — P3 — correct and enumerate the retained-file readers

Location: charter and MZ `cold-storage.json` addenda and matching human rows.

- Charter's `cold-storage-manifest.json` row says to restore it before `verify_cold_storage.py`. That script actually reads `<root>/bundle-manifest.json`; restoring the repository manifest is neither its input nor a way to recreate the off-repository bundle. The tool's six-file restoration itself passed.
- MZ's `final-id-map.json` row names only `check_response_01.py` and “the other readers.” The other working-tree readers are `tracks/mz-constants/evidence/protocol-check.py:8`, `astra-final-check.py:28` and `astra-response-01-check.py:99`. Name them rather than relying on an unspecified list.
- Distinguish working-tree readers from historical `git show` readers. For example, programme audit-04 allocation/literature checkers read pinned revisions; restoring current files does not replace their history prerequisite. Programme's live allocator also needs the lattice and bivariate topic maps before its own two literature maps (`pr-prep/allocate.py:30–31,59–62`). Existing notes mention these dependencies across several topics; give one explicit combined retrieval recipe.

The other eleven moved registry/source entries have valid pins and relevant reader notes (or are passive provenance records). No newly missing generating-code file was found in the command samples. Historical one-shot validators are not guaranteed to accept a cleanup head even after restoring outputs, because rules/link text/index inventories changed; run them at their recorded revisions.

### F5 — P3 — repair the aggregate moved-byte totals

Location: `topics/cold-storage-20261102/LOG.md:19`, `results/cold-storage-20261102.md`, PR #18 WORK.

The actual 176 deleted files and all nine manifest totals sum to **15,846,089 bytes**, not the PR's 15,796,752. The nine first-pass table rows sum to **15,468,874 bytes**, not the log's 15,419,537. The 13 addendum files correctly total 377,215 bytes. Both erroneous aggregate totals are short by 49,337 bytes; individual manifest hashes, sizes and totals are correct. Correct the aggregates without changing historical evidence.

## Executed checks and accepted parts

Environment: Linux x86_64 cloud executor, Python 3.12.14, SymPy 1.14.0. Standard library for the storage checks. No random seed for the storage tests, C0 enumeration or symbolic rerun. Full compact results and the tool hash: [receipt.json](audit-01/receipt.json). Reproducible audit drivers: [inventory.py](audit-01/inventory.py), [safety.py](audit-01/safety.py). Larger regenerated files and temporary fixtures stayed outside Git.

1. Independently enumerated `git diff --diff-filter=D --name-only <base> <candidate>` and joined every path to all manifests. Exactly 176 deletions, 176 distinct entries, no additional deletion or duplicate. For every entry, independently checked `git show <source_commit>:<path>`, SHA-256, byte size, and `git rev-parse <source_commit>:<path>` against the recorded blob. Every machine total and human table identity matched. This includes all 13 addendum files.
2. Executed `python tools/cold_storage.py verify <slug>` for all nine slugs; all accepted. The receipt contains their counts/totals. `plan .`'s extension policy leaves no nonmanifest generated-data candidate at or above 16 KiB. The conservative nonrecord-extension total at the candidate is **3,300,628 bytes**; this heuristic is not a classification of every source-data file as generated output.
3. Executed restore, compared each file to `git show 2b52b43:<path>`, then clean for **charter (6)** and **lattice (26)**. All 32 files matched exactly and were removed; no prior working copy existed. The safety harness separately confirmed that clean removes a matching untracked copy and preserves differing and tracked copies.
4. Exported all nine manifests to `/tmp/padua-cold-audit-export`, then independently reopened and hashed every exported path: all 176 passed. This establishes only the audit's cloud scratch copy, not AC delivery or long-term retention.
5. Executed these regenerations and compared to pinned base bytes; all four outputs were **byte-identical**, including all six symbolic records:

   ```sh
   python tracks/lattice-unisolvence/code/c0_catalogue.py --output-dir /tmp/cold-audit-c0
   python topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --symbolic --output /tmp/cold-audit-symbolic.json
   ```

   C0 regenerates `catalogue.json` and `count-trials.json`, with direct self-check enabled. The fourth output is MZ's `batch-registry-resolution.patch`, regenerated by the complete ten-path `git diff --unified=0` command stored in the receipt. stdout went to cloud scratch, never over original evidence.
6. Inspected at least one representative generating source and summary in every directory: bivariate L2 dots/audit-01 L2; charter symbolic factors; lattice C0 rounds/count receipt; MZ integration patch/impact; drift E34 checker/audit-02 E34; signed MZ exact producer/audit-01 R1; proof-attempts-2 A2 sanity/T-A2; programme obstruction checker/report; MZ track reproduction runner/reproduced-spectra table. Sample flags are supported, code remains committed, and summaries retain the stated evidence scopes. This is command inspection, not execution of all expensive historical campaigns. No new wrong generator flag was found in these samples; F3 records the incomplete command strings.
7. Compared all modified pre-existing Markdown after masking only inline link destinations. All **51 non-cold-storage documents** are otherwise identical. All four pre-existing `COLD_STORAGE.md` prefixes are preserved modulo their two redirected links; new sections are appended. Count: **91 + 2 = 93** destination changes, with unchanged labels/statements/statuses/IDs/audit verdicts. No code from the scientific campaigns was changed or deleted. The only other modified pre-existing file is the approved workflow paragraph.
8. Independently scanned relative inline Markdown targets, comparing sets of source/target pairs: 308 unresolved before and after, **zero new unresolved pairs**. This scanner counts unique pairs and excludes anchors/URLs/absolute paths; it does not reproduce the developer's occurrence count of 629. All redirected targets resolve.
9. Read the workflow delta against AGENTS and the surrounding evidence rules. AC's approved wording permits small necessary evidence/manifests, keeps repository-only results, and leaves owner merge/history authority intact. No additional rule inconsistency was found. The new command/checker metadata requirement motivates F3/F4.

To replay the audit drivers, use a disposable checkout of `1d90af5d58fca87f240a04c18c427e8f59e2d6b8`, then invoke these committed scripts by absolute path from that checkout's root. `inventory.py` requires the pinned HEAD; `safety.py` imports that checkout's tool and uses a separate temporary Git repository. Both write compact raw receipts to `/tmp/cold-audit-*.json`. Scientific rerun commands above also run from the pinned root. The committed receipt records the executions already performed here, not a future run.

## Residual limits and disposition

Git history is still the authoritative retrieval source. No Windows bridge, AC export receipt, history rewrite or force-push was attempted. Current restore/verify require Git objects; they do not implement retrieval from a future post-purge archive. A later purge plan must preserve exported metadata and code and replace locators/restore instructions before old objects disappear; that is outside this audit.

PR #18 remains **draft, Stage WORK** pending a Claude response to F1–F5 and a focused Codex re-audit of material fixes. The sampled mathematics, existing proof statuses and the cleanup's byte-preservation result stand. Coordinate any tool correction with PR #17's shared tool before integration. Only AC merges. Next instruction is in handoff 03.
