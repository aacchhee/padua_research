# Audit 02 — cold-storage protocol

Date: 2026-11-02. **Verdict: FINDINGS; return to Claude development.** Historical retrieval and the actual 36-file roundtrip pass. Two safety defects and one regeneration-documentation defect remain unresolved. No scientific claim or status is changed; audit-01's mathematical acceptance remains intact and PD-T099 remains OPEN.

## Identity, independence and scope

Auditor: distinct Codex protocol-audit agent `/root/cold_storage_audit`; requested/configured `gpt-6-astra`, high effort under handoff 07 Task B. Runtime serving model/effort metadata are not independently exposed. High effort was selected for destructive cleanup, history provenance and filesystem edge cases. The parent orchestrator alone controls Git. This auditor edited only this report and `response-support/cold-storage-audit/`; it did not repair Claude's implementation or approve its own repair.

Rules read: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md` at `b8fbb5c5be374bf658d2970681c7cac0fb40d737`. Source before deletion: `1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7`. Initial cold-storage output audited: `6fae535df28303b27ca1d533d9afa229660a3a20`. Tool impact extension: `b8fbb5c5be374bf658d2970681c7cac0fb40d737`.

The workspace is a selected-file snapshot with exact Git commit/tree objects imported by the parent through the GitHub connector, not a fresh full clone. The parent supplied all historical blobs needed for the diff, retrieval and comparisons. Actual Git `show`, `cat-file`, `rev-parse`, `diff` and `ls-files` were used; the current index represents the pinned full tree with unmaterialized files marked skip-worktree. This audit made no network CLI calls or Git mutations.

Read: the rules above; handoffs 06/07; LOG cold-storage/history entries; audit-01 and its six sub-reports; support README; both cold manifests; initial/current tool; generator interfaces, retained receipts and supporting summaries listed in the per-entry review. Scope is packaging, provenance, reproducibility and filesystem safety only. It adds no ideas, mechanisms, novelty or negative mathematical claims; therefore the workflow's no-novelty exception applies and the full `state/IDEAS.md` was not reread. No new mathematical audit, larger-degree run or status upgrade was undertaken.

## Pinned content identities

| Object | SHA-256 |
|---|---|
| Initial `tools/cold_storage.py` | `49c4842a4ff358e7b73f394042d0ff362cfc0c9087be770790cc2b5b17840b00` |
| Latest audited `tools/cold_storage.py` | `62ea9e0da86ef8a72a2298f093ed4c54691cc8cc1bd2850974248eebcaa43b58` |
| `cold-storage.json` | `ef6efffe18f81ad9e748ff91dfdc95f25770811e1304e75c835cb6ed4b0b262e` |
| `COLD_STORAGE.md` | `29094f0bd3c1858c6704e6738ed6dbfe696a084e4827562f007e336c46bdfdcc` |

Both manifests are unchanged between initial output and pinned head. Full tool Git blob IDs, generator/summary blobs and all source-file hashes used in regeneration are in the linked receipts. The manifest itself contains all 36 artifact identities; each was independently compared to the named source commit's path, not merely to an arbitrary blob with the right hash.

## Findings requiring Claude disposition

### CS1 — MAJOR: restore/export overwrite existing data

At current `tools/cold_storage.py:111–118` (`write_entries`), `target.write_bytes(data)` unconditionally replaces the target. `restore` and `export` share this routine. There is no tracked-file check, differing-content check, symlink rejection or all-entry collision preflight. Restoring over a locally regenerated file with different results silently loses those bytes; restoring a historical manifest after a file becomes tracked can overwrite tracked work. A final-component symlink also causes a write to its outside target.

Isolated probes loaded the exact source from each audited revision and demonstrated both differing untracked and tracked destination replacement, plus overwrite through a final symlink. The fixture uses the real repository index for `ls-files`, but redirects the command's ROOT and manifest loading to a temporary directory; no real user file was damaged. An ordinary all-36 scratch export passed, but that does not establish collision safety.

**Required response:** preserve existing differing files by default; reject tracked destinations for in-place historical restoration; reject unsafe symlink/path traversal, and define safe idempotent behavior for matching files. Cover both restore and export, including the export receipt destination. Preflight before modifying files, or document/recover partial progress. Reaudit the implementation and its refusal behavior. This report does not supply a repair.

### CS2 — MAJOR: clean can delete outside the intended root

At current `tools/cold_storage.py:130–136`, `p = ROOT / e['path']` followed by `exists/read_bytes/unlink` follows parent-directory symlinks. `ls-files` tests the lexical repository path, not the target reached through that symlink. In each exact audited revision, a manifest path `link/file.json`, with `link` pointing outside ROOT and the outside file matching the manifest bytes, caused `clean` to unlink the outside file and report one removed restored copy. Thus its regular-file hash/index guards do not enforce the stated restriction to restored repository copies.

Positive controls passed: tracked matching files and untracked differing files are preserved; matching ordinary untracked copies are removed. A `../outside/file.json` cleanup probe was rejected by Git with exit 128 and preserved the file. That incidental Git refusal does not prevent the parent-symlink deletion. No test asserted that the actual 36-entry manifest contains malicious paths: all actual paths are ordinary repository-relative paths, and its normal roundtrip was safe.

**Required response:** constrain cleanup to validated in-root regular files with no traversed symlink components, retain the tracked/hash guards, and test parent and final symlinks as well as ordinary mismatches. Consider concurrent replacement when designing the guard. Do not fix by deleting an entire directory or by a blanket `git clean`.

### CS3 — MINOR: several frozen generating commands are not reproducible instructions

The first eleven machine-manifest entries all contain the same generic “Claude audit-01 sub-auditor script … see README and subaudit-reports” string. It does not identify the actual script, flags or setup. The A producer has optional checker/leaf/grid switches and hard-coded original-session repository paths; the D producer writes beside its script. The historical audit-support manifest inventories scratch-only files whose bytes were never archived; it is incorrectly described as regenerable by rerunning a named sub-auditor script. No such manifest generator is identified.

Additionally, every T1 row gives `tests_T1.py OUT/tests_T1.json; then tests_analyze.py OUT`, but the analyzer first reads T2, T3 and T4 JSONs. A fresh OUT populated by only the stated T1 producer is insufficient. The `tests_summary.json` row does disclose these prerequisites; the T1 rows should link to or repeat that requirement.

**Required response:** record exact committed script paths/identities, arguments, output setup and relocation needs; distinguish historical retrieval-only inventory/provenance from reproducible scientific outputs; state analyzer prerequisites. Byte-exact Git retrieval already passes and need not be sacrificed. The [per-entry review](response-support/cold-storage-audit/entry-review.md) covers all 36 entries and identifies which command/summary applies to each.

## Executions and passing checks

Commands ran from `/workspace/padua-response-20261102`; large outputs stayed under `/tmp/padua-cold-audit/`. Python was 3.12.14. All ordinary roundtrip/export/regeneration commands exited zero.

1. `git diff --stat 1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7 6fae535df28303b27ca1d533d9afa229660a3a20`: 45 changed paths, 36 deleted files, 601 insertions and 92,805 deletions. Independent name-set equality proves every deleted path is manifested and there are no extra deletions. Total 2,526,191 bytes; 36 distinct entries. Every source `rev-parse <source>:<path>`, `git show <source>:<path>`, SHA-256 and byte count agrees with the manifest.
2. `python -B topics/padua-argmax-alln-20261101/response-support/cold-storage-audit/roundtrip.py`: for **each** exact tool revision, ran `verify`, `restore`, `verify`, compared every restored file with `git show 1cecd68…:<path>`, then `clean`, then `verify`. Each restore/clean handled 36 files, both post-restore checks accepted with 36 copies, both final checks accepted with zero copies. Latest-tool export to a fresh scratch directory also reproduced all 36 files and emitted its receipt. No delivery to AC's machine occurred.
3. `python -B topics/padua-argmax-alln-20261101/response-support/cold-storage-audit/safety.py`: nine isolated probes per revision, with the results described above. Expected Git rejection is recorded as exit 128; destructive behaviors are findings, not passes.
4. Practical regeneration: copied the exact nine producer/dependency/note files from pinned `b8fbb5c…` using `git show`, verified every one was unchanged from initial `6fae535…`, and executed `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B /tmp/padua-cold-audit/regen/topics/padua-argmax-alln-20261101/code/gated/d3_edge_generate.py --output /tmp/padua-cold-audit/regen/out/d3_edge_certificate.json --ep-output /tmp/padua-cold-audit/regen/out/d3_ep_screen.json`. The 24,993-byte E-P screen is **byte-identical** to the deleted artifact and its pinned source blob: SHA-256 `3215523e1a768ce7e81c76283ac18bf476f8162bdcd84e579a7b93388707d14c`. No scientific exclusions or tolerances were needed. The new certificate was only a by-product; its acceptance was not claimed or reaudited here.
5. Inspected each generator's interface and its retained short summary/receipt; checked 29 script/summary paths against both pinned trees. Coverage and shortcomings are recorded entry-by-entry. Exact historical recovery does not imply a fresh producer rerun would reproduce timing, argv, session paths or historical inventory bytes.

The runner executes code fetched from the requested revision with `git show`, sets `__file__` to the repository tool path and invokes its actual `main`; it never silently substitutes current source for initial source. The safety harness alone replaces ROOT/load for isolation and delegates Git reads to the real repository. Receipt files are distinct experiment records, each below 16,384 bytes; no raw output was split to evade the policy.

## Links, wording, statuses and latest-tool impact

All advertised redirected locations resolve to the committed `COLD_STORAGE.md`, and that manifest identifies the original artifact. The exact count is **six link targets on five changed lines across four documents**: report has input-snapshot and evidence-manifest links; LOG has one of each; ideas has evidence-manifest; ideas-codex-fallback has pairing_screens. “Five link targets” in LOG/handoff is a minor count error, not a missing target. Preserve frozen audit reports, including the deliberately unchanged D1 link; readers use the manifest to retrieve its historical target.

Initial diff inspection shows no modification to topic theory, scientific code or finite certificates. The ideas/report changes are retrieval-link changes; LOG/results add storage and next-step wording. No theorem, measured conclusion, candidate disposition or status changed. “In cold storage” in results means removed from the working tree and retained in Git history: COLD_STORAGE and LOG correctly disclose that AC delivery is PENDING and history/clone size has not shrunk. Older packaging instructions still refer to the pre-move committed gzip; the new manifest is the current retrieval authority.

From initial output to pinned head, changes are only the tool plus handoff 06 status/new handoff 07. Tool additions accept direct directory slugs, exclude names beginning `cold-storage` from planning, and replace slash characters in export-directory names. They do not repair CS1/CS2. Those command paths were rerun with the actual topic slug. No audit is claimed of other topics' manifests or a repository-wide cleanup.

**Advisory:** `verify` validates object bytes but does not itself verify the association between `source_commit`, entry path and Git blob. Both exact revisions accepted a synthetic manifest with an all-zero source commit and a valid blob/hash. This audit independently checked the real association for all entries, so current provenance passes. Adding that check would prevent a future misleading verification result.

## Evidence and remaining limits

- [Roundtrip runner](response-support/cold-storage-audit/roundtrip.py) and [receipt](response-support/cold-storage-audit/roundtrip.json): real object checks, both revisions, scratch export.
- [Safety probes](response-support/cold-storage-audit/safety.py) and [receipt](response-support/cold-storage-audit/safety.json): fixtures, observed behavior and rejection control.
- [Regeneration receipt](response-support/cold-storage-audit/regeneration.json): exact command, nine source hashes, stdout, output identity.
- [Metadata receipt](response-support/cold-storage-audit/metadata.json) and [36-entry review](response-support/cold-storage-audit/entry-review.md): retained sources/summaries, redirects and coverage.

Not covered: full re-execution of every scientific producer, reproof of accepted mathematics, remote AC filesystem delivery, Windows symlink/path behavior, deliberate concurrent filesystem races, history rewriting, repository-wide size policy or the parent's subsequent response changes. The historical evidence-manifest was restored only during the coordinated roundtrip and removed again before the parent resumed work. Running the supplied roundtrip again after the response creates a new evidence-manifest intentionally refuses the occupied destination; use an isolated pinned checkout for later reproduction.

Claude must disposition CS1–CS3 and submit material tool fixes for independent reaudit. This is a protocol finding, not a withdrawal of audit-01's scientific acceptance.
