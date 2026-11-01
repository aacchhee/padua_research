# PD-T?bivariate-lanczos-claude-502 — Measured growth of the Givens-updating error with M (Padua and random nodes, M = 66..2016)

Final ID: **PD-T078** (allocated at PR preparation, 2026-11-01; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-T.
Aliases: Givens deficit slopes; L5-Q1 first clause; IDEA?bivariate-lanczos-claude-501 (test of seed IDEA 015).
Split from: none.
Split into: none (the worst-case bound is `givens-updating-rotation-count-backward-bound.md`; the pivot-rule failure is PD-N?bivariate-lanczos-claude-506).

## Statement

[FP, MEASURED] Within the recorded scope below, the relative Frobenius error of the leading N×N blocks of (H_x, H_y) computed by (a) point-by-point Givens updating with the fixed 'scheme' rule (Van Barel–Chesnokov 2010, Algorithm 1, real nodes), (b) the HL recurrence (window 2 degrees, MGS + one reorthogonalisation), (c) BJ (same window, CGS, no reorthogonalisation), (d) full CGS2, (e) Householder QR of the weighted Chebyshev–Vandermonde matrix, against a long-double three-pass-reorthogonalised reference, has the following behaviour in M.

**Headline: the frozen kill test fires as written (reconstruction finding M3).** Plan L5-Q1 and the criterion pre-registered in candidates.md (IDEA 501) kill the rotation-counting explanation for a family if the Givens-scheme slope is <= 0.7 or the HL or CGS2 slope is >= 0.9, on the full range or on M >= 496, and call it not killed overall only if no family triggers. **The uniform-density random-node family triggers it** (CGS2 1.57, HL 2.28 on the full range; also on M >= 496). So the verdict on the test as written and as operationalised is **KILLED (in that family)**. The reading 'not killed in the four other families' (Padua with cubature, U(0.1,1) and unit weights; arcsine-density random nodes) is a **post-hoc reading**: it rests on (i) excluding the uniform family as confounded (a confound was anticipated, no exclusion rule was pre-registered) and (ii) adding the arcsine family after the runs had started (the arcsine family only reaches M = 1326). Both steps are disclosed here and in R01.

Primary table: slopes of the per-size mean of log10 error against log10 M (the effective sample is the number of sizes, 7 for M = 66..2016; 95% t-interval with df = sizes − 2; `logs/analysis_r01c.txt`, produced by `analyze_r01c.py`). 'quad' is the coefficient of (log10 M − mean)² in the quadratic fit (t-statistic in brackets).

| family / class | Givens-scheme | HL | BJ | CGS2 | Householder |
|---|---|---|---|---|---|
| Padua, cubature, 5 orders | 1.40 [1.01, 1.79]; quad +0.73 (3.7) | 0.73 [0.69, 0.77] | 1.17 [0.87, 1.48] | 0.48 [0.44, 0.53] | 0.38 |
| — structured orders (given, sortx) | 0.93 [0.88, 0.99]; quad +0.07 (1.5) | 0.80 [0.71, 0.88] | 1.31 [0.64, 1.97] | 0.50 | 0.37 |
| — random orders (rand1–3) | 1.71 [1.07, 2.35]; quad +1.17 (3.4) | 0.69 | 1.09 | 0.47 | 0.38 |
| Padua, U(0.1,1) weights, 5 orders | 1.55 [1.03, 2.06]; quad +0.93 (3.4) | 0.79 [0.74, 0.84] | 1.01 [0.82, 1.19] | 0.53 [0.50, 0.56] | 0.38 |
| — structured / random | 0.92 [0.88, 0.97] / 1.96 [1.13, 2.79] | 0.81 / 0.78 | 1.05 / 0.98 | 0.54 / 0.53 | 0.38 / 0.38 |
| Padua, unit weights, M = 66, 231, 496, 861 | 1.08 [0.81, 1.34] (df 2) | 0.77 [0.65, 0.88] | 0.65 [−0.45, 1.75] | 0.52 [0.50, 0.55] | 0.38 |
| random, arcsine density, M = 66..1326 | 1.28 [0.96, 1.60] (df 4) | 0.71 [0.69, 0.73] | 1.12 [0.94, 1.31] | 0.38 [0.35, 0.41] | 0.28 |
| **random, uniform density, M = 66..2016 (confounded)** | 2.87 [1.79, 3.96]; quad +2.16 (5.6) | 2.28 [1.66, 2.89] | 2.76 [2.14, 3.38] | **1.57 [1.01, 2.13]** | 2.11 [1.58, 2.64] |

Corrections to the earlier version of this table (reconstruction finding M2): the earlier intervals (e.g. Padua cubature 1.40 [1.09, 1.70]) came from OLS over all 35 (order, size) points and a within-size bootstrap, which treat the replicates of one size as independent evidence about the power law; they were too narrow. The size-level intervals above are the primary ones. The log–log curve for Givens-scheme is **convex** in the pooled Padua families (quad +0.73 and +0.93, t about 3.5) and the random orders (+1.2 to +1.5), so a single power law is a poor summary there: only the structured-order slope 0.93 [0.88, 0.99] shows no detected curvature (quad not significant at seven sizes: absence of detected curvature, not evidence for an asymptotic power law); the pooled 1.40/1.55 mixes it with a convex random-order curve that is associated with prefix conditioning (PD-T?bivariate-lanczos-claude-503 C reports a correlation only and does not establish causality; rotation count is neither confirmed nor excluded as a contributor). **The upper-range slopes (M >= 496, 4 sizes, df 2) are not statistically supported:** Padua cubature Givens 2.15 [0.60, 3.71], U(0.1,1) 2.50 [0.31, 4.70], with large quad terms; the arcsine family has df 1 there. The earlier cluster-bootstrap intervals in `logs/analysis_r01.txt` are retained as the original output and are superseded by `analysis_r01c.txt`.

Secondary, post-hoc and disclosed: **exploratory Householder-ratio comparison** (heuristic; per instance log10(error/Householder error), then the size-level fit). The point estimates are retained: Padua cubature Givens 1.02 [0.62, 1.42], HL 0.35 [0.30, 0.40], CGS2 0.11 [0.06, 0.15], BJ 0.80; Padua U(0.1,1) Givens 1.17 [0.65, 1.69], HL 0.41, CGS2 0.15; arcsine random Givens 1.00 [0.66, 1.34], HL 0.43, CGS2 0.10; **uniform random** Givens 0.76 [0.06, 1.46], HL 0.16 [−0.04, 0.37], CGS2 −0.54 [−0.72, −0.36], BJ 0.65 (they agree with the reviewer's independent re-analysis of the same logs: 0.76 [0.06, 1.46], HL 0.16, CGS2 −0.54). Dividing by the Householder error of the same instance would remove a per-instance conditioning factor only if the errors of all methods carried a common multiplicative dependence on the instance's conditioning; that assumption is neither made nor established here. The comparison is therefore heuristic and does **not** show that the conditioning confound of the uniform family is removed (audit-01 L5 M1). It also cannot change any pairwise comparison between the unnormalised methods: for paired errors G, H and Householder B, log(G/B) − log(H/B) = log(G/H), so the normalised slope difference (Givens − HL) equals the unnormalised one. The normalisation was chosen after seeing that the uniform family kills the test; it does not change the as-written verdict.

**Paired slope differences** (audit-01 L5 M1; `logs/analysis_r01d.txt` from `analyze_r01d.py`, a reanalysis of the committed logs; slope of the size-mean of log10(error_A/error_B) against log10 M, which equals slope(A) − slope(B); 95% t-intervals at size level, df = sizes − 2; descriptive estimates from 4–7 sizes that share nodes and have partly convex log–log curves, not significance tests and not causal statements):

| family / class | Givens − HL | Givens − CGS2 | Givens − Householder |
|---|---|---|---|
| Padua cubature, 5 orders | 0.668 [0.275, 1.060] | 0.914 [0.552, 1.276] | 1.019 [0.622, 1.416] |
| — structured (given, sortx) | 0.137 [0.031, 0.242] | 0.435 [0.382, 0.488] | 0.559 [0.502, 0.617] |
| — random (rand1–3) | 1.022 [0.389, 1.654] | 1.233 [0.633, 1.834] | 1.325 [0.676, 1.975] |
| Padua U(0.1,1), 5 orders | 0.756 [0.260, 1.251] | 1.015 [0.521, 1.509] | 1.168 [0.649, 1.686] |
| — structured / random | 0.116 [0.066, 0.165] / 1.183 [0.376, 1.990] | 0.386 [0.358, 0.413] / 1.435 [0.624, 2.245] | 0.543 [0.492, 0.593] / 1.584 [0.747, 2.421] |
| Padua unit weights (4 sizes, df 2) | 0.312 [−0.006, 0.631] | 0.556 [0.291, 0.821] | 0.696 [0.390, 1.002] |
| random, arcsine density (6 sizes, df 4) | 0.568 [0.245, 0.891] | 0.900 [0.566, 1.235] | 1.002 [0.664, 1.341] |
| **random, uniform density (confounded)** | **0.595 [−0.111, 1.301]** | 1.302 [0.620, 1.984] | 0.758 [0.057, 1.459] |

The Codex audit's independent calculation of the two uniform-family differences is 0.5953256 [−0.1106994, 1.3013506] (Givens − HL) and 1.3020027 [0.6202911, 1.9837143] (Givens − CGS2). The Givens − HL interval contains zero in the uniform-random family and in the Padua unit-weight family; in the other families the lower ends are positive, and the difference is small (0.12–0.14) for the structured orders. No resolved Givens-versus-HL rate separation is asserted for the uniform family; the point estimates are positive but the evidence is exploratory.

**What is and is not supported.** (1) In point estimates the Givens-scheme slope exceeds the HL, CGS2 and Householder slopes in every family (paired Givens − HL differences 0.12–1.18 across the families and order classes of the table above; Padua families as a whole 0.31–0.76); the Givens − HL interval contains zero in the uniform-random and unit-weight families and the difference is small for the structured orders (0.12–0.14). These are descriptive estimates, neither significance tests nor a causal attribution, and they do not establish a resolved uniform-family Givens-versus-HL rate separation. (2) A slope of about 1 is the only well-described slope for the structured orders (no curvature detected at seven sizes: absence of detected curvature, not proof of an asymptotic power law); on random orders the curve is convex (1.7–2.0 pooled), with the order dependence of PD-T?…-503 (an association only). (3) The HL slope (0.69–0.81) lies between ½ and 1, above the ½ of CGS2 and Householder: 'HL ∝ √M' is **not supported**, only HL < 0.9. (4) Nothing here distinguishes coherent from random accumulation of rotation errors. (5) The kill test cannot detect growth that is too steep (reconstruction finding L4): a Givens slope of 1.7–2.0 passes the '<= 0.7 kills' clause although the rotation-count picture does not predict it either; this is a remark on the frozen design, not a change to it. (6) The failed frozen criterion (Headline) is preserved unchanged: neither the Householder-ratio estimates nor the paired differences are part of it, and none of them revives the rotation-counting explanation as tested.

## Definitions

Error = ‖(Ĥ_x − H_x^ref, Ĥ_y − H_y^ref)‖_F / ‖(H_x^ref, H_y^ref)‖_F over the leading N×N blocks after fixing signs so that the primary pivots are positive; reference = `F.reference` of `f6_givens_vs_hl_deficit.py` (long double, three passes, full reorthogonalisation) on the unpermuted nodes (H is independent of the node order in exact arithmetic). Padua order labels: given (natural j-major order of the first family), sortx (lexicographic), rand1–3 (permutations with seeds 10n+k). Padua weights: normalised cubature weights; 'U(0.1,1)' weights are one vector per n, `default_rng(1000+n).uniform(0.1,1,N)`, shared by the five orders. Random nodes: seeds 7000·k+M, k = 1..5, unit weights, N = (n+1)(n+2)/2 with n = 5, 8, 11, 17, 22, 28, 34 for M = 66, 136, 231, 496, 861, 1326, 2016.

## Assumptions

IEEE double, numpy 2.5.3 / scipy 1.18.1 / Python 3.13, OPENBLAS_NUM_THREADS=1, x86-64; the C port of Givens (`givens_core.c`) was checked bit-identical to the unchanged input `givens()` at n = 6, 10, 14 (max |ΔH| = 0.0). The Givens Q is not accumulated in the C port (the metric is the H error only). The slope is an OLS fit in log–log over a 30-fold range of M; sizes are not independent (the same nodes), and slopes beyond the range are not claimed.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| table of size-level slopes, curvature, the as-written kill verdict, the exploratory Householder-ratio analysis and the paired slope differences (descriptive; no significance or causal claim) | MEASURED | `logs/r01_padua_cub.jsonl`, `r01_padua_rand.jsonl`, `r01_padua_unif.jsonl`, `r01_random.jsonl`, `r01_random_cheb.jsonl`; `logs/analysis_r01.txt` (original), `logs/analysis_r01c.txt` (size-level, primary) |
| interpretation: rotation counting | OPEN | worst-case bound (PD-T?…-501) gives M^{3/2} relative; no model in this file predicts the observed ≈ M^1 |

Candidate / claim disposition: IDEA?bivariate-lanczos-claude-501 (rotation counting explains the deficit): pre-registered kill criterion FIRED as written in the uniform-density random family (post-hoc reading: not killed in the other four families); see candidates.md.

## Depends on

Input code `f6_givens_vs_hl_deficit.py` (unchanged, unaudited input). `givens-updating-rotation-count-backward-bound.md` for the worst-case comparison. No registry dependency.

## Checks

Producer commands: `OPENBLAS_NUM_THREADS=1 python3 -I exp_r01.py FAMILY OUT.jsonl [sizes]` (FAMILY ∈ padua_cub, padua_rand, padua_unif, random, random_cheb) in `tracks/bivariate-lanczos/code/L5/` (library `l5_lib.py`, C core `givens_core.c`; build `gcc -O2 -ffp-contract=off -shared -fPIC -o libgivens_core.so givens_core.c -lm`); analysis `python3 -I analyze_r01.py LOGDIR` (original) and `python3 -I analyze_r01c.py LOGDIR > logs/analysis_r01c.txt` (size-level intervals, curvature, Householder-normalised; added after review). Rules/base SHA of the repository clone at run time: `2d8c3ab8348be80a6f16f69ee7ef9c7bb66ed42e` (read-only `git rev-parse`); code uncommitted at run time, so the sha256 of the scripts is in the first (`meta`) line of every jsonl. `exp_r01.py` was edited once after the Padua and uniform-random runs had started (added the `random_cheb` family and `np.clip` in the conditioning computation; no change to the computation of the reported errors). The runs shared two cores with other agents' jobs; timings are not reported. Paired differences: `python3 -I analyze_r01d.py LOGDIR > logs/analysis_r01d.txt` (added for audit-01 M1/L2; reanalysis of the committed logs, no new experiment; the check column of its output confirms that each paired slope equals the difference of the marginal slopes). Independent reanalysis/rerun: Codex audit-01 (`audit-01/L5.md`; Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0) reproduced the uniform-family paired differences (`audit-01/L5/diagnostics.jsonl`) and reran the uniform family on fresh data (35 size/seed cases, M up to 2016): full-range size-level slopes Givens-scheme 2.87152 [1.78578, 3.95726], HL 2.27619 [1.66055, 2.89184], CGS2 1.56952 [1.01274, 2.12630], Householder 2.11374 [1.60257, 2.62492], so the failure of the original criterion reproduces. That rerun covers the uniform family only.

## Sources

Seed claim: `adv_F1_F6_F3.md` §2.2 (unaudited input; slopes 0.96/0.8/0.5/0.4 for M = 66–496). VB–C 2010 Table 2 (p. 401: ratio 20–60 of 'norm1' to 'norm2' at 496–1326 Padua points, a different protocol: polynomial recovery) fulltext read. Not reproduced here: Table 2's protocol.

## Proof or evidence

Measured only; see Checks. No general claim.

## Scope

Padua first-family sets (M = N), nodes in [−1,1]², uniform/arcsine random nodes with M/N ≈ 3, one machine, one BLAS; the Householder/CGS2/HL implementations are those of the unchanged inputs (not tuned). Slopes in M mix algorithmic and node-order effects (see 503) and, for random nodes, problem conditioning.

## Open items

(1) Larger M (> 2016) and a cleaner conditioning-controlled random family (M ≫ N; the present arcsine family is only fitted to M = 1326). (2) A model explaining slope ≈ 1 for structured orders. (3) Independent rerun on AC's servers (Runs needed in R01.md). (4) Any 'removal of conditioning' reading of the Householder ratios needs a stated and tested model (for example a common multiplicative conditioning factor); until then the ratios are exploratory. Paired-difference uncertainty for M > 2016 and for a conditioning-controlled random family is not available.

## History

2026-10-31, Claude Sonnet 5.5 (high), L5 R01: created from the logs listed above.

2026-10-31T22:58Z, Claude Sonnet 5.5 (high), response to L5 reconstruction 01: findings M2 (size-level intervals, curvature, upper range unsupported), M3 (headline reordered: kill fires as written in the uniform family; Householder-normalised analysis added as post-hoc secondary), L4 (design remark), I1.

2026-11-01T08:21:01+01:00, Claude Sonnet 5.5 (high), response to Codex audit-01 (L5) finding **M1** (Householder ratios do not establish removal of conditioning). Status unchanged (MEASURED); the failed frozen criterion is preserved. Changes, original wording quoted: (a) "removes the per-instance conditioning that confounds the uniform family" replaced by an explicitly heuristic description (the ratio removes a conditioning factor only under an unstated common-multiplicative-factor assumption; identity log(G/B) − log(H/B) = log(G/H)); the heading "Householder-normalised comparison" became "exploratory Householder-ratio comparison", all point estimates kept. (b) "The Givens-versus-HL/CGS2 separation therefore survives the conditioning confound in the uniform family, with a wide interval for Givens" deleted; replaced by the paired-difference table (Givens − HL uniform 0.595 [−0.111, 1.301], which contains zero; Givens − CGS2 1.302 [0.620, 1.984]) and the statement that no resolved uniform-family Givens-versus-HL separation is asserted. (c) "(1) Givens-scheme grows faster than HL/CGS2/Householder in every family, by a slope difference of 0.3–0.8 (Padua) and a normalised difference of 0.6–0.9." replaced by a point-estimate statement with the paired differences, labelled descriptive (no significance or causal claim). (d) "driven by prefix conditioning (PD-T?bivariate-lanczos-claude-503 C), not by rotation count" replaced by "associated with prefix conditioning ... correlation only ... rotation count neither confirmed nor excluded". (e) Supplementary audit remark: "(2) A slope of about 1 is clean only for the structured orders" and "is a clean power-law statement" replaced by "no curvature detected at seven sizes: absence of detected curvature, not proof of an asymptotic power law". (f) Added clause (6) preserving the failed frozen criterion, the audit's independent rerun/reanalysis figures in Checks, Open item (4), and the new script `analyze_r01d.py` with output `logs/analysis_r01d.txt`.
