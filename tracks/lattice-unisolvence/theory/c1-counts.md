# PD-T?lattice-c1-codex-02 — Exact cardinality of the adjacent-mod4 union

ID kind: PD-T. Aliases: mod4 adjacent half-density counts.
Split from: none. Split into: none.

## Statement

For every integer n>=0, let `S_(n,p)={(i,j):0<=i<n+1,0<=j<n+2,i+j-p mod4 in{0,1}}` and N_n=binom(n+2,2). Its count equals N_n plus the correction in this table:

| n mod4 | phase0 | phase1 | phase2 | phase3 |
|---|---:|---:|---:|---:|
|0|1|0|-1|0|
|1|0|1|0|-1|
|2|0|0|0|0|
|3|0|0|0|0|

In particular phase0is cardinality-correct at every odd n; phase1is cardinality-correct at every even n. For n≡2mod4, every adjacent phase has exactly N_n nodes and is a row/column incidence relabelling of phase0.

## Definitions, assumptions and status

All indices start at0; lengths are n+1 and n+2. Counts are independent of physical coordinates. Overall status PROVED (developer analytic proof; independent Astra reconstruction pending).

## Depends on

Elementary residue convolution; no external theorem.

## Proof

For modulo4 let h_L be the axis residue histogram and u the all-ones length4vector. Then h_(L+4)=h_L+u. The cyclic-convolution vector F_n=h_(n+1)*h_(n+2) changes uniformly when n is replaced by n+4: each entry changes by `((n+5)(n+6)-(n+1)(n+2))/4`. Thus the sum of any two adjacent entries changes by half the box-volume change, exactly N_(n+4)-N_n. Every phase correction is4-periodic. Direct phase0base counts at n0,1,2,3are2,3,6,10, whereas N is1,3,6,10. Direct phase1base counts are1,4,6,10. Phases2and3are the complementary selections to phases0and1in a box with2Npoints, so their corrections are the negatives. This proves the complete table.

When n≡2mod4, n+2 is divisible4, so each row contains exactly half of its y indices in any adjacent phase; total cardinality is (n+1)(n+2)/2=N_n. Define the permutation on each complete y block by `4b+r -> 4b+((r+p)mod4)`. It sends phase0 incidence to phasep because the sum residue increases byp. The x labels are unchanged. This is an arbitrary-axis relabelling equivalence, not an assertion that the permutation preserves the physical Chebyshev geometry.

## Checks, sources and scope

C1/results.json preserves all actual phase0n1..8 counts, including failures at n4,n8. Shifted n2,6,10and extension n4,8checks are supplementary. No computer inference is needed for the general count identity. Source/prior-art coverage as C1/candidates.md; no novelty claim. Periodic yes; counts alone supply neither determinant factorization nor Lebesgue bounds. Count failures are limited to their phase and exact minimal-node target; no rank assertion follows for their rectangular matrices.

## Open items and history

Independent reconstruction pending. General interpolation/stability of the parity-adapted phase0odd/phase1even family remains unresolved.2026-10-31, Codex assigned gpt-6.1-sol xhigh, rules/source e949ef06895acd5463cdf8df7e0e5f795218f70f. Original statement covered phase0counts and complete-block phaseequivalence only; root-authorized rounds11–12expanded the table to all four phases, preserving the original scope/results.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
