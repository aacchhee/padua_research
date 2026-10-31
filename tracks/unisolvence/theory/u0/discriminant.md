# PD-T006 — Squared Padua Vandermonde in Dickson coordinates

ID kind: PD-T. Aliases: Padua discriminant, closed-form squared determinant.
Split from: supplied finite_field_padua.md Theorem 3.
Split into: none.

## Statement

Under `PD-T004`, let `A` be the total-degree monomial evaluation matrix at `(X,Y)=(2x,2y)` with columns `X^aY^b`, `a+b<=n`, and `N=(n+1)(n+2)/2`. Then

`det(A)^2 = 2^((n²+3n+6)/2) [n(n+1)]^N`.

For the characteristic-zero cyclotomic nodes, `(X,Y)` are algebraic integers. Reducing their labelled `N`-row matrix at any prime ideal of residue characteristic `p` gives a nonsingular matrix if and only if `p` does not divide `2n(n+1)`. Thus bad-characteristic reduction of this canonical integral construction cannot retain `N` distinct unisolvent nodes.

## Definitions and assumptions

Matrix row and column order is arbitrary because the determinant is squared. The bad-characteristic corollary reduces the integral Dickson coordinates; cosine coordinates with denominator `2` have no corresponding integral reduction at `p=2`.

## Status by part

Overall status: **PROVED** (complete developer derivation; supplementary Astra check complete; required Claude audit PENDING). No novelty verdict.

## Depends on

[gram-unisolvence.md](gram-unisolvence.md), `PD-T004`. Elementary determinant and integral-reduction arithmetic. No source theorem inherited.

## Proof

Let `V` denote the Chebyshev matrix there. There are `n(n+1)/2` basis indices with positive x exponent and the same number with positive y exponent. With the exceptional diagonal norm replacing `1/2` by `1`,

`det D = 2^(1-n(n+1))`.

Exactly two corners satisfy the even-parity condition. Counting vertical and horizontal boundary incidences gives `n+2+n+1=2n+3`; subtracting the two repeated corner incidences leaves `2n+1` distinct boundary nodes, hence `2n-1` noncorner boundary nodes. Corners have weight `1/[2n(n+1)]`, other boundary nodes `1/[n(n+1)]`, and interior nodes `2/[n(n+1)]`. Consequently

`det W = 2^(N-2n-3) [n(n+1)]^(-N)`.

This count includes `n=1`: two corners, one noncorner boundary point and no interior points. The Gram determinant now gives

`det V² = 2^(4+n-n²-N) [n(n+1)]^N`.

For `r>=1`, `T_r(X/2)` has leading coefficient `1/2` in `X`; `T_0=1`. All lower terms have smaller degree. The product-basis change from monomials in `(X,Y)` to these Chebyshev products is triangular with determinant `2^(-n(n+1))`. Thus `det A²=2^(2n(n+1)) det V²`. Combining exponents and substituting `N=(n²+3n+2)/2` gives `(n²+3n+6)/2` as required.

In characteristic zero, every `X_j=zeta^j+zeta^-j` and `Y_k=eta^k+eta^-k` is an algebraic integer. The displayed equality is therefore an equality of algebraic integers and can be reduced at any prime ideal. Its right side is nonzero in the residue field exactly when `p` does not divide `2n(n+1)`; a field element has nonzero square exactly when it is nonzero. This proves the reduction statement, including `p=2` for the integral coordinates.

## Checks and sources

The unmodified source modular checks passed in 76 cases. The source floating-point calculation for `1<=n<=12` is only an observation about log determinants; it is not an exact determinant check or a bound on relative determinant error. Independent developer code also checks `q=3,9` exactly. See [measurements.md](measurements.md) and the U0 evidence manifest.

Supplied Theorem 3 and predecessor records `LIT-002`, `LIT-003` are provenance, not proof dependencies. Original papers and priority remain unverified.

## Scope and open items

The formula is the squared monomial determinant in the specified coordinates, not the unsquared determinant or an arbitrary point normalization. It does not state that every unisolvent set of the same size is impossible in bad characteristic. Supplementary Astra check complete; required Claude audit pending.

## History

2026-10-31, Codex U0; rules/base `d36722823441dc40c6e19d69a174459348dd309c`; assigned `gpt-6.1-sol xhigh`. Recomputed both determinant exponents and the `n=1` boundary count; scoped the bad-characteristic corollary to integral canonical reduction.
