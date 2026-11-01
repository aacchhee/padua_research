# PD-T?bivariate-lanczos-claude-317 — MEASURED: d(κ∘Φ) has rank n(n+1)/2 at the tested square node sets

ID kind: PD-T.
Aliases: dkappa rank measurement; 304(c) MEASURED row; numerical first-order isomorphism.
Split from: PD-T?bivariate-lanczos-claude-304(c), pre-audit status row: «| (c) the induced map V*/T → Skew_{n+1} is an isomorphism ("κ is, to first order, the S_1*-component") | MEASURED | reconstruction `indep_measured.py dkappa`: rank n(n+1)/2 for Padua n = 2, 3; not proved |».
Split into: none.

## Statement

MEASURED, floating point, within the listed scope: at the square-case measure L_μ, the derivative of L ↦ κ(Φ(L)) has numerical rank n(n+1)/2 (= dim Skew_{n+1} = dim S_1, i.e. the induced map V*/T → Skew_{n+1} is numerically an isomorphism) for
1. Padua n = 2, 3 with the reviewer's weights and Legendre coordinates (L3-reconstruction-01): singular values 4.941, 3.327, 3.116 (n = 2) and 9.405, 8.226, 4.804, 3.599, 2.491, 2.111 (n = 3); |dκ| along T ≤ 2.5e-11 (n = 2), 4.2e-11 (n = 3);
2. Padua n = 1, 2, 3, 4, the equispaced checkerboard n = 3 and one random square set n = 3 (numpy default_rng(0) nodes, default_rng(1) weights), monomial moment coordinates, central differences (developer, 2026-11-01): smallest singular values 4.223 (Padua n = 1), 9.643 (n = 2), 15.36 (n = 3), 28.61 (n = 4), 12.76 (equispaced n = 3), 120.8 (random n = 3), largest ≤ 6230; in every case also dim{p_C : C ⊥ Hankel} = dim S_1 = n(n+1)/2.
Singular values depend on the weights and on the coordinates on V*; only the rank is compared across runs.

## Definitions / Assumptions

As in PD-T?…-304, 318. Numerical rank with relative threshold 1e-9 (developer) — the gaps are many orders of magnitude.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| items 1–2 | MEASURED | logs below; no general claim |

## Depends on

PD-T?…-318 (interpretation of the rank; the developer's FD matrix is also compared with the exact formula of 318(b)).

## Checks

- Reviewer (L3-reconstruction-01): `python3 -I -B tracks/bivariate-lanczos/code/review_L3/indep_measured.py dkappa 2` and `… dkappa 3`, log `topics/bivariate-lanczos-20261031/reviews/logs_L3/indep_dkappa.log` (numpy 2.5.3, scipy 1.18.1). Not rerun.
- Developer: `OPENBLAS_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L3/t318_dkappa_formula_check.py` → `topics/bivariate-lanczos-20261031/directions/L3/logs/t318_dkappa_formula_check.log` (hashes in PD-T?…-318 Checks). A separate implementation from the reviewer's (different basis, weights, step and code).

## Sources

None.

## Proof or evidence

Measurements only.

## Scope

Six node sets, n ≤ 4, one choice of weights per set. No claim for other n or node sets.

## Open items

Larger n (Padua n ≤ 7 is cheap; conditioning of monomial coordinates degrades — use a Chebyshev basis); the general statement is PD-T?…-316 (OPEN).

## History

- 2026-11-01T08:33:39+01:00, Claude Opus 5.5 (xhigh, requested), L3 developer: split from PD-T?…-304(c) per finding LF-M2 of Codex audit-01 (topics/bivariate-lanczos-20261031/audit-01/L3-framework.md; candidate 5ccfac2); item 1 is the reviewer's measurement formerly cited in 304, item 2 is the developer's new run.
