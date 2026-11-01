# PD-T?lattice-c3-codex-04 — An isolated degree-two periodic 3D fibre has axis-only factors

ID kind: PD-T. Aliases: C0-d3-n2-050; C3-8ea9e9f33e3d; (3,1,2) mod6 fibre.
Split from: rank-survivor family in c3-rank-observations.md. Split into: none. No n-dependent extension is claimed.

## Statement

Let K be any field and let X=(x0,x1,x2),Y=(y0,y1,y2,y3),Z=(z0,z1,z2,z3,z4) have pairwise distinct entries within each list. Select the ten indices in the primitive single congruence fibre

`3i+j+2k=0 mod6` in `[0,2]x[0,3]x[0,4]`, namely

`000,003,022,111,114,130,133,200,203,222`.

In that row order and columns `(1,z,y,x,z²,yz,y²,xz,xy,x²)`, the total-degree-two determinant equals `-F_X F_Y F_Z`, where

`F_X=(x1-x0)(x2-x0)^3(x2-x1)`,

`F_Y=(y2-y0)^2(y3-y0)(y3-y1)*(y2-y3-y1+y0)`,

`F_Z=(z3-z0)^3(z4-z1)*(z3-z4-z1+z0)`.

Consequently this set is unisolvent for Pi_2(K) iff both `y2-y3-y1+y0` and `z3-z4-z1+z0` are nonzero. It is unisolvent whenever the Y and Z lists are strictly monotone real lists (either orientation independently); no order assumption on X beyond distinctness is needed.

## Status by part

Overall status: PROVED (direct developer proof below; independent Astra reconstruction pending). The floating Lebesgue value belongs to the separate MEASURED record. Candidate is a finite-degree surviving example, not an accepted unbounded-degree 3D analogue of Padua points.

## Direct proof

Independently apply affine changes to each axis, sending its first two entries to0,1. These operations multiply the evaluation determinant by the fifth power of each axis scale: by determinant expansion the exponent sum for each axis is binomial(5,4)=5. Write normalized remaining labels as

`X=(0,1,u), Y=(0,1,v,w), Z=(0,1,r,s,t)`.

We show that the normalized determinant is

`-u³(u-1)*v²*w*(w-1)*(v-w-1)*s³*(t-1)*(s-t-1).` (1)

Replace the x² column by x²-u*x. Subtract each of the first three x=0 rows from its matching x=u row. The three bottom rows now have support only in columns x,xz,xy; their determinant in those columns is u³*s*v. Laplace expansion along them has positive sign in the stated row/column order. In the remaining seven rows the modified x² column is0 on x=0 and1-u on x=1. Hence the full determinant is `u³*s*v*(1-u)*E`, where E is the7x7 bivariate evaluation determinant with columns `(1,z,y,z²,yz,y²,Q)` and rows

`(y,z,Q)=(0,0,0),(0,s,0),(v,r,0),(1,1,1),(1,t,1),(w,0,1),(w,s,1)`.

In E, subtract row6 and row2 from row7 and add row1 (one-based row labels). The resulting final row has only its yz entry w*s. Expanding there gives a positive factor w*s. In the remaining6x6 determinant, replace the (0,s,0) row by its difference with (0,0,0), extracting s. Replace the (1,t,1) row by its difference with (1,1,1), extracting t-1. The two normalized rows have (z,z²) entries (1,s) and(1,t+1). Subtract the former from the latter and expand in its sole z² entry; the cofactor sign cancels the sign in t+1-s. Expanding next in the normalized (0,s,0) row's sole z entry leaves the4x4 matrix with columns(1,y,y²,Q) at y/Q pairs `(0,0),(v,0),(1,1),(w,1)`. Its determinant, after expansion in the first row, is

`det[[v,v²,0],[1,1,1],[w,w²,1]] = v*(w-1)*(v-w-1).`

Thus `E=w*s²*(t-1)*(s-t-1)*v*(w-1)*(v-w-1)`, giving(1). This proof uses only determinant row/column operations and polynomial identities; its initially used divisions by distinct affine axis scales are legitimate. Multiplying back those scales yields exactly the displayed F_X,F_Y,F_Z. The normalized result is polynomial and the calculation is integral, so it specializes in every characteristic.

Within-axis distinctness makes all difference factors displayed outside the two additive brackets nonzero, proving the iff. For a decreasing Y list, `(y2-y3)+(y0-y1)>0`; for an increasing one both summands are negative. The analogous bracket for Z is `(z3-z4)+(z0-z1)`. Therefore the ordered-real assertion follows.

## Per-pattern properties

(a) Periodic: primitive single index congruence modulo6. (b) Axis-factorized determinant and explicit iff above, in all fields with enough distinct nodes. (c) Chebyshev–Lobatto case: unisolvent by monotonicity; numerical condition2=4.8972493901 and sampled Lebesgue lower bound5.8480519591 on the21³ Lobatto mesh (MEASURED only). The true Lebesgue maximum and any higher-degree continuation are unknown.

## Checks and sources

c3_lowdegree.py directly computes the normalized10x10 symbolic determinant by SymPy domain-ge, factors it, and verifies expansion equality; lowdegree.json SHA256c23ee5bf0ca2bc22576628965e882360e1ea66821f50d1e1d7030791b3650b8d. The direct proof is separate from the CAS calculation. Four-axis rectangle tests were inconclusive, correctly retained rather than promoted into a factorization proof. Closest predecessors: 2D axis factorization PD-T001/T002 and lower-set/product-grid determinant techniques; no novelty claimed. Literature comparison to named 3D families remains coverage-qualified.

## Limitations / history

Only n=2 and this fixed fibre are proved. Repeating the same k,a on longer consecutive grids need not have the required cardinality and is a separate candidate, to be tested before any launch. 2026-10-31, Codex C3 developer, assigned gpt-6.1-sol xhigh, rules/base e949ef06895acd5463cdf8df7e0e5f795218f70f. Further substantive continuation is not automatic without a separated cardinality-valid higher-degree pattern.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
