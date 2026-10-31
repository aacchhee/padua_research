# Unisolvent lattice subsets beyond checkerboards — development report

**3D candidates survive the counting and exact-rank screens. No infinite-degree 3D family with an axis-factorized criterion or convincing Chebyshev stability emerges from this bounded campaign.** These conclusions have different scopes: correct counts hold for an infinite cyclic6 family; exact nonzero witnesses establish generic feasibility only for listed finite-degree patterns once the written reduction/checks are applied; finite Lebesgue samples do not prove an asymptotic obstruction. No publication-level novelty is claimed.

This is stacked on charter PR #2 and changes no charter text. Original base eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64, audited base update3bd9d4e merged without rebasing. Rules read e949ef06895acd5463cdf8df7e0e5f795218f70f. User's explicit Step0 and provisional-ID instructions govern this campaign. Exact ledger: [shared allocations](../padua-batch-20261031/ALLOCATIONS.md).

## Ranked development briefs

| Rank / candidate | What survives | (a) Periodic | (b) Axis factor / structural criterion | (c) Chebyshev stability | Disposition / next decisive step |
|---|---|---|---|---|---|
| 1: 3D cyclic6 fibers on lengths(n+1,n+2,n+3) | Infinite exact-cardinality count with full residue correction; finite-degree exact rank survivors | Yes, fixed sum congruence mod6 | No infinite-family factorization established; generic witness reduction is a feasibility certificate, not a replacement for the nontriviality requirement | Unfavorable finite measurements; n6 a111 consecutive fiber has sampled maximum about128123 | Retain as structural lead, **not an accepted 3D Padua analogue**. Resume only with a specific factorization/rank-induction mechanism or a new stable pattern, rather than more blind rank samples |
| 2: explicit small 3D mixed-axis determinant | Degree-one periodic example has an exact mixed-axis criterion and a counterexample to independent axis tests | Yes | Complete finite example; mixed y/z factor obstructs a pure axis product | Degree-one examples can be stable, but imply no increasing-degree construction | Retain scoped structural result; no novelty claim and no infinite-degree conclusion |
| 3: 2D adjacent mod4 coset union | Concrete departure from ordinary parity, investigated after counting closed | Yes, two residues mod4 | Low-degree exact criterion investigated in C1; broad factorization is a separate target | Recorded in C1, with finite scope | See C1 records; no automatic equivalence or novelty claim versus Floater/Harris/DU/Camargo |
| 4: all other bounded single-fiber instances | Every count failure, rank failure and survivor retained under unique parameter keys | Yes | Some failures have universal layer-cover certificates; unresolved rank failures remain finite observations | Most generic survivors specialize poorly on standard Lobatto axes | Retain failed/deferred scopes. Growing moduli, other offsets, zero coefficients, coset unions and boundary corrections are outside the finite catalogue |

## What was actually screened

C0 uses primitive characters with every coefficient nonzero, k2..6, n1..6 and sorted axis lengths in{n+1,n+2,n+3}. Shorter axes have a separate universal annihilator and are excluded from the potentially unisolvent catalogue. Zero coefficients, arbitrary unions and boundary corrections are explicitly deferred; the catalogue is not a classification of every periodic set.

All77616 raw parameter tuples are represented by5061 canonical count trials, with explicit orbit equivalences. Of these,4610 fail exact cardinality and451 match:39 in2D,412 in3D. The row-inheritance schema preserves each tried tuple's hypotheses, closest predecessor, kill test, exact count, disposition and aliases. It avoids treating thousands of parameter instances as unrelated new mechanisms.

C3 tests all412 3D count survivors, mapping identical/reversed point sets to364 representatives. Each receives two distinct-node draws at each of1009,1013,1019:2184 exact modular matrices. The seeded finite ranks stay MEASURED; the separate determinant-polynomial lifting/degree statement supplies any stronger conclusion only when its recorded exact witness and independent checks are present.

| n | Count-surviving 3D patterns | Distinct representatives | Full rank at least once | Deficient in every sampled matrix |
|---|---:|---:|---:|---:|
| 1 |119|77|50|27|
| 2 |68|62|19|43|
| 3 |78|78|32|46|
| 4 |45|45|18|27|
| 5 |56|56|16|40|
| 6 |46|46|7|39|

There are142 representative survivors and222 always-deficient representatives in this finite screen.127 of the latter have explicit coordinate-layer covers of total degree<=n, hence symbolic annihilators for arbitrary distinct axes. The95 other failures are not promoted to universal singularity. Small integer witnesses and normalized symbolic determinants are retained, including an accidentally singular integer draw rather than hiding it.

## Stability comparison and limits

C3 uses a21³ Chebyshev–Lobatto test mesh and floating solves in a total-degree tensor-Chebyshev basis. Numerical rank, condition number and nodal cardinality residuals are retained. Numerically singular cases do not receive a finite Lebesgue value. The reference approximate-Fekete set is a fresh QR extraction from a tensor Lobatto mesh, not a reproduction of a named paper's curve-based set. Lower-set references include both natural and discrete-Leja axis ordering; the latter is materially stronger in this experiment.

| n | Smallest recorded sampled maximum among screened 3D survivors | Lower set, discrete Leja order | QR approximate Fekete |
|---|---:|---:|---:|
|1|2.00|5.00|2.00|
|2|4.84|7.00|7.00|
|3|88.99|13.17|8.32|
|4|1497.77|19.50|11.24|
|5|3863.70|26.34|13.86|
|6|97819.06|40.28|22.19|

![Finite sampled Lebesgue comparison](figures/lebesgue.svg)

All values in this table/figure are **MEASURED**. They are sampled maxima, not certified continuous suprema; neither a universal lower bound nor an asymptotic growth law is inferred. The finite comparison gives no stability-driven continuation for the screened high-degree Lobatto patterns. It does not rule out other labels, other moduli, different coset unions, or boundary-corrected families.

## Literature separation and retained gaps

The [Step0 baseline](../../literature/lattice-unisolvence/baseline.md) was recorded before exploration. The later [search log](../../literature/lattice-unisolvence/search-log.md), [comparison](../../literature/lattice-unisolvence/comparison.md) and [candidate-specific screen](../../literature/lattice-unisolvence/candidate-screen.md) retain41 queries and20 coverage-qualified source records. Eighteen records inspect primary-paper excerpts, one primary slides and one publisher abstract; no complete-reading claim is made. The original Biermann/Chung–Yao/Gasca–Maeztu historical texts and Cools–Poppe detailed fulltext have named gaps.

Lower-set interpolation already supplies arbitrary distinct-node unisolvence. Natural lattices are a different construction, not an interchangeable attribution. Known Lissajous–Chebyshev interpolation uses its source spectral space; it is not silently equated with the full total-degree simplex in3D. Bos–De Marchi–Vianello's specific curve limitation is not a general no-go theorem. Li–Sun–Xu's cubature conjecture does not constrain this interpolation-only campaign. The inspected determinant predecessors make axis separation an established mechanism. Floater's interlaced-grid journal coverage remains pending-reference. No exact matching cyclic6/mod4 theorem was identified within the documented search, which leaves novelty UNVERIFIED.

## Evidence, stop conditions and handoff

Each direction freezes questions before runs and retains rounds/corrections. C0 closes after answering its bounded catalogue and infinite-count questions. C3 continues beyond rank to annihilator, determinant and stability tests; its broad infinite-degree structural/stability target remains OPEN. C1 is launched only after C0 closes. At most two substantive directions are active at a time, no ultra assignment, and no exhausted direction is described as a universal negative.

The separate Astra reconstruction covers every retained candidate and consequential computation; its exact coverage, findings and dispositions are linked in the audit handoff. Required Claude audit is distinct and remains PENDING until performed. Scientific statements keep provisional IDs at AC's request. Final global allocations, other-member acknowledgement, Windows cold-storage receipt and integration reconciliation remain visible obligations, not inferred approvals. See [audit handoff](AUDIT_HANDOFF.md) for exact commands, target hashes and remaining work.
