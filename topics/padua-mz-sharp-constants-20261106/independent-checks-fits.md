# Supplementary independent K1/K3 fit replay

2026-11-06. Codex supplementary checker, requested gpt-6-astra high;
actual runtime model/effort metadata unexposed. Rules/source corpus:
`2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`. Scope: finite numerical
reproduction and protocol implementation, not a spectral proof, model
transfer, asymptotic validation, novelty or priority determination.
No novelty gate is needed for this replay-only scope.

**PASS for faithful reproduction.** Both fit processes actually executed
separately and their complete numerical `results` objects exactly match
the developer's receipts. No unresolved finding in this scope.

## Pinned inputs and execution

Input hashes were verified before both executions:

| Input | SHA-256 |
|---|---|
| code/S4_k1_fit.py | `6fcdcd12c7c27164e06cd186f6796a70d687ce90d439d9eb1a15d2dd1e9e0329` |
| code/S4_k3_fit.py | `c360fd5bf6f4494028a47e114f35cdc7b948de434aa55f8522794038722c9825` |
| S4-scan-proposal.json | `26a8dc6f0943fa76abfa9aecbd2d22574bfa94d13bc7453cd6fb9a8c409f9177` |
| /tmp/sharp-S4/raw-cc-scan.json | `7ce16e5c61fb82fe1fc4125bbd9570fdc7579db7aa139cd116b4807322f500f2` |

The raw receipt is55192 bytes, remains outside the repository, and is
the common frozen numerical input. The coordinator authorized these
replays after prediction registration; K1 protocol commit is e2652c3,
S1 prediction977c07a, and K3 protocol18992e1. Inspected both complete
scripts, the proposal and the dated gate records. No alternative fit
or window extension was run.

Actual commands, from `/workspace/sharp-work`:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/S4_k1_fit.py --raw /tmp/sharp-S4/raw-cc-scan.json --output topics/padua-mz-sharp-constants-20261106/evidence/check-fits-k1.json > /tmp/check-fits-k1.stdout
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/S4_k3_fit.py --raw /tmp/sharp-S4/raw-cc-scan.json --output topics/padua-mz-sharp-constants-20261106/evidence/check-fits-k3.json > /tmp/check-fits-k3.stdout
```

Both exited0. Python3.12.14, NumPy2.3.5; complete versions, timestamps,
platform, commands and data hashes are in the separate receipts. The
environment thread variables above were explicitly set for both runs.
No random seed is used in the deterministic fits; raw eigensolver
provenance remains in its pinned receipt.

## Reconstructed implementation and results

K1 uses physical N for each parity, the seven-point j8–14 window and
disjoint six-point j15–20 window, and unweighted SVD columns
[1,log(log N)/log N,1/log N] against (log N)²lambda_min. The comparison
is |c_A−c_B|/max(|c_A|,|c_B|), with positive intercepts required.
The implementation matches the registered definition.

| Parity | Final-window intercept | Window disagreement | Difference from pi⁴/8 |
|---|---:|---:|---:|
| even | 13.061135993252737 | 1.1849378711% | 7.2683122662% |
| odd | 13.061132673210166 | 1.1845264676% | 7.2682849994% |

Thus K1 reproduces **PASS**, and K2 reproduces operational
**KILL_MODEL** under its5% threshold. The K1 design condition numbers
are about4396–4399 and14004 in the two windows. SVD solves these
specified finite least-squares problems, but neither their intercepts
nor their agreement prove an asymptotic constant or exclude systematic
fit bias. The killed equality prediction and the separately checked
one-sided analytic bound remain distinct.

K3 uses lambda_max−1 and columns [1,z,z log(N/Nref)], z=(Nref/N)²,
scaled to unit Euclidean norm before unweighted SVD. The registered
rank, window residual, intercept agreement and final parity checks
are implemented as stated; raw completion and spectral guards are
checked. The numerical fit reproduces **USABLE**.

| Parity | Final-window fitted limit | Maximum final-window residual |
|---|---:|---:|
| even | 1.0044369722946567 | 3.25112e-11 |
| odd | 1.0044369722985076 | 3.04196e-11 |

Final parity difference is3.850919583214818e-12. Window differences
are below1.15e-9. These meet the recorded thresholds. The fit script
does not itself perform the S2 model-norm comparison. A finite model
Galerkin value can supply a measured proxy comparison, but without a
certified infinite tail it cannot certify the proposed full model norm.

## Output identities and limits

| Independent receipt | Bytes | SHA-256 |
|---|---:|---|
| [check-fits-k1.json](evidence/check-fits-k1.json) | 6844 | `bb07316ae5bec7c8023e50da372670aba76eafa0a8875535ce11e2175ad73d96` |
| [check-fits-k3.json](evidence/check-fits-k3.json) | 7900 | `e3a8d76779994d2d48969724e2e2c94817376235ff8e76f3e027d105def97923` |

The developer comparison receipts had hashes
`9e9f1681a44dd28aa23124b9bc1a6f6ab0c5da2779d42915457d9082607a95cb`
(K1) and `fcf497a123aa0f9f8a752f187139f0bcf60b232c7ac0e23c30bcb0f7c04cda81`
(K3). Comparison tested their numerical result objects, not timestamps
or output paths. These independently executed replays reuse the same
frozen fitting algorithms and raw measurements. All conclusions here
are **MEASURED**; required Claude audit remains separate.
