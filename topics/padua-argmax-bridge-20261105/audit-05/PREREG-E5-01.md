# PREREG-E5-01 — audit-05 (handoff 32) technical reruns and controls
Saved before any run below. Auditor: Claude Opus 5.5 xhigh (subagent). Repo head 33b9eca8167980cad0b0a491da7de64280c9a158 (read-only).
Inputs: $A/inputs/padua30.zip (25,111,335 B, aac08e5f...e74d2), $A/inputs/return.tar.gz (36,045,486 B, b00fd57f...109a; cmp-identical to return-data copy).
Trusted code: git-archive copy of 33b9eca at $A/e5-run/tree. Package layout restored INTO THAT COPY only. No repo edits; no state-changing git.
All engine-free. Every consequential command runs ONCE via e5-code/observe.py (fork/exec, wait4, RLIMIT_CPU, wall cap, ECHILD).
No retry/rescue. A defect in MY harness is recorded as such; a corrected harness runs only under a new label after a dated amendment here.
Total cap: 40 CPU-min. Per-run caps below.

S0 pkg_auth (data-only): safe-extract padua30.zip (regular files only, safe names, CRC), runtime_manifest.json SHA must be 5b89fa66...,
   all 250 rows bytes+SHA must match; hash both internal verify_compact.py copies (expect 7c2dad53...). Restore padua30/ to
   tree/local-output/argmax-bridge-20261105/compact-release-aea62883/padua30 and every asset_provenance arithmetic file to tree/<path>
   from the authenticated package bytes. Expect: all pass.
R1 check_reader_repairs.py (cwd=tree; python3 -E -B; 120 CPU/180 wall): expect exit 0, status PASS, 40 controls.
R2 runtime_probe.py (cwd=tree; OPENBLAS/OMP=1; python3 -E -B; 60/90): expect exit 0, 31 controls, 4 probes true.
R3 onset512_analytic/check.py (cwd=tree; python3 -B; 60/90): expect exit 0, assertions PASS, enclosures equal to committed record.
R3o same under PYTHONOPTIMIZE=1 on a COPY whose gate `peak.hi < F(41, 1000)` is falsified to `< F(1, 1000)`: diagnostic;
   predicted exit 0 with "assertions": "PASS" (removable-assert fail-open). R3m: same mutated copy, normal mode: predicted exit 1.
R4 verify_compact.py RET --package PKG --manifest-sha 5b89fa66... --expect-plan all (python3 -I -S -B; 120/180): expect exit 0,
   expect_plan=all, coverage_mode=complete_plan, 280 pairs, degrees exactly 41..319+511, sampled [199,238]; stdout SHA compared to 3f6605da...
R5 same with --expect-plan small: expect exit 1 'expected complete plan coverage'.
R6 same without --expect-plan: expect exit 0, coverage_mode=completed_subset, expect_plan null; stdout differs from R4.
R7 R4 under python3 -O -I -S -B: informational; predicted exit 0, JSON identical to R4 (no assert in that path).
R8 reader/runner optimization refusals with my own forged ZIP (only COMPACT.json, empty files/degrees/selection):
   (a) -O -B (b) -B + PYTHONOPTIMIZE=1 (c) -E -O -B (d) -OO -B  -> expect exit 1, 'optimized Python is unsupported', no 'accepted'.
   (e) runner.py preregister NEWDIR under -O -B -> refusal, NEWDIR not created.
   (f) -E -B default pin -> exit 1 'external archive SHA256'.  (g) -E -B --archive-sha <forged sha> with REAL trusted runtime -> exit 1, no acceptance.
R9 compatibility probe (data-only parse): return_bundle.strict over every *.json member of the old return; list key-type rejections.
   Also compare per-pass file names in sampled full histories with check_members allowlist. Diagnostic; no prediction of pass/fail.
R10 real-runtime reader control (no Access adapter; spies only record call order): check_reader_repairs.fixture() re-pinned to the REAL
   local pins/trusted manifest/freeze; --archive-sha = its own SHA. Expect exit 1 rejected inside the real checker for n=320 produce
   (synthetic certificate); pins() recorded before Access construction; no acceptance.
R11 my reader controls under the developer's marked adapter (synthetic Access/pins/validate_pass), each expected to REJECT with reason:
   RB-a .preserve.lock + 382x storage-dedup.json (producer-written names) -> 'unregistered campaign member' (compatibility diagnostic)
   RB-a2 storage-dedup.json only -> 'unregistered pass member'; RB-b reg runner = repaired a198b651 -> 'preregistered campaign runner';
   RB-c produce-exit observed_returncode '0' -> 'integer field'; RB-d wrapper-exit True -> 'integer field';
   RB-e summary receipt path altered (bytes/sha kept), n=400 -> 'summary receipt identity';
   RB-f fresh certificate_identity sha altered consistently in 3 records, n=401 -> 'fresh input primary linkage';
   RB-g attempt status failed n=402 -> 'completed attempt status'; RB-h original-certificate bytes differ n=403 -> 'original-certificate';
   RB-i unsampled check-* member n=404 -> 'unsampled native history'; RB-j preserved object wrong hash -> 'preserved object hash';
   RB-k extra helper source -> 'unregistered helper source'; RB-l duplicate JSON key -> 'duplicate JSON key';
   RB-o pilot-summary row observed_returncode False (+matching wrapper-exit) -> 'integer field'.
   Diagnostics (no required outcome; predicted ACCEPT): RB-m symlink-typed ZIP member under allowlisted, inventoried name;
   RB-n directory-mode external_attr without trailing slash under allowlisted name.
R12 my compact-verifier controls on the OLD RETURN with the REAL package (in-process verify_payloads after read_payloads; rehash
   COMPACT.json rows and, where named, server validation hashes). Expected REJECT with reason:
   VC-1 last ledger entry removed -> 'unregistered attempt directory' or 'ledger'; VC-2 middle ledger entry removed -> 'ledger sequence';
   VC-3 n41 produce-exit observed_returncode false -> 'observed pass EXIT0'; VC-4 same '0' -> 'observed pass EXIT0';
   VC-5 n42 wrapper observed_returncode 0.0 -> 'observed wrapper EXIT0'; VC-5b wrapper True -> 'observed wrapper EXIT0';
   VC-6 n43 attempt status failed + server attempt hash -> 'completed attempt status';
   VC-7 n44 verify tree := n45 tree, receipt/summary/server hash updated -> rejection naming tree or 'exact rational reconstruction';
   VC-8 trusted-name shadow of engine checker.py -> 'archive shadows trusted package'; VC-9 jobs/999 -> 'unregistered job directory';
   VC-10 uninventoried extra member -> 'exact compact inventory'. Diagnostic: VC-11 inventoried extra file in unsampled pass dir (predicted ACCEPT).
   Transport end-to-end (rewritten tar.gz, observed subprocess, real package): VT-1 uninventoried hardlink alias of the 32.7 MB member ->
   'exact compact inventory'; VT-2 alias before its target -> 'hardlink target must precede alias'; VT-3 symlink member and VT-4
   directory member -> 'regular/hardlink members only'; VT-5 ~750+ hardlink aliases of the 32.7 MB member -> 'expanded inventory bound before read';
   VT-6 VC-9 archive under python3 -O -> still 'unregistered job directory'. Per subprocess 120 CPU/180 wall.
R13 budget: copy of audit-02/code/t2/size.py run with read-only `git ls-tree` on refs (f70a260,70a50d7), (8a94ce6,33b9eca),
   (b5388c2,33b9eca), (941aa33^1, 941aa33); per-path attribution; git diff --name-status for non-topic paths. Expect to reproduce
   9,895,866 / 11,723,154 and the 11,751,309 & 11,729,562 figures if the convention is as recorded.
R14 evidence_index.py --check from the tree copy (python3 -B; 30/60): expect PASS.

## Amendment A1 (saved before execution, after R14)
A1a forged tar.gz containing only COMPACT.json = {} through verify_compact under (i) PYTHONOPTIMIZE=1 python3 -S -B and
(ii) python3 -O -I -S -B: expect exit 1, no JSON on stdout. A1b authentic return, PYTHONOPTIMIZE=1 python3 -S -B,
--expect-plan small: expect exit 1 'expected complete plan coverage'. Caps 60 CPU / 90 wall each. Also recorded as executed but
not separately preregistered before running: R12-VT-6-normal (same VT-6 archive without -O; comparison run, exit 1 expected).

## Amendment A2 (saved before execution): runtime-probe sensitivity
Compile a 2-function helper (_mm_getcsr/_mm_setcsr) with gcc into $A/e5-run/mxcsr/; in ONE observed process (60 CPU/90 wall)
import the trusted runtime_probe.py from the tree copy and call its main() under five MXCSR settings in this order, recording
probe JSON or SystemExit and the bit pattern float.hex((np.array([2.0**-1022])/2)[0]): (1) default; (2) FTZ|DAZ;
(3) round-toward-zero; (4) FTZ only; (5) DAZ only; MXCSR restored to default after each.
Predictions: (1) pass; (2) all four probes TRUE although the bit pattern shows 0x0.0p+0 (probe insensitive to FTZ+DAZ);
(3) SystemExit (ties_even_up false); (4) SystemExit (gradual_underflow false); (5) pass. Diagnostic only; no result depends on it.

## Amendment A3 (saved before execution): integer bit readout
A2's float.hex readout is itself DAZ-affected (FP arithmetic). Re-read the same quotient as integer bits via
ndarray.view(np.uint64) under the same five MXCSR modes (no probe call). Predicted: default 0x8000000000000, FTZ|DAZ 0,
round-toward-zero 0x8000000000000, FTZ only 0, DAZ only 0x8000000000000. 30 CPU/60 wall.

## Amendment A4 (saved before execution): audit-03 30-control suite without adapter
Coordinator's request: confirm adapter-dependent audit-04 results without the adapter. Run once, from the tree copy,
python3 -I -S -B topics/.../code/compact_verifier_audit03/check.py --archive RET --package PKG --output $A/e5-run/A4-check30.json
(normal mode; 120 CPU/180 wall). Expect exit 0 and 30/30 controls behaving as designed (28 named rejections, 2 designed acceptances).
