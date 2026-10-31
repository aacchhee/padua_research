# REPRO: re-execution of the input scripts (bivariate-lanczos-20261031)

Developer: Claude Sonnet 5.5 (effort high), reproduction subagent. Date 2026-10-31. Rules `d36722823441dc40c6e19d69a174459348dd309c` (as recorded in `../plan.md`).
Every number below is **MEASURED (floating point)**: an observation of one deterministic run at the stated seeds, not a proof and not an error bound. "Reproduced" means that the printed digits agree with the claim; it does not validate the claim's interpretation.

## 1. Inputs and code identity

- Origin: AC-supplied archive `padua_lanczos_inputs.zip`, SHA-256 `5498074f1547c7117a7167d31b7346462b381718b85e6644e75b7f0d0d7ecf5c`; unaudited, untrusted. Unpacked under `../sources/padua_lanczos_inputs/` (not committed).
- The 12 scripts were copied unchanged to `tracks/bivariate-lanczos/code/inputs/`; every copy is byte-identical (`cmp`) to the unpacked source and its sha256 matches the archive's `SHA256SUMS.txt` (12/12 OK). Blob ids and sha256: `tracks/bivariate-lanczos/code/inputs/MANIFEST.md`.
- Safety read before execution: all 12 scripts read in full. Imports are numpy, sys, os, time, itertools only; no `open`, network, subprocess or file writes; the only filesystem effect is `sys.path.insert` of the script's own directory. Nothing unexpected.
- Claimed results compared against: `RESULTS` = archive `code/RESULTS.md` (working track); `ADV` = `notes/adv_F1_F6_F3.md`; `ICP` = `notes/ingest_classic_papers.md`; `OPV` = `reports/Open problems verification.md` (all inside `../sources/padua_lanczos_inputs/`).

| script | git blob id |
|---|---|
| f1_loss_vs_ritz.py | 809b83776c9b92e417c146e06726d11450b203fc |
| closed_form_H.py | 68fb3131813fee148f2fae181f2a129d926a4218 |
| harris_simanek_check.py | 06c3dc603039dd28c8b47278e173fb18f192e42c |
| bj_window.py | 3a8ba4c7904a7cc2e617226073fd57e21e659e85 |
| padua_weights_check.py | 09109e3c3d6d1063530d7ed994ea86167cdacb18 |
| f6_givens_vs_hl_deficit.py | 3b37cad538b441bd2c2d42587d76ac3d0b3d32c0 |
| f6_run_padua_large.py | ea83fc2fd30d985f8413f5726a2b5df6397f940a |
| f6_diag_redundant_pivot.py | eacb3f2b3d621cc26a43b2f17e1ebfb192ed9bac |
| f6_pivot_threshold_test.py | 893fa6ba9f852a0985403d91f2f66e6e42956977 |
| f3_qfree_vs_R_downdate.py | b8a77282e90cad6c674f56709d669fa133b347d6 |
| qfree_bivariate_downdate.py | 4abe6e03fbd940691733b9d28f5c491e17e1e465 |
| qfree_vs_conditioning.py | 23c9e7cf37a9361ace6a31065396f83525a56f8e |

## 2. Environment and protocol

- Python 3.13.18 (Clang 23.1.3), numpy 2.5.3, scipy 1.18.1 (installed; not imported by any script), numpy BLAS: scipy-openblas, OpenBLAS 0.3.34. Linux 6.18.44-fc-v185 x86_64, Intel Xeon @ 2.80 GHz, 2 cores, 8 GB RAM. `numpy.longdouble` = x87 80-bit (eps 1.08e-19), used by the F6 reference.
- Each script ran in a fresh, empty scratch working directory (`.../scratchpad/repro_run/<tag>/`; still empty afterwards for every run) as `timeout 1800 python3 -I -B <abs path of the copy> [args] > log 2>&1`. `-B` (no bytecode) was added to `-I` so that no `__pycache__` is written into the inputs directory; this is the only deviation from the requested invocation, except for run 12 (below). Environment `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`. Two runs were executed concurrently on the 2 cores, so wall times are indicative only. Runner: `analysis/run1.sh`.
- "Seeds" are those hard-coded in the scripts. A shared generator is consumed in program order, so a node set depends on everything drawn before it.
- Logs: `logs/<script>[_args].log` (stdout and stderr merged; all small, 25 KB in total, kept in full). SHA-256 of the logs are in section 7.

## 3. Completed runs

| # | command (arguments after the script) | seeds as hard-coded | exit | wall | log |
|---|---|---|---|---|---|
| 1 | `f1_loss_vs_ritz.py` | `default_rng(0)`, one generator drawn in order: random 625, 2500 (n=24), then 1681, 6724 (n=40); tensor grids deterministic; weights = 1 | 0 | 44.7 s | `logs/f1_loss_vs_ritz.log` |
| 2 | `closed_form_H.py` | none (deterministic); n in 5, 6, 20, 41. Imports `padua_weights_check`, whose top-level code also runs (n = 6, 20, 60 output at the head of the log) | 0 | 2.6 s | `logs/closed_form_H.log` |
| 3 | `harris_simanek_check.py` | `default_rng(0)`, m = 6, 15, 30 in order | 0 | 2.1 s | `logs/harris_simanek_check.log` |
| 4 | `bj_window.py` | none | 0 | <0.1 s | `logs/bj_window.log` |
| 5 | `padua_weights_check.py` | none | 0 | 2.4 s | `logs/padua_weights_check.log` |
| 6 | `f6_givens_vs_hl_deficit.py` (default sizes 10 20 30) | `default_rng(1)`: sanity 15 points, then random permutations, then random node sets M = 105, 300, 496 | 0 | 138.2 s | `logs/f6_givens_vs_hl_deficit.log` |
| 7 | `f6_run_padua_large.py 20 30` | `default_rng(2)`, fresh per invocation; per n: given and one random permutation, then random weights U(0.1,1) | 0 | 56.0 s | `logs/f6_run_padua_large_20_30.log` |
| 8 | `f6_diag_redundant_pivot.py` | `default_rng(2)`; n = 6, 10, 14, 20, uniform and random weights | 0 | 6.3 s | `logs/f6_diag_redundant_pivot.log` |
| 9 | `f6_pivot_threshold_test.py` | `default_rng(2)`; n = 20, 30; given order only | 0 | 104.2 s | `logs/f6_pivot_threshold_test.log` |
| 10 | `f3_qfree_vs_R_downdate.py` | seeds 0 and 1 per scenario | 0 | 33.3 s | `logs/f3_qfree_vs_R_downdate.log` |
| 11 | `qfree_bivariate_downdate.py` | module-level `default_rng(0)`, consumed over six cases in order | 0 | 8.5 s | `logs/qfree_bivariate_downdate.log` |
| 12a | `qfree_vs_conditioning.py` under `python3 -I -B` | own `default_rng(0)` | **1** | 0.1 s | `logs/qfree_vs_conditioning_I_fail.log` |
| 12b | same script under `python3 -B` (no `-I`), same empty cwd | same | 0 | 3.3 s | `logs/qfree_vs_conditioning_noI.log` |

Run 12a fails with `ModuleNotFoundError: qfree_bivariate_downdate`: unlike the other scripts it does not insert its own directory in `sys.path`, which `-I` needs. Run 12b is the same unchanged copy without `-I`; `sys.path[0]` is then the inputs directory, which contains only the 12 vetted copies and MANIFEST.md. This is a recorded deviation from the requested protocol, not a fix to the script.

Extension runs (not requested comparisons; same unchanged script, larger arguments, to extend the M range for the L5 question; each invocation has its own fresh seed-2 generator, so its random-order and random-weight draws are not those of run 7):

| # | command | exit | wall | log |
|---|---|---|---|---|
| X40 | `f6_run_padua_large.py 40` (M = 861) | 0 | 191.4 s | `logs/f6_run_padua_large_40.log` |
| X50 | `f6_run_padua_large.py 50` (M = 1326) | 0 | 546.1 s | `logs/f6_run_padua_large_50.log` |
| X60 | `f6_run_padua_large.py 60` (M = 1891) | @@X60@@ | | |

## 4. Comparison: claimed vs observed

Verdicts: **R** reproduced (printed digits agree), **D** differs (quantified), **N** not reproduced / not tested by the script.

### 4.1 F1: loss of orthogonality vs Ritz residual (run 1)

ADV §1.2 table, claimed vs observed (loss = max|QᵀQ−I|, res = min Ritz residual of Z = Uᵀ(X+iY)U; the claim's "u/res" column is evaluated with u = eps = 2.22e-16):

| Row (ADV §1.2) | claimed loss / res / (u/res) | observed loss / res / (u/res) | loss ÷ (u/res) | verdict |
|---|---|---|---|---|
| random M=1681, deg 24, N=325 | 1.8e-13 / 1.7e-3 / 1.3e-13 | 1.8e-13 / 1.7e-3 / 1.3e-13 | 1.38 | R |
| random M=1681, deg 32, N=561 | 1.8e-11 / 2.4e-5 / 9e-12 | 1.8e-11 / 2.4e-5 / 9.3e-12 | 1.95 | R |
| random M=1681, deg 40, N=861 | 8.4e-9 / 7.7e-8 / 2.9e-9 | 8.4e-9 / 7.7e-8 / 2.9e-9 | 2.91 | R |
| random M=6724, deg 40 | 8.8e-13 / 3.5e-4 / 6e-13 | 8.8e-13 / 3.5e-4 / 6.3e-13 | 1.39 | R |
| tensor Chebyshev 41², deg 40 | 9.6e-14 (flat) / 1.4e-2 | 9.6e-14 / 1.4e-2 | 6.05 (not a Ritz-driven row) | R |
| tensor 41², HL MGS + one reorth, deg 40 | 6.9e-15 | 6.9e-15 / 1.4e-2 | 0.44 | R |

Per-row ratio loss ÷ (u/res), all 57 printed rows: `analysis/f1_ratio_table_eps.txt` (u = 2.22e-16) and `analysis/f1_ratio_table_halfeps.txt` (u = 1.11e-16).

- (a) **Claim "loss ≈ u / min Ritz residual of H_x + iH_y, within 3×".** The four table rows give 1.38, 1.95, 2.91, 1.39: within 3× (the largest, 2.91, is at the edge). Over all random-node rows where the loss is clearly above its own start-up floor (loss ≥ 5 × the degree-4 loss of the same node set; 12 rows from M = 625, 1681, 2500, 6724) the ratio ranges over **0.55 to 2.91**, so the band holds on every row where a Ritz-driven rise is visible (and also falls below 1: loss can be 0.55 × u/res). In the start-up regime, where the loss sits on its floor (2e-15 to 1e-13) and res is large, the ratio is 0.33 to 15.2 (random nodes) and 2.5 to 88 (tensor grids 25² and 41²): the claim is not meant to apply there, where u/res is below the floor. Caveats that qualify the verdict: (i) it uses u = eps = 2.22e-16 (this reproduces the claim's u/res column); with u = 2^-53 = 1.11e-16 all ratios double, giving 1.1 to 5.8 on the 12 above-floor rows, of which 5 exceed 3 (including the M = 1681, deg-40 table row, 5.82), so the "within 3×" statement depends on the convention for u; (ii) one realisation per M (seed 0, no repeats, sequentially consumed generator); (iii) the Ritz residual is of Z = Uᵀ(X+iY)U with U the QR-orthonormalised computed basis, i.e. the Rayleigh–Ritz section of the span, **not** of the H_x + iH_y that the recurrence itself produces (the script never forms the recurrence's H_y); (iv) the script computes only the joint Z. It does **not** compute the Ritz residuals of H_x alone or H_y alone, so the plan's L1-Q1 kill test (single-section vs joint) is **N** here (see Runs needed). Status: MEASURED, 4 node-set realisations.
- Tensor grids: loss 1.2e-14 to 1.9e-14 (25²) and 6.5e-14 to 9.6e-14 (41²), nearly flat from deg 4 to 40, Ritz residual 0.3 → 1.4e-2: no rise, as claimed (R).
- Residual sizes: min Ritz residual falls monotonically with degree on random nodes (0.37 → 7.7e-8 at M = 1681); at M = 1681, deg 40 `#Ritz res<1e-8` is 0, i.e. the loss of 8.4e-9 occurs before any Ritz residual reaches 1e-8 (minimum 7.7e-8).

### 4.2 F6: Givens IEP vs HL etc. (runs 6, 7, X40, X50)

(b) **Relative error of (H_x, H_y)** (Frobenius, vs long-double three-pass reference), uniform weights, **given** (natural) order, Givens "scheme" rule; deterministic, so independent of seeds:

| M | Givens-scheme | HL | BJ | CGS2 | Householder | Givens ÷ HL | Givens ÷ HH |
|---|---|---|---|---|---|---|---|
| 66 | 3.3e-15 | 8.2e-16 | 5.0e-15 | 5.2e-16 | 8.3e-16 | 4.0 | 4.0 |
| 231 | 1.0e-14 | 2.6e-15 | 6.0e-14 | 1.0e-15 | 1.4e-15 | 3.8 | 7.1 |
| 496 | 2.3e-14 | 4.2e-15 | 4.6e-14 | 1.5e-15 | 1.8e-15 | 5.5 | 12.8 |
| 861 (X40) | 3.8e-14 | 6.0e-15 | 3.7e-14 | 2.1e-15 | 2.3e-15 | 6.3 | 16.5 |
| 1326 (X50) | 5.5e-14 | 8.4e-15 | 3.5e-14 | 2.5e-15 | 2.6e-15 | 6.5 | 21.2 |

**Log–log slopes** of error vs M (least squares over the points; `analysis/f6_slopes_M66_496.txt`, `analysis/f6_slopes_M66_1326.txt`; computed from the logs, the script does not print slopes):

| method | claimed (ADV §2.2, M = 66→496) | observed M = 66, 231, 496 (3 pts) | observed M = 66…1326 (5 pts) | verdict |
|---|---|---|---|---|
| Givens (scheme) | ≈ 0.96 | 0.95 | 0.95 (last pair 0.86) | R |
| HL | ≈ 0.8 | 0.82 | 0.76 (last pair 0.78) | R |
| CGS2 | ≈ 0.5 | 0.52 | 0.53 (last pair 0.40) | R |
| Householder | ≈ 0.4 | 0.39 | 0.38 (last pair 0.28) | R |
| BJ (not claimed) | n/a | 1.19, last pair −0.35 | 0.58, last pair −0.13 | erratic, not a power law |
| Givens "largest" | n/a | 6.0 (catastrophic, see 4.3) | not meaningful | n/a |

The slopes reproduce, but they rest on 3 (claimed range) or 5 sizes, one deterministic given-order node sequence, and HL's slope (0.76 to 0.82) is between √M (0.5) and M (1). Against the plan's L5 kill thresholds (Givens ≤ 0.7, or HL/CGS2 ≥ 0.9): neither triggers on these data; they do not meet the plan's design (M up to ≥ 2000, ≥ 5 orders/seeds per size). Random-order slopes are not given because each random order is a different permutation with only one or two draws per size.

**Deficit factors** (full list: `analysis/f6_deficit_factors.txt`). Claim ADV §2.2: Givens is behind HL by a factor 4 to 12 (0.6 to 1.1 digits) and behind Householder/CGS2 by 4 to 15, "for every node order and weight choice tried":

| Data set (Givens-scheme ÷ ...) | ÷ HL (digits) | ÷ Householder | ÷ CGS2 | verdict |
|---|---|---|---|---|
| Padua n = 10…30, uniform, all orders (16 rows, runs 6, 7) | 3.8 to 16.2 (0.59 to 1.21) | 4.0 to 36.1 | 6.3 to 43.3 | D: the sign and the 0.6 digit lower end reproduce; the upper ends exceed the claim (random-order n = 30: ÷HL 16.2 and 10.8/11.8, ÷HH 24 to 36) |
| Padua n = 40, 50, uniform, given / random (X40, X50) | 6.3 / 27.6 and 6.5 / 22.1 (0.80 to 1.44) | 16.5 / 69.6 and 21.2 / 73.1 | 18.1 / 80.0 and 22.0 / 73.1 | extends: deficit keeps growing with M |
| Padua random weights U(0.1,1), given order, n = 20, 30, 40, 50 | 4.2, 4.2, 5.3, 5.0 | 8.7, 13.2, 19.2, 22.2 | 10.8, 13.9, 20.0, 20.0 | R (within the claimed 4 to 12 ÷HL; ÷HH/CGS2 exceed 15 for n ≥ 40) |
| random nodes M = 105, 300, 496 (n = 6, 12, 20), 3 orders each | 1.6 to 7.1 (0.19 to 0.85) | 1.9 to 4.2 | 5.0 to 28.2 | D: the direction reproduces; at M = 496 the factor is only 1.6 to 2.2, below the claimed 4 |
| 15-point sanity case | 0.3 (Givens better) | 0.3 | 2.2 | the "systematic for every case" statement fails on this case (Givens better than HL and HH) |

Consistent with the claim, HL is worse than Householder/CGS2 as well: HL ÷ HH grows from 1.0 (M = 66) to 2.3 (496), 2.6 (861), 3.2 (1326) on the given order.

**Table ADV §2.2, row by row.**

| Row | claim | observed | verdict |
|---|---|---|---|
| Padua n=10, 4 orders: Givens 3.3 to 4.7e-15; HL 8.2 to 9.6e-16; BJ 3.9 to 5.0e-15; CGS2 5.1e-16; HH 8.5e-16 | | Givens 3.3, 4.5, 5.4, 6.4e-15; HL 7.8 to 9.1e-16; BJ 4.2 to 5.3e-15; CGS2 4.9 to 5.2e-16; HH 8.2 to 8.7e-16 | D (small): random-order Givens up to 6.4e-15 (1.4 × the claimed top); other columns agree to a few % |
| Padua n=20, given / random: Givens 1.0e-14 / 2.4e-14; HL 2.6e-15 / 2.2e-15; BJ 6.0e-14 / 1.4e-14; CGS2 1.0e-15; HH 1.4e-15 | | run 7: 1.0e-14 / 2.4e-14; 2.6e-15 / 2.2e-15; 6.0e-14 / 1.4e-14; 1.0e-15; 1.4e-15 | R (these numbers come from `f6_run_padua_large.py`, seed 2; run 6, seed 1, gives random-order Givens 1.6 and 2.2e-14) |
| Padua n=30, given / random: Givens 2.3e-14 / 4.6e-14; HL 4.2e-15 / 3.9e-15; BJ 4.6e-14 / 1.7e-14; CGS2 1.5e-15; HH 1.8e-15 | | run 7: identical | R |
| Padua n=30, random weights: 2.5e-14, 6.0e-15, 2.2e-14, 1.8e-15, 1.9e-15 | | run 7: identical | R |
| random M=496, n=20, 3 orders: Givens 2.4 to 6.0e-13; HL 1.1 to 1.2e-13; BJ 2.5 to 7.1e-13; CGS2 1.2 to 1.7e-14; HH 0.9 to 1.1e-13 | | run 6: Givens 5.9e-14 to 9.6e-14; HL 3.8 to 4.3e-14; BJ 1.1 to 2.9e-13; CGS2 3.4 to 3.6e-15; HH 2.8e-14 | **D**: absolute errors 2.3 to 6 × smaller than claimed (Givens 4 to 6 ×; BJ 2.3 ×; HL 2.8 ×; CGS2 3.5 to 4.7 ×; HH 3.2 to 3.9 ×), and the ordering changes (claimed HL ≈ HH; observed HL/HH = 1.4 to 1.5; claimed Givens/HL 2 to 5, observed 1.6 to 2.2). The claim's values cannot be tied to the committed seed (the random node set conditioning differs); no seed that produces them was found. |

### 4.3 F6: "largest" redundant-pivot rule, diagnostics, thresholds (runs 7, 8, 9, X40, X50)

ADV §2.3 table (Givens-scheme / Givens-largest, relative error of (H_x, H_y)):

| Row | claimed | observed | verdict |
|---|---|---|---|
| Padua n=20, uniform, given | 1.0e-14 / 1.1e-14 | 1.0e-14 / 1.1e-14 | R |
| Padua n=20, random weights | 1.3e-14 / 7.2e-4 | 1.3e-14 / 7.2e-4 | R |
| Padua n=30, uniform, given / random order | 2.3e-14 / 4.6e-14 and 2.0e-9 / 3.3e-12 | same | R |
| Padua n=30, random weights | 2.5e-14 / 6.9e-5 | 2.5e-14 / 6.9e-5 | R |
| random M=496, n=20 ("largest" better) | 2.4 to 6.0e-13 / 4.2 to 5.4e-14 | 5.9 to 9.6e-14 / 3.7 to 4.3e-14 (largest 0.45 to 0.64 × scheme) | direction R ("better"), absolute values D (see 4.2) |

(c) **"Largest" pivot errors, summary.** The catastrophe is not specific to one draw: Padua uniform given order 1.1e-14 (n=20), 2.0e-9 (30), 6.5e-5 (40), 3.9e-5 (50); random order 6.7e-14 (20, run 7; run 6: 8.9e-14, 9.2e-14), 3.3e-12 (30; run 6: 2.1e-12, 4.0e-12), 6.7e-11 (40), 2.8e-8 (50); random weights 7.2e-4 (20), 6.9e-5 (30), 2.0e-5 (40), 1.8e-4 (50), while "scheme" stays at 1e-14 to 2e-13 for all of these (largest ÷ scheme from 1.0 up to 1.7e9 on uniform given orders and 5.5e10 at n = 20 with random weights). The size of the failure is draw-dependent: at n = 20, 30 with random weights run 9 (another draw, same seed 2 but different consumption order) gives 3.3e-4 and 1.7e-3 instead of 7.2e-4 and 6.9e-5. The random-weight failures span 2e-5 to 2e-3 over the six draws seen, all far above scheme. The plan's L5-Q1 value "≈ 7e-4 on Padua n=20, random weights" is reproduced exactly for that draw and is a single draw.

(d-pivot) **Diagnostics (run 8).** ADV §2.3: "the residual at the unused pivot is O(1) to O(300) relative to that pivot, which is itself at noise level (~1e-17)". Observed max residual ratio: 3.0, 3.0, 0.32, 4.5 (n=6); 18, 18, 2.3, 2.3 (n=10); 7.1, 3.0e2, 15, 92 (n=14); 2.3e2, 2.3e2, 1.1e2, 1.1e2 (n=20): range 0.32 to 3.0e2: R. The unused pivot is 5e-19 to 4.4e-17 in 15 of the 16 lines (the exception: n=14, uniform, "largest": 2.1e-10, while the used pivot is 0.19): R. But the listing in ADV §5 says "both pivots sit at noise level": at the printed worst location this holds only for the four n = 6 lines (used pivot 1.2e-16 to 2.0e-16) and one n=14 line (3.5e-16); for the other 11 lines the used pivot is O(5e-3 to 0.2) while the unused one is at noise level. So "unused pivot at noise level" is R; "both at noise level" is **D**. The script does not check unisolvence of the node prefixes, so the plan's mechanism ("catastrophe only on orders with non-unisolvent intermediate prefixes") is **N** (inferred from zero pivots only, not tested).

**Skip thresholds (run 9).** ADV §2.3: "a skip threshold (1e-14 or 1e-12 relative) does not cure this, and it degrades the 'scheme' rule". Observed (relative error of (H_x, H_y), given order):

| case | scheme tol 0 / 1e-14 / 1e-12 | largest tol 0 / 1e-14 / 1e-12 |
|---|---|---|
| n=20 uniform | 1.0e-14 / 1.1e-14 / 8.2e-14 | 1.1e-14 / **7.7e-4** / 2.5e-13 |
| n=20 random weights | 1.4e-14 / 1.4e-14 / 1.4e-13 | 3.3e-4 / 2.4e-3 / 2.4e-3 |
| n=30 uniform | 2.3e-14 / 2.4e-14 / 2.8e-13 | 2.0e-9 / 1.6e-4 / 7.0e-3 |
| n=30 random weights | 3.0e-14 / 2.8e-14 / 3.2e-13 | 1.7e-3 / 1.1e-3 / 9.6e-3 |

R: no threshold cures "largest" (best case 2.5e-13, 25 × worse than scheme; at tol 1e-14 the uniform n=20 "largest" run changes from fine (1.1e-14) to 7.7e-4, so a skip threshold can create the catastrophe); the threshold 1e-12 degrades "scheme" 8 to 12 ×, 1e-14 does not.

### 4.4 F3: Q-free vs R/C downdating (runs 10, 11, 12b)

Run 10 (n = 12, N = 91). Claimed ADV §3.2 table (seed 0 = first seed) vs observed:

| Scenario | claimed Q-free / R-C / κ(R) | observed seed 0 | observed seed 1 | verdict |
|---|---|---|---|---|
| W=400, 400 steps | 3.7e-13 / 1.9e-14 / 8e1 (min(1−ℓ) 2.8e-3) | 3.7e-13 / 1.9e-14 / 8.1e1 (2.8e-3) | 6.3e-13 / 3.2e-14 / 7.9e1 | R |
| W=150 | 2.1e-9 / 3.9e-11 / 2e3 (1.4e-7) | same / 2.1e3 (1.4e-7) | 1.9e-8 / 3.4e-10 / 1.3e4 | R |
| W=100 | 1.7e-4 / 8.6e-8 / 1e5 (5.2e-10) | same / 1.0e5 (5.2e-10) | 1.8e-6 / 1.1e-9 / 8.6e3 | R |
| W=95 | 7.4e-3 / 1.6e-6 / 3e5 (3.3e-11) | same / 3.4e5 (3.3e-11) | 5.0e-5 / 1.6e-7 / 9.1e4 | R (κ = 3.4e5 vs "3e5" and "κ ≤ 3e5") |
| W=95 then grow to 400 | 6.9e-9 / 4.3e-14 / 2e2 | same / 1.9e2 | 3.4e-9 / 5.6e-14 / 5.0e2 | R (recovery of R/C reproduced) |
| W=93 then grow to 400 | 1.2e-8 / 2.6e-14 / 2e2 | same / 1.8e2 | 7.3e-9 / 5.6e-14 / 5.2e2 | R |

Ratio Q-free ÷ R/C: claimed "20 to 4000 ×": observed 19.5, 54, 1.98e3, 4.6e3 (seed 0) and 19.7, 56, 1.6e3, 3.1e2 (seed 1) on the four non-growing windows, so 20 to 4600 (the top end is 15% above the claim); on the grow-back scenarios 1.6e5, 4.6e5 (and, not in the claimed table, W=100 then grow: 1.6e6) for seed 0, 6e4 to 1.3e5 for seed 1, the Q-free error staying at 3e-9 to 5e-8 ("frozen") while R/C recovers to 1e-14 (R). The statement "second seed gives the same picture" is R. Status: MEASURED, 2 seeds, one n.

Runs 11 and 12b vs ICP table (§ on Q-free numerics):

| W | claimed error vs recompute / sensitivity to 1e-14 node noise / min(1−ℓ) | observed (run 12b) | verdict |
|---|---|---|---|
| 400 (n=8, N=45), max leverage 0.85 | 1e-14 to 3e-14 | run 11: 1.2e-14 to 2.7e-14, max leverage 0.852 | R |
| 400 | 2.5e-13 / 1.3e-13 / 3e-3 | 2.5e-13 / 1.3e-13 / 3.3e-3 | R |
| 150 | 9e-10 / 2e-13 / 2.7e-6 | 8.9e-10 / 2.2e-13 / 2.7e-6 | R |
| 100 | 1.8e-5 / 1e-12 / 9e-10 | 1.8e-5 / 1.2e-12 / 9.3e-10 | R |
| 95 | 1.2e-3 / 1e-11 / 1.3e-11 | 1.2e-3 / 1.1e-11 / 1.3e-11 | R |

Claim "the algorithmic error scales roughly like u/min(1−ℓ) times a modest factor": the observed factor error ÷ (eps/min(1−ℓ)) is 3.7 (W=400), 10.8 (150), 75 (100), 70 (95): not constant, grows by 20 × over the range, so the "roughly" holds in order of magnitude only (**D**, mild; the exponent in 1/min(1−ℓ) is about 1.2 over the four windows, from MEASURED data of one seed). Run 11 (not claimed numerically beyond the n=8 row) shows errors of 2.8e-11 to 1.3e-7 at W=150 and up to 5.5e-2 at W=95.

### 4.5 Closed-form and structure scripts (runs 2, 3, 4, 5)

(d-closed) **What `closed_form_H.py` verifies.** The family is **Padua points Pad_n (first family)** {(cos jπ/n, cos kπ/(n+1)) : 0 ≤ j ≤ n, 0 ≤ k ≤ n+1, j+k even} with the **cubature weights** 2 e_j e_k / (n(n+1)) (e = 1/2 at the grid ends), the normalized product-Chebyshev basis T_i(x)T_j(y) in graded order (degree d, x-degree descending). It builds H_x and H_y *only* from (i) the product-Chebyshev three-term multiplication rule and (ii) the reduction of degree-(n+1) products via the ideal relations T_{n+1}(x) = T_{n−1}(x), T_{n−k+1}(x)T_k(y) = s_k T_{k−1}(x)T_{n−k+1}(y), T_{n+1}(y) = s' T_n(x); the signs s_k, s' are **determined numerically in the script** and the relations are asserted with `np.allclose` (default tolerances rtol 1e-5, atol 1e-8), together with the norms d_col taken from the numerically computed Gram diagonal. It then compares with H = QᵀXQ, QᵀYQ computed from the weighted basis. Observed, for n = 5, 6, 20, 41 only (N = 21, 28, 231, 903): max |closed form − numeric| = 3.9e-16 / 4.4e-16, 3.9e-16 / 5.0e-16, 2.7e-15 / 2.2e-15, 3.7e-15 / 4.1e-15 (H_x / H_y); max nnz per column of the closed-form matrix = 2 (threshold 1e-14); both symmetric; eig(H_y) equals the y-coordinates of the nodes. The **sparsity** verified is therefore ≤ 2 nonzeros per column for the closed form (a consequence of the construction: each x- or y-multiplication produces at most two terms) and, by `padua_weights_check.py` on the numerically computed matrices (threshold 1e-12), ≤ 2 per column in the degree-<n block and in the degree-n block, with total nnz 48/49 (n=6), 440/441 (n=20), **3720/3721 (n=60, N=1891)** for H_x / H_y. Verdicts: RESULTS item 1 (orthonormality: off-diagonal Gram 7.8e-16, 3.0e-15, 7.7e-15 for n = 6, 20, 60; only T_n(x) has norm² 2.0): R. RESULTS item 2 (≤ 2 per column, nnz 3720, 3721, N = 1891 at n = 60): R exactly. RESULTS 2a "matches to 4e-15 for n ≤ 41": R at the four n tested (max 4.1e-15); the script does not test other n, and there is no proof in the inputs (the "three-line proof" and the analytic proof are not checked here). Equal weights: nnz(H_x) = 136, 3300, 77500 of N² for n = 6, 20, 60 (not sparse like the cubature case).

**Harris–Simanek (run 3).** Claim (RESULTS; OPV): every rectangular checkerboard set gives explicit H_x, H_y with ≤ 3 nonzeros per column, ≤ 2 on a symmetric side. Observed for random decreasing X, Y (m = 6, 15, 30, both parities k = 0, 1), "warped" X with Legendre–Gauss Y, and Chebyshev–Lobatto (= Padua): H_x and H_y max nnz per column 3 / 3 (random), 3 / 2 (warped; Y symmetric), 2 / 2 (Padua); (a) Gram − I ≤ 6.4e-15; (b) exactness error ≤ 2.7e-15; (e) |λ − w_Padua| ≤ 6.6e-17: R. (d) |Q_QR| vs |Q_explicit|: **D** for non-Chebyshev nodes: 5.8e-10 and 6.0e-10 (random m=15), 6.7e-5 and 8.0e-5 (random m=30), 5.1e-10 (warped m=30), against 3e-14 to 5e-14 at m=6 and 6.2e-16 at Padua m=30; the alternation-identity residual grows in step (1.5e-11 random m=15, 3.6e-12 m=30, 1.0e-10 warped m=30). The script does not diagnose the cause; ill-conditioning of the QR basis for these node sets is the plausible reading (not verified), so this is a floating-point conditioning difference, not evidence against the identity. Only three node families and one seed.

**BJ window (run 4).** Claim ICP §BJ window: the maximum number of nonzero α at degree k is 2k+1 for 2 variables and (k+1)² for 3 variables. Observed for k = 2…12: 2 variables 5, 7, …, 25 (= 2k+1); 3 variables 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169 (= (k+1)²): R. This only reproduces the script's count from its transcription of the BJ ordering rules (Thm 1 and Cor. 4); the faithfulness of the transcription to the paper is not checked here.

## 5. Runs needed (not executed)

1. **X60**: @@X60NEEDED@@
2. **M ≥ 2000** for the L5-Q1 range (plan: M from 66 to ≥ 2000, ≥ 5 node orders/seeds): the unchanged script has a fixed seed 2 per invocation, one random order and one random weight draw; n = 62 gives M = 2016. On AC's server (syvert0/1/2), per n, with a long timeout (single-thread cost grows like M³; n = 50 took 546 s here): `cd <fresh scratch dir> && OPENBLAS_NUM_THREADS=1 timeout 14400 python3 -I -B <repo>/tracks/bivariate-lanczos/code/inputs/f6_run_padua_large.py 62`. Several seeds and orders need a new driver (a new, audited script under `tracks/`), not the input script.
3. **Single-section Ritz residuals** (L1-Q1 kill test): `f1_loss_vs_ritz.py` computes only the joint Z = Uᵀ(X+iY)U. The residuals of H_x and H_y alone, of the recurrence's own H (not of U), repeated seeds, the Padua-with-cubature-weights and an irregular-domain node set are not covered and need a new script.
4. **Unisolvence of node prefixes** (L5-Q1 mechanism): no input script checks it; a prefix-by-prefix rank/unisolvence test along each node order is needed to test whether the "largest" catastrophe occurs only on non-unisolvent prefixes.
5. **Rerun by an independent party** of runs 1 to 12 (this is a developer run only; no independent rerun has been done).

## 6. Interpretation limits

- All results are single-seed floating-point observations in one environment (numpy 2.5.3 / OpenBLAS 0.3.34, x86-64); other BLAS or CPU may change low-order digits (the printed 2-digit values reproduced exactly against the claims where the same script and seed were used, which suggests the claims were produced with the same code and a similar numpy).
- The ADV §2.2 "rotation counting" explanation, the F1 "Paige mechanism" and the F3 "relational stability" attributions are interpretations ([inference] in the inputs) and are not tested by these runs.
- Nothing here upgrades any claim above MEASURED.

## 7. SHA-256 of the logs

```
@@SHA@@
```
