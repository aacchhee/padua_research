# Requested candidate-specific prior-art screen

Date2026-10-31; rules SHA e949ef06895acd5463cdf8df7e0e5f795218f70f. Literature-only handoff, no acceptance. Pattern descriptions supplied by the orchestrator, not independently re-enumerated in this pass. Exact follow-up queries are batches8–11 in [search-log.md](search-log.md).

## 3D cyclic6 sum fiber

Supplied family: 0≤i≤n,0≤j≤n+1,0≤k≤n+2, with i+j+k≡c mod6. The exact admissible n,c and cardinality identities belong to C0; finite ranks belong to C3.

Closest inspected node-pattern predecessors are [Dencker–Erb2017](records/dencker-erb-2017.md), its [general-parameter sequel](records/dencker-erb-unifying-2017.md), and [De Marchi–Vianello–Xu2009](records/demarchi-vianello-xu-2009.md). Their displayed 3D selections use common-parity blocks rather than a single sum class mod6. Exact space comparison matters: LC interpolation uses a spectral space; DMVXu uses an oversampled total-degree hyperinterpolant. [Bos–De Marchi–Vianello](records/bos-demarchi-vianello-2017.md) instead extracts interpolation nodes from a larger lattice.

Potential structural predecessor: [Fourier non-aliasing](records/sorevik-nome-2016.md), with a chosen frequency space on a group lattice. Its theorem hypotheses do not include arbitrary algebraic axis labels or the campaign's fixed total-degree monomial simplex. [Cools–Poppe](records/cools-poppe-2011.md) exact definitions remain pending-reference, so no claim of difference from every Chebyshev lattice is licensed.

Bounded verdict: no exact matching full-total-degree, arbitrary-axis cyclic6 factorization theorem was identified in the searches/sections read. **Novelty UNVERIFIED.** A distinction survives this reading only as a question about the exact mod6 incidence and the structural theorem eventually proved. Kill the claimed distinction if a source gives the same node selection up to axis relabelling and the same polynomial space/hypotheses, or if the proposed criterion reduces to an already existing lattice-character theorem. Merely finding a nonzero determinant at finitely many specializations is not the requested new property(b) or(c).

## 2D mod4 adjacent-residue union

Supplied family: 0≤i≤n,0≤j≤n+1, with i+j mod4∈{0,1}. This condition is recorded as supplied; counting, relabelling equivalence and factorization are not proved here.

[Harris2018](records/harris-2018.md), [Harris–Simanek2021](records/harris-simanek-2021.md), [Cao–Ghimire–Wang2022](records/cao-ghimire-wang-2022.md), and the inspected [Dencker–Erb general index formula](records/dencker-erb-unifying-2017.md) select mod2 parity blocks. Arbitrary rectangle excess in those papers is not an arbitrary modulus. A high Lissajous frequency is likewise different data from the residue condition in the index lattice.

The closest broader structural test is [Floater's union of two interlaced rectangles](records/floater-2017.md). The inspected slides assume that geometry and an explicitly associated lower polynomial space. Source29 does not itself establish that the supplied mod4 union fits those hypotheses. Before claiming a distinction, check allowable row/column permutations, whether the selected set is such a two-grid union, whether interlacing is retained, and whether its source space is exactly Π_n². Exact journal fulltext remains pending-reference. The [determinant papers](records/demarchi-usevich-2014.md) already factor triangular function/polynomial-matrix families; a new determinant formula must identify the additional structure beyond that framework.

Bounded verdict: no exact matching theorem identified. **Novelty UNVERIFIED.** Kill the claimed distinction if the set/space reduce to the known parity or two-interlaced-grid cases, or the determinant is an instance of the existing triangular-matrix factorization. No source inspected supplies a universal absence result for index-k>2 patterns. All three campaign properties must still be reported separately.

## C1 addendum: odd-degree and shifted-phase follow-up

The orchestrator reported full ranks at small odd n for C={0,1}, finite sampled Lebesgue values, and shifted sets C={1,2}/{3,0} as possible escapes from an even-degree symmetry obstruction. These are inputs to this literature check, not computations rerun here. Restrict all reports of stability to the developers' measured n, axes, sample sets and phase. Neither polylogarithmic growth nor universal odd-degree Chebyshev unisolvence follows from those samples.

Two apparent naming matches were inspected and separated:

- [Caliari–De Marchi–Vianello2008](records/caliari-demarchi-vianello-2008.md), §2 eq4b–7b, lists all four Padua families at odd degree. Each family has two Cartesian parity blocks; “four families” does not mean a four-block index pattern.
- [Erb–Kaethner–Ahlborg–Buzug2016](records/erb-kaethner-ahlborg-buzug-2016.md), eq6–9, starts with signed sine/Lobatto parametrizations but explicitly rearranges them into two opposite-parity tensor blocks. Its Theorem3 is in a specially chosen Chebyshev spectral space. Quarter phases in the curve are not automatically quarter-periodic sums in the finite index box.

The supplied mod4 pattern can be written as four row-residue Cartesian blocks: for each r mod4, use X_r times the union of the two Y-residue classes p−r and p+1−r. That decomposition merely restates its definition; it is not a new structural interpolation theorem. No inspected source supplied a general theorem identifying this four-row-type construction with full Π_n² interpolation. The developers' supplied reduced-incidence comparison (C8 at n=3; three different size-two row neighborhoods for a shifted n=2 case) is useful against axis-permutation equivalence to two disjoint parity blocks, but was not independently recomputed by this literature pass.

Keep three notions of equivalence separate: independent permutations of the existing axis labels, reflection/coordinate swap of the actual square, and a nonlinear change of coordinates. Only an explicitly justified map preserving the target polynomial space can transfer unisolvence/stability. A generic relabelling may preserve the incidence graph while changing the special Chebyshev node set. A nonlinear Chebyshev substitution may change total degree or produce a different spectral space. The2017 general LC formulas and the inspected2016 nondegenerate definitions therefore do not settle the odd subsequence or its shifts just by nomenclature.

Bounded result after queries42–67: no exact prior-art identification found. **Novelty remains UNVERIFIED.** The remaining priority screen needs the eventual exact theorem (specific odd/even degree range, phase, field, axes, Π_n² and determinant/stability conclusion). Floater's journal fulltext and Cools–Poppe detailed definitions remain pending-reference; neither gap is an absence theorem. No third substantive mathematical direction was launched.
