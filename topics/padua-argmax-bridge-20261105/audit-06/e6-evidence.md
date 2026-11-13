# Audit-06 part E6: focused technical audit of response-05 (handoff 34 items 1–2; budget and custody)

- **Auditor:** Claude Opus 5.5, xhigh (independent auditor subagent of the handoff-34 orchestrator). Chosen because this is an
  adversarial re-check of repaired verification code with new independent controls.
- **Rules/head:** AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md, handoffs 33 and 34 (in full), response-05.md,
  audit-05.md, audit-05/e5-evidence.md, supplementary-evidence-review-response05-20261113.md read at
  `5b1a4942af498e60e9da4c8860c57cb4f67be4ef` (branch `codex/padua-argmax-bridge-20261105`; handoff-34 input head `26ab08d`;
  5b1a494 adds only handoff 34). Code checkpoint `074c7da`: executable code at HEAD is byte-identical to it (only the campaign
  README changed after it). Repair diff read with `git diff b5a6946 074c7da`.
- **Scope:** E5-01 repair, E5-02/E5-04 repairs, handoff-34 commands 1–3, compact-verifier identity, budget/custody statements.
  Manuscript items 3–5 are outside this part. No novelty content (repairs of existing code and records): full `state/IDEAS.md` omitted.
- **Git/repo:** no state-changing git; no repository file written (`git status --porcelain` empty, HEAD unchanged before/after).
  Execution in a `git archive 5b1a494` copy at `A/e6-run/tree`. Only `git archive/show/diff/log/ls-tree/rev-parse/blame` used.
- **Labels:** [E] my execution; [D] derived from code/records; [I] inspection only.
- **Preregistration:** `e6-run/PREREG-E6.md` first saved 23:02:48Z (`590cdef9…`) before any run; amendment A1 23:08:30Z
  (`dfac147d…`) before I1; A2 23:12:00Z (final `b31e87b8…`) before O1–O6 (`PREREG-E6.sha256`). Every consequential command ran
  once through `e6-code/observe.py` (copy of audit-05 observer `b13bd6fb` with E6 env names: fork/exec, `os.wait4`, RLIMIT_CPU,
  wall cap, SIGCHLD default asserted, ECHILD recorded). No retry. 23 observed runs, all exits as preregistered, total child CPU
  **30.4 s** (cap 40 min). Environment: Linux 6.18.44 x86_64, glibc 2.39, Python 3.13.18, NumPy 2.5.3, gcc 13.3.0 (not the
  recorded 3.12.14 / 2.3.5).

## 1. Verdict (this part)

| Item | Verdict |
|---|---|
| E5-01 reader/producer allowlist | **Repaired** within synthetic storage-compatibility scope [E]: exactly the empty top-level `.preserve.lock` and schema-valid per-pass `storage-dedup.json` are newly admitted; 28 malformed/misplaced lock/receipt variants reject; the full n≥256 producer name set (60 per case) passes the repaired reader and is rejected by the previous reader. Canonical-ZIP run remains **OPEN** (ZIP absent). |
| Real round-trip | Real `deduplicate()` → `completed()` → `export()` → `verify()` confirmed in the developer regression (no mock of those, [I]) and in my own independent round-trip [E]. Adapters (trust pins, checker arithmetic, sampled closure, package relocation) are explicit; the evidence is storage compatibility only. |
| Optimization refusal, pins, parser, linkage | **Intact** [E/D]: reader diff touches only `check_members`; 6 own refusal/pin runs plus the 16 carried audit-05 reader controls behave as before. |
| Member count | **Consistent** [D]: 60 allowlisted names per case for n≥256 (old allowlist 58); 191×60 = 11,460 leaves 253 for root/sample overhead. |
| E5-02 analytic guard | **Repaired** [E]: 9/9 falsified/optimized controls refuse or assert; normal output equals receipt.json in 10 of 11 fields (`python` 3.13.18 vs 3.12.14 only). |
| E5-04 runtime probe | **Repaired at stated scope** [E]: FTZ, FTZ\|DAZ, RD, RU, RZ and two combinations reject; DAZ alone is not detected (E6-02, NOTE); probe evidence is per process. |
| Handoff-34 commands 1–3 | Exit 0 / 0 / 0 [E]. |
| Compact verifier | Byte-identical to audit-05's audited `2d26886f…` and its whole import closure [E git]; audit-05 R4–R7, A4, VC, VT results stand. |
| Budget/custody | All five figures **reproduce exactly** [E]; no non-topic file differs from main except the topic's own results file; no cold-storage destination invented [E]. |
| Findings | **No BLOCKING or MAJOR.** One MINOR (E6-01 stale deposit-README freeze), five NOTE, one EDITORIAL. |

## 2. Identities [E]

Tree copy hashes: `return_bundle.py` **3f903e62…**, `check_reader_repairs.py` 68bc9b70…, `runner.py` a198b651…, `compact_pack/storage.py`
274d009d…, `onset512_analytic/check.py` 5ce8cc07…, `runtime_probe.py` 9f1c503e…, frozen `controls.py` c1810bd1…, `verify_compact.py` 2d26886f….
All equal the supplementary review's table except the campaign README (`df869cd1…` vs reviewed `9bd96336…`; prose-only change after
review, disclosed in LOG L3191). Old reader `git show b5a6946:…/return_bundle.py` = **5e25c8a4…** (response-04 candidate).
Inputs re-authenticated: `return.tar.gz` 36,045,486 B `b00fd57f…109a`; `padua30.zip` 25,111,335 B `aac08e5f…e74d2` (data reads only).

## 3. Handoff-34 commands 1–3 (cwd = tree copy) [E]

| Run | Command | Exit | CPU s | Result |
|---|---|---:|---:|---|
| R1 | `python3 -E -B …/local_onset512_campaign/check_reader_repairs.py` | 0 | 11.04 | PASS, **60 controls**; all 40 audit-05 controls retained by name, 20 added; stdout `d4fcdad4…` = byte-identical to the supplementary reviewer's `reader-regression.json` (Py 3.12.14) |
| R2 | `python3 -E -B …/onset512_analytic/check.py` | 0 | 0.21 | 11 keys; 8 enclosures, `arithmetic`, `assertions` equal committed receipt.json; only `python` differs |
| R3 | `python3 -E -B …/independent_phase_checker/runtime_probe.py` | 0 | 0.15 | 31 arithmetic controls; 4 probes true |

## 4. E5-01: reconstruction of the fix [I/D]

- **Diff** (`b5a6946..074c7da`, reader): `pass_files` += `storage-dedup.json`; `top` += `.preserve.lock`; for a top-level lock
  `payload == b''` ('preserve lock must be empty'); for a 4-part pass member named `storage-dedup.json`: reader `strict()` parse
  (duplicate keys, NaN/Infinity rejected), `type is dict` and key set exactly `{immutable_paths_examined, paths_relinked,
  logical_bytes_relinked, scope}`, the three counts `type(...) is int` and ≥ 0 (bool/float/str excluded), `relinked ≤ examined`
  and `relinked == 0 ⇒ bytes == 0`, `scope ==` the producer's fixed string. Nothing else in the reader changed: optimization
  guard, `MANIFEST_SHA 5b89fa66…`, `CANONICAL_ARCHIVE_SHA da63280a…`, `CAMPAIGN_RUNNER_SHA 459d0728…`, typed `strict`, linkage
  and pin-before-checker order are byte-unchanged.
- **Producer facts [D]:** `storage.py` (274d009d…, only commit 2cab2a1; same bytes at the campaign commit 2d6be5f) writes
  `<pass>/storage-dedup.json` exclusively with exactly that schema (L60–62) and opens `<root>/.preserve.lock` `a+b` for `flock`
  only, so it stays empty (L44–45). Historical runner 459d0728 (2d6be5f L120) and current runner (L124) call
  `deduplicate(output, target)` after every validated pass; a raising call fails the case, and all 382 passes were recorded
  successful, so all 382 receipts and the lock existed. The historical exporter adds every top-level file (`iterdir`, dotfiles
  included) and every non-`check-` case file. The historical reader (d1dba234) had no member allowlist, so its acceptance of the
  canonical ZIP never tested names.
- **Real round-trip in the developer regression [I + E]:** `producer_roundtrip()` calls `deduplicate` (imported from
  `compact_pack/storage.py`), `B.export` (which calls the real `completed()`), then `B.verify` → real `check_members`/`strict`.
  The only `patch.object` targets are `R.ROOT`, `R.RELEASE`, `R.__file__`, `B.__file__`, `R.pins`, `R.LocalAccess`, `B.Access`,
  `B.MANIFEST_SHA`, `B.validate_pass` (plus zipfile size/plan stubs in unrelated controls). No mock of `deduplicate`, `export`,
  `completed` or `check_members`. Limitation: its build manifests have `linked_dependency_closure: []`, so the deps branch of
  `deduplicate` is not exercised (my B1 exercises it).
- **Adapters and scope [I]:** the regression docstring, campaign README, response-05, LOG and pr-update state that trust pins,
  proof arithmetic and sampled closure are adapted and that this is not canonical-data or proof-arithmetic acceptance. The README's
  adapter list omits the (benign) ROOT/RELEASE/`__file__` relocation (E6-04). No record calls the synthetic positive a canonical
  or real-checker acceptance.
- **Member count [D]:** reader constants give 9 case names, 27 pass names, 9 top names, 5 outside names. The frozen engine builds
  only `S` for n ≥ 256 (`runtime.py` L68: `('S','lambda') if n<256 else ('S',)`), so onset passes never contain
  `lambda-build.json`, and produce passes lack `original-certificate.json`. Engine writes 23 names per pass (6 controls + 6 checker
  stage files, tree, preregistration, summary, final-accounting, raw-evidence, essential-receipt, S-build, runtime-before/after,
  loaded-before/after.maps), the runner adds `local-validation.json` and `storage-dedup.json`: produce 25, verify 26, case
  9 + 25 + 26 = **60** (58 without receipts; the original return's sampled 199/238 passes show the same engine set plus
  `lambda-build.json`). 191 × 60 = 11,460; 11,713 − 11,460 = **253** = 5 outside + COMPACT.json + 9 top (incl. lock) + 24 sampled
  `check-*` files (1 build dir × 6 files × 4 passes, as in the original return's 6-file check dirs) + **214** helper sources and
  preserved objects. With 58/case the last term would be 597, versus 245 distinct outside-root SHAs for the original return's
  two sampled degrees with two builds each (I1). Consistent with 60/case; derived, not observed on the ZIP.

## 5. Own reader controls, developer-equivalent MARKED adapter (RB6 Part A) [E]

`e6-code/rb6.py` (`9b6dd396…`), R `RB6-reader-controls.json` `ab895f25…`; synthetic Access arithmetic, synthetic pins, stubbed
sampled `validate_pass`, temp release; every archive rebuilt and pinned by its own SHA. **50/50 Part-A controls as preregistered.**

| Group | Controls → observed |
|---|---|
| Carried audit-05 R11 (16, incl. 2 diagnostics) | RB-a lock + 382 receipts and RB-a2 receipts only → now **ACCEPT** (both REJECT in audit-05); RB-b runner a198b651 → `preregistered campaign runner`; RB-c `'0'`, RB-d `true`, RB-o `false` exits → `integer field`; RB-e → `summary receipt identity`; RB-f → `fresh input primary linkage`; RB-g → `completed attempt status`; RB-h → original-certificate equality; RB-i → `unsampled native history`; RB-j → `preserved object hash`; RB-k → `unregistered helper source`; RB-l → `duplicate JSON key`. RB-m symlink-mode, RB-n directory-mode → ACCEPT (E5-06 unchanged) |
| Lock (9: 8 reject, 1 diagnostic) | L1 `\n`, L2 NUL → `preserve lock must be empty`; L3 empty lock in a pass dir → `unregistered pass member`; L4 case level → `unregistered case member`; L5 `out/jobs/.preserve.lock` → `unregistered job directory`; L6 under helper-source → `unregistered helper source`; L7 archive root → `unregistered archive member`; L8 `.preserve.lock2` → `unregistered campaign member`; L9 lock inside a **sampled** `check-*` dir → ACCEPT (diagnostic; E6-04) |
| Receipt (24: 20 reject, 4 diagnostic) | D1 extra field, D2 missing field, D3 list, D4 null → `receipt schema`; D5 `"6"`, D6 `true`, D7 `6.0`, D8 `-1`, D9 `1e2` → `nonnegative integer counts`; D10 relinked > examined, D11 bytes without relinks → `consistent counts`; D12 scope + space, D13 scope `5` → `dedup scope`; D14 duplicate key → `duplicate JSON key`; D15 NaN, D15b Infinity → `nonfinite JSON`; D16 truncated → JSONDecodeError; D17 top-level receipt → `unregistered campaign member`; D18 case-level → `unregistered case member`; D19 in unsampled `check-*` → `unsampled native history`. Diagnostics ACCEPT: D20 reordered/compact keys; **D21 lying receipt 10^6/10^6/10^15**; D22 all zero; D23 one receipt, no lock (presence not required) |
| Baseline | adapter fixture without receipts/lock → ACCEPT 191/382 |

## 6. Own REAL producer round-trip and analogy check [E]

RB6 Part B (same run): synthetic tree from `fixture(tree, assets)` plus the **full n ≥ 256 producer name set** (23 engine names,
`local-validation.json`; 4 case-level stdout/stderr) and per pass one `S-build.json` whose `check-*` workdir holds 3 build
artifacts and 3 deps under `deps/` plus one external dependency row. No adapter on `deduplicate`, `completed`, `export`,
`verify`, `check_members`, `strict`.
- Real `deduplicate` ×382: 382 receipts, examined 2,292 (6 each, deps branch exercised, external row skipped), relinked 2,286
  (first pass 0), logical 40,767 B, lock 0 B, 6 store objects.
- Real `export`: ZIP 3,415,242 B `610aaa86…` (test data, not a canonical artifact), **11,502 members = 191 × 60 + 42**: every unsampled
  case exactly **60** members, sampled [445, 370] 72 each, 24 `check-*` files, 9 top-level (lock included, 0 B), 5 outside +
  COMPACT.json, 1 helper, 2 preserved; all 382 receipts byte-equal to disk.
- **B1** repaired reader → ACCEPT 191 pairs / 382 proofs, 4 sampled-closure adapter calls. **B2** previous reader 5e25c8a4 on the same
  archive → REJECT `unregistered campaign member: out/.preserve.lock` (the E5-01 defect, reproduced and shown fixed).
  **B3** one real receipt (`out/jobs/321/verify`, true 6/6/107) rewritten to 6/1/1 and re-pinned → ACCEPT (E6-03).
- **I1** (data-only, `ident6.py` `5f7f615a…`, report `99580df3…`): identity rows of the original return's sampled passes
  (199/238; 5 JSON names the exporter scans) against its `package_root` and the padua30 trusted manifest (all 180 arithmetic files
  are manifest rows): 196 under the output prefix, 214 trusted, 2,016 outside root (245 distinct SHAs ≤ 247 preserved objects),
  **0 other under-root rows**. By analogy the exporter's identity rule adds no further non-allowlisted names. The onset sandbox
  differs; an unknown extra top-level file in the historical output root can only be excluded by the canonical run.

## 7. E5-02 analytic checker [E]

Guard `if sys.flags.optimize: raise SystemExit(...)` at module level (L13), before every function and all 29 assert nodes (28 + the
new `log(PI).lo > F(11, 10)` at L146, matching the consumed `11/10 < log π < 23/20` in both texts). Copies under `e6-run/r2mut/`:
Mg (gate `< F(1,1000)`, bytes equal to the supplementary `false_gate.py` `ac028546…`), Ml (`log(PI).lo > F(23,20)`, `350b8e17…`).

| Run | Copy / flags | Exit | Observed |
|---|---|---:|---|
| R2a / R2b | Mg / Ml `-E -B` | 1 / 1 | AssertionError, empty stdout |
| R2c / R2d / R2f / R2i | Mg `-O -B`, Mg `-OO -B`, Mg `-E -O -B`, Ml `-O -B` | 1 | `optimization is not permitted…`, empty stdout |
| R2e / R2h | Mg, M0 `-B` + PYTHONOPTIMIZE=1 | 1 | refusal, empty stdout |
| R2g | Mg `-E -B` + PYTHONOPTIMIZE=1 | 1 | AssertionError (`-E` ignores env) |

No path prints `"assertions": "PASS"` without active assertions. receipt.json and PREREGISTRATION.md are unchanged since audit-05.
The analytic README states the safe command, the guard and the 11-field equality correctly.

## 8. E5-04 runtime probe challenge (P1) [E]

`gcc -shared -fPIC -O2` of `mxcsr.c` (`848e6904…`, `_mm_getcsr`/`_mm_setcsr` only) → `libmxcsr.so` `021ef637…`; `probe6.py`
(`66655e34…`) imports NumPy and the tree's probe first, sets MXCSR in the same thread, reads uint64 bit patterns, calls the real
`runtime_probe.main()`, restores in `finally`. Default MXCSR `0x1fa2`.

| Mode | `2^-1022/2` | `2^-1074·2` (subnormal operand) | `nextafter(0,1)` | tie_down / tie_up | Probe verdict |
|---|---|---|---|---|---|
| default | 0x8000000000000 | 0x2 | 0x1 | …000 / …002 | PASS |
| FTZ | **0x0** | 0x0 | 0x1 | …000 / …002 | REJECT gradual_underflow |
| DAZ | 0x8000000000000 | **0x0** | 0x1 | …000 / …002 | **PASS (undetected)** |
| FTZ\|DAZ | **0x0** | 0x0 | 0x1 | …000 / …002 | REJECT gradual_underflow |
| RD / RZ | 0x8000000000000 | 0x2 | 0x1 | …000 / **…001** | REJECT ties_even_up |
| RU | 0x8000000000000 | 0x2 | 0x1 | **…001** / …002 | REJECT ties_even_down |
| FTZ\|DAZ\|RZ | 0x0 | 0x0 | 0x1 | …000 / …001 | REJECT gradual_underflow, ties_even_up |
| DAZ\|RU | 0x8000000000000 | 0x0 | 0x1 | …001 / …002 | REJECT ties_even_down |

A fresh interpreter started while the parent thread held `0x9fe2` reads `0x1fa0` (execve resets SSE state): probe evidence is per
process. The `smallest_subnormal` (nextafter) probe is insensitive to every mode tested. Exact scope: in the probing process and
thread, NumPy binary64 addition at two tie points rounds to nearest-even (excludes RD/RU/RZ), division producing a subnormal result
is not flushed (excludes FTZ with or without DAZ), and nextafter returns the smallest-subnormal encoding. Not covered: DAZ alone
(subnormal operands), other operations or loop kernels, other processes (including the I25 checker and historical workers),
hardware/libm conformance. **Wording [I]:** J03's 2026-11-13 correction ("reject FTZ and FTZ|DAZ on the probed operation … finite,
prospective … in that process, not … all binary64 operations/SIMD loops, a historical worker's mode or universal hardware/libm
conformance"), response-05 E5-04, LOG L3123–3126, deposit README L412–414 and the probe docstring match this scope; none claims
DAZ-alone detection. G01 L210 ("model proved in J03") is unchanged pre-existing text with its dated correction at L238–242.

## 9. Compact verifier (item 4) [E git]

`git diff --stat 33b9eca 5b1a494 -- compact_pack code/final_hybrid_engine code/compact_verifier_audit03
code/independent_phase_checker/{check,controls,run}.py` is empty; `verify_compact.py` = `2d26886f…`, the version audit-05 ran.
I did not rerun it: with `--package`, `Access` imports `padua30/<ENGINE>/checker.py`, i.e. archive bytes, which this audit's
rules exclude. Audit-05's results (R4 `--expect-plan all` exit 0, 280 pairs, stdout `3f6605da…`; R5 `small` exit 1; R6/R7; A4
30/30; VC/VT controls) therefore apply unchanged. Reader and runner optimization refusal re-run [E]: O1 `-O`, O2 PYTHONOPTIMIZE=1,
O3 `-E -O`, O4 `-OO`, O5 runner `preregister` under `-O` (directory not created) → exit 1 `optimized Python is unsupported`,
empty stdout; O6 `-E -B` + PYTHONOPTIMIZE=1 → exit 1 `external archive SHA256`. E1 `evidence_index.py --check` → PASS, v4,
396 entries, index 32,414 B, total 1,710,416 B.

## 10. Budget and custody (Z1) [E]

Own implementation `size6.py` (`50beb8aa…`, report `bb31e81c…`) of the audit-02 `size.py` rules (count every blob except
`.py .sh .c .cpp .h .tex .bib .diff`, `.gitignore`, and `.md` other than `COLD_STORAGE.md`; the topic convention adds the 2,087 B
`code/post_audit_D09_threepoint/FREEZE.md`). `code/evidence_index.py` is the essential-evidence index tool and does not define
the class; the definition lives in `audit-02/code/t2/size.py`, `size-policy-review.md` and LOG L585.

| Quantity | Recorded | Mine |
|---|---:|---:|
| main `b5388c2` | 9,733,758 | **9,733,758** |
| HEAD = union | 11,734,394 | **11,734,394** |
| topic share (HEAD − main = counted topic paths at HEAD; main has 0 topic paths) | 2,000,636 | **2,000,636** |
| + FREEZE.md 2,087 | 11,736,481 | **11,736,481** |
| no-shrink bound 9,917,613 + positive deltas 8a94ce6→HEAD (1,833,696 + 4,832 = 1,838,528) | 11,756,141 | **11,756,141** |
| growth 33b9eca (= response-05 input 520b364) → HEAD | — | net = positive = 4,832: new `paper/notation-renames-audit05.json` 3,749; `zenodo-deposit/MANIFEST.json.in` +1,083; no shrink/removal |

- Only `results/padua-argmax-bridge-20261105.md` differs from main outside the topic directory (excluded `.md`); root
  `RESULTS.md` unchanged; nothing of another topic removed or reclassified. "Neither original branch alone exceeded 10 MB" holds
  (9,733,758; pre-merge topic 9,895,866 + 2,087). Note: the local `main` ref is a stale 2b52b43; `origin/main` = b5388c2 was used.
- Cold storage: `COLD_STORAGE.md` and `cold-storage.json` unchanged since 520b364; the response-05 diff adds no locator, URL or
  DOI (only "cold-storage destination remains AC's decision" and "no cold-storage transfer is claimed"). Both TeX data statements
  say the post-repair snapshot is "being prepared" and "DOI pending"; no a433c7d citation. Custody statements in response-05,
  handoff 34, LOG L3083–3102/L3175–3184, results and pr-update distinguish recorded witnesses from present availability and keep the
  canonical run, I25 checks, native-history custody and DOI open; I found no custody overclaim.

## 11. Findings

**E6-01 MINOR — deposit README still names ad908acb as the active freeze with 57/150-page PDFs.**
- Location: `zenodo-deposit/README.md` L366–372 ("The active paired source freeze is `ad908acb…`; current PDFs have57/150pages",
  from 98261ae) and the audit-05 dated note L385 ("superseded by the final paired freeze `ad908acb…`").
- Reason [E/I]: response-05 edited this README (new "Audit-05 response" section L388–422) but left these present-tense lines;
  `MANIFEST.json.in` L291–294, both BUILD.md files and the LOG give `8937d3b723c0…` and 58/152 pages (paper `1dc50b84…`,
  companion `9bd922db…`). No 8937d3b appears in the README.
- Impact: a deposit reader is pointed at a superseded freeze; no claim, code or evidence changes.
- Fix: dated addendum naming 8937d3b and 58/152 as current and ad908acb/57/150 as historical (stale process text; within the
  third-round auditor in-place rule).

**E6-02 NOTE — the runtime probe does not detect DAZ alone.** With MXCSR DAZ only, `2^-1074 · 2` gives 0x0 (0x2 normally) while all
four probes pass (P1). J03's trusted model includes gradual underflow for subnormal operands. No record claims DAZ-alone
detection, and response-04 J3-05 (cited in audit-05 E5-04) notes that no subnormal arises in the computation. Optional: a one-line subnormal-operand bit probe
(e.g. `[2^-1074]*[2]` must be 0x2), or "DAZ alone is not detected" in the J03 scope sentence. The nextafter probe tests the
library implementation, not the FP environment.

**E6-03 NOTE — storage receipts are only internally consistent.** The counts are not linked to the pass's `S-build.json`
(examined = 3 per build manifest + deps rows under `workdir/deps`; bytes ≤ their sum), so a consistent but false receipt is
accepted (D21 10^6/10^6/10^15; B3 a real receipt rewritten 6/6/107 → 6/1/1). The records say "consistent counts", which is
accurate. No scientific impact: the receipt is storage metadata outside the proof. Optional cross-check.

**E6-04 NOTE — coverage and precision of the committed regression.** The committed 60 controls test lock emptiness and receipt
schema but no misplaced lock/receipt (pass-dir, case-level, nested and top-level variants exist only in uncommitted scratch
harnesses: the supplementary reviewer's and mine). The developer round-trip does not exercise the deps branch of `deduplicate`.
The campaign README's adapter list omits the ROOT/RELEASE/`__file__` relocation. Inside sampled `check-*` dirs any name is accepted
under the adapter (L9), which is the same class as E5-06. Optional: add L3–L8/D17–D19-style negatives and one deps row to the regression.

**E6-05 NOTE — the audit-05 dated E5-08 addendum in `code/local_onset512_campaign/README.md` was replaced rather than superseded.**
The new dated section restates the runner identities, and the stale "fails until fixed" statement survives in audit-05.md and in the
deposit README (which kept its dated note and appended a superseding section). No information needed for verification is lost.
Record hygiene only.

**E6-06 EDITORIAL — missing spaces between words and numbers** in the new prose (e.g. "SHA256 is3f903e62…" in
local-onset512-summary L127; "main alone9,733,758bytes", "share2,000,636bytes" in LOG, results, pr-update, deposit README,
MANIFEST notes).

Carried unchanged: E5-05, E5-06 (RB-m/RB-n still accepted), E5-07 (export-side `completed()` still compares `== 0` on a
`common.strict` parse), E5-09 (single-archive reader).

## 12. Executions (each once; observations in `e6-run/obs/`)

R1 0 (11.04 s) · R2 0 (0.21) · R3 0 (0.15) · R2a–R2i 1 ×9 (≤0.18 each) · P1 0 (0.22) · RB6 0 (15.20; 53/53 as preregistered:
50 Part A + B1–B3) · I1 0 (0.96) · Z1 0 (0.22) · E1 0 (0.07) · O1–O6 1 ×6. Unobserved, read-only or data-only: `git archive/show/
diff/ls-tree/blame/rev-parse`, `tar -tzf` listing (4,324 members) and one `tar -xzOf …/run.json` read of the original return, the
`gcc` helper build, AST and `sha256sum` reads.
Code (`e6-code/`): observe `03a8e824…`, rb6 `9b6dd396…`, probe6 `66655e34…`, ident6 `5f7f615a…`, size6 `50beb8aa…`, mxcsr.c
`848e6904…`, return_bundle_b5a6946 `5e25c8a4…`. Reports (`e6-run/`): RB6 `ab895f25…`, P1 `91341791…`, I1 `99580df3…`, Z1 `bb31e81c…`.

## 13. Limits

- Absent and not checked: canonical `onset512-return-20261108.zip` (`da63280a…`), I25 bundle, derivative/inventory/review ZIPs,
  historical PDFs, 632 MiB native histories. The repaired reader has never read the canonical ZIP; E5-01 compatibility is shown
  on synthetic producer output, with the member count and the identity rule supported only by derivation and analogy.
- Every onset-reader positive uses adapters (pins, checker arithmetic, sampled closure, package relocation). No real-checker
  positive exists for 320..510.
- The compact verifier was not rerun (archive-code rule); its acceptance rests on byte identity plus audit-05's executions.
- MXCSR controls cover one thread of one process on this CPU/Python/NumPy; no claim about AVX-512 embedded rounding, other
  kernels or historical workers.
- No native, engine, Syvert, remote or archive-code execution. Manuscript items (handoff 34 items 3–5) are not covered by this part.
