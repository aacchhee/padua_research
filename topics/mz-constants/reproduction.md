# Bounded reproduction record

Rules read: `d36722823441dc40c6e19d69a174459348dd309c`. Developer role: Codex, gpt-6.1-sol, medium (explicit orchestration assignment); no Git operations. This is a numerical reproduction of assigned input, not a new mechanism or novelty claim; the novelty gate does not apply to this bounded scope.

## Completed run

From repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output tracks/mz-constants/evidence/reproduction.json
```

The actual shell redirected console output to ignored `local-output/mz-constants/reproduction-console.txt`. Essential output is `tracks/mz-constants/evidence/reproduction.json`; the manifest records its hash and size. The JSON includes the exact invocation, UTC start, measured elapsed time, Python/platform/NumPy/SciPy versions, thread settings, runner hash and every supplied Python source hash. Source input is the provided `padua_mz_inputs` bundle, identified by its SHA256SUMS manifest; `.out` files were not read as numerical evidence.

Before execution, source code was inspected. The runner executes only imports and function definitions extracted by Python AST from supplied files with inherited heavy top-level loops; it does not import `cc_asym.py`. The original `hankel_check.py` is run unchanged and safely extracts only the prefix of that file. The original `cc_mz_large.py` is also run unchanged with explicit bounded N arguments. Other suites use the extracted supplied functions, with an independently assembled direct Legendre/CC interpolation comparison and a corrected marginal normalization.

The first attempted run completed early suites but failed JSON serialization at the Padua negative-weight `numpy.int64`. Conversion to native scalar was added, and the entire run was executed again, overwriting incomplete evidence. That is a developer rerun after a mechanical fix, not independent verification. After pinning the full rules SHA, the entire suite was executed once more to bind the output to the final runner hash. The final full run exited 0. No failed numerical case was removed.

## Exact finite scope

- Hankel identity: original N=60, n=59.
- CC generalized eigenvalues and original CLI: N=40,80,160,320,640,1280, n=N-1; both parity blocks; supplied U_(N-1) Rayleigh quotient.
- Direct Legendre Gram versus generalized Chebyshev eigenproblem: N=3,4,5,9,10,21,40,81; distinct n=floor(N/2),N-1,N. The direct implementation uses NumPy Legendre Vandermonde values and a separate Chebyshev interpolation moment solve for weights.
- Fixed ratios: n=floor(rN), r=.6,.75,.9,.95; N=40,80,160,320,640. N1280 was used only for the n=N-1 suite.
- Padua interpolatory Lebesgue weights and product-Legendre Gram: m=10,20,30,40, n=m-1.
- True x marginal: m=10,20,31; compare wx with 2*wcc because the y integral is 2. The supplied script's first printed difference wx-wcc uses the wrong normalization; its second comparison wx-2*wcc is the appropriate one.
- Schur entries, weighted row sum and weight floor: N=40,80,160,320,640. This supplied function covers degree n=N, unlike the n=N-1 suite.
- Node HSS empirical offdiagonal ranks: N=256,512; thresholds 1e-12 and 1e-8 relative to full matrix spectral norm; recursive bisection stops below 64 entries or after depth 4. JSON retains every visited rank, not only the printed prefix used by the original script.

## Observed results and interpretation

All results are **MEASURED** float64 observations. The durable measured claim is `PD-T?mz-constants-codex-41` in `tracks/mz-constants/theory/reproduced-spectra.md`. Hankel maximum residuals were 1.1666254117360861e-14 and 6.772360450213455e-15; the source's finite zero-support Boolean was true. Maximum extremal eigenvalue disagreement in the direct comparison was 1.3433698597964394e-13. These are consistency checks, not interval bounds or exact-arithmetic proofs.

The original CC source emits a divide-by-zero RuntimeWarning because NumPy evaluates the unused even-moment expression at odd index 1 inside `np.where`; the selected odd moment is 0. Its retained output and the independent direct comparison show finite computed answers. The warning is retained in JSON.

The measured n=N-1 lower eigenvalue decreases from .2598490248754948 at N40 to .11763515599221253 at N1280. In this range the upper eigenvalue stays near 1.00444. Padua m10..40 has two negative weights in each tested case. This does not justify treating its weights as a positive discrete measure; the reported Gram eigenvalues are for the signed interpolatory rule. The true marginal maximum error is below 8.73e-16 in all three tested m values.

The nodal n=N Schur calculation gives upper eigenvalues near 2, so its upper spectrum must not be conflated with the n=N-1 CC results. Its reported entry constants, weight-floor ratios, Schur/log² ratios and HSS ranks are finite diagnostics only; they prove no uniform entry bound, logarithmic estimate or rank law.

## Evidence, storage and independent checks

Small necessary evidence is eligible for commitment within the repository's <1MB/file and <5MB aggregate limits; the manifest reports sizes. Bulk console output remains in ignored local-output and is unnecessary for reproduction because the JSON contains results and original subprocess stdout/stderr. Requested Windows cold-storage archival cannot be performed from this Linux workspace; archival remains pending with AC's destination/retrieval arrangement.

No independent agent rerun is claimed by this document. Consequential numerical checks must be separately executed by the assigned Astra auditor against the recorded hashes. Re-running the command above into a new file is the exact proposed audit reproduction; no inherited large defaults are required.

## Runs needed

The imported N=20480 narrative/output remains unverified. No run beyond N1280 for near-critical CC, N640 for ratios/Schur, m40 Padua, or N512 HSS was attempted. No such extension is needed for the finite claim here. General asymptotic conclusions and exact-arithmetic certification are outside this reproduction.
