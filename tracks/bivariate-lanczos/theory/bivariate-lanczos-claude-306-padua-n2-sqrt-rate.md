# PD-T?bivariate-lanczos-claude-306 — Padua n = 2: condition (H) holds, δ*(ε) ≍ √ε (exact certificate)

ID kind: PD-T.
Aliases: Padua n = 2 √ε law; dual PD certificate n = 2.
Split from: none (case of the target PD-T?bivariate-lanczos-claude-300).
Split into: none.

## Statement

For the Padua points of degree 2, P_2 = {(1,1), (1,−1/2), (0,1/2), (0,−1), (−1,1), (−1,−1/2)} (family {(cos jπ/2, cos kπ/3) : j+k even}), with any positive weights: dim S_1 = 3, the Hessian map is injective on S_1, and there are positive definite rational 2×2 matrices A_1..A_6 with Σ_i ⟨A_i, Hess p(z_i)⟩ = 0 for all p ∈ S_1. Hence (H) holds (PD-T?…-303(f)) and c δ² ≤ r(δ) ≤ C δ² (PD-T?…-303(c),(d)): exact backward representation of all consistent ε-perturbations of the degree-2 sections with support spread O(√ε), and √ε is necessary.

## Definitions / Assumptions

As in PD-T?…-303; [EXACT]; [IDEALIZED: perturbations given as data].

## Status by part

Overall status: CONDITIONAL.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| finite reduction: (H) ⟸ exact certificate (injectivity + PD A_i annihilating S_1) | PROVED | PD-T?…-303(f) |
| the certificate exists and passes the exact checks | CONDITIONAL | verified by the developer's exact Q(√2)/rational checker; obligation: independent rerun of the checker (workflow rule for computer-assisted proofs) |
| δ* ≍ √ε for Padua n = 2 | CONDITIONAL | on the row above |

## Depends on

PD-T?…-303; checker `tracks/bivariate-lanczos/code/L3/exact_certificates.py` (sha256 752188b6…ee6c5, see `directions/L3/logs/code_sha256.txt`).

## Checks

Command: `cd tracks/bivariate-lanczos/code/L3 && python3 exact_certificates.py` (Python 3.13.18, numpy 2.5.3, cvxpy 1.6.0 with CLARABEL used only to PROPOSE a candidate; all acceptance tests are exact Fraction arithmetic: exact nullspace of the 18 × 21 jet matrix in the monomial basis of Π_5, exact rank of the Hessian map (3), exact least-norm correction of the rounded candidate onto the 3 linear constraints, exact PD test a > 0, ac − b² > 0 for each A_i). Output `directions/L3/logs/exact_certificates.log`: "rank J=18 dim S1=3 (expected 3); rank Hess|S1=3 (injective: True) … DUAL certificate for (H): exact PD check PASS (float SDP margin t=0.0152) … (H) holds for Padua n=2: PROVED (exact)" — the word PROVED in the log is the checker's verdict; the registry status stays CONDITIONAL until an independent rerun. The six A_i are printed in the log.
MEASURED illustration: `lp_rate.py 2 bisect 0.03`: δ_min/√ε = 0.0574, 0.0538, 0.0535, 0.0535, 0.0542 for ε = 1e-2..1e-6, all LP S1-residual checks ok (log `lp_rate_n2_r0.03.log`); `lp_rate.py 2 resid 0.03`: minimal ℓ1 residual exactly 0 once δ ≥ 0.003 (ε = 1e-3) and δ ≥ 0.001 (ε = 1e-5) (log `lp_resid_n2.log`).

## Sources

None.

## Proof or evidence

Reduction PD-T?…-303(f); certificate in the log; the reduction is a finite exact check (rational entries).

## Scope

Padua n = 2 only (any positive weights; (H) does not depend on the weights). MEASURED: random square 6-point sets (3 seeds) also satisfy (H) numerically (PD-T?…-307).

## Open items

Independent rerun. A hand proof for n = 2 (e.g. via structure of S_1 for six points) not attempted.

## History

2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.
