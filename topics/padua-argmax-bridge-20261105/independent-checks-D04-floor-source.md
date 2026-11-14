# D04 stronger-floor adoption: independent pre-execution source review

2026-11-06. Rules/input head `5264178be22cc80f61952ff4cc534e2866073d44`.
AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md were read in this
review session; their bytes are unchanged from the previous reviewed rules
head f1ba23cfbfb557dd491730f9837f5efe413e7c75. Distinct Codex reviewer,
parent-assigned gpt-6-astra medium; serving metadata unexposed.

**Verdict: PASS for the frozen, bounded four-box component experiment below.
No build, native library load, board evaluation, pilot, or native replay was
performed by this reviewer.** Root must release execution. There is no new
mathematical proof, full-degree certificate, complete cover, timing comparison
against an old C08 run, or throughput extrapolation in this verdict.

## Scope and reviewed identities

This is a technical implementation review of already accepted C02 mathematics
inside already reviewed C08 arithmetic. The novelty-gate exception applies:
no new mechanism or novelty/equivalence classification is supplied here, and
no negative mathematical conclusion is inferred. The author's idea record was
read for scope; its novelty-gate coverage is not independently approved here.
This supplementary source check does not replace the formal Claude handoff.

Read the complete D04 SPEC, controller, predicates, builder, producer/header,
CASES, SOURCES and FREEZE; the full accepted C08 source review and C08 source
comparison; C02 dense-band theorem and independent reconstruction, especially
its exact physical domain and backend boundary. The unchanged PD-T369 radius
premise was read in full during the D03 review earlier in this session.

| Artifact | Final SHA-256 |
|---|---|
| controller.py | `3a33f45a191681d198e3947b192f4ec79f1de5ba72f5ddeda2aab09de1091e1b` |
| predicates.py | `3ac60e7fcf5a97acfb362907d01dfb7e16275eabfffbab6537248e3ffe11b595` |
| producer.c | `b90f0571c1ca623e70b440bc5e43d23d65811d7ae5455f31416bb7c489f68c77` |
| c08_interval.h | `275936b502180f2d92af94eb2138815114ba75afb9c258cadffa44e580be0a03` |
| build.py | `459cffb34ecbccb5c5e81042600c7e0e838d6399841c2094602e36a1ae32a0d3` |
| CASES.json | `8d09c9e7c187201bba19ea3c62b8187c77c9f13f378e73efa915d74e937aa49a` |
| SPEC.md (review identity only) | `42f98526e4f4addb48647c63cda8e3c03a41dbe4b5a43d7e9674454ff2a636d7` |
| FREEZE.json | `b7f0e9e718bfdd465cea02d07d80aa1ab753cafe06d4a65b4fa2f054439f7766` |

Initial controller `f461094e0c038fc14cd11b13e010abc8b302a5af74bc153b196893003a0df81f`
was not cleared. Author corrections below preserve its unexecuted candidate in
local preparation storage. Reviewer made no author-file or Git changes.

## Findings and author dispositions

1. **MAJOR, resolved — registered freeze identity.** Initial worker checked
   its controller identity and the current manifest's files, but not whether
   that manifest was the one preregistered. Changing another file together
   with FREEZE could therefore evade the registered input check. Final worker
   compares FREEZE identity with registration before build and on normal exit;
   its finally path also checks it on ordinary exception/CostStop exit.
   A focused extracted-prefix test rejects a mismatching registration.
2. **MAJOR, resolved — executable prose pins.** Initial runtime checker hashed
   registry, theory, idea, attempt and SPEC prose against frozen expectations,
   contrary to WORKFLOW's prohibition on new executable prose pins. Root
   confirmed there was no exception authorization. Final runtime enforcement
   covers code/data/ancestors; prose identities remain passive review context.
   A synthetic missing-prose test passes, while a changed code file fails.
3. **MAJOR, resolved — aggregate reserve scope.** Initial next-box reserve
   used only worker/descendant CPU, omitting supervisor CPU included by the
   170-second safety trigger. Final check adds supervisor own/waited-child
   CPU from /proc and requires aggregate<160 before the next n512 box. The
   live worker has not been reaped by its supervisor, so it is not counted
   again in that parent's waited-child total. This is sampled Linux CPU
   accounting, with the same clock-tick granularity as the supervisor.
4. **MAJOR at helper API scope, resolved — integer physical centers.** Initial
   center_scope admitted nonintegers, e.g. J=K=0.5, as odd physical centers.
   Final helper requires literal integers for n,J,K before ranges/parity;
   six noninteger/bool controls reject. Scheduled integer inputs are unchanged.

No unresolved MAJOR/BLOCKING finding within this bounded source-review scope.

## Mathematical-premise consumption and native delta

An independent literal source comparison establishes that the sole native
change from accepted C08 producer270eb7b0... is
`out[2]=1./2048` to `out[2]=n>=160?1./32:1./64`, inside its existing
n>=64 and full_half_radius guard. The header is byte-identical. The builder
changes only its output destination. Native n<=512 remains unchanged, so no
n4096 implementation is implicitly admitted.

The C02 premise is for signed phases satisfying the **entire box** bound
maxabs(alpha)+maxabs(beta)<=1/2 and physical odd centers. Its projections
apply only to interior center coordinates; every noncorner has at least one
such coordinate. Physical endpoint-coordinate cuts use alpha>=0 at J=0,
alpha<=0 at J=n, and the corresponding beta signs at K=0,m. The exact helper
distinguishes entire physical boxes from physical subsets and excludes
nonphysical points. It does not transpose the unequal coordinate meshes.
The existing native guard uses upward MPFR256 addition of exact binary64
endpoint magnitudes: it cannot admit a box whose exact radius exceeds1/2.
All four selected boxes satisfy the guard exactly, not merely by intersecting
the diamond. Fractions give1/32 at n512; both tiers are exactly representable.

Actual corners are excluded from the defect premise. The consumer requires
an independent cu<threshold or H3 premise in addition to S-defect<threshold,
unless the standalone S predicate succeeds. Every selected box has H3=false.
The H3 sufficient physical-radius bound remains exact on endpoint rationals;
no D03 larger corner patch is transferred. Exact Fraction comparisons use the
directed C08 corner lower endpoint and exact difference with stored epsilon.
Thus no rounded subtraction can turn equality into a strict consumer pass.
Reported float margins are diagnostics; the boolean is evaluated rationally.

The native source still resets c08_fault on each relevant API call and
propagates finite/fault failure as reviewed in C08. Static MPFR workspaces and
counters require sequential calls, as scheduled. out[3] means defect available,
not profile work. Counter6 identifies analytic adoption; counter7 identifies
cubic projected profiles. Counts are reset/read around each call. The n512
controller refuses counter7!=0 and verifies floor/availability when counter6=1.
The algebraic old-C08 comparison changes only defect to1/2048 for calls that
actually took the analytic branch; S/cu and the corner reference remain the
same. Historical D03 output is never substituted into this comparison.

CASES matches every field of the four pinned D03 trace rows exactly. Their
order is fixed10110,10111,01111,11, all root0/n512. The fourth is explicitly
retained as a corner-condition control. No old producer is rerun, and no tree,
extra degree, subdivision, precision change, replacement box or retry exists.
The positive quality gate requires all four completed boxes, at least two
passes among the first three, and an analytic-floor false-to-true conversion.
It remains provisional until the supervisor's CPU/exit result is reconciled.

## Controls, stopping, failure retention and provenance

Literal invalid-degree/NaN/reversed API checks, exact k1 ratio and half-radius
boundary controls precede one n32 point board. The n32 corner-interval overlap
and point consistency checks are smoke controls, not an independent complete
arithmetic validation. The n512 directed constants call supplies the new
reference and is timed under the same first-call stopping rule. All relevant
native outputs/references are checked finite before interpretation; native
output repr is checkpointed before a validation exception.

The first completed call>60 CPU seconds saves its output/counters then stops.
The supervisor kills an unfinished active call after65 sampled group CPU
seconds since its checkpoint. The170 aggregate trigger includes build/helper
and supervisor CPU; worker174/175 and parent179/180 soft/hard CPU limits plus
360 wall seconds provide independent stops. Accepted builder subprocesses
use bounded communicate-based subprocess.run calls; the worker's stdout/stderr
are direct exclusive files, so there is no undrained-pipe polling pattern.
Final accounting explicitly states that its own tiny serialization follows
the sample; the170 safety headroom is not advertised as exact final CPU.

Exclusive preregistration and worker-entry markers prevent reuse. Atomic JSON
replacement retains the last valid checkpoint through an interrupted write.
Checkpoint state contains completed calls, the active call and pending paths;
a hard stop earns no completed result for its active call. First native error
representations/exceptions are retained, and no automatic rescue is present.
A pre-native build failure has only the records reached before that failure.

The unchanged builder records source/header snapshots, preprocessed TU,
compiler/cc1/as/ld identities and their runtime closure, dependency headers,
linked closure and binary. Worker records and compares actual loaded mappings,
observes binary64 macros and default rounding, and hashes frozen code/data
again. The registered FREEZE identity is now enforced. These are source-level
obligations until execution: this review asserts no observed compiled format,
loaded binary, directed n512 result, control pass, or measured runtime.

## Independent checks actually executed

Only source reads and AST-extracted pure-Python functions ran; the full
controller/module entry point, builder and native code were never executed.
Scratch commands, retained locally:

- `python3 /tmp/D04_floor_review/check.py`:40 assertions on tiers, degree
  rejection, half-radius/oneULP guards, signed physical subsets/corners,
  corner-vs-defect separation, exact strict predicates/counterfactuals,
  pinned D03 row equality and literal native/header comparison. First run
  before helper repair used0.052498 CPU-s; focused final run0.043329 CPU-s.
- `python3 /tmp/D04_floor_review/focused.py`:11 checks on final controller
  hash above: passive missing prose vs enforced changed code, registered
  FREEZE mismatch, exclusive worker-entry reuse rejection, completed mock
  call61-second output retention/CostStop, and atomic failed JSON preserving
  the previous checkpoint. Mock callback only, no native call.0.031706 CPU-s.
- A separate AST-extracted helper invocation rejected six float/bool center
  indices/degrees after the integer-guard fix.0.024617 CPU-s.

Total recorded test CPU0.152150 seconds, within the delegated10-second cap.
These tests are independent implementation controls, not native replay or
new numerical evidence. Execution, runtime-manifest inspection, and any
interpretation of the four-box outcome remain subsequent work for root.
