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

## 2026-11-06 execution addendum: both partitions INCOMPLETE

This dated addendum supersedes the preparation-only execution state
above. Root released exactly one invocation after the distinct
[source review](../independent-checks-D03-pilot-source.md) passed and
the frozen candidate was committed/pushed at
`5264178be22cc80f61952ff4cc534e2866073d44`. The reviewed driver remained
SHA25632c6940afc45023b6a9c9082f59586db77634d31f3bad8301e4698269737c1e9;
SPEC3d6284e5... and SOURCESf2c23f94... matched the release. Rules were
unchanged from the preparation head. No source or schedule changed.

Executed exactly:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D03_near_only/pilot.py --run-once

Exit0. Build, both compiler metadata helpers, n32 controls and both
workers exited0. No retry, rescue, additional box allowance or degree.
Both radius cases hit the fixed128-visit box cap with unresolved
frontiers. Neither completed even its floating comparison partition.

| rho0 | Visited | Native calls | Outside-near leaves | Far leaves | Corner-orbit + defect leaves | Pending | Producer process CPU-s | Native-call CPU-s |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1/2 | 128 | 120 | 8 | 25 | 3 | 60 | 216.750025 | 216.428477 |
| 1/8 | 128 | 119 | 9 | 5 | 11 | 82 | 252.281466 | 251.973560 |

There were no local-corner accepted leaves. This is the actual limited
schedule outcome, not a rejection of H3 or of every near-only method.
The terminal frontier maximum-side widths ranged from1/16 to1/8 at
rho0=1/2 and from1/64 to1/32 at rho0=1/8.

Per-status native timings below are sums of the **recorded per-call
CPU differences**, grouped by their actual returned status. They are
measured for this pilot, not proportional allocations of total CPU or
transfers from the older n17/24/32 accounting. Split rows are internal
visited boxes, not retained leaves.

| rho0 | Status | Native calls | Native CPU-s | Calls with projected profiles |
|---:|---|---:|---:|---:|
| 1/2 | split | 92 | 155.975556 | 0 |
| 1/2 | far | 25 | 41.272827 | 0 |
| 1/2 | corner-orbit-plus-defect | 3 | 19.180094 | 3 |
| 1/8 | split | 103 | 170.857484 | 0 |
| 1/8 | far | 5 | 8.044896 | 0 |
| 1/8 | corner-orbit-plus-defect | 11 | 73.071180 | 11 |

At rho0=1/2, projected profiles ran on3 calls costing19.180094s;
117 calls without profiles cost197.248383s. At rho0=1/8,11 profile
calls cost73.071180s and108 calls without profiles cost178.902380s.
Most observed native CPU therefore occurred before/without profiles on
these truncated trees. This does not characterize the cost of their
unexplored frontiers. Board kernel-call count remains O(n^2), while
rp() fallback arithmetic and profile loops can separately be O(n^3).

Maximum completed-call CPU was6.571178s and6.946791s respectively,
so the prospective>60s single-call cost kill did not fire. A box cap is
INCOMPLETE, not the original growth-law kill. One degree supplies no
cross-degree box-count law, n2048 throughput projection or cost for
an exact checker. No new finite-degree global certification follows.

The minimum accepted diagnostic far margins were0.03137492680614429
and0.005794439751753089. For accepted corner-orbit-plus-defect leaves,
the minimum corner margins were0.012601913372652263 and
0.002828055989425593; minimum noncorner margins were
0.39188695609574964 and0.5065401747894178. These positive **floating
comparison margins** are not validated bounds on the continuous
Lebesgue function. All comparison components, including unsuccessful
margins on split boxes, remain in the raw traces.

## Actual accounting, controls and identity limits

The structural routines completed successfully for each retained
leaf/frontier partition. Each reported0.0 CPU-s; retain that value at
the timer's effective measurement resolution, without interpreting it
as cost-free checking. These routines check exact dyadic tree/geometry
only. Exact mathematical checker CPU is null: none was executed.

The three n32 point consistency controls passed. Maximum observed
point violation was1.865174681370263e-13, within the preregistered
floating diagnostic tolerance. They do not validate all interval boxes.
Runtime: cc(Debian14.2.0-19)14.2.0; Python3.12.14;8-byte C double;
compiler radix2, DBL_MANT_DIG53, FLT_EVAL_METHOD0. No randomness.
All calculations remain ordinary floating/libm without directed rounding.

Recorded aggregate runner CPU was486.13603s, including the supervisor
and all waited build/helper/control/case processes through final
summary preparation, below the1800s cap. Derived-receipt helpers
separately used0.027376s and0.028886s; they read/hash existing outputs
only and made no numerical kernel call. The aggregate command-window
CPU values include the live supervisor and should not be mislabeled as
worker-only or per-class CPU.

The short [receipt](../evidence/d03-near-only.json) is10,026 bytes,
SHA256`e66c70335a79ec2c594fccd48337ea9dcac97719bc280237cfa999178a0558bd`.
It pins the frozen code/input registration, binary, case summaries,
raw partitions, runtime/header manifests and the artifact inventory.
Original terminal summary SHA256 is
`e0e8d438849a5e6018e43f13999f97ea45a40a5f1c16d08ccb97799337c48904`;
artifact-manifest.json SHA256 is
`3f9a9288cd4a19f7893468f377701fceba8d18fa0f34c782da57f71b2c65632d`.
The first derived receipt was retained locally before adding root's
requested per-status/profile accounting; original numerical files
were not modified.

Identity coverage includes native sources, compiler executable,
preprocessor header dependencies, compiled binary and Python modules
and mapped-library files at worker startup. It does not include every
transient compiler/linker mapping or later transient runtime mapping;
no complete security/trust-closure claim is made. Raw output remains
under the released local-output path, pending the topic's authorized
Padua cold-storage transfer. No archival availability is asserted.

Runs needed within this released one-shot stage: none. Root's
independent read-only receipt/geometry review and decision about any
follow-up remain separate. No further pilot is authorized by these
finite, incomplete measurements.
