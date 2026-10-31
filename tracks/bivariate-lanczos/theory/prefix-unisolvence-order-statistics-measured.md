# PD-T?bivariate-lanczos-claude-503 — Prefix unisolvence of Padua node orders: measured statistics, the online pivot detector, and the effect on the 'scheme' error

ID kind: PD-T.
Aliases: prefix mechanism data; IDEA?bivariate-lanczos-claude-502 (test of seed IDEA 016); relational recovery of intermediate states.
Split from: none.
Split into: none (the existence of all-prefix-unisolvent orders is PROVED in `unisolvent-prefix-extension-lemma.md`; the failure of the 'largest' rule is PD-N?bivariate-lanczos-claude-506).

## Statement

All parts [FP/numerical-rank, MEASURED] within the scope below.

(A) *Prefix statistics.* For Padua first-family sets Pad_n, n = 10, 15, 20, 30, 40, 50 (M = N = 66, 136, 231, 496, 861, 1326), prefix K of an order = first K nodes versus the first K graded monomials; 'singular' = certified σ_min < 1e-11 of the leading K×K block of the row-permuted orthogonal product-Chebyshev matrix Q_c (observed: every singular prefix has σ_min ≤ 1e-15, nothing in the interval 1e-15..1e-11 at the scanned prefixes; n_amb = 0 for all 54 orders (9 orders × 6 sizes)). (i) The structured orders `given` and `sortx` are singular at almost all prefixes: 58/66, 126/136 (125 sortx), 218/231, 478/496, 838/861 (`sortx` 838), 1298/1326 prefixes (the exact line criterion — K nodes on c vertical lines with c(c+1)/2 < K — certifies ≥ 99% of them; see `prefix.py`). (ii) Random orders (rand1–3, 18 orders at n = 10..50): all prefixes unisolvent in 16 of 18 order/size cases (3 orders × 6 sizes), with exceptions n = 15 rand2 (4 singular prefixes, K = 127..130) and n = 40 rand2 (1 singular prefix, K = 2), and the minimal prefix σ_min over the order falls from ≈ 1e-3 (n = 10) to 2e-7..6e-7 (n = 30), 7e-8..4e-7 (n = 40) and 3e-9..3.5e-8 (n = 50). (iii) The constructed orders gepp (Gaussian elimination with partial pivoting on Q_c) and rpiv1–3 (randomised threshold pivoting, θ = 0.1) have all prefixes unisolvent with min σ_min = 1.3e-1, 7.8e-2, 6.2e-2, 2.9e-2, 1.5e-2, 7.5e-3 (gepp) and ≥ 4.7e-4 (rpiv, n ≤ 50).

(B) *Online detector.* 'Prefix K (K ≤ n=10,14,20 sets) is numerically singular ⇔ min over the monomials j ≤ K of the primary pivot |V(j)[j, p(j)]| (and |w_1| for j = 1) of the 'scheme' Givens state after K points is < 1e-10' holds without exception on 20 order/size cases (n = 10: given, sortx, rand1–3, gepp, rpiv1; n = 14: same; n = 20: given, sortx, rand1, rand2, gepp, rpiv1; `logs/r03_detector.log`): all 58 / 58, 110 / 110, 218 / 218 singular prefixes flagged, all singular prefixes of the random orders flagged (n = 14: 1 and 2), no unisolvent prefix flagged. The *newest* pivot alone (monomial K) is **not** a detector (n = 10 given: 6 of 58 singular prefixes have it < 1e-10; n = 14: 10 of 110). The min-pivot is also correlated with σ_min on unisolvent prefixes (Spearman 0.3..0.9, order dependent) — a conditioning proxy, not an estimate.

(C) *Effect on the 'scheme' rule.* On the 40 (n, order, weight) cases with all prefixes unisolvent and n ≥ 30 (3 random + gepp + 3 rpiv at n = 30, 40, 50 minus the singular rand2 at n = 40, cubature and U(0.1,1) weights), Spearman correlation of log10(scheme error) with log10(min prefix σ_min) is −0.51 (p = 9e-4); at n = 50 alone −0.71 (14 cases: scheme error 1.1e-13..1.3e-13 for gepp/rpiv with σ_min ≥ 4.7e-4 versus 3.1e-13, 3.7e-13, 1.6e-12 (cub) and 3.4e-12 (U) for the random orders with σ_min 3e-9..3.5e-8). The REPRO outlier (`topics/…/repro/REPRO.md`: Padua n = 60, uniform weights, random order from `default_rng(2)`): scheme 2.0e-12 and largest 2.1e-4 (error versus the Householder H) were reproduced bit-for-bit in magnitude by `diag_repro_x60.py`; its prefix scan (1008 s) found no singular prefix and a minimum exact prefix sigma_min of 9.7e-10 (158 prefixes with upper bound < 1e-6, 2 below 1e-8): the smallest value recorded in this study. Three further random n = 60 orders gave scheme errors 2.0e-11, 5.1e-13, 1.6e-12 (prefix scans not run) and the gepp order 2.0e-13 (`logs/r03_x60.json`, `logs/r03_x60_controls.jsonl`; R03.md): the REPRO value is a typical draw. 

(D) *Intermediate states are not continuous in the data on non-unisolvent prefixes.* Running double and long-double Givens in lockstep (`exp_r02_dual.py`, `logs/r02_dual.jsonl`), the active (H_x, H_y) blocks differ by relative Frobenius 0.24–0.6 at every checkpoint before the end for the `given` order at n = 15, 20, 30, 40 while the *final* matrices agree to 7.9e-15, 9.9e-15, 2.3e-14, 4.1e-14 (same as the error against the reference). For unisolvent orders the lockstep difference grows monotonically in the number i of inserted points with log–log slope 0.83–0.87 (gepp, n = 30, 40), 0.65–0.70 (gepp, n = 15, 20), and for random orders reaches 1e-12..1e-11 in mid-run (n = 40) before dropping to 1e-13 at i = M.

## Definitions

Q_c: the M×M orthogonal matrix diag(√w_cub)·V·D with V the product-Chebyshev basis T_a(x)T_b(y) in graded lex order (x-degree descending), w_cub the Padua cubature weights, D the diagonal making Q_c orthonormal (only (n,0) has norm² 2). Prefix block B_K = Q_c[perm[:K], :K]. Certified σ_min: either an SVD, or the bounds σ_S ≥ σ_min(B_K) ≥ 1/((1+b)² max(b, 1/σ_S)) from a bordered-inverse chain (`prefix.py`, validated against exhaustive SVD on 18 order/size cases at n = 6, 10, 14: 0 classification mismatches), refined by SVD where the bounds straddle the tolerance and at the ≤ 150 prefixes with the smallest upper bound. Singular/unisolvent for the weights: both are weight-independent (positive row scaling).

## Assumptions

Double precision entries of Q_c with errors ≲ 3u, so certified σ_min ≥ 1e-11 implies nonsingular for K ≤ 2016 (‖E‖₂ ≲ K·3u ≈ 1e-12); no high-precision (mpmath) cross-check was made (the pre-registered cross-check at M = 66, 136, 231 was replaced by the exhaustive-SVD validation and the clean gap above; stated as a deviation).

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (A) prefix statistics | MEASURED | `logs/r01_prefix_a.jsonl`, `r01_prefix_b.jsonl` |
| (B) detector: no counterexample at n = 10, 14, 20 | MEASURED | `logs/r03_detector.log`; no proof that the detector is exact in exact arithmetic (OPEN: needs the zero-pattern invariants for non-unisolvent prefixes, see R03.md) |
| (C) scheme error vs prefix conditioning | MEASURED (moderate correlation) | `analyze_r01b.py`-style join in R03.md; confounded by n |
| (D) lockstep instability | MEASURED | `logs/r02_dual.jsonl` |

Candidate / claim disposition: the prefix mechanism *as formulated in plan L5-Q1* is not here; see PD-N?bivariate-lanczos-claude-506.

## Depends on

`unisolvent-prefix-extension-lemma.md` (existence of the orders gepp/rpiv; PROVED).

## Checks

Commands: `python3 -I exp_r01b.py OUT.jsonl 10 15 20 30 40` and `… 50 62` (the n = 62 part was killed before it started its prefix scans because of run time; see Runs needed); `python3 -I diag_pivot_vs_sigma.py n [orders]`; `python3 -I exp_r02_dual.py OUT.jsonl padua_cub 15 20 30 40`. n = 62 has no prefix data. Independent rerun: none.

## Sources

None beyond the inputs' description of the mechanism (adv_F1_F6_F3.md §2.3, unaudited).

## Proof or evidence

Measured; see Checks.

## Scope

Padua first family n ≤ 50 (n = 60 single case), the specific orders listed (given, sortx, 3 random permutations per n, gepp, 3 rpiv per n), IEEE double. No claim for other node families, other random permutations, or n > 60.

## Open items

(1) Exactness of the detector in exact arithmetic. (2) A quantitative law for the best achievable min_K σ_min(B_K) over orders (halving per Δn = 10 in the gepp data). (3) Prefix data at n = 62 (Runs needed).

## History

2026-10-31, Claude Sonnet 5.5 (high), L5 R01/R03: created.
