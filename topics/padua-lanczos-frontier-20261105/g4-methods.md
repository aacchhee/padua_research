# G4 prospective replay and L7 source inspection

Rules/input head `bb67c1ee830d468fa33007e15008d5574d00ccf4`; Codex technical developer, gpt-6.1-sol medium, 2026-11-05. Root owns Git. This is routine replay and validation of a saved empirical protocol, not a new mechanism; no novelty claim or generation gate is invoked. No network access is needed with retained sources/dependencies.

## Plan recorded before execution

Read handoffs01/04, gates, report, E6 direction/producer/PD-T146 and external-code provenance, saved L7 protocol and skeleton, and L2.run_sel. G0's original FAIL and additive arithmetic-sensitivity resolution remain intact. G4 must execute both original cases before any new natural targets. Use unchanged current e6_benchmark.py and verify all manifested local Python source hashes against original E6 provenance. Restore historical e6-benchmarks.json from Git source2b52b432fe59c9a50aef9deebe5152c5d6874465 outside Git and verify239594 bytes / SHA256 e7a3f940c4bd79bbf84fbe4eeafca4186c9b969c92665fb972367becc23a3c58. Verify four polyrat source files at the original commit pin and exact NumPy2.3.5/SciPy1.17.0. Namespace loading retains unchanged upstream arithmetic.

Run rotpi4 n24 and triangle n20 as separate subprocesses with OPENBLAS_NUM_THREADS=1, no inherited OPENBLAS_CORETYPE, PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps and -B. Each cap1800s, no remote compute. Expected seconds/minutes per case; worst total60minutes. No duplicate successful rerun. Actual per-process command, environment/runtime/library configuration, code/source/input hashes, exit/time/output receipts and full comparisons go outside Git in /tmp/padua-lanczos-frontier-l7/g4. Commit only compact summaries, normally<16KiB.

Compare complete selected case objects recursively; retain every differing leaf externally including target QR coefficients and fit/closure metrics. Exact requirements: input hash, case dimensions, ranks and selection/order check. Saved diagnostic numeric screens remain gap absolute difference<=max(1e-10,1e-6*oldgap), reference condition relative difference<=1e-8, orthogonality<1e-12. Screens alone do not explain discrepancies or authorize PASS. Report every scalar metric difference and distinguish changed post-hoc target coefficients from fixed-target drift. Any unexplained discrepancy stops L7 pending root/reviewer explanation. G0 resolution supplies no blanket numerical tolerance waiver. No natural suite until separate root acceptance.

## Initial source findings (before runs)

The saved own() full branch uses Q[:,W] advanced-index copies, whereas L2.run_sel uses Q[:,:k] strided views. Equal mathematical CGS2 formulas do not imply equal floating operation/layout order; the skeleton's bitwise assertion is not justified by inspection. Fix by retaining the slice in the full branch, then verify actual entrywise outputs/paths on bounded validation inputs. Window branch must preserve its existing advanced-index arithmetic and adaptive scoring after first pass. This is an implementation repair, not a new selection.

Reference basis construction was inspected: total-degree product Chebyshev spans the intended polynomial space; triangle uses the same Jacobi/Dubiner formula as E6, implemented in longdouble. The Jacobi recurrence denominators and parameters match the standard three-term recurrence (positive parameters here). Execution must still cross-check against SciPy Jacobi on small cases, inspect longdouble rank/Gram and triangular solve residuals. Reference screens are numerical diagnostics, not rigorous enclosures.

The training/test replay executes the saved recurrence polynomial, with two projection-pass coefficients summed. It need not reproduce training Q bitwise because the recorded polynomial recurrence recombines coefficients in a different arithmetic order; quantify the error and avoid treating it as exact identity. The existing suite records it but has no prospective pass threshold, so root/reviewer must judge before suite interpretation. None of the natural-target suite is executed in this G4 step.

## Developer execution — 2026-11-05

Actual command from repository root:

```sh
python -B topics/padua-lanczos-frontier-20261105/code/g4_replay.py --external /tmp/padua-lanczos-frontier-g0/polyrat --deps /tmp/padua-lanczos-frontier-g0/deps --output-dir /tmp/padua-lanczos-frontier-l7/g4
python -B topics/padua-lanczos-frontier-20261105/code/g4_summarize.py --input-dir /tmp/padua-lanczos-frontier-l7/g4 --output topics/padua-lanczos-frontier-20261105/evidence/g4-replay.json
```

Both unchanged E6 subprocesses exited0, rotpi4 in2.57s, triangle in1.57s. Upstream source pins and all E6 manifested local Python source hashes match; both input hashes/dimensions/ranks/order checks match historical evidence. Upstream_yx and L2.dev are entrywise identical in both current cases. Reference condition relative discrepancy is2.84e-14 on rotpi4 and0 on triangle. Orthogonality stays<1e-12. **All12 method gap comparisons fail the saved numeric screens. G4 requires explanation; L7 STOP.**

| Case | Historical upstream_yx gap | Current gap | Absolute discrepancy | Historical/current midpoint adversarial test error |
| --- | ---: | ---: | ---: | ---: |
| rotpi4 n24 | .004105469352253462 | .005633784608963100 | .001528315256709638 | .001013860861616495 / .001549201669948424 |
| triangle n20 | .010163571396223751 | .015496196489764480 | .005332625093540728 | .001569426304778993 / .002628301644306280 |

The new target QR vector is again selected post hoc from the new missing direction; changed adversarial test numbers are not comparisons of one fixed target across environments. Full numerical leaf differences, including each target coefficient and closure/fit metric, remain in the hashed external comparison files. [Compact receipt](evidence/g4-replay.json) includes exact commands, timings, runtime, all method gap/Gram comparisons and raw file SHA/bytes. Small conditioning differences and small Gram errors do not explain the changed spans. No retrospective tolerance adjustment, G4 PASS or general numerical failure claim is made. These are developer executions, not independent audit; distinct supplementary review and root acceptance remain required before any suite.

## Bounded implementation/reference validation

Before fixing the skeleton, M80/n6 uniform-box validation (seed9107; no targets) showed nonzero full-mode L2 entry discrepancies: dev3.68e-16, mirror4.34e-16, alt7.03e-16, adapt5.00e-16. Replacing only full-mode advanced-index operands with the L2 slice restores bitwise equality. Window indexing/scoring unchanged.

Actual command:

```sh
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps OPENBLAS_NUM_THREADS=1 python -B topics/padua-lanczos-frontier-20261105/code/g4_validate.py --output topics/padua-lanczos-frontier-20261105/evidence/g4-primitives.json
```

Exit0; all8 method variants exactly reproduce L2 Q and parent paths on that bounded input. Training recurrence replay maximum is1.48e-15. Jacobi recurrence is compared for degrees0–7, parameters a=0,2,...,12,b=0 on97 grid points; max absolute difference from SciPy is1.27e-11 (large endpoint polynomial values, absolute comparison only). Longdouble QR reconstruction, Gram and known-coefficient triangular solves pass on all4 domains at degree6/M80; largest errors are8.81e-20,5.43e-19,1.79e-18 respectively. Longdouble mantissa63. This validates primitives at that finite scope, not the unexecuted degree24 suite, which still needs its casewise reference screens. No natural-target error, new fitting conclusion, or literature task was measured.

## Prospective bounded attribution — recorded before diagnostic execution

Root authorized diagnosis after the developer STOP; the STOP and original thresholds remain. For each actual rotpi4 n24 / triangle n20 input, create unchanged upstream_yx Q/H in separate Haswell and Nehalem binary64 processes and a Haswell longdouble process. Record actual loaded BLAS library/dispatch identities and hashes; cap each process1800s. Save arrays externally. Construct a separate longdouble polynomial reference without importing the L7 skeleton/reference (explicit Chebyshev recurrence after inverse rotation; separate Jacobi recurrence for triangle; longdouble CGS2). Compare same stored Q against both old double Householder and new longdouble reference to quantify reference noise separately from real measured normal error.

From stored binary64 Q/H, evaluate the raw local residual F_k=X_axis Q_parent-Q_prev H_prev,k-H_kk Q_k in longdouble. Propagate the frozen inverse E_k=(X_axis E_parent-E_prev H_prev,k-F_k)/H_kk, preserving all columns, actual parents and nodes. Compare normal(Q) to normal(E) against the independent reference and report the reconstruction defect. This reconstructs a measured normal error from local arithmetic residuals, not an operator norm or a worst-case inference. Compare residual magnitudes to u and to operation/input magnitudes; do not merely label any small residual u-scale without stating the scaling.

Prospective explanation-quality diagnostics: reference discrepancy and frozen-normal reconstruction defect should each be at most1% of the observed binary64 normal error and of the interkernel change used as evidence. Report actual values even on failure. Longdouble run should strongly reduce local residuals and normal error relative to binary64. These are quality screens for the explanation, not revised replay acceptance tolerances. If propagation precision cannot reconstruct the error at that scale, try one bounded higher-precision inverse control or leave attribution INCONCLUSIVE. No parameter search, no repeated successful baseline, no extrapolation from T24/n12. Historical Q/H are unavailable, so current arithmetic sensitivity and historical scale compatibility cannot establish the historical trajectory or enclose it by finitely many sampled kernels. Distinct reviewer must inspect/reexecute the diagnostic and root must issue an explicit additive G4 disposition before suite START.

### Diagnostic input-guard correction before comparison

The first diagnostic process stopped on its exact-input guard: L2.benchmark regenerates rotpi4 via BLAS rotation, so changing the worker kernel changed coordinates slightly. The Haswell Q/H was valid; Nehalem's generated-node artifact is retained as REJECTED-INPUT and never counted as a fixed-input control. Initial failure receipt records raw hashes and code hash externally. Correction: every worker now loads one parent-frozen P/w/n file; all kernels use exactly identical bytes. Reuse the valid Haswell Q/H, do not rerun that successful basis construction. New worker commands add --input; resumed driver records reused arrays explicitly. This discovery does not explain historical G4 mismatch, whose actual input hash matches exactly.

### Prospective coverage extension before class controls

Reviewer requires explanation of all12 failed method gaps, not an extrapolation from upstream_yx. L2.dev is entrywise identical to yx in both current/historical receipts; upstream_xy, forward-order mirror, alt and adapt are four additional classes. Reuse the frozen native P/w/n and execute those4 classes for the same3 kernel/precision controls, preserving exact sample bytes. Upstream_xy uses its actual H/idx. Own methods use actual L2.run_sel Q/info and reconstruct H by the exact existing slice arithmetic, checking each reconstructed column equals stored Q bitwise before diagnostic use. Extend propagation only to accept the recorded parent array. Quantify same-Q reference noise, local residual and frozen normal reconstruction separately for each class at its own gap scale. Each new worker retains1800s cap; no yx basis rerun. Adaptive path changes under arithmetic controls are recorded, not equated to fixed-parent runs.

## Attribution execution and scoped interpretation — developer, review pending

Actual driver commands (repository root; dependencies already retained, no network):

```sh
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps OPENBLAS_NUM_THREADS=1 OPENBLAS_CORETYPE=Haswell python -B topics/padua-lanczos-frontier-20261105/code/g4_attribution.py --external /tmp/padua-lanczos-frontier-g0/polyrat --output-dir /tmp/padua-lanczos-frontier-l7/attribution --receipt /tmp/padua-lanczos-frontier-l7/g4-attribution.json
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps OPENBLAS_NUM_THREADS=1 OPENBLAS_CORETYPE=Haswell python -B topics/padua-lanczos-frontier-20261105/code/g4_attribution.py --external /tmp/padua-lanczos-frontier-g0/polyrat --output-dir /tmp/padua-lanczos-frontier-l7/attribution --receipt /tmp/padua-lanczos-frontier-l7/g4-attribution.json --resume
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps OPENBLAS_NUM_THREADS=1 OPENBLAS_CORETYPE=Haswell python -B topics/padua-lanczos-frontier-20261105/code/g4_classes.py --external /tmp/padua-lanczos-frontier-g0/polyrat --input-dir /tmp/padua-lanczos-frontier-l7/attribution --output-dir /tmp/padua-lanczos-frontier-l7/classes --receipt /tmp/padua-lanczos-frontier-l7/g4-classes.json
python -B topics/padua-lanczos-frontier-20261105/code/g4_pack_attribution.py --work-dir /tmp/padua-lanczos-frontier-l7 --output topics/padua-lanczos-frontier-20261105/evidence/g4-attribution.json
```

First command exited1 on the input guard (max coordinate change2.22e-16). Second/third exited0; resumed yx diagnostic78.8s, other classes262.4s. No basis control timed out. Resumed receipt distinguishes the reused original Haswell worker command from its unexecuted prospective --input argv; no successful Q/H construction was repeated. Last packaging command exited0; earlier packaging exceeded its16KiB guard and was compacted into one13,683-byte receipt without splitting the scientific record. Full metric/command/array inventory remains external.

All30 controls use exactly the original replay inputs (rotpi4 hash a356501243b1fc883f795ee0908966b1fbeac4be09312e7eb8ee75f602229d42; triangle806ae0a1e54e9301955c9f7ddc52924922b3a8c51a7198174a0d476b291f0379). Source remains pinned. Actual BLAS libraries have SHA256 ee2039cf13a45e1e89f04d0cea9585657d93ffaa425594e1935161013fdf4e12 and8fb864c29cac4b25f6e2c139491ea96f2724dde42d51394f84e9c4a622e34790; runtime confirms Haswell/Nehalem dispatch respectively. Longdouble significand63. All recorded own-method coefficient reconstructions reproduce each stored Q column exactly. Both adaptive parent paths happen to remain identical across these controls; no general path invariance follows.

| Case / distinct class | Haswell binary64 gap | Nehalem binary64 gap | Haswell longdouble gap | Largest binary64 normal reconstruction defect |
| --- | ---: | ---: | ---: | ---: |
| rotpi4 yx=dev | .00563378 | .00447395 | 7.69e-6 | 4.83e-6 |
| rotpi4 xy | .0168917 | .0125899 | 5.53e-6 | 8.48e-6 |
| rotpi4 mirror | .973655 | .964836 | .0019424 | 5.20e-4 |
| rotpi4 alt | 1.52726e-8 | 1.50596e-8 | 9.75e-12 | 1.71e-11 |
| rotpi4 adapt | 3.38960e-6 | 2.09636e-6 | 1.50e-9 | 1.26e-9 |
| triangle yx=dev | .0154962 | .0148700 | 8.08e-6 | 1.01e-5 |
| triangle xy | .00175829 | .00281563 | 1.05e-6 | 1.45e-6 |
| triangle mirror | 2.46781e-7 | 1.98742e-7 | 5.08e-11 | 6.53e-11 |
| triangle alt | 8.73657e-8 | 1.64268e-7 | 9.44e-11 | 7.60e-11 |
| triangle adapt | 5.32254e-10 | 6.10635e-10 | 2.35e-13 | 2.45e-13 |

The separate higher-precision reference and original double reference differ by6.70e-13 (rotpi4) and8.43e-14 (triangle). These same-Q reference scales are much smaller than every reported binary64 gap, including triangle adapt. The measured local residual satisfies `max_k ||F_k|| / [u (||raw_k||+||projection_k||+||beta_k Q_k||)]` between .59 and .76 across binary64 controls (exact values retained); this gives an explicit operation-scale meaning to "u-scale". Propagating those actual residuals through each stored recurrence reconstructs its normal error. Across all10 class/cases, the largest ratio among reference noise or reconstruction defect divided by either binary64 normal error or the same-Q kernel normal difference is .001759, below the prospective .01 quality goal. Thus current arithmetic sensitivity is quantitatively demonstrated at each actual case/method scale; reference noise cannot account for it. Higher precision reduces normal errors by large factors in every class, consistent with that explanation. Extended-run inverse reconstruction itself is limited by longdouble arithmetic and is not claimed accurate at its much smaller drift scale.

This is numerical attribution, not a rigorous enclosure or computer proof. The local residual is evaluated from stored Q/H in longdouble; the remaining finite-precision reconstruction defect is measured explicitly. Historical gaps have the same orders as current binary64 controls but are **not** reconstructed or enclosed by kernel samples. Missing historical Q/H/dispatch prevents causal identification of its exact roundings. Changed adversarial coefficients select different targets, as already disclosed. No universal smooth-fit loss or safety result follows. The distinct supplementary reviewer has the stable code/arrays and must judge whether this evidence explains the replay discrepancy class under the unchanged criterion. **Developer attribution alone does not change the G4 STOP or authorize the suite.**
