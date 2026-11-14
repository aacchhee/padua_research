# code/mp: Morrow-Patterson points (direction X2), G0 / C-MP / G1-MP

Environment: python 3.13, numpy 2.5.3, scipy 1.18.1, mpmath 1.4.1 (pure python backend), python-flint (arb). Machine: 2 cores, shared with the X1 job (runtimes below are wall times under that load).
Run everything from this directory (`code/mp/`). Outputs go to `../../evidence/`; raw output to `/tmp/mp-runs/` (not committed).

## Files
| file | role |
|---|---|
| `mp_exact.py` | Path A: arb Vandermonde in the basis U_i(x)U_j(y), i+j<=n; Lagrange enclosures by solving V^T l = phi(P); determinant enclosure; adaptive precision (256 bits first) |
| `mp_kernel.py` | Path B: kernel formula (sum form, mpmath), omega (sum and closed form), Beberok closed form of K(1,1,w,v), float64/longdouble models, separable grid evaluation |
| `g0_check.py` | G0 checks, even n = 2..12, plus published Lambda_MP/Lambda_EMP at n = 34, 48, 62, 76 -> `evidence/mp-g0.json` |
| `cmp_generate.py` | C-MP, Path A: enclosures of lambda_n at the four vertices, even n <= 30 -> `evidence/mp-cmp-certificate.json` |
| `cmp_check.py` | C-MP checker, Path B only (mpmath.iv intervals, sum-form kernel, self-contained) -> `evidence/mp-cmp-check.json` |
| `cmp_identify.py` | MEASURED PSLQ identification of lambda_n(1,1), lambda_n(1,-1), n <= 10 -> `evidence/mp-cmp-identify.json` |
| `g1_screen.py` | G1-MP screen, even n = 2..60 -> `evidence/mp-g1-summary.json` |
| `corner_values.py`, `corner_analysis.py`, `corner_limit_heuristic.py` | lambda_n(1,1), even n <= 2000, analysis, heuristic limit -> `evidence/mp-corner-values.json` |

## Commands (as run) and wall times
```
python3 g0_check.py --out ../../evidence/mp-g0.json                 # 92 s
python3 cmp_generate.py --out ../../evidence/mp-cmp-certificate.json # 62 s
python3 cmp_check.py                                                 # 63 s  (reads the certificate, writes mp-cmp-check.json)
python3 cmp_identify.py --nmax 10 --dps 600                          # 98 s
python3 g1_screen.py                                                 # 945 s (raw files /tmp/mp-runs/g1_raw_nNN.json)
python3 g1_screen.py --from-raw                                      # <1 s: compact summary (< 16 KiB) rebuilt from the raw files of the run above
python3 corner_values.py                                             # 1248 s (float stage 1004 s, mp30 spot checks to n = 2000: 157 s for n = 2000)
python3 corner_limit_heuristic.py 401                                # 20 s -> c = 0.5169536534 (conjectural derivation)
python3 corner_analysis.py --heuristic 0.5169536534                  # <1 s, appends "analysis" to mp-corner-values.json
```
The G1 summary in the repository was produced by the full run followed by `--from-raw` (the first full run wrote an 18.9 KB file; the compact form is the one kept).

## Conventions and interpretation choices (flagged)
* Nodes, space, kernel: `literature-xu-mp.md` section 2. EMP: nodes scaled by 1/cos(pi/(n+2)) in x, 1/cos(pi/(n+3)) in y; its Lebesgue function on Q equals lambda_MP(a x, b y) with a = cos(pi/(n+2)), b = cos(pi/(n+3)) (same space Pi_n), so Lambda_EMP is a maximum of lambda_MP over the sub-rectangle [-a,a]x[-b,b]; it is computed on the grid of the screen plus an L-BFGS-B refinement.
* G0 "agreement to 1e-30 relative": max_a |l_a^A(mid) - l_a^B| / max(1, max_a |l_a^B|) over all nodes and the 200 random points (numpy default_rng(20261114).uniform(-1,1,(200,2))), and relative agreement of lambda.
* G1 grid local maxima: interior points compared with all 8 neighbours (mirror row at theta = pi/2); open-edge points (x = 1, y = +-1) compared only with their two neighbours along the edge (1-D faces); the 4 vertices are 0-D faces. Threshold 0.9*max(lambda(1,1), lambda(-1,1)) as in the addendum. Because NO non-vertex local maximum reaches the threshold at any n, the pre-registered candidate set is empty; for a meaningful g_n the three highest non-vertex grid local maxima are refined anyway and labelled `context_only` (float64 L-BFGS-B with analytic gradient, then Newton at 40 digits on a sign-frozen polynomial, accepted only if the sign pattern is confirmed by an exact full sum at the polished point: `mp_ok`).
* The 60-digit re-polish (required if g_n < 1e-6) was never needed: min g_n = 0.444.
* mpmath polish uses the closed-form omega (verified against the sum form in G0 for n <= 12).
* lambda_n(1,1) for n up to 2000 uses the closed form with the exact integer angle differences (delta = q(n+2) - p(n+3)) in x87 long double; compared with mpmath 30 digits at 13 values of n, max relative error 9.7e-17.

## Labelling
Everything in the evidence files is MEASURED except where a row says "certified" (arb / mpmath.iv enclosures). The limit constant in `mp-corner-values.json` is MEASURED (fits) and CONJECTURAL (heuristic derivation); nothing here is a proof (G5).
