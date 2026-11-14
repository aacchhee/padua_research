# PD-T?padua-xu-lebesgue-20261114-claude-07 — Sharp expansion of the Xu Lebesgue constant; verdict on BCDMV Conjecture (17)

ID kind: PD-T.
Aliases: X1-07; T2; G2 expansion; Xu vertex expansion; Conjecture (17) of BCDMV 2006; relation to the Padua corner value.
Split from: round X1-2 target T2 and BRIEF §1.2 outcomes 1 and 3.
Split into: the exact value is X1-03/X1-04, the maximizer set X1-05, the one-dimensional enclosure X1-06; this record only combines them.

## Statement

Let n ≥ 1 and v ∈ V* (all four vertices for n even; (1,−1), (−1,1) for n odd). Put

 c₁ = (2/π)(γ + log(8/π)), A_n = (2/π) log n + c₁, b = (4/π) c₁ = (8/π²)(γ + log(8/π)), c = c₁² = (4/π²)(γ + log(8/π))².

**(a) Expansion (expansion variable N = n, onset n₂ = 1).**

  Λ^Xu_n = λ_n(v) = (4/π²) log² n + b log n + c + R_n,  0 < R_n < π A_n/(36 n²) + π²/(5184 n⁴) < (log n + 1.55)/(18 n²).   (1)

**(b) Next term.** R_n = π A_n/(36 n²) + E_n with −7A_n/(120π n⁴) < E_n < π²/(5184 n⁴). So

  Λ^Xu_n = (4/π²) log² n + b log n + c + (log n)/(18 n²) + π c₁/(36 n²) + O(log n / n⁴), with the explicit O-bounds above.   (2)

**(c) A clean explicit bound.** Λ^Xu_n ≤ ((2/π) log n + 1)² for every n ≥ 1, with equality only for n = 1.

**(d) Conjecture (17) of BCDMV 2006 (n even).** Both parts hold for every even n ≥ 2, in the following precise sense: Λ^Xu_n / ((2/π) log(n+1))² → 1 as n → ∞, and max_Q λ_n is attained exactly at the four vertices. The literal inequality Λ^Xu_n ≤ ((2/π) log(n+1))² is false for every n ≥ 1; the difference is b log n + O(1) → +∞. The same statements hold for odd n ≥ 3 with the two non-node vertices in place of the four vertices (variant, outside the published conjecture).

**(e) Relation to the Padua corner value.** With Λ_c(n) the Padua corner value and κ the constant of PD-T269: Λ_c(n) − Λ^Xu_n → κ as n → ∞ (all integers n), and for n ≥ 32, |Λ_c(n) − Λ^Xu_n − κ| ≤ 604 n^{−1/5} + ((log n + 2)² + 1)/(n+1).

Decimal values (certified enclosures, `code/xu/research/x1_constants.py`):
 c₁ = 0.962522826760713007798132068363…, b = 1.225522125742012093966888999272…, c = 0.926450192035433544660320512157….

## Definitions

As in X1-01 to X1-06. Natural logarithms; γ is Euler's constant.

## Assumptions

Exact real arithmetic; conventions of `literature-xu-mp.md` §1.

## Status by part

Overall status: **PROVED** (written consequence of X1-03 to X1-06; audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a), (b): expansion with explicit two-sided remainder, every n ≥ 1, both parities | PROVED | X1-03 (b), X1-04 (3), X1-06 (2); §1 |
| (c) | PROVED | §2 (uses certified decimal enclosures of γ, π, log(8/π)) |
| (d) Conjecture (17), even n, both parts; odd variant | PROVED | X1-04, X1-05; §3 |
| (e) Padua relation | PROVED | X1-03 (b) and PD-T269 (1), (2); §4 |
| Decimal enclosures of c₁, b, c; arb verification of (1), (2), (c) for n ≤ 300 | PROVED enclosures (interval arithmetic) / MEASURED verification | Checks |

## Depends on

X1-03 (b), X1-04 (3), X1-05, X1-06 (2); PD-T269 (merged) for (e). No fitted constant (G5): b and c are closed forms.

## Checks

- `python3 code/xu/research/x1_constants.py` (python-flint 0.9.0, 256 bits; run 2026-11-14): prints the enclosures of c₁, b, c above (radii < 2e−35); asserts by interval arithmetic c₁ + π/288 < 1, πc₁/36 + π²/5184 < 1.55/18, π/72 > 7/(240π), (2/π)log 2 < c₁; and verifies (1), (2) and (c) with arb enclosures of L_n for n = 1..300: `bounds of X1-07 verified in arb for n = 1..300`.
- `python3 code/xu/research/x1_vertex_check.py --nmax 200`: Path B vertex value = L_n² to 3.1e−59 (G2 acceptance, see X1-03).
- `python3 code/xu/research/x1_t0_pslq.py` (60 digits): Λ_c(n) − λ^Xu_n(v) = 1.0, 0.99836, 0.99551, …, 0.94738 for n = 2, 3, 4, …, 40, decreasing towards κ = 0.9197…; consistent with (e) (the convergence rate of PD-T269 is slow).

## Sources

- LITERATURE: BCDMV, Computing 76 (2006), eq. (17) p. 319 and Fig. 2 p. 318 (least-squares fit (0.95 + (2/π)log(n+1))² for n even ≤ 100); `literature-xu-mp.md` §4. The fit constant 0.95 is explained by c₁ = 0.9625… (and by the shift log(n+1) vs log n).
- LITERATURE: BdMV, JAT 141 (2006), Thm 1: Λ^Xu_n ≤ 8((2/π)log n + 5)² + 4. (c) replaces it by a bound with leading constant 1 instead of 8.
- No source read states (1). Novelty wording: "no matching result found in the documented search"; the gate must be re-run for the exact statements (see X1-04).

## Proof or evidence

**§1. (a), (b).** By X1-04 (3) and X1-03 (b), Λ^Xu_n = λ_n(v) = L_n². By X1-06 (2), L_n = A_n + ε_n − η_n with ε_n = π/(72n²) and 0 < η_n < 7/(240π n⁴); also η_n < ε_n (π/72 > 7/(240π)) and A_n ≥ A_1 = c₁ > 0. Since A_n² = (4/π²)log² n + b log n + c,

 R_n = L_n² − A_n² = (ε_n − η_n)(2A_n + ε_n − η_n) = 2A_nε_n − 2A_nη_n + (ε_n − η_n)².

All factors are positive, so R_n > 0, and R_n < 2A_nε_n + ε_n² = πA_n/(36n²) + π²/(5184n⁴). Further πA_n/36 = (log n)/18 + πc₁/36 and n⁻⁴ ≤ n⁻², so R_n < [(log n)/18 + πc₁/36 + π²/5184]/n² < (log n + 1.55)/(18n²) by the certified inequality πc₁/36 + π²/5184 < 1.55/18. This is (1). For (b), E_n = R_n − 2A_nε_n = −2A_nη_n + (ε_n − η_n)² lies strictly between −2A_n · 7/(240πn⁴) and ε_n². ∎

**§2. (c).** For n = 1, L_1 = cot(π/4) = 1. For n ≥ 2, L_n < A_n + π/(72n²) ≤ (2/π)log n + c₁ + π/288 < (2/π) log n + 1 by the certified inequality c₁ + π/288 < 1. Square. ∎

**§3. (d).** X1-04 (3) gives Λ^Xu_n = L_n² and X1-05 gives the maximizer set for n ≥ 2. By (1), L_n² = (4/π²)log² n (1 + O(1/log n)), and log(n+1)/log n → 1, which gives the limit. For the literal inequality: L_n > A_n = (2/π)log(n+1) + c₁ − (2/π)log(1 + 1/n) ≥ (2/π)log(n+1) + c₁ − (2/π) log 2 > (2/π) log(n+1), since (2/π) log 2 < c₁. ∎

**§4. (e).** PD-T269 (1): lim_n (Λ_c(n) − L_n²) = κ over all integers, and PD-T269 (2): for n ≥ 32, |Λ_c(n) − L_n² − κ| ≤ 604n^{−1/5} + ((log n+2)²+1)/(n+1). The L_n of PD-T269 (defined in PD-T159) equals the present L_n by PD-T270 eq. (2). Substitute L_n² = Λ^Xu_n. ∎

## Scope

- G2 is met at V* for every n ≥ 1 with N = n: closed forms for b and c, a sign-definite remainder, and the next term.
- (e) explains the T0 outcome structurally: the Xu vertex value is the "same-mesh reference" F_n = L_n² of the Padua corner analysis (PD-T159 (4)–(5)); the Padua corner value exceeds it by the mesh-mismatch constant κ in the limit. The two expansions share the log² and log coefficients (b is PD-T271's b) and differ in the constant: c_Padua = c + κ.
- In terms of the usual count of interpolation points nothing is claimed; n is Xu's degree parameter throughout.

## Open items

- Audit.
- Novelty gate for the exact statements (orchestrator/auditor).

## History

2026-11-14, Claude Fable 5.2 (xhigh), round X1-2 researcher. The assigned form "λ^Xu_n(v) = (4/π²)log²N + b log N + c + R_n, choose N" is met with N = n: because λ_n(v) is an exact square of a one-dimensional sum with an even expansion in 1/n, no 1/n term occurs and the remainder is O(log n / n²) with an explicit sign.
