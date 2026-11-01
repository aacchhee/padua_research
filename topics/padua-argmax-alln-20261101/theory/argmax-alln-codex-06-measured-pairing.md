# PD-T?argmax-alln-codex-06 — measured pairing screens

ID kind: PD-T (provisional).
Aliases: IDEA03 screen; O-R diamond ordering; E-C centreward edge ordering.
Split from: none. Split into: none.

## Statement

Within the finite float64 optimization scope below, the unique-nearest-corner diamond-supremum ordering O-R has measured reversals. The amended centreward vertical-edge comparison E-C has no measured reversal in 76 eligible comparisons at n=7,12,24,50. Definitions and the preserved original IDEA03 wording are in [the attempt](../attempts/P3-P5-and-pairing.md).

## Assumptions and definitions

Mesh coordinates are (nθ/π,(n+1)φ/π), antinode diamonds have radius1 in mesh ℓ1 norm, and rhombus neighbor centers differ by (±1,±1). O-R compares numerical maxima on whole closed diamonds (clipped at the square boundary) as distance from the same unique nearest non-node corner increases. E-C uses complementary-ordinate vertical-edge intervals [k−1,k+1], excludes intervals meeting endpoint corners, and compares step2 neighbors toward (n+1)/2. The distinct exact certified-list O-Lt witness has its own [negative record](argmax-alln-codex-N01-pairing-order-obstruction.md).

## Status by part

Overall status: **MEASURED**.

| Claim | Status | Evidence |
|---|---|---|
| O-R numerical reversals at n4,7,12 | MEASURED | Float64 multistart search on diamonds |
| No E-C numerical reversals over the tested edges/degrees | MEASURED | 76 comparisons, finite grid plus bounded scalar optimization |

Candidate disposition: **REJECTED: failed** as a universal O-R ordering in this measured screen. E-C remains active and OPEN as an exact theorem. Neither conclusion rejects ambiguous IDEA03 in every interpretation or PD-T099.

## Depends on and checks

The existing corrected-kernel evaluator (`tests_common.py`) is validated against the coefficient-matrix evaluator at n=2,3,4,8,16; largest discrepancy 7.78×10^−15. This is agreement of float64 implementations, not an error enclosure.

Executed command from repository root:

```sh
OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/part3/pairing_screens.py --degrees 4 7 12 24 50 --output topics/padua-argmax-alln-20261101/outputs/part3/pairing_screens.json
```

Source snapshot `328be35e55143013047ec03a70e9906e82b95353`; output SHA-256 `f602acf48d82b91a26db422164836a4529828d027488f9f1b20e58497c8a93c2`. Last full run reported54.79 seconds. Independent numerical replay has not been run.

## Measured evidence

| n | O-R comparisons | Reversals >10^−6 | E-C comparisons | Reversals below −10^−6 |
|---|---:|---:|---:|---:|
| 4 | 10 | 6 | 0 | 0 |
| 7 | 42 | 16 | 2 | 0 |
| 12 | 130 | 60 | 8 | 0 |
| 24 | not run | not run | 20 | 0 |
| 50 | not run | not run | 46 | 0 |

For n4, O-R has M_(3,0)−M_(4,1)≈0.505255 away from corner (4,5), using numerical maxima3.598293 and3.093038. This crosses a physical edge stratum, so it is a particularly broad proposed pairing.

There are also interior-center failures: at n7, M_(3,2)−M_(4,1)≈0.226682, and M_(4,3)−M_(5,2)≈0.103182. All four indicated centers are interior; the optimizer can still land on an artificial diamond boundary, as allowed by M's definition.

For E-C the smallest measured target-minus-source gains were0.380036 (n7),0.063693 (n12),0.017229 (n24),0.003562 (n50). A positive finite sample does not establish a uniform all-degree margin, and the decreasing adjacent gains matter for exact comparison accuracy.

## Method and limits

Each diamond uses a 5×5 grid in its rhombus coordinates and constrained Nelder–Mead searches from the three best starts; at most180 iterations. Physical-square violations incur a penalty. Returned maxima are numerical lower bounds only, and a missed source maximum can manufacture a reversal. Thus these O-R failures are screening evidence, not certified inequalities or a proof of universal refutation. A 65-point grid and local bounded scalar optimization finds each edge-cell candidate. It does not certify all stationary points or rule out sign-cell creases.

No numerical diamond search was run at n24 or50. Zero-length comparison arrays there mean **not run**, not no violations. The n4 certified-list test with unique nearest corner has no eligible comparisons and therefore supplies no test of O-R.

## Sources and open items

No 1-D proof transferred: original Brutman/Günttner/midpoint sources unread; literature INDEX only. Next E-C task: exact whole-edge-cell comparisons at n7, with a common-phase inequality tested separately. Next O-R task, only if useful: certify one proposed reversal with an upper bound on its entire source diamond including artificial boundaries.

## History

2026-11-01, Codex, assigned gpt-6.1-sol xhigh; actual runtime metadata not independently exposed. Separate operationalizations and float kill threshold recorded in the attempt before this run. No original criterion overwritten.
