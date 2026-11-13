# Recheck certificate data from the small I25 bundle

The 2,843,611-byte I25 ZIP contains all 942 phase witnesses. Its numerical
checker is also available in the trusted repository source. This recipe
reads only proof JSON from the ZIP and imports the separately trusted source.
Python and NumPy are required; the recorded runtime and arithmetic assumptions
are in J03 and the bundle. The completed campaign and independent six-certificate
replay used the commands in their preregistrations. The alternative input
recipe below is supplied for future audit use; it is not an additional
reported numerical execution. Preregister the chosen audit scope before use.

From the repository root, with the bundle at its recorded local path:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -E -B - <<'PY'
import hashlib, json, resource, sys, zipfile
from pathlib import Path
def need(condition, message):
    if not condition:
        raise ValueError(message)
need(sys.flags.optimize == 0, 'optimized Python is unsupported')
code = Path('topics/padua-argmax-bridge-20261105/code/independent_phase_checker')
pins = json.loads((code / 'FULL-PREREGISTRATION.json').read_text())['source_sha256']
need(hashlib.sha256((code / 'check.py').read_bytes()).hexdigest() == pins['check.py'], 'check.py identity')
need(hashlib.sha256((code / 'controls.py').read_bytes()).hexdigest() == pins['controls.py'], 'controls.py identity')
sys.path.insert(0, str(code.resolve()))
import check
from controls import arithmetic_controls
bundle = Path('local-output/argmax-bridge-20261105/i25-evidence-20261108T112304Z.zip')
need(hashlib.sha256(bundle.read_bytes()).hexdigest() == 'd1d03156dde4248fecaa25d0144cd73c7c5414f28b66a39099342b31f2f7e0f8', 'I25 bundle identity')
resource.setrlimit(resource.RLIMIT_CPU, (300, 300))
arithmetic_controls()
with zipfile.ZipFile(bundle) as z:
    names = [s for s in z.namelist() if s.startswith('proofs/')]
    expected = {f'proofs/n{n}-{mode}.json' for n in range(41, 512)
                for mode in ('produce', 'verify')}
    need(len(names) == 942 and set(names) == expected, 'exact 942 proof members')
    for n in (41, 458, 511):
        cache = {}
        for mode in ('produce', 'verify'):
            data = json.loads(z.read(f'proofs/n{n}-{mode}.json'))
            need(type(data['n']) is int and data['n'] == n, 'proof degree')
            result = check.check(data, cache)
            print(n, mode, result)
PY
```

For a preregistered full serial recheck, replace the three-degree tuple by
`range(41, 512)` and set `resource.setrlimit(resource.RLIMIT_CPU, (7200, 7200))`.
This is a prospective serial process CPU cap, not a wall cap or a guarantee of
completion. Record the environment and a calibration observation in the new
preregistration before a consequential full replay. Do not alter the frozen
campaign preregistrations.

The existing calibration evidence is historical: audit-04 J3-02 (2026-11-08)
measured the n=511 primary at 21.73 CPU-s versus the earlier pilot's 14.600 s,
and n=238 at 4.56 s versus 2.689 s. Its n² fit estimated about 3,750 CPU-s
for a serial full replay; that estimate motivated the 7,200 s headroom here.
No new calibration or full replay was run for this recipe edit (2026-11-13).
The completed four-worker campaign recorded 2,519.421 aggregate CPU-s and
646.839 wall-s on its own environment. Each degree receives a fresh cache,
shared only by its two witnesses. The 942 witnesses represent 471 distinct
trees, each recorded twice.

`-E` ignores Python environment variables including `PYTHONOPTIMIZE`; it is
not full isolated mode. The explicit optimization guard also rejects `-O`.
Every integrity guard raises an error and remains active under optimization.

Manuscript preservation checks use a Git clone containing the source-freeze
and historical commits, together with the specified PDFs. A Git source ZIP
contains the tracked source tree; Git history is retrieved from the repository.
