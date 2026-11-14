"""P8 independent census. Usage: python3 -I census.py <newpkg> <oldpkg> <repo>"""
import gzip, hashlib, json, subprocess, sys, os, stat
from fractions import Fraction
from pathlib import Path

pkg, old, repo = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
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
def git(rev, path):
    r = subprocess.run(['git', '-C', str(repo), 'show', f'{rev}:{path}'], capture_output=True)
    return r.stdout if r.returncode == 0 else None

files = {p.relative_to(pkg).as_posix(): p for p in pkg.rglob('*') if p.is_file()}
ofiles = {p.relative_to(old).as_posix(): p for p in old.rglob('*') if p.is_file()}
ok(not [p for p in pkg.rglob('*') if p.is_symlink()], 'symlinks present')
tot = sum(p.stat().st_size for p in files.values())
print('files', len(files), 'bytes', tot)
ok(len(files) == 1019, 'file count'); ok(tot == 10229741, 'expanded bytes')
ok(set(files) == set(ofiles), 'same name set as old package')
changed = sorted(k for k in files if files[k].read_bytes() != ofiles[k].read_bytes())
print('changed members', changed)
ok(changed == sorted(['MANIFEST.json', 'SHA256SUMS', 'README.md', 'README.txt', 'verify.py', 'analytic/tables/paper.tex', 'analytic/tables/companion.tex', 'papers/paper.pdf', 'papers/companion.pdf']), 'changed set')
print('unchanged byte-identical', len(files) - len(changed))
raw = (pkg / 'SHA256SUMS').read_bytes()
ok(raw.endswith(b'\n') and b'\r' not in raw, 'SHA256SUMS format')
lines = raw.decode().splitlines(); names = []
for ln in lines:
    sha, name = ln[:64], ln[66:]
    ok(ln[64:66] == '  ' and len(sha) == 64 and all(c in '0123456789abcdef' for c in sha), 'sumline ' + ln)
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
om = strict((old / 'MANIFEST.json').read_bytes())
ok(m['phase_inputs'] == om['phase_inputs'], 'phase_inputs manifest unchanged vs old')
ok(m['polynomial_inputs'] == om['polynomial_inputs'], 'polynomial_inputs manifest unchanged vs old')
print('top-level manifest keys changed vs old:', sorted(k for k in set(m) | set(om) if m.get(k) != om.get(k)))
opay = {r['path']: r for r in om['payload']}
print('payload rows changed vs old:', sorted(k for k in pay if pay[k] != opay.get(k)))
exp = {(n, s) for n in range(41, 512) for s in ('produce', 'verify')}
ph = m['phase_inputs']
ok(len(ph) == 942 and {(r['n'], r['pass']) for r in ph} == exp, 'phase manifest scope')
ok({k for k in files if k.startswith('phase/inputs/')} == {f'phase/inputs/n{n:04d}-{s}.json' for n, s in exp}, 'phase file names')
ok({r['path'] for r in ph} == {f'phase/inputs/n{n:04d}-{s}.json' for n, s in exp}, 'phase manifest paths')
data = {}
for r in ph:
    b = files[r['path']].read_bytes()
    ok(r['bytes'] == len(b) and r['sha256'] == H(b) and pay[r['path']]['sha256'] == r['sha256'], 'phase id ' + r['path'])
    d = strict(b); ok(type(d['n']) is int and d['n'] == r['n'], 'phase n ' + r['path'])
    data[r['n'], r['pass']] = d
er = [strict(s) for s in (pkg / 'phase/expected-results.jsonl').read_bytes().decode().splitlines()]
ok(len(er) == 942 and {(r['n'], r['pass']) for r in er} == exp, 'expected rows scope')
rm = {(r['n'], r['pass']): r for r in er}
for n in range(41, 512):
    a, v = rm[n, 'produce'], rm[n, 'verify']
    ok(a['accepted'] is True and v['accepted'] is True, f'accepted {n}')
    ok({k: x for k, x in a.items() if k != 'pass'} == {k: x for k, x in v.items() if k != 'pass'}, f'exp pair {n}')
s = strict((pkg / 'phase/expected-summary.json').read_bytes())
ok(s['certificates'] == 942 and s['degrees'] == 471, 'summary counts')
ok(sum(r['S_keys'] for r in er) == s['S_checks'], 'S_checks')
ok(sum(r['lambda_keys'] for r in er) == s['actual_lambda_checks'], 'lambda checks')
for key in ('near_min', 'far_min', 'corner_gap', 'floor_min', 'M'):
    vals = {r['n']: Fraction(r[key]) for r in er if r[key] != 'None'}
    mn = min(vals.values())
    ok(Fraction(s['minima'][key]['exact']) == mn and s['minima'][key]['degrees'] == sorted(n for n, v in vals.items() if v == mn), 'minimum ' + key)
po = m['polynomial_inputs']
ok(len(po) == 39 and {r['n'] for r in po} == set(range(2, 41)), 'poly scope')
ok({k for k in files if k.startswith('polynomial/inputs/')} == {f'polynomial/inputs/n{n:04d}.json.gz' for n in range(2, 41)}, 'poly names')
for r in po:
    b = files[r['path']].read_bytes(); ok(H(b) == r['sha256'] and len(b) == r['bytes'], 'poly id')
    ok(git('HEAD', r['source']['path']) == b, 'poly git identity ' + r['source']['path'])
    d = strict(gzip.decompress(b)); ok(d.get('n') == r['n'], 'poly n')
# stored polynomial records vs manifest (my own reading)
recs = {}
for name in ('degrees-2-16.json', 'degrees-17-32.json'):
    for row in strict(files['polynomial/receipts/' + name].read_bytes())['accepted_rows']:
        recs[row['n']] = row
for n in range(33, 41): recs[n] = strict(files[f'polynomial/receipts/n{n:04d}.json'].read_bytes())
ok(set(recs) == set(range(2, 41)), 'receipt scope')
for r in po: ok(recs[r['n']]['certificate_sha256'] == r['sha256'], 'receipt cert sha %d' % r['n'])
print('receipt keys 2-16', sorted(recs[2])); print('receipt keys 17-32', sorted(recs[17])); print('receipt keys 33', sorted(recs[33]))
# git identity for mapped non-transformed sources at HEAD
same = []
for k, r in pay.items():
    src = r['source']
    if 'path' in src and not src['path'].startswith('/') and 'transformation' not in src and not k.startswith('polynomial/inputs/'):
        g = git('HEAD', src['path']); ok(g == files[k].read_bytes(), 'git HEAD identity ' + k); same.append(k)
print('mapped sources byte-identical to HEAD:', len(same))
for k in ('analytic/tables/paper.tex', 'analytic/tables/companion.tex'):
    ok(git('5f435be21f29f6fbf48e6d8cba15346117d7e151', pay[k]['source']['path']) == files[k].read_bytes(), 'table at freeze ' + k)
ok(git('dce3260b88c11a964168a64c34b168ac37f2a11c', pay['verify.py']['source']['path']) == files['verify.py'].read_bytes(), 'verify at dce3260')
ok(files['README.md'].read_bytes() == files['README.txt'].read_bytes(), 'README pair')
for k in ('papers/paper.pdf', 'papers/companion.pdf'):
    b = files[k].read_bytes(); src = pay[k]['source']
    ok(H(b) == src['sha256'] and len(b) == src['bytes'], 'pdf source identity ' + k)
    print(k, H(b), len(b), src.get('source_freeze'))
print('RESULT', 'PASS' if not fails else 'FAIL %d' % len(fails))
