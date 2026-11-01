# PD-T?lattice-c0-codex-02 — Infinite cardinality-admissible three-dimensional fibers

ID kind: PD-T. Aliases: six-periodic diagonal fibers; consecutive lengths modulo6.
Split from: none. Split into: none.

## Statement

For every integer n>=0 and c in {0,...,5}, let

`S_(n,c)={(i,j,l): 0<=i<n+1, 0<=j<n+2, 0<=l<n+3, i+j+l=c (mod6)}`,

and N_n=binom(n+3,3). Then `|S_(n,c)|=N_n+E_(r,c)`, where r=n mod6 and

| r \ c | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
|0|0|1|1|0|-1|-1|
|1|-2|-1|1|2|1|-1|
|2|0|-1|-1|0|1|1|
|3|0|0|0|0|0|0|
|4|0|0|0|0|0|0|
|5|0|0|0|0|0|0|

Consequently every fiber has exactly N_n points for n≡3,4,5 mod6; fibers c=0,3 also do for n≡0,2 mod6; no fiber does for n≡1 mod6. In particular a fixed primitive character has correct cardinality for infinitely many n.

## Definitions and assumptions

This is a statement on index counts only. The box has lengths n+1,n+2,n+3, not maximum indices of those values. Its total volume is6*N_n. Arbitrary physical axis labels can be attached, but no determinant conclusion follows.

## Status by part

Overall status: PROVED (developer-written elementary proof; independent Astra reconstruction pending; acceptance not claimed).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact correction table and infinite cardinality existence | PROVED | Written recurrence and explicit coefficient lists below |
| Generic unisolvence, axis factorization, Lebesgue growth | OPEN, outside statement | C3 and later structural work |

Candidate / claim disposition: retained counting family, no novelty claim.

## Depends on

Elementary cyclic convolution only; no charter result or external theorem.

## Proof

For an axis of length L define h_L(t)=the number of indices in {0,...,L-1} congruent to t modulo6. Then `h_(L+6)=h_L+u`, where u is the length6 all-ones vector. Write cyclic convolution as *. The count vector is `F_n=h_(n+1)*h_(n+2)*h_(n+3)`. For any vector v, `u*v=(sum v)u`; also u*u=6u. Expanding the three factors at n+6 shows F_(n+6)-F_n is uniform, with each entry

`((n+7)(n+8)(n+9)-(n+1)(n+2)(n+3))/6 = N_(n+6)-N_n`.

This follows either by summing the expanded uniform terms or by observing that their common value is the change in total box volume divided by6. Thus E_n=F_n-N_n*u is6-periodic.

For n=0,1,2, multiply `(1+z+...+z^n)(1+z+...+z^(n+1))(1+z+...+z^(n+2))`, then add coefficients whose exponents agree modulo6. The resulting residue count vectors are respectively

`F_0=(1,2,2,1,0,0)`, `F_1=(2,3,5,6,5,3)`, `F_2=(10,9,9,10,11,11)`.

For explicit verification, the ordinary coefficient lists are `(1,2,2,1)` at n0, `(1,3,5,6,5,3,1)` at n1, and `(1,3,6,9,11,11,9,6,3,1)` at n2. Subtracting N_0=1,N_1=4,N_2=10 gives the first three rows. For n=3,4,5 one axis has length6. Hence its h vector is u, and convolution with the other axes is uniform with value product_j L_j/6=N_n. This gives the last rows. Six-periodicity completes the proof.

## Checks

`c0_catalogue.py` separately compares direct point enumeration and residue convolution for every finite canonical tuple, and checks the uniform-count identity at n=3,4,5,9,10,11. Those checks are supplementary; the displayed recurrence and coefficient lists prove the infinite statement without extrapolating a finite sample. Commands and hashes are in C0/rounds.md. Independent Astra reconstruction pending.

## Sources, scope and open items

The periodic pattern addresses the precise counting opening deferred in IDEA-013/029, but cardinality alone is elementary and is not offered as a new interpolation family. Literature baseline coverage limitations remain. Properties: (a) periodic/character-defined yes; (b) axis factorization/analogous unisolvence criterion unknown; (c) Lebesgue growth unknown. In particular this does not imply any analogue of Padua stability or any cubature property. Next: C3 ranks and independent reconstruction.

## History

2026-10-31, Codex assigned gpt-6.1-sol xhigh, rules/source e949ef06895acd5463cdf8df7e0e5f795218f70f. Initial sufficient observation n≡3,4,5 was sharpened to the full correction table; the extra matches at n≡0,2 are retained rather than silently omitted. No mistaken claim of uniformity for every n was made.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
