# Native exact producer attempt

- Rules/input head: `8a1f394739293953e1566fd24a0a193cc78ff26f`.
- Base/main supplied by orchestrator: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`.
- Role: bounded technical developer; tool-configured model `gpt-6.1-sol`, medium, fresh fork (`fork_turns=none`). No Git mutations; ownership limited to this
  attempt and `code/native_producer/`.
- Status: MEASURED implementation/verification record; no new theorem or novelty
  claim. Gate exemption: port of the existing PD-T210 algorithm with unchanged
  mathematical criterion, source schema, and operation order.
- Dependencies read: root rules/workflow/Codex role, handoff02, BRIEF, and frozen
  `finite_general.py`, `finite_bernstein.py`, producer/checker/controls modules.

## Scope and implementation

C/GMP performs the corrected PD-T101 cardinal monomial construction, both
rational tensor Bernstein transforms, all de Casteljau subdivision, sums of
absolute interval endpoints, and corner/bound comparisons. Python supplies only
exact rational cosine seeds, small exact transform/monomial constants, and JSON.
This is a compiled heavy path rather than a Python arithmetic wrapper.

GCC14.2.0, GMP6.3.0, Python3.12.14 were available locally; no installs/network or
proxy changes. Native single thread, scale2^192, inherited n<=100.
Build/commands and limits are in `code/native_producer/README.md`.

The initial allocation-per-child version was replaced by in-place left halves
and one reusable right coefficient table per active depth. Each line is fully
copied before writing; only storage lifetime changes, not arithmetic order.
The first driver hashed sources after execution; concurrent editing could give
misleading provenance. Final driver instead compiles a frozen source copy and
records its early hash. Earlier artifacts are retained as interim evidence and
must not supply final provenance; final regenerated certificates live in
`/workspace/padua-work/producer/final/` and their entire mathematical payload is
compared against the earlier replayed output.

## Executed controls and evidence

`validate.py --work /workspace/padua-work/producer/optimized-validation` passed
n=2 and9: every initial coefficient interval equals the reference constructor
(54 and5500 intervals respectively), every metadata field agrees, unchanged
Python checker accepts, all14 deliberate corruption cases reject, and a valid
partial certificate remains unaccepted. Receipt is `validation.json` in that
work directory. This is developer validation, not independent audit. Direct native `--boxes 1`
and `--depth 1` runs at9 also replayed as valid partial partitions with
`accepted=false` (receipts `optimized-validation/partial-*-check.json`).

Reference Python replay accepted every produced degree n=9..24; individual receipts
are `/workspace/padua-work/producer/nN-reference-check.json`. Final-source reruns
and exact mathematical-payload equality receipts are in
`/workspace/padua-work/producer/final/producer-timings.jsonl`. No pure-Python
producer is run here above32. Larger native runs remain bounded by this round's
budget and independent replay is required before any finite theorem upgrade.

## Runs needed

Remaining publication work: independent n40 replay and cold-storage archival.
Reference overlap9..24, independent G0reference17..24, independent final9..32
acceptance and compact receipt freeze are complete.
Producer computation is finished; no48 or larger run is planned this round. All large
or regenerable artifacts remain under `/workspace/padua-work/producer/` outside
Git; orchestrator owns cold-storage manifest/publication and independent status.

## Frozen compiled candidate

- `producer.c`: `ae3002a995c199660ad8c31dd2c7577a8416208ab8b3868c0795ebe728ab72ff`.
- `run.py`: `718cf9fc39653766c86fe862398a4670d4426215a994f2cb9063d482554fa934`.
- Final outputs pin these hashes and the executable/input identities. Every
  mathematical field for9..24 equals the reference-accepted earlier output;
  only setup/search/total times and explicit producer provenance differ.
- Independent checker has its own arithmetic kernel. Its receipts are
  `/workspace/padua-work/checker/nN-final-producer.json`; claims must match each
  receipt to the final certificate raw hash. Orchestrator owns final status.

## G1 measured cost, clocks and projection limits

Final native n=17..32 completed. On exactly the same complete partitions,
reference constructor/search CPU/wall time was measured using `time.process_time()` and
`time.monotonic()` around `finite_general_run.run(n,600,200000,48)` at17 and24.
The executed inline measurement loop is preserved as the equivalent
`code/native_producer/time_reference.py`; reproducible command:

```sh
python topics/padua-argmax-effective-20261103/code/native_producer/time_reference.py --work /workspace/padua-work/producer/python-cpu
```

| n | Python constructor/search CPU s | native hot-path CPU s | hot-path/reference ratio |
|---|---:|---:|---:|
|17|25.396661|2.027244|12.5277|
|24|161.677115|14.030283|11.5234|
|32|not remeasured|83.699980|not claimed|

The native driver wall times include cold compilation and Python input/metadata
work; setup/search fields are native process CPU. Python producer wall times
from the independent sweep are a separate, contention-sensitive series. The table above compares the same CPU clock but different run boundaries:
Python includes seed/metadata work while native hot-path fields omit it. It is
a hot-path comparison, not the primary full-driver speedup. No
Python-wall/native-CPU ratio is called a speedup. All runs are single-threaded,
sharing a four-core quota with other campaign workers; wall-fit parameters can
therefore change with scheduling.

Log-log least squares on final native17..24 CPU gives exponent5.618711;
including17..32 gives5.828518. The Python CPU two-point fit17,24 gives5.367651;
two points supply no residual goodness-of-fit test. On the17..32 native fit,
cumulative cost from17 throughN projects N=70 in24h and94 in7days; the Python
two-point fit projects51 and70. The same native17..24-only fit instead gives73
and98, exposing fit sensitivity. These are unconstrained cost extrapolations,
not validated n_cert: fixed192-bit widths, n<=100 cap, memory growth and checker
cost are excluded. Single-degree projections are separately labeled in the
receipt; they must not be mistaken for a contiguous finite bridge.

Current producer result: complete covers exist for9..32 and40;
33..39 remain unrun. The n=40 capacity probe completed352leaves
(350bound,2corner), depth12, CPU35.141881setup+251.237701search,
wall300.524294s. Its independent replay is pending at this worker checkpoint.
No degree outside actual, independently accepted certificates is certified. No n>=48 run is planned
this round. Failure to complete within a budget would be an implementation/
capacity limitation, not a counterexample to PD-T099.

The final **full-driver** comparison separately executes `time_native.py --work
/workspace/padua-work/producer/native-full-cpu`. CPU is parent process CPU plus
`resource.getrusage(RUSAGE_CHILDREN)` user+system deltas, including cold GCC,
Python constants/metadata, native child, and certificate compression/write.
The reference CPU measurement covers constructor+search and omits final
compression/write; charging that extra work only to the native driver makes the
reported improvement conservative with respect to those output costs.

| n | full native CPU s | reference CPU / full native CPU |
|---|---:|---:|
|17|2.128400|11.9323|
|24|13.937444|11.6002|

This full-driver two-point fit has exponent5.449501 and unconstrained cumulative
24h/7days projections75/102. These are the primary full-driver cost comparisons;
the larger17..32 series remains a hot-path fit. The102 projection exceeds the
inherited n<=100 implementation cap. The stronger limitations above continue to
apply, and differing machine scheduling/frequency across reruns explains small
timing differences even at the same n. All repeated certificates have identical
mathematical payloads; the receipt builder checks that identity before reporting
these ratios. No extra reference/native mathematical replay was substituted for
independent acceptance.

The independent checker's measured full child CPU is5.473492s at17 and35.283062s
at24, from `/workspace/padua-work/checker/cpu-bench.json` (separate executable,
no producer arithmetic import). Adding it to the full native driver gives
7.601892s and49.220506s. The two-point **producer+checker pipeline** exponent is
5.416746; its unconstrained cumulative24h/7days projections are62/84. This is a
provisional certification-budget projection. The Python51/70 projections above
are producer-only because matching Python checker CPU was not measured; these
must not be presented as comparable complete certification pipelines. All
projections remain conditional on memory, precision, cap, future partition
complexity and storage assumptions. No additional benchmark runs are planned.

An obsolete duplicate n=28 run was interrupted before completion once final
frozen-source regeneration was selected. It contributes neither a certificate
nor a failed mathematical claim; the final n=28 run completed independently.

The full-pipeline fit is only an input to gateG5. This worker supplies no explicit
n0 and makes no all-degree comparison between n0 and projected certification
capacity. PD-T099 and all bridge degrees without accepted certificates remain
OPEN; there is no new all-n proof or counterexample here.

## Final worker checkpoint

- Complete native covers: every degree9..32, plus isolated40. Gap33..39 is unrun.
- Unmodified reference Python checker accepted all16overlap degrees9..24.
- Different agent independently ran reference producer+checker for17..24; all
  complete payloads equal canonical native after excluding only timings and
  native provenance. Independent compiled checker accepted every final9..32
  certificate. These are executed validation facts; final theorem/audit/archival
  status belongs to the orchestrator.
- n40 producer complete352leaves; independent n40 replay pending at this freeze.
- Compact receipt: `evidence/native-producer-summary.json`,15747bytes, SHA256
  `a69e3f855d0aab6d56533f12ab1b9e8ddf4af6dc8e38235a9b84f71793ea564c`.
  It pins raw certificate and deterministic mathematical-payload hashes, exact
  acceptance snapshots, source identities, timing clocks and fits.
- Final native hot-path fit17..32plus40 exponent5.826416; unconstrained producer
  budget projections70/94 remain unchanged. The full pipeline two-point62/84
  projection is the certification-budget estimate, with all stated limitations.
- No n>=48 computation, no pure-Python computation above32, no external
  machines, no installs, no proxy changes, and no Git mutations by this worker.
- Bulk outputs remain under `/workspace/padua-work/producer/`; cold-storage
  handoff/manifest is pending with the orchestrator.


## Dated integration finding: checker rational contract

After this worker's initial freeze, the checker author identified noncanonical
GMP rational summands in the independent C++ transform weights. The old native
acceptance snapshot above is historical and does not by itself support the
final25+ proof. Corrected checker replays and summaries supersede it. Root
removed duplicated native acceptance fields from the producer summary;
producer performance and reference-Python validation remain valid.

The producer has no analogous issue: every imported W is canonicalized before
arithmetic; combine temporaries start canonical or use mpq_set_z. A targeted
n2 run multiplied every rational input numerator and denominator by7 and
reproduced every scientific output field. Frozen producer sources and all
canonical certificate bytes are unchanged. Corrected checker CPU benchmarks
supersede the historical pipeline timings above for future capacity estimates.


Corrected checker CPU benchmarks (kernelb0c871e7…, independently executed
within the corrected overlap replay) are5.010504s at17 and34.778060s at24.
Adding the unchanged full producer CPU gives7.138904s and48.715504s.
The updated two-point pipeline fit has exponent5.569062 and cumulative
projections N=61 for24h and82 for7days. This replaces the earlier62/84
pipeline projection; the sensitivity illustrates why these are only
heuristic cost estimates. Producer-only timing series and speedups do
not change. The final native-producer-summary.json is regenerated from
cpu-bench-corrected.json and intentionally omits native acceptance flags;
corrected checker evidence governs those claims.


Final integration outcome: corrected independent acceptance covers9–32.
The corrected n40 checker reached the authorized600CPU-second cap
(SIGXCPU;605.562s wall) without an acceptance receipt. Therefore n40
remains a producer-only capacity checkpoint, not a certified degree or
counterexample;33–39 remain unrun. No further production/replay is launched.
