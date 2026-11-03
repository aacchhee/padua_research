# R3 comparison candidates — retained bounded variants

2026-11-03. Rules/input `8a1f394739293953e1566fd24a0a193cc78ff26f`, base `440d107`; Codex mathematics assigned gpt-6-astra ultra. G6 code by the parent's gpt-6.1-sol medium gates worker. Gate, precise conventions and original pre-execution criteria: [attempt](../attempts/r3-r4-comparison.md).

## IDEA?argmax-effective-codex-03-ec — Extended whole-cell E-C gate

Aliases: IDEA-324 continuation; centreward complementary vertical-edge cells; G6.

- Question / scope: for every degree n and every eligible pair in IDEA-324, is the source whole-cell supremum no larger than the target's?
- Mechanism and hypotheses: compare closed complementary cells [k-1,k+1] on each vertical edge, excluding endpoint-touching cells, under a parity-preserving step two toward (n+1)/2; maximizing phases may differ.
- Closest registry entries (read in full): IDEA-324, IDEA-318 and IDEA-303–305; full original/final E-C records and PD-T231.
- Separation criterion: this is continuation of the same mathematical candidate, with the newly authorized n13…60 gate. The computational refinement searches every local maximum visible on the fixed grid. It is not a new all-n mechanism or a novelty claim.
- Literature baseline and search limitations: literature INDEX read; no 1-D theorem imported. G8 remains required before transferring one.
- Applicable obstructions and hypotheses escaped: PD-N080 refutes common-phase E-P; E-C compares suprema at independently optimized phases. PD-N078/081 use different orderings and do not refute E-C. A finite positive screen cannot upper-bound an entire source cell.
- Novelty gate verdict: **variant with difference** as an authorized finite-range extension; mathematically the same retained IDEA-324.
- Cheapest decisive test: 65-point closed-cell grids and refinement of all local grid maxima for n13…60, followed by rigorous source upper bounds for any observed reversal.
- Kill criterion written before testing: float target-minus-source below -1e-6 triggers exact investigation. G6 kills all-n E-C only after an exact reversed whole-cell comparison.
- Test discriminability: a missed source or target maximum can reverse a numerical comparison. Only exact whole-source upper bounds plus target witness lower bounds certify a direction.
- Actual test results: the final full run reports 1536 comparisons, no reversal, and minimum target-minus-source 0.0027806941162857868 at n=60. A different agent replayed 96 comparisons at n=13,17,24,60 with exact float-row agreement. Three further whole-cell comparisons at n=13,17,24 were certified with actual different-agent checker acceptance; their rational margins exceed 1/20,1/40,1/100. The measured record and separate exact theorem carry final hashes.
- Disposition: **retained / OPEN**; no G6 kill. Positive finite evidence supplies no all-degree proof or effective threshold.
- Disposition reason: no numerical reversal in the executed finite scope; analytic control of different maximizing phases remains missing.
- Canonical theory / negative-result ID: [PD-T?argmax-effective-codex-03](../theory/argmax-effective-codex-03-comparison-screen.md), MEASURED; [PD-T?argmax-effective-codex-03-spots](../theory/argmax-effective-codex-03-exact-edge-spots.md), PROVED finite cases. No negative record for passing a screen.
- Topic / audit / history: the new handoff explicitly authorizes this larger screen despite the prior campaign's stop after n7/12. Original E-C and E-P dispositions remain unchanged. Claude audit pending.

## IDEA?argmax-effective-codex-03-strip — First-strip domination by the matching vertical-edge cell

Aliases: I-B0; rectangle-to-edge supremum comparison; bounded interior-to-boundary gate.

- Question / scope: for each eligible vertical edge cell, does its entire first inward mesh rectangle have supremum equal to the boundary cell's supremum?
- Mechanism and hypotheses: fix the rectangle and corresponding edge interval before testing; both use the same qy interval, the rectangle has inward qx width one. Equality is the desired direction because the edge is contained in the rectangle.
- Closest registry entries (read in full): IDEA-206/318, IDEA-324 and PD-T207's measured band maxima. The older PD-T207 offset bands optimize the whole other coordinate and are not this matched rectangle comparison.
- Separation criterion: pointwise domination by the *supremum* of an explicitly matched edge cell, without demanding equal phase or all-cell rhombus monotonicity. A rigorous interior witness above a whole-edge-cell upper bound refutes this specific map.
- Literature baseline and search limitations: no source theorem is transferred and no historical novelty asserted.
- Applicable obstructions: PD-N080 precludes simply assuming equal-phase translation. Artificial rectangle boundaries can host maxima; all grid endpoints and bounded searches are retained. Coarse sign stability is not assumed.
- Novelty gate verdict: **variant with difference**: a frozen geometric map and limited strip domain operationalize the brief's unspecified interior-to-boundary suggestion.
- Cheapest decisive test: the attempt's 9 by17 grid plus bounded local searches and edge optimizer point.
- Kill criterion written before testing: rectangle-minus-edge above1e-6 triggers exact investigation; only certified opposite bounds refute the mathematical comparison.
- Test discriminability: the boundary supplies a lower bound for the rectangle maximum, so excess near floating precision is expected when both found maxima lie on that boundary. Absence of a found interior competitor is not a global bound.
- Actual test results: final run covered 182 rectangles at n=13,17,24,32,48,60; maximum reported excess 3.412381488487881e-12, no threshold crossing and no optimizer nonconvergence. The parent narrowed this run to representative degrees for the bounded-round budget; the original larger intended scope remains in the attempt's dated history.
- Disposition: **retained / OPEN**, representative measurement only; no statement for every degree13…60, other strips, horizontal edges or all interior cells.
- Disposition reason: the specified finite search found no reversal. Resume with a rigorous rectangle bound/comparison or explicit map, not by treating these samples as a proof.
- Canonical theory / negative-result ID: `PD-T?argmax-effective-codex-03`, measured screen record; no PD-N.
- Topic / audit / history: precise rectangle geometry registered before testing; parent-directed degree reduction disclosed afterwards. No retrospective enlargement of the measurements.
