# D07 actual four-copy point — preparation and source freeze

Rules/input2e4ac49fa0687a7736bc1df82c12e6483b1c7a94,2026-11-06.
Parent-assigned Sol medium; serving metadata unexposed. Root owns Git and
shared state. **No numerical library call or diagnostic was executed.**

Read full accepted D06 proof/idea/attempt and distinct review, plus full
accepted C11 point/partial source, attempt and source review. The technical
[gate](../ideas/D07-fourcopy-point.md) reuses those mechanisms and the
unchanged complete registry screen; no historical novelty is asserted.

Prepared a complete source and bounded controller in
[post_audit_D07_fourcopy_point](../code/post_audit_D07_fourcopy_point/SPEC.md).
The new point API uses rational inward turns on the physical odd grid,
retaining half endpoint factors and1/(2nm), and applies absolute value
after summing all four corrected finite kernels. Accepted C11 files are
included unchanged, with their complete returned radii and weighted tails.

The row engine builds the cubic numerator/monic quartic denominator,
retains every original pole/endpoints directly, and obtains Acb root
candidates at fixed precision/iteration count. It independently certifies
d disjoint Rouche disks containing all d roots for every coefficient
member; uncertain degree, failed multiplicity/coverage, wide buffers,
unresolved sign or partial pole guards trigger complete finite-row
fallback with honest counts. This fallback may occur on every row;
no universal O(n) CPU or useful accuracy claim is made. Exact zeta0/xi0
reductions avoid avoidable common factors; exact nodes return1 and the
nonnode zero corner uses accepted C11 S0. No off-grid alias continuation
is substituted for finite collision values.

The separate512-bit reference uses direct Chebyshev divided differences
and derivatives at exact rational-angle collisions, not production ratios,
roots or partial sums. It is limited to n128 controls. Later large-point
S output is context only. CASES.json freezes n2/17/32 generic/node/corner,
n128 generic/reference and n512 generic/axes. Controller includes all
API controls, exact input pins, full runtime closure, no-overwrite locks,
atomic retention, direct output files,180 aggregate CPU/170 safety,
20CPU completed-call stop and25CPU unfinished-call kill. Generic512
<=10CPU is a finite performance gate, not a full-certifier projection.

Preparation verification only: Python AST parsing and C++ syntax parsing.
A first shell meter invocation failed127 because /usr/bin/time is absent;
its stderr is preserved. Syntax-only point.cpp passed .483437CPU.
Reference controls initially failed syntax (.438618CPU) because the
Chebyshev C API orders degree before input; after reading the actual
header and correcting that argument order, full controls syntax passed
.415403CPU. Total measured syntax CPU1.337458s is below the30CPU compile
allowance. These jobs did not link/load a library or call any numerical
function. Raw prep logs remain under local-output/argmax-bridge-20261105/
post-audit-D07/preparation/. No first numerical failure exists to hide.

Runs needed: distinct source/contract review of the frozen SPEC, full
row/root/fallback/reference source and controller. Only after root release:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D07_fourcopy_point/controller.py --run-once

No full cover, new degree, whole-box enclosure, C08 speedup, source rescue
or further experiment is authorized by this preparation. Broad evaluator
usefulness and certifier bridge remain OPEN. All predecessor code, proofs,
receipts and D04/D06 records are unchanged.

## Initial frozen review and controller response — 2026-11-06

Initial source, SPEC, controller and findings are preserved in Git commit
cbfdb044e184731984e3bf8be487008a86e68c37. Initial controller SHA256
fd561ea714812a70abc4bb2bdc6d3c9fce196be3180e412740c69947483aeb5d
was not executed. Initial source review found no mathematical core/root/
reference enclosure defect, but withheld execution clearance for F1/F2.

F1: the supervisor now enables/verifies Linux subreaper adoption before
spawn and wait4-reaps all orphan helper descendants after worker/group
termination, before a complete descendant-inclusive CPU label. An
incomplete cleanup is explicitly a lower bound and cannot be success.
F2: case results and pending removal are durably committed before a
completed-call cost stop. The combined native point/reference stage
explicitly exposes no intermediate result; completed output pairs survive
a cost stop and no output is invented for an interrupted stage.
The numerical core, finite reference, frozen cases, precision, mathematical
contracts, performance threshold and no-retry policy are unchanged.

Pure Python controller_checks.py extracts only current infrastructure
helpers using AST. A fake worker/middle/CPU-burning grandchild chain was
group-killed; subreaper wait4 collected both helper subtrees, including
.266539CPU-s charged to supervisor RUSAGE_CHILDREN. Completion/CostStop
ledger checks passed. Total measured test CPU .337978s including all
children, below the10CPU infrastructure allowance. No research library,
compiler, polynomial, point/reference or numerical diagnostic ran.
Before-fix local bytes and the test record are retained in authorized
post-audit-D07/preparation/controller-fixes/. Focused source recheck
of these controller-only changes remains required before release.

## Released bounded numerical attempt — 2026-11-06

Root released the reviewed final source in commit
d4956aea3bda9d5ff9917a5b410778fc7adf4fb7. The exact SPEC command
ran once, without retry, source/precision change, rescue or additional cases.
Supervisor exit0/result COMPLETED; no cost stop or arithmetic failure.
All six invalid API controls and all13 fixed point cases completed.
Ten n<=128 cases passed complete512-bit finite-reference containment;
the exact node1 cases use the explicitly allowed converse containment.

| n / case | call CPU s | full Arb radius | numerical row fallbacks |
| --- | ---: | ---: | ---: |
|2 / generic|0.001434|7.63626613e-47|0|
|2 / node|0.000594|0|0|
|2 / corner|0.019210|9.6416123e-08|0|
|17 / generic|0.058328|5.25671492e-10|0|
|17 / node|0.007594|0|0|
|17 / corner|0.023455|1.50088457e-10|0|
|32 / generic|0.115796|5.37436513e-11|0|
|32 / node|0.021633|0|0|
|32 / corner|0.047198|1.58265209e-11|0|
|128 / generic-reference|0.881081|5.86045863e-14|1|
|512 / generic|2.093200|2.58321508e-16|3|
|512 / axis-zeta-zero|2.168013|3.07339362e-16|0|
|512 / axis-xi-zero|2.028607|1.09348787e-15|0|

The n<=128 times combine production point and independent reference;
n512 times are production point calls. They are not a matched scaling
benchmark. The n2 corner radius9.64e-8 is the paid C11 S0/J16 enclosure,
not a failed uniform accuracy promise. No uniform-width promise was made.

The finite generic512 performance gate<=10CPU-s passed at
2.093200s, with lambda in[25.032197529883806, 25.03219752988381] and
full radius2.58321507766e-16. Its514 rows include3 numerical
root-coverage fallbacks,0 sign failures,1012 signed blocks,8096 partial
calls and3365 direct four-copy evaluations including discarded attempts.
This is a hybrid measured success, not a guarantee of pure fast-path
success or universally linear runtime.

The n128 generic/reference used1 root fallback. Both512 axes used0
numerical fallbacks; zeta0 retained2 mathematically eta-degenerate rows,
while xi0 had none. Exact axis reductions, all three small nodal shortcuts
and all three small S0-corner shortcuts were exercised and counted.
S0 shortcut counters do not expose internal C11 work; no zero-cost claim
is inferred from those zero D07 row counters.

The separately measured C11 common-S context at512 was
[25.06801827708105, 25.068018277081052], costing0.596345CPU-s.
It is not an actual-lambda reference and supplies no C08/old-code speedup
ratio. Large512 points have no independent full-board reference here.

Complete waited-descendant run CPU through supervisor serialization was
12.056157s, well below180;
subreaper cleanup/accounting was complete. The final tiny write/print lies
after that explicit sample and is bounded by the registered parent limit;
an exact process-exit time is not fabricated. Metadata-only receipt
postprocessing is separately metered in its raw accounting record.
Fresh source/header/compiler/runtime closure and loaded-before/after
identities agree, and the postprocessor rechecked recorded code/data and
build closure identities. Full raw records remain in authorized Padua
post-audit-D07/point/. No archival upload is claimed.

The small receipt is evidence/d07-fourcopy-point.json. Its generator
is preserved at code/post_audit_D07_fourcopy_point/receipt_postprocess.py,
outside the executed primary freeze, without changing controller/FREEZE/
SOURCES. Regeneration needs fresh primary outputs at the configured Padua
local paths, an isolated workspace without the essential receipt, and the
pre-addendum attempt bytes retained as attempt-before-result-addendum.md;
it must never overwrite or repeat the published first attempt. Metadata
timing and resulting summary hashes can differ. All scientific claims
remain MEASURED point-component observations: no new degree, whole-box
bound, complete cover, global argmax proof or throughput projection.
