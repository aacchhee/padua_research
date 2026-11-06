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

## 2026-11-06 — focused repository-input update check

After the executions above, the developer preserved the original scripts
as S4_k1_fit_original.py and S4_k3_fit_original.py and added a shared
loader for compact repository evidence. This was treated as a material
code/input change and checked separately. The historical executions and
receipts above remain unchanged.

Inspected the complete generator, loader and K3 comparison code, and
reviewed both fit-script diffs. The fitting arithmetic and thresholds
are unchanged; the diffs replace input loading and record the additional
input provenance. The loader accepts only the pinned full or essential
receipt hash, restores exactly the required columns, and checks all42
rows' completion, positivity, ordering, residual and constraint guards.

Executed the deterministic generator in `--check` mode against the
original frozen raw file. It confirmed byte-for-byte equality of the
7163-byte,42-row essential receipt, hash
`7e18253a25fb8ab3b78389ef444c8014313b0d4231b6fb0c2467aaa062edacfb`.
Then separately ran both updated fits using only that repository-local
input. Both complete numerical result objects exactly equal the earlier
independent raw-input outputs. This focused update check **PASSES**.

Updated executed code hashes:

| File | SHA-256 |
|---|---|
| S4_essential.py | `d2ef9c457c8cf8b958a175d95cc235fe92b02ff0ac070eefdff59abbef61fcca` |
| S4_fit_inputs.py | `ba263a1e6cc377ab3ebd9a1e8fbc0c662ccb874ea04ce4e80dfdaf9223ea6545` |
| S4_k1_fit.py | `00d9567a6ac3230c0d06c1a6a32f684d89fc386eb88511c7b62acfcbd5c846d8` |
| S4_k3_fit.py | `a95c4d9b18a80de86c5e44563d37f6e1f9da3b16c573b6fa84ea8955e3df64ad` |
| S4_k3_compare.py | `8636ff80576715094c9e0a76b6409883717c5459116e8f1970912a282aac346f` |

Exact commands, again from `/workspace/sharp-work`:

```bash
python topics/padua-mz-sharp-constants-20261106/code/S4_essential.py --raw /tmp/sharp-S4/raw-cc-scan.json --output topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --check
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/S4_k1_fit.py --raw topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --output /tmp/check-fits-k1-essential.json > /tmp/check-fits-k1-essential.stdout
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/S4_k3_fit.py --raw topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --output /tmp/check-fits-k3-essential.json > /tmp/check-fits-k3-essential.stdout
python topics/padua-mz-sharp-constants-20261106/code/S4_k3_compare.py --model topics/padua-mz-sharp-constants-20261106/evidence/check-S2-model-replay.json --fit /tmp/check-fits-k3-essential.json --output topics/padua-mz-sharp-constants-20261106/evidence/check-fits-k3-comparison.json
```

All four commands exited0. The same Python/NumPy environment applies.
The [compact portability receipt](evidence/check-fits-portability.json)
records exact updated commands, source/input hashes, timestamps,
environment, temporary output hashes and the successful full-results
comparisons. It is4057 bytes, SHA-256
`880a94bdbac91efae9b10f0aaa0205635cffd1b784d0d255bac0a2e7f5eb0943`.
Duplicated full fit outputs remain local and are regenerable from the
repository-only input by the commands above.

The separately executed [K3 comparison](evidence/check-fits-k3-comparison.json)
gives operational **MEASURED PASS**: absolute differences5.3429989322e-8
and5.3433840241e-8 from the finite J512 model estimate, below1e-3.
Its receipt is1393 bytes, SHA-256
`152871f67644a8271fc3d33bd131811597b1416f6a1ec0cba09a841955f984ff`.
This comparison has no certified infinite-model-tail bound; it does
not establish that the full model norm differs from either fit by
less than the threshold. The operational and mathematical statements
must remain separate.
