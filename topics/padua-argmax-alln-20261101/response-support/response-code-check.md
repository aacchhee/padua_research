# Supplementary response packaging review

2026-11-02. Reviewer: separate Codex agent `/root/cold_storage_audit`, configured/requested `gpt-6-astra` high; serving model/effort metadata not independently exposed. Rules read at `b8fbb5c5be374bf658d2970681c7cac0fb40d737`. This reviews the parent's response packaging code, independently of the frozen Claude cold-storage implementation and audit-02 findings. It supplements, and does not replace, the required Claude protocol review. No mathematical acceptance or claim status changes.

**Result: executed reconstruction/analyzer and historical archive verification PASS.** No material defect found in the reviewed response behavior. Full current-manifest plain check awaits the orchestrator's final refresh; its result must be recorded at that output boundary. This report does not claim that pending execution passed.

## Reviewed source hashes

| Response source under `code/part3/` | SHA-256 |
|---|---|
| `reconstruct_t1.py` | `21199f3806d2cbdb117bcf77d5d48c368fed79f977cf4cfdf90f5f8adae7fb5d` |
| `tests_analyze.py` | `d6952eae3948505d80c2e3539dda38a7c377b895799c57f681c4e9bb776b7b05` |
| `check_evidence.py` (final schema guards) | `797506c7edbdc648ca9c4bddc32f9c8fa1779b9bb16e1c23dd401171770aed71` |

Execution hashes were recorded before execution and confirmed unchanged afterward. The integrity checker was then changed only to add active-format and duplicate-row guards; that final diff was inspected and its updated hash is listed above. The earlier eight archive controls executed checker hash `a4c804bb3ab852a09e0c49a19c3fcf5ead4fbfdb24134b87c487b1f9a9963170`; their archive-verification code is unchanged. No developer source, frozen audit-02 artifact, historical support file or Git state was modified. Only this review and [its compact receipt](response-code-check.json) were written in the repository. Temporary runner files and large outputs remained in `/tmp`.

## Reconstruction and analysis actually executed

From `/workspace/padua-response-20261102`, Python 3.12.14:

```text
python -B topics/padua-argmax-alln-20261101/code/part3/reconstruct_t1.py --output /tmp/padua-response-code-oh66rch6/tests_T1.json
git show 1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7:topics/padua-argmax-alln-20261101/outputs/part3/tests_T2.json
git show 1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7:topics/padua-argmax-alln-20261101/outputs/part3/tests_T3.json
git show 1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7:topics/padua-argmax-alln-20261101/outputs/part3/tests_T4.json
git show 1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7:topics/padua-argmax-alln-20261101/outputs/part3/tests_summary.json
python -B topics/padua-argmax-alln-20261101/code/part3/tests_analyze.py /tmp/padua-response-code-oh66rch6
```

The Python harness wrote each `git show` result to the corresponding scratch path; the old summary was named `archived_tests_summary.json`. It recursively compared the entire parsed summaries, checked input SHA-256 values before/after and checked that no per-degree split files appeared. Both scripts exited zero.

- Reconstruction reads the pinned historical source paths, checks available cold-storage SHA-256/size identities, matches each short profile against the corresponding full split profile, restores original profile order, rejects duplicate/mismatched/unused profiles, removes only the postprocessor-added comparison field, and serializes with the producer's indent/no-final-newline convention.
- Result: one complete **1,342,719-byte** artifact, SHA-256 **`bfb0acd697bfe8530a9b8441130c400f1a3601342277ab0a0c77d2cfd6cfcb90`**. This preserves developer timing bytes; it is not claimed byte-identical to the separate audit replay `4d7792e6…`.
- The analyzer retains the previous fit, selection, threshold and interpretation calculations. It reads complete profile cells directly instead of splitting/reloading them. It writes only its output summary, preserving the raw T1/T2/T3/T4 input bytes.
- Comparison: **978 leaves total; 977 exactly equal; one intended metadata difference** at `/T1/minimum_noncorner_cell/cell_evidence`: `tests_T1_n399.json` → `tests_T1.json`. No numerical tolerance, rounding exclusion or scientific difference was used. The first harness assertion incorrectly expected the old filename to end in n400; inspection corrected that harness expectation to the actual archived n399 value, after which the complete comparison passed.
- A repeat reconstruction to the identical destination succeeded without changing bytes. A different existing destination was refused with nonzero exit and preserved byte-exactly.
- No fresh T1 measurement, larger-degree scan or mathematical checker run was performed. The large reconstructed artifact and 53-KiB summary stay in scratch storage.

## Integrity checker review and controls

`verify_archives()` was invoked directly from the exact hashed module, without changing repository paths or refreshing the active integrity manifest. It verified all **36 historical objects / 2,526,191 bytes** through source-commit/path → blob identity and blob SHA-256/size; it checked the total, unique entry paths, topic containment and absence of restored historical files. This independently avoids the unsafe Claude restore/clean/export operations identified in audit-02.

Eight in-memory malformed-manifest controls were each rejected by explicit `ValueError`: duplicate path, parent traversal, absolute path, another topic's path, wrong blob ID, wrong SHA-256, wrong byte size and wrong aggregate total. The control harness replaced only the module's manifest-loading function with deep-copied data; the Git object reads and checks remained the reviewed implementation. No manifest or Git object was mutated.

Code inspection of `run()` establishes these intended checks, still subject to the pending full invocation:

- The current file inventory and historical archive inventory are checked separately. The historical `evidence-manifest.json` blob is preserved at its old source commit while the same working pathname holds the explicitly excepted current integrity manifest. All other archived files must remain absent.
- Active-file path-set equality is checked against discovered topic files plus this topic's results and the storage tool; handoffs, archived paths, the active manifest and packaging receipt are explicitly excluded. Each inventoried file's size and hash are checked.
- Generated files must be strictly below 16,384 bytes, except the cold manifest and the one active integrity manifest. The generated total is checked below 5 MB. Source/handwritten-record extensions retain the existing explicit policy classification.
- JSON developer outputs and current response receipts are parsed; frozen `audit-support` files are instead hashed as opaque bytes because some old `.json` files contain concatenated stdout. This is disclosed, not mistaken for JSON validation.
- Compressed finite certificates must be complete with no pending leaves; named finite checker receipts must retain accepted/complete/verified flags; minimum evidence counts are enforced. These are integrity checks, not fresh verification of mathematical predicates.
- Plain `run(False)` performs no filesystem writes. `--refresh` and explicit `--output` are the only writing modes. The old automatic rewrite of packaging-validation is removed.

**Advisory resolved by the response developer:** the final checker explicitly requires active format `padua-argmax-current-and-cold-evidence-v3` and checks the inventory row count against the expected path count before exact set equality. Together these reject duplicate current rows and an unsupported schema version. I inspected the narrow guard addition; no archive-verification or scientific predicate changed. The parent owns fresh CLI negative controls and records their executions separately; this reviewer does not claim to have executed those controls. Archive-row uniqueness was already enforced and was tested here.

Filesystem limits: reconstruction safely refuses differing ordinary destinations, but it does not establish a general symlink-resistant output sandbox; the user chooses its output path and this audit used a fresh scratch directory. No concurrent filesystem race or Windows behavior was tested. The checker trusts the local repository object database and declared input manifests. This does not resolve the separate cold-tool symlink findings.

## Boundary still required

After the orchestrator stops editing covered files and refreshes the active manifest, run the **plain** `check_evidence.py` and record its output/hash at the response boundary. Adding that result to a covered report/receipt requires a subsequent refresh by the orchestrator. No `--refresh` was run by this reviewer.
