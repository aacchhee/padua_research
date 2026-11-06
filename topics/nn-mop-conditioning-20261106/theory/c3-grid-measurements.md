# PD-T?nn-mop-cond-codex-31 — native full integer-grid screen

ID kind: PD-T. Aliases: C3 A-LU comparison; expanded C4 excess screen.
Split from / into: none. Overall status: **MEASURED**.

## Statement and definitions

On the recorded platform, all 58 frozen family/size inputs, both PD-T290
families at every integer N=4,...,32, completed for A-LU, A-QR, B-nodeqr and
C4 (232 solver cases). E is the maximum over fields a1,a2,b1,b2 of the sup
absolute error divided by the exact-reference field sup, structural zeros
included. The denominator is the **seven-significant-digit committed
PD-T434 NN/mixed table**, with u=2^-53. Ratios inherit that rounding; they
are neither derivative enclosures nor a theorem constant.

Inputs are exact rational PD-T290 nodes z=2k/(N-1)-1 and weights, converted
by the unchanged solvers to binary64. Positive common-support weights and
full normal triangles are inherited from the predecessor's frozen family
records. The 220-dps C4 graph supplies the reference; 140/220 agreement
is at most 1.411322602e-99. Both N4 exact Fraction defining-moment checks
pass, with errors below 3.59e-217. Higher-N precision agreement is not an
independent reference algorithm or rigorous interval certificate.

## Measured results

Completion of all232 solves and every table maximum below are observations
on the developer stack only. In audit-01's Python3.13.18/NumPy2.5.3 rerun,
Krawtchouk N32 A-LU broke down (singular matrix), so231/232 completed.
Its Krawtchouk A-LU full-grid maximum was1.609547 atN21 and the
kappa*u<=1 maximum was.809084 atN17, versus1.132694/.809315 here.
All C4 values and the Hahn A-LU cutoff maximum reproduced. These are
attributed audit observations, not a new developer rerun or all-platform
completion claim. See [audit-01 section4](../audit-01.md#4-c3-weak-stability-open-target-confirmed-grid-accepted-as-measured).


Each pair below is `maximum E/(kappa*u) (N attaining it)` over the stated
subset. A cutoff is a diagnostic subset, not a proved finite-u Taylor
radius; even kappa*u<1 alone does not control the remainder.

| Method/family | All N4-32 | kappa*u<=1 | kappa*u<=1e-4 |
|---|---:|---:|---:|
| A-LU Krawtchouk | 1.132694 (19) | .809315 (17) | .293662 (9) |
| A-LU Hahn | .469316 (7) | .469316 (7) | .469316 (7) |
| A-QR Krawtchouk | 4.481565 (18) | 4.481565 (18) | 1.257107 (14) |
| A-QR Hahn | .462204 (7) | .462204 (7) | .462204 (7) |
| B-nodeqr Krawtchouk | .878717 (4) | .878717 (4) | .878717 (4) |
| B-nodeqr Hahn | 11.861181 (19) | .396261 (11) | .396261 (11) |
| C4 Krawtchouk | 30837.9007 (20) | 49.903739 (18) | 17.915273 (13) |
| C4 Hahn | 40533.1034 (14) | 40533.1034 (14) | 556.241587 (11) |

The kappa*u<=1 subsets have 15 Krawtchouk and 13 Hahn sizes; the <=1e-4
subsets have 11 and 9. A-LU's full-grid Krawtchouk maximum occurs where
kappa*u=4.950262>1 and E=5.607132. B-nodeqr's Hahn maximum likewise occurs
where kappa*u=912.848352. Tiny ratios at still larger kappa*u do not
indicate an accurate computation. A-LU first has E>=1 at Krawtchouk N19
and Hahn N18; its LU ill-conditioning warnings begin at N17 in both
families, totaling 2378 and 1625 warnings over their 29 size runs. These
count individual mixed-system solves, not failed whole-array runs.

The all-integer grid exposes C4 spikes missed by the predecessor six-size
error grid. At Hahn N14, kappa*u=.004877224180, E=197.6890321 and the ratio
is 40533.1034. At Hahn N11 the ratio is 556.241587 with kappa*u=3.4527e-6.
These are finite algorithmic excess-error observations in the declared
metric. They do **not** prove an asymptotic roundoff lower bound, activation
of a worst-case rounding direction, or impossibility of a larger-C
weak-stability theorem. No C3 theorem is claimed; M3 remains unactivated.

## Dependencies and provenance

PD-T286/289 define F and the exact reconstruction. PD-T290 fixes inputs and
E; PD-T432 fixes the input model; PD-T434 supplies the rounded condition
table; PD-T440 supplies the existing native algorithms. No primary-source
algorithm is newly implemented. QR/nodeqr are the unchanged predecessor
variants, with no new algorithmic novelty claim.

Producer is `code/c3_grid.py`, 10097 bytes, SHA256
`c14b7c67418a5350000083169ec47666d2b01a22008be67d73ec509afed92638`.
Imported `native_mixed.py` SHA256
`3aef4afb6ce48c71d69f6337ce20b4c700f98de24e9465def864881a01f0c506`;
baseline SHA256
`9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8`;
N4 exact-checker SHA256
`13d59af82304a712d792c6e2f96c76f42ec732575dcfa3452a92295071c011b3`.
The parsed table-value hash, input identities and full reference/output
digests are recorded in the compact receipt and raw payload.

Platform: Linux 6.18.57 x86_64 glibc2.41; Python3.12.14; NumPy2.3.5;
SciPy1.17.0; mpmath1.3.0; binary64 mantissa53 bits;
OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. BLAS build metadata is in
raw.numpy_build_config. Values depend on the numerical stack; no timing
comparison or all-platform agreement is claimed. The measured producer
elapsed time was 14.034987415 seconds. No randomization.

## Checks actually executed and storage

From the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/nn-mop-conditioning-20261106/code/c3_grid.py --output topics/nn-mop-conditioning-20261106/c3-grid-summary.json --raw /tmp/nn-mop-c3-grid-raw.json
```

The coding worker checked all 232 field maxima and ratios. The distinct
C3 mathematical worker separately executed the same producer with output
`/tmp/c3-replay-summary.json` and raw `/tmp/c3-replay-raw.json`, and compared
all 58 compact rows and the complete raw scientific payload: exact match.
This is an executed supplementary replay of the same code, not independent
algorithm verification or the required Claude audit.

Compact `c3-grid-summary.json`: 11329 bytes; SHA256
`175c9d3abac0d471ffc1b33c24431eab5105121891c6e16bfa1060408368480d`.
Raw `/tmp/nn-mop-c3-grid-raw.json`: 5835364 bytes; SHA256
`3da04b46dcc7d621543544235adf8517b26f316f8b303e4dc77fc5027fb873f6`.
The separate replay raw has the identical hash. Raw coefficients are JSON
round-trip representations of the actual binary64 outputs; references
are identified by digest rather than stored wholesale. The raw file is
temporary, regenerable and not committed; no archival delivery is claimed.

## Scope, open items and history

The distinct forward weak-stability target PD-T?nn-mop-cond-codex-C3-02
remains OPEN in
[c3-weak-stability-open.md](c3-weak-stability-open.md). Measurements do not
supply its constant C_N, precision radius or remainder bound. M2/M4 and
the external IEP-MOP comparison are outside this record; no literature
normalization metric is substituted for monic NN fields.

2026-11-06. Rules/source `b4a04981d42c7cd872957facf5e3995e4096ca67`.
Code and primary run: Codex gpt-6.1-sol medium; mathematics and separate
replay: Codex gpt-6.1-sol xhigh. The initial six-size pilot was superseded
by the complete integer grid without changing the algorithm or thresholds.
