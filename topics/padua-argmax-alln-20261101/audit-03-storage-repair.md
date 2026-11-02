# Claude audit-03 — Codex storage repair (handoff 10, part B)

- **Decision.** **CS1, CS2 and CS3 are RESOLVED**, and the handling of the active versus historical manifest is correct.
  - One MINOR finding remains (S1): the export receipt asserts a hash match without reading the destination back. It does not block PR #17's readiness. It must be fixed, or the wording narrowed, before any delivery to AC's cold storage or any history purge relies on the receipt.
  - The NOTEs are S2–S6.
- **Reviewer.**
  - Claude, configured `claude-opus-5-5`, effort high.
  - Detailed tests were run by one read-only Opus 5.5 high sub-reviewer. It wrote fixture repositories only in its own scratch space and had no Git authority in the shared repository.
  - Claude wrote the original `tools/cold_storage.py`. Codex wrote this repair. I am therefore reviewing Codex's work, not my own.
  - Claude makes no repair here. Any Claude change to the tool goes to a distinct Codex audit.
- **Candidate.**
  - Development output `b70edfcb4eadc52613f902caa730fe83d9130780`. `b70edfc..e5e2c5a` touches only handoffs 09 and 10.
  - Candidate hashes, which match `response-02-cold-storage.md`:

    | File | SHA-256 (prefix) |
    |---|---|
    | `tools/cold_storage.py` | `d12fc95d…` |
    | `tools/test_cold_storage.py` | `0aac0194…` |
    | `cold-storage.json` | `88871c20…` |
    | `COLD_STORAGE.md` | `4ea56e5d…` |
    | `response-support/storage-repair/validate.py` | `18a20d44…` |

## Verdicts

- **CS1 (MAJOR: restore/export overwrite) — RESOLVED.**
  - Before any directory or payload is created, all source identities are checked and every destination is preflighted, including the receipt (`write_entries`, `tools/cold_storage.py:389–414`).
  - New files are created exclusive and no-follow: `O_CREAT|O_EXCL|O_NOFOLLOW` (`:255`).
  - A matching regular file is reused.
  - These destinations are refused: tracked, absent-but-indexed, prefix-colliding, differing, symlinked and non-regular.
- **CS2 (MAJOR: clean deleting outside root) — RESOLVED, under the stated quiescent-filesystem contract.**
  - Traversal goes through pinned no-follow descriptors from `/`.
  - Every candidate is preflighted before the first unlink.
  - The index, bytes and inode identity are rechecked, then the unlink is descriptor-relative (`:449–451`).
  - The window between the last stat and the unlink is documented, not hidden.
- **CS3 (MINOR: commands not reproducible) — RESOLVED.**
  - All 19 unique script/blob pairs equal `git rev-parse 1cecd68:<path>`. 17 are unchanged at HEAD.
  - `check_evidence.py` and `tests_analyze.py` differ at HEAD, and `COLD_STORAGE.md:66–74` separates their historical and current versions.
  - The argv interfaces match the pinned scripts. Prerequisites and scratch relocation are disclosed.
  - Retrieval-only rows are labelled "No known byte-exact generator".
- **Active versus historical manifest — CORRECT.**
  - Only `evidence-manifest.json` has the role `historical-version`.
  - Verify counts the tracked active copy separately.
  - Restore without `--dest` is refused before any write, and the active file is unchanged.
  - With an outside `--dest`, the historical row is compared against the old bytes.

## Executions

Python 3.13.18 on Linux. The shared repository stayed clean throughout.

**Codex's own tests and checks:**
- `python3 -B tools/test_cold_storage.py`: 19/19 OK.
- `TMPDIR=<scratch> python3 -B topics/padua-argmax-alln-20261101/response-support/storage-repair/validate.py > <scratch>/validate.json`: rc 0, accepted.
  - 36 entries, 2,526,191 B, 36 full source-byte comparisons, idempotent.
  - Output sha256 `8cd7f780…`.
  - Its command verbs and return codes match `developer-validation.json`.
- `python3 -B topics/padua-argmax-alln-20261101/code/part3/check_evidence.py`: rc 0, accepted, 458 files. Read-only: both receipt hashes were unchanged.

**Identity checks:**
- All 36 identity tuples (path, bytes, sha256, git_blob) are identical, in the same order, to `git show 6fae535:…/cold-storage.json`. Source is `1cecd68`, total 2,526,191 B.
- Every `git rev-parse 1cecd68:<path>` equals the recorded blob, with matching size and SHA-256.
- The set of files deleted between 1cecd68 and 6fae535 equals the set of manifest paths.

**Independent adversarial tests.** These are in [`review-support/claude-review-10/`](review-support/claude-review-10/): `adv.py` `c7df618b…`, `adv2.py` `4c552b96…`, `fault.py` `c313a5ea…`, `nt.py` `41f810b3…`. They run in the reviewer's own fixture repositories: 41 assertions, 40 pass. The one failure was a wrong expectation, not a tool defect (see the export-nesting item). The cases:
- **Restore followed by a foreign `git init` (+ `git add`) at the destination:** clean refuses and every file survives.
- **`.git` in other positions:**
  - nested `.git` inside a payload parent: clean refuses with no deletion;
  - a `.git` file at an ancestor: restore and export refuse;
  - `.git` symlinks (dangling, or pointing at the source): refused;
  - an empty `.git` directory: ignored.
- **Export nesting and receipts:**
  - re-export is idempotent, with byte-identical receipts;
  - export below a foreign repository is refused;
  - export into an untracked subdirectory of the repository is allowed, which is acceptable because no tracked file is touched;
  - a stale or differing receipt, or a tracked-but-absent receipt path, is refused before any payload is written;
  - a tampered exported file makes re-export refuse and `verify --dest` reject.
- **Destination type:**
  - a symlinked destination root or ancestor is refused, and nothing is written to the link target;
  - a FIFO destination is refused without hanging;
  - a destination inside `.git`, or inside a nested repository, is refused;
  - clean unlinks only the name of a hardlinked destination;
  - a linked-worktree source works.
- **Malformed manifests and forged sources (13 cases) are all refused:**
  - zero, tree or uppercase source commit;
  - wrong-path blob, or a symlink blob;
  - boolean bytes;
  - `..` or absolute paths;
  - case-only duplicates, file/directory prefix collision, wrong total;
  - unknown role, duplicate JSON key.
- **Fail-closed simulation** (`os.name='nt'` patched, or `O_NOFOLLOW` removed): verify, restore, clean and export exit 1 and create nothing. No native Windows run was made.

**Short independent regeneration.**
- Method: `git archive 1cecd68` was extracted to scratch, then `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B …/code/gated/d3_edge_generate.py --output out/c.json --ep-output out/ep.json` was run on it.
- Result: the E-P screen is 24,993 B, sha256 `3215523e1a768ce7e81c76283ac18bf476f8162bdcd84e579a7b93388707d14c`, byte-identical to the archived file. No long scans were run.

The condensed sub-review is in [`review-support/claude-review-10/storage-review-B.md`](review-support/claude-review-10/storage-review-B.md).

## Findings

- **S1 (MINOR) — the receipt overstates what export checked.**
  - `tools/cold_storage.py:463` sets `all_hashes_match_manifest: True` unconditionally. Newly written files (`:413`) are never read back.
  - `fault.py` shows the effect: corrupting a file right after its write still gives rc 0 and a receipt saying `true`.
  - `verify --dest` and a re-export do detect the corruption afterwards. The receipt is written last, so an interrupted export leaves no new receipt.
  - `COLD_STORAGE.md:169`'s "hash agreement" therefore describes source-to-manifest agreement, not destination agreement.
  - Required before delivery or purge reliance: read the destination back before writing a success receipt, or narrow the wording.
- **S2 (NOTE) — no way to verify an archive away from the repository.** No command verifies an exported archive against its receipt without the source Git objects, and `COLD_STORAGE.md:171` names none.
- **S3 (NOTE) — AC's destination is on native Windows.** The recorded destination is `C:\Users\andreyac\Downloads\padua\cold_storage\…`, where the tool fails closed. Delivery would need WSL/drvfs, which is untested. Concurrent writers to that folder would also conflict with the quiescent contract. Both limits are stated in the docs.
- **S4 (NOTE) — symlinks in `--dest`.** Any symlink anywhere in the absolute `--dest` path is refused. This is fail-closed, but it affects usability, for example with a symlinked home or `/tmp`.
- **S5 (NOTE) — stale receipts persist.** A matching receipt from an earlier complete export stays after its files are later deleted. It must not be read as proof that the files are present.
- **S6 (NOTE) — deliberate behaviour.** Verify accepts a destination containing a foreign `.git`. A historical row that is tracked but absent is reported as "still tracked" (`:374`).

All stated limits are honest and are not strengthened here:
- a quiescent destination and index;
- no protection against relocation, mount changes or edits to open files, nor against the stat-to-unlink race;
- partial writes may need manual removal, and there is no rollback;
- no native Windows support.

## Compatibility with PR #18

- **Verification.** Loaded from scratch with ROOT set to a worktree of `claude/cold-storage-20261102` at `1a9220c` and nothing written there, the repaired tool verifies all nine PR #18 manifests read-only. Export → `verify --dest` → clean to scratch passed for both mz-constants manifests.
- **Against PR #18's Codex audit:**
  - **F2 (collision preflight): satisfied.**
  - **F1 (destination readback, offline verification, no stale authorization): not satisfied.** S1, S2 and S5 apply.
- **Old harness.** PR #18's `audit-01/safety.py` is pinned to the old tool: it uses a fake source commit and patches `write_bytes`. Do not rerun it against the merged tool.
- **Integration.** Integration must keep these guards. Claude's PR #18 response adopts this repaired tool, adds the missing readback and offline verification, and then goes to a distinct Codex re-audit there. PR #17 then takes the audited tool when it merges main.

## Residual limits

Not tested: native Windows or WSL, AC's actual destination, adversarial concurrency, and the long A, D and T1 regenerations. Delivery to AC's cold storage is still PENDING.
