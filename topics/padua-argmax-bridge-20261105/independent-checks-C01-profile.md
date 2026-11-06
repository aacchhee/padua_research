# C01 profiling: supplementary independent check

Rules read at `4b728b04216a5490910780bc609a82b853058426`; current main supplied by the coordinator is `f654e32daff27b6846849311092f6daebbbf235b`.
Reviewer: distinct Codex supplementary reviewer, allocated gpt-6-astra high; serving model/effort metadata unexposed. Date: 2026-11-06.
Verdict: ACCEPTED within the diagnostic scope below. This supplements, and does not replace, the pending formal Claude audit.

## Scope and identities

Reviewed the exact operation counts, instrumentation-only source changes, frozen five-box receipt, build/input closure, actual timing/caps and one fresh uninstrumented n32 saved-box comparison. No new proof of the old kernel or certificate acceptance, historical novelty verdict, analytic replacement, future feasibility note, whole cover or degree extension is included. The full IDEAS read is omitted because this review adds no novelty or mechanism claim.

- Instrumentation `code/cheap_C01/profile.py`: SHA256 `c839838a51766f322ed6d1f2df155307c42e6d24980015f9aaea57311862762a`, 5102 bytes.
- Frozen small receipt `evidence/c01-fast-profile.json`: `146abbe78426ab81bdd5f73a4e46e1677da732fc1210dd87084609edf144688b`, 8591 bytes.
- Original v3 kernel: `f52d1a9da3c86212663f7ac22e9475b76811d7be4bbc4916779fd32a59d95bf0`; generated instrumented source: `6765b5e4d41b84f575bd5b37cc9780bde6a7544d579ff18556e941b3a25b80f4`.
- Attempt record `attempts/C01-fast-code.md` as read: `e96e49ae2ef68705606535f80394dd39d60dae4a2e16bcf2a1882db1024d7cc2`. Later appended feasibility discussion is outside this review.
- Full author receipt: local `cheap-C01/profile.json`, `3cb5ae233c12a306478284764af33c9a14abc71468d4e82572c42a0b703edfcb`, 58016 bytes.

## Independent source reconstruction

One parity board contains T=2n(n+1) primitives. `all_bounds` constructs exactly three boards. Every primitive calls `ratios` twice, and each ratio call runs j=1,...,n with exactly one `arb_sin_cos`. The harmonic call count is therefore 3T·2n=12n²(n+1), not quadratic. There is also one correction trig call and four refinement calls per primitive. Every refinement performs one trig call before its denominator guard, and at most one after it. Thus the total trig-call count lies between 3T(2n+5) and 3T(2n+9), exactly as now stated in the attempt record. These count calls to the Arb API, not the internal work of each transcendental routine.

Each collect pass visits every parity board entry for K=0,...,n+1 and for J=0,...,n, giving T(2n+3) pair visits. There are two passes, so the exact count is 4n(n+1)(2n+3). The final admissible-center minimization is quadratic. Thus both finite harmonics and projected profile accumulation retain cubic source work; replacing only the harmonics cannot establish subcubic evaluation of this backend.

The review code independently removes the six precisely identified instrumentation insertions and demands byte-for-byte equality with the original source. This passes. Added state is confined to counters, process clocks and RAII timers; arithmetic expressions, loops, order, return values and branches are preserved. The counters agree with all five saved cases, including the data-dependent quotient-attempt counts. Harmonic/refinement timers are nested inside board timers, so their columns must not be added to board time.

## Executed controls and bounded measurement

Command actually run:

```sh
python topics/padua-argmax-bridge-20261105/code/cheap_c01_review/profile_review.py
```

Observed shell exit: 0. Code SHA256 `b395cb60b1a9b537c69e90566ed15aab8b99013ab35c5b9357e70a91730e62c7`.

All 257 entries in the saved toolchain, toolchain-runtime, headers, dependency-input, linked and loaded closure groups rehash correctly. Saved input files, original/instrumented source, source snapshot, preprocessed translation unit and binary identities also match. The raw receipt agrees with the small receipt's results. This is a present identity check plus inspection of the author's before/after checks, not a retrospective reconstruction of arbitrary past machine state.

The independent fresh build uses the original uninstrumented v3 kernel and its pinned snapshot builder. It executes exactly one saved n32 box, reconstructed from candidate `97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e`. All seven binary64 results equal the saved instrumented results exactly. Kernel CPU 0.435974357 s; own CPU 0.926919 s plus build/helper CPU 1.385574 s = 2.312493 s; wall 2.312160828 s. Fresh source/TU/binary and build/runtime closure rechecks pass. No author's instrumented binary is executed by this check, and n17/24/64/128 are not rerun.

The independent evidence is `evidence/c01-review-profile.json`; its local full build manifest is SHA256 `411606c5d6865f7db5238345eba4a17bfd8a463ca1b69053ff243fb4f79c34cf`, 48612 bytes. Compiler: x86_64-linux-gnu-g++-14, Debian 14.2.0-19. The review stays well within its 60 CPU-s one-case cap and 120 CPU-s overall allocation. Local raw artifacts remain regenerable; physical archive transfer is not asserted.

## Findings and limits

No BLOCKING, MAJOR or MINOR finding in the frozen measurement scope.

NOTE: the author's `(150,155)` RLIMIT_CPU is per process, and the 120-second pre-box stop uses parent process CPU, excluding compiler/helper children. It is not a general aggregate 180 CPU-s watchdog. The actual completed run uses 28.70712586 own + 1.400104 child = 30.10722986 CPU-s, so it obeys the authorized total budget. A future workload must not infer an aggregate resource guarantee from this wrapper.

NOTE: the recorded n128 harmonic/collect shares are consistent with the saved timers, but include instrumentation overhead. The one uninstrumented n32 measurement checks unchanged outputs; neither it nor the five heterogeneous boxes provides a general overhead estimate, certified throughput, or asymptotic timing law. The inspected source already proves the stated operation-count growth without fitting timings.

No subsequent ratio, all-class defect, effective-tail, or near-model proof is accepted by this report. Those require separately frozen identities and independent reconstruction.
