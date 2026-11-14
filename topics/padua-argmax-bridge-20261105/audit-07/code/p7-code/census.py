"""P7 independent census of the public package. Usage: python3 -I census.py <pkgdir> <repo>"""
import gzip, hashlib, json, subprocess, sys
from fractions import Fraction
from pathlib import Path

pkg = Path(sys.argv[1]); repo = Path(sys.argv[2])
fails = []
def ok(c, m):
    if not c: fails.append(m); print('FAIL', m)
def H(b): return hashlib.sha256(b).hexdigest()
def strict(b):
    def hook(items):
        d = {}
        for k, v in items:
            if k in d: raise ValueError('dup ' + k)
            d[k] = v
        return d
    def bad(c): raise ValueError('nonfinite ' + c)
    return json.loads(b, object_pairs_hook=hook, parse_constant=bad)
def git(path):
    r = subprocess.run(['git', '-C', str(repo), 'show', 'HEAD:' + path], capture_output=True)
    return r.stdout if r.returncode == 0 else None

files = {p.relative_to(pkg).as_posix(): p for p in pkg.rglob('*') if p.is_file()}
ok(not [p for p in pkg.rglob('*') if p.is_symlink()], 'symlinks present')
print('files', len(files), 'bytes', sum(p.stat().st_size for p in files.values()))
ok(len(files) == 1019, 'file count')
ok(sum(p.stat().st_size for p in files.values()) == 10213669, 'expanded bytes')
raw = (pkg / 'SHA256SUMS').read_bytes()
ok(raw.endswith(b'\n') and b'\r' not in raw, 'SHA256SUMS format')
lines = raw.decode().splitlines(); names = []
for ln in lines:
    sha, name = ln[:64], ln[66:]
    ok(ln[64:66] == '  ' and len(sha) == 64, 'sumline ' + ln)
    names.append(name)
    ok(name in files and H(files[name].read_bytes()) == sha, 'sum ' + name)
ok(len(names) == len(set(names)) == 1018 and set(names) == set(files) - {'SHA256SUMS'}, 'sum coverage')
ok(names == sorted(names), 'sum order')
print('SHA256SUMS lines', len(lines))
m = strict((pkg / 'MANIFEST.json').read_bytes())
pay = {r['path']: r for r in m['payload']}
ok(len(pay) == len(m['payload']) == 1017 and set(pay) == set(files) - {'SHA256SUMS', 'MANIFEST.json'}, 'payload coverage')
for k, r in pay.items():
    b = files[k].read_bytes(); ok(r['bytes'] == len(b) and r['sha256'] == H(b), 'payload ' + k)
ok(H((pkg / 'verify.py').read_bytes()) == m['public_adapter_sha256'], 'adapter sha in manifest')
# phase
exp = {(n, s) for n in range(41, 512) for s in ('produce', 'verify')}
ph = m['phase_inputs']
ok(len(ph) == 942 and {(r['n'], r['pass']) for r in ph} == exp, 'phase manifest scope')
inputs = {k for k in files if k.startswith('phase/inputs/')}
ok(inputs == {f'phase/inputs/n{n:04d}-{s}.json' for n, s in exp}, 'phase file names')
data = {}
for r in ph:
    b = files[r['path']].read_bytes()
    ok(r['bytes'] == len(b) and r['sha256'] == H(b) and pay[r['path']]['sha256'] == r['sha256'], 'phase id ' + r['path'])
    d = strict(b); ok(type(d['n']) is int and d['n'] == r['n'], 'phase n ' + r['path'])
    data[r['n'], r['pass']] = d
diffkeys = set()
for n in range(41, 512):
    a, v = data[n, 'produce'], data[n, 'verify']
    ok(set(a) == set(v), f'keyset {n}')
    diffkeys |= {k for k in a if a[k] != v[k]}
print('keys differing produce/verify across all degrees:', sorted(diffkeys))
# expected rows
er = [strict(s) for s in (pkg / 'phase/expected-results.jsonl').read_bytes().decode().splitlines()]
ok(len(er) == 942 and {(r['n'], r['pass']) for r in er} == exp, 'expected rows scope')
rm = {(r['n'], r['pass']): r for r in er}
for n in range(41, 512):
    a, v = rm[n, 'produce'], rm[n, 'verify']
    ok(a['accepted'] is True and v['accepted'] is True, f'accepted {n}')
    ok({k: x for k, x in a.items() if k != 'pass'} == {k: x for k, x in v.items() if k != 'pass'}, f'exp pair {n}')
    ok('CPU_seconds' not in a, 'cpu present')
print('expected row keys', sorted(er[0]))
# recompute summary
s = strict((pkg / 'phase/expected-summary.json').read_bytes())
ok(s['certificates'] == 942 and s['degrees'] == 471, 'summary counts')
ok(sum(r['S_keys'] for r in er) == s['S_checks'], 'S_checks %d' % sum(r['S_keys'] for r in er))
ok(sum(r['S_keys'] for r in er if r['pass'] == 'produce') == s['distinct_S_keys'], 'distinct S')
ok(sum(r['lambda_keys'] for r in er) == s['actual_lambda_checks'], 'lambda checks')
ok(sum(r['lambda_keys'] for r in er if r['pass'] == 'produce') == s['distinct_actual_lambda_keys'], 'distinct lambda')
ok(sum(r['native_S_upper_contained'] for r in er) == s['native_S_uppers_contained'], 'native S contained')
ok(sum(r['native_S_upper_total'] for r in er) == s['native_S_uppers_total'], 'native S total')
ok(sum(r['native_lower_contained'] is True for r in er) == s['native_lowers_contained'], 'native lowers')
ok(str(max(int(r['M']) for r in er)) == s['M_max'], 'M_max')
for key in ('near_min', 'far_min', 'corner_gap', 'floor_min', 'M'):
    vals = {r['n']: Fraction(r[key]) for r in er if r[key] != 'None'}
    mn = min(vals.values())
    ok(Fraction(s['minima'][key]['exact']) == mn and s['minima'][key]['degrees'] == sorted(n for n, v in vals.items() if v == mn), 'minimum ' + key)
ok(s['all_native_endpoints_validated'] is False, 'endpoint flag')
# polynomial
po = m['polynomial_inputs']
ok(len(po) == 39 and {r['n'] for r in po} == set(range(2, 41)), 'poly scope')
ok({k for k in files if k.startswith('polynomial/inputs/')} == {f'polynomial/inputs/n{n:04d}.json.gz' for n in range(2, 41)}, 'poly names')
for r in po:
    b = files[r['path']].read_bytes(); ok(H(b) == r['sha256'] and len(b) == r['bytes'], 'poly id')
    g = git(r['source']['path']); ok(g == b, 'poly git identity ' + r['source']['path'])
    d = strict(gzip.decompress(b)); ok(d.get('n') == r['n'], 'poly n %d (%r)' % (r['n'], d.get('n')))
# git identities of mapped sources
same = 0
for k, r in pay.items():
    src = r['source']
    if 'path' in src and not src['path'].startswith('/') and 'transformation' not in src and not k.startswith('polynomial/inputs/'):
        g = git(src['path']); ok(g is not None and g == files[k].read_bytes(), 'git identity ' + k); same += g == files[k].read_bytes()
print('mapped sources byte-identical to HEAD:', same)
ok(files['README.md'].read_bytes() == files['README.txt'].read_bytes(), 'README pair')
# compact transforms
for name, lo, hi, rk, ck in [('polynomial/receipts/degrees-2-16.json', 2, 16, 'rows', 'columns'), ('polynomial/receipts/degrees-17-32.json', 17, 32, 'final_rows', 'final_rows_columns')]:
    c = strict(files[name].read_bytes()); g = git(c['source']['path'])
    ok(H(g) == c['source']['sha256'], 'transform source sha ' + name)
    o = json.loads(g)
    rows = [{k: v for k, v in dict(zip(o[ck], row)).items() if k not in ('wall_seconds', 'child_cpu_seconds')} for row in o[rk] if lo <= row[0] <= hi]
    ok(rows == c['accepted_rows'], 'transform rows ' + name)
    print(name, 'columns', o[ck], 'n rows', len(rows), 'all accepted?', {r.get('accepted', r.get('status')) for r in rows})
# phase input provenance for regenerated set (git-tracked? no: local-output) -- report only
print('origins', {r['source'].get('origin') for r in ph})
print('RESULT', 'PASS' if not fails else 'FAIL %d' % len(fails))
