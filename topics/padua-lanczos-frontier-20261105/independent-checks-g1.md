# G1 independent native exact port

Verification record, not a new mathematical or asymptotic claim. Codex technical checker, gpt-6.1-sol medium requested; model/effort metadata are not independently exposed by this runtime. Rules/input head: `0e493be7f9883e00e6260cf6b081c607a230177f` (unchanged rules verified against current head `79c3d6a211325eca6e8311b3ae03187c100a1d8a`). Main supplied: `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`. No novelty-bearing mechanism was generated; this implements the frozen G1 preregistration and PD-T136/137 finite formulas, so the novelty generation gate does not apply to this checker task.

## Implementation independence and finite reduction

`code/g1_independent.cpp` is a separate C++17 implementation using GMP `mpq_class`, compiled with g++14.2.0 against the environment's existing GMP6.3.0 (Debian package2:6.3.0+dfsg-3). No dependency installation or system mutation was needed. It imports, links, and executes no producer mathematical functions. The only shared inputs are the frozen node definitions, graded monomial conventions, four parent rules, and the written PD-T136/137 formulas. The Python harness imports no producer code; it orchestrates the native executable and parses exact rational strings using `fractions.Fraction`.

The port independently generates all 325 T24 or 625 rotQ24 nodes, constructs each monic column by exact full projection, checks positive input scales and positive residual norms, and checks every new column's inner product with every earlier column is zero. Its stored diagonal is the exact squared norm of that column. These exact Gram checks verify orthogonality; the later projector trace alone is merely a consistency identity. Parent comparisons use integer numerator/denominator cross products. Both eligible pivot candidates are evaluated and every exact tie recorded; the X candidate comes first and is retained on equality.

For every source h=1,...,N-1, it separately propagates the full frozen impulse recurrence through every later column and forms the cumulative squared response divided by the exact column norm. At each complete degree, it stores per-node sum_h v_hi and max_h v_hi, with v_hi as defined in PD-T137. Since the normal projector diagonal is independent of h, the same formulas become L²=max_i R_ii max_h v_hi, H²=sum_i R_ii sum_h v_hi, and Urow²=max_i sum_h v_hi. This reorders exact finite sums and maxima only; no source is omitted and no floating value enters any endpoint or ordering decision. U² is the exact minimum of H² and Urow².

A max-degree build yields all smaller complete-degree prefixes. Separate fresh degree-2, -3, and -4 builds check prefix agreement on both grids and every rule before higher-degree interpretation. The overlap harness compares each of the 88 degree-2–12 rows against old PD-T139 all-source evidence, including exact endpoints, dimensions, source counts, choices and projector trace. Fresh pivot ties must be absent on T24 and exactly [(2,1)] on rotQ24, resolved to X. The harness also checks source cardinalities, exact endpoint ordering, the exact upper minimum and Gram-check coverage. No fit, asymptotic interpretation, target disposition, or actual rounding claim is made by this checker.

## Regeneration

Old overlap input is recovered outside Git from the historical source commit `2b52b432fe59c9a50aef9deebe5152c5d6874465`, path `topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json`, Git blob `b252ae7c1837`. It is 616693 bytes with SHA-256 `0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344`. The harness asserts that hash before using any old row. This is comparison data, not native construction input.

```
python topics/padua-lanczos-frontier-20261105/code/g1_independent_run.py \
  --old /tmp/padua-lanczos-frontier-g1/inputs/e1-full-sweep.json \
  --out /tmp/padua-lanczos-frontier-g1-independent/overlap \
  --degree 12 --workers 4 --timeout 1800 \
  --receipt /tmp/padua-lanczos-frontier-g1-independent/overlap-receipt.json
```

The runner's compile command is `g++ -O3 -std=c++17 code/g1_independent.cpp -lgmpxx -lgmp -o <outside-Git executable>` from the topic directory. Raw exact JSONL rows, native progress logs, binary and full receipt remain under `/tmp/padua-lanczos-frontier-g1-independent`; the committed short evidence receipt records their paths, hashes, commands and measured timing. Temporary local retention is not an archive guarantee.

## Executed scope and limits

The native overlap execution completed: all 88 degree-2–12 rows matched the old PD-T139 all-source endpoints and frozen choices exactly. All 24 fresh degree-2/3/4 constructions passed, and all 24 comparisons with higher-build prefixes passed. Every exact Gram pairing was checked in every native build. T24 had no pivot tie; rotQ24 had exactly the (2,1) tie with X selected. The short receipt is `evidence/g1-independent-overlap.json`.

All 12 malformed controls were rejected: omitted source count, wrong point count, wrong basis dimension, negative endpoint, incorrect upper minimum, missing tie, Y tie break, wrong trace, missing Gram-check coverage, degree 21, invalid native rule and invalid native grid. The first nine deliberately corrupt receipt data and test the acceptance layer; the last three execute the native argument checks. They do not pretend that receipt-field corruption alone tests construction mathematics.

Triangle max-degree-12 native cases took 2.58–4.49 seconds each; rotated cases took 163.21–311.12 seconds each with four workers. Timings include exact native construction/propagation and output, plus harness comparison overhead. Separate fresh producer comparisons of all T24 degree2–20 rows (76 rows) were executed and passed, including the four exact endpoints, dimensions, source counts, frozen choices and ties. `evidence/g1-independent-triangle20-comparison.json` records these actual comparisons and both input hashes for every rule. Fresh producer overlap comparison subsequently passed all 88 degree2–12 rows on both grids and all four rules; `evidence/g1-independent-overlap-comparison.json` records the actual comparisons and both input hashes. Two initially partial producer files were treated as incomplete until they finished, and then successfully compared.

The bounded max-degree-20 run is finished. All four T24 cases completed through degree20 (76 rows total), taking 24.60–78.95 seconds per case. Their degree2–12 overlaps again match the old evidence; all dimensions, positive pivots, Gram checks, source counts, exact endpoint minima/orderings and recorded ties pass. Twelve additional explicit comparisons of independent fresh degree2/3/4 builds to max20 prefixes passed. T24 pivot has no exact tie through degree20. The fresh producer/native comparison passed all76 T24 rows.

All four rotated max20 cases reached their existing 1800-second per-case wall-time cap and were stopped by the runner, after full degree20 basis construction and only partial all-source propagation. No rotated degree13–20 endpoint was emitted or claimed. The exact final source counts are recorded in the final receipt. This is a computational cost limit, not a mathematical failure or target disposition. No new heavy round was started. `evidence/g1-independent-high20.json` records the final incomplete cost receipt, native code hash, command, exact output hashes and progress-log identities.

The completed independent scope is therefore both grids/all four rules at degrees2–12, plus T24/all four rules at degrees13–20. G1's full two-grid degree2–20 endpoint obligation remains incomplete. Numerical log conversion, finite fits, interval-wide operational criteria and any target status remain outside this checker assignment. Native GMP bit lengths/runtime can grow sharply on the rotated grid; no performance or mathematical asymptotic inference is made. The raw inventory for the orchestrator's cold-storage index is `/tmp/padua-lanczos-frontier-g1-independent/inventory.json`.
