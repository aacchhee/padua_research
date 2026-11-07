# Operational variant contract — audit-02 local feasibility

2026-11-07. Developer Codex; technical work requested as gpt-6.1-sol medium,
serving model/effort metadata unavailable to this worker. Rules read at
4a5de2012bad94601c713b2ff5517f2e3fb80af2. Scope is operational repair of
accepted code, no mathematical mechanism or novelty claim; novelty gate
does not apply. Static preparation only; no source import or execution.

## Identity and architecture

All writes are confined to this new directory. Files originate from
syvert2_pack at the input head, with explicit reviewed operational edits.
Original pack, hybrid FREEZE/code, native sources and scientific checker
are unchanged. There is no runtime monkeypatch of engine arithmetic or
engine imports. The local builder authenticates code against a full published
SHA, copies the engine's existing freeze closure unchanged, and includes
local operations plus pinned arithmetic assets under a new local manifest
schema. Builder execution, resulting artifact identity and release are
separate from this source preparation. Existing ZIP8274249f… is untouched.

## PA1: directly observed status

server and worker normalize SIGCHLD before any child. Nondefault inherited
dispositions are normalized then refused, with a flushed JSON stderr record
of the original disposition; accepted preflight epochs record SIG_DFL.
process_guard.Popen repeats this immediately before every operational child
and owns its explicit waitpid status. Missing direct child/ECHILD propagates
as failure, never EXIT0. Cleanup's eventual ECHILD means absence of owned
descendants only, not a fabricated direct status. The original engine
inherits SIG_DFL, has no startup hook under -E -S -B, and never changes it;
therefore its frozen subprocess calls remain valid in this supported path.
No claim covers an arbitrary hostile in-process mutation of engine state.

## PA2: shutdown and recovery

INT/TERM/HUP/QUIT request stop and owned descendant cleanup. Worker sets
PR_SET_PDEATHSIG(SIGTERM) before any engine child and compares getppid with
the explicit supervisor PID, closing the startup parent-death race. SIGTERM
is catchable so the worker can kill/reap the engine. Its own SIGKILL or
simultaneous hard failures can leave descendants until their existing caps;
the persisted state remains false and collection refuses. This is not a
whole-tree termination guarantee for hard kills.

Collection alone can validate a historical writer domain after reboot.
Each run must already have strict source-bound quiescent=true/ECHILD=true;
collection records current boot separately and never relabels the original
domain. Admission/resume still require the original boot and affinity.
Nonquiescent reboot states have no supported recovery in this candidate.

A preflight-only failure with no ledger admission/job can resume only its
preflight under a new epoch. Summary snapshots and epoch records remain
append-only; prior failure is retained even when the working summary changes.
No numerical attempt is rerun. Failed/interrupted attempts remain terminal.

## PA3: scope and return

Root decision: KEEP stop-on-first-failure initially. At most one other active
case is interrupted with the default two workers. Residual set stays exactly
43–62,65–158,161–319 (273). Degrees161–191 use the valid existing numeric
model-free path, three actual corner points and accepted floor tiers; their
lack of analytic leaves does not predict failure. No degree is attempted here.

The admission hash ledger records each degree before its directory/child.
Resume compares pending exactly with prior never_started and reconciles
all ledger admissions against directories. A missing admitted directory
refuses resume. Histories and resume provenance are retained and checked.
This detects supported-protocol accidental deletion/retry; it is not an
authenticated proof against deliberate rewriting/deletion of all history.

verify_return --partial reconstructs every purportedly completed pair using
the unchanged trusted rational checker and full raw closure. Any invalid
completed pair fails validation; exceptions are not silently classified as
failure. Admitted incomplete cases (including no directory after a crash)
are listed separately. Exact completed, failed/interrupted and never-started
sets are returned. complete280=false in partial mode even if all pass.
Ordinary mode still requires exactly280 complete pairs and no failure.

## A7/A8/A10/A12 operational corrections

Preflight compares arithmetic provenance pins to both manifest and file
bytes before ldd/compiler/engine admission. Return validation additionally
compares actual mapped FLINT/GMP/MPFR hashes with those frozen pins and
requires all three families. Engine already checks mappings before/after
against build identities; no scientific-source variant is necessary.

Package root is a fresh resolved /workspace path <=32 characters. It is never
a long source checkout or symlink to one. All receipt bytes remain intact;
the exact <16384 cap can still bind for proof complexity and ends an attempt.

Asset metadata includes public snapshot package-index and binary JSON API
locators in addition to original pool URLs; retrieved bytes must still match
the six unchanged SHA256 pins. Availability of snapshot URLs was not tested.
The snapshot file endpoint uses returned snapshot hashes, not assumed SHA256
identifiers. Cold-storage transfer remains root/AC work and is not claimed.

Return reader checks ZIP declared member sizes, count, expanded total and
inventory BEFORE payload reads: 512MiB/member,24GiB expanded total,
16MiB collection,200000 members. It hashes streamed 1MiB chunks. History is
bounded separately (1024 entries,64KiB each). These operational bounds are
not theorem or raw-size forecasts; overflow refuses without truncation.

Collector streams files instead of materializing them. A deflate prepass
measures compressed payload bytes, adds conservative ZIP/collection overhead
and a1GiB free reserve, then checks the destination volume before writing.
Raw and archive coexist; no deletion/compaction is authorized. Out-of-protocol
mutations during collection fail. Other unrelated filesystem writers can
still exhaust space; an incomplete archive is preserved as a failed artifact.

Runs needed: exact-source independent review, synthetic signal/wait/history/
partial-return/size controls, published source, separately released local
known-case integration. No residual campaign or Syvert2 rebuild is released.
