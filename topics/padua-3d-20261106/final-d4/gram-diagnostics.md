# PD-T?padua-3d-20261106-codex-D4-gram — finite normalized-Gram diagnostics

ID kind: PD-T. Aliases: C3; normalized-kernel Gram; Riesz diagnostic.
Split from: none. Split into: none.

## Statement, definitions and status

Overall status: **MEASURED**. On the exact dyadic QR fallback point sets
retained in evidence/fd4-qr-nN-nodes.json, and the existing optimized n12
payload, the binary64 diagnostics below were actually computed. These
are finite measurements, with no asymptotic, optimality or universal
Riesz-basis conclusion.

Use the product Chebyshev orthonormal basis for the probability product
arcsine measure: phi_alpha=2^(s(alpha)/2)T_alpha, where s counts nonzero
coordinates and |alpha|<=n. V evaluates that basis; D=diag(VV^T), and
Ghat=D^(-1/2)VV^T D^(-1/2). Its diagonal is1 and trace=N; reported
lambda_min/max are floating eigvalsh values, not interval eigenbounds.

| n | N | QR lambda_min | QR lambda_max | Gram expression |
|---:|---:|---:|---:|---:|
|4|35|0.0396222875|2.41370561|47.033449|
|5|56|0.0409472105|2.16010403|61.925446|
|6|84|0.0199045832|2.65678888|120.413800|
|7|120|0.0218453191|2.4668572|147.296380|
|8|165|0.0101816981|2.54943506|256.628203|
|9|220|0.00812641615|2.34203123|349.368605|
|10|286|0.00521733272|2.44221302|509.657492|
|11|364|0.003795365|2.47062265|675.222968|
|12|455|0.00141957101|2.62020266|1259.516045|
|13|560|0.00179966913|2.42004914|1262.754673|
|14|680|0.00137972943|2.55143519|1615.419483|
|15|816|0.00118687995|2.45891544|1927.462558|
|16|969|0.000809119392|2.46648045|2558.079836|

Optimized n12/N455: lambda_min=0.0588056534536,
lambda_max=2.22498258586, Gram expression=206.911543.
The same-degree QR lambda_min is0.00141957101236.

## Depends on / exact diagnostic identity

With ell(x)=V^(-T)phi(x), one has
ell^T D ell=phi^T(V^T D^-1 V)^-1 phi. Therefore, if the exact smallest
eigenvalue gamma of Ghat is positive, Cauchy–Schwarz gives
Lambda<=sqrt(Kinf*sum_i 1/K(xi,xi)/gamma),
Kinf=sum_[|alpha|<=n]2^s(alpha), attained at a cube corner.
This is a routine finite-matrix identity from S3, not a new general
interpolation theorem. The displayed Gram expression substitutes measured
eigenvalues and kernels, so is itself MEASURED and is not the numerical
certificate. Whole-cube certificates are separate integer/rational checks.

## Checks, sources and scope

Preregistered in protocol.md; code fd4_certify.py and exact commands in the
producer receipts. OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1; no seed.
[QR receipt](../evidence/fd4-qr.json),
[optimized n12 receipt](../evidence/fd4-payload-m2.json).
Actual libraries: Python3.12.14, NumPy2.3.5,
SciPy1.17.0. Independent final checker is separate.
S3 is the topic precursor; IDEA027/058/466/611 and LIT489 are contextual
predecessors. No external theorem is imported to infer a rate from this
table. Only one regenerated QR baseline family plus one optimized degree
is available; the scout's two-optimizer polynomial-decay kill criterion
cannot be assessed from these data.

## Limitations / open items

The historical optimized coordinates at other degrees are unavailable in
this workspace; fd4-input-inventory.json records actual absent scratch
paths. QR is a fresh fallback, not an assertion that these were the best
historical sets. Missing optimized-family diagnostics remain uncomputed.
No optimization was reopened to replace them. Any uniform Riesz lower
bound, Riesz nonexistence or polynomial-decay law remains OPEN.

## History

2026-11-12, Codex assigned gpt-6.1-sol high, runtime identifier unexposed;
rules04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b. D4 round1 published9cf64ef
before execution; all13 QR degree diagnostics and n12 actually completed.
