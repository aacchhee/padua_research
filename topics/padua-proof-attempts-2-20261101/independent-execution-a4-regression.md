# Exact A4 all-edge regression — planned before execution

Rules were reread at `3062f77f5ead1d888fa319a7c3a20371d4f305f7`.
Developer/executor: Codex `/root/input_manifest`, requested gpt-6.1-sol medium;
separate serving-model metadata is not exposed. This is technical finite
regression of the already written analytic identity70, not new mathematics,
novelty/priority work, a gap/global proof or a Claude audit. The target's
refreshed registry gate belongs to the lead's A4 records; no new mechanism is
proposed here.

Read the complete theory
`theory/proof-attempts-2-codex-70-all-edge-kernel-formula.md`, accepted A1
`PD-T?proof-attempts-codex-01 (audit pending)` (historical requested label;
Claude audit accepted and dispositions complete), and its exact-check scaffold.
No old file is imported or edited by the new script.

## Planned finite check and kill criteria

This plan is written before the first mathematical execution of the new code.

1. For n=1,...,6, independently construct and invert the square product-Chebyshev
   Vandermonde over the exact cyclotomic field of order `2*n*(n+1)`. Check its
   inverse identity without assuming the corrected kernel.
2. Construct `P_n=T_(n+1)+T_n` with integer coefficients and its polynomial
   divided difference Q(A,B). Compare Q coefficient by coefficient with the
   finite rhombus Chebyshev sum and verify the entire diagonal polynomial
   `Q(Z,Z)=P_n'(Z)`, including both endpoint diagonal values.
3. For every Padua node and each of the four closed edges, compare the full
   free-coordinate polynomial obtained from the Vandermonde inverse with the
   corrected kernel and with theory70's symmetrized Q formula. Formal sine
   terms are averaged exactly and even powers reduced by `sin²t=1-cos²t`.
   The y-edge correction remains in the free x coordinate. Check partition of
   unity on each edge. No absolute-value sign choice is needed.
4. Enumerate exact coincident-argument branches on the joint angular mesh
   `t=r*pi/[n*(n+1)]`, including its endpoints, and evaluate each with the
   derivative diagonal limit. The full diagonal polynomial check also covers
   the removable limit as an identity, not a numerical approximation.
5. Freeze the complete new source hash before execution, require it as a CLI
   argument, and check it again before reporting success. Print only a small
   JSON receipt. Run once in a fresh process and retain its own output.

Kill criteria: any nonzero exact polynomial difference, inverse failure,
incorrect diagonal evaluation, source drift or execution failure stops the
claim and is reported; no tolerance or successful finite scope is substituted
silently. If the intended degree range proves infeasible, record the actually
completed scope explicitly rather than claim n<=6 coverage.

## Runs needed

The new source was frozen before its first execution at SHA-256
`13e8c524c4c21701bdee2a009cda2245d8f289d6a6cca0dba19afec1842f872e`.
The plan above was recorded before execution. Authoritative read-file SHA-256s:
theory70 `f2e76ff091a964be15c28607ca49d52ff5ce4e12fa91dc42df5aa12a7e6b0ebe`;
accepted A1 `ea59aa077a4d021fc69354383f69340f21d17d87d3a28c6ecaaf302cc763612c`;
old A1 scaffold `e7ea17bc56e44214fdf4206c654fb1710e7a8d3ca194dcdc15390a066a7920b0`.
The first actual command is:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a4reg_exact_check.py --source-sha256 13e8c524c4c21701bdee2a009cda2245d8f289d6a6cca0dba19afec1842f872e > topics/padua-proof-attempts-2-20261101/outputs/a4reg_exact_developer.json
```

Then a different agent must actually execute the same frozen source into
`outputs/a4reg_exact_independent.json`. Reading or comparing the developer
output alone is not that rerun. Root retains all Git, manifest, protocol and
handoff ownership. All generated outputs are targeted below 20 KB.

## Actual developer execution

The exact command above was executed once from `/workspace/padua_research`
in a fresh process. Actual exit was 0; reported elapsed time was 2.408987 s.
The output is `outputs/a4reg_exact_developer.json`, 4561 bytes, SHA-256
`1bfcfa3a08861911d2b6ec1cf857f797a0f14c3d22fd3acda1b43aa08a88cef1`.
Source SHA-256 before and after was the frozen `13e8c524...42f872e`; the script
checked both itself, and an external post-execution hash also matched.

Runtime: Python 3.12.14, SymPy 1.14.0, exact ground type `flint`,
python-flint 0.9.0, FLINT 3.6.0. No floating-point test or sign tolerance is
used; elapsed-time measurement is administrative metadata.

| n | nodes | full edge polynomials per formula | removable values | diagonal branches |
|---|---:|---:|---:|---:|
| 1 | 3 | 12 | 12 | 22 |
| 2 | 6 | 24 | 28 | 42 |
| 3 | 10 | 40 | 52 | 70 |
| 4 | 15 | 60 | 84 | 106 |
| 5 | 21 | 84 | 124 | 150 |
| 6 | 28 | 112 | 172 | 202 |

All stated checks passed. Totals: 1595 inverse entries; 332 full edge
polynomials for each of the corrected-kernel and symmetrized-divided-difference
comparisons; 472 removable cardinal values, including 48 endpoint values;
592 derivative-branch evaluations; six full diagonal polynomial identities;
12 explicit endpoint diagonal checks; 24 exact edge partitions of unity.
Both divided-difference numerator and rhombus polynomial identities passed
coefficient by coefficient at each degree.

These results check finite degrees 1 through 6 only. They supplement the
analytic all-degree derivation in theory70, and establish no gap, global
maximum, completeness of a stationary-point search, or audit acceptance.

## Actual different-agent rerun

The lead `/root/a5_develop` separately executed the same frozen source and
reported actual exit 0, elapsed 2.415554 s, unchanged source guards and output
`outputs/a4reg_exact_independent.json`, 4561 bytes, SHA-256
`7f21d8e033b260de220f578f2cf81fefd23101417a2fed8781bdd9285351b7a6`.
The exact command was the developer command above with only its final
redirection changed to `outputs/a4reg_exact_independent.json` (under the same
topic). This receipt distinguishes my actual developer execution from the
lead's actual different-agent execution; merely reading their output is not
being counted as another mathematical run.

I independently loaded both completed JSON outputs and compared every field
after removing only top-level `elapsed_seconds`: exact equality passed.
The output hashes/sizes and frozen source hash were externally reread and
matched the reported identities. Versions, arithmetic backend, all scope and
check counts, booleans, and source guards agree. Both exact executions passed;
there was no source revision, failed mathematical run, narrowed scope or
tolerance fallback. No further mathematical execution was needed.

## Complementary-grid extension — preregistration before execution

The frozen all-edge source `13e8c524...42f872e` remains unchanged. The full
records71 and72 have now been read. Before executing any new exact check,
register this finite scope: n=1,...,6, both endpoint signs and every admissible
interior q with the complementary parity. Independently invert each exact
cyclotomic Vandermonde; at every node compare the resulting cardinal value
with the regular E+ + E- identity, or with the actual divided-difference
endpoint branch. Verify uniqueness of that exceptional endpoint, its actual
corrected kernel magnitude n-1 versus formal magnitude1, and its weight1/N.
Compare weighted raw-E multisets after translation with the odd checkerboard;
this is stronger than their signed sum and implies equality after applying
any common value function, including absolute value. Verify the rational
normalization correction 1/m-(n-2)/N=2/N exactly.

No numerical absolute-value signs will be guessed. This extension does not
execute an embedding-dependent absolute-value gap sum, quadrature, a limit,
root search or global proof. Any exact discrepancy or source drift stops the
run; no silent narrowing. Freeze the new source and imported source pins
before its first run, retain a tiny developer JSON, and require an actual
separate-agent rerun with a distinct output. The analytic proofs71/72 remain
separate from this finite regression.

Before its first execution the extension source was frozen at
`978bf8e00e09f4671d36d9de0e3c8dae531d34491ed7cdec1741aa6542032fca`;
its sole local import is guarded at the unchanged original
`13e8c524c4c21701bdee2a009cda2245d8f289d6a6cca0dba19afec1842f872e`.
Read record71 SHA-256 `4718a1e8e50b1e350f771b39b03540c05e3ef9c8d0b6abcb7abdcf1f6e8eecf3`
and record72 `82a742be149b634df03f56f625242f4da3e347f2cbf795777dd37b2e9e91175b`.
The planned command, executed from the repository root, is:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a4reg_complementary_check.py --source-sha256 978bf8e00e09f4671d36d9de0e3c8dae531d34491ed7cdec1741aa6542032fca > topics/padua-proof-attempts-2-20261101/outputs/a4reg_complementary_developer.json
```

### Actual complementary developer execution

The exact command above actually exited 0 in 1.543606 s. Developer output
`outputs/a4reg_complementary_developer.json` is 3074 bytes, SHA-256
`1c6c3ef524ce9d21a4eec1fe19d2120b7f572ce1e8c78847fbdafb96f0553f93`.
Python 3.12.14, SymPy 1.14.0, FLINT ground type, python-flint 0.9.0,
FLINT 3.6.0 were observed. Both source guards passed before/after; external
post-run SHA-256 rereads also matched. No source revision or failed run.

Every admissible complementary point for n=1,...,6 passed: point counts 1,2,3,4,5,6;
regular cardinal identity counts 2,10,27,56,100,162; unique endpoint counts
1,2,3,4,5,6. Totals are 21 points, 357 regular identities and 21 endpoint checks.
All weighted raw-E multisets agree exactly, and every rational +2/N
normalization identity passed. The actual derivative endpoint branch and
Vandermonde cardinal agree, including n=1's true magnitude 0 versus formal 1.
The multiset entries are exact cyclotomic-field elements with exact rational
weights; no signs or approximate absolute values were used. This verifies the
finite algebraic translation behind 71, but does not independently compute
its full absolute-value gap or 72's limiting integral.

An actual different-agent replay has been requested; its receipt follows
only after execution.

### Actual complementary different-agent replay

Lead `/root/a5_develop` actually reran the identical frozen command with only
its output redirection changed to the distinct topic output
`outputs/a4reg_complementary_independent.json`. Actual exit 0, elapsed
1.681193 s; 3074 bytes, SHA-256
`fbdff9c29bee11828ac173fbd7f93d5606ff05d5b159e1813e91d8c1018c1520`.
I loaded both JSON outputs and compared every field after removing only
`elapsed_seconds`: exact equality passed. The output identity and both frozen
source identities were externally reread and matched; both executions'
before/after guards passed. This closes the actual separate-agent finite
regression. The four A4 regression JSON outputs together occupy 15270 bytes.
No additional mathematical run, source revision or broader conclusion follows.
