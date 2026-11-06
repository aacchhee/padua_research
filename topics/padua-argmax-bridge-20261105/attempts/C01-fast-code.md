# C01 cheap independent kernel audit

Rules/source head: `4b728b04216a5490910780bc609a82b853058426`.
Developer: Codex, requested gpt-6.1-sol medium; serving metadata unexposed.
Status: prospective diagnostic plan; no new mathematical candidate or certification.

Scope: inspect and time unchanged independent Arb v3 arithmetic using a separate generated instrumented translation unit. Old sources, producer arithmetic, checker and inputs remain untouched. Novelty gate is inapplicable to this source/operation audit; any analytic replacement awaits the separately assigned mathematical author and review gate.

## Exact source operation plan before execution

For degree n, let T=2n(n+1), the number of parity-admissible grid entries. A call builds three boards, each T primitives. Each primitive runs two length-n harmonic loops, calls one cosine correction and attempts four quotient refinements. Each refinement always performs one sin/cos call and, when its denominator excludes zero, performs another. Thus harmonic calls =12n²(n+1), correction calls=6n(n+1), and refinement calls range from24n(n+1) to48n(n+1). Total trig-call range =6n(n+1)(2n+5) to6n(n+1)(2n+9). Finite harmonics are always evaluated before optional quotient intersection; removing quotient work alone cannot remove the cubic cost.

Two collect passes each perform T(n+2+n+1) pair visits; total =4n(n+1)(2n+3). Each visit evaluates both natural and positive-pair bounds. Hence independently removing harmonic degree growth still leaves cubic projected profiles. Final center admissibility minimum is quadratic.

Instrumentation freezes before measurements: process CPU scopes for board, harmonic ratios, quotient refinements, and collect, plus call/iteration counts. Scope timer overhead is included. One selected existing numeric leaf at each n17/24/32, then exactly one synthetic [0.125,0.1328125]x[0.25,0.2578125] box each n64/128. No cover, candidate traversal, refinement or certification; CPU ceiling180s for all C01 diagnostics, with worker cap150s allowing build/headroom. Stop before the next box if cumulative CPU exceeds120s. Results are MEASURED only; asymptotic formulas above are source counts, not timing extrapolation.

Trigonometric cache opportunity: board values depend on s=(u+v)/2 and t=(u-v)/2 at rational mesh combinations. gcd(n,n+1)=1 means no generic collisions among single-board grid s or t modulo2pi on the parity class; caching full degree-dependent harmonic grids is not automatically a subcubic method. Corner board and its corner norm are constant across boxes and can be cached per n, reducing a fixed factor only. Fixed pi/node coordinates can also be cached. Mathematical periodic/phase symmetries require explicit proof before reuse.

## Runs needed

Frozen instrumentation build; bounded timings and runtime closure. Inspect actual pinned FLINT sinc implementation or disassembly for hidden degree-growing work before selecting that API. No analytic replacement or consequential replay yet authorized by the mathematical gate.

## Executed diagnostic: MEASURED

Frozen `profile.py` SHA256 `c839838a51766f322ed6d1f2df155307c42e6d24980015f9aaea57311862762a`; original v3 `f52d1a9da3c86212663f7ac22e9475b76811d7be4bbc4916779fd32a59d95bf0`. Command: `python topics/padua-argmax-bridge-20261105/code/cheap_C01/profile.py`; native worker and command exit0. One first saved nonoutside leaf each n17/24/32, then one synthetic box each n64/128. No tree replay, cover, new certified degree, arithmetic replacement or acceptance predicate occurred.

| n | whole box CPU s | finite harmonics | optional quotient | board total | two collect passes |
|---|---:|---:|---:|---:|---:|
|17|0.09207|0.04012|0.01987|0.08000|0.01207|
|24|0.21995|0.12784|0.03604|0.18393|0.03601|
|32|0.47997|0.28820|0.08014|0.40393|0.07604|
|64|3.43463|2.14651|0.41661|2.66289|0.76770|
|128|24.11995|16.84820|1.47621|18.84470|5.26725|

Whole diagnostic ownCPU28.707126 + childCPU1.400104 =30.107230, wall30.111908. Scope timers nest: board includes harmonic and refinement CPU; columns must not be summed. Instrumentation overhead is included; no uninstrumented timing comparison was run. All observed loop counts match the prospective formulas. n128 spends69.9percent in finite harmonic evaluation and21.8percent in collect; suppressing the optional quotient alone addresses6.1percent. This supports pursuing both ratio and projected-profile algorithm changes, without asserting an asymptotic timing law.

Essential record: `evidence/c01-fast-profile.json` (8591bytes). Full source snapshots, preprocessed TU, binary, complete header/toolchain/link/loaded closure, frozen input hashes and actual command are in hash-pinned local `cheap-C01/profile.json`. Raw/local archive transfer remains pending. No old source changed.

Pinned FLINT3.1.3 header provides `arb_sinc`, `arb_sinc_pi`, `arb_poly_sinc_series`, and `arb_poly_sinc_pi_series`, but no scalar sinc derivative API. Actual `libflint.so.19` disassembly shows `arb_sinc` calling `_arb_sinc_direct` and `_arb_sinc_derivative_bound`; direct calls `arb_sin` then `arb_div`, and interval path bounds radius using the derivative bound. These inspected wrappers contain no degree-index harmonic loop. This is a bounded binary call-structure observation, not a complete complexity proof for transcendental routines; arithmetic precision and argument reduction still cost work. Disassemblies stay local and have evidence hashes. Fixed Taylor value/derivative enclosure from the separate ratio author may give tighter pole behavior than this generic API.

Next: mathematical author freezes exact pole/quotient/global formula and an independent mathematical review accepts it before any replacement implementation. Independent instrumentation/source review remains pending. No consequential replay is released here.

## Read-only row-backend feasibility inspection — OPEN

This is an inventory of existing formulas/interfaces, not a new mathematical candidate, revised model, complexity result or executed experiment. Read `theory/N2-row-decomposition.md`, `N2-profile-target.md`, `N1-row-model.md`, `N5-partial-cotangent.md`, `N1-round4-rows.md`, `N1-round4-endpoint-block.md`, and the block/special-row definitions in `N1-round6-near-model.md`; inspected `code/n2_rows.py`, `code/n1_rows.py`, and loop sites in `n1_near_r7_normalization.py`.

Existing N2 exact row algebra reduces the absolute row to its closed signed sum plus two partial cotangent channels on the negative set, with explicit polynomial collision negative parts. The negative set is a symmetric difference of two arcs with at most four arc boundary points. This already avoids discovering signs by testing n kernel entries. N1-01 maps those sets to mesh blocks, cuts at channel wraps/collisions, and applies the existing N5 fourth-order regularized-cotangent formula. N1-round6 records the conservative bound of twelve contiguous blocks per channel after allowing two collision points, two numerator zeros and the circle cut. Thus block enumeration has a fixed bound per row at a fixed phase; this does not bound the number of membership changes over a whole phase box.

The existing executable diagnostics do not implement the resulting cheap certifier:

- `n2_rows.py:direct_q` first allocates the whole 2n(n+1) board, then loops over the O(n²) finite Fourier coefficients; its vectorized board operations therefore grow as O(n⁴) arithmetic. Its subsequent reconstruction still visits every column of every row, detects collisions by binary64 tolerance, and sums selected cotangents explicitly. This is a sanity script, not a validated backend.
- `n1_rows.py:phase_case` builds all n `us` and `fs` in every one of2(n+1) rows, visits each point to determine membership/collisions, and computes endpoint rows by explicit sums. `finite_g(direct=False)` uses a closed quotient/collision formula per point, but this still leaves quadratic point work. With `direct=True`, its nested polynomial loop is quadratic per point. `block_model` receives an already enumerated point list, sorts it, and detects progression gaps; replacing only its final block evaluation does not remove that input cost. Its `mp.digamma` differences are not outward rounding. The harmonic error bound at the end is also evaluated by an n-term `fsum`. `phases` has a separate quadratic collision-search diagnostic.
- `n1_near_r7_normalization.py` likewise has explicit row/column or tensor loops; it is a finite normalization check, not an implementation of the fixed-count continuous near model.

An O(n)-row interface would therefore require, under a new prospective gate and independent mathematical review:

1. Direct interval-safe arc-to-integer endpoint conversion, with no per-column search. Floored/ceiled endpoints must be certified or both neighboring choices enclosed. Tangent roots and p=0 need explicit cases; interval `asin(W/p)` cannot be used when division or root branches are unresolved. A phase box can contain many grid crossings: twelve blocks at each phase does not license one fixed membership list throughout the box.
2. Validated reciprocal-block evaluation, e.g. exact identity `sum_{i=0}^{q-1}1/(y+i)=psi(y+q)-psi(y)` for positive arguments, with bounded hidden work and a cancellation-safe enclosure. Pinned Arb header has `arb_digamma`, but its implementation/cost has not been inspected here. Calling a special function is not evidence that its recurrence/shift work is degree independent. Existing H8 (eight explicit terms plus a logarithm) is proved with error<=1/[8(y+15/2)^2] for arbitrary q; current near-model proof spends that error only on at most four special rows, not on2(n+1) rows. Extending its use requires a newly proved total weighted budget, especially near endpoint coefficients.
3. Stable validated W,w' evaluation at/near0 and pi, including removable continuation on the full N5 cell domain, rather than subtracting singular cot/csc terms in interval arithmetic. N5 bounds approximation error to the cot sum; outward arithmetic error is a separate charge.
4. Endpoint and collision handling that preserves the original corrected x-mode and both signs of the explicit collision value. Two endpoint rows kept as n-term sums would still be O(n) total, but naive finite-polynomial evaluation at each endpoint would not be. The fixed-R endpoint profiles are approximations with existing error bounds, not drop-in exact rows; using them changes the enclosure contract and requires charging their errors. Exact whole-row quotient/sinc forms would need their own validated proof/control interface.
5. A whole-box output contract compatible with strict maximum exclusion: S_upper, needed corner-orbit upper, defect lower or an explicitly reviewed analytic premise, corner constant interval, and pi interval. N2/N1 row formulas directly address S; they do not automatically compute corner-orbit sums or projected triangle defects. A pointwise cheap S evaluator alone cannot replace `phase_bounds`.
6. Either direct whole-box row enclosures with branch changes covered or a proved phase-derivative/Lipschitz interface. Differentiating floor-selected block expressions across changing membership without charging boundary terms is invalid. Absolute-row values remain continuous, but absolute gradients can switch at zeros and collisions; N1-round8 separately charges branch artifacts for its existing Q_n bookkeeping and does not supply a generic row-backend derivative API. Numerical derivative agreement would be only a control, not the missing theorem.

A conditional operation count is straightforward only after these obligations:2(n+1) rows times a fixed number of validated blocks and endpoint operations, plus finitely many analytic error terms. It does not establish practical million-degree throughput: O(n) high-precision transcendental work per phase box may remain expensive, and no timing was run or inferred. The accepted fixed-count near model avoids the outer row scan by proved quadrature/profile terms, but its validated integrals and decisive continuous comparison remain separate OPEN tasks. This inspection does not introduce a second model or relax those obligations.
