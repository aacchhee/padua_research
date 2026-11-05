# G1 hybrid native exact certifier — development record

Rules/input: `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`; frozen main/base `440d1079e42c3ef21c40d1cf8870f5b206410c6a`. Developer: Codex certifier worker, assigned gpt-6.1-sol medium; resolved runtime metadata is not independently exposed. No Git operations by this worker. G0 execution was performed separately; root released this worker after its PASS on 2026-11-05. No mathematical run preceded that release.

This is an **implementation-only port of PD-T106/107**, with no new mechanism or novelty claim. The novelty gate does not apply to generating ideas because none is proposed. The predecessor is the exact rational pencil and integer signed-dominance congruence mechanism in `tracks/mz-constants/code/mz2d_exact.py` and PD-T107. This record is verification/development evidence. Separate independent checker execution is now complete at m10/20/30/40/60; m80 and the contiguous integer batch remain distinct obligations. Finite checks give no all-m statement.

## Implementation and unchanged reduction

`code/cert_pencil.c` builds the frozen total-degree product-Chebyshev pencil with GMP rational arithmetic. The basis order, four product-to-sum terms **including multiplicities**, fold thresholds and parity split are unchanged. It checks every upper-triangular off-block entry of both matrices is exactly zero. Symmetric lower entries are copied from their equal upper entries. Unlike approximate matrix assembly, this stage never uses floating point to decide an exact value.

Every `h(k)` is initialized with a positive denominator and explicitly passed through `mpq_canonicalize`. All subsequent GMP rational operations have canonical inputs and produce canonical outputs. In particular h(0)=2, odd h=0, and even nonzero h=-2/(k²-1); numerator signs are never hidden in denominators. Each block uses the **positive** LCM D of all denominators in H and Q, and checks divisibility before `mpz_divexact` to produce H0=DH and Q0=DQ. This scale need not be the minimal endpoint denominator used in the frozen producer; it is an exact positive common multiple, which leaves inertia unchanged.

The Python driver calls SciPy only to propose rational bracket endpoints and integer R obtained by scaling and rounding eigenvectors at 10¹². Native FLINT `fmpz_mat` multiplication computes BH=RᵀH0R and BQ=RᵀQ0R. For t=tn/td in canonical form, td>0, the acceptance matrix is

`B = td*BQ - tn*BH = Rᵀ[D*td*(Q-tH)]R`.

Distributing the congruence saves repeated integer products but changes neither the matrix nor the frozen acceptance theorem. The driver checks exact symmetry and every integer margin `abs(Bii)-sum(j!=i)abs(Bij)>0`, then counts signs. As in PD-T107, strict signed dominance proves nonsingularity and diagonal-sign inertia by continuously turning off off-diagonal entries. Nonsingularity of B implies R invertible; Sylvester congruence and positive scaling transfer the count to Q-tH. Since H is the positive continuous mass matrix, negative inertia counts eigenvalues below t. Minimum endpoint counts (0,1), maximum counts (N-1,N) give strict open extremal brackets. Acceptance uses explicit exceptions, so Python `-O` cannot disable checks.

This is a **hybrid native port**, not a standalone C acceptance executable: C/GMP constructs the pencil, FLINT's compiled integer kernels perform congruences, and Python controls/checks integer rows. FLINT development headers were absent. System GMP and the wheel's private GMP exchange only serialized integers, never ABI objects.

## Executed validation and costs

Full-entry exact comparisons with the frozen Python Fraction pencil passed at m=2,3,10,11,20,30,40: 940,942 within-block entries across both matrices. The frozen code also checks off-block zeros. This includes both even-x and odd-y parity conventions. Receipt: `evidence/cert-exact-entry-regression.json`. This is developer regression, not independent verification.

| m | Dimension | Wall seconds | Peak Python RSS KiB | Strict minimum interval | Strict maximum interval |
|---|---:|---:|---:|---|---|
| 10 | 55 | 0.0157 | 60,476 | (0.356191,0.356192) | (1.634856,1.634857) |
| 20 | 210 | 0.2765 | 64,060 | (0.272233,0.272234) | (1.723313,1.723314) |
| 30 | 465 | 1.2486 | 95,208 | (0.236705,0.236706) | (1.757929,1.757930) |
| 40 | 820 | 6.6237 | 185,616 | (0.214817,0.214818) | (1.778088,1.778089) |
| 60 | 1,830 | 46.9120 | 747,052 | (0.188593,0.188594) | (1.802011,1.802012) |
| 80 | 3,240 | 302.4373 | 2,663,896 | (0.172730,0.172731) | (1.816497,1.816498) |

All four PD-T107 intervals match exactly. **G1 m60 cost gate passes:** 46.912 seconds wall, below 2 hours. Peak Python RSS is a process high-water mark including earlier targets in that invocation; native-child peak RSS was not separately measured. All runs are sandbox-only, one BLAS/OMP thread, with other campaign workers sharing the sandbox.

Per-target receipts `evidence/cert-m{10,20,30,40,60}.json` preserve all endpoint counts, positive scales, minimum strict margins, transform hashes, source/binary/input hashes, command, compiler and environment versions, and component timings. Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, python-flint 0.9.0, FLINT 3.6.0, native GMP 6.3.0; compiler details are in each receipt. Exact versions in receipts are authoritative.

The identity case m=2 was checked separately: H=Q exactly, dimension 3, hence both extrema equal 1. Receipt `evidence/cert-m2-identity.json`. A default micro-grid attempt at m=2 correctly rejected because an endpoint coincided with its triple eigenvalue 1. At m=3 the rational extrema 15/32 and 5/4 similarly require a noncoincident grid; the batch uses width 1/999999 there. This is an endpoint-proposal issue, not a failed inertia theorem or spectral counterexample.

Four malformed synthetic acceptance matrices reject: zero, non-strict dominance boundary, nonsymmetry, and a nondominant indefinite matrix. A mixed-sign strictly dominant matrix accepts with the correct one-negative/one-positive inertia. A separately executed real m10 run with `--scale 1` rejects with `ValueError: strict diagonal dominance rejected`, exit 1, before emitting an accepted receipt. Thus poor floating transform proposals fail closed. Two initial engineering attempts failed before any mathematics (stdio/GMP include order; repository-root path), were corrected, and are not scientific runs.

## Reproduction, storage and pending work

From the repository root, with python-flint 0.9.0 installed in a scratch target:

```sh
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/cert_native.py --m 10 20 30 40 60 --scratch /tmp/padua-cert-native --output-dir /tmp/padua-cert-replay-receipts
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/cert_validate.py --scratch /tmp/padua-cert-native --output /tmp/padua-cert-regression.json
```

Bulk exact pencils, float proposals and integer transforms are in `/tmp/padua-cert-native`; their byte sizes and SHA-256 identities are in each receipt. They are regenerable outputs, not committed artifacts. AC cold-storage delivery is PENDING; a scratch path is not an archival retrieval claim.

The contiguous m3..30 batch completed; `evidence/cert-range-3-30.json` is 11,456 bytes. Together with the m2 identity record this covers every integer2..30 as exact development execution. Raw per-m receipts stay in `/tmp/padua-cert-batch/receipts`; new bulk matrices are deleted after their hashes are recorded, and remain regenerable. Previously retained frozen-case bulk stays in `/tmp/padua-cert-native`. The batch uses one command per new target and reuses the explicitly identified earlier executions at m10,20,30.

Separate worker `/root/replay` independently reconstructed and checked m60, comparing all3,349,800 within-block H/Q entries as exact rationals and837,000 off-block pairs, then using fresh integer transforms at10¹³ and its own exact acceptance implementation. All four endpoint counts passed in232.594s. Its source/receipt identities and command are recorded in `independent-checks-cert.md`; producer and checker share FLINT and the mathematical signed-dominance predicate, an explicit trust limitation. The developer inspected the actual receipt after the independent worker reported completion. The m60 finite result is **PROVED (computer-assisted development)** in `theory/cert-finite-extension.md`, with Claude audit pending. The m80 candidate is separated as **CONDITIONAL** in `theory/cert-finite-extension-m80.md` while its independent run proceeds.

Runs in progress at this checkpoint: m100 native extension and contiguous31..60 batch. The observed five-minute m80 wall cost supports trying m100 in the sandbox; no execution beyond100 is planned here. Runs needed: complete these bounded executions; complete the independent m80 checker/rerun; independently confirm any contiguous-range finite claim. Native exact output does not bypass that requirement. The m60 status does not silently certify other integer sizes.
