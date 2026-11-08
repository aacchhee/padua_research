# Recheck certificate data from the small I25 bundle

The 2,843,611-byte I25 ZIP contains all942 phase witnesses. Its numerical
checker is also available in the trusted repository source. This recipe
reads only proof JSON from the ZIP and imports the separately trusted source.
Python and NumPy are required; the recorded runtime and arithmetic assumptions
are in J03 and the bundle. The completed campaign and independent six-certificate
replay used the commands in their preregistrations. The alternative input
recipe below is supplied for future audit use; it is not an additional
reported numerical execution. Preregister the chosen audit scope before use.

From the repository root, with the bundle at its recorded local path:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B - <<'PY'
import hashlib, json, resource, sys, zipfile
from pathlib import Path
code = Path('topics/padua-argmax-bridge-20261105/code/independent_phase_checker')
pins = json.loads((code / 'FULL-PREREGISTRATION.json').read_text())['source_sha256']
assert hashlib.sha256((code / 'check.py').read_bytes()).hexdigest() == pins['check.py']
assert hashlib.sha256((code / 'controls.py').read_bytes()).hexdigest() == pins['controls.py']
sys.path.insert(0, str(code.resolve()))
import check
from controls import arithmetic_controls
bundle = Path('local-output/argmax-bridge-20261105/i25-evidence-20261108T112304Z.zip')
assert hashlib.sha256(bundle.read_bytes()).hexdigest() == 'd1d03156dde4248fecaa25d0144cd73c7c5414f28b66a39099342b31f2f7e0f8'
resource.setrlimit(resource.RLIMIT_CPU, (300, 300))
arithmetic_controls()
with zipfile.ZipFile(bundle) as z:
    names = [s for s in z.namelist() if s.startswith('proofs/')]
    expected = {f'proofs/n{n}-{mode}.json' for n in range(41, 512)
                for mode in ('produce', 'verify')}
    assert len(names) == 942 and set(names) == expected
    for n in (41, 458, 511):
        cache = {}
        for mode in ('produce', 'verify'):
            data = json.loads(z.read(f'proofs/n{n}-{mode}.json'))
            assert data['n'] == n
            result = check.check(data, cache)
            print(n, mode, result)
PY
```

For a preregistered full serial recheck, replace the three-degree tuple by
`range(41, 512)` and raise the CPU limit to3600seconds. The completed
four-worker run used2519.421 aggregate CPU-seconds and646.839wall-seconds;
these are observations rather than a guarantee for another machine. Each
degree receives a fresh cache, shared only by its two witnesses.

Manuscript preservation checks use a Git clone containing the source-freeze
and historical commits, together with the specified PDFs. A Git source ZIP
contains the tracked source tree; Git history is retrieved from the repository.
