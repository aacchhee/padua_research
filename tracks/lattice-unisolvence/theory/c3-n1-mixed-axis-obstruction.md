# PD-N?lattice-c3-codex-02 — A four-point 3D congruence fibre has an essential mixed-axis condition

ID kind: PD-N. Aliases: normalized t-s obstruction; primitive (2,1,1) mod4 fibre. Split from: none. Split into: broader measured rectangle tests in c3-rectangle-observations.md.

## Statement

Let K be a field and X=(x0,x1), Y=(y0,y1,y2), Z=(z0,z1,z2) be distinct within each list. Take n=1 and the single congruence fibre

`I={(i,j,k) in [0,1]x[0,2]x[0,2] : 2i+j+k=1 mod4}`

` = {(0,0,1),(0,1,0),(1,1,2),(1,2,1)}.`

In that row order and columns (1,z,y,x), the evaluation determinant is

`D=(x1-x0)*[(y2-y0)(z1-z0)-(z2-z0)(y1-y0)].` (1)

In particular over Q this periodic, cardinality-correct 3D pattern is generically unisolvent, but its unisolvence cannot be characterized by a conjunction of three conditions depending separately on X, Y and Z. Its determinant cannot be a product of three nonzero axis-only rational functions over Q.

## Negative-result scope

Attempted mechanism: extend the checkerboard's independent per-axis necessary-and-sufficient criterion to every cardinality-admissible primitive 3D congruence fibre. This one pattern refutes that universal extension over Q. It does not rule out mixed criteria, exceptional families, a different n-dependent construction or useful special-node interpolation.

## Assumptions and definitions

The index congruence is ordinary integer congruence; no fourth root of unity is needed in K. Formula (1) is an integral polynomial identity, so specializes in every characteristic. The no-independent-criterion conclusion below is stated over Q, where the listed values 0,1,2,3 are distinct as needed.

## Status by part

Overall status: PROVED (developer direct written proof; independent Astra reconstruction pending).
Candidate disposition: universal axis-only extension REJECTED: refuted within the stated class. This is not a rejection of 3D interpolation or of the surviving pattern itself.

## Proof

Independently translate each axis so its first label is zero. Translation gives a triangular monomial-column change of determinant one. Then divide each nonconstant monomial column by its corresponding nonzero axis difference x1-x0, y1-y0, z1-z0. The normalized axes are X=(0,1), Y=(0,1,t), Z=(0,1,s), and the normalized matrix is

`[[1,1,0,0],[1,0,1,0],[1,s,1,1],[1,1,t,1]].`

Subtract its first row from the remaining rows and expand along the first column. The remaining 3x3 determinant is t-s. Multiplying back the three axis differences gives (1). This is a direct determinant identity; the SymPy experiment merely found it.

For the independent-condition impossibility, fix X=(0,1). Both (t,s)=(2,3) and (3,2) give nonzero determinants. Any conjunction C_X(X) and C_Y(Y) and C_Z(Z) equivalent to unisolvence would therefore make C_Y true at t=2 and at t=3, and C_Z true at s=2 and at s=3. It would predict unisolvence at (t,s)=(2,2), whose determinant vanishes. This contradiction proves the assertion even for arbitrary predicates, not merely polynomial minors.

For rational product impossibility, any identity D=F(X)G(Y)H(Z) would imply the rectangle identity D(2,2)D(3,3)=D(2,3)D(3,2) on the normalized slices as a rational-polynomial identity. Here its sides are 0 and -1. This contradiction remains valid after clearing any axis-only denominators; it concerns polynomial identities, not chosen values at poles.

## Per-pattern properties

(a) Periodic: yes, a primitive index character fibre modulo4. (b) Structural criterion: exactly the mixed bracket in (1), nonzero; no axis-only conjunction over Q. (c) Chebyshev–Lobatto specialization: Y=Z=(1,0,-1) makes the bracket zero, so this particular Chebyshev set is exactly singular and has no interpolation Lebesgue constant. This last fact follows directly from (1), not from a floating rank threshold.

## Checks and sources

C0-d3-n1-035, C3-b083ccfa404b; C0-d3-n1-039 has the same selected triples, and C0-d3-n1-043 transports by x reversal. The direct proof is self-contained. Closest predecessor is the 2D axis factorization PD-T001/T002 and De Marchi–Usevich (LITERATURE); no novelty claim. A scientific acceptance decision still requires Astra reconstruction.

## History

2026-10-31, Codex C3 developer, assigned gpt-6.1-sol xhigh; rules/base e949ef06895acd5463cdf8df7e0e5f795218f70f. General axis-only hypothesis preserved and explicitly refuted by one scoped example; no higher-dimensional universal negative is inferred.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
