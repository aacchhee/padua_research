# PD-N?mz-constants-codex-26 — strictly alternating node trials miss the degree constraint

ID kind: PD-N.
Aliases: full-space alternating vector obstruction; missing top Chebyshev coefficient.
Split from: M2 screening of supplied B2b test vectors.
Split into: none.

## Statement

For any N≥2 and any strictly positive numbers a_0,…,a_N, the polynomial interpolating v_k=(−1)^k a_k at the N+1 CC nodes has degree exactly N. Therefore a large inverse quotient for such a vector in Π_N does not by itself supply an upper bound for λ_min(CC,N−1).

## Definitions

If y is a vector normalized by CC weights, its polynomial values are v_k=y_k/√w_k. Endpoint c_k=2 and interior c_k=1.

## Assumptions

All a_k>0; degree-N cardinal interpolation at the exact CC nodes.

## Status by part

Overall status: PROVED (development; audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Positive alternating trial cannot satisfy top-coefficient constraint | PROVED | Exact inverse DCT coefficient |

Candidate / claim disposition: IDEA?mz-constants-codex-26 REJECTED: failed as a direct transfer to Π_(N−1).
Rejection reason: failed; statement does not exclude a separately corrected trial.

## Negative-result scope (PD-N only)

Attempted mechanism: directly use the supplied y_k=(−1)^k m_k^−1/2 full-space trial at degree N−1.
Parameter range: every N≥2, whenever all amplitudes are strictly positive.

## Depends on

Finite cosine interpolation; positivity of the CC weights from PD-T?mz-constants-codex-21.

## Checks

No floating or finite numerical dependency. Rules/base d36722823441dc40c6e19d69a174459348dd309c; independent audit pending.

## Sources

Supplied `bttbmap_b2b_cc_testvec.py`, SHA-256 34b1dbc0a08a2a7095241ae35407196b4510bf996cd0eb2716b1803374341d0c. The original script labels the full Π_N interpolation model; this is a warning against an invalid degree-restricted transfer, not a claim that its full-space computation is wrong.

## Proof or evidence

The coefficient of T_N in the interpolant is

    a_N^(Cheb)=(1/N)Σ_(k=0)^N (−1)^k v_k/c_k.

For v_k=(−1)^k a_k the sum is strictly positive. Thus it does not vanish, proving exact degree N. In normalized coordinates the admissibility constraint is Σ(−1)^k y_k/(c_k√w_k)=0, which the stated trial violates. The endpoint-cancelled harmonic U witness in PD-T?mz-constants-codex-22 is separately constructed within Π_(N−1).

## Scope

Only the direct unconstrained transfer is obstructed. Signed corrections and different explicit witnesses remain possible.

## Open items

Independent acceptance. No larger failure claim.

## History

2026-10-31, Codex subagent, gpt-6.1-sol xhigh (explicit orchestrator assignment); supplied vector screened before accepting any endpoint conclusion.
