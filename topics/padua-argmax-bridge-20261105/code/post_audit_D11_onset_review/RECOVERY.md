# Hash-only recovery preregistration, 2026-11-06

First frozen execution exited1 at line73's author-evidence SHA assertion;
no evidence JSON was written. The original source is preserved byte-for-byte
as check-first-failed.py, SHA256
abeb5d5c147cbd16cdb63843f7cf79c65aab465265c0379f409a31b12b4d429b.
Observed stderr is preserved in evidence/post_audit_D11_onset_review/
first-failure-stderr.txt; stdout was empty. First process CPU was not
emitted and remains UNKNOWN. The enclosing functions.exec tool reported
wall0.3 seconds (the inner exec_command reported0.000028072, not used as
CPU). Charge a conservative1 CPU second for the entire first execution.
This timing is an observed tool receipt, not independently instrumented CPU.

Root inspected the exact hash-only-repair.diff and byte-compared old/new
source: exactly one replacement, incorrect expected hash ending afb47
replaced by actual budget SHA256
34675d877186c34f16a40c2dc5b2470c27ec2fbb40f62b338c2dd24e96583afb.
No arithmetic, precision, degree, threshold, or guard placement changed.
Corrected source SHA256
4816e2ee9109baad796aceb59580c120a5dae8c48a41eb4daf87054750a742d7.

Root explicitly released ONE recovery after this focused review. Before
that execution, register a subprocess.run(timeout=2) wrapper, fresh stdout
and stderr paths, RUSAGE_CHILDREN user+system CPU measurement, wrapper
process CPU and wall-time receipt. This pure checker has no child/thread
creation; the2second wall cap conservatively limits checker CPU. Wrapper
softCPU3/hard10, separate from checker9/10. First charge1 + recovery child
wall cap2 + wrapper softCPU3 leaves the aggregate below10 (subject to the
ordinary OS timeout/CPU-signal scheduling contract). No recovery repeat.

Command from repository root:

    python topics/padua-argmax-bridge-20261105/code/post_audit_D11_onset_review/recover_once.py

The scientific run remains n16000 only. This is an explicit changed-source
recovery of a hash transcription error, not an unreported retry or fallback.
The canonical review report states the timing limitation and actual outcome.
