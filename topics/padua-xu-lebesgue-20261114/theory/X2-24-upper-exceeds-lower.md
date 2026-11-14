# PD-T?padua-xu-lebesgue-20261114-claude-24 — λ_n(±1, 1) > n + 1 = λ_n(±1, −1) for every even n ≥ 2

ID kind: PD-T.
Aliases: X2-24; vertex inequality; first half of target T4(a) of round X2-2.
Split from: none.
Split into: none. The negative consequences for the published open questions are registered separately as PD-N?padua-xu-lebesgue-20261114-claude-29.

## Statement

For every even n ≥ 2, for the Morrow–Patterson points MP_n and interpolation in Π_n:

λ_n(1, 1) = λ_n(−1, 1) = (n + 1) + 2 Σ_{(p,q)∈𝒩∖B} A_{p,q} > n + 1 = λ_n(1, −1) = λ_n(−1, −1),

where A_{p,q} > 0 on 𝒩∖B (notation of X2-23) and 𝒩∖B ≠ ∅. Consequently Λ_n := max_Q λ_n ≥ λ_n(1,1) > n + 1.

## Definitions

As in X2-21 and X2-23: A_{p,q} = (−1)^p ℓ_{p,q}(1,1); B = {Y < X < κY}.

## Assumptions

n even, n ≥ 2.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| identity λ_n(1,1) − (n+1) = 2Σ_{𝒩∖B} A | PROVED | X2-23 (c) |
| strict inequality | PROVED | explicit node of 𝒩∖B below |

Candidate / claim disposition: none.

## Depends on

- X2-22 (λ_n(±1,−1) = n + 1); X2-23 (b), (c) (signs, band formula, λ_n(−1,1) = λ_n(1,1)).

## Checks

- `python3 code/mp/research/x2_corner_arb.py --nmax 60`: flag `gt_n+1` true for every even n ≤ 60 (ball arithmetic).
- `evidence/mp-cmp-certificate.json` (path A, independent): `claim_lam(1,1)_ne_lam(1,-1)` true for every even n ≤ 30.
- Independent rerun: pending (auditor).

## Sources

None used.

## Proof or evidence

By X2-23 (c), λ_n(1,1) = (n+1) + 2Σ_{𝒩∖B} A_{p,q}, and by X2-23 (b) every A_{p,q} with (p,q) ∈ 𝒩∖B is ≥ 0, and > 0 whenever X < Y. The node (p, q) = (M−1, 2) belongs to 𝒩 (M − 1 + 2 is odd, 2 ≤ M) and has x_p = cos((M−1)π/M) < 0 < cos(2π/(M+1)) = y_q, because 2π/(M+1) ≤ 2π/5 < π/2 for M ≥ 4. So X < Y there, the node lies in 𝒩∖B and contributes A > 0. Hence λ_n(1,1) > n + 1. The remaining equalities are X2-22 and X2-23 (c). ∎

## Scope

Strict inequality between the vertex values, for every even n ≥ 2. The size of the gap is given asymptotically by X2-25 (it is of order n²).

## Open items

None.

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-2; uncommitted at writing. First version.
