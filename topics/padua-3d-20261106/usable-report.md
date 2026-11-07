# Usable construction campaign — progress checkpoint

2026-11-07; rules/input38227202bc6908d5a5a874950145761a8ca4312f.
ACauthorized U1/U2up to10rounds each andU3up to20.
[Campaign](usable-campaign.md), [gate](usable-gate.md).
No final IDs, ranges, shared-registry changes or merge.

Completed development at this checkpoint: U1two routes, U2one pilot.
U3and further direct-update work remain active. Required Claude audit
still includes the preserved handoff09 scope; no audit is fabricated.

## Extra-point reconstruction: a usable known recipe

[U1](usable1.md) supplies explicit nodes/weights, a direct moment solver
and a tested Python API. At degrees4/8/12/16 it uses45/225/637/1377
points for polynomial dimensions35/165/455/969. All24prescribed cases
pass. Exact all-degree construction/Gram and elementary noise/OLS algebra
are separate PROVED records; actual approximation/cost comparisons are
MEASURED in [the operational record](theory/u1-operational-comparison.md).

At degree16, equal-total-budget independent-noise risk coefficient is
972.594versusQR6001.249 (6.170times smaller), accounting for the extra
measurements. The rational-function empirical RMS improves, but its
sampled maximum error is0.222254versusQR0.174501. Thus average/noise
robustness does not guarantee a better worst-case error for every function.
The known OLS alternative lowers iid-noise risk2.47–8.03percent, with
more factorization setup and mixed deterministic-error changes.

The direct API reproduces explicit low-degree polynomials for vector,
single-column and multiple-column values, maximum observed error9.33e−15.
No FFT or uniform-volume error guarantee is claimed. Full nodes/weights,
coefficients and costs are regenerable from committed source.

## Direct optimization: finite gain and a diagnosed update failure

[U2](usable2.md) minimizes a smooth training approximation to Lebesgue
amplification jointly over all coordinates, distinct from one-column
determinant ascent. At degree4 its fresh refined lower sample decreases
11.140116to5.434721 in about1.03CPU seconds total construction, including
QR/localdet setup. A nonsmooth function's RMS worsens despite that gain.
Every assessed set has a positive exact dyadic-node modular rank witness,
but no generic continuous maximum or all-degree quality theorem follows.

At n2/6/8 the first projected optimizer trial collides and gets a singular
zero-gradient penalty, then returns to the start. Apparent convergence
is not stationarity. The frozen rule fails its n6/8five-percent gate;
its n10/12holdout is unrun. A separate prospectively registered bounded
projected-gradient/Neumann-guard update is next, using the same known
pilot assessment and an explicitly still-unseen higher-degree holdout.
The failed source/receipts and exact diagnosed traces are preserved.

## Remaining work at this checkpoint

U3's structural, coherent folded and mixed-union routes are executing
under their published protocol; no round is counted prematurely.
Independent checkers report actual U1/U2replays without discrepancy;
their final fresh-assessment/source-frozen receipts are still being
integrated and do not replace the required Claude audit. Raw output is
unique/tmp regeneration-only with identities, not claimed archived.
