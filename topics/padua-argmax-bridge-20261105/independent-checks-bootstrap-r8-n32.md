# Supplementary independent full replay — bootstrap round8 n32

2026-11-06. Rules/source commit
`c8bdb63de00984701515a2d9c193dea32766a6c0`; repository rules are unchanged
from the preplay review. Distinct reviewer `/root/review_bootstrap_r8`,
coordinator allocation Astra high; serving metadata unexposed. Required
Claude audit remains separate. No source arithmetic, candidate, old proof,
old review, old receipt or Git state was changed by this worker.

## Preregistered one-shot execution

The coordinator explicitly released one complete independent Arb replay
only after the accepted [preplay mathematical/source review](independent-checks-bootstrap-r8.md)
and the developer's completed MPFR candidate. This is a known-degree n32
overlap calibration, not a degree-range extension or complexity theorem.

Frozen input:
`local-output/argmax-bridge-20261105/bootstrap-r8/n32/n32-phase-compact.json`,
21338bytes, SHA256
97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e.
It contains364leaves:32outside,280far,28corner-orbit-plus-defect and
24maximum-exclusion-plus-defect. There are no pending boxes. Producer
accepted=false is preserved and does not supply the independent verdict.

The new reproducible supervisor is `code/phase_checker/check_r8_run.py`,
frozen before execution at SHA256
77e543ed9c2e37b16a8af42e711c8e1f586918498767181a610f81f6d0adef4b.
Actual supervisor command:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/check_r8_run.py --run-once

Its fresh worker uses `runpy.run_path` on the unchanged frozen checker with
exact CLI arguments equivalent to:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/check_r8.py local-output/argmax-bridge-20261105/bootstrap-r8/n32/n32-phase-compact.json --kernel round5 --output local-output/argmax-bridge-20261105/bootstrap-r8/checker-n32/checker-report.json

The raw receipt records the fully resolved executable/argument paths.
Runpy only permits an external CPU-accounting sidecar after SystemExit;
no checker function, interval calculation or acceptance predicate is
modified or intercepted. Worker own CPU and waited compiler/build-helper
CPU are measured separately. An independent process-group watchdog polls
aggregate self plus reaped-child ticks and kills at1188CPU-s; worker
RLIMIT_CPU is1190soft/1191hard, with the total acceptance ceiling1200CPU-s.
The margin covers polling and accounting overhead. No overwrite, retry,
max-leaf cap, source change, tree refinement or other degree is allowed.

The worker pins checker3c71ada8..., old checker437378a5..., build helper
19a5a7c2..., unchanged hybrid-v2 kernel17fea91d... and exact candidate bytes
before launch. The parent rechecks source/input/supervisor after completion.
The independent build uses a fresh isolated translation unit, binary,
header/toolchain closure and FLINT/GMP runtime snapshots; actual loaded
mappings are retained in the raw report. The supervisor also rehashes the
recorded build/runtime entries after replay. The finite energy premise
remains the authenticated2..128 receipt, not the new eventual-energy proof.

## Actual outcome

**FAIL / certificate not independently accepted.** The one authorized
replay finished normally with checker/worker/supervisor exit1. Every one
of364leaves was checked; pending0, failed20, passed344, complete=true,
accepted=false. This is a completed rejection, not a cap or partial run.
The first failed block is stopped: no retries, source changes, refinements
or other degrees were executed.

Actual timing and guard outcomes:

| Measurement | Result |
|---|---:|
| Checker-worker process CPU, including final serialization/accounting |134.957831783s|
| Waited compiler/build-helper child CPU |1.172865s|
| Supervisor's total reaped subprocess CPU |136.175287s|
| Elapsed wall |136.206298841s|
| Process-group watchdog stopped |false|
| Source/input/supervisor unchanged after |true|
| Build/runtime entries independently rehashed after |254, all unchanged|

The total includes process startup/exit overhead, so it slightly exceeds
the sum of the two internal worker measurements. Start/end UTC:
2026-11-06T09:24:25Z / 2026-11-06T09:26:42Z. The1200CPU-second ceiling
was respected. A shorter rejected replay does not establish a speedup of
an accepted certificate; the round6 accepted992-leaf baseline is unchanged.

The essential receipt is [bootstrap-r8-n32.json](evidence/bootstrap-r8-n32.json),
SHA2565ead6761025c1df1505543c574068ea7620c375416a92adcc4834db8133b291f.
It records exact argv, input/source/wrapper identities, all counts, CPU,
exit, runtime checks and raw-output locators. The raw independent report
at the output path above is168068bytes, SHA256
b7801039c828a200f46aa44787cca370e6fcc09c1e300f196d160b76877107a1.
stdout has identical bytes/hash; stderr is empty. Worker-accounting sidecar
is643bytes, SHA256941dd8f5b9e0c4ad739c711f4040cd2c2bc1cda14153554fe7a405c9268de880.
All raw records remain local and unchanged. The fresh checker binary is
60728bytes, SHA256c21f33079d590cea57fe4a29af71b14acc8ee69c2ca751844b9b9c0e93a401f2;
its source snapshot retains reviewed kernel SHA17fea91d.... The complete
preprocessed/toolchain/header/linked/loaded manifest is in the raw report.

## Read-only failure classification

No additional kernel execution was used to classify the saved result.
All20 failures are `maximum-exclusion-plus-defect`, exactly5 per root.
Every failed box passes the exact half-diamond geometry predicate.
All32outside,280far and28corner-orbit leaves pass, as do4 of the24bootstrap
leaves. The failed condition is solely the mandatory strict noncorner
inequality U_S-d<L; it is not the corner maximum-exclusion theorem,
root coverage, premise authentication or a failed inward-sign guard.

For each failed box the independently returned defect lower bound is0.
The common independent L is exactly1547210883711321/140737488355328
(approximately10.993594541100443). The exact positive strictness excesses
U_S-d-L range from

    3815219210361/140737488355328
    to32145262421111/140737488355328,

approximately0.027108762952544 through0.228405827024226. Thus none is a
rounding tie. Corner_upper also exceeds L on these boxes, but that
comparison is deliberately not required by the new bootstrap leaf.

For example, root0/path111111011 is
[-0.29452431127404316,-0.1963495408493621] x
[-0.1963495408493621,0]. Its saved Arb bounds are
U_S=11.174094925592955, U_C=11.13400010303907, d=0, giving positive
noncorner excess0.18050038449251282. Its producer diagnostics were
U_S=11.321962909069983, U_C=11.286671242737283,
d=0.4136264866783589. These values are compared only as diagnosis;
producer bounds are never imported into the independent checker.

Across all20 failed leaves, the independent S upper bound is no larger
than the saved producer S upper bound, while the producer has a positive
defect bound in every case. Combining the independent S with those
producer defects would pass algebraically, but is not an independent
certificate and is not done for acceptance. This isolates loss of a
positive independent defect bound as the practical bottleneck in this
candidate. A lower bound0 does not assert that the true defect is0, and
an upper estimate above L does not assert that any true value exceeds
Lambda_c. These failures are not counterexamples to the argmax theorem
or the accepted bootstrap reduction.

## Disposition and possible next bounded test

The preplay source/mathematical sufficiency review remains accepted.
This particular complete producer tree fails the separate independent
arithmetic gate; no complete round8 certificate or higher-degree result
is established. The failure, original tree and raw diagnostics are frozen.
The finite energy range2..128, known global range2..40 and separate enormous
analytic energy onset are unchanged. Required Claude audit remains pending.

For a future separately gated round only, the cheapest useful test is a
bounded examination of the independent projected-defect enclosures on
representative failed box shapes: identify the limiting noncorner center
and which interval pair terms lose their positive lower bound. Compare
that diagnosis with the existing producer calculation and already reviewed
mathematical defect identities, retaining independent arithmetic. This
would distinguish conservative interval dependency from insufficient box
width before considering any source optimization or new partition.
It would not need a new whole-degree job. No such test, alternative
arithmetic, refinement or successor round was executed here.
