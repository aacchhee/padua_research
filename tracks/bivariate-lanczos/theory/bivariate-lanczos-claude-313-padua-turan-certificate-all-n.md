# PD-T?bivariate-lanczos-claude-313 — Explicit certificate: for every n ≥ 4, P_n = 9(g_1² − ½g_0g_2) + (g_2² − g_1g_3) has double zeros and positive definite Hessians at all Padua nodes

ID kind: PD-T.
Aliases: Padua Turán certificate; all-n robust failure of (H) for Padua; R05.
Split from: none (supporting result for PD-N?…-303).
Split into: none.

## Statement

For every n ≥ 4, with g_m := T_{n−m}(x)T_m(y) − T_m(x)T_{n+1−m}(y), the polynomial
 P_n := 9(g_1² − ½ g_0 g_2) + (g_2² − g_1 g_3)  (= (10·4^{n−1}) p_{1/10} in the notation of PD-T?…-312)
has degree ≤ 2n+1, vanishes together with its gradient at every Padua point {(cos jπ/n, cos kπ/(n+1)) : j + k even}, and has a positive definite Hessian at every Padua point. Hence condition (H) fails robustly for the Padua points of every degree n ≥ 4.

## Definitions / Assumptions

[EXACT].

## Status by part

Overall status: CONDITIONAL.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| P_n ∈ S_1 | PROVED | PD-T?…-312 (first row) |
| interior nodes PD (all n ≥ 3, c = 1/10) | PROVED | PD-T?…-312 |
| boundary gradient formulas (edges, corners, sign reductions) | PROVED | Chebyshev identities below; floating cross-check max error 5.7e-14 (n = 3..8) |
| boundary quadratic forms: closed forms of A, B, X and 4AB − X² (E1, E3, C11) | CONDITIONAL | obtained by exact symbolic expansion (sympy, `r05_boundary_proof.py`); short polynomials, hand-checkable; obligation: independent rerun or hand check |
| positivity of 4AB − X² and of A or B (n ≥ 4) | PROVED given the row above | elementary bounds below |

## Depends on

PD-T?…-309(c), PD-T?…-312.

## Checks

`python3 r05_boundary_proof.py` → `logs/r05_boundary_proof.log` (gradient formulas vs direct differentiation; closed forms; s-polynomials; exact n = 4 node values). End-to-end MEASURED check `python3 r05_direct_check.py 3 14` → `logs/r05_direct_check.log`: deg P_n ≤ 2n+1, node values/gradients at rounding level, minimal Hessian eigenvalue over nodes 3.06, 1.49, 0.80, 0.46, 0.28, 0.18, 0.12, 0.087, 0.063, 0.046, 0.034 for n = 4..14, and −225 for n = 3 (the certificate does not work at n = 3; n = 3 is PD-N?…-301 with a different p*). Environment: Python 3.13.18, sympy 1.13.3, numpy 2.5.3. No independent rerun yet.

## Sources

None.

## Proof or evidence

Normalisation: q_0 = −g_0/2^n, q_m = −g_m/2^{n−1} (1 ≤ m ≤ 3) have top forms x^m y^{n+1−m}; at a node Hess P_n(u,u) = 2·10·Q(w) with Q(w) := (9/10)(w_1² − w_0w_2) + (1/10)(w_2² − w_1w_3), w_m := ∂_u g_m (m = 1, 2, 3), w_0 := ∂_u g_0/2 (positive overall factors dropped).
Boundary gradients (t = cos φ or cos θ): using T_k(±1) = (±1)^k, T_k′(±1) = (±1)^{k+1}k², and at the nodes T_{n+1−m}(y) = (−1)^k T_m(y), U_{n−m}(y) = −(−1)^k U_{m−1}(y) (y = cos φ, sin φ ≠ 0), T_{n−m}(x) = (−1)^j T_m(x), U_{n−m−1}(x) = −(−1)^j U_{m−1}(x) (x = cos θ, sin θ ≠ 0):
 E1 (x = 1, 0 < φ < π, k even): ∇g_m = (n(n−2m)T_m(t), (n+1)U_{m−1}(t));
 E2 (x = −1, k ≡ n mod 2): ∇g_m = (−1)^{n+m}(−n(n−2m)T_m(t), (n+1)U_{m−1}(t));
 E3 (y = 1, 0 < θ < π, j even): ∇g_m = (−nU_{m−1}(t), −(n+1)(n+1−2m)T_m(t));
 E4 (y = −1, j ≡ n+1 mod 2): ∇g_m = (−1)^{n+m}(nU_{m−1}(t), −(n+1)(n+1−2m)T_m(t));
 corners (1,1): (n(n−2m), −(n+1)(n+1−2m)); (1,−1) (n odd): (−1)^m(n(n−2m), (n+1)(n+1−2m)); (−1,1) (n even): −(−1)^m(n(n−2m), (n+1)(n+1−2m)); (−1,−1) is not a node.
Q contains only products w_jw_k with j + k even, so the factors (−1)^m drop out and E2, E4 and the corners (1,−1), (−1,1) reduce to E1, E3, C11 respectively under u_1 ↦ −u_1 or u_2 ↦ −u_2, which preserves positive definiteness.
Closed forms (symbolic expansion, see Checks), Q = A u_1² + X u_1u_2 + B u_2²:
 E1: B = (n+1)², (4AB − X²)/(n²(n+1)²) = (32/5)s² + n(121n − 1040)/100 · s + 99n²/100, s = 1 − t² ∈ (0, 1];
 E3: A = n², (4AB − X²)/(n²(n+1)²) = (32/5)s² + (n+1)(121n − 919)/100 · s + 99(n+1)²/100;
 C11: 4AB − X² = 99n²(n+1)²/25, A = n²(9n² − 36n + 80)/20 > 0 (negative discriminant).
Positivity: dropping (32/5)s² ≥ 0 leaves a linear function of s whose values at s = 0 and s = 1 are 99n²/100 and n(11n − 52)/5 (E1), 99(n+1)²/100 and (n+1)(11n − 41)/5 (E3). For E3 both are > 0 for n ≥ 4; for E1 both are > 0 for n ≥ 5. For n = 4, E1/E2 nodes have φ = kπ/5, and the exact values are (247 ± 89√5)/50 > 0 (247² = 61009 > 39605 = 89²·5). Since B > 0 (E1) and A > 0 (E3, C11) and 4AB − X² > 0, every boundary Hessian is PD. With PD-T?…-312 at interior nodes, all node Hessians are PD.

## Scope

All Padua degrees n ≥ 4 (this family of Padua points). n = 3: separate exact certificate (PD-N?…-301). n ≤ 2: (H) holds (PD-T?…-305, 306).

## Open items

Independent rerun / hand check of the three expansions; explicit radius δ_0(n) (exists by PD-T?…-303(e), not computed; it shrinks with n).

## History

2026-10-31T23:23+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer, round R05.
