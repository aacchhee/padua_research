# PD-T?padua-3d-20261106-usable-U1-measurements — parity accuracy, noise and cost

ID kind: PD-T. Aliases: usable oversampled least squares; Haar versus OLS.
Split from: none. Split into: none. No final ID allocated.

## Statement

For n=4,8,12,16 the explicit known anisotropic/equal parity recipes,
inherited globalQR and inherited discrete-Leja interpolation were executed
on all four functions and both independent assessment sets fixed in
[the published protocol](../usable1.md). All16 Round1 cases and all8
same-node OLS Round2 cases passed the frozen reproduction/Gram gates.
Within this finite experiment, anisotropic Haar-WLS improves empirical
Sobol RMS for every prescribed function versus both interpolation controls
(with entire-function errors at n12/16 below the prewritten ratio floor).
Its common-total-budget iid-noise risk coefficient is smaller at every
tested degree. It does not uniformly improve sampled maximum error:
the radial rational function gives explicit losses at n12 and16.

OLS reduces covariance risk on both parity families at every tested
degree, with a modest2.47–8.03percent risk decrease and greater setup cost.
Deterministic error changes have both signs. These statements concern
exactly the saved algorithms, inputs, assessment and environment; no
continuous supremum, asymptotic rate or universal superiority is claimed.

## Definitions and assumptions

N=binom(n+3,3). M is the number of distinct observations. Basis, nodes,
weights, ordering, four functions, assessment seeds, noise seeds and σ=1e−3
are exactly the prospectively fixed definitions in usable1.md. RMS uses
4096 product-Chebyshev scrambled Sobol assessment points. Sampled maximum
uses their union with21³ angular Lobatto points. Every assessment is
independent of node selection, although individual assessment coordinates
may coincide with some construction coordinates. No data were tuned.

With c=C y, risk means tr(CC^T); budget risk is M tr(CC^T), corresponding
to a common total B observations with σ²M/B variance at each node average.
The finite trace is binary64 evaluation of an exact-model covariance
formula. The separately saved noisy RMS is one realization, not an
estimate of the expectation. All claims use product Chebyshev probability,
not uniform volume. Solver costs exclude target-function evaluation time.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / limit |
|---|---|---|
| Actual finite errors, covariance traces, conditioning and timings | MEASURED | Both frozen receipts and raw maps; supplementary replay separate |
| All-degree construction, reproduction and analytic noise bounds | PROVED under separate IDs | [Recipe](u1-parity-recipe.md), [noise](u1-noise-bound.md), [OLS](u1-ordinary-ls-blue.md) |
| Universal error dominance, near-minimal interpolation or global optimality | OPEN, outside statement | No such conclusion follows from these data |

Candidate C1 disposition: retained known-mechanism operational recipe.
Candidate C2 disposition: retained known same-node solver tradeoff; no
automatic replacement or new mechanism is claimed. Neither is a PD-N.
The old restricted-QR and boundary-priority extraction failures remain
unchanged and were not rerun.

## Depends on

Known explicit parity Grams and inherited QR/Leja algorithms, with exact
source identities in both receipts. Analytic interpretations use the
separate local recipe/noise/OLS records. No imported log³ theorem is a
premise of any finite numerical observation here.

## Checks and executed evidence

Protocol published by root in
`fe23e002f25912b2ca2a09b225e385f596f824fe`, after shared gate
`26a4b5e3b7d74f58c862e95f51a540a9935d1240`. Both runs use the unchanged
17584-byte `code/u1_usable.py`, SHA256
`50da9061b5ec4a5a0735664450d62e7e8e2f19675eed66aca0eb463ff193b0d4`.
Its source snapshot is present in each raw directory; code/data only are
hash-pinned. Actual commands, relative to the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u1_usable.py round1 --raw /tmp/padua-u1-38227202-20261107-r1-0722 --out topics/padua-3d-20261106/evidence/u1-round1.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u1_usable.py round2 --raw /tmp/padua-u1-38227202-20261107-r2-0724 --reference-raw /tmp/padua-u1-38227202-20261107-r1-0722 --out topics/padua-3d-20261106/evidence/u1-round2.json
```

Round1 executed07:13:40–07:14:10UTC; Round2 07:14:19–07:14:29UTC on
2026-11-07. Python3.12.14, NumPy2.3.5, SciPy1.17.0, Linux x86_64.
Every case had a supervising120-second wall cap; none capped or failed,
and no fallback was needed. The16 and8 actual subprocess commands,
full node recipes, weights, coefficient maps, function coefficients,
noise draws and timing fields remain in the raw JSON/NPZ inventory.
Raw is regeneration-only in the unique `/tmp` paths, with byte/hash
identities in receipts; no cold-storage delivery is claimed.

Receipts: [Round1](../evidence/u1-round1.json),10731bytes, SHA256
`7e6b257ccc894260f54910334560d8b283d67dfe0c7d1f14c66a3501df7e436e`;
[Round2](../evidence/u1-round2.json),7391bytes, SHA256
`0498f2aa38adecbe61a5b9f6db908dcb9e454b3876c3491c2c55ebee74d7da52`.
All24 cases are retained, including error regressions and numerical-floor
cases. Independent supplementary checks are documented separately by
their checker; the required independent Claude audit is not replaced.

## Evidence and practical interpretation

All parity Gram residuals were at most4.52e−14. Their weighted design
condition numbers agreed with sqrt2 (anisotropic) and1 (equal orders).
Across all Round1 cases the largest reproduction infinity residual was
1.64e−11; Round2's largest was1.06e−13, both below the1e−9 gate.
The OLS covariance identity residual was at most1.27e−16.

| n | aniso M / N | aniso budget risk | globalQR budget risk | Leja budget risk | QR/aniso risk |
|---|---:|---:|---:|---:|---:|
|4|45 /35|35.4341|58.9628|213.281|1.664|
|8|225 /165|166.532|479.463|2404.736|2.879|
|12|637 /455|457.572|2157.275|12838.003|4.715|
|16|1377 /969|972.594|6001.249|34082.950|6.170|

Equal-order Haar budget risks are36.1515,167.1947,458.2116,973.2206.
They use54,250,686,1458 nodes respectively. Thus their per-observation
variance is smaller, but after equal-budget normalization they are
slightly worse than anisotropic Haar on this finite scope. That distinction
is preserved rather than credited entirely to taking more samples.

At n16 the anisotropic/globalQR/Leja Sobol RMS values are:

| Function | aniso Haar | globalQR | Leja |
|---|---:|---:|---:|
|Entire exponential|2.98e−15|7.30e−14|1.44e−13|
|Radial rational|0.0039633|0.0269541|0.0868073|
|Absolute ridge|0.0092628|0.0297284|0.0437267|
|Oscillatory cosine|1.3753e−5|9.1034e−5|1.2751e−4|

The entire-function row is below the1e−12 ratio floor and supports no
performance ratio. More consequentially, the rational function's sampled
maximum error at n16 is0.222254 for anisotropic Haar versus0.174501 for
QR, although its RMS is better. At n12 the corresponding maxima are
0.354675 versus0.285866. These are concrete exceptions to uniform maximum
error dominance. Every other function/case is in the compact receipts.

At n16 construction plus full diagnostic setup was0.1391seconds for
anisotropic Haar and11.5751seconds for globalQR, including the latter's
11.3869-second candidate selection. Dense four-RHS application was
0.744milliseconds versus0.522milliseconds; the extra points increase
application work. The anisotropic operator occupies10674504bytes and
the QR operator7511688bytes. No FFT/streaming implementation is claimed.
The parity formula itself forms its operator in0.897milliseconds; the
rest of measured setup includes basis construction and Gram diagnostics.
These one-environment timings are not hardware-independent complexity
comparisons or repeated benchmark confidence intervals.

For anisotropic OLS the risk reductions are5.50,4.07,3.09,2.47percent
at n4/8/12/16. Equal-order reductions are8.03,5.02,3.58,2.77percent.
At n16 anisotropic OLS operator formation took0.1422seconds versus
0.000897seconds for the Haar formula, and total diagnostic setup was
0.2527seconds versus0.1379seconds. Anisotropic n16 OLS budget risk is
948.532, while equal-order OLS is946.219. Its rational sampled maximum
error increases to0.224320, and oscillatory RMS increases to1.4262e−5
despite a lower sampled maximum. Known iid-noise optimality supplies a
specific optional solver, not a universal approximation improvement.

## Usable recipe and limits

For the measured cost/error/noise tradeoff, retain the explicit anisotropic
Haar moment solver as the simple default. Use the saved same-node OLS
when its small additional iid-noise gain justifies factorization setup.
The public producer functions `parity_nodes(n)`, `parity_fit(n,values)`
and `basis(query,n)` supply a direct reproducible recipe. Values follow
the returned canonical node order; predictions are `basis(query,n) @ c`.
No target-function evaluations or filesystem service are hidden by this API.

The separately executed developer API check used two explicit degree-two/
degree-one polynomials at n4/16 on both parity families,64 independent
uniform-cube query points (seed20261107), and input shapes M, Mx2, Mx1.
It returned N, Nx2, Nx1 coefficients and maximum prediction error9.33e−15.
Command in the same recorded Python/NumPy environment:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u1_api_check.py --out topics/padua-3d-20261106/evidence/u1-api.json --raw /tmp/padua-u1-38227202-20261107-api-0726
```

[API receipt](../evidence/u1-api.json) pins the2647-byte helper source
SHA256`f519e8388d0e7fe585048ce41068922a462e7f214364f8f3e9244948f3b3e478`
and the unchanged producer. Its retained raw source is regeneration-only.
This is developer verification of the public path, not a new counted
round, a general floating error theorem or an independent audit.

Only the two registered routes are completed. Other noise models,
uniform-measure weighting, optimized oversampling constants, higher
degrees and transform implementations remain possible future work,
requiring their own prospective objectives. No arbitrary round budget
or claim of whole-direction exhaustion is used to stop.

## History

2026-11-07, Codex developer, assigned Sol xhigh. Both runs executed after
root's prospective publication, with unchanged source and retained full
candidate outcomes. Root owns counted-round publication and LOG.
