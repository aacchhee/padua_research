# C3 frozen questions and round ledger

Rules and worktree base: `e949ef06895acd5463cdf8df7e0e5f795218f70f`.
Developer: Codex mathematical C3 subagent, assigned gpt-6.1-sol xhigh; runtime effort metadata unexposed. Git and shared-state owner is root.

## Reading and novelty gate

Read AGENTS, WORKFLOW, CODEX, REQUEST, campaign plan, complete state/IDEAS including every obstruction, U2 candidate records, literature INDEX and lattice baseline, lower-set/Dencker–Erb/Cools–Poppe records, and PD-T001/T002 proofs. Searched `three.dim|trivariat|annihilat|tensor|axis|congruence|Lissajous|checkerboard` across tracks, topics/directions and literature/records. Shortlist: IDEA-013/029 (higher-dimensional interpolation), IDEA-002/003 (axis determinant factors), lower sets and Lissajous–Chebyshev interpolation. Baseline sources are LITERATURE with their recorded reading limits; no novelty or equivalence claim follows from a title.

Separation sought: a precise finite-index periodic 3D subset with total-degree cardinality and an explicit generic/structural criterion. Ordinary lower sets already solve arbitrary-node unisolvence. Existing Lissajous constructions require spectral-space comparison; no such source theorem is inherited. Finite random ranks alone stay MEASURED for generic claims. All candidates, including rank failures and failed proof scopes, are retained.

## Round 1 — frozen before execution

Question: for every C0 admissible primitive single-congruence pattern in the delivered bounded catalogue, restricted here to d=3, n=1..6 and sorted lengths drawn from {n+1,n+2,n+3}, what are the exact total-degree evaluation ranks? The initial consecutive-length-only draft was widened at root's instruction before any rank run; every admissible C0 3D pattern is now included.

Inputs: `topics/lattice-unisolvence-20261031/directions/C0/catalogue.json`, with explicit n,lengths,k,a,residues and pattern ID. C0 delivered 412 d3 representatives, n1..6 counts 119,68,78,45,56,46; its own catalogue symmetry already includes axis reversals, unit character scaling and equal-length-axis permutations. C3 generates selected index triples directly and verifies cardinality binomial(n+3,3). Deduplicate identical selected index sets and axis reversals only, preserving an explicit per-pattern representative map. Axis reversal merely permutes the names of free node variables, hence preserves generic rank; within each run a representative specialization transports to its aliases by reversal.

Runs: primes 1009,1013,1019; two seeded independently sampled distinct node lists per axis and prime. Base seed 2026103103; actual deterministic seed formula and every sampled axis are recorded in JSON. Standard-library exact modular Gaussian elimination. Record full ranks and determinant residues; no floating rank test. Selective exact rational witnesses follow any surviving small-degree pattern.

Kill criterion: rank deficiency at every sampled specialization only kills those specializations, not generic unisolvence. A written nonzero annihilator with total degree <=n proves a scoped universal obstruction. A nonzero modular determinant witnesses a nonzero determinant polynomial in that characteristic; char-zero generic conclusions require their own written reduction and independently checked witness.

All patterns report periodicity (yes by construction), axis-factorized criterion (unknown until developed), and Lebesgue behavior (unknown until measured). The first continuation, frozen before its run, will ask for product-of-coordinate-layer annihilators and a written determinant-polynomial degree/failure-probability reduction.

## Round ledger

| Round | Question frozen | Actual outcome | Continuation |
|---|---|---|---|
| 1 | Exact finite ranks as above | 412source rows ->364reps,2184tests;142full-rank witnesses | Round2 structure |
| 2 | Coordinate covers, integer witnesses, normalized n1 factors |127covers;68/69integer witnesses nonzero;23/50mixed n1 factors | Round3 Lobatto |
| 3 | Fixed-mesh Lebesgue vs lower/QR references | No favorable n3..6 performance lead; all floating MEASURED | Round4 exact rectangle/projection |
| 4 | Axis-product rectangle tests, slice-removal projected counts |114nonseparable witnesses;86new annihilatorcerts,9leftovers | Sole n2 zero-test case merits Round5 |
| 5 | Isolated n2 symbolic determinant, nine subbox checks | Direct axis factorization proved;0/9subboxcerts; naive n2 continuation deficient at represented n3,4,6 | Close C3; original unbounded target OPEN |

## Round 2 — frozen while Round 1 runs, before continuation execution

Question: do deficient representatives admit a product of coordinate-node factors of total degree <=n, and which survivors have an exact characteristic-zero nonzero determinant witness? Search all coordinate-layer covers of degree <=n; a cover is an explicit symbolic annihilator for arbitrary distinct axis values. Absence of this narrow cover says nothing about other annihilators. For small surviving representatives n<=2, compute integer determinants on seeded distinct integer axes by fraction-free Bareiss elimination. Separately prove the integer determinant-polynomial degree bound D=3*binomial(n+3,4), its modular-specialization nonvanishing implication and a without-replacement Schwartz–Zippel bound D/(p-max(L)+1). This supporting reduction does not confer axis separation or Lebesgue control.

Cheapest determinant-structure test: for surviving n=1 representatives, factor their exact symbolic determinant after independently translating/scaling the first two values on each axis to 0 and 1. Any mixed-axis irreducible residual factor is a scoped obstruction to an axis-only product factorization. A single exact specialization cannot establish a global factor identity; SymPy expressions must be checked against a direct determinant and the symbolic reduction written out.

## Round 3 — frozen after Round 2, before Chebyshev execution

Question: among the 142 representatives with at least one full modular rank, which Chebyshev–Lobatto specializations are numerically invertible and what sampled Lebesgue values do they exhibit for n<=6? Use product Chebyshev total-degree basis, tensor21^3 equispaced-angle evaluation mesh, and two reference sets per degree: the ordinary first-axis-index lower set i+j+k<=n on three (n+1)-point Lobatto axes, and QR column-pivoted approximate Fekete extraction from the (2n+1)^3 Lobatto tensor mesh. The latter is a transparent standard extraction baseline, not a reconstruction of Bos–De Marchi–Vianello's curve-specific implementation.

Use singular values and condition numbers only as numerical diagnostics; report singular/ill-conditioned cases as numerical unresolved, never exact singularity. Solving V^T against basis evaluation yields Lagrange cardinal functions; maximum sum of absolute values over the fixed mesh is a sampled lower bound on the true Lebesgue constant. No growth-law inference from n<=6. All floating observations are MEASURED. Record NumPy/SciPy/BLAS versions, code/input hashes and actual mesh parameters.

## Round 4 — frozen after Round 3, before execution

Opening: the surviving k=6,a=(1,1,1),consecutive-axis family merits a cheap axis-separability test even though its observed Chebyshev conditioning is poor. For every modular-rank survivor, choose seeded distinct random axis lists over F1009 and vary two axis blocks independently in a 2x2 rectangle, fixing the third. Test whether D(A,A)D(B,B)-D(A,B)D(B,A) is nonzero. Nonzero exact residue proves the integer determinant polynomial cannot be a product of three axis-only rational functions. Try all three axis pairs once, retaining zero tests as inconclusive; this is scoped to each fixed pattern/degree.

For always-deficient representatives unresolved by coordinate-layer covers, remove subsets of coordinate layers on one axis, of cost q<=n. If the projection of all remaining nodes onto the other two axes has fewer than binomial(n-q+2,2) distinct pairs, dimension counting gives a nonzero bivariate annihilator of degree<=n-q; multiply by the removed coordinate factors. Search all three axis choices. This is a symbolic, all-fields obstruction once its finite cardinality certificate is checked. Failure of this narrow projected-count mechanism leaves that representative unresolved.

## Round 5 — frozen before execution

The only degree2 survivor with all rectangle tests zero is C3-8ea9e9f33e3d / C0-d3-n2-050, lengths(3,4,5), k6,a=(3,1,2),c0; Chebyshev condition2=4.90 and sampled Lebesgue=5.848. Question: does its normalized symbolic determinant factor into axis-only polynomials? Compute the direct 10x10 symbolic determinant over Q[x2,y2,y3,z2,z3,z4] with each axis's first labels0,1, factor it and verify the product exactly. Restore affine scaling by the axis-block degree5 from PD-T?lattice-c3-codex-01; state only this isolated degree2 result, with no n-dependent extension inferred.

For the nine rank-deficient degree2/3 representatives not explained by previous certificates, enumerate coordinate subboxes A1xA2xA3. The dimension of Pi_n restricted to the full Cartesian subbox is H= #{alpha: |alpha|<=n, alpha_r<|A_r|}, by the standard monic-grid reduction (to be proved if used). More than H selected points in such a box proves row dependence for every distinct axis specialization. Exhaustive failure of this test is only a failure of this certificate mechanism. Freeze the nine IDs from obstructions.json; do not expand the search silently.

## Runs needed

Frozen rank command: `python tracks/lattice-unisolvence/code/c3_rank.py topics/lattice-unisolvence-20261031/directions/C0/catalogue.json --output topics/lattice-unisolvence-20261031/directions/C3/ranks.json`. Independent Astra rerun and adversarial reconstruction are mandatory before acceptance. Generated evidence stays small or in the AC-designated Padua cold-storage staging with receipt pending; no third-party fulltext is committed.

## Closure decision after Round 5

Root instructed closure after the five frozen rounds unless a concrete infinite-family structural/performance opening remains. The isolated n2 factorization has no straightforward fixed-character continuation: existing C0/C3 records for k6,a312 give n3 ranks19/20, n4 ranks33/35, n6 ranks79/84 at every represented residue; n5 has no cardinality-admissible consecutive row. The k6,a111 generic feasibility lead has exact axis-product obstructions in each tested degree n3..6 and poor measured Lobatto performance. A useful mixed structural criterion remains OPEN, without a concrete current route. Nine deficient generic cases also remain OPEN beyond the tested certificate mechanisms. This is a scoped close, not a universal nonexistence assertion. No blind further rank search is planned.

Supplementary Astra separately reran the consequential computations and reconstructed the written lemmas; its final signed file snapshot is requested. Required Claude audit remains pending. Root alone integrates IDs, shared registries, Git and PR.
