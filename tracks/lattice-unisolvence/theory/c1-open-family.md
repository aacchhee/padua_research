# PD-T?lattice-c1-codex-05 — Parity-adapted adjacent-mod4 Chebyshev interpolation target

ID kind: PD-T. Aliases: phase0odd/phase1even; antipodal-transversal half-grid.
Split from: IDEA?lattice-c1-codex-01's broad family question; the proved structural reductions retain their own IDs. Split into: none.

## Statement of the unresolved target

For every n>=1, use Lobatto axes `x_i=cos(pi*i/n)`, `y_j=cos(pi*j/(n+1))`, and phase p_n=0if n is odd,1if n is even. Let `S_n={(x_i,y_j):i+j-p_n mod4 in{0,1}}`.

Target U: S_n is unisolvent for Pi_n for every n>=1.

Target L2: there exists an absolute constant C such that, for every n>=1, these interpolation sets exist and their Lebesgue constants satisfy `Lambda_n<=C*log(n+2)^2`.

These are research questions, not accepted conjectures or inferred theorems. L2includes Uas an existence obligation. Other fixed polylogarithmic exponents may be investigated separately; no exponent is supported by a finite fit here.

## Definitions, assumptions and status

Real nodes, ordinary Lagrange total-degree interpolation, supremum over[-1,1]^2. The phase is allowed to depend on parity of n as explicitly stated. Overall status OPEN. Elementary finite base cases under PD-T?lattice-c1-codex-01 and measured finite samples do not make this universal target PARTIAL; its infinite claims have no proved infinite parameter case. This file keeps the original broad goal visible rather than narrowing it to a measured finite scope.

## Supporting dependencies and exact remaining obligations

PD-T?lattice-c1-codex-02proves correct cardinality for every n. PD-T?lattice-c1-codex-04gives an explicit matrix A_n with ||A_n||<=1and proves Uequivalent to `||A_n||<1` at every degree. PD-T?lattice-c1-codex-03gives an arbitrary-field row-root matrix criterion if a different algebraic route is useful. These are supporting reductions, not proofs of UorL2.

The same Gram theorem supplies a coarse conditional bound `Lambda_n<=2sqrt(N)/sqrt(1-||A_n||)`. It retains a sqrtNfactor even with a uniform gap, so does not establish L2. The quarter-character moments have explicit geometric/cotangent expressions, but no proved Cauchy/Hilbert inverse comparison, no exclusion of norm1for all n, and no localized L1kernel estimate were obtained. Those are exact unresolved steps.

## Evidence and scope

PD-T?lattice-c1-codex-06contains finite exact-rank and floating diagnostics, including a positive measured cross-block gap through originalodd n63and shiftedeven n64. These samples do not prove generic nonvanishing, all-degree unisolvence, any asymptotic rate or a certified Lebesgue supremum. No novelty claim. Literature follow-up found no exact identification within its stated queries/sections, with remaining fulltext gaps; this is not an exhaustive absence result.

Properties: (a)periodic adjacent-character union at each n, yes; (b)proved complete structural reductions, yes, with the decisive nonvanishing inequality OPEN; (c)polylogarithmic Lebesgue growth OPEN, finite values MEASURED only. The unshifted even phase0failures in PD-N?lattice-c1-codex-02do not reject this parity-adapted family.

## Development stop and resumption

Twelve rounds used: original ten plus the written two-round extension that filled the omitted n≡0mod4phase1case. Stop at that budget with U/L2 OPEN and candidate retained for further development, not REJECTED. Resume only with a concrete proposed proof of strict contraction, a structural identification with a verified known family preserving this polynomial space, or an inverse/kernel estimate that removes the sqrtNloss. Further ranks, condition numbers or asymptotic fits alone do not meet that resumption condition. Independent Astra reconstruction of every proved supporting claim remains required before acceptance; the separate Claude handoff is unchanged.

## History

2026-10-31, Codex assigned gpt-6.1-sol xhigh, rules/source e949ef06895acd5463cdf8df7e0e5f795218f70f. Initially investigated phase0, then phase1only at n≡2. Root's explicit rounds11–12extension added phase1at n≡0, producing this all-degree cardinality/transversal target. No earlier singular phase was silently erased.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
