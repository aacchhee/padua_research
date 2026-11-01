# PD-T?bivariate-lanczos-claude-313 — Explicit certificate: for every n ≥ 4, P_n = 9(g_1² − ½g_0g_2) + (g_2² − g_1g_3) has double zeros and positive definite Hessians at all Padua nodes

Final ID: **PD-T069** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

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

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| P_n ∈ S_1 | PROVED | PD-T?…-312 (first row) |
| interior nodes PD (all n ≥ 3, c = 1/10) | PROVED | PD-T?…-312 |
| boundary gradient formulas (edges, corners, sign reductions) | PROVED | Chebyshev identities below; floating cross-check max error 5.7e-14 (n = 3..8) |
| boundary quadratic forms: closed forms of A, B, X and 4AB − X² (E1, E3, C11) | PROVED | exact symbolic expansion (`r05_boundary_proof.py`); hand-checked and independently re-derived (n symbolic) by L3-reconstruction-02 (`review_L3b/turan_symbolic.py`), and the whole certificate independently verified exactly (rigorous rational interval arithmetic) for n = 4..16 (`review_L3b/padua_turan_check.py`, log `reviews/logs_L3b/padua_turan_check.log`); re-derived again (E1, E3, corner discriminants and the exceptional n = 4 values) and rerun by Codex audit-01 L3-certificates |
| positivity of 4AB − X² and of A or B (n ≥ 4) | PROVED | elementary bounds below |

## Depends on

PD-T?…-309(c), PD-T?…-312.

## Checks

`python3 r05_boundary_proof.py` → `logs/r05_boundary_proof.log` (gradient formulas vs direct differentiation; closed forms; s-polynomials; exact n = 4 node values). End-to-end MEASURED check `python3 r05_direct_check.py 3 14` → `logs/r05_direct_check.log`: deg P_n ≤ 2n+1, node values/gradients at rounding level, minimal Hessian eigenvalue over nodes 3.06, 1.49, 0.80, 0.46, 0.28, 0.18, 0.12, 0.087, 0.063, 0.046, 0.034 for n = 4..14, and −225 for n = 3 (the certificate does not work at n = 3; n = 3 is PD-N?…-301 with a different p*). Environment: Python 3.13.18, sympy 1.13.3, numpy 2.5.3. Independent rerun: L3-reconstruction-02 (own exact code, no developer import): degree, exact double zeros, exact boundary gradient formulas and rigorous PD for n = 4..16; minima of λ_min(Hess P_n) 3.0587 (n = 4) … 0.02079 (n = 16), attained at the interior node (1,1); n = 3 fails (−225) as stated. The developer's floating values drift from n = 13 (monomial cancellation). Codex audit-01 L3-certificates (2026-11-01; `topics/bivariate-lanczos-20261031/audit-01/L3-certificates.md`) freshly executed `review_L3b/padua_turan_check.py 3 16` (n = 3 expected FAIL −225; n = 4..16 PASS), `review_L3b/turan_symbolic.py` (PASS) and its own independently written `audit-01/L3-certificates/independent_certificate_check.py` (symbolic interior determinant, E1/E3/corner discriminants: PASS); logs in that folder. Trusted dependencies: Python integers/fractions (reviewer exact code), sympy (developer's, reviewer's and auditor's symbolic expansions).

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

Explicit radius: for each n ≥ 4 a valid (chosen) radius δ_0(n) > 0 exists by PD-T?…-303(e). The certified lower bounds for the positivity radius ρ_n of P_n (L3-reconstruction-02, `padua_delta0.py`, a reviewer computation; fresh rerun with identical output by Codex audit-01 L3-certificates, `audit-01/L3-certificates/rerun_delta0.log`) decrease over n = 4..12: ρ_n ≥ 5.63e-4, 1.02e-4, 2.36e-5, 6.61e-6, 2.15e-6, 7.87e-7, 3.18e-7, 1.40e-7, 6.55e-8; floating samples find P_n < 0 at radii 3.4e-2 … 3.5e-4 from the binding node (MEASURED). Lower bounds cannot bound ρ_n from above, and P_n is one certificate among many: no uniform-in-n obstruction radius is established here, and neither ρ_n → 0 nor the absence of a uniform obstruction radius is proved. Both questions are OPEN (PD-T?…-319). A chosen radius may of course be taken nonincreasing in n.

## History

2026-10-31T23:23+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer, round R05.
- 2026-11-01T00:47:14+01:00, L3 developer (Claude Opus 5.5, xhigh requested): CONDITIONAL → PROVED citing the independent exact rerun and hand check; findings L7 (δ_0(n) → 0) and L13 (stale 'No independent rerun yet') of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1). Original wording of the replaced passages: «Overall status: CONDITIONAL.»; «| boundary quadratic forms: closed forms of A, B, X and 4AB − X² (E1, E3, C11) | CONDITIONAL | obtained by exact symbolic expansion (sympy, `r05_boundary_proof.py`); short polynomials, hand-checkable; obligation: independent rerun or hand check |»; «| positivity of 4AB − X² and of A or B (n ≥ 4) | PROVED given the row above | elementary bounds below |»; «No independent rerun yet.»; «Independent rerun / hand check of the three expansions; explicit radius δ_0(n) (exists by PD-T?…-303(e), not computed; it shrinks with n).».
- 2026-11-01T08:33:39+01:00, L3 developer (Claude Opus 5.5, xhigh requested): finding LC-M1 of Codex audit-01 (audit-01/L3-certificates.md; candidate 5ccfac2) — the inference «δ_0(n) → 0 … no radius uniform in n» from finite lower bounds and sampled values withdrawn; stronger statements recorded as OPEN in PD-T?…-319; the descriptive "roughly n⁻³" is not supported by a log–log fit (slope ≈ −4.1, see 319) and is dropped; the audit's fresh reruns cited (LC-L1: current-evidence pointers). This corrects the developer's acceptance of finding L7 of L3-reconstruction-02 (response-recon-02). No change to the statement or proof; status PROVED unchanged. Original wording of the replaced passages: «Explicit radius δ_0(n): exists by PD-T?…-303(e); rigorous reviewer bounds (L3-reconstruction-02, `padua_delta0.py`, a reviewer computation, not yet independently rerun): δ_0(n) ≥ 5.63e-4, 1.02e-4, 2.36e-5, 6.61e-6, 2.15e-6, 7.87e-7, 3.18e-7, 1.40e-7, 6.55e-8 for n = 4..12; first sampled negative radius 3.4e-2 … 3.5e-4 (MEASURED). So δ_0(n) → 0 with n (roughly n⁻³ in the sampled column): the obstruction holds for each n, with no radius uniform in n.»; «| boundary quadratic forms: closed forms of A, B, X and 4AB − X² (E1, E3, C11) | PROVED | exact symbolic expansion (`r05_boundary_proof.py`); hand-checked and independently re-derived (n symbolic) by L3-reconstruction-02 (`review_L3b/turan_symbolic.py`), and the whole certificate independently verified exactly (rigorous rational interval arithmetic) for n = 4..16 (`review_L3b/padua_turan_check.py`, log `reviews/logs_L3b/padua_turan_check.log`) |»; «Trusted dependencies: Python integers/fractions (reviewer exact code), sympy (developer's and reviewer's symbolic expansions).».
