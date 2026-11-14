# PD-T?padua-xu-lebesgue-20261114-claude-27 — measured behaviour of the remainder R_n = λ_n(1,1) + (n+1) − c*(n+5/2)² (Morrow–Patterson points)

ID kind: PD-T.
Aliases: X2-27; remainder of the vertex expansion; measured companion of X2-25.
Split from: none (a distinct measured claim, kept apart from the proved X2-25).
Split into: none.

## Statement

MEASURED, for even n in the scope listed under Checks (2 ≤ n ≤ 6400, 15 values in float64; every even n ≤ 60 in ball arithmetic):

1. R_n := λ_n(1,1) + (n+1) − c*(n+5/2)² is negative and decreasing in n on the sampled values: R_2 = −1.6228, R_10 = −2.8556, R_100 = −6.9715, R_1600 = −15.1402, R_6400 = −20.4203.
2. The second differences along doublings n ↦ 2n are nearly constant: with M = n + 2, R(M=802) − R(402) = −2.1451, R(1602) − R(802) = −2.3537, R(3202) − R(1602) = −2.5454, R(6402) − R(3202) = −2.7347; consecutive differences of these are −0.209, −0.192, −0.189. A remainder −a log²M − b log M − c would give 2a log²2 = 0.961a for these, i.e. a ≈ 0.20; the value a = 2/π² = 0.2026 fits, and then R_n + (2/π²) log²M = −3.72, −4.11, −4.48, −4.85 at M = 802, 1602, 3202, 6402 (slope ≈ −0.54 per unit of log M).
3. Decomposition (notation of X2-25; M = 1202, R_n = −14.1428): R_n = 2Σe₁ − 2Σ(c_Mĥ − 𝓜) + 2c_M(Σ_{r≥1}ĥ(ηr) − I/η) − 2c_MΣ_miss with Σe₁ = 0.8145, Σ(c_Mĥ − 𝓜) = 6.80 (majorised by ΣL_c + ΣL_s = 6.41 + 1.78, of which ΣL_c grows like log²M and ΣL_s stays bounded), 2c_M(Σĥ(ηr) − I/η) = +0.14 and 2c_MΣ_miss = 2.30 (growing like log M).
4. λ_n(1,1)/d_n, d_n = (n+1)(n+2)/2, is not monotone: 0.97426 (n=2), 1.00089 (6), 1.03197 (50), 1.033872 (200), 1.033958 (400), 1.033956 (800), 1.033925 (3200), 1.033917 (6400), with limit 2c* = 1.033907 (PROVED in X2-25) approached from above for large n.

Conjectural reading (OPEN, not claimed): R_n = −(2/π²) log²n + O(log n).

## Definitions

As in X2-25.

## Assumptions

None beyond the definitions; finite scope as listed.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| items 1–4 on the listed n | MEASURED | scripts below |
| R_n = −(2/π²) log²n + O(log n) | OPEN | plausible mechanism: the term L_c of X2-25 with its factor (1 − V̂) kept; no proof attempted |
| R_n = O(log²n) with explicit constants | PROVED elsewhere | X2-25 (not part of this record) |

Candidate / claim disposition: none.

## Depends on

X2-23 (closed form evaluated), X2-25 (definition of c*, proved bounds used only for comparison).

## Checks

- `python3 code/mp/research/x2_corner_checks.py table` (float64 band sums with exact integer angle numerators; c* = 0.516953653366806…): the R_n values above for n ∈ {2,4,6,8,10,20,30,50,100,200,400,800,1600,3200,6400}; wall time 21 s.
- `python3 code/mp/research/x2_corner_checks.py decomp`: the decomposition (item 3) for M ∈ {4,…,1202}.
- `python3 code/mp/research/x2_corner_arb.py --nmax 60`: R_n in ball arithmetic for every even n ≤ 60 (agrees with the float values to all printed digits, e.g. R_30 = −4.4900863, R_60 = −5.8301628).
- Float64 accuracy: the band terms are evaluated from X − Y = sin(πs/(2N)) sin(πr/(2N)) with integer r, s, so there is no cancellation; λ_n(1,1) for n ≤ 60 agrees with the ball-arithmetic values to ≥ 12 significant digits. For n = 6400 the absolute error of R_n is estimated below 1e−6 (not certified).
- Independent rerun: pending.

## Sources

None.

## Proof or evidence

Measured evidence only (see Checks). No general claim is made.

## Scope

The listed degrees. In particular "decreasing" and "negative" are observations on the sample, although R_n ≤ 7.66 and R_n ≥ −(0.4053 log²M + 2.9833 log M + 15.82) are proved for all even n (X2-25).

## Open items

- Prove the sharp log² coefficient (expected 2/π²) or the sign R_n < 0. Not needed for any current consequence.

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-2; uncommitted at writing. First version.
