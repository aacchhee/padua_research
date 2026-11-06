# P2 prospective protocol — finite-m two-mode mechanism

2026-11-06; saved after R publication `17ca9f441cece178354e70504a6c739df501a224`,
before any P2 code execution, calibration, validation or new prediction
calculation. Root publishes this protocol before Step 1. Main test requires
a separate published measured b2/K-stability registration and root release.

## Definitions and fixed numerical method

Use exactly S3-02 L_m and full signed Lebesgue Padua Q_m on the continuously
orthonormal total-degree Legendre basis for Pi_(m-1), unnormalized dxdy mass4.
R=floor(m/2). Reimplement the reviewed audit lm_spectra2 tensor contraction
using the frozen signed weights g1_spectral.weights_dct. Audit files remain
untouched; every code/input SHA256, package version, seed, thread setting,
CPU/wall time and command enters new small receipts. Repository paths are
resolved relative to __file__; no machine-specific source path allowed.

Main eigsh: Q smallest algebraic pair and L lowest six eigenpairs,
seed1, tolerance1e-9, ncv40, maxiter3000. No upper Q solve or Ep solve.
No seed/precision/window tuning or retry chosen from observed outcomes.
Record residual norms, orthogonality, doublet widths and inter-doublet gaps.
For each normalized Q minimum vector q, let U_i be the two columns with
zero-based indices (0,1),(2,3),(4,5) of the ordered L eigenvectors.
Mode i weight=||U_i^T q||²; Q(mode i)=lambda_min(U_i^T Q U_i).
The second-mode L comparison uses distance of q^T L q to the interval
[nu_L[2],nu_L[3]], not an arbitrary eigenvector within a near-degenerate pair.
Compression spectra are invariant under orthogonal doublet-basis changes.

## Step 1 — bounded calibration and validation, before main release

B_K uses exactly S3-03 product truncation, j+k even, coefficients
-16 e_j e_k(-1)^j and H=L²(D,ab da db), triangle mapping b=(1-a)s.
Gauss order128 at K16,32,64,128; order160 repeats K128. Remove Gram
nullspace at relative1e-13 as reviewed audit/S3 model code, reporting
rank and discarded scale. Record lowest four eigenvalues, especially b2
(the second eigenvalue of one-corner B_K, not duplicated finite-L index2).
Calibration accepted only if |b2_128-b2_64|<=0.002,
|b2_128+0.0955|<=0.002, and order128/160 K128 difference<=1e-5.
Use the order128,K128 b2 without rounding as the fixed comparison proxy;
no adaptive K/quadrature extension. These checks give measured stability,
not a certified B value; tail120/K is too large for decimal certification.

Small validation m12,13: explicitly assembled dense nodal Gram using the
separately implemented frozen Chebyshev weights versus new DCT/tensor Q,
and independently assembled dense nodal L; random-vector relative errors
and symmetry error<=1e-10, weight max difference<=1e-10, Q/L minimum and
lowest-six eigenvalue differences<=1e-8. Dense doublet projector weight,
compressed Q spectra and L(q) must agree with matrix-free values<=1e-8.

Audit-overlap m400: compare Q_min, L_low6, L_at_Qmin within1e-7 of existing
big.json, and mode2 summed weight within1e-6. This checks implementation,
not a fresh prospective confirmation, because audit values were read.
Expected calibration<1min, smallvalidation<1sec, overlap<1min; timing
forecasts are rough and impose no scientific acceptance criterion.
Any failed validation/calibration stops main release as INCONCLUSIVE.

## Main forecasts and fixed tests

Main cases exactly m1600,1601,3000,3001. Positive second-mode prediction
applies to these four cases, including the odd partner3001 explicitly.

1. At every main m, mode2 projector weight>0.9 and distance of L(qmin)
   to second-doublet eigenvalue interval<=0.005.
2. Define D(m)=Q(mode1)-Q(mode2). For parity pairs (1600,3000) and
   (1601,3001), decrease rate=-(D(mhi)-D(mlo))/(logRhi-logRlo).
   Target band0.038±0.006 per unit logR. Deviation>50% from0.038
   is a scoped kill; outside target but within the50% band is INCONCLUSIVE.
3. For the same parity pairs, Qmin secant slope uses physical log m:
   (Qmin(mhi)-Qmin(mlo))/(log(mhi)-log(mlo)). Each must be within0.006
   of separately registered measured b2. Existing K4 regression windows
   are already observed and contextual only; they are not fresh tests.

A failure of item1 or item3 is a measured departure at this scope. Record
scoped kill only on numerically valid rows. No universal theorem, actual
crossing degree, two-term asymptotic or limit value follows from passing.
No K4 criterion, window, threshold, receipt or outcome changes.

## Numerical validity and cost guards

Absolute Q/L eigenpair residuals<=1e-7; L-vector orthogonality error<=1e-8.
Each L doublet width<0.001; neighbor gaps>0.01. Failed/ambiguous pairing,
ARPACK failure, wall/cost cap or missing rows=>INCONCLUSIVE; no branch label.
Each run uses one BLAS/OpenMP thread, at most two heavy processes across
all directions, 6h/run and48CPU-h total campaign ceilings. Main forecast
1–3CPU-h total; up to6rounds allowed but stop after2no-progress rounds.
No upper-pilot retry, Syvert or new upper Padua campaign. Save compact
per-case JSON receipts under16KiB. Computed values are MEASURED only.

## Sequence and reproducibility

Root publication of this protocol -> new code -> Step1 -> root publication
of measured b2/K stability -> main release -> four cases -> fixed summary.
Code/input/evidence identities are pinned; prose is not hash-pinned by a
checker. Scripts will expose model, validation, overlap, main and summary
commands so a checker can independently execute them from the repository.
