# T2 — INTERIM Claude audit of the concrete Syvert2 pack (artifact and source)

Auditor: Claude Opus 5.5, xhigh (adversarial protocol/technical audit, handoff 10, task 2 only).
Role: independent auditor subagent. No git state change, no repository edit (one accidental
ignored-cache write disclosed in section 7). Rules read at the branch head
`1b6aa31ae759022ce89bb8a3be70a881790e259f` (AGENTS.md, agents/WORKFLOW.md,
agents/claude/CLAUDE_ROLES.md). No novelty content in this scope (operational pack audit),
so the full `state/IDEAS.md` read is omitted for this part; the ideas task is separate.

Labels: [E] own execution in this session; [D] derivation from code/records; [I] inspection only.

## 0. Audited identities and hard limitation

- Branch head 1b6aa31; pack/engine/review code byte-identical between build source
  `498f4f4c896d9b4a3ac1b5603b27e5fa21b58aeb` and head (`git diff --stat` empty) [E].
- `syvert2_pack/CANDIDATE.sha256` (SHA256 a6a0f1f9…) verifies all 16 files [E]; hybrid
  `FREEZE.json` SHA256 0d9ce0a5…eb, all 13 code_data rows match bytes/SHA [E];
  `code/final_hybrid_engine/AUDIT.sha256` 9/9 OK [E].
- Controls 03 ran at 1e62afbe; between 1e62afbe and head only build_pack.py, README.md and
  CANDIDATE.sha256 changed (FOPS-10); operations code exercised by 03 is unchanged [E].
- Prose hashes quoted in the handoff match: final-syvert2-pack review 9267aa77…, hybrid-engine
  review f812fd44…, E14 review 25529c8a…; all evidence receipts/observations match their
  recorded SHA256 (01 9b3bfc08…, 02 dbfb8254…, 03 0369e984…, genuine 280a988d…, builder
  observation b6ae50b9…) [E].
- **The ZIP (25,104,521 B, SHA256 8274249f…e38b), its 239 entries, the 50,509 B runtime
  manifest, the six .deb files and all of `local-output/` are absent from this checkout.** I
  could not inspect the actual archive. Archive claims below are audited through the build
  recipe and the recorded independent inspection only [I]. Download of the six Debian pins
  was attempted (HEAD only) and refused by the session egress proxy (403 on deb.debian.org);
  per proxy policy I did not retry. Pin hashes, header/library counts and the GLIBC_2.38
  requirement are therefore not independently tested here.

## 1. Verdict

**No BLOCKING finding in this scope.** The scientific reduction (7 + 273 = 280, exact
residual set) is correct, the cap/first-failure/replay/verifier logic exists in code (not only
prose), and my independent rerun of operational controls 03 reproduced all 67 recorded events
exactly. **Four MAJOR findings** should be dispositioned before any Syvert2 release; A1 and
A2 are concrete code defects demonstrated with synthetic fake-worker controls; A3 is a
planning decision for AC/root; A4 is a missing pre-release integration execution. Six MINOR
and several NOTE items follow. Branch stays WORK; this is not a readiness or release decision.

## 2. Findings

### A1 — MAJOR: "directly observed EXIT0" can be fabricated by an inherited SIGCHLD=SIG_IGN

`server.py:102,110-113` (proc.poll), `job_worker.py:149-151` (active.wait) and the engine's
`stage_run` (`engine.py:113,128`) all rely on CPython `subprocess`. CPython converts
`ECHILD` from waitpid into `returncode = 0` (`_internal_poll`/`_try_wait`). An ignored SIGCHLD
survives `execve` (only caught handlers are reset; `restore_signals` resets only SIGPIPE/XFSZ),
so if `beregning`, a shell or a batch wrapper starts the launcher with SIGCHLD ignored, the
kernel auto-reaps children and every observed exit becomes 0; `cleanup()`'s `wait4(-1)` also
reaches ECHILD trivially. Nothing in preflight records or refuses this disposition.

[E] Auditor control `x_controls.py` (fake worker only, copied tree): fake case 41 exits 7.
With default SIGCHLD: `wrapper-exit observed_returncode 7`, first failure "case 41 failed".
With SIGCHLD ignored in the supervisor: `observed_returncode 0` for case 41, run returns
normally, summary `first_failure null, quiescent true`. Exit 0 both runs, <0.2 CPU s.

Impact: per-attempt proof data still has to validate (`evidence.py:69-155`), so a false
proof is not accepted by this alone; but the mandatory independent signal "observed EXIT0"
(the very limitation preserved for the historical D36 primary) is silently forgeable, and an
engine/worker killed after writing complete-looking files (e.g. at a final RLIMIT boundary or
during teardown) would pass. Fix (two lines + control): `signal.signal(SIGCHLD, SIG_DFL)` at
the top of `server.py` and `job_worker.py` before any Popen (children then inherit default),
record the inherited disposition in preflight provenance, and add a synthetic control.

### A2 — MAJOR: ordinary events leave supported paths with no exit except an unspecified manual recovery

Each case below is fail-closed (good), but several are common operational events, and the
only way to produce a verifiable return afterwards would be hand-writing `COLLECTION.json`
with `quiescent: true` — exactly the attestation the protocol exists to prevent.

1. **Reboot** [E]: after a complete, strictly quiescent synthetic run, a changed `boot_id`
   makes `collect()` refuse forever (`ValueError('writer domain boot mismatch…')`;
   `ownership.py:84-85,99` via `server.py:175`); admission/resume of every group is refused
   too. The boot/birth floor was introduced for the removed environment scan (FOPS-07);
   after a reboot no writer of the previous boot can exist, so collection (not admission)
   across a boot change is safe if all groups were already true, and a recorded supervised
   `recover`/collect-after-reboot path is needed for false groups.
2. **SIGHUP** [E]: only SIGINT/SIGTERM are handled (`server.py:81-86`). A terminal/ssh
   hang-up kills the supervisor by default action; summary stays false (phase still
   "preflight"), and the case worker (own session, `start_new_session=True`) keeps running
   unsupervised (observed alive; the 2120 s case-wall guard lives only in the supervisor).
   README gives no nohup/tmux instruction. Fix: treat SIGHUP/SIGQUIT like SIGTERM; add
   `PR_SET_PDEATHSIG(SIGKILL)` in `job_worker.py` (check `getppid()` after setting).
3. **Recoverable preflight failure bricks the group** [E] (`x_preflight_brick.py`): a fake
   free-space-floor failure leaves `run.json` with `provenance: null` and a true summary;
   thereafter fresh run → "fresh/resume output mismatch" (`server.py:54`) and resume →
   "resume lacks original selected-core provenance" (`server.py:57-60`), even after the
   precondition is fixed; `./run` is also blocked by the overlap guard (`server.py:49-51`).
   Hostname, `module load`, missing `ldd`/`c++`, disk floor or loader errors all take this
   path. The undocumented remedy is a fresh unpack (new package_root identity).
4. Resume is practically unreachable (see B6), so after any stop the large group in that
   directory is finished.

### A3 — MAJOR (decision required, not a code defect): stop-on-first-failure vs 273 OPEN degrees

This semantics is a frozen D40 obligation (`independent-checks-D40-syvert2-pack.md:61`) and
the code implements it faithfully [I]. Consequences for this campaign [D]: one per-degree
non-certification (e.g. 256-S cap, 2047-node cap, 15/10-CPU call stop — plausible somewhere in
161–191, where neither the n>=192 far nor the n>=256 corner premise exists) stops admissions,
terminates up to 39 in-flight cases into permanently non-reusable failed attempts, and the
plan cannot be narrowed without a source change and a new ZIP. Moreover `verify_return.py`
is all-or-nothing (`:42-45` requires `first_failure None`/`never_started []`; `:53` requires
exact 280 coverage), so no completed subset of a stopped campaign can be data-validated by
the shipped verifier. Recommend that AC/root decide explicitly before release whether to (a)
keep this knowingly, or (b) distinguish operational failure (stop) from a scientific terminal
non-certification (record, continue, never retry), and in either case add a partial-return
mode that runs `validate_attempt` per started case and reports coverage without claiming it.
bttb A/B/C keeps completed terminal outcomes and continues (`syvert-reference.md:42`).

### A4 — MAJOR (pre-release): the real `job_worker.py` → engine path has never executed

Every operational control replaces `job_worker.py` by `fake_worker.py`
(`review_controls_03.py:39`); genuine-data checking calls only `validate_pass`
(`genuine_data_check.py:42`); the four accepted known-case runs were plain engine invocations
(`independent-checks-final-hybrid-engine.md:520-527`). Not yet exercised together [D/I]:
worker `RLIMIT_AS` 2 GiB and `RLIMIT_CPU` 260 inherited by cc1plus/as/ld and native code
(`job_worker.py:133-134`); single-core affinity (`:132`); `LD_LIBRARY_PATH=ASSET/lib`
(`preflight.py:214`) inherited by the system compiler — here [E] `cc1plus` links
`libgmp.so.10`/`libmpfr.so.6`, so on the target the toolchain would load the pinned GMP/MPFR
instead of the system ones; in-worker `check_pass` external capture under 40-way concurrency;
`-I` startup for the worker. The disclosures are honest ("no numerical pack case has run"),
but the first execution of this code would be on Syvert2. Recommend a preregistered, root-
released local dress rehearsal of the actual unpacked ZIP for known degrees (e.g. the small
group, ≤7×2×120 CPU s envelope; the hostname gate can be met in a UTS namespace without
editing frozen code), or an explicit recorded decision that `run_small` on Syvert2 is that
integration test. I did not run any engine/native/pack case.

### MINOR

- **B1 Size bound understated by 2,333 B.** Using the reviewed size-policy rule
  (`size-policy-review.md` Reproduction: count everything except source suffixes and `.md`
  other than `COLD_STORAGE.md`), positive generated deltas 2d45727→a68533f are 76,611 B, not
  74,278 B; the 2,333 B difference is exactly the `COLD_STORAGE.md` growth, which LOG.md:1591
  excluded as prose. Corrected conservative bound 9,433,015 + 76,611 = **9,509,626 B**, still
  < 10,000,000 [E]. Head = a68533f for counted paths (no further counted change) [E].
- **B2 Retry undetectable after out-of-protocol deletion** [E]: failed/interrupted job
  directories deleted, then `--resume` reruns them; final summary shows `first_failure null`,
  all three synthetic attempts validate; only an unchecked `resume-*.json` remains. Documented
  exclusion (README:133-135) but the return cannot prove "no retry". Recommend resume require
  `pending == previous summary.never_started`, keep prior summaries append-only, and have
  `verify_return` check resume records.
- **B3 Untrusted-return size handling**: `verify_return.py:27-31` and `Access` use `z.read`
  without comparing `ZipInfo.file_size` to the inventory or bounding totals → decompression
  bomb/memory DoS (fails closed). No zip-slip/symlink exposure: nothing is extracted, every
  name passes `safe()`, duplicates refused [I; 03 mutation controls E].
- **B4 Regeneration locators**: `assets.py:30` and `phase_checker/setup.py:15` use
  deb.debian.org pool URLs, which drop superseded versions; add snapshot.debian.org locators
  so "source + six pins permit a new audited build" stays true. Untested here (403).
- **B5 Wording**: `syvert2-delivery.md:28` "Shared return validation also passed over all
  four genuine saved proofs and full artifact linkage" — the genuine check exercised
  `validate_pass` only, not `validate_attempt`/`verify_return`; README:99 is accurate.
- **B6 Resume utility overstated**: README:88-91,120 ("partial campaigns are supported").
  Any stop terminates in-flight cases (which then refuse resume); preflight-failed runs have
  null provenance; resume also requires identical selected cores, which beregning may not
  reproduce. In practice resume works only if interrupted with zero active cases.

### NOTE

- `verify_return`/`validate_pass` do not recount checkpoint native calls (S ≤256, λ exactly
  3/0) or check hostname; the engine enforces these at run time (`runtime.py:86-88`,
  `engine.py:51,88-89`) and the checker bounds retained S rows.
- `cleanup()` can list the same pid twice in `cleanup_killed` (`ownership.py:43-46`; observed
  [E]); summary `phase` stays "preflight" during dispatch (`server.py:79`).
- PID-reuse window between start-tick check and `os.kill` (`ownership.py:45-46`) is tiny;
  pidfd would close it. A signal between `server.py:79` and `:87` escapes cleanup but no
  child exists yet → fail-closed. `save()` does not fsync the directory; post-crash
  staleness is covered by the boot check (the one remaining safety role of that check).
- Stale superseded prose at `final-syvert2-preparation.md:126` (writer marker); E12/E15
  header status lines still say "adoption pending" though appended root-adoption sections
  exist (`E12-corner256.md:242`, `E15-analytic-far192.md:328`).
- `cold-storage.json` has no entry for the ZIP; consistent with "transfer pending"; add one
  when the transfer happens.
- "Matches bttb A/B/C" holds at interface level (five names, beregning executable/function/
  module fallback, inherited affinity, profile A 40/2 GiB/8 GiB, hostname/UTC return name);
  semantics are deliberately stricter (no `--retry-interrupted`, quiescent instead of
  live-snapshot collection, different small/large meaning) [I via syvert-reference.md; the
  bttb-research repository itself is not in this session and was not accessed].

## 3. Task results that pass

1. **Scientific reduction** [E]: open set = [2,319] minus {2..42,63,64,159,160} =
   43–62, 65–158, 161–319, 273 degrees; `plans.LARGE` equals it exactly, no duplicates;
   `SMALL` = [41,42,63,64,159,160,511], all proved, disjoint; plan groups 7/273/280 sorted.
   Premise gating [I]: `checker.analytic_far` requires n>=192 and is re-required in both
   `decode` and `verify` for every `f` leaf; actual-corner keys raise for n>=256 and
   `parse_essential` requires 0 rows from 256; floor tiers switch at 64/160/512, matching the
   n>=41 (D29), n>=64 and n>=160 (C02) statement ranges; `degree()` restricts to 41..4095.
2. **Caps enforced in code** [I]: whole 120 (`engine.py:190` RLIMIT 119/120, checks at
   `:203,:217,:222,:226`, `final_cpu_limit` absolute self limit ≤119 with child CPU);
   controls 2/checker 100 (`:22-23` RLIMIT, `:132` used<=budget); safety 110 (`:115`);
   unfinished-call 15 (`:120`); completed-call 10 (`runtime.py:98`); walls 15/900/1000 and
   poll 0.25 (`:108,:117,:122`); 256 S (`:51`, `runtime.py:88`); 3/0 actual
   (`:64,:88-89`, `runtime.py:86`); 2047 nodes/depth 18 (`checker.py:119-123`,
   `producer.py:10,22`); essential proof <16384 B (`engine.py:157`, `evidence.py:72`).
   Return verifier requires per pass: complete final account with cap checks, provisional
   summary, preregistration/FREEZE linkage, exact rational reconstruction by the trusted
   package checker, raw/checkpoint/native-endpoint linkage, both stage supervisors/checkpoints/
   descendant records/stdout/stderr, mandatory source snapshot/TU/binary/compiler/header/
   dependency/linked closures, before/after runtime and maps with every mapped file
   preserved, recursive identity closure, fresh-replay byte linkage to the primary; per
   attempt: started identity/core, wrapper EXIT0 without timeout/cleanup, attempt closure,
   both pass exits with exact commands (`evidence.py:69-201`). Status-only success cannot
   pass; manifest bytes are re-verified from the trusted package (`verify_return.py:29-32`).
   Failed attempts are never retried: resume validates every existing attempt (refused [E]).
3. **Quiescence contract** [I + E]: one flock for admission and collection; every output
   group must be strict `True/True` with source/plan/domain/identity binding before either
   (`server.py:23-35`, `evidence.py:158-170`); state saved false before preflight and any
   child (`:79`, subreaper before first child `:88`); true only after direct waits plus
   owned-subreaper ECHILD with no later child (`:145-161`); cleanup failure leaves false
   (`:162-165`). The lock fd is not inherited by workers, so state (not the lock) protects
   after a supervisor SIGKILL — correctly. I agree no global environment scan is needed for
   supported launch paths; out-of-protocol writers stay excluded as documented.
4. **Executed controls** [E]: see section 5. Failures 01/02 are preserved: receipts with
   `PermissionError` and root observations `observed_exit_code 1`, `no_rerun true`; their
   preregistrations and harnesses remain with matching SHA256 (review_controls 13e423b3…,
   _02 c7942287…); source commits edcc80a5/7cce03f1 exist [E].
5. **Target prerequisites** [I]: preflight checks CPython>=3.10, Linux x86_64, LP64
   (`l`,`P` = 8), hostname `syvert2` (exact first label — the real host label is unverified),
   affinity, c++/readelf/ldd, free floor, four assets in manifest, ldd with "not found"
   refusal (also catches GLIBC version errors), arithmetic libraries resolved inside the
   package, and 8 GiB soft AS. FOPS-10 separation is present in `build_pack.py:114-127,139-150`.
   The setup.py network fallback (`runtime.py:66`) is unreachable when preflight passes.
   Launchers are LF-only bash with quoted `"$@"`; git modes are 100644 and the builder sets
   0755/external_attr for the five (`build_pack.py:151,156`). Grammar of all 18 runtime
   Python files parses under 3.10 [E]; the operational controls pass under 3.11 and 3.13 [E].
6. **Honesty/accounting** [E]: evidence index 336 entries, 27,665 B (<32 KiB), every entry
   rehashes, none ≥16 KiB, sum 1,531,377 B as declared; all `final-*` evidence indexed.
   Storage statements (ZIP ephemeral, transfer pending) are consistent across delivery.json,
   syvert2-delivery.md and COLD_STORAGE.md. D36 primary missing-outer-EXIT0 limitation is
   preserved (`theory/D36-global1023.md:17-21,421`, LOG.md:928, D39 freeze). Arithmetic:
   239 = 232 + manifest + custody + 2 README copies + 3 producer objects; 74,836,219 =
   49,731,698 + 25,104,521; 4 checkpoint CPU values sum to 28.060015 [D/E].

## 4. Data-only proof reconstruction of committed receipts [E]

`evidence/final-hybrid-validation/{primary,fresh}-{41,511}.json` equal the pinned genuine
receipts (faca3065…, a2af589a…, c5369110…, 0c00807f…). Running the exact checker
(`verify_essential`, copied) reconstructs every recorded verification: 41 TREE, 101 nodes,
64 S, 3 actual (NEAR 5/FAR 43/OUTSIDE 3), fresh tree identical; 511 GRID, 51 nodes, 45 S,
0 actual, 3 ANALYTIC_FAR. FREEZE identity matches; all <16 KiB. The four committed final
accounts satisfy the `validate_pass` account rules. 14 of 22 genuine pins verifiable here all
match; 8 (summaries/raw) are in absent local-output. Native endpoint/raw linkage and the
234 captured objects were not checkable.

## 5. What I ran (all in copies under t2-run/, fake workers only, no science)

Run dir: `/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit2/t2-run/`.
`tree-head/` = copied `syvert2_pack/` and `code/final_pack_ops_review/` (+ checker/FREEZE and
committed receipts); fixture hashes equal PREREGISTRATION-03 values.

| Command (cwd tree-head) | Exit | CPU (user+sys) | Result |
| --- | --- | --- | --- |
| `python3 -I -S -B …/review_controls_03.py --source …/syvert2_pack --output t2-run/out-03-head` (3.13.18, timeout 180) | 0 | 6.48 s; receipt self 6.07, children 0.32, wall 27.3 | 67 events, list **identical** to recorded receipt; failure null; 36.97 MB output |
| same with `/usr/bin/python3.11 … --output t2-run/out-03-py311` | 0 | 6.26 s | 67 identical events |
| `scripts/x_controls.py tree-head x-<case> <case>` for sigchld_dfl, sigchld_ign, reboot, delete_resume, sighup | 0 each | <1 s total | A1, A2.1, A2.2, B2 evidence above |
| `scripts/x_preflight_brick.py tree-head x-preflight-brick` | 0 | <0.2 s | A2.3 |
| `scripts/receipt_check.py tree-head` | 0 | 0.04 s | section 4 |
| `scripts/size.py 2d45727 a68533f` / `a68533f HEAD` (git ls-tree only) | 0 | <1 s | B1 |

No leftover processes after runs (checked with ps). Total ≈ 15 CPU s, far below the ~30 CPU-min cap.
Not run: controls 01/02 (historical; they target removed scanner sources and would read other
processes' `/proc/*/environ`, whose outcome here as root would be environment-specific and
cannot change the preserved history); `genuine_data_check.py` (requires absent local-output).

## 6. Could not test

Actual ZIP/manifest/entries/modes; six .deb hashes, metadata, header/library counts and the
GLIBC_2.38 ELF requirement (egress 403); captured objects and raw evidence; any real
job_worker/engine/compiler/native path; Syvert2 OS, glibc, hostname string, beregning behaviour
(including its SIGCHLD/SIGHUP handling and core allocation stability), disk, NFS/flock
semantics; CPython 3.10 itself; bttb-research sources; the builder run and root tool-session
observations (accepted as recorded only).

## 7. Disclosure

One inspection command (`python3 -I -c 'import plans'` with cwd in the repo, without `-B`)
created the git-ignored `topics/padua-argmax-bridge-20261105/syvert2_pack/__pycache__/
plans.cpython-313.pyc` at 06:01:46Z. I removed exactly that directory immediately; no tracked
file was changed (`git status --short --ignored` shows only pre-existing ignored items).
