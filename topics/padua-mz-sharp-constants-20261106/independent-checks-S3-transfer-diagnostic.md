# Preregistered bounded S3 normalization diagnostic

Date: 2026-11-06. Separate Codex mathematical checker; requested
gpt-6-astra high, runtime model metadata not independently exposed.
Rules/source: `2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.

## Prospective specification — before diagnostic execution

The complete registered Padua fit was independently replayed first.
It operationally rejects the finite-K128 negative proxy: final-window
discrepancies are31.013928% and30.768461%, with both parity windows
passing the registered stability checks. This rejection is retained.
The coordinator authorized the following bounded review diagnostic of
existing normalization and transfer claims. It is not model revision,
a new fit, a new constant prediction, or an additional full-space solve.

- Fix K=16 and the single active corner(1,1), with the26 retained local
  pairs(r,s) satisfying(1+r)(1+s)<=16 and r+s even.
- Use exactly m=40,200,800,3000, with n=m-1 and the actual x/y mesh
  denominators m,m+1. Construct normalized Legendre values by the
  three-term recurrence. Accumulate the exact continuous finite-kernel
  formula in floating arithmetic as a sum of x-degree outer products
  times cumulative y-degree outer products, with total degree<=m-1
  and normalization m^(-4). Cost O(m*26^2), not a full Gram matrix.
- Compute the signed finite-corner form using its actual
  gamma_m=-2m^3/[(m+1)floor(m/2)^2] times endpoint factors and the
  two exact cosines. Only26-by-26 symmetric eigensystems are allowed.
- Compare with B_16 using the same previously specified192-point
  triangle Gauss rule and the displayed Bessel feature formula.
  Record Gram differences, coefficient differences, and extrema.
  These quadrature quantities are MEASURED, not rigorous enclosures.
- At m=800 and3000, construct the lowest finite-corner eigenpolynomial
  as a kernel combination, form its total-degree coefficient triangle,
  and normalize by its continuous product-Legendre coefficient norm.
  Evaluate once on the actual Padua tensor grid using precisely the
  unchanged PaduaOperator Legendre table formula and frozen signed
  DCT weights. Since a coefficient matrix is already available, omit
  the operator's unused vector-index enumeration and Krylov objects.
  This avoids extra full-space allocation; no full-space eigensolver
  or minimum-degree process is launched.
- Record actual Q/log(m), full L_m Rayleigh quotient, retained-corner
  L_m Rayleigh quotient, and Q-log(floor(m/2))*L_m. Cross-check the
  retained quotient from grid values against the finite-Gram minimum.
  Report the three differences separately; do not fit their degree
  dependence or infer an asymptotic explanation from these samples.
- Initial budget120 CPU seconds, one BLAS thread. No raw arrays are
  saved. Retain only one degree's polynomial/grid arrays at a time;
  temporary memory beyond the ordinary coefficient, grid, weight and
  Legendre evaluation arrays is limited to512MiB. An explicit CPU
  limit and conservative process RSS check are included. If limits
  prevent completion, preserve failed status and return the blocker.

The script, actual command, source hashes, timings, environment,
finite diagnostics and any failed guard will be recorded in
`evidence/check-S3-transfer-diagnostic.json`, below16KiB. No claim in
the fixed-operator theorem is changed by running this diagnostic.

## Outcome

The prospective section above was saved before the first diagnostic
calculation. The prescribed run completed successfully without a budget
extension:3.21439017 CPU seconds,3.231737176 wall seconds, peak619964KiB.
At m=3000 the ordinary polynomial arrays total360216032 bytes and the
peak above those arrays is274627104 bytes, below512MiB. No raw arrays
or vectors were saved, and no full-space eigensolver was invoked.

Executed from `/workspace/sharp-work`:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/check_S3_transfer_diagnostic.py --output topics/padua-mz-sharp-constants-20261106/evidence/check-S3-transfer-diagnostic.json
```

Script SHA-256:
`9bd601e312b70d7ba66d8e4041940391a7757c4733badede152b2853babbfb5e`.
Frozen operator SHA-256:
`f246b7a436fa9e6133153a87fd5af887d80f6fb0ab12dc2208fbd9ade223c241`.
Underlying signed-rule code SHA-256:
`623acdf06e4ad1c50c3c0562f47f037b8efa15fcc332c2f1ee7a7d0f88ee8b76`.
Environment: Python3.12.14, NumPy2.3.5, SciPy1.17.0; deterministic,
no seed; all three specified thread limits equal one. Started at
2026-11-06T13:00:21.656950+00:00 and ended at
2026-11-06T13:00:24.888667+00:00.

## Observed normalization and transfer quantities

The independently assembled B_16 quadrature minimum is
-0.1333153989725775. Its maximum is0.04567831707822768. All26 Gram
eigenvalues are positive; no numerical nullspace clipping occurs.

| m | Finite corner minimum | Difference from B_16 minimum | Gram operator difference |
|---|---:|---:|---:|
| 40 | -0.13703478086106638 | -0.0037193818884888874 | 0.002529897704369305 |
| 200 | -0.1339981144938375 | -0.0006827155212600078 | 0.000492841527613005 |
| 800 | -0.133483059843248 | -0.00016766087067049407 | 0.00012260943161302422 |
| 3000 | -0.1333599098702702 | -0.00004451089769269556 | 0.00003265685852276577 |

The total-degree origin diagonal agrees with its closed finite sum in
all four computations. Finite signed26-by-26 eigensystem residuals
are below3.34e-16. The continuous norms of the constructed eigenpolynomial
coefficients are within2.7e-15 of one before normalization. After
normalization, evaluating the retained corner form directly on the
actual grid agrees with its Gram eigenvalue within1.95e-14 at m=800
and2.12e-13 at m=3000.

For the two normalized finite-corner eigenpolynomials:

| Quantity | m=800 | m=3000 |
|---|---:|---:|
| Retained corner L_m from grid | -0.13348305984322853 | -0.13335990987005866 |
| Full L_m | -0.1337259074125902 | -0.13360253719029075 |
| Full minus retained L_m | -0.0002428475693616594 | -0.0002426273202320861 |
| Actual Q | 0.38727018118124446 | 0.21004668642169605 |
| Actual Q/log(m) | 0.05793458123802684 | 0.026234954197005687 |
| Q-log(floor(m/2))*L_m | 1.1884842144736232 | 1.1871114851687206 |
| Q/log(m)-L_m | 0.19166048865061702 | 0.15983749138729644 |

This separates the effects on the prescribed trial vectors: the finite
corner kernels and signed spectra approach the B_16 values across the
four samples; replacing the retained corner form by full L_m changes
these two trial quotients by about0.000243; replacing log(R)*L_m by
actual Q instead gives an additive correction about1.187. Thus the
full-form correction is numerically substantial at the tested degrees
on these particular vectors. The direct coefficient/grid agreement
does not reveal a normalization or missing-factor discrepancy in the
tested finite-kernel and retained-form constructions.

## Limits and disposition

All quantities here are MEASURED floating diagnostics. The rigorous
B_16 tail bound remains120/16=7.5 and supplies no decimal certificate.
The trial vectors are finite-corner minimizers, not full-Q minimizers;
their actual Q values are positive at both tested degrees. No inference
about the complete minimum branch, its asymptotic regime, or the cause
of the operational K4 rejection follows merely from these samples.
The registered rejection is preserved. No fit, new constant prediction,
model repair, or proof modification was introduced.

**Disposition:** no concrete normalization error found within this
bounded diagnostic; report the substantial measured full-form correction
on the stated vectors without promoting it to a general explanation.
Receipt: [check-S3-transfer-diagnostic.json](evidence/check-S3-transfer-diagnostic.json).
