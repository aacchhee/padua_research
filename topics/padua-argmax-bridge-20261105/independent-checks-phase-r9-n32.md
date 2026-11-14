# Supplementary independent full replay — round9 original n32 candidate

2026-11-06. Source publication/input
`b39eec3f61b90815f465442268630c2b2c6b8522`. Distinct reviewer
`/root/review_bootstrap_r8`, coordinator allocation Astra high; serving
model/effort metadata unexposed. Repository rules and the accepted preplay
scope are unchanged. The required Claude audit remains separate.
No producer, candidate, old source, old receipt or Git state was changed.

## Frozen inputs and preregistered execution

The coordinator explicitly authorized one full round9 replay after the
[mathematical/source review](independent-checks-phase-r9.md) and its distinct
bounded controls were accepted and published. This is a new reviewed
backend applied to the exact original tree whose round8 failure remains
preserved in [the old report](independent-checks-bootstrap-r8-n32.md).
It is neither a silent retry under the old source nor a refined candidate.

Original input:
`local-output/argmax-bridge-20261105/bootstrap-r8/n32/n32-phase-compact.json`,
21338bytes, SHA256
97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e.
It has364leaves:32outside,280far,28corner-orbit-plus-defect and
24maximum-exclusion-plus-defect. Producer accepted=false stays preserved;
the independent checker supplies its own verdict.

Frozen supervisor: `code/phase_checker/check_r9_run.py`, SHA256
10bacbc9ff58a44e54f5a95f8065536f113f67999b646b2acd29bf8e5e904078.
Actually launched once, with the exact authorized command:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/check_r9_run.py --run-once --source-commit b39eec3f61b90815f465442268630c2b2c6b8522

The worker executes unchanged check_r9.py via runpy, with CLI equivalent to:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/check_r9.py local-output/argmax-bridge-20261105/bootstrap-r8/n32/n32-phase-compact.json --kernel round9 --output local-output/argmax-bridge-20261105/phase-r9/n32/checker-report.json

Runpy only surrounds the ordinary checker with post-exit CPU accounting;
no numerical function, strict comparison or acceptance predicate is
modified. There is no max-leaf cap. The supervisor refuses an existing
output directory and records actual resolved worker/checker argv.
A process-group watchdog triggers at1188CPU-s, worker RLIMIT_CPU is
1190soft/1191hard, and final acceptance requires total reaped subprocess
CPU<=1200seconds. Checker self CPU and compiler/build-helper CPU are
measured separately. No rescue, further source change, producer rerun,
refinement, second replay or other degree is included in this authorization.

The seven source pins include new checker1161ad5c..., new builder6e29f599...,
v3f52d1a9d..., unchanged acceptance3c71ada8..., r6437378a5..., legacy builder
19a5a7c2..., and preserved v217fea91d.... The candidate, supervisor and all
source pins are checked before/after. A fresh isolated v3 binary is built
from a frozen preprocessed translation unit with header/toolchain and
linked/actually loaded FLINT/GMP dependencies. The checker and supervisor
both verify the reported build/runtime closure after the full replay.

## Actual outcome

**PASS / independently accepted.** The one authorized full round9 replay
returned checker/worker/supervisor exit0, accepted=true and complete=true.
All364original leaves were checked, with0failed and0pending. Counts are
exactly32outside,280far,28corner-orbit-plus-defect and24bootstrap leaves.
No cap, rescue, second round9 replay, candidate change or other degree ran.

| Actual measurement | Result |
|---|---:|
| Checker-worker own CPU, including final serialization/accounting |138.193144816s|
| Waited compiler/build-helper CPU |1.171140s|
| Total reaped subprocess CPU including startup/exit overhead |139.405409s|
| Elapsed wall |139.434566319s|
| Process-group watchdog stopped |false|
| Source/input/supervisor stable after execution |true|
| Build/runtime entries independently rehashed after |254, all unchanged|

Start/end UTC:2026-11-06T09:42:04Z /2026-11-06T09:44:24Z. The total CPU
is below the1200-second limit. Timings are measurements of this finite
run, not a complexity bound or extrapolated higher-degree throughput.

The small essential receipt is [phase-r9-n32.json](evidence/phase-r9-n32.json),
10224bytes, SHA256
5bdab76556a37552121afabe172d641e57a60026d1b07b36c4f6e5e5069977ae.
Its core records the supervisor's actual argv/status/timing/identity
checks; its labeled saved_output_comparison is the subsequent read-only
verification described below, with no additional kernel execution.

The raw report at the exact output path above is166401bytes, SHA256
05247fa822055bc0dcfd9ceac2932bd9dca97309d7e351be48d6100da61f7df7.
stdout has identical bytes/hash and stderr is empty. The worker CPU
sidecar is641bytes, SHA256
cce783edca39e59a2d26ce170d46307cd79f0c0157d6fec0c08dbcd3dea46cce.
The fresh65168-byte checker binary has SHA256
6fec304ba14ed9dfd207beee3992073d05c82701510869759bdb4130c85c2bee.
The entire source snapshot/preprocessed translation unit/toolchain/header/
linked and actually loaded runtime manifest remains in the raw report.
All raw records and old failed outputs are retained locally and unchanged.

## All previous failures closed, without a tree change

Read-only comparison matched all364(root,path) keys and leaf kinds against
the frozen full round8 reportb7801039.... For all332numerical leaves,
all six nondefect outputs S, corner, Lc lower/upper and pi lower/upper
are bit-identical to the old saved outputs. Every new defect lower bound
is at least its old value. Outside leaves retain no numerical bounds.
Thus this comparison isolates the new defect lower enclosure; it does not
silently substitute a stronger S bound, a different radius or another tree.

All20previously failed bootstrap leaves now pass the exact strict
noncorner inequality. Their new positive deficit lower bounds range
approximately0.38451777061742426 to0.4472473916226339. For those20leaves
the positive margins L-U_S+d range exactly from

    2994108869083203/18014398509481984
    to7568544686090273/18014398509481984,

approximately0.16620643023452802 to0.42013862867008994. The receipt stores
every original root/path with its exact new rational lower bound and strict
margin. These are recombinations of the already saved independent outputs;
no producer numerical endpoint supplies an accepted inequality.

The original round8 completed failure remains a valid historical record:
its v2 kernel returned0defect on these20boxes, while the reviewed v3
algorithm now certifies positive lower bounds. Both enclosures can be
mathematically valid; a weak zero lower bound was never a counterexample
to the theorem. No old source, old receipt or preplay result was overwritten.

## Scientific conclusion and measurement limits

Under the separately accepted holistic phase-cover reduction and fixed
finite energy premise, this complete certificate independently establishes
the n32maximum/equality assertion: the global maximum is Lambda_c and the
two parity-correct nonnode corners are exactly the equality set. This is
validation of an already known degree, not an extension of global2..40.
The finite energy scope remains2..128; the separate enormous analytic
energy onset does not enter this certificate. PD-T099 remains OPEN.

The round6 accepted n32cover had992leaves and recorded checker CPU
382.569138s. This accepted round9 replay has364leaves and measured checker-
worker CPU138.193144816s. This is a useful finite cost/count observation
for the larger bootstrap patches plus the reviewed new defect enclosure;
it does not isolate a general kernel speedup or establish an asymptotic
cost law. In particular, the prior round8 v2 replay of this same smaller
tree was slightly shorter but failed and is not an accepted baseline.

The authorized block is complete. No new producer, refinement, degree or
mathematical round is automatically released by this pass. The required
Claude audit remains separate and pending.
