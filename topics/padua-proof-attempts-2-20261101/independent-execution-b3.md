# B3 actual independent exact execution

Rules refreshed from the root-supplied `d8b878b` rule integration: AGENTS.md,
full WORKFLOW.md and agents/codex/CODEX.md were read. The changed repository-only
results paragraph was read explicitly. AC's topic-only writes and the root's
exclusive results/Git/manifest/handoff ownership remain controlling. Executor:
Codex `/root/input_manifest`, requested gpt-6.1-sol medium; separate runtime
serving-model metadata is not exposed. This is a supplementary technical
rerun, not mathematical development, a new novelty claim or the Claude audit.

Read the complete registered `attempts/T-B3.md`, including its fresh gate,
C1/C2 dispositions, C3 pre-run scope and kill criteria; and the full frozen
source `code/b3_four_atom_exact.py`. The first combined read was truncated;
bounded rereads closed the missing rule/task/source text before execution.
No source, proof, handoff or other agent's output was edited.

## Exact executed command and source identity

From `/workspace/padua_research`, actually executed once in a fresh process:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/b3_four_atom_exact.py --expect-source-sha256 b33647b8cff4c1b23e9b9089f9822fe307e1f8980786eec043b8bfc9ad3f9b7b --output topics/padua-proof-attempts-2-20261101/outputs/b3_four_atom_independent.json
```

Actual tool exit was 0; the script reported `exact_checks_passed: true` and
elapsed 0.3306512320014008 s. Source size 6921 bytes, SHA-256
`b33647b8cff4c1b23e9b9089f9822fe307e1f8980786eec043b8bfc9ad3f9b7b`
was externally read before and after, and both script source guards passed.
No input data file or random seed is used: all four atoms, weights, basis,
parameter interval and exact formulas are in that frozen source.

Runtime independently queried: Python 3.12.14, SymPy 1.14.0, ground type
`flint`, python-flint 0.9.0, FLINT 3.6.0. Mathematics uses exact rational
symbolic polynomial identities and coefficient bounds; time metadata alone
uses a clock. No floating sign decision, tolerance, quadrature or sample
extrapolation occurs. Bytecode writes were disabled.

## Observed identities and interval scope

The actual run reconstructs the declared positive four-atom measure's Gram
and coordinate moment matrices, verifies the stated rational degree-one
sections, their weighted self-adjointness, weight normalization and a nonzero
three-node determining minor. It verifies commutator support and exactly

`delta² = 27*t²/[2*(25*t+2)^3]`, `h²=t/10`.

It constructs the symmetrized product, certifies its determinant negative
(after removing positive t²) and trace positive by explicit rational
constant-minus-absolute-coefficient-tail bounds on the ENTIRE interval
`0 < t <= 1/1000000`. The leading determinant coefficient is
`-217/204800`. Five ancillary sign certificates cover r² and v above 1/100,
the nonzero x spectral square above 1/5, y-block trace above 2/5, and delta²
below 4t². Two squared reference/gap inequalities at the interval endpoint
also pass. All exact assertions passed; there was no failed run or revision.

The spectral interpretation of these signs as inertia, positive-pivot class
membership, computed marginal gap, nearby commuting reference and count
failure belongs to the separately written proof. This execution does not
replace that proof or the required Claude audit, and establishes no broader
B3 family or mechanism claim by extrapolation.

## Output identities and actual comparison

Independent output `outputs/b3_four_atom_independent.json`: 8974 bytes,
SHA-256 `21eb93c3a5d34c3c43633d678034b5c4347c8e478bd1860873a7c79ddadb9575`.
Developer output `outputs/b3_four_atom_exact.json`: 8975 bytes,
SHA-256 `bf95045657bf9f164c3e5a56895ec7bc39d34e2a4cf47b69d2e935585f39a6ef`.
Both retain exact proof-payload SHA-256
`8fe7d5937ae698c255823bed941376e3f0338d972114ca93f333127564df2bc7`.

After the actual independent execution, I loaded both completed JSON files
and compared their ENTIRE contents after removing ONLY `metadata.seconds`.
All remaining fields agree exactly: formulas, every numerator/denominator
coefficient and bound, interval, versions, source guards and proof-payload
identity. No process binding or unexplained field normalization was removed.
Developer time is 0.28936160000012023 s; independent time is recorded above.
Comparison is separately identified from my actual fresh execution; neither
reading the developer output nor matching its payload is counted as a run.
No extra unchanged mathematical execution was performed.
