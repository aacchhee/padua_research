# PD-N?lattice-c1-codex-01 — The quadratic mod4 determinant is not a pure axis product

Final ID: **PD-N033** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N. Aliases: crossed singularity obstruction; nonseparable n2 determinant.
Split from: PD-T?lattice-c1-codex-01 criterion; this is its distinct negative consequence. Split into: none.

## Statement

For phase0 at n2 or n3 over Q, there do not exist functions F on all distinct rational(n+1)-node X lists and G on all distinct rational(n+2)-node Y lists such that `det V(X,Y)=F(X)*G(Y)` for every such pair. The same conclusion holds after dividing the determinant by any everywhere-nonzero within-axis factors. Thus this family does not admit a universal pure axis-product determinant at either degree, although it has complete mixed-axis criteria.

## Definitions, assumptions and status

The determinant convention is fixed in C1/frozen-scope.md. Functions need no polynomial/rational regularity; the domain excludes within-axis collisions. Overall status PROVED (developer proof; independent Astra reconstruction pending).

Candidate/claim disposition: proposed pure-axis-product mechanism REJECTED: failed over the stated domain. This does not refute all structural criteria, all mod4 patterns, all larger degrees, or a factorization containing mixed factors.

## Negative-result scope and dependencies

Attempted mechanism: phase0 IDEA?lattice-c1-codex-01 interpreted as an all-axis product analogous to a checkerboard. Parameter range: n2or3, one explicit2x2rectangle per degree suffices. The n2proof depends on PD-T?lattice-c1-codex-01; the n3proof is the exact finite modular certificate below, with committed checker/input/output and independent replay pending.

## Proof

Take X_A=(0,1,2), X_B=(0,3,5), Y_A=(0,1,2,3), Y_B=(0,1,2,4). Direct evaluation, or the complete criterion, gives the2x2 determinant-value matrix, rows A/B for X and columns A/B for Y,

`[[0,16],[-180,0]]`.

If det=F(X)G(Y), the two nonzero off-diagonal entries force F(X_A),F(X_B),G(Y_A),G(Y_B) all nonzero in Q. Both diagonal entries would then be nonzero, a contradiction. Dividing each entry by a nonzero product of within-axis factors preserves this zero/nonzero pattern, proving the extended statement.

For n3take integer lists X_A=(692,619,116,299), X_B=(418,202,907,646), Y_A=(683,167,402,988,776), Y_B=(873,563,295,641,484). Their within-axis entries are distinct. Build the ten total-degree monomial columns in increasing total degree, then increasing x exponent, on the phase0selected rows in increasing(i,j). Exact modular Gaussian elimination at prime1009gives determinant residues `[[469,520],[14,277]]`. The cross product is `469*277-520*14≡544 (mod1009)`, nonzero. Every integer determinant reduces to its modular determinant, so the cross-product integer is nonzero over Q. An outer product F(X)G(Y) always has zero cross product, contradiction. Dividing by nonzero separable factors merely multiplies the cross product by an overall nonzero scalar, preserving failure.

This finite proof reduction needs only four explicit10x10determinants over F1009, no sampling assertion. The deterministic seed generated the displayed inputs but plays no role after they are fixed. The committed checker c1_stability.py rectangle() and stability.json record them; independent exact replay is required before computer-proof acceptance. No conclusion is drawn from a zero residue or from random rank samples.

## Checks, sources and scope

c1_mod4.py computes all four6x6 determinants by exact Fraction elimination and asserts equality with the formula. Evidence C1/results.json; hashes/command in C1/rounds.md. Independent reconstruction pending. No literature absence/novelty claim: existing determinant frameworks can include mixed factors. Properties: periodic yes; complete mixed criterion exists; Lebesgue asymptotics unknown.

## Open items and history

General-degree nonvanishing/stability remains OPEN; the complete row-moment criterion PD-T?lattice-c1-codex-03 is available.2026-10-31, Codex assigned gpt-6.1-sol xhigh, rules/source e949ef06895acd5463cdf8df7e0e5f795218f70f. Original negative scope n2was explicitly extended to n3after round6's nonzero certificate; no claim of universal failure at other degrees.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
