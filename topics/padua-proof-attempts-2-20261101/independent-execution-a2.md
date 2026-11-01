# Supplementary independent execution of the A2 regressions

Date: 2026-11-01. Executor: Codex subagent `/root/input_manifest`, separately
assigned after developer execution. Role: independent executor, not developer or
Claude auditor. Requested model/effort for mechanical execution: gpt-6.1-sol
medium; no separate serving-model receipt is exposed by the runtime.
Rules read at `a09d910ae7d5526b1e216066421a0bee7fc20da4`.

Read both scripts and the complete current supporting comparison theory -04 and
logarithmic-coefficient theory -03 before executing. These runs use the same
developer code in fresh processes; they are an actual independent rerun, not an
independently implemented mathematical checker. No source file or producer
output was changed. No Git mutation, manifest edit, or shared-checks edit was
performed.

## Exact commands actually executed

Working directory: `/workspace/padua_research`.

```sh
python topics/padua-proof-attempts-2-20261101/code/a2_exact_check.py > topics/padua-proof-attempts-2-20261101/outputs/a2_exact_independent.json
python topics/padua-proof-attempts-2-20261101/code/a2_sanity.py > topics/padua-proof-attempts-2-20261101/outputs/a2_sanity_independent.json
```

Both exited 0. Input source files were SHA-256 checked immediately before the
runs. The exact script hash equals the developer-assigned pin. Each script also
records its own source hash in its output.

| Source | SHA-256 |
|---|---|
| `code/a2_exact_check.py` | `94438117d4510b248beaac3e22afb23c159c21d107e17d300206b73751be4101` |
| `code/a2_sanity.py` | `8ca20d9690664430fe596ebdda881183034ef6e1ea81ca3bd841d9c2bfbb0649` |

Environment: Python 3.12.14, SymPy 1.14.0, NumPy 2.3.5; NumPy longdouble reports
64 mantissa/significand bits through `nmant+1`. No random seed applies: both
scripts are deterministic and use no random generator.

## Observed results and output identity

The exact regression uses rational cyclotomic fields `QQ(zeta)` with orders
8, 24, 48, 80, 120 and 168 for n=1,...,6, with respective field degrees
4, 8, 16, 32, 32 and 48. It checks 3, 6, 10, 15, 21 and 28 odd-board kernel
terms, totaling 83 terms. All six coincident-endpoint checks, positive-corner
sum identities, same-mesh square identities, and `all_equalities_exact` flags
returned true. This is finite supplementary regression; it does not establish
the all-degree deformation bound or asymptotic remainder.

The separate longdouble sanity run evaluates 67 degrees: n=2,...,64 and
128, 256, 512, 1024. Across that finite set, the largest observed absolute
corner-minus-square value is 1, and the largest observed absolute remainder
after the leading and proposed b terms is approximately 1.9558125216092106.
These observations are **MEASURED**, with no interval enclosure or proof status.

After both executions, parsed JSON equality and byte identity were checked
against the developer outputs. Both are exactly equal, including environment
and source-identity fields.

| Independently produced output | Bytes | SHA-256 | Producer comparison |
|---|---:|---|---|
| `outputs/a2_exact_independent.json` | 2067 | `91db451c362d59c8bd1d155b10e0e5da275d62cced0e165b82cff7242fcc3d0e` | byte-identical to `outputs/a2_exact_check.json` |
| `outputs/a2_sanity_independent.json` | 19691 | `caf52a027f271f0f47ab07ed4289ca2115618aa2970290d2d10d89b90da59b4f` | byte-identical to `outputs/a2_sanity.json` |

## Limits

This supplies the requested independent execution receipt for the supplementary
exact and measured computations. It is neither a reconstruction of the full
analytic proof nor the required Claude audit. The exact regression has finite
n≤6 coverage and relies on SymPy's exact number-field implementation. The sanity
run uses floating arithmetic and cannot certify inequalities, limits, a bounded
remainder, or the value of an asymptotic coefficient. The analytic proof must be
checked as written independently of these diagnostics.
