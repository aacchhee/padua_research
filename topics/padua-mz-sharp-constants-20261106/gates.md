# Gates and pre-registrations

Registered before first campaign computation, 2026-11-06, at input head 2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861. Original criteria are handoff01; preserve them unchanged.

| Gate | Criterion | Current verdict |
|---|---|---|
| K0 | PD-T026 CC near-critical recorded N; PD-T300 minima m800/1000; one PD-T379 carrier norm limit. Unexplained float mismatch >1e-10 relative stops inference. | PASS under dated clarification below; independent replay pending |
| K1 | Fit log(N)^2 lambda_min = c + a log(log N)/log N + b/log N separately by parity on two disjoint windows; c agreement within 2%. Otherwise INCONCLUSIVE, one extension maximum. | PENDING |
| K2 | S1 prediction committed before final K1 numbers; kill model for >5% disagreement with passed K1; one revision only. | PENDING |
| K3 | Kill S2 model for predicted upper limit discrepancy >1e-3. | PENDING |
| K4 | Kill S3 model for >10% slope discrepancy on stable large-m windows. Stability must be documented before calling asymptotic. | PENDING |
| K5 | Register equality or inequality prediction before parity agreement claim. | PENDING |

K0 is verification, with no fitted target. No K1/K3/K4 fit execution is authorized until exact grids, windows, weights and residual checks are appended here and published. S1–S3 model predictions are not yet registered. Existing handoff steering measurements are historical inputs, never fresh evidence.


## 2026-11-06 — K0 clarification and developer outcome

K0 original remains above and in handoff01. A finite norm need not equal its limiting value at1e-10. The operational replay compares its exact finite Fourier/moment norm to a separately assembled composite angular quadrature at1e-10; convergence to the stated limit is recorded separately without a fit. Developer K0: PASS under this clarification. CC max relative difference3.997e-15; Padua m800/m1000 bit-identical. Carrier finite norm replay max relative error3.31e-16; limiting offset at4096 about−5.22e-5, not a1e-10 limit match. Initial high-degree global x-Gauss mismatch and corrected check are both preserved. Supplementary independent rerun PENDING.

## 2026-11-06 — S4 CC scan pre-registration

Accept the exact grid, disjoint windows, SVD columns, parity treatment, tolerances, seed and one-extension rule in [S4-scan-proposal.json](S4-scan-proposal.json), before the large scan. Raw extrema may be computed now. K1 fit and disclosure of final-window data to S1 remain held until S1's model prediction is committed (or an explicit documented failure to derive one). K3 upper fit remains held for its separate pre-registration after S2 prediction. Structured solver validation is finite MEASURED evidence, not a computer proof or limit theorem.

## Independent K0 outcome

PASS under the dated clarification above. [Independent check](independent-checks-k0.md) changed the Padua seed and separately reran all cases; maximum relative reference differences4.00e-15 (CC),1.84e-14 (Padua) and3.31e-16 (finite carrier quadrature). No limiting-norm equality or spectral proof follows.

## 2026-11-06 — S1 prediction registration before K1

S1 registers c_model=pi^4/8 for both N parities, before any K1 fit or disclosure of final-window data to S1. [Model record](theory/S1-model.md) labels transfer CONDITIONAL; [Volterra model](theory/S1-volterra-model.md) supplies its separate analytic model norm. Neither proves the finite CC spectral limit. K5's S1 parity prediction is equality; the2-D K5 prediction is not yet registered. K2 compares the committed prediction against K1 only if K1 passes. The original handoff fit is retained as a preregistered numerical ansatz; classical Widom–Wilf attribution has not been verified by the [bounded literature screen](literature-screen.md).

## 2026-11-06 — K1/K2 outcome and S1 stop

Exact registered K1 fits pass both parities: windowA/windowB intercepts13.2177582161/13.0611359933 (even),13.2176998261/13.0611326732 (odd), relative window differences1.185%. K2 operationally KILL_MODEL: pi^4/8 differs from final-windowB by7.268% (relative to the prediction), above5%. This is not a proof the actual limit differs. S1 accepts the gate outcome, makes no arbitrary revision and stops this limiting-model route; no second model or extension is run. Its one-sided bound, completed before K2 receipt, is retained independently of the prediction. [Fit receipt](evidence/S4-k1-fit.json).

## 2026-11-06 — S2 operator prediction before Galerkin solve / K3 fit

Register the exact microscopic endpoint variational norm in [S2-endpoint-model.md](theory/S2-endpoint-model.md) as S2's proposed common even/odd limiting value. No numerical norm or upper-spectrum fit has been computed/read by S2 at registration. The record states its unproved finite-to-model obligations. K3 final extrapolation remains held for an exact numerical fit pre-registration; model Galerkin computation may follow publication.

## 2026-11-06 — K3 numerical protocol before fitting

Use the already registered disjoint raw-grid windows j8–14 and j15–20, parity separate with physicalN. Fit lambda_max−1=c0+a(Nref/N)^2+b(Nref/N)^2 log(N/Nref), Nref the smallest N in each window, by unweighted float64 SVD with columns scaled to unit2norm and rank3 required. Limit display1+c0. Require max absolute residual<=1e-7 inA and<=1e-8 inB, intercept agreement<=1e-6 across windows and final parity agreement<=1e-6; otherwise INCONCLUSIVE, no posthoc alternative fit. Raw residual/constraint guards apply. Original K3 kill is absolute model-norm discrepancy>1e-3 to finalB. Model Galerkin J32/64/128/256/512; one J1024 extension only if final change>1e-5. Galerkin stability is MEASURED; without a tail bound, no certified full norm is claimed.
