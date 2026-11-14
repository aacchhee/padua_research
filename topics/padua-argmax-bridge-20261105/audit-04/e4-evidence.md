# Audit-04 part E4: new finite evidence, verifier repair, I25 outer accounting, custody

- **Auditor:** Claude Opus 5.5, xhigh. This is an adversarial operational and evidence audit under handoff 30.
- **Role:** independent auditor subagent. It made no Git state change and wrote nothing to the repository. `git status --porcelain` was empty before and after, and HEAD stayed unchanged.
- **Rules:** AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md, read at head `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9`. The handoff input head is `f4c6229871a494b1b859d3140e81e9eb48b6b56a`.
- **Brief:** handoff 30 and `claude-audit-brief-onset512-20261108.md`, sections "Evidence identities" and "Focused operational checks".
- **Novelty:** this scope has no novelty content, so the full read of `state/IDEAS.md` is omitted.
- **Labels:** [E] means my own execution here. [D] means derived from code or records. [I] means inspection only.
- **Outputs:** this file, plus `e4-code/` (all auditor scripts) and `e4-run/` (copies, obs/*.observation.json, reports).
- **Preregistration:** `e4-run/PREREG-01.md`, SHA-256 a6fdc15f…, saved at 13:01:46Z, before R1. CPU used: 102.8 s observed child CPU in total.

## 1. Verdict (scoped)

| Task | Verdict |
|---|---|
| 1. New 320..510 evidence | **Not yet accepted by this audit.** I find **one MAJOR** (E4-01, a demonstrated fail-open in the data-only reader) and MINORs. The actual ZIP checks are **BLOCKED** because the artifacts are absent. The engine and FREEZE are unchanged [E]. The sandbox-only protocol was respected per code and records [I]. |
| 2. E-01..E-04 repair | **Accepted** for source candidate `5867ac0c…`. My own reruns on the old actual return, the 30 controls and 20 of my 21 own rehashed corruptions behave as required. The remaining case (C5b) was also rejected, but for a different reason than I preregistered. MINOR E4-04. The historical package verifier is unchanged and unrepaired [E], and the records attribute the repair correctly. |
| 3. I25 outer accounting | **Consistent** with the committed records [E]. MINOR E4-05. Bundle authentication and the 942-proof comparison are **BLOCKED**. |
| 4. Deposit and custody | Accepted **as preparation only**. The source snapshot is reproduced byte-exact [E]. The index check passes [E]. The size bound reproduces [E]. Custody verify is vacuous (0 entries) [E]. MINOR E4-06/E4-07. |
| 5. Honesty | No misreported execution found. Two wording or evidence-scope items (E4-05, E4-08). |

The topic should return to WORK for E4-01: a small, material verifier fix that needs a focused re-review. No finding refutes a recorded result. The recorded developer and Astra runs of the reader very probably ran with asserts active, because Astra's in-process corruption controls rejected. I25 independently recertifies all 382 new trees.

## 2. Inputs and availability

- `audit4/inputs/` was empty at start and at end, and no matching artifact exists anywhere on this filesystem [E]. Absent: the canonical `onset512-return-20261108.zip`, `onset512-certificates-20261108.zip`, the essential inventory, the I25 bundle, the review ZIP and `padua30.zip`.
- Original return: rehashed [E] at 36,045,486 B, SHA-256 `b00fd57f…109a`. Its runtime_manifest member hashes to 54,003 B, `5b89fa66…2a16` [E].
- Trusted sources: read-only `git archive` copies of HEAD (`e4-run/tree-head`) and of `996fedc` (`tree-996`).
- Trusted package rebuild (R2): uses audit-03's `rebuild_package.py`, byte-identical (`fbc0adb6…`). Result: 38 git, 24 git-copy, 2 regenerated and 9 archive-hash-matched rows, all authenticated. **177 rows are absent:** the 6 `.deb` files and 171 headers. R1 tried one GET per pinned package at deb.debian.org, and the session proxy returned **403** for all 6. Per the preregistration there was no retry and no second source, so I used the audit-03 absent-file adapter (`e4-code/e4_harness.py` header):
  - manifest checking tolerates exactly those rows, and every present row is still checked;
  - `Access.identity` records, instead of raising on, reads of exactly those absent names.

  Under R3 this left 136 reads of 19 headers unverified, identical to audit-03.

## 3. Task 1 — new 320..510 evidence (source audit; ZIP checks blocked)

**Freeze and engine [E]:**
- `git diff f366535 HEAD -- code/final_hybrid_engine/` is empty, and so is the diff from `996fedc` to HEAD.
- The FREEZE SHA is `0d9ce0a5…` in HEAD, in 996fedc and in the rebuilt package. All 13 `code_data` rows match in all three.
- Since b45e29f the only change in compact_pack is `verify_compact.py`, which the runner does not import. The helpers the campaign imported (process_guard, ownership, evidence, storage, common, plans) are therefore unchanged.

**Pins [E]:**
- The current runner hashes to `459d0728…`, equal to the preregistered runner.
- The reader `return_bundle.py` hashes to `d1dba234…`, equal to the reviewed exporter/verifier.

**Protocol [I]/[D]:**
- AC's decision (handoff 29, item 1) was: run "in your own environment with the pinned runtime … Syvert is not required". The LOG at line 2718 records the sandbox-only choice.
- The runner has no network or remote path. The engine runs with `-E -S -B` and `LD_LIBRARY_PATH` set to the pinned extracted arithmetic directory.
- The in-flight `validate_pass` requires the mapped flint/gmp/mpfr libraries to be the pinned hashes. The compiler, toolchain and Python are recorded identities but not pinned (E4-09).
- The worker observes exits with `os.wait4` (`observe()`). The flag `'ECHILD': True` is a literal, but it is justified by control flow: `ownership.cleanup()` raises unless ECHILD is reached with no descendants.
- Output and admission files are created exclusively (`open('x')`). A failure stops further admissions. There is no retry or resume entry point.
- Git chronology: runner.py and the preregistration markdown were first committed at 0c29ba2 (10:51:02Z), after the pilot and while "remaining" was running. This is disclosed in the LOG at line 2722 ("It is running"). Pre-execution status therefore rests on the off-Git `preregistration.json` (`532e5af6…`): every per-case and per-stage admission embeds its identity, and the reader checks that for all 191 cases. Confirming this needs the ZIP (E4-08).

**Reader `return_bundle.verify` [I] plus synthetic negative controls [E] (R6, `e4-code/rb_controls.py`):**
- The canonical ZIP is absent, so I make **no positive claim**.
- With asserts active, all of the following reject: `../x`, `/x`, `./x`, `a//b`, a directory entry, a duplicate name, a missing COMPACT.json, an inventory hash mismatch, and a trusted-name shadow of the engine's `checker.py` with correct bytes ("archive shadows trusted package").
- A member declared at 513 MiB is rejected **before any read** (0 members read). Five 450 MiB members are rejected **before reading the 5th** (4 read).
- A symlink-typed member is treated as data and never extracted. It is not rejected at the member check (E4-09).
- A forged empty-degree ZIP is rejected at line 166 (`reg['degrees']==…==range(320,511)`).
- Namespace separation holds: payload names must be disjoint from the trusted manifest, and trusted names are always served from the repository with a hash check.

**Fail-open probe (E4-01) [E]:**
- I used the same forged ZIP: 26,529 B, `ee1f89f4…`, containing **no certificate at all**, run through the documented `python3 -B …/return_bundle.py verify` command.
- With `PYTHONOPTIMIZE=1` in the environment the command exits **0**. With `python3 -O -B` it also exits **0**.
- In both cases it prints `{"status":"accepted_pending_independent_review","pairs":191,"proofs":382,"sample":[]…}`.
- Normal mode exits 1 at line 166.
- Context for the probe:
  - The runtime copy that `R.pins()` reads was staged in the scratch tree.
  - The 171 absent headers were replaced there by marked placeholders. Their hash asserts are stripped under `-O`, which is part of the same defect.

**Linkage review [I]:**
- For every pass the reader checks:
  - n and freeze;
  - `verify_essential` (inside an `assert`);
  - exit, accounting, summary, label and CPU caps;
  - raw identity;
  - that python is mapped;
  - the exact engine command;
  - the local-validation identities;
  - equality of the COMPARE fields;
  - produce receipt == verify/original-certificate;
  - attempt failure is None, with passes equal to the exit records;
  - admission bound to the preregistration identity;
  - wrapper exit;
  - stage admissions and summaries, with summary rows equal to the wrapper files;
  - helper pins.
- `validate_pass` runs only for the two sampled degrees.
- Parity gaps against the repaired compact verifier are listed in E4-03.

**Blocked [precise]:**
- the documented verify run on the actual ZIP;
- independent rehash and inspection of its 11,713 members;
- coverage of 191 pairs and 382 passes, EXIT0/ECHILD, and absence of retry, timeout or cleanup kill as recorded;
- complete histories for the sampled degrees 475 and 458, and the seed → draw;
- byte equality of the certificate ZIP with the inventory;
- runtime and pin records inside the ZIP.

Even if the ZIP arrives, the reader cannot pass here without the complete trusted package: `R.pins()` reads all 171 headers. `padua30.zip` (25,111,335 B, `aac08e5f…`) is needed too. Exact next commands are in `e4-code/WHEN-INPUTS-ARRIVE.md`. I precomputed `e4-run/old560-receipt-identities.json`: all 560 old receipts, an exact match of 41..319 plus 511 [E].

## 4. Task 2 — E-01..E-04 repair (actual old return; own reruns)

The patch was inspected [I] (`git diff f366535 HEAD`, 144 lines added and 60 removed). The changes are:
- **Package authentication first:** frozen manifest SHA, then `manifest()`, then `Access`, which loads the checker.
- **Namespace:** `receipt['files']` must be disjoint from the trusted manifest. The reader forces ENGINE/, asset_provenance and manifest names to the package.
- **History reuse:** `archive_io.verify_admissions`/`verify_history` are reused through `PayloadView`.
- **Run-level checks:** started binding; summary result, first_failure and receipt identity; the freeze triple; exact commands; fresh primary path linkage; `check_replay_shape`. Exact server-validation coverage, plus attempt, receipt and raw hashes.
- **Plan coverage:** `--expect-plan` gives exact plan coverage.
- **Size bound:** a cumulative logical bound before each regular read or alias addition.

| Run [E] | Command (under the adapter, `python3 -I -S -B`) | Exit | CPU s | Result |
|---|---|---:|---:|---|
| R3a | `verify RET --package PKG --manifest-sha 5b89fa66… --expect-plan all` | 0 | 6.64 | 280 pairs, exactly 41..319 plus 511, sample [199,238] |
| R3b | same, no `--expect-plan` | 0 | 6.47 | identical output JSON (see E4-04) |
| R3c | `--expect-plan small` | 1 | 1.22 | "expected complete plan coverage" |
| R4 | `code/compact_verifier_audit03/check.py` (new output path) | 0 | 16.26 | **30/30 controls**: 28 rejected for the named reason, 2 accepted as designed. Receipt `bcb7ee40…` |

**Own rehashed corruptions (R5, `e4-code/e4_harness.py mine`) [E]:**
- **Baseline:** the unmodified payloads with `--expect-plan all` are accepted.
- **Rejected:**
  - C1: ledger *last* entry removed → "unregistered attempt directory".
  - C2: ledger *middle* entry removed → "ledger sequence".
  - C3: attempt `status="failed"`, with the server attempt hash also rehashed → "completed attempt status".
  - C4: summary receipt *path* altered, bytes and SHA kept → "summary receipt identity".
  - C5a: fresh tree replaced by the n=42 tree → "fresh retained tree".
  - C5b: the fresh receipt's tree swapped, with all identities and server hashes updated → rejected, but at "complete tree degree/schema" in the rational checker. I preregistered "exact rational reconstruction", so this is recorded as a reason mismatch. It is fail-closed.
  - C5c: the fresh receipt replaced by n=42's → "essential degree/size".
  - C6: degree 41 dropped consistently under `all` → "expected complete plan coverage".
  - C6c: degree dropped but its validation row kept → "exact server validation coverage".
  - C7: never_started edited → rejected.
  - C8: trusted shadows of `checker.py`, top-level `common.py` and `compact_pack/evidence.py` → "archive shadows trusted package".
  - C9: archive-supplied `ENGINE/evil.py` referenced from a sampled record → "unmanifested trusted source".
  - C10: job directory 999 → "unregistered job directory".
- **Production 24 GiB cap, unpatched:**
  - C12a: one 512 MiB member plus 47 aliases, then a 48th alias → rejected.
  - C12b: the same 47 aliases, then a 1-byte regular member → rejected. In both, only `big` was ever extracted.
- **Diagnostics:**
  - C6b: dropping degree 41 consistently is accepted in default subset mode, with 279 pairs. This is documented behaviour, but see E4-04.
  - **C11:** a rehashed `observed_returncode: false` is **accepted** (E4-04).
- **Historical package verifier `7c2dad53…`:** it **accepts** H1 (attempt status altered), H2 (summary receipt path altered) and H3 (shadow `common.py`). So the repair is real, and it cannot be attributed to the historical release, which still authenticates its old verifier.

## 5. Task 3 — I25 outer accounting (committed records only)

R10 (`e4-code/i25_outer.py`) [E] confirms all of the following on the committed records:
- `range(41+j,512,4)` gives 118/118/118/117 degrees, disjoint, with union exactly 41..511.
- 942 = 2·471 = 560 + 382.
- Worker exits are [0,0,0,0] and the outer exit is 0.
- CPU 2519.42 is below 10800, and wall 646.84 is below 7200.
- 43116 = 2·21558 and 1290 = 2·645, with 645 = 3·|41..255|.
- 42174 + 942 = 43116.
- The RESULTS source pins equal both the preregistration and the HEAD files (`1501ce94…`, `c1810bd1…`, `c55b77d2…`, `8779ab2a…`), and the preregistration and amendment hashes equal the brief.

Code review [I]:
- `run.py` authenticates the old tar SHA, the exact 560 regex-matched members, the pinned new inventory, the 382 names and their content, and the complete 942 set before filtering.
- `launch_full.py` rejects unless there are exactly 942 accepted rows over the expected union and total CPU is at most 10800.
- The worker exits come from stdlib `Popen` (E4-05).

`check.need` raises ValueError and the I25 sources contain no asserts [E grep].

**Blocked:** authenticating the bundle (2,843,611 B, `d1d03156…`). `bundle.sh` shows that its 560 old proofs are byte copies of the pinned tar's essential receipts, so a byte comparison against my precomputed table is ready to run.

## 6. Task 4 — deposit and custody

- **R8 [E].** I ran the README's exact `git archive --format=zip --prefix=padua_research-a433c7d/ … a433c7d` (git 2.43.0) with output in scratch. The result is **22,105,198 B, SHA-256 `66acbadb…cc03`**, byte-identical to the inventory. It has 7,586 entries (6,900 files, equal to `git ls-tree -r a433c7d`), passes `testzip`, and its comment is the commit SHA. After a433c7d only prose, records, deposit text and handoffs changed. No code changed.
- **R7 [E].** From the copy, `python3 -B …/code/evidence_index.py --check` gives **PASS**: v4 schema, 396 entries, index 32,414 B, 1,710,416 B indexed.
- **R7c [E].** `python3 -B tools/cold_storage.py verify padua-argmax-bridge-20261105` (read-only, in the repository) gives exit 0, `entries: 0, bytes: 0, accepted: true`. This is **vacuous**: it proves index and source compatibility only. The tool needs a .git directory, so it cannot run from a git-archive copy (R7b, exit 1).
- **R9 [E].** `audit-02/code/t2/size.py f70a260 70a50d7` gives a head_total of 9,895,866 B. Adding the inherited 2,087 B FREEZE charge gives **9,897,953 B, exactly the recorded bound**, below 10,000,000 B. Over b45e29f→HEAD the net change is +23,997 B and the positive deltas are +43,657 B (see E4-07). Since the base, the only new or changed generated-class file above 16 KiB is `evidence-manifest.json` (32,414 B, the reviewed exception).
- **Deposit preparation is not custody** [I]:
  - `MANIFEST.json.in` is `DRAFT_TEMPLATE_NOT_A_DEPOSIT_RECEIPT`, with DOI `PENDING_AC_RESERVATION`.
  - cold-storage.json has `entries: []`, `total_bytes: 0` and `completed_external_delivery_receipt: null`.
  - Neither a Zenodo upload, a DOI, a Windows delivery nor a remote retrieval is evidenced. The custody-tool smoke shows none of these.

**Unresolved data-access limits:**
1. All off-Git payloads except the old return are unavailable to this audit.
2. The pinned Debian packages are unreachable here (proxy 403). Verification needs `padua30.zip`, and a deposit user depends on it or on Debian/snapshot availability.
3. There is no delivered cold storage, Zenodo record or DOI.
4. The 632 MiB of unsampled complete native histories for 320..510 exist only in the Codex sandbox campaign tree. That tree is ephemeral and has no custody or deposit entry.
5. The old return's unsampled histories exist as server-recorded identities only (deleted under AC's waiver).
6. The Astra review scratch in `/tmp/onset512-independent-review` survives only inside the absent 51,749 B review ZIP.

## 7. Task 5 — honesty (executed versus inspected)

**Recorded executions, consistent with the code [D]:**
- the developer campaign (382 passes);
- the export and two verify runs, the second relocated;
- `verify_compact` and check.py on the full package, with no adapter;
- the I25 full run;
- the bundle and snapshot exports.

**Distinct Astra executions [I], none native:**
- the Fraction checker;
- synthetic scalar and interval controls;
- runner `controls`;
- its own campaign_accounting and inventory checks;
- the actual-ZIP `return_bundle verify`, exit 0;
- 12 in-memory ZIP corruptions through a synthetic reader adapter, all rejected;
- `verify_compact --expect-plan all` and the 30 controls;
- custody readback and the vacuous custody verify;
- `full_records.py`;
- one prospective six-certificate I25 replay (41, 458, 511, exit 0).

The Astra record states clearly that "No native process was rerun".

For 320..510 there is therefore **no independent native replay**, which is by design. The independent arithmetic is the developer-run I25 over all 382 trees. A distinct reviewer executed it only for n=458 (both passes).

No record I read claims an execution that did not occur. Disclosed failures are preserved:
- the `/usr/bin/time` exit 127;
- Astra's two failed record readers;
- the I25 pilot-v1 failure;
- the early BadZipFile readback.

The "no Syvert / remote" requirement was complied with per the records and code.

## 8. Findings

**E4-01 MAJOR: the data-only reader fails open under Python optimization.**
- **Location:** `code/local_onset512_campaign/return_bundle.py`. Lines 139–222: every check, 47 `assert` statements (67 in the file). Line 223: an unconditional print of constants. The documented command appears in local-onset512-summary.md:97–99, zenodo-deposit/README.md:126–127 and the ZIP's own README.txt (return_bundle.py:100).
- **Reason:** with `-O`, or with `PYTHONOPTIMIZE` set (the documented `python3 -B` does not use `-E`/`-I`), every check including `verify_essential` is stripped. A forged zero-certificate ZIP is accepted with exit 0 and the output "191 pairs/382 proofs" [E].
- **Impact:** the deposit-facing verification route for the canonical 320..510 return can report success without verifying anything, and the output cannot reveal this. It does not refute the recorded runs (see §1).
- **Fix:**
  - Replace the asserts with a raising `require`, and refuse to run when `sys.flags.optimize` is set.
  - Compute the printed counts from verified data, and print the reader's own SHA.
  - Document `python3 -E -B`. `-I` would need an explicit `sys.path` insert, as in verify_compact.
  - Apply the same fix to `runner.pins()`/`run()` and to the `assert` pin lines in `zenodo-deposit/RECHECK-SMALL-BUNDLE.md`.
  - This is a material change: run a focused re-review, with an actual-ZIP rerun of the repaired reader.

**E4-02 MINOR: trust anchoring and ordering in the reader.**
- **Location:** return_bundle.py:151–155 and :164–169.
- **Reason:** the trusted runtime manifest is authenticated only by equality with the archive's own `trusted_manifest` claim. There is no external pin of `5b89fa66…` or of the archive SHA `da63280a…`, unlike verify_compact's required `--manifest-sha`. `Access()` executes the checkout's `checker.py` before `R.pins()` authenticates the FREEZE rows. That is the ordering E-01 repaired in verify_compact.
- **Impact:** safe only if the user verifies the ZIP SHA externally first.
- **Fix:** require the pins as arguments or constants, and authenticate before constructing `Access`.

**E4-03 MINOR: reader linkage parity with E-02.**
- **Location:** return_bundle.py:176–209.
- **Reason:** for the 189 unsampled pairs the reader does not check:
  - `summary['essential_receipt']`;
  - the verify pass's `engine_config.certificate_identity`/`certificate` against the primary bytes and path;
  - `attempt['status']`;
  - `reg['runner']` against the committed `459d0728…`.

  It also accepts unregistered extra members, for example `jobs/<n>` outside 320..510 or a `failure.txt`, because only inventory equals payload is required. Its truthiness and `==0` checks accept non-boolean or false-typed values.
- **Fix:** add these checks, using `is True` and type checks.

**E4-04 MINOR: type confusion and coverage-mode reporting in verify_compact.**
- **Location:** verify_compact.py:23 and :51, and the result dict at :192–194.
- **Reason:** a rehashed `observed_returncode: false` is accepted (C11 [E]). The result JSON for `--expect-plan all` and for the default subset mode is identical (R3a/R3b [E]), and C6b shows that subset mode silently accepts 279 pairs.
- **Fix:** require `type(x) is int and x == 0`, and add `expect_plan` and an explicit coverage-mode field to the result.

**E4-05 MINOR: I25 worker exits are stdlib-derived.**
- **Location:** code/independent_phase_checker/launch_full.py (`subprocess.Popen.poll/wait`, no `normalize_startup`). RESULTS.json `worker_exits` and the summary's "All four workers exited 0".
- **Reason:** the stdlib maps ECHILD to returncode 0. That is the PA1/PA2 hazard the project's own rule excludes ("ECHILD cannot imply EXIT0"), and the SIGCHLD disposition is not recorded.
- **Impact:** low. Acceptance also requires 942 accepted rows over the exact union, plus the per-worker controls and summaries.
- **Fix:** word it as "stdlib returncode 0; completeness by 942 rows", or use `process_guard` in future runs. No rerun is needed.

**E4-06 MINOR: stale or contradictory deposit text, and a missing verifier warning.**
- **Stale text:** `MANIFEST.json.in` pending_items[0] says the source snapshot "remains to be packaged and hashed after substantive audit", while its row is populated. README:252–253 also says the source ZIP is pending, contradicting README:289. The role `final_reviewed_repository_source_snapshot` predates this substantive audit.
- **Missing warning:** the deposit README pins neither the reviewed repaired verifier (`5867ac0c…`, inside snapshot a433c7d) nor warns that the deposited `original-padua30.zip` carries the historical verifier `7c2dad53…`, which accepts H1–H3 [E].
- **Fix:** one-line edits.

**E4-07 MINOR: size-bound convention.**
- **Reason:** 9,897,953 B is the current-tree total. It takes credit for shrinking cold-storage.json from 23,904 B to 4,244 B. This topic's earlier bounds (LOG:1591, 1622) used "all positive deltas, no deletion credit". Under that convention the bound is 9,873,956 + 43,657 = **9,917,613 B** (82,387 B headroom). Both are below the cap, and neither is "well below".
- **Fix:** state the convention once.

**E4-08 NOTE: in-flight enforcement is not recorded.** The runner's per-case pin checks, exit and fresh-equality asserts and the stage-entry runner check run in a `python3 -B` wrapper, and `sys.flags` is not recorded. They write no per-case record, so the summary statement "pins checked before/after each case" is code-supported but not record-evidenced. The records the reader checks do not depend on them. The prospective status of the preregistration rests on the admission identities (§3).

**E4-09 NOTE: residual bounds.**
- `tarfile` reads PAX/GNU long-header blocks before yielding a member. E-04's "before read" bound therefore covers payloads and aliases, not header metadata; the effect is memory DoS and fail-closed [I].
- ZIP symlink-typed members are data [E].
- Fresh key sets are compared as sets, and duplicates are left to the rational checker.
- The compiler, toolchain and Python are recorded but not pinned.

**E4-10 NOTE (for the J03 reviewer).** Exactly one stored S upper per certificate (942/942) fails `new ≤ stored` (RESULTS.json [D]). The pattern is systematic. Naming that key in J03 would make the diagnostic interpretable.

**E4-11 NOTE: independent rerun coverage for 320..510.** A distinct reviewer has executed arithmetic only for n=458. This audit's independent reruns of the actual ZIP, the certificate ZIP, the inventory and the I25 bundle are blocked (§3, §5). Substantive acceptance of the new finite evidence awaits those artifacts and `padua30.zip`.

## 9. Execution record

All runs used `e4-code/observe.py`: fork/exec, `os.wait4`, SIGCHLD asserted default, wall cap, and ECHILD after every run. Each command ran once.

| Label | Exit | Child CPU s | Wall s | Max RSS KiB |
|---|---:|---:|---:|---:|
| R2-rebuild | 0 | 1.24 | 1.25 | 129,520 |
| R3-all | 0 | 6.64 | 6.68 | 184,652 |
| R3-none | 0 | 6.47 | 6.56 | 184,580 |
| R3-small | 1 (expected) | 1.22 | 1.23 | 184,584 |
| R4-check | 0 | 16.26 | 16.38 | 184,768 |
| R5-mine | 1 (the C5b reason mismatch only; all corruptions rejected) | 60.49 | 60.85 | 1,721,072 |
| R6-controls | 0 | 7.85 | 7.92 | 2,331,248 |
| R6-probe-normal | 1 | 0.08 | 0.08 | 21,440 |
| R6-probe-envopt (`PYTHONOPTIMIZE=1`) | **0** | 0.30 | 0.32 | 34,360 |
| R6-probe-dashO (`-O`) | **0** | 0.29 | 0.29 | 34,456 |
| R7-index | 0 | 0.07 | 0.08 | 16,880 |
| R7b-coldtool (copy, no .git) | 1 | 0.05 | 0.06 | 17,872 |
| R7c-coldtool (repo, read-only) | 0 | 0.06 | 0.06 | 19,608 |
| R8-snapshot | 0 | 1.75 | 1.78 | 49,108 |
| R10-i25-outer | 0 | 0.03 | 0.04 | 14,304 |

Three runs did not go through the observer:
- R1: curl via `subprocess.run`, all six 403. The log is in `e4-run/debs/R1.log`.
- R9: size.py, read-only `git ls-tree`.
- The old-receipt hash table.

**Report hashes:** R5 `2b6756fb…`, R6 `4d8a5f76…`, check receipt `bcb7ee40…`.

## 10. Limits

- No canonical new ZIP, certificate ZIP, inventory, I25 bundle, review ZIP or `padua30.zip` was available.
- Reruns of the repaired compact verifier needed an adapter for 177 network-only package rows. Under it, 136 reads of 19 headers in the sampled closures are not byte-checked.
- The return_bundle controls are negative-only and synthetic. The fail-open probe used header placeholders in a scratch tree.
- I25 arithmetic, J01/J02 and the manuscripts are outside this part.
- No native, compiler, Syvert or remote computation ran. No retry or rescue was made.
