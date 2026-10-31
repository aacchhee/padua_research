# PD-T?bivariate-lanczos-claude-502 — Measured growth of the Givens-updating error with M (Padua and random nodes, M = 66..2016)

ID kind: PD-T.
Aliases: Givens deficit slopes; L5-Q1 first clause; IDEA?bivariate-lanczos-claude-501 (test of seed IDEA 015).
Split from: none.
Split into: none (the worst-case bound is `givens-updating-rotation-count-backward-bound.md`; the pivot-rule failure is PD-N?bivariate-lanczos-claude-506).

## Statement

[FP, MEASURED] Within the recorded scope below, the relative Frobenius error of the leading N×N blocks of (H_x, H_y) computed by (a) point-by-point Givens updating with the fixed 'scheme' rule (Van Barel–Chesnokov 2010, Algorithm 1, real nodes), (b) the HL recurrence (window 2 degrees, MGS + one reorthogonalisation), (c) BJ (same window, CGS, no reorthogonalisation), (d) full CGS2, (e) Householder QR of the weighted Chebyshev–Vandermonde matrix, against a long-double three-pass-reorthogonalised reference, has the following fitted log–log slopes in M:

| family (replicates per size) | Givens-scheme | HL | BJ | CGS2 | Householder |
|---|---|---|---|---|---|
| Padua, cubature weights, M = 66..2016 (5 orders) | 1.40 [1.09, 1.70] | 0.73 [0.70, 0.76] | 1.17 [0.95, 1.40] | 0.48 [0.46, 0.50] | 0.38 |
|   — structured orders (given, sortx) only | 0.93 [0.89, 0.98] | 0.80 | 1.31 | 0.50 | 0.37 |
|   — random orders (rand1–3) only | 1.71 [1.35, 2.07] | 0.69 | 1.09 | 0.47 | 0.38 |
| Padua, weights U(0.1,1), M = 66..2016 (5 orders) | 1.55 [1.15, 1.94] | 0.79 [0.77, 0.81] | 1.01 [0.86, 1.15] | 0.53 [0.51, 0.55] | 0.38 |
|   — structured / random orders only | 0.92 / 1.96 | 0.81 / 0.78 | 1.05 / 0.98 | 0.54 / 0.53 | 0.38 / 0.38 |
| Padua, unit weights, M = 66, 231, 496, 861 (5 orders) | 1.08 [0.90, 1.25] | 0.77 [0.74, 0.80] | 0.65 | 0.52 [0.51, 0.54] | 0.38 |
| random nodes, arcsine density, M/N ≈ 3, M = 66..1326 (5 seeds) | 1.28 [1.06, 1.50] | 0.71 [0.69, 0.74] | 1.12 [0.97, 1.28] | 0.38 [0.36, 0.40] | 0.28 [0.26, 0.30] |
| random nodes, uniform on [−1,1]², M/N ≈ 3, M = 66..2016 (5 seeds) — **confounded** | 2.87 [2.49, 3.26] | 2.28 | 2.76 | 1.57 | 2.11 |

Brackets: 95% t-interval of the OLS slope over all (order or seed, size) replicates; the cluster-bootstrap intervals are in `logs/analysis_r01.txt` and agree to ±0.05 on the full range (they are wider for the upper range M ≥ 496, which has only 4 sizes). Geometric-mean errors by size, ratios Givens/HL (4–7 at M = 66, up to 26 at M = 1326 for Padua cubature; 4.1 → 70 for uniform random nodes) and the 'largest' rule are in the same file.

**Kill test of plan L5-Q1 (operational reading in candidates.md, IDEA 501).** The explanation 'Givens ∝ M, HL/CGS2 ∝ √M' is *not killed* in the Padua families (Givens slope > 0.7 on the full range and for M ≥ 496; HL ≤ 0.81 and CGS2 ≤ 0.57 < 0.9) and not killed in the conditioning-controlled random family. It is *literally killed* in the uniform-random-node family (CGS2 slope 1.57 ≥ 0.9, HL 2.28), but that family is confounded: cond of the weighted Chebyshev–Vandermonde matrix grows like M^2.96 (geometric means 2.1e1 at M = 66 to 3.8e5 at M = 2016), the Householder slope is 2.11, and the slopes measure sensitivity of the problem, not rounding of the algorithm; the controlled arcsine family shows Householder 0.28, CGS2 0.38, HL 0.71.

**What is and is not supported.** (1) Givens-scheme grows faster than HL/CGS2/Householder in every family, by a slope difference of 0.3–0.8 over M = 66..2016 (excluding the confounded uniform-random family). (2) The slope of ≈ 1 (0.91–0.93 on structured orders, 1.08–1.28 pooled) is consistent with 'one unit of error per rotation touching an entry'; the slope is **not** 1 on random orders (1.7–2.0 in Padua), where the error depends on the node order beyond M (see PD-T?bivariate-lanczos-claude-503). (3) The HL slope (0.71–0.81) lies between ½ and 1; it is above the ½ of CGS2 and Householder. The statement 'HL ∝ √M' is therefore not supported at the precision of this experiment; only HL < 0.9 is. (4) Nothing here distinguishes a coherent from a random accumulation of rotation errors; the long-double replay in R02 is the only direct evidence on that.

## Definitions

Error = ‖(Ĥ_x − H_x^ref, Ĥ_y − H_y^ref)‖_F / ‖(H_x^ref, H_y^ref)‖_F over the leading N×N blocks after fixing signs so that the primary pivots are positive; reference = `F.reference` of `f6_givens_vs_hl_deficit.py` (long double, three passes, full reorthogonalisation) on the unpermuted nodes (H is independent of the node order in exact arithmetic). Padua order labels: given (natural j-major order of the first family), sortx (lexicographic), rand1–3 (permutations with seeds 10n+k). Padua weights: normalised cubature weights; 'U(0.1,1)' weights are one vector per n, `default_rng(1000+n).uniform(0.1,1,N)`, shared by the five orders. Random nodes: seeds 7000·k+M, k = 1..5, unit weights, N = (n+1)(n+2)/2 with n = 5, 8, 11, 17, 22, 28, 34 for M = 66, 136, 231, 496, 861, 1326, 2016.

## Assumptions

IEEE double, numpy 2.5.3 / scipy 1.18.1 / Python 3.13, OPENBLAS_NUM_THREADS=1, x86-64; the C port of Givens (`givens_core.c`) was checked bit-identical to the unchanged input `givens()` at n = 6, 10, 14 (max |ΔH| = 0.0). The Givens Q is not accumulated in the C port (the metric is the H error only). The slope is an OLS fit in log–log over a 30-fold range of M; sizes are not independent (the same nodes), and slopes beyond the range are not claimed.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| table of fitted slopes and the kill-test verdicts above | MEASURED | `logs/r01_padua_cub.jsonl`, `r01_padua_rand.jsonl`, `r01_padua_unif.jsonl`, `r01_random.jsonl`, `r01_random_cheb.jsonl`; `logs/analysis_r01.txt` |
| interpretation: rotation counting | OPEN | worst-case bound (PD-T?…-501) gives M^{3/2} relative; no model in this file predicts the observed ≈ M^1 |

Candidate / claim disposition: not applicable.

## Depends on

Input code `f6_givens_vs_hl_deficit.py` (unchanged, unaudited input). `givens-updating-rotation-count-backward-bound.md` for the worst-case comparison. No registry dependency.

## Checks

Producer commands: `OPENBLAS_NUM_THREADS=1 python3 -I exp_r01.py FAMILY OUT.jsonl [sizes]` (FAMILY ∈ padua_cub, padua_rand, padua_unif, random, random_cheb) in `tracks/bivariate-lanczos/code/L5/` (library `l5_lib.py`, C core `givens_core.c`; build `gcc -O2 -ffp-contract=off -shared -fPIC -o libgivens_core.so givens_core.c -lm`); analysis `python3 -I analyze_r01.py LOGDIR`. Rules/base SHA of the repository clone at run time: `2d8c3ab8348be80a6f16f69ee7ef9c7bb66ed42e` (read-only `git rev-parse`); code uncommitted at run time, so the sha256 of the scripts is in the first (`meta`) line of every jsonl. `exp_r01.py` was edited once after the Padua and uniform-random runs had started (added the `random_cheb` family and `np.clip` in the conditioning computation; no change to the computation of the reported errors). The runs shared two cores with other agents' jobs; timings are not reported. Independent rerun: none yet.

## Sources

Seed claim: `adv_F1_F6_F3.md` §2.2 (unaudited input; slopes 0.96/0.8/0.5/0.4 for M = 66–496). VB–C 2010 Table 2 (p. 401: ratio 20–60 of 'norm1' to 'norm2' at 496–1326 Padua points, a different protocol: polynomial recovery) fulltext read. Not reproduced here: Table 2's protocol.

## Proof or evidence

Measured only; see Checks. No general claim.

## Scope

Padua first-family sets (M = N), nodes in [−1,1]², uniform/arcsine random nodes with M/N ≈ 3, one machine, one BLAS; the Householder/CGS2/HL implementations are those of the unchanged inputs (not tuned). Slopes in M mix algorithmic and node-order effects (see 503) and, for random nodes, problem conditioning.

## Open items

(1) Larger M (> 2016) and a cleaner conditioning-controlled random family (M ≫ N; the present arcsine family is only fitted to M = 1326). (2) A model explaining slope ≈ 1 for structured orders. (3) Independent rerun on AC's servers (Runs needed in R01.md).

## History

2026-10-31, Claude Sonnet 5.5 (high), L5 R01: created from the logs listed above.
