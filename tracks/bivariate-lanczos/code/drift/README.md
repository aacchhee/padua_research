# Reproduce the drift experiments

Run commands from the repository root. The recorded environment used Python
3.12.14, python-flint 0.9.0, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0,
mpmath 1.3.0, and `OPENBLAS_NUM_THREADS=1`. Install dependencies and retain
generated outputs outside Git; the paths below match the development layout.

```bash
mkdir -p /workspace/padua-drift-runs/python-deps /workspace/padua-drift-runs/reproduce
python -m pip install --target /workspace/padua-drift-runs/python-deps python-flint==0.9.0 numpy==2.3.5 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
export PYTHONPATH=/workspace/padua-drift-runs/python-deps
export OPENBLAS_NUM_THREADS=1
```

These are setup commands for a fresh workspace; availability of compatible
wheels and network access must be supplied by that workspace. The repository
does not vendor these packages. `python -I` ignores `PYTHONPATH`; omit `-I`
when using the target-directory installation above.

## E1 exact aggregate map and declared scalar-CGS2 graph

Check the committed aggregate evidence, generate one exact case, and verify
the differentiated recurrence:

```bash
python tracks/bivariate-lanczos/code/drift/e1_check.py --evidence topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json --output /workspace/padua-drift-runs/reproduce/e1-check.json
python tracks/bivariate-lanczos/code/drift/e1_exact.py --set triangle --degree 12 --rule bj --sources all --output /workspace/padua-drift-runs/reproduce/e1-triangle-n12-bj.json
python tracks/bivariate-lanczos/code/drift/e1_verify.py --output /workspace/padua-drift-runs/reproduce/e1-derivative-check.json
```

`e1_batch.py --output-dir DIR --summary FILE --workers 4` regenerates all 88
aggregate cases at degrees 2–12. Each case has a 240-second timeout. Exact
fractions and rational square-root bounds are the evidence; floating-point
summaries are for readability. The evidence checker checks recorded arithmetic
and coverage, and does not independently regenerate the map.

The compact scalar certificates can be regenerated without the original
3.6 MB capacity artifact:

```bash
python tracks/bivariate-lanczos/code/drift/e1_reproduce.py --set triangle --output /workspace/padua-drift-runs/reproduce/e1-scalar-triangle.json
python tracks/bivariate-lanczos/code/drift/e1_reproduce.py --set rotated --output /workspace/padua-drift-runs/reproduce/e1-scalar-rotated.json
```

The wrapper validates input and producer hashes, reconstructs capacities in
temporary storage, compares exact gains and signs with the compact record,
and checks an explicit final normal projection. The rotated run took about
90 seconds during development. This is a declared formal scalar-CGS2 graph;
it does not assert actual IEEE error realizability. See `e1-summary.md` and
the E1 manifests under the topic's `evidence/` directory for the distinct
aggregate and scalar verdicts.

## E5 symbolic checks

```bash
python -B tracks/bivariate-lanczos/code/drift/e5_exact_checks.py > /workspace/padua-drift-runs/reproduce/e5-exact-checks.json
```

SymPy corroborates finite identities; the written proofs supply the all-degree
statements. The isolated command in `e5-manifest.json` assumes dependencies
installed in the interpreter environment rather than through `PYTHONPATH`.

## E6 upstream code and numerical adapters

The external source is Jeffrey Hokanson's
[polyrat](https://github.com/jeffrey-hokanson/polyrat), pinned to
`6903d7af9995c9d88e661fb229626696e00fdfba` (reported version 0.2.2).
Clone it outside this repository and install its small adapter dependency in
the sibling `deps` directory expected by `load_upstream`:

```bash
mkdir -p /workspace/padua-drift-external/deps
git clone https://github.com/jeffrey-hokanson/polyrat.git /workspace/padua-drift-external/polyrat
git -C /workspace/padua-drift-external/polyrat checkout --detach 6903d7af9995c9d88e661fb229626696e00fdfba
python -m pip install --target /workspace/padua-drift-external/deps backports.cached-property==1.0.2
python tracks/bivariate-lanczos/code/drift/e6_benchmark.py --external /workspace/padua-drift-external/polyrat --output /workspace/padua-drift-runs/reproduce/e6-benchmarks.json
python tracks/bivariate-lanczos/code/drift/e6_benchmark.py --external /workspace/padua-drift-external/polyrat --sets T24 Q24 --grid-degree 12 --output /workspace/padua-drift-runs/reproduce/e6-grids12.json
python tracks/bivariate-lanczos/code/drift/e6_benchmark.py --external /workspace/padua-drift-external/polyrat --sets T24 Q24 --grid-degree 16 --output /workspace/padua-drift-runs/reproduce/e6-grids16.json
python tracks/bivariate-lanczos/code/drift/e6_smooth.py --external /workspace/padua-drift-external/polyrat --output /workspace/padua-drift-runs/reproduce/e6-smooth.json
```

Do not copy upstream source into Git. The namespace adapter imports unchanged
`polyrat` Arnoldi/basis/index modules while bypassing unrelated package-level
solver imports; a full upstream package installation is not required. It adds
the checkout's sibling `deps` directory automatically. If either directory
is absent, supply it before running; missing external code is not an executed
benchmark.

The local comparison adapter imports existing repository files
`tracks/bivariate-lanczos/code/L2/l2_core.py` and its L1 dependencies. These
were already present at the recorded base
`806cc7b4509fd93bae652f9545d32d95529f8281`; their pinned content hashes appear
in `e6-provenance.json`. Use the complete repository checkout rather than
copying this `drift/` directory alone. Compare case/method metrics and validity
flags; BLAS/library changes need not preserve numerical results bit for bit.
