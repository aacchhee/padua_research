# Numerical results — 2026-11-05

Rules/input `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`; developer Codex numerical subagent, delegated gpt-6.1-sol medium (resolved runtime metadata not independently exposed). All results here are **MEASURED**, not interval enclosures or all-m conclusions. G0 was independently completed and the orchestrator explicitly released numerical runs before execution. Preregistration is `numerical-plan.md`.

## Completed validation

Executed from `/workspace/padua_research`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py --validate 10 20 30 40 --output /tmp/g1-frontier/validation.json > /tmp/g1-frontier/validation.log 2>&1
```

Exit 0. DCT weights versus frozen producer: maximum absolute difference 6.94e−17; explicit dense Gram versus new operator: maximum relative vector discrepancy 3.80e−15; dense extrema versus matrix-free extrema: maximum absolute difference 1.78e−15. All validation tolerances in the preregistration passed. Continuous H=I is the algebraic orthonormal Legendre normalization, not a numerically inverted Chebyshev mass matrix. This implementation is O(m³) tensor contractions with O(m²) operator storage; DCT accelerates weight formation, not the Legendre matvec.

## Running jobs (not yet completed evidence)

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py --m 60 80 100 120 150 200 250 300 400 600 800 1000 --output /tmp/g1-frontier/scaling.json --vector-dir /tmp/g1-frontier/vectors > /tmp/g1-frontier/scaling.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py --m 100 200 400 --localize --output /tmp/g1-frontier/localization.json > /tmp/g1-frontier/localization.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py --m $(seq 2 300) --offsets 1 2 --output /tmp/g1-frontier/screen.json > /tmp/g1-frontier/screen.log 2>&1
```

Each receipt persists completed rows only. Screen coverage must be read from the receipt, not from the command's requested list. Early localization at K=10: edge-union mass fractions (min,max) are (.3205391924,.4401355965) at m100 and (.2166873672,.3577648695) at m200. Corner-square masses are below 4e−8. Refinement discrepancies below 3e−13. The prescribed 90% pass is already unavailable; the m400 kill test is pending.

Bulk output and eigenvectors remain local `/tmp/g1-frontier/`; cold-storage delivery is pending. Separate worker owns the exact/native certifier. No certified extension is claimed by this floating work.

## Completed G3: original localized R1 killed

Localization command above exited 0. Short full receipt: `evidence/g1-localization.json`. At m400, K10 upper edge-union mass=.29345156824788154 and corner mass=1.9065e−16. This is below the original 50% kill threshold. Thus **KILL for R1 localization as stated**; this is a finite measured route verdict, not a theorem ruling out other limiting operators. At m400 lower mass instead becomes strongly corner concentrated: corner=.777508668964928, edge=.8813374365015367, lambda_min=.10281890623388915. At m100/200 the minimum had negligible corner mass. This suggests a crossing of different extremal families, not an asymptotic conclusion. A sparse monotone fit across it may be misleading; keep the original preregistered fitting protocol unchanged.

Upper eigenvalue m400=1.8733622908153866, residual2.84e−11; lower residual7.41e−13. G3 total m400 time32.64s, process peak RSS95,964KiB. Composite tensor Gauss orders400/408: maximum fraction change6.48e−11; max observed total mass error over either rule1.93e−10. These are floating quadrature diagnostics. Eigenvectors are individually normalized to continuous coefficient norm one. Short validation receipt is `evidence/g1-validation.json`.
