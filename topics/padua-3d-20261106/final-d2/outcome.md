# D2 ordered determinantal programme — outcome record

Rules/input head `04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b`; developer
Codex gpt-6.1-sol xhigh. Scope: C2 /
`IDEA?padua-3d-20261106-claude-02`, ceiling3 rounds.
This developer controls no Git or shared files. Protocol and code were
published by the coordinator before execution: R1 db8c3cc, R2 9cf64ef,
initial R3 0971807, repaired R3 3bea991.

## Current target and status

Original target retained: structured EN/symmetric rank loci with N=binom(n+3,3)
real cube nodes, Π_n-unisolvence and competitive Λ atn3/4, with a plausible
Padua-derived structure. **OPEN** as a broad construction/quality target.
Exact known real configurations and their measured quality are separate
outcomes. No asymptotic or historical novelty claim.

## Round 1 — exact 2D calibration, then algebra

Actual command and code hash are in the protocol and receipt
[`fd2-exact.json`](../evidence/fd2-exact.json). The run took198.671 wall seconds.

For orientation x=cos(iπ/n), y=cos(jπ/(n+1)), i+j even, use rational generators
q0=T_(n+1)(x)−T_(n−1)(x),
qk=T_(n+1−k)(x)T_k(y)−T_(k−1)(x)T_(n+1−k)(y), 1≤k≤n+1.
The first vanishes on the x Lobatto axis; the others vanish because
T_n(x)=T_(n+1)(y) at the checkerboard nodes and cosine reflection exchanges
the two factors. Their leading terms span all degree-n+1 bivariate monomials.

The exact coefficient-nullspace calculation gives n+1 linear syzygies.
Their matrices, generators and nonzero common signed-minor scales are in
the receipt. For example, atn4 the 6×5 matrix is

```
[-y/4, -y/2,      0,    0,  1/2]
[ x/2,    x,    1/2,  2*y,    0]
[1/2-y,   0,      0, -2*x,   -1]
[   x,    0, -y-1/2,   -1,    0]
[   0,    1,      x,    0, -2*y]
[   0,    0,      0,    1,    x]
```

The n2/3/4 matrices have10/14/18 nonzero entries, respectively, versus 12/20/30 total. These counts refer to SymPy's RREF nullspace basis in the per-generator (1,x,y) unknown order. Other RREF orders give 9/13/17 or more, so sparsity is basis-dependent, not an invariant (audit-05). All syzygy products vanish exactly and signed maximal minors
equal the generators times a nonzero rational constant. These finite exact
executions are **MEASURED exact-arithmetic checks**; their independent
Padua-syzygy replay also passed ([receipt](../evidence/fdr-d2-padua-replay.json)). The coordinator separately replayed the20
algebra cases recorded below. No all-n structural theorem follows. They expose sparse Chebyshev structure,
but neither a higher-dimensional compatible recurrence nor a successful
3D embedding has been derived. The premise “no exploitable2D structure” is
therefore **not established**. Sparsity alone does not settle that premise. D2 did not construct or test a 3D analogue of the Padua Hilbert–Burch shape. R2/R3 used ORSV, tensor-Chebyshev Jacobi and natural-lattice inputs as specified, so the exploitability conjunct is undetermined (audit-05).

The gate corrects a material predecessor omission: IDEA-199 already derived
Hilbert–Burch pencils from recurrence residuals and genuine linear syzygies
atn5. Its construction/extraction was known; its numerical investment was
abandoned. S6/frontier's “never derived” statement is too broad.

| Pencil cases | Actual exact result |
|---|---|
| Both structured families, n2/3/4, Q and GF(1000003):12 cases | Groebner quotient dimensions10/20/35; all degree≤n monomials standard. |
| Both random families, n2/3, both fields:8 cases | Same dimensions/standard monomials; squarefree multiplication characteristic polynomial, certifying reducedness in these exact quotients. |
| Both random families, n4, both fields:4 cases | Each full algebra pipeline hit CPU25s (signal24). No quotient dimension, standard-basis or radicality result returned. |

The structured cases' chosen linear form x+2y+3z has coincident values, so
its characteristic polynomial is not squarefree. The receipt correctly
calls radicality **inconclusive**, not nonradical. R2 supplies a distinct
explicit-zero certificate for precisely those structured inputs.

## Round 2 — real loci and the concrete Jacobi link

[`fd2-real.json`](../evidence/fd2-real.json) records the actual run.
Atn2/3/4 the moment-curve planes x+t y+t²z−t³, t0..n+2, give exactly10/20/35
distinct rational triple-intersection points. Exact cardinal-product
evaluation is the identity, every triple of normals is independent and no
four projective planes meet. Both EN and symmetric pencils realize this
known natural-lattice geometry. R1 quotient dimension=N plus N distinct
common zeros proves their finite ideals radical; the original failed
separating-form test is retained. Rational affine cube normalization is
explicit. The separate [written proof](real-calibration-theory.md) establishes
the all-n known calibration without importing a general degree theorem.

Starting from D5's primary ORSV p7 (rho,sigma)=(10,10) matrix, the declared
Schur-chart search finds10 distinct real corank-two points for size4.
Its specified bordered size5/6 extensions find14/22 points against expected
counts20/35. These are lower counts only; the multistart search is not a
completeness or real-root exclusion argument.

The concrete IDEA-120 probe fixed the tensor-Chebyshev Π_(n−1) sections and
compatibility zeros, freeing last cross blocks and symmetric last blocks.
It used345/810 variables atn3/4, two prescribed starts, analytic commutator
Jacobians and LSMR. All four attempts completed below caps.

| n,start | Commutator residual | Joint diagonalization / original-cube guard |
|---|---|---|
| 3,0 | 1.02488e−7 | Above1e−8 extraction threshold; no node extraction. |
| 3,1 | 1.50218e−13 | Offdiag1.22e−12, rank20, minweight.000172, but maxabs coordinate1.25145. |
| 4,0 | 1.30748e−11 | Offdiag7.80e−11, rank35, minweight1.63e−8, maxabs1.19016. |
| 4,1 | 2.14762e−11 | Offdiag1.36e−10, rank35, minweight.000813, maxabs1.14438. |

These are **MEASURED** outcomes. The concrete unconstrained Jacobi search
failed its original-cube guards, so no positive cube-cubature set is claimed.
Affine normalization of such nodes would change the target Chebyshev
measure and cannot repair that cubature claim.

## Round 3 — measured Λ optimization

The declared full symmetric-pencil search actually varied all60/84 free
matrix coefficients, rather than only moving natural-lattice planes.
The initial-only engineering failure and its prospective mechanical repair
are recorded once in the [protocol repair addendum](protocol.md#r3-mechanical-repair-before-resumed-execution).
Its failed receipt remains separate. The resumed run completed all8 paths,
499 objectives each, so previous1+new499 equals the original500 per-path
budget. No path hit a cap. The actual observations are in
[`fd2-optimize.json`](../evidence/fd2-optimize.json).

| n,start | Baseline sampled Λ | Final sampled Λ | Accepted / guard-rejected proposals | CPU seconds |
|---|---|---|---|---|
|3,0|94681.00|8099.98093|79 /157|.804|
|3,1|94681.00|7774.68218|74 /123|.804|
|3,2|94681.00|5478.14834|102 /155|.860|
|3,3|94681.00|14962.14957|51 /202|.897|
|4,0|10355098.60|1893095.89272|60 /318|1.513|
|4,1|10355098.60|1648075.46627|58 /326|1.420|
|4,2|10355098.60|546899.58091|75 /255|1.420|
|4,3|10355098.60|2549792.06292|52 /277|1.384|

These use the13³ training mesh; assessment adds41³ and512 uniform queries.
For these runs the same maximum was observed on both query sets. Every
trajectory improves the chosen baseline but remains extremely poor against
GT's external4.05/5.09 benchmarks. Best ratios are about1352.6/107445.9.
The explicit moment-curve starting geometry was badly conditioned; a short
local search around it says little about a global matrix-family optimum.

The final best matrices/nodes are committed. Their numerical node counts
are20/35, maximum absolute coordinate1, minimum pair distances.0899868/.0309260,
maximum second-smallest pencil singular values8.22e−12/8.04e−11 and minimum
third-smallest1.37174e−3/3.82631e−4. Vandermonde condition estimates are3340.64
and305641.66. These are **MEASURED** corank/interpolation diagnostics, not
exact certification of the rounded optimized sets or projective completeness.

## Final disposition and counters

**D2 completes3/3 rounds**, with actual attempts at all four ordered steps.
The delivered finite outcomes are exact sparse 2D calibration, exact known
real-cube configurations inside both proposed families, scoped failed/capped
algebra and Jacobi attempts, and poor measured quality after the bounded
matrix optimization. The broad C2 Padua-transfer/quality target remains
**OPEN and deferred under the approved final freeze**.

The real-existence kill does not fire: the written known calibration supplies
real cube configurations at both degrees. Both measured quality thresholds
are exceeded, but the additional “no exploitable2D structure” premise was
not established. Therefore the conjunctive broad-family kill is **not
asserted**. The result is the actual bounded outcome above, not a claim that
the determinant programme or every listed mathematical possibility is exhausted.
No unused round from another frozen direction is consumed.

## Evidence integrity and limits

Only code and small receipts are retained. R1's pretty incremental JSON
grew to52,596B. After the frozen run ended, its exact parsed contents were
losslessly minified to22,340B; original raw hash/size and the administrative
serialization step are in the compact receipt. Raw pretty bytes are/tmp
regenerate-only. No field, failed case or matrix was dropped, and no
scientific code changed during execution. This is zero research rounds.

This developer does not represent its own executions as independent checks.
The coordinator subsequently performed the actual independent checks below.
The written natural-lattice proof is a separate algebraic proof, with no
quality conclusion. No lower-sampled Lebesgue value is a certified supremum.

## Actual independent checks by the coordinator

The coordinator reran all20 completed R1 algebra pipelines and all their
non-timing fields match exactly; actual wall92.8136s. The four randomn4
CPU-cap cases were not rerun or upgraded. Receipt:
[`fdr-d2-exact-replay.json`](../evidence/fdr-d2-exact-replay.json).

For the two best R3 sets, the coordinator used a different monomial basis
and SVD solution, instead of the producer's Chebyshev basis/inverse, on the
same41³+512 queries. It obtained5478.148340739174 and546899.5809121559,
with matrix singular-value, count and cube guards passing;
relative agreement is better than1e−6. Receipt:
[`fdr-d2-quality-replay.json`](../evidence/fdr-d2-quality-replay.json).
Reproduction commands are in the coordinator's `final-root-checks` record.
The coordinator also reviewed the written known-natural-lattice pencil
proof and found it coherent. These are supplementary checks; they do not
upgrade the broad C2 target or constitute the later formal Claude audit.

## Runs needed / unresolved work

- Formal independent mathematical audit remains separate from the completed
  coordinator exact replay and numerical assessment.
- Random n4 exact algebra remains unresolved after actual capped attempts;
  it must not be described as computed, unattempted, or infeasible in general.
- A Padua-specific structure with a proved 3D transfer remains OPEN. The
  known real natural-lattice example does not close this target.
- ORSV bordered searches are incomplete; Jacobi cube-constrained existence
  is unresolved beyond the four specified attempts.
- Optimized rounded pencils/nodes have independent numerical assessment;
  their exact unisolvence/projective completeness is not certified here.

## History

2026-11-12: prospective gate/protocol, R1/R2 actual executions and preservation
of every failed/inconclusive obligation. New counters, old directions frozen.
The coordinator's later actual replay/quality checks were added without a
scope, status, counter or failed-case change.
