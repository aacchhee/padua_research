# Bounded comparison for lattice-subset interpolation

LITERATURE only. Rules SHA e949ef06895acd5463cdf8df7e0e5f795218f70f; 2026-10-31. Exact source coverage and gaps are in [search-log.md](search-log.md) and linked records. No theorem is inherited as local proof and no novelty/acceptance decision is made.

## Keep the three constructions separate

[Lower-set interpolation](records/lower-sets-2015.md) is coordinatewise downward closure of selected grid indices, with the matching monomial space. [Natural lattices](records/natural-lattices-2013.md) are intersections of hyperplanes in general position. GC sets require fundamental polynomials factored into affine forms. These are related interpolation traditions, not interchangeable names. Exact Biermann/Gasca–Maeztu historical credits remain UNVERIFIED; the available modern primary formulas already establish that ordinary total-degree unisolvent sets are not the open target.

## Campaign properties (a), (b), (c)

“Unverified” refers to this reading; it does not claim absence in the source or wider literature.

| Family | (a) Periodic/character index pattern | Interpolation space / axis hypotheses | (b) Structural evidence inspected | (c) Lebesgue evidence inspected |
| --- | --- | --- | --- | --- |
| Coordinate lower set | Downward closure; periodicity is not the defining property | P_L; distinct coordinate lists | Newton construction, source11 | No general asymptotic checked |
| Chung–Yao natural lattice | Hyperplane intersections | Full total degree, real general position | Product affine fundamental functions, source12 | Unverified |
| Padua | Parity grid | Full total degree; special Lobatto axes | Kernel/ideal formulas, sources13–14; determinant predecessors25–26 | O(log²n), source13; sharper leading constant unverified |
| Xu / MP variants | Actual nodes must be specified; inspected formulas use parity | Xu: associated subspace; MP name has multiple meanings | Selected degree modes/kernel, sources15–16 | Unverified here |
| Harris / Harris–Simanek | Mod2 checkerboard | Decreasing real axes; σ=1 gives full degree-m space | Alternation and kernel, sources17–18 | Unverified for arbitrary axes |
| Cao–Ghimire–Wang | Mod2, arbitrary rectangle excess | Degree n+floor(σ/2); quotient uniqueness | Explicit Lagrange construction, source19 | Unverified |
| Dencker–Erb JAT2017 | Union of two common-parity tensor blocks | Chebyshev axes; spectral Γ, not automatically total-degree simplex | Discrete orthogonality, source20 | Separate theorem not checked |
| Dencker–Erb unifying2017 | Shifted common-parity blocks, general lengths | Spectral representative/symmetrized spaces | Interpolation theorems and FFT setup, source21 | Unverified here |
| Bos–De Marchi–Vianello2017 | Curve-sampled Chebyshev lattice, then extraction | Extracted Fekete/Leja-type full-total-degree interpolation | WAM/extraction route, source22 | Reported finite numerical values, not independently rerun |
| De Marchi–Vianello–Xu2009 | Two complementary parity tensor blocks | Hyperinterpolation has more nodes than dimΠ_n³ | Explicit source distinction, source23 | Interpolation Lebesgue conclusion inapplicable |
| Cools–Poppe2011 | Lattice framework; precise definitions pending | Weighted cubature/hyperinterpolation abstract | Detailed original fulltext UNVERIFIED/pending-reference, source24 | Unverified |
| Floater2017 | Two interlaced rectangles | Real interlacing; associated lower polynomial space | Divided-difference determinant criterion in slides, source29 | Unverified |
| Sørevik–Nome2016 | Lattice/Fourier characters | Periodic trigonometric space matching spectral residues | Non-aliasing criterion, source30 | General log^d bound conjectural in this source |

## Scope of open-problem wording

[De Marchi2022](records/demarchi-2022.md), §3.3(1), discusses higher-dimensional Padua points. It does not claim that arbitrary 3D unisolvent sets are unknown. [Xu2407.09903](records/xu-2024.md) concerns two-variable minimal cubature. Positive continuous cubature and its node lower bounds are not requirements for this campaign's interpolation target.

The decisive comparison for a survivor is the complete tuple (index set, box lengths, polynomial space, axis hypotheses, field, determinant criterion, and stability guarantee). Equality of one component, or a new name for it, does not settle equivalence or novelty. The [candidate-specific screen](candidate-screen.md) records the two requested next comparisons.
