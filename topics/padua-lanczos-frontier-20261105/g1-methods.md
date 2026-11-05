# G1 exact producer methods and execution record

Technical developer: Codex, requested gpt-6.1-sol medium. Rules/head read at
`0e493be7f9883e00e6260cf6b081c607a230177f`; current base main is
`21dbfc90257b952d8923f6d01739d12aa8d6e0a1`. Rules are unchanged from the
previous read. No Git mutation. This is implementation of the frozen
`attempts/L1.md` G1 preregistration after the completed repository gate in
`ideas-l1-l2.md`; no new mechanism or primary-source/priority claim is added.

## Scope and exact quantities

Frozen T24 and rational rotQ24, degrees2–20 inclusive, all four fixed rules
BJ/mirror/alternating/exact-pivot, X wins exact ties, and **every** source
column1,...,N_s-1. The sample counts are325/625; N_20=231, so both have
M>N_s throughout. The source metric and output are PD-T136/137's aggregate
Hilbert source norm and spectral normal-output condition, not the scalar
operation cube used for L4.

For each prefix stage, the producer computes exact rational node/source
energies, L², H², Urow² and U²=min(H²,Urow²). Its recurrence implementation
copies the frozen `e1_exact.py` construction with exact pivot tie recording;
the frozen file remains read-only and its SHA-256 is asserted. Every column
has positive exact pivot and source scale. The projector diagonal is computed
from the exact basis. Its nonnegativity and trace are checked; the trace is
only a consistency identity, not an independent orthogonality proof.

## Prefix reuse validation and aggregation

Before reusing a degree-max basis, the producer constructs independent
bases at degrees2,3,4 with the unchanged frozen `e1_exact.build` and compares
all prefix b,d,recurrence and metadata exactly. It separately executes
`e1_exact.bounds` at those degrees and compares all four endpoints and pivot
choices with the frozen sweep. Every generated degree2–12 prefix endpoint
and choice sequence must subsequently equal its old independent-degree
record exactly. Higher-degree runs require the corresponding completed
maxdegree12 overlap receipt before execution. A mismatch is an assertion
failure and G1 STOP, not a tolerance comparison.

At each source, energy is accumulated along the complete frozen recurrence
and sampled at whole-degree boundaries. Per stage and node, the producer
retains the sum and maximum of the nonnegative source energies. Multiplying
these by that stage's nonnegative normal-projector diagonal gives H² and
L² respectively. This reorders only exact finite sums and maxima; it does
not replace the source class or output. Witness ties retain the earliest
source/node as in the original source-major traversal. Stages are finalized
only when every source in their prefix has actually been processed.
Incremental exact endpoints survive in external files if a later stage is
interrupted.

## Input recovery and reproduction

The old88-row full-source sweep was recovered read-only from commit
`2b52b432fe59c9a50aef9deebe5152c5d6874465`, path
`topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json`:
616,693bytes, SHA-256
`0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344`.
It is restored under `/tmp/padua-lanczos-frontier-g1/inputs/`; no removed bulk
file is repopulated in Git. This input may be recovered with read-only
`git show COMMIT:PATH` and the recorded size/hash checks.

Initial overlap command, repeated for the eight set/rule combinations:

```sh
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps python -B topics/padua-lanczos-frontier-20261105/code/g1_exact_prefix.py --set triangle --rule bj --max-degree 12 --old-sweep /tmp/padua-lanczos-frontier-g1/inputs/e1-full-sweep.json --output-dir /tmp/padua-lanczos-frontier-g1/overlap/triangle-bj --receipt /tmp/padua-lanczos-frontier-g1/overlap-triangle-bj.json
```

Fresh output directories are required. Eight processes were dispatched in a
bounded two-worker external launcher, except the first triangle/BJ pilot
which ran separately. Exact subprocess commands are in each case receipt;
logs and launcher receipts stay external. `g1_manifest.py` builds a compact
inventory from actually completed case receipts and hashes their external
endpoint/recurrence artifacts.

For higher cases use a new output directory, set `--max-degree` prospectively,
and pass the matching `--overlap-receipt`. Each case has a1800-second hard
cost deadline covering all work. A timeout records pending status and partial
stage/source progress; it does not silently omit sources or report a finished
scan. The separate native GMP port is the planned continuation if the limit
is reached. High-degree cost is benchmarked before launching all eight
maxdegree20 cases.

## Status and limits

Execution is in progress. Completed cases, actual costs and pending cases
will be recorded additively below and in compact inventories. No fitting or
trend/gate interpretation occurs before all152 required rows are complete.
Independent reconstruction/porting is assigned separately; this producer
cannot self-approve. No finite trend can establish an all-degree rate, IEEE
activation or the separate SH_n candidate.

Raw exact arrays stay under `/tmp/padua-lanczos-frontier-g1` with size/hash and
regeneration commands in receipts. They are temporary working artifacts;
cold-storage archival/delivery remains pending the orchestrator's procedure.

## Executed checkpoint — T24 complete, rotated cases pending

The first T24/BJ maxdegree14 cost benchmark completed in22.22s, after its
maxdegree12 overlap case passed. All four T24 maxdegree20 cases subsequently
completed, giving76 exact rows across degrees2–20. Per-case elapsed times
were63.97s (BJ),62.85s (mirror),51.17s (alternating),46.58s (pivot), with two
concurrent workers. These commands use the higher-case arguments above;
their complete argv, code hash, versions and output identities are in the
external `full-triangle-*.json` receipts and compact `evidence/g1-scan.json`.
Their legacy2–12 endpoints and choices were rechecked exactly in each run.
No fits or higher-degree trend interpretation have been made.

At this checkpoint, own rotated BJ/mirror legacy cases completed all11
stages, at268.9/275.4s wall respectively. Own rotated alternating/pivot
legacy cases are still running, so the compact overlap inventory currently
contains66 completed rows and explicitly lists the two missing cases.
The matching independently implemented native port separately completed
all88 legacy comparisons; its audit/receipts are owned by the independent
worker. That worker also reports exact comparison of all76 T24 high rows
in `evidence/g1-independent-triangle20-comparison.json`; these are its
executions, not additional executions by this developer.

A rotated BJ maxdegree14 benchmark is running prospectively, using its own
passed legacy overlap receipt. Full rotated maxdegree20 Python cases have
not been launched pending that cost measurement. The separate native port
has begun its high-degree cases with1800-second limits; any timeout remains
pending work rather than a completed row. This checkpoint does not complete
the152-row scan and does not authorize fitting on a subset.

### Additive overlap completion

Own rotated alternating/pivot overlap cases later completed at358.51s and
302.53s wall respectively. The producer now matches **all88** inherited
source-complete degree2–12 rows, all four endpoints and every choice sequence.
Rotated pivot includes the exact (2,1) tie with X chosen; T24 has no pivot
tie in the inherited2–12 scope. `evidence/g1-overlap.json` now inventories
eight completed cases and no missing overlap case. The earlier66-row
checkpoint remains historical, not the final overlap status. The high scan
still has only the76 completed T24 rows at this boundary; rotated BJ14
cost benchmarking and native rotated20 work continue under their deadlines.

### Rotated cost benchmark completion

The rotated BJ maxdegree14 benchmark completed in703.35s wall, including
exact reproduction of its legacy2–12 rows and exact endpoints at13/14.
Its receipt is `/tmp/padua-lanczos-frontier-g1/benchmark14-rotated-bj.json`,
with endpoint and basis identities. Together with the full legacy overlap
and completed T24 high cases, the best available actual coverage is122
unique preregistered rows:76 T24 plus13 rotated/BJ and11 for each other
rotated rule. Remaining are rotated/BJ degrees15–20 and rotated
mirror/alt/pivot degrees13–20,30 rows. `g1-scan.json` deliberately inventories
only completed maxdegree20 cases, rather than relabeling benchmark/overlap
runs as full high-case completions. Native rotated20 cases remain running;
Python rotated20 cases were not launched after this high-cost benchmark.
No fitting or operational trend decision has been performed.
