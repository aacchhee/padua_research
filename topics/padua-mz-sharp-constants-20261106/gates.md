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
