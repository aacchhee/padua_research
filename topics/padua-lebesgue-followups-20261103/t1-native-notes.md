# T1 exact native endpoint-loop hedge

Status: **MEASURED implementation controls; not live installed; supplementary independent review accepted for optional future runs.** This is a bounded technical acceleration of frozen A5, not a new mathematical mechanism or acceptance predicate. T1's existing gate applies. Rules read at `b604f0d19471f4b323d3eb89204eeb9b4ef6bcf1`. Developer: Codex child `/root/t1_native_loop`; configured gpt-6.1-sol medium as recorded by the parent spawn, with serving metadata not separately exposed. No Git mutation or existing scientific source edit was performed.

## Implementation and exact correspondence

`t1_native.py` retains the same frozen `power` and `mul` functions, the same nine-by-nine monomial table, and the same bounded512-entry cache as `t1_memo.py`. Its default factory explicitly requires scale `2**160`; historical controls explicitly supply their original96/112/128-bit scales. Changed scales and noninteger endpoints raise explicitly. No Python `assert` controls the factory's scale or endpoint validation.

`t1_native.c` receives that already-computed table and actual coefficient term vectors. Every endpoint remains an exact arbitrary-precision CPython integer. For each term, it performs `c0*m0`, `c0*m1`, `c1*m0`, `c1*m1` in that order, selects their integer minimum/maximum, computes `min//unit` and `-((-max)//unit)`, and adds the two results to the corresponding running integer sum in original term order. Only public CPython arithmetic is used; there is no fixed-width endpoint arithmetic, floating approximation, division reassociation or rounding change. C-width indices are range-checked; overflow refuses. Accepted inputs are exact tuple/list containers and exact integer entries. Every owned temporary reference has a success/failure release path. The GIL remains held.

`t1_native_produce.py` is a separate, currently unused execution wrapper with the same fresh/continuation/left module selection and solve arguments as `t1_produce.py`. Only `field.evaluate`, selected producer `evaluate`, and node-driver `evaluate` are replaced. It preserves frozen source hashes and write behavior, and attaches actual native source/binary/build-receipt hashes plus compiler/runtime identity to execution metadata. At write time, frozen/native source hashes, binary/receipt hashes and evaluator identities must remain unchanged. It explicitly refuses optimized Python before imports, as do every new Python entrypoint. Existing active sources and processes are untouched.

## Executed controls

- `evidence/t1-native-controls.json`: **41172** bit-identical frozen n4–7 endpoint comparisons, matching the original memo controls' endpoint payload digests. These include sampled actual certificate leaves, all actual interior root boxes, cardinal derivatives through order2, and actual signed-root polynomial derivative vectors. Original certificate hashes are recorded. Native evaluation versus memo was1.48x/1.97x/1.38x/1.10x faster at n4/5/6/7 in these short timed loops. These are local evaluation timings, not whole-certifier speed estimates.
- `evidence/t1-native-edge-controls.json`: **3120** deterministic n4–8 synthetic endpoint identities, including the live160-bit n8 scale; empty terms, zero/negative/large coefficients, point/sign-crossing/full/outside-square boxes and remainder signs. Eight malformed native inputs were refused. Scale mutation was refused at each tested degree.
- `evidence/t1-native-wrapper-controls.json`: publication-only fake-solve controls passed ordinary metadata publication plus native-source and runtime-evaluator mutation refusal. No scientific solve ran in these controls.
- `evidence/t1-native-source-freeze.json`: source hashes, both actually used binary hashes, control hashes and14 pre-import `-O`/`-OO` refusals. The extension was first built manually for historical controls, then rebuilt using the recorded build script for edge/wrapper controls. Both binary hashes are preserved.
- `evidence/t1-native-build.json`: actual reproducible build command, source/binary hashes, compiler executable/version/hash, Python executable/version and SOABI. Compiled binaries stay in scratch.

An initial historical-control launch correctly refused n4's96-bit scale because the factory default pins160; the controls were then changed to pass the explicitly expected historical scale. An initial synthetic edge control incorrectly requested degree8 monomials from n4's frozen evaluator, which only precomputes to degree4; that test construction was corrected to use each degree's allowed exponents. Neither failed launch produced acceptance evidence. Both final control receipts report completed passing runs.

## Reproduction and proposed use

From `/workspace/padua_research`:

```sh
python -B topics/padua-lebesgue-followups-20261103/code/t1_native_build.py --output-dir /workspace/scratch/lebesgue-t1-native/reprobuild
PYTHONPATH=/workspace/scratch/lebesgue-t1-native/reprobuild:/workspace/scratch/lebesgue-t1/deps python -B topics/padua-lebesgue-followups-20261103/code/t1_native_controls.py --frozen-output-dir /workspace/scratch/lebesgue-frozen-reference/topics/padua-proof-attempts-2-20261101/outputs --output /workspace/scratch/lebesgue-t1-native/replayed-controls.json
PYTHONPATH=/workspace/scratch/lebesgue-t1-native/reprobuild:/workspace/scratch/lebesgue-t1/deps python -B topics/padua-lebesgue-followups-20261103/code/t1_native_edge_controls.py --output /workspace/scratch/lebesgue-t1-native/replayed-edge-controls.json
PYTHONPATH=/workspace/scratch/lebesgue-t1-native/reprobuild:/workspace/scratch/lebesgue-t1/deps python -B topics/padua-lebesgue-followups-20261103/code/t1_native_wrapper_controls.py --native-build-receipt /workspace/scratch/lebesgue-t1-native/reprobuild/build-receipt.json --output /workspace/scratch/lebesgue-t1-native/replayed-wrapper-controls.json
```

After independent review, the parent's selected fresh/continuation invocation can use `t1_native_produce.py` with the same scientific arguments plus `--native-build-receipt /workspace/scratch/lebesgue-t1-native/reprobuild/build-receipt.json` and the above `PYTHONPATH`. No live invocation was performed here. Full certificate replay and distinct-agent replay remain necessary; endpoint equivalence controls alone establish no maxima count. A subsequent explicitly authorized checker hedge is recorded below.


## Additional bounded checker hedge

Parent explicitly authorized a further10-minute checker adapter after the producer hedge. `t1_native_check_backend.py` calls the unchanged frozen `cached.monomials` and caches only a tuple view of its integer endpoints (512entries). Every coefficient vector is converted afresh on every evaluation; no coefficient identity cache, mutable-vector trust, field operation, acceptance test or `Verifier.run` body is introduced. The reviewed C primitive handles the same endpoint sum. `t1_native_check.py` calls the complete original `check.main()` with this evaluator installed, then restores evaluator/arguments. It preserves the native build/source/binary and frozen source guards, input before/after hashes, explicit backend metadata and atomic receipt publication. All new Python entries explicitly refuse optimized execution before imports.

Actually completed developer controls:

- `evidence/t1-native-check-controls.json`:3594 exact original/cached/native endpoint identities,333 actual n8 polynomial vectors,10 common boxes,44 actual root boxes, repeated identical terms and wrong precision/cache-bound controls.100 actual universal leaves were replayed under each evaluator after warm-up. Native adapter time1.9415s versus frozen cached time2.3082s, measured1.189x speedup in this local sample.
- `evidence/t1-native-check-wrapper-controls.json`: six publication-only mock cases passed: ordinary metadata publication; source, evaluator, input and receipt-binding mutation refusal; exception cleanup. Existing output remained intact on failure, unpublished files were cleaned, and evaluator/arguments were restored. The mock cases do not run a mathematical checker.
- `evidence/t1-native-check-source-freeze.json`: four new checker source hashes, control hashes and eight further pre-import optimization refusals. Core producer/native primitive sources remained frozen.

An initial completed checker-controls calculation failed only while serializing because a derivative-loop variable shadowed parsed arguments. Its unrecorded numerical results were discarded; the corrected control script was rerun to completion and its actual final receipt is the cited evidence.

Reproduction uses the previously built extension and dependency prefix:

```sh
PYTHONPATH=/workspace/scratch/lebesgue-t1-native/reprobuild:/workspace/scratch/lebesgue-t1/deps python -B topics/padua-lebesgue-followups-20261103/code/t1_native_check_controls.py --interior /workspace/scratch/lebesgue-frozen-reference/topics/padua-proof-attempts-2-20261101/outputs/a5_n8_interior_candidate.json.gz --output /workspace/scratch/lebesgue-t1-native/replayed-check-controls.json
PYTHONPATH=/workspace/scratch/lebesgue-t1-native/reprobuild:/workspace/scratch/lebesgue-t1/deps python -B topics/padua-lebesgue-followups-20261103/code/t1_native_check_wrapper_controls.py --native-build-receipt /workspace/scratch/lebesgue-t1-native/reprobuild/build-receipt.json --output /workspace/scratch/lebesgue-t1-native/replayed-check-wrapper-controls.json
```

Proposed full replay, only after separate independent adapter/wrapper review and controls: use `t1_native_check.py INPUT --output RECEIPT --native-build-receipt BUILD_RECEIPT` with the same dependency prefix and optional original `--allow-partial` flag. No such live/full replay ran in this subtask. Different-agent reviewer `/root/t1_independent` has the frozen hashes/commands; its independent record controls whether use is allowed. The modest local timing gain is a measured hedge, not a guaranteed whole-replay acceleration. Counts remain OPEN without complete accepted replays.

## Orchestrator review disposition

Distinct gpt-6-astra high reviewed and independently rebuilt/reran the producer
and checker controls; see independent-checks-t1.md for exact scope, hashes,
malformed-input/ownership checks and added compiler/C-glue trust. Optional use
in a new continuation or replay is accepted. Current frozen executions are not
restarted for the modest measured speed gain. No maxima-count certification
follows from these implementation controls.
