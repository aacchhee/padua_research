# Focused supplementary review — U1-M1 API response

Date: 2026-11-07. Rules and baseline source commit:
`97c323bfae15cf3c76f40802c3ebabedceeb0c60`.
Reviewer: distinct Codex agent, configured gpt-6-astra high; runtime
model/effort not independently exposed. Review covers the working-tree
patch identified below, not an assumed future publication commit.

**Verdict: PASS for the material observation-shape correction.** The two
reported silent broadcasts now raise clear `ValueError`s before weighting.
Valid vector, single-column and multiple-column paths retain their ranks,
dtypes and arithmetic, including complex values. No BLOCKING or MAJOR
finding remains in this focused shape-fix scope. This supplementary Codex
review does not replace the pending formal Claude review or authorize
readiness/merge. Repair and verification consume zero construction rounds.

## Scope and inspected identities

Read AGENTS, WORKFLOW, CODEX, handoff13 and its superseding handoff14,
interim-audit-01/U1.md including U1-M1, the public usable-recipes contract,
relevant integer-domain statements in the U1 parity theory, the complete
producer and new API checker, developer API receipt, preserved original
API checker, and the science replay checker/receipt/comparison record.
Reviewed the producer diff against the input commit: only `parity_fit`
changes, by converting the observation input once, checking rank and
leading length, then retaining the original weighted multiplication and
highest-x coefficient correction.

**Novelty-gate exception:** this review introduces no mathematical
mechanism, construction candidate, priority claim or general negative
result. It tests an existing API and a narrow input-validation correction;
full IDEAS/literature reading is unnecessary for this scope and was not
performed. No theorem status or earlier scientific conclusion is reopened.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| code/u1_usable.py |17849|`2b8a087126189a9a161acd449260b9ec456d28813337c820a90f5fc3cc991938`|
| code/u1c_api_check.py |4251|`16389ca8c1d7b96e518270e363de5992e926313d41a96985f5977e7675208ac9`|
| evidence/u1c-api.json |6108|`962d251e86c9685d9f765d5d86f632f43f24031442689d13d6a9fb6ff1cc13ad`|
| evidence/u1c-science-replay.json |2920|`7587fed49ba11acf04a99f677b3cafdab93854ba2e1a3a29224d71658efb9d8e`|
| api-response-check/check_api.py |9014|`75b36c956c05108ab9f3c501369b7f692a329d6814b89595af1853f6cb78241c`|
| api-response-check/receipt.json |9752|`4ecccaf2d8124e48fdef14ef22766e15b7be171e9537f31130ce3f7d5bb8c732`|

The [independent receipt](api-response-check/receipt.json) also identifies
the baseline source and both inherited executable dependencies. All six
reviewed inputs/checker identities were unchanged before/after execution;
every source hash and size in the developer API receipt matched disk.

## Independent execution

Executed from repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/api-response-check/check_api.py --raw /tmp/padua-api-response-review-20261107b --out topics/padua-3d-20261106/api-response-check/receipt.json
```

Execution: 08:20:07.198412–08:20:07.834660 UTC. Python3.12.14,
NumPy2.3.5, SciPy1.17.0, Linux6.18.57 x86_64/glibc2.41; three thread
variables set to1. Seed20261107113, 61 fresh physical-cube queries.
Runtime skill/environment status showed the attached executor running,
current observations and enforced network policy. No network access or
package installation was needed.

The [independent checker](api-response-check/check_api.py) retrieves the
old source with read-only `git show` at the recorded commit and executes
old and new functions separately. An independent cosine-definition basis
provides every basis column and fresh full-degree polynomials, rather than
using the producer's recurrence as the reproduction oracle.

- Ten grids: degrees1,2,3,5,9 and both anisotropic/equal families.
- 140 valid cases have identical coefficient shape, dtype and raw bytes
  before/after. They include vector, column, three-channel, nested lists,
  complex vector/matrix, float32/complex64, integer/boolean, noncontiguous,
  read-only, and the already-supported empty-channel shape. No input was
  mutated. Empty channels are preserved behavior, not a newly recommended
  measurement use case.
- 110 malformed cases reject with a descriptive `ValueError`: scalar,
  one-value vector, one-row matrix, empty/short/long vectors, short/long
  matrices, transposed arrays and ranks3/4. Separate degree4 probes
  reproduce both original silent broadcasts and their corrected rejection.
- Complete-basis coefficient reproduction infinity residual at most
  9.810580734408174e-15; query prediction error at most
  3.019806626980426e-14; highest-x coefficient error at most
  1.0927207671383252e-15. Odd-degree and top-mode paths therefore receive
  explicit independent checks. These are finite binary64 measurements.

The first invocation used raw suffix `a`. Its checks completed but the
final console-print helper failed on a relative output path after writing
the receipt. I corrected only my checker to resolve that path, then reran
the entire check with fresh raw suffix `b`; the recorded identities and
successful command above belong to the final run. Both temporary source
snapshot directories are regenerate-only, with no cold archive delivery.

## Scientific-output regression evidence

The developer's [24-case replay](evidence/u1c-science-replay.json) actually
reruns both original scientific rounds at n4/8/12/16 under producer hash
`2b8a0871...`, using the preserved `uc12_replay_u1.py`. I inspected that
checker and its comparison record and independently verified all six
source/input pins, the comparison-file size/hash, agreement of its pins
with the receipt, all24 passing rows, empty scientific-difference lists,
and zero deltas across all144 saved-array comparisons. The receipt reports
40.797159141999146 seconds and comparison tolerance rtol2e-10/atol2e-12.
Original arrays and receipts retain their historical identities.

The replay inspection was a separate read-only Python invocation, not a
second producer run. Its executed validation body was:

```python
import hashlib, json
from pathlib import Path
p = Path('topics/padua-3d-20261106/evidence/u1c-science-replay.json')
r = json.loads(p.read_text())
for s in r['pins'] + [r['details']]:
    b = Path(s['path']).read_bytes()
    assert len(b) == s['bytes'] and hashlib.sha256(b).hexdigest() == s['sha256']
d = json.loads(Path(r['details']['path']).read_text())
assert d['pins'] == r['pins'] and len(d['rows']) == 24
assert all(x['passed'] and not x['scientific_differences']
           and all(v == 0 for v in x['array_deltas'].values()) for x in d['rows'])
```

This full scientific replay was performed by the developer, not by this
reviewer; its reuse of a formerly independent checker does not make the
present execution independent. My actual independent executions are the
shape/baseline/cosine tests above. `run_case` builds its scientific operator
directly and does not invoke the modified public `parity_fit`, so the full
replay checks unchanged producer results while the independent API probes
exercise the changed path. This distinction is necessary to interpret
what each check covers.

## Remaining NOTE and limits

**API-R-N1 — inherited degree-domain hardening was not implemented.**
The theory uses integer n>=1. Original U1-M1 mentioned validating that
domain as additional hardening; handoff13's concrete fix is the malformed
observation-shape defect. `parity_nodes` still raises incidental exceptions
for invalid n (e.g. n0 anisotropic gives `AssertionError`, nonintegral1.5
gives `TypeError`) and Python `True` acts like degree1. The focused patch
does not add a consistent domain validator. The receipt records these
observations without promoting them into a supported API extension. At
equal n0 a short one-value observation formerly broadcast and now rejects,
which is the same intended shape correction outside the stated n>=1
science domain. This is not a regression on the documented valid domain
and does not block the narrow shape-fix PASS. A response should not claim
that every hardening suggestion in the original finding was implemented.

No complex-input restriction, finite-value policy, masked-array contract,
arbitrary array-subclass support or degree-domain expansion was introduced
or certified. Tests cover the stated numeric/list paths, not every possible
Python object or hardware/BLAS environment. No timing comparison is inferred
from these quick checks, no general proof is inferred from floating
agreement, and historical target/noise tradeoffs remain unchanged.

Only the new report and `api-response-check/` files were written by this
reviewer. No producer fix, shared manifest, log, Git mutation or handoff was
made. The orchestrator owns integration and the pending formal audit chain.
