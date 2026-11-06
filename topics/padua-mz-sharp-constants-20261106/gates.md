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

## 2026-11-06 — K3 measured comparison

Both upper-spectrum fits are USABLE under all preregistered checks. Final-window limits1.0044369722946567 (even),1.0044369722985076 (odd); window drift<=1.15e-9 and parity difference3.85e-12. S2 finiteJ512 proxy1.0044369188646673 differs by<=5.344e-8<1e-3: operational MEASURED PASS. No certified infinite Galerkin tail or finite-spectrum limit is claimed. [Comparison](evidence/S4-k3-comparison.json). K4 and the2-D K5 prediction are still pending.

## 2026-11-06 — S3 exact operator / K5 registration before model computation

Register [S3 corner operator](ideas/S3-corner-operator.md): H=L²({a,b>=0,a+b<=1},ab da db), psi_jk=J0(pi j a)J0(pi k b), B_K=−16 sum_((1+j)(1+k)<=K,j+k even) e_j e_k(−1)^j |psi_jk><psi_jk|. Predicted slopes are inf/sup spectrum of the operator-norm limitB, equal on even and oddm. Two active corners predict identical blocks; other corner leading blocks are zero. This is a prospective model assertion with proof OPEN at registration, not an observed fit or established parity agreement. Its finite-rank norm convergence and kernel transfer must be proved. K4 has no decimal model prediction or slope-window protocol yet; K5's2-D prediction is equality, registered before S3 model computation and any new S4 parity fit.

## 2026-11-06 — S4 Padua scan and K4/K5 numerical protocol

Accept [S4-padua-proposal.json](S4-padua-proposal.json) and [cost/fit rationale](attempts/S4-padua-proposal.md) before runs. Each parity uses disjoint m windows800/1000/1200/1400 and1800/2200/2600/3000 (odd+1), freshseed20261106. Two-column scaled SVD fits to intercept+slope log(m/mref); required rank/conditioning/residual, signed slope and5%two-window stability checks are exactly in the proposal. K4 is usable only if both parity slopes pass stability, then compare to preregistered heuristic−0.1336,+0.0456 at10%. Those decimals are finiteK128 model proxies with uncertified numerical tail, not exact constant evaluations. Exact prediction is spectrumB. K5 predicted equality already registered; measured parity agreement needs both stable and final-window slopes within5%, never proves true agreement.

Upper FIRST: evenm800 pilot,30min or2000matvec cap. Continue upper cases only after a successful residual-guarded pilot and2xcubic forecast<=16CPUh cumulative and<=6h perrow; otherwise retain failed receipt and mark upper numerical gate INCONCLUSIVE, no automatic stalled campaign. Minima may proceed on all16rows, at most2degrees concurrently. Finite validation10/11/20/21 and weight/seed/residual controls are required. No Syvert use.

Registration chronology: S3 exact operator was saved before its model computation, while publication59d02c7 followed that first model-only computation and preceded all new S4 slopefits. The source file/receipt UTC chronology is retained in the S3 attempt. This distinction does not change K5's prospective parity requirement; no final slope data informed the model.
