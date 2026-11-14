# D03 near-only floating pilot: proposed one-shot contract

**PREPARATION ONLY. Pilot not executed.** Root review and a distinct
source/domain review must precede any invocation. Rules/input head:
`f1ba23cfbfb557dd491730f9837f5efe413e7c75`,2026-11-06.
Codex, parent-assigned Sol medium; serving metadata unexposed.

## Fixed question and finite domain

Measure whether the existing N3 natural-floating-interval kernel is a
useful producer on the near phase diamond at **n=512 only**, separately
for rho0=1/2 and1/8. There is no all-degree or n2048 projection.
The original source n3_float_v3.py has no near-only option, initializes
the whole [-pi,pi]^2 square, transfers its larger corner patch only at
n33/64/128, and writes an old evidence destination. Its unchanged direct
invocation is unsuitable and will not be used. No inherited source is
edited. The new thin driver changes domain/scheduling and provenance;
the exact compiled kernel and arithmetic remain unchanged.

Each case targets D_rho={|alpha|+|beta|<=rho}. Initialize the four closed
quadrant squares of [-rho,rho]^2 in lexicographic quadrant order, each
with its own root0..3. Preserve all signed quadrants. On a box outside
the near diamond, minabs(alpha interval)+minabs(beta interval)>rho,
record outside-near. Otherwise bound the entire box, which may cross
the near boundary, using the unchanged kernel. This overshoot is
conservative at the mathematical-domain level; the floating arithmetic
is not an enclosure proof. The complement rho>rho0 is **unmeasured**;
no far theorem is assumed or inferred.

Breadth-first queue, longest-side bisection, alpha on ties, midpoint
lo+(hi-lo)/2, lower child then upper. No priority/adaptive queue, tree
rescue, post-hoc radius/precision change, extra degree or repeated run.
The splitter is the inherited policy, now applied only to this domain.
128 **visited** boxes per case (including outside-near geometry boxes),
not128 accepted leaves or128 required native calls. The result may be
an incomplete partition. Both cases are scheduled, in fixed order
1/2 then1/8; a numerical/control/build failure stops the whole invocation.
A normal completed-case cost stop does not change the second schedule.

## Kernel API, arithmetic and predicates

Compile unchanged phase_probe.c and n3_meanvalue.c; the latter includes
the unchanged effective-2 box_pilot.c. No exact checker is imported.

    int n3_box(int n, double al, double ah, double bl, double bh,
               double corner, double eps, int local, double out[6]);

Return0 means the numerical routine completed,1 allocation failure,
2 invalid/nonfinite result. out[0]=S upper diagnostic,
out[1]=corner-orbit upper diagnostic, out[2]=noncorner defect lower
diagnostic, out[3]=1 if projected profiles were actually computed,
out[4:6]=natural bounds before the derivative improvement. The kernel
may return out[2]=out[3]=0 after an early exit; this is not a measured
positive defect. Profiles still cost O(n^3); the board has O(n^2)
entries/kernel calls, without a uniform O(n^2) arithmetic-cost claim.
2026-11-06 clarification requested in source review: rp()'s near-pole
fallback can loop O(n) times per entry, so board arithmetic can itself
reach O(n^3), separately from the projected-profile loops. This changes
no execution behavior or cost-stop threshold.
Every returned quantity is ordinary C double/libm, without directed
rounding. The driver uses ctypes.c_double and Python float. Record
sizeof(double), Python float radix/mantissa and compiler float macros;
expected host format is binary64,53 significand bits, but the eventual
runtime record must state the observed compiler/platform values.
Reject nonfinite or nonpositive corner references/epsilon, nonfinite
point-control references/differences and nonfinite signed margins.
JSON checkpoints are written to a temporary file and atomically
replaced, preserving the last complete checkpoint on a hard stop.

Corner reference is unchanged phase_lambda(n,pi,pi), which is the
nonnode corner because n+(n+1) is odd. eps=10^-12(1+corner), inherited
from n3_float_v3.py, is a **diagnostic comparison cushion**, not a
rounding-error bound. Accept the diagnostic box by this fixed order:

1. far if S_upper < corner-eps;
2. local-corner-plus-defect if the H3 guard applies and
   S_upper-defect_lower < corner-eps;
3. corner-orbit-plus-defect if corner_orbit_upper < corner-eps and
   S_upper-defect_lower < corner-eps;
4. otherwise split.

"Far" here is only the inherited S predicate's name. It can occur
inside the near domain and does not mean that an outside phase region
was measured. Record every returned component, branch, projected-profile
flag and signed margin, including failed comparison margins.

## Explicit H3 applicability at512; no n128 patch transfer

Read PD-T369, effective-2/theory/corner-n2-local-radius.md, in full.
It states strict corner descent for every integer n>=2 and physical
inward H=h_x+h_y<=10^-11/n^2, at both parity-correct nonnode corners.
Thus n512 satisfies its degree floor. For every point in a signed phase
box set a=max|alpha|,b=max|beta|. The corresponding actual corner has
physical increments1-cos(|alpha|/n),1-cos(|beta|/(n+1)); therefore

    H <= a^2/(2n^2)+b^2/(2(n+1)^2).

The driver evaluates this sufficient upper bound and the threshold as
**exact Fractions of the stored binary endpoints**. local=true only if
that upper bound <=1/(10^11 n^2). It applies the theorem only to the
corner class, while the separate noncorner defect comparison remains
required. Equality at zero phase is permitted by the corner theorem;
strictness away from zero is its inherited scope. No H3 loss constant
is asserted outside its own radius. The larger1/128 phase square from
the finite n2..128 batch is never transferred to n512. The older
physical n^-6 radius is not needed by this pilot's conservative guard.
This guard/domain implementation is a review obligation, not a new
mathematical theorem or a certification by floating outputs.

## Controls and independent structural accounting

Before512, run only three n32 point boxes: (0,0),(-1/32,0),(0,-1/32).
Compare n3_box to the separately implemented unchanged phase_s and
phase_lambda sums for the actual(n,m) corner and one admissible
noncorner(16,17) center. Require scaled violations<=10^-10(1+|S|),
with the inherited diagnostic tolerance. This checks finite numerical
consistency, not whole-box validation or a new degree proof. No full
n32 certificate, calibration sweep or model fitting.

After each case, a separate exact-rational **structural** routine
reconstructs every leaf/frontier box from its(root,path), checks a
complete prefix-tree partition of all four root squares, and checks
outside-near exclusions. Its time is reported separately. It does not
recompute S, corner or defect bounds; it is not an exact mathematical
checker. No current exact checker CPU is available: record null,
not a projected cost. A hard-stopped worker retains the checkpoint
before its current native call; it has no completed structural check
unless the saved summary says otherwise.

## Fixed resource and stopping contract

Total **1800 aggregate CPU-s**, including compiler, compiler-format
helpers, controls, both workers, Python startup and supervisor.
The supervisor samples process-group CPU with a1790s safety trigger;
final accounting uses waited-child plus supervisor rusage. Build cap60s,
compiler-version helper10s, float-format helper10s, n32 controls60s.
Each512 case stops voluntarily at720 process-CPU-s or128 visits;
worker hard CPU limit740s, parent per-worker750s. No unused allowance
is transferred to enlarge a later case. Worker stdout is small.
All subprocess stdout/stderr go directly to files, including compiler
macro output. The supervisor never waits on an undrained output pipe.
Each command additionally has fixed wall limit
min(900,2*command_CPU_limit+30) seconds, so a hung or idle subprocess
does not evade the CPU watchdog. A wall stop preserves its first
stdout/stderr and checkpoint and stops the invocation.

Stop the current case after any completed native box call costs>60 CPU-s;
record the box, its output, margins and pending frontier. This is a
prospective **implementation cost kill**, confined to this unchanged
kernel and fixed pilot allowance. Arithmetic/nonfinite/control failure
stops the whole invocation and preserves its first report/checkpoint.
At a box/CPU cap, the case is INCOMPLETE, not a mechanism refutation.

The original P3 at-least-linear-growth kill and the <=1000 CPU-s
n2048 projection cannot be evaluated from one degree. Do not label
either satisfied. An informative positive result would be both completed
floating partitions within these caps, positive recorded diagnostic
acceptance margins and passed controls/structural checks. Even then it
establishes no exact-checker throughput or global argmax theorem. The
root decides whether the measured kernel/leaf quality warrants any
further design; no second run is preregistered here.

## Proposed invocation and recorded artifacts

Only after root approval and distinct source/domain review:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D03_near_only/pilot.py --run-once

The wrapper itself does not import NumPy/BLAS; the thread settings make
the intended one-worker environment explicit. Frozen input identities
are in SOURCES.json. Driver SHA256:
`32c6940afc45023b6a9c9082f59586db77634d31f3bad8301e4698269737c1e9`.
Source changes invalidate this review candidate and require a refreshed
gate/source review before execution. This is not authorization to run.

Output only under
local-output/argmax-bridge-20261105/post-audit-D03/near-only/.
Record preregistration/source hashes, commands, compiler/binary/header
inputs, format macros, worker-loaded file hashes/maps, numerical trace,
per-case checkpoints, retained leaves/frontiers, measured margins and
separate producer/native/structural/aggregate CPU. No large output is
committed. A later short receipt may summarize the raw file identities.
The runner refuses an existing preregistration; failures are never
overwritten or rescued. The files are planned, not currently generated.
