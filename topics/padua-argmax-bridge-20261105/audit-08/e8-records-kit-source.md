# E8 — records, public-kit source and delivered-ZIP static review (audit-08 focused)

Reviewer: Claude Opus 5.5, xhigh, independent auditor (subagent; read-only on repository). Model choice: adversarial soundness review of verifier code and records. Rules read at branch head `50070f520b3d5cfe9afbc75f10fdb1bc664b7b71` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md); `agents/` unchanged since d6dd673. No novelty content in scope, so the full IDEAS read is omitted.

T = topics/padua-argmax-bridge-20261105. Old package: audit7/zip-ro (15885d34). Delivered package: audit8/zip-ro (b341e6a1, ZIP hash verified by coordinator, not by me). Per coordinator instruction, NO numerical replay was run on the delivered ZIP; negative controls are integrity-path only plus a stubbed (non-numerical) polynomial comparison test. All results labelled "delivered ZIP" refer to disposable copies of that extraction.

## Verdict

No BLOCKING or MAJOR finding. The verify.py delta is sound for what it claims: strict JSON now covers expected-results, manifest population and payload identities are enforced independently of SHA256SUMS, stored polynomial receipts of all three formats are parsed and hash-bound during integrity, fresh replay compares counts, -O/-OO refused. Numerical cores unchanged. Delivered verify.py/README.txt/README.md/table TeX equal the Git sources byte-for-byte. Budget figures reproduce exactly. Findings are MINOR/NOTE/EDITORIAL on wording and records.

## Findings

**E8-01 MINOR — README overstates what is compared against the manifest, and the certificate-hash comparison adds no strength after integrity.**
`T/code/zenodo_public_20261114/README.txt:139-142` says the fresh receipt's "certificate SHA256 and bound/corner/split counts must equal the stored accepted record and input manifest". Evidence: MANIFEST `polynomial_inputs` rows carry only path/bytes/sha256/source (no counts); verify.py:149-150 compares only the stored certificate_sha256 with the manifest. The fresh `certificate_sha256` is `digest(args.certificate)` of the input file (`small_degree_unification/check.py:39`), the same file whose hash integrity already checked against the manifest (verify.py:90-92), so verify.py:164's hash comparison is implied by integrity; the substantive new check is the counts. Not a soundness defect: a certificate that differs from the shipped bytes fails integrity, and stored counts tampered with refreshed checksums are caught at replay (C7/C7b below). Fix: "its certificate SHA256 must equal the input manifest and the stored record, and its bound/corner/split counts must equal the stored record". Response-07's P7-05 row is accurate as written.

**E8-02 MINOR — the retained audit-07 dated correction in pr-update now refers to statements that are no longer above it.**
`T/pr-update-20261113.md:29` begins "Two statements above are inaccurate as worded" and quotes "Neither branch alone exceeds the cap" and the 16 KiB sentence. The response-07 rewrite (lines 1-25) removed both quoted sentences. The correction is retained, as audit-07 required, but read against the current text it now points at nothing. Fix: add a short dated prefix such as "(Applies to the text of this file at 9d3f5e0, since superseded.)".

**E8-03 MINOR — stale "current" in the deposit manifest template.**
`T/zenodo-deposit/MANIFEST.json.in:292` still says "current e861c752 59/152-page pair is separate", while the same file now sets `active_paired_source_commit` and `current_manuscript_revision.source_freeze` to `5f435be…` (diffed hunk at about lines 291-300). Fix: mark it as historical or update it to 5f435be.

**E8-04 NOTE — the path/provenance disclosure is accurate by category, but two items are only implicit.**
`README.txt:154-163` against `audit-07/p7-public.md:132-141` and a grep of the delivered package:
- `/home/ahomel/…` appears in 560 phase inputs only. Correct.
- `/workspace/padua_research/…` appears in 382 inputs, MANIFEST.json, analytic/receipt.json and polynomial receipts n37-40. Covered by "other records".
- `/opt/codex/runtimes/…` appears in receipts n37-40 only. Correct.
- Corner dependency process prose. Correct.

Two things are not named explicitly. (a) MANIFEST.json itself, the package's own control file, carries the absolute PDF source paths `/workspace/…/response07-*-20261114/padua-*-105928-Oslo.pdf`. "Records" arguably covers it. (b) The corner text also contains the agent path `/root/a1_develop` (line 170), and its filename contains "codex"; the README calls this "process prose", not a path. AC has decided the matter. This is optional, for completeness only.

**E8-05 EDITORIAL — "The audit" is unspecified in a public README.**
`README.txt:49-52`: "The audit also passed with Python 3.13.18 and NumPy 2.5.3 … Polynomial degree 33 used about 1.7 GB RAM in that audit". The figures are accurate: audit-07.md:12 and p7-public.md:163 record 1,717,840 KiB. But a ZIP reader has no audit to refer to. Suggest "An independent audit …". The independent supplementary smoke environment (Python 3.13.5/NumPy 2.2.4) is not mentioned. That is acceptable.

**E8-06 NOTE — the exactness of the committed staging body (E7-09) cannot be checked from Git.**
`T/code/regeneration_i25_20261114/stage_inputs_20261114.py` is 1,775 B with SHA256 `ef88f9f7…` (measured), matching response-07:43. `native-execution.md:21` says the executed heredoc body is retained off Git as `regeneration-20261114-direct-stage-*`. No Git record made before 687e9d4 gives that file's hash, and response-07/LOG do not say how byte equality with it was established. Fix: record the off-Git file's path/sha256 and the comparison command, for example in cold-storage.json or the I25 README.

**E8-07 NOTE — stored acceptance for degrees 17..32 rests on membership in `accepted_rows`.**
`verify.py:134-144`: for 2..16 the code also requires `actual_returncode == 0`, for 33..40 the three booleans, and for 17..32 nothing beyond the receipt-scope check (that format has no acceptance field). This is reasonable given the format. Recorded so nobody reads integrity as re-checking stored acceptance for 17..32.

**E8-08 EDITORIAL — README layout residue.**
`README.txt:121` is 93 characters, and eight other lines run 81-89. That is harmless in Markdown and only cosmetic in plain text. The `--analytic` path still prints analytic/check.py's JSON before the new single PASS line (verify.py:178-180), and the README does not mention this. Optional.

## Response-07 dispositions (accurate / overclaimed / missing)

| ID | Assessment |
|---|---|
| P7-01/E7-01/M7-01 | Accurate. The data statement text checked is paper/main.tex:85-92; companion/main.tex:92-99 is the same text. The kit contents it lists match the delivered package. Full TeX review is outside E8. |
| P7-02 | Accurate. The disclosure is present and correct by category (E8-04). |
| P7-03 | Accurate (README:112-118). |
| P7-04 | Accurate. Duplicate key, NaN and 1e999 rejected (C1-C3). Large ints are not "overflow". Python would reject >4300-digit ints anyway. |
| P7-05 | Accurate. Counts are compared (C7b, C7d). The hash part is tautological (E8-01). |
| P7-06 | Accurate. |
| P7-07 | Accurate. The None branch is confirmed in the delivered expected-results: 512 rows with "None", exactly for n=256..511. Numeric for 41..255. |
| P7-08 | Accurate (design note). |
| P7-09 | Accurate (C4, C5). |
| P7-10 | Accepted from the receipt and supplementary review. I did not inspect ZIP member modes, because I had only the extraction. build.py now sets 0o100644. |
| P7-11 | Accurate, with residue (E8-08). |
| M7-02..M7-10 | Spot-checked only. M7-03: the `--built-labels` option exists (check_correspondence.py:159-166). M7-07: the "no DOI has been assigned" wording is present. The others were not independently read (TeX outside E8). |
| E7-02/E7-03 | Accurate. pr-update:25 and LOG now state main / incremental share / whole tree. All files added since 9d3f5e0 are under 16 KiB. The dangling correction is E8-02. |
| E7-04/E7-05 | Corrections retained. The stale note is E8-03. |
| E7-06 | Accurate (regeneration-20261114.md addendum retained). |
| E7-07 | Accurate ("maximum pass RSS", regeneration-20261114.md tail). |
| E7-08 | Accurate. The named commits are real and their dates and contents are consistent: b918c1d 00:09, 4ed88e9 00:14 touching both preregistrations, 164a04c 00:31 touching the I25 preregistration. |
| E7-09 | File committed. Exactness is not verifiable from Git (E8-06). |
| E7-10, E7-12, E7-13 | Accurate (no new claims). |
| E7-11 | Accurate. The J03 diff (+9 lines) is a dated clarification only. No claim, status, result name or value changed. |

## Static source checks

- `git diff 9d3f5e0 HEAD` over the numerical code (independent_phase_checker, onset512_analytic, small_degree_unification, regeneration_20261114, evidence) is empty. The only code change in regeneration_i25_20261114 is the new staging file. The non-.md/.tex changes are limited to the zenodo_public adapter (4 files), the build.sh and check_correspondence.py tooling, and JSON records.
- `git diff dce3260 HEAD -- T/code` is empty.
- HEAD hashes match the MANIFEST and receipt:
  - verify.py `92319b64…` = MANIFEST public_adapter_sha256 = receipt
  - build.py `fabac559…` = MANIFEST builder_sha256
  - README.txt `93afed79…` = MANIFEST payload row
- The delivered package matches Git (delivered ZIP):
  - verify.py, README.txt and README.md are each byte-equal to HEAD verify.py/README.txt.
  - analytic/tables/{paper,companion}.tex are byte-equal to HEAD and to 5f435be `*/sections/comparison-unified.tex`.
  - The PDF hashes equal the receipt (d51627f5…, 9de87206…).
  - 1,019 files, 10,229,741 bytes. Exactly the nine stated members differ from the old extraction.
  - MANIFEST: manuscript_source_freeze 5f435be, public_adapter_source_commit dce3260, payload 1,017 rows; SHA256SUMS has 1,018 lines.
- build.py validates the PDF identities (full SHA, absolute path, exact bytes and hash) before creating output and never overwrites. Reading of smoke.py: no defects. The receipt records `cleanup=false` and a 2 GiB AS cap.

## Negative controls (delivered ZIP, disposable copies)

Script: `…/scratchpad/audit8/e8/controls.py`. Copies are in `…/audit8/e8/work/`. Each run refreshes MANIFEST payload and SHA256SUMS except where noted. Integrity was run with `python3 -E -B verify.py` (no numerical flags).

| Control | Result |
|---|---|
| C0 unmodified copy | rc 0, PASS |
| C0b refresh-only (refresh is a no-op) | rc 0, PASS |
| C1 duplicate key in expected-results line 1 | rc 1 `duplicate JSON key` |
| C2 NaN in expected-results | rc 1 `ValueError: NaN` |
| C3 1e999 in expected-results | rc 1 `nonfinite JSON number` |
| C4 extra file added to SHA256SUMS only | rc 1 `manifest payload population differs` |
| C5 README.txt manifest payload sha zeroed, SHA256SUMS refreshed | rc 1 `manifest payload identity README.txt` |
| C6 stored n33 certificate_sha256 tampered | rc 1 `stored polynomial certificate identity` |
| C7 n2 stored bound_leaves +1, everything refreshed | integrity rc 0 PASS (as designed; caught only at replay) |
| C7b `polynomial([2])` with subprocess stubbed to emit the true stored counts, vs tampered copy | REJECT `polynomial stored result mismatch 2` |
| C7c same stub vs unmodified copy | PASS |
| C7d stub with an extra `counts` key | REJECT (exact dict equality) |
| C8 `python3 -O` / `-OO` | rc 1 `Python optimization is not permitted` (both) |

C7b-C7d test only the comparison logic. No kernel was compiled and no certificate was checked.

## Budget (reproduced; counting rule of T/audit-02/code/t2/size.py as cited in audit-07 E7 §6, using `git ls-tree -rl`)

- main 99a9b1d = **9,787,481**; HEAD = **11,848,485**; topic share (all under T/, no main path changed/removed) = **2,061,004**
- +2,087 exception = **11,850,572**; +20,191 inherited no-shrink allowance (not re-derived) = **11,870,763** vs 10,000,000. All equal the records.
- Positive deltas 9d3f5e0→HEAD = 6,537 B: zenodo-public-response07-delivery.json 4,202 new; README.txt +2,249; cold-storage.json +62; MANIFEST.json.in +13; COLD_STORAGE.md +11.
- Files added since 9d3f5e0, all types: stage_inputs 1,775; delivery.json 4,202; handoff 39 4,739; response-07 8,427; supplementary review 14,298. **None is over 16 KiB.** COLD_STORAGE.md (16,075) and MANIFEST.json.in (16,056) are modified, not added, and remain under 16,384.

## Commands (exit status)

1. `git rev-parse HEAD; git status --short; git log 9d3f5e0..HEAD; git diff --stat; wc -l` — 0
2. `cat CLAUDE_ROLES.md; grep WORKFLOW.md` — 0
3. `cat response-07.md` — 0
4. `git diff 9d3f5e0 HEAD -- T/code/` — 0
5. `git show HEAD:…/verify.py | cat -n` — 0
6. python3 -E -B inspection of the old MANIFEST/receipts; grep check.py — 0
7. `git diff --stat` over the core dirs; name-only; record diffs (J03, preregistrations, regeneration, COLD_STORAGE, cold-storage.json) — 0
8. staging file wc/sha256; `git log -1`/`show --stat` for 4ed88e9/164a04c/b918c1d; grep — 0
9. grep of audit-07 E7-09/P7-02 — 0
10. grep for path patterns in the old package — 0
11. grep for codex/claude mentions — 0
12. `cat zenodo-public-response07-delivery.json` — 0
13. sha256 of the adapter at HEAD/dce3260; `git diff --stat dce3260 HEAD -- T/code` (empty); python/numpy/g++ versions; grep — 0
14. cmp of the delivered members against HEAD sources; PDF sha256; file count and bytes; member diff against the old package — 0
15. delivered MANIFEST inspection — 0
16. `ulimit -v 4000000; timeout 1200 python3 -E -B e8/controls.py <delivered> e8/work` — **1**. C0-C7d completed as tabulated. The final C8 step crashed because of my own global subprocess monkeypatch, a script bug and not a verifier result. It was rerun separately in 17.
17. `python3 -O -E -B work/c0/verify.py`, `python3 -OO …` — 1 each (expected refusal)
18. `git diff` pr-update, zenodo-deposit, handoff 38 — 0
19. `sed` pr-update tail; grep; `git log d6dd673..HEAD -- agents AGENTS.md` (empty) — 0
20. grep/sed of audit-07 E7-02/E7-03, size.py — 0
21. `python3 -E -B e8/size.py 99a9b1d HEAD | head` — totals printed, then BrokenPipe from head; reported rc 0. `size.py 9d3f5e0 HEAD`, and an inline recount of the topic share — 0.
22. `git cat-file -s` for the added files — 0
23. `cat` of the supplementary review; LOG diff; handoff 39; paper data statement — 0
24. corner_gap census of the delivered expected-results — 0

Environment: Python 3.13.18, NumPy 2.5.3, g++ 13.3.0.

## Limits

- No numerical replay of the delivered ZIP (left to P8 by coordinator). The README quick/full commands were not run by me.
- ZIP-level properties were not checked by me: member modes, ZIP sha, testzip. I had only the extraction.
- Manuscript TeX beyond the data-statement spot check, the rendered PDFs and the M7 items were not reviewed. The 13-scenario harness and build were not rerun.
- E7-09 exactness and the off-Git preservation/cold storage are unverifiable here.
- The 20,191 no-shrink allowance is inherited, not re-derived.
- I made no repository writes. Off-Git outputs are only under `…/scratchpad/audit8/e8/` and this report.
