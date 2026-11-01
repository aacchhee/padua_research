# A5 degree-five spatial certificate — draft v1

No degree-five count is claimed until the complete independent verification passes.
Use only new n5 modules. The n3/n4 files are frozen.

## Exact board and arithmetic

Nodes are `(cos(pi*j/5),cos(pi*k/6))`, j=0,…,5,k=0,…,6,j+k even, in lexicographic order; N=21. Total-degree≤5 monomials are ordered by degree then descending x exponent. Coefficients lie in Q(sqrt3,sqrt5), encoded as four rational strings in basis1,sqrt3,sqrt5,sqrt15. Construct cardinals by exact Vandermonde inversion; verify interpolation and partition of unity. Outward fixed-dyadic arithmetic uses S=2^96 and verified square-root brackets for3,5,15. Polynomial powers now extend through degree5. The exact integer coefficient-vector mask reconstruction follows n4's scheme with21 cardinals and21 monomials.

## Spatial tree and ordinary predicates

The complete prefix-free binary leaf partition, widest-side splits and centered/natural interval intersection follow the explicit method in n4 proof09, now for degreefive. `format=a5-n5-spatial-v1`, n=5, precision96. Compatible signs are derived from cardinal intervals; ambiguous bits permit both signs. An ordinary leaf has exactly one ordered disposition per compatible21-bit mask. The degree-independent predicates are `flat`, `gradient`, strict-positive-curvature/negative-determinant `hessian`, exact `regular_point`, regular common-gradient-curve `factor`, and accepted root with whole-hull gradient injectivity. Root witnesses require exact Krawczyk/contraction, strict negative definiteness and strict cardinal signs. Singular Hessians are never excluded merely for being singular.

## New node-cone records

Top field `node_cones` lists exact node records. Each contains:

- `index`: cardinal/node index0,…,20;
- `node`: exact coordinate FIELD vectors (four rational strings each), checked against the reconstructed board;
- `segments`: EVERY feasible portion of each side of the direction unit square. A record has `axis` (fixed coordinate0/1), `fixed` (−1/+1), rational `bounds` for the other coordinate, and sorted `breaks` as FIELD vectors. Include both endpoints and every root of `fixed*g_i[axis]+t*g_i[1-axis]=0` in bounds for i≠index, ignoring identicallyzero forms. Verify the complete list exactly; extra distinct breakpoints are permitted only if verified in range. Feasibility follows the active faces at the exact node.
- `gap_lower`: rational m. Verify at every breakpoint that `gradL_index·d + sum_other abs(gradLi·d) >= m`, using exact field signs or outward inclusion. Piecewise affinity proves the bound on the entire feasible direction set.
- `status`: `accepted`, `zero_gap` or `no_cube`. Only accepted records may be referenced by a leaf. Zero-gap and failed-cube records carry no discard authority.

An accepted record also contains rational rectangle `B`, rational `R`, rational `H_i` list and sum `H`, and rational `Lq_lower`:

1. Exact node lies strictly inside B.
2. B meets no square face except those that contain the exact node. For an interior coordinate B lies strictly in(−1,1); at coordinate−1 require B_upper<1, and at+1 require B_lower>−1.
3. R≥sup_{w∈B}||w−z||∞ and R>0.
4. The interval evaluation of L_index(B) has lower endpoint at least `Lq_lower`>0.
5. Each H_i bounds `abs(Hxx_i)+2abs(Hxy_i)+abs(Hyy_i)` on B, and H is their sum (or a greater verified bound).
6. m>0 and R*H<m (producer currently seeks the stronger margin R*H<m/2).

All gradients at the exact node and every Hessian polynomial are independently reconstructed. The theorem15 integral argument then excludes strict maxima on int(B)∩square, including exact zeros and crossings.

A node leaf is `{"path":binarypath,"node_cone":index}` with no ordinary `patterns` list. Its rational boxQ must lie STRICTLY inside the referenced B in both coordinates. This strictness ensures a forward radial step remains in B; the face condition ensures it remains feasible in the square. It discards the WHOLE leaf, avoiding exponential mask enumeration only by a proved uniform predicate. A node on the leaf is excluded by exact λ(node)=1 and λ≥1. Node-cone leaves count no maximum.

No cone may be accepted from a numerical gradient, sampled direction set, unverified breakpoint omission or zero gap. Every uncovered region must still receive ordinary compatible-mask dispositions or remain unresolved.

## Boundary pending extension

The n4 edge-arrangement method may be used only after verifying its hypotheses for n5. Identicallyzero restricted cardinals must be excluded from the edge product and their actual one-sided signs determined by exact normal factors; these factors need not be assumed simple without verification. Multiplicity-one crease coverage, complete norm-root partitions, sign-gap samples and all derivative-root dispositions remain mandatory. The final boundary schema will record any needed extension before accepting it.

Boundary hypotheses have now been checked exactly in a diagnostic: all21 restricted cardinals are nonzero on every edge; multiplicity-one crease coverage holds on all four edges. Therefore use the complete n4 boundary serialization unchanged, with N=21 and field basis1,sqrt3,sqrt5,sqrt15: `E_norm_intervals`, gap`samples`, exact`sample_masks`, one pattern per sample mask, reduced derivative `Dr=sf(D)/gcd(sf(D),E)`, all`Dr_norm_intervals` and point dispositions. The exact hypotheses are checked again by the final independent verifier. Degenerate tangent and zero-normal candidates are never silently discarded.

Summary accounting: one node-cone leaf contributes1 to`leaf_counts.node_cone` and`stats.node_cone`;`node_leaves` equals that count. `leaf_pattern_records` counts ordinary mask dispositions only, excluding node-cone leaves. The top`node_cones` list always contains all21 node records in index order. No accepted node cone implies that all nodes were covered; every uncovered point still requires ordinary complete-tree coverage.

## Additional A4(d) global-value evidence

Separate `a5-n5-global-v1` object references the compressed count certificate by SHA256 and supplies rational cut19/4, exact`corner_value` FIELD, `bounded_codes`=["flat","factor"], `exception_leaf_occurrences`, `exception_upper`, `node_value`="1", `edge_flat_patterns`, and complete `interior_values`/`edge_values` rows{id,enclosure}. Reconstruct and bound P_s over EVERY ordinary leaf-pattern occurrence whose code is flat or factor. Their interval upper endpoints must be no greater than supplied exception_upper<cut; match the exact occurrence count. Node-cone leaves contain no local maxima except possibly the node itself, of value1, so do not enumerate their masks for this value check. Every accepted root value enclosure lies strictly below cut. Every constant edge restriction is checked to be±1. Exact cardinal corner evaluations at(−1,−1),(−1,1) agree with corner_value and its verified lower bound exceeds cut>1; the other corners are exact nodes of value1.

Global proof: a non-strict global maximum in an ordinary interior leaf still forces stationarity and negative semidefinite Hessian of every active P_s. Gradient/strict-curvature/regular-point predicates exclude it (nodes have value1); a root predicate identifies the certified strict maximum via whole-hull injectivity. Flat/factor occurrences are excluded from global maximality by their separately verified value bound<cut. Node-cone leaves have radial ascent except at value1 nodes. On edges, nonconstant active q_s global maxima are covered by derivative roots with the same complete exclusions; constant q_s=±1 cannot attain the corner lower bound. Thus all global maxima occur in the certified strict list/corners. This treats non-strict plateaus separately rather than inferring global maximality from a strict-count list alone.
