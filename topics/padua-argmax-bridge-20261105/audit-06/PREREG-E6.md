# PREREG-E6 — audit-06 (handoff 34) focused technical reruns and controls

Saved before any run below. Auditor: Claude Opus 5.5 xhigh (independent auditor subagent). Repo head
5b1a4942af498e60e9da4c8860c57cb4f67be4ef (read-only; no state-changing git; no repo file written).
Trusted code: `git archive 5b1a494` copy at $A/e6-run/tree (A = scratchpad/audit6). Reader 3f903e62..., check_reader_repairs
68bc9b70..., runner a198b651..., storage 274d009d..., analytic check 5ce8cc07..., runtime_probe 9f1c503e...
Old reader for comparison: `git show b5a6946:.../return_bundle.py` -> e6-code/return_bundle_b5a6946.py (5e25c8a4...).
Every consequential command runs ONCE via e6-code/observe.py (copy of audit-05 observer b13bd6fb, env names E6*):
fork/exec, os.wait4, RLIMIT_CPU, wall cap, SIGCHLD default asserted, ECHILD recorded. No retry/rescue. A defect in MY
harness is recorded as such; a corrected harness runs only under a new label after a dated amendment appended here.
No engine, native campaign, Syvert, remote, or archive-code execution. Total cap 40 CPU-min. Env for all python runs:
OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1. Python 3.13.18 / NumPy 2.5.3 (not the recorded 3.12.14 / 2.3.5).

## Handoff-34 cheap commands (cwd = tree root)
R1 `python3 -E -B topics/.../code/local_onset512_campaign/check_reader_repairs.py` (120 CPU/240 wall): expect exit 0,
   status PASS, 60 controls, first case 'real deduplicate/completed/export/reader roundtrip...'.
R2 `python3 -E -B topics/.../code/onset512_analytic/check.py` (60/90): expect exit 0; 11 output keys; the 8 enclosures,
   `arithmetic` and `assertions` equal committed receipt.json; only `python` differs (3.13.18 vs 3.12.14).
R3 `python3 -E -B topics/.../code/independent_phase_checker/runtime_probe.py` (60/90): expect exit 0, 31 controls, 4 probes true.

## Analytic optimization guard (copies under e6-run/r2mut/, never in the tree)
M0 = exact copy of check.py; Mg = copy with `assert peak.hi < F(41, 1000)` -> `< F(1, 1000)` (falsified gate);
Ml = copy with `assert log(PI).lo > F(11, 10)` -> `> F(23, 20)` (falsified new log-pi bound; log pi ~ 1.1447 < 1.15).
R2a Mg `-E -B` -> exit 1, AssertionError, empty stdout.     R2b Ml `-E -B` -> exit 1, AssertionError, empty stdout.
R2c Mg `-O -B` -> exit 1, 'optimization is not permitted', empty stdout.   R2d Mg `-OO -B` -> same.
R2e Mg `-B` + PYTHONOPTIMIZE=1 -> same refusal.   R2f Mg `-E -O -B` -> same refusal.
R2g Mg `-E -B` + PYTHONOPTIMIZE=1 -> exit 1 AssertionError (-E ignores env).  R2h M0 `-B` + PYTHONOPTIMIZE=1 -> exit 1 refusal.
R2i Ml `-O -B` -> refusal. (each 30 CPU/60 wall)
Also [D]: AST count of assert nodes in check.py and position of the guard before any assert-bearing call.

## Runtime probe challenge (P)
gcc -shared -fPIC -O2 e6-code/mxcsr.c (copy of audit-05 848e6904: _mm_getcsr/_mm_setcsr only) -> e6-run/mxcsr/libmxcsr.so.
P1 e6-code/probe6.py: imports NumPy + the tree's runtime_probe first, then per mode sets MXCSR in the same thread, computes
   uint64 bits of [2^-1022]/[2], [2^-1074]*[2] (subnormal OPERAND), nextafter(0,1), the two tie sums, then calls the real
   runtime_probe.main(); restores MXCSR in finally. Predictions (probe verdict):
   default PASS; FTZ -> reject gradual_underflow; DAZ -> PASS (undetected; subnormal-operand product bits 0x0 vs 0x2);
   FTZ|DAZ -> reject gradual_underflow; RD -> reject ties_even_up; RU -> reject ties_even_down; RZ -> reject ties_even_up;
   FTZ|DAZ|RZ -> reject (gradual_underflow and ties_even_up false); DAZ|RU -> reject ties_even_down.
   Also: a fresh child process (subprocess python3 -E -B -c reading MXCSR) after the parent set FTZ|DAZ: predicted default
   MXCSR in the child (execve resets SSE state) -> probe evidence is per process (diagnostic). 60 CPU/90 wall.

## E5-01 reader controls (e6-code/rb6.py; 300 CPU/600 wall)
Part A — developer-equivalent MARKED adapter (synthetic Access arithmetic, synthetic pins, stubbed sampled validate_pass, temp
release), developer fixture() docs; each archive rebuilt and its own SHA passed as the external pin. Predicted outcome/reason:
 Carried audit-05 R11 controls: RB-a lock + 382 receipts -> ACCEPT (was REJECT); RB-a2 382 receipts only -> ACCEPT (was REJECT);
 RB-b runner a198b651 -> 'preregistered campaign runner'; RB-c produce-exit '0' -> 'integer field'; RB-d wrapper True ->
 'integer field'; RB-e n400 summary receipt path -> 'summary receipt identity'; RB-f n401 fresh certificate_identity ->
 'fresh input primary linkage'; RB-g n402 attempt failed -> 'completed attempt status'; RB-h n403 original-certificate ->
 'original-certificate'; RB-i n404 unsampled check-* -> 'unsampled native history'; RB-j preserved wrong hash -> 'preserved object
 hash'; RB-k extra helper -> 'unregistered helper source'; RB-l duplicate key -> 'duplicate JSON key'; RB-o pilot+wrapper False ->
 'integer field'. Diagnostics RB-m symlink-mode, RB-n directory-mode member -> ACCEPT (E5-06 unchanged).
 New, on the RB-a archive (base) with one change each:
 L1 lock b'\n' -> 'preserve lock must be empty'; L2 lock b'\0' -> same; L3 empty lock in pass dir -> 'unregistered pass member';
 L4 lock at case level -> 'unregistered case member'; L5 out/jobs/.preserve.lock -> 'unregistered job directory';
 L6 out/helper-source/.preserve.lock -> 'unregistered helper source'; L7 archive-root .preserve.lock -> 'unregistered archive member';
 L8 out/.preserve.lock2 -> 'unregistered campaign member'; L9 (diag) lock inside a SAMPLED check-* dir -> ACCEPT.
 D1 extra field -> 'receipt schema'; D2 missing field -> 'receipt schema'; D3 list -> 'receipt schema'; D4 null -> 'receipt schema';
 D5 string count -> 'integer counts'; D6 true -> 'integer counts'; D7 6.0 -> 'integer counts'; D8 -1 -> 'integer counts';
 D9 1e2 -> 'integer counts'; D10 relinked>examined -> 'consistent counts'; D11 relinked 0, bytes>0 -> 'consistent counts';
 D12 scope + trailing space -> 'dedup scope'; D13 scope 5 -> 'dedup scope'; D14 duplicate key -> 'duplicate JSON key';
 D15 NaN -> 'nonfinite JSON'; D15b Infinity -> 'nonfinite JSON'; D16 truncated JSON -> REJECT (any JSON error);
 D17 out/storage-dedup.json -> 'unregistered campaign member'; D18 case-level receipt -> 'unregistered case member';
 D19 receipt in UNSAMPLED check-* dir -> 'unsampled native history'.
 Diagnostics (predicted ACCEPT; would be NOTE-level if so): D20 reordered keys/compact whitespace; D21 'lying' receipt
 examined=10^6, relinked=10^6, bytes=10^15 (no build manifest in the pass); D22 examined=relinked=bytes=0;
 D23 receipt in one pass only and no lock.
Part B — my own REAL producer round-trip (no adapter on storage.deduplicate, completed(), export(), check_members, strict):
 synthetic tree from fixture(tree, assets) plus the full n>=256 producer name set per pass (23 engine names + local-validation
 + storage-dedup; verify adds original-certificate) and the 9 case-level names; one S-build.json per pass whose
 workdir check-* holds 3 build artifacts + 3 deps under deps/ (all six identity-checked by the real deduplicate) and one external
 dependency row (skipped by design). Predicted: 382 receipts, examined 6 each (2,292), relinked 2,286 (first pass 0),
 empty lock; export exit normal; per unsampled case exactly 60 ZIP members; reader (repaired) ACCEPT 191 pairs/382 proofs,
 4 sampled-closure adapter calls. Adapters (same as developer): R.ROOT/RELEASE/__file__ relocation, pins, LocalAccess/Access
 arithmetic, MANIFEST_SHA, validate_pass. B2: the OLD reader 5e25c8a4 on the same archive under the same adapter -> REJECT
 'unregistered campaign member: out/.preserve.lock'. B3 (diag): one real produced receipt rewritten to lie
 (paths_relinked=1, logical_bytes_relinked=1, examined unchanged) and re-pinned -> ACCEPT (counts not linked to build manifests).
Also [I/E-derived]: grep check_reader_repairs.py for any patch/mock of deduplicate/export/completed (predict none).

## Compact verifier (item 4)
No rerun with the padua30 package (Access would import the package's checker.py, i.e. archive bytes). Instead [E] read-only
git: `git diff --stat 33b9eca 5b1a494 -- compact_pack code/final_hybrid_engine code/compact_verifier_audit03` -> predicted empty;
then rely on audit-05 R4-R7/A4/VC/VT.

## Budget and scope (read-only git; e6-code/size6.py, my own implementation of the size.py rules)
Rules: count every blob except suffixes .py .sh .c .cpp .h .tex .bib .diff, basename .gitignore, and .md other than COLD_STORAGE.md;
topic convention adds the 2,087 B code/post_audit_D09_threepoint/FREEZE.md. Predictions: main b5388c2 = 9,733,758; HEAD =
11,734,394; HEAD-main = 2,000,636 = sum of counted paths under topics/padua-argmax-bridge-20261105/ at HEAD; +2,087 = 11,736,481;
positive deltas 8a94ce6->HEAD = 1,838,528 and 9,917,613 + that = 11,756,141; 33b9eca->HEAD net = positive = 4,832.
`git diff --name-only b5388c2 5b1a494` outside the topic dir: only results/padua-argmax-bridge-20261105.md.
E1 `python3 -B topics/.../code/evidence_index.py --check` (30/60): exit 0, 396 entries.

## Amendment A1 (saved before I1; after R1-R3, R2a-i, P1, RB6 ran as recorded)
I1 e6-code/ident6.py, data-only (tarfile/zipfile reads in memory, json parse; nothing extracted or executed; 60 CPU/120 wall):
   question: besides storage-dedup.json/.preserve.lock, could the exporter's identity rule (export L145-152: identity rows
   from 5 sampled-pass JSONs under ROOT and not trusted -> added under their ROOT-relative name) emit names the repaired
   allowlist rejects ('unregistered archive member')? Analogy on the ORIGINAL return (same frozen engine; n=199/238): collect
   identity rows of {raw-evidence,summary,final-accounting,preregistration,essential-receipt}.json for sampled passes;
   classify vs the run's package_root: under the output prefix / trusted manifest name (padua30 runtime_manifest 5b89fa66) /
   other under-root (would-be extra names) / outside root (preserved objects). Prediction: other-under-root = 0; distinct
   outside-root SHA count <= 247 (the original return's preserved objects). Diagnostic only; the onset512 sandbox root and
   environment differ, so this is analogy, not canonical-ZIP evidence.

## Amendment A2 (saved before O1-O6; after I1, Z1, E1 ran as recorded: I1 other-under-root 0, 245 outside SHAs; Z1 all
## figures as predicted; E1 PASS 396)
Reader/runner optimization refusal with the audit-05 forged ZIP (forged-empty.zip 9ab68303..., copied to e6-run/forged/),
cwd = tree, each 30 CPU/60 wall, predicted exit 1, stderr contains 'optimized Python is unsupported', empty stdout:
O1 reader `-O -B verify FORGED`; O2 reader `-B` + PYTHONOPTIMIZE=1; O3 reader `-E -O -B`; O4 reader `-OO -B`;
O5 runner `-O -B preregister e6-run/never-created` (dir must not exist afterwards);
O6 reader `-E -B verify FORGED` with PYTHONOPTIMIZE=1 -> exit 1 'external archive SHA256' (env ignored; default pin rejects).
