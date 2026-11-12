# PD-T?padua-3d-20261106-codex-T10-08 — bounded near-critical HNF search

ID kind:PD-T. Aliases: source-neighborhood census. Split from:none. Split into:none. Overall status:**MEASURED**.

## Statement and scope

The prospective addendum to preregistration-T10 was executed for n4..16. It tests the source seed's fixed diagonal a,d, b within source±1 modulo d, c/e independently within source±4 modulo f, and all f from ceil(38n³/(27ad)) through the seed f. All4941 matrices were checked, with13 admissible results total: exactly the original source seed at every degree. Thus no determinant improvement occurs **in these explicit boxes**. This is not unrestricted optimality, nor completeness over the literature's K class. The finite observations remain MEASURED as a conservative bounded-computation report; independent replay is already recorded.

## Reduction, checks and actual feasibility

Each tested row-HNF is an integer lattice of determinantadf. The producer checks every nonzero integer vector in the l1 ball of radius2n−1; survivors get exact shortest-vector, folded-count and rational Fourier-rank checks from the frozen census helper. The search lower endpoint is the named source packing bound; completeness is only over the stated f interval and off-diagonal sets. Its validity as a global lower bound is not required to interpret the finite tested box, and no global conclusion is drawn.

`code/t10_search.py` and `evidence/t10-search.json` record tested/admissible counts, complete flags, intervals, selected matrices, exact ranks, node hashes, code/helper hashes, and raw regenerate-only hash/size. Runtime was1.96seconds summed across degrees; slowest was n16 at0.81seconds, below the frozen120-second cap. Every box completed, so the source-seed fallback was not needed. At n16 all1134 tested matrices yield only B=[[2,0,98],[0,2,158],[0,0,1448]], det5792, degree31,2897 nodes and full rank969. The bounded best folded full-rank parity snapshots from round1 are unchanged.

Frozen command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t10_search.py --raw "$T10_TMP/neighborhood.json" --out topics/padua-3d-20261106/evidence/t10-search.json`. T10_TMP is configurable. The helper is pinned at43d074620c0ea271dbd94a774f472dd5fb0f23c7920204da3262775207f99c1f. 4941-box replay: independent-checks-round06.md (audit03 companion NV-F11, applied2026-11-06).

## Sources and limits

Closest predecessor: Cools–Lyness structured K-optimal search, Cools–Nuyens structured lattice algorithms, Poppe–Cools Chebyshev search. This is a bounded replication/extension, not a new mechanism. No classes outside the finite boxes are rejected. History:2026-11-06 Codex Sol xhigh assigned; frozen and executed after first pushed boundary26434e73.

History2026-11-06 response03: stale replay rationale removed; no material status upgrade is claimed for this historical bounded report.
