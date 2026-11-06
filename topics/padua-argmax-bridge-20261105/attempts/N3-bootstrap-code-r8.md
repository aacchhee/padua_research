# N3 round8 explicit bootstrap certificate implementation

Developer allocation: Sol medium, inherited parent allocation; serving metadata
unexposed. Rules/input head: `8dc1521cf68f7780bd10e02495f6f71a639c03c6`.
No novel mathematical mechanism is proposed here: this implements the accepted
round7 maximum-bootstrap reduction and fixed independent finite energy theorem.
The mathematical sibling owns the new holistic reduction and novelty record.

Status: code and bounded controls implemented; distinct source/mathematical
review PENDING. No full producer or checker calibration has executed.

## Frozen interface and source

New format `n3-phase-maximum-bootstrap-v2`, explicit mode
`global-maximum-bootstrap`, new kind `maximum-exclusion-plus-defect`.
It requires exact rational maxabs(alpha)+maxabs(beta)<=1/2, an exact integer
2<=n<=128, the fixed independent energy theorem, and the independently
recomputed strict S_upper−defect_lower<Lambda_c_lower comparison for all
admissible noncorner classes. No corner_upper comparison is required for
this kind. The actual physical corner class is handled only as maximum
exclusion; the origin exception denotes the two actual nonnode corners,
not every center at phase zero. All other leaf predicates remain the r6
strict predicates. A complete prefix-free partition of all four roots,
with zero pending leaves and every leaf checked, is required for acceptance.
The old r6 checker rejects this format and kind. It is unchanged.

The fixed `bootstrap_premise` descriptor is exactly:

```json
{"receipt_sha256":"f0c48ea7f55e3a926b36537ebe46724b4305cacb9f1254c6417b2abd9676425b","degree_first":2,"degree_last":128,"normalized_threshold":"3/4","phase_diamond_radius":"1/2"}
```

That candidate descriptor does not supply the theorem. The checker reads
only the fixed repository receipt path, verifies its bytes before parsing,
checks the exact schema,127-case range, integer metadata, threshold and
predicate, independence and pass flags, n2 control, source/build/runner
identities and execution-manifest identity. It verifies current executable
GMP source and collector bytes. It does not pin prose. The accepted small
independent receipt supplies the finite theorem; regenerable bulk endpoints
are not new proof inputs to the phase cover. Old pointwise locality uses
the unchanged r6 exact predicate and independently validated fixed old
range receipt, not a caller assertion. Both premise closures are rechecked
after replay.

Frozen sources (all new):

- `code/n3_bootstrap_r8.py`: SHA256 `9058deac09eec2ddd7cfae4815fdf79d702e52099de13820e44af4f82db0a12c`.
- `code/phase_checker/check_r8.py`: SHA256 `3c71ada8e49829cb897ee1c064fcdc70d08c846afcb1fb067c6c84673e205bb9`.
- `code/phase_checker/r8_controls.py`: SHA256 `13cdf5da05e1ce31416dc5685b0be1c8c3565feb2e3606675607be7c1fc56944`.

The producer keeps the frozen MPFR C/header arithmetic. The independent
checker explicitly selects the corrected round5 Arb backend and imports
only the immutable r6 checker helpers; it imports no producer arithmetic.
The source mathematical reviewer must assess the new Python dispatch,
fixed-premise controls, complete-cover reduction and the following C-call
interface before any calibration.

### Explicit calculation request, separate from locality

The historical C `local` argument occurs only in its signature and at
line39, `if(su<lc-eps||(!local&&cu>=lc-eps)){free(h);return 0;}`.
It bypasses an early exit before calculating the projected defect. The
new explicit Python `producer_bounds(..., always_compute_defect=...)`
requests calculation for oldlocal OR bootstrap_geometry. This supplies
no pointwise descent permission; the Python acceptance dispatch separately
retains old locality or uses the new maximum-exclusion theorem. No C,
header, checker kernel, old source or old evidence was edited.

## Executed bounded controls

Actual successful final command, from the repository root:

```sh
python topics/padua-argmax-bridge-20261105/code/phase_checker/r8_controls.py
```

Exit0,55 controls PASS,2.658776967 command-tool wall seconds,
1.112599918 own CPU seconds and0.422611 MPFR compiler child CPU seconds.
The script did not capture aggregate Arb-build child CPU; no aggregate
child timing is claimed. An earlier52-control version passed before the
explicit MPFR flag control was added (1.604521125 command-tool wall seconds).
These are two cheap control executions, not full degree covers or retries
of a consequential computation. Both inherit bounded CPU limits; their
combined observed sequential wall duration was below5seconds.

Controls cover duplicate/nonfinite JSON, malformed/falsified receipt
metadata and code bytes, fixed receipt hash mismatch, exact rho boundary,
its adjacent binary64 values, invalid degrees/bools/reversed/nonfinite
endpoints, altered mode/format/premise, missing/overlapping/duplicate tree
leaves, incomplete flags, unsupported kinds, oversized bootstrap leaves,
and missing strict noncorner comparison. Synthetic bounds exercise only
parser/dispatch/partition logic and supply no numerical proof evidence.
Fresh independent Arb n2 smoke evaluation returned finite bounds at three
boxes, including the diamond boundary and its just-outside neighbor.

A fresh unchanged MPFR n32 single-box evaluation at `[0,.25,0,.25]`,
which lies in the bootstrap diamond and outside old locality, gives
S_upper=12.019045280465887 and corner_upper=11.967214606575629 identically
with and without the calculation request. The early-exit call returns
defect_lower=0; the explicit request computes0.31109586590546684. This
confirms the dispatch correction computes a bound; it does not assert
that this wide box satisfies the strict leaf comparison.

Small essential receipt: `evidence/bootstrap-r8-controls.json` (5223bytes).
Full local report: `local-output/argmax-bridge-20261105/bootstrap-r8/controls.json`,
SHA256 `29ebe2f79d835cec9c33d0945e0ead642137e0309f8b16fdc2dc0575b8a5e366`.
The receipt preserves exact source sizes/hashes, actual argv, exit,
recorded CPU fields, fresh backend identities and real numerical bounds.
No cold-storage destination is invented.

## Runs needed — only after separate source/math review and coordinator start

The preregistered local input inventory is
`local-output/argmax-bridge-20261105/bootstrap-r8/preregistered-inputs.json`.
It pins new sources, old arithmetic/backend/build sources, both fixed
receipts, independent GMP source/collector and the exact MPFR header.
The coordinator commits frozen reviewed source and reduction before the
single planned known-degree calibration.

Producer, exactly once:

```sh
python topics/padua-argmax-bridge-20261105/code/n3_bootstrap_r8.py --run-n32
```

Budget:1200 total process-group CPU seconds,1100 search CPU seconds,
100000 visited boxes. The parent watchdog stops at1195groupCPU and the
worker has a1195/1196 CPU limit. Fresh n32 destination; no overwrite,
retry, changed arithmetic, adaptive budget or further degree. Stop the
block on first incomplete/failure/cap. A completed output is projected
only by removing diagnostic leaf numbers; exact compact bytes and gzip
are retained with identities. Projection does not supply acceptance.

Separate checker, exactly once on the compact bytes:

```sh
python topics/padua-argmax-bridge-20261105/code/phase_checker/check_r8.py local-output/argmax-bridge-20261105/bootstrap-r8/n32/n32-phase-compact.json --kernel round5 --output local-output/argmax-bridge-20261105/bootstrap-r8/n32/checker-report.json
```

Budget:1200 total process-group CPU seconds, enforced by the coordinator's
separate-run supervisor; no max-leaves truncation. Fresh unique checker
build via the pinned builder, no reused producer binary, immutable input
snapshot and full runtime/source provenance. The coordinator records exact
supervisor argv, child CPU, wall time, status, report and output identities.
The CLI itself does not impose an aggregate checker subprocess budget.
A failure/incomplete/cap freezes the first attempt with no retry.

Matched r6 n32 baseline:992leaves,620.093producerCPU-s,
382.569checkerCPU-s. Any future change in cover size/time is a known-degree
measurement, not a new global degree, complexity law, all-n energy bound,
effective onset, B3 completion or B4 authorization. No n64/n128 full job
is planned or authorized here.


## Focused n2 exact-type correction — 2026-11-06

The supplementary reviewer identified a MINOR private-validator mismatch:
Python dict equality permits bool/int aliases for n2 control fields, while
the source specification requires exact types. Fixed receipt SHA blocked
production false acceptance. The corrected checker now requires
`both_enclosed is True` and exact `int` types for both cardinal counts,
in addition to the existing complete expected-value dict comparison.
Three negative controls explicitly mutate `both_enclosed=1`,
`nonzero_cardinals=True`, and `zero_cardinals_omitted=True`.

The frozen-source list above now records the corrected checker and controls;
the producer is byte-unchanged. A fresh bounded controls-only execution used
the same actual argv above and a new `controls-mpfr-v2` build directory.
Exit0,58controls PASS,2.7383490779993735 seconds script wall,
1.049559661 own CPU and1.686661 total child CPU seconds. The corrected
control collector now measures aggregate child CPU. No full degree cover
executed; no calibration was retried.

Prior raw control report remains `bootstrap-r8/controls.json`; its prior
small receipt is preserved as `bootstrap-r8/controls-receipt-v1.json`.
New full report is `bootstrap-r8/controls-v2.json`. The committed small
receipt `evidence/bootstrap-r8-controls.json` now has v2 format and pins
both reports and the old small receipt. The old preregistration inventory
is preserved as `bootstrap-r8/preregistered-inputs-v1.json`; the active
inventory pins corrected source bytes. These paths are under the same
`local-output/argmax-bridge-20261105/` prefix used above.

Focused supplementary re-review and coordinator explicit start remain
required before the single planned n32 calibration. No full run launched.

## Released single producer calibration — 2026-11-06

After separate source/mathematical review accepted the frozen source and
focused exact-type response, the coordinator committed and pushed
`c8bdb63de00984701515a2d9c193dea32766a6c0` and explicitly released exactly
one preregistered n32 producer. The exact planned producer command above
executed once, beginning09:18:09Z and ending09:21:52Z. No source edit,
rerun, budget change or other degree occurred.

Observed exit0, watchdog_stopped=false, complete=true, pending0,
accepted=false; source/build/premise closure unchanged after execution.
724visited boxes,360splits,364leaves:32outside,280far,
28corner-orbit-plus-defect and24maximum-exclusion-plus-defect.
Search CPU222.0772617s; worker own CPU222.31348531s;
worker compiler/helper child CPU0.443148s; parent-measured total worker
subprocess CPU222.81307s and wall223.05083705799916s. All fixed budgets
were respected. The separate checker has not yet supplied acceptance.

Raw candidate:48481bytes, SHA256
`1cebb32c9678cb858010c4b048cca62ee12653373f24775bd7ed12a01bf07398`.
Exact compact candidate:21338bytes, SHA256
`97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e`.
Its gzip:3367bytes, SHA256
`a01bc14b968676161afa0690e5ed41005da8cb3f87fb8c6393594bc37ed3986a`.
The gzip was explicitly decompressed and compared byte-for-byte with the
compact candidate; it preserves the reviewed explicit format/mode/kinds.
Both local candidate files are read-only. An identical essential gzip is
`evidence/n3-phase-n32-bootstrap-r8.json.gz`; full raw outputs remain in
the preregistered local n32 directory.

Small producer receipt `evidence/bootstrap-r8-producer.json` records actual
launch and worker argv, source commit and inventory, all statuses/counts,
CPU/wall accounting, source/header/compiler/runtime identities, both fixed
premises and candidate/build/output identities. The full compiler/system
header dependency list is pinned through the local immutable build manifest
and a canonical dependency-list hash. No source arithmetic was changed.

Relative to the matched known n32 r6 baseline, producer visits decrease
1980→724 and leaves992→364; this is only a measurement for the new
maximum-cover mode at this known degree. It does not establish independent
acceptance, a new certified degree, an all-n cost law or any B4 release.
The coordinator assigns the separate whole-leaf checker next.
