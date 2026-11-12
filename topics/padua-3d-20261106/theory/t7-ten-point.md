# PD-T?padua-3d-20261106-codex-T7-05 — reproduced ten-point interpolation and cubature separation

ID kind: PD-T. Aliases: audit T1 NOTE-1 witness, H4×4 example.
Split from: none. Split into: none. Supports the OPEN T7 target.

## Statement and status

For H={(i,j,i+j)/4 mod1:i,j∈Z/4}, a=0, the cosine image is

    X={(x,y,z)∈{−1,1}³:xyz=1} ∪ {(±1,0,0),(0,±1,0),(0,0,±1)}.

It consists of10 distinct Π_2-unisolvent nodes, has monomial determinant
of absolute value256, and the original H is invariant under none of
the three coordinate reflections. Pushing uniform Haar measure on H
forward gives weight1/16 at each tetrahedral vertex and1/8 at each
axis point, exact on Π_2. No real weights on X are exact on Π_3 for
normalized product first-kind Chebyshev measure on the cube.

Overall status: PROVED by the elementary proof below; duplicate
verification of the supplied audited example, no novelty claim.

## Proof

Even-even indices give the four xyz=1 vertices, each once; the other
parity cases give the six axis points, each twice. This proves the
count, displayed set and Haar weights. The points (1/4,0,1/4) and
(0,1/4,1/4) and their reflected versions show that none of R1,R2,R3
preserves the defining congruence θ_3=θ_1+θ_2.

Let a quadratic p=c+ℓ·x+Σ_j A_jx_j²+Dxy+Exz+Fyz vanish on X.
Its values at ±e_j give ℓ_j=0 and A_j=−c. At the four vertices,
xy=z, xz=y, yz=x, so its remaining values are

    −2c+Dz+Ey+Fx.

The four vectors (1,x,y,z) form a Hadamard matrix of order4. Hence
c=D=E=F=0, and p=0. Dimension10 proves unisolvence. The same
elimination computes the absolute determinant: subtract paired axis
rows to pivot on the three linear columns, contributing2³. The three
remaining axis rows pivot on A_j with determinant1. Subtracting them
from each vertex row leaves the four columns (−2,z,y,x), whose
absolute determinant is2·16=32. Their product is256. Only determinant-
preserving row additions and permutations, besides these pivots, are
used, so this also proves the determinant value without software.

By sign symmetry all odd linear moments and distinct-coordinate
quadratic moments vanish. Each coordinate-square average is
4/16+2/8=1/2. These are precisely the continuous Chebyshev moments,
so the Haar weights integrate Π_2. At degree3 the only defective
monomial is xyz: its weighted sum is1/4, whereas its integral is0.

For arbitrary weights use the pointwise vanishing polynomial

    P=x²+y²+z²−2xyz−1.

It vanishes at both displayed types of nodes. Its continuous integral
is3/2−1=1/2. Thus every weighted rule on X has Q(P)=0≠I(P), even
if weights may be signed. No degree3 rule exists on these nodes.

## Dependencies, checks and scope

The vanishing cubic is the compatible relation u=(1,1,−1), q=3,
from [T7-02](t7-short-relation.md). This fixed unshifted plane family
therefore cannot interpolate Π_n for n≥3. Its failure is not an
exclusion of other rank-two groups or translations. The elementary
moment calculation proves the all-weight cubature impossibility;
positivity/quality need not be inferred from unisolvence.

[t7_cosets.py](../code/t7_cosets.py) reconstructs all16 torus points,
folds exactly with rational angles, and reproduces determinant−256
in its recorded basis/order and the single moment defect. The
independent checker reconstructs the same set without producer imports.
See evidence/t7-diagnostics.json and root's independent-checks ledger.
No published result is imported; source comparison: literature-T7.

2026-11-06, Codex, assigned gpt-6.1-sol xhigh, rules e5b6445.
Provisional ID; duplicate example retained for validation.
