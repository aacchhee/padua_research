# PD-N?bivariate-lanczos-claude-301 — Exact-section (Greenbaum-type) backward interpretation with δ(ε) → 0 fails for Padua n = 3

ID kind: PD-N.
Aliases: Padua n = 3 obstruction; locally nonnegative singular septic p*; failure of the commuting (graded) backward model in the square case; kill test of L3-Q1 (square case) fires at n = 3.
Split from: none (case of the target PD-T?bivariate-lanczos-claude-300).
Split into: none.

## Statement

Let P_3 be the ten Padua points of degree 3 ({(cos jπ/3, cos kπ/4) : 0 ≤ j ≤ 3, 0 ≤ k ≤ 4, j+k even}), μ = Σ w_i δ_{z_i} with any positive weights. There is an explicit polynomial p* ∈ Π_7 with rational coefficients (listed in `directions/L3/logs/exact_certificates.log`; even in y) such that p*(z_i) = 0, ∇p*(z_i) = 0 and Hess p*(z_i) ≻ 0 for all ten nodes, and p* ≥ 0 on K_{δ_0} with δ_0 = 30117029139000/77370908310949543 ≈ 3.89·10⁻⁴ (rigorous Taylor bound; numerically p* ≥ 0 up to radius ≈ 0.05). Consequently (PD-T?…-303(e)): for every ε ∈ (0, ε_1] (ε_1 > 0 such that M_3(L_μ + E) ≻ 0 for ‖E‖ ≤ ε_1) and every functional E on Π_7 with ‖E‖ ≤ ε and E(p*) < 0 — for example E = −ε ev_ζ with ζ any point where p*(ζ) > 0, i.e. removing a mass ε at ζ — the consistent degree-3 section pair Φ(L_μ + E) (exact structural zero pattern, all interior commutativity conditions exact, last-block commutator O(ε)) is NOT the exact section pair of any positive measure supported in K_δ for any δ ≤ δ_0, and any positive measure on K_δ, δ ≤ δ_0, has functional distance ≥ |E(p*)|/‖p*‖_* from L_μ + E. Hence no δ(ε) → 0 exists for the exact form of L3-Q1 at Padua n = 3.

## Negative-result scope (PD-N only)

Attempted mechanism: IDEA?bivariate-lanczos-claude-307 / seed 005 — "a Greenbaum-type backward model: perturbed square-case sections are exact sections of a positive measure (equivalently a graded commuting symmetric extension) with joint spectrum within δ(ε) → 0 of the nodes".
Parameter range: Padua points n = 3, any positive weights, perturbative regime, exact representation or residual smaller than |E(p*)|/‖p*‖_*; [IDEALIZED: perturbations given as data] (all directions E allowed). Not covered: residuals as large as the perturbation (then μ itself works, PD-T?…-302(c)); whether actual floating-point errors have E(p*) < 0 (for Padua the computed entries are overdetermined, so the sign is not defined at the O(u) level; PD-T?…-301(d)); n ≥ 4 (MEASURED only, PD-T?…-307); support at distance > δ_0.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| reduction: existence of such p* ⇒ obstruction | PROVED | PD-T?…-303(e), PD-T?…-302, PD-T?…-301 |
| p* ∈ S_1 with all Hessians PD (exact, Q(√2)) and the explicit δ_0 bound | PROVED | developer's exact checker; independent exact rerun by L3-reconstruction-01 (`indep_exact_check.py`: p*(z_i) = 0, ∇p*(z_i) = 0, Hess p*(z_i) ≻ 0 exactly, min λ_min ≥ 0.112782; developer δ_0 confirmed; rigorous rational interval arithmetic shows p* > 0 on punctured discs of radius 0.04 — a reviewer computation, cited as such) and a second, independently derived certificate (reviewer, radius 0.02) |

Candidate / claim disposition: the mechanism (exact Greenbaum-type commuting model with δ → 0, square case) is REJECTED: refuted for Padua n = 3.
Rejection reason: refuted (within the stated scope).

## Depends on

PD-T?bivariate-lanczos-claude-301, 302, 303; checker `exact_certificates.py` (sha256 752188b6…ee6c5).

## Checks

Command `cd tracks/bivariate-lanczos/code/L3 && python3 exact_certificates.py` (Python 3.13.18; cvxpy 1.6.0/CLARABEL only proposes c; acceptance in exact arithmetic over Q(√2) implemented with fractions.Fraction and an exact sign test). Output (`directions/L3/logs/exact_certificates.log`): "Padua n=3: M=10 D=36 rank J=30 dim S1=6 (expected 6); rank Hess|S1=6 (injective: True) … PRIMAL certificate (robust failure of (H)): exact PD check at all nodes PASS … rigorous radius: min lambda_min lower bound = 0.0931188, C3 upper bound = 717.669, delta_0 = 30117029139000/77370908310949543". The δ_0 bound uses λ_min ≥ det/tr, rational enclosures 1.4142135 ≤ √2 ≤ 1.4142136 and a coefficient bound on third derivatives over |x|, |y| ≤ 1.1.
MEASURED corroboration: `inspect_certificate.py 3` (min p* on balls of radius 0.05 around the nodes = 1.08e-5 > 0, radius 0.1: −1.9e-2; log `inspect_certificate_n3.log`); `lp_rate.py 3 resid 0.03`: minimal ℓ1 moment residual over positive measures on nested grids of K_δ stays ≈ 0.023–0.035·ε for all δ ∈ [0.003, 0.2] at ε = 1e-3 and 1e-5 (never → 0), above the certificate lower bound 0.0146·ε (log `lp_resid_n3.log`).

## Sources

None.

## Proof or evidence

PD-T?…-303(e) applied to the certified p*.

## Scope

As in the negative-result scope.

## Open items

Exact certificates for n ≥ 4 (now: PD-T?…-313 / PD-N?…-303 for all n ≥ 4, and the reconstruction's exact n = 4 certificate); structural explanation of p* (why (H) fails from n = 3 on for Padua).

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.
- 2026-10-31T23:54:00+01:00, L3 developer: findings L1 (quantifier ε ≤ ε_1) and L2 (reviewer's rigorous radius 0.04 cited; the developer's δ_0 ≈ 3.89e-4 remains the developer-certified value) of L3-reconstruction-01 (topics/bivariate-lanczos-20261031/reviews/L3-reconstruction-01.md, audited head 0b7b396); CONDITIONAL → PROVED citing that review's independent exact rerun.
