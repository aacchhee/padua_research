# PD-T?lattice-c1-codex-06 — Finite mod4-union ranks and Chebyshev diagnostics

Final ID: **PD-T089** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T. Aliases: C1 sampled stability; finite gap diagnostics.
Split from: none. Split into: all proved analytic reductions and OPEN infinite target have separate IDs.

## Statement and status

Overall status MEASURED. In the exact/floating executions below:

- Phase0counts for n1..8were3,6,10,16,21,28,36,46, with mismatches only n4/8against targets15/45. Original cardinality matches had full exact modular rank in36seeded draws; shifted phases1/3at n2,6,10added36full draws; phase1at n4,8added12full draws. Total84exact modular full-rank samples, no generic/all-degree inference.
- Exact Fraction checks verified the n2determinant identity at four crossed examples and80seeded rational draws across four phases. The n3normalized6x6row-moment determinant has59expanded monomials, total degree6, and the exact factorization in symbolic.json; the product check passed. The separate n3nonfactorization certificate is in PD-N?lattice-c1-codex-01, not inferred from generic samples.
- Float64SVD/condition/Lebesgue diagnostics are preserved per row in results.json, stability.json and extension.json. The latter two contain57adaptive comparison rows: three families at19degree/phase choices, with identical base/refinement protocol. Mod4odd n31gave sampled Lambda71.5070703794and Chebyshev-product-basis condition2=12.3540779268; standard Padua and specified greedy-Leja lower-set controls at n31are recorded in the same file. Shiftedphase1n32gave sampled Lambda45.8532738820and condition2=10.4809529030, compared with Padua10.9935945411and lower-Leja149.787392818sampled maxima.
- Direct restricted-Gram/cross-block comparisons passed at seven small configurations (five in gram.json plus n4/8in extension.json). The explicit moment formula matched direct sums for all m1..12,a,c0..m, maximum observed discrepancy1.4106e-15. Cross-block diagnostics have17rows total, including positive measured gap0.0250121554347at phase0n63and0.0344938473307at phase1n64. These gaps are floating observations, not exact sign certificates or asymptotic bounds.

## Definitions and assumptions

All parameter rows inherit the detailed scope and properties in C1/candidates.md and frozen-scope.md/extension.md. Samples use Python Random with explicit seed per row, distinct integer axes over primes1009,1013,1019, and exact modular elimination. Floating nodes are cosines, total-degree Chebyshev product basis; rank tolerance is `max(shape)*eps*sigma_max`. A condition number depends on this stated basis. The81angle-grid plus three adaptive levels gives sampled lower values, not a certified continuous maximum; differing grids can yield differing finite maxima. No rounding interval or exact nonzero proof is claimed for floating matrices.

## Checks, provenance and actual commands

Python3.12.14, NumPy2.3.5, SymPy1.14.0; standard-library Fraction/modular arithmetic for exact checks. Source/rules SHA e949ef06895acd5463cdf8df7e0e5f795218f70f. Each output embeds source/dependency hashes. Exact commands and final file hashes are in C1/rounds.md and hashes.txt. The four small JSON files plus symbolic.json total98365bytes, all necessary finite evidence, individually below1MB. No external PDFs/fulltexts, cold upload or Windows archival receipt is claimed.

The producer commands were actually executed. A preliminary phase0run was superseded by the final pinned combined run; it is not separately relied upon as immutable evidence. Independent Astra exact/floating replay is pending at developer freeze and will have its own record; reading these outputs is not a rerun.

## Sources, scope and open items

No novelty claim. Correct count and full finite rank are necessary screens, not proof of the infinite-family properties. Proved structural results: PD-T?lattice-c1-codex-01..04. OPEN targets: PD-T?lattice-c1-codex-05. Scoped negative results: PD-N?lattice-c1-codex-01..02. Next: independent replay, then analytic work only under the stated resumption condition.

## History

2026-10-31, Codex assigned gpt-6.1-sol xhigh; twelve conceptual rounds, with the extension written before execution. No results were promoted from floating agreement to proof.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
