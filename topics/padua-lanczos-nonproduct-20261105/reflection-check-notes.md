# Sign-reflection scalar-checker implementation — 2026-11-05

Technical developer: Codex, requested gpt-6.1-sol medium; serving metadata is
not independently exposed. Rules read at dbe5c811e0b22498382c8b3a6f2b0f2d9eb66bfc.
Own only the new source, these notes and evidence/reflection-check*.json.
Original native/scalar checkers and the unsuccessful FLINT attempts stay frozen.

## Prospective implementation and gate

Read the complete written p6-reflection-methods.md from P4 before preparing
this implementation. This is the dated existing-model method variant it
registers, not a new mechanism, family, endpoint or priority claim. Its
conditional equivalence and mandatory guards control this implementation.
Preparation is authorized before review; **no experiment or scientific
execution before distinct mathematical review and coordinator approval**.
Approval provenance and actual execution will be recorded below when received.

The source is copied from ORIGINAL code/p6_scalar_check.cpp. Per-entry GMP
mpq_class arithmetic, full weighted input, basis, creator candidates/scales,
pivots/ties and off-diagonal Gram checks remain independent of the producer's
common-vector-denominator arithmetic. An additional exact diagonal Gram check
is retained alongside the original norm calculation. No producer functions,
FLINT arithmetic or earlier zero-fast-path variant is used.

New exact guards verify distinct weighted nodes, both reflection coordinate
and equal-weight permutations, bijectivity, involution, commutation and the
exact orbit partition by (abs(x),abs(y)). Actual representatives are original
indices. Sizes1/2/4 and counts are computed, not inferred from a family label.
Every full-node basis column is checked against its exact exponent parity
under both reflections; every candidate alpha with different character must
be exactly zero, and every candidate parent has its exact required exponents.
These guard counts and phase timings go to stderr; endpoint JSON is unchanged.

Only g_kh and squared energy are propagated on the representatives, for
EVERY original source h=1,...,N-1. Each completed-prefix v snapshot is copied
back to every original node before updating the original full-node totals and
maxima arrays. A counted coverage guard checks exactly
M*sum_(s=2..degree)(N_s-1) original-node/source snapshots were updated. Final
normal diagonals, trace, L/H/Urow/upper aggregation still visit every original
node with its actual weights and the full basis. Thus H retains every original
summand; Urow is a maximum over actual nodes and is not multiplied by orbit
size. Source positions and endpoint schema remain unchanged.

The coordinator explicitly confirmed retaining this stricter full-node
snapshot expansion to match P4 mandatory guard6; no proof wording change or
representative-total shortcut is used.

## Prospective pilot and acceptance

After approval: compile new reflection source and unmodified original scalar
source, run guard self-test and malformed nonclosed-coordinate/unequal-weight
inputs, then degrees6 and8 all four rules, one extra process at a time,
60seconds per process. Compare every non-timing JSON field against a fresh
original scalar execution at the SAME cap, including its exact Gram count.
Also match accepted producer/scalar degree8 reference prefixes; for cap6,
verify reference and current Gram counts separately against each run's own
full basis dimension before comparing the remaining scientific fields.

Both supplied disk inputs must actually report324 original nodes,
90 representatives,18 size2 and72 size4 orbits. Full prescribed source counts,
exact traces, choices/ties, all endpoint rationals and every degree prefix
must agree. Timings are a finite cost screen, not an inferred degree16 speed.
No degree16 launch is authorized to this worker until root explicitly decides.

## Runs

At preparation, none executed; mathematical approval remains pending. Exact
commands, source/binary/input/output identities, guard counts, environment,
comparison coverage and timing/timeout masks will be in compact receipts.
Raw arrays stay in the topic-specific /tmp directory. No prose hash guard,
Git operation, shared proof mutation or archival-delivery claim is introduced.


## Approval and first executed results

The coordinator reported distinct mathematical acceptance of all seven
written guards and explicitly authorized bounded execution before compiling
or running this source. The approved review identity was supplied in-session;
this checker does not hash-pin or parse the prose proof as an executable guard.
The narrowed initial pilot is D36BJ/alt6, then all4rules8, plus D65 if cheap.

Compiled the new source and ORIGINAL scalar with g++ -O3 -std=c++17 and
-lgmpxx -lgmp into the topic's /tmp/reflection-check directory. The unchanged
new source SHA256 at experiment start is
09d524f915076105b04fb196ee98c6c6cd4cecbc6b6e49bcfacb541ffc999088.
Exact compile argv and both binary/source identities are in
reflection-check-guards.json.

Guard tests PASS: built-in controls detect missing reflection, normalized
unequal weights and corrupted basis parity; two independently prepared full
normalized disk inputs with nonclosed coordinates or unequal reflected weights
reject at their intended guards before any output row. No bad input is silently
coerced. Every successful node/orbit count is derived from exact input.

D36BJ/alt6 and BJ8 first completed: all non-timing fields match fresh ORIGINAL
scalar at identical cap, including Gram count, and accepted producer/scalar8
prefixes agree after independently checking each build's full Gram count.
The complete prospective queue, current status and eventual timings are in
reflection-check-pilots.json; individual receipts carry guard counts and
all actual command/file identities. Later entries must be read for the final
mask; this addendum does not claim unfinished cases.


## Completed bounded outcome

All10developer pairs completed within60seconds per process: D36BJ/alt6,
and all4rules through8 on BOTH D36x9/D65x9. No timeout or mismatch.
Each pair is a separately executed fresh original and reflection process;
this is developer comparison, not distinct-agent approval. All scientific
fields including same-cap Gram counts match exactly, apart from elapsed_seconds.
Accepted producer and scalar8 reference prefixes also agree with their own
full-build Gram counts verified separately. The two exact input hashes agree
with the original accepted input identities. Source bytes stayed frozen.

| Family | Cap | Rule | Fresh original (s) | Reflection (s) |
| --- | ---: | --- | ---: | ---: |
| D36x9 | 6 | bj | 1.447 | 1.067 |
| D36x9 | 6 | alt | 1.993 | 1.139 |
| D36x9 | 8 | bj | 9.948 | 5.705 |
| D36x9 | 8 | mirror | 10.151 | 5.858 |
| D36x9 | 8 | alt | 12.746 | 5.733 |
| D36x9 | 8 | pivot | 9.601 | 5.527 |
| D65x9 | 8 | bj | 3.473 | 2.023 |
| D65x9 | 8 | mirror | 3.724 | 2.070 |
| D65x9 | 8 | alt | 4.927 | 2.672 |
| D65x9 | 8 | pivot | 4.876 | 2.872 |

Every case computed324nodes and90representatives:18size2 and72size4.
Through8 every full-node parity check count is29160, every source loop has
44positions, and exactly49896 full-node/source snapshots are expanded and
updated across all completed2–8 prefixes. Nonpivot cases check44exact parent
relations and990alpha slots, of which750require zero across characters.
Pivot cases additionally check both admissible candidate creators where
available; their separately recorded guard counts were recomputed from the
original exponent order and candidate counts by the pilot harness.

At8 this gives about1.7–2.2x total wall improvement on these serial pairs,
with changing concurrent original successor load. It does not establish a
precise isolated speed ratio or degree16 timing. Every full-node norm,
Gram, source scale, normal and endpoint contribution remains present;
the improvement comes solely from reusing proved equal squared-response
values. No source or endpoint model change is introduced.

All evidence/reflection-check*.json files are compact command/identity/count
receipts, with raw stdout/log/input fixtures under the topic's /tmp directory.
The summary links individual receipt hashes; no prose record is hash-guarded.
Root owns method acceptance, provenance integration, final inventory and any
full16runner. The developer's one-extra-CPU slot was released to scan_check
for independent fresh conformity/replay checks after this queue completed.

## Next boundary

Source is stable and ready for focused code acceptance, with the mathematical
proof already reviewed. No degree16 run has been launched by this worker.
The existing original scalar3600jobs remain unchanged. Full16 reuse may be
scheduled only by the coordinator after reviewing these actual timings and
the distinct code/finite checks; success at8 does not certify16 rows.
