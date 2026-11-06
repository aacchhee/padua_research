# D03 near-only pilot preparation

2026-11-06; rules/input `f1ba23cfbfb557dd491730f9837f5efe413e7c75`.
Codex, parent-assigned Sol medium; serving metadata unexposed.

**Pilot not executed.** The authorized deliverable here is a concrete
one-shot proposal and source for root review. The corresponding gate is
[D03-near-only](../ideas/D03-near-only.md); exact scope, H3 application,
API, caps, measurements and stopping semantics are in
[SPEC](../code/post_audit_D03_near_only/SPEC.md).

## What preparation established

The old N3 float driver cannot be invoked unchanged for the requested
near-only512 study. It has no near-domain option, initializes the whole
phase square, hardcodes a larger corner patch only at33/64/128, and
writes an existing receipt destination. The chosen implementation is a
thin new domain driver around the unchanged C sources. This difference
requires distinct source/domain inspection before execution. No inherited
source or exact checker was changed.

The full PD-T369 theorem covers every n>=2, hence512. Its physical
H<=10^-11/n^2 guard is checked by the new driver through the sufficient
quadratic upper bound in exact Fractions of the stored box endpoints.
The corner class uses that guard; the separate noncorner defect
comparison remains necessary. The n2..128 common finite patch is never
applied at512. The old kernel's analytic constants remain diagnostic
floating guards and are not converted into exact enclosure claims.

Proposed fixed work: both radii1/2 then1/8; four signed quadrant roots;
breadth-first longest-side split;128 visits or720CPU-s per case. Stop
that case after a completed native call costs>60CPU-s. Total1800CPU-s
including compilation, precision helpers, n32 three-point controls,
workers and supervisor. No schedule/precision change, pilot retry,
additional degree, producer campaign, exact checker or Syvert pack.

The scope is a capped **floating partition diagnostic**, not just a
point sample. If a queue empties, the structural routine checks that
its leaves partition the original square and outside-near exclusions
are sound as dyadic geometry. If the queue remains, coverage is
INCOMPLETE and the frontier is retained. Arithmetic is ordinary C
double/Python float/libm; even a complete floating partition proves no
new global maximum theorem or exact-checker throughput. Per-box native
timing and predicate margins are direct measurements if the run later
occurs. Exact checker time must remain unavailable, not a proportional
allocation of old total CPU.

## Source and proposed command

New wrapper:
`../code/post_audit_D03_near_only/pilot.py`, SHA256
`32c6940afc45023b6a9c9082f59586db77634d31f3bad8301e4698269737c1e9`.
The immutable existing source identities and old-driver identity are in
`../code/post_audit_D03_near_only/SOURCES.json`.

After root approval and distinct source/domain review only:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D03_near_only/pilot.py --run-once

Output would be confined to
`local-output/argmax-bridge-20261105/post-audit-D03/near-only/`.
Source edits invalidate this proposed candidate and must be separately
reviewed before execution. The wrapper refuses an existing registration.
It preserves checkpoints before native calls, all completed numerical
results and first failure stdout/stderr; it never rescues a failed box.

## Verification performed and remaining review

Performed only static source inspection, unchanged-input hashing,
novelty-gate refresh and Python AST parsing. The AST parse passed without
importing the wrapper, compiling C, loading a library or calling a
numerical function. There are no measured512 results, build timings,
leaf counts, margins or runtime claims to report.

Distinct review should check the new domain roots, signed/parity
interpretation, exact H3 guard, API early-return/profile semantics,
controls, structural partition routine, source pins, aggregate CPU
watchdog and fixed stopping/no-rescue policy. The original P3 growth-law
kill and n2048 cost target remain untestable at this single degree.

Runs needed: the proposed one-shot command above, **only after** the
root's review and a distinct source/domain review. No execution is
authorized by this preparation record alone. No Git/shared file change.

## Pre-execution source-review corrections

The first source candidate, SHA70b11d63..., was not run. Distinct review
identified a blocking supervisor issue: polling a subprocess without
draining PIPE output could deadlock on the compiler's macro output.
It also identified missing nonfinite scalar-reference checks, and
recommended atomic checkpoint replacement. These were corrected before
any build or numerical execution: direct output files, fixed per-command
wall deadlines, explicit finite/positivity guards and atomic temp-file
replacement. A process-exit race during group termination is handled.

The original source/SPEC/inventory bytes are retained with full hashes
in `local-output/argmax-bridge-20261105/post-audit-D03/near-only-preparation/freeze-01/`.
This is local preparation provenance, not an archival availability claim.
The new source hash above supersedes that unexecuted candidate for
review. The gate remains the same P3 implementation variant: these
corrections change execution reliability and diagnostic validation,
not the mathematical mechanism, domain, thresholds or box schedule.
Focused review of the current bytes is still required before running.
