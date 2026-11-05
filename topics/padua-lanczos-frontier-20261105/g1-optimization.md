# G1 common-denominator optimization — prospective bounded plan

Rules/read head `02a465b`; integration head supplied by root is
`bb67c1ee830d468fa33007e15008d5574d00ccf4`, merging main
`aff30e8`. Frozen Lanczos sources and rules are unchanged. Codex technical
developer, requested gpt-6.1-sol medium. Own only new `code/g1_fast*`, this
record and `evidence/g1-fast*`; no Git or old-source/receipt mutation.

Read handoff04, saved attempts/L1 G1 preregistration, old producer methods,
independent implementation report and bounded high20 cost receipt. This is
routine exact representation/implementation work for the already gated G1
scan, not a new scientific mechanism, node family, source class or criterion.
The saved gate is used at that restricted scope; no new novelty claim.

## Bottleneck and first implementation choice

The old FLINT and C++/GMP scalar-rational implementations canonicalize many
nodewise fractions during full projection, propagation, squaring and energy
aggregation. Rotated degree20 already spent minutes on its exact basis and
then reached the1800s cap with only12–37 of230 sources propagated. All625
nodes and every source remain mandatory.

The first optimization is **one common denominator per whole node vector**:
represent exactly the same vector as `(integer FLINT row, positive integer D)`.
Use native integer matrix operations for dot products, scalar axpy and vector
addition; coordinate products and elementwise squares use arbitrary-precision
integers. Canonicalize common content once per completed vector, not at every
node operation. No symmetry reduction, paired-node compression, gauge change,
source omission, floating arithmetic or interval replacement is used in this
first round. Thus no new parity lemma is needed.

The representation invariant is componentwise `v_i=num_i/D`. Addition uses
the lcm of positive denominators, scalar multiplication multiplies its rational
numerator/denominator, and dot products form one exact integer inner product
divided by the two denominators. Dividing common content preserves every
component. Squaring is componentwise. A nodewise maximum uses a common positive
denominator before integer comparisons. These elementary identities preserve
exact b,d,alpha,g,normal diagonals and endpoint sums/maxima; independent checks
must still verify implementation rather than assume that invariant holds.

## Frozen experiment and acceptance

Exactly the original T24/rotQ24 nodes, graded order, four rules BJ/mirror/alt/
pivot with X ties, all source columns, PD-T137 L²/H²/Urow² and
U²=min(H²,Urow²). Prefix reuse is allowed only after exact fresh-degree controls.
No fitting or operational G1 decision occurs before all152 original rows.
The full all-degree/scalar/IEEE questions remain separate.

Before any scientific run, record the new source hash and command. Planned
bounded sequence, stopped on any mismatch:

1. Deterministic rational-vector arithmetic controls against FLINT fmpq, including
   negative values, nontrivial common factors, zeros, signed scalar coefficients,
   squares, nodewise maxima and dot products. These test representation only.
2. Fresh exact degree2,3,4 baseline/endpoint comparisons on both grids and all
   four rules. Verify every basis component, norm, recurrence coefficient and
   choice/tie sequence against the frozen scalar code where feasible.
3. Full maxdegree12 overlap on both grids/all four rules, with exact equality of
   all88 inherited endpoint rows and choices/ties. Cap each new case at120s;
   a cap reports incomplete cost, never missing-source completion. Keep at most
   two cases active. Exact small-degree independent builds precede prefix use.
4. Only after all88 overlap rows pass, run one moderate rotated BJ maxdegree14
   benchmark, cap180s, and compare its13/14 endpoints with the retained old
   FLINT benchmark. Record wall and process CPU time, phase times and bit sizes.
   The prior703.35s run is context, not a controlled timing comparator. A small
   matched-degree old/new timing may be used to separate resource effects.
5. No degree20 run in this round without measured feasibility and **new explicit
   root authorization**. Do not rerun old1800s cases unchanged or extend their
   cap. If common denominators fail or provide insufficient speedup, retain the
   obstruction/cost evidence and propose the next bounded change prospectively.

Large exact endpoints/bases/logs stay under
`/tmp/padua-lanczos-frontier-g1-fast`; compact receipts retain commands,
source/input hashes and outcomes. All historical code/receipts stay unchanged.
The independent port/checker worker receives this plan before execution and
chooses its own implementation/reconstruction route. Root/math reviewer must
check any subsequent nontrivial reduction before it is used.

## Execution status at plan registration

No optimized scientific calculation or benchmark has run. Only source/rule/
receipt reads and installed FLINT API introspection have occurred. The source
has not yet been written. Results and implementation revisions will be appended
below without rewriting this prospective plan.

## Executed bounded round — implementation 7dbc7ecb

`code/g1_fast.py`, SHA-256
`7dbc7ecb609ee5db9ebcb9a52bf39f13e5273ccfebc330791223ca2923f49f3b`,
was written and its hash recorded before the first run. The source has not
changed during these executions. Primitive rational-vector controls pass,
including signed coefficients, zero-vector denominator canonicalization,
nontrivial common content, products/squares/dot products and maxima/ties.

Eight full-node degree4 cases completed: all24 stage rows match old exact
endpoints/choices, and fresh scalar degree2/3/4 bases, norms and recurrence
coefficients match every prefix component. Every new-column Gram pairing
is checked directly by the new integer-dot implementation.

All eight maxdegree12 cases then completed within the prospective120s cap,
matching all88 old endpoint/choice rows exactly, with recorded pivot ties.
All original325/625 nodes and every source remain present. Timings were
6.1–14.2s for T24 and90.5–97.2s for rotQ24, with at most two workers.
Rotated basis construction took1.8–3.3s. T24 is slower than the earlier
small-denominator scalar implementation; no universal speedup is claimed.
Rotated comparisons with old wall times are historical context under different
concurrency, not a controlled performance ratio. Root directed skipping
unnecessary old-backend benchmark duplication.

`evidence/g1-fast-overlap.json` is the compact completed checkpoint; external
per-case receipts retain exact argv, wall/CPU phase times, output identities,
and recorded basis/endpoint integer bit sizes. The prospective plan bytes
are retained at `/tmp/padua-lanczos-frontier-g1-fast/plan-prospective.md`.
The mathematical reviewer independently inspected all155 source lines and
found no representation/aggregation defect. That source review is not a
new execution or an independent implementation.

The approved single rotated BJ14 benchmark used cap180s and the original
retained benchmark as its intended exact comparator. It reached source83/119
at180.0003s and stopped; only degree2–11 endpoints were complete. Its baseline
was complete, but no degree12/13/14 endpoint or full-case completion is claimed
for this benchmark. The end-of-case comparator therefore was not reached.
This cost result is recorded separately in `evidence/g1-fast-benchmark14.json`;
it does not invalidate the completed all88 overlap or reject a scientific
target. No producer degree20 run was made.

The distinct C++/GMP common-denominator implementation independently completed
BJ14 in23.207s and exactly matched all13 old benchmark rows, and root separately
authorized its BJ20 pilot capped600s. Its worker reports actual BJ20 completion
in329.175s with all625 nodes and230 sources. Those are independent worker
executions, not executions by this producer; its code/receipts are separately
owned and further root decisions remain explicit.

## Proposed next bounded revision — not executed

The current producer still materializes625 Python fmpz entries for each
intermediate scale/add vector and promotes nodewise maxima to one shared lcm
denominator. Neither is mathematically required. A possible next revision is
lazy numerator materialization/early-index common-content gcd and separate
unreduced positive-denominator pairs for each node's peak. Compare peaks only
by integer cross products; do not canonicalize them until the final endpoint.
The independent native port already used the latter representation in its
own independently written backend. This proposal is routine exact arithmetic,
not a new scientific mechanism, but any revised implementation needs signed/
zero/tie primitive controls and fresh old overlap before scaling.

Root direction and a prospective next cost bound are required before this
revision or any new producer degree20 run. No unchanged1800s retry or cap
extension is implied. All previous source/receipts remain unchanged.

The short rules-read identifier above resolves to full commit
`02a465bea0339f20278ba4888e28f9e9b6041603`; this provenance expansion
changes no prospective scope or computation.

## Root-authorized second bounded revision — registered before new runs

Root now authorizes the next exact implementation revision: lazy numerator
materialization and per-node unreduced peak pairs. The first source bytes
are preserved as `/tmp/padua-lanczos-frontier-g1-fast/source-v1-7dbc7ecb.py`,
SHA-256 `7dbc7ecb609ee5db9ebcb9a52bf39f13e5273ccfebc330791223ca2923f49f3b`;
the completed overlap and failed180s benchmark receipts remain unchanged.

In the revised vector constructor, common-content gcd examines integer
entries by index and can stop at gcd1 without allocating625 Python objects.
A numerator tuple is materialized only when componentwise work needs it,
then cached for that immutable vector. All rational vector values are
unchanged. Peak values are625 separate `(numerator, positive denominator)`
pairs per stage; compare `newnum*oldden>oldnum*newden` exactly, replace only
on strict improvement, and reduce to a rational only at final endpoint
selection. The normal diagonal is multiplied before selecting the final
node/source maximum, using exact denominator comparisons. No node/source,
gauge, family, endpoint or tie convention changes.

Prospective validation repeats targeted signed/zero/common-content/tie
arithmetic controls and rejects zero denominators, invalid dimensions,
nonpositive source indices and malformed peak denominators. Fresh scalar
degree2/3/4 controls and all88 old overlap rows must pass again, max120s per
case and two workers. Next run one rotated BJ14 benchmark, cap180s, requiring
exact agreement with original13/14 endpoints. No old-backend rerun is planned.

Root conditionally preauthorizes **one** new producer rotated BJ20 pilot
only if this stable source completes BJ14 in at most60s and matches old13/14.
The pilot cap is600s, and every one of its19 rows must compare exactly with
the independently completed native BJ20 output. CLI guards will require the
same-source accepted benchmark receipt and that comparator. No other20 rule
or larger cost cap is authorized. If the condition fails, report the measured
cost and next plan before20. Source hashes and actual commands will again be
recorded before each new scientific execution.

### Second revision actual outcome — source 963d61bc

Source SHA-256
`963d61bc13e4bfe90776be3d76f1b613a3191f3447e3ce0b918c0cdca1be5a22`
was recorded before its first run and remained unchanged throughout. A copy
is preserved as `/tmp/padua-lanczos-frontier-g1-fast/source-v2-963d61bc.py`.
All eight fresh degree4 cases and all88 old maxdegree12 overlap rows pass;
nine malformed primitive controls are rejected in each case. The full12
baseline/norm/recurrence dumps match v1 byte-for-byte after decompression.
Rotated12 wall times are70.1–72.9s; T24 times4.1–10.1s. See the separate
`evidence/g1-fast-v2-overlap.json` checkpoint.

The stable-source rotated BJ14 run completed all625 nodes/all119 sources in
170.857s (CPU170.760s, basis2.621s), below its180s case cap. All13 endpoints,
including original13/14, exactly match the retained old benchmark. The
conditional60s prerequisite for a producer20 run is **not met**. Therefore
no producer20 pilot has been run or silently substituted. Its source guards
also reject20 without an accepted same-source fast benchmark. The cost result
is in `evidence/g1-fast-v2-benchmark14.json`; the independent native BJ20
execution remains separate.

Static inspection of the retained exact rotated12 recurrence counts34,654
nonzero scalar-vector subtraction uses across all source responses. The
current Python implementation constructs/canonicalizes a scaled vector and
a difference for each term, despite the common-denominator representation.
A prospective next cost change is one lcm-weighted integer linear combination
per formed column, with common-content normalization only after the full sum;
energy updates could use the same exact sum identity. This reorders only
finite rational arithmetic, never drops coefficients or changes scientific
criteria. A short degree8 profile (cap30s), primitive/small controls, all88
old overlaps and BJ14 at the same bounds were proposed to root. No such
revision/profile or further scientific run has occurred at this boundary.

## Final bounded stop and unexecuted batched-sum follow-up

Root explicitly stops this round at the completed revision2 boundary. No
further optimization, profile, benchmark or20 run is authorized now. Current
scientific source remains963d61bc and all prior receipts remain unchanged.
The distinct native pilot's completion does not satisfy this producer's
unmet60s prerequisite. The following is a proposed next-handoff implementation,
not work performed in this round.

For rational coefficients a_j=A_j/B_j, B_j>0, and complete node vectors
v_j=n_j/d_j, d_j>0, form

    D = lcm_j(B_j*d_j),
    n = sum_j A_j*(D/(B_j*d_j))*n_j.

Then componentwise `n/D=sum_j a_j v_j`. One final division by the common
content preserves every component. Cancelling gcd(A_j,d_j) before computing
term denominators is also exact; any further cancellation/caching change
needs its own explicit invariant. Zero terms/empty sums must produce the
correct full-length zero row. Negative coefficients and strict peak ties
must remain supported. This identity uses only arbitrary-precision integers
and positive denominators, introduces no overflow assumption and changes
neither source/output gauges nor any mathematical recurrence coefficient.

Proposed applications are the complete formed basis column
`u-sum_l alpha_l b_l`, frozen response
`coordinate*g_parent-sum_l alpha_l g_l`, and exact energy update
`energy+g_k^2/d_k`. Do not omit any term, coordinate, source or degree. All
maxima remain the already checked per-node positive-denominator pairs.
The proposed batched sum removes intermediate Python vector creation and
canonicalization; it may also enlarge temporary integer heights. Record
intermediate denominator/numerator bit sizes and memory/cost rather than
assuming a speedup.

A bounded next plan for root to authorize prospectively:

1. Preserve the full963d61bc source/receipts and record the next source hash.
   Obtain a brief degree8 current-source cProfile diagnostic, cap30s, only to
   identify arithmetic/allocation cost. Profiled timing is not a speedup
   benchmark or scientific fit.
2. Implement the integer batched linear combination independently of the
   separate native port. Check signed, zero, common-content, cross-denominator,
   malformed-dimension and peak-tie cases against direct FLINT rational sums.
   Have the mathematical/implementation reviewer verify the component invariant.
3. Repeat fresh scalar degree2/3/4 basis/norm/recurrence controls and all88 old
   rows, max120s per case and at most two workers. Check full Gram pairings,
   exact choices/X ties, complete source counts and all endpoint equalities.
4. Only after those pass, one rotated BJ14 benchmark, cap180s, comparing all13
   exact rows with the retained original benchmark and independent native result.
   Record unprofiled wall/process CPU time and phase/bit-size evidence.
5. Report measured feasibility before any new20 authorization. The prior goal
   remains BJ14<=60s followed by at most one BJ20 cap600s with exact independent
   all19-row comparison; root must carry or amend that budget explicitly in the
   next handoff. Other20 rules and unchanged1800s retries remain unauthorized.

No G1 fit or operational verdict can use the incomplete two-grid scan, and
no finite computation proves an all-degree rate. This implementation follow-up
adds no new scientific mechanism or novelty claim.
