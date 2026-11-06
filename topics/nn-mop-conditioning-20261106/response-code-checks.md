# Audit-01 response: code and replay checks

Rules/source input: `3d5b29d7aa8c1274793139d7040695035e1bda22`.
Codex technical response worker; assigned model gpt-6.1-sol, medium.
No novelty development: this scope repairs code/receipt hygiene and checks
existing finite outputs. The mathematical claims and dependencies are unchanged.

`code/c4_compare.py` now reads C3 status and reason from
`case['measurement'][method]`, where the producer actually stores them.
A native breakdown has no top-level coefficient entry. It is recorded with
its reason before coefficient access. Missing methods, missing coefficients,
and invalid coefficient data receive explicit failure statuses. CSV metrics
for these failures are blank; failures are included in the comparison receipt.
Healthy methods retain the original calculation and output schema.

Run from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 python3 topics/nn-mop-conditioning-20261106/code/response_code_checks.py
```

The retained [JSON record](response-code-checks.json) gives exact commands,
platform versions, input/code hashes, and generated raw output pins. The check
runs the complete 116-case healthy comparison, requiring exact equality of
all scientific case data and 58 binary64 input identities with the original
raw output. It also requires every byte of all 14 generated CSV tables to
match the authenticated source tables. Runtime and producer file-hash
metadata are expected to change; these are excluded from scientific equality.
Executed on Python 3.12.14, NumPy 2.3.5, mpmath 1.3.0 and SymPy 1.14.0:
all checks passed. The original tables are read only, and generated replay outputs stay under
`/tmp/nn-mop-response-code-checks`.

A second comparison uses one real shared-normalized input and synthetic
native data following the actual C3 raw structure. It tests a breakdown with
reason, an absent method, completed status with absent coefficients, and
invalid coefficients. It requires the four statuses to appear in raw data,
CSV rows and receipt failures; all seven numeric CSV cells must be blank.
The three healthy external methods must exactly match their original payload.
These inputs test robustness only, not a newly measured scientific case.

`code/c2_hard_check.py` is the byte-exact extraction of the sole Python block
formerly embedded in `attempts/C2-hard.md`; SHA256 remains
`452d72d73b7116068a6b7b2f7fabebdb2eb77e5e51d83ae25507173014fecb66`.
Its fresh execution requires the recorded exact-rational counts:
50 polynomial identities, 735 differentiated-jet coordinate checks,
1050 a-field comparisons and 330 support-polynomial coordinate checks.
It remains supplementary finite evidence, not a theorem premise.

`code/c1_error_diagnostic.py` is rerun against the final committed
`c4-comparison-receipt.json`. The regression requires all 12 case summaries
(representing 348 original table rows) to remain exactly equal and the receipt
pin to match its current bytes. The raw matrix artifact also needs a manifest
entry: `/tmp/nn-mop-conditioning-20261106/c1-matrix-all.json`, 29,090 bytes,
SHA256 `b4e53167089eb2c8f78a2bd492e611ef9540ddc82c1aefbaf014d812af4e0f43`.
The coordinator owns the manifest update.

[external-code.md](external-code.md) now separates the historical pre-grid
M2 gate from the final post-grid two-family fidelity receipt and records the
actual full-bit-grid fidelity replay command. It documents the shared CSV
header's method-specific semantics without changing table schema or values.
The exploratory receipt keeps its rejected historical disposition and its
original gate labels, with added scope metadata clarifying that they do not
validate the rejected decimal-transport comparison.

This response does not execute third-party source, reproduce Advanpix
experiments, or establish a stability theorem. The full healthy replay and
synthetic failure checks are code regression evidence on the recorded stack.

The final M2 documentation command was also executed separately:

```sh
python3 topics/nn-mop-conditioning-20261106/code/c4_fidelity.py --external /tmp/c4-external-grid-bits.json --receipt /tmp/c4-m2-bits-replay.json
```

The resulting JSON equals the committed `c4-m2-bits-receipt.json` in its
entire parsed payload, including both families and the pinned input/code hashes.
