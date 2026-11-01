# Signed Padua MZ — development report

Branch: `codex/padua-mz-2d-20261101`. [Draft PR14](https://github.com/aacchhee/padua_research/pull/14). Base/main synchronized at `806cc7b4509fd93bae652f9545d32d95529f8281`. Stage WORK; Claude audit PENDING. This report is being updated during the campaign and does not request merge.

All conventions are fixed in [definitions.md](definitions.md). In particular the measure is unnormalized dxdy, the weights are signed, and the approximation space has total degree n. Positive Chebyshev cubature is a separate object.

## Current results

| Item | Result / status | Evidence and limitation |
|---|---|---|
| D1 | All-degree exact aliases and rational Gram pencil; analytic proof being finalized | Complement and rectangular folds; error already at degree m+1; theoretical source attribution screened without a novelty claim |
| D1 verdict | PASS: a bounded family of masked tensor Hankel/Toeplitz terms, with explicit one-dimensional Fourier norm control | Generic coefficient-norm control does not prove a sharp bound in the Legendre/Lebesgue metric |
| D0 | MEASURED reproduction and extension to m100 with full extreme eigenvectors and matching tensor-CC controls | [D0](directions/D0.md), [durable measured record](../../tracks/mz-constants/theory/mz2d-measured-spectra.md); no asymptotic inference |
| Finite exact spectra | Exact integer-congruence checks m10/20/30/40 completed; certification status awaits written reduction and different-agent rerun | [D6](directions/D6.md); four1e-6-wide extremal brackets per m |
| Moderate-degree threshold | Exact m30 rational witness has Q(p²)/integral(p²)<1/4 | Therefore eta>3/4 once the reduction and independent rerun are complete; this refutes an applicability hypothesis, not a conditional theorem |
| D2/D3/D4/D5 | Active; universal signed-Padua conclusions OPEN | Individual direction records retain actual failed mechanisms and candidate dispositions |
| D7 | Waiting for D2/D3 to stop | [D7](directions/D7.md) |

Measured Padua endpoint extrema, n=m−1:

| m | lambda_minus | lambda_plus | eta |
|---:|---:|---:|---:|
|10|0.356191382630|1.634856614784|0.643808617370|
|20|0.272233004958|1.723313731670|0.727766995042|
|30|0.236705530370|1.757929855946|0.763294469630|
|40|0.214817029467|1.778088623884|0.785182970533|
|60|0.188593480489|1.802011149918|0.811406519511|
|80|0.172730495887|1.816497914219|0.827269504113|
|100|0.161748411019|1.826582423850|0.838251588981|

Finite tables do not determine endpoint logarithmic order, positivity for every m, a universal upper threshold, or convergence of eta. Known marginal compression already supplies a one-sided upper bound for lambda_minus and liminf eta>=1; it supplies no matching 2D lower bound or limsup.

## Source distinctions and ASV context

[Primary-source review](literature.md) is being completed. The verified source conventions separate the signed interpolatory Lebesgue Padua rule, positive product-Chebyshev Padua cubature, and Xu/MPX hyperinterpolation. The selected author-preprint formula discrepancy is scoped to that inspected version and normalized independently; no journal erratum is asserted. The exact published ASV wording remains a prior-reader report wherever this session reached only its author version.

What to tell An–Sommariva–Vianello, without contacting them: the campaign now has an explicit signed-Padua alias formula and finite rigorously checkable endpoint brackets, plus a moderate-degree eta>3/4 witness. The all-degree Padua spectral and endpoint questions must be reported with their actual final statuses after the direction work; numerical evidence cannot supply the missing theory. No message has been sent.

## Runs needed / local delivery

Independent exact rerun, analytic reconstruction and final Claude audit remain pending at this checkpoint. Final-ID assignment follows another fresh reservation check during preparation. No bridge to AC's Windows files is available: copy this topic's final entry to `C:\Users\andreyac\Downloads\padua\results\padua-mz-2d-20261101.md`. Large evidence, if any, needs the specified cold-storage manifest and handoff. No archival delivery is claimed.
