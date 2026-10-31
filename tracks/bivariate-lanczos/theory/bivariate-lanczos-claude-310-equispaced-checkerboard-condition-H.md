# PD-T?bivariate-lanczos-claude-310 — Equispaced checkerboards n ≤ 7: condition (H) holds (exact certificates), δ*(ε) ≍ √ε

ID kind: PD-T.
Aliases: equispaced Harris–Simanek checkerboard (H); exact dual certificates n ≤ 7; R04.
Split from: none (case of the target PD-T?bivariate-lanczos-claude-300).
Split into: none.

## Statement

For n = 1, …, 7 and the ordered equispaced checkerboard S_0(n) = {(−1 + 2i/n, −1 + 2j/(n+1)) : 0 ≤ i ≤ n, 0 ≤ j ≤ n+1, i + j even} (M = N_n rational nodes), with any positive weights: dim S_1 = n(n+1)/2, the Hessian map is injective on S_1, and there are rational positive definite 2×2 matrices A_i with Σ_i ⟨A_i, Hess p(z_i)⟩ = 0 for all p ∈ S_1. Hence (H) holds (PD-T?…-303(f)) and c δ² ≤ r(δ) ≤ C δ²: consistent ε-perturbations of the degree-n sections are exactly representable with support spread O(√ε), and √ε is necessary.

## Definitions / Assumptions

As in PD-T?…-303; [EXACT]; [IDEALIZED: perturbations given as data]. Positivity of the checkerboard weights (plan.md Benchmarks; source codex/charter-unisolvence-20261031@eb7bdcd PD-T001, NOT accepted) is not needed: (H) depends only on the nodes; any positive weights.

## Status by part

Overall status: PROVED (n = 1..7).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| finite reduction (certificate ⇒ (H) ⇒ √ε rate) | PROVED | PD-T?…-303(c),(d),(f) |
| certificates exist and pass the exact checks, n = 1..7 | PROVED | developer's exact checker; independent exact rerun by L3-reconstruction-02 (`review_L3b/equi_H_cert.py`, Chebyshev basis, own Fraction RREF, mpmath log-barrier proposer, exact acceptance; log `reviews/logs_L3b/equi_H_cert_n1_7.log`) |
| n = 8: (H) holds | reviewer computation (L3-reconstruction-02, `equi_H_cert_n8.log`, high-precision t_D = 4.12e-15, exact min det/tr 2.06e-15) | not yet a developer record and not independently rerun; the developer's double-precision proposal (t_D = −1.3e-12) had the wrong sign and was correctly left unresolved |

## Depends on

PD-T?…-303; checker `tracks/bivariate-lanczos/code/L3/exact_checkerboard.py` (imports the exact Q2 arithmetic of `exact_certificates.py`; hashes in `directions/L3/logs/code_sha256.txt`).

## Checks

`python3 exact_checkerboard.py 1 6 equi` and `python3 exact_checkerboard.py 7 8 equi` (Python 3.13.18, numpy 2.5.3, cvxpy 1.6.0/CLARABEL tol 1e-12 only as proposer; acceptance in exact Fraction arithmetic: exact nullspace of the 3M × dim Π_{2n+1} jet matrix, exact rank of the Hessian map, exact least-norm correction of the rounded proposal onto the exact constraints, exact PD tests). Logs `logs/exact_checkerboard_equi.log`, `logs/exact_checkerboard_equi_n7_8.log`: "DUAL exact PASS … => (H) CERTIFIED" for n = 1..7; n = 8 UNRESOLVED.

## Sources

None.

## Proof or evidence

Reduction PD-T?…-303(f) plus the exact certificates.

## Scope

n ≤ 7, this node family. n = 8 unresolved (margin below double-precision proposals). Contrast: Padua (Chebyshev–Lobatto checkerboard) fails (H) robustly from n = 3 (PD-N?…-301, PD-T?…-307).

## Open items

n = 8: independent rerun of the reviewer's certificate (then cite); n ≥ 9 needs an extended-precision proposer; whether (H) eventually fails for equispaced checkerboards.

## History

2026-10-31T23:15+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer, round R04 (working tree fba4d2f).
- 2026-11-01T00:47:14+01:00, L3 developer (Claude Opus 5.5, xhigh requested): CONDITIONAL → PROVED for n = 1..7 citing the independent exact rerun; reviewer's n = 8 certificate recorded as a reviewer computation of L3-reconstruction-02 (reviews/L3-reconstruction-02.md, audited head ae991c1). Original wording of the replaced passages: «Overall status: CONDITIONAL.»; «| certificates exist and pass the exact checks, n = 1..7 | CONDITIONAL | developer's exact checker passes; obligation: independent rerun |»; «Independent rerun; n ≥ 8 (extended-precision proposer); whether (H) eventually fails for equispaced checkerboards.».
