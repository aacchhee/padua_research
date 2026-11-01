# Response-01, group E1 (Claude Sonnet 5.5, high): E1-F1..F9, P-F6, P-F8, E1 parts of P-F3/P-F7

All paths relative to the repo root `/home/claude/padua_research`. T = `topics/padua-lanczos-drift-20261101`, TH = `tracks/bivariate-lanczos/theory`. No git state-changing command was run; no immutable file was touched; no producer was modified.

## (a) Dispositions

| ID | Disposition | Files and lines changed | Summary |
|---|---|---|---|
| E1-F1 | FIXED | new `tracks/bivariate-lanczos/code/drift/e1_response_checks.py`; new `T/evidence/response-01-e1-checks.json`; `TH/drift-codex-e1-04-...` lines 17-18 (disclosure), 100-104 (History); `T/directions/E1.md` 33 and 103-131; `T/ideas-e1.md` 19 | Ties detected exactly: T24 none (min margin 0.008426 at column (8,5), degrees 8..12); rotQ24 exact tie at (2,1) at every degree 2..12 (cause verified exactly: node set invariant under 90 degree rotation, b_(1,0)=x, b_(1,1)=y, both candidate products are the identical vector x∘y). rotQ24 pivot rows labelled "X-tie-broken frozen sequence"; e1-summary.md noted immutable without disclosure. Tie resolved to Y (my own exact producer run, 208 s): only column 4 (=(2,1)) differs; Knode² unchanged, KHS² +12.4%, Urow² +3.8%, matching the auditor. |
| E1-F2 | FIXED | record 04 lines 69 (Checks), 101-102 (History); E1.md annotations | Projector trace described as a consistency identity; new exact BᵀB = D check (plus exact recurrence identity at every node and tr P = N as consequence) at degree 12 for T24 bj/pivot/alt and rotQ24 bj/alt/pivot, all PASS. |
| E1-F3 | FIXED | record 04 line 71, History; JSON check c | Six inequalities, integer chain, factor-100 criterion, original KHS-only verdict (rotQ24 62.16 < 100) checked by Fraction arithmetic from the committed rationals: PASS. rotQ24 U_alt² < 6.42e8 headroom 1.985e-4 (0.02%) recorded. |
| E1-F4 | FIXED | record 04 line 57-59 ("preregistered" -> "frozen"; provenance paragraph) and History; record 02 line 91 (corrective History line); `E1.md` 54, 68, annotations table; `ideas-e1.md` 22; JSON check d | Disclosed: 6920ba6 already contains Urow under frozen_before_run (verified with git show, in JSON); `dead` edited in place at c89eb6a; only `dead` and `amendment_audit` differ between 6920ba6 and c89eb6a. Exact facts: original any-degree KHS DEAD never fires; sharpened-U clause 2 would fire at T24 degrees 2-4 and rotQ24 2-6 (clause 1 never). Per-field table in E1.md. Original sentences quoted. |
| E1-F5 | FIXED (status unchanged: MEASURED, per orchestrator decision) | record 05 lines 43, 51-52 (rationale), 69, 79, 87, 89-98 (new section), 100+ (snapshot note, History); `E2.md` 7, 9, 13; `ideas-e1.md` 74/75, 95-96 (renumbered after edits); E1.md 79 | Stale "pending" lines reconciled with originals quoted. Rationale stated; finite PROVED split flagged for re-audit, not done. Stale manifest/scalar-cgs2 snapshots annotated as immutable. plan.md text below. |
| P-F8 | FIXED | same as E1-F5 (ideas-e1 lines 95-96, record 05 :85) | Synchronised. |
| E1-F6 | FIXED (record 05 part); README text returned (below) | record 05 new "Regeneration path" section | e1_cgs2.py commands for both comparators (found in `e1-scalar-cgs2.json` `full_graph_upper_runs[*].command`); `input_sha256` lives in the `explicit_projection_check` block (from `e1_sign_check.py`) and hashes a temporary file. |
| E1-F7 | FIXED | `E1.md` annotations; `ideas-e1.md` 11, 13 | IDEA-087/088, LIT-114, LIT-255 added with titles quoted from IDEAS.md / INDEX.md and one-line separations. |
| P-F7 (E1 part) | FIXED | same | IDEA-087/088 for -01. (PD-T061/PD-N021/IDEA-161 and IDEA-086/116 are E5/E6 parts, not mine.) |
| P-F6 | FIXED | record 03 lines 53 and 71 (Depends on, Sources) + History; `ideas-e1.md` 67-68 (IDEA-04), 86 (IDEA-05); E1.md annotations | PD-T042/IDEA-141, PD-T043/IDEA-142-144, IDEA-139 added with separation: span-normal quotient vs Gram defect; formal l∞ operation graph vs Gaussian/dot64 models. Read in `first-order-coefficient-channel-gains-product-type.md` and `closed-loop-dot-product-rounding-carries-coefficient-channel.md`. Stated as predecessors, not dependencies, no priority claim, no claim that they are contradicted. |
| P-F3 (ideas-e1) | FIXED | `ideas-e1.md` 3 | "Relaxed ... per AC" dropped, original quoted, WORKFLOW-minimum sentence added. (ideas-e5:8 is not mine.) |
| E1-F8 | FIXED | record 03 lines 1, 4, History | Title no longer says "rounding map"; alias now "vector-operation amplitudes determine the first-order normal map in the formal relative-error model". Provisional ID kept. |
| E1-F9 | FIXED | record 01 line 29, History | "for s ≤ n". |

Also (not requested, consistent with the same audit): status lines of records 01, 02, 03, 04, 05 now say "Claude audit-01: CONFIRMED / CONFIRMED-WITH-CORRECTIONS, Codex re-audit pending" instead of "independent audit pending" (statuses unchanged); record 03 Checks/Open items updated for the audit's degree 3-4 trajectory replay.

## (b) Commands run

- `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e1_response_checks.py --skip-tie-break-bounds --output <scratch>/e1/test.json`: PASS, 29 s (trial run in scratchpad).
- Final single run: `... e1_response_checks.py --output topics/padua-lanczos-drift-20261101/evidence/response-01-e1-checks.json`: overall PASS, 239.5 s wall (208 s of it the rotQ24 degree-12 Y-tie bounds run), 76,613 bytes. Python 3.13.18, python-flint 0.9.0. code sha256 `6edcedabf21444ed8d84ce379c6396dac40dde179aac991e5299e68b7511c4dd`; producer e1_exact.py sha256 `19ce7b77...` equals the committed sweep rows; input e1-full-sweep.json sha256 `0d9c236f...` equals the manifest.
- Results: rebuilt pivot sequences equal the committed sweep `pivot_choices` at every degree 2..12 on both grids; BᵀB = D PASS for 6 cases; record-04 inequalities PASS; DEAD history as above; `git show` of freeze at 6920ba6 and c89eb6a PASS (blob sha256 in JSON).
- Read-only: `git show 6920ba6:...e1-freeze.json`, `git diff` between the two freeze versions, `git log`.
- Independence caveat (also in the script docstring and JSON): the checker imports the committed producer (`build`, `points`, `bounds`), observed through a module-level `max` hook; the producer file is unchanged. It checks the committed construction and is not an independent reimplementation. The independent confirmation is the audit's `ind_aggregate.py`.

## (c) Proposed text for files I do not own

1. **`T/plan.md`, E1 row (line 20), replace the whole row with:**
`| E1 | Exact aggregate comparison PROVED; scalar-graph finite capacities MEASURED | Tightened exact certificate survives both grids; original KHS-only sufficient test inconclusive. Scalar graph evidence complete and independently reproduced (record 05 MEASURED: factor-ten INCONCLUSIVE, >7/>800 thresholds post hoc). Response-01 added the rotQ24 pivot-tie disclosure (exact tie at column (2,1)), an exact BᵀB = D check and a committed checker for the record-04 inequalities | Theory01-05, evidence/e1*.json, evidence/response-01-e1-checks.json |`

2. **`tracks/bivariate-lanczos/code/drift/README.md`, after the paragraph ending "...aggregate and scalar verdicts." (the e1_reproduce paragraph), insert:**
```
The comparator full-graph uppers U_inf (T24/pivot and rotQ24/alternating) are
not regenerated by `e1_reproduce.py`. Their commands, as recorded in
`topics/padua-lanczos-drift-20261101/evidence/e1-scalar-cgs2.json`
(`full_graph_upper_runs`), are:

```bash
python tracks/bivariate-lanczos/code/drift/e1_cgs2.py --set triangle --degree 12 --rule pivot --output /workspace/padua-drift-runs/e1/cgs2-triangle-n12-pivot.json
python tracks/bivariate-lanczos/code/drift/e1_cgs2.py --set rotated --degree 12 --rule alt --output /workspace/padua-drift-runs/e1/cgs2-rotated-n12-alt.json
```

`upper_squared.exact` of each output is the comparator upper of PD-T?drift-codex-05.
The field `input_sha256` inside the `explicit_projection_check` block of
`e1_reproduce.py`'s output hashes a temporary JSON file (it contains timings and
paths), so it is not reproducible and should not be used as an identity; use
`generator_sha256`, `certificate_sha256` and `source_record_sha256`.

The response-01 checks for the E1 records (pivot ties, exact BᵀB = D at degree 12,
the record-04 inequalities, DEAD-clause history) are regenerated in about four
minutes by
`PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e1_response_checks.py --output <out>.json`
(`--skip-tie-break-bounds` omits the 3.5-minute Y-tie bounds run). It imports the
committed producer and is not an independent reimplementation.
```
3. **`T/evidence/e1-manifest.json` / `e1-scalar-manifest.json`:** immutable; nothing to edit. If the orchestrator keeps a response manifest, add `response-01-e1-checks.json` (76,613 bytes) and `e1_response_checks.py` (sha256 above).
4. **`T/report.md`, local-results-entry.md, `checks/independent-math-01.md`, `evidence/e1-summary.md`** (immutable or not mine): they carry the rotQ24 pivot values without the tie label (report.md:18 "exact pivot-adaptive selections"). Suggested one-sentence addition wherever rotQ24 pivot is cited: "rotQ24 pivot values are an X-tie-broken frozen sequence (exact tie at column (2,1) from the 90 degree symmetry; see evidence/response-01-e1-checks.json)." Also LOG: add a line listing the new evidence file and checker.
5. **`T/final-validation.json` / `protocol-check.json` / allocation scans:** immutable; they predate the new file and checker, so any registry or file-list receipt must be refreshed at preparation.

## (d) For the Codex re-audit

- **No change of any PROVED/MEASURED status, threshold or numerical claim.** Record 04 stays PROVED (computer-assisted), 05 stays MEASURED (rationale added; a separate finite PROVED record for the exact inequalities is explicitly not created and is flagged for AC/re-audit), 01-03 unchanged PROVED.
- Changed scope wording: record 04 "original KHS-only preregistered test" -> "frozen"; E1.md/record 02/ideas-e1 "sent before receiving results" removed in favour of the freeze file's own notes (originals quoted). The chronology itself remains unverifiable.
- New disclosure to check: rotQ24 pivot tie and its cause; my Y-tie bounds (first-party exact producer run, unchanged producer); T24 margin 0.008426. Note that the minimum untied rotQ24 margin is also small (0.003188 at column (8,6)); not a tie, but worth knowing.
- The sharpened-U DEAD low-degree facts come from my reimplementation of the auditor's logic (c1 and c2 clauses separately: c1 never fires with either U; c2 fires with sharpened U only).
- New code is a check of the committed construction, not independent; independence rests on the audit scripts.
- Record 03's title changed (provisional ID kept); the file name is unchanged.
- `ideas-e1.md` line numbers shifted after edits; the P-F6 separation is stated identically in record 03 and ideas-e1 IDEA?drift-codex-04. IDEA/LIT titles were quoted from `state/IDEAS.md` and `literature/INDEX.md` (read-only). I read PD-T042/043 only in the two theory files named above, not the L1 candidate files.
