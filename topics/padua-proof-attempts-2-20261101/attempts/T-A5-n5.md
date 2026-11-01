# T-A5-n5 — exact degree-five extension

Rules read again at `44be0080c69495cc6959e3d4c2b602fa73678d76`.
Developer: Codex, allocated `gpt-6.1-sol` xhigh for mathematics; serving metadata is not separately exposed.

## Pre-run scope, time and kill criteria

- Extension starts2026-11-01 10:03UTC within the original A5 timebox09:19–15:19UTC.
- First viability checkpoint around10:23UTC; this is a checkpoint, not an extra stop criterion.
- Stop at a complete independently checked count certificate, a rigorously established counterexample to the measured reference, or15:19UTC.
- Degree-five reference14 interior /9 edge /2 corner /25 total is MEASURED only and is not a truth assumption.
- All degree-three and degree-four code, evidence and theory files are frozen. Writes are confined to this attempt, theory IDs15–19, code/a5_n5* and outputs/a5_n5*. No Git operations.
- Before promotion: written finite reduction, exact/outward arithmetic, all compatible patterns/regions, rigorous roots and exact crease/crossing/boundary coverage, separate verifier of certificate rather than search rerun, actual different-agent producer/checker execution, complete essential evidence under size limits.
- Required new difficulty: degree-five node ambiguity can involve2^20 patterns; prove a physical radial node cone and certify its exact gap before using it to discard any neighbourhood. A zero/uncertified gap cannot justify a discard.

## Status

Degree-five count PROVED under result16; separate A4(d) global argmax PROVED under17. Supporting15,18,19 are PROVED within their stated analytic scopes. Required Claude audit remains PENDING. The original A5 timebox continues for higher degrees.

## Runs needed

Exact node-gap construction and certificate design; adapted degree-five spatial producer; independently implemented certificate verifier; actual independent producer/checker runs. None has yet been executed.

## Gate before mathematics (2026-11-01)

Re-read the current three rule files at44be0080c69495cc6959e3d4c2b602fa73678d76. Repeated the complete496-line IDEAS registry review: headings, IDs, aliases, summaries and obstruction/disposition tables, rereading the MZ obstruction range separately after a displayed truncation. Searched node-cone/radial/Bernstein/exact-maxima/crease/degenerate synonyms across state, tracks and programme/part1/part2 theory. Read full programme IDEA17 and source06, charter IDEA048 contextual entry, old T3 N-node-cone definitions and implementation, and part1 auditF2's boundary limits. Read the full new n4 spatial producer, schema, boundary producer and proof09.

Closest entries: IDEA048 and programme IDEA17/source06 (the same count problem); old N node cone is the predecessor for a physical-coordinate exact version; the new n4 spatial compatible-mask certificate is the retained general method. Applicable obstructions: floating source margins and tolerance coincidence do not certify anything; missing compatible patterns or an unjustified node discard kill completeness; degree-three Hessian-singular exclusions cannot be imported to degreefive. No priority/novelty claim.

CandidateA: exact piecewise-linear physical node gap plus a rigorously bounded radial remainder, integrated as a whole-node-cube leaf predicate. Verdict: proof completion / variant of the old node cone, retaining all boundary directions explicitly. Separation criterion: every breakpoint and feasible direction is covered exactly and the whole certified cube has positive outward radial derivative; a nonpositive gap or failed remainder inequality kills that cube's acceptance. Cheapest decisive test: compute all21 exact node gaps before expensive spatial search. Zero-gap nodes remain unresolved and require a new argument.

CandidateB: n4's complete compatible-sign spatial tree extended to degreefive, using only the new copied n5 modules and the new node predicate. All root/regular-curve/injectivity predicates are degree-independent where their actual inequalities hold. No singular-Hessian maximum is discarded merely for being singular. Boundary arrangement must separately handle any identicallyzero edge cardinal; do not assume the n4 no-zero-edge condition.

## Actual early commands / diagnostics

All Python executions use `PYTHONDONTWRITEBYTECODE=1 python -B` and only new n5 modules. Exact board fieldQ(sqrt3,sqrt5), outward integer dyadics at96bits, no seed and no floating preconditioner.

1. `python -B code/a5_n5_nodes.py --gaps-only --output /tmp/a5-n5-node-gaps.json > /tmp/a5-n5-node-gaps.out 2> /tmp/a5-n5-node-gaps.log` is computing all21 exact feasible-direction gaps. At the10:15UTC progress point, the first13 gaps have strictlypositive rational lower bounds. This is a preliminary computation, not a count or an independently accepted node-cube certificate. During that in-flight diagnostic only the unexecuted cube branch's Poly.diff syntax was corrected; final proof runs will use the frozen corrected source and be independently repeated.
2. Exact edge-restriction diagnostic completed in15.433961s: every cardinal restriction is nonzero on each edge, and multiplicity-one regular-crease coverage holds exactly on every edge. Squarefree edge product degrees are37,18,44,44 in order(axis0,−1),(axis0,+1),(axis1,−1),(axis1,+1). Output:/tmp/a5-n5-edge-diagnostic.json. Final boundary verifier must recheck these identities; this diagnostic is not a count proof.
3. `python -B code/a5_n5_boundary.py --output /tmp/a5-n5-boundary.json > /tmp/a5-n5-boundary.out 2> /tmp/a5-n5-boundary.log` begun after that prerequisite check. Boundary code is a new n5 copy, not an edit to n4. It retains unresolved zero-normal or degenerate tangent cases explicitly.

The new checker implementer `/root/a5_checker` owns only code/a5_checker_n5*, outputs/a5_checker_n5* and its independent-check record. The serialized node/leaf fields are fixed in code/a5_n5_schema.md. An independent mathematical review by `/root/a2_independent_route` found no gap in theory15's supporting implication and the exact node geometry; it did not inspect finite node gaps or counts.

## Viability checkpoint,10:23UTC

The first exact node route succeeded: native algebraic-number coefficient arithmetic produced all21 positive gaps and21 accepted node rectangles in6.217735s. It uses the exact primitive-element identities α=sqrt3+sqrt5, α²=8+2sqrt15, α³=18sqrt3+14sqrt5, checked by the independent verifier's independent field reconstruction. This replaces symbolic parsing, not arithmetic or proof predicates. The slow preliminary symbolic process was stopped after its computed prefix agreed with the new exact output; no count claim depended on that prefix.

Independent node-only verification actually passed all21 rectangles and738 complete direction breakpoints in9.920s. Receipt:outputs/a5_checker_n5_nodes-integration.json. This is local node coverage only, not a maxima-count certificate.

Spatial pilot command:
`python -B code/a5_n5_boxes.py --node-file /tmp/a5-n5-node-cones.json --certificate --boxes 20000 --seconds 180 --depth 32 --full-depth 30 --ambiguity 6 --root-depth 12 --output /tmp/a5-n5-spatial-pilot.json.gz`.
It stopped at the diagnostic180s budget with9849 visited boxes,91421 ordinary leaf-pattern records,88 node-cone leaves,11 accepted interior root witnesses,10 pending paths and0 unresolved depth-limit leaves. The output correctly reports interior_complete:false and complete:false. An independent partial-witness check passed the supplied4920 leaf records without promoting the count. This is a successful viability checkpoint, not an A5 stop.

Full developer command begun:
`python -B code/a5_n5_boxes.py --certificate --boundary --boxes 100000 --seconds 3600 --depth 36 --full-depth 30 --ambiguity 6 --root-depth 12 --output outputs/a5_n5_certificate.json.gz > outputs/a5_n5_producer.jsonl 2> /tmp/a5-n5-final.log`.
All paths are within the assigned topic. Default full execution independently regenerates exact node data instead of loading the pilot node file.

Boundary performance route: direct isolation of an expanded large norm product produced no first-edge completion before replacement. The new exact procedure factors small restricted cardinals, norms the factors, deduplicates monic irreducible QQ factors and isolates each factor, refining until the complete union has strictly separated intervals. Norm multiplicativity proves the same root coverage; final checker still verifies the complete supplied root partition against the full norm. This is an implementation-efficiency change, not a mathematical refutation or a new count assumption. The older diagnostic process was stopped; the revised boundary run is in progress.

Generic certificate correctness is written separately as result18, explicitly extending the degree scope of n4-only result09 and adding the result15 node leaves. Separate global-value schema records EVERY flat/factor leaf value occurrence and all accepted-root values; node leaves are handled by radial ascent plus exact node value1. No strict-list-only global-argmax inference is made.

## Post-merge registry impact

During this run root integrated current main/registry changes. The pre-run N5 gate at44be008 remains its actual provenance. Reviewed the newly inserted15 bivariate obstruction rows (commuting extensions, non-normal sections, computed patterns, finite-precision/block truncation, pivots, downdates, cubature and citation limits) and the changed final-ID/alias context; searched the expanded current registry for node-gap, quadratic-reproduction, radial-cardinal and maxima mechanisms. These rows concern different spectral/recurrence claims and do not change the exact Padua board, reproduction identities, node-cone theorem, compatible-sign certificate or the pinned A5 source. No N5 mathematical dependency or computational input changed, so no dependent run required restarting. A subsequent degree's gate will scan the expanded current registry in full before new work.

## Developer full producer and value evidence completed

The pure-Python developer producer completed with10182 leaves,225656 ordinary mask dispositions,150 node-cone leaves,14 interior roots,9 edge roots and2 corner maxima: total25, complete:true, no pending/unresolved paths. Its gzip is125245bytes, SHA256 a1238d59781733cc0d380dc513a0a642d0e24b985aeb9b90bb7233756273386e. Boundary checked139 sample masks and1815 derivative candidates; all21 node cones and738 breakpoints are embedded.

Developer global producer also exited0. Output:a5_n5_global.json, SHA25657a7c9c12667b5d441cea4fc60a68563cc1accc8d8adc8ca41ccd339fa16f17d. It bounds all4 flat/factor leaf occurrences, all14 interior values and all9 edge values below19/4, and verifies common corner value(38+8sqrt3+10sqrt5)/15>19/4 at(−1,±1). The source modules remain frozen. A different agent's flint-backed complete producer has the same mathematical summary and its own artifact/global pair; actual full checker and controls have passed there. Final developer-pair verification is running before count/global status promotion.


## Degree-five done criterion met

The different-agent full producer/global run and its own full checker passed. The same agent then actually checked the developer pair, exiting0 in257.679985s. The checker implementer separately passed the full independent pair. All31 controls passed:27 negative witnesses rejected and4 positive accepted. Every code pin remained fixed. The independent receipt independent-execution-a5-n5.md records exact commands, environment/backend, hashes and semantic comparison: decoded certificates differ only in phase timers, and global files only in the raw count-artifact bindings.

Final degree-five claims are now PROVED:25 strict maxima =14 interior +9 edge +2 corner, and exact global maximum(38+8sqrt3+10sqrt5)/15 attained only at(−1,±1). The complete tree has10182 leaves,225656 ordinary mask records and150 uniform node-cone leaves; all21 nodes/738 breakpoints,139 edge masks/1815 derivative candidates and all four corners are verified. Primary Table3 agrees atn=5. No n=6,7,8 claim is inferred.

Administrative rule changes were read at4bd1d65ad36ddded9bf4799c0557d4a6bb83e764: numbered handoffs belong only to the orchestrator, and fresh final-ID reservation rules do not authorise worker allocations. They change no frozen mathematical source. Root owns mainT-A5/LOG/plan/proposals/manifest/Git/handoff. No worker handoff or Git mutation was performed. The new degree-seven extension begins only after this N5 done boundary; all N5 source and evidence are frozen.
