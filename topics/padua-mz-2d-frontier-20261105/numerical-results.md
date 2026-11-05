# Final numerical record — 2026-11-05

Rules/input: `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`. Codex numerical subagent, delegated gpt-6.1-sol medium (resolved runtime metadata not independently exposed). **All numerical observations here are MEASURED**, without rigorous enclosures. G0 was independently completed and explicitly released by the orchestrator before these runs. No Git operations were performed by this worker.

## Gate dispositions

| Gate | Numerical disposition | Exact scope / limitation |
| --- | --- | --- |
| G1 floating solver | Validated; endpoint grid through m400, minima through1600 | Matrix-free O(m³) tensor contractions, O(m²) operator storage. DCT-I accelerates weight formation; this is not a fast Legendre transform. Native certification belongs to a separate worker. |
| G2 scaling laws | INCONCLUSIVE | Preregistered heldout full endpoint rows600/800/1000 incomplete after upper600 cost stop. No fit winner or endpoint order asserted. |
| G3 localization | KILL for R1 as stated | Upper edge-union K10 mass .29345 at m400, below original50% threshold. This does not exclude other limiting operators. |
| G4 integer float screen | Partial completed scope, no hits | Every m2..239, n=m−1 andm−2; requested240..300 unexecuted after dated priority change. Separate exploratorym1600 minimum is negative but uncertified. |

The orchestrator stopped further numerical extension once an independent analytic countersequence changed the need for a finite complement. That mathematical result is owned and documented by the mathematics worker; this file does not promote it into a numerical certification. No job owned by this numerical worker remains running.

## Environment and operator validation

Python 3.12.14 (main, Aug 25 2026, 14:00:49) [Clang 22.1.3 ]; NumPy2.3.5; SciPy1.17.0; Linux-6.18.57-x86_64-with-glibc2.41. Every numerical command used `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`; seed20261105, eigsh tolerance2e−11, ncv40 unless noted. Full command, code SHA-256, frozen definitions/code hashes and environment are in the receipts.

Normalized Legendre products make continuous H=I algebraically. The signed nodal Gram is applied by tensor contractions without forming its matrix. DCT-I weights are the same finite kernel polynomial as the frozen producer, including the exceptional T_m coefficient. Dense validationm10/20/30/40 passed: maximum weight difference6.94e−17, vector discrepancy3.80e−15, extrema difference1.78e−15. Additional oddm9/11 validation passed, maximum extrema discrepancy1.55e−15; this checks parity absent from the original even grid. Short receipt `evidence/g1-validation.json`; odd receipt remains in scratch with identity below.

## Completed endpoint measurements

| m | lambda_min | lambda_max | seconds | max residual |
| --- | --- | --- | --- | --- |
| 60 | 0.188593480489 | 1.80201114992 | 0.100 | 2.03e-11 |
| 80 | 0.172730495887 | 1.81649791422 | 0.252 | 9.14e-12 |
| 100 | 0.161748411019 | 1.82658242385 | 0.486 | 8.44e-12 |
| 120 | 0.153528992119 | 1.83417565038 | 0.858 | 1.52e-11 |
| 150 | 0.144291028147 | 1.84276943064 | 1.784 | 2.48e-11 |
| 200 | 0.133559661782 | 1.85284883045 | 4.585 | 3.7e-11 |
| 250 | 0.126038561644 | 1.85998565379 | 14.589 | 1.93e-11 |
| 300 | 0.120355012342 | 1.86542395944 | 23.449 | 3.04e-11 |
| 400 | 0.102818906234 | 1.87336229082 | 29.632 | 2.84e-11 |

Full completed rows are in `evidence/g1-scaling.json`. The original ncv40 process was interrupted after an observed311s total, with upperm600 unfinished after roughly240s. Its completed rows stop at400. A saved m600 minimum vector was reapplied once: Rayleigh+.06618340588496109, residual2.07e−13; this was a diagnostic, not a completed two-endpoint receipt.

The permitted cost-driven ncv increase to120 did not complete upperm600: stopped at observed640s wall,462sCPU,RSS246,916KiB. No m800/1000 upper solve started. Both SIGINT traces remain in scratch logs. G2 fit runner executed and returned “inconclusive: incomplete preregistered grid”; `evidence/g1-fits.json`. The original training/heldout protocol in `numerical-plan.md` was not changed.

## Minimum-only exploratory sign screen

After observing the corner branch, the orchestrator requested minima800/1000/1200/1600. m>1000 is explicitly post hoc and outside G2/G4. Each normalized vector was saved immediately. All four jobs completed, with n=m−1:

| m | minimum Rayleigh | residual | matvecs | seconds |
| --- | --- | --- | --- | --- |
| 800 | 0.0400252621515716 | 2.47e-14 | 162 | 32.930 |
| 1000 | 0.0196594720137416 | 1.65e-13 | 142 | 50.756 |
| 1200 | 0.00297687254955763 | 4.66e-14 | 142 | 106.190 |
| 1600 | -0.0234144165903457 | 1.95e-13 | 122 | 307.006 |

**m1600 negative candidate:** vector `/tmp/g1-frontier/minimum-only-vectors/m1600-n1599-min.npy`,10,246,528bytes, SHA-256 `a23cb0e6e241993e5458474c64f153c965e8dc5047c2f1dfe08c7bc293e0a338`. Dimension1,280,800; process peakRSS703,852KiB. Root and upper-mathematics worker were alerted immediately. `evidence/g1-minimum-only.json` preserves the finite observation. This is not a certified finite counterexample or PD-N. An exact/outward finite witness and independent rerun remain necessary if the explicitm1600 claim is to be certified. The orchestrator explicitly deferred that separate finite-threshold task because the analytic campaign result suffices for its scope.

## G3 continuous mass localization

Angles alpha,beta in[0,pi]; physical mass is |p(cos alpha,cos beta)|² sin alpha sin beta d alpha d beta. Corner squares require both endpoint angle distances<=K/m; edge union requires either, including corners. Thus corner+edge neighbourhood means the edge union, never a double-counted sum. Fractions at K10:

| m | minimum corner | minimum edge union | maximum corner | maximum edge union |
| --- | --- | --- | --- | --- |
| 100 | 3.505971e-08 | 0.3205391924 | 1.076164e-11 | 0.4401355965 |
| 200 | 6.5862395e-10 | 0.2166873672 | 5.3007352e-14 | 0.3577648695 |
| 400 | 0.77750867 | 0.8813374365 | 1.9065049e-16 | 0.2934515682 |

All K2/5/10 corner, edge-only and bulk fractions are in `evidence/g1-localization.json`. Tensor Gauss-Legendre integrates nine physical rectangles with orders n+1 andn+9 per coordinate, algebraically exact in degree apart from floating arithmetic. Largest fraction change6.48e−11; maximum observed total-mass error over either order1.93e−10. At m400 upper mass is diffuse, killing original R1; lower mass becomes corner concentrated after being diffuse at100/200. This suggests a branch crossing, not an asymptotic theorem. G3 m400 total32.64s, peakRSS95,964KiB.

## G4 final finite scope

Every integer m2..239 was completed at both n=m−1 andn=m−2: 476 rows; no lambda_min<=0 orlambda_max>=2 hits. Sum of per-row elapsed times1106.556s; process peakRSS71,192KiB; largest eigenpair residual3.7e-11. Smallest measured minimum .10489783128705327 and largest measured maximum1.8584608499872286 both occur at m239,n238. Exact coverage and bulk hash are in `evidence/g1-screen.json`.

The process was stopped only after completing its then-current row (m239,n237), on the orchestrator’s dated instruction to prioritize the analytic resolution. No m240..300 scan or certified every-integer range is claimed. The separatem1600 negative hit is outside this scan. No-hit finite measurements do not establish positivity or an upper threshold.

## Additional bounded probes requested by mathematics worker

Fejér candidate `ideas-f12.md`, IDEA?mz2d-frontier-codex-14, primary prewritten ratio(.65,.30); additional root-requested probes(.55,.40),(.75,.20). p=F_r(x)F_s(y), F_r(cos t)=(r+1)^−1[sin((r+1)t/2)/sin(t/2)]². Closest predecessors IDEA-216/217/218/226; PD-N047 addresses critical CC factors, not this asymmetric variant. No novelty or logarithmic-instability claim is made here.

| m | Fejér(.65,.30) | Fejér(.55,.40) | Fejér(.75,.20) | single corner kernel | carrier |
| --- | --- | --- | --- | --- | --- |
| 100 | 0.9835879889 | 1.003623327 | 0.9625161236 | 0.7256428992 | 1.023232731 |
| 400 | 0.979406536 | 1.002879555 | 0.9517942394 | 0.5596513309 | 1.031458724 |
| 1000 | 0.9758610754 | 1.002555857 | 0.943288275 | 0.4514285954 | 1.037705583 |
| 2000 | 0.9729914746 | 1.002335435 | 0.9365180175 | 0.369957668 | 1.042625338 |

All these quotients remain positive; finite positivity does not rule out eventual instability. Fejér mass denominators use independent degree-adequate1-D Gauss integrals and eight-node refinement (maximum relative change4.54e−8). Corner-kernel coefficients are sqrt((2i+1)(2j+1))/2 for i+j<m, normalized in continuous mass; sym/antisym combinations with the second retained corner were also tested, within1.01e−5 of the single-corner quotient. The second retained corner is(−1,1) for evenm and(1,−1) for oddm.

Even-m carrier p=.5[T_(m/2−b)−T_(m/2+b)]F_r(x)F_s(y), b=floor(.1m),r=s=floor(.15m), degree .9m. Grid evaluation uses sin(j*pi/2)^2=0/1 exactly; denominator Gauss refinement error<=1.89e−9. Slow observed growth does not establish growth to infinity. Receipts: `evidence/g1-fejer.json`, `g1-corner-trial.json`, `g1-carrier.json`.

Carrier receipt also records eight fixed-node ratios m^4*w_jk/logm against proposed constants, without claiming convergence. At m2000:(0,0)−3.87334;(0,2)−.502711;(1,1)+37.5293;(2,2)+91.7068;(3,3)+240.408. Large noncorner preasymptotic discrepancies remain. Floating edge weight at(0,2) changes from positive at100 to negative at2000; no exact sign proof is supplied by this observation.

## Executed commands and bulk identities

Working directory `/workspace/padua_research`. Prefix every command below with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`. All use `python topics/padua-mz-2d-frontier-20261105/code/` plus the named script:

```sh
g1_spectral.py --validate 10 20 30 40 --output /tmp/g1-frontier/validation.json
g1_spectral.py --validate 9 11 --output /tmp/g1-frontier/validation-odd.json
g1_spectral.py --m 60 80 100 120 150 200 250 300 400 600 800 1000 --output /tmp/g1-frontier/scaling.json --vector-dir /tmp/g1-frontier/vectors
g1_spectral.py --m 600 800 1000 --ncv 120 --output /tmp/g1-frontier/scaling-extension.json --vector-dir /tmp/g1-frontier/vectors
g1_spectral.py --m 100 200 400 --localize --output /tmp/g1-frontier/localization.json
g1_spectral.py --m $(seq 2 300) --offsets 1 2 --output /tmp/g1-frontier/screen.json
g1_minimum.py --m 800 1000 1200 1600 --output /tmp/g1-frontier/minimum-only.json --vector-dir /tmp/g1-frontier/minimum-only-vectors
g1_fejer.py --m 100 400 1000 2000 --output /tmp/g1-frontier/fejer.json
g1_corner_trial.py --m 100 400 1000 2000 --output /tmp/g1-frontier/corner-trial.json
g1_carrier.py --m 100 400 1000 2000 --output /tmp/g1-frontier/carrier.json
g1_fit.py /tmp/g1-frontier/scaling.json --output /tmp/g1-frontier/fits.json
g1_summary.py /tmp/g1-frontier/scaling.json --full-rows --output topics/padua-mz-2d-frontier-20261105/evidence/g1-scaling.json
g1_summary.py /tmp/g1-frontier/screen.json --output topics/padua-mz-2d-frontier-20261105/evidence/g1-screen.json
```

Actual stderr/stdout logs have matching scratch basenames; scaling-extension.json was never created because no full row completed. Both scaling jobs and the final G4 process ended by intentional SIGINT, not solver success. Other commands completed exit0. Full `sys.argv` arrays are in receipts. Source/receipt hashes in compact evidence establish exact inputs; the bulk table below is stable at this numerical handoff.

| Scratch basename | Bytes | SHA-256 |
| --- | --- | --- |
| validation.json | 5092 | `1a7f1aa4c1a1b2d485d0f4e453f4ee4440d39333cf9336f0a3808557f541cc4e` |
| validation-odd.json | 3008 | `3e3ae50090083a871f5be1987a3078532355d85d692c50acfca5930608039308` |
| scaling.json | 11329 | `7d299dc81cfaa7f6bfa60e2c42300cad54fefd25719ba4b3193334bd6d45a919` |
| localization.json | 10605 | `9a46bc12b06eb61728e98dbff0ddd7f0ec3572ebd428630d1e1f4f9957237830` |
| screen.json | 334800 | `8923d6570ba6b99dca917f9ce83437c72b46806af8cb350efaf3a475da475745` |
| minimum-only.json | 2547 | `a0742d962cee5326872ae859c8d448852dfc1cfd8a242d938bc5164f663a6805` |
| fejer.json | 7534 | `849426325fb5112edea7414a2e3a5c1be23a20973fe93da89b7c0771eb92f0a2` |
| corner-trial.json | 4867 | `59cfc04ee1c50c496d4338d2c81a0e5a133c1a6383bef436124fdb2fe19c57ef` |
| carrier.json | 7741 | `5513830aa20eb5ead8b35c80f00d80cb1c360ba58b7d1426813651b047f6af02` |
| fits.json | 679 | `f5cc4b8cd749a71cb96a9c5dfb8169ca0143a691d6df5a1068e0bf1bb151bcb6` |
| scaling.log | 1806 | `774cd0b74833916cc1bdec5428da99d2f5ef38088faeefce998d92e4f47bd3ba` |
| scaling-extension.log | 1221 | `4983a1aae8b0c5ce2f71b17c9f7a096a65570cd43cbeb674c4e98a66580b5b07` |
| screen.log | 32861 | `ffdd809abfb8c64d314f09c8ee111f7007c980782f1cd13f71beb5f7cc1a4fb8` |

Bulk eigenvectors, logs and outputs remain local `/tmp/g1-frontier/`; Padua cold-storage delivery is pending. Short evidence files stay below16KiB. Earlier simultaneous RSS snapshot: scaling146MB + screen59MB + nativecertifier542MB ≈747MB; later nativecertifier RSS≈4.4GB while this worker’s minimum1600 peaked≈704MB. These are actual snapshots/per-process peaks, not a joint high-water bound. Native work belongs to another worker.

## Remaining verification obligations

- Independent finite numerical validation/reruns of this new code belong to the supplementary checker; do not count source inspection as rerun.
- The explicitm1600 negative candidate remains uncertified unless a separate exact/outward certificate and independent rerun are added.
- G2 heldout fits and original G4m240..300 were deliberately left unexecuted; no laws or missing finite coverage are inferred.
- Cold-storage delivery/retrievability remains pending. Mathematical analytic claims and native certificates are recorded separately by their owners.
