# PD-T?bivariate-lanczos-claude-312 — Interior-node lemma for the two-term Turán certificate (Padua, all n ≥ 3)

Final ID: **PD-T068** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: interior lemma; Turán-type certificate (q_1² − q_0q_2, q_2² − q_1q_3); sine-sequence representation of generator gradients; R05.
Split from: none (supporting result for PD-T?…-313 and PD-N?…-303).
Split into: none.

## Statement

Let n ≥ 3, Padua points {(cos jπ/n, cos kπ/(n+1)) : j + k even}, q_m the normalised two-term generators of PD-T?…-309(c) (q_0 = −g_0/2^n, q_m = −g_m/2^{n−1} for 1 ≤ m ≤ 3), 0 < c < 1, and
 p_c := (1 − c)(q_1² − q_0 q_2) + c(q_2² − q_1 q_3).
Then p_c ∈ Π_{2n+1}, p_c and ∇p_c vanish at every Padua node, and at every INTERIOR node (0 < j < n, 0 < k < n+1) with S := sin²(jπ/n), T := sin²(kπ/(n+1)):
 Hess p_c is positive definite ⟺ 0 < c S T < 1/4.
In particular Hess p_c ≻ 0 at all interior nodes for every 0 < c < 1/4 (e.g. c = 1/10) and every n ≥ 3.

## Definitions / Assumptions

[EXACT]. T_k, U_k Chebyshev polynomials; g_m := T_{n−m}(x)T_m(y) − T_m(x)T_{n+1−m}(y).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| p_c ∈ S_1 (degree, double zeros) | PROVED | top forms x^m y^{n+1−m} cancel in q_1² − q_0q_2 and q_2² − q_1q_3; products of polynomials vanishing on the nodes |
| interior Hessian formula and PD criterion | PROVED | hand derivation below; symbolic + numerical checks |

## Depends on

PD-T?…-309(c) (vanishing of g_m at the nodes, top forms, interior gradients; PROVED there by trigonometric identities).

## Checks

`python3 r05_interior_identity.py` (sympy 1.13.3) → `directions/L3/logs/r05_interior_identity.log`: P = sin²α, R = sin²β, W = −(S − T)(8cST − 1), PR − W² = 16cST(S − T)²(1 − 4cST); numerical confirmation over 2000 random (θ, φ) ∈ (0, π)² (all cosine signs): max deviation 6.7e-16. Consistent with `r05_kappa_family.py` (interior minima > 0 for n = 2..12, c = 0.1, 0.2; log `r05_kappa_family.log`).

## Sources

None.

## Proof or evidence

Interior node: θ = jπ/n, φ = kπ/(n+1) ∈ (0, π), s := T_n(x) = (−1)^j. By 309(c), for a direction u, ∂_u g_m = s[a sin mθ cos mφ + b cos mθ sin mφ] with a = −n u_1/sin θ, b = (n+1) u_2/sin φ, i.e. ∂_u g_m = s[A sin mα + B sin mβ], α = θ + φ, β = θ − φ, A = (a+b)/2, B = (a−b)/2 ((A, B) ↔ u is a linear bijection; ∂_u g_0 = 0). So ∂_u q_m = −(s/2^{n−1}) v_m, v_m := A sin mα + B sin mβ, for m = 0..3, and since every q_m vanishes at the node, uᵀ Hess p_c u = (2/4^{n−1}) Q with Q := (1 − c)(v_1² − v_0v_2) + c(v_2² − v_1v_3), v_0 = 0.
Coefficients: v_1² gives A² sin²α + B² sin²β + 2AB sin α sin β. v_2² − v_1v_3: A²(sin²2α − sin α sin 3α) = A² sin²α (since sin x sin y = sin²((x+y)/2) − sin²((x−y)/2)); likewise B² sin²β; AB-coefficient 2 sin 2α sin 2β − sin α sin 3β − sin 3α sin β = (cos 4φ − cos 4θ) − (cos 4φ cos 2θ − cos 4θ cos 2φ) = 2S cos 4φ − 2T cos 4θ (product-to-sum with α ± 3β, 3α ± β expressed in θ, φ) = 2(S − T)(1 − 8ST) (cos 4γ = 1 − 8 sin²γ cos²γ). With sin α sin β = sin²θ − sin²φ = S − T:
 Q = sin²α A² + sin²β B² + 2W AB, W = (S − T)(1 − 8cST).
sin α, sin β ≠ 0 at interior nodes (θ ± φ ∉ πℤ: θ = φ or θ + φ = π would force n | j). Q is PD iff sin²α sin²β > W², i.e. (S − T)² > (S − T)²(1 − 8cST)², i.e. |1 − 8cST| < 1, i.e. 0 < cST < 1/4 (S ≠ T because sin²α sin²β = (S − T)² ≠ 0).

## Scope

Interior Padua nodes, all n ≥ 3. Boundary nodes: PD-T?…-313.

## Open items

None for this statement.

## History

2026-10-31T23:23+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer, round R05.
