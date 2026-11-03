# Supplementary independent finite-certificate check 01

Rules/input: `8a1f394739293953e1566fd24a0a193cc78ff26f`.
Checker: Codex, gpt-6-astra high, assigned by handoff 02. This is a
supplementary independent check, **not the required Claude audit**.
Date: 2026-11-03. Status: **IN PROGRESS**.

## Scope and independence

Read AGENTS, WORKFLOW, CODEX, the complete effective BRIEF and handoff 02,
the Claude pilot record, PD-T210's proof and general-constructor appendix,
and the reference producer, arithmetic, checker and controls. No new
mechanism or novelty claim is being assessed; the full ideas-campaign
novelty audit is outside this execution/reduction check.

The assigned first step regenerates every reference certificate at
n=17,...,24, then runs its reference checker in a fresh subprocess.
Neither the developer's native outputs nor Claude's pilot outputs are
used as the source for these independent certificates. This separately
replays Claude's n=17,20,24 cases; no costly reference n=32 run is launched.
The reference producer/checker share arithmetic, as PD-T210 discloses.

The second step independently compiles and executes the separate C++/GMP
checker against these new certificates and the C/GMP producer's outputs,
and repeats deliberate-corruption controls. The producer and checker
source directories remain owned by their developers. No Git operation
is performed by this worker.

## Reduction review

PD-T210's reduction checks out at this scope: nonnegative tensor Bernstein
weights sum to one; every nonvertex coefficient is strictly below the
common corner value on a corner leaf; the exceptional vertex coefficient
equals the actual cardinal value, irrespective of interval width.
Thus its tensor weight can equal one only at that vertex. A complete
closed-square prefix cover includes split boundaries. The all-n appendix
supplies the PD-T101 cardinal formula, rigorous Machin/Taylor cosine
enclosures and parity-valid reflection equality of the two nonnode
corners. Fixed-point multiplication and subdivision round lower bounds
down and upper bounds up, including negative values.

This is inspection of the stated reduction and code, not an independent
new proof of all earlier PD-T101 dependencies. Success at finitely many
degrees supplies no effective all-n threshold.

## Executed reference work

The bounded runner is `code/independent/reference_g0.py` (1800 seconds
total wall-clock budget). Executed from the repository root:

```text
python topics/padua-argmax-effective-20261103/code/independent/reference_g0.py /workspace/padua-work/independent
```

It records full per-degree commands, runtimes, leaf/depth counts and
certificate/checker SHA-256 values in
`/workspace/padua-work/independent/reference-g0-receipt.json` and pins
reference source bytes in `reference-g0-status.json` on exit.
These working files are not cold-storage locators.

Completed so far: n=17, 106 leaves (104 bound, 2 corner), depth 8,
producer 24.783 s and reference checker 39.459 s, accepted. The leaf/depth
counts agree with Claude's pilot. Wall timings are measured under shared
container load, not isolated single-core benchmark observations.

## Native replay and remaining work

Initial independent native candidate:

- `code/native_checker/check.py`: `b6c7320db2f7cfebf27fe33aa38ffdd45ff719870e3d23e15f845b6e8026eb2e`.
- `code/native_checker/kernel.cpp`: `94c520b0c96332ef60ab72e0d67c1e43a5bd5e9ae8382f8b7914b99b0147e189`.
- `code/native_checker/controls.py`: `65f0b68079f8330dd5b350eb979bafdb185ef29a26b1d006c4cc3d9e9ba2b5d4`.

Built independently with `g++ -O3 -std=c++17 .../kernel.cpp -lgmpxx -lgmp`
as `/workspace/padua-work/independent/checker-kernel`. Initial n=17 replay
accepted and all 36 negative controls were rejected, with complete and
partial positives handled correctly. This initial candidate was then
superseded by the outward-division optimization below. The native checker
imports no producer/reference arithmetic module.

Final checker arithmetic source:
`ae4f20b69c5e676a5d2fefa55c903c8b3efd87a5807a5c5617ca21390a1cab3d`;
driver and controls hashes above are unchanged. Independently rebuilt as
`checker-kernel-final`, binary
`6ba308759192b977453cfd7373a629106998b66d2cd86babb6d7dd5bab1f15e9`.
Inspected the replacement of rational half-averages and scaled-product
quotients by direct GMP floor/ceiling division by powers of two. The
outward rounding rule is unchanged. **All 36 negative controls were
independently rejected again on reference n=17**, complete positive
accepted, partial positive verified but not accepted; 23.478 s under
shared load. Receipt: `reference-n17-native-final-controls.json`.

The independently compiled final checker replayed final native
producer degrees 9–24 via `code/independent/native_replay.py`, which pins
source and executable hashes and checks they remain unchanged across each
replay. Each accepted input receives a separate hash-bound receipt.
**Completed: all sixteen final producer certificates n=9,...,24 accepted.**
The batch receipt is `native-final-batch-1793704872036025774.json`.
Also independently accepted canonical final n=32: 282 leaves (280 bound,
2 corner), depth 11, 232.767 s; input SHA-256
`e17a8712fb257a219436e44e977eaa6a1e0287ba6a64a86c78e34009f984c609`,
receipt SHA-256
`a95d3834e8f02f8fe59d17fdfc0c910a7552ebca7ef0e27940cffdda537dfe80`.
No reference-Python n=32 execution is claimed.
The reference checker's original fourteen negative controls were also
independently repeated on the fresh final-native n=9 certificate: all
rejected, complete positive accepted and partial positive not accepted,
5.340 s; receipt `native-final-n9-reference-controls.json`.

Independently ran final producer sources at n=9 and n=24:
`producer.c` hash `ae3002a995c199660ad8c31dd2c7577a8416208ab8b3868c0795ebe728ab72ff`,
`run.py` hash `718cf9fc39653766c86fe862398a4670d4426215a994f2cb9063d482554fa934`.
Both complete covers reproduce every mathematical field of the developer's
final outputs: 42 and 154 leaves, respectively. Compared leaves, pending
paths, threshold, corners, pi brackets, Machin terms, cosine seeds and all
search statistics. Timing/provenance fields naturally differ. n=24 uses
2.638 s setup CPU, 11.422 s search CPU, 36.252 s total wall time.

Pending: finish reference G0 at n=24 and its n=17 controls; deliver the compact
hash-bound receipt to the orchestrator for durable retention and
degree-specific claim records. All reference/native mathematical fields
match exactly through the already completed reference n=23. Canonical
final-native n=9–24 acceptance and both corruption suites are complete.
No unexecuted receipt is counted, and local scratch paths alone are not
treated as durable evidence locators.

## Mathematical check scope

The exact degree-four obstruction, all-degree corner spectrum and normalized
slopes/local radius, and R5 equivalence were independently reconstructed.
See [independent-math-checks-01.md](independent-math-checks-01.md) for proof
checks, final source identities and limitations. These supplement Claude audit.

## Intermediate provenance finding

The initial native producer driver hashed its source only after a run
finished, although compilation occurred before the run. Concurrent source
edits could therefore misidentify the compiled source. Reported to the
producer worker; the response snapshots source bytes before compilation
and records early source/driver/binary hashes. **Resolved:** inspected
the final driver and independently reran its n=9 and n=24 outputs with
the final source hashes above. Earlier independently checked
mathematical payloads remain usable as arithmetic observations, but their
producer-source attribution must not be upgraded from a possibly raced
receipt. No developer source was silently repaired by this checker.

