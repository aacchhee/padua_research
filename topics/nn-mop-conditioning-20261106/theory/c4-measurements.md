# C4 — external/native monic matrix and full-field measurements

ID kind: finite comparison/verification record; no new theorem or negative-result ID.
Aliases: IEP-MOP comparison; anchored full-NN lift.
Split from: none. Split into: none.

## Statement and status

Overall status: MEASURED. On the recorded Debian13/Octave9.4/reference-BLAS platform, execute pinned IEP_CORE, IEP_KRYL and IEP_KRYLREORTH(full,1) for both frozen families, every topicN4–32, in archive integer mode and a bitwise shared normalized-input mode. The latter compares with C3's direct C4/A-LU/A-QR/B-nodeqr outputs. All348 final external calls complete; all58 shared node/weight bit-vector identities pass; all348 high-precision functional lifts complete with140/220dps fieldwise relative disagreement at most1.698e-107. These checks are not outward error bounds, stability theorems, or positive-input inverse certificates.

## Definitions and assumptions

N is node count; source paperN=N−1. Frozen families are Krawtchouk p1=2/5,p2=1/2 and Hahn alpha1=1,alpha2=3/2,beta=1 in the source's argument names. The same exact rational family generates binary64 inputs for all shared runs. Each native algorithm's internal weight mass normalization and basis construction remain part of its algorithm. The external starting-vector construction remains unchanged source code. Input arrays cross the Octave boundary as IEEE754 hex; numerical JSON fields are ignored by the postprocessor. Source/input identities and every bit-vector hash are retained in the raw receipt.

The exact target is the frozen rational-family NN array evaluated at220dps. NN error is PD-T290's maximum over four fieldwise relative sup errors, including structural zeros in the numerators. Separate a1,a2,b1,b2 errors appear in each CSV. C3's native outputs are directly compared. For external methods, the NN output is explicitly the composite **IEP solver + actual-input d0 anchor + high-precision functional lift**. It is not a native IEP-MOP output.

Matrix error is relative spectral norm of monic upper Hessenberg H in integer-node coordinates. For normalized z, t=(N−1)(z+1)/2, use the degree-dependent monic conversion documented in c4-interface-validation.md, rather than a naive affine matrix transform. H has unit subdiagonal and beta/gamma/delta on the diagonal/two superdiagonals. Differences are formed at220dps before binary64 NumPy spectral-norm evaluation. Archive integer rows retain their distinct input-rounding history; they are not silently pooled with the bitwise shared normalized rows.

For the added lift, with normalized masses and first-e1 monic path, ell1=e0 and ell2=e0+d0e1, where d0 is mean2−mean1. Moments are ell_s H^k e0. The d0 used in a floating run is calculated with NumPy binary64 dot/sum from that run's actual input nodes/weights; no oracle NN coefficient is supplied. These moments determine formal marginal recurrence coefficients, followed by the existing layer map. Exact H+d0 moments/fullNN agree with independently solved defining moments in Fraction arithmetic for N4/6/8 both families. For rounded H, this algebraic lift may correspond to nonreal or nonpositive spectral data, and normality is only numerically supported by nonzero computed divisors. No eigenvalue positivity test or common positive-input inverse is claimed.

## Prerequisite gates and transport failure

M4 actual unchanged-driver replay passes selected Kravchuk paperN10 CORE:2.691214553706643e-10, log10ratio−0.4058177524 to the inherited quoted paper6.851191e-10. The paper-data source itself is not newly authenticated here. M2 exact-generator fidelity passes at topicN6, using full IEEE matrix bits: relative spectral discrepancy7.18485e-17 (Krawtchouk),3.90939e-17 (Hahn). Every returned H is monic according to the inspected source; scaled returned basis matrices do not define a different returned-H gauge. Source constants and matrix orientation were sent to C1.

An initial wrapper using decimal JSON did not preserve all normalized input bits. It moved some N12 nodes by one ulp. That exploratory comparison is rejected for the identical-input claim and its receipt retained. Final tables use the repaired hex transport. A separate exploratory all-solver1e-12 diagnostic failed because KRYL's numerical error exceeded that threshold; the actual M2 criterion concerns normalization agreement with the source exact generator, which passes. Both issues and the source-access history remain in attempts/C4.md.

## Selected final shared-input measurements

Each entry is NN-field E / integer-coordinate matrix error. External NN entries include the lift. Full all-integer sizes and all four separate fields are in c4-tables; large errors are retained.

| Method | Kraw N8 | Hahn N8 | Kraw N16 | Hahn N16 |
|---|---:|---:|---:|---:|
| C4 | 1.871e-09 / 1.627e-10 | 2.614e-07 / 1.399e-08 | 9.667e-02 / 5.179e-03 | 7.031e+01 / 7.740e-01 |
| A-LU | 3.096e-12 / 2.393e-13 | 4.238e-10 / 1.324e-11 | 3.782e-04 / 5.969e-05 | 5.998e-02 / 1.398e-03 |
| A-QR | 2.804e-11 / 2.556e-12 | 4.074e-10 / 1.305e-11 | 1.034e-02 / 1.290e-03 | 6.102e-02 / 1.405e-03 |
| B-nodeqr | 2.634e-11 / 2.407e-12 | 2.845e-10 / 7.350e-12 | 3.919e-04 / 5.279e-05 | 2.294e-02 / 4.977e-04 |
| CORE | 1.169e-11 / 1.206e-12 | 4.271e-10 / 1.237e-11 | 5.651e-04 / 7.143e-05 | 4.467e-02 / 1.058e-03 |
| KRYL | 6.097e-11 / 4.922e-12 | 1.184e-09 / 6.310e-11 | 1.474e-02 / 9.043e-04 | 1.344e-01 / 5.903e-03 |
| REORTH | 1.160e-11 / 1.201e-12 | 3.594e-10 / 1.042e-11 | 6.561e-04 / 7.855e-05 | 1.761e-02 / 3.999e-04 |

At N32 every tested method in both families has at least order-one matrix or NN error; no uniformly accurate large-N solver emerges. Rankings depend on family, size, metric and composite postprocessing. These finite measurements do not establish an algorithmic error bound of the form C kappa u. The lift can amplify path errors and changes the algorithm whose NN accuracy is being reported.

## Depends on

PD-T286/289/432 (normal family, layer map, step-line extraction and metrics); predecessor path_recovery.py's normalized-functional representation; exact auditor defining-moment routine for the finite lift checks; C3 native-grid raw identity. LIT-347 source and literature coverage are explicitly pinned in external-code.md. No general published stability claim is inherited as a proof.

## Checks, artifacts and reproducibility

[Final comparison receipt](../c4-comparison-receipt.json) pins raw inputs, helper code hashes, table hashes, platform and all failure statuses (none in the final finite scope). [Source](../c4-source-receipt.json), [runtime](../c4-runtime-receipt.json), [M2](../c4-m2-bits-receipt.json), [lift checks](../c4-lift-check.json), and [interface checks](../c4-interface-check.json) provide the distinct obligations. All14 CSVs are below9KiB. Large regenerable raw data remain in /tmp with hashes; no cold-storage upload is asserted. Complete commands, installation provenance and historical failure are in external-code.md and attempts/C4.md. Independent replay is performed by a distinct worker, not this developer's own validation.

## Scope and open items

The finite non-Advanpix archive-family scope, including original paperN5–30, is covered. The licensed Advanpix conditioning, backward and random-weight experiments are not reproduced; neither are MATLAB platform behavior, arbitrary input families, exact positivity of lifted data or general stable-algorithm claims. Fieldwise metrics and matrix norms cannot be exchanged without their specified conversions. A native fullNN implementation of the external algorithms, with a stability analysis of the required lift/extra boundary data, remains unresolved.

## History

2026-11-06: Codex technical development, assigned gpt-6.1-sol medium; serving metadata not independently exposed. Rules/source b4a04981d42c7cd872957facf5e3995e4096ca67. Round1–2 blocked source preparation; AC supply restored source/runtime in round3; round4 exploratory transport failed bit check; round5 corrected transport produced final measurements. No third-party source or Git mutation by this worker.
