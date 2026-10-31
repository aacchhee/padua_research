# PD-T026 — Bounded reproduced numerical spectra

Review update, 2026-10-31: final ID allocation and scoped independent Astra review are complete; see topics/mz-constants/independent-astra-01.md and ID_CROSSWALK.md. The original development-stage pending-review wording below is historical. Required Claude audit and unresolved literature/novelty coverage remain PENDING. This administrative update changes no mathematical claim or proof.

ID kind: PD-T.
Aliases: CC/Padua finite-spectrum reproduction; Hankel and nodal diagnostics.
Split from: none. Split into: none.

## Statement

In the finite float64 runs listed below, the supplied CC generalized eigenproblem and separately assembled direct Legendre Gram problem agree in their extreme eigenvalues within 1.35e-13; the original N60 Hankel reconstruction residuals are below 1.17e-14; the listed CC and Padua spectra, marginal discrepancies, nodal Schur diagnostics and HSS ranks were measured as recorded in the linked JSON. These are observations of explicitly specified finite numerical computations, without universal quantifiers over N or m.

## Definitions

CC uses N+1 points cos(k*pi/N), Lebesgue measure dx on [-1,1], polynomials degree at most n, and orthonormal Legendre Gram G. Its generalized Chebyshev pencil is Q a=lambda T a with T_ij=(I(T_(i+j))+I(T_|i-j|))/2 and Q using the supplied Lobatto moment aliasing. eta=max(1-lambda_min,lambda_max-1). Padua uses the supplied m-degree point convention and signed interpolatory weights for dx dy; total-degree product-Legendre basis degree n. Node diagnostics use W^(-1/2)(Mc-W)W^(-1/2) for degree N.

## Assumptions

Pinned supplied Python inputs, inspected function extraction in the runner, float64 NumPy/SciPy linear algebra, and the exact finite parameter scope in `topics/mz-constants/reproduction.md`. There is no assumption that signed Padua weights form a positive measure.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Finite scope / evidence |
|---|---|---|
| Hankel reconstruction | MEASURED | Original N60: residuals 1.16663e-14, 6.77236e-15; support Boolean true |
| Two CC formulations | MEASURED | N=3,4,5,9,10,21,40,81; n=floor(N/2),N-1,N; max extreme discrepancy 1.34337e-13 |
| Near-critical CC | MEASURED | N=40,80,160,320,640,1280; n=N-1 |
| Fixed-ratio CC | MEASURED | ratios .6,.75,.9,.95; N=40,80,160,320,640 |
| Signed Padua | MEASURED | m=10,20,30,40; n=m-1 |
| Correct x marginal | MEASURED | m=10,20,31; max abs(wx-2*wcc)<8.73e-16 |
| Schur/weight-floor diagnostics | MEASURED | N=40,80,160,320,640; degree n=N |
| Node HSS ranks | MEASURED | N=256,512; finite hierarchy and thresholds in runner |

Candidate / claim disposition: none. This record adds no candidate mechanism or novelty claim.

## Depends on

Supplied `padua_mz_inputs/code` routines and numerical libraries, identified by SHA256 and versions in evidence. No unproved asymptotic result is assumed. Mathematical identity/proof records maintained elsewhere are not upgraded by this computation.

## Checks

Producer: `tracks/mz-constants/code/reproduce.py`. Essential output: `tracks/mz-constants/evidence/reproduction.json`. Command, input identities, environment, unsuccessful initial serialization attempt and exact finite scope: `topics/mz-constants/reproduction.md`. Hashes/sizes: `tracks/mz-constants/evidence/reproduction-manifest.json`.

The separate direct assembly is a cross-formulation comparison executed by the developer, **not** an independent-agent rerun. Assigned Astra independent replay remains pending until its own execution is recorded.

## Sources

Supplied input bundle only for computational reproduction. Imported `.out` claims, including N20480, were not treated as reproduced evidence.

## Proof or evidence

There is no proof claim. Near-critical CC measured values:

| N | lambda_min | lambda_max | eta |
|---:|---:|---:|---:|
|40|.259849024875495|1.004471120722071|.740150975124505|
|80|.216153284009021|1.004439734729248|.783846715990979|
|160|.182490276565946|1.004439101388067|.817509723434055|
|320|.156015183642123|1.004437800957723|.843984816357877|
|640|.134833488162936|1.004437221578550|.865166511837064|
|1280|.117635155992213|1.004437035065849|.882364844007788|

Padua measured values:

|m|n|lambda_min|lambda_max|eta|negative weights|
|---:|---:|---:|---:|---:|---:|
|10|9|.356191382629827|1.634856614783791|.643808617370174|2|
|20|19|.272233004958059|1.723313731669768|.727766995041941|2|
|30|29|.236705530370051|1.757929855946481|.763294469629949|2|
|40|39|.214817029467331|1.778088623883760|.785182970532669|2|

The JSON is authoritative for additional parity values, U Rayleigh quotients, fixed-ratio spectra, marginal sums, Schur stdout and all finite HSS ranks.

## Scope

Finite measured consistency and spectra only. No monotonicity, limit, uniform positivity, asymptotic decay, Schur bound, HSS rank law, or computer-assisted proof is established. In particular, n=N Schur upper eigenvalues near 2 concern a different space from n=N-1 upper eigenvalues near 1.00444.

## Open items

Independent actual replay; external archival at AC's designated destination. Asymptotic claims and imported large-N output remain unverified by this record.

## History

2026-10-31: Codex reproduction worker; rules d36722823441dc40c6e19d69a174459348dd309c; gpt-6.1-sol, medium (explicit orchestration assignment). Created bounded numerical observation record from actual completed execution, without inherited source-output promotion.
