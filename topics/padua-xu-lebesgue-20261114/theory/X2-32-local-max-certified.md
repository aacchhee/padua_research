# PD-T?padua-xu-lebesgue-20261114-claude-32 — (±1,1) are strict local maxima of the Morrow–Patterson Lebesgue function for every even n with 2 ≤ n ≤ 3000 (computer-assisted)

ID kind: PD-T.
Aliases: X2-32; P1 finite range; first-variation certificate.
Split from: X2-28 plan item P1 ("(±1,1) are strict local maxima for every even n ≥ 2"), parameter range 2 ≤ n ≤ 3000.
Split into: none. The range n > 3000 stays OPEN (X2-28 addendum).

## Statement

For every even n with 2 ≤ n ≤ 3000:
1. ℓ_a(1,1) ≠ 0 for every node a of MP_n;
2. D_x(n) > 0 and D_y(n) > 0 (notation of X2-31); more precisely D_x(n) ≥ 0.01934·(n+2)⁴ and D_y(n) ≥ 0.02735·(n+2)⁴, the minima being attained at n = 2;
3. consequently (1,1) and (−1,1) are strict local maxima of λ_n on Q = [−1,1]².

## Definitions

As in X2-31.

## Assumptions

n even, 2 ≤ n ≤ 3000. Trusted: python-flint/Arb ball arithmetic (rigorous enclosures of sin(πr) for rational r and of field operations), and the script below.

## Status by part

Overall status: PROVED, computer-assisted; independent rerun pending (gate G3 requires it before a finite-degree claim is accepted).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| reduction of 1–3 to a finite ball-arithmetic check | PROVED | below |
| the check, even n ≤ 3000 | computed once by the developer (ball arithmetic, 192 bits) | `x2r3_first_variation_arb.py --band`; rerun pending |
| second code path, even n ≤ 24 | computed (defining sums, all nodes) | `--full` |

Candidate / claim disposition: none.

## Depends on

X2-31 (a), (c), (d); X2-23 (a), (b) (closed form and sign rule of A_{p,q}); X2-25 Step A (X > Y ⟺ q' ≤ p'). X2-23 (f) is **not** used.

## Checks

- `python3 code/mp/research/x2r3_first_variation_arb.py --band --nmin 2 --nmax 3000 --out /tmp/x2r3/fv_band_2_3000.json` (python 3.13.18, python-flint 0.9.0, 192 bits; 2026-11-14; 106 s): `all_signs_certified: true`, `all_Dx_pos: true`, `all_Dy_pos: true`, `min_Dx_over_M4_lower: 0.019340…` and `min_Dy_over_M4_lower: 0.027351…` (both at n = 2). Samples (n, |B|, D_x, D_y, D_x/M⁴, D_y/M⁴): (2, 3, 4.95113, 7.00196, 0.019340, 0.027351); (10, 11, 795.051, 946.564, 0.038342, 0.045648); (100, 120, 5390657.80, 5516572.79, 0.049801, 0.050965); (1000, 1430, 5.15178e10, 5.16404e10, 0.051108, 0.051229); (3000, 4633, 4.157838e12, 4.161141e12, 0.051195, 0.051235). The same run reproduces λ_n(1,1) = 2Σ_B|A| − (n+1) (e.g. n = 100: 5323.272846703042299635419).
- Same run, extra flags (measured facts, not needed for the statement): `all_band_Tx_positive: true` (T_a > 0 at every band node, every n ≤ 3000) and `Ty_nonpositive_only_at_(1,2): true` (T'_a > 0 at every band node except the node (p,q) = (1,2), where T'_a < 0).
- `… --full --nmin 2 --nmax 24` (0.2 s): D_x, D_y from the defining kernel sums over all nodes, with signs of ℓ_a(1,1) certified node by node, agree with the band path to all printed digits; all positive.
- Output JSON is in /tmp/x2r3 (not committed; regenerable in 2 minutes).
- Independent rerun: pending (auditor; a rerun on a separate code path for all n ≤ 3000 would need the `--full` path, which costs O(n⁴) per n, or an independent implementation of the band path).

## Sources

None.

## Proof or evidence

*Reduction.* Fix n. Reindex nodes by p' = M − p, q' = M + 1 − q (p' ≡ q' mod 2), X = sin²(πp'/(2M)), Y = sin²(πq'/(2M+2)). By X2-23 (a), (b): A_{p,q} has the sign of −g, g := (M−½)X − (M+3/2)Y, when X > Y, and A_{p,q} > 0 when X < Y; X = Y does not occur. By X2-25 Step A, X > Y ⟺ q' ≤ p'. For fixed p', g strictly increases as q' decreases (Y decreases). The script scans, for each p' = 1..M−1, q' = p', p'−2, …; it adds the node to B when the ball of g is negative, and stops the column at the first q' whose ball of g is positive (or at q' < 1); a ball containing 0 aborts with `signs_certified: false`. By monotonicity, all nodes below the stopping node have g > 0. Hence, when the run reports `signs_certified: true`, the scanned set is exactly B, g ≠ 0 at every node with q' ≤ p', and so ℓ_a(1,1) ≠ 0 for every node (item 1). The script then encloses D_x = −n(n+1)(n+2)/3 + 2Σ_B T_a and D_y = 2Σ_B T'_a (X2-31 (c)) with T_a = −ωN_x/(4d⁵), T'_a = −ωN_y/(4d⁵), using d = 2(X−Y) = 2 sin(πS/(2N)) sin(πR/(2N)) (R = p'(M+1) − q'M, S = p'(M+1) + q'M), x = 2X − 1, y = 2Y − 1, 1 − x² = 4X(1−X), 1 − y² = 4Y(1−Y), ω = 8(1−x²)(1−y²)/N. Positivity of the two balls is item 2; item 3 is X2-31 (d). The bounds in item 2 are the reported lower ends of D/M⁴. ∎

## Scope

Finite range only. Nothing is claimed for n > 3000 or about global maxima.

## Open items

- Independent rerun.
- Analytic tail n > 3000 (OPEN): see X2-28 addendum (measured D_x/M⁴, D_y/M⁴ → d = 0.05123730576…, and the reduction to node-wise inequalities).

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-3; uncommitted at writing. First version.
