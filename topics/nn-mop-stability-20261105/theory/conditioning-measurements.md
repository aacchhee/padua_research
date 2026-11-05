# PD-T?nn-mop-stability-codex-D1-03 — sampled NN and monic step-line conditioning

ID kind: PD-T. Aliases: analytic AD table; D1 round 1 grid.
Split from: D1 sharp all-N growth target (OPEN). Split into: none.

## Statement

At N in {4,8,12,16,24,32,48,64}, the full analytic 3N-column Jacobian gives
the following floating evaluations of the induced condition number. Both source
families use the exact rational PD-T290 inputs. No finite-difference estimate or
directional-only lower bound replaces the induced norm.

## Definitions and assumptions

Definitions, normality domain and input/output norms: [local theorem](conditioning-local.md).
NN E is the baseline fieldwise relative sup metric. SL denotes the monic
alternating first-e1 four-term path, with separate sup scales for beta/gamma/delta.
It is not assumed to match a diagonally scaled literature output. cw-input means
componentwise input and fieldwise normwise output. Full componentwise output is
infinite on the symmetric Krawtchouk family and is not tabulated.

## Status by part

Overall status: MEASURED. All observations below are bounded high-precision
floating measurements. Analytic derivative correctness has a separate written
PROVED theorem; floating evaluation is not an outward enclosure. Independent
exact small-N verification is tracked by the coordinator.

## Depends on

PD-T286/288/289, PD-T290 input definitions, conditioning-local.md; mpmath1.3.0.

## Proof or evidence

### krawtchouk

| N | NN mixed | NN cw-input | NN block-normwise | SL mixed | log10 NN mixed |
|---|---|---|---|---|---|
| 4 | 165.04 | 144.57 | 269.51 | 218.12222222 | 2.2175892 |
| 8 | 959279.26853 | 684816.48229 | 2214975.0058 | 732977.58711 | 5.9819451 |
| 12 | 6629393752.8 | 3988112679.6 | 21480931322.0 | 3333356683.3 | 9.8214738 |
| 16 | 5.0783994643e+13 | 2.651334456e+13 | 2.4906975944e+14 | 1.9834419159e+13 | 13.705727 |
| 24 | 3.4661477987e+21 | 1.444802072e+21 | 5.5792488026e+22 | 9.8636407327e+20 | 21.539847 |
| 32 | 2.6165049124e+29 | 9.1575271267e+28 | 1.7882208478e+31 | 7.2015061732e+28 | 29.417722 |
| 48 | 1.7072981739e+45 | 4.5972311117e+44 | 2.8034042077e+48 | 4.5477821905e+44 | 45.232309 |
| 64 | 1.215787923e+61 | 2.6966767947e+60 | 5.6228710986e+65 | 3.1867087358e+60 | 61.084858 |

Maximum relative 180/260-dps difference over the six tabulated model/target
kappas at each N is at most 1.76327e-115. This is a precision-convergence
measurement, not a rigorous error bar. N4 independently formulated AD moments
versus AD-C4 have max absolute coefficient difference 4.64673e-259
and max absolute Jacobian-entry difference 1.96743e-256.

### hahn

| N | NN mixed | NN cw-input | NN block-normwise | SL mixed | log10 NN mixed |
|---|---|---|---|---|---|
| 4 | 1573.9159965 | 1492.3725568 | 1794.7946738 | 1582.8023388 | 3.1969815 |
| 8 | 23385441.019 | 21449047.796 | 26433980.648 | 9676671.9441 | 7.3689456 |
| 12 | 3.5007483313e+11 | 3.1779738823e+11 | 3.919626134e+11 | 1.0800781975e+11 | 11.544161 |
| 16 | 5.5804917169e+15 | 5.0461188102e+15 | 6.204882901e+15 | 1.4769848817e+15 | 15.746672 |
| 24 | 1.6210862397e+24 | 1.4621716544e+24 | 1.7861817688e+24 | 3.6479475782e+23 | 24.209806 |
| 32 | 5.2619101692e+32 | 4.7434075402e+32 | 5.7700356667e+32 | 1.0870478209e+32 | 32.721143 |
| 48 | 6.6192033177e+49 | 5.966467089e+49 | 7.2256513176e+49 | 1.258818203e+49 | 49.820806 |
| 64 | 9.5953074996e+66 | 8.6499568579e+66 | 1.0451276522e+67 | 1.7485754524e+66 | 66.982059 |

Maximum relative 180/260-dps difference over the six tabulated model/target
kappas at each N is at most 1.28417e-93. This is a precision-convergence
measurement, not a rigorous error bar. N4 independently formulated AD moments
versus AD-C4 have max absolute coefficient difference 1.22682e-257
and max absolute Jacobian-entry difference 1.52835e-255.

### G3 approaching proportionality, N8 only

The plan preregistered kappa proportional to 1/min interior |d|. The product
below would be constant under literal proportionality. Krawtchouk products
increase by over seven orders over these gaps, so a single inverse-divisor
factor does not explain this bounded sweep. Hahn products change strongly at
the larger gaps and much less at the smaller gaps. No asymptotic exponent or
limiting constant is inferred from either finite sample.

| Family | Parameter gap | NN mixed | min interior abs d | Product |
|---|---|---|---|---|
| krawtchouk | 1/10 | 959279.2685 | 0.0285714286 | 27407.9791 |
| krawtchouk | 1/20 | 88649401.83 | 0.0142857143 | 1266420.026 |
| krawtchouk | 1/50 | 4.202238144e+10 | 0.00571428571 | 240127894.0 |
| krawtchouk | 1/100 | 4.884216405e+12 | 0.00285714286 | 1.395490401e+10 |
| krawtchouk | 1/200 | 5.94154319e+14 | 0.00142857143 | 8.487918843e+11 |
| hahn | 1/2 | 23385441.02 | 0.00371184371 | 86803.1022 |
| hahn | 1/4 | 11613259.68 | 0.00187875275 | 21818.4435 |
| hahn | 1/10 | 10483065.21 | 0.000757050028 | 7936.204816 |
| hahn | 1/20 | 18773440.13 | 0.000379455523 | 7123.685547 |
| hahn | 1/40 | 36134879.17 | 0.000189960916 | 6864.214759 |

The Krawtchouk gap is p2−2/5; the Hahn gap is beta2−1, gamma=1.
For two disjoint-support measures, each marginal has fewer than N support
points and is singular at a degree <=N on its axis. Therefore that Angelesco
case does not satisfy this full common-support normal triangle domain; a
different domain and metric must be specified before an honest comparison.

## Checks and reproducible commands

From the pinned snapshot root, run each family command at dps180 and260:

```bash
python3 topics/nn-mop-stability-20261105/code/conditioning.py --family krawtchouk --sizes 4 8 12 16 24 32 48 64 --dps 260 --check
python3 topics/nn-mop-stability-20261105/code/conditioning.py --family hahn --sizes 4 8 12 16 24 32 48 64 --dps 260 --check
python3 topics/nn-mop-stability-20261105/code/conditioning_sweep.py --N 8 --family krawtchouk --dps 260
python3 topics/nn-mop-stability-20261105/code/conditioning_sweep.py --N 8 --family hahn --gaps 1/2 1/4 1/10 1/20 1/40 --dps 260
```

Raw regenerable outputs remain in /tmp pending coordinator evidence handling.
Early180-dps grid outputs include a removed misleading near-zero-output ratio
diagnostic. Its removal changed no derivative or table values; final-code180-dps
replays completed with exit0 and reproduce all displayed norms, with final matching metadata. Use the260-dps receipts
for the displayed values. Code and pinned baseline hashes:

- `topics/nn-mop-stability-20261105/code/conditioning.py`: `11c4b49be8541697e74d383b908db47b42480e11c60f92c35821340eacea929c`.
- `topics/nn-mop-stability-20261105/code/conditioning_sweep.py`: `c5f38ca894571205bb9cbe9d2c7c194b2eb8441e73d9dd6e257049339ab59a5b`.
- `topics/nn-mop-iep-20261103/code/c4_float_baseline.py`: `9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8`.

## Sources

No new primary-source claim. Family formulas are inherited from PD-T290 and
the pinned baseline; no classical closed-form NN formula is used.

## Scope

Worst-case first-order sensitivity does not require an algorithm to make this
error. A heuristic digits-lost allowance is log10(kappa), with achievable
relative rounding scale kappa*u; it is uninformative once kappa*u exceeds one.
The gate convention u must be stated: unit roundoff is2^-53, whereas the old
baseline calls epsilon=2^-52. The factor two changes ratios but no table value.

## Open items

Every intervening integer N in4..64, independent larger-N checks, certified
outward derivative enclosures, a sharp growth theorem and fixed-mass norms.
The coordinator requested a separate round2 for the full integer sweep.

## History

2026-11-05 D1 developer, gpt-6.1-sol xhigh, pinned rules/input SHA
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. Python3.12.14; mpmath1.3.0.
Plan was written before any execution. This record freezes round1 only.
