# Audit-05 part E5: E4-01..E4-04 repairs, reruns, own controls, recipes/provenance, global budget

- **Auditor:** Claude Opus 5.5, xhigh (independent auditor subagent of the handoff-32 orchestrator). Chosen because this is an adversarial check of repaired verification code.
- **Rules/head:** AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md, handoff 32, audit-04/e4-evidence.md, audit-04/WHEN-INPUTS-ARRIVE.md, audit-04/j03-i25.md read at `33b9eca8167980cad0b0a491da7de64280c9a158` (branch `codex/padua-argmax-bridge-20261105`; handoff input head `f8168255…`; 33b9eca adds only a LOG addendum). Repair commit `b5a6946` read with `git show`.
- **Scope:** handoff 32 items 2, 3 (three technical commands), 5 (provenance/recipes) and the global budget. The manuscript items (32 pairs, J1/J2 clauses, check_correspondence/baseline controls) are outside this part. No novelty content: full `state/IDEAS.md` read omitted.
- **Git/repo:** no state-changing git; no repository file created or edited (`git status --porcelain` empty before and after; HEAD unchanged). All execution in `git archive` copy `e5-run/tree`.
- **Labels:** [E] my execution; [D] derived from code/records; [I] inspection only.
- **Preregistration:** `e5-run/PREREG-E5-01.md`, first saved 20:44:19Z (SHA `6780e470…`) before any run; amendments A1 (20:54:24Z, `c050da5e…`), A2 (20:56:30Z, `2eeffc1b…`), A3 (20:57:01Z, `5fcddade…`), A4 (20:57:23Z, final `ae5bdf43…`) appended and re-hashed before their runs (`PREREG-E5-01.sha256`). Every consequential command ran once through `e5-code/observe.py` (fork/exec, `os.wait4`, RLIMIT_CPU, wall cap, SIGCHLD default asserted by explicit check, ECHILD recorded). No retry. Total observed child CPU ≈ 165 s (cap 40 min).

## 1. Verdict (this part)

| Item | Verdict |
|---|---|
| E4-01 removable asserts / optimization | **Repaired** in the reader/runner [E]; zero `assert` nodes on the reader/verifier production path [E]. |
| E4-02 pins / ordering | **Repaired** [E]: external manifest and archive constants present; with the REAL restored runtime, `pins()` authenticates before the real checker is constructed. |
| E4-03 linkage / members / types | Linkage and type checks **repaired** [E]. **But the new member allowlist rejects files the campaign's own producer writes (E5-01, MAJOR)**: the required canonical rerun cannot pass as committed. |
| E4-04 types / coverage | **Repaired** [E] without adapter: `false`, `'0'`, `0.0`, `true` exits rejected; `all` vs subset outputs differ; `small` rejects. |
| Cheap reruns (R1–R3) | Reproduced [E]: 40/40 controls; 31 controls + 4 probes; analytic enclosures identical to the committed receipt. |
| Recipes / provenance wording | Mostly accurate [I/E]; E5-02, E5-04, E5-08 wording items; runner identity not retroactively attributed [E]. |
| Global budget | Figures reproduced exactly [E]; no non-topic file changed or removed vs main [E]; attribution wording incomplete (E5-03). |

**Topic returns to WORK for E5-01** (small material code fix + focused re-check). No finding refutes a recorded result; all reader failures found are fail-closed.

## 2. Inputs and trusted layout (S0) [E]

- `inputs/padua30.zip` 25,111,335 B, SHA `aac08e5f…e74d2`; `inputs/return.tar.gz` 36,045,486 B, SHA `b00fd57f…109a`, `cmp`-identical to the earlier return-data copy.
- S0 (`pkg_auth.py`, data-only): 257 regular members, safe names, CRC OK; `runtime_manifest.json` 54,003 B = `5b89fa66…`; **all 250 manifest rows authenticated**; 7 unlisted members (README.md, SOURCE_CUSTODY.json = `c9051f19…` as pinned in the deposit README, compact_pack/README.md, the manifest itself, 3 `producer-runtime-custody/<sha>/` libs whose bytes hash to their directory names).
- Both internal verifier copies (`padua30/verify_compact.py`, `padua30/topics/…/compact_pack/verify_compact.py`) are **`7c2dad53…`** (the unrepaired historical verifier); never executed.
- Restored into the tree copy only: `local-output/argmax-bridge-20261105/compact-release-aea62883/padua30` and all **180** `asset_provenance` arithmetic files (each authenticated). FREEZE `0d9ce0a5…`, 13 code rows match the tree.
- **No absent-file adapter was used in any run below.**

## 3. Reruns of the handoff commands [E] (cwd = tree copy root, as the scripts expect)

| Run | Command | Exit | CPU s | Result |
|---|---|---:|---:|---|
| R1 | `python3 -E -B topics/…/code/local_onset512_campaign/check_reader_repairs.py` | 0 | 5.96 | `PASS`, 40 controls (list identical to the record); stdout `dbd82fe6…` |
| R2 | `OPENBLAS/OMP=1 python3 -E -B topics/…/code/independent_phase_checker/runtime_probe.py` | 0 | 0.17 | Python 3.13.18, NumPy 2.5.3; 31 controls; 4 probes true |
| R3 | `python3 -B topics/…/code/onset512_analytic/check.py` | 0 | 0.26 | all 8 enclosures identical to committed `receipt.json` (checker `ff2859ee…`); only `python` differs (3.13.18 vs 3.12.14) |

## 4. Repaired compact verifier on the original return, no adapter [E]

`python3 -I -S -B topics/…/compact_pack/verify_compact.py RET --package local-output/…/padua30 --manifest-sha 5b89fa66… [plan]`, verifier `2d26886f…`:

| Run | Plan / flags | Exit | CPU s | Output |
|---|---|---:|---:|---|
| R4 | `--expect-plan all` | 0 | 6.08 | `expect_plan=all`, `coverage_mode=complete_plan`, 280 pairs, degrees exactly 41..319+511, sampled [199,238]; stdout 2,781 B **`3f6605da…` = byte-identical to root's and Astra's recorded stdout** |
| R5 | `--expect-plan small` | 1 | 1.08 | `ValueError: expected complete plan coverage` |
| R6 | no plan | 0 | 5.87 | `coverage_mode=completed_subset`, `expect_plan=null`; differs from R4 only in these two fields (`19ec85ef…`) |
| R7 | `-O -I -S -B`, all | 0 | 6.14 | byte-identical to R4 (no assert on this path) |
| A1a | forged tar (`COMPACT.json={}`), `PYTHONOPTIMIZE=1 -S -B` and `-O -I -S -B` | 1, 1 | 0.3 | `KeyError: 'schema'`, no output |
| A1b | real return, `PYTHONOPTIMIZE=1`, `small` | 1 | 1.25 | `expected complete plan coverage` |
| A4 | `code/compact_verifier_audit03/check.py` (audit-03 30-control suite) | 0 | 16.5 | **30/30 as designed** (28 named rejections, 2 designed acceptances); receipt `ca08e1a0…` |

Agreement with `reader-repair-execution-20261113.md`: same command, inputs, exit 0, coverage and stdout bytes; CPU 6.08 s vs 5.536 (root) / 5.349 (Astra).

## 5. Code review of the repairs [I/D], with execution where marked

- **Assertions.** AST count [E]: 0 `assert` nodes in return_bundle, runner, verify_compact, evidence, common, archive_io, ownership, process_guard, storage, the frozen engine `checker.py` (imports only `fractions`; in FREEZE code_data), I25 check/run, runtime_probe, accept_controls. `compact_pack/plans.py` keeps 3 asserts on fixed constants (no behavioural effect under `-O`; R7 identical). Both embedded deposit recipes parse with 0 asserts and an optimization guard [E].
- **Optimization refusal** [E] (`forged-empty.zip`, SHA `9ab68303…`): reader under `-O -B`, `-B`+`PYTHONOPTIMIZE=1`, `-E -O -B`, `-OO -B` → exit 1 `optimized Python is unsupported`, empty stdout; `runner.py preregister NEWDIR` under `-O` → exit 1, NEWDIR not created. `-E -B` with `PYTHONOPTIMIZE=1` ignores the variable and rejects normally (R8h).
- **External pins.** `MANIFEST_SHA=5b89fa66…`, `CANONICAL_ARCHIVE_SHA=da63280a…`, `CAMPAIGN_RUNNER_SHA=459d0728…` are module constants (return_bundle.py:24–26). Default pin rejects any other archive (R8f `external archive SHA256`). `--archive-sha` is an explicit operator pin; the printed result carries the archive identity and reader identity.
- **Pins before checker, with the REAL runtime** [E] R10 (`rb_real.py`, call-through spies only): the developer fixture re-pinned to the real local pins/manifest/freeze; events `['pins','checker']`; the **real** checker then rejects the synthetic certificate (`strict essential schema/version`); CLI rerun R10b exit 1. So the developer's positive 191-pair baseline exists only under its arithmetic adapter. This is also the first audit execution in which the reader's `R.pins()` passes on a restored trusted layout (blocked in audit-04).
- **Strict parser** [E] R9: the reader's typed `strict()` accepts all **3,978** authentic JSON records of the original return (same frozen engine; all `bytes/n/observed_returncode/hard_aggregate_cap` ints; all `ECHILD/complete/terminal/timeout/…` bools). No type incompatibility found.
- **Unsampled linkage** [E] (R11 under the developer-equivalent adapter, my own mutations): summary receipt path altered with bytes/SHA kept → `summary receipt identity`; fresh `certificate_identity` altered consistently in 3 records → `fresh input primary linkage`; attempt `failed` → `completed attempt status`; original-certificate ≠ primary → rejected; prereg runner = repaired `a198b651…` → `preregistered campaign runner`.
- **Types** [E]: reader `'0'`, `true`, `false` (pilot-summary + wrapper) → `integer field`; duplicate key → `duplicate JSON key`. Compact verifier (no adapter) `false`, `'0'` → `observed pass EXIT0`; `0.0`, `true` → `observed wrapper EXIT0`.
- **Members** [E]: unsampled `check-*` → `unsampled native history`; extra helper → `unregistered helper source`; wrong preserved hash → `preserved object hash`. Diagnostics: symlink-typed and directory-mode (no trailing slash) inventoried ZIP members under allowlisted names are **accepted as data** (never extracted) — E5-06.
- **Runner identity** [D/E]: `runner.run()` requires `identity(__file__)==reg['runner']`, so the repaired runner (`a198b651…`) cannot continue the historical campaign; the reader requires the historical `459d0728…` (R11 RB-b). Deposit README L132–133 and MANIFEST `verifier_provenance` do not attribute the repair to the run. `code/local_onset512_campaign/README.md` says nothing about this (E5-08).
- **Export path** [I]: `completed()` still compares `observed_returncode == 0` on a `common.strict` parse (accepts `false`); producer side only (E5-07).

## 6. Own corruption controls, compact verifier, REAL package [E]

In-process (`vc_mine.py`, `verify_payloads(..., 'all')` after `read_payloads`, COMPACT rows and named server hashes rehashed), R12 exit 0, 12.4 CPU s; all 13 as preregistered:

| Control | Outcome / reason |
|---|---|
| VC-0 unmodified | ACCEPT, 280 pairs, complete_plan |
| VC-1 last ledger entry (000279) removed | REJECT `unregistered attempt directory` |
| VC-2 middle ledger entry (000100) removed | REJECT `ledger sequence` |
| VC-3 / VC-4 n41 produce-exit `false` / `'0'` | REJECT `observed pass EXIT0` |
| VC-5 / VC-5b n42 wrapper `0.0` / `true` | REJECT `observed wrapper EXIT0` |
| VC-6 n43 attempt `failed` + server attempt hash | REJECT `completed attempt status` |
| VC-7 n44 fresh tree := n45 tree (receipt, summary, server hash updated) | REJECT `complete tree degree/schema` (checker) |
| VC-8 shadow of engine `checker.py` (trusted bytes) | REJECT `archive shadows trusted package` |
| VC-9 `jobs/999` inventoried | REJECT `unregistered job directory` |
| VC-10 uninventoried extra member | REJECT `exact compact inventory` |
| VC-11 inventoried extra file in unsampled pass dir (diagnostic) | ACCEPT (inventory-exact, not schema-exact; E5-06) |

Transport, end-to-end CLI on rewritten tar.gz (built once, R12t 94 CPU s): VT-1 uninventoried hardlink alias of the 32,675,168-B member → `exact compact inventory`; VT-2 alias before target → `hardlink target must precede alias`; VT-3 symlink and VT-4 directory → `regular/hardlink members only`; VT-5 800 hardlink aliases of that member → `expanded inventory bound before read` (RSS 178 MB: aliases never materialized); VT-6 `jobs/999` under `python3 -O` and normally → `unregistered job directory`. All exit 1 with empty stdout.

## 7. Adapter-dependent results now confirmed without the adapter (coordinator request)

- audit-04 R3a/R3b/R3c (all / none / small) → R4/R6/R5 here, full package, no adapter; R4 bytes equal the recorded root/Astra stdout.
- audit-04 R4 (30 controls) → A4, 30/30, no adapter.
- audit-04 R5 own corruption classes (ledger, status, fresh-tree swap, shadow, job dir, aliases/cap) → my VC/VT controls, no adapter; the fresh-tree swap again rejects at `complete tree degree/schema`.
- The 136 previously unverified header reads (19 headers) in the 199/238 closures are now byte-checked through the real package (R4, A4, VC-0).
- New: the onset reader's `R.pins()` passes on the restored layout and precedes real checker construction (R10).
- **Still adapter-only:** every positive onset-512 reader result (synthetic arithmetic); R10 shows the real checker refuses that fixture. No canonical onset-512 data were available.

## 8. Recipes and provenance wording [I], with probe sensitivity [E]

- `RECHECK-SMALL-BUNDLE.md`: serial cap 7,200 CPU-s, explicit "record a calibration observation" before a full replay, historical calibration (n511 21.73 s; ~3,750 s fit) correctly labelled historical; 3-degree recipe cap 300 s is ample (~45 s by J3-02 timings); exact 942-member coverage enforced; pins checked before import. Uses 41/458/511 whereas WHEN-INPUTS-ARRIVE preregisters 320/384/458/510 — a future audit substitutes its own tuple.
- Deposit README: E4-06 stale pending text fixed (MANIFEST `pending_items[0]` now accurate); `7c2dad53…` (inside padua30.zip, both copies [E]) vs `5867ac0c…` (a433c7d snapshot) vs current `2d26886f…` correctly distinguished (L102–133); runner identity not attributed. The prospective onset command (L170–175) will fail on the canonical ZIP until E5-01 is fixed. L227–231 still calls `24a98db` "the accepted final manuscript baseline" in present tense (superseded by `ad908ac`, L366) — EDITORIAL under the L21–33 historical umbrella.
- Popen/ECHILD: J03 L257–261, summary L61–62 and README L196–198 state precisely that historical worker exits came from Popen, which returns 0 on ECHILD (CPython `_internal_poll`/`_wait` set returncode 0 on `ChildProcessError`), and that completeness rests on 942 accepted rows. Manuscripts make no exit-status claim [I, grep]. Accurate.
- **Runtime probe scope (A2/A3) [E]:** with MXCSR FTZ|DAZ set in the probing thread, `2^-1022/2` is bitwise `0x0` (A3, `view(uint64)`), yet `runtime_probe.main()` reports all four probes true and its 31 controls pass, because its checks are floating-point comparisons that DAZ also flushes. FTZ alone is detected (`gradual_underflow` false); round-toward-zero is detected (`ties_even_up` false); DAZ alone is harmless here. What the probe establishes: in that process, NumPy float64 addition at two tie points rounds to nearest-even (excludes RZ/RD/RU/ties-away for addition), division underflow is gradual unless DAZ is also set, and `nextafter(0,1)` compares equal to the smallest subnormal. What it does not: rounding of mul/sub/div in general or in long-array SIMD loops; FTZ under DAZ; the state of the historical worker processes (prospective only, correctly not backdated); hardware/libm conformance. J03 L264–267 and response-04 J3-05 ("tests ... gradual underflow") overstate detection (E5-04).

## 9. Global generated-output budget (R13) [E]

Classification = `audit-02/code/t2/size.py` (copy `d14439b8…`, read-only `git ls-tree`); full per-path attribution `size_attr.py`.

| Quantity | Bytes |
|---|---:|
| f70a260→70a50d7 head total (E4 R9 reproduction) | 9,895,866 |
| old topic head `8a94ce6` total | 9,895,866 |
| main `b5388c2` total | **9,733,758** (< 10,000,000) |
| merge `941aa33` total; positive vs 8a94ce6 | 11,723,154; +1,827,288 = **all 296 paths in `topics/padua-3d-20261106`** |
| head `33b9eca` total ("actual classified sum") | **11,729,562** |
| post-merge topic growth (notation-renames-audit04.json 3,537 new; MANIFEST.json.in +2,871) | 6,408 |
| 8a94ce6→head positive deltas; bound 9,917,613 + 1,833,696 | 1,833,696; **11,751,309** (reproduced) |
| this topic's counted share at head (= head − main exactly) | **1,995,804** |
| Padua3D share at head | 1,827,288 |
| head total + inherited 2,087 B `code/post_audit_D09_threepoint/FREEZE.md` exception (topic convention, LOG L585/1622) | 11,731,649 |

- **No non-topic file differs from main** at head (all file classes; only `topics/padua-argmax-bridge-20261105/` and `results/padua-argmax-bridge-20261105.md` differ; root `RESULTS.md` unchanged). No unrelated evidence deleted or relabelled. Evidence index R14 `--check` PASS, v4, 396 entries, 32,414 B index, 1,710,416 B (unchanged from E4).
- The 10 MB figure is AC's recorded temporary allowance (LOG L178), superseding WORKFLOW's "well below 5 MB" for now.
- **Limitation (honest attribution):** neither main (9.73 MB) nor the pre-merge topic (9.90 MB) exceeds 10 MB; their union does. Merging PR27 is the step that would take main from 9,733,758 to 11,729,562 B. The records attribute the excess to Padua3D ("most excess arrived from … Padua3D") without stating the topic's own 1,995,804 B (E5-03). I do not suggest deleting other topics' evidence; the global repair is AC's decision.

## 10. Findings

**E5-01 MAJOR — the repaired onset reader rejects files its own campaign producer writes; the required canonical rerun cannot pass as committed.**
- Location: `code/local_onset512_campaign/return_bundle.py:171–181` (`pass_files`, `top`) and `:186–216` (`check_members`), against `compact_pack/storage.py:44` (`(root/'.preserve.lock').open('a+b')`) and `:62` (`exclusive(pass_directory/'storage-dedup.json', …)`), the historical runner `459d0728` L120 / current runner L124 (`deduplicate(output, target)` after every validated pass), and the exporter (historical L105–111, current L131–137: every top-level file and every non-`check-*` case file is added).
- Reason [D]: every one of the 382 successful passes ran `deduplicate`, which unconditionally writes `<pass>/storage-dedup.json` and creates `<output>/.preserve.lock`; the exporter adds both; `check_members` requires `parts[3] ∈ pass_files` (no `storage-dedup.json`) and top-level names `∈ top` (no `.preserve.lock`). [E] R11 RB-a/RB-a2: exactly these names are rejected (`unregistered campaign member: out/.preserve.lock`; `unregistered pass member`). Corroboration [E/D]: the original return's sampled pass directories contain `storage-dedup.json` (data-only listing); the recorded 11,713 members fit 60 members per case (191×60 = 11,460, leaving 253 root-level members) only if `storage-dedup.json` is present (58 per case would leave 635).
- Impact: fail-closed (no false acceptance), but the deposit/summary verification command will reject the canonical ZIP, so E4-01..E4-03 cannot be closed by the planned rerun. The developer's fixture and the supplementary review ("allowlist inferred from frozen producer writes") omitted helper-written outputs.
- Fix: allow and schema-check `storage-dedup.json` (keys `immutable_paths_examined, paths_relinked, logical_bytes_relinked, scope`) and a zero-byte top-level `.preserve.lock`; add a producer→exporter→reader round-trip control that runs the real `storage.deduplicate` and `export()` on a synthetic campaign tree (no engine); focused re-check; then the canonical rerun. Material change.

**E5-02 MINOR — the J01/J02 analytic checker's verdict is removable under optimization.**
- Location: `code/onset512_analytic/check.py` (28 assert nodes; L249 prints `assertions='PASS'` unconditionally); handoff 32 / PREREGISTRATION command `python3 -B` (no `-E`).
- [E] R3o: a scratch copy with the gate falsified (`peak.hi < F(1,1000)`) prints `"assertions": "PASS"`, exit 0, under `PYTHONOPTIMIZE=1`; R3m (same copy, normal) → `AssertionError`, exit 1.
- Impact: none on recorded results (normal-mode runs, including R3, pass with identical enclosures). Same defect class as E4-01 in a proof-bearing checker.
- Fix: document `python3 -E -B` in the rerun commands (wording). Optionally add an optimization guard with a re-pinned identity (that is a material code change).

**E5-03 MINOR — budget attribution omits the topic's own share; "actual" omits the 2,087 B exception.**
- Location: handoff 32 L128–131; LOG L2972–2979 and L3028–3032; `pr-update-20261113.md` L23; deposit README L372–377; MANIFEST `generated_output_bound`.
- Reason: see §9. The figures are correct; the attribution is timeline-dependent and omits that main alone is under the allowance and that this topic contributes 1,995,804 B. "Actual 11,729,562" omits the topic's own 2,087 B FREEZE.md convention (11,731,649), while the bound includes it through its baseline.
- Fix: state both shares, that neither branch alone exceeds 10 MB, and the convention for the 2,087 B. Wording only; fixable in place.

**E5-04 MINOR — the runtime probe's gradual-underflow check is blind to FTZ+DAZ; the records overstate it.**
- Location: `code/independent_phase_checker/runtime_probe.py:21–25`; J03 L264–267; response-04 J3-05.
- [E] A2/A3 (see §8).
- Impact: low. J03 already calls the probe finite evidence, and J3-05 notes that no subnormal arises in the computation.
- Fix: state the exact scope (addition ties; division underflow unless DAZ is also set). Optionally compare `view(np.uint64)` bit patterns instead of floating-point equality (supplementary code, not result-bearing).

**E5-05 NOTE — `verify_compact.py` has no optimization refusal and needs none:** no assert on its path, and R7/A1/VT-6-O behave identically under `-O`/`PYTHONOPTIMIZE`.

**E5-06 NOTE — metadata accepted as data:** the reader accepts inventoried symlink-mode or directory-mode (no slash) ZIP members under allowlisted names; `verify_compact` accepts an inventoried extra file in a pass directory and pins only the manifest, not the archive. Nothing is extracted or executed. Optionally reject non-regular mode bits.

**E5-07 NOTE — export-side `completed()` uses `observed_returncode == 0` on a `common.strict` parse** (accepts `false`). This is the producer path only; the reader enforces integer zero.

**E5-08 EDITORIAL — provenance one-liners.**
- `code/local_onset512_campaign/README.md` should say that the campaign ran `runner.py` `459d0728…` and that the current file (`a198b651…`) has executed no campaign.
- Deposit README L170–175: mark the onset command as expected to fail until E5-01 is fixed.
- Deposit README L227–231: label `24a98db` as historical, superseded by `ad908ac`.

**E5-09 NOTE — the reader is single-archive by construction:** it accepts only degrees 320..510, runner `459d0728` and the default `da63280a` pin. A future campaign by the repaired runner needs new constants and review. This is consistent with non-retroactive attribution.

## 11. Executions (all once; observed exits via wait4; obs in `e5-run/obs/`)

S0 0 (0.58 s) · R1 0 (5.96) · R2 0 (0.17) · R3 0 (0.26) · R3m 1 / R3o 0 · R4 0 (6.08) · R5 1 · R6 0 · R7 0 · R8a–e 1 (refusal) · R8f/g/h 1 · R9 0 (1.18) · R10 0 (spy run; reader REJECTED) / R10b 1 · R11 0 (3.73; 17/17 as preregistered) · R12 0 (12.36; 13/13) · R12t 0 (94.2) · VT-1..5 1 · VT-6-O 1 · VT-6-normal 1 (comparison, recorded in A1) · R14 0 · A1a-i/ii 1 · A1b 1 · A2 0 (probe sensitivity) · A3 0 · A4 0 (16.5). Unobserved, data-only/read-only: tar member listings and the `size.py`/`size_attr.py` `git ls-tree` runs (R13).
Code (`e5-code/`): observe `b13bd6fb…`, pkg_auth `e485a79c…`, r9_compat `c1ed915d…`, rb_real `f1cf623e…`, rb_mine `ced9924e…`, vc_mine `8cea6f58…`, vt_build `437044ec…`, size_attr `72d24765…`, probe_sens `481c7ebb…`, bits_readout `51a83e79…`, mxcsr.c `848e6904…`.
Reports (`e5-run/`): S0 `e61a251e…`, R9 `01d66ffa…`, R10 `b65937dd…`, R11 `ca958807…`, R12 `5402bcdb…`, R13 `eeceebfa…`, A2 `969f8543…`, A4 `ca08e1a0…`.

## 12. Limits

- Absent: canonical `onset512-return-20261108.zip` (`da63280a…`), certificate derivative (`c22d600c…`), mirror inventory (`d7cea34d…`), I25 bundle (`d1d03156…`), review ZIP (`96f84b29…`), historical PDFs and the 632 MiB native histories. WHEN-INPUTS-ARRIVE steps 2–5 remain unexecuted, and step 2 additionally needs the E5-01 fix.
- E5-01 is derived from code plus a member-count consistency check, not observed on the canonical ZIP.
- Onset-reader positives are adapter-only.
- No native, engine, Syvert or remote execution. The `gcc` helper only sets or reads MXCSR.
- Python 3.13.18 / NumPy 2.5.3 here, not the recorded 3.12.14 / 2.3.5.
- Manuscript scope is not covered by this part.
