"""Check byte-exact hardening deltas and narrow source-version compatibility."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

TOPIC = Path(__file__).resolve().parents[1]
ROOT = TOPIC.parents[1]
INPUT = 'cdb12257af24ea2542de707b9730f8278d69a168'
sys.path.insert(0, str(TOPIC / 'code/part3'))
import proof_runtime as p

GENERAL_CURRENT = (
    '    source_map = {name: b.digest(folder/name) for name in\n'
    '                  ("finite_bernstein.py", "finite_general.py", "finite_general_run.py", "finite_n2_exact.py")}\n'
    '    assert guard_compatible_sources(data["source_sha256"], source_map,\n'
    '                                    folder / "finite_n2_exact.py", "finite_n2_exact.py")\n'
).encode()
GENERAL_HISTORICAL = (
    '    assert data["source_sha256"] == {name: b.digest(folder/name) for name in\n'
    '            ("finite_bernstein.py", "finite_general.py", "finite_general_run.py", "finite_n2_exact.py")}\n'
).encode()
ENTRIES = (
    'code/part3/finite_n2_exact.py', 'code/part3/finite_bernstein_check.py',
    'code/part3/finite_general_check.py', 'code/part3/finite_general_controls.py',
    'code/part3/pairing_exact_check.py', 'code/part3/pairing_independent_reconstruction.py',
    'code/gated/d3_edge_check.py',
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run():
    identities = []
    for name in ENTRIES:
        path = TOPIC / name
        current = path.read_bytes()
        original = subprocess.check_output(['git', '-C', str(ROOT), 'show',
                                           INPUT + ':' + str(path.relative_to(ROOT))])
        require(current.count(p.N2_OPTIMIZATION_GUARD) == 1, 'guard occurrence count: ' + name)
        recovered = current.replace(p.N2_OPTIMIZATION_GUARD, b'', 1)
        if name.endswith('finite_general_check.py'):
            require(recovered.count(p.D3_COMPAT_IMPORT) == 1
                    and recovered.count(GENERAL_CURRENT) == 1, 'general adapter occurrence counts')
            recovered = recovered.replace(p.D3_COMPAT_IMPORT, b'', 1)
            recovered = recovered.replace(GENERAL_CURRENT, GENERAL_HISTORICAL, 1)
        if name.endswith('d3_edge_check.py'):
            require(recovered.count(p.D3_COMPAT_IMPORT) == 1
                    and recovered.count(p.D3_CURRENT_SOURCE_CHECK) == 1, 'D3 adapter occurrence counts')
            recovered = recovered.replace(p.D3_COMPAT_IMPORT, b'', 1)
            recovered = recovered.replace(p.D3_CURRENT_SOURCE_CHECK, p.D3_HISTORICAL_SOURCE_CHECK, 1)
        require(recovered == original, 'non-enumerated source change: ' + name)
        identities.append({'path': name, 'old_sha256': sha(original), 'current_sha256': sha(current),
                           'exact_enumerated_reversal': True})
    n2 = (TOPIC / ENTRIES[0]).read_bytes()
    d3 = (TOPIC / ENTRIES[-1]).read_bytes()
    old_n2 = n2.replace(p.N2_OPTIMIZATION_GUARD, b'', 1)
    old_d3 = d3.replace(p.N2_OPTIMIZATION_GUARD, b'', 1).replace(p.D3_COMPAT_IMPORT, b'', 1)
    old_d3 = old_d3.replace(p.D3_CURRENT_SOURCE_CHECK, p.D3_HISTORICAL_SOURCE_CHECK, 1)
    cases = []
    with tempfile.TemporaryDirectory(prefix='padua-source-compat-') as folder:
        np, dp = Path(folder) / 'n2.py', Path(folder) / 'd3.py'
        np.write_bytes(n2)
        dp.write_bytes(d3)
        nkey, dkey = 'code/part3/finite_n2_exact.py', 'code/gated/d3_edge_check.py'
        actual = {nkey: sha(n2), dkey: sha(d3), 'other.py': 'f' * 64}
        recorded = {**actual, nkey: sha(old_n2), dkey: sha(old_d3)}

        def check(label, want):
            accepted = p.guard_compatible_sources(recorded, actual, np, nkey, d3_checker_path=dp)
            require(accepted == want, 'unexpected metadata acceptance: ' + label)
            cases.append({'case': label, 'accepted': accepted})

        check('exact_historical_n2_and_d3', True)
        actual['other.py'] = '0' * 64
        check('unrelated_source_change', False)
        actual['other.py'] = 'f' * 64
        np.write_bytes(n2 + b'# changed source\n')
        actual[nkey] = sha(np.read_bytes())
        check('extra_n2_edit', False)
        np.write_bytes(n2 + p.N2_OPTIMIZATION_GUARD)
        actual[nkey] = sha(np.read_bytes())
        check('doubled_guard', False)
        np.write_bytes(n2)
        actual[nkey] = sha(n2)
        dp.write_bytes(d3.replace(b'assert margin > 0', b'assert margin >= 0'))
        actual[dkey] = sha(dp.read_bytes())
        check('changed_d3_mathematical_predicate', False)
        dp.write_bytes(d3 + p.D3_COMPAT_IMPORT)
        actual[dkey] = sha(dp.read_bytes())
        check('doubled_adapter_import', False)
        dp.write_bytes(d3)
        actual[dkey] = sha(d3)
        check('restored_historical_case', True)
    return {'accepted': True, 'input_head': INPUT, 'identities': identities,
            'helper_sha256': sha(Path(p.__file__).read_bytes()), 'cases': cases,
            'scope': 'Exact byte reversals and metadata controls only; no mathematical predicates changed.'}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
