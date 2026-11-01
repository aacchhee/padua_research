# PD-T?lattice-c0-codex-01 — Density requirement for fixed congruence fibers

ID kind: PD-T. Aliases: fixed-modulus cardinality screen; factorial density.
Split from: none. Split into: none.

## Statement

Fix d>=1, k>=1, integers b_1,...,b_d, a primitive character coefficient vector a in (Z/k)^d (meaning `gcd(k,a_1,...,a_d)=1`), and a set C of q residues modulo k. For all sufficiently large integers n let L_j=n+b_j>0 and

`S_n={i in product_j {0,...,L_j-1}: sum_j a_j*i_j in C (mod k)}`.

Then `|S_n|=(q/k)n^d+O(n^(d-1))`. If `|S_n|=binom(n+d,d)` for infinitely many n, necessarily `q/k=1/d!`. In particular a single primitive fiber requires `k=d!`; unions of fibers require `d!` to divide k and `q=k/d!`. For d3 and k2,...,6, the only possible such infinite family is a single fiber modulo6. For d2 a single-fiber infinite family requires modulo2; the density-compatible nonempty unions for k2,...,6 have (k,q)=(2,1),(4,2),(6,3).

## Definitions and assumptions

All parameters other than n are fixed; in particular k does not grow with n, offsets do not change with n, and C is fixed. No field, axis nodes, determinant, interpolation or cubature hypotheses enter. Primitivity is essential: a nonprimitive encoding must first be reduced to its image group; a huge redundant modulus does not change the density argument.

## Status by part

Overall status: PROVED (developer-written elementary proof; independent Astra reconstruction pending; acceptance not claimed).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Asymptotic density and necessary equality | PROVED | Complete counting proof below |
| Unisolvence or stability of any surviving family | OPEN, outside statement | Separate C3 obligation |

Candidate / claim disposition: retained screening lemma, no novelty claim.

## Depends on

Only elementary finite-group counting and the leading term of `binom(n+d,d)`. No charter result or unread literature theorem is used.

## Proof

The homomorphism `phi:(Z/k)^d -> Z/k`, `phi(r)=sum a_j*r_j`, is surjective: Bezout's identity applied to `k,a_1,...,a_d` gives a preimage of1. Every fiber has k^(d-1) elements, since its fibers are translates of the kernel and k equal fibers partition k^d elements. Thus every translated full k-by-...-by-k index block has exactly q*k^(d-1) selected points.

Partition each axis into floor(L_j/k) full k-blocks and a remainder of length<k. The Cartesian product of the full blocks has volume `product_j (k*floor(L_j/k))=n^d+O(n^(d-1))`. The remaining boundary has O(n^(d-1)) points, because d,k,b are fixed. Full-block selection is exactly q/k of full-block volume, and boundary selection lies between0 and its volume. This proves the asymptotic statement. Dividing an infinite sequence of exact cardinality equalities by n^d and taking n->infinity gives q/k=1/d!. The divisibility consequences follow because q is an integer.

## Checks

This is an analytic proof, not an inference from catalogue samples. Finite enumeration illustrating its compatible/incompatible small-n cases is `topics/lattice-unisolvence-20261031/directions/C0/count-trials.json`; it is not load bearing. Independent reconstruction remains pending.

## Sources, scope and open items

This elementary screen is a variant of standard periodic counting, with no publication novelty claim. Closest campaign entries read: IDEA-012/013/029 and the complete U2 record. It does not rule out isolated n at another modulus, changing parameters with n, zero-coefficient cylinders after proper primitive reduction, nonconsecutive axes, growing offsets, boundary corrections, or nonperiodic sets. All properties of physical interpolation nodes remain unproved here. Next: independent Astra reconstruction and C3 rank checks of density-compatible tuples.

## History

2026-10-31, Codex assigned gpt-6.1-sol xhigh, rules/source e949ef06895acd5463cdf8df7e0e5f795218f70f. Scope explicitly fixed before enumeration in C0/frozen-scope.md. This result was not used to erase finite cardinality matches at k!=d!.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
