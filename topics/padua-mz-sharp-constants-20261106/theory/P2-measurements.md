# PD-T?mz-sharp-codex-P2-01 — finite-m two-mode measurements

ID kind: PD-T.
Aliases: second-mode projector; compressed signed branch difference;
B_K second-mode calibration.
Split from: supporting measured test for PD-T381, not a new target conjunct.
Split into: none.

## Statement

In the prospectively fixed floating computation described in
[protocol](../ideas/P2-protocol.md), the one-corner B_K second-eigenvalue
proxy at K128, triangle Gauss order128, is b2=-0.0955298083997758.
Its K64→128 change is7.78663282741121e-8, and repeating K128 at order160
changes it by3.0531133177191805e-16. The prescribed calibration tests pass.
The independently assembled small dense versus tensor-form comparisons
at m12/13 and existing audit m400 overlap pass their registered guards.
No main-case observation is asserted before it is executed.

## Definitions

Q_m is the complete signed Lebesgue Padua rule of mass4 on Pi_(m-1),
represented in the continuously orthonormal product-Legendre basis.
L_m is exactly the S3-02 finite form, R=floor(m/2). Mode2 means the
second ordered L doublet, columns2/3 with zero-based indexing. Its weight
is the squared norm of the orthogonal doublet projection. A branch value
means the smaller eigenvalue of Q compressed to one L doublet.
B_K is precisely S3-03, single corner, H=L²(D,ab da db); its second
ordered eigenvalue is b2. The two finite active corners duplicate modes.

## Assumptions and status

Overall status: **MEASURED**. Binary64 NumPy/SciPy calculations only;
quadrature, residuals and solver tolerances are not rigorous enclosures.
Scope currently calibration K16/32/64/128, orders128/160, validation12/13
and audit overlap400. Main1600/1601/3000/3001 remain runs needed.
Candidate disposition: supplied continuation/test; no negative result yet.

## Depends on

S3-02 exact definitions and S3-03 B_K definition; frozen definitions,
g1_spectral signed DCT weights and mz2d_spectra independent Chebyshev
weight construction. Audit-01 A2/P2 supplies the hypothesis and existing
m400 receipt. No measured proxy is a premise of the exact S3 theorem.

## Evidence and checks

Producer [P2_modes.py](../code/P2_modes.py), code SHA256
8e15fe58b19a1ef1a2ff71da80d18de04349d90081e02a885bcbb38b143d1161.
Protocol published d03e74dcf94020ba26d9fae84d3ff6c5519db901 before
all P2 calculations; its receipt hash is recorded in every output.
All code/input identities, commands, numerical packages and thread settings
are in [calibration](../evidence/P2-b2-calibration.json),
[validation](../evidence/P2-validation.json), and
[overlap](../evidence/P2-overlap400.json). Run commands from repository root:

    env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/P2_modes.py model --output /tmp/P2-model-replay.json
    env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/P2_modes.py validate --output /tmp/P2-validation-replay.json
    env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 timeout 21600 python topics/padua-mz-sharp-constants-20261106/code/P2_modes.py overlap --output /tmp/P2-overlap-replay.json

The small comparison uses separately implemented frozen Chebyshev
weights and explicit nodal Gram matrices; L is assembled by literal
scalar node loops independently of tensor contraction. m400 is an
implementation replay of already-read audit data, not a fresh hypothesis
test. An independent agent rerun is not yet performed by this developer.

## Scope and limitations

B_K calibration demonstrates only measured stability of the selected
low eigenvalue, not full Gram/operator accuracy: K128 Gram minima differ
materially between orders128/160. The analytic tail120/128=0.9375 cannot
certify decimal accuracy. Finite doublet identification and Q secants,
when measured, prove no two-term asymptotic or crossing degree. No result
changes K4's original criterion, window, threshold, receipt or outcome,
or PD-T381's registry status. No upper Q eigensolve is performed.

## Open items

Publish measured b2/K stability before main release; execute four frozen
main rows, evaluate the fixed criteria, and obtain independent rerun.
The optional two-term O(1) corner theorem is unattempted, not rejected.

## History

2026-11-06, Codex allocated gpt-6.1-sol medium; runtime metadata not
independently exposed. Rules0205690b9c4e959a28e949083e9a1808735abf4b;
R response17ca9f4. Step1 only after prospective protocol publication.
Source-preflight failure and verified-copy repair are preserved once in
[attempt](../attempts/P2.md); no scientific input/protocol tuning followed.
