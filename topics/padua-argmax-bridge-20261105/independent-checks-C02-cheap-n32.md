# C02 cheap known-n32 replay — frozen preparation, NOT RUN

2026-11-06. Rules/input `4b728b04216a5490910780bc609a82b853058426`.
Prepared by the distinct C01 reviewer, Codex assigned Astra high; actual
serving model/effort metadata unexposed. This agent now authors the C02
supervisor; this preparation record is **not an independent audit of its
own new wrapper**. Coordinator/source review and explicit release remain
required. Formal Claude audit is separate.

**Status: PREPARED, NOT RUN.** No build, native kernel call, whole-candidate
replay, producer, refined tree, changed candidate or additional degree
has been executed for C02. `evidence/c02-cheap-n32.json` is intentionally
absent until the authorized run produces its first receipt. This record
is the prospective plan; it does not fabricate execution evidence.

## Frozen scope

Wrapper: `code/cheap_C02/replay.py`,21346 bytes, SHA256
`d3fc74dbf4f211fc3fce0f24b7fc6b90a1250a2ef6ee5b8112c58712582f98fa`.
C01 source remains exactly
`178bbe5a969a018d91454dc877572a691c9831a4b8793971f5aa303343465dab`,
14311 bytes; its bounded independent source/control review is
`independent-checks-C01-prototype.md` SHA
`68bf3051b61a62ffc13eb984ee8725c1052d61e349e4554a1f19d6854cf27fb9`.
No replacement arithmetic, coefficient, guard, degree range or rounding
rule is introduced by C02.

Exactly one input is permitted: committed
`evidence/n3-phase-n32-bootstrap-r8.json.gz`, gzip SHA
`a01bc14b968676161afa0690e5ed41005da8cb3f87fb8c6393594bc37ed3986a`,
which decompresses to21338 bytes with SHA
`97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e`.
It is the unchanged complete364-leaf, n32 candidate. Existing strict JSON
parsing, partition, premises and acceptance predicates are retained.

The sole acceptance invocation is `check_r8.check(data, kernel)` with an
explicit new Kernel object. There is no monkeypatch, alternate predicate,
max-leaves argument or acceptance-by-supplied-number path. The unchanged
checker processes all364 leaves and returns every failed predicate; C02
retains the first failed leaf and total count. “First failure” means the
first failed outcome is preserved without rescue, not a changed checker
that aborts its normal full traversal at the first false predicate.

The Kernel calls the reviewed C ABI `phase_bounds`, returns its seven
finite enclosures without adjustment, validates endpoint order, and
records its counters and per-call CPU. It restricts n to32. It cannot
change candidate geometry, native arithmetic or checker predicates.

## Publication and prospective launch

Only after the coordinator has published the reviewed source bundle and
wrapper and separately released this job may it invoke:

    python topics/padua-argmax-bridge-20261105/code/cheap_C02/replay.py --run-once --source-commit <FULL_PUBLISHED_40_HEX_SHA>

The wrapper checks each pinned project code/data file and itself against
the supplied commit via read-only `git cat-file blob`. This checks content
identity in the local commit database; remote publication and explicit
run release remain the coordinator's responsibility. No Git mutation or
network access is performed by the wrapper. Its SHA cannot be assumed
published merely because a matching local object exists.

The dedicated directory
`local-output/argmax-bridge-20261105/cheap-C02/n32` and essential receipt
must both be absent before launch. Files are created exclusively; output
reuse is refused. The parent records a launch token and PID, and the
worker validates both its parent and its new process group before doing
any work. An interrupted or unsuccessful attempt consumes the directory;
there is no automatic retry or cleanup-and-relaunch branch.

## Source, input and runtime closure

Before execution,14 fixed code/data identities cover the reviewed
prototype, unchanged check_r8/check_r6, both transitive snapshot modules,
fixed corner/energy code and evidence, candidate gzip and the accepted
old-v3 summary. The wrapper identity is recorded separately. Candidate
bytes are snapshotted once into the new work directory and strictly
parsed; their identity is checked again afterward. No prose record is
an executable pin. Accepted C01 ratio/all-class mathematics is referenced
through the C01 review, not re-read as a caller-controlled proof flag.

The new builder reuses the entire frozen r9 snapshot implementation with
exactly two checked text substitutions: prototype source path and C02
output directory. It saves the executed builder text locally. No function
on an imported checker module is modified. A unique fresh build directory
holds source snapshot, preprocessed translation unit, private arithmetic
library copies and binary; the source snapshot must equal the reviewed
prototype SHA.

The worker snapshots and checks all imported **project** Python modules,
the Python executable, and fixed inputs. It records compiler commands and
version, compiler/helpers and their runtime dependencies, preprocessor
header closure, FLINT/GMP/MPFR inputs, linked dependency closure and the
**actual loaded mappings**. All groups, source snapshot, preprocessed unit,
binary and executed builder snapshot are checked before acceptance and
again after execution. Actual loaded mappings must remain identical.
An unexpected project Python import is rejected. The supervisor then
rechecks the output build/runtime identities independently of worker
claims before admitting success. Full identities stay in the local raw
report; the small receipt pins that report.

Thus the historical C01 driver provenance limitation is addressed in the
new wrapper rather than silently attributed to older receipts. The old
reports and source generations remain unchanged.

## CPU, failure and comparison contract

Prospective total limit:180CPU seconds, counting supervisor, worker and
compiler/build helpers. The process-group watchdog polls every.1s and
kills the whole worker group at observed176CPU seconds. Worker CPU soft
and hard limits are178/179 seconds. Group accounting sums live own CPU
and waited-for descendant CPU from `/proc`, preserving compiler time as
helpers exit; final accounting uses actual child resource usage plus
supervisor process CPU. Success additionally requires final total<=180.
Supervisor exceptions kill and wait for the group before propagating.

No degree-growing harmonic rescue, new producer, candidate replacement,
tree refinement or second attempt is permitted. Native per-call outputs
and counters are flushed to a local JSONL trace, so partial diagnostics
survive a watchdog stop even when the complete checker report is absent.
No failure is reported as complete acceptance.

PASS requires actual worker exit0, no watchdog termination, every closure
check complete and stable, n32, complete=true,364/364 checked leaves,
zero pending and zero failed predicates, exact input identity, and CPU
within cap. Any weakened bound that loses a predicate produces FAIL and
retains that first failed leaf. Source/runtime exceptions also forbid PASS.

The old accepted v3 receipt is frozen at
`evidence/phase-r9-n32.json` SHA
`5bdab76556a37552121afabe172d641e57a60026d1b07b36c4f6e5e5069977ae`:
364/364 accepted,139.405409 total subprocess CPU seconds. C02 compares
its actual complete outcome and CPU with that saved acceptance. If the
old raw report is locally present, its pinned identity is checked before
and after and it supplies a read-only ordered-leaf/bound comparison,
including weakened output counts and old-valid/new-failed predicates.
If absent, no old replay is launched: the receipt explicitly limits the
comparison to the committed acceptance/CPU summary. The comparison is
diagnostic and supplies no premise to the new acceptance decision.

Only a successful complete run could support a measured cheaper replay
of this known candidate. It would still establish neither a degree-wide
cost law nor a new certified degree. A failed complete run would show
insufficient tightness on this fixed tree, not a false underlying theorem.

## Preparation checks actually performed

Python AST parse and compile passed. A helper-only import checked all14
source/data hashes and the exact21338-byte decompressed input. Static
inspection confirmed one two-argument uncapped `acceptance.check` call
and no assignment to the acceptance module. The dedicated run directory
and C02 evidence receipt were verified absent. These checks imported no
acceptance module, built no library and called no native kernel. No
publication SHA check or Git command was executed during preparation.

Next step: distinct/coordinator source review, publication, explicit run
release, then one invocation under this unchanged prospective contract.
Until that release the run remains NOT RUN. No acceptance result or
timing estimate is inferred from wrapper preparation.

## 2026-11-06 released execution — COMPLETE CHECK, NOT ACCEPTED

The preparation-only status above is historical. The coordinator completed
its distinct source-only wrapper review, committed and pushed the accepted
C01 bundle and frozen C02 wrapper at
`b6e67b3c78cb668b6d2f9da5a5560537d2960bf3`, and explicitly released exactly
one full known-candidate replay. Rules AGENTS/WORKFLOW/CODEX were re-read
at that input. The executing reviewer remained assigned Astra high,
serving metadata unexposed. No source was changed for execution.

Executed exactly once from repository root:

    python topics/padua-argmax-bridge-20261105/code/cheap_C02/replay.py --run-once --source-commit b6e67b3c78cb668b6d2f9da5a5560537d2960bf3

**Actual exit1, status FAIL, accepted=false.** The checker completed
364/364 leaves with zero pending,76 failed predicates and288 passed.
It was not watchdog-stopped and reported no source/runtime error. There
was no retry, rescue, candidate change, tree refinement, new producer or
additional degree. The first outcome has been preserved; no follow-up
native run was performed.

| Unchanged leaf kind | Checked | Passed | Failed |
|---|---:|---:|---:|
| outside |32|32|0|
| far |280|232|48|
| corner-orbit-plus-defect |28|0|28|
| maximum-exclusion-plus-defect |24|24|0|
| Total |364|288|76|

The first failure is root0, path`0101`, kind`far`. Its complete returned
tuple `(S_upper,C_upper,defect_lower,Lc_lower,Lc_upper,pi_lower,pi_upper)`
is

    [11.467798411235936, 10.920225581178373, 0.0,
     10.993594541100443, 10.993594541100444,
     3.141592653589793, 3.1415926535897936].

Its exact strict margin `Lc_lower-S_upper` is
`-133476523302491/281474976710656`, so the required far predicate fails.
The old v3 tuple on that same leaf began
`[10.559446940553098,9.97026067079385,0.0]`, with identical constants
and positive margin`122201685753051/281474976710656`. Thus this is an
observed loss of enclosure tightness on the frozen tree, not an input,
geometry, constant, proof-premise or provenance discrepancy.

The read-only comparison with the hash-verified old full report confirms
all364 root/path/kind triples remain in exactly the same order. All332
numerical S upper bounds and corner upper bounds weaken;270 defect lower
bounds weaken. Every Lc/pi output tuple is bit-identical to its old
counterpart. Precisely76 formerly valid predicates now fail. All per-leaf
bounds and all failed leaves are retained in the full raw report; the
small receipt carries the first failure and summary counts. No predicate
was changed to convert any of these failures into acceptance.

### Actual cost and operation counts

Total measured supervisor+subprocess CPU is31.965007580s, comprising
31.414464 subprocess CPU and.550543580 supervisor CPU. Worker accounting
records29.880111699 process CPU and1.449228 compiler/helper CPU; the
remaining subprocess overhead includes worker startup and pre-accounting
work. Native bound calls total29.221249906CPU-s. Wall time is
31.616981617s. All are within the prospective180CPU-s cap; watchdog stop
is false and native/report error lists are empty.

The333 native calls comprise one constants call and332 numerical leaves.
Aggregate native counters, in the frozen order, are:

    ratio_calls       8,439,552
    sin_cos_calls    18,980,740
    pole_charts         17,900
    global_fallbacks         0
    lazy_S_skips           232
    analytic_floor_skips     0
    profile_scans          101
    boards                999

The analytic n>=64 floor correctly did not activate at n32. The232 lazy
skips coincide with the232 passing far leaves. The full checker run has
no hidden harmonic fallback; the zero global-fallback count also shows
these particular losses cannot be attributed to resorting to the coarse
global caps. This does not isolate a single tighter replacement formula.

Old v3 accepted this exact candidate in139.405409 subprocess CPU seconds;
the new failed check used31.414464 subprocess CPU seconds. This measures
the cheaper unsuccessful replay only. Since the outcomes differ, it is
not an accepted-certifier speedup or evidence of a complete cheap
certifier. The mathematical source review remains valid for enclosure
correctness; adoption on this unchanged tree fails its tightness test.

### Frozen provenance and retained output

Publication-content checks passed for every pinned code/data input and
the supervisor. The candidate stayed21338 bytes with SHA`97c3391816...`;
prototype SHA`178bbe5a...` and wrapper SHA`d3fc74db...` were unchanged.
All5 project Python source modules, the Python executable, input snapshot,
executed adapted builder, source snapshot, preprocessed unit, binary and
254 build/runtime entries were checked unchanged after execution.
The closure contains4 toolchain entries,13 toolchain-runtime entries,
212 headers,6 dependency inputs,8 linked and8 actually loaded entries.
Actual loaded mappings were checked in the worker before and after the
full replay. Python3.12.14 and Debian g++14.2.0 were recorded. No seed is
used by this deterministic replay.

Essential receipt `evidence/c02-cheap-n32.json`:4417 bytes, SHA256
`924e8ebbe15ff8fd9a46e1d6c6887ae77e47fa4533af548df864fcea19bf3f41`.
It pins all raw artifacts and the exact command. Under
`local-output/argmax-bridge-20261105/cheap-C02/n32/`:

| Artifact | Bytes | SHA256 |
|---|---:|---|
| checker-report.json |189283|`fe8436d5d7e6232d9e235052abf7bd69a2833883a394c16a602ddb1fdd664157`|
| native-calls.jsonl |120105|`7ed5e356b08d996800c48777351989c5875972afe83374bb8117d0c0281032d2`|
| worker-accounting.json |152|`46c724a10715cd0d10dfbc95876ab9491df5bb689f8e31b4811a4d4816d3fd6e`|

Raw outputs remain local and regenerable from the published source and
frozen input; physical archive transfer is pending. The one-shot wrapper
will refuse reuse of this output directory or essential receipt. Source,
input, controls, old C01 reports, and the old accepted v3 receipt were not
edited. No new degree or status of PD-T099 follows from this failed
known-candidate replay. This authorized execution task is complete.
