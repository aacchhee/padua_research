# Using the constructed point sets

Run the examples from the repository root with Python, NumPy and SciPy.
The recorded experiments used Python3.12.14, NumPy2.3.5 and SciPy1.17.0,
with one BLAS/OpenMP thread. Coordinates lie in[-1,1]^3. The approximation
and noise comparisons use product-Chebyshev probability measure.

## Simple default: explicit extra-point least squares

The anisotropic parity recipe gives45/225/637/1377points at degrees
4/8/12/16, for polynomial dimensions35/165/455/969. It supplies positive
weights and a direct moment formula whose exact Gram correction is known.
Its empirical RMS/noise tradeoff is strong; sampled maximum error can
still be worse for a particular function. See [U1 results](theory/u1-operational-comparison.md).

```python
import sys
import numpy as np
sys.path.insert(0, "topics/padua-3d-20261106/code")
from u1_usable import parity_nodes, parity_fit, basis

n = 8
points, weights, integer_recipe = parity_nodes(n)
# Replace this example by measurements in the returned canonical point order.
values = 2 + points[:, 0] - points[:, 1] * points[:, 2]
coefficients = parity_fit(n, values)
query = np.array([[0.1, 0.2, 0.3], [-0.4, 0.5, 0.6]])
prediction = basis(query, n) @ coefficients
```

For several data channels, supply an M-by-k value array; the coefficient
array is N-by-k. Scalars, wrong observation counts and arrays with more
than two dimensions now raise `ValueError`; see the [focused check](api-response-review.md).
`basis` uses the continuous orthonormal product-Chebyshev
basis in total-degree order. `parity_fit` includes the required factor1/2
on the(n,0,0)coefficient. Store the integer recipe when exporting a grid.

For iid observation noise, ordinary least squares on the identical nodes
is an optional solver:

```python
from scipy.linalg import qr, solve_triangular
Q, R = qr(basis(points, n), mode="economic")
coefficients_ols = solve_triangular(R, Q.T @ values)
```

Its extra factorization improves same-node integrated iid-noise risk by
2.47–8.03percent in the registered tests. Deterministic error changes have
both signs. The Haar moment formula is the lower-setup-cost default.

## Minimum count: the stored degree-twelve example

The essential [455-point artifact](evidence/u2-degree12-nodes.json)
contains every actual coordinate losslessly. It can be loaded without
rerunning optimization:

```python
import base64
import json
from pathlib import Path
from scipy.linalg import solve

record = json.loads(Path(
    "topics/padua-3d-20261106/evidence/u2-degree12-nodes.json"
).read_text())
points = np.frombuffer(
    base64.b85decode(record["coordinates_base85"]), dtype="<f8"
).reshape(record["N"], 3)
n = record["n"]
values = 2 + points[:, 0] - points[:, 1] * points[:, 2]
coefficients = solve(basis(points, n), values)
prediction = basis(query, n) @ coefficients
```

The first example's imports, generic `basis` and `query` are reused here.
This square solve interpolates455values in Pi_12. The stored binary64
coordinates are treated as exact dyadic rationals by the separate
unisolvence certificate. The degree-twelve measured refined lower sample
is26.0073versus55.6779for the prior one-sweep localdet set; it is not a
certified continuous maximum or an all-degree quality theorem. Target
function errors still have individual regressions. See [U2](usable2.md).

Verify the essential point artifact independently:

```sh
python topics/padua-3d-20261106/code/uc12_payload_check.py \
  --payload topics/padua-3d-20261106/evidence/u2-degree12-nodes.json \
  --output /tmp/UNIQUE-degree12-proof.json
```

Choose a fresh output filename. The recorded invocation and nonzero exact modular determinant
are in its [receipt](evidence/uc12-u2-payload.json). The actual independent
implementation decodes IEEE754 bits with the standard library, checks
exact cube membership/distinctness and certifies a full monomial matrix
at a freshly verified prime. The stored-point proof is separate from
all floating approximation, optimizer and norm claims.

To generate other registered-degree examples, use the frozen command
and unique scratch/output arguments in [usable2](usable2.md). Its
bounded projected update starts from the known localdet set and records
all geometric/Neumann/Armijo safeguards. Construction is an offline cost;
all 200-step stops are recorded as caps, not convergence. The stored
artifact avoids that cost when using this particular degree-twelve set.

## Minimum count: the degree-sixteen procedural example

The new40-step procedure produces969points for Pi_16. On the recorded
machine it used65.78extra CPU seconds after QR/initial exchange,
124.20seconds total construction. Its searched amplification was71.71
versus80.12for a determinant control using nearly the same extra budget.
Its noise risk and most tested function RMS comparisons were worse;
choose this example only when its strict distinct-site count and
amplification objective fit the task. Optimization stopped at a step cap.

Reproduce the construction and its recorded benchmark with a new scratch
directory and output filename:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2c_heldout.py --scratch /tmp/UNIQUE-padua16 --output /tmp/UNIQUE-padua16-receipt.json
```

The generated coordinates are `/tmp/UNIQUE-padua16/joint_norm.npy`.
Load them with `np.load` and use the square solve above at n=16. This full
benchmark also times controls and assesses errors, so its end-to-end cost
exceeds candidate construction alone. Commands, versions, safeguards,
regressions and independent checks are in [continuation results](continuation-results.md).
The new coordinates are procedural regeneration output, with numerical
validation; they do not inherit the committed455-point artifact's exact
unisolvence proof or an all-degree guarantee.

## Pruned grids with fewer sites than the full parity recipe

Two exported subsets are available:546sites at degree12and1163at degree16.
They remove14–16percent of the full grid and improve the measured noise/
amplification tradeoff against same-size restrictedQR. Minimal-site examples
use fewer observations; full grids retain better quality. See the
[comparison](pruning-summary.md) before choosing a size.

```python
from pdpr_certify import load
from scipy.linalg import lstsq

n = 16
points = load("topics/padua-3d-20261106/evidence/pdpr-pruned16-nodes.json")
values = 2 + points[:, 0] - points[:, 1] * points[:, 2]
coefficients, _, rank, _ = lstsq(basis(points, n), values, lapack_driver="gelsy")
prediction = basis(query, n) @ coefficients
```

Use the initial example's imports and code-directory path; replace the
example values with observations in the returned order. For degree12set
n=12and load pdpr-pruned12-nodes.json. The displayed physical OLS example
was executed for both files, returning ranks455/969and maximum errors below
8e−15on64fresh queries. This numerical check is separate from the exact
rank certificates. The [artifact guide](pruning-artifacts.md) gives repository-
only verification commands; no temporary optimization files are needed.

## Scope and review

U1 offers a known explicit recipe with a directly proved Gram/noise
interpretation. U2 offers a measured procedural improvement and one
fully stored finite unisolvent set. Shifted/folded/mixed research produced
exact finite classifications and witnesses, but the tested selectors lost
quality controls; those results are retained in [usable3](usable3.md).
The broad minimal-node polylogarithmic construction remains OPEN.
Independent supplementary checks are complete or recorded in their
reports; required Claude audit is a separate next step. No priority claim,
archival delivery or hardware-independent timing guarantee is made.

## Choosing a method after the continuation tests

Extra-point least squares remains the simple explicit default under the
stated measure/noise assumptions. At a fixed observation allowance, a
lower degree can be more useful when noise is large; spending the entire
budget on the highest degree is not universally best. The new
[degree/noise study](u1-continuation.md) compares38feasible designs and
integer repeat allocations. Its choices use known noiseless test functions
to estimate bias, so they are calibration examples rather than an automatic
data-only degree selector for an unknown function. GLS refitting after
those allocations improved covariance but missed the registered total-error
gate; its extra complexity is not recommended by that experiment.

The stored455-point degree12example remains the fully committed exact
witness above. New higher-degree optimization measurements are documented
in [continuation results](continuation-results.md); they are distinct from
that stored-set proof. A finite searched norm gain alone is not a guarantee
of smaller target error, completed convergence or an economical runtime.

The complete28-case degree7structural diagnostic found no QR-competitive
case. Keep those finite results as [scoped negative evidence](theory/u3c-nonunique-quality-boundary.md),
without treating them as an impossibility theorem for wider families.

## Executed release check

The following check ran from repository root under the versions above,
with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -`. Its stdout
reported errors3.55e−15/2.66e−15/1.33e−15; it creates no artifact and
is not a proof premise or a new counted research round.

```python
import sys, json, base64, hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import solve, qr, solve_triangular
sys.path.insert(0, "topics/padua-3d-20261106/code")
from u1_usable import parity_nodes, parity_fit, basis
query = np.random.default_rng(20261107).uniform(-1, 1, (64, 3))
expected = 2 + query[:, 0] - query[:, 1] * query[:, 2]
points, weights, recipe = parity_nodes(8)
values = 2 + points[:, 0] - points[:, 1] * points[:, 2]
c = parity_fit(8, values)
Q, R = qr(basis(points, 8), mode="economic")
d = solve_triangular(R, Q.T @ values)
p = Path("topics/padua-3d-20261106/evidence/u2-degree12-nodes.json")
j = json.loads(p.read_text())
raw = base64.b85decode(j["coordinates_base85"])
assert hashlib.sha256(raw).hexdigest() == j["coordinates_sha256"]
x = np.frombuffer(raw, dtype="<f8").reshape(j["N"], 3)
y = 2 + x[:, 0] - x[:, 1] * x[:, 2]
e = solve(basis(x, 12), y)
errors = [np.max(abs(basis(query, 8) @ c - expected)),
          np.max(abs(basis(query, 8) @ d - expected)),
          np.max(abs(basis(query, 12) @ e - expected))]
assert max(errors) < 1e-11
print(errors)
```
