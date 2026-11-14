# PD-T?padua-xu-lebesgue-20261114-claude-22 — λ_n(±1, −1) = n + 1 for Morrow–Patterson points

ID kind: PD-T.
Aliases: X2-22; lower-vertex value; target T1 of round X2-2.
Split from: none.
Split into: none.

## Statement

For every even n ≥ 2, the Lebesgue function of the Morrow–Patterson points MP_n (interpolation in Π_n) satisfies

λ_n(1, −1) = λ_n(−1, −1) = n + 1.

More precisely, with the notation of X2-21, for every node (p, q) ∈ 𝒩:
ℓ_{p,q}(1, −1) = (−1)^{p+1} ω_{p,q}/(4(x_p + y_q)²) and ℓ_{p,q}(−1, −1) = (−1)^{p+1} ω_{p,q}/(4(x_p − y_q)²), so that sgn ℓ_{p,q}(±1, −1) = (−1)^{p+1} = U_n(x_p).

Equivalently (closed sums): Σ_{(p,q)∈𝒩} (1 − x_p²)(1 − y_q²)/(x_p + y_q)² = Σ_{(p,q)∈𝒩} (1 − x_p²)(1 − y_q²)/(x_p − y_q)² = (n+1)(n+2)(n+3)/2.

## Definitions

As in X2-21: M = n + 2, N = M(M+1), 𝒩, x_p = cos(pπ/M), y_q = cos(qπ/(M+1)), ω_{p,q} = 8(1 − x_p²)(1 − y_q²)/N, ℓ_{p,q}, λ_n = Σ|ℓ_{p,q}|. In the (m, k) indexing of the literature p = m.

## Assumptions

n even, n ≥ 2.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Sign pattern sgn ℓ_{p,q}(±1,−1) = (−1)^{p+1} | PROVED | X2-21 part 3 |
| λ_n(±1, −1) = n + 1 | PROVED | proof below |
| The two closed sums | PROVED | restatement |

Candidate / claim disposition: none.

## Depends on

- X2-21 (`…-claude-21`): part 1 (reproduction f = Σ f(z)ℓ_z on Π_n) and part 3 (vertex formulas at (1,−1), (−1,−1)).

## Checks

- `python3 code/mp/research/x2_corner_checks.py ident`: |λ_n(1,−1) − (n+1)| and |λ_n(−1,−1) − (n+1)| ≤ 7e−38 for n ∈ {2,4,6,8,10,12,16,20,24,30} (closed forms, 40 digits; for n ≤ 12 the closed forms are also compared with the defining kernel sums).
- The path-A interval certificate `evidence/mp-cmp-certificate.json` (orchestrator, independent code path, even n ≤ 30) has enclosures of λ_n(±1,−1) containing n + 1 (width 2e−45); confirmed by the same run (`pathA_(1,-1)_contains_n+1: True`).
- Independent rerun: pending (auditor).

## Sources

- LITERATURE (contradicted, see PD-N…-30): BBDM, Constr. Approx. 63 (2026) §7 p. 63 report corner values (n+1)(n+2)/2 at each corner.

## Proof or evidence

By X2-21 part 3, ℓ_{p,q}(1,−1) = (−1)^{p+1} ω_{p,q}/(4(x_p + y_q)²) with ω_{p,q} > 0 and x_p + y_q ≠ 0; so |ℓ_{p,q}(1,−1)| = (−1)^{p+1} ℓ_{p,q}(1,−1).
With w = pπ/M and n + 1 = M − 1: U_n(x_p) = sin((M−1)w)/sin w = sin(pπ − w)/sin w = −(−1)^p = (−1)^{p+1}.
Hence λ_n(1,−1) = Σ_𝒩 U_n(x_p) ℓ_{p,q}(1,−1). The polynomial f(x, y) := U_n(x) lies in Π_n, so by X2-21 part 1 the sum is f(1, −1) = U_n(1) = n + 1.
The same argument at (−1,−1), where ℓ_{p,q}(−1,−1) = (−1)^{p+1} ω_{p,q}/(4(x_p − y_q)²), gives λ_n(−1,−1) = U_n(−1) = (−1)^n (n+1) = n + 1 (n even).
Finally λ_n(1,−1) = (8/N) Σ (1−x_p²)(1−y_q²)/(4(x_p+y_q)²) = n + 1 gives the first closed sum (N = (n+2)(n+3)), and likewise the second. ∎

Remark (mechanism). At the two lower vertices the alternating function (−1)^{p+1} that realises the Lebesgue sum is the restriction to the nodes of a polynomial of the interpolation space (U_n(x)), so the Lebesgue function equals that polynomial's value. At the upper vertices the sign pattern is (−1)^p except on a thin band of nodes below the diagonal (X2-23), and that band carries the n² growth.

## Scope

Exact for every even n ≥ 2, at the two vertices (±1, −1) only.

## Open items

None.

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-2; uncommitted at writing. First version.
