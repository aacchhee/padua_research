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
| 1 | Exact finite ranks as above | Awaiting C0 catalogue | Rank-survivor structure |

## Round 2 — frozen while Round 1 runs, before continuation execution

Question: do deficient representatives admit a product of coordinate-node factors of total degree <=n, and which survivors have an exact characteristic-zero nonzero determinant witness? Search all coordinate-layer covers of degree <=n; a cover is an explicit symbolic annihilator for arbitrary distinct axis values. Absence of this narrow cover says nothing about other annihilators. For small surviving representatives n<=2, compute integer determinants on seeded distinct integer axes by fraction-free Bareiss elimination. Separately prove the integer determinant-polynomial degree bound D=3*binomial(n+3,4), its modular-specialization nonvanishing implication and a without-replacement Schwartz–Zippel bound D/(p-max(L)+1). This supporting reduction does not confer axis separation or Lebesgue control.

Cheapest determinant-structure test: for surviving n=1 representatives, factor their exact symbolic determinant after independently translating/scaling the first two values on each axis to 0 and 1. Any mixed-axis irreducible residual factor is a scoped obstruction to an axis-only product factorization. A single exact specialization cannot establish a global factor identity; SymPy expressions must be checked against a direct determinant and the symbolic reduction written out.

## Runs needed

Frozen rank command: `python tracks/lattice-unisolvence/code/c3_rank.py topics/lattice-unisolvence-20261031/directions/C0/catalogue.json --output topics/lattice-unisolvence-20261031/directions/C3/ranks.json`. Independent Astra rerun and adversarial reconstruction are mandatory before acceptance. Generated evidence stays small or in the AC-designated Padua cold-storage staging with receipt pending; no third-party fulltext is committed.
