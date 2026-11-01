# PD-N?lattice-c3-codex-04 — Exact axis-separation rectangle obstructions in finite degrees

Final ID: **PD-N038** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N. Aliases: cross-determinant test; axis-block multiplicative rank1 test. Split from: n1 example c3-n1-mixed-axis-obstruction.md. Split into: none.

## Statement

For each of the142 modular-rank survivors in the frozen C3 catalogue, c3_obstructions.py tested all three pairs of axis blocks at one independently seeded 2x2 rectangle over F1009. There is a nonzero exact rectangle residue for114 representatives: counts by n1..6 are23,18,32,18,16,7. In particular every rank survivor at n=3..6 has a witness against an axis-only rational product factorization of its determinant polynomial. The28 all-zero rectangle tests remain inconclusive, not positive factorization evidence.

## Status and negative scope

Overall status: MEASURED finite exact witness output, with the following written symbolic certificate reduction. A completed computer-assisted per-pattern refutation additionally requires the independent rerun/audit recorded separately. Candidate mechanism: factor D(X,Y,Z) as an axis-only rational product F(X)G(Y)H(Z), in the fixed-degree fixed-index-pattern scope. No other kind of structural criterion is ruled out, nor is every distinct-axis specialization alleged singular.

## Certificate reduction (written proof)

If a polynomial D factors as such a rational product, then varying any two axis blocks independently while fixing the third yields the polynomial identity

`R=D(A,A)D(B,B)-D(A,B)D(B,A)=0.`

Indeed the two products of rational factors agree formally; clearing denominators gives an identity, and D itself is polynomial, so the polynomial R vanishes identically. A nonzero R at integer lists modulo any prime implies the integer polynomial R is nonzero, because specialization and reduction commute. This contradicts the required identity. The reduction is deterministic and does not require any of the four determinant values to be nonzero. It rules out rational, hence polynomial, axis-only products; it does not rule out an additive/mixed criterion or a change of pattern.

This elementary test is not a claim of novelty. The explicit n1 proof and stronger failure of arbitrary independent predicates are separately PROVED in PD-N?lattice-c3-codex-02.

## Checks and limits

All axes, seeds, four determinants and residues are stored in C3/obstructions.json, SHA256 d61b0a60f1b99aad93b96514ef78f05f5e1542514d6db7756fbd916a54a76def. Code c3_obstructions.py SHA2569088670ef3aa95b8493b7afa6029e3f90a00a184e825e2045dd24fd8cad0f379. Exact commands and versions are in C3/evidence.md. Independent Astra rectangle rerun is pending at drafting. No all-degree obstruction follows from this finite list.

## History

2026-10-31, Codex C3 developer, assigned gpt-6.1-sol xhigh, rules/base e949ef06895acd5463cdf8df7e0e5f795218f70f. The auditor suggested this cheap test as a development opening; its independent verification remains separate from development.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
