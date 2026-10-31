# Lattice-unisolvence literature search and inspection log

Date: 2026-10-31. Reader: Codex literature developer; assigned gpt-6.1-sol high, runtime model/effort unexposed. Rules read at full SHA e949ef06895acd5463cdf8df7e0e5f795218f70f. Scope: sourced baseline and bounded prior-art comparisons only; no candidate launch, acceptance or exhaustive priority verdict. Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, literature/INDEX.md, topic REQUEST.md/plan.md and frozen baseline. Existing LIT-001–041 retain their recorded coverage.

## Access mechanism and limits

Used the native `search_service_web_run` search/open/find/click tools. Read `/etc/codex/network-policy.json`; shell networking was not used, no proxy/allowlist settings changed, and no denial was bypassed. Source PDFs were remotely inspected through the native reader, not downloaded or committed. Tool page numbering is zero-based; record locators are one-based PDF pages or printed journal pages as explicitly indicated. A successful fulltext opening is not a complete reading. No record in this pass claims a complete fulltext reading, independent theorem proof, numerical rerun, or journal/preprint textual identity. Short paraphrases only are retained.

## Exact queries executed

Each line is an actual query, in execution order within each batch. Queries with broad or irrelevant results do not imply an absence theorem.

Batch 1:

- `Dencker Erb 2017 multivariate polynomial interpolation Lissajous Chebyshev nodes pdf`
- `Bos De Marchi Vianello 2017 trivariate Lissajous total degree polynomial interpolation pdf`
- `De Marchi 2022 Constr Math Anal 5 1 Padua points d 3`
- `Xu 2407.09903`

Batch 2:

- `Biermann interpolation lower sets multivariate Chung Yao natural lattices 1977 Gasca Maeztu 1982 Carnicer Gasca`
- `Harris 2015 2018 bivariate polynomial interpolation Morrow Patterson Xu points alternation`
- `Cools Poppe Chebyshev lattices 2011 pdf`
- `De Marchi Vianello Xu 2009 cube hyperinterpolation nodes pdf`

Batch 3:

- `"Cao" "Ghimire" "Wang" "2022" interpolation rectangular pdf`
- `"Chebyshev lattices, a unifying" pdf`
- `"Biermann" "lower" interpolation polynomial`
- `"Chung" "Yao" "natural lattice" hyperplanes interpolation pdf`

Batch 4:

- `polynomial interpolation Cartesian grid congruence modulo 3 checkerboard roots unity determinant`
- `"Bivariate Lagrange interpolation at the checkerboard nodes" pdf Wang`
- `"Biermann interpolation" "lower" pdf`
- `"Chebyshev lattices" "0300" pdf`

Batch 5:

- `"Padua points and fake nodes" pdf`
- `"New cubature formulae" "Chebyshev" "3D" nodes`
- `"Biermann" "1887" interpolation`
- `"Chebyshev points of two variables" Xu 1996 pdf`

Batch 6:

- `"lower sets" interpolation "Carnicer" Gasca pdf`
- `"Biermann interpolation" multivariate polynomial primary`

Batch 7:

- `Bos De Marchi Vianello Xu 2007 bivariate Lagrange Padua ideal theory arxiv`
- `Bos Caliari De Marchi Vianello Xu 2006 generating curve approach pdf`
- `Morrow Patterson 1978 Construction algebraic cubature rules polynomial ideal theory pdf`

## Access and reading register

The record links give citations, URLs, versions, exact inspected excerpts and remaining gaps. Provisional numbers11–28 are disjoint from frozen baseline01–10.

| Provisional suffix | Source and access locator | Actual reading coverage / access outcome |
| --- | --- | --- |
| 11 | [Carnicer–Godés2015](records/lower-sets-2015.md) | Fulltext excerpts: introduction, lower-set theorem, total-degree example, experiment and references |
| 12 | [Calvi–Phung2013; original Chung–Yao1977](records/natural-lattices-2013.md) | Modern fulltext §2 theorem/formula; original publisher metadata/abstract only, subscription access |
| 13 | [Padua generating curve2006](records/padua-2006.md) | Author fulltext theorem/lemma excerpts |
| 14 | [Padua ideal2007](records/padua-ideal-2007.md) | arXivv1 theorem/kernel/cubature excerpts; alternate math.unipd.it/users/~demarchi/papers/paperIdeal.pdf inaccessible |
| 15 | [Xu1996](records/xu-1996.md) | Author fulltext abstract, node/count definitions and interpolation-space/kernel excerpts |
| 16 | [Harris2015](records/harris-2015.md) | Author fulltext abstract/introduction and MP cardinality/classification |
| 17 | [Harris2018](records/harris-2018.md) | Author fulltext alternation theorem and discrete-weight/application excerpts |
| 18 | [Harris–Simanek2021](records/harris-simanek-2021.md) | Author DRAFT theorem/corollary/conjecture and uniqueness discussion excerpts |
| 19 | [Cao–Ghimire–Wang2022](records/cao-ghimire-wang-2022.md) | Publisher offprint theorem/quotient/conjecture-resolution excerpts |
| 20 | [Dencker–Erb JAT2017](records/dencker-erb-2017.md) | arXivv2 node, cardinality, spectral-space and interpolation excerpts |
| 21 | [Dencker–Erb unifying2017](records/dencker-erb-unifying-2017.md) | arXivv1 general-parity and spectral-interpolation theorem excerpts |
| 22 | [Bos–De Marchi–Vianello2017](records/bos-demarchi-vianello-2017.md) | arXivv1 introduction and numerical Lebesgue paragraph excerpts |
| 23 | [De Marchi–Vianello–Xu2009](records/demarchi-vianello-xu-2009.md) | arXiv abstract and §3 node/count/noninterpolation excerpts |
| 24 | [Cools–Poppe2011](records/cools-poppe-2011.md) | Publisher abstract/metadata only; detailed imported claims UNVERIFIED, pending-reference |
| 25 | [De Marchi–Usevich2014](records/demarchi-usevich-2014.md) | arXivv3 proposition/application excerpts |
| 26 | [de Camargo–De Marchi2015](records/camargo-demarchi-2015.md) | Primary theorem/proof-opening excerpts |
| 27 | [De Marchi2022](records/demarchi-2022.md) | Primary §3.1–3.3 excerpts; initial PDF timeout superseded by successful publisher PDF link |
| 28 | [Xu2407.09903v1](records/xu-2024.md) | Primary abstract plus HTML theorem excerpts; not a 3D interpolation paper |

Other access attempts: `https://arxiv.org/html/1511.04564` returned406; its PDF succeeded. `https://www.fernuni-hagen.de/angewandte-mathematik/docs/rrw/2016/denckererb.pdf` opened but is only a one-page conference abstract, not the JAT fulltext. `https://www.research.unipd.it/handle/11577/3421369` returned403; publisher landing/PDF succeeded. `https://doi.org/10.1007/s10543-010-0300-6` was inaccessible through the tool, direct Springer landing succeeded and showed subscription preview. `https://epubs.siam.org/doi/abs/10.1137/0715062` (Morrow–Patterson1978) timed out; DOI/metadata known, original statement UNVERIFIED. `https://www.texmacs.org/joris/amp/amp.pdf` was an unrelated van der Hoeven–Lecerf2020 paper, not the intended lower-set source; discarded with no imported claim. The CAA bibliography `https://www.math.unipd.it/~marcov/CAApadua.html` and Harris bibliography `https://www.ms.uky.edu/~larry/pubs.pdf.html` were opened for source discovery.

## Bounded findings and pending references

No matching index-k>2 arbitrary-axis full-total-degree factorization theorem was identified by these queries. This is a coverage statement only. The primary records show that large frequency vectors and arbitrary rectangular excess still occur in constructions with mod2 index selection; neither parameter establishes an index-k>2 novelty distinction. Any surviving candidate needs a targeted search on its exact pattern, spectral space, field and determinant mechanism before acceptance.

Historical originals still pending: Biermann (precise original source/year); Gasca–Maeztu1982, DOI10.1007/BF01399308; Carnicer–Gasca and Carnicer–Gasca–Sauer2006; Chung–Yao1977 fulltext; Morrow–Patterson1978 fulltext. Modern primary lower-set and natural-lattice formulas suffice to distinguish the constructions without assigning those unverified historical credits. Cools–Poppe2011 detailed definitions and theorem claims remain pending-reference. None of these gaps stops independent interpolation exploration; none licenses a priority claim.

## Candidate-specific follow-up requested by orchestrator

Targets: 3D sum fibers i+j+k≡c mod6 on lengths(n+1,n+2,n+3); 2D union i+j mod4∈{0,1} on lengths(n+1,n+2). No new mathematical direction launched. Exact additional queries:

Batch 8:

- `polynomial interpolation grid "modulo 6" three variables`
- `trivariate interpolation lattice "congruence" determinant`
- `polynomial interpolation "modulo 4" checkerboard`
- `interpolation grid "block" "parity" Lagrange`

Batch 9:

- `"Padua" "modulo" interpolation "3"`
- `"polynomial interpolation" "congruence" "Chebyshev"`
- `"polynomial interpolation" "four" "checkerboard"`
- `"trivariate" "interpolation" "lattice" "six"`

Batch 10:

- `trivariate polynomial interpolation periodic subsets Cartesian grids Chebyshev lattices`
- `bivariate Lagrange interpolation union four rectangular grids determinant`
- `polynomial interpolation checkerboard higher modulus roots of unity axis factorization`
- `total degree interpolation rank one lattice three dimensional`

Batch 11:

- `Floater 2017 polynomial interpolation interlacing rectangular grids pdf`
- `"Trigonometric interpolation on lattice grids" author pdf`
- `"bivariate" "interpolation" "residue classes"`
- `"trivariate" "interpolation" "congruences"`

The exact-modulus searches were dominated by unrelated lattice/congruence algebra, coding and spline results; those are not evidential predecessors. The less literal searches returned the already inspected LC/Bos/Harris families, Floater, and a trigonometric-lattice source. Added [Floater source29](records/floater-2017.md) (journal direct403, primary slides inspected) and [Sørevik–Nome source30](records/sorevik-nome-2016.md) (d-nb PDF429; primary Springer open-access HTML succeeds). No exact matching candidate theorem identified; this bounded screen does not prove novelty. See [candidate screen](candidate-screen.md).

## C1 odd-degree and shifted-phase identification follow-up

The orchestrator requested this bounded literature follow-up after reporting small odd-degree Chebyshev experiments and shifted phases. Those experiments were not rerun by this literature developer and retain their mathematical developers' own scope/status. Query numbering continues the41 queries above; numbers here are query IDs, separate from provisional source IDs.

42. `"polynomial interpolation" "modulo 4"`
43. `"Chebyshev" interpolation "four grids"`
44. `"Lagrange" interpolation "quarter" Chebyshev`
45. `"interpolation" "shifted parity" nodes`
46. `bivariate total degree interpolation Chebyshev Lobatto nodes odd degree union grids`
47. `Padua points generalized checkerboard four rectangular grids interpolation`
48. `Lissajous Chebyshev interpolation shifted nodes modulo four`
49. `quarter periodic bivariate polynomial interpolation nodes`
50. `bivariate polynomial interpolation unions rectangular grids periodic patterns nodes`
51. `"Chebyshev" "mod 4" "interpolation"`
52. `"Padua" "mod 4"`
53. `"interpolation" "four rectangular grids"`
54. `"bivariate interpolation" "diagonal" Chebyshev nodes`
55. `"Padua-like" "four" grids`
56. `"Chebyshev" interpolation "stripes"`
57. `"polynomial interpolation" "periodic pattern"`
58. `"Chebyshev" "quarter-periodic"`
59. `"polynomial interpolation" "union of four"`
60. `"Lissajous" "modulo 4"`
61. `"Padua" "odd" "antipodal" interpolation`
62. `"Bivariate Lagrange interpolation" "non-degenerate" Lissajous arxiv`
63. `Chebyshev interpolation nodes diagonal modulo4 Padua variants`
64. `"polynomial interpolation" "multi-grid" total degree`
65. `"Lagrange interpolation" "union" "four" Chebyshev`
66. `"Caliari" "Computational aspects" "284" 2008`
67. `"Erb" "Kaethner" "Ahlborg" "Buzug" "124" "2016" interpolation`

Primary follow-up reading: [Caliari–De Marchi–Vianello2008, source31](records/caliari-demarchi-vianello-2008.md), all four odd/even Padua definitions and orientation changes; [Erb–Kaethner–Ahlborg–Buzug2016, source32](records/erb-kaethner-ahlborg-buzug-2016.md), nondegenerate signed-node simplification and interpolation space. Both reduce their displayed geometric node descriptions to two Cartesian parity blocks. No complete-paper reading claimed.

Access details: `https://www.math.unipd.it/~marcov/pdf/PDcomp.pdf` succeeded; its direct journal page `https://www.sciencedirect.com/science/article/pii/S0377042707005614` returned403. `https://arxiv.org/pdf/1411.7589` succeeded. The2015 Lissajous survey `https://www2.math.ethz.ch/EMIS/journals/DRNA/pdf/erb_etal_10ypdpts.pdf` returned404 and its tcd mirror timed out. `https://www.research.unipd.it/retrieve/e14fb26e-15a6-3de1-e053-1705fe0ac030/2015-ErbKaethnerDenckerAlborg.pdf` initially exposed its primary introduction/phase convention but subsequent find operations returned403; its later sections were not inspected in this pass. No claim about eq11 or its interpolation theorem is taken from that inaccessible remainder.

A newly surfaced2026 article, Nasri–Mezzanotte–Occorsio, [Extended interpolation on the square and a mixed interpolating sequence](https://link.springer.com/article/10.1007/s40314-025-03489-0), was screened through its primary abstract/introduction and definition of P_(m,m) in §2. It uses tensor products of univariate Jacobi-zero extended interpolation and a mixed sequence, rather than the supplied fixed total-degree mod4 subset. Full remainder and any more distant relation remain UNVERIFIED; no result is inherited from it.

Outcome: no exact match to the odd-degree mod4 adjacent-sum family or shifted phases was identified. “Four Padua families,” a signed parametrization, or phase shifts in Lissajous notation alone are not an identification. The [candidate-screen addendum](candidate-screen.md#c1-addendum-odd-degree-and-shifted-phase-follow-up) states the precise limits; no universal absence or novelty conclusion.
