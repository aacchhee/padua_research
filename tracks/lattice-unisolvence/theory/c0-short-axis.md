# PD-N?lattice-c0-codex-01 — A short coordinate axis prevents total-degree unisolvence

ID kind: PD-N. Aliases: coordinate annihilator; short-box exclusion.
Split from: none. Split into: none.

## Statement

Let K be any field, d>=1 and n>=0. Let H_j be finite nonempty lists of distinct axis nodes of lengths L_j. If some L_j<=n, no subset S of their Cartesian product is unisolvent for total-degree<=n polynomials: its evaluation map has a nonzero kernel polynomial of degree L_j.

## Definitions and assumptions

Unisolvent means the polynomial evaluation map is bijective onto values on S. The noninjectivity statement also applies when |S| differs from binom(n+d,d). No order, characteristic, modulus or physical separation of different axes is assumed.

## Status by part

Overall status: PROVED (developer-written one-line annihilator proof; independent Astra reconstruction pending).

Candidate / claim disposition: the short-axis family IDEA?lattice-c0-codex-03 is REJECTED: failed within these hypotheses.
Rejection reason: a nonzero polynomial of allowed total degree vanishes on every box point.

## Negative-result scope

Attempted mechanism: any congruence/coset-union subset of a box with a short coordinate axis. Parameter range: every field and every d,n,L with at least one L_j<=n. For C0's original positive-length bound L_j<=n+3 this removes exactly those tuples from the potentially-unisolvent finite catalogue; they are retained as this quantified family, even if their cardinality happens to match.

## Depends on

Elementary polynomial arithmetic only.

## Proof

Choose j with L_j<=n. The polynomial `p(x_1,...,x_d)=prod_(h in H_j) (x_j-h)` is monic in x_j, hence nonzero over every field; its total degree is L_j<=n. It vanishes at every point in the Cartesian product and therefore on S. Thus evaluation is not injective, so cannot be bijective.

## Checks, sources and scope

The proof is analytic and has no computational dependency. This is a standard coordinate annihilator, no novelty claim. It does not rule out lengths>n or allow conclusions about failed random-axis specializations. Property (a) the congruence subfamily is periodic; (b) the coordinate annihilator is a universal singularity criterion in the stated scope; (c) no Lebesgue constant exists for a nonunisolvent square interpolation matrix. No claim covers derivative/Hermite interpolation.

## Open items and history

Independent reconstruction pending; C3 can skip these universally singular boxes. 2026-10-31, Codex assigned gpt-6.1-sol xhigh, rules/source e949ef06895acd5463cdf8df7e0e5f795218f70f.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
