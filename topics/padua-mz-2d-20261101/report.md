# Signed Padua MZ — campaign report

[Draft PR14](https://github.com/aacchhee/padua_research/pull/14) · branch `codex/padua-mz-2d-20261101` · main/base `806cc7b4509fd93bae652f9545d32d95529f8281`. Claude Opus 5.5 xhigh [audit-01](audit-01.md) **ACCEPTED the mathematics at its stated scope**. Stage PR after the six documentation findings are addressed in [response-01](response-01.md); draft retained pending AC's merge order and integration preparation. Development mathematics used gpt-6.1-sol xhigh, code/mechanical work medium, supplementary adversarial review gpt-6-astra xhigh. Root runtime metadata is unexposed.

The [definitions](definitions.md) fix signed interpolatory weights for unnormalized dxdy and a total-degree Legendre space. Positive Chebyshev cubature is distinct. Accepted PD-T101 is a dependency; audit-pending A2 records were contextual inputs, not proof dependencies of the new theorems.

## Proved development results

| ID | Exact scope | Durable record |
|---|---|---|
| PD-T106 | All-degree signed Padua aliases; exactness precisely m; rational Gram pencil | [Aliases](../../tracks/mz-constants/theory/mz2d-aliasing.md) |
| PD-T109 | At most160 controlled masked tensor Hankel/Toeplitz terms | [Structure](../../tracks/mz-constants/theory/mz2d-defect-structure.md) |
| PD-T107 | Independently replayed strict rational spectral brackets at m10/20/30/40 | [Certification](../../tracks/mz-constants/theory/mz2d-certified-spectra.md) |
| PD-T111 | Exact corner weights, negative for every m>=3, with w_c=−(4log m+O(1))/m^4 | [Corners](../../tracks/mz-constants/theory/mz2d-lower-corner-weights.md) |
| PD-T115 | Exact diamond-filter reconstruction for every n<m | [Reconstruction](../../tracks/mz-constants/theory/mz2d-fixed-ratio-diamond-reconstruction.md) |
| PD-T112/113 | Correct signed operator norm identity, degree-dependent bound, reproduction/error estimate when n+r<=m | [Norm](../../tracks/mz-constants/theory/mz2d-hyperinterpolation-absolute.md), [reproduction](../../tracks/mz-constants/theory/mz2d-hyperinterpolation-reproduction.md) |
| PD-T117 | Tensor-CC extrema on the same total-degree space equal the extrema of the coordinate CC rules; endpoint minimum has order log^-2 m, eta tends to1 | [Tensor control](../../tracks/mz-constants/theory/mz2d-tensor-control.md) |

Claude audit-01 accepts all17 PROVED,2 MEASURED and3 OPEN classifications and every candidate disposition. Response-01 changes records and registries only; mathematical statuses and proof bodies remain unchanged. No historical novelty is claimed.

## D1 verdict and endpoint answer

**D1 PASS.** Put A=f_m(a), B=f_(m+1)(b), where f_N folds modulo2N into[0,N], and h_even=2/(1−k²), h_odd=0. Then Q_m(T_a T_b)=h_A h_B if A+B<=m, and h_(m−A)h_(m+1−B) otherwise. The nodal identity T_(m+1)(y)=T_m(x) makes degree m+1 inexact: considering only degrees>=2m would miss endpoint defects.

Five alias regions give ten separable scalar kernels. Product-to-sum and difference-sign sectors give at most160 tensor terms. Their coupled half-plane masks are one-dimensional signed-degree truncations with Fourier norm multiplier<=1+log(8n+1). This is actual operator control, not merely an index table. It does not settle the continuously normalized signed spectrum.

D2/D3/D4 each stopped after three bounded rounds. For **signed Padua**, all-m lambda_plus<2, all-m positive definiteness, two-sided endpoint order (log^-2 versus log^-4 or another law), eta convergence and explicit eta(theta)<1 for every theta<1 remain **OPEN**. Existing PD-T018/021 give only lambda_minus<=C/(log m)^2 and liminf eta>=1. PD-T028 retains OPEN status. The tensor-control order is proved log^-2 and is not transferred to the signed rule.

D7 began only after D2/D3 stopped and selected one structural family, tensor CC. Xu, Morrow–Patterson and general Lissajous–Chebyshev theorem attempts remain deferred; primary convention checks are in the source review.

## Scoped counterexamples and failed routes

| ID | Conclusion and limit |
|---|---|
| PD-N044 | Explicit degree29 polynomial at m30 has Q(p²)/integral(p²)<1/4, hence eta>3/4. Refutes the uniform applicability hypothesis, not An–Wu's conditional theorem. |
| PD-N045/046 | Coefficient sign-switch/Z-matrix transfer fails; doubled pointwise tensor-weight domination fails at m2. D4's repeated negative-node floor failure is consolidated into PD-N045. |
| PD-N047 | Two critical coordinate witnesses exceed the total-degree cutoff. This does not refute a Padua log^-4 law. |
| PD-N048 | Negative-corner correction has continuous-metric norm~(log m)/6, or theta^4(log m)/6 at fixed positive ratio; separate pieces can diverge even inside half-exactness where their signed sum is I. |
| PD-N049 | MEASURED only: the specified rhombus packet failed its bounded improvement screen; other packets remain possible. |
| PD-N050/051 | Signed Gram upper bound alone fails for general arbitrary continuous inputs. The actual endpoint Padua coefficient operator reproduces the complete space Pi1 but fails on quadratics for every m>=3, precluding E2-only bounds. |
| PD-N052/053 | Uniform absolute-Gram/negative-leverage majorants diverge; direct rectangular Fejer reconstruction has an explicit spurious mode. Degree-dependent bounds and diamond reconstruction remain valid. |

All18 candidates, including equivalent and deferred ones, are retained. Failed routes do not reject the universal spectral targets. Actual uniform signed Padua C-to-L2 operator stability remains OPEN.

## Measurements and independent evidence

PD-T108 is **MEASURED**: full extreme vectors and matching tensor controls at m=10,20,30,40,60,80,100. Maximum recorded float residual1.30e−12; direct old-case crosschecks agree within7.3e−14. A separate every-integer m2..40 sweep includes odd degrees and found no nonpositive minimum or maximum reaching2. No fitted asymptotic is claimed.

| m | Padua lambda_minus | Padua lambda_plus | eta |
|---:|---:|---:|---:|
|10|0.356191382630|1.634856614784|0.643808617370|
|20|0.272233004958|1.723313731670|0.727766995042|
|30|0.236705530370|1.757929855946|0.763294469630|
|40|0.214817029467|1.778088623884|0.785182970533|
|60|0.188593480489|1.802011149918|0.811406519511|
|80|0.172730495887|1.816497914219|0.827269504113|
|100|0.161748411019|1.826582423850|0.838251588981|

At m10/20/30/40 each extremum has an independently checked strict bracket of width10^-6. Acceptance uses rational moments, exact integer congruences and signed strict row dominance; floats only propose transformations. A different worker reran the full producer, independently evaluated the stored225-term witness, and checked245 cyclotomic nodal moments,371 Gram pairs,1,221 region cases and six rejection controls. [Independent evidence](independent-checks.md) and [supplementary Astra review](supplementary-audit.md) record scope and hashes. Both supplementary findings were repaired and rechecked. Claude audit-01 accepted the scoped mathematics after its own full exact-producer rerun and additional checks. Its committed second-method certificate receipt covers m10–30; m40 was still running at audit commit. The accepted m40 result also has the complete exact-producer rerun, so that partial extra receipt does not weaken acceptance.

## What to tell An–Sommariva–Vianello

Their work supplies the numerical question and weak/strong distinction. This campaign adds an explicit signed-Padua error pencil, finite operator architecture, exact endpoint brackets and a moderate m30 eta>3/4 certificate. It identifies the direct signed coefficient operator's correct reproduction degree and distinguishes positive Chebyshev/Xu hyperinterpolation. The signed all-m positivity, upper threshold and endpoint order remain OPEN. The tensor-control theorem is separate. Historical novelty is screened, not cleared; communicate these claims after audit. No contact was made.

## Runs needed / missing fulltexts / delivery

- Next step: AC's merge-order decision and the corresponding integration preparation in handoff04. The required Claude audit is complete; audit-01 explicitly permits these listed documentation fixes to proceed without re-audit. PR stays draft.
- Integration rehearsal: this campaign squashes cleanly onto pinned main; prospective PR15 integration conflicts in the crosswalk and allocation ledger. Reconcile those reservation texts at readiness, after audit and AC's merge-order decision; no live merge was performed.
- Missing independent final-version comparisons: SVZ DOI10.1007/s11075-008-9203-x; Dencker–Erb DOI10.1016/j.jat.2017.03.003; Kolomoitsev–Lomako DOI10.1016/j.amc.2021.126192; Xu1996 DOI10.1006/jath.1996.0102; ASV published body DOI10.1016/j.matcom.2026.10.001. KLP2018 body DOI10.1016/j.jat.2018.02.005 was unreachable. [Source review](literature.md) supplies journal links, inspected versions and locators; unread bodies are not theorem dependencies.
- No Windows bridge: copy this report and the audit handoff to `C:\Users\andreyac\Downloads\padua\results\padua-mz-2d-20261101.md`. No local delivery is claimed. All essential evidence fits Git limits; no large artifact requires cold-storage export.
- No separate2D manuscript section was added because the signed D2/D3 spectral targets did not reach their success criterion. The merged manuscript is unchanged.
