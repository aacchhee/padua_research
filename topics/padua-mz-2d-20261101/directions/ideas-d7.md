# IDEA-227 — Disjoint coordinate defects on the total-degree tensor control

Aliases: exact tensor-CC extreme eigenvalues; wedge decomposition;
total-degree Hankel pullback; no mixed alias term.

- Question / scope: an exact spectral reduction for `C_m tensor C_(m+1)` on `Pi_n`, m>=2 and 0<=n<=m-1, with dxdy normalization.
- Mechanism and hypotheses: tensor-factor the Gram entries, use one-dimensional exactness to exclude simultaneous high-coordinate errors, then show the two surviving defects occupy disjoint Legendre-coordinate wedges.
- Closest registry entries read in full: IDEA-056/072 and their marginal records; IDEA-205 generic product-grid OP reduction; accepted PD-T013/017/018/022--024. The fresh gate and source-reading limits are in D7.md.
- Separation criterion vs closest entry: exact equality of the full total-degree extreme eigenvalues to the extrema among the two coordinate CC spectra. A mere product inequality or coordinate compression does not provide this equality. An allowed nonzero mixed defect or shared active wedge would kill the proposed distinction.
- Literature baseline and search limitations: product quadrature and OPs are classical; literature index plus ASV/classical-MZ records screened. No exhaustive historical novelty claim or primary-source all-family theorem is inferred.
- Applicable obstructions and exact hypotheses broken: rectangular tensor-degree estimates can lose a second logarithm; signed Padua weights have extra complement aliases and cannot inherit this theorem. D2's failed pointwise tensor majorant prevents a free Padua comparison.
- Novelty gate verdict: variant with a specified structural difference within the documented local search; historical duplication unresolved.
- Cheapest decisive test: degree-count the mixed defect, then identify its two row supports before any spectrum.
- Kill criterion written before testing: a single legal pair with both coordinate defects nonzero, or an index belonging to both active coordinate supports, stops the exact decomposition. A later floating mismatch also stops the claimed extrema formula but finite agreement cannot prove it.
- Test discriminability: the exact support test is valid for all m,n in the stated range; it can justify an operator identity, while finite spectral tests only check implementation.
- Actual test results: the mixed defect requires forbidden total degree at least 2m+3, and the remaining supports are the disjoint wedges a-b>m-n and b-a>m+1-n. Full analytic proof establishes exact tensor extrema and the stated one-dimensional consequences. A 20-case float64 regression found maximum extreme discrepancy 1.12e-15; it is diagnostic only.
- Disposition: retained PROVED analytic theorem for one family; other named families remain deferred pending their primary conventions. No failed candidate or D7 negative record was generated.
- Canonical theory / ID: PD-T117, `mz2d-tensor-control.md`; required audit pending.
- History: D7 activated by root only after D2/D3 STOP, 2026-11-01; requested gpt-6.1-sol xhigh.
