# IDEA?mz-sharp-codex-S3-03 — compact signed Bessel corner operator

Prospective registration,2026-11-06; no Bessel-model eigenvalues or final
S4 slope fits have been computed/read by S3. Complete preceding gate:
../novelty-gate-S3.md, including its prospective kernel refinement.

## Exact predeclared model and parity prediction

Let D={(a,b):a,b>=0,a+b<=1}, H=L2(D,ab da db), and

    J0(z)=sum_(r>=0) (-1)^r (z^2/4)^r/(r!)^2,
    psi_jk(a,b)=J0(pi j a)J0(pi k b),
    e_0=1/2, e_j=1 for j>=1.

For K>=1 define the finite-rank selfadjoint operator

    B_K=-16 sum_((1+j)(1+k)<=K, j+k even)
               e_j e_k (-1)^j |psi_jk><psi_jk|,

where |psi><psi|f=psi integral_D f psi ab da db. The predicted B is the
operator-norm limit of these B_K. Predicted signed logarithmic slopes:

    c_minus=inf spectrum(B),    c_plus=sup spectrum(B),
    lambda_minus(m,m-1)/log m -> c_minus<0,
    lambda_plus(m,m-1)/log m -> c_plus>0.

These exact constants and the **same values on even and odd m** are the
predeclared prediction. Even m has two active corners (1,1),(-1,1);
odd m has two active corners (1,1),(1,-1). Each active corner predicts
the identical B block. The other two corners predict a zero leading
block. Thus the full corner model is B direct-sum B, with zero allowed
in the remaining spectrum. This is an exact operator-value prediction;
no decimal slope is guessed before constructing that operator.

## Why this is falsifiable and what remains unproved at registration

The uniform finite-family L_m in S3-02 has tail norm at most120/K when
the retained nodes with endpoint-distance product>(K) are omitted. Its
fixed-corner scaled continuous reproducing kernel should converge to

    kappa((u,v),(u',v'))
       =integral_D ab J0(au)J0(au')J0(bv)J0(bv') da db.

At a shared corner kappa((0,0),(0,0))=1/24, fixing normalization.
Opposite-corner cross kernels should vanish by alternating sums.
Together these steps would control the full signed spectrum, with an
explicit tail error rather than fixed-index weights alone. A missing
tail bound, wrong sign/factor, nonzero cross-corner limit, or failure of
kernel convergence kills this formulation until repaired.

At registration the compact-operator construction and full spectral
transfer are **OPEN** and conjectural; the full-form reduction S3-02 is proved
separately. Kernel-hard development is allocated by the coordinator to
a separate worker; it is a dependency, not an independent audit. This
record is preserved when the proof status is resolved in a theory file.

## Candidate disposition and numerical protocol

Retained implementation of the supplied corner-operator direction. No
historical novelty or priority claim. PD-T381 stays OPEN pending full
proof and independent review. The first numerical construction will
diagonalize finite B_K via its continuous Gram matrix, using a triangle
Gauss quadrature of increasing order; compare truncations before quoting
decimals. Such values remain MEASURED unless rigorous enclosures are
supplied. Parent publishes this exact prediction before final S4 fits.

Developer Codex S3, allocated gpt-6.1-sol xhigh; runtime metadata
unexposed. Input/rules2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861.

## Dated model computation and heuristic decimal registration

Filesystem UTC chronology: original exact registration saved
2026-11-06T11:52:15.469405Z, SHA256
c2e8b10ac01c04c514b16b1c239682d16342aef7a55590c99afc22e5611c5263.
Numerical code saved11:53:01.642425Z; receipt completed11:53:03.027191Z.
First-run start UTC was not explicitly instrumented; these latter times
bound its execution. Thus the saved exact model preceded its numerical
construction. Coordinator published the original prediction in commit
59d02c7e7dca3faa4a4687db331a784366595a26 before final S4 fits.

Code SHA256 dc4c5f0c4d935d065ea3409d234c2727890a3ddcb10cdaf59c397127bda03b20.
Actual command, from /workspace/sharp-work:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/S3_corner_model.py --orders 128 192 --cuts 16 32 64 128 --output topics/padua-mz-sharp-constants-20261106/evidence/S3-corner-model.json
```

The receipt records Python, NumPy/SciPy versions, code hash and original
preregistration hash.

Triangle Gauss orders128 and192 gave at K=128 approximately
c_minus(K)=-0.133580002120 and c_plus(K)=0.0455983195703; at K=64,
-0.133563291962 and0.0456050998011. The rigorous truncation bound120/128
is0.9375, and floating quadrature is not enclosed. Therefore these
decimals have no proved accuracy for B. For future K4 comparison only,
the heuristic pre-fit decimal prediction is **-0.1336 and+0.0456, equal
on even and odd m**. Exact spectral values of the declared B remain the
authoritative mathematical prediction. No final S4 fit has been read.

This dated addition preserves the original exact prediction. Minor
editorial corrections use the provisional IDEA identifier and standard
OPEN status; they change neither the model nor the parity prediction.

## Round 3 development disposition

The complete integration is now proved in analytic development in
../theory/S3-corner-operator-limit.md, subject to independent check. The
earlier OPEN registration is historical and preserved. That theorem
constructs B in norm, identifies the entire signed extremal limits and
both parity blocks, and provides a quantitative finite approximation.
The heuristic decimals above remain MEASURED; no decimal enclosure or
closed elementary expression is claimed. Required audit is separate.


## 2026-11-06 audit-01 A2 interpretation

Equations (3) and (4) of S3-03 predict limits, and make no prediction about
finite-window slopes. K4 compared those limits with finite-window slopes;
its KILL_HEURISTIC_PROXY outcome remains unchanged and is not a PD-N.
The audit diagnostic audit-01-support/S3/big.json (MEASURED floating point,
m=400,800,801 with mid.json) places roughly 94–96% of the Q-minimiser on
L_m's second mode, while the bottom L_m mode is already near −0.1336.
Mode-dependent O(1) corrections explain the observed slopes near −0.092
without contradicting the limit theorem. This is finite-scope audit evidence,
not a proved branch law or certified crossover prediction.


## 2026-11-06 template completion (audit A10)

Aliases: S3-corner-operator; IDEA-470 continuation.
- Question / scope: the exact candidate and parameter scope preserved above; see linked theory, without expanding its quantifiers.
- Mechanism and hypotheses: the signed mechanism stated above under the exact Lebesgue normalization; no sign-erased surrogate.
- Closest registry entries (read in full): IDEA-470 and the full shortlist in novelty-gate-S3.md (prior recorded gate reading, not a new reading claimed in this response).
- Separation criterion vs closest entry (and observation that falsifies it): a full signed normalized form reduction and compact corner spectral transfer; fixed-index or carrier-only convergence erases the distinction from the deferred continuation.
- Literature baseline and search limitations: bounded repository gate novelty-gate-S3.md; response literature screen is search/abstract level only; no priority claim.
- Applicable obstructions and exact hypotheses broken: fixed-index logarithmic weights alone do not control the full signed spectrum; global continuous-mass control is required. Carrier-family restrictions remain explicit.
- Novelty gate verdict: variant with difference; consolidated continuation of IDEA-470 at PR preparation, not an unrelated fresh mechanism.
- Cheapest decisive test: the analytic bound/transfer or strict family inequality stated above; see novelty-gate-S3.md for the original gate chronology.
- Kill criterion written before testing: the original failure obligations above and in novelty-gate-S3.md are preserved; missing signed control, wrong normalization or absent uniform error blocks the proposed conclusion.
- Test discriminability: the exact analytic obligations distinguish full-spectrum control from trial-only convergence; floating decimal comparisons alone cannot decide the theorem.
- Actual test results and committed evidence: the linked theory files and audit-01.md give the analytic outcome at its stated scope; existing floating receipts retain MEASURED status.
- Disposition and precise rejected scope, if any: retained continuation; no family-wide refutation or new PD-N.
- Disposition reason: no rejection; the completed obligations are recorded in linked theory and audit-01.md.
- Canonical theory / negative-result ID: the provisional IDs of the linked theory files; no final ID allocated in this response.
- Topic / completed audit link / history (no pending process stage): padua-mz-sharp-constants-20261106; audit-01.md; 2026-11-06 template completion preserving the original registration prose.

Canonical result pointer (audit A10): PD-T?mz-sharp-codex-S3-03; [theory](../theory/S3-corner-operator-limit.md). Completed [audit-01](../audit-01.md) accepts the linked analytic scope.
