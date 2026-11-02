# Supplementary storage-repair check

2026-11-02. Distinct Codex checker `/root/cold_storage_audit`, requested/configured `gpt-6-astra` high; serving model/effort metadata not independently exposed. This is a supplementary independent recheck of Codex development under handoff 09, **not the required independent Claude protocol review**. Audit-02 and its original CS1/CS2/CS3 verdict remain unchanged as historical records. No mathematical claim, scientific acceptance predicate, status or ID was changed or reapproved.

**Final supplementary verdict: PASS within the documented static/quiescent POSIX scope.** One newly identified foreign-worktree defect was returned to the developer, repaired by that developer and independently rechecked below. Required independent Claude review remains pending.

Rules and snapshot Git HEAD: `93169ab6e193fbbef91af16914cd1191e7564420`. The parent separately published the administrative handoff-09 redirection at `863c319b…`; this selected-file snapshot's Git HEAD remains 93169ab. Rules hashes match those already read; AGENTS, WORKFLOW, Codex role, handoffs 08/09, old CS1–CS3/support, response-01, its supplementary review, PR_PREPARATION and the revised helper/manifests were inspected. This is protocol-only work with no novelty content, so no full IDEAS reread or generation gate was needed.

## Candidate identities and scope

| Candidate file | SHA-256 |
|---|---|
| `tools/cold_storage.py` | `d12fc95dc1fe6145ad0f82b225104cee568bab5586bcd247fe445c671f123bd5` |
| `tools/test_cold_storage.py` | `0aac0194efcd551a6ebe97216d2bf22992d9f3e86c8b0aa77e584285cf5fc3fe` |
| `cold-storage.json` | `88871c2064aa300bcdbcfae93e7b9de528daf3d60241d608454d8ea420216908` |
| `COLD_STORAGE.md` | `4ea56e5d2548a75e1ef1752c79e59a40d274c6efb7be07da3f01f0c482c34ce9` |

These are working candidate hashes, not a claim that they were already committed at the snapshot HEAD. The frozen source of the archived artifacts is `1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7`. Tests invoke this exact helper file after recording its hash; it remained unchanged during those executions. All large outputs and destructive fixtures stayed in exclusively owned `/tmp` directories. Only this report and its compact [JSON receipt](storage-repair-check.json) were written in the shared repository; there were no shared Git index/ref mutations. The supplied test harness initializes and stages files only in its own temporary repositories, as expressly permitted by the parent.

## Reconstructed safety argument

The implementation validates the manifest format, unique JSON keys, full object identifiers, integer byte counts, path normalization, role markers, duplicate/casefold paths and file/directory prefix collisions. `source_entries` requires an actual commit, a regular Git source entry at the exact literal path, the declared blob ID and matching SHA-256/length. Thus correct arbitrary blob bytes cannot masquerade as a different source path.

`SafeTree` opens each directory component from `/` with `O_DIRECTORY|O_NOFOLLOW`; final reads use non-following stat, regular-file checks, `O_NOFOLLOW|O_NONBLOCK` and identity comparisons. It requires the relevant POSIX descriptor primitives and refuses unsupported platforms; this applies to manifest loading and verify as well as mutation. There is no unsafe path fallback. This supports Linux/macOS where primitives are available or an appropriate WSL filesystem, not an untested native-Windows guarantee.

Before writes, every source and destination—including the deterministic export receipt—is checked. Known tracked/prefix collisions in the source repository and differing/nonregular destinations are refused before directory creation or payload writes. Matching regular files are reused without rewriting. New files use exclusive creation. Cleanup validates all destination paths before deleting any candidate; it retains mismatches and tracked paths and repeats identity/index checks before descriptor-relative unlink. It never recursively deletes directories, arbitrary unknown files or export receipts.

These guards address the original static overwrite and symlink cases. They are deliberately not a transaction or an adversarial-concurrency guarantee: the destination/index must remain quiescent; an actor can move open directories or swap a final entry after the last comparison; partial new writes can remain after I/O errors. Those limits are explicit in helper/docs. No proof of atomic compare-and-unlink or hostile concurrent safety is claimed.

## Executed checks

### Supplied CLI suite, expanded from 16 to 19 tests

Executed `python -B tools/test_cold_storage.py` from `/workspace/padua-storage-fix-20261102`; the initial 16 tests passed, and after the developer added the foreign-worktree repair, the complete expanded **19-test suite passed** independently. Final stdout/stderr are in `/tmp/padua-storage-final-tests.stdout` and `.stderr`; the receipt pins the latter's SHA-256.

The suite covers the historical active-version exception, directory addressing, refusal before any payload when a tracked active manifest exists, normal restore/verify/clean, differing late collisions, matching-file and receipt idempotence, receipt conflict preflight, parent/final symlinks, cleanup preflight, tracked/differing preservation, unexpected tracked payload rejection, unsafe paths/roles, duplicate entries, forged source association and generic planning thresholds.

### Eleven additional static controls

An independent temporary harness reused only the test driver's isolated fixture construction, then exercised additional cases:

1. Destination-root symlink: restore, clean and verify all refused.
2. FIFO target: all three refused without blocking or writing later payloads.
3. Export-receipt symlink: refused before payload creation, outside bytes preserved.
4. Duplicate JSON object key: rejected.
5. Casefold destination alias: rejected.
6. Manifest file/directory prefix collision: rejected.
7. Absent-but-indexed destination: refused before creating its destination directory.
8. Manifest-file symlink: rejected at load.
9. Dangling final symlink: refused, target remains absent and symlink preserved.
10. Tree object supplied as `source_commit`: rejected.
11. Missing descriptor support simulated in-process: load fails closed with the POSIX requirement; original process capability set was restored immediately.

All eleven passed their refusal/preservation criteria on the final helper; they were repeated after the source change. The harness and temporary repositories never changed the shared index or user data. They supplement code inspection; they do not cover arbitrary races, mounts or every filesystem implementation.

### Real 36-file operations

The actual revised manifest and real pinned Git objects were used, with fresh scratch root `/tmp/padua-storage-supp-uvxsg5bi` after the final helper/metadata freeze. Full CLI argument/output records are in the receipt.

- `verify padua-argmax-alln-20261101`: accepted, 36 objects, zero restored copies, **one** regular active tracked historical-version path (`evidence-manifest.json`). This distinction does not validate the active manifest's contents.
- Default `restore padua-argmax-alln-20261101`: correctly refused the tracked active manifest **before any archived payload was written**. Its current bytes remained unchanged.
- `restore … --dest <scratch>/restore`, then `verify … --dest …`: all 36 present/accepted. Every restored file was independently byte-compared with `git show <source>:<path>`.
- Repeat restore: all payload mtimes unchanged, establishing idempotent reuse for this static case.
- `clean … --dest …`: removed exactly 36 matching copies, preserving a separately created unrelated file; no archive files remained. Final scratch verify accepted with zero copies.
- `export … --dest <scratch>/export`: all 36 payloads byte-equal to their source paths. Repeated export preserved the deterministic receipt's bytes and mtime.
- `plan topics/padua-argmax-alln-20261101`: its remaining candidate is the explicitly excepted active integrity manifest. This is a generic candidate list, not a claim of zero large files or policy failure.

The active current manifest and the shared `.git/index` were hashed before/after and remained unchanged during this sequence. AC delivery was not attempted; scratch export does not complete delivery.

## Metadata and short regeneration

Every one of the **36 path/bytes/SHA-256/blob tuples**, their order, source commit and **2,526,191-byte** total is unchanged from the original manifest. Every tuple was independently verified against the real source path and bytes. All **19 unique script-path/blob pairs** resolve correctly at that source; all 36 human-table rows agree with the machine identities and invocation strings. Exactly one entry has the explicit historical-version role.

CS3 coverage:

- A n9–16: all eight archived JSONs confirm 90 dps, grid 801 and the specified checker/leaf options. The frozen producer contains exactly three old-root occurrences, matching the documented scratch relocation; original process grouping is honestly unrecorded. The n8–12 log's unrecorded shell-timing wrapper is distinguished from equivalent scientific stdout.
- D: the explicit 21-degree argument matches the source defaults; adjacent `padlib.py` relocation and writing beside the copied producer are documented.
- The audit-support inventory and input snapshot are explicitly historical retrieval-only records; unavailable scratch provenance is not advertised as regenerable. The old evidence manifest is distinguished from the active tracked manifest at the same pathname.
- Historical T1 rows now name the historical analyzer and the T2/T3/T4 prerequisites. The current non-splitting analyzer and complete scratch reconstruction are distinguished. No historical split was recreated at the branch head.
- Remaining producers' arguments, dependencies and short evidence locations are retained with scientific-versus-timing/argv differences disclosed. Full source-tree bootstrap requirements include inherited inputs; no current source is silently substituted for the pinned source.

Regeneration used `/tmp/padua-storage-supp-0vg39wkb`; the later helper-only repair did not change these scientific sources. Executed a short fresh D3 E-P regeneration from eight pinned source/dependency files plus the historical note, materialized into scratch using `git show`. All eight Python files are byte-identical to the current scientific sources; the dated note has subsequently changed and the historical version was deliberately used. Command:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B <scratch>/regen/topics/padua-argmax-alln-20261101/code/gated/d3_edge_generate.py --output <scratch>/regen-output/d3_edge_certificate.json --ep-output <scratch>/regen-output/d3_ep_screen.json
```

Exit 0. The E-P screen is **byte-identical**, 24,993 bytes, SHA-256 `3215523e1a768ce7e81c76283ac18bf476f8162bdcd84e579a7b93388707d14c`. Sources, exact absolute command and result are pinned in the receipt. The certificate is only a by-product; no new mathematical audit/acceptance is claimed. No full T1/A/D scan or new research was performed.

## Newly found foreign-worktree defect and developer repair

The first candidate (helper SHA-256 `416b03cb8e55f0f4bf8b75b1989d73b30e6f2fc16986d79f8b53baf37aa8c7d2`) consulted only the source repository's index. An exclusively owned fixture restored three matching files to an external directory, initialized/staged that directory as another repository, then ran `clean --dest`: all three foreign-index-tracked files were removed. I returned this defect to the developer without editing the implementation.

The developer's final helper adds descriptor-based `.git` marker detection at absolute destination ancestors and throughout payload parent traversal for **restore/export/clean**. Source ROOT's own metadata is permitted with its existing tracked checks; its containing ancestors are shadowed when operating within that source checkout. Nested foreign checkouts are refused. Nonempty `.git` directories, marker files (including linked-worktree-style files), symlinks and other non-directory markers cause refusal. Empty `.git` directories contain no index and are explicitly ignored, including the execution environment's empty sentinels. Quiescence includes no concurrent Git initialization or marker creation. Read-only verify intentionally retains safe reads without this mutation refusal.

Independent recheck on the final hash passed: the foreign-root tracked-file case now refuses without deletion; destinations beneath a foreign ancestor and nested checkouts along payload paths also refuse restore/clean; a `.git` file marker refuses both. Further probes confirmed `.git` symlink refusal, nested-worktree export refusal before payload/receipt creation, and successful restore/clean with an empty `.git` sentinel. The supplied final suite independently covers foreign ancestor restore/export and nested mutation preflight. The new finding is resolved within this stated static contract; it is preserved in the receipt's discovery/disposition history.

## Preservation and next boundary

The ten prior audit-02/support/response-code-review files were independently compared to their snapshot Git blobs and remain unchanged. This review does not close the historical audit in place or approve Codex's own repair as a Claude reviewer. Final current-integrity refresh and plain checking await the parent's covered-record freeze; no final plain check is claimed yet. Required independent Claude review of response-01 and this repair, other-topic integration, AC delivery and actual Windows/WSL behavior remain outside this supplementary acceptance scope.
