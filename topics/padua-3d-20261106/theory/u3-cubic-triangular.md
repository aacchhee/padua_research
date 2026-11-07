# PD-T?padua-3d-20261106-codex-U3-01 — the cubic half-shift has a triangular alias inverse

ID kind: PD-T. Aliases: M40 z1411 sparse DCT inverse; alias paths.
Split from: none. Split into: none. No final ID allocated.

## Statement

Let theta_k=(2k+1)pi/40, k=0,...,19, and
X={(cos theta_k,cos4theta_k,cos11theta_k)}. In the product-Chebyshev
basis of Pi_3, its evaluation matrix factors V=B A, where
B[k,r]=cos(r theta_k),0<=r<20. A has a row/column ordering making it
triangular with diagonal absolute values ten1s, nine1/2s and one1/4.
Thus det(A) has absolute value2^(−11), X is unisolvent, and A^(-1)
has induced infinity norm4 and sum of absolute entries52.
The interpolation cardinal functions are explicitly

    ell_k(x)=v(x)^T A^(-1) d_k,
    d_k[r]=(1 if r=0 else2) cos(r theta_k)/20.

Consequently this representation gives the coarse rigorous bound
Lambda(X)<=103 on the cube. Its measured mesh values9.7888/9.8071
are separate observations, not this bound or a certified maximum.

## Definitions and assumptions

v(x) is the column of product-Chebyshev modes in the inherited order
in code/u3_constructions.py:modes. Rows of A are frequencies0..19;
columns are these20modes. The exact DCT reduction is the already proved
T8 cubic reduction; all required aliases are also displayed below.

## Status by part

Overall status: **PROVED**, direct finite symbolic proof below. The
independently executed sparse-class census and numerical observations
have their own records; no all-degree or novelty claim is made here.

Candidate disposition: retained explanation of an inherited example.
This does not revive the old determinant selector.

## Depends on

Elementary product-to-sum and cosine orthogonality, reconstructed here;
the predecessor is [T8 cubic classification](t8-r08-cubic-classification.md).
No external theorem, modular defect or numerical rank is a premise.

## Proof

At these angles cos((40−r)theta_k)=−cos(r theta_k),
cos(20theta_k)=0, and cosine has period80in its integer frequency.
Write b_r(k)=cos(r theta_k). The ten pure modes

    1,x,y,z,T2(x),T2(y),T2(z),T3(x),T3(y),T3(z)

are respectively b0,b1,b4,b11,b2,b8,−b18,b3,b12,−b7.
The remaining modes in the following order have these exact expansions:

| Mode | Expansion | New pivot frequency |
|---|---|---:|
|xy|(b3+b5)/2|5|
|xz|(b10+b12)/2|10|
|yz|(b7+b15)/2|15|
|T2(x)y|(b2+b6)/2|6|
|xT2(y)|(b7+b9)/2|9|
|T2(x)z|(b9+b13)/2|13|
|T2(y)z|(b3+b19)/2|19|
|xT2(z)|−(b17+b19)/2|17|
|yT2(z)|(b18−b14)/2|14|
|xyz|(b6+b8+b14+b16)/4|16|

Every nonpivot frequency in this table already occurred as a pivot in
an earlier pure/mixed column. All20frequencies occur exactly once as
pivots. Permuting rows into this pivot order gives triangular A and
the stated determinant; this is a direct check of the displayed symbolic
identities, rather than a floating determinant.

The same substitutions solve each original mode coefficient by backward
triangular substitution. In inherited mode order the exact row absolute
sums of A^(-1) are

    1,1,1,1,3,2,2,2,2,3,4,4,4,2,2,4,4,2,4,4.

They sum to52and have maximum4. These integers can be checked by
substituting the table and multiplying the resulting rational inverse;
the complete20-column sparse table and row sums are essential evidence
in [u3-s.json](../evidence/u3-s.json). Each row is also recoverable directly
from the displayed triangular identities, so no unavailable bulk output
is a premise. The constant-frequency column of A^(-1) has only its
constant-mode entry1, since A's constant column is the unit b0column.

Elementary discrete cosine orthogonality gives B^T B=diag(20,10,...,10).
For example apply2cosu cosv=cos(u−v)+cos(u+v) and sum the finite geometric
series; all nonconstant frequencies less40have zero real sum. Therefore
B^(-1)[r,k]=(1 if r=0 else2)cos(r theta_k)/20, proving the formula.
Since each product-Chebyshev mode has absolute value<=1on the cube,

    sum_k |ell_k(x)|
      <= sum_(a,r) |A^(-1)[a,r]| (1 if r=0 else2)
      = 2*52−1=103.

This completes the claimed finite bound and explicit reconstruction.

## Checks

Frozen producer source8c230e3a6bd857c8b3f8c63cd49a2c818d1449b60d9cb131c8662158ff8bc79b
actually ran S after published protocol3b5cb29f5d68306fa61d3079627247110911b552.
It reconstructed A by eight-sign expansion and rational inversion, and
certified actual distinct nodes at two splitting primes. Commands,
versions, all code/data identities and regenerate-only raw identity are
in the linked receipt. Separate U3 checker uses independent symbolic
substitution/leaf elimination and monomial actual-node checks; its final
executed scope is recorded in [usable-check3](../usable-check3.md).

## Sources, scope and open items

Known cosine aliasing and triangular elimination; shared gate and full
closest-body reading are in [usable3](../usable3.md). This explains the
moderate finite coefficient amplification of the inherited cubic example.
It does not establish an asymptotic Lebesgue law. The higher-degree sparse
support subclass is classified separately, and even-degree half-shifts
retain their existing trace obstruction.

## History

2026-11-07, Codex mathematical developer, assigned gpt-6.1-sol xhigh;
rules/input38227202bc6908d5a5a874950145761a8ca4312f. The cubic example
and its eight unisolvent generators were inherited, fully disclosed inputs.
The independent checker supplied a hand triangular pivot ordering after
the gate; the producer reconstructed all exact columns/inverse separately.
