# PD-T?lattice-c3-codex-02 — Coordinate-layer and projected-count annihilator certificates

Final ID: **PD-T091** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T. Aliases: product cover; slice-removal dimension obstruction. Split from: none. Split into: catalogue certificate observations in c3-rank-observations.md.

## Statement

Let K be any field, n>=0 and I a finite subset of a three-axis index product. For any distinct within-axis lists H1,H2,H3, let S_I be the associated coordinate points.

(A) If index sets A1,A2,A3 cover every i in I, in the sense that some i_r belongs to A_r, and sum_r |A_r|<=n, then S_I is not unisolvent for Pi_n. An explicit nonzero annihilator is `prod_r prod_(j in A_r) (x_r-H_(r,j))`.

(B) Fix an axis r, remove q<=n of its coordinate layers indexed by A, and project all remaining triples onto the other two axes. If that index projection has cardinality strictly less than binomial(n-q+2,2), then S_I is not unisolvent for Pi_n, for every such axis specialization over K.

## Definitions and assumptions

Pi_n consists of formal polynomials of total degree<=n. Distinctness within axes is sufficient; no cross-axis distinctness or characteristic condition is needed. Unisolvence requires injectivity, so any formal nonzero degree<=n annihilator suffices. These are sufficient obstruction certificates; failure to find either says nothing about unisolvence.

## Status by part

Overall status: PROVED (developer written proof; independent Astra reconstruction pending). This is a general elementary result, independent of any enumerated certificate output.

## Proof

In (A), the displayed product is a formal nonzero polynomial because K[x1,x2,x3] is a domain and each factor is nonzero. Its total degree is the sum of the layer counts. At every selected triple one of its factors vanishes.

For (B), put m=n-q. Evaluation of bivariate Pi_m at the projected nodes is a linear map from a vector space of dimension binomial(m+2,2) into a space of strictly smaller dimension. Its kernel therefore contains a nonzero bivariate polynomial P. Multiply P, viewed as independent of x_r, by `prod_(j in A)(x_r-H_(r,j))`. The resulting polynomial is nonzero, has degree<=m+q=n, vanishes on removed layers by its product factors and on all remaining points by P. This proves both parts over every field. Even if projected coordinate values were to collide, their count could only decrease.

## Checks and limitations

c3_structure.py enumerates all coordinate-layer covers of degree<=n; c3_obstructions.py enumerates layer removal/projection counts. Their certificates are finite index objects, and checking each is enough to invoke this theorem. Exact computational scope and independent rerun status remain in C3/evidence.md and c3-rank-observations.md. No completeness claim for all annihilators or all singular patterns follows.

## Sources / novelty

Elementary dimension counting and product polynomials; closest campaign entries IDEA-013/029 and the lower-set background. No source theorem is a dependency and no novelty claim is made.

## History

2026-10-31, Codex C3 developer, assigned gpt-6.1-sol xhigh; rules/base e949ef06895acd5463cdf8df7e0e5f795218f70f.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
