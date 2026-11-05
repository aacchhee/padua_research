# T1 sub-audit: evidence/protocol layer (padua-lebesgue-followups-20261103)

Sub-auditor: Claude Opus 5.5 (high). Clone `/home/claude/padua_research`, HEAD `407fe83`, audited dev SHA `5b2e367`, base `440d107`. Read-only: `git status --porcelain` was empty at the end, and HEAD stayed `407fe83`. Scratch files are only under `/home/claude/audit/subreports/t1work/`. No long computation was run. The longest step was the canonical-hash recompute, about 1 minute.

T = `topics/padua-lebesgue-followups-20261103`. `git diff 5b2e367 407fe83` touches only LOG.md and the handoffs, so the evidence, theory and code at HEAD equal those at 5b2e367.

## Verdict

Every check in scope came out consistent with the claims, apart from the items below. There is no BLOCKER.

- All 7 guard-only deltas verify byte-for-byte and by AST against their Git blobs.
- No executed source identity was relabeled.
- Both compositions bind the stated raw and receipt SHAs.
- All three comparison receipts reproduce their canonical SHAs from the committed receipts.
- No excluded field is read by the frozen checker.
- Native code appears in no acceptance receipt.
- Every interrupted or capped run I found is recorded as a non-pass.

There is one MAJOR item, a retention gap that the prose discloses honestly, plus four MINOR items and a few NOTEs.

## Findings

### F1. MAJOR: the PD-T180 boundary proof input is not retrievable outside the developer sandbox
- Where: T/COLD_STORAGE.md:13,18,73-76; T/theory/t1-closed-count.md:110; T/independent-checks-t1.md:225.
- Evidence: the fresh boundary artifact (`adfe1107…`, 4,822,048 B) is the only input that both boundary replays checked. It exists only at `/workspace/scratch/lebesgue-t1/…`, and that directory does not exist in this environment (`ls /workspace` gives "No such file or directory"). The fresh interior (`c5cdcfed…`) and the join (`033e8516…`) are also scratch-only.
  - The interior is covered: its proof payload is typed-identical to the archive, which is retrievable from Git (see F-ok-4).
  - The boundary has no durable copy. Regenerating it gives a new raw SHA, which by COLD_STORAGE.md:65-67 needs new replays.
- The prose is honest about this: delivery is marked "pending", the sandbox has "no promised retention", and no export is claimed. So this is a retention gap, not a misstatement. Still, the PROVED status of PD-T180's boundary stratum currently rests on receipts whose input cannot be retrieved for audit.
- Minimal fix:
  1. Deliver `adfe…`, and preferably `c5cd…`/`033e…` too, to AC cold storage with a manifest entry.
  2. If that is impossible, keep the claim conditional on the orchestrator's independent regeneration and replay, and record that dependency explicitly.

### F2. MINOR: the AST identity hashes depend on the CPython version, and a 3.13 rerun of the composition contract fails
- Where: `boundary_method_ast_sha256` in t1-boundary-check.json and t1-independent-boundary-check.json; `original_summary_ast_sha256` in both final compositions; `frozen_boundary_ast()` in T/code/t1_check_boundary.py:15-21; T/code/t1_compose.py:86.
- Evidence: `ast.dump` output changes between Python versions.
  - Python 3.12.3 gives boundaries `73fc0216…` and summary `61812bc0…`, matching the receipts.
  - Python 3.13.18 gives `aad6c3e2…` and `658c7fff…`.
  - Running `t1_compose.boundary_receipt` under 3.13 raised `Rejected: boundary method AST identity`. This is a reproducibility issue, not a correctness one.
- Minimal fix: in COLD_STORAGE.md and in handoff 02, state that the AST identities are valid only on CPython 3.12.x, and that reruns must use 3.12.

### F3. MINOR: the developer's interrupted corner cross-validation is said to have a "receipt preserved", but no such receipt exists
- Where: T/attempts/T1.md:39 ("actual exit130, incomplete n7, receipt preserved").
- Evidence: no developer `t1-corner-crossvalidation*` file appears in T/evidence at any commit in 440d107..5b2e367. Only `t1-independent-corner-crossvalidation-interrupted.json` exists, and it records exit 143. The run is correctly not claimed as a pass, but its receipt locator is missing.
- Minimal fix: give the scratch path and SHA of that receipt, or change the wording to "logs in scratch; no committed receipt".

### F4. MINOR: the join receipt does not itself carry the 7753 producer binding, exit code or timestamp
- Where: T/evidence/t1-fresh-join.json (keys: base_joiner, boundary/interior/output SHA, counts, joiner_sha256 `a88b…`); T/attempts/T1.md:129 says "generation/join receipts remain bound to old7753".
- Evidence:
  - The binding to `7753e4ba…` exists directly only in t1-boundary-generation.json:`source_sha256`.
  - For the join it exists only indirectly: `t1_join.py:24` asserts it at join time, and the composition (`t1_compose.py:120`) checks it against the scratch-only joined metadata.
  - Exit 0 and session 34437 are recorded only in the prose.
  - Nothing was relabeled. At join-era commits d5e937a and bb05df2, `t1_boundary.py` was still blob `011b8c41` (= 7753).
- Minimal fix: soften the T1.md:129 wording, or add an addendum receipt that records `boundary_source_sha256=7753…`, the exit code and the session for the join.

### F5. MINOR: the "about 4.21 MB" whole-repo generated-data figure does not reproduce, and the method is unstated
- Where: T/LOG.md:103.
- Method: I listed every blob in `git ls-tree -r -l` at 5b2e367 and excluded the `tools/cold_storage.py` RECORD_EXT extensions (md, py, sh, tex, bib, svg, gitignore).

| Variant | Bytes | MB | MiB |
|---|---:|---:|---:|
| All non-record files, at 5b2e367 (same at 407fe83) | 4,574,085 | 4.57 | 4.36 |
| Same, at base 440d107 | 4,332,217 | 4.33 | — |
| Excluding `cold-storage*` files | 4,368,255 | 4.37 | 4.17 |
| Excluding every `*manifest*` file | 4,188,770 | 4.19 | — |

- At 5b2e367 the topic's own non-record files total 241,868 B, which is the growth over base.
- No variant I tried gives 4.21 MB. The LOG's own phrase "including existing manifests" points to 4.57 MB.
- The total is under WORKFLOW.md:107's "well below 5 MB" in every variant, but 4.57 MB is close to the limit.
- Committed evidence: no file in T/evidence exceeds 16 KiB (largest 12,709 B; evidence total 259,620 B). The only topic files above 16 KiB are md records: LOG, T1.md, independent-checks-t1.md, and two preparation proposals.
- Minimal fix: replace "about 4.21 MB" with an exact byte count and the classification used.

### NOTEs
- N1. The developer interior replay receipt has no `python_optimize_flag` field; the boundary receipts record 0, and the independent run used an environment probe. Impact is nil, for two reasons:
  - `grep -c "assert "` gives 0 in a5_checker_n8.py, a5_checker_n8_staged.py, a5_checker_n8_staged_cached.py and t1_check_boundary.py. All predicates use `require()`.
  - The asserts in old t1_check.py (blob 59ebc4f, lines 25-28) are post-run integrity guards only.
- N2. COLD_STORAGE.md:19 begins with a space directly after the table, with no blank line, so GFM renders "Progress logs…" as a table row. Cosmetic.
- N3. The per-edge pattern split 107/107/155/123 (independent-checks-t1.md:123) has no receipt field. The receipts carry only the total, 492. 107/107/155 is corroborated by T1.md:59, but 123 is prose-only. The arithmetic is correct.
- N4. Typed-identity exclusions and the frozen checker:
  - Present exclusions: `metadata` and `summary.seconds`. Allowed but absent: `summary.Pcache` and `boundary_summary.seconds`.
  - a5_checker_n8.py never reads any of these. Its only `seconds` (line 1311) is written to its own output. `summary` is read only by specific keys (lines 1143-1166) and `boundary_summary` only by complete/unresolved/edge/corner/counts (1167-1172). No `metadata` or `Pcache` appears anywhere.
  - The staged validator (a5_checker_n8_staged.py:74,89-93) does read `metadata`, but structurally and on raw inputs, not inside `Verifier.run`.
- N5. The fresh-reflection receipt has no elapsed time, and T1.md:115 says so explicitly.
- N6. The ordinary-reflection gate registration was first committed at bb05df2 (13:11:40Z), before V5 was recorded (13:13:41Z) and before the reflection (13:20:09Z). The native-continuation registration was committed at 66eaf85 (12:25:36Z), about 80 s after the V3 cap receipt (12:24:17Z). The V4 launch time is not recorded, so I could not check strictly that the registration came first. The final commit (13:28:41Z) is inside the 17:15Z ceiling.

## Positive checks (actually executed)

- F-ok-1, guard deltas, all 7 pass. Script: `t1work/guard_check.py`. For each entry point:
  1. `git cat-file blob <old blob>` and SHA-256 equals the recorded old executed SHA; byte count matches where one was recorded.
  2. The current file at 5b2e367 (identical at HEAD) has the recorded new SHA.
  3. The unified diff has 0 removed lines and exactly 2 added lines (`if not __debug__:` / `raise RuntimeError(...)`), placed before the first import.
  4. Removing that block restores the old bytes exactly.
  5. `ast.dump` with the guard `If` removed equals the old AST.

| File | Blob | Old SHA | New SHA |
|---|---|---|---|
| t1_check | 59ebc4f | 0345e62e | 13fdfa85 |
| t1_produce | cd78c69 | 1ac5cbb8 | b52cdec4 |
| t1_memo | 90a84a6 | d910cb58 | 0e433e08 |
| t1_memo_controls | f26724d | e5c146fd | ac4c1364 |
| t1_corner_certificate_controls | 6e7d5cb | cf237404 | 9b0f7d4b |
| t1_corner_crossvalidate | c3f4288 | 291ce1a3 | f1a9c73f |
| t1_boundary | 011b8c4 (4622 B) | 7753e4ba | a70e2532 |

  - The blobs exist at the stated commits: 05cca84 for the six legacy files and f346d99 for t1_boundary, which is also present at 05cca84, d5e937a and bb05df2.
  - Running all 14 `-O`/`-OO` invocations gave rc=1 with the expected RuntimeError, before any import.
  - The receipts' `development_delta_sha256` values match the delta files (2f90a0de…, 5fd46ae9…), and the control-script SHAs match the committed .py files.
- F-ok-2, no relabeling:
  - t1-boundary-generation.json `source_sha256` = 7753…
  - Both compositions bind interior driver 0345… (`execution_driver_source_sha256.interior`, `used_source_sha256[…/executed-sources/t1_check.py]`).
  - Pre-guard and guarded control receipts (wrapper, memo) carry their own respective driver SHAs (0345/13fd, d910/0e43).
  - The only evidence files containing a70e or 13fd are the guard deltas, the guard controls and the guarded wrapper receipt.
- F-ok-3, compositions:
  - The two receipts differ only in `inputs.archived_interior.path` (sorted `json.tool` diff).
  - Both bind archived a3b4f278… (637,163 B), fresh c5cdcfed… (637,165 B), boundary adfe1107… (4,822,048 B) and joined 033e8516… (1,696,013 B), plus replay receipts b009c46a/3971aee0 (12,709 B) and d274ab0f/bfe1d5cb (11,413 B), all as COLD_STORAGE.md states. `sha256sum` of the four committed replay receipts matches.
  - Using the committed t1_compose contract functions on the archive restored from the Git blob, I recomputed:
    - interior facts SHA `020deb8c…`, identical for both receipts (= t1-archived-interior-comparison and t1-independent-actual-interior-comparison);
    - boundary facts SHA `f4f1e990…`, identical (= t1-independent-actual-boundary-comparison). This needed the 3.12 AST value injected, see F2;
    - composition retained-facts SHA `075741b1…`, identical (= t1-independent-final-composition-comparison);
    - composition receipt SHAs 171f2a67… (5014 B) and 044c67d8… (5017 B), matching the comparison file;
    - archive proof payload 18,969,878 B, SHA `e22a9b55…`, excluded fields [metadata, summary.seconds], excluded-SHA `aed95ef8…`, matching both identity receipts and both compositions.
  - The paired replay receipts differ only in `seconds`.
- F-ok-4, archive: blob 3f65a77d is 637,163 B with sha256 a3b4f278…, sits at `outputs/a5_n8_interior_candidate.json.gz` in commit 2b52b432, which is an ancestor of HEAD and contained in `origin/codex/padua-lebesgue-followups-20261103`. The COLD_STORAGE.md source-locator table is correct: the native_produce, join and reflect blobs/SHAs verified at 1b7ebd8, 05cca84 and 440d107.
- F-ok-5, native code: the acceptance receipts have `runtime_evaluate_backend = "frozen bit-identical cached monomials…"`. The only "native" key in them is `native_tensor_inverse_verified`, a field-embedding property. No native file appears in the compositions' `used_source_sha256`. The native producer is used only in V4/V5 (proposal phases). The live jobs did not import any of the six files guarded at 5b23fce (12:35Z): t1_native_produce imports t1_native, and t1_check_boundary imports staged_cached.
- F-ok-6, operational history. All of the following are recorded as non-pass:
  - baseline SIGINT, exit 130, `artifact_present:false`;
  - independent cross-validation, exit 143, `all_degrees_completed:false`;
  - V3 cap (`complete:false`, 9 pending) and V4 cap (8 pending);
  - V5 (only "1" pending);
  - the memo-harness IndexError, initial native scale refusal and native-check serialization failure, all disclosed in prose with no receipt claimed;
  - the unused resume option (`numerical_resume_executed:false`).
  Every scoped receipt keeps `count_certified:false`. The developer cross-validation receipt is missing (F3).
- F-ok-7, prose against receipts: every number I checked matches.
  - Interior: 153520 / 541882 / 44 / 45 / 3474 / 346; dispositions 144902 / 534358 / 7002 / 522; 102103370982 mask occurrences; 2933.331170984 s and 2759.540105958 s.
  - Boundary: 492 / 16 / 32 / 2; dispositions 27142 / 1472 / 4454 / 1404 / 16; corners (-1,-1) and (1,-1); 1973.479216484 s and 1711.843283739 s; 4 edge roots per side.
  - Fresh phases: V3 3600.418962 s / 71190 / 35591 / 10 / 9; V4 2401.142279 s / 145085 / 72539 / 8; V5 420.532652 s / 153520 / 76760 / 270941 / 24; boundary generation 3242.357562 s.
  - Controls: 4926; 26.65 s; 6.66/2.40 s; 37 controls (30 rejected), 98.03 s; 41172 = 5208+7392+11742+16830; 5310 = 558+774+1026+1314+1638; 69.76 s; 10/28/31/13/24/7/6/3; 3120; 19; 3379; 10000×2; 23 refs; 3594.
  - Speedups: 1.89/2.59/2.76/2.85; 1.48/1.97/1.38/1.10; 0.98/1.16/1.19/1.20; 1.219; 1.189.
  - Theory-file SHAs 6ae38bcf / 9b8a9911 / 3953b70e match independent-checks-t1.md:218.
- F-ok-8, results file: results/padua-lebesgue-followups-20261103.md matches report.md (T1 PROVED 44/16/2 = 62; T2–T4 PROVED with supplementary check; Claude audit pending; stage AUDIT; delivery pending).

## Commands run (exit code; key output)
1. `git rev-parse HEAD; git status --short; ls` T dirs: 0; 407fe83, clean.
2. Read independent-checks-t1.md, gate-t1.md, COLD_STORAGE.md, ALLOCATIONS.md, attempts/T1.md, t1-native-notes.md, theory/t1-*.md, report.md, results/…md, LOG.md:95-105, handoffs/02-audit.md:105-114, code/t1_compose.py, code/t1_payload.py, relevant parts of a5_checker_n8.py and a5_checker_n8_staged.py, and tools/cold_storage.py:60-66,350-367 (exit 0).
3. `python3 -B t1work/guard_check.py`: 0; ALL_OK True.
4. `git ls-tree <commit> <path>` for the 7 blobs: 0; all present.
5. 14× `python3 {-O,-OO} -B code/<f>.py --help`: each rc=1, RuntimeError.
6. `json.tool` dumps of the guard, generation, join, payload, composition, comparison, cap, interrupt and reflection receipts: 0.
7. `diff` of the sorted composition receipts: 1; only the archived path differs. `diff` of the paired replay receipts: 1; only `seconds` differs.
8. `sha256sum` of the 6 replay/composition receipts and of code/*.py: 0; all match.
9. `grep` in a5_checker_n8*.py for metadata/seconds/Pcache/summary: 0 (see N4).
10. `git cat-file -t/-s blob 3f65a77d | sha256sum`; `git ls-tree 2b52b432`; `merge-base --is-ancestor`: all 0; a3b4f278…, ancestor confirmed.
11. `PYTHONPATH=/home/claude/audit/deps python3 -B t1work/recompute.py`: 1, Rejected at boundary AST under 3.13 (F2). `python3.12 -I -B t1work/asthash.py`: 0; 73fc…/61812bc…. `python3.13 …asthash.py`: 0; aad6…/658c…. `recompute2.py` (3.12 AST value injected): 0; all SHAs reproduced.
12. `git rev-list 440d107..5b2e367` scans for crossvalidation receipts: 0; independent receipt only.
13. `python3 -I -B t1work/bucket.py` (440d107, 5b2e367, 407fe83) plus variant script: 0; values as in F5.
14. `git ls-tree -r -l 5b2e367 -- T` for files >16 KiB: 0; 5 md files, no evidence file.
15. `git log --format='%h %cI'` over the range, and gate-registration presence per commit: 0 (see N6).
16. `ls /workspace`: 2; absent (F1).

## Could not check
- Scratch artifacts: the fresh interior/boundary/joined data, the executed-source copies, logs, and the developer cross-validation receipt.
- Actual exit codes, sessions and distinct-agent execution, beyond what the receipts and prose say.
- Exact wall-clock order of the V4 launch relative to its registration.
- Whether the PYTHONOPTIMIZE environment variable was unset for the developer interior run.
