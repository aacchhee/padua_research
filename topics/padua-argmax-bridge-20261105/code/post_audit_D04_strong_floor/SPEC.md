# D04 strong-floor adoption: prospective source and four-box gate

**PREPARATION ONLY. No build/native/pilot run is authorized yet.**
Rules/input5264178be22cc80f61952ff4cc534e2866073d44,2026-11-06.
Root accepted the four-box preparation plan; root review and a distinct
source/physical-domain review of these frozen bytes precede execution.
Codex, parent-assigned Sol medium, serving metadata unexposed.

## Frozen scope and material diff

C08 MPFR producer270eb7b0f073efcb996c7c832f6e946d37b0e6f780fdac63fc66591332560a5e,
header275936b502180f2d92af94eb2138815114ba75afb9c258cadffa44e580be0a03.
Copy the header byte-for-byte and preserve all ratio, derivative,
rounding, geometry, allocation, counter, profile and native API code.
The single producer change, recorded verbatim in producer.diff, is:

```
if(n>=64&&full_half_radius(al,ah,bl,bh)){
    out[2]=n>=160?1./32:1./64; ...
}
```

The source already restricts n to2..512; the n4096 tier is absent.
The builder differs from accepted C08 only in its local output path.
C08 already avoided cubic profiles within this guard using1/2048;
this adoption changes that floor only. It does not newly remove the
ratio derivative fallback or profile loop. No source in C08/D03 or
ratio/math records changes. No new theorem or novelty is claimed.

## Exact physical noncorner consumer contract

The entire stored binary endpoint box must satisfy
max(|al|,|ah|)+max(|bl|,|bh|)<=1/2, verified as exact dyadic rationals.
Native full_half_radius uses directed MPFR256 and admits the same
closed domain. Merely intersecting the near diamond is insufficient.
All four selected boxes meet this full-box guard; no overshoot excuse
is allowed. Outside it, the stronger floor is unavailable.

For each physical center, n integer,0<=J<=n,0<=K<=m=n+1,J+K odd.
For a represented real(alpha,beta) in the box require
0<=(J*pi+alpha)/n<=pi and0<=(K*pi+beta)/m<=pi.
At interior J/K, the half-radius guard makes these inequalities automatic.
At J=0 require alpha>=0; at J=n require alpha<=0. Similarly K=0
requires beta>=0; K=m requires beta<=0. The exact signs, including
zero, determine physical subsets when a box crosses a cell boundary.
`predicates.center_scope` implements these possible/entire distinctions
on dyadic endpoints. Inadmissible points are not assigned defects.

If both J and K are endpoints, this is an actual corner and the
positive noncorner floor is NOT used. Otherwise at least one of
0<J<n or0<K<m holds, licensing its C02 projection and hence Delta>=floor.
No J/K mesh interchange is used. C08's out[2] is a uniform noncorner
premise, never a defect at the actual corner. The complete box predicate
must additionally accept the actual corner by cu<corner_threshold or
its separately justified H3 local guard. Every selected nonpoint box
has H3=false. At zero point H3 may apply using the existing PD-T369
quadratic physical-radius sufficient guard, evaluated exactly.

For reported acceptance compare exact Fractions of returned finite
binary64 outputs with t=corner_lower-epsilon (exact rational difference).
Accept if su<t, or [(local_H3 or cu<t) and su-defect<t]. This is a
consumer contract; the native branch threshold is conservatively rounded
down and can stop earlier. Epsilon is a fixed comparison cushion,
not an independent rounding-error estimate. A complete experimental
predicate is a component observation, not a complete cover theorem.

## Frozen cases and source-specific counterfactual

CASES.json pins the completed D03 half-radius trace, including every
old output, old profile flag, margin, status and native CPU. All four
have root0, n512; order is fixed:

| path | exact box (al,ah,bl,bh) | old D03 status / flag |
| --- | --- | --- |
|10110|(-1/8,-1/16,-3/8,-1/4)|corner-orbit-plus-defect /1|
|10111|(-1/16,0,-3/8,-1/4)|corner-orbit-plus-defect /1|
|01111|(-5/16,-1/4,-1/8,0)|corner-orbit-plus-defect /1|
|11|(-1/4,0,-1/4,0)|split /0|

First two old S excesses .01395,.02863 are below1/32; third .052996
is above it, providing a quality boundary. The fourth failed the old
corner predicate, so it checks that noncorner adoption cannot silently
accept actual corners. These observations selected the cases before
new arithmetic; they are not predictions of directed C08 output.
D03 uses different floating/libm arithmetic and no directed enclosure.
Matched geometry does not establish performance improvement relative
to an old C08 run, and D03's profile flags are historical context only.

Do not rerun the old n512 producer. On each new call record all six
outputs and counters. If analytic-skip counter6==1, replacing only
defect with1/2048 gives the exact algebraic old-C08 counterfactual for
these identical su/cu bounds. If it is0, no floor substitution occurred
and no stronger-tier benefit is credited. Counter7 must remain0:
no cubic profile branch is permitted in these n512 tests.

## Controls, fixed cost/quality gates and stopping

Only after review: fresh build, no cached binary. Source/header,
preprocessed TU, toolchain, headers, linked and actual loaded runtime
closure must be captured unchanged before/after; versions alone do not
replace native identities. Verify IEEE binary64/default rounding and
no fast-math/reassociation under accepted C08 assumptions.

Before n512: cheap API invalid-degree1/513/NaN/reversed checks,
fixed k1 ratio value/derivative control, exact whole-half-radius guard
boundary checks using dyadic .25+.25 and the next representable larger
endpoint. One n32 point box(0,0) is the only small-degree board control;
its source floor branch is unchanged. Compare its corner constant
interval with historical C08[10.993594541097181,10.993594541103743]
and verify finite output/consistent primitive value. No full n32 cover.
A directed n512 corner constant call supplies its lower reference;
D03's floating corner is context only. Record constants timing too.

Cap **180 aggregate CPU seconds including build, constants, controls,
worker/supervisor startup and finalization**. Use a safety watchdog at
170 process-group CPU, final inclusive rusage must remain<=180.
Single-threaded, sequential calls. No unbounded output pipe polling;
write child stdout/stderr directly to immutable local files. Fixed wall
cap360s and worker CPU hard cap175s. An unfinished native call is killed at65 process-group
CPU-s since its checkpoint; a completed call>60s stops without another call. Native build/helper commands retain
accepted bounded subprocess timeouts. After the FIRST completed native
call (including constants/controls) costing>60 CPU-s, stop the entire
experiment and preserve its output. Do not transfer unused cases into
new boxes, refine boxes, change precision, retry or rescue a failure.
Before a next n512 call, add the worker/reaped-descendant CPU to the
live supervisor CPU read from /proc; require this aggregate to be<160,
leaving at least10 CPU-s below the170 safety trigger; otherwise report an incomplete schedule.

Prospective positive adoption gate: all controls pass, >=2 of the first
three boxes satisfy the complete consumer predicate, and >=1 of them
changes false→true under the stronger floor versus its matched algebraic
old-C08 counterfactual. Every completed call must cost<=60CPU-s and
aggregate<=180. Independently report whether the fourth actual-corner
predicate succeeds; a floor alone never counts as corner success.
Cost stop, arithmetic/control failure, or absent measured floor benefit
blocks further adoption testing; none refutes the theorem or all C08
uses. INCOMPLETE is not a mathematical kill. Even a positive outcome
measures four boxes, with no tree/coverage or throughput extrapolation.

## Artifacts and runs needed

All raw output only under existing Padua local-output namespace
`argmax-bridge-20261105/post-audit-D04/strong-floor/`.
Preregistration pins code, CASES/SOURCES and the machine FREEZE identity
before any compiler/library invocation. SPEC, theory, registry, idea and
attempt hashes are passive review provenance, not runtime-enforced prose
pins. Reviewer inspection checks SPEC consistency against fixed controller
constants and CASES. At worker start/end, the FREEZE identity must still
equal its preregistered value; code/data/ancestor files are also rechecked. Refuse any existing
registration; preserve first failure. Save full per-call timing, outputs,
counters, margins, analytic/cubic branch flags, exact radius/H3 guards,
corner intervals and algebraic counterfactuals, plus all CPU/closure.
The concrete thin controller is controller.py. With no --run-once it
refuses execution; the internal worker additionally requires registration.
Exclusive preregistration and worker-entry markers prevent overwrite or
manual internal-worker reuse as well as automatic retry. The worker
verifies its identity and the registered FREEZE before building; normal
and exception exits recheck that registered FREEZE and code/data pins.
Child stdout/stderr use direct immutable files. Checkpoints are atomic,
contain the current uncomputed call plus prior completed calls and pending
paths, and retain native output repr/first exceptions before interpretation.
The actual loaded closure before the first control is saved immediately,
so a subsequent hard stop retains it. Completed execution also checks the
native closure and all frozen inputs again. The worker summary and parent
supervisor/final-accounting records stay raw; no committed numerical
receipt or measured result exists at preparation.

out[3] is named defect_available_flag, not computed-profile flag.
Only counter6 identifies the analytic floor; counter7 identifies actual
projected-profile computation. These counters, all six outputs, margins,
call CPU and old-C08 algebraic counterfactual are retained per fixed box.
Exact Fraction comparisons alone provide no certificate when the corner
reference is merely floating. Here the reference is the lower endpoint of
C08's directed component corner interval, conditional on its independently
reviewed source/arithmetic assumptions; this four-box attempt is still
MEASURED and supplies no independently checked new-degree certificate.

Proposed command, ONLY after root approval and distinct review:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D04_strong_floor/controller.py --run-once

Root must review the concrete source and arrange distinct review, then
separately authorize the frozen bounded run. The command is a reproducible
proposal, not permission to invoke it during preparation.
